# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **100:2**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s100-regular-20260911/s100/100_2/micro.discovery.json` and modify nothing
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
  "ayah_ref": "100:2",
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
{"analysis_context":{"analysis_id":"s100-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"100:2","host_surah":100,"lane_context_refs":[],"ordered_context_refs":["100:0","100:1","100:3","100:4","100:5","100:6","100:7","100:8","100:9","100:10","100:11","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, ateş çıkarma eylemiyle bu işin araçlarını kapsar; içecek kabı, ok, soy kötülemesi veya sıvı alma anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001203/B001","candidate_links":[{"candidate_id":"cand_67b2dc4c2b81e967f501","lane":"micro"},{"candidate_id":"cand_1e2df9ee9cd8ac109fdd","lane":"micro"},{"candidate_id":"cand_51e6c67c379e15c425b7","lane":"micro"},{"candidate_id":"cand_e5e93d899d5d4dbce459","lane":"micro"},{"candidate_id":"cand_7274ee5a76dde7e9de19","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَدْح","morph_features":"STEM|POS:N|LEM:qadoH|ROOT:qdH|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:2:1","qac_word_ref":"100:2:2","surface_ar":"قَدْحًا"}],"gloss":"ateş çıkarmak ve ateş çakma araçları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir çakma aracını vurarak kıvılcım ve ateş çıkarma eylemidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ateş çıkarmada kullanılan metal parça, taş veya başka araç da bu anlam alanında adlandırılır."}}],"root_ar":"ق د ح","root_id":"root_001203","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Eylem ile ona bağlı araç adlarının birlikte temsil edilmesi gereken genel açıklamada kullanılır.","boundary_detail":"Dal, ateş çıkarma eylemiyle bu işin araçlarını kapsar; içecek kabı, ok, soy kötülemesi veya sıvı alma anlamlarını kapsamaz.","branch_image_ar":"إيراء النار بالقدح","concept_gloss":"ateş çıkarmak ve ateş çakma araçları","contextual_glosses":[{"applicability":"Bir taş ya da metal parçayı vurarak kıvılcım çıkarma eylemi anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Vurma yoluyla kıvılcım çıkarıp ateş yakma eylemini korur."},"facet_ids":["F001"],"text":"ateş çakmak","usage_role":"general"},{"applicability":"Taş, metal parça veya başka bir ateş çıkarma aracı adlandırılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ateş çıkarmak için kullanılan araç olma özelliğini korur."},"facet_ids":["F002"],"text":"ateş çakma aracı","usage_role":"explanatory"}],"definition":"Taş, metal veya benzeri bir aracı vurarak kıvılcım çıkarıp ateş yakma; ayrıca bu işte kullanılan metal parça, taş ve araçların adlarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir çakma aracını vurarak kıvılcım ve ateş çıkarma eylemidir."},{"facet_id":"F002","role":"associated_use","statement":"Ateş çıkarmada kullanılan metal parça, taş veya başka araç da bu anlam alanında adlandırılır."}],"identity_rationale":"Kaynak ifadesi, vurma yoluyla ateş çıkarma eylemini ve bu eylemde kullanılan metal parça, taş ve aracı aynı anlam alanında toplar. Geçici dal çerçevesi bu eylem-araç bağını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ateş çakmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"çakma aracını vurarak ateş çıkarmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"ateş çakmaya yarayan metal parça"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"ateş çıkarmaya yarayan çakmak taşı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"çakmak taşı veya ateş çıkarma aracı"}],"lexicalization_note":"Tanım, ateş ve ateş çıkarma aracıyla kurulan kullanımları araç adlarından ayırır; bu yapıya bağlı anlamları yalın bir genel vurma anlamına genişletmez.","neighbor_coverage_note":"Bütün aday kartlar değerlendirildi; ateşin çıkmasıyla olan yakınlık ve ateş vermeyen araçla kurulan karşıtlık dal sınırını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal vurma eylemini ve onun somut araçlarını öne çıkarır; komşu dal ise ateşin çıkması, yanması ve yeniden tutuşturulması sonucuna daha geniş yer verir.","focus_only":"Kıvılcım üretmek için vurma eylemini ve kullanılan taş ile metal parçaları adlandırır.","gloss":"ateş çakmak ile ateşin tutuşması","neighbor_only":"Ateşin araçtan çıkmasını ve sönük ateşin yeniden tutuşturulmasını da kapsar.","neighbor_ref":"root_001642/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir ateş çıkarma aracından ateş elde etme alanında buluşur."},{"boundary_match":"opposed","distinction":"Karşıtlık, çakma girişiminin ateş üretip üretmemesidir: odak dal başarılı çıkarma eylemi ile araçlarını, komşu dal ise ateş vermeyen parçayı anlatır.","focus_only":"Başarılı biçimde kıvılcım çıkaran eylem ve araçları kapsar.","gloss":"ateş çıkaran ve çıkarmayan çakma aracı","neighbor_only":"Kullanıldığı halde ateş çıkarmayan çakma parçasını adlandırır.","neighbor_ref":"root_000451/B002","relation_type":"polarity_pair","shared_zone":"İki dal da ateş çıkarma amacıyla vurulan bir aracın işleyişini değerlendirir."}],"source_phrase_ar":"قدحت النار (maqayis;sihah)؛ قدحت النار أقدحها قدحا من الزند وغيره (jamhara)؛ المقدح الحديدة التي يقدح بها والقداح الحجر الذي تورى منه النار (ayn)؛ المقدحة ما تقدح به النار والقداحة والقداح الحجر الذي يوري النار (sihah)","source_summary":"Kaynaklar, ateşin vurma yoluyla çıkarılmasında ve bu iş için kullanılan taş ile metal araçların adlandırılmasında birleşir.","sources":["MQ","AY","JA","SI"],"what_is_ar":"قدح النار والزند والحجر والحديدة التي تورى بها النار","what_is_not_ar":"قدح الشرب؛ قدح السهم؛ الطعن في النسب؛ غرف القدر"},"support_links":["sup_0038997092c3d7f5c042","sup_20bb3eac7d4e1c042e07","sup_7fa24b15fa1a9eac840c","sup_8e704e9307a40d0a511d","sup_b1f045d586d5376cba7b"]},{"boundary":"Dal, nesnede fiziksel bir iz veya kusur oluşturma ve bunun sonucunu kapsar; çürüme, ateş çıkarma ve sözlü kötüleme anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001203/B002","candidate_links":[{"candidate_id":"cand_d72e6b293b6e7b9e90e3","lane":"micro"},{"candidate_id":"cand_20ed608e7980f8340c47","lane":"micro"},{"candidate_id":"cand_d0e9f665449e155785f1","lane":"micro"},{"candidate_id":"cand_6b8a123830fdac961a35","lane":"micro"},{"candidate_id":"cand_7652d264cda10c10e551","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَدْح","morph_features":"STEM|POS:N|LEM:qadoH|ROOT:qdH|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:2:1","qac_word_ref":"100:2:2","surface_ar":"قَدْحًا"}],"gloss":"çentik açmak ve oluşan kusur","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesneyi çenterek, ezerek veya metal araçla oyarak üzerinde fiziksel bir iz oluşturmadır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ağaçta ya da kemikte oluşan kusur izi ve ağaçtaki çatlak, eylemin sonucu olarak adlandırılır."}}],"root_ar":"ق د ح","root_id":"root_001203","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel iz oluşturma eylemiyle ağaç veya kemikteki sonucunun birlikte anlatılması gereken yerde kullanılır.","boundary_detail":"Dal, nesnede fiziksel bir iz veya kusur oluşturma ve bunun sonucunu kapsar; çürüme, ateş çıkarma ve sözlü kötüleme anlamlarını kapsamaz.","branch_image_ar":"نقر الشيء وعيبه","concept_gloss":"çentik açmak ve oluşan kusur","contextual_glosses":[{"applicability":"Kemikte metal bir araçla oyuk ya da delik açma bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başka nesnelerdeki çentik ve ezik oluşturma kapsamını dışarıda bırakır.","preserves":"Metal araçla fiziksel bir oyuk oluşturma eylemini korur."},"facet_ids":["F001"],"text":"kemiği metal aletle oymak","usage_role":"contextual"},{"applicability":"Eylemden bağımsız olarak ağaçta görülen sonuç adlandırılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ağaçta ortaya çıkan çatlak ve kusur izi sonucunu korur."},"facet_ids":["F002"],"text":"ağaçtaki çatlak veya kusur izi","usage_role":"explanatory"}],"definition":"Bir nesnede, özellikle kemik ya da ağaçta, metal bir araçla çentik, ezik veya oyuk oluşturma; ortaya çıkan kusur izi ya da çatlak da bu adla anılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesneyi çenterek, ezerek veya metal araçla oyarak üzerinde fiziksel bir iz oluşturmadır."},{"facet_id":"F002","role":"extension","statement":"Ağaçta ya da kemikte oluşan kusur izi ve ağaçtaki çatlak, eylemin sonucu olarak adlandırılır."}],"identity_rationale":"Kaynak ifadesi bir nesnede ezik ya da çentik oluşturmayı, kemiği metal araçla oymayı ve ağaç ile kemikte ortaya çıkan iz, kusur veya çatlağı birlikte verir. Geçici çerçeve eylem ile sonucunu doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bir nesnede çentik veya ezik oluşturmak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"içindeki bozukluğu çıkarmak için kemiği metal aletle oymak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"ağaç ve kemiklerdeki kusur izleri"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ağaçtaki çatlak"}],"lexicalization_note":"Tanım, nesne ve kemikle kurulan eylem kullanımlarını ağaç ile kemikteki sonuç adlarından ayırır; bu özel kapsamı her türlü zarar verme anlamına genişletmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yüzey bütünlüğünün bozulmasını paylaşan yarık ve yırtık dalı, çentik ile çatlağın sınırını en yararlı biçimde belirledi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal vurma veya oyma sonucu oluşan çentik ile kusura dayanır; komşu dal ise yüzeyin açılmasıyla oluşan yarık ve yırtığı temel alır.","focus_only":"Vurma ya da oyma yoluyla nesnede çentik, ezik ve kusur izi oluşturmayı kapsar.","gloss":"çentik ve kusur ile yarık ve yırtık","neighbor_only":"Deri, giysi ve su kabı gibi yüzeylerdeki yarık, delik ve onarılamayan küçük yırtığı kapsar.","neighbor_ref":"root_001688/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da katı bir yüzeyin bütünlüğünün bozulması ve görünür bir kusur oluşması alanındadır."}],"source_phrase_ar":"يدل أحدهما على شيء كالهزم في الشيء (maqayis)؛ القدح فعلك إذا قدحت الشيء (maqayis)؛ قدحت العظم إذا نقرته بحديدة (jamhara)؛ القوادح الوصوم في العيدان والعظام (jamhara)؛ القادح الصدع في العود (sihah)","source_summary":"Kaynaklar, nesnede fiziksel bir iz oluşturma eylemiyle ağaç ve kemikte kalan kusur ya da çatlak sonucunu aynı dalda toplar.","sources":["MQ","JA","SI"],"what_is_ar":"قدح الشيء ونقر العظم وإحداث صدع أو وصمة في العود والعظم","what_is_not_ar":"قدح النار؛ القادحة التي تأكل الشجر والسن؛ الطعن في النسب؛ غرف القدر"},"support_links":["sup_4663a1f9d53122baeb95","sup_820492beff1443fb51f3","sup_8cca43a23df303bfbf15","sup_a67ea33db9bc803b54e2","sup_abd45b352cfcac0a5a52"]},{"boundary":"Dal yalnızca bir kişinin soyuna yöneltilen sözlü kötülemeyi kapsar; genel hakaret, fiziksel kusur verme veya soyla övünme anlamlarını kapsamaz.","branch_kind":"collocation","branch_ref":"root_001203/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَدْح","morph_features":"STEM|POS:N|LEM:qadoH|ROOT:qdH|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:2:1","qac_word_ref":"100:2:2","surface_ar":"قَدْحًا"}],"gloss":"birinin soyuna dil uzatmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözlü saldırı, kişinin davranışına değil doğrudan soyuna ve kökenine yönelir."}}],"root_ar":"ق د ح","root_id":"root_001203","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin kökenini veya soyunun doğruluğunu sözle kötüleme bağlamında kullanılır.","boundary_detail":"Dal yalnızca bir kişinin soyuna yöneltilen sözlü kötülemeyi kapsar; genel hakaret, fiziksel kusur verme veya soyla övünme anlamlarını kapsamaz.","branch_image_ar":"طعن في النسب","concept_gloss":"birinin soyuna dil uzatmak","contextual_glosses":[{"applicability":"Eylemin daha düz ve açıklayıcı bir anlatımla verilmesi gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kötülemenin kişinin soyunu hedef alması koşulunu korur."},"facet_ids":["F001"],"text":"soyunu kötülemek","usage_role":"contextual"}],"definition":"Bir kişinin soyunu veya soyunun doğruluğunu sözle hedef alıp kötülemek ve kuşkulu göstermektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözlü saldırı, kişinin davranışına değil doğrudan soyuna ve kökenine yönelir."}],"identity_rationale":"Kaynak ifadesi, bir kişinin soyunu sözle hedef alıp kötüleme eylemini açık ve tutarlı biçimde verir. Geçici dal çerçevesi bu yapıya bağlı anlamı doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"birinin soyuna dil uzatmak"}],"lexicalization_note":"Tanım yalnızca soy bildiren tamamlayıcıyla kurulan sözlü kötüleme yapısına bağlıdır; yalın biçime genel bir eleştirme anlamı yüklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel sözlü saldırı dalı, bu dalın yalnızca soya yönelen dar yapısını en açık karşılaştırmayla gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın zorunlu konusu kişinin soyudur; komşu dal ise konusu sınırlanmamış hakaret ve suçlama eylemlerini daha geniş biçimde kapsar.","focus_only":"Sözlü saldırının yalnızca kişinin soyuna ve kökenine yönelmesini gerektirir.","gloss":"soya dil uzatmak ile genel sözlü saldırı","neighbor_only":"Soy dışındaki konularda hakaret, suçlama ve kötüleme eylemlerini de kapsar.","neighbor_ref":"root_000603/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişiyi sözle değersizleştirme ve ona karşı olumsuz bir iddia yöneltme alanındadır."}],"source_phrase_ar":"قدح في نسبه طعن (maqayis)؛ قدحت في نسب الرجل إذا طعنت فيه (jamhara)؛ قدحت في نسبه إذا طعنت (sihah)","source_summary":"Kaynaklar, yapıyı bir kişinin soyuna yöneltilen sözlü saldırı ve kötüleme olarak ortak biçimde açıklar.","sources":["MQ","JA","SI"],"what_is_ar":"القدح في نسب الرجل بالطعن فيه","what_is_not_ar":"النقر في العظم؛ تأكل الشجر والسن؛ قدح النار؛ قدح السهم والإناء"},"support_links":[]},{"boundary":"Dal ağaç ve dişteki kemirilme kaynaklı bozulmayı, etken kurtçuğu ve diş lekesini kapsar; genel çatlak, deri soyulması veya göz rahatsızlığını kapsamaz.","branch_kind":"bare","branch_ref":"root_001203/B004","candidate_links":[{"candidate_id":"cand_b6fd7a931cd92299499c","lane":"micro"},{"candidate_id":"cand_a049af0ff9c8dcc76947","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَدْح","morph_features":"STEM|POS:N|LEM:qadoH|ROOT:qdH|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:2:1","qac_word_ref":"100:2:2","surface_ar":"قَدْحًا"}],"gloss":"ağaç ve dişte kemirilme ya da çürüme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ağaç dokusunda veya dişte kemirilme ve çürüme biçiminde bir bozulma ortaya çıkar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ağacı ve dişi yiyerek bu bozulmaya yol açan kurtçuk ayrıca adlandırılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dişte bozulmanın belirtisi olarak görülen kara leke veya kusur izi ayrıca adlandırılır."}}],"root_ar":"ق د ح","root_id":"root_001203","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın ağaç ile dişte ortak olan bozulma çekirdeği anlatılırken kullanılır.","boundary_detail":"Dal ağaç ve dişteki kemirilme kaynaklı bozulmayı, etken kurtçuğu ve diş lekesini kapsar; genel çatlak, deri soyulması veya göz rahatsızlığını kapsamaz.","branch_image_ar":"أكال الشجر والسن","concept_gloss":"ağaç ve dişte kemirilme ya da çürüme","contextual_glosses":[{"applicability":"Bozulmaya yol açan canlı etken doğrudan adlandırılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ağaç veya dişi yiyen kurtçuk olma özelliğini korur."},"facet_ids":["F002"],"text":"ağacı veya dişi yiyen kurtçuk","usage_role":"explanatory"},{"applicability":"Dişte görülen kara iz ya da çürük belirtisi anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dişte görülen kara bozulma izini ve çürük belirtisini korur."},"facet_ids":["F003"],"text":"dişteki kara çürük lekesi","usage_role":"contextual"}],"definition":"Ağaçta ya da dişte kemirilme ve çürüme biçiminde beliren bozulma; bunu yapan kurtçuk ve dişte görünen kara leke de aynı alanın adlandırmalarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ağaç dokusunda veya dişte kemirilme ve çürüme biçiminde bir bozulma ortaya çıkar."},{"facet_id":"F002","role":"specialization","statement":"Ağacı ve dişi yiyerek bu bozulmaya yol açan kurtçuk ayrıca adlandırılır."},{"facet_id":"F003","role":"specialization","statement":"Dişte bozulmanın belirtisi olarak görülen kara leke veya kusur izi ayrıca adlandırılır."}],"identity_rationale":"Kaynak ifadesi ağaçta ve dişte görülen kemirilme ya da çürümeyi, buna yol açan kurtçuğu ve dişte beliren kara izi aynı bozulma alanında toplar. Geçici çerçeve bu alt görünümleri doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ağaçta veya dişte oluşan kemirilme ve çürük"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ağacı ve dişi yiyen kurtçuk"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"dişte beliren kara leke"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"dişlerdeki kusur ve kara lekeler"}],"lexicalization_note":"Tanım, yalın dalın ağaç ve dişteki bozulma alanını esas alır; başka dallardaki yapı bağımlı oyma veya kusur anlamlarını içeri taşımaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnız diş bozulmasına ayrılan komşu dal, bu dalın ağaç, kurtçuk ve kara leke uzantılarını en iyi sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dişten ağaca uzanır ve kurtçuğu da içerir; komşu dal yalnız dişteki çürüme ile yüzey ve dip birikintilerine bağlıdır.","focus_only":"Ağaçtaki bozulmayı, bunu yapan kurtçuğu ve dişteki kara lekeyi de kapsar.","gloss":"ağaç ve diş çürüğü ile yalnız diş çürüğü","neighbor_only":"Yalnız dişlerdeki aşınma, çürüme ve diş diplerine yapışan birikintileri kapsar.","neighbor_ref":"root_000341/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da diş dokusundaki çürüme ve bozulmayı adlandırır."}],"source_phrase_ar":"القدح تأكل يقع في الشجر والأسنان (maqayis)؛ القادحة الدودة تأكل الشجرة (maqayis)؛ القدح أكال يقع في الشجر وفي الأسنان (ayn)؛ القادحة الدودة التي تأكل الشجرة والسن (ayn)؛ قدح العود إذا وقع فيه الأكال وكذلك السن (jamhara)؛ القادح في الأسنان سواد يظهر فيها (jamhara)؛ قدح الدود في الأسنان والشجر (sihah)","source_summary":"Kaynaklar, ağaç ve dişteki kemirilme kaynaklı bozulmayı ortak çekirdek olarak verir; kurtçuk ile dişteki kara görünüm bu çekirdeğin özel adlandırmalarıdır.","sources":["MQ","AY","JA","SI"],"what_is_ar":"الأكال أو الدودة أو السواد الذي يقع في الشجر والأسنان","what_is_not_ar":"الطعن في النسب؛ نقر العظم بالحديدة؛ غؤور العين؛ غرف القدر"},"support_links":["sup_666c11b53573bb907d5a","sup_fb18fefa7d46de4bde6c"]},{"boundary":"Çekirdek sıvıyı elle veya araçla alıp çıkarmadır; dip kalıntısı, kepçe, bir alışlık miktar ve kuyu bu çekirdeğe bağlı ayrı kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001203/B005","candidate_links":[{"candidate_id":"cand_ae9d5aa08d3fee718fe0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَدْح","morph_features":"STEM|POS:N|LEM:qadoH|ROOT:qdH|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:2:1","qac_word_ref":"100:2:2","surface_ar":"قَدْحًا"}],"gloss":"sıvıyı elle ya da kepçeyle alma; bunun aracı, miktarı, kalıntısı ve kuyusu","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tencere, çorba veya benzeri bir kaynaktaki sıvı elle ya da kepçeyle alınıp çıkarılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tencerenin dibinde kalan ve ancak güçlükle alınabilen yemek veya çorba kalıntısı ayrıca adlandırılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Alma işinde kullanılan kepçe ve tek seferde alınan bir kepçelik miktar adlaşmıştır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Suyu araçsız olarak elle alınan kuyu, alma biçimine göre nitelenir."}}],"root_ar":"ق د ح","root_id":"root_001203","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın eylem merkezini ve buna bağlı bütün adlaşmış kullanımlarını birlikte gösteren açıklamada kullanılır.","boundary_detail":"Çekirdek sıvıyı elle veya araçla alıp çıkarmadır; dip kalıntısı, kepçe, bir alışlık miktar ve kuyu bu çekirdeğe bağlı ayrı kullanımlardır.","branch_image_ar":"غرف ما في القدر","concept_gloss":"sıvıyı elle ya da kepçeyle alma; bunun aracı, miktarı, kalıntısı ve kuyusu","contextual_glosses":[{"applicability":"Tencere veya başka bir kaptaki çorbanın kepçeyle çıkarılması anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Elle alma ve çorba dışındaki sıvıları alma kapsamını dışarıda bırakır.","preserves":"Sıvıyı bir araçla alıp kaptan çıkarma eylemini korur."},"facet_ids":["F001"],"text":"çorbayı kepçeyle almak","usage_role":"contextual"},{"applicability":"Tencerenin dibinde kalan az miktardaki yemeğin güçlükle çıkarılması anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dipte kalan kalıntıyı güçlükle alma koşulunu korur."},"facet_ids":["F002"],"text":"tencere dibindeki kalıntıyı güçlükle almak","usage_role":"explanatory"},{"applicability":"Alma aracı ile tek alışta çıkarılan miktarın birlikte açıklanması gereken yerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hem aracı hem de tek seferde alınan miktarı korur."},"facet_ids":["F003"],"text":"kepçe veya bir kepçelik miktar","usage_role":"explanatory"},{"applicability":"Suyu bir araç yerine doğrudan elle alınan kuyu anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kuyudan suyun doğrudan elle alınması özelliğini korur."},"facet_ids":["F004"],"text":"elle su çekilen kuyu","usage_role":"contextual"}],"definition":"Bir kaptaki ya da kuyudaki sıvıyı elle veya kepçeyle alıp çıkarma; ayrıca tencere dibinde güçlükle alınan kalıntıyı, kepçeyi, bir alışlık miktarı ve elle su alınan kuyuyu adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tencere, çorba veya benzeri bir kaynaktaki sıvı elle ya da kepçeyle alınıp çıkarılır."},{"facet_id":"F002","role":"specialization","statement":"Tencerenin dibinde kalan ve ancak güçlükle alınabilen yemek veya çorba kalıntısı ayrıca adlandırılır."},{"facet_id":"F003","role":"extension","statement":"Alma işinde kullanılan kepçe ve tek seferde alınan bir kepçelik miktar adlaşmıştır."},{"facet_id":"F004","role":"associated_use","statement":"Suyu araçsız olarak elle alınan kuyu, alma biçimine göre nitelenir."}],"identity_rationale":"Kaynak ifadesi tencere veya çorbadaki sıvıyı alma eylemini, dipte güçlükle alınan kalıntıyı, kepçeyi, bir alışlık miktarı ve elle su alınan kuyuyu ortak alma işlemi çevresinde toplar. Dal kullanılabilir, ancak eylem, sonuç, araç, miktar ve kuyu kullanımları tek bir eşdeğer gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"tencere dibinde kalan ve güçlükle alınan yemek artığı"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"tenceredekini kepçeyle almak"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"çorbayı kepçeyle almak"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"çorbayı kepçeyle almak"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"kepçe"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"bir kepçe çorba"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"elle su çekilen kuyu"}],"lexicalization_note":"Tanım, tencere ve çorbayla kurulan alma eylemlerini adlaşmış kalıntı, araç, miktar ve kuyu kullanımlarından ayırır; bunları yalın ve sınırsız bir alma anlamında birleştirmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel sıvı alma dalı, bu dalın tencere, kalıntı, kepçe ve kuyuya bağlı özel kapsamını en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli kap yapıları ile dip kalıntısı, araç ve kuyu adlarına bağlıdır; komşu dal ise sıvı almanın daha genel eylem ve miktar alanını temsil eder.","focus_only":"Tencere dibi kalıntısı, kepçe, bir kepçelik miktar ve elle su alınan kuyu gibi adlaşmış kullanımları içerir.","gloss":"özel sıvı alma kullanımları ile genel sıvı alma","neighbor_only":"Suyu veya çorbayı elle ya da kepçeyle kaldırmanın genel eylemini ve genel alış ölçüsünü kapsar.","neighbor_ref":"root_001079/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da sıvının el veya kepçe yardımıyla bulunduğu yerden alınıp çıkarılması eylemini paylaşır."}],"source_phrase_ar":"الأصل الآخر القديح ما يبقى في أسفل القدر فيغرف بجهد (maqayis)؛ قدحت القدر غرفت ما فيها (maqayis)؛ ركى قدوح تغرف باليد (maqayis;jamhara;sihah)؛ القديح ما يبقى في أسفل القدر فيعرف بجهد (ayn)؛ وقدحت ما في القدر إذا اغترفته (jamhara)؛ المقدحة المغرفة (jamhara)؛ وقدحت المرق غرفته (sihah)؛ القدحة الغرفة (sihah)","source_summary":"Kaynaklar sıvıyı alma eylemini ortak merkez yapar; dip kalıntısı, kepçe, bir alışlık miktar ve elle su alınan kuyu bu merkeze bağlı kullanımlardır.","sources":["MQ","AY","JA","SI"],"what_is_ar":"قدح القدر أو المرق والغرف بالمقدحة وما يبقى في أسفل القدر فيغرف بجهد والركي التي تغرف باليد","what_is_not_ar":"قدح الشرب نفسه؛ قدح السهم؛ قدح النار؛ الطعن في النسب"},"support_links":["sup_8491936c09669d92d8cf"]},{"boundary":"Dal içmekte kullanılan kabı ve onun yapımcısıyla yapım işini kapsar; kepçe, pişirme kabı, ok veya ateş çıkarma aracı anlamlarını kapsamaz.","branch_kind":"bare","branch_ref":"root_001203/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَدْح","morph_features":"STEM|POS:N|LEM:qadoH|ROOT:qdH|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:2:1","qac_word_ref":"100:2:2","surface_ar":"قَدْحًا"}],"gloss":"içecek kabı, yapımcısı ve yapım işi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Küçük veya büyük olabilen ve içmek için kullanılan bir kaptır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu tür içecek kaplarını yapan kişi ayrıca adlandırılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İçecek kabı yapma işi ve zanaatı ayrıca adlandırılır."}}],"root_ar":"ق د ح","root_id":"root_001203","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesne adının yanı sıra bu nesneyi yapan kişi ve zanaatın birlikte gösterilmesi gereken açıklamada kullanılır.","boundary_detail":"Dal içmekte kullanılan kabı ve onun yapımcısıyla yapım işini kapsar; kepçe, pişirme kabı, ok veya ateş çıkarma aracı anlamlarını kapsamaz.","branch_image_ar":"قدح الشرب","concept_gloss":"içecek kabı, yapımcısı ve yapım işi","contextual_glosses":[{"applicability":"Küçük veya büyük bir içme kabı doğrudan adlandırılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kabın içmek için kullanılma işlevini ve nesne niteliğini korur."},"facet_ids":["F001"],"text":"içecek tası","usage_role":"general"},{"applicability":"İçecek kaplarını yapan kişi adlandırılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İçecek kaplarını yapan kişi olma anlamını korur."},"facet_ids":["F002"],"text":"içecek kabı ustası","usage_role":"contextual"},{"applicability":"İçecek kabı üretme işi ve zanaatı adlandırılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İçecek kaplarını üretmeye dayalı zanaat anlamını korur."},"facet_ids":["F003"],"text":"içecek kabı yapımcılığı","usage_role":"contextual"}],"definition":"İçmekte kullanılan küçük ya da büyük kap; ayrıca bu kapları yapan kişi ile kap yapma zanaatının adıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Küçük veya büyük olabilen ve içmek için kullanılan bir kaptır."},{"facet_id":"F002","role":"extension","statement":"Bu tür içecek kaplarını yapan kişi ayrıca adlandırılır."},{"facet_id":"F003","role":"extension","statement":"İçecek kabı yapma işi ve zanaatı ayrıca adlandırılır."}],"identity_rationale":"Kaynak ifadesi küçük ya da büyük içecek kabını, bu kapları yapan kişiyi ve onun zanaatını birlikte verir. Geçici çerçeve nesne ile düzenli türevlerini doğru biçimde kapsar.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"içecek tası"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"içecek kabı yapan usta"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"içecek kabı yapımcılığı"}],"lexicalization_note":"Tanım, yalın dalın içecek kabı çekirdeğini ve ondan türeyen yapımcı ile zanaat adlarını korur; komşu kap türlerinin işlevlerini içeri taşımaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yem ve ölçü kabı dalı, ortak kap biçimine rağmen içme işlevinin belirleyici sınır olduğunu en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın belirleyici işlevi içmedir ve yapımcı türevleri vardır; komşu dalın kapları yem verme ya da ölçme işlevine bağlıdır.","focus_only":"Kabın içmekte kullanılmasını ve bu kabın yapımcısı ile yapım zanaatını kapsar.","gloss":"içecek kabı ile yem veya ölçü kabı","neighbor_only":"Yem koyma, ölçme veya genel kap işlevi taşıyan kap ve ölçek türlerini kapsar.","neighbor_ref":"root_000340/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da elde taşınabilen bir kap veya tas türünü adlandırır."}],"source_phrase_ar":"القدح من الآنية من هذا (maqayis)؛ القداح متخذ الأقداح وصنعته القداحة (ayn)؛ القدح معروف اسم يجمع صغار الأقداح وكبارها (jamhara)؛ القدح واحد الأقداح التي للشرب (sihah)","source_summary":"Kaynaklar içmekte kullanılan kabı ortak çekirdek olarak verir; kap yapımcısı ile yapım zanaatı bu nesne adından türeyen kullanımlardır.","sources":["MQ","AY","JA","SI"],"what_is_ar":"القدح من الآنية وأقداح الشرب وصانع الأقداح","what_is_not_ar":"قدح السهم؛ قدح الميسر؛ القدر التي يغرف منها؛ المقدحة المغرفة"},"support_links":[]},{"boundary":"Dalın yalın çekirdeği tamamlanmamış ok gövdesidir; talih oyunu parçası yalnız belirtilen yapıya bağlı özel kullanımdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001203/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَدْح","morph_features":"STEM|POS:N|LEM:qadoH|ROOT:qdH|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:2:1","qac_word_ref":"100:2:2","surface_ar":"قَدْحًا"}],"gloss":"uçsuz ve tüysüz ok gövdesi; talih oyunu oku","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ok, metal ucu ve denge tüyleri takılmadan önce yalnız gövde durumundadır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Talih oyununda kullanılan ok benzeri parçalardan biri, özel bir yapı içinde aynı adla anılır."}}],"root_ar":"ق د ح","root_id":"root_001203","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın ok gövdesi ile oyuna bağlı özel kullanımın birlikte gösterilmesi gereken genel açıklamada kullanılır.","boundary_detail":"Dalın yalın çekirdeği tamamlanmamış ok gövdesidir; talih oyunu parçası yalnız belirtilen yapıya bağlı özel kullanımdır.","branch_image_ar":"عود السهم والقدح في الميسر","concept_gloss":"uçsuz ve tüysüz ok gövdesi; talih oyunu oku","contextual_glosses":[{"applicability":"Ok yapımının, gövdenin henüz tamamlanmadığı aşaması anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Okun uç ve tüy eklenmemiş gövde aşamasını eksiksiz korur."},"facet_ids":["F001"],"text":"uç ve tüy takılmamış ok gövdesi","usage_role":"general"},{"applicability":"Özel bir talih oyunundaki ok benzeri parçalardan biri anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Parçanın talih oyununa bağlı ok olma işlevini korur."},"facet_ids":["F002"],"text":"talih oyununda kullanılan ok","usage_role":"contextual"}],"definition":"Henüz metal ucu ve denge tüyleri takılmamış ok gövdesi; ayrıca belirli bir talih oyununda kullanılan ok benzeri parçalardan biridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ok, metal ucu ve denge tüyleri takılmadan önce yalnız gövde durumundadır."},{"facet_id":"F002","role":"specialization","statement":"Talih oyununda kullanılan ok benzeri parçalardan biri, özel bir yapı içinde aynı adla anılır."}],"identity_rationale":"Kaynak ifadesi henüz ucu ve tüyleri takılmamış ok gövdesiyle talih oyununda kullanılan ok benzeri parçayı aynı dalda verir. Çerçeve kullanılabilir, ancak genel ok gövdesi ile oyuna bağlı özel parçanın kapsamları ayrı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"uç ve tüy takılmamış ok gövdesi"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"talih oyununda kullanılan oklardan biri"}],"lexicalization_note":"Tanım, yalın biçimdeki uçsuz ve tüysüz ok gövdesini talih oyunu yapısına bağlı özel kullanımdan ayırır; oyun anlamını bütün dala yaymaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; küçük oyun ve alıştırma oku, uçsuz gövde ortaklığını korurken amaç ve boyut sınırını en açık biçimde ortaya koydu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal boyut veya eğitim amacıyla sınırlı değildir ve talih oyunu kullanımına uzanır; komşu dal küçük boy ile oyun ya da eğitim amacını zorunlu kılar.","focus_only":"Genel olarak tamamlanmamış ok gövdesini ve talih oyununda kullanılan özel oku kapsar.","gloss":"tamamlanmamış ok gövdesi ile küçük alıştırma oku","neighbor_only":"Çocukların oynaması veya atış öğrenmesi için yapılan küçük okla sınırlıdır.","neighbor_ref":"root_001285/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da metal ucu ve tüyleri bulunmayan ok benzeri ince bir gövdeyi kapsar."}],"source_phrase_ar":"القدح وهو السهم بلا نصل ولا قذذ (maqayis)؛ القدح الواحد من قداح الميسر (maqayis)؛ القدح السهم قبل أن يراش وينصل (ayn)؛ القدح قدح السهم العود بلا نصل ولا قذذ (jamhara)؛ القدح الواحد من قداح الميسر (jamhara)؛ القدح بالكسر السهم قبل أن يراش ويركب نصله (sihah)؛ وقدح الميسر أيضا (sihah)","source_summary":"Kaynaklar uç ve tüy takılmamış ok gövdesinde birleşir ve talih oyununda kullanılan ok benzeri parçayı bunun yapı bağımlı özel kullanımı olarak verir.","sources":["MQ","AY","JA","SI"],"what_is_ar":"السهم قبل النصل والريش والقدح الواحد من قداح الميسر","what_is_not_ar":"قدح الشرب؛ قدح النار؛ قدح القدر؛ القادحة في السن والشجر"},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"collocation","branch_ref":"root_001203/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَدْح","morph_features":"STEM|POS:N|LEM:qadoH|ROOT:qdH|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:2:1","qac_word_ref":"100:2:2","surface_ar":"قَدْحًا"}],"gloss":"yalıtık adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir at, çubuk gibi ince görünecek ölçüde zayıflatılır veya bu incelikte nitelenir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir atın, devenin veya başka bir canlının gözü içeri çöker."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gözde bulunan bozuk sıvı bir işlemle dışarı çıkarılır."}}],"root_ar":"ق د ح","root_id":"root_001203","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"ضمر الفرس وغؤور العين","concept_gloss":"yalıtık adlandırmalar","contextual_glosses":[{"applicability":"Atın bedensel olarak çok ince duruma getirilmesi anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Atın çubuk benzeri inceliğe dek zayıflatılması sonucunu korur."},"facet_ids":["F001"],"text":"atı çubuk gibi ince olana dek zayıflatmak","usage_role":"explanatory"},{"applicability":"Bir canlının gözünün yuvasında içeri doğru çökmesi anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gözün içeri çökmesi biçimindeki durum değişikliğini korur."},"facet_ids":["F002"],"text":"gözü içeri çökmek","usage_role":"contextual"},{"applicability":"Gözde bulunan sağlıksız sıvının dışarı alınması işlemi anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gözdeki bozuk sıvının dışarı çıkarılması işlemini korur."},"facet_ids":["F003"],"text":"gözdeki bozuk sıvıyı çıkarmak","usage_role":"contextual"}],"definition":"Kanıt tek bir çekirdek sunmaz: bir atı çubuk gibi ince olana dek zayıflatma, gözün içeri çökmesi ve gözdeki bozuk sıvıyı çıkarma ayrı olaylardır ve bölünmeden ortak tanım altında birleştirilemez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir at, çubuk gibi ince görünecek ölçüde zayıflatılır veya bu incelikte nitelenir."},{"facet_id":"F002","role":"source_variant","statement":"Bir atın, devenin veya başka bir canlının gözü içeri çöker."},{"facet_id":"F003","role":"source_variant","statement":"Gözde bulunan bozuk sıvı bir işlemle dışarı çıkarılır."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"atı çubuk gibi ince olana dek zayıflatmak"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"çubuk gibi ince, zayıf at"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"gözü içeri çökmek"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"gözdeki bozuk sıvıyı çıkarmak"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"içeri çökmüş göz"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"قدح الفرس تقديحا إذا ضمر حتى يصير مثل القدح (maqayis)؛ قدحت العين غارت (maqayis)؛ قدحت العين أخرجت ماءها الفاسد (maqayis)؛ قدح الفرس تقديحا إذا ضمر حتى يصير مثل القدح (jamhara)؛ قدحت عين الفرس وكذلك عين البعير إذا غارت (jamhara)؛ قدحت العين إذا أخرجت منها الماء الفاسد (sihah)؛ وقدحت عينه وقدحت أيضا مخففة إذا غارت (sihah)؛ وقدح فرسه تقديحا ضمره (sihah)","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["MQ","JA","SI"],"what_is_ar":"ضمر الفرس حتى يصير مثل القدح وغؤور العين أو إخراج مائها الفاسد","what_is_not_ar":"أكال الأسنان؛ قدح السهم نفسه؛ قدح النار؛ الطعن في النسب"},"support_links":[]},{"boundary":"Dal yalnız bitkinin körpe uçlarını ve taze uç yapraklarını kapsar; kuru sap, genel filizlenme, içecek kabı veya ateş çıkarma aracı anlamlarını kapsamaz.","branch_kind":"bare","branch_ref":"root_001203/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَدْح","morph_features":"STEM|POS:N|LEM:qadoH|ROOT:qdH|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:2:1","qac_word_ref":"100:2:2","surface_ar":"قَدْحًا"}],"gloss":"bitkinin körpe uç yaprakları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bitkinin büyüme ucundaki yumuşak, taze ve körpe yapraklı bölüm adlandırılır."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir yem bitkisinin yumuşak ve taze uçları bu kullanımın örneğidir."}}],"root_ar":"ق د ح","root_id":"root_001203","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bitkinin yumuşak, taze ve uçta bulunan yapraklı bölümü genel olarak adlandırılırken kullanılır.","boundary_detail":"Dal yalnız bitkinin körpe uçlarını ve taze uç yapraklarını kapsar; kuru sap, genel filizlenme, içecek kabı veya ateş çıkarma aracı anlamlarını kapsamaz.","branch_image_ar":"رخص أطراف النبت","concept_gloss":"bitkinin körpe uç yaprakları","contextual_glosses":[{"applicability":"Kanıtta örneklenen yem bitkisinin yumuşak uç bölümleri anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yem bitkisinin yumuşak ve taze uçları olma özelliğini korur."},"facet_ids":["F002"],"text":"yem bitkisinin taze uçları","usage_role":"contextual"}],"definition":"Bir bitkinin, özellikle yem bitkisinin, yumuşak ve taze uçları ile uçlarda bulunan körpe yapraklardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bitkinin büyüme ucundaki yumuşak, taze ve körpe yapraklı bölüm adlandırılır."},{"facet_id":"F002","role":"example","statement":"Bir yem bitkisinin yumuşak ve taze uçları bu kullanımın örneğidir."}],"identity_rationale":"Kaynak ifadesi bitkinin, özellikle bir yem bitkisinin, yumuşak ve taze uçlarını ve körpe uç yapraklarını verir. Geçici çerçeve bu bitkisel parça anlamını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"bitkinin körpe uçları ve taze yaprakları"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"tek bir körpe bitki ucu"}],"lexicalization_note":"Tanım, yalın dalın körpe bitki ucu anlamını esas alır; başka yapılardan kap, ok veya ateş aracı anlamı aktarmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yeni sürgün dalı, taze büyüme ortaklığını korurken bu dalın uç yapraklarla sınırlı kapsamını en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bitkinin körpe uç yapraklarıyla sınırlıdır; komşu dal yeni sürgünün tamamını ve bitki dışındaki benzetmeli kullanımları da kapsar.","focus_only":"Bitkinin özellikle uçta bulunan körpe ve taze yapraklı bölümüne bağlıdır.","gloss":"körpe uç yaprak ile yeni sürgün","neighbor_only":"Yeni sürgün ve ince dalın yanı sıra saç, ince tüy ve küçük yavru gibi benzetmeli uzantıları da kapsar.","neighbor_ref":"root_000810/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da bitki üzerinde yeni çıkmış, yumuşak ve taze büyümeyi adlandırır."}],"source_phrase_ar":"القداح أرآد رخصة من الفسفسة (ayn)؛ القداح أطراف النبت من الورق الغض (jamhara)","source_summary":"Kaynaklar bitkinin körpe uçları ve taze uç yapraklarında birleşir; bir yem bitkisinin yumuşak uçları somut örnek olarak verilir.","sources":["AY","JA"],"what_is_ar":"القداح من أطراف النبت والورق الغض ورخص النبات","what_is_not_ar":"قدح الشرب؛ قدح السهم؛ القداح الذي تورى منه النار؛ القادحة الدودة"},"support_links":[]},{"boundary":"Dal, belirli bir iş üzerinde düşünme ile o işi düzenleyip yürütme tasarısını birlikte gerektirir; salt bakma, karar verme veya danışma anlamına indirgenmez.","branch_kind":"collocation","branch_ref":"root_001203/B010","candidate_links":[{"candidate_id":"cand_5ad8fa83d37710436d66","lane":"micro"},{"candidate_id":"cand_6b1c0da1b307c065eaf7","lane":"micro"},{"candidate_id":"cand_1f47d9ca9449c0f7c218","lane":"micro"},{"candidate_id":"cand_38f5213e2e84f740cfec","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَدْح","morph_features":"STEM|POS:N|LEM:qadoH|ROOT:qdH|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:2:1","qac_word_ref":"100:2:2","surface_ar":"قَدْحًا"}],"gloss":"bir işi düşünüp nasıl yürütüleceğini tasarlamak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi belirli bir işin koşullarını ve yönlerini dikkatle düşünür."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu düşünme, işin nasıl düzenlenip yürütüleceğine ilişkin bir tasarı kurmaya yönelir."}}],"root_ar":"ق د ح","root_id":"root_001203","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli bir işi değerlendirme ve onun yürütülüşünü planlama birlikte anlatılırken kullanılır.","boundary_detail":"Dal, belirli bir iş üzerinde düşünme ile o işi düzenleyip yürütme tasarısını birlikte gerektirir; salt bakma, karar verme veya danışma anlamına indirgenmez.","branch_image_ar":"اقتداح الأمر بالنظر والتدبير","concept_gloss":"bir işi düşünüp nasıl yürütüleceğini tasarlamak","contextual_glosses":[{"applicability":"Bir meselenin yönlerini değerlendirip uygulanabilir bir düzen kurma bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Meseleyi düşünme ve onu düzenleme yönelimini birlikte korur."},"facet_ids":["F001","F002"],"text":"bir meseleyi düşünüp düzenlemek","usage_role":"contextual"}],"definition":"Bir işi veya meseleyi ele alıp üzerinde düşünerek nasıl düzenleneceğini ve yürütüleceğini tasarlamaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi belirli bir işin koşullarını ve yönlerini dikkatle düşünür."},{"facet_id":"F002","role":"core","statement":"Bu düşünme, işin nasıl düzenlenip yürütüleceğine ilişkin bir tasarı kurmaya yönelir."}],"identity_rationale":"Kaynak ifadesi bir işi veya meseleyi ele alıp üzerinde düşünme ve onu nasıl yürüteceğini tasarlama eylemini açıkça verir. Geçici çerçeve bu iki aşamalı yapıyı doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"bir işi düşünüp nasıl yürütüleceğini tasarlamak"}],"lexicalization_note":"Tanım yalnız iş veya mesele bildiren tamamlayıcıyla kurulan düşünme ve tasarlama yapısına bağlıdır; yalın biçime genel bir düşünmek anlamı verilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; işin sonucunu gözeterek yönetme dalı, düşünme ve tasarlama ortaklığını korurken sonuç odağındaki farkı en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal düşünmeden yürütme tasarısına geçişi vurgular; komşu dal ise düzenlemenin yanında işin sonunu ve sonuçlarını önceden gözetmeyi belirginleştirir.","focus_only":"İşi ele alıp onun yürütme biçimini kurma eylemini öne çıkarır.","gloss":"işi tasarlamak ile sonucunu gözeterek yönetmek","neighbor_only":"İşin sonunda neye varacağını ve doğuracağı sonucu düşünmeyi açıkça öne çıkarır.","neighbor_ref":"root_000458/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da bir işi düşünerek düzenleme ve bilinçli biçimde yürütme alanındadır."}],"source_phrase_ar":"الإنسان يقتدح الأمر إذا نظر فيه ودبر (ayn)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu kullanım yalnız bir tanıklıkta, belirli bir işi düşünüp yürütme biçimini tasarlama anlamıyla yer alır."}],"source_summary":"Tek tanıklık, bir işi düşünme ile onun nasıl düzenlenip yürütüleceğini tasarlama aşamalarını birlikte verir.","sources":["AY"],"what_is_ar":"اقتداح الأمر بالنظر فيه وتدبيره","what_is_not_ar":"قدح النار؛ قدح السهم؛ الطعن في النسب؛ غرف القدر"},"support_links":["sup_600ad722dbe3b7fdd23a","sup_79dd429d524c22e0f1d3","sup_894e12d93de9e07af3e0","sup_e5087cf0eafc7928d3e9"]},{"boundary":"Dal, iç organları ya da akciğeri tutan hastalıkla sınırlıdır; yara yoklama kullanımı yalnızca kendi sözlüksel biriminde gösterilir.","branch_kind":"mixed_non_bare","branch_ref":"root_001642/B001","candidate_links":[{"candidate_id":"cand_b6fd7a931cd92299499c","lane":"micro"},{"candidate_id":"cand_20ed608e7980f8340c47","lane":"micro"},{"candidate_id":"cand_a049af0ff9c8dcc76947","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُورِيَٰت","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:muwriya`t|ROOT:wry|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:1:3","qac_word_ref":"100:2:1","surface_ar":"مُورِيَٰتِ"}],"gloss":"iç organları bozan ya da akciğeri tutan hastalık","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hastalık insanın ya da devenin içine yerleşir ve iç organları bozar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hastalığın bozuşu, irinin içi yiyip tüketmesi biçiminde anlatılabilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hastalığın akciğeri tutan bir türü de belirtilir."}}],"root_ar":"و ر ي","root_id":"root_001642","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hastalığın içteki bozuşunu ve akciğer tutulumunu birlikte temsil eden genel açıklamada kullanılır.","boundary_detail":"Dal, iç organları ya da akciğeri tutan hastalıkla sınırlıdır; yara yoklama kullanımı yalnızca kendi sözlüksel biriminde gösterilir.","branch_image_ar":"داء يأكل الجوف أو يصيب الرئة","concept_gloss":"iç organları bozan ya da akciğeri tutan hastalık","contextual_glosses":[{"applicability":"İrinin kişinin ya da hayvanın içini bozması anlatıldığında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İrinin içi yiyerek bozması biçimindeki özel gerçekleşmeyi korur."},"facet_ids":["F002"],"text":"irin içini yiyip bitirdi","usage_role":"contextual"},{"applicability":"Hastalığın özellikle akciğerde ortaya çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hastalığın akciğeri tutan özel görünümünü açıkça korur."},"facet_ids":["F003"],"text":"akciğerini tutan hastalığa yakalandı","usage_role":"contextual"}],"definition":"İnsanın veya devenin iç organlarına girip onları bozan, kimi kullanımda akciğeri tutan bir hastalıktır; irin içi yiyip bozabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hastalık insanın ya da devenin içine yerleşir ve iç organları bozar."},{"facet_id":"F002","role":"specialization","statement":"Hastalığın bozuşu, irinin içi yiyip tüketmesi biçiminde anlatılabilir."},{"facet_id":"F003","role":"specialization","statement":"Hastalığın akciğeri tutan bir türü de belirtilir."}],"identity_rationale":"Kaynak ifade, insanın veya devenin içini bozan ve akciğeri tutabilen bir hastalığı doğrular. Yaranın yoklayana hastalık geçirmesi ayrı bir söz öbeğinde tanıklansa da yetkili dal iddiasında bulunmadığından dal tanımının kurucu parçası yapılmamıştır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"iç organları ya da akciğeri tutan hastalık"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"içi hastalıktan bozuldu; irin içini yedi"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"içi bu hastalıkla bozulmuş kimse"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"akciğeri tutan hastalık"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"akciğerinden yaraladı"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yara, onu yoklayana bu hastalığı geçirdi"}],"lexicalization_note":"Tanım, hastalık adını temel alır; içi bozma ve akciğeri yaralama gibi kullanımları yalnızca tanıklandıkları yapılara bağlı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca içe ilerleyen hastalık ile irin birikimi, dal sınırını açıklayan yararlı karşılaştırmalar sundu.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dalın çekirdeği içte yerleşen hastalıktır; komşunun çekirdeği ise yüzeyden içe doğru delen yara veya deri hastalığıdır.","focus_only":"Odak dal, iç organları bozan veya akciğeri tutan hastalığı adlandırır.","gloss":"içe ilerleyen yara ya da deri hastalığı","neighbor_only":"Komşu dal, deriyi delerek iç boşluğa ilerleyen yara ve deri hastalıklarını adlandırır.","neighbor_ref":"root_001539/B002","relation_type":"same_field","shared_zone":"İki dal da bedenin içine ulaşan ağır bir hastalık veya bozuş alanındadır."},{"boundary_match":"field_only","distinction":"Odakta irin hastalığın içteki yıkıcı etkisidir; komşuda ise yaranın içinde biriken madde doğrudan adlandırılır.","focus_only":"Odak dal, irinin iç organları yiyip bozabildiği bir hastalığı anlatır.","gloss":"yarada biriken irin","neighbor_only":"Komşu dal, çıban ya da yarada birikmiş irin ve cerahati adlandırır.","neighbor_ref":"root_000282/B003","relation_type":"same_field","shared_zone":"İrin ve bedensel bozuş iki dalın ortak alanını oluşturur."}],"source_phrase_ar":"الورى داء يداخل الجسم (maqayis)؛ وري جوف فلان فهو موري إذا فسد من داء يصيبه (jamhara)؛ ورى القيح جوفه يريه وريا: أكله (sihah)؛ الورى داء يصيب الرجل والبعير في أجوافهما (tahdhib)؛ الوارية داء يأخذ في الرئة (ayn;tahdhib)","source_summary":"Kaynaklar, içe yerleşip bedeni bozan hastalık çekirdeğinde birleşir; bazı anlatımlar irinin içi yemesini, bazıları da akciğer tutulumunu öne çıkarır.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه الوري والورى داء الجوف أو الرئة، وأكل القيح للجوف، وإصابة الرئة، والجراحة التي يصيب سابرها الوري.","what_is_not_ar":"لا يدخل فيه ستر الخبر، ولا وراء المكان، ولا خروج نار الزند، ولا السمن."},"support_links":["sup_666c11b53573bb907d5a","sup_8cca43a23df303bfbf15","sup_fb18fefa7d46de4bde6c"]},{"boundary":"Dal, ateşin çakmaktan çıkması ve sönük ateşin harlanmasıyla sınırlıdır; araç adı yalnızca sözlüksel karşılığında yer alır.","branch_kind":"mixed_non_bare","branch_ref":"root_001642/B002","candidate_links":[{"candidate_id":"cand_67b2dc4c2b81e967f501","lane":"micro"},{"candidate_id":"cand_1e2df9ee9cd8ac109fdd","lane":"micro"},{"candidate_id":"cand_51e6c67c379e15c425b7","lane":"micro"},{"candidate_id":"cand_e5e93d899d5d4dbce459","lane":"micro"},{"candidate_id":"cand_6b8a123830fdac961a35","lane":"micro"},{"candidate_id":"cand_7274ee5a76dde7e9de19","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُورِيَٰت","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:muwriya`t|ROOT:wry|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:1:3","qac_word_ref":"100:2:1","surface_ar":"مُورِيَٰتِ"}],"gloss":"çakmaktan ateş çıkarma ve sönük ateşi harlama","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çakmağın işlenmesi sonucunda içinde gizli ateş açığa çıkar."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sönük ateşin harlanıp alevinin yükseltilmesi de aynı dalda yer alır."}}],"root_ar":"و ر ي","root_id":"root_001642","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ateşin çakmaktan çıkarılmasıyla sönük ateşin yeniden canlandırılmasını birlikte anlatan genel açıklamadır.","boundary_detail":"Dal, ateşin çakmaktan çıkması ve sönük ateşin harlanmasıyla sınırlıdır; araç adı yalnızca sözlüksel karşılığında yer alır.","branch_image_ar":"نار كامنة تخرج من الزند","concept_gloss":"çakmaktan ateş çıkarma ve sönük ateşi harlama","contextual_glosses":[{"applicability":"Çakmağın kıvılcım verip ateşi açığa çıkardığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çakmaktaki ateşin dışarı çıkması olayını doğrudan korur."},"facet_ids":["F001"],"text":"çakmaktan ateş çıktı","usage_role":"contextual"},{"applicability":"Sönmeye yüz tutmuş ateşin canlandırılıp yükseltildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sönük ateşi yeniden canlandırma ve yükseltme işlemini korur."},"facet_ids":["F002"],"text":"sönük ateşi yeniden harladı","usage_role":"contextual"}],"definition":"Çakmaktan ateşin çıkması veya sönük durumdaki ateşin harlanarak yeniden yükseltilmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çakmağın işlenmesi sonucunda içinde gizli ateş açığa çıkar."},{"facet_id":"F002","role":"extension","statement":"Sönük ateşin harlanıp alevinin yükseltilmesi de aynı dalda yer alır."}],"identity_rationale":"Yetkili kaynak ifadesi, çakmaktan ateş çıkmasını ve sönük ateşin yeniden harlanıp yükseltilmesini doğrular. Ateş yakmaya yarayan araç yalnızca ayrı sözlüksel birimde tanıklandığı için dalın kurucu tanımından çıkarılmıştır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"çakmaktan ateş çıktı"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"sönük ateşi harlayıp yükseltti"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ateş yakmaya yarayan araç"}],"lexicalization_note":"Çakmaktan ateş çıkması ile sönük ateşi harlama ayrılır; her eylem tanıklandığı yapının sınırında tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ateş çıkarma, genel tutuşma ve közü karıştırma dalları işlemin kapsamını en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çakmaktan ilk ateşi çıkarma bağlamında örtüşürler; odak dal ayrıca sönük ateşi canlandırırken komşu, vurarak ateş çıkarma yöntemine ve araçlarına yoğunlaşır.","focus_only":"Odak dal, çakmaktan ateş çıkmasına ek olarak sönük ateşin harlanmasını da kapsar.","gloss":"vurarak ateş çıkarma","neighbor_only":"Komşu dal, çakmak, taş veya demirle vurarak ateş çıkarma eylemini ve araçlarını öne çıkarır.","neighbor_ref":"root_001203/B001","relation_type":"near_synonym","shared_zone":"İki dal da çakmak benzeri bir araçtan ateş çıkarma olayını paylaşır."},{"boundary_match":"partial","distinction":"Odak belirli bir ateş çıkarma veya yeniden canlandırma işlemidir; komşu ise tutuşma ve yanmanın daha geniş durum alanını adlandırır.","focus_only":"Odak dal, ateşin çakmaktan çıkışını ve sönük ateşin harlanmasını anlatır.","gloss":"ateşin tutuşup yanması","neighbor_only":"Komşu dal, ateşin tutuşması, yanması, ısısı ve yakıtıyla daha geniş bir yanma alanını kapsar.","neighbor_ref":"root_000708/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda ateşin yanar duruma gelmesi ortak sonuçtur."},{"boundary_match":"partial","distinction":"Odak dal kullanılan yöntemi zorunlu kılmaz; komşu dalda ise közün fiziksel olarak karıştırılması kurucu işlemdir.","focus_only":"Odak dal, çakmaktan ateş çıkarma ve sönük ateşi genel olarak harlama kapsamına sahiptir.","gloss":"közü karıştırıp ateşi tutuşturma","neighbor_only":"Komşu dal, özellikle közleri karıştırarak ateşi yeniden tutuşturma işlemini belirtir.","neighbor_ref":"root_001639/B005","relation_type":"near_neighbor","shared_zone":"Sönmüş ya da zayıflamış ateşi yeniden canlandırma iki dalda ortaktır."}],"source_phrase_ar":"ورى الزند خرجت ناره (maqayis;jamhara;sihah;mufradat)؛ إذا أخرج الزند النار قيل وري الزند يري (tahdhib)؛ أوريت النار إذا كانت خامدة فأججتها (ayn)؛ أريت النار تأرية إذا رفعتها (tahdhib)","source_summary":"Kaynaklar çakmaktan ateş çıkması üzerinde birleşir ve buna sönük ateşi yeniden harlayıp yükseltme kullanımını ekler.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه وري الزند وورى الزند وخروج ناره، وإيراء الزند أو النار، وإيقاد النار الخامدة ورفعها، وما يثقب به النار.","what_is_not_ar":"لا يدخل فيه مجاز نجاح الزند أو الإعانة، ولا ستر الخبر، ولا المرض."},"support_links":["sup_0038997092c3d7f5c042","sup_20bb3eac7d4e1c042e07","sup_7fa24b15fa1a9eac840c","sup_820492beff1443fb51f3","sup_8e704e9307a40d0a511d","sup_b1f045d586d5376cba7b"]},{"boundary":"Anlamlar yalnızca belirtilen çakmaklı söz öbeklerine aittir; çıplak biçime genel bir başarı ya da yardım anlamı yüklenmez.","branch_kind":"collocation","branch_ref":"root_001642/B003","candidate_links":[{"candidate_id":"cand_5ad8fa83d37710436d66","lane":"micro"},{"candidate_id":"cand_6b1c0da1b307c065eaf7","lane":"micro"},{"candidate_id":"cand_1f47d9ca9449c0f7c218","lane":"micro"},{"candidate_id":"cand_ae9d5aa08d3fee718fe0","lane":"micro"},{"candidate_id":"cand_38f5213e2e84f740cfec","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُورِيَٰت","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:muwriya`t|ROOT:wry|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:1:3","qac_word_ref":"100:2:1","surface_ar":"مُورِيَٰتِ"}],"gloss":"çakmak benzetmesiyle başarma, yardım görme ya da savunma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir işe girişen kişinin çakmağının iyi ateş vermesi imgesi, amacına başarıyla ulaşmasını anlatır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kimsenin çakmağının başkasında ateş vermesi, onda yardım, içten öğüt, yetkinlik veya cömertlik bulmasını anlatır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birinin adına ateş çıkarma imgesi, onu destekleyip kendisinden zararı uzaklaştırmayı anlatır."}}],"root_ar":"و ر ي","root_id":"root_001642","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Üç ayrı söz öbeğinin ortak imgesini ve farklı sonuçlarını birlikte açıklamak gerektiğinde kullanılır.","boundary_detail":"Anlamlar yalnızca belirtilen çakmaklı söz öbeklerine aittir; çıplak biçime genel bir başarı ya da yardım anlamı yüklenmez.","branch_image_ar":"زند يقدح نجاحا أو نصرة","concept_gloss":"çakmak benzetmesiyle başarma, yardım görme ya da savunma","contextual_glosses":[{"applicability":"Çakmağı iyi ateş veren kişi üzerinden başarı anlatılan söz öbeğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir amaca girişip istenen sonucu elde etme anlamını korur."},"facet_ids":["F001"],"text":"giriştiği işte başarıya ulaştı","usage_role":"contextual"},{"applicability":"Bir kimseden yardım, öğüt, yetkinlik veya cömertlik görüldüğünde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başka bir kişide beklenen iyi nitelikleri ve yardımı bulmayı korur."},"facet_ids":["F002"],"text":"sende içtenlik ve yardım buldum","usage_role":"contextual"},{"applicability":"Bir kişinin yanında durup ondan zararı uzaklaştırma bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Birine yardım etme ve onu saldırıya karşı savunma anlamını korur."},"facet_ids":["F003"],"text":"onu destekleyip savundu","usage_role":"contextual"}],"definition":"Çakmak imgesine bağlı söz öbeklerinde bir işte başarıya ulaşmayı, bir kimsede yardım ve iyi nitelikler bulmayı ya da birini destekleyip savunmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir işe girişen kişinin çakmağının iyi ateş vermesi imgesi, amacına başarıyla ulaşmasını anlatır."},{"facet_id":"F002","role":"associated_use","statement":"Bir kimsenin çakmağının başkasında ateş vermesi, onda yardım, içten öğüt, yetkinlik veya cömertlik bulmasını anlatır."},{"facet_id":"F003","role":"associated_use","statement":"Birinin adına ateş çıkarma imgesi, onu destekleyip kendisinden zararı uzaklaştırmayı anlatır."}],"identity_rationale":"Kaynak ifade, çakmak imgesine bağlı üç yapıyı açıkça destekler: girişilen işte başarıya ulaşma, bir kimsede yardım ve iyi nitelikler bulma, birini destekleyip savunma.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"giriştiği işte başarıya ulaşan"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"sende yardım, içten öğüt ve cömertlik buldum"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"onu destekledi ve savundu"}],"lexicalization_note":"Dal bütünüyle söz öbeklerine bağlıdır; başarı, yardım görme ve savunma kullanımları kendi yapılarından dışarı genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yardım, amaca ulaşma ve saygıyla savunma dalları üç yapı arasındaki sınırları en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın yardım anlamı sabit imgesel yapılara bağlıdır; komşu dal ise imge ve yapı kısıtı olmadan yardım ilişkisini doğrudan anlatır.","focus_only":"Odak dal, yardımı çakmak imgesine bağlı belirli söz öbekleri içinde anlatır ve başarı ile savunmayı da kapsar.","gloss":"genel yardım ve dayanışma","neighbor_only":"Komşu dal, yardım etme, yardım isteme ve karşılıklı yardımlaşmayı genel olarak adlandırır.","neighbor_ref":"root_001064/B001","relation_type":"near_neighbor","shared_zone":"Bir kişiye destek sağlama iki dalın ortak anlam alanıdır."},{"boundary_match":"partial","distinction":"Odakta başarı yalnızca belirli çakmaklı yapı içinde ortaya çıkar; komşuda başarı ve elde etme bağımsız anlam çekirdeğidir.","focus_only":"Odak dal başarıyı çakmak imgesiyle anlatır ve yardım ile savunma kullanımlarını da içerir.","gloss":"istenen sonuca ulaşma","neighbor_only":"Komşu dal, istenen şeyi elde edip amaca ulaşmayı doğrudan anlatır.","neighbor_ref":"root_000941/B002","relation_type":"near_neighbor","shared_zone":"Amaçlanan sonucu elde etme, odak dalın bir söz öbeğiyle komşunun çekirdeğinde ortaktır."},{"boundary_match":"partial","distinction":"Odak dal yalnızca yapı içindeki destek ve savunmayı verir; komşu dal bunlara yüceltme ve saygı gösterme koşulunu ekler.","focus_only":"Odak dalın savunma kullanımı belirli bir söz öbeğine bağlıdır ve saygı göstermeyi içermez.","gloss":"savunma ve saygıyla yüceltme","neighbor_only":"Komşu dal, destek ve savunmaya ek olarak kişiyi yüceltme ve ona saygı gösterme anlamlarını taşır.","neighbor_ref":"root_001007/B001","relation_type":"near_neighbor","shared_zone":"Bir kişiyi destekleyip ondan zararı uzaklaştırma iki dalda ortaktır."}],"source_phrase_ar":"ورت بك زنادي إذا أنجده وأعانه (jamhara)؛ وريت بك زنادي أي رأيت منك ما أحب من النصح والنجابة والسماحة (ayn)؛ لواري الزناد إذا رام أمرا أنجح فيه وأدرك ما طلب (tahdhib;mufradat)؛ لوريت عن مولاك أي نصرته ودفعت عنه (tahdhib)","source_summary":"Kaynaklar çakmak imgesini başarı, yardım ve savunma alanlarına taşır; kullanımlar aynı mecaz çevresinde olsa da farklı söz öbeklerine bağlıdır.","sources":["AY","JA","TA","MU"],"what_is_ar":"يدخل فيه قولهم فلان واري الزند إذا أنجح وأدرك طلبه، وورت بك زنادي إذا وجد منك نصحا وسماحة أو إعانة، ووريت عن فلان إذا نصرته ودفعت عنه.","what_is_not_ar":"لا يدخل فيه الاشتعال الحسي للزند، ولا مجرد ستر الخبر."},"support_links":["sup_600ad722dbe3b7fdd23a","sup_79dd429d524c22e0f1d3","sup_8491936c09669d92d8cf","sup_894e12d93de9e07af3e0","sup_e5087cf0eafc7928d3e9"]},{"boundary":"Dal semizlik ve yağ dolgunluğuyla sınırlıdır; hastalık, ateş ve yaratılmışlar anlamları bu daldan ayrıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001642/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُورِيَٰت","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:muwriya`t|ROOT:wry|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:1:3","qac_word_ref":"100:2:1","surface_ar":"مُورِيَٰتِ"}],"gloss":"yağlı ve semiz olma; iliğin dolgunlaşması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Et veya yağ, belirgin yağlılık ve semizlik niteliği taşır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı nitelik dişi devenin semizliğini belirtmek için kullanılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kemik iliği için kullanım, iliğin dolup yoğunlaşmasını belirtir."}}],"root_ar":"و ر ي","root_id":"root_001642","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Et, yağ ve hayvan semizliğiyle kemik iliğinin dolgunlaşmasını birlikte temsil eden açıklamadır.","boundary_detail":"Dal semizlik ve yağ dolgunluğuyla sınırlıdır; hastalık, ateş ve yaratılmışlar anlamları bu daldan ayrıdır.","branch_image_ar":"شحم وار وسمن ظاهر","concept_gloss":"yağlı ve semiz olma; iliğin dolgunlaşması","contextual_glosses":[{"applicability":"Etin veya yağın dolgun ve semiz olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Etteki belirgin yağlılık ve semizlik niteliğini korur."},"facet_ids":["F001"],"text":"eti yağlı ve semizdi","usage_role":"contextual"},{"applicability":"Kemik iliğinin dolgunlaşıp sıkılaştığı özel söz öbeğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kemik iliğinin dolması ve yoğunlaşması sürecini korur."},"facet_ids":["F003"],"text":"kemik iliği dolup yoğunlaştı","usage_role":"contextual"}],"definition":"Etin, yağın veya hayvanın yağlı ve semiz olmasıdır; kemik iliği söz konusu olduğunda dolup yoğunlaşmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Et veya yağ, belirgin yağlılık ve semizlik niteliği taşır."},{"facet_id":"F002","role":"specialization","statement":"Aynı nitelik dişi devenin semizliğini belirtmek için kullanılır."},{"facet_id":"F003","role":"extension","statement":"Kemik iliği için kullanım, iliğin dolup yoğunlaşmasını belirtir."}],"identity_rationale":"Kaynak ifade yağlı ve semiz et ya da hayvan niteliğini açıkça verir; ayrıca kemik iliğinin dolup yoğunlaşmasını aynı dalın ayrı bir kullanımı olarak doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yağlı ve semiz"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"semiz dişi deve"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kemik iliği dolup yoğunlaştı"}],"lexicalization_note":"Semizlik bildiren biçim ile dişi deve ve kemik iliği söz öbekleri ayrılır; söz öbeğine özgü ayrıntılar genel niteliğe taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ilik, devenin semizleşmesi ve ilikte yağ tadı dalları semizlik çekirdeğinin kapsamını belirginleştirir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal et ve yağın genel semiz niteliğine kadar uzanır; komşu dalın merkezi kemik içindeki ilik ve ona bağlı semizliktir.","focus_only":"Odak dal, yağlı et ve semiz hayvan niteliğini, ayrıca iliğin dolgunlaşmasını kapsar.","gloss":"kemik iliği ve buna bağlı semizlik","neighbor_only":"Komşu dal, özellikle kemik içindeki iliği ve hayvanın bu ilikle ilişkilendirilen semizliğini adlandırır.","neighbor_ref":"root_000601/B002","relation_type":"near_synonym","shared_zone":"Kemik iliğinin dolgunluğu ve hayvanın semizliği iki dalda güçlü biçimde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal daha çok niteliği bildirir ve et ile iliğe de uygulanır; komşu dal özellikle devenin semizleşme sürecine bağlıdır.","focus_only":"Odak dal, mevcut semizlik niteliğini ve iliğin dolgunluğunu belirtir.","gloss":"dişi devenin semizleşmesi","neighbor_only":"Komşu dal, dişi devenin semizleşmesi veya yağının artması sürecini belirtir.","neighbor_ref":"root_001570/B005","relation_type":"near_neighbor","shared_zone":"Dişi devenin yağlı ve semiz duruma gelmesi iki dalda ortak alandır."},{"boundary_match":"field_only","distinction":"Odak doğrudan semizlik niteliğidir; komşu ise semizliği ilikteki yağ tadı gibi belirli bir göstergeyle tanımlar.","focus_only":"Odak dal etin, yağın veya hayvanın semiz niteliğini doğrudan bildirir.","gloss":"ilikte yağ tadıyla anlaşılan semizlik","neighbor_only":"Komşu dal, hayvanın iliğinde yağ tadı bulunması gibi bir belirti üzerinden semizliği anlatır.","neighbor_ref":"root_000934/B007","relation_type":"same_field","shared_zone":"Hayvanın yağlı ve semiz oluşu iki dalın ortak alanıdır."}],"source_phrase_ar":"اللحم الواري: السمين (maqayis;mufradat)؛ الواري الشحم السمين والوري مثله (ayn)؛ ناقة وارية بغير همز: سمينة (jamhara)؛ وري المخ إذا اكتنز وناقة وارية أي سمينة ولحم وري أي سمين (sihah)","source_summary":"Kaynaklar et, yağ ve dişi deve için semizlikte birleşir; bir kullanım da kemik iliğinin dolgunlaşıp yoğunlaşmasını bildirir.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه اللحم الواري والشحم الواري والوري مثله، والناقة الوارية، واكتناز المخ.","what_is_not_ar":"لا يدخل فيه داء الجوف وإن اتحد اللفظ، ولا النار، ولا الورى بمعنى الخلق."},"support_links":[]},{"boundary":"Dal fiziksel gizleme ile iletişimsel niyet gizlemeyi kapsar; yer yönü, soy ve ateş anlamları bu daldan ayrıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001642/B005","candidate_links":[{"candidate_id":"cand_d72e6b293b6e7b9e90e3","lane":"micro"},{"candidate_id":"cand_d0e9f665449e155785f1","lane":"micro"},{"candidate_id":"cand_6b8a123830fdac961a35","lane":"micro"},{"candidate_id":"cand_7652d264cda10c10e551","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُورِيَٰت","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:muwriya`t|ROOT:wry|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:1:3","qac_word_ref":"100:2:1","surface_ar":"مُورِيَٰتِ"}],"gloss":"gizleme, gizlenme ve başka anlam gösterme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesne görünürlükten kaldırılarak gizlenir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi kendisini saklayarak gözden kaybolur."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir haber veya niyet, asıl anlam saklanıp görünürde başka bir anlam gösterilerek gizlenir."}}],"root_ar":"و ر ي","root_id":"root_001642","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel saklama ile haber veya niyeti başka bir görünür anlam altında örtmeyi birlikte açıklamak için kullanılır.","boundary_detail":"Dal fiziksel gizleme ile iletişimsel niyet gizlemeyi kapsar; yer yönü, soy ve ateş anlamları bu daldan ayrıdır.","branch_image_ar":"ستر الشيء وجعله وراء الظهور","concept_gloss":"gizleme, gizlenme ve başka anlam gösterme","contextual_glosses":[{"applicability":"Bir nesnenin görünmeyecek biçimde gizlendiği fiziksel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesneyi görünürlükten kaldırarak gizleme işlemini korur."},"facet_ids":["F001"],"text":"onu gözden sakladı","usage_role":"contextual"},{"applicability":"Bir kişinin kendisini saklayıp görünmez olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin kendi isteğiyle saklanıp gözden kaybolmasını korur."},"facet_ids":["F002"],"text":"gizlenip gözden kayboldu","usage_role":"contextual"},{"applicability":"Konuşanın gerçek niyetini saklayıp görünürde başka bir anlam sunduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Asıl niyeti gizleme ve yerine başka bir görünür anlam sunma işlemini korur."},"facet_ids":["F003"],"text":"asıl niyetini başka sözle gizledi","usage_role":"contextual"}],"definition":"Bir şeyi görünürlükten kaldırmak veya kişinin kendisini saklamasıdır; haber ya da niyet söz konusu olduğunda asıl olanı gizleyip görünürde başka bir anlam sunmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesne görünürlükten kaldırılarak gizlenir."},{"facet_id":"F002","role":"core","statement":"Kişi kendisini saklayarak gözden kaybolur."},{"facet_id":"F003","role":"specialization","statement":"Bir haber veya niyet, asıl anlam saklanıp görünürde başka bir anlam gösterilerek gizlenir."}],"identity_rationale":"Kaynak ifade bir şeyi gizlemeyi, kişinin gözden saklanmasını ve haber ya da niyeti gizlemek için görünürde başka bir anlam öne çıkarmayı açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"şeyi gizleyip gözden sakladı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"gizlendi, gözden kayboldu"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"haberi gizleyip başka bir anlamı öne çıkarma"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"niyetini gizlemek için başka bir şey söyledi"}],"lexicalization_note":"Genel gizleme ve gizlenme çekirdeği korunur; haberi veya niyeti başka sözle örtme yalnızca ilgili yapılara bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel gizlenme, dolaylı anlatım ve anlamı açığa çıkarma dalları fiziksel ve iletişimsel sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Fiziksel gizleme alanında büyük ölçüde örtüşürler; odak dal iletişimde başka anlam gösterme yapısını belirginleştirirken komşu daha genel örtme araçlarını kapsar.","focus_only":"Odak dal, fiziksel gizlemeye ek olarak haber veya niyeti başka bir anlam göstererek örtmeyi kapsar.","gloss":"genel örtme ve gizlenme","neighbor_only":"Komşu dal, nesneyi duyulardan saklama, bir şeyle örtünme ve düşünceyi içinde tutma gibi daha genel gizlilik kullanımlarına uzanır.","neighbor_ref":"root_000266/B001","relation_type":"near_synonym","shared_zone":"Bir şeyi görünürlükten kaldırma ve kişinin saklanması iki dalda ortaktır."},{"boundary_match":"partial","distinction":"Odakta gizleme ve başka bir görünür anlam sunma kurucu işlemdir; komşu ise mutlaka gizleme amacı taşımayan genel dolaylı anlatımı da kapsar.","focus_only":"Odak dal, asıl haber veya niyeti gizleyip görünürde başka bir anlam sunma işlemini içerir.","gloss":"üstü kapalı ve çift anlamlı söz","neighbor_only":"Komşu dal, doğrudan söylememe, üstü kapalı anlatma ve sözün iki yoruma açık olması alanını daha geniş kapsar.","neighbor_ref":"root_001001/B010","relation_type":"near_neighbor","shared_zone":"Konuşanın gerçek maksadını açıkça söylememesi iki dalda ortaktır."},{"boundary_match":"opposed","distinction":"Odak anlamı örter veya başka anlamla perdeler; komşu aynı iletişim ekseninde anlamı açar ve belirginleştirir.","focus_only":"Odak dal, nesneyi veya anlamı görünmez ve anlaşılmaz kılmaya yönelir.","gloss":"anlamı açıkça ortaya koyma","neighbor_only":"Komşu dal, söz, yazı ya da işaretle anlamı açığa çıkarıp anlaşılır kılmaya yönelir.","neighbor_ref":"root_000170/B005","relation_type":"polarity_pair","shared_zone":"İki dal, bir anlamın muhataba görünür olup olmaması ekseninde karşı karşıya gelir."}],"source_phrase_ar":"التورية إخفاء الخبر وعدم إظهار السر تقول وريته تورية (ayn)؛ واريت الشيء أي أخفيته وتوارى هو أي استتر (sihah)؛ التورية الستر وريت الخبر أوريه تورية إذا سترته وأظهرت غيره (tahdhib)؛ واريت كذا إذا سترته وتوارى استتر (mufradat)","source_summary":"Kaynaklar fiziksel gizleme ve gizlenme çekirdeğinde birleşir; iletişim alanında bu çekirdek, asıl haber veya niyet yerine başka bir görünür anlam sunmaya dönüşür.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه وارى الشيء إذا أخفاه، وتوارى إذا استتر، ووري الخبر تورية إذا ستره وأظهر غيره، وإظهار غير المراد.","what_is_not_ar":"لا يدخل فيه وراء المكان إلا من جهة التعليل، ولا ولد الولد، ولا نار الزند."},"support_links":["sup_4663a1f9d53122baeb95","sup_820492beff1443fb51f3","sup_a67ea33db9bc803b54e2","sup_abd45b352cfcac0a5a52"]},{"boundary":"Dal göreli konum ve taraf ilişkisini anlatır; geri çekilme buyruğu yalnızca kendi sözlüksel biriminde gösterilir.","branch_kind":"mixed_non_bare","branch_ref":"root_001642/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُورِيَٰت","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:muwriya`t|ROOT:wry|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:1:3","qac_word_ref":"100:2:1","surface_ar":"مُورِيَٰتِ"}],"gloss":"konuma göre arka, ön, öte ya da öbür yan","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığın arkasındaki tarafı gösterir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bakış yönüne ve bağlama göre ön taraftaki konumu da gösterebilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Öte, başka olan veya bir duvarın ya da engelin öbür yanı anlamına genişler."}}],"root_ar":"و ر ي","root_id":"root_001642","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Göreli yer değerinin bağlama göre değişebildiğini eksiksiz açıklamak gerektiğinde kullanılır.","boundary_detail":"Dal göreli konum ve taraf ilişkisini anlatır; geri çekilme buyruğu yalnızca kendi sözlüksel biriminde gösterilir.","branch_image_ar":"الجانب الوراء: خلف أو أمام أو سوى","concept_gloss":"konuma göre arka, ön, öte ya da öbür yan","contextual_glosses":[{"applicability":"Bir varlığın arka tarafındaki konumun belirtildiği olağan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Referans alınan varlığın arka tarafında bulunma ilişkisini korur."},"facet_ids":["F001"],"text":"arkasında","usage_role":"contextual"},{"applicability":"Sözcüğün bağlama göre ön tarafı gösterdiği karşıt yönlü kullanımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bağlama bağlı ön tarafta bulunma değerini korur."},"facet_ids":["F002"],"text":"önünde","usage_role":"contextual"},{"applicability":"Bir şeyin ötesi, başkası veya bir engelin diğer yanı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öte ve engelin öbür yanı biçimindeki genişlemiş konum değerini korur."},"facet_ids":["F003"],"text":"ötesinde ya da öbür yanında","usage_role":"contextual"}],"definition":"Bir referans noktasına göre arka, kimi bağlamda ön, öte veya öbür tarafı; bir engelin bağlama göre herhangi bir yanını gösteren göreli yer ilişkisidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığın arkasındaki tarafı gösterir."},{"facet_id":"F002","role":"source_variant","statement":"Bakış yönüne ve bağlama göre ön taraftaki konumu da gösterebilir."},{"facet_id":"F003","role":"extension","statement":"Öte, başka olan veya bir duvarın ya da engelin öbür yanı anlamına genişler."}],"identity_rationale":"Kaynak ifade, konuma ve bakış yönüne göre arka, ön, öte, başka taraf veya bir engelin herhangi bir yanı anlamlarını doğrular. Geri çekilme buyruğu ayrı sözlüksel birimde tanıklansa da yetkili dal iddiasında açıkça kurulmadığı için ana tanıma alınmamıştır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"arka, ön, öte ya da öbür yan"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"geri çekil; yana açıl"}],"lexicalization_note":"Göreli yer bildiren biçim temel alınır; farklı yön değerleri bağlama göre ayrılır ve buyruk kullanımı genel yer anlamına karıştırılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ön taraf, yana yönelme ve gelinen yön dalları göreli konumun yön ve hareketten farkını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ön değeri bağlama bağlı seçeneklerden yalnızca biridir; komşu dalda ön ve karşı konum çekirdektir, arka taraf anlamı bulunmaz.","focus_only":"Odak dal bağlama göre arka, ön, öte veya öbür tarafı gösterebilir.","gloss":"ön taraf ve karşı konum","neighbor_only":"Komşu dal ön tarafı temel alır ve yakın, karşıda ya da yaklaşık olma değerlerine de uzanır.","neighbor_ref":"root_000053/B011","relation_type":"near_synonym","shared_zone":"Ön tarafta veya karşıda bulunma değeri iki dalın bir bölümünde örtüşür."},{"boundary_match":"partial","distinction":"Odak durağan ya da göreli bir yer ilişkisidir; komşu ise kişinin belirli bir yana doğru hareket etmesini veya yerleşmesini kurucu unsur yapar.","focus_only":"Odak dal, bir referans noktasına göre taraf veya konum bildirir.","gloss":"bir yana çekilme ya da yönelme","neighbor_only":"Komşu dal, bir yana oturma, gitme veya yönelme hareketini bildirir.","neighbor_ref":"root_001466/B004","relation_type":"near_neighbor","shared_zone":"Bir yanın seçilmesi, konum ve hareket bağlamlarında iki dalı birbirine yaklaştırır."},{"boundary_match":"field_only","distinction":"Odak bir referans nesnesine göre konum kurar; komşu ise hareketin geldiği yönü veya genel bir yönü belirtir.","focus_only":"Odak dal, bir nesnenin arka, ön, öte veya öbür tarafındaki göreli konumu bildirir.","gloss":"gelinen yön ya da taraf","neighbor_only":"Komşu dal, bir yerden gelinen yönü veya herhangi bir yön ve tarafı adlandırır.","neighbor_ref":"root_000065/B004","relation_type":"same_field","shared_zone":"Yön ve taraf bildirme iki dalın ortak kavramsal alanıdır."}],"source_phrase_ar":"وراءك يكون من خلف ويكون من قدام (maqayis)؛ وراء ممدود خلاف قدام (ayn)؛ وراء بمعنى خلف وقد يكون بمعنى قدام وهي من الأضداد (sihah)؛ الوراء الخلف ويكون الأمام وبما وراءه أي بما سواه (tahdhib)؛ وراء زيد كذا لمن خلفه ويقال لما كان قدامه أو في أي جانب من الجدار (mufradat)","source_summary":"Kaynaklar arka taraf anlamını temel değer olarak verir; bağlama göre ön, öte, başka olan ve bir engelin herhangi bir yanı değerlerinin de kullanılabildiğini belirtir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه وراء بمعنى خلف، وقدام أو أمام في بعض الاستعمال، وما بعد الشيء أو سواه، والجانب الآخر من حجاب أو جدار، وصيغة وراءك للإغراء بالتأخر أو التنحي.","what_is_not_ar":"لا يدخل فيه الوراء بمعنى ولد الولد، ولا الورى بمعنى الخلق، ولا ستر الخبر إلا إذا صرح بالستر."},"support_links":[]},{"boundary":"Dal yalnızca torunluk ilişkisini adlandırır; genel çocukluk, bütün soy çizgisi ve yer bildiren arka taraf anlamı dışarıda kalır.","branch_kind":"bare","branch_ref":"root_001642/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُورِيَٰت","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:muwriya`t|ROOT:wry|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:1:3","qac_word_ref":"100:2:1","surface_ar":"مُورِيَٰتِ"}],"gloss":"torun","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin çocuğundan doğan çocuk, yani torun adlandırılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bazı anlatımlarda kapsam özellikle oğlun oğluyla sınırlandırılır."}}],"root_ar":"و ر ي","root_id":"root_001642","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çocuğun çocuğunu genel olarak adlandıran en kısa doğal Türkçe karşılıktır.","boundary_detail":"Dal yalnızca torunluk ilişkisini adlandırır; genel çocukluk, bütün soy çizgisi ve yer bildiren arka taraf anlamı dışarıda kalır.","branch_image_ar":"ولد الولد يأتي من وراء الابن","concept_gloss":"torun","contextual_glosses":[{"applicability":"Torunluk ilişkisinin kuşak yapısını açıkça belirtmek gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir alt kuşaktaki çocuktan doğan çocuk ilişkisini korur."},"facet_ids":["F001"],"text":"çocuğunun çocuğu","usage_role":"explanatory"},{"applicability":"Kaynak ifadenin torunu özellikle erkek soy çizgisinde daralttığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Erkek çocuk üzerinden gelen erkek torun sınırlamasını korur."},"facet_ids":["F002"],"text":"oğlunun oğlu","usage_role":"contextual"}],"definition":"Bir kişinin çocuğunun çocuğu, daha dar kullanımda oğlunun oğludur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin çocuğundan doğan çocuk, yani torun adlandırılır."},{"facet_id":"F002","role":"specialization","statement":"Bazı anlatımlarda kapsam özellikle oğlun oğluyla sınırlandırılır."}],"identity_rationale":"Kaynak ifade çıplak biçimin çocuğun çocuğunu, daha dar bir anlatımla oğlun oğlunu gösterdiğinde tutarlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"torun, özellikle oğlun oğlu"}],"lexicalization_note":"Tanım çıplak biçimin torun anlamıyla sınırlıdır; komşu soy terimlerinin daha geniş kapsamı içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ek kuşak, devam eden soy ve soy kolu dalları torun anlamının kuşak ve topluluk sınırlarını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Gönderim aynıdır; odak yalnızca akrabalık ilişkisini verirken komşu torunu önceki çocuğa eklenen yeni kuşak olarak niteler.","focus_only":"Odak dal torunu doğrudan bir akrabalık kuşağı olarak adlandırır.","gloss":"çocuğa eklenen torun","neighbor_only":"Komşu dal torunu, asıl çocuğa eklenen bir fazlalık oluşu bakımından kavramlaştırır.","neighbor_ref":"root_001538/B004","relation_type":"near_synonym","shared_zone":"İki dalın gönderimi çocuğun çocuğu olan torunda örtüşür."},{"boundary_match":"partial","distinction":"Odak tek bir kuşak ilişkisiyle sınırlıdır; komşu çocuklardan başlayıp sonraki kuşaklara uzanan daha geniş bir soy bütününü anlatır.","focus_only":"Odak dal yalnızca çocuğun çocuğunu, kimi kullanımda oğlun oğlunu belirtir.","gloss":"çocuklar ve devam eden soy","neighbor_only":"Komşu dal kişinin çocuklarını, torunlarını ve kendisinden sonra kalan bütün soy çizgisini kapsar.","neighbor_ref":"root_001033/B004","relation_type":"near_synonym","shared_zone":"Torunlar, iki dalın kapsamlarının kesiştiği akrabalık grubudur."},{"boundary_match":"partial","distinction":"Odak yalnızca torunluk derecesidir; komşu bu dereceden bir soy kolu veya topluluk anlamına genişler.","focus_only":"Odak dal bireysel olarak çocuğun çocuğunu adlandırır.","gloss":"torun ve aynı soydan gelen kol","neighbor_only":"Komşu dal torun yanında aynı soydan gelen kolu, topluluğu veya bölümü de adlandırır.","neighbor_ref":"root_000668/B003","relation_type":"near_neighbor","shared_zone":"Çocuğun çocuğu anlamı iki dalda ortak bir gönderim alanıdır."}],"source_phrase_ar":"الوراء ولد الولد (maqayis;sihah;mufradat)؛ الوراء ممدود ولد الولد (ayn)؛ الوراء ابن الابن (tahdhib)","source_summary":"Kaynaklar çocuğun çocuğu anlamında birleşir; daha dar açıklama bunu özellikle oğlun oğlu olarak belirtir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الوراء أو وراء بمعنى ولد الولد أو ابن الابن.","what_is_not_ar":"لا يدخل فيه وراء المكان أو الجهة، ولا الورى الخلق."},"support_links":[]},{"boundary":"Dal yeryüzündeki yaratılmışlar topluluğudur; hastalık, torun ve göreli yer anlamlarıyla yalnızca biçim benzerliği taşır.","branch_kind":"bare","branch_ref":"root_001642/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُورِيَٰت","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:muwriya`t|ROOT:wry|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:1:3","qac_word_ref":"100:2:1","surface_ar":"مُورِيَٰتِ"}],"gloss":"yeryüzündeki bütün yaratılmışlar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yeryüzündeki yaratılmışların bütünü tek bir topluluk olarak gösterilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Topluluğun belirli bir zamanda yeryüzünde bulunan varlıklar olduğu vurgulanabilir."}}],"root_ar":"و ر ي","root_id":"root_001642","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yeryüzünde bulunan yaratılmışlar topluluğunu ayrım yapmadan topluca belirtmek için kullanılır.","boundary_detail":"Dal yeryüzündeki yaratılmışlar topluluğudur; hastalık, torun ve göreli yer anlamlarıyla yalnızca biçim benzerliği taşır.","branch_image_ar":"الورى: الخلق على ظهر الأرض","concept_gloss":"yeryüzündeki bütün yaratılmışlar","contextual_glosses":[{"applicability":"Topluluk adı bağlam içinde yaşayan varlıkların bütünü olarak kullanıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yaratılmışlar kapsamı canlı sayılmayan varlıkları da içeriyorsa onları dışarıda bırakır.","preserves":"Yeryüzünde bulunan varlıkları topluca gösterme değerini korur."},"facet_ids":["F001","F002"],"text":"yeryüzündeki tüm canlılar","usage_role":"contextual"}],"definition":"Belirli bir zamanda yeryüzünde bulunan yaratılmışların tümünü topluca adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yeryüzündeki yaratılmışların bütünü tek bir topluluk olarak gösterilir."},{"facet_id":"F002","role":"specialization","statement":"Topluluğun belirli bir zamanda yeryüzünde bulunan varlıklar olduğu vurgulanabilir."}],"identity_rationale":"Kaynak ifade, yeryüzünde bulunan yaratılmışların veya canlı topluluğunun tümünü gösteren topluluk adını tutarlı biçimde destekler.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"yeryüzündeki yaratılmışlar"}],"lexicalization_note":"Tanım çıplak topluluk adının yeryüzündeki yaratılmışlar anlamıyla sınırlıdır; yaratma eylemi veya yalnız insan türü içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yaratılmışlar, insan türü ve yaratma eylemi dalları topluluğun kapsamını en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Genel kullanımda çok yakındırlar; odak zaman bakımından mevcut topluluğu vurgularken komşunun kapsamı yorumlara göre bütün yaratılmışlar ile iki bilinçli tür arasında değişebilir.","focus_only":"Odak dal, belirli zamanda yeryüzünde bulunan yaratılmışların toplu adıdır.","gloss":"yeryüzündeki bütün varlıklar","neighbor_only":"Komşu dal bütün yaratılmışları kapsayabilir, ancak bazı yorumlarda görünmeyen ve insan türleriyle sınırlandırılır.","neighbor_ref":"root_000061/B001","relation_type":"near_synonym","shared_zone":"Yeryüzündeki yaratılmışların tümünü topluca adlandırma iki dalda büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak tüm yaratılmışları kapsayan üst topluluktur; komşu insan türü ve insan bireyleriyle sınırlı daha dar bir alandır.","focus_only":"Odak dal insanlarla sınırlı olmayıp yeryüzündeki yaratılmışların bütününe uzanır.","gloss":"insanlar ve insan türü","neighbor_only":"Komşu dal özellikle insanı, insan topluluğunu ve insan varlığını adlandırır.","neighbor_ref":"root_000059/B001","relation_type":"near_synonym","shared_zone":"İnsan topluluğu, yeryüzündeki yaratılmışlar bütününün bir parçası olarak iki dalda kesişir."},{"boundary_match":"partial","distinction":"Odak yalnızca ortaya çıkmış topluluğu gösterir; komşu yaratma eylemine ve yaratıcıya uzanan daha geniş bir kavram örgüsüne sahiptir.","focus_only":"Odak dal hazır bulunan yaratılmışlar topluluğunu adlandırır ve yaratma eylemini içermez.","gloss":"yaratma ve yaratılmışlar","neighbor_only":"Komşu dal yaratma eylemini ve yaratıcı adını kapsadığı gibi yaratılmışlar için de bir topluluk adı verir.","neighbor_ref":"root_000099/B001","relation_type":"near_neighbor","shared_zone":"Yaratılmış varlıkların topluca adlandırılması iki dalın kesişim alanıdır."}],"source_phrase_ar":"الورى: الخلق (maqayis;sihah;tahdhib)؛ الورى مقصور الأنام الذي على ظهر الأرض (ayn)؛ الورى الأنام الذين على وجه الأرض في الوقت (mufradat)","source_summary":"Kaynaklar yeryüzündeki yaratılmışların toplu adı üzerinde birleşir; bazı anlatımlar bu topluluğun o anda yeryüzünde bulunan varlıklar olduğunu belirginleştirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الورى بمعنى الخلق أو الأنام الذين على وجه الأرض في الوقت.","what_is_not_ar":"لا يدخل فيه الوري الداء، ولا الوراء ولد الولد، ولا وراء الجهة."},"support_links":[]},{"boundary":"Dal yalnızca sapıklık çakmağından ateş çıkarmaya çalışma söz öbeğidir; başarı, yardım ve gerçek ateş yakma anlamları yüklenmez.","branch_kind":"collocation","branch_ref":"root_001642/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُورِيَٰت","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:muwriya`t|ROOT:wry|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:1:3","qac_word_ref":"100:2:1","surface_ar":"مُورِيَٰتِ"}],"gloss":"sapıklık çakmağından kıvılcım çıkarmaya çalışma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sapıklık, ateş çıkarılması istenen bir çakmak imgesiyle sunulur."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi bu imgesel çakmaktan kıvılcım çıkarmaya çalışır."}}],"root_ar":"و ر ي","root_id":"root_001642","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca tanıklanan sabit söz öbeğinin imgesini yorum eklemeden açıklamak için kullanılır.","boundary_detail":"Dal yalnızca sapıklık çakmağından ateş çıkarmaya çalışma söz öbeğidir; başarı, yardım ve gerçek ateş yakma anlamları yüklenmez.","branch_image_ar":"استيراء زند الضلالة","concept_gloss":"sapıklık çakmağından kıvılcım çıkarmaya çalışma","contextual_glosses":[{"applicability":"Sabit söz öbeği doğal Türkçe içinde açıklayıcı biçimde aktarılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İmgesel çakmağı ve kıvılcım çıkarma girişimini birlikte korur."},"facet_ids":["F001","F002"],"text":"sapıklık çakmağından kıvılcım çıkarmaya çalışıyor","usage_role":"explanatory"}],"definition":"Sapıklığın bir çakmak olarak düşünüldüğü sabit söz öbeğinde, o çakmaktan kıvılcım çıkarmaya çalışmayı anlatır; kaynak bunun ötesinde bir amaç belirtmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sapıklık, ateş çıkarılması istenen bir çakmak imgesiyle sunulur."},{"facet_id":"F002","role":"associated_use","statement":"Kişi bu imgesel çakmaktan kıvılcım çıkarmaya çalışır."}],"identity_rationale":"Kaynak yalnızca sapıklığın bir çakmak gibi tasarlanıp kıvılcımının çıkarılmaya çalışıldığı sabit ifadeyi verir; eylemin daha ileri amacı veya sonucu açıklanmaz. Bu nedenle dal korunur, ancak yorum kıvılcım arama imgesinin ötesine taşınmaz.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"sapıklık çakmağından kıvılcım çıkarmaya çalışıyor"}],"lexicalization_note":"Anlam tek bir sabit söz öbeğine bağlıdır; çıplak biçime veya başka çakmaklı yapılara genellenemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; gerçek ateş çıkarma ile savaşı ateş üzerinden kışkırtma, sabit imgenin sınırını açıklayan iki tematik karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"thematic_only","distinction":"Odakta çakmak sapıklık için kurulmuş bir imgedir ve yapı sabittir; komşuda fiziksel ateş çıkarma ya da ateşi canlandırma gerçek olaydır.","focus_only":"Odak dal sapıklığı çakmak olarak kuran tek bir imgesel söz öbeğidir.","gloss":"gerçek çakmaktan ateş çıkarma","neighbor_only":"Komşu dal gerçek çakmaktan ateş çıkmasını ve sönük ateşin harlanmasını anlatır.","neighbor_ref":"root_001642/B002","relation_type":"thematic","shared_zone":"Çakmaktan ateş veya kıvılcım çıkarma görüntüsü iki dalı tematik olarak birleştirir."},{"boundary_match":"thematic_only","distinction":"Odakta soyut alan sapıklıktır ve sonuç açıklanmaz; komşuda fiziksel ateş hareketi ile savaş kışkırtma arasında açık bir uzantı vardır.","focus_only":"Odak dal, sapıklık çakmağından kıvılcım arayan tek bir sabit ifadeyle sınırlıdır.","gloss":"ateşi canlandırma ve savaşı kışkırtma","neighbor_only":"Komşu dal gerçek ateşi hareketlendirip yakmayı ve bunun üzerinden savaşı kışkırtmayı kapsar.","neighbor_ref":"root_000303/B005","relation_type":"thematic","shared_zone":"Ateş yakma imgesinin soyut bir kötülük veya çatışmaya taşınması iki dalda tematik yakınlık kurar."}],"source_phrase_ar":"فلان يستوري زناد الضلالة","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, sapıklık çakmağından kıvılcım çıkarmaya çalışma imgesini verir ve daha ileri bir anlam çözümlemesi sunmaz."}],"source_summary":"Bu dal tek bir sabit söz öbeğiyle tanıklanır; söz öbeği sapıklığı ateşi aranacak bir çakmak gibi kurar, fakat amacı veya sonucu ayrıca açıklamaz.","sources":["SI"],"what_is_ar":"يدخل فيه التعبير المفرد فلان يستوري زناد الضلالة، حيث تصور الضلالة كزند تطلب ناره.","what_is_not_ar":"لا يدخل فيه نجاح الزند في الطلب، ولا الإعانة، ولا الإيقاد الحسي للنار."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["100:2:1"],"branch_refs":[],"candidate_id":"cand_f247d8c5c112c12df6c5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:2:1:compact-launch","source_type":"word_analysis","support_ids":["sup_609fd566caeb77033662","sup_b82944147129c5b2e088"],"title":"attached connector quickens the beat","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:2:1","qac_refs":["100:2:1:1"],"status":"accepted"}},{"anchor_refs":["100:2:1"],"branch_refs":[],"candidate_id":"cand_1c46142ce81988a54439","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:2:1:oath-chain-momentum","source_type":"word_analysis","support_ids":["sup_609fd566caeb77033662","sup_7f8c637ca927067c7c35"],"title":"the oath becomes a chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:2:1","qac_refs":["100:2:1:1"],"status":"accepted"}},{"anchor_refs":["100:2:1"],"branch_refs":[],"candidate_id":"cand_2825a92d417d17be2571","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:2:1:sequential-causation","source_type":"word_analysis","support_ids":["sup_609fd566caeb77033662","sup_dbc035ec1d60bd9ef77e"],"title":"sequence becomes cause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:2:1","qac_refs":["100:2:1:1"],"status":"accepted"}},{"anchor_refs":["100:2:2"],"branch_refs":[],"candidate_id":"cand_c749fda8a41e6f946566","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001642"],"scope":"focus_ayah","source_local_id":"100:2:2:boundary-transition","source_type":"word_analysis","support_ids":["sup_16f6bdf97d3ede00f272","sup_977f1ed9a30925d7ff44"],"title":"motion becomes visible fire","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:2:2","qac_refs":["100:2:1:2","100:2:1:3"],"status":"accepted"}},{"anchor_refs":["100:2:2"],"branch_refs":[],"candidate_id":"cand_e160ac418f313990e084","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001642"],"scope":"focus_ayah","source_local_id":"100:2:2:caused-oath-beat","source_type":"word_analysis","support_ids":["sup_16f6bdf97d3ede00f272","sup_f99e207092e1660b6b30"],"title":"the participle carries the second oath station","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:2:2","qac_refs":["100:2:1:2","100:2:1:3"],"status":"accepted"}},{"anchor_refs":["100:2:2"],"branch_refs":[],"candidate_id":"cand_c07e178f074abe696aa0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001642"],"scope":"focus_ayah","source_local_id":"100:2:2:hidden-fire-root-pressure","source_type":"word_analysis","support_ids":["sup_13507fbf3cee8b9f940a","sup_16f6bdf97d3ede00f272"],"title":"concealed fire becomes visible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:2:2","qac_refs":["100:2:1:2","100:2:1:3"],"status":"accepted"}},{"anchor_refs":["100:2:2"],"branch_refs":[],"candidate_id":"cand_bbf17ddc2f3904541475","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001642"],"scope":"focus_ayah","source_local_id":"100:2:2:local-pairing-and-cadence","source_type":"word_analysis","support_ids":["sup_16f6bdf97d3ede00f272","sup_4a5e024a1f270f46a0f4"],"title":"long agent form releases into strike","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:2:2","qac_refs":["100:2:1:2","100:2:1:3"],"status":"accepted"}},{"anchor_refs":["100:2:2"],"branch_refs":[],"candidate_id":"cand_c3d1067e469761ed33a1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001642"],"scope":"focus_ayah","source_local_id":"100:2:2:marked-rare-form","source_type":"word_analysis","support_ids":["sup_0b0eefb5db28e3e0bc95","sup_16f6bdf97d3ede00f272"],"title":"rare morphology marks ignition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:2:2","qac_refs":["100:2:1:2","100:2:1:3"],"status":"accepted"}},{"anchor_refs":["100:2:2"],"branch_refs":[],"candidate_id":"cand_05da170b02127eb960fd","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001642"],"scope":"focus_ayah","source_local_id":"100:2:2:substantive-agent-form","source_type":"word_analysis","support_ids":["sup_16f6bdf97d3ede00f272","sup_1bc32833b36341de8279"],"title":"derived form names agents by action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:2:2","qac_refs":["100:2:1:2","100:2:1:3"],"status":"accepted"}},{"anchor_refs":["100:2:2"],"branch_refs":[],"candidate_id":"cand_795fa8d9480c54225ab4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001642"],"scope":"focus_ayah","source_local_id":"100:2:2:variant-sound-pressure","source_type":"word_analysis","support_ids":["sup_16f6bdf97d3ede00f272","sup_2b50322001b3a8651740"],"title":"variant intensifies without replacing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:2:2","qac_refs":["100:2:1:2","100:2:1:3"],"status":"accepted"}},{"anchor_refs":["100:2:3"],"branch_refs":[],"candidate_id":"cand_d091dd4432f9691c17a6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001203"],"scope":"focus_ayah","source_local_id":"100:2:3:accusative-manner","source_type":"word_analysis","support_ids":["sup_27875688d79d9f024b15","sup_36e85e0ecbc52eb1ef0b"],"title":"action noun gives the manner","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:2:3","qac_refs":["100:2:2:1"],"status":"accepted"}},{"anchor_refs":["100:2:3"],"branch_refs":[],"candidate_id":"cand_53eae9eea13fcfe9e44c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001203"],"scope":"focus_ayah","source_local_id":"100:2:3:final-impact-cadence","source_type":"word_analysis","support_ids":["sup_17c1fe86c59b285ba5c8","sup_27875688d79d9f024b15"],"title":"the ayah closes on impact","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:2:3","qac_refs":["100:2:2:1"],"status":"accepted"}},{"anchor_refs":["100:2:3"],"branch_refs":[],"candidate_id":"cand_15bb368d2b154eec3ea5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001203"],"scope":"focus_ayah","source_local_id":"100:2:3:fire-striking-extraction","source_type":"word_analysis","support_ids":["sup_1c884283fa871540ba49","sup_27875688d79d9f024b15"],"title":"impact extracts the spark","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:2:3","qac_refs":["100:2:2:1"],"status":"accepted"}},{"anchor_refs":["100:2:3"],"branch_refs":[],"candidate_id":"cand_3beca04c49ddc379b35a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001203"],"scope":"focus_ayah","source_local_id":"100:2:3:hapax-concentration","source_type":"word_analysis","support_ids":["sup_27875688d79d9f024b15","sup_52a3197148f0a3bfabb8"],"title":"one occurrence bears the load","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:2:3","qac_refs":["100:2:2:1"],"status":"accepted"}},{"anchor_refs":["100:2:3"],"branch_refs":[],"candidate_id":"cand_6524cb300f0935bda355","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001203"],"scope":"focus_ayah","source_local_id":"100:2:3:oath-chain-echo","source_type":"word_analysis","support_ids":["sup_0a3d30fbeed5cce5cb45","sup_27875688d79d9f024b15"],"title":"heat turns into visible spark","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:2:3","qac_refs":["100:2:2:1"],"status":"accepted"}},{"anchor_refs":["100:2:1"],"branch_refs":[],"candidate_id":"cand_c4f692d052ee6f7b7408","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001642"],"scope":"focus_ayah","source_local_id":"100:2:1:3","source_type":"qac_morpheme","support_ids":["sup_d84cb90386283e2cfe7c"],"title":"QAC root occurrence: و ر ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["100:2:2"],"branch_refs":[],"candidate_id":"cand_d8d9a66c3dd456e985bd","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001203"],"scope":"focus_ayah","source_local_id":"100:2:2:1","source_type":"qac_morpheme","support_ids":["sup_e3c0d0b7e8aaac5a7bad"],"title":"QAC root occurrence: ق د ح","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["100:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:2","branch_refs":["root_001203/B001","root_001642/B002"],"candidate_id":"cand_67b2dc4c2b81e967f501","commentary_obligation":"review","hft_ref":"hft_6ad49421f6c0dd6f168c","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:BL-IGNITION","source_type":"hft","support_ids":["sup_8e704e9307a40d0a511d"],"title":"BL-IGNITION","trust":"legacy_unbound"},{"anchor_refs":["100:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:2","branch_refs":["root_001203/B002","root_001642/B005"],"candidate_id":"cand_d72e6b293b6e7b9e90e3","commentary_obligation":"review","hft_ref":"hft_de692e854923f3af170b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:BL-DISCLOSIVE-SCORE","source_type":"hft","support_ids":["sup_abd45b352cfcac0a5a52"],"title":"BL-DISCLOSIVE-SCORE","trust":"legacy_unbound"},{"anchor_refs":["100:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:2","branch_refs":["root_001203/B010","root_001642/B003"],"candidate_id":"cand_5ad8fa83d37710436d66","commentary_obligation":"review","hft_ref":"hft_e5affa543664a06ed11a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:BL-SUCCESSFUL-TAKE","source_type":"hft","support_ids":["sup_e5087cf0eafc7928d3e9"],"title":"BL-SUCCESSFUL-TAKE","trust":"legacy_unbound"},{"anchor_refs":["100:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:2","branch_refs":["root_001203/B004","root_001642/B001"],"candidate_id":"cand_b6fd7a931cd92299499c","commentary_obligation":"review","hft_ref":"hft_c7705be1a4f851b62afe","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:BL-INTERIOR-CORROSION","source_type":"hft","support_ids":["sup_fb18fefa7d46de4bde6c"],"title":"BL-INTERIOR-CORROSION","trust":"legacy_unbound"},{"anchor_refs":["100:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:2","branch_refs":["root_001203/B001","root_001642/B002"],"candidate_id":"cand_1e2df9ee9cd8ac109fdd","commentary_obligation":"review","hft_ref":"hft_a598942c73b5be07b85a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:5.5-high:base_hidden_fire_by_strike","source_type":"hft","support_ids":["sup_7fa24b15fa1a9eac840c"],"title":"base_hidden_fire_by_strike","trust":"legacy_unbound"},{"anchor_refs":["100:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:2","branch_refs":["root_001203/B002","root_001642/B001"],"candidate_id":"cand_20ed608e7980f8340c47","commentary_obligation":"review","hft_ref":"hft_af21e2aa29641cb58974","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:5.5-high:base_wounding_mark","source_type":"hft","support_ids":["sup_8cca43a23df303bfbf15"],"title":"base_wounding_mark","trust":"legacy_unbound"},{"anchor_refs":["100:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:2","branch_refs":["root_001203/B010","root_001642/B003"],"candidate_id":"cand_6b1c0da1b307c065eaf7","commentary_obligation":"review","hft_ref":"hft_3e880b6801961a614a67","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:5.5-high:base_successful_kindling","source_type":"hft","support_ids":["sup_894e12d93de9e07af3e0"],"title":"base_successful_kindling","trust":"legacy_unbound"},{"anchor_refs":["100:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:2","branch_refs":["root_001203/B001","root_001642/B002"],"candidate_id":"cand_51e6c67c379e15c425b7","commentary_obligation":"review","hft_ref":"hft_1ce921cf43585814396b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:5.5-xhigh:bm_impact_ignition","source_type":"hft","support_ids":["sup_20bb3eac7d4e1c042e07"],"title":"bm_impact_ignition","trust":"legacy_unbound"},{"anchor_refs":["100:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:2","branch_refs":["root_001203/B010","root_001642/B003"],"candidate_id":"cand_1f47d9ca9449c0f7c218","commentary_obligation":"review","hft_ref":"hft_51ba9579c8e22b1ad908","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:5.5-xhigh:bm_successful_initiation","source_type":"hft","support_ids":["sup_600ad722dbe3b7fdd23a"],"title":"bm_successful_initiation","trust":"legacy_unbound"},{"anchor_refs":["100:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:2","branch_refs":["root_001203/B002","root_001642/B005"],"candidate_id":"cand_d0e9f665449e155785f1","commentary_obligation":"review","hft_ref":"hft_9c4c3ea2eef1f389c45a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:5.5-xhigh:bm_scored_concealment","source_type":"hft","support_ids":["sup_4663a1f9d53122baeb95"],"title":"bm_scored_concealment","trust":"legacy_unbound"},{"anchor_refs":["100:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:2","branch_refs":["root_001203/B001","root_001642/B002"],"candidate_id":"cand_e5e93d899d5d4dbce459","commentary_obligation":"review","hft_ref":"hft_e67045eee0280e379f48","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:5.6-sol-high:B-IGNITION-01","source_type":"hft","support_ids":["sup_0038997092c3d7f5c042"],"title":"B-IGNITION-01","trust":"legacy_unbound"},{"anchor_refs":["100:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:2","branch_refs":["root_001203/B002","root_001642/B002","root_001642/B005"],"candidate_id":"cand_6b8a123830fdac961a35","commentary_obligation":"review","hft_ref":"hft_33d193d9e530055ef88e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:5.6-sol-high:B-MARK-EXPOSURE-02","source_type":"hft","support_ids":["sup_820492beff1443fb51f3"],"title":"B-MARK-EXPOSURE-02","trust":"legacy_unbound"},{"anchor_refs":["100:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:2","branch_refs":["root_001203/B005","root_001642/B003"],"candidate_id":"cand_ae9d5aa08d3fee718fe0","commentary_obligation":"review","hft_ref":"hft_4ef6e90f1417db718ec7","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:5.6-sol-high:B-YIELD-AID-03","source_type":"hft","support_ids":["sup_8491936c09669d92d8cf"],"title":"B-YIELD-AID-03","trust":"legacy_unbound"},{"anchor_refs":["100:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:2","branch_refs":["root_001203/B004","root_001642/B001"],"candidate_id":"cand_a049af0ff9c8dcc76947","commentary_obligation":"review","hft_ref":"hft_1efeaa14d9eaebc79bc6","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:5.6-sol-high:B-CORROSIVE-04","source_type":"hft","support_ids":["sup_666c11b53573bb907d5a"],"title":"B-CORROSIVE-04","trust":"legacy_unbound"},{"anchor_refs":["100:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:2","branch_refs":["root_001203/B001","root_001642/B002"],"candidate_id":"cand_7274ee5a76dde7e9de19","commentary_obligation":"review","hft_ref":"hft_6d2dc6efc0fafed55911","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:5.6-sol-xhigh:baseline_latent_ignition","source_type":"hft","support_ids":["sup_b1f045d586d5376cba7b"],"title":"baseline_latent_ignition","trust":"legacy_unbound"},{"anchor_refs":["100:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:2","branch_refs":["root_001203/B002","root_001642/B005"],"candidate_id":"cand_7652d264cda10c10e551","commentary_obligation":"review","hft_ref":"hft_d0364e3c4b718825ecae","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:5.6-sol-xhigh:baseline_revealing_score","source_type":"hft","support_ids":["sup_a67ea33db9bc803b54e2"],"title":"baseline_revealing_score","trust":"legacy_unbound"},{"anchor_refs":["100:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:2","branch_refs":["root_001203/B010","root_001642/B003"],"candidate_id":"cand_38f5213e2e84f740cfec","commentary_obligation":"review","hft_ref":"hft_0eb98953e28a3069016f","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:5.6-sol-xhigh:baseline_successful_operation","source_type":"hft","support_ids":["sup_79dd429d524c22e0f1d3"],"title":"baseline_successful_operation","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فَٱلْمُورِيَٰتِ قَدْحًۭا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"100:2:1:1","qac_word_ref":"100:2:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"100:2:1:2","qac_word_ref":"100:2:1","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"مُورِيَٰت","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:muwriya`t|ROOT:wry|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:1:3","qac_word_ref":"100:2:1","root_ar":"و ر ي","surface_ar":"مُورِيَٰتِ"},{"lemma_ar":"قَدْح","morph_features":"STEM|POS:N|LEM:qadoH|ROOT:qdH|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:2:1","qac_word_ref":"100:2:2","root_ar":"ق د ح","surface_ar":"قَدْحًا"}],"word_analysis_qac_refs":[["100:2:1:1"],["100:2:1:2","100:2:1:3"],["100:2:2:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["100:2:1","100:2:2","100:2:3"]},"focus_surface_evidence":{"arabic_uthmani":"فَٱلْمُورِيَٰتِ قَدْحًۭا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"100:2:1:1","qac_word_ref":"100:2:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"100:2:1:2","qac_word_ref":"100:2:1","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"مُورِيَٰت","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:muwriya`t|ROOT:wry|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:1:3","qac_word_ref":"100:2:1","root_ar":"و ر ي","surface_ar":"مُورِيَٰتِ"},{"lemma_ar":"قَدْح","morph_features":"STEM|POS:N|LEM:qadoH|ROOT:qdH|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:2:2:1","qac_word_ref":"100:2:2","root_ar":"ق د ح","surface_ar":"قَدْحًا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["100:2:1:1"],["100:2:1:2","100:2:1:3"],["100:2:2:1"]],"word_analysis_refs":["100:2:1","100:2:2","100:2:3"],"word_rows":[{"analysis_record_ref":"100:2:1","analytic_gloss_range_en":"sequential and resultive connector inside the oath chain; not a flat additive conjunction here","analytic_root_gloss_range_en":null,"qac_refs":["100:2:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"100:2:2","analytic_gloss_range_en":"definite Form IV feminine plural active participle: the agents that cause fire to appear, continuing the oath-chain group without naming it","analytic_root_gloss_range_en":"broad field includes hidden fire emerging, covering or being behind, illness, fullness, and other branches; local Form IV participle selects causative ignition while allowing hidden-fire pressure","qac_refs":["100:2:1:2","100:2:1:3"],"root":{"arabic":"و ر ي","transliteration":"w-r-y"},"surface":{"arabic":"ٱلْمُورِيَٰتِ","transliteration":"al-mūriyāti"}},{"analysis_record_ref":"100:2:3","analytic_gloss_range_en":"indefinite accusative masdar specifying and intensifying the manner of fire-striking","analytic_root_gloss_range_en":"broad range includes striking out fire, scoring or hollowing, impugning, decay, drawing, cups, arrow shafts, and planning; local pairing with the fire-kindling participle selects fire-striking with impact-extraction pressure","qac_refs":["100:2:2:1"],"root":{"arabic":"ق د ح","transliteration":"q-d-ḥ"},"surface":{"arabic":"قَدْحًۭا","transliteration":"qadḥan"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":17,"assigned_records":[{"anchor_refs":["100:2"],"branch_refs":["root_001203/B001","root_001642/B002"],"candidate_id":"cand_67b2dc4c2b81e967f501","evidence_scope":"focus_ayah","hft_ref":"hft_6ad49421f6c0dd6f168c","item_id":"BL-IGNITION","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:BL-IGNITION","support_id":"sup_8e704e9307a40d0a511d"},{"anchor_refs":["100:2"],"branch_refs":["root_001203/B002","root_001642/B005"],"candidate_id":"cand_d72e6b293b6e7b9e90e3","evidence_scope":"focus_ayah","hft_ref":"hft_de692e854923f3af170b","item_id":"BL-DISCLOSIVE-SCORE","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:BL-DISCLOSIVE-SCORE","support_id":"sup_abd45b352cfcac0a5a52"},{"anchor_refs":["100:2"],"branch_refs":["root_001203/B010","root_001642/B003"],"candidate_id":"cand_5ad8fa83d37710436d66","evidence_scope":"focus_ayah","hft_ref":"hft_e5affa543664a06ed11a","item_id":"BL-SUCCESSFUL-TAKE","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:BL-SUCCESSFUL-TAKE","support_id":"sup_e5087cf0eafc7928d3e9"},{"anchor_refs":["100:2"],"branch_refs":["root_001203/B004","root_001642/B001"],"candidate_id":"cand_b6fd7a931cd92299499c","evidence_scope":"focus_ayah","hft_ref":"hft_c7705be1a4f851b62afe","item_id":"BL-INTERIOR-CORROSION","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:BL-INTERIOR-CORROSION","support_id":"sup_fb18fefa7d46de4bde6c"},{"anchor_refs":["100:2"],"branch_refs":["root_001203/B001","root_001642/B002"],"candidate_id":"cand_1e2df9ee9cd8ac109fdd","evidence_scope":"focus_ayah","hft_ref":"hft_a598942c73b5be07b85a","item_id":"base_hidden_fire_by_strike","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a:5.5-high","source_local_id":"reader_hft_a:5.5-high:base_hidden_fire_by_strike","support_id":"sup_7fa24b15fa1a9eac840c"},{"anchor_refs":["100:2"],"branch_refs":["root_001203/B002","root_001642/B001"],"candidate_id":"cand_20ed608e7980f8340c47","evidence_scope":"focus_ayah","hft_ref":"hft_af21e2aa29641cb58974","item_id":"base_wounding_mark","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a:5.5-high","source_local_id":"reader_hft_a:5.5-high:base_wounding_mark","support_id":"sup_8cca43a23df303bfbf15"},{"anchor_refs":["100:2"],"branch_refs":["root_001203/B010","root_001642/B003"],"candidate_id":"cand_6b1c0da1b307c065eaf7","evidence_scope":"focus_ayah","hft_ref":"hft_3e880b6801961a614a67","item_id":"base_successful_kindling","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a:5.5-high","source_local_id":"reader_hft_a:5.5-high:base_successful_kindling","support_id":"sup_894e12d93de9e07af3e0"},{"anchor_refs":["100:2"],"branch_refs":["root_001203/B001","root_001642/B002"],"candidate_id":"cand_51e6c67c379e15c425b7","evidence_scope":"focus_ayah","hft_ref":"hft_1ce921cf43585814396b","item_id":"bm_impact_ignition","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a:5.5-xhigh","source_local_id":"reader_hft_a:5.5-xhigh:bm_impact_ignition","support_id":"sup_20bb3eac7d4e1c042e07"},{"anchor_refs":["100:2"],"branch_refs":["root_001203/B010","root_001642/B003"],"candidate_id":"cand_1f47d9ca9449c0f7c218","evidence_scope":"focus_ayah","hft_ref":"hft_51ba9579c8e22b1ad908","item_id":"bm_successful_initiation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a:5.5-xhigh","source_local_id":"reader_hft_a:5.5-xhigh:bm_successful_initiation","support_id":"sup_600ad722dbe3b7fdd23a"},{"anchor_refs":["100:2"],"branch_refs":["root_001203/B002","root_001642/B005"],"candidate_id":"cand_d0e9f665449e155785f1","evidence_scope":"focus_ayah","hft_ref":"hft_9c4c3ea2eef1f389c45a","item_id":"bm_scored_concealment","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a:5.5-xhigh","source_local_id":"reader_hft_a:5.5-xhigh:bm_scored_concealment","support_id":"sup_4663a1f9d53122baeb95"},{"anchor_refs":["100:2"],"branch_refs":["root_001203/B001","root_001642/B002"],"candidate_id":"cand_e5e93d899d5d4dbce459","evidence_scope":"focus_ayah","hft_ref":"hft_e67045eee0280e379f48","item_id":"B-IGNITION-01","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a:5.6-sol-high","source_local_id":"reader_hft_a:5.6-sol-high:B-IGNITION-01","support_id":"sup_0038997092c3d7f5c042"},{"anchor_refs":["100:2"],"branch_refs":["root_001203/B002","root_001642/B002","root_001642/B005"],"candidate_id":"cand_6b8a123830fdac961a35","evidence_scope":"focus_ayah","hft_ref":"hft_33d193d9e530055ef88e","item_id":"B-MARK-EXPOSURE-02","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a:5.6-sol-high","source_local_id":"reader_hft_a:5.6-sol-high:B-MARK-EXPOSURE-02","support_id":"sup_820492beff1443fb51f3"},{"anchor_refs":["100:2"],"branch_refs":["root_001203/B005","root_001642/B003"],"candidate_id":"cand_ae9d5aa08d3fee718fe0","evidence_scope":"focus_ayah","hft_ref":"hft_4ef6e90f1417db718ec7","item_id":"B-YIELD-AID-03","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a:5.6-sol-high","source_local_id":"reader_hft_a:5.6-sol-high:B-YIELD-AID-03","support_id":"sup_8491936c09669d92d8cf"},{"anchor_refs":["100:2"],"branch_refs":["root_001203/B004","root_001642/B001"],"candidate_id":"cand_a049af0ff9c8dcc76947","evidence_scope":"focus_ayah","hft_ref":"hft_1efeaa14d9eaebc79bc6","item_id":"B-CORROSIVE-04","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a:5.6-sol-high","source_local_id":"reader_hft_a:5.6-sol-high:B-CORROSIVE-04","support_id":"sup_666c11b53573bb907d5a"},{"anchor_refs":["100:2"],"branch_refs":["root_001203/B001","root_001642/B002"],"candidate_id":"cand_7274ee5a76dde7e9de19","evidence_scope":"focus_ayah","hft_ref":"hft_6d2dc6efc0fafed55911","item_id":"baseline_latent_ignition","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a:5.6-sol-xhigh","source_local_id":"reader_hft_a:5.6-sol-xhigh:baseline_latent_ignition","support_id":"sup_b1f045d586d5376cba7b"},{"anchor_refs":["100:2"],"branch_refs":["root_001203/B002","root_001642/B005"],"candidate_id":"cand_7652d264cda10c10e551","evidence_scope":"focus_ayah","hft_ref":"hft_d0364e3c4b718825ecae","item_id":"baseline_revealing_score","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a:5.6-sol-xhigh","source_local_id":"reader_hft_a:5.6-sol-xhigh:baseline_revealing_score","support_id":"sup_a67ea33db9bc803b54e2"},{"anchor_refs":["100:2"],"branch_refs":["root_001203/B010","root_001642/B003"],"candidate_id":"cand_38f5213e2e84f740cfec","evidence_scope":"focus_ayah","hft_ref":"hft_0eb98953e28a3069016f","item_id":"baseline_successful_operation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a:5.6-sol-xhigh","source_local_id":"reader_hft_a:5.6-sol-xhigh:baseline_successful_operation","support_id":"sup_79dd429d524c22e0f1d3"}],"diagnostics":[{"warning":"Unrecognized HFT reader field is preserved as a global review record"},{"warning":"Unrecognized HFT reader field is preserved as a global review record"},{"warning":"Unrecognized HFT reader field is preserved as a global review record"},{"warning":"Unrecognized HFT reader field is preserved as a global review record"},{"warning":"Unrecognized HFT reader field is preserved as a global review record"},{"warning":"Unrecognized HFT reader field is preserved as a global review record"}],"lane_counts":{"global":49,"macro":54,"micro":17},"packet_summary":{"ayah_count":11,"focus_ref":"100:2","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ع د و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000993","furuq_root_norm":"ع د و","furuq_source_root_norm":"ع د و","is_dominant":true,"target_occurrences":68,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":5,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":false,"target_occurrences":4,"target_rank":3}]},{"qac_root":"ث و ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000210","furuq_root_norm":"ث و ر","furuq_source_root_norm":"ث و ر","is_dominant":true,"target_occurrences":4,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000011","furuq_root_norm":"ء ث ر","furuq_source_root_norm":"أ ث ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["100:1","100:2","100:3","100:4","100:5","100:6","100:7","100:8","100:9","100:10","100:11"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"100:2","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v3","reader_id":"reader_hft_a","trace_kind":null},{"focus_ref":"100:2","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v3","reader_id":"reader_hft_a:5.5-high","trace_kind":null},{"focus_ref":"100:2","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a:5.5-xhigh","trace_kind":"reconstructed"},{"focus_ref":"100:2","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v3","reader_id":"reader_hft_a:5.6-sol-high","trace_kind":null},{"focus_ref":"100:2","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a:5.6-sol-xhigh","trace_kind":"reconstructed"}]},"reader_synthesis_count":43,"source_present":true,"structured_insight_count":71,"unstructured_record_count":6},"identity":{"ayah_ref":"100:2","lane":"micro","linguistic_source_ref":"100:2","surface_ref":"100:2","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"100:2","target_tokens":[["Ardından",["100:2:1"]],["çakarak",["100:2:2"]],["kıvılcım",["100:2:1","100:2:2"]],["çıkaranlara",["100:2:1"]]],"text":"Ardından çakarak kıvılcım çıkaranlara,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":17,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":11,"id":"s100-p01-001-011","label":"Whole surah","number":1,"refs":["100:1","100:2","100:3","100:4","100:5","100:6","100:7","100:8","100:9","100:10","100:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:2:3:oath-chain-echo","source_type":"word_analysis","support_id":"sup_0a3d30fbeed5cce5cb45","text":"{\"blocking_evidence\":null,\"headline\":\"heat turns into visible spark\",\"reader_payoff\":\"The reader notices that the previous hot-breath beat develops into visible spark-striking here, while the same accusative action slot keeps the oath sequence linked.\",\"reason\":\"The supplied context window supports reading this word within the oath chain from 100:1, and the local masdar slot preserves the action-complement pattern.\",\"representative_source_ids\":[\"QI-52ad86c7\",\"QE-8358c998\",\"QB-b1a2cc12\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:2:2:marked-rare-form","source_type":"word_analysis","support_id":"sup_0b0eefb5db28e3e0bc95","text":"{\"blocking_evidence\":null,\"headline\":\"rare morphology marks ignition\",\"reader_payoff\":\"The reader notices that the markedness falls on this specific agent-form, making causative ignition the selected oath image.\",\"reason\":\"The contextual profile marks this exact root-form as a one-instance item, while the local grammar confirms the rare definite feminine plural active participle.\",\"representative_source_ids\":[\"QI-fc05be28\",\"QH-9b665f92\",\"QY-0b0fee10\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:2:2:hidden-fire-root-pressure","source_type":"word_analysis","support_id":"sup_13507fbf3cee8b9f940a","text":"{\"blocking_evidence\":null,\"headline\":\"concealed fire becomes visible\",\"reader_payoff\":\"The reader notices that the ignition is not generic brightness; it is fire drawn out from what had been hidden.\",\"reason\":\"V4 supports a hidden-fire branch for {{ar:و ر ي}} ({{tr:w-r-y}}), and QAC selects Form IV causative ignition; wider branches such as illness, fullness, far-side location, and scripture associations are not local sense activations.\",\"representative_source_ids\":[\"QS-5843c374\",\"QS-836e8e5a\",\"MH-13a26a2b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:2:2","source_type":"word_analysis","support_id":"sup_16f6bdf97d3ede00f272","text":"{\"gloss_range\":\"definite Form IV feminine plural active participle: the agents that cause fire to appear, continuing the oath-chain group without naming it\",\"prose\":\"{{ar:ٱلْمُورِيَٰتِ}} ({{tr:al-mūriyāti}}) is a definite Form IV feminine plural active participle, so the oath does not name horses or another referent directly; it presents the same unnamed group by what they now do, causing fire to appear. That morphology continues the preceding agent pattern while the initial {{ar:فَ}} ({{tr:fa}}) places the word under the chain of consequence, making it the second station in the participial oath sequence. The root field is locally narrowed to causative ignition, but its hidden-fire branch gives the image a sharper payoff: energy that was concealed in motion or material becomes visible when {{ar:قَدْحًۭا}} ({{tr:qadḥan}}) supplies the striking manner. The form is also marked as this specific agent-shape within the supplied root distribution, so causative fire-production is not a generic root fact but the selected oath image. The long participial form then stretches before the clipped final action noun, making the two-word beat feel like sustained motion releasing into impact. The reported intensified variant {{ar:المُورِيَاتِ}} ({{tr:al-mūriyyāti}}) can be kept as an apparatus-level sound pressure, but it does not replace the local canonical form. The fire image remains transitional as well: the spark flashes before the dawn-raiding beat that follows (100:3).\",\"root_display\":\"{{ar:و ر ي}} ({{tr:w-r-y}})\",\"root_gloss_range\":\"broad field includes hidden fire emerging, covering or being behind, illness, fullness, and other branches; local Form IV participle selects causative ignition while allowing hidden-fire pressure\",\"surface_display\":\"{{ar:ٱلْمُورِيَٰتِ}} ({{tr:al-mūriyāti}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:2:3:final-impact-cadence","source_type":"word_analysis","support_id":"sup_17c1fe86c59b285ba5c8","text":"{\"blocking_evidence\":null,\"headline\":\"the ayah closes on impact\",\"reader_payoff\":\"The reader notices that the final word makes the oath beat land as a sharp striking sound and image.\",\"reason\":\"The word is the final indefinite accusative masdar of the ayah, and the CRITICAL sound observations are compatible with its hard consonantal surface and impact meaning.\",\"representative_source_ids\":[\"QF-32c2e369\",\"QT-8090e74c\",\"QP-c88ea253\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:2:2:substantive-agent-form","source_type":"word_analysis","support_id":"sup_1bc32833b36341de8279","text":"{\"blocking_evidence\":null,\"headline\":\"derived form names agents by action\",\"reader_payoff\":\"The reader notices that the oath identifies the group through fire-producing agency while leaving the exact referent unnamed.\",\"reason\":\"QAC identifies the word as a definite Form IV feminine plural active participle, supporting the rows about substantive agency and implicit referent continuity.\",\"representative_source_ids\":[\"QG-4f997335\",\"QF-b445d1bf\",\"QB-520e5d71\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:2:3:fire-striking-extraction","source_type":"word_analysis","support_id":"sup_1c884283fa871540ba49","text":"{\"blocking_evidence\":null,\"headline\":\"impact extracts the spark\",\"reader_payoff\":\"The reader notices that the spark is pictured as forced out by impact, not as effortless light.\",\"reason\":\"V4 accepts the fire-striking branch and related physical branches for {{ar:ق د ح}} ({{tr:q-d-ḥ}}), but the local pairing with the ignition participle selects fire-striking; lot-drawing or destiny implications are not locally licensed.\",\"representative_source_ids\":[\"QS-bb24df82\",\"QS-d3c981aa\",\"MH-1a47f9c0\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:2:3","source_type":"word_analysis","support_id":"sup_27875688d79d9f024b15","text":"{\"gloss_range\":\"indefinite accusative masdar specifying and intensifying the manner of fire-striking\",\"prose\":\"{{ar:قَدْحًۭا}} ({{tr:qadḥan}}) is the accusative verbal noun that tells how {{ar:ٱلْمُورِيَٰتِ}} ({{tr:al-mūriyāti}}) produce fire. It is dependent on the active participle, so agency and action are compressed into a two-word oath image rather than spread through a finite clause. The local sense is fire-striking, and the wider root field is narrowed to that branch; still, the accepted related images of scoring, hollowing, and shaping help the reader feel the spark as something extracted by force from resistant material. Its indefiniteness and final position also matter: the ayah does not close on the agents but on an unbounded striking event, a clipped impact after the longer participle. Within the oath-chain action series, the prior hot-breath beat develops into visible spark-striking (100:1), and this same short accusative action slot points onward toward dawn visibility (100:3). Because the root occurs here as a one-instance Quranic presence, the local pairing, hard sound, extraction semantics, and final placement carry the word's interpretive weight together.\",\"root_display\":\"{{ar:ق د ح}} ({{tr:q-d-ḥ}})\",\"root_gloss_range\":\"broad range includes striking out fire, scoring or hollowing, impugning, decay, drawing, cups, arrow shafts, and planning; local pairing with the fire-kindling participle selects fire-striking with impact-extraction pressure\",\"surface_display\":\"{{ar:قَدْحًۭا}} ({{tr:qadḥan}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:2:2:variant-sound-pressure","source_type":"word_analysis","support_id":"sup_2b50322001b3a8651740","text":"{\"blocking_evidence\":null,\"headline\":\"variant intensifies without replacing\",\"reader_payoff\":\"The reader notices that the reported intensified recitation can reinforce ignition pressure as sound, while the local analysis stays with the canonical surface.\",\"reason\":\"The variant supports an apparatus-level phonetic observation, but QAC alignment and local display remain with {{ar:ٱلْمُورِيَٰتِ}} ({{tr:al-mūriyāti}}).\",\"representative_source_ids\":[\"QF-de7b3b70\",\"QP-297ce3ab\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:2:3:accusative-manner","source_type":"word_analysis","support_id":"sup_36e85e0ecbc52eb1ef0b","text":"{\"blocking_evidence\":null,\"headline\":\"action noun gives the manner\",\"reader_payoff\":\"The reader notices that the word is not a separate object; it is the striking manner by which the agents cause fire to appear.\",\"reason\":\"QAC calls the word an indefinite accusative masdar functioning as emphatic manner, and attachment evidence makes it circumstantial under {{ar:ٱلْمُورِيَٰتِ}} ({{tr:al-mūriyāti}}).\",\"representative_source_ids\":[\"QG-349dd77c\",\"QG-efd8a29d\",\"QS-254fc636\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:2:2:local-pairing-and-cadence","source_type":"word_analysis","support_id":"sup_4a5e024a1f270f46a0f4","text":"{\"blocking_evidence\":null,\"headline\":\"long agent form releases into strike\",\"reader_payoff\":\"The reader notices the order and sound: the agents are sustained first, then their means of ignition lands as the final strike.\",\"reason\":\"Attachment evidence makes {{ar:قَدْحًۭا}} ({{tr:qadḥan}}) the manner expression governed by this participle, preserving the local agent-before-action pairing.\",\"representative_source_ids\":[\"QT-9671d17b\",\"QE-a6d97819\",\"QP-8918b4ca\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:2:3:hapax-concentration","source_type":"word_analysis","support_id":"sup_52a3197148f0a3bfabb8","text":"{\"blocking_evidence\":null,\"headline\":\"one occurrence bears the load\",\"reader_payoff\":\"The reader notices that this single Quranic occurrence has to draw its force from local grammar, sound, lexicon, and position at once.\",\"reason\":\"The contextual profile marks the exact root-form as one occurrence and the collocation profile places its whole local relation with {{ar:ٱلْمُورِيَٰتِ}} ({{tr:al-mūriyāti}}).\",\"representative_source_ids\":[\"QI-6c163495\",\"QH-536c1c51\",\"QY-85c101ba\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:2:1","source_type":"word_analysis","support_id":"sup_609fd566caeb77033662","text":"{\"gloss_range\":\"sequential and resultive connector inside the oath chain; not a flat additive conjunction here\",\"prose\":\"{{ar:فَ}} ({{tr:fa}}) makes 100:2 arrive as immediate consequence, not as a fresh item loosely added to the oath list. The particle carries both sequence and result: the previous running becomes the condition from which the spark-making beat follows. Its attached, one-syllable surface also matters; the connector is heard almost as a quick pickup into {{ar:ٱلْمُورِيَٰتِ}} ({{tr:al-mūriyāti}}), so continuation and causation are compressed before the fire image even appears. Because the same connector pattern carries the next oath beats, this first reprise helps turn the opening oath into a kinetic chain rather than a set of static witnesses: running produces sparking (100:2), then the movement continues into dawn-raiding (100:3), dust-raising (100:4), and entering the center (100:5).\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:2:1:oath-chain-momentum","source_type":"word_analysis","support_id":"sup_7f8c637ca927067c7c35","text":"{\"blocking_evidence\":null,\"headline\":\"the oath becomes a chain\",\"reader_payoff\":\"The reader notices that the repeated connector pattern turns the opening oath sequence into escalating movement rather than a flat catalogue.\",\"reason\":\"The local particle opens the second oath beat and is explicitly warned by translation support against flattening into simple addition.\",\"representative_source_ids\":[\"MG-b5bcb561\",\"QT-d4e2ba10\",\"QE-6c03d23a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:2:2:boundary-transition","source_type":"word_analysis","support_id":"sup_977f1ed9a30925d7ff44","text":"{\"blocking_evidence\":null,\"headline\":\"motion becomes visible fire\",\"reader_payoff\":\"The reader notices that the running energy from 100:1 turns into visible fire here and points forward toward the next dawn beat.\",\"reason\":\"Translation support preserves the context window from the previous oath beat, and the participle's causative ignition allows the boundary rows to survive without naming an explicit referent.\",\"representative_source_ids\":[\"QB-5d70e215\",\"QB-bada5d80\",\"QB-8b3669df\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:2:1:compact-launch","source_type":"word_analysis","support_id":"sup_b82944147129c5b2e088","text":"{\"blocking_evidence\":null,\"headline\":\"attached connector quickens the beat\",\"reader_payoff\":\"The reader notices that the transition is visibly and audibly compact before the longer ignition word begins.\",\"reason\":\"The particle is a proclitic at the opening of 100:2 and runs into the following definite participle, so the rows about compressed transition and audible liaison are locally coherent.\",\"representative_source_ids\":[\"QF-a85a235a\",\"QT-bf798f2b\",\"QP-f9fdefb6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"100:2:1:3","source_type":"qac_morpheme","support_id":"sup_d84cb90386283e2cfe7c","text":"{\"lemma_ar\":\"مُورِيَٰت\",\"morph_features\":\"STEM|POS:N|ACT|PCPL|(IV)|LEM:muwriya`t|ROOT:wry|FP|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"100:2:1:3\",\"qac_word_ref\":\"100:2:1\",\"root_ar\":\"و ر ي\",\"surface_ar\":\"مُورِيَٰتِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:2:1:sequential-causation","source_type":"word_analysis","support_id":"sup_dbc035ec1d60bd9ef77e","text":"{\"blocking_evidence\":null,\"headline\":\"sequence becomes cause\",\"reader_payoff\":\"The reader notices that the sparks are grammatically produced by the prior rushing motion, not merely listed after it.\",\"reason\":\"QAC and translation-support evidence identify {{ar:فَ}} ({{tr:fa}}) as sequential and connected to the previous oath clause, supporting the CRITICAL claim that the second beat follows as result.\",\"representative_source_ids\":[\"QG-e9425b7f\",\"QS-71a1e90b\",\"QB-aa9da0e3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"100:2:2:1","source_type":"qac_morpheme","support_id":"sup_e3c0d0b7e8aaac5a7bad","text":"{\"lemma_ar\":\"قَدْح\",\"morph_features\":\"STEM|POS:N|LEM:qadoH|ROOT:qdH|M|INDEF|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"100:2:2:1\",\"qac_word_ref\":\"100:2:2\",\"root_ar\":\"ق د ح\",\"surface_ar\":\"قَدْحًا\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:2:2:caused-oath-beat","source_type":"word_analysis","support_id":"sup_f99e207092e1660b6b30","text":"{\"blocking_evidence\":null,\"headline\":\"the participle carries the second oath station\",\"reader_payoff\":\"The reader notices that this word is the second station in a chained participial oath pattern, not a free-standing label.\",\"reason\":\"The preceding connector scopes the participial unit, and the following accusative manner expression depends on this word, so the participle is load-bearing in the oath beat.\",\"representative_source_ids\":[\"QG-7391118a\",\"QI-d842c639\",\"QE-0a42b162\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُورِيَٰتِ قَدْحًۭا","ayah_ref":"100:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001203/B001","root_001642/B002"],"payload":{"activation_trace":[{"assigned_role":"Supplies the concealed potential and its emergence.","branch_id":"B002","branch_image_ar":"نار كامنة تخرج من الزند","literal_contribution":"A fire is latent in the fire-stick and comes out.","mapped_root_id":"root_001642","mapped_root_norm":"و ر ي","root":"و ر ي","source_phrase_ar":"مُورِيَٰتِ","source_ref":"100:2"},{"assigned_role":"Supplies the physical operation that releases the latent fire.","branch_id":"B001","branch_image_ar":"إيراء النار بالقدح","literal_contribution":"Fire is struck or kindled from a stick, stone, or implement.","mapped_root_id":"root_001203","mapped_root_norm":"ق د ح","root":"ق د ح","source_phrase_ar":"قَدْحًا","source_ref":"100:2"}],"changed_reading":{"after":"The agents are defined by converting repeated contact into the appearance of a fire that was present but inaccessible.","before":"A generic scene of fire-making."},"confidence":"strong","focus_anchor":"مُورِيَٰتِ from و ر ي and the manner/result accusative قَدْحًا from ق د ح.","mechanism":"Plural agents apply contact that makes a previously hidden fire emerge; the second word specifies the striking operation rather than merely adding a second fire image.","model_id":"BL-IGNITION","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:BL-IGNITION","source_type":"hft","support_id":"sup_8e704e9307a40d0a511d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُورِيَٰتِ قَدْحًۭا","ayah_ref":"100:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001203/B002","root_001642/B005"],"payload":{"activation_trace":[{"assigned_role":"Makes concealment the initial state acted upon.","branch_id":"B005","branch_image_ar":"ستر الشيء وجعله وراء الظهور","literal_contribution":"A thing is covered and placed out of sight.","mapped_root_id":"root_001642","mapped_root_norm":"و ر ي","root":"و ر ي","source_phrase_ar":"مُورِيَٰتِ","source_ref":"100:2"},{"assigned_role":"Makes the releasing contact leave a material wound or trace.","branch_id":"B002","branch_image_ar":"نقر الشيء وعيبه","literal_contribution":"A physical thing is scored, bored, split, or marked.","mapped_root_id":"root_001203","mapped_root_norm":"ق د ح","root":"ق د ح","source_phrase_ar":"قَدْحًا","source_ref":"100:2"}],"changed_reading":{"after":"The spark is a disclosure event produced by breaching a cover, while the scored substrate preserves evidence of the contact.","before":"The spark is only a bright product."},"confidence":"medium","focus_anchor":"The causative force of مُورِيَٰتِ and the material-contact range of قَدْحًا.","mechanism":"The strike is also a breach: it scores a covering surface, and the brief emission is evidence that something hidden lay behind it. Light and damage coexist rather than cancel one another.","model_id":"BL-DISCLOSIVE-SCORE","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:BL-DISCLOSIVE-SCORE","source_type":"hft","support_id":"sup_abd45b352cfcac0a5a52","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُورِيَٰتِ قَدْحًۭا","ayah_ref":"100:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001203/B010","root_001642/B003"],"payload":{"activation_trace":[{"assigned_role":"Transfers ignition into enabled success without losing the focus root.","branch_id":"B003","branch_image_ar":"زند يقدح نجاحا أو نصرة","literal_contribution":"A fire-stick taking can image success, aid, counsel, or defense.","mapped_root_id":"root_001642","mapped_root_norm":"و ر ي","root":"و ر ي","source_phrase_ar":"مُورِيَٰتِ","source_ref":"100:2"},{"assigned_role":"Supplies deliberate probing as the means by which the affair takes.","branch_id":"B010","branch_image_ar":"اقتداح الأمر بالنظر والتدبير","literal_contribution":"An affair is examined and planned.","mapped_root_id":"root_001203","mapped_root_norm":"ق د ح","root":"ق د ح","source_phrase_ar":"قَدْحًا","source_ref":"100:2"}],"changed_reading":{"after":"Agents make a difficult possibility take through planned probing, aid, and successful activation.","before":"Agents mechanically strike an implement."},"confidence":"exploratory","focus_anchor":"مُورِيَٰتِ retains the fire-stick idiom of taking successfully, while قَدْحًا can describe working an affair out by consideration.","mechanism":"The physical catching of fire supports an operational analogy: deliberate probing makes an undertaking catch, and aid converts an inert possibility into effective action.","model_id":"BL-SUCCESSFUL-TAKE","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:BL-SUCCESSFUL-TAKE","source_type":"hft","support_id":"sup_e5087cf0eafc7928d3e9","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُورِيَٰتِ قَدْحًۭا","ayah_ref":"100:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001203/B004","root_001642/B001"],"payload":{"activation_trace":[{"assigned_role":"Places the consequential process inside rather than at the visible surface.","branch_id":"B001","branch_image_ar":"داء يأكل الجوف أو يصيب الرئة","literal_contribution":"An illness eats into the belly or affects the lung.","mapped_root_id":"root_001642","mapped_root_norm":"و ر ي","root":"و ر ي","source_phrase_ar":"مُورِيَٰتِ","source_ref":"100:2"},{"assigned_role":"Provides a material analogue for hidden deterioration revealed by a mark.","branch_id":"B004","branch_image_ar":"أكال الشجر والسن","literal_contribution":"Decay eats wood or teeth from within.","mapped_root_id":"root_001203","mapped_root_norm":"ق د ح","root":"ق د ح","source_phrase_ar":"قَدْحًا","source_ref":"100:2"}],"changed_reading":{"after":"A visible surface event can be the symptom of an unseen consuming process, so brightness does not guarantee health or benefit.","before":"A clean, productive flash."},"confidence":"exploratory","focus_anchor":"Form-distant but packet-attested branches of both و ر ي and ق د ح converge on an eating process inside a body or material.","mechanism":"Instead of treating every emission as healthy ignition, the focus can carry a diagnostic shadow: surface scoring may disclose a process already consuming the inside.","model_id":"BL-INTERIOR-CORROSION","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:BL-INTERIOR-CORROSION","source_type":"hft","support_id":"sup_fb18fefa7d46de4bde6c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُورِيَٰتِ قَدْحًۭا","ayah_ref":"100:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001203/B001","root_001642/B002"],"payload":{"activation_trace":[{"assigned_role":"Supplies the hidden combustible content.","branch_id":"B002","branch_image_ar":"نار كامنة تخرج من الزند","literal_contribution":"Latent fire in a fire-stick becomes visible.","mapped_root_id":"root_001642","mapped_root_norm":"و ر ي","root":"و ر ي","source_phrase_ar":"مُورِيَٰتِ","source_ref":"100:2"},{"assigned_role":"Supplies the causal trigger that extracts the fire.","branch_id":"B001","branch_image_ar":"إيراء النار بالقدح","literal_contribution":"Striking produces ignition.","mapped_root_id":"root_001203","mapped_root_norm":"ق د ح","root":"ق د ح","source_phrase_ar":"قَدْحًا","source_ref":"100:2"}],"changed_reading":{"after":"A process-image: latent force is locked inside matter and becomes visible only through impact.","before":"A simple oath-image: spark-makers striking sparks."},"confidence":"strong","focus_anchor":"فَٱلْمُورِيَٰتِ قَدْحًا: مُورِيَٰتِ from و ر ي and قَدْحًا from ق د ح.","mechanism":"A hidden fire is made manifest by a forceful strike; the participle names agents whose action draws latent flame out of resistant matter.","model_id":"base_hidden_fire_by_strike","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:5.5-high:base_hidden_fire_by_strike","source_type":"hft","support_id":"sup_7fa24b15fa1a9eac840c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُورِيَٰتِ قَدْحًۭا","ayah_ref":"100:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001203/B002","root_001642/B001"],"payload":{"activation_trace":[{"assigned_role":"Recasts the spark as a wound-mark rather than pure light.","branch_id":"B002","branch_image_ar":"نقر الشيء وعيبه","literal_contribution":"The act of striking can score or flaw a thing.","mapped_root_id":"root_001203","mapped_root_norm":"ق د ح","root":"ق د ح","source_phrase_ar":"قَدْحًا","source_ref":"100:2"},{"assigned_role":"Lets the struck sign point inward, toward hidden damage.","branch_id":"B001","branch_image_ar":"داء يأكل الجوف أو يصيب الرئة","literal_contribution":"The root can name an inward injury or eating disease.","mapped_root_id":"root_001642","mapped_root_norm":"و ر ي","root":"و ر ي","source_phrase_ar":"مُورِيَٰتِ","source_ref":"100:2"}],"changed_reading":{"after":"The line can also show impact leaving a diagnostic wound: light appears as the surface evidence of inner harm.","before":"The line shows bright sparks thrown off by motion."},"confidence":"medium","focus_anchor":"قَدْحًا can be flawing/scoring, while مُورِيَٰتِ keeps an interior hiddenness beside its fire sense.","mechanism":"The strike may not merely illuminate; it may score, puncture, or blemish the struck surface, making the spark a visible sign of damage.","model_id":"base_wounding_mark","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:5.5-high:base_wounding_mark","source_type":"hft","support_id":"sup_8cca43a23df303bfbf15","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُورِيَٰتِ قَدْحًۭا","ayah_ref":"100:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001203/B010","root_001642/B003"],"payload":{"activation_trace":[{"assigned_role":"Turns ignition into achieved intent.","branch_id":"B003","branch_image_ar":"زند يقدح نجاحا أو نصرة","literal_contribution":"A fire-stick that takes can signify success, aid, or defense.","mapped_root_id":"root_001642","mapped_root_norm":"و ر ي","root":"و ر ي","source_phrase_ar":"مُورِيَٰتِ","source_ref":"100:2"},{"assigned_role":"Adds deliberation behind the physical strike.","branch_id":"B010","branch_image_ar":"اقتداح الأمر بالنظر والتدبير","literal_contribution":"An affair is examined and planned.","mapped_root_id":"root_001203","mapped_root_norm":"ق د ح","root":"ق د ح","source_phrase_ar":"قَدْحًا","source_ref":"100:2"}],"changed_reading":{"after":"Spark-making becomes a figure for an undertaking made to catch: impact plus planning yields result.","before":"Spark-making is a raw sensory event."},"confidence":"exploratory","focus_anchor":"مُورِيَٰتِ and قَدْحًا together invite fire-stick idioms of success and deliberate undertaking.","mechanism":"A fire-stick that catches becomes a model for achieving an intended result; the strike is an act of considering, testing, and making an enterprise take.","model_id":"base_successful_kindling","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:5.5-high:base_successful_kindling","source_type":"hft","support_id":"sup_894e12d93de9e07af3e0","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُورِيَٰتِ قَدْحًۭا","ayah_ref":"100:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001203/B001","root_001642/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001642","role":"Concealed fire inside a fire-tool supplies the latent energy carried by word 1.","root":"و ر ي","source_ref":"100:2","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001203","role":"Striking fire out supplies the impact that turns latent energy into visible flash.","root":"ق د ح","source_ref":"100:2","source_word_indices":["2"]}],"changed_reading":{"after":"The focus line is a compact causality scene: hidden energy becomes visible at the instant of impact.","before":"A bare oath by spark-making agents."},"confidence":"strong","focus_anchor":"100:2 word 1 root و ر ي joined to word 2 root ق د ح.","mechanism":"The focus-only reading is a two-part ignition machine: latent fire is present but unseen, and impact makes it appear.","model_id":"bm_impact_ignition"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:5.5-xhigh:bm_impact_ignition","source_type":"hft","support_id":"sup_20bb3eac7d4e1c042e07","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُورِيَٰتِ قَدْحًۭا","ayah_ref":"100:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001203/B010","root_001642/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001642","role":"A fire-tool that takes successfully turns word 1 into achieved activation rather than mere light.","root":"و ر ي","source_ref":"100:2","source_word_indices":["1"]},{"branch_id":"B010","mapped_root_id":"root_001203","role":"Considering and managing an affair lets the strike function as deliberate initiation.","root":"ق د ح","source_ref":"100:2","source_word_indices":["2"]}],"changed_reading":{"after":"The line can also signal successful launch: the action catches and becomes operational.","before":"The line reports a physical spark."},"confidence":"medium","focus_anchor":"100:2 word 1 as successful kindling or aid, plus word 2 as purposeful striking or planning.","mechanism":"The focus roots allow ignition to mean effective activation: an intended action catches, succeeds, and begins to work.","model_id":"bm_successful_initiation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:5.5-xhigh:bm_successful_initiation","source_type":"hft","support_id":"sup_600ad722dbe3b7fdd23a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُورِيَٰتِ قَدْحًۭا","ayah_ref":"100:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001203/B002","root_001642/B005"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_001642","role":"Covering and concealment supply the hidden layer from which the reading starts.","root":"و ر ي","source_ref":"100:2","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001203","role":"Scoring or flawing a thing supplies the breach that makes concealed material vulnerable.","root":"ق د ح","source_ref":"100:2","source_word_indices":["2"]}],"changed_reading":{"after":"Ignition also becomes incision: the focus line can mark the first damaging opening of what was covered.","before":"Ignition is clean flash."},"confidence":"exploratory","focus_anchor":"100:2 word 1 can carry covering or hiddenness, while word 2 can carry scoring, boring, or flawing.","mechanism":"A second focus-only model treats the blow as a breach in a cover: what matters is not flame alone but a surface being marked open.","model_id":"bm_scored_concealment"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:5.5-xhigh:bm_scored_concealment","source_type":"hft","support_id":"sup_4663a1f9d53122baeb95","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُورِيَٰتِ قَدْحًۭا","ayah_ref":"100:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001203/B001","root_001642/B002"],"payload":{"activation_trace":[{"assigned_role":"Supplies the latent state and the emergence event.","branch_id":"B002","branch_image_ar":"نار كامنة تخرج من الزند","literal_contribution":"A fire is already potential inside the fire-stick and comes out.","mapped_root_id":"root_001642","mapped_root_norm":"و ر ي","root":"و ر ي","source_phrase_ar":"مُورِيَٰتِ","source_ref":"100:2"},{"assigned_role":"Supplies the enabling contact that releases the latent fire.","branch_id":"B001","branch_image_ar":"إيراء النار بالقدح","literal_contribution":"Fire is elicited through striking.","mapped_root_id":"root_001203","mapped_root_norm":"ق د ح","root":"ق د ح","source_phrase_ar":"قَدْحًا","source_ref":"100:2"}],"changed_reading":{"after":"Agents whose forceful contact converts hidden potential into a visible, active event.","before":"Agents that simply emit sparks."},"confidence":"strong","focus_anchor":"The participle مُورِيَٰتِ (و ر ي) is followed by the cognate-like action specification قَدْحًا (ق د ح): agents make something latent catch by striking.","mechanism":"Contact is not merely luminous description. A blow or frictional act supplies the condition under which hidden fire crosses from latency into visibility.","model_id":"B-IGNITION-01","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:5.6-sol-high:B-IGNITION-01","source_type":"hft","support_id":"sup_0038997092c3d7f5c042","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُورِيَٰتِ قَدْحًۭا","ayah_ref":"100:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001203/B002","root_001642/B002","root_001642/B005"],"payload":{"activation_trace":[{"assigned_role":"Supplies the concealed side of the reveal mechanism.","branch_id":"B005","branch_image_ar":"ستر الشيء وجعله وراء الظهور","literal_contribution":"Something is covered and placed behind appearance.","mapped_root_id":"root_001642","mapped_root_norm":"و ر ي","root":"و ر ي","source_phrase_ar":"مُورِيَٰتِ","source_ref":"100:2"},{"assigned_role":"Supplies the surface-changing mark that breaches concealment.","branch_id":"B002","branch_image_ar":"نقر الشيء وعيبه","literal_contribution":"A thing is scored, split, or visibly flawed.","mapped_root_id":"root_001203","mapped_root_norm":"ق د ح","root":"ق د ح","source_phrase_ar":"قَدْحًا","source_ref":"100:2"},{"assigned_role":"Provides the focus-internal precedent for emergence from latency.","branch_id":"B002","branch_image_ar":"نار كامنة تخرج من الزند","literal_contribution":"A hidden content becomes manifest under impact.","mapped_root_id":"root_001642","mapped_root_norm":"و ر ي","root":"و ر ي","source_phrase_ar":"مُورِيَٰتِ","source_ref":"100:2"}],"changed_reading":{"after":"A contact-event that writes a mark on a cover and makes a concealed interior legible.","before":"A flash produced on contact."},"confidence":"medium","focus_anchor":"قَدْحًا can image scoring or flawing a surface, while the same root inventory behind مُورِيَٰتِ includes both concealment and bringing hidden fire out.","mechanism":"A strike alters a covering surface by leaving a mark; that rupture can expose what the surface had kept out of sight. The focus can therefore stage disclosure through abrasion as well as ignition.","model_id":"B-MARK-EXPOSURE-02","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:5.6-sol-high:B-MARK-EXPOSURE-02","source_type":"hft","support_id":"sup_820492beff1443fb51f3","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُورِيَٰتِ قَدْحًۭا","ayah_ref":"100:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001203/B005","root_001642/B003"],"payload":{"activation_trace":[{"assigned_role":"Supplies the successful yield and beneficiary relation.","branch_id":"B003","branch_image_ar":"زند يقدح نجاحا أو نصرة","literal_contribution":"A fire-stick that takes images success, counsel, aid, or defense.","mapped_root_id":"root_001642","mapped_root_norm":"و ر ي","root":"و ر ي","source_phrase_ar":"مُورِيَٰتِ","source_ref":"100:2"},{"assigned_role":"Supplies extraction from a holding source.","branch_id":"B005","branch_image_ar":"غرف ما في القدر","literal_contribution":"Contents, including difficult residue, are drawn from a vessel or well.","mapped_root_id":"root_001203","mapped_root_norm":"ق د ح","root":"ق د ح","source_phrase_ar":"قَدْحًا","source_ref":"100:2"}],"changed_reading":{"after":"A worked source yielding aid, success, or a usable remainder.","before":"A physical spark-making motion."},"confidence":"exploratory","focus_anchor":"The two focus roots admit a success-bearing fire-stick and the strenuous drawing of contents or residue.","mechanism":"The action can be modeled as productive extraction: an implement is worked until it yields a useful result. The spark is then one instance of a more abstract conversion from stored resource to obtained benefit.","model_id":"B-YIELD-AID-03","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:5.6-sol-high:B-YIELD-AID-03","source_type":"hft","support_id":"sup_8491936c09669d92d8cf","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُورِيَٰتِ قَدْحًۭا","ayah_ref":"100:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001203/B004","root_001642/B001"],"payload":{"activation_trace":[{"assigned_role":"Supplies concealed inward consumption.","branch_id":"B001","branch_image_ar":"داء يأكل الجوف أو يصيب الرئة","literal_contribution":"An illness eats the interior or strikes the lung.","mapped_root_id":"root_001642","mapped_root_norm":"و ر ي","root":"و ر ي","source_phrase_ar":"مُورِيَٰتِ","source_ref":"100:2"},{"assigned_role":"Supplies material damage as the trace left by inward consumption.","branch_id":"B004","branch_image_ar":"أكال الشجر والسن","literal_contribution":"Decay or a worm eats wood or teeth and darkens them.","mapped_root_id":"root_001203","mapped_root_norm":"ق د ح","root":"ق د ح","source_phrase_ar":"قَدْحًا","source_ref":"100:2"}],"changed_reading":{"after":"A latent consuming process becoming perceptible through the wound, darkening, or cavity it produces.","before":"A brief external flare."},"confidence":"exploratory","focus_anchor":"Both focus roots contain branch images of something eating inward: illness in the belly or lung under و ر ي and decay in wood or teeth under ق د ح.","mechanism":"Instead of an instant outward spark, the focus can weakly activate a slow inward combustion analogue: hidden consumption announces itself through damage.","model_id":"B-CORROSIVE-04","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:5.6-sol-high:B-CORROSIVE-04","source_type":"hft","support_id":"sup_666c11b53573bb907d5a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُورِيَٰتِ قَدْحًۭا","ayah_ref":"100:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001203/B001","root_001642/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001642","role":"Hidden fire emerging from a fire-stick supplies the latent capacity and the causative act of releasing it.","root":"و ر ي","source_ref":"100:2","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001203","role":"Striking out fire supplies the contact operation and its visible fiery result.","root":"ق د ح","source_ref":"100:2","source_word_indices":["2"]}],"changed_reading":{"after":"Agents repeatedly make concealed fire take through forceful contact.","before":"A static mention of sparks."},"confidence":"strong","focus_anchor":"The causative participle مُورِيَات and the manner/result accusative قَدْحًا form a release-by-contact construction.","mechanism":"A striker does not manufacture fire from nothing; repeated contact makes a hidden capacity take and become visible.","model_id":"baseline_latent_ignition"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:5.6-sol-xhigh:baseline_latent_ignition","source_type":"hft","support_id":"sup_b1f045d586d5376cba7b","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُورِيَٰتِ قَدْحًۭا","ayah_ref":"100:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001203/B002","root_001642/B005"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_001642","role":"Covering and withdrawal from sight supplies the concealed state that the causative form reverses.","root":"و ر ي","source_ref":"100:2","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001203","role":"Scoring, splitting, or flawing supplies the revealing breach and the durable mark.","root":"ق د ح","source_ref":"100:2","source_word_indices":["2"]}],"changed_reading":{"after":"The action scores a cover so that a concealed condition flashes into evidence.","before":"The action merely emits light."},"confidence":"medium","focus_anchor":"مُورِيَات marks active bringers-forth, while قَدْحًا can name an incision, score, or flaw.","mechanism":"Impact opens or marks a surface, and the mark makes an otherwise hidden condition legible.","model_id":"baseline_revealing_score"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:5.6-sol-xhigh:baseline_revealing_score","source_type":"hft","support_id":"sup_a67ea33db9bc803b54e2","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُورِيَٰتِ قَدْحًۭا","ayah_ref":"100:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001203/B010","root_001642/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001642","role":"A fire-stick taking as success, counsel, aid, or defense supplies achieved efficacy rather than flame alone.","root":"و ر ي","source_ref":"100:2","source_word_indices":["1"]},{"branch_id":"B010","mapped_root_id":"root_001203","role":"Considering and planning an affair supplies the deliberate operation through which efficacy is obtained.","root":"ق د ح","source_ref":"100:2","source_word_indices":["2"]}],"changed_reading":{"after":"Capable agents make an undertaking catch through aided, deliberate engagement.","before":"Unplanned friction happens to spark."},"confidence":"exploratory","focus_anchor":"The same two focus roots carry an idiom of a fire-stick taking successfully and a branch of deliberative undertaking.","mechanism":"The fire-making construction can model an operation that succeeds because counsel, aid, and decisive examination make it catch.","model_id":"baseline_successful_operation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:5.6-sol-xhigh:baseline_successful_operation","source_type":"hft","support_id":"sup_79dd429d524c22e0f1d3","trust":"legacy_unbound"}]}
</lane_packet_json>
