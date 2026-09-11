# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **100:5**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s100-regular-20260911/s100/100_5/micro.discovery.json` and modify nothing
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
  "ayah_ref": "100:5",
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
{"analysis_context":{"analysis_id":"s100-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"100:5","host_surah":100,"lane_context_refs":[],"ordered_context_refs":["100:0","100:1","100:2","100:3","100:4","100:6","100:7","100:8","100:9","100:10","100:11","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Çekirdek toplama eylemidir; mal biriktirme ve yağma malını derleme gibi özel kullanımlar bütün dala yayılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000259/B001","candidate_links":[{"candidate_id":"cand_3a071dc4f4719f1ba1b0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَمْع","morph_features":"STEM|POS:N|LEM:jamoE|ROOT:jmE|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:5:3:1","qac_word_ref":"100:5:3","surface_ar":"جَمْعًا"}],"gloss":"dağınık parçaları bir araya toplama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ayrı parçalar birbirine yaklaştırılır ve dağınıklık sona erdirilir."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dağınık öğelerin yaklaştırılıp tek bir topluluk durumuna getirildiği genel çekirdeği karşılar.","boundary_detail":"Çekirdek toplama eylemidir; mal biriktirme ve yağma malını derleme gibi özel kullanımlar bütün dala yayılmaz.","branch_image_ar":"ضم المتفرق حتى يصير شيئا مجموعا","concept_gloss":"dağınık parçaları bir araya toplama","contextual_glosses":[{"applicability":"Nesnelerin veya kişilerin ayrı yerlerden tek yerde toplandığı cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ayrı olanları yaklaştırıp birlikte bulundurma sonucunu korur."},"facet_ids":["F001"],"text":"bir araya getirmek","usage_role":"general"}],"definition":"Önceden ayrı veya dağınık duran parçaları birbirine yaklaştırarak bir araya getirme eylemidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ayrı parçalar birbirine yaklaştırılır ve dağınıklık sona erdirilir."}],"identity_rationale":"Kaynak ifadesi, dağınık parçaların birbirine yaklaştırılıp bir araya getirilmesini açıkça ortak anlam çekirdeği olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"dağınık şeyi bir araya toplamak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"mal biriktirmek ve saymak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"ayrı yerlerdeki şeyleri bütünüyle bir araya getirmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"çeşitli yerlerden toplanmış şey"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"çeşitli yerlerden toplanıp götürülen yağma malı"}],"lexicalization_note":"Tanım genel toplama çekirdeğini korur; mal ve yağma malıyla ilgili anlamları yalnız kendi özel birimlerinde tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; işlem ile ortaya çıkan insan topluluğu arasındaki ayrım en yararlı karşılaştırma olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal birleştirme işlemini anlatır; komşu dal ise özellikle insanların oluşturduğu topluluğu adlandırır.","focus_only":"Dağınık parçaları birbirine yaklaştıran eylem ve süreçtir.","gloss":"bir araya gelmiş insan topluluğu","neighbor_only":"Eylemin sonucu olarak bir arada bulunan insan topluluğudur.","neighbor_ref":"root_000259/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da ayrılığın yerini bir arada bulunma durumu alır."}],"source_phrase_ar":"أصل واحد يدل على تضام الشيء (maqayis)؛ الجمع مصدر جمعت الشيء (ayn)؛ الجمع خلاف التفريق جمعت الشيء إذا ضممت بعضه إلى بعض (jamhara)؛ جمعت الشئ المتفرق فاجتمع (sihah)؛ الجمع أن تجمع شيئا إلى شيء (tahdhib)؛ الجمع ضم الشيء بتقريب بعضه من بعض (mufradat)","source_summary":"Kaynakların ortak anlatımı, toplamanın karşıtını dağıtma olarak görür ve eylemi bir şeyi başka bir şeye katıp parçaları yakınlaştırma biçiminde açıklar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه جمع الشيء أو المال أو القوم، وجعل المتفرق جميعا، وما جمع من مواضع شتى كنهب مجمع.","what_is_not_ar":"لا يدخل فيه عزم الرأي وحده ولا أسماء الأزمنة والمواضع إلا من جهة سبب التسمية."},"support_links":["sup_f66908e1e4897066becf"]},{"boundary":"Dal, toplama eylemini değil bir araya gelmiş insanları; cinsel birleşme anlamını değil insan topluluğunu gösterir.","branch_kind":"bare","branch_ref":"root_000259/B002","candidate_links":[{"candidate_id":"cand_d02865cfa158ca726614","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَمْع","morph_features":"STEM|POS:N|LEM:jamoE|ROOT:jmE|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:5:3:1","qac_word_ref":"100:5:3","surface_ar":"جَمْعًا"}],"gloss":"bir araya gelmiş insan topluluğu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birden çok insan bir arada bulunan bir topluluk oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Topluluk farklı boylardan veya kesimlerden gelen karışık insanlardan oluşabilir."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsanların birlikte bir küme oluşturduğu genel anlamı ve karışık kökenli topluluk özel durumunu kapsar.","boundary_detail":"Dal, toplama eylemini değil bir araya gelmiş insanları; cinsel birleşme anlamını değil insan topluluğunu gösterir.","branch_image_ar":"جماعة اجتمعت أو أخلاط ضمتها الجهة","concept_gloss":"bir araya gelmiş insan topluluğu","contextual_glosses":[{"applicability":"Farklı boy veya kesimlerden gelen kişilerin oluşturduğu topluluk anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluk olmayı ve üyelerin farklı kökenlerden gelmesini birlikte korur."},"facet_ids":["F002"],"text":"karışık bir insan topluluğu","usage_role":"contextual"}],"definition":"Bir araya gelerek topluluk oluşturan insanlar, özellikle farklı boylardan veya kesimlerden gelmiş karışık bir insan kümesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birden çok insan bir arada bulunan bir topluluk oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Topluluk farklı boylardan veya kesimlerden gelen karışık insanlardan oluşabilir."}],"identity_rationale":"Kaynak ifadesi hem genel insan topluluğunu hem de farklı boylardan gelmiş karışık insan kümesini doğrudan tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"insan topluluğu veya çokluk"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"farklı boylardan karışık insan topluluğu"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"toplanmış topluluk veya ordu"}],"lexicalization_note":"Tanım çıplak dalın insan topluluğu anlamıyla sınırlıdır ve başka dallardaki eylem ya da cinsellik anlamlarını içermez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; insan grubu çekirdeğini paylaşırken üye türü ve karışık köken bakımından ayrılan aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Örtüşme insan topluluğundadır; bu dal karışık kökeni de anlatabilirken komşu dal hayvan sürülerine uzanır.","focus_only":"Farklı boylardan gelen karışık insan topluluğunu da kapsar.","gloss":"insan veya sürü topluluğu","neighbor_only":"İnsanların yanı sıra çok sayıdaki koyun veya keçi topluluğunu da kapsar.","neighbor_ref":"root_001184/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir arada bulunan insan grubunu adlandırabilir."}],"source_phrase_ar":"الجماع الأشابة من قبائل شتى (maqayis)؛ الجمع اسم لجماعة الناس والجموع اسم لجماعة الناس (ayn)؛ الجماع ما تجمع من أشابة الناس وأخلاطهم (jamhara)؛ جماع الناس أخلاطهم وهم الأشابة من قبائل شتى (sihah)؛ الجماع يقال في أقوام متفاوتة اجتمعوا (mufradat)","source_summary":"Ortak anlatım, sözü bir insan topluluğunun adı olarak verir; bazı anlatımlarda bu topluluğun farklı boylardan gelen karışık kişilerden oluştuğu özellikle belirtilir.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الجمع والجموع والجميع والجماعة والجماع إذا أريد بها جماعة الناس أو أخلاطهم أو الجيش.","what_is_not_ar":"لا يدخل فيه فعل الجمع نفسه، ولا الجماع بمعنى النكاح."},"support_links":["sup_eba78b263c1d1790e977"]},{"boundary":"Dalın çekirdeği kesin yöneliş ve sağlamlaştırmadır; birden çok kişinin görüş birliği bütün kullanımlara genellenmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000259/B003","candidate_links":[{"candidate_id":"cand_3491206cad5a8f64ba6b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَمْع","morph_features":"STEM|POS:N|LEM:jamoE|ROOT:jmE|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:5:3:1","qac_word_ref":"100:5:3","surface_ar":"جَمْعًا"}],"gloss":"düşünüp kesin bir tutuma bağlanma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Düşünme ve hazırlığın ardından bir işi yapma yönünde kesin tutum alınır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İş veya düzen, dağınık düşünceler bir sonuca bağlanarak sağlamlaştırılır."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir işin düşünme ve hazırlık sonrasında kesinleştirildiği çekirdeği karşılar.","boundary_detail":"Dalın çekirdeği kesin yöneliş ve sağlamlaştırmadır; birden çok kişinin görüş birliği bütün kullanımlara genellenmez.","branch_image_ar":"عزم محكم جمع الرأي بعد تفرقه","concept_gloss":"düşünüp kesin bir tutuma bağlanma","contextual_glosses":[{"applicability":"Bir iş veya tasarı üzerinde düşünüldükten sonra geri dönülmez bir tutum alındığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Düşünme sonunda kararı ve işi sağlamlaştırma yönünü korur."},"facet_ids":["F001","F002"],"text":"iyice düşünüp kesinleştirmek","usage_role":"general"}],"definition":"Bir işi düşünüp hazırladıktan sonra onu yapmaya kesin biçimde bağlanma ve tutumu sağlamlaştırmadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Düşünme ve hazırlığın ardından bir işi yapma yönünde kesin tutum alınır."},{"facet_id":"F002","role":"specialization","statement":"İş veya düzen, dağınık düşünceler bir sonuca bağlanarak sağlamlaştırılır."}],"identity_rationale":"Kaynak ifadesi düşünme sonunda bir işe kesin biçimde yönelmeyi, hazırlanmayı ve işi sağlamlaştırmayı destekler; görüş birliği ise yalnız ayrı bir söz biriminde belirgindir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bir işi yapmaya kesin biçimde karar vermek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"hazırlık, kesin karar veya görüş birliği"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"işi veya düzeni sağlamlaştırıp kesinleştirmek"}],"lexicalization_note":"Genel kesin yöneliş ile işi veya düzeni sağlamlaştıran özel yapılar ayrılır; görüş birliği yalnız ilgili birimde tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kesin karar ile başkasıyla ortak davranma arasındaki sınır en güçlü karışma noktasıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kararın kesinleşmesine odaklanır; komşu dal ise ikinci bir katılımcıyla birlikte davranma ilişkisini zorunlu kılar.","focus_only":"Kişinin veya kurulun düşünüp kesin bir tutuma varmasını anlatır.","gloss":"bir işte başkasıyla güç birliği yapma","neighbor_only":"Başka biriyle aynı iş üzerinde birleşip ona destek olmayı gerektirir.","neighbor_ref":"root_000259/B013","relation_type":"near_neighbor","shared_zone":"Her iki dalda da belirli bir iş üzerinde birleşme ve dağınıklığı giderme vardır."}],"source_phrase_ar":"أجمعت على الأمر إجماعا وأجمعته (maqayis)؛ أجمعت على الأمر إجماعا إذا عزمت عليه (jamhara)؛ أجمعت الأمر وعلى الأمر إذا عزمت عليه (sihah)؛ الإجماع الإعداد والعزيمة على الأمر (tahdhib)؛ أجمعت كذا فيما يكون جمعا يتوصل إليه بالفكرة (mufradat)","source_summary":"Kaynaklar bir işe yönelmeyi kesin karar, hazırlık ve sağlamlaştırma yönleriyle açıklar; düşünerek bir sonuca varma bu anlatımları birbirine bağlar.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه أجمع على الأمر، أجمع الأمر أو الكيد، الإجماع بمعنى الإعداد والعزيمة والإحكام، واجتماع الآراء على تدبير.","what_is_not_ar":"لا يدخل فيه مجرد جمع الأجسام أو اجتماع الناس في مكان."},"support_links":["sup_4e72a3a36834bba7f1a6"]},{"boundary":"Dal çekirdeği toplanmayla belirlenen yer veya gündür; ibadet çağrısı ve ıssız alan kullanımları genel tanımı genişletmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000259/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَمْع","morph_features":"STEM|POS:N|LEM:jamoE|ROOT:jmE|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:5:3:1","qac_word_ref":"100:5:3","surface_ar":"جَمْعًا"}],"gloss":"toplanmayla belirlenen yer veya gün","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yer, insanların orada toplanması nedeniyle bu anlamla adlandırılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir gün, insanların ibadet veya yeniden bir araya geliş için toplanmasıyla belirlenir."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsanların bir araya gelmesinin bir yerin ya da günün adı ve işlevi için belirleyici olduğu kullanımları kapsar.","boundary_detail":"Dal çekirdeği toplanmayla belirlenen yer veya gündür; ibadet çağrısı ve ıssız alan kullanımları genel tanımı genişletmez.","branch_image_ar":"موضع أو يوم أو نداء يجمع الناس","concept_gloss":"toplanmayla belirlenen yer veya gün","contextual_glosses":[{"applicability":"Bir yerin insanları bir araya getirme işlevi öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yer ile insanların orada toplanması arasındaki bağı korur."},"facet_ids":["F001"],"text":"insanların toplandığı yer","usage_role":"contextual"}],"definition":"İnsanların bir araya gelmesi nedeniyle adı veya işlevi belirlenen bir yer ya da gündür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yer, insanların orada toplanması nedeniyle bu anlamla adlandırılır."},{"facet_id":"F002","role":"specialization","statement":"Bir gün, insanların ibadet veya yeniden bir araya geliş için toplanmasıyla belirlenir."}],"identity_rationale":"Kaynak ifadesi insanların toplanması nedeniyle adlandırılmış yerleri ve günleri açıkça destekler; çağrı ve başka özel yapılar yalnız ayrı söz birimlerinde bulunur.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"insanların toplandığı yer"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"insanların bir araya geldiği kutsal yer veya günler için kullanılan ad"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"insanların ibadet veya yeniden diriliş için toplandığı gün"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"haftalık toplu ibadete katılıp namazı kılmak"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"halkı toplu ibadet için bir araya getiren ibadet yeri"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ibadet için toplanma çağrısı"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yolunu yitirme korkusuyla insanların ayrılmadığı ıssız alan"}],"lexicalization_note":"Yer ve gün çekirdeği korunur; ibadet yeri, çağrı ve ayrılmama anlatan özel yapılar kendi birimleriyle sınırlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; toplantı yeriyle olan yakınlık ve günlere uzanan kapsam farkı en açıklayıcı karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yer veya günün toplanmayla adlandırılmasına odaklanır; komşu dal toplantı yerini, oradaki etkinliği ve topluluğu kapsar.","focus_only":"Toplanma nedeniyle adlandırılmış günleri ve özel yerleri birlikte kapsar.","gloss":"toplantı yeri ve topluluğu","neighbor_only":"Toplantı yerindeki konuşma, danışma ve orada bulunan topluluğu da kapsar.","neighbor_ref":"root_001487/B003","relation_type":"near_neighbor","shared_zone":"İki dal da insanların bir araya geldiği yeri anlatabilir."}],"source_phrase_ar":"جمع مكة سمي لاجتماع الناس به وكذلك يوم الجمعة (maqayis)؛ المجمع حيث يجمع الناس (ayn)؛ أيام جمع أيام منى والجمعة مشتقة من اجتماع الناس فيها للصلاة (jamhara)؛ يقال للمزدلفة جمع لاجتماع الناس فيها (sihah)؛ يوم الجمع ويوم يجمعكم ليوم الجمع (mufradat)","source_summary":"Kaynakların ortak noktası, belirli yer ve gün adlarını insanların oralarda veya o zamanlarda toplanmasıyla açıklamalarıdır.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه المجمع والموضع الذي يجتمع فيه الناس، وجمع للمزدلفة أو أيام منى، ويوم الجمعة ويوم الجمع، والمسجد الجامع، ونداء الصلاة جامعة، وفلاة مجمعة.","what_is_not_ar":"لا يدخل فيه الجماعة نفسها إذا لم يكن اللفظ زمنا أو موضعا أو نداء."},"support_links":[]},{"boundary":"Anlam genel sayısal çokluk değildir; sıkılmış avucun biçimi, vuruşu veya alabildiği miktarla sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000259/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَمْع","morph_features":"STEM|POS:N|LEM:jamoE|ROOT:jmE|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:5:3:1","qac_word_ref":"100:5:3","surface_ar":"جَمْعًا"}],"gloss":"sıkılmış avuç veya bir avuçluk miktar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Parmakların kapanmasıyla el sıkılmış bir avuç biçimi alır ve bu biçimle vurulabilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sıkılmış avucun aldığı şey bir avuçluk miktar olarak ölçülür."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Elin kapanmış biçimini, onunla vurmayı ve bu elin aldığı miktarı birlikte kapsar.","boundary_detail":"Anlam genel sayısal çokluk değildir; sıkılmış avucun biçimi, vuruşu veya alabildiği miktarla sınırlıdır.","branch_image_ar":"قبضة الكف إذا ضمت الأصابع","concept_gloss":"sıkılmış avuç veya bir avuçluk miktar","contextual_glosses":[{"applicability":"Meyve, para veya benzeri bir şeyin avucun alacağı miktarı anlatırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Miktarın kapalı avucun kapasitesiyle belirlenmesini korur."},"facet_ids":["F002"],"text":"bir avuç dolusu","usage_role":"contextual"}],"definition":"Parmaklar içe kapanınca oluşan sıkılmış avuç ve bu avucun kavrayabildiği miktardır; aynı el biçimiyle vurma da buna bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Parmakların kapanmasıyla el sıkılmış bir avuç biçimi alır ve bu biçimle vurulabilir."},{"facet_id":"F002","role":"extension","statement":"Sıkılmış avucun aldığı şey bir avuçluk miktar olarak ölçülür."}],"identity_rationale":"Kaynak ifadesi parmaklar kapanınca oluşan sıkılmış avucu, onunla vurmayı ve avuç miktarını aynı somut biçim çevresinde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"sıkılmış avuç veya bu avuçla vurma"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"bir avuç dolusu"}],"lexicalization_note":"Sıkılmış avuç çekirdeği ile avuç dolusu miktar ve bu avuçla vurma kullanımları birbirinden açıkça ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; avucun biçimi ile avuçlayarak alma eylemi arasındaki ayrım okuyucu için en yararlı sınırdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal el biçimi ve ondan doğan ölçüdür; komşu dal ise o elle bir şeyi tutup alma eylemidir.","focus_only":"Kapalı avucun biçimini, vuruşunu ve aldığı miktarı adlandırır.","gloss":"avuçlayarak almak","neighbor_only":"Bir şeyi bütün avuçla kavrayıp alma eylemini anlatır.","neighbor_ref":"root_001197/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da parmakların bir şey çevresinde kapanması belirleyicidir."}],"source_phrase_ar":"ضربته بجمع كفي وجمع كفي (maqayis)؛ ضربته بجمع كفي وأعطيته من الدراهم جمع الكف (ayn)؛ ضربته بجمع يدي إذا ضممت كفك ثم ضربته بها (jamhara)؛ جمع الكف وهو حين تقبضها وجمعة من تمر أي قبضة منه (sihah)","source_summary":"Ortak anlatım sıkılmış avucu temel alır; bu avuçla vurmayı ve avucun doldurduğu para ya da meyve miktarını aynı biçime bağlar.","sources":["MQ","AY","JA","SI"],"what_is_ar":"يدخل فيه جمع الكف، الضرب بجمع الكف، ملء الجمع، والقبضة أو جمعة التمر.","what_is_not_ar":"لا يدخل فيه مطلق الجمع العددي إلا إذا كان بمقدار الكف."},"support_links":[]},{"boundary":"Dal yalnız cinsel birleşmeyi anlatır; insan topluluğu ya da gebelikle birlikte kalma anlamları bu sınıra girmez.","branch_kind":"bare","branch_ref":"root_000259/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَمْع","morph_features":"STEM|POS:N|LEM:jamoE|ROOT:jmE|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:5:3:1","qac_word_ref":"100:5:3","surface_ar":"جَمْعًا"}],"gloss":"cinsel birleşme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadınla erkek arasında cinsel birleşme gerçekleşir ve söz bunu doğrudan ya da örtülü biçimde anlatır."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kadınla erkek arasındaki cinsel birleşmenin doğrudan veya örtülü biçimde anlatıldığı kullanımları karşılar.","boundary_detail":"Dal yalnız cinsel birleşmeyi anlatır; insan topluluğu ya da gebelikle birlikte kalma anlamları bu sınıra girmez.","branch_image_ar":"اتصال الجماع والمجامعة","concept_gloss":"cinsel birleşme","contextual_glosses":[{"applicability":"Eylemin doğal ve açık bir Türkçe yüklemle verilmesi gereken cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki kişi arasındaki cinsel birleşme eylemini korur."},"facet_ids":["F001"],"text":"cinsel ilişkide bulunmak","usage_role":"general"}],"definition":"Kadınla erkek arasındaki cinsel birleşme veya bu birleşmeyi anlatan örtülü söyleyiştir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadınla erkek arasında cinsel birleşme gerçekleşir ve söz bunu doğrudan ya da örtülü biçimde anlatır."}],"identity_rationale":"Kaynak ifadesi iki biçimi de kadınla erkek arasındaki cinsel birleşmenin dolaylı veya doğrudan anlatımı olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"cinsel birleşme için kullanılan örtülü söz"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"cinsel ilişkide bulunma"}],"lexicalization_note":"Tanım çıplak dalın cinsel birleşme anlamını verir ve aynı ses dizisine bağlı topluluk anlamını dışarıda bırakır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı çekirdek ve sınıra sahip örtülü cinsel birleşme dalı eş anlamlı olarak seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek olay ve anlam sınırı aynıdır; ayrılık yalnız bu olayı adlandıran sözlerin görüntüsündedir.","focus_only":null,"gloss":"cinsel birleşme","neighbor_only":null,"neighbor_ref":"root_001423/B002","relation_type":"synonym","shared_zone":"Her iki dal da kadınla erkek arasındaki cinsel birleşmeyi, örtülü söyleyişe açık biçimde anlatır."}],"source_phrase_ar":"الجماع كناية عن النكاح (jamhara)؛ المجامعة المباضعة (sihah)","source_summary":"Kaynaklar iki söz biçimini aynı cinsel birleşme anlamında buluşturur; bunlardan biri özellikle örtülü anlatım olarak nitelenir.","sources":["JA","SI"],"what_is_ar":"يدخل فيه الجماع كناية عن النكاح، والمجامعة بمعنى المباضعة.","what_is_not_ar":"لا يدخل فيه جماع الناس بمعنى أخلاطهم، ولا المرأة بجمع إذا أريد موتها مع حملها."},"support_links":[]},{"boundary":"Çekirdek kadınla ilgili ölüm veya el değmemişlik durumudur; hayvanın ilk gebeliği genel tanıma katılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000259/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَمْع","morph_features":"STEM|POS:N|LEM:jamoE|ROOT:jmE|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:5:3:1","qac_word_ref":"100:5:3","surface_ar":"جَمْعًا"}],"gloss":"çocuğu karnındayken ölen veya el değmemiş kalan kadın","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadın, çocuğu hâlâ karnındayken ölür."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kadın ölünceye dek ya da kocasının yanında bulunduğu sırada cinsel birleşme yaşamamıştır."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kadının karnındaki çocukla ölmesi veya cinsel birleşme yaşamamış durumda kalması anlamlarını birlikte gösterir.","boundary_detail":"Çekirdek kadınla ilgili ölüm veya el değmemişlik durumudur; hayvanın ilk gebeliği genel tanıma katılmaz.","branch_image_ar":"حال المرأة أو الأنثى التي بقي حملها أو عذرها معها","concept_gloss":"çocuğu karnındayken ölen veya el değmemiş kalan kadın","contextual_glosses":[{"applicability":"Kadının doğum gerçekleşmeden, karnındaki çocukla birlikte öldüğü anlatımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölüm sırasında çocuğun hâlâ kadının karnında bulunması koşulunu korur."},"facet_ids":["F001"],"text":"çocuğu karnındayken ölmek","usage_role":"contextual"}],"definition":"Bir kadının çocuğu karnındayken ölmesi veya evlilikte cinsel birleşme yaşamadan el değmemiş durumda kalmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadın, çocuğu hâlâ karnındayken ölür."},{"facet_id":"F002","role":"source_variant","statement":"Kadın ölünceye dek ya da kocasının yanında bulunduğu sırada cinsel birleşme yaşamamıştır."}],"identity_rationale":"Kaynak ifadesi kadının çocuğu karnındayken ölmesini ve el değmemiş durumda kalmasını birlikte destekler; ilk gebeliğindeki dişi eşek yalnız ayrı söz biriminde tanıklanır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"çocuğu karnındayken veya el değmemişken ölmek"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"kocasıyla cinsel birleşme yaşamamış kadın"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"ilk kez gebe kalan dişi eşek"}],"lexicalization_note":"Kadının gebeyken ölmesi ile birleşme yaşamamış olması ayrılır; dişi eşeğin ilk gebeliği yalnız kendi biriminde tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel gebelik alanıyla özel ölüm veya el değmemişlik koşulunun ayrımı yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal ölüm ya da el değmemişlik gibi özel bir durumu gerektirir; komşu dal gebeliği ve ana karnındaki çocuğu genel olarak anlatır.","focus_only":"Gebelik sürerken ölme veya el değmemiş durumda kalma koşulunu anlatır.","gloss":"gebelik ve karındaki çocuk","neighbor_only":"Kadın ya da dişinin gebeliğini ve karnındaki çocuğun bulunduğu yeri genel olarak adlandırır.","neighbor_ref":"root_000291/B006","relation_type":"same_field","shared_zone":"İki dal da gebelik sırasında çocuğun ana karnında bulunması alanına girer."}],"source_phrase_ar":"ماتت بجمع أي في بطنها ولد (maqayis)؛ ماتت المرأة بجمع أي مع ما في بطنها وكذلك إذا ماتت عذراء (ayn)؛ ماتت المرأة بجمع إذا ماتت وولدها في بطنها (jamhara)؛ أمر بني فلان بجمع أي لم يقتضها وماتت فلانة بجمع أي ماتت وولدها في بطنها (sihah)","source_summary":"Kaynakların çoğu kadının karnındaki çocukla birlikte ölmesini verir; anlatım ayrıca el değmemiş olarak ölme veya evlilikte henüz birleşme yaşamamış olma durumuna uzanır.","sources":["MQ","AY","JA","SI"],"what_is_ar":"يدخل فيه ماتت المرأة بجمع أي وولدها في بطنها، أو عذراء لم تمسس، وفلانة عند زوجها بجمع إذا لم يصل إليها، وأتان جامع إذا حملت أول ما تحمل.","what_is_not_ar":"لا يدخل فيه الجماع بمعنى المباضعة نفسها."},"support_links":[]},{"boundary":"Dal genel olarak her türlü bağ veya tutukluluk değil, elleri boyna bağlayan belirli kelepçe türüdür.","branch_kind":"bare","branch_ref":"root_000259/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَمْع","morph_features":"STEM|POS:N|LEM:jamoE|ROOT:jmE|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:5:3:1","qac_word_ref":"100:5:3","surface_ar":"جَمْعًا"}],"gloss":"elleri boyna bağlayan kelepçe","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bağ, iki eli boyunla bir araya getirerek hareketi engeller."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ellerin boyunla birlikte bağlanıp hareketin kısıtlandığı özel bağ aracını karşılar.","boundary_detail":"Dal genel olarak her türlü bağ veya tutukluluk değil, elleri boyna bağlayan belirli kelepçe türüdür.","branch_image_ar":"القيد الذي يجمع اليدين إلى العنق","concept_gloss":"elleri boyna bağlayan kelepçe","contextual_glosses":[{"applicability":"Tarihsel bağ aracının biçiminin açıkça anlatılması gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aracın demir bağ oluşunu ve el ile boynu birleştirmesini korur."},"facet_ids":["F001"],"text":"elleri boyna bağlayan demir bağ","usage_role":"explanatory"}],"definition":"Elleri boyna doğru bağlayarak kişinin hareketini kısıtlayan kelepçe veya demir bağdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bağ, iki eli boyunla bir araya getirerek hareketi engeller."}],"identity_rationale":"Kaynak ifadesi tekil ve çoğul biçimleri, elleri boyna doğru birleştirerek hareketi kısıtlayan demir bağ olarak açıklar.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"elleri boyna bağlayan kelepçe veya demir bağ"}],"lexicalization_note":"Tanım çıplak dalın özel kelepçe anlamını korur ve aynı biçimin topluluk ya da ibadet yeri anlamlarını dışlar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; elleri boyna bağlama biçimini eksiksiz paylaşan dal eş anlamlı olarak seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek araç, bağlama biçimi ve kısıtlama sınırı bakımından anlamlı bir ayrım yoktur.","focus_only":null,"gloss":"elleri boyna bağlayan kelepçe","neighbor_only":null,"neighbor_ref":"root_000995/B020","relation_type":"synonym","shared_zone":"Her iki dal da elleri boyna doğru bağlayan kelepçe türünü anlatır."}],"source_phrase_ar":"الجوامع الأغلال (maqayis)؛ الجوامع الأغلال الواحدة جامعة (jamhara)؛ الجامعة الغل لأنها تجمع اليدين إلى العنق (sihah)","source_summary":"Kaynaklar sözü kelepçe ve demir bağ olarak açıklar; adlandırma, iki elin boyna doğru bağlanarak bir araya getirilmesine dayanır.","sources":["MQ","JA","SI"],"what_is_ar":"يدخل فيه الجامعة والجوامع بمعنى الأغلال.","what_is_not_ar":"لا يدخل فيه المسجد الجامع ولا الجماعة."},"support_links":[]},{"boundary":"Çekirdek eksiksiz bütünlüktür; büyüyüp belirli giysileri giyme kullanımı bütün dala ait kurucu bir özellik değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000259/B009","candidate_links":[{"candidate_id":"cand_2d587d089fc28c47cf7e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَمْع","morph_features":"STEM|POS:N|LEM:jamoE|ROOT:jmE|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:5:3:1","qac_word_ref":"100:5:3","surface_ar":"جَمْعًا"}],"gloss":"eksiksiz bütünlük","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Canlının bedeninden hiçbir parça eksilmemiştir ve varlık bütündür."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi bedence derli toplu bir yapıya ulaşmış veya gelişimini tamamlamıştır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir topluluğun üyeleri eksiksiz biçimde hep birlikte bulunur."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedenin parçasız eksiksizliğini, gelişimin tamamlanmasını ve üyelerin tümünün birlikte bulunmasını kapsar.","boundary_detail":"Çekirdek eksiksiz bütünlüktür; büyüyüp belirli giysileri giyme kullanımı bütün dala ait kurucu bir özellik değildir.","branch_image_ar":"اكتمال الشيء كله بلا تفرق أو نقص","concept_gloss":"eksiksiz bütünlük","contextual_glosses":[{"applicability":"Bir topluluğun bütün üyelerinin birlikte bulunduğunu pekiştiren cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluğun hiçbir üyesinin dışarıda kalmaması anlamını korur."},"facet_ids":["F003"],"text":"bütünüyle, eksiksiz olarak","usage_role":"contextual"}],"definition":"Bir varlığın hiçbir parçası eksilmeden bütün olması, kişinin yapıca gelişimini tamamlaması veya bir topluluğun tüm üyeleriyle birlikte bulunmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Canlının bedeninden hiçbir parça eksilmemiştir ve varlık bütündür."},{"facet_id":"F002","role":"specialization","statement":"Kişi bedence derli toplu bir yapıya ulaşmış veya gelişimini tamamlamıştır."},{"facet_id":"F003","role":"extension","statement":"Bir topluluğun üyeleri eksiksiz biçimde hep birlikte bulunur."}],"identity_rationale":"Kaynak ifadesi bedenin eksiksizliğini, kişinin gelişmiş yapısını ve herkesin birlikte bulunmasını destekler; genç kızın giysi çağı yalnız ayrı söz birimindedir.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bedeni eksiksiz hayvan veya varlık"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"bedence derli toplu veya gelişimini tamamlamış adam"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"büyüyüp bütün dış giysileri giyecek çağa gelmek"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"bütünlük bildiren pekiştirme sözleri"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"dağılmamış bütün veya hepsi"}],"lexicalization_note":"Bütünlük çekirdeği korunur; beden, pekiştirme ve giysi çağıyla ilgili özel gerçekleşmeler ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; durum olarak bütünlük ile süreç ve yükümlülük olarak tamamlama arasındaki ayrım seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal varlığın veya topluluğun bütün durumuna odaklanır; komşu dal süreç tamamlamaya ve yükümlülüğü eksiksiz yerine getirmeye uzanır.","focus_only":"Bedenin eksiksiz yapısını ve topluluğun tüm üyeleriyle bulunmasını da anlatır.","gloss":"tamamlama ve eksiksiz yerine getirme","neighbor_only":"Söz, ölçü, hak veya anlaşma yükümlülüğünü tam yerine getirmeyi de kapsar.","neighbor_ref":"root_001669/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyde eksik kalmaması ve bütünün tamamlanması düşüncesini taşır."}],"source_phrase_ar":"الجمعاء من البهائم وغيرها التي لم يذهب من بدنها شيء (maqayis)؛ رجل جميع أي مجتمع في خلقه (ayn)؛ الرجل المجتمع الذي بلغ أشده (sihah)؛ جميع لدينا محضرون (mufradat)","source_summary":"Kaynak anlatımı eksiksiz bedeni, olgunlaşmış insan yapısını ve herkesin birlikte hazır bulunmasını aynı bütünlük düşüncesinde birleştirir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه جمعاء للبهيمة التي لم يذهب من بدنها شيء، وجميع وأجمعون وجمع في التوكيد والكلية، والرجل المجتمع أو الجميع في خلقه، والجارية جمعت الثياب.","what_is_not_ar":"لا يدخل فيه مجرد جماعة الناس إلا إذا كان المقصود الكل أو تمام الذات."},"support_links":["sup_117f89a299628d50d2fa"]},{"boundary":"Bu anlam yalnız belirtilen yapılarda geçerlidir; genel toplama eylemi veya salt kesin karar anlamı değildir.","branch_kind":"collocation","branch_ref":"root_000259/B010","candidate_links":[{"candidate_id":"cand_5e3300fe786cdc2333f6","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَمْع","morph_features":"STEM|POS:N|LEM:jamoE|ROOT:jmE|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:5:3:1","qac_word_ref":"100:5:3","surface_ar":"جَمْعًا"}],"gloss":"parçaları toplanıp tamamlanma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yalnız belirtilen yapılarda parçalar veya güçler bir araya gelerek tamamlanmış bir duruma ulaşır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Atın koşusu ve gücü toparlanarak bütün hızına erişir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sel çeşitli yerlerden gelen suların birleşmesiyle toplanır."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kişinin işleri onun yararına hazırlanıp yoluna girer."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız atın koşusu, sel ve kişinin işleriyle ilgili belirtilen yapılarda toparlanıp tam işlerliğe erişmeyi karşılar.","boundary_detail":"Bu anlam yalnız belirtilen yapılarda geçerlidir; genel toplama eylemi veya salt kesin karar anlamı değildir.","branch_image_ar":"استجماع القوة أو السير حتى تتلاحق أجزاؤه","concept_gloss":"parçaları toplanıp tamamlanma","contextual_glosses":[{"applicability":"Atın koşusunun toparlanıp tam hız ve güce eriştiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Koşunun ayrı güçlerinin birleşip tam düzeye erişmesini korur."},"facet_ids":["F002"],"text":"bütün gücünü toplayıp koşmak","usage_role":"contextual"}],"definition":"Belirtilen yapılarda ayrı güçlerin veya parçaların toplanarak tam işlerlik kazanmasıdır: koşu bütün gücüne erişir, sel birleşir ya da işler hazır hâle gelir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yalnız belirtilen yapılarda parçalar veya güçler bir araya gelerek tamamlanmış bir duruma ulaşır."},{"facet_id":"F002","role":"specialization","statement":"Atın koşusu ve gücü toparlanarak bütün hızına erişir."},{"facet_id":"F003","role":"specialization","statement":"Sel çeşitli yerlerden gelen suların birleşmesiyle toplanır."},{"facet_id":"F004","role":"specialization","statement":"Kişinin işleri onun yararına hazırlanıp yoluna girer."}],"identity_rationale":"Kaynak ifadesi atın koşusunun güçlenmesi, selin çeşitli yerlerden birleşmesi ve işlerin kişi için hazırlanmasını aynı toparlanıp tamamlanma görüntüsünde verir.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"koşusunu ve gücünü bütünüyle toplamak"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"çeşitli yerlerden birleşip büyümek"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"işlerin kişi için yoluna girip hazır duruma gelmesi"}],"lexicalization_note":"Tanım yalnız atın koşusu, sel ve kişinin işleriyle kurulan üç özel yapıya bağlıdır; çıplak kök anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; özel yapılardaki sonuçsal toparlanma ile genel toplama eylemi arasındaki sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal koşu, sel ve işler için sonuçsal toparlanmaya bağlıdır; komşu dal genel ve etkili bir toplama eylemidir.","focus_only":"Yalnız belirli yapılarda güçlerin veya parçaların kendiliğinden toparlanıp tamamlanmasını anlatır.","gloss":"dağınık parçaları bir araya toplama","neighbor_only":"Bir öznenin dağınık şeyleri yaklaştırıp bir araya getirdiği genel eylemdir.","neighbor_ref":"root_000259/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da ayrı parçaların bir araya gelmesi ortak görüntüdür."}],"source_phrase_ar":"استجمع الفرس جريا (maqayis)؛ استجمع للمرء أموره (ayn)؛ استجمع السيل اجتمع من كل موضع واستجمع الفرس جريا (sihah)","source_summary":"Kaynaklar aynı yapıyı üç alanda tanıklar: koşunun güç toplaması, suyun çeşitli yönlerden birleşmesi ve işlerin kişi için hazırlanması.","sources":["MQ","AY","SI"],"what_is_ar":"يدخل فيه استجمع الفرس جريا، واستجمع السيل، واستجمع الأمر للمرء أي تهيأ له واجتمع.","what_is_not_ar":"لا يدخل فيه العزم الإرادي المحكم إذا عبر عنه بأجمع الأمر."},"support_links":["sup_48c540562d2c52a8dff9"]},{"boundary":"Dal bir avuç meyve veya ağaçların bir yerde toplanması değil, adı bilinmeyen çekirdekten yetişme hurma türüdür.","branch_kind":"bare","branch_ref":"root_000259/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَمْع","morph_features":"STEM|POS:N|LEM:jamoE|ROOT:jmE|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:5:3:1","qac_word_ref":"100:5:3","surface_ar":"جَمْعًا"}],"gloss":"adı bilinmeyen çekirdekten yetişme hurma ağacı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ağaç çekirdekten yetişir ve türünün özel adı bilinmez."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çekirdekten yetiştiği için belirli çeşidi veya özel adı bilinmeyen hurma ağacını karşılar.","boundary_detail":"Dal bir avuç meyve veya ağaçların bir yerde toplanması değil, adı bilinmeyen çekirdekten yetişme hurma türüdür.","branch_image_ar":"نخل دقل اجتمع من النوى لا يعرف اسمه","concept_gloss":"adı bilinmeyen çekirdekten yetişme hurma ağacı","contextual_glosses":[{"applicability":"Ağacın yetişme biçimi ile çeşidinin bilinmemesi birlikte açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çekirdekten çıkma ve özel bir çeşit adı taşımama yönlerini korur."},"facet_ids":["F001"],"text":"çekirdekten çıkmış adsız hurma ağacı","usage_role":"explanatory"}],"definition":"Çekirdekten yetişmiş ve özel adı ya da çeşidi bilinmeyen, düşük nitelikli sayılabilen hurma ağacı türüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ağaç çekirdekten yetişir ve türünün özel adı bilinmez."}],"identity_rationale":"Kaynak ifadesi çekirdekten kendiliğinden yetişmiş, adı veya çeşidi bilinmeyen düşük nitelikli hurma ağacını doğrudan tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"adı bilinmeyen çekirdekten yetişme hurma ağacı"}],"lexicalization_note":"Tanım çıplak dalın hurma ağacı türü anlamıyla sınırlıdır ve miktar bildiren bir avuç meyve anlamını içermez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı ağaç türü alanındaki yetişme yolu ve adsızlık farkı en güçlü karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal çekirdekten yetişme ve adının bilinmemesiyle sınırlıdır; komşu dal daha genel bir ağaç ve meyve türünü anlatır.","focus_only":"Çekirdekten yetişmiş olmayı ve özel çeşit adının bilinmemesini birlikte gerektirir.","gloss":"düşük nitelikli hurma ağacı ve meyvesi","neighbor_only":"Düşük nitelikli hurma ağacı veya meyvesini, yetişme yoluna ve adsızlığa bağlamadan kapsar.","neighbor_ref":"root_001387/B005","relation_type":"near_synonym","shared_zone":"İki dal da düşük nitelikli sayılan bir hurma ağacı türünü gösterebilir."}],"source_phrase_ar":"الجمع كل لون من النخل لا يعرف اسمه لنخل خرج من النوى (maqayis)؛ الجمع أيضا الدقل لنخل يخرج من النوى ولا يعرف اسمه (sihah)","source_summary":"Kaynaklar sözü çekirdekten çıkan, adı bilinmeyen hurma ağacı çeşidi olarak açıklar ve bunu düşük nitelikli hurma sınıfıyla ilişkilendirir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه الجمع بمعنى الدقل أو كل لون من النخل خرج من النوى ولا يعرف اسمه.","what_is_not_ar":"لا يدخل فيه جمعة من تمر بمعنى قبضة، ولا مطلق جمع النخل في مكان."},"support_links":[]},{"boundary":"Dal her türlü kap veya doluluk değil, özellikle büyük bir kazanı niteleyen boyut anlamıdır.","branch_kind":"bare","branch_ref":"root_000259/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَمْع","morph_features":"STEM|POS:N|LEM:jamoE|ROOT:jmE|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:5:3:1","qac_word_ref":"100:5:3","surface_ar":"جَمْعًا"}],"gloss":"büyük kazan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kazan, ayırt edici biçimde büyük bir boyuta sahiptir."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kazanın türünden veya yapıldığı maddeden çok olağandışı büyüklüğünün öne çıktığı kullanımı karşılar.","boundary_detail":"Dal her türlü kap veya doluluk değil, özellikle büyük bir kazanı niteleyen boyut anlamıdır.","branch_image_ar":"عظم الشيء كأنه جامع ممتلئ","concept_gloss":"büyük kazan","contextual_glosses":[{"applicability":"Kısa ve doğal bir nitelemeyle kazanın büyük boyutunun anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesnenin kazan oluşunu ve büyük boyutunu birlikte korur."},"facet_ids":["F001"],"text":"iri kazan","usage_role":"contextual"}],"definition":"Boyutu olağandan büyük olan bir kazandır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kazan, ayırt edici biçimde büyük bir boyuta sahiptir."}],"identity_rationale":"Kaynak ifadesi iki söz biçiminin de büyük boyutlu kazanı nitelediğini açık ve ortak biçimde bildirir.","lexical_glosses":[{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"büyük kazan"}],"lexicalization_note":"Tanım çıplak dalda tanıklanan büyük kazan anlamını korur ve komşu kökün benzer sesli biçimlerini içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kap türünü paylaşan fakat boyut ile malzeme bakımından ayrılan aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal boyuta göre belirlenir; komşu dal ise taş malzemeye ve bunun işçiliğine göre belirlenir.","focus_only":"Kazanın büyük boyutlu olmasını belirtir, yapıldığı maddeyi sınırlamaz.","gloss":"taş kazan ve yapımcısı","neighbor_only":"Kabın taştan yapılmış olmasını ve bu kapların üreticisini de kapsar.","neighbor_ref":"root_000110/B006","relation_type":"same_field","shared_zone":"İki dal da yemek veya sıvı için kullanılan kazan türünü adlandırır."}],"source_phrase_ar":"قدر جماع وجامعة وهي العظيمة (maqayis)؛ قدر جامعة وهي العظيمة وقدر جماع أيضا للعظيمة (sihah)","source_summary":"Kaynaklar iki niteleme biçimini aynı açıklamayla verir ve her ikisini de büyük kazan anlamında birleştirir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه قدر جماع أو جامعة بمعنى القدر العظيمة.","what_is_not_ar":"لا يدخل فيه جمل أو جمال من الجذر المجاور ج م ل."},"support_links":[]},{"boundary":"Dal ikinci bir katılımcı ve ortak bir iş gerektirir; cinsel birleşme veya tek başına karar verme anlamı taşımaz.","branch_kind":"collocation","branch_ref":"root_000259/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَمْع","morph_features":"STEM|POS:N|LEM:jamoE|ROOT:jmE|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:5:3:1","qac_word_ref":"100:5:3","surface_ar":"جَمْعًا"}],"gloss":"bir işte başkasıyla birleşip destek olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi başka biriyle aynı iş üzerinde birleşir ve onun yanında yer alır."}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin başka biriyle belirli bir iş üzerinde aynı yönde davranıp onun yanında yer aldığı durumları karşılar.","boundary_detail":"Dal ikinci bir katılımcı ve ortak bir iş gerektirir; cinsel birleşme veya tek başına karar verme anlamı taşımaz.","branch_image_ar":"ممالأة واجتماع مع غيرك على أمر","concept_gloss":"bir işte başkasıyla birleşip destek olma","contextual_glosses":[{"applicability":"İki kişinin aynı iş için birlikte hareket edip birbirini desteklediği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ortak iş üzerinde birleşme ve birlikte davranma ilişkisini korur."},"facet_ids":["F001"],"text":"bir işte güç birliği yapmak","usage_role":"general"}],"definition":"Belirli bir işte başka biriyle birleşip aynı yönde davranma ve ona destek olmadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi başka biriyle aynı iş üzerinde birleşir ve onun yanında yer alır."}],"identity_rationale":"Kaynak ifadesi bir kişinin başka biriyle belirli bir iş üzerinde birleşmesini ve ona destek vermesini iki anlatımla doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"bir işte başkasıyla birleşip ona destek olmak"}],"lexicalization_note":"Tanım yalnız bir kişiyle belirli bir iş üzerinde birleşme yapısına bağlıdır; çıplak köke genel ortaklık anlamı verilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ortak işte birleşme çekirdeğini paylaşan fakat kapsamı daha geniş olan aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kişi ve iş ilişkisini açıkça kuran özel yapıdır; komşu dal yardım ve yandaşlığı daha geniş biçimde anlatır.","focus_only":"Belirli bir kişiyle belirli bir iş üzerinde birleşme yapısına sıkıca bağlıdır.","gloss":"yardımlaşıp aynı yanda birleşme","neighbor_only":"Yardım etme ve bir görüşün yanında yer alma anlamlarını daha genel biçimde kapsar.","neighbor_ref":"root_001441/B003","relation_type":"near_synonym","shared_zone":"İki dal da ortak bir işte aynı yönde davranma ve destek olma alanında buluşur."}],"source_phrase_ar":"جامعت الرجل على الأمر مجامعة وجماعا إذا مالأته عليه (jamhara)؛ جامعه على أمر كذا أي اجتمع معه (sihah)","source_summary":"Kaynaklar yapıyı belirli bir iş üzerinde başka biriyle birleşmek, aynı yönde davranmak ve ona destek olmak biçiminde açıklar.","sources":["JA","SI"],"what_is_ar":"يدخل فيه جامعت الرجل على الأمر إذا مالأته عليه، وجامعه على أمر إذا اجتمع معه.","what_is_not_ar":"لا يدخل فيه المجامعة بمعنى المباضعة، ولا إجماع الرأي إذا لم يذكر المشاركة مع شخص آخر."},"support_links":[]},{"boundary":"Anlam, fiziksel orta noktadan ve insanlar arasındaki aracılıktan ayrılır; yalın değerlendirme ile soy ve topluluk içindeki özel kullanımlar birlikte fakat ayrı düzeylerde tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_001646/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَسَطْ","morph_features":"STEM|POS:V|PERF|LEM:wasaTo|ROOT:wsT|3FP","morpheme_role":"STEM","pos":"V","qac_ref":"100:5:1:2","qac_word_ref":"100:5:1","surface_ar":"وَسَطْ"}],"gloss":"adil ve seçkin orta olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Aşırılık ve eksiklikten korunmuş orta, adalet ve ölçülülük bakımından olumlu bir değer taşır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Topluluk veya soy bağlamında orta sayılan kişi, grubun en seçkin ve en itibarlı üyelerinden biridir."}}],"root_ar":"و س ط","root_id":"root_001646","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Adalet, ölçülülük ve olumlu seçkinlik çekirdeğinin birlikte anlatılması gereken genel açıklamalarda kullanılır.","boundary_detail":"Anlam, fiziksel orta noktadan ve insanlar arasındaki aracılıktan ayrılır; yalın değerlendirme ile soy ve topluluk içindeki özel kullanımlar birlikte fakat ayrı düzeylerde tutulur.","branch_image_ar":"العدل والخيار في موضع الوسط","concept_gloss":"adil ve seçkin orta olma","contextual_glosses":[{"applicability":"Davranışın, tutumun veya bir topluluğun aşırılık ile eksiklikten uzaklığı övüldüğünde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Topluluk içindeki seçkinlik ve yüksek itibar özel kullanımını dışarıda bırakır.","preserves":"Adalet, ölçü ve iki aşırı uçtan korunma yönünü korur."},"facet_ids":["F001"],"text":"aşırılıktan uzak adil ve ölçülü","usage_role":"contextual"},{"applicability":"Bir kişinin kendi topluluğu içindeki üstün değeri veya itibarlı soyu anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel adalet ve aşırılıktan uzak ölçülülük çekirdeğini doğrudan anlatmaz.","preserves":"Kişinin topluluk içindeki seçkinliğini ve yüksek itibarını korur."},"facet_ids":["F002"],"text":"topluluğun en seçkinlerinden","usage_role":"contextual"}],"definition":"Aşırılık ile eksiklikten uzak duran adil, dengeli ve ölçülü nitelik; bu olumlu orta oluş, kişi veya topluluk bağlamında en seçkin ve itibarlı olmayı da anlatabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Aşırılık ve eksiklikten korunmuş orta, adalet ve ölçülülük bakımından olumlu bir değer taşır."},{"facet_id":"F002","role":"specialization","statement":"Topluluk veya soy bağlamında orta sayılan kişi, grubun en seçkin ve en itibarlı üyelerinden biridir."}],"identity_rationale":"Kaynak ifadesi, orta olmayı yalnızca konumsal bir özellik olarak değil, aşırılıktan ve eksiklikten korunmuş adalet, ölçülülük ve seçkinlik olarak açıkça kurar. Bir topluluğun en değerli veya itibarlı kişisiyle ilgili kullanımlar da bu olumlu değerlendirme çekirdeğinin özel gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"adil, seçkin ve aşırılıktan uzak ölçülü olma"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"en adil veya topluluğun en seçkinlerinden"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"topluluğunda soyu seçkin ve konumu yüksek kişi"}],"lexicalization_note":"Tanım yalın biçimdeki adalet ve ölçülülük çekirdeğini kapsar; topluluğun seçkini ve soyluluk değeri bildiren kalıplaşmış kullanımları bu çekirdeğe bağlı özel yüzler olarak sınırlar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca adil ölçü, seçkinlik ve fiziksel orta sınırlarını doğrudan aydınlatan dört karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak anlam, dengeli konumu adalet ve seçkinlik değeriyle kurar; komşu ise yaşam ve eylem alanlarındaki ölçülü davranışa daha belirgin biçimde bağlıdır.","focus_only":"Adaletin yanı sıra kişi veya topluluk için seçkinlik ve yüksek itibar da bildirir.","gloss":"ölçülü olma","neighbor_only":"Geçim, harcama ve çalışma gibi eylem alanlarında iki aşırı uç arasında kalmayı özellikle kapsar.","neighbor_ref":"root_001230/B003","relation_type":"near_synonym","shared_zone":"Her iki anlam da aşırılık ile eksiklik arasında dengeli ve övülen bir konumu anlatır."},{"boundary_match":"partial","distinction":"Odak anlamın çekirdeği övülen adil denge ve seçkinliktir; komşunun kapsamı fiziksel orta, eşitlik, düzlük ve yansız konumlara da yayılır.","focus_only":"Topluluğun seçkin kişisini ve yüksek soy itibarını anlatan değerlendirme uzantısına sahiptir.","gloss":"orta ve adil olma","neighbor_only":"Eşit, düz, belirli ve taraflara göre yansız bir yer veya durum anlamlarını ayrıca taşır.","neighbor_ref":"root_000766/B006","relation_type":"near_synonym","shared_zone":"İki anlam da orta konum ile adalet veya yansızlık arasında bağ kurar."},{"boundary_match":"partial","distinction":"Odak anlamda olumlu değer orta ve adil denge üzerinden kurulur; komşu anlam bu konumsal veya ölçülü olma şartı bulunmadan genel iyilik ve seçilmişlik bildirir.","focus_only":"Seçkinliği aşırılıktan uzak adil orta olma düşüncesine bağlar.","gloss":"seçkin ve iyi olma","neighbor_only":"İyilik, güzellik, uygunluk ve bir şeyi seçme sonucu üstün sayılma gibi daha geniş değerleri kapsar.","neighbor_ref":"root_000452/B002","relation_type":"near_synonym","shared_zone":"Her iki anlam kişi veya şey için olumlu değer ve seçkinlik bildirebilir."},{"boundary_match":"field_only","distinction":"Odak dal değerlendirme ve övgü bildirirken komşu dal yalnızca taraflar arasındaki yeri belirler; fiziksel ortada bulunmak tek başına adalet veya seçkinlik doğurmaz.","focus_only":"Orta olmayı adalet, ölçü ve seçkinlik bakımından değerlendirir.","gloss":"değer olarak orta ile konum olarak orta","neighbor_only":"Bir şeyin uçları veya sıralı parçaları arasında bulunan fiziksel ya da düzen içi konumu gösterir.","neighbor_ref":"root_001646/B002","relation_type":"near_neighbor","shared_zone":"İki dal da orta düşüncesini temel alır."}],"source_phrase_ar":"بناء صحيح يدل على العدل والنصف، وأعدل الشيء أوسطه (maqayis)؛ فلان وسيط الحسب في قومه (ayn)؛ الوسط من كل شيء أعدله، أمة وسطا أي عدلا (sihah)؛ وسطا عدلا، خيارا، أوسط قومه أي من خيارهم (tahdhib)؛ يستعمل استعمال القصد المصون عن الإفراط والتفريط، فيمدح به نحو السواء والعدل والنصفة (mufradat)","source_summary":"Kaynaklar, ortanın adalet ve dengeli ölçü bakımından övülen bir değer olduğunu; kişi ve topluluk söz konusu olduğunda seçkinlik ve yüksek konum bildirebildiğini birlikte destekler.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الوسط بمعنى العدل والخيار والقصد المصون عن الإفراط والتفريط، ومنه أمة وسطا، وأوسط القوم أو وسيط الحسب بمعنى خيارهم وأرفعهم محلا.","what_is_not_ar":"ليس هو مجرد الموضع الحسي بين الطرفين، ولا المرتبة المتوسطة المذمومة، ولا الوساطة بين الناس."},"support_links":[]},{"boundary":"Bu dal konumu bildirir; adalet değeri, ortaya girme eylemi, aracılık ve bir şeyi iki eşit parçaya kesme işlemi tanımın dışında kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_001646/B002","candidate_links":[{"candidate_id":"cand_5e3300fe786cdc2333f6","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَسَطْ","morph_features":"STEM|POS:V|PERF|LEM:wasaTo|ROOT:wsT|3FP","morpheme_role":"STEM","pos":"V","qac_ref":"100:5:1:2","qac_word_ref":"100:5:1","surface_ar":"وَسَطْ"}],"gloss":"uçlar veya parçalar arasındaki orta yer","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Orta, iki uç arasında ya da bir bütünün sıralı parçaları içinde bulunan konumdur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Takının merkez taşı, orta parmak ve sıralamada orta sayılan ibadet bu konumun yapıya bağlı özel uygulamalarıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir şehir adı, iki başka yer arasındaki konumuna dayanan bir adlandırma olarak açıklanır."}}],"root_ar":"و س ط","root_id":"root_001646","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel bir bütünün ya da düzenli bir sıranın orta konumu genel olarak açıklanırken kullanılır.","boundary_detail":"Bu dal konumu bildirir; adalet değeri, ortaya girme eylemi, aracılık ve bir şeyi iki eşit parçaya kesme işlemi tanımın dışında kalır.","branch_image_ar":"موضع الوسط بين الأطراف","concept_gloss":"uçlar veya parçalar arasındaki orta yer","contextual_glosses":[{"applicability":"Bir nesnenin, yerin, beden bölümünün veya topluluğun içindeki orta nokta kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sıra ve özel adlandırmalardaki bütün uygulamaları tek başına göstermez.","preserves":"Bir bütünün uçları arasında bulunan merkezi konumu doğal biçimde korur."},"facet_ids":["F001"],"text":"tam ortası","usage_role":"contextual"},{"applicability":"Bir dizinin veya takının ortasında yer alan belirgin parça anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel yer anlamını ve diğer özel uygulamaları dışarıda bırakır.","preserves":"Sıralı bir bütün içindeki merkez parça konumunu korur."},"facet_ids":["F002"],"text":"merkezdeki parça","usage_role":"contextual"}],"definition":"Bir şeyin iki ucu arasında veya sıralı parçaları içinde bulunan orta yer; belirli nesne, beden bölümü, sıra ve yer adlandırmalarında bu konuma bağlı özel karşılıklar kazanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Orta, iki uç arasında ya da bir bütünün sıralı parçaları içinde bulunan konumdur."},{"facet_id":"F002","role":"specialization","statement":"Takının merkez taşı, orta parmak ve sıralamada orta sayılan ibadet bu konumun yapıya bağlı özel uygulamalarıdır."},{"facet_id":"F003","role":"associated_use","statement":"Bir şehir adı, iki başka yer arasındaki konumuna dayanan bir adlandırma olarak açıklanır."}],"identity_rationale":"Kaynak ifadesi, iki uç arasında veya sıralı parçalar içinde bulunan yeri açıkça temel anlam yapar. Başın ve topluluğun ortası, kolyenin merkez taşı, orta parmak, sıralamadaki orta ibadet ve iki yer arasındaki konumuna göre adlandırılan şehir bu konumsal çekirdeğin farklı uygulamalarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"iki uç veya parçalar arasındaki orta yer"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kolyenin ortasındaki değerli taş"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"orta parmak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"sıralamadaki yerine göre orta sayılan ibadet"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"iki kent arasındaki konumundan adını alan şehir"}],"lexicalization_note":"Yalın biçimin iki uç veya parçalar arasındaki yer anlamı tanımın çekirdeğidir; takı, parmak, ibadet sırası ve şehir adıyla ilgili kullanımlar kendi yapılarıyla sınırlı özel gerçekleşmelerdir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel fiziksel orta, yarıya erişme, ortaya yönelen eylem ve değer yüklü orta ile sınırı en açık gösteren dört aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal orta konumu genel ve düzen içi bir ilişki olarak kurar; komşu dal aynı bölgeyi adlandırmakla birlikte renk işareti ve göksel ad gibi kendine özgü uzantılar taşır.","focus_only":"Sıralı parçalar, beden bölümü, takı ve ibadet düzenindeki orta konumu da kapsar.","gloss":"bir şeyin ortası","neighbor_only":"Hayvanın gövdesindeki renk işareti ve göksel adlandırma gibi özel uzantıları vardır.","neighbor_ref":"root_000276/B001","relation_type":"near_synonym","shared_zone":"Her iki anlam da bir bütünün uçları arasında kalan fiziksel orta bölgeyi gösterebilir."},{"boundary_match":"partial","distinction":"Odak anlam orta yerin kendisidir; komşu anlam ise süreç içinde o yere veya miktarın yarısına erişmeyi anlatır.","focus_only":"Orta yerde bulunmayı bir konum veya bölüm olarak adlandırır.","gloss":"orta yer ve yarıya ulaşma","neighbor_only":"Bir miktarın, zamanın veya yolun yarısına ulaşma olayını bildirir.","neighbor_ref":"root_001511/B002","relation_type":"near_neighbor","shared_zone":"İki anlam da bir bütünün yarısı veya orta noktasıyla ilişkilidir."},{"boundary_match":"partial","distinction":"Odak dal durağan konumu, komşu dal ise o konuma geçişi ya da başka bir şeyi o konuma getirme işlemini anlatır.","focus_only":"İki uç arasındaki yerin kendisini adlandırır.","gloss":"orta yer ve ortaya girme","neighbor_only":"Bir kişinin ortaya girmesini veya bir şeyin ortaya yerleştirilmesini eylem olarak bildirir.","neighbor_ref":"root_001646/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da hedef veya referans noktası orta konumdur."},{"boundary_match":"field_only","distinction":"Bir şeyin ortada bulunması odak dal için yeterlidir; komşu dalda ise bu orta oluşun adil, ölçülü veya seçkin bir değer taşıması gerekir.","focus_only":"Değer yüklemeksizin uçlar veya parçalar arasındaki yeri belirtir.","gloss":"konumsal orta ve adil orta","neighbor_only":"Orta oluşu adalet, ölçülülük ve seçkinlik bakımından olumlu değerlendirir.","neighbor_ref":"root_001646/B001","relation_type":"near_neighbor","shared_zone":"İki dal da orta kavramına dayanır."}],"source_phrase_ar":"النصف، ضربت وسط رأسه، وسط القوم (maqayis)؛ الوسط مخففا يكون موضعا للشيء، اسما لما بين طرفي كل شيء، واسطة القلادة جوهرة تكون في وسط الكرس المنظوم (ayn)؛ الأصبع الوسطى، واسطة القلادة، واسط بلد سمي بالقصر بين الكوفة والبصرة (sihah)؛ ما كان يبين جزء من جزء فهو وسط، وسط الدار، واسطة القلادة (tahdhib)؛ وسط الشيء ما له طرفان، الصلاة الوسطى بين الركعتين وبين الأربع أو بين صلاة الليل والنهار (mufradat)","source_summary":"Kaynaklar, iki uç veya bir bütünün parçaları arasındaki konumu ortak çekirdek olarak verir ve bu çekirdeği beden, takı, ibadet sırası ve yer adlandırması gibi özel alanlarda örneklendirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه وسط الشيء أو الدار أو الرأس أو القوم، وما كان بين طرفين أو بين أجزاء مرتبة، وواسطة القلادة والأصبع الوسطى والصلاة الوسطى، واسم واسط إذا علل بالوقوع بين موضعين.","what_is_not_ar":"لا يدخل فيه العدل والخيار إلا إذا صرح بهما، ولا فعل الدخول في الوسط، ولا واسط الرحل المختلف فيه، ولا قطع الشيء نصفين."},"support_links":["sup_48c540562d2c52a8dff9"]},{"boundary":"Dal, orta yerin kendisini değil o yere girme veya bir şeyi oraya koyma eylemini anlatır; insanlar arasında aracılık etme anlamını içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_001646/B003","candidate_links":[{"candidate_id":"cand_d02865cfa158ca726614","lane":"micro"},{"candidate_id":"cand_3a071dc4f4719f1ba1b0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَسَطْ","morph_features":"STEM|POS:V|PERF|LEM:wasaTo|ROOT:wsT|3FP","morpheme_role":"STEM","pos":"V","qac_ref":"100:5:1:2","qac_word_ref":"100:5:1","surface_ar":"وَسَطْ"}],"gloss":"ortaya girme veya ortaya yerleştirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, bir topluluğun ortasına girerek onların arasında yer alır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir nesne, yapılan bir işlemle orta konuma getirilir."}}],"root_ar":"و س ط","root_id":"root_001646","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Özne orta konuma geçtiğinde ya da bir nesne işlem yoluyla orta konuma getirildiğinde genel açıklama olarak kullanılır.","boundary_detail":"Dal, orta yerin kendisini değil o yere girme veya bir şeyi oraya koyma eylemini anlatır; insanlar arasında aracılık etme anlamını içermez.","branch_image_ar":"الدخول أو الجعل في الوسط","concept_gloss":"ortaya girme veya ortaya yerleştirme","contextual_glosses":[{"applicability":"Bir kişinin bir topluluğun ortasına girip üyelerin arasında yer alması anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir nesneyi orta konuma yerleştirme işlemini kapsamaz.","preserves":"Topluluğun ortasına geçme ve üyeler arasında bulunma olayını korur."},"facet_ids":["F001"],"text":"aralarına girmek","usage_role":"contextual"},{"applicability":"Bir nesnenin iki yanın veya çevresindekilerin ortasına getirilmesi anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin bir topluluğun ortasına kendisinin girmesini kapsamaz.","preserves":"Nesneyi orta konuma getiren ettirgen işlemi korur."},"facet_ids":["F002"],"text":"ortaya yerleştirmek","usage_role":"contextual"}],"definition":"Bir topluluğun ortasına girip aralarında yer almak veya bir şeyi iki yanın ya da çevresindekilerin ortasına yerleştirmek.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, bir topluluğun ortasına girerek onların arasında yer alır."},{"facet_id":"F002","role":"core","statement":"Bir nesne, yapılan bir işlemle orta konuma getirilir."}],"identity_rationale":"Kaynak ifadesi iki bağlantılı işlemi açıkça verir: kişinin bir topluluğun ortasına girmesi ve bir nesnenin ortaya yerleştirilmesi. Bunlar orta konumu adlandıran durağan anlamdan farklı, hedefi orta olan geçişli veya geçişsiz eylemlerdir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"topluluğun ortasına girip aralarında yer almak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir şeyi ortaya yerleştirmek"}],"lexicalization_note":"Topluluğun ortasına girme, belirtilen yapıya bağlı bir kullanımdır; bir şeyi ortaya yerleştiren biçim ayrı eylem yüzü olarak korunur ve ikisi durağan yer anlamıyla karıştırılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel içeri girme, içeri sokma, durağan orta yer ve toplumsal aracılık ayrımlarını gösteren dört aday yeterli bulundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak anlamda hedef özellikle ortadır; komşu anlamda herhangi bir iç konum yeterlidir ve bir nesneyi ortaya yerleştirme yüzü bulunmaz.","focus_only":"Girişin hedefini bir şeyin veya topluluğun orta konumuyla sınırlar ve ortaya yerleştirmeyi de kapsar.","gloss":"ortaya girme ve içine girme","neighbor_only":"Orta olma şartı aramadan genel olarak bir şeyin iç kısmına girmeyi bildirir.","neighbor_ref":"root_000279/B003","relation_type":"near_neighbor","shared_zone":"Her iki anlam da dışarıdan içerideki bir konuma geçişi anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalda varış noktası ortadır; komşu dalda ise herhangi bir iç konum veya içinden geçirme yeterlidir.","focus_only":"Nesneyi özellikle orta konuma getirir ve öznenin ortaya girmesini de kapsar.","gloss":"ortaya koyma ve içine sokma","neighbor_only":"Bir şeyi başka bir şeyin içine geçirme veya oradan ilerletme gibi daha genel bir işlemdir.","neighbor_ref":"root_000735/B002","relation_type":"near_neighbor","shared_zone":"Her iki anlam bir varlığı belirli bir iç konuma getiren işlem bildirebilir."},{"boundary_match":"partial","distinction":"Odak anlam hareket veya yerleştirme içerir; komşu anlamın gerçekleşmesi için hiçbir hareket ya da konum değişikliği gerekmez.","focus_only":"Orta konuma geçişi veya bir şeyi oraya getirmeyi olay olarak anlatır.","gloss":"ortaya geçiş ve orta yer","neighbor_only":"Orta konumun kendisini durağan bir yer veya sıra bölümü olarak adlandırır.","neighbor_ref":"root_001646/B002","relation_type":"near_neighbor","shared_zone":"Her iki anlam aynı orta konumu referans alır."},{"boundary_match":"thematic_only","distinction":"Odak anlam konumsal bir geçiştir; komşu anlam fiziksel orta konum gerektirmeyen toplumsal bir aracılık görevidir.","focus_only":"Bir topluluğun arasına fiziksel olarak girme veya nesneyi ortaya koyma eylemidir.","gloss":"araya girme ve aracılık etme","neighbor_only":"İnsanlar arasında iletişim ve uzlaşma için aracılık etme işlevini bildirir.","neighbor_ref":"root_001646/B005","relation_type":"thematic","shared_zone":"İki anlamda da birden çok tarafın arasında bulunma sahnesi düşünülebilir."}],"source_phrase_ar":"وسط فلان جماعة من الناس وهو يسطهم إذا صار في وسطهم (ayn)؛ وسطت القوم أسطهم وسطا وسطة أي توسطتهم، التوسيط أن تجعل الشيء في الوسط (sihah)؛ أوسطت القوم ووسطتهم وتوسطتهم بمعنى واحد إذا دخلت وسطهم (tahdhib)","source_summary":"Kaynaklar, topluluğun ortasına girme kullanımı üzerinde birleşir; ayrıca bir şeyi orta konuma getiren ettirgen işlemi aynı eylem alanının ayrı bir yüzü olarak verir.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه وسط القوم أو أوسطهم أو توسطهم إذا دخل وسطهم، والتوسيط بمعنى جعل الشيء في الوسط.","what_is_not_ar":"ليس هو اسم الموضع نفسه ولا الحكم بالعدل أو الخيار ولا الوساطة بين المتخاصمين."},"support_links":["sup_eba78b263c1d1790e977","sup_f66908e1e4897066becf"]},{"boundary":"Orta derece burada her zaman yansız değildir; özellikle kişi hakkında düşük değer ima edebilir, fakat doğrudan en kötü veya değersiz anlamına gelmez.","branch_kind":"bare","branch_ref":"root_001646/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَسَطْ","morph_features":"STEM|POS:V|PERF|LEM:wasaTo|ROOT:wsT|3FP","morpheme_role":"STEM","pos":"V","qac_ref":"100:5:1:2","qac_word_ref":"100:5:1","surface_ar":"وَسَطْ"}],"gloss":"iyi ile kötü arasında orta nitelikte","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Şey veya kişi, iyi ile kötü uçlarının arasında bir nitelik derecesinde bulunur."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi için kullanım, onun iyi sayılma sınırını aşamadığını belirterek küçültücü bir değer kazanabilir."}}],"root_ar":"و س ط","root_id":"root_001646","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin veya kişinin niteliği iki değerlendirme ucu arasında derecelendirildiğinde kullanılır.","boundary_detail":"Orta derece burada her zaman yansız değildir; özellikle kişi hakkında düşük değer ima edebilir, fakat doğrudan en kötü veya değersiz anlamına gelmez.","branch_image_ar":"مرتبة وسطى بين الجيد والرديء","concept_gloss":"iyi ile kötü arasında orta nitelikte","contextual_glosses":[{"applicability":"Bir şeyin niteliği iki uç arasında yansız bir orta derece olarak anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişi hakkında ortaya çıkabilen küçültücü çağrışımı belirtmez.","preserves":"İyi ve kötü uçları arasındaki orta dereceyi açık biçimde korur."},"facet_ids":["F001"],"text":"ne iyi ne kötü","usage_role":"contextual"},{"applicability":"Bir kişinin iyi sayılma sınırının dışında kaldığı küçültücü biçimde ima edildiğinde uygundur.","error_profile":{"adds":null,"collision":"Güncel kullanımda kesin bir nicel ortalamanın altı gibi anlaşılabilir.","fit":"narrowing","loses":"Yansız biçimde iyi ile kötü arasındaki genel orta dereceyi daraltır.","preserves":"Kişiye yönelen küçültücü değerlendirmeyi ve iyiden uzaklığı korur."},"facet_ids":["F002"],"text":"vasatın altında sayılan","usage_role":"contextual"}],"definition":"Nitelik bakımından iyi ile kötü arasında bulunan orta derece; kişi hakkında söylendiğinde iyi sayılma sınırının altında kalmayı ve dolayısıyla küçültücü bir değerlendirmeyi ima edebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Şey veya kişi, iyi ile kötü uçlarının arasında bir nitelik derecesinde bulunur."},{"facet_id":"F002","role":"associated_use","statement":"Kişi için kullanım, onun iyi sayılma sınırını aşamadığını belirterek küçültücü bir değer kazanabilir."}],"identity_rationale":"Kaynak ifadesi, iyi ile kötü arasındaki dereceyi temel alır ve kişi için kullanıldığında iyi sayılma sınırının dışına çıkmış olma yönünde küçültücü bir çağrışım taşıyabileceğini belirtir. Bu nedenle dal, övülen adil orta anlamından bağımsız bir değerlendirme derecesidir.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"iyi ile kötü arasında, kimi bağlamda iyinin altında"}],"lexicalization_note":"Tanım yalnızca yalın dalın iyi ile kötü arasındaki derece ve bağlama göre küçültücü değerlendirme anlamını kapsar; başka yapılara özgü anlam eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ara derece, yaklaşık kalite, övülen orta ve doğrudan düşüklükle sınırı en iyi kuran dört karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal nitelik değerlendirmesine ve olası küçültücü kullanıma bağlıdır; komşu dal farklı alanlardaki ara durumları da kapsayan daha geniş bir yapıdır.","focus_only":"Kişi hakkında iyi sayılma sınırının dışında kalma yönünde küçültücü değer kazanabilir.","gloss":"iki uç arasında orta durumda","neighbor_only":"Sesletim ve tanıklık gibi alanlarda iki biçim veya değer arasında kalan özel durumları da kapsar.","neighbor_ref":"root_000170/B011","relation_type":"near_synonym","shared_zone":"Her iki anlam da iyi ile kötü arasındaki bir ara dereceyi anlatabilir."},{"boundary_match":"partial","distinction":"Odak anlam doğrudan değerlendirme ölçeğinin orta derecesidir; komşu anlamın çekirdeği çeşitli ölçülerde bir sınıra veya miktara yaklaşmadır.","focus_only":"Orta dereceyi iyi ve kötü karşıtlığına göre belirler ve kişi için küçültücüleşebilir.","gloss":"kalitece orta veya yakına düşen","neighbor_only":"Doluluk, sayı, zaman, fiyat ve miktar bakımından bir değere yaklaşmayı da anlatır.","neighbor_ref":"root_001212/B016","relation_type":"near_synonym","shared_zone":"İki anlam kalite bakımından iyi ile kötü arasına yakın bir dereceyi gösterebilir."},{"boundary_match":"opposed","distinction":"Odak dal orta dereceyi sıradan veya küçültücü kılabilir; komşu dal aynı orta düşüncesini olumlu adalet ve üstünlük değeriyle kurar.","focus_only":"İyi ile kötü arasında kalır ve bağlama göre iyilik sınırının dışında sayılabilir.","gloss":"övgüsüz orta ve övülen orta","neighbor_only":"Orta oluşu adalet, ölçülülük ve seçkinlik bakımından açıkça över.","neighbor_ref":"root_001646/B001","relation_type":"polarity_pair","shared_zone":"Her iki dal orta konumu bir değer ölçeğine uygular."},{"boundary_match":"partial","distinction":"Odak dal ara dereceyi korur; komşu dal ise ara konum şartı olmadan doğrudan düşüklük ve istenmezlik bildirir.","focus_only":"İyi ile kötü arasında bir derece bırakır ve mutlaka tümüyle değersiz saymaz.","gloss":"orta nitelik ve düşük nitelik","neighbor_only":"Doğrudan istenmeyen, aşağı ve değersiz görülen şeyi bildirir.","neighbor_ref":"root_001297/B002","relation_type":"near_neighbor","shared_zone":"İki anlam da olumlu değerin altında kalan kişi veya şeyi değerlendirebilir."}],"source_phrase_ar":"شيء وسط أي بين الجيد والردئ (sihah)؛ يقال فيما له طرف محمود وطرف مذموم، ويكنى به عن الرذل، فلان وسط من الرجال تنبيها أنه قد خرج من حد الخير (mufradat)","source_summary":"Kaynaklar orta niteliği iyi ile kötü arasındaki derece olarak verir; toplu ifade ayrıca kişi hakkında bu derecenin iyi olma sınırının altında kalmayı ima edebileceğini gösterir.","sources":["SI","MU"],"what_is_ar":"يدخل فيه وصف الشيء أو الرجل بأنه وسط أي بين الجيد والرديء أو خارج عن حد الخير بحسب طرفي المقابلة.","what_is_not_ar":"لا يدخل فيه الوسط الممدوح بمعنى العدل والخيار، ولا الموضع الحسي بين الطرفين."},"support_links":[]},{"boundary":"Anlam yalnızca insanlar arasında aracılık etmeyi bildiren yapıda geçerlidir; ortaya girmek, ortada durmak veya genel olarak uzlaştırmak tek başına bu dalı karşılamaz.","branch_kind":"collocation","branch_ref":"root_001646/B005","candidate_links":[{"candidate_id":"cand_3491206cad5a8f64ba6b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَسَطْ","morph_features":"STEM|POS:V|PERF|LEM:wasaTo|ROOT:wsT|3FP","morpheme_role":"STEM","pos":"V","qac_ref":"100:5:1:2","qac_word_ref":"100:5:1","surface_ar":"وَسَطْ"}],"gloss":"insanlar arasında aracılık etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, insanlar veya taraflar arasında bağlantı kuran aracı rolünü üstlenir."}}],"root_ar":"و س ط","root_id":"root_001646","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin iki veya daha çok insan ya da taraf arasında aracı rolü üstlendiği bağlamlarda kullanılır.","boundary_detail":"Anlam yalnızca insanlar arasında aracılık etmeyi bildiren yapıda geçerlidir; ortaya girmek, ortada durmak veya genel olarak uzlaştırmak tek başına bu dalı karşılamaz.","branch_image_ar":"الوساطة بين الناس","concept_gloss":"insanlar arasında aracılık etme","contextual_glosses":[{"applicability":"Taraflar arasında iletişim kurma veya anlaşmalarına yardım etme amacı belirgin olduğunda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uzlaşma hedefi taşımayan daha genel aracılık durumlarını dışarıda bırakabilir.","preserves":"İnsanlar arasında etkin bir aracı olma işlevini korur."},"facet_ids":["F001"],"text":"arabuluculuk etmek","usage_role":"contextual"}],"definition":"İnsanlar veya taraflar arasında bağlantı kurmak, söz taşımak ya da bir sonuca ulaşmalarına yardım etmek üzere aracılık etmek.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, insanlar veya taraflar arasında bağlantı kuran aracı rolünü üstlenir."}],"identity_rationale":"Tek kaynak ifadesi, insanlar arasında bulunmayı konumsal bir durum olarak değil, taraflar arasında aracılık ve girişimde bulunma işi olarak açıkça tanımlar. Dalın yapıya bağlı kapsamı korununca fiziksel orta yer ve soy itibarı anlamlarıyla karışmaz.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"insanlar arasında aracılık etmek"}],"lexicalization_note":"Tanım, insanlar arasında aracılık etmeyi bildiren belirli yapıya bütünüyle bağlıdır ve bundan yalın biçim için genel bir anlam çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; elçilik türü aracı rol, başkası adına girişim, arayı düzeltme ve fiziksel ortaya girme ile sınırı gösteren dört aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal aracılık etme işidir; komşu dal ise arada bulunan kişinin elçilik veya ayırıcı bağlantı niteliğini daha belirgin biçimde öne çıkarır.","focus_only":"Aracılık işini genel olarak insanlar veya taraflar arasında yürütülen bir etkinlik olarak adlandırır.","gloss":"iki taraf arasında aracı olma","neighbor_only":"İki kişi arasında elçi, perdeleyici kişi veya aradaki somut bağlantı olma rolünü özellikle betimler.","neighbor_ref":"root_000674/B005","relation_type":"near_synonym","shared_zone":"Her iki anlam da iki kişi veya taraf arasında bağlantı kuran bir aracı rolünü anlatır."},{"boundary_match":"partial","distinction":"Odak dal taraflar arası aracı konumudur; komşu dal belirli bir kişi adına destek ve talepte bulunma yönü taşır.","focus_only":"Taraflardan birinin lehine konuşma şartı olmadan aralarında aracılık etmeyi kapsar.","gloss":"aracılık ve başkası için girişim","neighbor_only":"Bir başkası için istekte bulunmayı, onun lehine konuşmayı veya ona yardım etmeyi gerektirir.","neighbor_ref":"root_000802/B002","relation_type":"near_neighbor","shared_zone":"İki anlam da bir kişinin başkaları arasındaki ilişkiye söz veya yardım yoluyla katılmasını içerir."},{"boundary_match":"field_only","distinction":"Odak dalın çekirdeği aracı roldür; komşu dalın çekirdeği iyilikte bulunma veya bozulan ilişkiyi düzeltmedir.","focus_only":"Aracılık, uzlaşma gerçekleşmese ve ayrıca iyilik yapılmasa da kurulabilir.","gloss":"aracılık ve arayı düzeltme","neighbor_only":"İyilik yapmayı ve özellikle iki kişi arasını düzeltmeyi sonuç veya amaç olarak içerir.","neighbor_ref":"root_000690/B005","relation_type":"same_field","shared_zone":"Her iki anlam insanlar arasındaki ilişkiye üçüncü kişinin yapıcı katılımını kapsayabilir."},{"boundary_match":"thematic_only","distinction":"Odak dal işlevsel ve toplumsal aracılıktır; komşu dal yalnızca konumsal geçiş veya yerleştirme içerir.","focus_only":"İletişim veya sonuç sağlamak için insanlar arasında toplumsal bir görev üstlenir.","gloss":"aracılık ve ortaya girme","neighbor_only":"Bir topluluğun ortasına fiziksel olarak girmeyi veya nesneyi ortaya koymayı anlatır.","neighbor_ref":"root_001646/B003","relation_type":"thematic","shared_zone":"İki anlamda da birden çok kişinin arasında bulunma sahnesi oluşabilir."}],"source_phrase_ar":"التوسط بين الناس، من الوساطة (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Yapı, insanlar arasında bağlantı kurup aracılık etme işini anlatır."}],"source_summary":"Tek kaynak, yapıyı insanlar arasında aracılık etme ve taraflar arasında girişimde bulunma anlamında tanıklar.","sources":["SI"],"what_is_ar":"يدخل فيه التوسط بين الناس بمعنى الوساطة والسعي بين الأطراف.","what_is_not_ar":"لا يدخل فيه مجرد الوجود في الوسط المكاني ولا شرف الحسب."},"support_links":["sup_4e72a3a36834bba7f1a6"]},{"boundary":"Kesme işlemi iki yarı oluşturmalıdır; genel kesme, yarma, orta yerde bulunma veya ortaya yerleştirme bu koşul olmadan dalın karşılığı değildir.","branch_kind":"bare","branch_ref":"root_001646/B006","candidate_links":[{"candidate_id":"cand_2d587d089fc28c47cf7e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَسَطْ","morph_features":"STEM|POS:V|PERF|LEM:wasaTo|ROOT:wsT|3FP","morpheme_role":"STEM","pos":"V","qac_ref":"100:5:1:2","qac_word_ref":"100:5:1","surface_ar":"وَسَطْ"}],"gloss":"ortasından kesip ikiye ayırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne, ortasından kesilmesi sonucunda iki yarıya ayrılır."}}],"root_ar":"و س ط","root_id":"root_001646","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesne kesme işlemiyle iki yarıya ayrıldığında kullanılır.","boundary_detail":"Kesme işlemi iki yarı oluşturmalıdır; genel kesme, yarma, orta yerde bulunma veya ortaya yerleştirme bu koşul olmadan dalın karşılığı değildir.","branch_image_ar":"قطع الشيء نصفين","concept_gloss":"ortasından kesip ikiye ayırma","contextual_glosses":[{"applicability":"Kesme çizgisinin ortadan geçtiği ve sonuçta iki yarı oluştuğu bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesnenin ortadan kesilmesini ve iki yarı elde edilmesini açıkça korur."},"facet_ids":["F001"],"text":"iki eşit parçaya kesmek","usage_role":"contextual"}],"definition":"Bir şeyi ortasından keserek iki yarıya ayırmak.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne, ortasından kesilmesi sonucunda iki yarıya ayrılır."}],"identity_rationale":"Kaynak ifadesi işlemi açık ve dar biçimde bir şeyi iki yarıya kesmek olarak tanımlar. Orta nokta işlemin sınırını belirlese de anlam, orta yerin kendisi veya bir nesneyi ortaya koyma değil, kesme sonucunda iki yarı oluşturmadır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir şeyi ortasından kesip iki yarıya ayırmak"}],"lexicalization_note":"Tanım yalın eylemin bir nesneyi iki yarıya ayırma anlamıyla sınırlıdır ve komşu kesme ya da konum anlamlarından ek kapsam almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; iki yarıya ayırma, genel yarma, genel kesme ve durağan orta konum arasındaki sınırları gösteren dört aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnızca keserek iki yarı oluşturma eylemidir; komşu dal yarının kendisini, orta bölümü ve paylaşmayı da kapsayan daha geniş bir alana sahiptir.","focus_only":"Belirli eylem anlamında kesme yoluyla iki yarı oluşturmayı zorunlu kılar.","gloss":"iki yarıya ayırma","neighbor_only":"Yarı, orta, paylaştırma ve malı bölüşme gibi durum ve ilişki anlamlarını da kapsar.","neighbor_ref":"root_000794/B001","relation_type":"near_synonym","shared_zone":"Her iki anlam da bir bütünü iki yarıya ayırma işlemini doğrudan karşılayabilir."},{"boundary_match":"partial","distinction":"Odak anlamın sonucu iki yarıdır; komşu anlamda yarık açılması veya belirsiz sayıda parçaya ayrılma yeterlidir.","focus_only":"Kesmenin ortadan geçmesini ve iki yarı sonucunu gerektirir.","gloss":"ikiye kesme ve yarma","neighbor_only":"Bir şeyi yarma, açma veya kesme işlemini parça sayısı ve eşitlik şartı olmadan kapsar.","neighbor_ref":"root_001175/B001","relation_type":"near_neighbor","shared_zone":"Her iki anlam da bir bütünün kesilerek ayrılmasını anlatır."},{"boundary_match":"partial","distinction":"Odak anlam genel kesmenin özel bir türüdür: işlem ortadan yapılır ve iki yarı doğurur; komşu anlamda bu sınırlar yoktur.","focus_only":"Orta çizgi ve iki yarı oluşması koşullarını birlikte taşır.","gloss":"ikiye kesme ve genel kesme","neighbor_only":"Sonuçtaki parça sayısını veya kesme yerini belirtmeyen genel kesme eylemidir.","neighbor_ref":"root_000172/B004","relation_type":"near_neighbor","shared_zone":"İki anlam da kesme işlemini bildirir."},{"boundary_match":"field_only","distinction":"Odak dalda orta, kesme işleminin çizgisidir ve sonuç iki yarıdır; komşu dalda orta yalnızca bir konumdur.","focus_only":"Orta noktayı kesme sınırı yapıp nesneyi iki parçaya dönüştürür.","gloss":"ortadan kesme ve orta yer","neighbor_only":"İki uç arasındaki orta konumu herhangi bir kesme veya dönüşüm gerektirmeden gösterir.","neighbor_ref":"root_001646/B002","relation_type":"near_neighbor","shared_zone":"İki dal da nesnenin orta noktasını referans alabilir."}],"source_phrase_ar":"التوسيط قطع الشيء نصفين (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"İşlem, nesneyi keserek iki yarıya ayırma sonucunu doğurur."}],"source_summary":"Tek kaynak, eylemi bir nesneyi ortasından kesip iki yarı oluşturmak biçiminde tanıklar.","sources":["SI"],"what_is_ar":"يدخل فيه التوسيط بمعنى قطع الشيء نصفين.","what_is_not_ar":"لا يدخل فيه النصف بوصفه موضع الوسط فقط ولا جعل الشيء في الوسط."},"support_links":["sup_117f89a299628d50d2fa"]},{"boundary":"Bu dalın öğeleri genel kök anlamı gibi genişletilmemeli, birbirinin yerine geçebilen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtta verilen biçim veya bağlam sınırı içinde tutulmalıdır.","branch_kind":"bare","branch_ref":"root_001646/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَسَطْ","morph_features":"STEM|POS:V|PERF|LEM:wasaTo|ROOT:wsT|3FP","morpheme_role":"STEM","pos":"V","qac_ref":"100:5:1:2","qac_word_ref":"100:5:1","surface_ar":"وَسَطْ"}],"gloss":"özel adlandırma kümesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kullanım, başka bir küçük çadır türünden daha büyük olan kıl çadırını adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Diğer kullanım, sütüyle kabı dolduran özel nitelikte bir deveyi adlandırır."}}],"root_ar":"و س ط","root_id":"root_001646","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki dağınık veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu dalın öğeleri genel kök anlamı gibi genişletilmemeli, birbirinin yerine geçebilen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtta verilen biçim veya bağlam sınırı içinde tutulmalıdır.","branch_image_ar":"الوسوط: بيت أو ناقة مخصوصة","concept_gloss":"özel adlandırma kümesi","definition":"Mevcut dal, ortak çekirdeği bulunmayan iki ayrı adlandırmayı birlikte taşır: belirli büyüklükte bir kıl çadırı ve bol süt vererek kabı dolduran bir deve; bunlar ayrı dallar olarak düzenlenmelidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kullanım, başka bir küçük çadır türünden daha büyük olan kıl çadırını adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Diğer kullanım, sütüyle kabı dolduran özel nitelikte bir deveyi adlandırır."}],"identity_rationale":"Bu dal packet düzeyinde inceleme statüsünde tutulmuş sınır-riskli malzemeyi taşır. Kanıt, tek bir yalın kök imgesinden çok biçime veya özel kullanıma bağlı dağınık adlandırmaları gösterdiği için dal yapısal bölme şartı koşmadan sınırlı bir adlandırma kümesi olarak okunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"benzer küçük bir çadırdan daha büyük kıl çadırı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"sütüyle kabı dolduran deve"}],"lexicalization_note":"Kapsam verilen biçim veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"الوسوط بيت من بيوت الشعر أكبر من المظلة، ويقال الوسوط من النوق كالصفوف تملأ الإناء (maqayis)","source_qualifications":[{"kind":"sole_attestation","summary":"Aynı biçim, biri kıl çadırı diğeri bol süt veren deve olan iki ayrı adı taşır."}],"source_summary":"İnceleme statüsündeki kanıt, tek bir birleşik anlamdan çok biçime veya özel bağlama bağlı sınırlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["MQ"],"what_is_ar":"يدخل فيه الوسوط كما عده Maqayis اسما لبيت من بيوت الشعر أكبر من المظلة، وقيل من النوق كالصفوف تملأ الإناء.","what_is_not_ar":"لا يدخل فيه معنى الوسط العام أو العدل أو الدخول في الوسط إلا بدليل مستقل."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["100:5:1"],"branch_refs":[],"candidate_id":"cand_b21378985682cb098023","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:5:1:boundary-continuity","source_type":"word_analysis","support_ids":["sup_0be04e46a840a6c4d717","sup_2def16747d84ecfa86a9"],"title":"ayah boundary stays connected","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:1","qac_refs":["100:5:1:1"],"status":"accepted"}},{"anchor_refs":["100:5:1"],"branch_refs":[],"candidate_id":"cand_3299b00ef363fe2b8cb1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:5:1:fused-launch-cadence","source_type":"word_analysis","support_ids":["sup_2def16747d84ecfa86a9","sup_c5a7e8ba464812b34ae3"],"title":"short connector snaps into the verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:1","qac_refs":["100:5:1:1"],"status":"accepted"}},{"anchor_refs":["100:5:1"],"branch_refs":[],"candidate_id":"cand_9c27c60e4e84a7390b4c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:5:1:immediate-result-sequence","source_type":"word_analysis","support_ids":["sup_2def16747d84ecfa86a9","sup_7a1606f3b0ac38f064bd"],"title":"immediate sequence becomes culminating result","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:1","qac_refs":["100:5:1:1"],"status":"accepted"}},{"anchor_refs":["100:5:1"],"branch_refs":[],"candidate_id":"cand_c99b17dbfd1a6da7600d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:5:1:oath-bridge-before-answer","source_type":"word_analysis","support_ids":["sup_2def16747d84ecfa86a9","sup_c7ddad4b9e0827a7c1a1"],"title":"image closes before the oath answer","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:1","qac_refs":["100:5:1:1"],"status":"accepted"}},{"anchor_refs":["100:5:2"],"branch_refs":[],"candidate_id":"cand_6453407d9cab25ad0794","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001646"],"scope":"focus_ayah","source_local_id":"100:5:2:boundary-and-shape-echo","source_type":"word_analysis","support_ids":["sup_2f35e8f7aba067757991","sup_3c45153ace97fb308f4f"],"title":"verb pivots from dust to target","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:2","qac_refs":["100:5:1:2","100:5:1:3"],"status":"accepted"}},{"anchor_refs":["100:5:2"],"branch_refs":[],"candidate_id":"cand_c25fc96ffbe6271ee83a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001646"],"scope":"focus_ayah","source_local_id":"100:5:2:compact-subject-achieved-action","source_type":"word_analysis","support_ids":["sup_26aaf83395561e5b6c0d","sup_3c45153ace97fb308f4f"],"title":"feminine plural perfect carries the agents forward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:2","qac_refs":["100:5:1:2","100:5:1:3"],"status":"accepted"}},{"anchor_refs":["100:5:2"],"branch_refs":[],"candidate_id":"cand_7cfb440f1bdb5c1c6bdc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001646"],"scope":"focus_ayah","source_local_id":"100:5:2:form-ii-variant-pressure","source_type":"word_analysis","support_ids":["sup_3c45153ace97fb308f4f","sup_4d892b1ecebdb3b15f8c"],"title":"variant intensifies the same center-entry","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:2","qac_refs":["100:5:1:2","100:5:1:3"],"status":"accepted"}},{"anchor_refs":["100:5:2"],"branch_refs":[],"candidate_id":"cand_a3147a3f54e28ef9e09f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001646"],"scope":"focus_ayah","source_local_id":"100:5:2:kinetic-center-entry","source_type":"word_analysis","support_ids":["sup_3c45153ace97fb308f4f","sup_bc01c6666e9f7bc16a7c"],"title":"middle becomes target-penetrating motion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:2","qac_refs":["100:5:1:2","100:5:1:3"],"status":"accepted"}},{"anchor_refs":["100:5:2"],"branch_refs":[],"candidate_id":"cand_deae96ab7197dbe8cffc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001646"],"scope":"focus_ayah","source_local_id":"100:5:2:rare-verbalized-middle","source_type":"word_analysis","support_ids":["sup_3c45153ace97fb308f4f","sup_d83cc107c078f585aee7"],"title":"rare verbal form contrasts with adjectival centrality","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:2","qac_refs":["100:5:1:2","100:5:1:3"],"status":"accepted"}},{"anchor_refs":["100:5:2"],"branch_refs":[],"candidate_id":"cand_2411891158f797558305","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001646"],"scope":"focus_ayah","source_local_id":"100:5:2:sharp-sound-texture","source_type":"word_analysis","support_ids":["sup_3c45153ace97fb308f4f","sup_e8c6f479f0b014c8691f"],"title":"sibilant and emphatic stop sharpen the action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:2","qac_refs":["100:5:1:2","100:5:1:3"],"status":"accepted"}},{"anchor_refs":["100:5:2"],"branch_refs":[],"candidate_id":"cand_4a6bc9767c2bf3c1c731","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001646"],"scope":"focus_ayah","source_local_id":"100:5:2:synthesis-center-as-force","source_type":"word_analysis","support_ids":["sup_3c45153ace97fb308f4f","sup_c4bcfcdb53d8359fe94f"],"title":"center becomes a force point","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:2","qac_refs":["100:5:1:2","100:5:1:3"],"status":"accepted"}},{"anchor_refs":["100:5:3"],"branch_refs":[],"candidate_id":"cand_2bd996ccb4b1fb0919d2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:5:3:adjacent-ayah-pronoun-echo","source_type":"word_analysis","support_ids":["sup_65868c7e9cf71f81511b","sup_8f557933e6f97f2431c7"],"title":"same pronoun binds dust-raising and entry","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:3","qac_refs":["100:5:2:1","100:5:2:2"],"status":"accepted"}},{"anchor_refs":["100:5:3"],"branch_refs":[],"candidate_id":"cand_50ba7ddefd22216f705a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:5:3:ambiguous-masculine-suffix","source_type":"word_analysis","support_ids":["sup_69b0b05e94b879c41440","sup_8f557933e6f97f2431c7"],"title":"masculine suffix narrows but does not resolve the referent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:3","qac_refs":["100:5:2:1","100:5:2:2"],"status":"accepted"}},{"anchor_refs":["100:5:3"],"branch_refs":[],"candidate_id":"cand_3c72cd68071b91d94c5f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:5:3:fused-audible-suffix","source_type":"word_analysis","support_ids":["sup_4646d3836c78282e2a44","sup_8f557933e6f97f2431c7"],"title":"bound pronoun remains audible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:3","qac_refs":["100:5:2:1","100:5:2:2"],"status":"accepted"}},{"anchor_refs":["100:5:3"],"branch_refs":[],"candidate_id":"cand_b372c93d9c9d6e41dc05","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:5:3:instrument-cause-attachment","source_type":"word_analysis","support_ids":["sup_8f557933e6f97f2431c7","sup_fed322fd15de1ba3e7db"],"title":"preposition makes prior material operative","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:3","qac_refs":["100:5:2:1","100:5:2:2"],"status":"accepted"}},{"anchor_refs":["100:5:3"],"branch_refs":[],"candidate_id":"cand_6817af8c863b89e96a88","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:5:3:light-to-heavy-cadence","source_type":"word_analysis","support_ids":["sup_3deeecd32d169b079316","sup_8f557933e6f97f2431c7"],"title":"short hinge releases into heavier closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:3","qac_refs":["100:5:2:1","100:5:2:2"],"status":"accepted"}},{"anchor_refs":["100:5:3"],"branch_refs":[],"candidate_id":"cand_2cd021d652c103387063","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:5:3:verb-target-hinge-position","source_type":"word_analysis","support_ids":["sup_8f557933e6f97f2431c7","sup_9c0d371034ab4cbc79b8"],"title":"middle phrase bridges verb and target","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:3","qac_refs":["100:5:2:1","100:5:2:2"],"status":"accepted"}},{"anchor_refs":["100:5:4"],"branch_refs":[],"candidate_id":"cand_609050e05d7e95f0db19","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000259"],"scope":"focus_ayah","source_local_id":"100:5:4:boundary-scene-shift","source_type":"word_analysis","support_ids":["sup_73c6b3c10d35b37557aa","sup_7f229402eba2b9b29d13"],"title":"dust medium gives way to gathered target","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:4","qac_refs":["100:5:3:1"],"status":"accepted"}},{"anchor_refs":["100:5:4"],"branch_refs":[],"candidate_id":"cand_44fbd97da49d5c7fe701","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000259"],"scope":"focus_ayah","source_local_id":"100:5:4:closure-synthesis","source_type":"word_analysis","support_ids":["sup_48418ed0448a0d7daabb","sup_7f229402eba2b9b29d13"],"title":"case, indefiniteness, and echo converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:4","qac_refs":["100:5:3:1"],"status":"accepted"}},{"anchor_refs":["100:5:4"],"branch_refs":[],"candidate_id":"cand_26aa8f65ac889e8e0064","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000259"],"scope":"focus_ayah","source_local_id":"100:5:4:collective-mass-affected","source_type":"word_analysis","support_ids":["sup_3f59d8ffcfb12b38ae69","sup_7f229402eba2b9b29d13"],"title":"gathered unity becomes the affected mass","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:4","qac_refs":["100:5:3:1"],"status":"accepted"}},{"anchor_refs":["100:5:4"],"branch_refs":[],"candidate_id":"cand_9f954a6afcf4ec2a6b8e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000259"],"scope":"focus_ayah","source_local_id":"100:5:4:final-target-compression","source_type":"word_analysis","support_ids":["sup_7f229402eba2b9b29d13","sup_c050717f2ef799f24f38"],"title":"final noun lands the compact clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:4","qac_refs":["100:5:3:1"],"status":"accepted"}},{"anchor_refs":["100:5:4"],"branch_refs":[],"candidate_id":"cand_65a678afe6ffb43fe93b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000259"],"scope":"focus_ayah","source_local_id":"100:5:4:indefinite-open-gathering","source_type":"word_analysis","support_ids":["sup_3ad3684eb39a3918c622","sup_7f229402eba2b9b29d13"],"title":"tanwin leaves the gathering unspecified","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:4","qac_refs":["100:5:3:1"],"status":"accepted"}},{"anchor_refs":["100:5:4"],"branch_refs":[],"candidate_id":"cand_b8dc2e6b41514029dc85","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000259"],"scope":"focus_ayah","source_local_id":"100:5:4:marked-form-within-common-root","source_type":"word_analysis","support_ids":["sup_7f229402eba2b9b29d13","sup_a382859675e0c65a1613"],"title":"common root appears in a marked local slot","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:4","qac_refs":["100:5:3:1"],"status":"accepted"}},{"anchor_refs":["100:5:4"],"branch_refs":[],"candidate_id":"cand_d97cc0efc46cd6cc33a3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000259"],"scope":"focus_ayah","source_local_id":"100:5:4:object-with-manner-pressure","source_type":"word_analysis","support_ids":["sup_7f229402eba2b9b29d13","sup_ad0bf96b38c751cd088a"],"title":"direct object remains primary while manner pressure survives","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:4","qac_refs":["100:5:3:1"],"status":"accepted"}},{"anchor_refs":["100:5:4"],"branch_refs":[],"candidate_id":"cand_9b65ed7b41d539e1ffc3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000259"],"scope":"focus_ayah","source_local_id":"100:5:4:tanwin-echo-and-heavy-closure","source_type":"word_analysis","support_ids":["sup_7f229402eba2b9b29d13","sup_8d9c6fbcdeb6d971b900"],"title":"cadence echoes dust while meaning reverses direction","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:4","qac_refs":["100:5:3:1"],"status":"accepted"}},{"anchor_refs":["100:5:4"],"branch_refs":[],"candidate_id":"cand_37bcdc137a4f82475509","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000259"],"scope":"focus_ayah","source_local_id":"100:5:4:verbal-noun-result-form","source_type":"word_analysis","support_ids":["sup_7f229402eba2b9b29d13","sup_e12e270d8021811e7265"],"title":"gerund objectifies gatheredness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:5:4","qac_refs":["100:5:3:1"],"status":"accepted"}},{"anchor_refs":["100:5:1"],"branch_refs":[],"candidate_id":"cand_90bcde5e9a6bec8a7952","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001646"],"scope":"focus_ayah","source_local_id":"100:5:1:2","source_type":"qac_morpheme","support_ids":["sup_d805d5da05c0b5b26af0"],"title":"QAC root occurrence: و س ط","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["100:5:3"],"branch_refs":[],"candidate_id":"cand_995c73d17f3240430113","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000259"],"scope":"focus_ayah","source_local_id":"100:5:3:1","source_type":"qac_morpheme","support_ids":["sup_446a5ad721616c0f8a0e"],"title":"QAC root occurrence: ج م ع","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["100:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:5","branch_refs":["root_000259/B002","root_001646/B003"],"candidate_id":"cand_d02865cfa158ca726614","commentary_obligation":"review","hft_ref":"hft_97b18a7b44f08bcc0cee","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:BL-penetrated-collective-center","source_type":"hft","support_ids":["sup_eba78b263c1d1790e977"],"title":"BL-penetrated-collective-center","trust":"legacy_unbound"},{"anchor_refs":["100:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:5","branch_refs":["root_000259/B010","root_001646/B002"],"candidate_id":"cand_5e3300fe786cdc2333f6","commentary_obligation":"review","hft_ref":"hft_91be29b1d347e671ad34","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:BL-concentrated-momentum","source_type":"hft","support_ids":["sup_48c540562d2c52a8dff9"],"title":"BL-concentrated-momentum","trust":"legacy_unbound"},{"anchor_refs":["100:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:5","branch_refs":["root_000259/B001","root_001646/B003"],"candidate_id":"cand_3a071dc4f4719f1ba1b0","commentary_obligation":"review","hft_ref":"hft_253c18cb1263c64711e1","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:BL-entry-reconfigures-whole","source_type":"hft","support_ids":["sup_f66908e1e4897066becf"],"title":"BL-entry-reconfigures-whole","trust":"legacy_unbound"},{"anchor_refs":["100:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:5","branch_refs":["root_000259/B003","root_001646/B005"],"candidate_id":"cand_3491206cad5a8f64ba6b","commentary_obligation":"review","hft_ref":"hft_1e3330952e981f1461c7","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:BL-interposition-in-concert","source_type":"hft","support_ids":["sup_4e72a3a36834bba7f1a6"],"title":"BL-interposition-in-concert","trust":"legacy_unbound"},{"anchor_refs":["100:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:5","branch_refs":["root_000259/B009","root_001646/B006"],"candidate_id":"cand_2d587d089fc28c47cf7e","commentary_obligation":"review","hft_ref":"hft_d8d19a2a10096aeab382","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:BL-center-as-faultline","source_type":"hft","support_ids":["sup_117f89a299628d50d2fa"],"title":"BL-center-as-faultline","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فَوَسَطْنَ بِهِۦ جَمْعًا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"100:5:1:1","qac_word_ref":"100:5:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"وَسَطْ","morph_features":"STEM|POS:V|PERF|LEM:wasaTo|ROOT:wsT|3FP","morpheme_role":"STEM","pos":"V","qac_ref":"100:5:1:2","qac_word_ref":"100:5:1","root_ar":"و س ط","surface_ar":"وَسَطْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"100:5:1:3","qac_word_ref":"100:5:1","root_ar":"","surface_ar":"نَ"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"100:5:2:1","qac_word_ref":"100:5:2","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|3MS","morpheme_role":"STEM","pos":"PRON","qac_ref":"100:5:2:2","qac_word_ref":"100:5:2","root_ar":"","surface_ar":"هِۦ"},{"lemma_ar":"جَمْع","morph_features":"STEM|POS:N|LEM:jamoE|ROOT:jmE|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:5:3:1","qac_word_ref":"100:5:3","root_ar":"ج م ع","surface_ar":"جَمْعًا"}],"word_analysis_qac_refs":[["100:5:1:1"],["100:5:1:2","100:5:1:3"],["100:5:2:1","100:5:2:2"],["100:5:3:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["100:5:1","100:5:2","100:5:3","100:5:4"]},"focus_surface_evidence":{"arabic_uthmani":"فَوَسَطْنَ بِهِۦ جَمْعًا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"100:5:1:1","qac_word_ref":"100:5:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"وَسَطْ","morph_features":"STEM|POS:V|PERF|LEM:wasaTo|ROOT:wsT|3FP","morpheme_role":"STEM","pos":"V","qac_ref":"100:5:1:2","qac_word_ref":"100:5:1","root_ar":"و س ط","surface_ar":"وَسَطْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"100:5:1:3","qac_word_ref":"100:5:1","root_ar":"","surface_ar":"نَ"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"100:5:2:1","qac_word_ref":"100:5:2","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|3MS","morpheme_role":"STEM","pos":"PRON","qac_ref":"100:5:2:2","qac_word_ref":"100:5:2","root_ar":"","surface_ar":"هِۦ"},{"lemma_ar":"جَمْع","morph_features":"STEM|POS:N|LEM:jamoE|ROOT:jmE|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"100:5:3:1","qac_word_ref":"100:5:3","root_ar":"ج م ع","surface_ar":"جَمْعًا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["100:5:1:1"],["100:5:1:2","100:5:1:3"],["100:5:2:1","100:5:2:2"],["100:5:3:1"]],"word_analysis_refs":["100:5:1","100:5:2","100:5:3","100:5:4"],"word_rows":[{"analysis_record_ref":"100:5:1","analytic_gloss_range_en":"immediate connective particle that moves the oath-scene into its culminating center-entry while the oath answer remains pending","analytic_root_gloss_range_en":null,"qac_refs":["100:5:1:1"],"root":{},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"100:5:2","analytic_gloss_range_en":"completed feminine-plural action of entering the middle of a gathered body; mediation and ethical balance remain background contrasts, not the selected local sense","analytic_root_gloss_range_en":"middle-position, choice balance, entering or setting in the middle, mediation, and cutting-in-half branches; the local Form I perfect selects kinetic center-entry","qac_refs":["100:5:1:2","100:5:1:3"],"root":{"arabic":"و س ط","transliteration":"w-s-ṭ"},"surface":{"arabic":"وَسَطْنَ","transliteration":"wasatna"}},{"analysis_record_ref":"100:5:3","analytic_gloss_range_en":"prepositional phrase with an ambiguous masculine singular suffix, functioning as the means, accompaniment, or cause by which the center-entry occurs","analytic_root_gloss_range_en":null,"qac_refs":["100:5:2:1","100:5:2:2"],"root":{},"surface":{"arabic":"بِهِ","transliteration":"bihi"}},{"analysis_record_ref":"100:5:4","analytic_gloss_range_en":"an indefinite accusative verbal noun naming a gathered body or collective gathering, most strongly the object entered by the charge while still allowing collective manner pressure","analytic_root_gloss_range_en":"gathering scattered parts into one whole, assembled groups, totality, concerted resolve, and other construction-bound extensions; the local form selects gathered collective mass","qac_refs":["100:5:3:1"],"root":{"arabic":"ج م ع","transliteration":"j-m-ʿ"},"surface":{"arabic":"جَمْعًا","transliteration":"jam'an"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["100:5"],"branch_refs":["root_000259/B002","root_001646/B003"],"candidate_id":"cand_d02865cfa158ca726614","evidence_scope":"focus_ayah","hft_ref":"hft_97b18a7b44f08bcc0cee","item_id":"BL-penetrated-collective-center","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:BL-penetrated-collective-center","support_id":"sup_eba78b263c1d1790e977"},{"anchor_refs":["100:5"],"branch_refs":["root_000259/B010","root_001646/B002"],"candidate_id":"cand_5e3300fe786cdc2333f6","evidence_scope":"focus_ayah","hft_ref":"hft_91be29b1d347e671ad34","item_id":"BL-concentrated-momentum","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:BL-concentrated-momentum","support_id":"sup_48c540562d2c52a8dff9"},{"anchor_refs":["100:5"],"branch_refs":["root_000259/B001","root_001646/B003"],"candidate_id":"cand_3a071dc4f4719f1ba1b0","evidence_scope":"focus_ayah","hft_ref":"hft_253c18cb1263c64711e1","item_id":"BL-entry-reconfigures-whole","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:BL-entry-reconfigures-whole","support_id":"sup_f66908e1e4897066becf"},{"anchor_refs":["100:5"],"branch_refs":["root_000259/B003","root_001646/B005"],"candidate_id":"cand_3491206cad5a8f64ba6b","evidence_scope":"focus_ayah","hft_ref":"hft_1e3330952e981f1461c7","item_id":"BL-interposition-in-concert","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:BL-interposition-in-concert","support_id":"sup_4e72a3a36834bba7f1a6"},{"anchor_refs":["100:5"],"branch_refs":["root_000259/B009","root_001646/B006"],"candidate_id":"cand_2d587d089fc28c47cf7e","evidence_scope":"focus_ayah","hft_ref":"hft_d8d19a2a10096aeab382","item_id":"BL-center-as-faultline","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:BL-center-as-faultline","support_id":"sup_117f89a299628d50d2fa"}],"diagnostics":[{"warning":"Unrecognized HFT reader field is preserved as a global review record"},{"warning":"Unrecognized HFT reader field is preserved as a global review record"}],"lane_counts":{"global":13,"macro":16,"micro":5},"packet_summary":{"ayah_count":11,"focus_ref":"100:5","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ع د و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000993","furuq_root_norm":"ع د و","furuq_source_root_norm":"ع د و","is_dominant":true,"target_occurrences":68,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":5,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":false,"target_occurrences":4,"target_rank":3}]},{"qac_root":"ث و ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000210","furuq_root_norm":"ث و ر","furuq_source_root_norm":"ث و ر","is_dominant":true,"target_occurrences":4,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000011","furuq_root_norm":"ء ث ر","furuq_source_root_norm":"أ ث ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["100:1","100:2","100:3","100:4","100:5","100:6","100:7","100:8","100:9","100:10","100:11"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"100:5","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v3","reader_id":"reader_hft_a","trace_kind":null}]},"reader_synthesis_count":11,"source_present":true,"structured_insight_count":21,"unstructured_record_count":2},"identity":{"ayah_ref":"100:5","lane":"micro","linguistic_source_ref":"100:5","surface_ref":"100:5","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"100:5","target_tokens":[["Ardından",["100:5:1"]],["onunla",["100:5:2"]],["bir",["100:5:3"]],["topluluğun",["100:5:3"]],["ortasına",["100:5:1","100:5:3"]],["girenlere",["100:5:1"]]],"text":"Ardından onunla bir topluluğun ortasına girenlere:"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":11,"id":"s100-p01-001-011","label":"Whole surah","number":1,"refs":["100:1","100:2","100:3","100:4","100:5","100:6","100:7","100:8","100:9","100:10","100:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:1:boundary-continuity","source_type":"word_analysis","support_id":"sup_0be04e46a840a6c4d717","text":"{\"blocking_evidence\":null,\"headline\":\"ayah boundary stays connected\",\"reader_payoff\":\"The reader feels the 100:4 to 100:5 boundary as one continuous charge rather than a reset after the dust has been raised.\",\"reason\":\"The opening connector repeats the fa-led sequencing mechanism across the boundary and keeps the prior action inside the same motion chain.\",\"representative_source_ids\":[\"QT-03c1c7a1\",\"QT-21bcda98\",\"QE-285e7ab0\",\"QB-fe283e61\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:2:compact-subject-achieved-action","source_type":"word_analysis","support_id":"sup_26aaf83395561e5b6c0d","text":"{\"blocking_evidence\":null,\"headline\":\"feminine plural perfect carries the agents forward\",\"reader_payoff\":\"The reader notices that the same unspoken agents continue the charge and that the center-entry is presented as an achieved act.\",\"reason\":\"QAC and attachment evidence identify a Form I perfect with 3fp agreement, continuing the implicit feminine plural subject from the oath sequence.\",\"representative_source_ids\":[\"QG-3f748925\",\"QG-e7897958\",\"QF-d5d0ba73\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:1","source_type":"word_analysis","support_id":"sup_2def16747d84ecfa86a9","text":"{\"gloss_range\":\"immediate connective particle that moves the oath-scene into its culminating center-entry while the oath answer remains pending\",\"prose\":\"{{ar:فَ}} ({{tr:fa}}) makes 100:5 arrive as the next beat of the same charge, not as a detached sentence after the dust scene. It carries immediate sequence and result together: the prior motion, sparks, dawn raid, and dust now resolve into entry at the center. Because the oath answer is still delayed until 100:6, this particle also keeps the martial image suspended inside the oath architecture. In {{ar:فَوَسَطْنَ}} ({{tr:fa-wasatna}}), the clipped connector is fused directly to the heavier verb, so the final image launches with a compressed forward snap before the explicit human proposition appears.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:2:boundary-and-shape-echo","source_type":"word_analysis","support_id":"sup_2f35e8f7aba067757991","text":"{\"blocking_evidence\":null,\"headline\":\"verb pivots from dust to target\",\"reader_payoff\":\"The reader hears the same agents and a similar clause shape carry the scene from dust-raising into target-centered penetration.\",\"reason\":\"The local verb repeats the feminine plural perfect pattern and combines with {{ar:بِهِ}} ({{tr:bihi}}), matching the prior action's linked structure across the ayah boundary.\",\"representative_source_ids\":[\"QT-3cc1ba1b\",\"QT-72f563a9\",\"QE-941a6252\",\"QE-c3c8488f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:4:indefinite-open-gathering","source_type":"word_analysis","support_id":"sup_3ad3684eb39a3918c622","text":"{\"blocking_evidence\":null,\"headline\":\"tanwin leaves the gathering unspecified\",\"reader_payoff\":\"The reader notices an unnamed, unbounded gathering rather than a specified historical group.\",\"reason\":\"QAC and noun-instance evidence mark the word as an indefinite accusative verbal noun with tanwin.\",\"representative_source_ids\":[\"QG-ba86460f\",\"QF-8a91411d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:2","source_type":"word_analysis","support_id":"sup_3c45153ace97fb308f4f","text":"{\"gloss_range\":\"completed feminine-plural action of entering the middle of a gathered body; mediation and ethical balance remain background contrasts, not the selected local sense\",\"prose\":\"{{ar:وَسَطْنَ}} ({{tr:wasatna}}) turns the root's middle-field into motion: the agents have entered the center of {{ar:جَمْعًا}} ({{tr:jam'an}}), and the direct object makes the gathered body the thing reached and breached. Its feminine plural ending carries the same unspoken oath-subject forward, while the perfect form presents the penetration as already achieved at the scene's climax. The root can mark balance, centrality, mediation, and division elsewhere, but the local object selects kinetic center-entry; that selection is marked because the middle-root is verbalized here rather than left in its more familiar adjectival or comparative field. The reported {{ar:فَوَسَّطْنَ}} ({{tr:fa-wassatna}}) variant intensifies that same pressure without replacing the canonical Form I movement, and the verb's sibilant plus emphatic stop gives the center-entry a narrowed, striking texture. Across the boundary, the same feminine plural perfect pattern and prepositional-pronoun frame carry the scene from dust disturbance into target-centered penetration.\",\"root_display\":\"{{ar:و س ط}} ({{tr:w-s-ṭ}})\",\"root_gloss_range\":\"middle-position, choice balance, entering or setting in the middle, mediation, and cutting-in-half branches; the local Form I perfect selects kinetic center-entry\",\"surface_display\":\"{{ar:وَسَطْنَ}} ({{tr:wasatna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:3:light-to-heavy-cadence","source_type":"word_analysis","support_id":"sup_3deeecd32d169b079316","text":"{\"blocking_evidence\":null,\"headline\":\"short hinge releases into heavier closure\",\"reader_payoff\":\"The reader can feel the brief prepositional phrase move quickly into the heavier final object.\",\"reason\":\"The cadence row is tied to the local sequence {{ar:بِهِ جَمْعًا}} ({{tr:bihi jam'an}}), where the shorter phrase precedes the final noun.\",\"representative_source_ids\":[\"QP-4dbcd96b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:4:collective-mass-affected","source_type":"word_analysis","support_id":"sup_3f59d8ffcfb12b38ae69","text":"{\"blocking_evidence\":null,\"headline\":\"gathered unity becomes the affected mass\",\"reader_payoff\":\"The reader sees the target as many units collected into one body, so entering the middle affects the unity itself.\",\"reason\":\"V4 supports gathering into a collected whole and assembled-body branches, and local grammar makes that collective body the object affected by the verb.\",\"representative_source_ids\":[\"QS-29c77901\",\"QS-94a7cb4a\",\"QS-b7deac82\",\"QF-f6036de6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"100:5:3:1","source_type":"qac_morpheme","support_id":"sup_446a5ad721616c0f8a0e","text":"{\"lemma_ar\":\"جَمْع\",\"morph_features\":\"STEM|POS:N|LEM:jamoE|ROOT:jmE|M|INDEF|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"100:5:3:1\",\"qac_word_ref\":\"100:5:3\",\"root_ar\":\"ج م ع\",\"surface_ar\":\"جَمْعًا\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:3:fused-audible-suffix","source_type":"word_analysis","support_id":"sup_4646d3836c78282e2a44","text":"{\"blocking_evidence\":null,\"headline\":\"bound pronoun remains audible\",\"reader_payoff\":\"The reader hears the antecedent question as part of one dependent word, not as a separate detachable pronoun.\",\"reason\":\"The local word fuses the preposition and bound 3ms suffix; the recited suffix keeps the pronoun's ambiguity audible.\",\"representative_source_ids\":[\"QF-3405faa2\",\"QF-5eade073\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:4:closure-synthesis","source_type":"word_analysis","support_id":"sup_48418ed0448a0d7daabb","text":"{\"blocking_evidence\":null,\"headline\":\"case, indefiniteness, and echo converge\",\"reader_payoff\":\"The reader can hold the final noun as syntactic target, open-ended gathered mass, and audible echo of the dust object at once.\",\"reason\":\"The synthesis is narrowed by attachment evidence: direct object is the primary parse, while indefiniteness and echo remain fully local payoffs.\",\"representative_source_ids\":[\"QY-61156eb9\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:2:form-ii-variant-pressure","source_type":"word_analysis","support_id":"sup_4d892b1ecebdb3b15f8c","text":"{\"blocking_evidence\":null,\"headline\":\"variant intensifies the same center-entry\",\"reader_payoff\":\"The reader can register the variant as apparatus that exposes the verb's pressure point, while the canonical wording remains Form I center-entry.\",\"reason\":\"The aligned local form is Form I {{ar:وَسَطْنَ}} ({{tr:wasatna}}); the reported {{ar:فَوَسَّطْنَ}} ({{tr:fa-wassatna}}) reading may serve as contrast or intensification but does not replace the canonical parse.\",\"representative_source_ids\":[\"QF-2f89d122\",\"QF-f0baabfb\",\"QP-09d37b76\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:3:adjacent-ayah-pronoun-echo","source_type":"word_analysis","support_id":"sup_65868c7e9cf71f81511b","text":"{\"blocking_evidence\":null,\"headline\":\"same pronoun binds dust-raising and entry\",\"reader_payoff\":\"The reader notices that the same ambiguous pronoun carries across 100:4 and 100:5, binding the dust event to the center-entry.\",\"reason\":\"The boundary rows identify the repeated {{ar:بِهِ}} ({{tr:bihi}}), and attachment support keeps the suffix referent unresolved rather than resetting it at 100:5.\",\"representative_source_ids\":[\"QE-213cedaa\",\"QB-3c66ef82\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:3:ambiguous-masculine-suffix","source_type":"word_analysis","support_id":"sup_69b0b05e94b879c41440","text":"{\"blocking_evidence\":null,\"headline\":\"masculine suffix narrows but does not resolve the referent\",\"reader_payoff\":\"The reader sees the pronoun pull earlier material into the clause while refusing to reduce that material to a single named antecedent.\",\"reason\":\"The suffix is masculine singular, but attachment evidence marks the antecedent as ambiguous and recommends preserving the ambiguity among the dust, prior event, dawn-time setting, or broader scene.\",\"representative_source_ids\":[\"QG-148c3ba2\",\"MG-707cce80\",\"MG-9996bc9a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:4:boundary-scene-shift","source_type":"word_analysis","support_id":"sup_73c6b3c10d35b37557aa","text":"{\"blocking_evidence\":null,\"headline\":\"dust medium gives way to gathered target\",\"reader_payoff\":\"The reader sees the image move from atmosphere around the charge to the compact target it enters, then hand forward to the human proposition in 100:6.\",\"reason\":\"The boundary rows tie the previous dust scene to the final gathered target and then to the shift into the explicit human statement in 100:6.\",\"representative_source_ids\":[\"QB-7c771e90\",\"QB-a2409433\",\"QB-dd1a2d5c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:1:immediate-result-sequence","source_type":"word_analysis","support_id":"sup_7a1606f3b0ac38f064bd","text":"{\"blocking_evidence\":null,\"headline\":\"immediate sequence becomes culminating result\",\"reader_payoff\":\"The reader notices that 100:5 is the next immediate tactical step and also the result toward which the preceding image has been moving.\",\"reason\":\"QAC identifies the particle as immediate sequence, and the local clause continues the same verbal oath-scene rather than beginning a new subject or setting.\",\"representative_source_ids\":[\"QG-ac900df2\",\"QG-ce7705e1\",\"QS-7a03912a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:4","source_type":"word_analysis","support_id":"sup_7f229402eba2b9b29d13","text":"{\"gloss_range\":\"an indefinite accusative verbal noun naming a gathered body or collective gathering, most strongly the object entered by the charge while still allowing collective manner pressure\",\"prose\":\"{{ar:جَمْعًا}} ({{tr:jam'an}}) is the clause's landing point: the charge enters a gathered body, not merely an empty location. Its accusative case most strongly serves as the direct object of {{ar:وَسَطْنَ}} ({{tr:wasatna}}), while the same form can still carry collective-manner pressure, so collectivity is both what is breached and how the action feels massed. The indefinite tanwin leaves the gathering unnamed and scalable. As a compact verbal noun from the gathering field, it treats collectedness itself as the impacted unity, using a marked action/result slot inside a common root rather than a generic people-word. Its final cadence links the earlier dawn-time term in 100:3, the dust object in 100:4, and the gathered target here; the sound echo pairs outward-spreading dust with concentrated mass, while the constricted final consonant and nasal close make the impact feel dense. The final indefinite gathering also hands the image forward to the definite human proposition in 100:6.\",\"root_display\":\"{{ar:ج م ع}} ({{tr:j-m-ʿ}})\",\"root_gloss_range\":\"gathering scattered parts into one whole, assembled groups, totality, concerted resolve, and other construction-bound extensions; the local form selects gathered collective mass\",\"surface_display\":\"{{ar:جَمْعًا}} ({{tr:jam'an}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:4:tanwin-echo-and-heavy-closure","source_type":"word_analysis","support_id":"sup_8d9c6fbcdeb6d971b900","text":"{\"blocking_evidence\":null,\"headline\":\"cadence echoes dust while meaning reverses direction\",\"reader_payoff\":\"The reader hears the final -an cadence link dawn, dust, and gathering, while the meaning shifts from spreading dust to concentrated mass.\",\"reason\":\"The sound rows compare {{ar:جَمْعًا}} ({{tr:jam'an}}) with the dust object in 100:4 and the dawn-time term in 100:3, preserving the concrete references without adding out-of-bundle anchors.\",\"representative_source_ids\":[\"QE-d264147a\",\"QE-d69c316b\",\"QP-67965dee\",\"QP-bef052d6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:3","source_type":"word_analysis","support_id":"sup_8f557933e6f97f2431c7","text":"{\"gloss_range\":\"prepositional phrase with an ambiguous masculine singular suffix, functioning as the means, accompaniment, or cause by which the center-entry occurs\",\"prose\":\"{{ar:بِهِ}} ({{tr:bihi}}) is the hinge between action and target: it attaches to {{ar:وَسَطْنَ}} ({{tr:wasatna}}), then the clause names {{ar:جَمْعًا}} ({{tr:jam'an}}). The preposition can mark means, accompaniment, or cause, so the word draws the preceding scene into the act of center-entry without forcing one English label. Its masculine singular suffix keeps the referent open among live candidates such as the dust, the dawn-time raid setting, or the prior event as a whole, and because the suffix is bound inside this one dependent word the antecedent question remains audible rather than detached. The repeated {{ar:بِهِ}} ({{tr:bihi}}) across 100:4 and 100:5 makes the same ambiguous back-reference drive both dust-raising and penetration, while the brief phrase releases quickly into the heavier final object.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:بِهِ}} ({{tr:bihi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:3:verb-target-hinge-position","source_type":"word_analysis","support_id":"sup_9c0d371034ab4cbc79b8","text":"{\"blocking_evidence\":null,\"headline\":\"middle phrase bridges verb and target\",\"reader_payoff\":\"The reader receives the route, means, or cause before the target is named, so the clause pivots through the pronoun before landing on the gathering.\",\"reason\":\"The phrase sits between the verb and the explicit object and attaches to the verb rather than to the noun that follows.\",\"representative_source_ids\":[\"QG-173c02b4\",\"QT-ac9237c0\",\"QT-fe759e38\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:4:marked-form-within-common-root","source_type":"word_analysis","support_id":"sup_a382859675e0c65a1613","text":"{\"blocking_evidence\":null,\"headline\":\"common root appears in a marked local slot\",\"reader_payoff\":\"The reader sees that the common gathering root is locally carried by a compact action/result noun at the climactic close, not by a generic plural people-word.\",\"reason\":\"Contextual evidence gives a smaller exact-form gerund profile inside a broader root field; the rarity is narrowed to form choice rather than lexical uniqueness.\",\"representative_source_ids\":[\"QI-a01639d6\",\"QI-b862eb94\",\"QH-b4e58226\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:4:object-with-manner-pressure","source_type":"word_analysis","support_id":"sup_ad0bf96b38c751cd088a","text":"{\"blocking_evidence\":null,\"headline\":\"direct object remains primary while manner pressure survives\",\"reader_payoff\":\"The reader sees the gathered body as the target entered by the charge while still feeling the collective force of the action.\",\"reason\":\"Attachment evidence strongly licenses {{ar:جَمْعًا}} ({{tr:jam'an}}) as the explicit direct object of {{ar:وَسَطْنَ}} ({{tr:wasatna}}); the accusative alternative is preserved only as secondary manner or setting pressure.\",\"representative_source_ids\":[\"QG-6524879c\",\"QG-d599893e\",\"MG-6883bcd4\",\"QS-34d67e91\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:2:kinetic-center-entry","source_type":"word_analysis","support_id":"sup_bc01c6666e9f7bc16a7c","text":"{\"blocking_evidence\":null,\"headline\":\"middle becomes target-penetrating motion\",\"reader_payoff\":\"The reader sees centrality become an event: the charge enters the core of a gathered body and thereby affects its unity.\",\"reason\":\"The verb takes {{ar:جَمْعًا}} ({{tr:jam'an}}) as an explicit object and V4 includes an entering-the-middle branch, while mediation or balance branches are not selected by this local frame.\",\"representative_source_ids\":[\"QG-edcec780\",\"QS-58cd09f9\",\"QS-905a5bb1\",\"QS-941c4bed\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:4:final-target-compression","source_type":"word_analysis","support_id":"sup_c050717f2ef799f24f38","text":"{\"blocking_evidence\":null,\"headline\":\"final noun lands the compact clause\",\"reader_payoff\":\"The reader feels the three-part clause rush from action through means into the final named target.\",\"reason\":\"The local verbal clause is compactly built as verb, prepositional complement, and final object, with {{ar:جَمْعًا}} ({{tr:jam'an}}) closing the ayah.\",\"representative_source_ids\":[\"QT-6eddd845\",\"QT-b06026f4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:2:synthesis-center-as-force","source_type":"word_analysis","support_id":"sup_c4bcfcdb53d8359fe94f","text":"{\"blocking_evidence\":null,\"headline\":\"center becomes a force point\",\"reader_payoff\":\"The reader sees the verb gather local sense, rarity, variant contrast, and sound into one pressure point: middle is not a neutral location here but the force of entry.\",\"reason\":\"The synthesis is valid as a local convergence, but it is narrowed so that ethical balance, mediation, and Form II intensification remain contrastive rather than all becoming selected meanings of the canonical form.\",\"representative_source_ids\":[\"QI-b45bcd10\",\"QH-501679bf\",\"MH-5c921c82\",\"QY-a50ee93f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:1:fused-launch-cadence","source_type":"word_analysis","support_id":"sup_c5a7e8ba464812b34ae3","text":"{\"blocking_evidence\":null,\"headline\":\"short connector snaps into the verb\",\"reader_payoff\":\"The reader hears the clipped connector attach directly to the heavier verb, making the transition feel abrupt and compressed.\",\"reason\":\"The particle is a proclitic at the ayah opening and is heard as part of the launch into {{ar:فَوَسَطْنَ}} ({{tr:fa-wasatna}}).\",\"representative_source_ids\":[\"QF-3f1d68e7\",\"QP-4d2c6611\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:1:oath-bridge-before-answer","source_type":"word_analysis","support_id":"sup_c7ddad4b9e0827a7c1a1","text":"{\"blocking_evidence\":null,\"headline\":\"image closes before the oath answer\",\"reader_payoff\":\"The reader sees that the scene is narratively complete but structurally still waiting for the oath's explicit claim in 100:6.\",\"reason\":\"The particle opens a complete verbal clause, while the following ayah supplies the explicit oath payload rather than this horse-scene clause doing so by itself.\",\"representative_source_ids\":[\"MG-56cbe225\",\"QI-18106b40\",\"QB-bcbfe1cd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"100:5:1:2","source_type":"qac_morpheme","support_id":"sup_d805d5da05c0b5b26af0","text":"{\"lemma_ar\":\"وَسَطْ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:wasaTo|ROOT:wsT|3FP\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"100:5:1:2\",\"qac_word_ref\":\"100:5:1\",\"root_ar\":\"و س ط\",\"surface_ar\":\"وَسَطْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:2:rare-verbalized-middle","source_type":"word_analysis","support_id":"sup_d83cc107c078f585aee7","text":"{\"blocking_evidence\":null,\"headline\":\"rare verbal form contrasts with adjectival centrality\",\"reader_payoff\":\"The reader notices that a root often associated with middle-position or balance is here verbalized as disruptive motion, while those broader associations remain contrastive rather than locally governing.\",\"reason\":\"Contextual evidence marks the local PV occurrence as low occurrence and V4 separates central-position, balance, mediation, and entering-middle branches; the local syntax selects the entering-middle branch.\",\"representative_source_ids\":[\"QS-23678b8b\",\"QI-25f3f102\",\"QI-830b1a1a\",\"QH-27d4665e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:4:verbal-noun-result-form","source_type":"word_analysis","support_id":"sup_e12e270d8021811e7265","text":"{\"blocking_evidence\":null,\"headline\":\"gerund objectifies gatheredness\",\"reader_payoff\":\"The reader notices that the word can name gatheredness as an act or result, not only a list of people.\",\"reason\":\"QAC identifies the local word as a gerund or verbal noun, and V4's gathering branches support an act/result sense narrowed here to the body entered by the charge.\",\"representative_source_ids\":[\"QF-927a2067\",\"QI-0c882faa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:2:sharp-sound-texture","source_type":"word_analysis","support_id":"sup_e8c6f479f0b014c8691f","text":"{\"blocking_evidence\":null,\"headline\":\"sibilant and emphatic stop sharpen the action\",\"reader_payoff\":\"The reader can hear a narrowed, striking consonant texture in the verb that suits the entry into the center.\",\"reason\":\"The sound row is tied to the local consonants of {{ar:وَسَطْنَ}} ({{tr:wasatna}}), especially {{ar:س}} ({{tr:s}}) and {{ar:ط}} ({{tr:ṭ}}).\",\"representative_source_ids\":[\"QP-c1af52c4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:5:3:instrument-cause-attachment","source_type":"word_analysis","support_id":"sup_fed322fd15de1ba3e7db","text":"{\"blocking_evidence\":null,\"headline\":\"preposition makes prior material operative\",\"reader_payoff\":\"The reader notices that the center-entry happens by, with, or because of what the suffix retrieves from the preceding scene.\",\"reason\":\"Attachment evidence makes {{ar:بِهِ}} ({{tr:bihi}}) a prepositional complement of the verb, while translation support keeps instrumental, accompaniment, and causal values live.\",\"representative_source_ids\":[\"QG-01397168\",\"QG-44f03f2b\",\"QS-3ea1d02d\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فَوَسَطْنَ بِهِۦ جَمْعًا","ayah_ref":"100:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000259/B002","root_001646/B003"],"payload":{"activation_trace":[{"assigned_role":"Supplies the focus event's inward topological motion.","branch_id":"B003","branch_image_ar":"الدخول أو الجعل في الوسط","literal_contribution":"Entering, or causing placement, in the middle.","mapped_root_id":"root_001646","mapped_root_norm":"و س ط","root":"و س ط","source_phrase_ar":"وَسَطْ","source_ref":"100:5"},{"assigned_role":"Supplies the bounded collective whose middle can be entered.","branch_id":"B002","branch_image_ar":"جماعة اجتمعت أو أخلاط ضمتها الجهة","literal_contribution":"An assembled body, mixed multitude, or army.","mapped_root_id":"root_000259","mapped_root_norm":"ج م ع","root":"ج م ع","source_phrase_ar":"جَمْعًا","source_ref":"100:5"}],"changed_reading":{"after":"The movers penetrate from the collective's edge into its interior center; جَمْعًا is a spatially organized body, not just nearby people.","before":"A minimal gloss in which the movers merely arrive among some people."},"confidence":"strong","focus_anchor":"وَسَطْ as a finite plural verb plus جَمْعًا as its gathered field","mechanism":"The verbal middle-branch supplies ingress rather than static centrality, while the group-branch supplies an assembled body. Together they form a topological event: plural movers pass from an edge into the interior zone of a collective.","model_id":"BL-penetrated-collective-center","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:BL-penetrated-collective-center","source_type":"hft","support_id":"sup_eba78b263c1d1790e977","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَوَسَطْنَ بِهِۦ جَمْعًا","ayah_ref":"100:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000259/B010","root_001646/B002"],"payload":{"activation_trace":[{"assigned_role":"Supplies the point toward which movement converges.","branch_id":"B002","branch_image_ar":"موضع الوسط بين الأطراف","literal_contribution":"A center defined between surrounding sides or ordered parts.","mapped_root_id":"root_001646","mapped_root_norm":"و س ط","root":"و س ط","source_phrase_ar":"وَسَطْ","source_ref":"100:5"},{"assigned_role":"Turns the entry into a culmination of accumulated momentum.","branch_id":"B010","branch_image_ar":"استجماع القوة أو السير حتى تتلاحق أجزاؤه","literal_contribution":"Force or motion gathers until its parts catch up and become concentrated.","mapped_root_id":"root_000259","mapped_root_norm":"ج م ع","root":"ج م ع","source_phrase_ar":"جَمْعًا","source_ref":"100:5"}],"changed_reading":{"after":"The middle is the convergence point at which previously distributed motion becomes a single concentrated force.","before":"A location change: they moved into a middle."},"confidence":"medium","focus_anchor":"The pairing of وَسَطْ with the force-gathering branch of جَمْعًا","mechanism":"A middle between sides supplies a point of maximum inward reach, and gathering motion supplies concentration. The packet gives the two images; I infer that reaching the center marks the culmination of converging momentum.","model_id":"BL-concentrated-momentum","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:BL-concentrated-momentum","source_type":"hft","support_id":"sup_48c540562d2c52a8dff9","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَوَسَطْنَ بِهِۦ جَمْعًا","ayah_ref":"100:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000259/B001","root_001646/B003"],"payload":{"activation_trace":[{"assigned_role":"Places the movers at the organizing interior of the field.","branch_id":"B003","branch_image_ar":"الدخول أو الجعل في الوسط","literal_contribution":"Entering or setting something in the middle.","mapped_root_id":"root_001646","mapped_root_norm":"و س ط","root":"و س ط","source_phrase_ar":"وَسَطْ","source_ref":"100:5"},{"assigned_role":"Makes the target a produced configuration whose integrity can change.","branch_id":"B001","branch_image_ar":"ضم المتفرق حتى يصير شيئا مجموعا","literal_contribution":"Scattered parts are joined until they become one collected whole.","mapped_root_id":"root_000259","mapped_root_norm":"ج م ع","root":"ج م ع","source_phrase_ar":"جَمْعًا","source_ref":"100:5"}],"changed_reading":{"after":"The entry reaches the organizing middle of a collected whole and may alter how its previously distributed parts hold together.","before":"The gathering is a fixed crowd that merely receives the entry."},"confidence":"medium","focus_anchor":"وَسَطْ as ingress and جَمْعًا as the making of a whole from dispersion","mechanism":"The collective need not be a passive, already fixed target. The جمع branch exposes an active relation between scattered parts and a collected whole; entry into its middle can therefore be read as contact with the organizing point of that whole. The claim that ingress may reconfigure it is my inferred arrow.","model_id":"BL-entry-reconfigures-whole","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:BL-entry-reconfigures-whole","source_type":"hft","support_id":"sup_f66908e1e4897066becf","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَوَسَطْنَ بِهِۦ جَمْعًا","ayah_ref":"100:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000259/B003","root_001646/B005"],"payload":{"activation_trace":[{"assigned_role":"Recasts middle-entry as interposition among parties.","branch_id":"B005","branch_image_ar":"الوساطة بين الناس","literal_contribution":"Mediation or action between human parties.","mapped_root_id":"root_001646","mapped_root_norm":"و س ط","root":"و س ط","source_phrase_ar":"وَسَطْ","source_ref":"100:5"},{"assigned_role":"Supplies a strategic or deliberative collective center.","branch_id":"B003","branch_image_ar":"عزم محكم جمع الرأي بعد تفرقه","literal_contribution":"Scattered opinion is gathered into firm, concerted resolve.","mapped_root_id":"root_000259","mapped_root_norm":"ج م ع","root":"ج م ع","source_phrase_ar":"جَمْعًا","source_ref":"100:5"}],"changed_reading":{"after":"A coexisting social reading appears: the movers interpose within a coalition at the point where its divided intentions have become concerted resolve.","before":"The middle is exclusively physical and the gathering exclusively bodily."},"confidence":"exploratory","focus_anchor":"The mediation branch of وَسَطْ and the concerted-resolve branch of جَمْعًا","mechanism":"Two social branches coexist with the physical reading: وسط can act between parties, and جمع can collect divided opinions into one resolve. Their conjunction permits an interposition into the decision-center of an alliance. This is form-distant from the most direct verbal construal, so it remains exploratory rather than replacing physical ingress.","model_id":"BL-interposition-in-concert","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:BL-interposition-in-concert","source_type":"hft","support_id":"sup_4e72a3a36834bba7f1a6","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَوَسَطْنَ بِهِۦ جَمْعًا","ayah_ref":"100:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000259/B009","root_001646/B006"],"payload":{"activation_trace":[{"assigned_role":"Makes the center a latent division-line rather than only a destination.","branch_id":"B006","branch_image_ar":"قطع الشيء نصفين","literal_contribution":"Cutting a thing into two halves at its middle.","mapped_root_id":"root_001646","mapped_root_norm":"و س ط","root":"و س ط","source_phrase_ar":"وَسَطْ","source_ref":"100:5"},{"assigned_role":"Supplies the integrity put at risk by contact with the middle.","branch_id":"B009","branch_image_ar":"اكتمال الشيء كله بلا تفرق أو نقص","literal_contribution":"Wholeness without scattering, loss, or deficiency.","mapped_root_id":"root_000259","mapped_root_norm":"ج م ع","root":"ج م ع","source_phrase_ar":"جَمْعًا","source_ref":"100:5"}],"changed_reading":{"after":"The center is also the gathered whole's faultline: penetration there carries the possibility of bisection and loss of integrity.","before":"The center is simply the safest description of where entry ends."},"confidence":"exploratory","focus_anchor":"The cutting branch of وَسَطْ against the intact-whole branch of جَمْعًا","mechanism":"One accepted وسط branch makes the middle the line at which a thing is divided into halves, while جمع can mark intact totality. Their tension permits the center to be a faultline: reaching it threatens the integrity that جَمْعًا names. The cutting sense is associated with a derived form in the branch scope, which limits confidence but does not erase the activation.","model_id":"BL-center-as-faultline","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:BL-center-as-faultline","source_type":"hft","support_id":"sup_117f89a299628d50d2fa","trust":"legacy_unbound"}]}
</lane_packet_json>
