# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **113:5**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s113-regular-20260911/s113/113_5/micro.discovery.json` and modify nothing
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
  "ayah_ref": "113:5",
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
{"analysis_context":{"analysis_id":"s113-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"113:5","host_surah":113,"lane_context_refs":[],"ordered_context_refs":["113:0","113:1","113:2","113:3","113:4","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, yalnızca başkasında bulunan iyi şeyin benzerini istemeyi değil, o kişinin elindekini yitirmesini istemeyi gerektirir.","branch_kind":"mixed_non_bare","branch_ref":"root_000319/B001","candidate_links":[{"candidate_id":"cand_914bfb7d0684ef1c8964","lane":"micro"},{"candidate_id":"cand_adbe095dcc684168200b","lane":"micro"},{"candidate_id":"cand_cc2dd73a9f468d6783ea","lane":"micro"},{"candidate_id":"cand_8e8ade73f0f9958d523c","lane":"micro"},{"candidate_id":"cand_7983e493711ca3a93025","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَاسِد","morph_features":"STEM|POS:N|ACT|PCPL|LEM:HaAsid|ROOT:Hsd|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:3:1","qac_word_ref":"113:5:3","surface_ar":"حَاسِدٍ"},{"lemma_ar":"حَسَدَ","morph_features":"STEM|POS:V|PERF|LEM:Hasada|ROOT:Hsd|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"113:5:5:1","qac_word_ref":"113:5:5","surface_ar":"حَسَدَ"}],"gloss":"başkasındaki iyi şeyin ondan gitmesini isteme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir başkasının sahip olduğu iyi bir şeyi yitirmesini isteme, dalın zorunlu anlam çekirdeğidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yitirilmesi istenen iyi şeyin isteyene geçmesi ayrıca dilenebilir, fakat bu yön her kullanımda bulunmak zorunda değildir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İstek, kimi durumda ötekinin elindeki iyi şeyi ortadan kaldırmaya yönelik bir çabayla birlikte görülebilir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir kaynak, yitirilmesi istenen iyi şeyi kişinin sahip olmayı hak ettiği nimetle sınırlar."}}],"root_ar":"ح س د","root_id":"root_000319","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın zorunlu çekirdeğini, iyi şeyin hak edilmiş olması, isteyene geçmesi veya onu yok etmek için uğraşılması gibi zorunlu olmayan yönlerden ayırarak karşılar.","boundary_detail":"Dal, yalnızca başkasında bulunan iyi şeyin benzerini istemeyi değil, o kişinin elindekini yitirmesini istemeyi gerektirir.","branch_image_ar":"تمنّي زوال النعمة عن المحسود","concept_gloss":"başkasındaki iyi şeyin ondan gitmesini isteme","contextual_glosses":[{"applicability":"Söz konusu iyi şeyin bağlamdan belli olduğu eylem cümlelerinde doğal bir karşılıktır; kimin kayba uğramasının istendiğini açıkça belirtir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başkasında bulunan iyi şeyin o kişinin elinden gitmesine yönelen isteği korur."},"facet_ids":["F001"],"text":"elindekini yitirmesini istemek","usage_role":"contextual"},{"applicability":"Birinin elindeki iyi şey karşısındaki düşmanca tutumun bağlamda açık olduğu gündelik anlatımlarda kullanılabilir.","error_profile":{"adds":null,"collision":"Bağlama göre yalnızca hoşlanmama veya katlanamama anlamında da anlaşılabilir.","fit":"narrowing","loses":"Tek başına kullanıldığında ötekinin elindeki iyi şeyi yitirmesini isteme sonucunu açıkça bildirmez.","preserves":"Başkasının iyi durumuna karşı duyulan olumsuz ve karşılaştırmalı tutumu korur."},"facet_ids":["F001"],"text":"çekememek","usage_role":"contextual"}],"definition":"Bir başkasındaki iyi bir durumun ya da kazanımın ondan gitmesini istemektir. İsteyen, bunun kendisine geçmesini de dileyebilir ve bazen ortadan kalkması için uğraşabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir başkasının sahip olduğu iyi bir şeyi yitirmesini isteme, dalın zorunlu anlam çekirdeğidir."},{"facet_id":"F002","role":"extension","statement":"Yitirilmesi istenen iyi şeyin isteyene geçmesi ayrıca dilenebilir, fakat bu yön her kullanımda bulunmak zorunda değildir."},{"facet_id":"F003","role":"associated_use","statement":"İstek, kimi durumda ötekinin elindeki iyi şeyi ortadan kaldırmaya yönelik bir çabayla birlikte görülebilir."},{"facet_id":"F004","role":"source_variant","statement":"Bir kaynak, yitirilmesi istenen iyi şeyi kişinin sahip olmayı hak ettiği nimetle sınırlar."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"İyi şey ötekinde kalırken onun benzerine kendisinin de sahip olmasını isteme anlamını getirir.","collision":"Kökün zarar vermeyen ikinci dalıyla karışır.","fit":"displacement","loses":"Ötekinin elindeki iyi şeyi yitirmesini isteme yönünü ortadan kaldırır.","preserves":"Başkasındaki iyi bir şeye yönelen karşılaştırmalı isteği korur."},"text":"imrenme"}],"identity_rationale":"Kaynak ifadesi, bir başkasındaki iyi bir durumun ya da kazanımın ondan gitmesini istemeyi dalın ortak çekirdeği olarak verir. Bir kaynak bunu kişinin hak ettiği nimetle sınırlar. Kazanımın isteyene geçmesini dilemek veya onu ortadan kaldırmaya çalışmak bu çekirdeğe eşlik edebilir, ancak her durumda zorunlu değildir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"başkasındaki iyi şeyin ondan gitmesini isteme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"başkasının elindeki iyi şeyi yitirmesini istemek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"birini elindeki iyi şey yüzünden çekememek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"birinin sahip olduğu şeyi çekememek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"elindeki iyi şeyi yitirmesi istenen kişi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"başkasının elindeki iyi şeyi yitirmesini isteyen kişi"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"başkalarının iyi durumunu yitirmesini sık sık isteyen kişi"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"başkalarının iyi durumunu yitirmesini şiddetle isteyen kişi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"başkalarının iyi durumlarını yitirmesini isteyenler topluluğu"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"birbirlerinin elindeki iyi şeyleri yitirmesini istemek"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"başkasının elindeki iyi şeyi yitirmesini isteme"}],"lexicalization_note":"Tanım yalın ad ve eylem biçimlerinin ortak çekirdeğini verir; birini elindeki şey yüzünden çekememeyi anlatan kuruluşlar ile karşılıklı eylem biçimi ayrı sözlü gerçekleşmeler olarak korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; zarar vermeyen ikinci dal, kayıp isteği sınırını doğrudan gösteren tek keskin karşıtlıktır. Öteki adaylar yoksun bırakma, çekişme, tutumluluk veya genel duygu alanlarını paylaşsa da anlam çekirdeğini daha iyi ayırmaz.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Bu dal ötekinin kaybını hedefler; komşu dal ise ötekinin elindekine dokunmadan benzer bir iyiliği kendisi için ister. Ayrım, iyi durumun mevcut sahibinde kalıp kalmaması eksenindedir.","focus_only":"İyi şeyin mevcut sahibinden gitmesini istemek bu dala özgüdür.","gloss":"zarar veren istek ile zarar vermeyen imrenme","neighbor_only":"İyi şey sahibinde kalırken onun bir benzerine kendisinin de sahip olmasını istemek öteki dala özgüdür.","neighbor_ref":"root_000319/B002","relation_type":"polarity_pair","shared_zone":"Her iki dal da bir başkasında görülen iyi bir durumun kişide doğurduğu karşılaştırmalı isteği anlatır."}],"source_phrase_ar":"الحاء والسين والدال أصل واحد وهو الحسد (maqayis)؛ الحسد معروف والفعل حسد يحسد حسدا (ayn;tahdhib)؛ حسدت أحسد حسدا، وحسدتك على الشيء وحسدتك الشيء بمعنى واحد (jamhara;sihah)؛ أن تتمنى زوال نعمة المحسود إليك (sihah)؛ الحسد أن يرى الإنسان لأخيه نعمة فيتمنى أن تزوى عنه وتكون له (tahdhib)؛ تمني زوال نعمة من مستحق لها وربما كان مع ذلك سعي في إزالتها (mufradat)","source_summary":"Kaynakların ortak anlatımı, başkasındaki bir iyiliğin ondan gitmesini istemeyi temel alır. Bir anlatım bu iyiliği kişinin sahip olmayı hak ettiği nimetle sınırlar; bazı anlatımlar iyiliğin isteyene geçmesini, bazıları da onu ortadan kaldırmaya yönelik çabayı olası ek yönler olarak belirtir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحسد المعروف: أن يرى الإنسان نعمة لغيره فيتمنى زوالها عنه، وقد يتمنى انتقالها إليه أو يسعى في إزالتها، ويستعمل الفعل حسد يحسد وحسدته على الشيء وحسدته الشيء.","what_is_not_ar":"لا يدخل فيه مجرد الغبطة التي لا يتمنى صاحبها زوال النعمة عن غيره."},"support_links":["sup_06bd1370c77bf67f0f3f","sup_1f51e32cf1b79883ebaa","sup_35613bbd5efe1eed9eb1","sup_86b6ecca7eb8170531c4","sup_9816952df4200296b721"]},{"boundary":"Dalın sınırı, başkasının kaybını istememek ve isteği yalnızca aynı iyiliğin bir benzerine kendisi de sahip olmaya yöneltmektir.","branch_kind":"mixed_non_bare","branch_ref":"root_000319/B002","candidate_links":[{"candidate_id":"cand_adbe095dcc684168200b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حَاسِد","morph_features":"STEM|POS:N|ACT|PCPL|LEM:HaAsid|ROOT:Hsd|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:3:1","qac_word_ref":"113:5:3","surface_ar":"حَاسِدٍ"},{"lemma_ar":"حَسَدَ","morph_features":"STEM|POS:V|PERF|LEM:Hasada|ROOT:Hsd|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"113:5:5:1","qac_word_ref":"113:5:5","surface_ar":"حَسَدَ"}],"gloss":"başkasındaki iyiliğin benzerini onu yoksun bırakmadan isteme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, başkasında gördüğü iyi şeyin bir benzerine kendisi de sahip olmayı isterken mevcut sahibin onu yitirmesini istemez."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynak anlatımı bu zarar vermeyen isteği, ötekinin kaybını isteyen tutumun daha hafif bir türü olarak sınıflandırır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Mal sahibinin malını veya okuduğunu belleğinde tutan kişinin bu becerisini yitirmesini istemeden bunların bir benzerini dilemek örnek olarak verilir."}}],"root_ar":"ح س د","root_id":"root_000319","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem kendisi için benzer bir iyi şey isteme yönünü hem de mevcut sahibin kaybını istememe koşulunu eksiksiz karşılar.","boundary_detail":"Dalın sınırı, başkasının kaybını istememek ve isteği yalnızca aynı iyiliğin bir benzerine kendisi de sahip olmaya yöneltmektir.","branch_image_ar":"الغبطة بلا إزالة النعمة","concept_gloss":"başkasındaki iyiliğin benzerini onu yoksun bırakmadan isteme","contextual_glosses":[{"applicability":"Başkasındaki iyi durumun benzerini kendisi için istemenin, o kişiye zarar dilemeden anlatıldığı genel bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başkasındaki iyi şeye bakarak onun benzerini istemeyi ve mevcut sahibin kaybını dilememe yönünü korur."},"facet_ids":["F001"],"text":"imrenmek","usage_role":"general"},{"applicability":"İsteğin başkasındaki iyi şeyi ortadan kaldırmaya değil, kendisi için ona denk bir iyi duruma yöneldiğinin açıklanması gereken bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ötekinin elindekine dokunmadan onun benzerine sahip olma isteğini açıkça korur."},"facet_ids":["F001"],"text":"aynı iyilikten kendine de istemek","usage_role":"explanatory"}],"definition":"Başkasında bulunan iyi bir durumun ya da kazanımın bir benzerine, o kişiyi elindekinden yoksun bırakmayı istemeden, kendisinin de sahip olmayı dilemesidir. Bu yönüyle ötekinin kaybını isteyen tutumdan daha hafif ve zarar vermeyen bir istektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, başkasında gördüğü iyi şeyin bir benzerine kendisi de sahip olmayı isterken mevcut sahibin onu yitirmesini istemez."},{"facet_id":"F002","role":"source_variant","statement":"Kaynak anlatımı bu zarar vermeyen isteği, ötekinin kaybını isteyen tutumun daha hafif bir türü olarak sınıflandırır."},{"facet_id":"F003","role":"example","statement":"Mal sahibinin malını veya okuduğunu belleğinde tutan kişinin bu becerisini yitirmesini istemeden bunların bir benzerini dilemek örnek olarak verilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Sevilen kişiyi paylaşmama, üstünlük çekişmesi veya ötekinin kaybına dönük tutumlar gibi daha geniş anlamlar getirir.","collision":"Ötekinin elindeki iyi şeyi yitirmesini isteyen ilk dalla karışabilir.","fit":"broadening","loses":"Mevcut sahibin elindekini yitirmesini istememe koşulunu açıkça güvence altına almaz.","preserves":"Başkasındaki bir üstünlüğe veya iyi duruma verilen karşılaştırmalı tepkiyi korur."},"text":"kıskançlık"}],"identity_rationale":"Kaynak ifadesi, kişinin başkasındaki iyi şeyin bir benzerine sahip olmayı istemesini ve mevcut sahibin elindekini yitirmesini istememesini açıkça birlikte verir. Bu yüzden zarar vermeyen imrenme çerçevesi kaynak ifadesini doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"başkasındaki iyi şeyin benzerini onu yoksun bırakmadan isteme"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yalnız iki durumda zarar vermeyen bir imrenme vardır"}],"lexicalization_note":"Tanım zarar vermeyen yalın kullanımın çekirdeğini verir; yalnız iki duruma bağlanan kalıplaşmış söz bu çekirdeğin genel kapsamı sayılmaz ve kendi kuruluşuyla sınırlı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ilk dal sonuç bakımından doğrudan karşıtlığı, iyi dileme adayı yararlanıcı farkını ve hoşnutluk adayı edinme isteği sınırını belirginleştirir. Bereket, mutluluk ve bolluk adayları ise istenebilecek durumları anlatır, bu isteğin kendisini değil.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Bu dal mevcut sahibin kaybını istemez ve benzer bir iyiliği kendisi için diler; komşu dal doğrudan ötekinin elindekini yitirmesine yönelir. İki dal aynı uyaran karşısında zıt sonuçlar ister.","focus_only":"İyi şey ötekinde kalırken onun bir benzerini kendisi için istemek bu dala özgüdür.","gloss":"zarar vermeyen imrenme ile zarar veren istek","neighbor_only":"İyi şeyin mevcut sahibinden gitmesini istemek öteki dala özgüdür.","neighbor_ref":"root_000319/B001","relation_type":"polarity_pair","shared_zone":"Her iki dal da bir başkasında görülen iyi bir durumun kişide doğurduğu karşılaştırmalı isteği anlatır."},{"boundary_match":"partial","distinction":"Bu dalda isteğin yararlanıcısı isteği duyan kişidir; komşuda ise iyi dilek doğrudan başka kişiye yönelir. Olumlu yönelim ortak olsa da katılımcı rolleri farklıdır.","focus_only":"Kişinin iyi şeyin bir benzerini kendisi için istemesi bu dala özgüdür.","gloss":"kendine benzerini isteme ile başkası için iyilik dileme","neighbor_only":"İyi sonucu doğrudan öteki kişi için dilemek ve onun adına olumlu beklenti taşımak komşuya özgüdür.","neighbor_ref":"root_000292/B004","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir iyi duruma zarar vermeyen, olumlu yönelim vardır."},{"boundary_match":"field_only","distinction":"Bu dal elde bulunmayan benzer bir iyiliğe yönelen isteği anlatır; komşu ise yeni bir edinme isteğini değil, verilmiş olanla yetinmeyi anlatır.","focus_only":"Başkasında görülen iyi şeyin bir benzerini edinme isteği bu dala özgüdür.","gloss":"benzerini isteme ile elindekinden hoşnut olma","neighbor_only":"Kendisine verilmiş olanla yetinip ona gönül rahatlığıyla bağlanmak komşuya özgüdür.","neighbor_ref":"root_001265/B008","relation_type":"same_field","shared_zone":"İki dal da kişinin iyi şeylerin dağılımı karşısındaki tutumunu konu edinir."}],"source_phrase_ar":"الغبط أن يتمنى أن يكون له مثلها من غير أن تزوى عنه؛ الغبط ضرب من الحسد وهو أخف منه؛ لا يتمنى أن يرزأ صاحب المال في ماله أو تالي القرآن في حفظه (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Zarar vermeyen bu kullanım, mal sahibinin malını veya okuduğunu belleğinde tutan kişinin bu becerisini yitirmesini istememe koşuluyla birlikte kaydedilir."}],"source_summary":"Bu dal, başkasındaki iyi şeyin sürmesine karşı çıkmadan onun bir benzerine sahip olma isteğini anlatır ve ötekinin kaybını isteyen ilk daldan bu sonuç bakımından ayrılır.","sources":["TA"],"what_is_ar":"يدخل فيه استعمال الحسد في معنى الغبطة: أن يتمنى الإنسان مثل نعمة غيره من غير أن يتمنى أن يرزأ صاحب النعمة في نعمته.","what_is_not_ar":"لا يدخل فيه الحسد الضار الذي يتمنى زوال النعمة عن صاحبها."},"support_links":["sup_35613bbd5efe1eed9eb1"]},{"boundary":"Dal ateşten sıçrayan parçacıkları, kurutmak için serme eylemini ve böcek adını kapsamaz.","branch_kind":"bare","branch_ref":"root_000787/B001","candidate_links":[{"candidate_id":"cand_914bfb7d0684ef1c8964","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"iyinin karşıtı olan kötülük","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İyinin karşıtı olan kötülük, kötü durum ve kaçınılan şey anlamı çekirdeği oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kötülüğü çok olan kişi ve kötülük sahibi topluluk bu çekirdeğin kişi üzerindeki gerçekleşmesidir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birini kötülüğe bağlama, o kişiyi kötü sayma ya da kötülükle niteleme işlemidir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kimi kullanımlarda anlam kusur veya hoş karşılanmayan şeyle sınırlandırılır."}}],"root_ar":"ش ر ر","root_id":"root_000787","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kötü olanı ve iyinin karşıtını bildiren temel kullanımında en kısa ve doğal karşılıktır.","boundary_detail":"Dal ateşten sıçrayan parçacıkları, kurutmak için serme eylemini ve böcek adını kapsamaz.","branch_image_ar":"الشَّرّ والسوء","concept_gloss":"iyinin karşıtı olan kötülük","contextual_glosses":[{"applicability":"Kötülüğü çok olan bir kişiyi niteleyen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin kötülükle belirginleşmesini ve kötülüğün çokluğunu korur."},"facet_ids":["F002"],"text":"çok kötü kimse","usage_role":"contextual"},{"applicability":"Bir kişiyi kötülüğe bağlama veya onu kötü diye niteleme eyleminde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir kişiye kötülük niteliği yükleme işlemini korur."},"facet_ids":["F003"],"text":"kötü saymak","usage_role":"contextual"},{"applicability":"Anlamın kusur ya da hoş karşılanmayan şeyle daraldığı kullanımlar içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dar kullanımdaki kusur ve istenmeme sınırını açıkça korur."},"facet_ids":["F004"],"text":"kusur veya istenmeyen şey","usage_role":"explanatory"}],"definition":"İyinin karşıtı olan, kaçınılan kötü ve istenmeyen şey ya da durumdur. Kötülüğü çok olan kişiyi, birini kötülüğe bağlamayı ve kimi kullanımlarda kusur ya da hoş karşılanmayan şeyi de anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İyinin karşıtı olan kötülük, kötü durum ve kaçınılan şey anlamı çekirdeği oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Kötülüğü çok olan kişi ve kötülük sahibi topluluk bu çekirdeğin kişi üzerindeki gerçekleşmesidir."},{"facet_id":"F003","role":"associated_use","statement":"Birini kötülüğe bağlama, o kişiyi kötü sayma ya da kötülükle niteleme işlemidir."},{"facet_id":"F004","role":"source_variant","statement":"Kimi kullanımlarda anlam kusur veya hoş karşılanmayan şeyle sınırlandırılır."}],"identity_rationale":"Kaynak ifadesi bu dalı iyinin karşıtı olan kötülük ve kötü durum çevresinde kurar; kötü kişi, kötülüğün çokluğu, birini kötülüğe bağlama ve kusur ya da hoş karşılanmayan şey kullanımları da aynı anlam alanının belirtilmiş uzantılarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kötülük; iyinin karşıtı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kötülük etme veya kötü olma durumu"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"kötülüğü çok olan adam"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"kötü kimseler"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"birini kötülüğe bağladı; onu kötü saydı"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kusur veya hoş karşılanmayan şey"}],"lexicalization_note":"Tanım yalın dal anlamını verir; aynı ses yapısındaki öteki dalların kalıba veya nesneye bağlı anlamlarını buraya taşımaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yararlı sınırlar genel kötülüğün çirkinlik ve iç bozukluktan ayrıldığı iki karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal daha geniş bir ahlaki ve değerlendirici kötülük çekirdeğine sahiptir; komşu dalın merkezi ise çirkinlik ve olması gerekenden düşük niteliktir.","focus_only":"Odak dal iyinin karşıtı olan genel kötülüğü, kötü kişiyi ve birini kötü sayma işlemini de kapsar.","gloss":"kötülük ile çirkinlik ve nitelik düşüklüğü","neighbor_only":"Komşu dal özellikle çirkinlik, nitelik düşüklüğü ve kötü söz ya da davranış üzerinde durur.","neighbor_ref":"root_000755/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da kötü, beğenilmeyen ve olumlu değerin karşısında duran şeyi anlatır."},{"boundary_match":"partial","distinction":"Kötülük başlı başına bir değer karşıtlığıdır; komşu kavram ise önceden beklenen sağlamlığı veya arılığı bozan bir kusuru gerektirir.","focus_only":"Odak dal genel kötülüğü ve iyinin karşıtını bildirir.","gloss":"kötülük ile iç bozukluk","neighbor_only":"Komşu dal sağlam ya da arı olması beklenen bir şeye giren bozukluk, kusur ve eğriliği bildirir.","neighbor_ref":"root_000977/B003","relation_type":"near_neighbor","shared_zone":"Her ikisi de kusur ve olumsuz değerlendirme alanında kesişir."}],"source_phrase_ar":"الشَّرّ خلاف الخير (maqayis;jamhara)؛ الشر السوء (ayn)؛ الشر نقيض الخير (sihah)؛ الشر الذي يرغب عنه الكل (mufradat)؛ رجل شرير كثير الشر (maqayis;jamhara;sihah;mufradat)؛ أشررت فلانا إذا نسبته إلى الشر (maqayis;sihah;mufradat)؛ الشُّرّ العيب (sihah)؛ الشر بالضم خص بالمكروه (mufradat)","source_summary":"Kaynakların ortak ekseni iyinin karşıtı olan kötülüktür; toplu ifade ayrıca kötü kişiyi, kötülüğün çokluğunu, birini kötü saymayı ve daha dar olarak kusur ya da istenmeyen şeyi kapsar.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه نقيض الخير والسوء والرجل الشرير وكثرة الشر ونسبة المرء إلى الشر والعيب أو المكروه","what_is_not_ar":"لا يدخل فيه شرر النار ولا بسط الشيء ليجف ولا الشرّان الحشرة"},"support_links":["sup_06bd1370c77bf67f0f3f"]},{"boundary":"Dal yalnız yaymayı değil, yaymanın kurutma amacını da gerektirir; kötülük ve ateş parçacığı anlamları dışarıda kalır.","branch_kind":"bare","branch_ref":"root_000787/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"güneşe serip kurutmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi güneşte veya uygun bir yüzeyde açıp sermek ve böylece kurutmak temel işlemdir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Et, kumaş, kurutulmuş süt ürünü ve tahıl serilip kurutulan şeylere örnektir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kurutulacak şeyin üzerine yayıldığı hasır benzeri yüzey ve serilmiş kuru parçalar da bu işlemle adlandırılır."}}],"root_ar":"ش ر ر","root_id":"root_000787","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin açılarak güneşe veya uygun bir yüzeye serildiği ve kurumaya bırakıldığı temel eylem içindir.","boundary_detail":"Dal yalnız yaymayı değil, yaymanın kurutma amacını da gerektirir; kötülük ve ateş parçacığı anlamları dışarıda kalır.","branch_image_ar":"نشر الشيء في الشمس ليجف","concept_gloss":"güneşe serip kurutmak","contextual_glosses":[{"applicability":"Yiyecek veya tahılın kuruması için üzerine serildiği hasır benzeri yüzey adlandırılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Serme işleminin üzerinde gerçekleştiği yüzey görevini korur."},"facet_ids":["F003"],"text":"kurutma yaygısı","usage_role":"contextual"},{"applicability":"Sözün kurutma işlemi sonunda elde edilen et parçalarını anlattığı bağlam içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Parçaların serilmiş ve kurutulmuş ürün oluşunu korur."},"facet_ids":["F003"],"text":"serilip kurutulmuş parçalar","usage_role":"explanatory"}],"definition":"Kumaş, et, süt ürünü veya tahıl gibi bir şeyi güneşte ya da bir yaygı üzerinde açıp sererek kurutmaktır. İşlem, üzerine serme yapılan yüzeyleri ve kurutulan parçaları da adlandırabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi güneşte veya uygun bir yüzeyde açıp sermek ve böylece kurutmak temel işlemdir."},{"facet_id":"F002","role":"example","statement":"Et, kumaş, kurutulmuş süt ürünü ve tahıl serilip kurutulan şeylere örnektir."},{"facet_id":"F003","role":"associated_use","statement":"Kurutulacak şeyin üzerine yayıldığı hasır benzeri yüzey ve serilmiş kuru parçalar da bu işlemle adlandırılır."}],"identity_rationale":"Kaynak ifadesi eylemi bir şeyi güneşe ya da bir yaygı üzerine sererek kurutma olarak açıkça tanımlar; kurutma yüzeyleri ve serilip kurutulan parçalar bu işlemle bağlı adlandırmalardır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"güneşe serip kuruttu"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"güneşte kuruması için serdi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kurutulacak şeylerin serildiği yaygı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"süt ürünü veya tahıl kurutma yaygısı"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kurutma yaygıları veya kurutulmuş et parçaları"}],"lexicalization_note":"Tanım yalın serip kurutma dalını kapsar; belirli bir yiyeceğe veya tek bir kurutma yüzeyine indirgenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; güneşte et kurutma ve sıralanmış et adayları, amaç ile nesne sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal nesne bakımından daha geniş ve kurutma amacı bakımından belirgindir; komşu dal etle sınırlı bir uygulamadan zaman adlandırmasına uzanır.","focus_only":"Odak dal kumaş, süt ürünü ve tahıl gibi et dışındaki nesneleri ve kurutma yaygısını da kapsar.","gloss":"güneşte kurutma ile eti güneşe çıkarma","neighbor_only":"Komşu dal etin güneşe çıkarılmasına ek olarak belirli günlerin adlandırılmasını da kapsar.","neighbor_ref":"root_000790/B002","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak alanı eti güneşe sererek kurutma işlemidir."},{"boundary_match":"partial","distinction":"Odak kavram bir kurutma işlemidir; komşu kavram etin dizilmiş veya taşınan biçimini ve pişme durumunu adlandırır.","focus_only":"Odak dal serme işlemini kurutma amacıyla tanımlar ve et dışındaki nesneleri de alır.","gloss":"serip kurutma ile sıralanmış et","neighbor_only":"Komşu dal güneşte ya da kor üzerinde sıralanmış, yolculukta taşınan ve bazen iyi pişmemiş eti adlandırır.","neighbor_ref":"root_000871/B003","relation_type":"near_neighbor","shared_zone":"Her ikisinde etin açılıp sıralanması ve ısıyla ya da havayla işlenmesi bulunabilir."}],"source_phrase_ar":"الشر بسطك الشيء في الشمس (maqayis;ayn)؛ شررت اللحم والثوب وأشررته إذا بسطته ليجف (jamhara)؛ شررت الثوب بسطته في الشمس (sihah)؛ شررت الأقط أشره إذا جعلته على خصفة ليجف (sihah)؛ الإشرارة ما يبسط عليه الشيء (maqayis)؛ الإشرار ما يبسط عليه الأقط والبر ليجف (ayn)؛ الأشارير قطع قديد (sihah)","source_summary":"Kaynaklar güneşte sererek kurutma işleminde birleşir; toplu ifade farklı kurutulan nesneleri, serme yüzeyini ve kuru et parçaları yorumunu birlikte verir.","sources":["MQ","AY","JA","SI"],"what_is_ar":"يدخل فيه بسط الثوب واللحم والأقط والملح والبر في الشمس أو على خصفة ليجف وما يبسط عليه ذلك كالإشرارة والأشارير","what_is_not_ar":"لا يدخل فيه الشر خلاف الخير ولا الشرر المتطاير من النار ولا المخاصمة"},"support_links":[]},{"boundary":"Dal alevin kendisini veya ateşi yakma eylemini değil, ateşten ayrılıp uçuşan parçacıkları bildirir.","branch_kind":"bare","branch_ref":"root_000787/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"kıvılcım","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ateşten ayrılıp havaya sıçrayan yanar parçacık temel nesnedir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Söz varlığı tek parçacık ile parçacıklar topluluğunu ayrı biçimlerle adlandırır."}}],"root_ar":"ش ر ر","root_id":"root_000787","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ateşten kopup sıçrayan tek yanar parçacık veya bu parçacıkların türü anlatılırken kullanılır.","boundary_detail":"Dal alevin kendisini veya ateşi yakma eylemini değil, ateşten ayrılıp uçuşan parçacıkları bildirir.","branch_image_ar":"شَرَر النار المتطاير","concept_gloss":"kıvılcım","contextual_glosses":[{"applicability":"Ateşten birlikte sıçrayan çok sayıdaki yanar parçacık anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Parçacıkların ateşten sıçramasını ve topluluk oluşunu korur."},"facet_ids":["F001","F002"],"text":"kıvılcımlar","usage_role":"contextual"}],"definition":"Ateşten kopup havaya sıçrayan küçük, parlak ve yanar parçacıktır; tek bir parçacığı ve bunların topluluğunu bildiren biçimler aynı çekirdeğe bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ateşten ayrılıp havaya sıçrayan yanar parçacık temel nesnedir."},{"facet_id":"F002","role":"associated_use","statement":"Söz varlığı tek parçacık ile parçacıklar topluluğunu ayrı biçimlerle adlandırır."}],"identity_rationale":"Kaynak ifadesi dalı ateşten kopup havaya saçılan küçük, parlak parçalar olarak tutarlı biçimde tanımlar ve tekil ile topluluk biçimlerini aynı nesne çevresinde birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ateşten sıçrayan kıvılcımlar"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"kıvılcımlar topluluğu"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"tek kıvılcım"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"tek kıvılcım"}],"lexicalization_note":"Tanım yalın nesne anlamını verir; aynı kökün kötülük, serme ve kesme dalları bu kapsama alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; düşen ateş parçası en yakın sınırı, alev ise aynı alandaki temel nesne ayrımını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda havaya saçılma belirgindir; komşu dalda parçanın çakma anında düşmesi ve tutuşturma çubuğundan da çıkabilmesi belirleyicidir.","focus_only":"Odak dal ateşten havaya sıçrayan parçacıkların genel adıdır.","gloss":"kıvılcım ile çakma sırasında düşen ateş parçası","neighbor_only":"Komşu dal ateşten veya tutuşturma çubuğundan çakma sırasında düşen parçayı özellikle bildirir.","neighbor_ref":"root_000719/B005","relation_type":"near_synonym","shared_zone":"Her ikisi de ana ateşten ayrılan küçük yanar parçayı anlatır."},{"boundary_match":"field_only","distinction":"Kıvılcım ateşten ayrılan parçacıktır; alev ise ateşin kendisine bağlı, süreklilik gösteren yanma bölümüdür.","focus_only":"Odak dal ana ateşten kopup uçuşan küçük parçacığı bildirir.","gloss":"kıvılcım ile alev","neighbor_only":"Komşu dal ateşin bağlı ve sürekli yanan dili ile tutuşma durumunu bildirir.","neighbor_ref":"root_001379/B001","relation_type":"same_field","shared_zone":"İki kavram da yanan ateşin görünür ve ışıklı parçaları alanındadır."}],"source_phrase_ar":"الشرارة والجمع الشرار (maqayis)؛ الشرر ما تطاير من النار الواحدة شررة (maqayis)؛ الشرارة والشرر ما تطاير من النار (ayn)؛ شرار النار فيقال شررة وشرارة (jamhara)؛ الشرارة واحدة الشرار وهو ما يتطاير من النار وكذلك الشرر (sihah)؛ شرار النار ما تطاير منها (mufradat)","source_summary":"Bütün kaynaklar ateşten sıçrayan parçacık anlamında birleşir; farklılık yalnız tekil ve topluluk biçimlerinin düzenlenişindedir.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الشرر والشرار والشرارة وما يتطاير من النار","what_is_not_ar":"لا يدخل فيه الشر بمعنى السوء ولا بسط الشيء في الشمس"},"support_links":[]},{"boundary":"Dal ortaya çıkan parçanın adını tek başına bildirmez ve ateş parçacığı anlamıyla karıştırılmaz.","branch_kind":"bare","branch_ref":"root_000787/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"kesip parçalamak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesneyi kesme, yarma ve parçalara ayırma işlemi temel anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Isırılmış bir şeyi ağızdan silkeleyip çıkarma, kaynakta belirtilen özel eylemdir."}}],"root_ar":"ش ر ر","root_id":"root_000787","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin kesilerek, yarılarak veya birkaç parçaya ayrıldığı temel eylem için kullanılır.","boundary_detail":"Dal ortaya çıkan parçanın adını tek başına bildirmez ve ateş parçacığı anlamıyla karıştırılmaz.","branch_image_ar":"الشَّرْشَرَة تقطيع ونفض","concept_gloss":"kesip parçalamak","contextual_glosses":[{"applicability":"Isırılmış bir şeyin ağızdan silkelenerek çıkarıldığı özel kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Isırma sonrasında ağızdan silkeleyerek çıkarma işlemini korur."},"facet_ids":["F002"],"text":"ağızdan silkeleyip çıkarmak","usage_role":"contextual"}],"definition":"Bir şeyi kesmek, yarmak veya parçalara ayırmaktır. Ayrıca ısırılan bir şeyi ağızdan silkeleyip çıkarma eylemini anlatan özel bir kullanımı vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesneyi kesme, yarma ve parçalara ayırma işlemi temel anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Isırılmış bir şeyi ağızdan silkeleyip çıkarma, kaynakta belirtilen özel eylemdir."}],"identity_rationale":"Kaynak ifadesi kesme, yarma ve parçalara ayırma işlemini açıkça verir; ısırılmış bir şeyi ağızdan silkeleyip çıkarma ise aynı adlandırmanın ayrıca belirtilen özel kullanımıdır.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bir şeyi kesip yardı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kesip parçalama; ısırılan şeyi ağızdan silkeleyip çıkarma"}],"lexicalization_note":"Tanım yalın kesip yarma dalını ve kaynakta açıkça verilen ağızdan silkeleyip çıkarma kullanımını kapsar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yırtıp dağıtma ve kesip ayırma dalları eylemin sonucu ile aracına ilişkin en yararlı sınırları verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kesme ve yarma eylemine bağlıdır; komşu dal yırtılma ve dağılma sonucunu daha geniş nesne ve topluluklara taşır.","focus_only":"Odak dal ısırılmış şeyi ağızdan silkeleyip çıkarma özel kullanımını da içerir.","gloss":"kesip parçalama ile yırtıp dağıtma","neighbor_only":"Komşu dal kumaş yırtma dışında bulutları bölme, topluluğu dağıtma ve kıl yolma gibi daha geniş uygulamalara uzanır.","neighbor_ref":"root_001418/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bir bütünün yarılıp parçalara ayrılmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal parçalama ve yarma yönünü öne çıkarır; komşu dal kesme aracını ve ayrılan artığı da anlam yapısına katar.","focus_only":"Odak dal yarma ile ağızdan silkeleyip çıkarma kullanımını barındırır.","gloss":"parçalamak ile kesip ayırmak","neighbor_only":"Komşu dal makas veya dişle kesmeyi ve kesimden düşen artık parçaları ayrıca adlandırır.","neighbor_ref":"root_001217/B001","relation_type":"near_synonym","shared_zone":"İki dalın ortak çekirdeği bir şeyi keserek bütünlüğünden ayırmaktır."}],"source_phrase_ar":"شرشر الشيء إذا قطعه (maqayis)؛ الشرشرة أن تنفض الشيء من فيك بعد عضك إياه (maqayis)؛ شرشره أي قطع شراشره (ayn)؛ شرشرة الشيء تشقيقه وتقطيعه (sihah)","source_summary":"Kaynaklar kesme ve yarma anlamında birleşir; toplu ifade buna ısırılan şeyi ağızdan silkeleyip çıkarma kullanımını ekler.","sources":["MQ","AY","SI"],"what_is_ar":"يدخل فيه شرشرة الشيء بتقطيعه أو تشقيقه وما ينفض من الفم بعد العض","what_is_not_ar":"لا يدخل فيه شرر النار ولا شراشر النفس"},"support_links":[]},{"boundary":"Dal yalnız yağı damlayan pişmiş et niteliğidir; eti kurutmak, parçalamak veya yağı eritmek değildir.","branch_kind":"collocation","branch_ref":"root_000787/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"yağı damlayan pişmiş et","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Niteleme pişmiş etin yağının üzerinden damlayacak kadar bol olmasını bildirir."}}],"root_ar":"ش ر ر","root_id":"root_000787","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız pişmiş etin üzerinden yağ damlayacak ölçüde yağlı oluşunu niteleyen söz öbeği için geçerlidir.","boundary_detail":"Dal yalnız yağı damlayan pişmiş et niteliğidir; eti kurutmak, parçalamak veya yağı eritmek değildir.","branch_image_ar":"الشواء المتقاطر دسمه","concept_gloss":"yağı damlayan pişmiş et","contextual_glosses":[{"applicability":"Pişmiş etin belirgin biçimde yağ damlattığını canlı bir nitelemeyle aktaran bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yağın sürekli ve görünür biçimde damlamasını korur."},"facet_ids":["F001"],"text":"yağı şıpır şıpır damlayan","usage_role":"contextual"}],"definition":"Yalnız pişmiş et için kullanılan ve etin yağının bolca damladığını bildiren bir nitelemedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Niteleme pişmiş etin yağının üzerinden damlayacak kadar bol olmasını bildirir."}],"identity_rationale":"Kaynak ifadesi yalnız belirli bir yiyecek söz öbeğini tanımlar: pişmiş et öyle yağlıdır ki yağı damlar. Bu nedenle durum genel bir yağlılık veya eritme anlamına genişletilemez.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yağı damlayan pişmiş et"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"yağı damlayan pişmiş et"}],"lexicalization_note":"Tanım yalnız yağı damlayan pişmiş eti bildiren söz öbeğine bağlıdır; tek başına yalın kök anlamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; eritilmiş yağ ve pişmiş et kokusu, damlama niteliğini işlem ile kokudan ayıran en yararlı karşılaştırmalardır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak kavram etin gözlenen niteliğidir; komşu kavram yağın eritilme işlemi ile ortaya çıkan maddeyi adlandırır.","focus_only":"Odak dal pişmiş etin üzerinden yağ damlamasını niteler.","gloss":"yağı damlayan et ile eritilmiş yağ","neighbor_only":"Komşu dal yağın eritilmesini, erimiş yağı ve bu yağın yenme ya da sürünme kullanımını kapsar.","neighbor_ref":"root_000260/B005","relation_type":"same_field","shared_zone":"Her iki dal pişmiş yiyecek ve akışkan duruma gelmiş yağ alanında buluşur."},{"boundary_match":"field_only","distinction":"Biri yağın damlama durumudur, öteki pişirme sırasında yayılan koku ve dumandır.","focus_only":"Odak dal pişmiş etten damlayan yağı görsel bir özellik olarak bildirir.","gloss":"damlayan yağ ile pişmiş et kokusu","neighbor_only":"Komşu dal pişmiş etin ya da yağın kokusunu ve dumanını bildirir.","neighbor_ref":"root_001199/B003","relation_type":"same_field","shared_zone":"İki kavram da pişmiş et ve yağın duyularla algılanan özelliklerine ilişkindir."}],"source_phrase_ar":"الشواء الشرشار الذي يتقاطر دسمه (maqayis)؛ شواء شرشر يتقاطر دسمه (sihah)","source_summary":"Kaynaklar söz öbeğini yağı damlayan pişmiş et nitelemesi olarak aynı sınırla açıklar.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه وصف الشواء بأنه شرشار أو شرشر إذا تقاطر دسمه","what_is_not_ar":"لا يدخل فيه بسط اللحم ليجف ولا تقطيعه"},"support_links":[]},{"boundary":"Sarkan kuyruk uçları ile ağırlıklar ayrı facetlerdir; benliğini ve ilgisini bütünüyle verme deyimi bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000787/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"kuyrukların sarkan uçları veya ağırlıklar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Söz öbeğine bağlı kullanım kuyrukların aşağı sarkan ve salınan uçlarını bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yalın ad kullanımı ayrı bir anlam olarak ağırlıkları, tekil biçimiyle de bir ağırlığı bildirir."}}],"root_ar":"ش ر ر","root_id":"root_000787","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın birbirinden ayrılması gereken söz öbeği kullanımı ile yalın ad kullanımını birlikte gösteren açıklayıcı üst karşılıktır.","boundary_detail":"Sarkan kuyruk uçları ile ağırlıklar ayrı facetlerdir; benliğini ve ilgisini bütünüyle verme deyimi bu dala girmez.","branch_image_ar":"الشراشر ذباذب وأثقال","concept_gloss":"kuyrukların sarkan uçları veya ağırlıklar","contextual_glosses":[{"applicability":"Yalnız kuyruklara bağlı sarkan ve salınan uçları bildiren söz öbeğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kuyruk bağımlılığını ve aşağı sarkan uç niteliğini korur."},"facet_ids":["F001"],"text":"kuyrukların sarkan uçları","usage_role":"contextual"},{"applicability":"Yalın çoğul biçimin taşınan veya yük oluşturan ağırlıkları bildirdiği kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ayrı yalın kullanımın ağırlık nesnelerini korur."},"facet_ids":["F002"],"text":"ağırlıklar","usage_role":"contextual"}],"definition":"Belirli bir söz öbeğinde kuyrukların sarkan, salınan uçlarını anlatır. Yalın çoğul biçim ise ayrı bir kullanımda ağırlıkları bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Söz öbeğine bağlı kullanım kuyrukların aşağı sarkan ve salınan uçlarını bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Yalın ad kullanımı ayrı bir anlam olarak ağırlıkları, tekil biçimiyle de bir ağırlığı bildirir."}],"identity_rationale":"Kaynak ifadesi aynı biçim altında iki ayrı kapsam verir: kuyrukların sarkan uçları yalnız belirli bir söz öbeğinde bulunurken ağırlıklar yalın ad kullanımıdır. Dal korunabilir, ancak bu iki kullanım ortak bir nesneymiş gibi birleştirilemez.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"kuyrukların sarkan ve salınan uçları"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"ağırlıklar"}],"lexicalization_note":"Tanım söz öbeğine bağlı sarkan kuyruk uçlarını yalın biçimin ağırlık anlamından açıkça ayırır ve ikisini tek çekirdekte eritmez.","neighbor_coverage_note":"Bütün adaylar her iki facet bakımından değerlendirildi; sarkan uç ve ağır yük karşılaştırmaları dalın iki ayrı kapsamını en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kullanım kuyruklarla sınırlıdır; komşu kavram çok çeşitli nesnelerin uç ve bağlarını içine alan daha geniş bir sınıftır.","focus_only":"Odak dal sarkan uçları yalnız kuyruklara bağlı söz öbeğinde bildirir ve ayrıca ayrı bir ağırlık anlamı taşır.","gloss":"kuyruk ucu ile sarkan uç veya bağ","neighbor_only":"Komşu dal kamçı, dil, bez, kayış, ip ve dal gibi çok çeşitli sarkan uç veya bağları kapsar.","neighbor_ref":"root_000994/B006","relation_type":"near_synonym","shared_zone":"İki dalın ortak alanı aşağı doğru sarkan ince uçlardır."},{"boundary_match":"partial","distinction":"Odak dal yalnız nesne adı düzeyinde ağırlıkları verir; komşu dal taşıyan kişiye yüklenen somut veya soyut ağır sorumluluğu öne çıkarır.","focus_only":"Odak dalın yalın kullanımı somut ağırlıkları adlandırır.","gloss":"ağırlıklar ile taşınan ağır yük","neighbor_only":"Komşu dal taşınan ağır yükten günah ve bağlayıcı söz gibi soyut yüklere de uzanır.","neighbor_ref":"root_000037/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal yük ve ağırlık alanında kesişir."}],"source_phrase_ar":"شراشر الأذناب ذباذبها (maqayis;sihah)؛ الشراشر الأثقال الواحدة شرشرة (sihah)","source_summary":"Toplu kaynak ifadesi kuyrukların sarkan uçlarını ortak söz öbeği içinde verir; ayrıca kaynaklardan birinde aynı çoğul biçim ağırlıklar olarak açıklanır.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه شراشر الأذناب وذباذبها والأثقال المسماة شراشر","what_is_not_ar":"لا يدخل فيه إلقاء النفس كلها حرصا ومحبة ولا الشرر"},"support_links":[]},{"boundary":"Dal sıradan ilgiyi veya yalnız sevmeyi değil, benliğin ve bütün uğraşların yoğun biçimde yöneltilmesini gerektirir.","branch_kind":"non_bare","branch_ref":"root_000787/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"kendini bütün isteğiyle vermek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi kendisini, isteğini ve bütün ilgilerini tek bir hedefe bütünüyle yöneltir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu bütünüyle yöneliş sevgi, güçlü istek ve yoğun düşkünlükle gerçekleşir."}}],"root_ar":"ش ر ر","root_id":"root_000787","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin bütün benliğini ve ilgilerini sevgi veya yoğun istekle tek hedefe yönelttiği sabit söz birimi için kullanılır.","boundary_detail":"Dal sıradan ilgiyi veya yalnız sevmeyi değil, benliğin ve bütün uğraşların yoğun biçimde yöneltilmesini gerektirir.","branch_image_ar":"إلقاء الشراشر إلقاء النفس كلها","concept_gloss":"kendini bütün isteğiyle vermek","contextual_glosses":[{"applicability":"Yönelişin sevgi ve güçlü kişisel bağlılık olarak öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bütün benlikle yönelmeyi ve güçlü bağlılığı korur."},"facet_ids":["F001","F002"],"text":"bütün varlığıyla bağlanmak","usage_role":"contextual"}],"definition":"Kişinin bütün benliğini, isteğini ve zihinsel uğraşlarını sevgi ya da yoğun istekle birine veya bir şeye yöneltmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi kendisini, isteğini ve bütün ilgilerini tek bir hedefe bütünüyle yöneltir."},{"facet_id":"F002","role":"specialization","statement":"Bu bütünüyle yöneliş sevgi, güçlü istek ve yoğun düşkünlükle gerçekleşir."}],"identity_rationale":"Kaynak ifadesi sabit söz birimini kişinin bütün benliğini, isteğini ve ilgilerini sevgi ya da güçlü istekle birine veya bir şeye yöneltmesi olarak açıklar.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kendini, isteğini ve bütün ilgisini ona verdi"}],"lexicalization_note":"Tanım yalnız kaynakta verilen sabit söz birimine aittir; buradan yalın bir kök anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; güçlü tutku ve bir işe kapanma, bütün benliği verme anlamının duygu ile süreklilik sınırlarını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kavram kişinin kendisini bütünüyle yöneltmesini anlatan bir eylemdir; komşu kavram kalıcı ve şiddetli tutku durumunu öne çıkarır.","focus_only":"Odak dal benliğin ve bütün ilgilerin tek hedefe yöneltilmesi işlemini bildirir.","gloss":"kendini vermek ile güçlü tutku","neighbor_only":"Komşu dal kişiye ya da şeye yapışan sürekli ve şiddetli tutku durumunu bildirir.","neighbor_ref":"root_001081/B004","relation_type":"near_synonym","shared_zone":"Her iki dal yoğun sevgi, düşkünlük ve hedeften kopamama alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal duygusal ve istemli bir bütünlük bildirir; komşu dal süreklilik gösteren uğraş veya bedensel yönelişle tanımlanır.","focus_only":"Odak dal sevgi veya istekle bütün benliği ve ilgileri hedefe vermeyi gerektirir.","gloss":"kendini vermek ile bir işe kapanmak","neighbor_only":"Komşu dal bir işe kapanıp sürekli uğraşmayı, öne eğilmeyi veya bir kişiyi ısrarla izlemeyi kapsar.","neighbor_ref":"root_001278/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da kişinin dikkatini bir hedef üzerinde yoğunlaştırması vardır."}],"source_phrase_ar":"ألقى عليه شراشره إذا ألقى عليه نفسه حرصا ومحبة (maqayis)؛ ألقى علي شراشره أي ألقى علي نفسه حرصا (ayn)؛ ألقى عليه شراشره أي نفسه حرصا ومحبة (sihah)؛ جمع ما انتشر من هممه لهذا الشيء وشغل همومه كلها به (maqayis)","source_summary":"Kaynaklar kişinin kendisini ve bütün isteğini hedefe vermesinde birleşir; toplu ifade ayrıca dağınık ilgilerin tek şeyde toplanmasını açıklar.","sources":["MQ","AY","SI"],"what_is_ar":"يدخل فيه قولهم ألقى عليه شراشره أي ألقى عليه نفسه وحرصه وهممه كلها","what_is_not_ar":"لا يدخل فيه شراشر الأذناب ولا الأثقال الحسية"},"support_links":[]},{"boundary":"Dal görünür kılma anlamıyla korunur; tartışmalı işaret etme örneği kesin bir gösterme tanığı sayılmaz.","branch_kind":"unresolved","branch_ref":"root_000787/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"görünür kılmak","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi görünür duruma getirme ve ortaya koyma eylemi temel anlamdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli bir işaret etme örneği, gösterme yerine işaret edilen kişiyi kötülüğe bağlama olarak da yorumlanabilir."}}],"root_ar":"ش ر ر","root_id":"root_000787","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin saklı veya geri planda kalmış durumdan çıkarılıp görülebilir hale getirildiği kullanım için geçerlidir.","boundary_detail":"Dal görünür kılma anlamıyla korunur; tartışmalı işaret etme örneği kesin bir gösterme tanığı sayılmaz.","branch_image_ar":"إظهار الشيء وإبرازه","concept_gloss":"görünür kılmak","contextual_glosses":[{"applicability":"Bir şeyin gizli veya örtülü konumdan çıkarılarak göz önüne getirildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gizli konumdan çıkarma ve görünür hale getirme işlemini korur."},"facet_ids":["F001"],"text":"ortaya çıkarmak","usage_role":"contextual"},{"applicability":"Yalnız tartışmalı işaret etme örneğinin alternatif kaynak yorumunu açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşaret edilen kişiyi kötülüğe bağlama yorumunu korur."},"facet_ids":["F002"],"text":"birini kötü sayarak işaret etmek","usage_role":"explanatory"}],"definition":"Bir şeyi saklı veya geri planda kalmış durumdan çıkarıp görünür kılmak ve ortaya koymaktır. Belirli bir işaret etme örneğinin ise birini kötülüğe bağlama anlamında olabileceği ayrıca belirtilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi görünür duruma getirme ve ortaya koyma eylemi temel anlamdır."},{"facet_id":"F002","role":"source_variant","statement":"Belirli bir işaret etme örneği, gösterme yerine işaret edilen kişiyi kötülüğe bağlama olarak da yorumlanabilir."}],"identity_rationale":"Kaynak ifadesinin çoğu bir şeyi görünür kılma ve ortaya çıkarma anlamını doğrudan destekler. Bununla birlikte belirli bir örnek için, hareketin göstermeden çok işaret edilen kişiyi kötülüğe bağlama anlamına gelebileceği yönünde kaynaklar arası bir yorum ayrılığı vardır.","lexicalization_note":"Tanım kanıttaki görünür kılma kullanımını açıklar, ancak yalın dal statüsü çözülmediği için bunu genel bir yalın kök anlamı olarak varsaymaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; görünür olma ve gizliliği gidererek dışarı çıkarma dalları, geçişli görünür kılma anlamının en yakın sınırlarını verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kavram bir nesneyi görünür hale getiren geçişli işlemdir; komşu kavram hem ortaya çıkışı hem ortaya çıkarmayı ve yayımlanmış olmayı kapsayan daha geniş bir alandır.","focus_only":"Odak dal bir nesneyi etkin biçimde görünür kılma ve ortaya koyma eylemidir.","gloss":"görünür kılmak ile görünür olmak","neighbor_only":"Komşu dal kendiliğinden görünür olmayı, örtünün açılmasını ve bir yazının yayımlanmış durumunu da kapsar.","neighbor_ref":"root_000105/B001","relation_type":"near_synonym","shared_zone":"Her iki dal gizli veya örtülü olanın göz önüne gelmesi alanında kesişir."},{"boundary_match":"partial","distinction":"Odak dalın sonucu görünürlüktür; komşu dal gizliliği kaldıran ve saklanan varlığı bulunduğu yerden çıkaran özel işlemi de içerir.","focus_only":"Odak dal nesneyi genel olarak görünür kılmayı bildirir.","gloss":"görünür kılmak ile gizliliği giderip dışarı çıkarmak","neighbor_only":"Komşu dal gizliliği gidermeyi ve yağmurun saklanan küçük hayvanları yuvalarından çıkarması gibi dışarı çıkarma örneklerini kapsar.","neighbor_ref":"root_000428/B003","relation_type":"near_synonym","shared_zone":"İki dal saklı olanı açığa çıkarma işleminde örtüşür."}],"source_phrase_ar":"أشررت الشيء إذا أبرزته وأظهرته (maqayis)؛ أشررت الشيء أظهرته (sihah)؛ يحتمل أنها نسبت الأصابع إلى الشر بالإشارة إليه (mufradat)","source_summary":"Toplu kaynak ifadesi görünür kılma ve ortaya çıkarma açıklamasını verir; ayrıca belirli bir işaret etme örneğinin kişiyi kötülüğe bağlama biçiminde anlaşılabileceği karşıt yorumunu kaydeder.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه أشررت الشيء إذا أبرزته أو أظهرته","what_is_not_ar":"لا يدخل فيه أشررت فلانا بمعنى نسبته إلى الشر"},"support_links":[]},{"boundary":"Dal genel zararı veya bütün küçük böcekleri değil, yüz çevresinde dolaşan ve ısırmayan belirli böcek türünü bildirir.","branch_kind":"bare","branch_ref":"root_000787/B009","candidate_links":[{"candidate_id":"cand_7983e493711ca3a93025","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"yüz çevresinde dolaşan ısırmayan sivrisinek benzeri böcek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sivrisineğe benzeyen küçük bir böcek türü temel varlıktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsanın yüzü çevresinde dolaşıp rahatsız eder, ancak ısırmaz."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Topluluk ve bu topluluğun tek bireyi ayrı ad biçimleriyle gösterilir."}}],"root_ar":"ش ر ر","root_id":"root_000787","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Türün görünüşünü, insana yaklaşma biçimini ve ısırmama sınırını birlikte açıklamak gerektiğinde kullanılır.","boundary_detail":"Dal genel zararı veya bütün küçük böcekleri değil, yüz çevresinde dolaşan ve ısırmayan belirli böcek türünü bildirir.","branch_image_ar":"الشَّرّان أذى كالبعوض","concept_gloss":"yüz çevresinde dolaşan ısırmayan sivrisinek benzeri böcek","contextual_glosses":[{"applicability":"Canlının yüz çevresinde dolaşarak verdiği rahatsızlığın öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":"Başka rahatsız edici küçük böcek türlerini de kapsayabilecek genel bir sınıf ekler.","collision":"Türün sivrisineğe benzeme ve ısırmama özelliklerini tek başına ayırt etmez.","fit":"broadening","loses":null,"preserves":"Küçük böcek oluşunu ve rahatsız edici davranışını korur."},"facet_ids":["F001","F002"],"text":"rahatsız edici küçük böcek","usage_role":"contextual"}],"definition":"Sivrisineğe benzeyen, insanın yüzü çevresinde dolaşıp rahatsız eden fakat ısırmayan küçük bir böcek türüdür; tek bireyi ayrı bir biçimle adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sivrisineğe benzeyen küçük bir böcek türü temel varlıktır."},{"facet_id":"F002","role":"specialization","statement":"İnsanın yüzü çevresinde dolaşıp rahatsız eder, ancak ısırmaz."},{"facet_id":"F003","role":"associated_use","statement":"Topluluk ve bu topluluğun tek bireyi ayrı ad biçimleriyle gösterilir."}],"identity_rationale":"Kaynak ifadesi dalı sivrisineğe benzeyen, insanın yüzü çevresinde dolaşan ve ısırmayan küçük bir böcek türü olarak açıkça sınırlar; rahatsızlık adı bu canlıya verilen ikincil adlandırmadır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"yüz çevresinde dolaşan, ısırmayan sivrisinek benzeri böcekler"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bu türden tek böcek"}],"lexicalization_note":"Tanım yalın böcek adını kapsar ve onun belirtilen davranış özelliklerini korur; genel kötülük anlamına genişlemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sivrisinek ve genel sinek türü karşılaştırmaları bu canlının ısırmama ve yüz çevresinde dolaşma özelliklerini en iyi sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak türün ayırıcı özelliği yüz çevresinde dolaşıp ısırmamasıdır; komşu tür gerçek sivrisinek ve onun zararlarıdır.","focus_only":"Odak dal sivrisineğe benzeyen fakat ısırmayan ve yüz çevresinde dolaşan ayrı bir türdür.","gloss":"ısırmayan benzer böcek ile sivrisinek","neighbor_only":"Komşu dal bilinen sivrisineği, onun ısırma zararını ve bir yerde çoğalmasını kapsar.","neighbor_ref":"root_000133/B002","relation_type":"near_synonym","shared_zone":"İki dal küçük, uçan, insanı rahatsız eden ve görünüşçe birbirine benzeyen böcekleri anlatır."},{"boundary_match":"field_only","distinction":"Odak böcek görünüş ve davranışla ayrıntılı biçimde sınırlandırılır; komşu böcek için yalnız tür adı niteliği bildirilir.","focus_only":"Odak dal sivrisineğe benzer, yüz çevresinde dolaşır ve ısırmaz.","gloss":"sivrisinek benzeri böcek ile sinek türü","neighbor_only":"Komşu dal yalnız bir sinek türü olarak verilir ve bu davranış özellikleriyle tanımlanmaz.","neighbor_ref":"root_000338/B005","relation_type":"same_field","shared_zone":"Her ikisi de küçük uçucu böcek adlarıdır."}],"source_phrase_ar":"الشران شيء تسميه العرب الأذى شبه البعوض يغشى وجه الإنسان لا يعض الواحدة شرانة (ayn)؛ الشران شبيه بالبعوض يغشى وجه الإنسان ولا يعض وربما سموه الأذى (sihah)","source_summary":"Kaynaklar sivrisineğe benzeyen, yüz çevresini saran ve ısırmayan böcek tanımında birleşir; bu canlıya rahatsızlık veren şey anlamında bir ad da verildiği belirtilir.","sources":["AY","SI"],"what_is_ar":"يدخل فيه الشرّان وهو شيء شبيه بالبعوض أو الأذى يغشى وجه الإنسان ولا يعض","what_is_not_ar":"لا يدخل فيه الشر بمعنى السوء ولا الشرر"},"support_links":["sup_86b6ecca7eb8170531c4"]},{"boundary":"Dal her yaştaki canlılığı değil, yalnız gençliğin güçlü isteğiyle birleşen hareketliliğini bildirir.","branch_kind":"collocation","branch_ref":"root_000787/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"gençlik canlılığı ve atılganlığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gençlik dönemindeki belirgin canlılık ve hareket gücü temel durumdur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Canlılığa güçlü istek ve heves eşlik eder."}}],"root_ar":"ش ر ر","root_id":"root_000787","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız gençlik dönemine özgü hareket gücü ile güçlü isteğin birlikte anlatıldığı söz öbeği için geçerlidir.","boundary_detail":"Dal her yaştaki canlılığı değil, yalnız gençliğin güçlü isteğiyle birleşen hareketliliğini bildirir.","branch_image_ar":"شِرّة الشباب نشاط وحرص","concept_gloss":"gençlik canlılığı ve atılganlığı","contextual_glosses":[{"applicability":"Gençliğin taşkın canlılığını ve güçlü hevesini doğal bir anlatımla aktaran bağlamlarda kullanılır.","error_profile":{"adds":"Düşüncesiz taşkınlık veya geçici tutku çağrışımı ekleyebilir.","collision":"Gerçek ateşle ilgili bir anlatım sanılabilir.","fit":"broadening","loses":null,"preserves":"Gençlik dönemindeki yoğun canlılık ve atılganlık izlenimini korur."},"facet_ids":["F001","F002"],"text":"gençlik ateşi","usage_role":"contextual"}],"definition":"Gençlik dönemine özgü güçlü canlılığı, hevesi ve harekete geçme isteğini birlikte bildiren bir söz öbeğidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gençlik dönemindeki belirgin canlılık ve hareket gücü temel durumdur."},{"facet_id":"F002","role":"specialization","statement":"Canlılığa güçlü istek ve heves eşlik eder."}],"identity_rationale":"Kaynak ifadesi belirli söz öbeğini gençlik dönemine özgü canlılık ve güçlü istek olarak tanımlar; bu anlam genel canlılık dalına dönüştürülmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"gençliğin canlılığı, güçlü isteği ve atılganlığı"}],"lexicalization_note":"Tanım yalnız gençliğin canlılığı ve güçlü isteğini bildiren söz öbeğine bağlıdır; yalın kök anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel canlılık ve genç beden dolgunluğu, yaşa bağlı atılganlığın işlevsel ve bedensel komşularını açıkça ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kavram yaş dönemi ve güçlü hevesle sınırlıdır; komşu kavram yaş sınırı olmayan genel bir canlılık ve iyi oluş durumudur.","focus_only":"Odak dal gençlik dönemine ve güçlü istekle birleşen atılganlığa bağlıdır.","gloss":"gençlik atılganlığı ile genel canlılık","neighbor_only":"Komşu dal her yaştaki insanın veya hayvanın çalışma ve hareket için duyduğu genel canlılığı kapsar.","neighbor_ref":"root_001505/B001","relation_type":"near_synonym","shared_zone":"Her iki dal hareket etme ve çalışma isteği veren canlılık durumunu anlatır."},{"boundary_match":"field_only","distinction":"Odak ruhsal ve davranışsal canlılıktır; komşu dal bedensel dolgunluk ve görünüş özelliğidir.","focus_only":"Odak dal gencin hareketli, hevesli ve atılgan oluşunu bildirir.","gloss":"gençlik canlılığı ile genç beden dolgunluğu","neighbor_only":"Komşu dal gencin bedence dolgun, güçlü ve gençlikle gelişmiş görünümünü bildirir.","neighbor_ref":"root_001043/B011","relation_type":"same_field","shared_zone":"İki dal da gençlik dönemindeki belirgin güç ve gelişmişlik alanındadır."}],"source_phrase_ar":"شرة الشباب نشاطه ولهذا باب تراه (jamhara)؛ شرة الشباب حرصه ونشاطه (sihah)","source_summary":"Kaynaklar gençlik döneminin canlılığı ve güçlü isteği üzerinde birleşir; söz öbeği bu iki özelliği tek durumda toplar.","sources":["JA","SI"],"what_is_ar":"يدخل فيه شرة الشباب بمعنى نشاطه وحرصه","what_is_not_ar":"لا يدخل فيه الشر بمعنى السوء ولا المخاصمة"},"support_links":[]},{"boundary":"Dal genel çekişmeyi bildirir; düşmanlığı açıkça gösterme, şakalaşma veya yalnız karşı çıkma anlamları kendiliğinden buna girmez.","branch_kind":"bare","branch_ref":"root_000787/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"çekişme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tarafların birbirine karşı çıkarak çekişmesi temel anlamdır."}}],"root_ar":"ش ر ر","root_id":"root_000787","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tarafların birbirine karşı çıktığı genel uyuşmazlık ve ağız dalaşı durumunda kullanılır.","boundary_detail":"Dal genel çekişmeyi bildirir; düşmanlığı açıkça gösterme, şakalaşma veya yalnız karşı çıkma anlamları kendiliğinden buna girmez.","branch_image_ar":"المشارة مخاصمة","concept_gloss":"çekişme","contextual_glosses":[{"applicability":"Çekişmenin özellikle sözlü karşı çıkış ve tartışma biçiminde gerçekleştiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Söz dışındaki tutumlarla gerçekleşebilecek daha genel çekişme kapsamını dışarıda bırakır.","preserves":"Taraflar arasındaki karşılıklı sözlü çekişmeyi korur."},"facet_ids":["F001"],"text":"ağız dalaşı","usage_role":"contextual"}],"definition":"İki ya da daha çok tarafın söz veya tutumla birbirine karşı çıktığı çekişme ve ağız dalaşıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tarafların birbirine karşı çıkarak çekişmesi temel anlamdır."}],"identity_rationale":"Tek kaynak ifadesi dalı doğrudan karşılıklı çekişme ve ağız dalaşı olarak tanımlar; daha dar bir araç, sonuç veya taraf yapısı belirtilmez.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"çekişme; ağız dalaşı"}],"lexicalization_note":"Tanım yalın çekişme adını kapsar; komşu dallardaki belirli tartışma biçimleri veya sonuçları eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sözle özel çekişme ve karşılıklı suç atma adayları genel çekişmenin en yakın iki sınırını verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kavram genel çekişmedir; komşu kavram tartışmanın sözle ve sözü eğip bükme yoluyla yürütülen özel biçimidir.","focus_only":"Odak dal çekişmenin genel adıdır ve belirli bir sözlü yöntemi şart koşmaz.","gloss":"çekişme ile sözü eğip bükerek tartışma","neighbor_only":"Komşu dal karşı tarafın sözünü eğip bükerek yürütülen sözlü çekişmeyi özellikle bildirir.","neighbor_ref":"root_001037/B012","relation_type":"near_synonym","shared_zone":"Her iki dal karşı tarafla sözlü uyuşmazlık ve tartışma alanında kesişir."},{"boundary_match":"partial","distinction":"Odak dal yalın çekişme adıdır; komşu dal karşılıklı itme, direnme ve sorumluluğu ötekine yükleme yapısıyla daha ayrıntılıdır.","focus_only":"Odak dal taraf sayısı ve suç aktarma gibi ek koşullar olmadan genel çekişmeyi bildirir.","gloss":"çekişme ile karşılıklı itişme ve suç atma","neighbor_only":"Komşu dal tarafların birbirini itmesini, karşılıklı direnmesini ve işi ya da suçu ötekine atmasını kapsar.","neighbor_ref":"root_000466/B002","relation_type":"near_synonym","shared_zone":"Her iki dal birden çok tarafın birbirine karşı çıktığı uyuşmazlığı anlatır."}],"source_phrase_ar":"المشارة المخاصمة (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Sözcük karşılıklı çekişme ve ağız dalaşı adı olarak verilir."}],"source_summary":"Dal yalnız bir kaynakta doğrudan karşılıklı çekişme anlamıyla tanıklanmıştır.","sources":["SI"],"what_is_ar":"يدخل فيه المشارة بمعنى المخاصمة","what_is_not_ar":"لا يدخل فيه الشر بمعنى السوء ولا شرة الشباب"},"support_links":[]},{"boundary":"Dal yalnız kaynakta adı verilen bitkiyi bildirir; kesme eylemi ve ateş parçacığı anlamları dışarıda kalır.","branch_kind":"bare","branch_ref":"root_000787/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"adı belirtilen bir bitki","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Söz belirli bir bitkinin adı olarak kullanılır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynak bitkinin görünüşü, yetişme yeri veya kullanımına ilişkin ek ayırt edici bilgi vermez."}}],"root_ar":"ش ر ر","root_id":"root_000787","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kanıt yalnız bitki adı işlevini desteklediğinden, ek tür özelliği ileri sürmeden açıklama yapılacağı zaman kullanılır.","boundary_detail":"Dal yalnız kaynakta adı verilen bitkiyi bildirir; kesme eylemi ve ateş parçacığı anlamları dışarıda kalır.","branch_image_ar":"الشِّرْشِر نبت","concept_gloss":"adı belirtilen bir bitki","contextual_glosses":[{"applicability":"Bitkinin adı hedef dilde yeniden üretilmeden yalnız varlık sınıfının belirtilmesi gereken bağlamlarda kullanılır.","error_profile":{"adds":"Belirli bitki yerine herhangi bir bitki türünü kapsayabilecek genel bir sınıf ekler.","collision":"Kanıttaki belirli adın hangi bitkiye ait olduğunu ayırt ettirmez.","fit":"broadening","loses":null,"preserves":"Sözün bir bitkiyi adlandırdığı bilgisini korur."},"facet_ids":["F001"],"text":"bir bitki türü","usage_role":"explanatory"}],"definition":"Kaynakta yalnızca adı belirtilen, ayırt edici özellikleri veya kullanım alanı açıklanmayan bir bitkidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Söz belirli bir bitkinin adı olarak kullanılır."},{"facet_id":"F002","role":"source_variant","statement":"Kaynak bitkinin görünüşü, yetişme yeri veya kullanımına ilişkin ek ayırt edici bilgi vermez."}],"identity_rationale":"Tek kaynak ifadesi bu dalı özellikleri açıklanmayan bir bitki adı olarak verir. Kanıt, bitkinin türünü başka bir bilinen bitkiyle özdeşleştirmeye veya adına hedef dilde yeni bir biçim vermeye yetmez.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"kaynakta adı verilen bir bitki"}],"lexicalization_note":"Tanım yalın bitki adı dalını kapsar; kanıtta bulunmayan görünüş, kullanım veya tür özellikleri eklenmez.","neighbor_coverage_note":"Bütün adaylar yalnız başka bitki adlarıdır; kanıt ayırt edici botanik özellik vermediği için güvenilir ve yararlı bir karşılaştırma yayımlanamaz.","source_phrase_ar":"الشرشر نبت يقال له الشرشر بالكسر (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Sözcük, tür özellikleri belirtilmeden bir bitkinin adı olarak verilir."}],"source_summary":"Dal yalnız bir kaynakta, başka bir özelliği açıklanmayan bitki adı olarak tanıklanmıştır.","sources":["SI"],"what_is_ar":"يدخل فيه اسم النبات الشرشر بالكسر","what_is_not_ar":"لا يدخل فيه الشرشرة بمعنى التقطيع ولا الشرر"},"support_links":[]},{"boundary":"Anlam, bedelli değiş tokuşla sınırlıdır; benzerlik, yön, bitki ve taşkın hareket anlamlarını içermez.","branch_kind":"bare","branch_ref":"root_000792/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"bedel karşılığında alıp satma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bedelli değişimde bir malı edinme ve elden çıkarma yönlerinin ikisini de kapsar."}}],"root_ar":"ش ر ر","root_id":"root_000792","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedelli bir değişimin hem edinme hem de elden çıkarma yönünün birlikte temsil edildiği genel kullanımlara uygundur.","boundary_detail":"Anlam, bedelli değiş tokuşla sınırlıdır; benzerlik, yön, bitki ve taşkın hareket anlamlarını içermez.","branch_image_ar":"المعاوضة بين بيع وشراء","concept_gloss":"bedel karşılığında alıp satma","contextual_glosses":[{"applicability":"Bağlamın malı bedel karşılığında elden çıkaran tarafı öne çıkardığı yerlerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı biçimin edinme yönünü de gösterebilmesini dışarıda bırakır.","preserves":"Bedel karşılığında elden çıkarma yönünü korur."},"facet_ids":["F001"],"text":"satmak","usage_role":"contextual"},{"applicability":"Bağlamın bir şeyi sahibinden bedeli karşılığında edinmeyi öne çıkardığı yerlerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı biçimin elden çıkarma yönünü de gösterebilmesini dışarıda bırakır.","preserves":"Bedel karşılığında edinme yönünü korur."},"facet_ids":["F001"],"text":"satın almak","usage_role":"contextual"}],"definition":"Bir şeyi sahibinden bedeli karşılığında almak ya da bir şeyi bedeli karşılığında başkasına vermektir; aynı değişimin alış ve satış yönleri birlikte ifade edilebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bedelli değişimde bir malı edinme ve elden çıkarma yönlerinin ikisini de kapsar."}],"identity_rationale":"Kaynak ifadesi, bedel karşılığında bir şeyi hem edinme hem de elden çıkarma yönlerini açıkça bildirir. Bu nedenle dal, alış ve satışın karşılıklı değişim içindeki iki yönünü birlikte kapsar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"satmak veya bedelini verip almak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"satın almak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"alış ve satış"}],"lexicalization_note":"Dal yalın kullanımdır; tanım herhangi bir özel tamlamaya bağlı olmadan bedelli alış ve satışı kapsar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; işlem çekirdeğini doğrudan paylaşan tek yararlı karşılaştırma yayımlandı, diğerleri fiyat, zarar veya özel satış türleriyle sınırlı kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ayırıcı yanı, aynı kullanımın değişimin iki karşıt yönünden birini bağlama göre gösterebilmesidir; komşu dal ise bu işlemleri genel satış alanı olarak sunar.","focus_only":"Tek bir söz biçiminin bağlama göre hem alma hem satma yönünü gösterebilmesi bu dala özgüdür.","gloss":"bedelli alışveriş","neighbor_only":"Komşu dal, satış işleminin taraflarını ve işlem adlarını daha genel bir ticaret alanında toplar.","neighbor_ref":"root_000169/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da mal ile bedelin el değiştirdiği alış ve satış işlemlerini kapsar."}],"source_phrase_ar":"شريت الشيء واشتريته إذا أخذته من صاحبه بثمنه (maqayis); شرى يشري شرى وشراء وهو شار إذا باع (ayn); شريت الشيء إذا بعته وإذا اشتريته أيضا (sihah); الشراء والبيع يتلازمان (mufradat); شريت بمعنى بعت وشريت أي اشتريت (tahdhib)","source_summary":"Kaynakların ortak anlatımı, alış ile satışın aynı bedelli değişimin birbirine bağlı iki yönü olduğunu ve ilgili kullanımın her iki yönü de gösterebildiğini belirtir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"البيع والابتياع والمشاراة، واستعمال شريت وشروا واشتروا في أخذ شيء بثمن أو دفعه بثمن","what_is_not_ar":"المثل والنواحي والنبات والهيجان"},"support_links":[]},{"boundary":"Dal, iki şey arasındaki benzerlik ve denklik ilişkisini bildirir; bedelli değişim ya da karşılıklı işlem anlamı taşımaz.","branch_kind":"bare","branch_ref":"root_000792/B002","candidate_links":[{"candidate_id":"cand_cc2dd73a9f468d6783ea","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"eş ve denk","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığı başka bir varlığın benzeri, eşi veya dengi olarak gösterir."}}],"root_ar":"ش ر ر","root_id":"root_000792","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin başka bir şeyle benzerlik veya denklik ilişkisi içinde sunulduğu genel kullanımlara uygundur.","boundary_detail":"Dal, iki şey arasındaki benzerlik ve denklik ilişkisini bildirir; bedelli değişim ya da karşılıklı işlem anlamı taşımaz.","branch_image_ar":"المماثلة والمقابلة","concept_gloss":"eş ve denk","contextual_glosses":[{"applicability":"Bir nesnenin başka bir nesneye örnek veya nitelik bakımından benzetildiği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bağlamdaki benzerlik ve eşlik yargısını doğal biçimde korur."},"facet_ids":["F001"],"text":"onun gibisi","usage_role":"contextual"}],"definition":"Bir şeyin başka bir şeye benzemesi ve onun eşi ya da dengi sayılmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığı başka bir varlığın benzeri, eşi veya dengi olarak gösterir."}],"identity_rationale":"Kaynak ifadesi bu dalı doğrudan bir şeyin benzeri, eşi veya dengi olarak tanımlar. Geçici çerçeve bu kimliği doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"benzeri ve dengi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"eş ve benzer"}],"lexicalization_note":"Dal yalın kullanımdır ve tanım, belirli bir kalıba bağlı olmadan eşlik ve benzerlik ilişkisini verir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel benzerlik alanını en açık biçimde paylaşan komşu seçildi, öteki adaylar özel karşıtlık veya eşleşme koşulları ekledi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın kapsamı eş ya da denk olan varlık üzerindedir; komşu dal ise benzerlik kurma ve eşitleme süreçlerini de içine alır.","focus_only":"Odak dal, bir varlığı doğrudan başka bir varlığın eşi veya dengi diye adlandırır.","gloss":"benzerlik ve denklik","neighbor_only":"Komşu dal, benzetme ve eşitleme işlemlerini de kapsayan daha geniş bir ilişki alanına sahiptir.","neighbor_ref":"root_001397/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da iki şey arasındaki benzerlik veya denklik bağını ifade eder."}],"source_phrase_ar":"هذا شروى هذا أي مثله (maqayis); شرواها أي مثلها (maqayis); شروى الشيء مثله (sihah); هذا شرواه وشرية أي مثله (tahdhib)","source_summary":"Kaynaklar, dalın bir şeyin başka bir şeyle benzer veya denk oluşunu bildirdiği konusunda birleşir.","sources":["MQ","SI","TA"],"what_is_ar":"الشروى والشرية بمعنى المثل والنظير، وقولهم شرواها أي مثلها","what_is_not_ar":"البيع والشراء والنواحي والنبات"},"support_links":["sup_9816952df4200296b721"]},{"boundary":"Anlam bağımsız bir genel yön adı değildir; kanıtta verilen ad birliklerinde yan veya uç bildiren kullanımla sınırlıdır.","branch_kind":"collocation","branch_ref":"root_000792/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"bir şeyin yanları ve uçları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kanıtlanan ad birliklerinde bir şeyin yanlarını, çevresini veya uçlarını adlandırır."}}],"root_ar":"ش ر ر","root_id":"root_000792","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kanıtlanan ad birliklerinde bir nesnenin veya yerin çevresel yanlarını belirtmek için uygundur.","boundary_detail":"Anlam bağımsız bir genel yön adı değildir; kanıtta verilen ad birliklerinde yan veya uç bildiren kullanımla sınırlıdır.","branch_image_ar":"الناحية والطرف","concept_gloss":"bir şeyin yanları ve uçları","contextual_glosses":[{"applicability":"Sınırlandırılmış bir alanın çevresindeki yanların çoğul olarak anlatıldığı kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Alanla bağlı çevresel yanlar anlamını eksiksiz korur."},"facet_ids":["F001"],"text":"bölgenin çevre yanları","usage_role":"contextual"},{"applicability":"Kanıtlanan tekil nehir adı birliğinde nehrin bir yanını belirtmek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli nehre bağlı yan anlamını doğal biçimde korur."},"facet_ids":["F001"],"text":"nehrin yanı","usage_role":"contextual"}],"definition":"Belirli ad birliklerinde bir nesnenin, sınırlandırılmış bir alanın veya Fırat'ın yanını, çevresel bölümünü ya da ucunu belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kanıtlanan ad birliklerinde bir şeyin yanlarını, çevresini veya uçlarını adlandırır."}],"identity_rationale":"Kaynak ifadesi, yalnızca belirli ad birliklerinde bir şeyin, kutsal bölgenin veya büyük nehrin yanlarını ve uçlarını bildirir. Geçici çerçeve bu sınırlı kapsamı doğru verir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bir şeyin yanları ve uçları"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"büyük nehrin yanı"}],"lexicalization_note":"Dal yalnızca belirtilen ad birliklerinde sözlükselleşir; tanım buradan yalın kök için genel bir yan anlamı çıkarmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kalıba bağlı yan anlamıyla genel kenar anlamı arasındaki sınırı en iyi gösteren komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Anlamsal alan yakın olsa da odak dal kalıba bağlıdır; komşu dalın yan ve kenar anlamı daha genel bir adlandırmadır.","focus_only":"Odak anlam yalnızca kanıtlanan ad birliklerinde ortaya çıkar.","gloss":"yan ve kenar","neighbor_only":"Komşu dal, kuyu ve gök gibi farklı varlıklarda bağımsız biçimde yan ve kenar bildirebilir.","neighbor_ref":"root_000548/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da bir varlığın merkez dışındaki yan veya kenar bölümünü gösterir."}],"source_phrase_ar":"أشراء الشيء نواحيه الواحد شرى (maqayis); أشراء الحرم نواحيه الواحد شرى (sihah); أشراء الحرم نواحيه وشرى الفرات ناحيته (tahdhib)","source_summary":"Kaynaklar, çoğul kullanımın bir şeyin veya sınırlandırılmış alanın yanlarını bildirdiğini; tekil kullanımın da belirli bir büyük nehrin yanı için geçtiğini aktarır.","sources":["MQ","SI","TA"],"what_is_ar":"أشراء الشيء والحرم وشرى الفرات بمعنى النواحي والأطراف","what_is_not_ar":"البيع والمثل والنبات"},"support_links":[]},{"boundary":"Acı meyveli bitki ile çekirdekten yetişen palmiye ayrı alt kullanımlardır; yay yapımında kullanılan ağaç ve bitkili yer bu dala girmez.","branch_kind":"bare","branch_ref":"root_000792/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"acı elma bitkisi veya çekirdekten yetişen palmiye","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Acı meyveli bitkiyi ya da bu bitkinin kendisini adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı bir kullanımda çekirdekten yetişen palmiye ağacını adlandırır."}}],"root_ar":"ش ر ر","root_id":"root_000792","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın iki ayrı botanik göndermesini tek tür saymadan birlikte özetlemek gerektiğinde kullanılır.","boundary_detail":"Acı meyveli bitki ile çekirdekten yetişen palmiye ayrı alt kullanımlardır; yay yapımında kullanılan ağaç ve bitkili yer bu dala girmez.","branch_image_ar":"نبات الشَّري والشرية","concept_gloss":"acı elma bitkisi veya çekirdekten yetişen palmiye","contextual_glosses":[{"applicability":"Acı ve zehirli meyveli sürünücü bitkinin veya onun bitki örtüsünün kastedildiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İlgili bitki göndermesini açık ve doğal biçimde korur."},"facet_ids":["F001"],"text":"acı elma bitkisi","usage_role":"contextual"},{"applicability":"Tohumdan veya çekirdekten yetişmiş palmiye ağacının kastedildiği ayrı kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Palmiye türü ile yetişme biçimi koşulunu birlikte korur."},"facet_ids":["F002"],"text":"çekirdekten yetişen palmiye","usage_role":"contextual"}],"definition":"Bir kullanım acı meyveli bitkiyi veya onun bitki örtüsünü, ayrı bir kullanım ise çekirdekten yetişen palmiye ağacını adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Acı meyveli bitkiyi ya da bu bitkinin kendisini adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Ayrı bir kullanımda çekirdekten yetişen palmiye ağacını adlandırır."}],"identity_rationale":"Kaynak ifadesi aynı dal altında iki ayrı bitkisel göndermeyi bir araya getirir: acı meyveli bir bitki veya onun bitkisi ile çekirdekten yetişen bir palmiye. Dal kullanılabilir, ancak bu iki gönderme tek bir bitki türü gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"acı elma bitkisi veya bu bitkinin topluluğu"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"çekirdekten yetişen palmiye ağacı"}],"lexicalization_note":"Dal yalın bitki adlarını kapsar; iki ayrı bitkisel gönderme tanım ve yüzey karşılıklarında açıkça ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnız palmiye alt kullanımının sınırını açıklayan komşu yayımlandı, diğer bitki adayları yalnız aynı botanik alanını paylaşır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal yetişme kaynağını, komşu dal ise ağacın küçüklüğünü öne çıkarır; bu nedenle olağan ikame mümkün değildir.","focus_only":"Odak dalın palmiye kullanımı ağacın çekirdekten yetişmesi koşulunu taşır ve ayrıca başka bir bitki adını da içerir.","gloss":"genç palmiye","neighbor_only":"Komşu dal küçük palmiye ağaçlarını yaş veya boy bakımından adlandırır.","neighbor_ref":"root_000832/B006","relation_type":"near_neighbor","shared_zone":"Her iki dalın bir bölümü genç veya yeni yetişen palmiye ağaçlarıyla ilgilidir."}],"source_phrase_ar":"الشَّرى يقال إنه الحنظل (maqayis); الشرية النخلة التي تنبت من النواة (maqayis); الشري بالتسكين الحنظل (sihah); الشرى أيضا شجر الحنظل (sihah); الحنظل هو الشري واحدته شرية (tahdhib)","source_summary":"Toplu kaynak kanıtı, acı meyveli bitkiyi bildiren ana botanik kullanımın yanında çekirdekten yetişen palmiye için ayrı bir kullanımı da içerir.","sources":["MQ","SI","TA"],"what_is_ar":"الشَّري بمعنى الحنظل أو شجره، والشرية النخلة التي تنبت من النواة","what_is_not_ar":"الشِّريان شجر القسي والمواضع والغياض"},"support_links":[]},{"boundary":"Dal bir bitki türünü değil, çalılık ve aslanlarla nitelenen yeri ya da yolu; buna bağlı olarak oranın aslanlarını bildirir.","branch_kind":"mixed_non_bare","branch_ref":"root_000792/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"çalılık ve aslanlarıyla tanınan yer","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çalılığı yoğun ve aslanları çok olan bir yer veya yolu adlandırır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu yere bağlı bir ad birliğinde oranın aslanlarını belirtir."}}],"root_ar":"ش ر ر","root_id":"root_000792","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yer veya yolun yoğun bitki örtüsü ve aslan varlığıyla birlikte nitelendiği ana kullanıma uygundur.","boundary_detail":"Dal bir bitki türünü değil, çalılık ve aslanlarla nitelenen yeri ya da yolu; buna bağlı olarak oranın aslanlarını bildirir.","branch_image_ar":"الموضع ذو الغياض والأسد","concept_gloss":"çalılık ve aslanlarıyla tanınan yer","contextual_glosses":[{"applicability":"Yalnızca kanıtlanan aslanlı ad birliğinde, söz konusu yere bağlı aslanlar kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aslanları belirli çalılık yere bağlayan ilişkiyi korur."},"facet_ids":["F002"],"text":"o çalılık bölgenin aslanları","usage_role":"contextual"}],"definition":"Yoğun çalılıkları, korulukları ve aslanlarıyla tanınan bir yer ya da yolu belirtir; buna bağlı bir söyleyişte o yerin aslanları anılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çalılığı yoğun ve aslanları çok olan bir yer veya yolu adlandırır."},{"facet_id":"F002","role":"associated_use","statement":"Bu yere bağlı bir ad birliğinde oranın aslanlarını belirtir."}],"identity_rationale":"Kaynak ifadesi, yoğun çalılıkları ve aslanlarıyla tanınan bir yer veya yol anlamını açıkça destekler. Topluluk için kullanılan aslanlı söyleyiş de bu yer anlamına bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"çalılığı ve aslanı bol yer veya yol"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"çalılık bölgenin aslanları"}],"lexicalization_note":"Yalın yer adı ile bu yere bağlı aslanlı ad birliği ayrılır; ad birliğinin anlamı yalın biçimin bütün kapsamına yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yer ile sık bitki örtüsü arasındaki en yararlı sınırı veren komşu seçildi, öteki adaylar yalnız barınak veya özel bitki türü düzeyinde kaldı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dalın çekirdeği çalılık ve aslanlarla nitelenen yerdir; komşu dalın çekirdeği ise sık ağaç topluluğunun kendisidir.","focus_only":"Odak dal, yoğun bitki örtüsüne ek olarak belirli bir yer veya yol ve oradaki aslanları içerir.","gloss":"sık ağaçlık","neighbor_only":"Komşu dal, birbirine girmiş ağaç topluluğunu doğrudan bitki örtüsü olarak adlandırır.","neighbor_ref":"root_000072/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da sık ve birbirine yakın bitkilerin oluşturduğu koruluk alanını çağrıştırır."}],"source_phrase_ar":"الشرى موضع كثير الدغل والأسد (maqayis); الشرى طريق في سلمى كثير الأسد (sihah); ما هم إلا أسود الشرى (tahdhib); شرى مأسدة بعينها وبه غياض وآجام (tahdhib)","source_summary":"Kaynak kanıtı, yoğun çalılık ve koruluklar barındıran, aslanlarıyla tanınan bir yer veya yol tasvirini; ayrıca bu yerin aslanlarına yapılan bağlı göndermeyi birleştirir.","sources":["MQ","SI","TA"],"what_is_ar":"الشرى والشرى في المواضع الكثيرة الدغل أو الأسد، وما قيل فيه من مأسدة وغياض وآجام","what_is_not_ar":"الحنظل والشِّريان والنواحي"},"support_links":[]},{"boundary":"Yaylık ağaç ile beden damarları ayrı alt kullanımlardır; acı meyveli bitki ve çalılık yer anlamları bu dala girmez.","branch_kind":"bare","branch_ref":"root_000792/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"yaylık ağaç veya atardamar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yay yapmaya elverişli ağacı veya bu ağacın odununu adlandırır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsan bedenindeki atan veya ince damarları adlandırır."}}],"root_ar":"ش ر ر","root_id":"root_000792","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ağaç ve anatomi göndermelerini birbirine karıştırmadan dalın bütününü kısa biçimde özetlemek için uygundur.","boundary_detail":"Yaylık ağaç ile beden damarları ayrı alt kullanımlardır; acı meyveli bitki ve çalılık yer anlamları bu dala girmez.","branch_image_ar":"الشِّريان عود القسي والعروق","concept_gloss":"yaylık ağaç veya atardamar","contextual_glosses":[{"applicability":"Ağaç türünün veya odunun yay yapımındaki kullanımının kastedildiği botanik ve zanaat bağlamlarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ağaç ile yay yapımı arasındaki amaç ilişkisini korur."},"facet_ids":["F001"],"text":"yay yapımında kullanılan ağaç","usage_role":"contextual"},{"applicability":"İnsan bedenindeki atan ya da ince damarların çoğul olarak kastedildiği anatomi bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Beden içindeki damarları ve verilen iki niteliği korur."},"facet_ids":["F002"],"text":"atan veya ince damarlar","usage_role":"contextual"}],"definition":"Bir kullanım yay yapımında kullanılan bir ağaç veya odunu, ayrı bir kullanım ise insan bedenindeki atan ya da ince damarları adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yay yapmaya elverişli ağacı veya bu ağacın odununu adlandırır."},{"facet_id":"F002","role":"extension","statement":"İnsan bedenindeki atan veya ince damarları adlandırır."}],"identity_rationale":"Kaynak ifadesi aynı söz biçimi çevresinde yay yapımında kullanılan bir ağacı ve insan bedenindeki atan ya da ince damarları birlikte verir. Bunlar tek bir nesne gibi tanımlanmamalı, iki ayrı gönderme olarak korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yay yapımında kullanılan ağaç veya odun"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"atan veya ince beden damarları"}],"lexicalization_note":"Dal yalın biçimleri kapsar, ancak ağaç ve anatomi göndermeleri tanımda birbirinden açıkça ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yaylık ağaç çekirdeğini doğrudan paylaşan komşu yayımlandı, damar ve odun adayları yalnız alan benzerliği taşıdı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Botanik gönderme örtüşse de odak dalın anatomi kullanımı komşuda yoktur; komşu dal ise yetişme yeri ve ok yapımı ayrıntılarını ekler.","focus_only":"Odak dal ayrıca beden damarlarını adlandıran ayrı bir anatomi kullanımına sahiptir.","gloss":"yay ve ok yapılan ağaç","neighbor_only":"Komşu dal ağacı, dağ yamacındaki yetişme yeri ve ok yapımında kullanımıyla daha geniş biçimde niteler.","neighbor_ref":"root_001469/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da yay yapımında kullanılan bir ağaç veya odun türünü belirtir."}],"source_phrase_ar":"الشريان من شجر القسى (maqayis); الشريان شجر يتخذ منه القسى (sihah); الشريان واحد الشرايين وهي العروق النابضة (sihah); الشريان من الشجر الذي يتخذ منه القسي (tahdhib); الشريانات عروق رقاق في جسد الإنسان (tahdhib)","source_summary":"Toplu kaynak kanıtı, yay yapımında kullanılan ağaç veya odun anlamıyla insan bedenindeki atan ya da ince damar anlamını ayrı göndermeler olarak aktarır.","sources":["MQ","SI","TA"],"what_is_ar":"الشِّريان شجر يتخذ منه القسي، والشرايين عروق في جسد الإنسان","what_is_not_ar":"الشَّري الحنظل والشرى الموضع"},"support_links":[]},{"boundary":"Dal yalnız şimşekle kurulan kullanımlardaki yayılma ve yinelenen parlama olayını kapsar; genel ışıldama anlamına genişletilmez.","branch_kind":"collocation","branch_ref":"root_000792/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"şimşeğin yayılıp art arda parlaması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Şimşeğin bulut içinde veya bulut yüzünde dağılıp yayılmasını bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Şimşeğin sık ve art arda parlamasını bildirir."}}],"root_ar":"ش ر ر","root_id":"root_000792","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Şimşeğin bulut içinde dağıldığı ve parlamalarının sıkça birbirini izlediği hava olayları için uygundur.","boundary_detail":"Dal yalnız şimşekle kurulan kullanımlardaki yayılma ve yinelenen parlama olayını kapsar; genel ışıldama anlamına genişletilmez.","branch_image_ar":"انتشار البرق ولمعانه","concept_gloss":"şimşeğin yayılıp art arda parlaması","contextual_glosses":[{"applicability":"Şimşeğin bulut yüzünde farklı yönlere dağılarak görünmesi öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Şimşeğin bulut içindeki dağılıp yayılma yönünü korur."},"facet_ids":["F001"],"text":"şimşek buluta yayıldı","usage_role":"contextual"},{"applicability":"Parlamaların sıklaşıp birbirini izlemesi öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sık ve ardışık parlama olayını doğal biçimde korur."},"facet_ids":["F002"],"text":"şimşek art arda çaktı","usage_role":"contextual"}],"definition":"Şimşeğin bulutun yüzüne dağılarak yayılması, sık parlaması veya parlamalarının art arda sürmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Şimşeğin bulut içinde veya bulut yüzünde dağılıp yayılmasını bildirir."},{"facet_id":"F002","role":"specialization","statement":"Şimşeğin sık ve art arda parlamasını bildirir."}],"identity_rationale":"Kaynak ifadesi şimşeğin bulut içinde yayılması, sık parlaması ve parlamalarının art arda gelmesi özelliklerini birlikte destekler. Geçici çerçeve bu olay örgüsünü doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"şimşek buluta yayıldı veya art arda parladı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"şimşek art arda parladı"}],"lexicalization_note":"Dal şimşekle kurulan ad birliklerine bağlıdır; buradan yalın biçim için genel parlama veya yayılma anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ardışık parlama koşulunu en keskin biçimde karşılaştıran komşu yayımlandı, diğerleri genel ışık veya zayıf parlama alanında kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda yayılma veya sık parlama yeterli olabilir; komşu dal ise parlamalar arasında ara kalmamasını zorunlu kılar.","focus_only":"Odak dal, ardışıklığın yanında şimşeğin bulut yüzüne dağılıp yayılmasını ve parlamanın sıklaşmasını da kapsar.","gloss":"kesintisiz şimşek çakması","neighbor_only":"Komşu dal, iki parlama arasında boşluk kalmayacak ölçüde kesintisiz ardışıklık koşulu taşır.","neighbor_ref":"root_001379/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da şimşek parlamalarının sıklaşarak birbirini izlemesini anlatır."}],"source_phrase_ar":"شرى البرق إذا استطار (maqayis); شري البرق في السحاب يشرى شرى إذا تفرق فيه (ayn); شرى البرق إذا كثر لمعانه (sihah); شري البرق إذا تفرق في وجه الغيم (tahdhib); شري البرق إذا تتابع لمعانه واستشرى مثله (tahdhib)","source_summary":"Kaynakların birleşik anlatımı, şimşeğin bulut içinde yayılması ile parlamalarının çoğalıp birbirini izlemesini aynı olay alanının bağlı yönleri olarak verir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"شري البرق إذا تفرق في السحاب أو كثر لمعانه وتتابع","what_is_not_ar":"البيع والنبات وداء الجلد"},"support_links":[]},{"boundary":"Dal, her bağlamda aynı hareketi değil; öfke, ısrar, hız, yinelenme ve büyüme biçimindeki bağlantılı fakat ayrı gerçekleşmeleri kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000792/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"taşkın biçimde sürme, yinelenme veya büyüme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin öfkesinin taşkın biçimde yükselmesini bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir işte, yolda veya yanlış davranışta inatla sürmeyi ve geri durmamayı bildirir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hızlı ilerlemeyi veya dizgin gibi bir nesnenin sık ve ardışık hareketini bildirir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Gözyaşının durmadan akması ya da insanlar arasındaki işlerin büyüyüp ağırlaşması gibi süreklilik ve artış durumlarını bildirir."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Birini bir kimseye veya şeye karşı kışkırtmayı bildirir."}}],"root_ar":"ش ر ر","root_id":"root_000792","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın öfke, ısrar, hareket, akış ve durum artışı kullanımlarındaki ortak dinamik yapıyı özetlemek için uygundur.","boundary_detail":"Dal, her bağlamda aynı hareketi değil; öfke, ısrar, hız, yinelenme ve büyüme biçimindeki bağlantılı fakat ayrı gerçekleşmeleri kapsar.","branch_image_ar":"الهيجان واللجاج والاندفاع","concept_gloss":"taşkın biçimde sürme, yinelenme veya büyüme","contextual_glosses":[{"applicability":"Kişinin öfkesinin birden yükselip taşkın hale gelmesini anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öfkenin taşkın ve denetimsiz biçimde yükselmesini korur."},"facet_ids":["F001"],"text":"öfkesinden çılgına dönmek","usage_role":"contextual"},{"applicability":"Bir işte, yolda veya yanlış davranışta vazgeçmeden ilerleme bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geri durmadan ısrarla devam etme anlamını korur."},"facet_ids":["F002"],"text":"inatla sürdürmek","usage_role":"contextual"},{"applicability":"İnsanlar arasındaki sorun veya işlerin ağırlaşıp büyümesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Durumların zaman içinde büyüyüp ağırlaşmasını korur."},"facet_ids":["F004"],"text":"gittikçe büyümek","usage_role":"contextual"}],"definition":"Bir duygu, davranış, hareket veya durumun taşkın biçimde hızlanması, inatla sürmesi, yinelenmesi ya da büyümesidir. Ayrı bir kullanım, birini bir şeye karşı kışkırtmayı bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin öfkesinin taşkın biçimde yükselmesini bildirir."},{"facet_id":"F002","role":"extension","statement":"Bir işte, yolda veya yanlış davranışta inatla sürmeyi ve geri durmamayı bildirir."},{"facet_id":"F003","role":"extension","statement":"Hızlı ilerlemeyi veya dizgin gibi bir nesnenin sık ve ardışık hareketini bildirir."},{"facet_id":"F004","role":"extension","statement":"Gözyaşının durmadan akması ya da insanlar arasındaki işlerin büyüyüp ağırlaşması gibi süreklilik ve artış durumlarını bildirir."},{"facet_id":"F005","role":"associated_use","statement":"Birini bir kimseye veya şeye karşı kışkırtmayı bildirir."}],"identity_rationale":"Kaynak ifadesi öfke, inatla sürdürme, hızlı ilerleme, dizginin çırpınması, gözyaşının yinelenmesi, işlerin büyümesi ve birini kışkırtma gibi ayrı kurulumları verir. Bunları tek bir eylem gibi birleştirmek yerine taşkınlık, süreklilik veya artış ortaklığı altında ayrı tutmak gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"öfkesinden çılgına döndü"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bir işte inatla diretti ve ileri gitti"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"karşılıklı inatlaşma ve çekişme"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"yolunda hızlandı veya durmadan ilerledi"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"dişi devenin dizgini durmadan çırpındı"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"gözyaşları durmadan aktı"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"aralarındaki işler büyüyüp ağırlaştı"}],"lexicalization_note":"Yalın karşılıklı inatlaşma adı ile kişi, yolculuk, dizgin, gözyaşı ve işler üzerinden kurulan kullanımlar ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; öfke ve taşkın yükseliş çekirdeğini en çok paylaşan komşu yayımlandı, diğerleri yalnız hareket, kışkırtma veya huzursuzluk alanında kesişti.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Öfke alanında yakınlaşırlar; odak dalın ayırıcı yönü inatçı süreklilik ve yinelenmedir, komşu dalınki ise sıçrayış ve şiddet artışıdır.","focus_only":"Odak dal öfkenin yanı sıra ısrar, hız, yinelenen hareket, sürekli akış ve işlerin büyümesini de kapsar.","gloss":"şiddetle kabarma","neighbor_only":"Komşu dal, savaşın şiddeti, içkinin keskinliği ve sıçrayarak saldırma gibi yükselme görüntülerini de içerir.","neighbor_ref":"root_000758/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da öfkenin veya bir durumun taşkın biçimde yükselmesini anlatır."}],"source_phrase_ar":"شرى الرجل إذا استطير غضبا (maqayis); شرى البعير في سيره إذا أسرع (maqayis); استشرى الرجل إذا لج في الأمر (maqayis); شرى زمام الناقة إذا كثر اضطرابه (maqayis); شري فلان غضبا إذا استطار غضبا (sihah); استشرى أي لج في سننه (sihah); استشرى فلان في الغي إذا لج فيه (tahdhib); المشاراة الملاجة (tahdhib); شريت عينه بالدمع أي لجت وتابعت الهملان (tahdhib); استشرت أمور بينهم تفاقمت وعظمت (tahdhib); أشريته به فشري مثل أغريته به فغري (tahdhib)","source_summary":"Toplu kaynak kanıtı, öfkenin taşması, bir işte direnerek sürme, hızlanma, hareket veya akışın yinelenmesi, durumların büyümesi ve birinin kışkırtılması gibi ayrı gerçekleşmeleri aynı dalda toplar.","sources":["MQ","SI","TA"],"what_is_ar":"شدة الغضب، واللجاج في الأمر أو الغي، والمضي في السير بلا فتور، واضطراب الزمام، وتتابع الدمع أو الحركات، وتفاقم الأمور","what_is_not_ar":"البرق إذا جعل فرعا مستقلا وداء الجلد والبيع"},"support_links":[]},{"boundary":"Dal genel ağrı veya her tür deri çıkıntısı değildir; küçük, kızarık ve yakıcı deri kabarcıklarıyla belirlenen rahatsızlıktır.","branch_kind":"mixed_non_bare","branch_ref":"root_000792/B009","candidate_links":[{"candidate_id":"cand_7983e493711ca3a93025","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"yakıcı küçük kırmızı deri kabarcıkları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Deride küçük, kızarık ve şiddetli yakıcılığı olan kabarcıklarla görülen rahatsızlığı adlandırır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Derinin bu kabarcıklı ve yakıcı rahatsızlığa tutulmasını bildirir."}}],"root_ar":"ش ر ر","root_id":"root_000792","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Rahatsızlığın ayırt edici deri görünümünü ve yakıcılığını birlikte belirtmek için uygundur.","boundary_detail":"Dal genel ağrı veya her tür deri çıkıntısı değildir; küçük, kızarık ve yakıcı deri kabarcıklarıyla belirlenen rahatsızlıktır.","branch_image_ar":"داء الشَّرى في الجلد","concept_gloss":"yakıcı küçük kırmızı deri kabarcıkları","contextual_glosses":[{"applicability":"Derinin bu rahatsızlığa tutulmasını olay olarak anlatan cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Deride kabarcık oluşması ile yakıcılık özelliğini birlikte korur."},"facet_ids":["F002"],"text":"derisinde yakıcı kabarcıklar çıktı","usage_role":"contextual"}],"definition":"Deride küçük, kızarık, belirgin biçimli ve şiddetli yakıcılık veren kabarcıkların ortaya çıktığı bir rahatsızlıktır; bağlı kullanım derinin buna tutulmasını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Deride küçük, kızarık ve şiddetli yakıcılığı olan kabarcıklarla görülen rahatsızlığı adlandırır."},{"facet_id":"F002","role":"associated_use","statement":"Derinin bu kabarcıklı ve yakıcı rahatsızlığa tutulmasını bildirir."}],"identity_rationale":"Kaynak ifadesi deride küçük, kırmızı, para biçimli ve şiddetli yakıcılığı olan kabarcıklar veya bir deri hastalığı anlamını destekler. Derinin bu hastalığa tutulmasını bildiren kullanım da aynı çekirdeğe bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"yakıcı küçük kırmızı deri kabarcıklarıyla görülen hastalık"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"derisinde yakıcı küçük kabarcıklar çıktı"}],"lexicalization_note":"Hastalık adı ile derinin bu hastalığa tutulmasını bildiren ad birliği ayrılır; ikisi aynı deri rahatsızlığına bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel deri çıkıntısı alanıyla özel yakıcı kabarcık sınırını en iyi gösteren komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal belirli görünüm ve yakıcılıkla sınırlıdır; komşu dal farklı neden ve türlerdeki deri çıkıntılarını genel olarak toplar.","focus_only":"Odak dal küçük, kırmızı ve şiddetli yakıcılığı olan belirli deri kabarcıklarını gerektirir.","gloss":"deri kabartısı","neighbor_only":"Komşu dal irinli şişlik, çiçek hastalığı, yara ve darbe izi gibi çok çeşitli deri çıkıntılarını kapsar.","neighbor_ref":"root_000228/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da deride belirginleşen kabarıklık veya çıkıntıları içeren rahatsızlıklarla ilgilidir."}],"source_phrase_ar":"شري جلده من الشرى وهي خراج صغار لها لذع شديد (sihah); الشري داء يأخذ في الرجل أحمر كهيئة الدراهم (tahdhib); شرى جلده شرى وهو شر (tahdhib)","source_summary":"Kaynaklar, küçük ve yakıcı deri kabarcıklarıyla tanımlanan kırmızı bir rahatsızlığı ve derinin bu rahatsızlığa tutulmasını birlikte aktarır; kaynaklardan biri bu rahatsızlığı para biçimli görünümüyle ayrıca ayırır.","sources":["SI","TA"],"what_is_ar":"الشَّرى داء أو خراج صغار في الجلد لها لذع، ويقال شرى جلده أو شرى الرجل","what_is_not_ar":"الحنظل والبرق واللجاج"},"support_links":["sup_86b6ecca7eb8170531c4"]},{"boundary":"Dal kabın dolu sonucu veya içindekini sunma eylemi değil, havuz ya da yemek kabını doldurma işlemidir.","branch_kind":"collocation","branch_ref":"root_000792/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"havuzu veya yemek kabını doldurmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Havuzu veya büyük yemek kabını içeriğiyle doldurmayı bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Misafirler için yemek kaplarını doldurmayı özel bir gerçekleşme olarak bildirir."}}],"root_ar":"ش ر ر","root_id":"root_000792","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kanıtlanan havuz ve büyük yemek kabı nesneleriyle kurulan doldurma eylemi için uygundur.","boundary_detail":"Dal kabın dolu sonucu veya içindekini sunma eylemi değil, havuz ya da yemek kabını doldurma işlemidir.","branch_image_ar":"إملاء الحوض والجفنة","concept_gloss":"havuzu veya yemek kabını doldurmak","contextual_glosses":[{"applicability":"Yemek kaplarının konuklara sunulmak üzere doldurulduğu ağırlama bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doldurma eylemini, kap türünü ve misafir amacını korur."},"facet_ids":["F002"],"text":"misafirler için yemek kaplarını doldurmak","usage_role":"contextual"}],"definition":"Bir havuzu veya büyük yemek kabını doldurmak, özellikle misafirlere sunulacak yemek kaplarını dolu hale getirmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Havuzu veya büyük yemek kabını içeriğiyle doldurmayı bildirir."},{"facet_id":"F002","role":"specialization","statement":"Misafirler için yemek kaplarını doldurmayı özel bir gerçekleşme olarak bildirir."}],"identity_rationale":"Kaynak ifadesi bir havuzu ya da büyük yemek kabını doldurma eylemini açıkça bildirir ve misafirler için yemek kaplarını doldurmayı özel bir durum olarak ekler. Geçici çerçeve kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"havuzu veya büyük yemek kabını doldurmak"}],"lexicalization_note":"Dal havuz ve yemek kabıyla kurulan kullanıma bağlıdır; buradan yalın biçim için genel doldurma anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı doldurma eylemini paylaşan komşu seçildi, diğerleri kap adı, doluluk sonucu veya taşma gibi farklı çekirdeklere sahipti.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Havuz bağlamında yakın anlamlıdırlar; odak dal kap türünü genişletirken komşu dal suyla yoğun doldurma koşulunu öne çıkarır.","focus_only":"Odak dal havuzun yanında büyük yemek kaplarını ve bunların misafir için doldurulmasını da kapsar.","gloss":"havuzu iyice suyla doldurmak","neighbor_only":"Komşu dal yalnız havuzun suyla iyice ve sıkıca doldurulmasını bildirir.","neighbor_ref":"root_000444/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da bir havuzu suyla dolu hale getirme eylemini kapsar."}],"source_phrase_ar":"أشريت الحوض وأشريت الجفنة إذا ملأتهما (sihah); أشرى حوضه ملأه وأشرى جفانه إذا ملأها للضيفان (tahdhib)","source_summary":"Kaynaklar havuz ile büyük yemek kabını doldurma çekirdeğinde birleşir; misafirler için yemek kaplarını doldurma bunun özel bağlamıdır.","sources":["SI","TA"],"what_is_ar":"أشرى الحوض والجفنة إذا ملأهما، وخاصة ملء الجفان للضيفان","what_is_not_ar":"البيع والهيجان والسقي نفسه"},"support_links":[]},{"boundary":"Dal genel satış değildir; kendini Tanrı uğruna sattığını ileri süren belirli topluluğun adı, üyesi ve o topluluğa katılma kullanımıdır.","branch_kind":"bare","branch_ref":"root_000792/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"kendini Tanrı uğruna sattığını söyleyen topluluk","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kendilerini Tanrı uğruna sattıkları yorumunu benimseyen belirli ayrılıkçı topluluğu adlandırır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tekil kullanım topluluğun bir üyesini, eylem kullanımı ise bu topluluğa katılmayı bildirir."}}],"root_ar":"ش ر ر","root_id":"root_000792","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli ayrılıkçı topluluğun kendi adlandırma gerekçesiyle birlikte açıklanması gereken kullanımlara uygundur.","boundary_detail":"Dal genel satış değildir; kendini Tanrı uğruna sattığını ileri süren belirli topluluğun adı, üyesi ve o topluluğa katılma kullanımıdır.","branch_image_ar":"الشُّراة وبيع النفس","concept_gloss":"kendini Tanrı uğruna sattığını söyleyen topluluk","contextual_glosses":[{"applicability":"Topluluk adının tekil biçimiyle o topluluğa bağlı bir kişinin kastedildiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tek bir kişi ile tanımlı topluluk arasındaki üyelik bağını korur."},"facet_ids":["F002"],"text":"bu topluluğun bir üyesi","usage_role":"contextual"},{"applicability":"Bir kişinin söz konusu topluluğa bağlanmasını bildiren eylem kullanımında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin belirli topluluğa katılma yönelimini korur."},"facet_ids":["F002"],"text":"bu topluluğa katılmak","usage_role":"contextual"}],"definition":"Kendilerini Tanrı uğruna sattıklarını söyleyen belirli bir ayrılıkçı topluluğa verilen addır; tekil biçim bir üyeyi, ilgili eylem de bu topluluğa katılmayı bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kendilerini Tanrı uğruna sattıkları yorumunu benimseyen belirli ayrılıkçı topluluğu adlandırır."},{"facet_id":"F002","role":"extension","statement":"Tekil kullanım topluluğun bir üyesini, eylem kullanımı ise bu topluluğa katılmayı bildirir."}],"identity_rationale":"Kaynak ifadesi, belirli bir ayrılıkçı topluluğun kendisini Tanrı uğruna sattığı yorumundan doğan topluluk adını destekler. Geçici çerçevedeki cennet seçeneği doğrudan kaynak ifadesinde yer almadığından tanım yalnız Tanrı uğruna kendini satma yorumuna bağlanmıştır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"kendilerini Tanrı uğruna sattıklarını söyleyen ayrılıkçı topluluk"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bu topluluğun bir üyesi"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"bu topluluğa katılmak"}],"lexicalization_note":"Dal yalın topluluk ve üye adlarını kapsar; genel bedelli satış anlamından türemiş özel bir topluluk adlandırması olarak sınırlandırılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kendini bedel sayma düşüncesini en açık paylaşan komşu yayımlandı, diğer adaylar ibadet, işaret veya kişi adı alanında daha uzaktı.","neighbor_distinctions":[{"boundary_match":"thematic_only","distinction":"Odak dal mecazi bir öz adlandırma ve topluluk kimliğidir; komşu dal ise başka birini kurtarmaya yönelik gerçek bir yerine koyma işlemidir.","focus_only":"Odak dal, kendini Tanrı uğruna satma yorumundan doğan belirli bir topluluk ve üye adıdır.","gloss":"birini kurtarmak için bedel vermek","neighbor_only":"Komşu dal, bir kişiyi kurtarmak veya korumak için mal, can ya da kurbanı onun yerine verme işlemidir.","neighbor_ref":"root_001136/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir canın daha yüksek bir amaç uğruna verilmesi veya bedel sayılması düşüncesi bulunur."}],"source_phrase_ar":"الشراة الخوارج الواحد شار سموا بذلك لقولهم إنا شرينا أنفسنا في طاعة الله (sihah); الشراة الخوارج سموا أنفسهم شراة لأنهم أرادوا أنهم باعوا أنفسهم لله (tahdhib); يسمى الخوارج بالشراة متأولين فيه ومن الناس من يشري نفسه (mufradat)","source_summary":"Kaynaklar, topluluk adını üyelerin kendilerini Tanrı uğruna sattıkları yorumuyla açıklar; tekil üye adı ile topluluğa katılma eylemi aynı adlandırmaya bağlıdır.","sources":["SI","TA","MU"],"what_is_ar":"الشراة اسم لمن قيل إنهم باعوا أنفسهم لله أو للجنة، والواحد شار، وتشرى الرجل في هذا المعنى","what_is_not_ar":"مجرد البيع العام بغير تسمية الجماعة"},"support_links":[]},{"boundary":"Dal yalnız kanıtlanan beddua kalıbıdır; satış, deri hastalığı veya genel olarak her tür dua anlamına genişletilmez.","branch_kind":"collocation","branch_ref":"root_000792/B012","candidate_links":[{"candidate_id":"cand_8e8ade73f0f9958d523c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","surface_ar":"شَرِّ"}],"gloss":"Tanrı seni sıkıntıya ve aşağılanmaya uğratsın","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi için Tanrı'dan sıkıntı, zarar veya aşağılanma dileyen kalıplaşmış sözü bildirir."}}],"root_ar":"ش ر ر","root_id":"root_000792","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kanıtlanan kalıplaşmış sözün bir kişiye yönelik beddua işlevini açıklamak için uygundur.","boundary_detail":"Dal yalnız kanıtlanan beddua kalıbıdır; satış, deri hastalığı veya genel olarak her tür dua anlamına genişletilmez.","branch_image_ar":"الدعاء بالمساءة","concept_gloss":"Tanrı seni sıkıntıya ve aşağılanmaya uğratsın","contextual_glosses":[{"applicability":"Kalıplaşmış sözün genel bir kötü sonuç dileği olarak çevrildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kaynak açıklamasındaki şişme ve aşağılanma çağrışımlarını ayrı ayrı göstermez.","preserves":"Tanrı'ya yöneltilen zarar dileğini açık biçimde korur."},"facet_ids":["F001"],"text":"Tanrı seni zarara uğratsın","usage_role":"contextual"}],"definition":"Bir kişinin sıkıntıya, bedensel zarara veya aşağılanmaya uğramasını Tanrı'dan dileyen kalıplaşmış bir bedduadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi için Tanrı'dan sıkıntı, zarar veya aşağılanma dileyen kalıplaşmış sözü bildirir."}],"identity_rationale":"Kaynak ifadesi, bir kişi için şişme, sıkıntı ve aşağılanma gibi kötü sonuçlar dileyen kalıplaşmış bir bedduayı verir. Geçici çerçeve bunu genel olarak doğru biçimde kötü dilek olarak sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"Tanrı seni sıkıntıya ve aşağılanmaya uğratsın"}],"lexicalization_note":"Dal yalnız Tanrı adıyla kurulan kanıtlanmış beddua kalıbında geçerlidir; yalın biçime genel kötü dilek anlamı yüklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel kötü sonuç dileğiyle en yakın sınırı kuran komşu yayımlandı, öteki adaylar özel hastalık, nazar veya farklı beddua kalıplarıydı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kalıplaşmış ve anlam ayrıntıları belirli bir bedduadır; komşu dal kötü sonuç dilemenin daha genel anlatımıdır.","focus_only":"Odak dal belirli bir söz kalıbına ve sıkıntı, bedensel zarar ya da aşağılama çağrışımlarına bağlıdır.","gloss":"birine kötülük gelmesini dilemek","neighbor_only":"Komşu dal, bir kişi için herhangi bir istenmeyen sonucun Tanrı'dan dilenmesini genel olarak kapsar.","neighbor_ref":"root_000478/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da Tanrı'dan bir kişiye istenmeyen bir sonuç gelmesini dileme eylemidir."}],"source_phrase_ar":"لحاه الله وشراه (tahdhib); شراه الله وعظاه وأورمه وأرغمه (tahdhib)","source_summary":"Tek kaynaklı kanıt, sözün bir kişiye yöneltilen beddua olduğunu ve sıkıntı, şişme ya da aşağılanma çağrışımlarıyla açıklandığını gösterir.","sources":["TA"],"what_is_ar":"شراه الله في الدعاء بالمساءة، مع لحاه الله وشراه، وفسره المصدر بعظاه وأورمه وأرغمه","what_is_not_ar":"البيع والشراء والداء"},"support_links":["sup_1f51e32cf1b79883ebaa"]}],"candidate_inventory":[{"anchor_refs":["113:5:1"],"branch_refs":[],"candidate_id":"cand_dd8b948587912e6ffcd4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"113:5:1:accumulative-wa-min-refrain","source_type":"word_analysis","support_ids":["sup_580baa7f9eab91793428","sup_6684ca1c3723086a6281"],"title":"the wa-min opening audibly repeats the refuge refrain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:1","qac_refs":["113:5:1:1"],"status":"accepted"}},{"anchor_refs":["113:5:1"],"branch_refs":[],"candidate_id":"cand_94ce4c6d47ad612a80b4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"113:5:1:coordinated-final-refuge-clause","source_type":"word_analysis","support_ids":["sup_0a73e43b8ab2c603a3a9","sup_580baa7f9eab91793428"],"title":"the final threat remains inside the coordinated refuge list","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:1","qac_refs":["113:5:1:1"],"status":"accepted"}},{"anchor_refs":["113:5:1"],"branch_refs":[],"candidate_id":"cand_0a405dd98298a9294093","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"113:5:1:coordination-plus-resumption","source_type":"word_analysis","support_ids":["sup_580baa7f9eab91793428","sup_99896141d1f5d5336f9f"],"title":"the boundary both joins and restarts attention","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:1","qac_refs":["113:5:1:1"],"status":"accepted"}},{"anchor_refs":["113:5:2"],"branch_refs":[],"candidate_id":"cand_8fedaa0d15fb6e489a3c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"113:5:2:min-source-governance","source_type":"word_analysis","support_ids":["sup_7724a90715e8ddebe807","sup_eee656a043c6cdfbe331"],"title":"the preposition governs the source of harm","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:2","qac_refs":["113:5:1:2"],"status":"accepted"}},{"anchor_refs":["113:5:2"],"branch_refs":[],"candidate_id":"cand_4d901d2c4e7387d70b8a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"113:5:2:partitive-harm-dimension","source_type":"word_analysis","support_ids":["sup_6bc2b901d011a45840d2","sup_7724a90715e8ddebe807"],"title":"partitive pressure focuses the evil-dimension","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:2","qac_refs":["113:5:1:2"],"status":"accepted"}},{"anchor_refs":["113:5:2"],"branch_refs":[],"candidate_id":"cand_d11075d61b41f16dfee7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"113:5:2:wa-min-prepositional-refrain","source_type":"word_analysis","support_ids":["sup_70dcb8477d9adaff250b","sup_7724a90715e8ddebe807"],"title":"wa-min preserves the fourth prepositional refuge frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:2","qac_refs":["113:5:1:2"],"status":"accepted"}},{"anchor_refs":["113:5:3"],"branch_refs":[],"candidate_id":"cand_eebbef511919a883e57d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000787","root_000792"],"scope":"focus_ayah","source_local_id":"113:5:3:closing-convergence","source_type":"word_analysis","support_ids":["sup_3cef889af34ade0b96bc","sup_963da8091420588ef64a"],"title":"recurrence and image converge at the final threat","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:3","qac_refs":["113:5:2:1"],"status":"accepted"}},{"anchor_refs":["113:5:3"],"branch_refs":[],"candidate_id":"cand_a3b2477719f4eb12287f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000787","root_000792"],"scope":"focus_ayah","source_local_id":"113:5:3:compressed-sound-weight","source_type":"word_analysis","support_ids":["sup_3cef889af34ade0b96bc","sup_7e754d7bf5862065c92b"],"title":"geminated sound gives the harm noun compact weight","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:3","qac_refs":["113:5:2:1"],"status":"accepted"}},{"anchor_refs":["113:5:3"],"branch_refs":[],"candidate_id":"cand_992415cf639a7d517af5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000787","root_000792"],"scope":"focus_ayah","source_local_id":"113:5:3:governed-harm-source","source_type":"word_analysis","support_ids":["sup_3cef889af34ade0b96bc","sup_fd3ee3899cf74d9443ae"],"title":"the harm noun is governed as the refuge source","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:3","qac_refs":["113:5:2:1"],"status":"accepted"}},{"anchor_refs":["113:5:3"],"branch_refs":[],"candidate_id":"cand_5febef41f76b03572706","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000787","root_000792"],"scope":"focus_ayah","source_local_id":"113:5:3:idafa-envier-specification","source_type":"word_analysis","support_ids":["sup_3cef889af34ade0b96bc","sup_d1d46b8cd0cbb3a4d984"],"title":"construct state makes the envier specify the evil","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:3","qac_refs":["113:5:2:1"],"status":"accepted"}},{"anchor_refs":["113:5:3"],"branch_refs":[],"candidate_id":"cand_7945ca4e85e1f1062bc2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000787","root_000792"],"scope":"focus_ayah","source_local_id":"113:5:3:root-correction-evil-branch","source_type":"word_analysis","support_ids":["sup_3cef889af34ade0b96bc","sup_4988198428b4d6e12695"],"title":"the operative root is evil, not buying and selling","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:3","qac_refs":["113:5:2:1"],"status":"accepted"}},{"anchor_refs":["113:5:3"],"branch_refs":[],"candidate_id":"cand_6c76726529bbf60e6c93","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000787","root_000792"],"scope":"focus_ayah","source_local_id":"113:5:3:same-surah-sharr-thread","source_type":"word_analysis","support_ids":["sup_3cef889af34ade0b96bc","sup_adf9b7f5312382acae9d"],"title":"the repeated harm noun binds the threat list","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:3","qac_refs":["113:5:2:1"],"status":"accepted"}},{"anchor_refs":["113:5:3"],"branch_refs":[],"candidate_id":"cand_6f5cb5c70368a4666e68","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000787","root_000792"],"scope":"focus_ayah","source_local_id":"113:5:3:singular-abstract-harm-field","source_type":"word_analysis","support_ids":["sup_3cef889af34ade0b96bc","sup_8b251cfc35f7e707f29c"],"title":"the singular abstract gathers the harm field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:3","qac_refs":["113:5:2:1"],"status":"accepted"}},{"anchor_refs":["113:5:3"],"branch_refs":[],"candidate_id":"cand_dbfa5527df1b407e4000","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000787","root_000792"],"scope":"focus_ayah","source_local_id":"113:5:3:source-before-activation","source_type":"word_analysis","support_ids":["sup_3cef889af34ade0b96bc","sup_59478a55a2e713676d42"],"title":"the phrase names the source before the event","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:3","qac_refs":["113:5:2:1"],"status":"accepted"}},{"anchor_refs":["113:5:3"],"branch_refs":[],"candidate_id":"cand_75f162d20d2e7f742efe","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000787","root_000792"],"scope":"focus_ayah","source_local_id":"113:5:3:spreading-sparks-image-narrowed","source_type":"word_analysis","support_ids":["sup_3cef889af34ade0b96bc","sup_76d0db5b141437afef49"],"title":"spreading and spark images sharpen outgoing harm","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:3","qac_refs":["113:5:2:1"],"status":"accepted"}},{"anchor_refs":["113:5:4"],"branch_refs":[],"candidate_id":"cand_3bbb2a8ccd965c5202a0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:4:active-participle-disposition-before-event","source_type":"word_analysis","support_ids":["sup_3cc73bb23f06784dc7ea","sup_745cf6f831ea66e994d0"],"title":"the participle names disposition before the act","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:4","qac_refs":["113:5:3:1"],"status":"accepted"}},{"anchor_refs":["113:5:4"],"branch_refs":[],"candidate_id":"cand_ed712cc757baee50b6d1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:4:boundary-to-inward-source","source_type":"word_analysis","support_ids":["sup_745cf6f831ea66e994d0","sup_cd664dd7d1173fe30d33"],"title":"the boundary moves from ritual medium to inward disposition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:4","qac_refs":["113:5:3:1"],"status":"accepted"}},{"anchor_refs":["113:5:4"],"branch_refs":[],"candidate_id":"cand_994eb2c1976089c46c9a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:4:convergent-agent-anchor","source_type":"word_analysis","support_ids":["sup_745cf6f831ea66e994d0","sup_b7a7ed3b2b64f182759f"],"title":"rarity, range, and imāla converge on one agent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:4","qac_refs":["113:5:3:1"],"status":"accepted"}},{"anchor_refs":["113:5:4"],"branch_refs":[],"candidate_id":"cand_cfd0f6f43bb89b32812a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:4:destructive-envy-not-admiration","source_type":"word_analysis","support_ids":["sup_3be0b58156ecefb9e57f","sup_745cf6f831ea66e994d0"],"title":"the active threat is destructive envy","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:4","qac_refs":["113:5:3:1"],"status":"accepted"}},{"anchor_refs":["113:5:4"],"branch_refs":[],"candidate_id":"cand_671dea149155889d2450","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:4:envious-gaze-extension","source_type":"word_analysis","support_ids":["sup_2c21a2be40c9be6772de","sup_745cf6f831ea66e994d0"],"title":"the agent word can include the envious gaze","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:4","qac_refs":["113:5:3:1"],"status":"accepted"}},{"anchor_refs":["113:5:4"],"branch_refs":[],"candidate_id":"cand_c8c95a304118424fb68a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:4:idafa-source-possessor","source_type":"word_analysis","support_ids":["sup_745cf6f831ea66e994d0","sup_7daed34fe947e8175130"],"title":"the envier specifies whose evil is in view","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:4","qac_refs":["113:5:3:1"],"status":"accepted"}},{"anchor_refs":["113:5:4"],"branch_refs":[],"candidate_id":"cand_da12e1f606309358e147","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:4:indefinite-unbounded-envier","source_type":"word_analysis","support_ids":["sup_745cf6f831ea66e994d0","sup_c6cc52d32f68b5480319"],"title":"tanwīn leaves the envier source open-ended","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:4","qac_refs":["113:5:3:1"],"status":"accepted"}},{"anchor_refs":["113:5:4"],"branch_refs":[],"candidate_id":"cand_5183b418356e10704ce5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:4:phonetic-clipped-texture","source_type":"word_analysis","support_ids":["sup_745cf6f831ea66e994d0","sup_f138363c3b22bab37732"],"title":"the consonants give the agent noun a clipped texture","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:4","qac_refs":["113:5:3:1"],"status":"accepted"}},{"anchor_refs":["113:5:4"],"branch_refs":[],"candidate_id":"cand_24da1381e107d2743da3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:4:qiraat-imala-stable-referent","source_type":"word_analysis","support_ids":["sup_745cf6f831ea66e994d0","sup_df97fa8abd37f050da62"],"title":"imāla changes recitational color, not the agent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:4","qac_refs":["113:5:3:1"],"status":"accepted"}},{"anchor_refs":["113:5:4"],"branch_refs":[],"candidate_id":"cand_74bf44875e967614738e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:4:rare-root-agent-salience","source_type":"word_analysis","support_ids":["sup_745cf6f831ea66e994d0","sup_cbe3465a9cead061a064"],"title":"the small root field makes the envier salient","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:4","qac_refs":["113:5:3:1"],"status":"accepted"}},{"anchor_refs":["113:5:4"],"branch_refs":[],"candidate_id":"cand_ae02709ea0acb307e010","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:4:root-echo-agent-act","source_type":"word_analysis","support_ids":["sup_745cf6f831ea66e994d0","sup_bfaaa176f72f3fa03cca"],"title":"the noun and verb bind agent to act","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:4","qac_refs":["113:5:3:1"],"status":"accepted"}},{"anchor_refs":["113:5:5"],"branch_refs":[],"candidate_id":"cand_843e59726a5cd6629849","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"113:5:5:activation-scope","source_type":"word_analysis","support_ids":["sup_171ea0fe6f49dccb8fee","sup_f86eb1cd74e370ef49ef"],"title":"idhā scopes the harm to the envying moment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:5","qac_refs":["113:5:4:1"],"status":"accepted"}},{"anchor_refs":["113:5:5"],"branch_refs":[],"candidate_id":"cand_34d74be454d25292efd4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"113:5:5:echoes-113-3-trigger-frame","source_type":"word_analysis","support_ids":["sup_156bc57aa96fee01b077","sup_171ea0fe6f49dccb8fee"],"title":"the idhā frame echoes the earlier danger trigger","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:5","qac_refs":["113:5:4:1"],"status":"accepted"}},{"anchor_refs":["113:5:5"],"branch_refs":[],"candidate_id":"cand_d5a2465544fca2b33018","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"113:5:5:expected-when-not-sudden-if","source_type":"word_analysis","support_ids":["sup_171ea0fe6f49dccb8fee","sup_6ab094ca694e7e956bcf"],"title":"the particle selects expected when over suddenness or remote if","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:5","qac_refs":["113:5:4:1"],"status":"accepted"}},{"anchor_refs":["113:5:5"],"branch_refs":[],"candidate_id":"cand_52b62a3d2dd216f4a72f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"113:5:5:nominal-source-to-event-trigger","source_type":"word_analysis","support_ids":["sup_171ea0fe6f49dccb8fee","sup_1f6c40e7a0e765f3608c"],"title":"the particle pivots from source to event","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:5","qac_refs":["113:5:4:1"],"status":"accepted"}},{"anchor_refs":["113:5:5"],"branch_refs":[],"candidate_id":"cand_8c654d4aa6a549c2655b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"113:5:5:particle-perfect-conditional-unit","source_type":"word_analysis","support_ids":["sup_0676f9b6e08de10cdadc","sup_171ea0fe6f49dccb8fee"],"title":"idhā plus perfect makes a compact whenever-unit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:5","qac_refs":["113:5:4:1"],"status":"accepted"}},{"anchor_refs":["113:5:6"],"branch_refs":[],"candidate_id":"cand_e57095bd4d78889e4e28","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:6:agent-act-root-reprise","source_type":"word_analysis","support_ids":["sup_02be739ad530c8918057","sup_8d93f9ec2dd7550a33fa"],"title":"the root reprise turns identity into action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:6","qac_refs":["113:5:5:1"],"status":"accepted"}},{"anchor_refs":["113:5:6"],"branch_refs":[],"candidate_id":"cand_ab0349322e2c0d098018","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:6:convergence-root-ellipsis-closure","source_type":"word_analysis","support_ids":["sup_02be739ad530c8918057","sup_cdd7463e0596c2af3dc0"],"title":"root echo, object omission, and closure converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:6","qac_refs":["113:5:5:1"],"status":"accepted"}},{"anchor_refs":["113:5:6"],"branch_refs":[],"candidate_id":"cand_3bff355b847066cb4982","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:6:destructive-envy-selected","source_type":"word_analysis","support_ids":["sup_02be739ad530c8918057","sup_fa238da94159eafa9041"],"title":"the verb means harmful envying, not neutral admiration","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:6","qac_refs":["113:5:5:1"],"status":"accepted"}},{"anchor_refs":["113:5:6"],"branch_refs":[],"candidate_id":"cand_7760543783afd59f326b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:6:echoes-113-3-trigger-frame","source_type":"word_analysis","support_ids":["sup_02be739ad530c8918057","sup_3ea64d9ffe3feef86f6c"],"title":"the final trigger frame echoes 113:3","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:6","qac_refs":["113:5:5:1"],"status":"accepted"}},{"anchor_refs":["113:5:6"],"branch_refs":[],"candidate_id":"cand_9fb8c4a3ee082189804a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:6:final-sound-echo","source_type":"word_analysis","support_ids":["sup_02be739ad530c8918057","sup_7709ab059e111e176e78"],"title":"sound closes the agent-act thread","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:6","qac_refs":["113:5:5:1"],"status":"accepted"}},{"anchor_refs":["113:5:6"],"branch_refs":[],"candidate_id":"cand_2b0f1ae8fc669a77732c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:6:object-ellipsis-broadens-act","source_type":"word_analysis","support_ids":["sup_02be739ad530c8918057","sup_26f06453cad19cef3e7a"],"title":"the object is omitted so the act is foregrounded","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:6","qac_refs":["113:5:5:1"],"status":"accepted"}},{"anchor_refs":["113:5:6"],"branch_refs":[],"candidate_id":"cand_960a3e7462f9af4a2147","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:6:perfect-form-salience","source_type":"word_analysis","support_ids":["sup_02be739ad530c8918057","sup_996f87116bf6ce4313f2"],"title":"the final perfect stands out in the small root field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:6","qac_refs":["113:5:5:1"],"status":"accepted"}},{"anchor_refs":["113:5:6"],"branch_refs":[],"candidate_id":"cand_ffadd566d032d5c3c313","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:6:perfect-under-idha-activation","source_type":"word_analysis","support_ids":["sup_02be739ad530c8918057","sup_3812d037152a7de9574f"],"title":"the perfect verb supplies the activated event","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:6","qac_refs":["113:5:5:1"],"status":"accepted"}},{"anchor_refs":["113:5:6"],"branch_refs":[],"candidate_id":"cand_7eea425adef3eeec51f9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:6:stripping-image-narrowed","source_type":"word_analysis","support_ids":["sup_02be739ad530c8918057","sup_c2455050e62c694f844f"],"title":"stripping imagery sharpens envy as removal-force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:6","qac_refs":["113:5:5:1"],"status":"accepted"}},{"anchor_refs":["113:5:6"],"branch_refs":[],"candidate_id":"cand_4d1a3824252f90874828","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:6:subject-controlled-by-envier","source_type":"word_analysis","support_ids":["sup_02be739ad530c8918057","sup_ab128490baaea2f1ce03"],"title":"the compact verb resolves back to the envier","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:6","qac_refs":["113:5:5:1"],"status":"accepted"}},{"anchor_refs":["113:5:6"],"branch_refs":[],"candidate_id":"cand_b3c6bf65d4fa321754bd","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:6:surah-closure-on-activated-envy","source_type":"word_analysis","support_ids":["sup_02be739ad530c8918057","sup_d9e6d93d3f7eea25b08f"],"title":"the surah closes on activated envy","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"113:5:6","qac_refs":["113:5:5:1"],"status":"accepted"}},{"anchor_refs":["113:5:2"],"branch_refs":[],"candidate_id":"cand_65c9cd4b470c42eca4b4","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000787","root_000792"],"scope":"focus_ayah","source_local_id":"113:5:2:1","source_type":"qac_morpheme","support_ids":["sup_4955117267bd3a60baa7"],"title":"QAC root occurrence: ش ر ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["113:5:3"],"branch_refs":[],"candidate_id":"cand_af40b0bfc440e013d59e","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000319"],"scope":"focus_ayah","source_local_id":"113:5:3:1","source_type":"qac_morpheme","support_ids":["sup_cf8791188d0cc6bfa937"],"title":"QAC root occurrence: ح س د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["113:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"113:5","branch_refs":["root_000319/B001","root_000787/B001"],"candidate_id":"cand_914bfb7d0684ef1c8964","commentary_obligation":"review","hft_ref":"hft_64a295499980e5ddd4b6","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_event_gated_envy","source_type":"hft","support_ids":["sup_06bd1370c77bf67f0f3f"],"title":"baseline_event_gated_envy","trust":"legacy_unbound"},{"anchor_refs":["113:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"113:5","branch_refs":["root_000319/B001","root_000319/B002"],"candidate_id":"cand_adbe095dcc684168200b","commentary_obligation":"review","hft_ref":"hft_e377f9be0545958c5de7","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_admiration_fork","source_type":"hft","support_ids":["sup_35613bbd5efe1eed9eb1"],"title":"baseline_admiration_fork","trust":"legacy_unbound"},{"anchor_refs":["113:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"113:5","branch_refs":["root_000319/B001","root_000792/B002"],"candidate_id":"cand_cc2dd73a9f468d6783ea","commentary_obligation":"review","hft_ref":"hft_8669d3934f3c2fca32bc","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_false_parity","source_type":"hft","support_ids":["sup_9816952df4200296b721"],"title":"baseline_false_parity","trust":"legacy_unbound"},{"anchor_refs":["113:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"113:5","branch_refs":["root_000319/B001","root_000792/B012"],"candidate_id":"cand_8e8ade73f0f9958d523c","commentary_obligation":"review","hft_ref":"hft_08d0743e8d898aec7fa3","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_maledictive_projection","source_type":"hft","support_ids":["sup_1f51e32cf1b79883ebaa"],"title":"baseline_maledictive_projection","trust":"legacy_unbound"},{"anchor_refs":["113:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"113:5","branch_refs":["root_000319/B001","root_000787/B009","root_000792/B009"],"candidate_id":"cand_7983e493711ca3a93025","commentary_obligation":"review","hft_ref":"hft_f6fe006036c4238e472c","kind":"surprising_outlier","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:outlier_distributed_irritation","source_type":"hft","support_ids":["sup_86b6ecca7eb8170531c4"],"title":"outlier_distributed_irritation","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"113:5:1:1","qac_word_ref":"113:5:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"مِن","morph_features":"STEM|POS:P|LEM:min","morpheme_role":"STEM","pos":"P","qac_ref":"113:5:1:2","qac_word_ref":"113:5:1","root_ar":"","surface_ar":"مِن"},{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","root_ar":"ش ر ر","surface_ar":"شَرِّ"},{"lemma_ar":"حَاسِد","morph_features":"STEM|POS:N|ACT|PCPL|LEM:HaAsid|ROOT:Hsd|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:3:1","qac_word_ref":"113:5:3","root_ar":"ح س د","surface_ar":"حَاسِدٍ"},{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"113:5:4:1","qac_word_ref":"113:5:4","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"حَسَدَ","morph_features":"STEM|POS:V|PERF|LEM:Hasada|ROOT:Hsd|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"113:5:5:1","qac_word_ref":"113:5:5","root_ar":"ح س د","surface_ar":"حَسَدَ"}],"word_analysis_qac_refs":[["113:5:1:1"],["113:5:1:2"],["113:5:2:1"],["113:5:3:1"],["113:5:4:1"],["113:5:5:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["113:5:1","113:5:2","113:5:3","113:5:4","113:5:5","113:5:6"]},"focus_surface_evidence":{"arabic_uthmani":"وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"113:5:1:1","qac_word_ref":"113:5:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"مِن","morph_features":"STEM|POS:P|LEM:min","morpheme_role":"STEM","pos":"P","qac_ref":"113:5:1:2","qac_word_ref":"113:5:1","root_ar":"","surface_ar":"مِن"},{"lemma_ar":"شَرّ","morph_features":"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:2:1","qac_word_ref":"113:5:2","root_ar":"ش ر ر","surface_ar":"شَرِّ"},{"lemma_ar":"حَاسِد","morph_features":"STEM|POS:N|ACT|PCPL|LEM:HaAsid|ROOT:Hsd|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"113:5:3:1","qac_word_ref":"113:5:3","root_ar":"ح س د","surface_ar":"حَاسِدٍ"},{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"113:5:4:1","qac_word_ref":"113:5:4","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"حَسَدَ","morph_features":"STEM|POS:V|PERF|LEM:Hasada|ROOT:Hsd|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"113:5:5:1","qac_word_ref":"113:5:5","root_ar":"ح س د","surface_ar":"حَسَدَ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["113:5:1:1"],["113:5:1:2"],["113:5:2:1"],["113:5:3:1"],["113:5:4:1"],["113:5:5:1"]],"word_analysis_refs":["113:5:1","113:5:2","113:5:3","113:5:4","113:5:5","113:5:6"],"word_rows":[{"analysis_record_ref":"113:5:1","analytic_gloss_range_en":"coordinating particle that keeps the final refuge phrase joined to the preceding list","analytic_root_gloss_range_en":null,"qac_refs":["113:5:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"113:5:2","analytic_gloss_range_en":"source preposition governing the harm phrase, with a limited partitive nuance where the evil-dimension is in view","analytic_root_gloss_range_en":null,"qac_refs":["113:5:1:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"مِن","transliteration":"min"}},{"analysis_record_ref":"113:5:3","analytic_gloss_range_en":"evil, harm, or harmful force, locally governed by the source preposition and specified by the envier","analytic_root_gloss_range_en":"evil and badness is the active local branch; spreading, sparks, and scattering images remain secondary root-image pressure, not the lexical sense selected here","qac_refs":["113:5:2:1"],"root":{"arabic":"ش ر ر","transliteration":"sh-r-r"},"surface":{"arabic":"شَرِّ","transliteration":"sharri"}},{"analysis_record_ref":"113:5:4","analytic_gloss_range_en":"an indefinite active-participle envier, locally the genitive source of harm and the participant later resumed by the verb","analytic_root_gloss_range_en":"destructive envy, wishing-away, and possible envious-gaze extension; non-harmful emulative envy is excluded by the refuge context","qac_refs":["113:5:3:1"],"root":{"arabic":"ح س د","transliteration":"ḥ-s-d"},"surface":{"arabic":"حَاسِدٍ","transliteration":"ḥāsidin"}},{"analysis_record_ref":"113:5:5","analytic_gloss_range_en":"temporal-conditional particle marking expected or recurring activation, not sudden arrival or remote uncertainty","analytic_root_gloss_range_en":null,"qac_refs":["113:5:4:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"إِذَا","transliteration":"idhā"}},{"analysis_record_ref":"113:5:6","analytic_gloss_range_en":"Form I perfect verb of destructive envying, locally without an overt object or cause and controlled by the named envier","analytic_root_gloss_range_en":"destructive envy and wishing-away is active; scraping or stripping imagery survives as root-image pressure, not as a replacement for envying","qac_refs":["113:5:5:1"],"root":{"arabic":"ح س د","transliteration":"ḥ-s-d"},"surface":{"arabic":"حَسَدَ","transliteration":"ḥasada"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":6,"words_total":6,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["113:5"],"branch_refs":["root_000319/B001","root_000787/B001"],"candidate_id":"cand_914bfb7d0684ef1c8964","evidence_scope":"focus_ayah","hft_ref":"hft_64a295499980e5ddd4b6","item_id":"baseline_event_gated_envy","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_event_gated_envy","support_id":"sup_06bd1370c77bf67f0f3f"},{"anchor_refs":["113:5"],"branch_refs":["root_000319/B001","root_000319/B002"],"candidate_id":"cand_adbe095dcc684168200b","evidence_scope":"focus_ayah","hft_ref":"hft_e377f9be0545958c5de7","item_id":"baseline_admiration_fork","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_admiration_fork","support_id":"sup_35613bbd5efe1eed9eb1"},{"anchor_refs":["113:5"],"branch_refs":["root_000319/B001","root_000792/B002"],"candidate_id":"cand_cc2dd73a9f468d6783ea","evidence_scope":"focus_ayah","hft_ref":"hft_8669d3934f3c2fca32bc","item_id":"baseline_false_parity","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_false_parity","support_id":"sup_9816952df4200296b721"},{"anchor_refs":["113:5"],"branch_refs":["root_000319/B001","root_000792/B012"],"candidate_id":"cand_8e8ade73f0f9958d523c","evidence_scope":"focus_ayah","hft_ref":"hft_08d0743e8d898aec7fa3","item_id":"baseline_maledictive_projection","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_maledictive_projection","support_id":"sup_1f51e32cf1b79883ebaa"},{"anchor_refs":["113:5"],"branch_refs":["root_000319/B001","root_000787/B009","root_000792/B009"],"candidate_id":"cand_7983e493711ca3a93025","evidence_scope":"focus_ayah","hft_ref":"hft_f6fe006036c4238e472c","item_id":"outlier_distributed_irritation","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_distributed_irritation","support_id":"sup_86b6ecca7eb8170531c4"}],"diagnostics":[],"lane_counts":{"global":10,"macro":10,"micro":5},"packet_summary":{"ayah_count":5,"focus_ref":"113:5","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ش ر ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000787","furuq_root_norm":"ش ر ر","furuq_source_root_norm":"ش ر ر","is_dominant":true,"target_occurrences":19,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000792","furuq_root_norm":"ش ر ي","furuq_source_root_norm":"ش ر ي","is_dominant":false,"target_occurrences":11,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["113:1","113:2","113:3","113:4","113:5"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"113:5","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"113:5","lane":"micro","linguistic_source_ref":"113:5","surface_ref":"113:5","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"113:5","target_tokens":[["ve",["113:5:1"]],["kıskanan",["113:5:3"]],["kıskandığında",["113:5:4","113:5:5"]],["onun",["113:5:3"]],["kötülüğünden",["113:5:1","113:5:2"]]],"text":"ve kıskanan kıskandığında onun kötülüğünden.\""},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":5,"id":"s113-p01-001-005","label":"Whole surah","number":1,"refs":["113:1","113:2","113:3","113:4","113:5"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:6","source_type":"word_analysis","support_id":"sup_02be739ad530c8918057","text":"{\"gloss_range\":\"Form I perfect verb of destructive envying, locally without an overt object or cause and controlled by the named envier\",\"prose\":\"{{ar:حَسَدَ}} ({{tr:ḥasada}}) closes the ayah and the surah by turning the named envier into an act. Its 3ms subject is not restated because it resolves back to {{ar:حَاسِدٍ}} ({{tr:ḥāsidin}}), and its object is not stated at all, so the focus falls on envying itself rather than on one envied person, possession, or cause. Under {{ar:إِذَا}} ({{tr:idhā}}), the perfect form works as a recurring activation point while still packaging each envy-act as complete, and it reprises the danger-trigger pattern from 113:3 with an agent already named. The destructive envy branch is selected over harmless admiration; scraping or stripping imagery can explain the removing force of the act, but the local verb still means envying. As the final perfect in a small h-s-d field, it stands out as a marked eventive close, with a breath-hiss-stop texture and same-root echo that tighten the agent-act thread.\",\"root_display\":\"{{ar:ح س د}} ({{tr:ḥ-s-d}})\",\"root_gloss_range\":\"destructive envy and wishing-away is active; scraping or stripping imagery survives as root-image pressure, not as a replacement for envying\",\"surface_display\":\"{{ar:حَسَدَ}} ({{tr:ḥasada}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:5:particle-perfect-conditional-unit","source_type":"word_analysis","support_id":"sup_0676f9b6e08de10cdadc","text":"{\"blocking_evidence\":null,\"headline\":\"idhā plus perfect makes a compact whenever-unit\",\"reader_payoff\":\"The reader notices that the whenever-he-envies sense comes from the particle and verb together, not from the verb alone.\",\"reason\":\"{{ar:إِذَا}} ({{tr:idhā}}) introduces the temporal clause and governs how the perfect verb projects habitual or future conditional force.\",\"representative_source_ids\":[\"QF-423f2a4f\",\"QT-0e098310\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:1:coordinated-final-refuge-clause","source_type":"word_analysis","support_id":"sup_0a73e43b8ab2c603a3a9","text":"{\"blocking_evidence\":null,\"headline\":\"the final threat remains inside the coordinated refuge list\",\"reader_payoff\":\"The reader notices that the last ayah is a linked final member of the refuge sequence, not an independent afterthought.\",\"reason\":\"QAC identifies {{ar:وَ}} ({{tr:wa}}) as coordination, and the attachment support keeps the repeated refuge frame attached to the opening request.\",\"representative_source_ids\":[\"QG-0f16b893\",\"QT-728e7d36\",\"QT-b0744bb4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:5:echoes-113-3-trigger-frame","source_type":"word_analysis","support_id":"sup_156bc57aa96fee01b077","text":"{\"blocking_evidence\":null,\"headline\":\"the idhā frame echoes the earlier danger trigger\",\"reader_payoff\":\"The reader hears 113:5 repeat the danger-at-a-moment pattern already used in 113:3.\",\"reason\":\"The row gives the concrete same-surah parallel, so the echo can survive without making the earlier frame control the local parse.\",\"representative_source_ids\":[\"QE-f27652a2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:5","source_type":"word_analysis","support_id":"sup_171ea0fe6f49dccb8fee","text":"{\"gloss_range\":\"temporal-conditional particle marking expected or recurring activation, not sudden arrival or remote uncertainty\",\"prose\":\"{{ar:إِذَا}} ({{tr:idhā}}) is the hinge between the named source and the act. It opens {{ar:إِذَا حَسَدَ}} ({{tr:idhā ḥasada}}), a temporal-conditional unit that ties the evil to the moment the envier envies. The particle gives an expected when-ever force rather than a sudden-arrival reading or a remote if, so the threat is not the bare existence of the envier but the activation of envy. That trigger logic repeats the surah's earlier danger-at-a-moment pattern in 113:3 while making the final threat event-based.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِذَا}} ({{tr:idhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:5:nominal-source-to-event-trigger","source_type":"word_analysis","support_id":"sup_1f6c40e7a0e765f3608c","text":"{\"blocking_evidence\":null,\"headline\":\"the particle pivots from source to event\",\"reader_payoff\":\"The reader sees the ayah move from naming the source of harm to naming the event that makes the source active.\",\"reason\":\"The particle stands after the nominal construct and before the finite verb, marking the transition from source phrase to activation clause.\",\"representative_source_ids\":[\"QT-1b757c1d\",\"QB-f0989f9e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:6:object-ellipsis-broadens-act","source_type":"word_analysis","support_id":"sup_26f06453cad19cef3e7a","text":"{\"blocking_evidence\":null,\"headline\":\"the object is omitted so the act is foregrounded\",\"reader_payoff\":\"The reader notices that the ayah does not name what is envied, making the act of envy itself the focal danger.\",\"reason\":\"The verb instance and translation support mark the object as absent, with the frame status obj=none_absolute.\",\"representative_source_ids\":[\"QG-135f5fb0\",\"QG-3c21316f\",\"QG-641cb7d7\",\"QT-4c415abd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:4:envious-gaze-extension","source_type":"word_analysis","support_id":"sup_2c21a2be40c9be6772de","text":"{\"blocking_evidence\":null,\"headline\":\"the agent word can include the envious gaze\",\"reader_payoff\":\"The reader can include the manifestation of an envious gaze without replacing the basic agent noun.\",\"reason\":\"The extension survives as range around the envier, but local grammar still names an active-participle agent.\",\"representative_source_ids\":[\"QS-6ed49414\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:6:perfect-under-idha-activation","source_type":"word_analysis","support_id":"sup_3812d037152a7de9574f","text":"{\"blocking_evidence\":null,\"headline\":\"the perfect verb supplies the activated event\",\"reader_payoff\":\"The reader notices that the perfect form under {{ar:إِذَا}} ({{tr:idhā}}) gives a recurring condition while keeping each act event-like and complete.\",\"reason\":\"QAC marks the verb as perfect under {{ar:إِذَا}} ({{tr:idhā}}), yielding habitual or future conditional force.\",\"representative_source_ids\":[\"QG-da08d455\",\"QF-8d240546\",\"QT-7812d39d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:4:destructive-envy-not-admiration","source_type":"word_analysis","support_id":"sup_3be0b58156ecefb9e57f","text":"{\"blocking_evidence\":null,\"headline\":\"the active threat is destructive envy\",\"reader_payoff\":\"The reader distinguishes the envier from a neutral admirer: the danger is wishing-away or resentful harm.\",\"reason\":\"V4 includes both destructive and emulative envy branches, but the refuge-from-harm frame selects destructive envy; broader claims about Quran-wide divine-giving patterns are not needed for the local payoff.\",\"representative_source_ids\":[\"QS-bcf7526f\",\"QS-f26ea6a6\",\"MI-473a6d44\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:4:active-participle-disposition-before-event","source_type":"word_analysis","support_id":"sup_3cc73bb23f06784dc7ea","text":"{\"blocking_evidence\":null,\"headline\":\"the participle names disposition before the act\",\"reader_payoff\":\"The reader sees the ayah first name the disposition-bearing agent, then activate that agent through the later verb.\",\"reason\":\"QAC identifies the word as an active participle, and the later 3ms subject of {{ar:حَسَدَ}} ({{tr:ḥasada}}) is controlled by this same envier.\",\"representative_source_ids\":[\"QG-b6becc5e\",\"QF-ae45e4d7\",\"QS-13fb3ef6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:3","source_type":"word_analysis","support_id":"sup_3cef889af34ade0b96bc","text":"{\"gloss_range\":\"evil, harm, or harmful force, locally governed by the source preposition and specified by the envier\",\"prose\":\"{{ar:شَرِّ}} ({{tr:sharri}}) is the repeated harm noun of the surah's refuge list, but here it is tightly governed and specified: {{ar:مِن}} ({{tr:min}}) makes it the source-domain to be escaped, and iḍāfa binds it to {{ar:حَاسِدٍ}} ({{tr:ḥāsidin}}). As a singular abstract, it names the harmful principle rather than counting separate evils, and it establishes the nominal source before the following temporal clause activates it. The root correction matters because the active field is {{ar:ش ر ر}} ({{tr:sh-r-r}}), evil or badness, not a buying-selling root. Secondary root images of spreading or sparks can sharpen the outgoing feel of harm, and the doubled sound gives the noun compact weight before the envier is named, but neither feature replaces the local sense of evil sourced through the envier.\",\"root_display\":\"{{ar:ش ر ر}} ({{tr:sh-r-r}})\",\"root_gloss_range\":\"evil and badness is the active local branch; spreading, sparks, and scattering images remain secondary root-image pressure, not the lexical sense selected here\",\"surface_display\":\"{{ar:شَرِّ}} ({{tr:sharri}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:6:echoes-113-3-trigger-frame","source_type":"word_analysis","support_id":"sup_3ea64d9ffe3feef86f6c","text":"{\"blocking_evidence\":null,\"headline\":\"the final trigger frame echoes 113:3\",\"reader_payoff\":\"The reader hears the same-surah pattern of dangers becoming relevant at a specified moment in 113:3 and 113:5.\",\"reason\":\"The concrete reference is local and useful as an echo, while the current verb still governs the final envy event.\",\"representative_source_ids\":[\"QE-dfaa3db2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"113:5:2:1","source_type":"qac_morpheme","support_id":"sup_4955117267bd3a60baa7","text":"{\"lemma_ar\":\"شَرّ\",\"morph_features\":\"STEM|POS:N|LEM:$ar~|ROOT:$rr|MS|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"113:5:2:1\",\"qac_word_ref\":\"113:5:2\",\"root_ar\":\"ش ر ر\",\"surface_ar\":\"شَرِّ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:3:root-correction-evil-branch","source_type":"word_analysis","support_id":"sup_4988198428b4d6e12695","text":"{\"blocking_evidence\":null,\"headline\":\"the operative root is evil, not buying and selling\",\"reader_payoff\":\"The reader keeps the analysis in the harm field and avoids importing a false exchange-root association.\",\"reason\":\"QAC explicitly corrects the root to {{ar:ش ر ر}} ({{tr:sh-r-r}}), and V4 lists evil and badness as the relevant accepted branch.\",\"representative_source_ids\":[\"QS-c49ba757\",\"QF-1f78d732\",\"QS-5e9bcb30\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:1","source_type":"word_analysis","support_id":"sup_580baa7f9eab91793428","text":"{\"gloss_range\":\"coordinating particle that keeps the final refuge phrase joined to the preceding list\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) does not let the final line stand as a detached sentence. It coordinates the last source of harm with the earlier refuge sequence, and because it is fused in the visible launch {{ar:وَمِن}} ({{tr:wa-min}}), the listener hears both continuation and a fresh final entry in the list. The payoff is structural: the ayah crosses the boundary from the previous threat while still remaining inside the same refuge request, so the series can reach its final psychological source without losing the accumulated list-pressure.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:3:source-before-activation","source_type":"word_analysis","support_id":"sup_59478a55a2e713676d42","text":"{\"blocking_evidence\":null,\"headline\":\"the phrase names the source before the event\",\"reader_payoff\":\"The reader notices the sequence: first the nominal source of harm, then the temporal activation of that source.\",\"reason\":\"The construct phrase precedes the {{ar:إِذَا حَسَدَ}} ({{tr:idhā ḥasada}}) temporal clause, separating named source from triggered event.\",\"representative_source_ids\":[\"QT-be9cbc27\",\"QT-4040caa5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:1:accumulative-wa-min-refrain","source_type":"word_analysis","support_id":"sup_6684ca1c3723086a6281","text":"{\"blocking_evidence\":null,\"headline\":\"the wa-min opening audibly repeats the refuge refrain\",\"reader_payoff\":\"The reader hears the repeated {{ar:وَمِن}} ({{tr:wa-min}}) frame as an accumulative refrain that reaches its final source in 113:5.\",\"reason\":\"The same-surah repetition is licensed by the cross-reference evidence for the repeated refuge-from-evil formula first instantiated in 113:2.\",\"representative_source_ids\":[\"MG-112969bf\",\"QE-f0d2fa1f\",\"QB-60684bc3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:5:expected-when-not-sudden-if","source_type":"word_analysis","support_id":"sup_6ab094ca694e7e956bcf","text":"{\"blocking_evidence\":null,\"headline\":\"the particle selects expected when over suddenness or remote if\",\"reader_payoff\":\"The reader hears a likely or recurring condition, not a surprise event and not a merely hypothetical possibility.\",\"reason\":\"QAC identifies the particle as temporal-conditional and contrasts it with uncertain conditions, while the perfect verb in the clause blocks the suddenness reading here.\",\"representative_source_ids\":[\"QS-ae806d55\",\"QS-c6111fbe\",\"QS-fda471b3\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:2:partitive-harm-dimension","source_type":"word_analysis","support_id":"sup_6bc2b901d011a45840d2","text":"{\"blocking_evidence\":null,\"headline\":\"partitive pressure focuses the evil-dimension\",\"reader_payoff\":\"The reader notices that the refuge can target the harmful dimension activated by envy without turning the whole person into a flat category of evil.\",\"reason\":\"The source relation is primary in the local grammar; the partitive reading survives only as a qualifying nuance of the harm being sought away from.\",\"representative_source_ids\":[\"QS-3b3c5b8e\",\"MH-d713a0ef\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:2:wa-min-prepositional-refrain","source_type":"word_analysis","support_id":"sup_70dcb8477d9adaff250b","text":"{\"blocking_evidence\":null,\"headline\":\"wa-min preserves the fourth prepositional refuge frame\",\"reader_payoff\":\"The reader hears the final phrase as the fourth occurrence of the local refuge pattern rather than as a new syntactic design.\",\"reason\":\"The attachment cross-reference explicitly links the repeated {{ar:وَمِن شَرِّ}} ({{tr:wa-min sharri}}) formula to 113:2, while the preposition remains separately governing inside the fused surface.\",\"representative_source_ids\":[\"QF-9c691981\",\"QT-cb4d0720\",\"QE-cdd40c11\",\"QB-7a7b3c24\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:4","source_type":"word_analysis","support_id":"sup_745cf6f831ea66e994d0","text":"{\"gloss_range\":\"an indefinite active-participle envier, locally the genitive source of harm and the participant later resumed by the verb\",\"prose\":\"{{ar:حَاسِدٍ}} ({{tr:ḥāsidin}}) is not a named class with a definite article; its tanwīn leaves the source open, so the final threat can be any envier rather than a bounded practitioner-class like the prior threat in 113:4. As an active participle it names a disposition-bearing agent before the verb shows the act, and the iḍāfa with {{ar:شَرِّ}} ({{tr:sharri}}) makes that agent the source or possessor of the harm. The destructive branch of envy is active here; the non-harmful admiration sense is blocked by the refuge context, while the envious-gaze extension can remain a secondary range within the same agent word. Its rare root field, breath-hiss-stop consonants, and imāla variant make the final agent a marked, reading-sensitive anchor: the sound can shift without changing the harmful referent, and the later same-root verb turns this inward disposition into action.\",\"root_display\":\"{{ar:ح س د}} ({{tr:ḥ-s-d}})\",\"root_gloss_range\":\"destructive envy, wishing-away, and possible envious-gaze extension; non-harmful emulative envy is excluded by the refuge context\",\"surface_display\":\"{{ar:حَاسِدٍ}} ({{tr:ḥāsidin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:3:spreading-sparks-image-narrowed","source_type":"word_analysis","support_id":"sup_76d0db5b141437afef49","text":"{\"blocking_evidence\":null,\"headline\":\"spreading and spark images sharpen outgoing harm\",\"reader_payoff\":\"The reader can feel the evil as an outgoing harmful force from the envier, while keeping evil as the selected lexical sense.\",\"reason\":\"V4 accepts spreading and spark branches for the root family, but the local noun and QAC grammar select evil and badness; the image survives only as concrete pressure.\",\"representative_source_ids\":[\"MG-a40215b5\",\"QS-8cb2cd54\",\"QS-8ed5f9f9\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:6:final-sound-echo","source_type":"word_analysis","support_id":"sup_7709ab059e111e176e78","text":"{\"blocking_evidence\":null,\"headline\":\"sound closes the agent-act thread\",\"reader_payoff\":\"The reader hears a clipped final sound and a consonantal echo between the envier and the act.\",\"reason\":\"The phonetic thread is anchored in the repeated {{ar:ح س د}} ({{tr:ḥ-s-d}}) consonants and the final position of the verb.\",\"representative_source_ids\":[\"QP-09043e6d\",\"QP-0b56bbe9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:2","source_type":"word_analysis","support_id":"sup_7724a90715e8ddebe807","text":"{\"gloss_range\":\"source preposition governing the harm phrase, with a limited partitive nuance where the evil-dimension is in view\",\"prose\":\"{{ar:مِن}} ({{tr:min}}) is the first governing word after the conjunction. It makes {{ar:شَرِّ}} ({{tr:sharri}}) genitive and frames the envier as a source from which refuge is sought. The repeated {{ar:مِن شَرِّ}} ({{tr:min sharri}}) frame ties 113:5 to 113:2, 113:3, and 113:4, while the possible partitive shade keeps the focus on the harmful dimension of the envier, not on every aspect of the person.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مِن}} ({{tr:min}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:4:idafa-source-possessor","source_type":"word_analysis","support_id":"sup_7daed34fe947e8175130","text":"{\"blocking_evidence\":null,\"headline\":\"the envier specifies whose evil is in view\",\"reader_payoff\":\"The reader sees the envier as the specifying source or possessor of the evil, not merely as a person mentioned after it.\",\"reason\":\"Attachment evidence forces {{ar:حَاسِدٍ}} ({{tr:ḥāsidin}}) as the genitive complement in {{ar:شَرِّ حَاسِدٍ}} ({{tr:sharri ḥāsidin}}).\",\"representative_source_ids\":[\"QG-542ffef6\",\"QT-e68f4da4\",\"QT-eddfac8e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:3:compressed-sound-weight","source_type":"word_analysis","support_id":"sup_7e754d7bf5862065c92b","text":"{\"blocking_evidence\":null,\"headline\":\"geminated sound gives the harm noun compact weight\",\"reader_payoff\":\"The reader notices the compact acoustic weight of the harm noun before the envier is named.\",\"reason\":\"The surface is a compact geminate-root noun; this is a phonetic payoff rather than a separate lexical sense.\",\"representative_source_ids\":[\"QP-76caca5b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:3:singular-abstract-harm-field","source_type":"word_analysis","support_id":"sup_8b251cfc35f7e707f29c","text":"{\"blocking_evidence\":null,\"headline\":\"the singular abstract gathers the harm field\",\"reader_payoff\":\"The reader notices that the singular noun names the harmful principle being sourced, rather than counting multiple separate evils.\",\"reason\":\"The local form is an abstract noun, and the contextual profile shows this root-form regularly functioning as a noun in harm-related environments.\",\"representative_source_ids\":[\"QS-486827c8\",\"QS-ffda1e04\",\"QF-01624634\",\"QI-24ae33c6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:6:agent-act-root-reprise","source_type":"word_analysis","support_id":"sup_8d93f9ec2dd7550a33fa","text":"{\"blocking_evidence\":null,\"headline\":\"the root reprise turns identity into action\",\"reader_payoff\":\"The reader hears the agent noun answered by the verb, so the final clause moves from who the envier is to what he does.\",\"reason\":\"The same root appears first as active participle and then as finite perfect verb, with the verb subject controlled by the named agent.\",\"representative_source_ids\":[\"QS-2b911744\",\"QF-0bc481e7\",\"QE-2289300e\",\"QE-33cb0b11\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:3:closing-convergence","source_type":"word_analysis","support_id":"sup_963da8091420588ef64a","text":"{\"blocking_evidence\":null,\"headline\":\"recurrence and image converge at the final threat\",\"reader_payoff\":\"The reader sees the final occurrence of the repeated harm formula as both locally specified and less bounded through the envier source.\",\"reason\":\"The convergence is kept, with the scattering image narrowed to secondary pressure and the local sense anchored in the repeated harm noun.\",\"representative_source_ids\":[\"QY-57b10a09\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:6:perfect-form-salience","source_type":"word_analysis","support_id":"sup_996f87116bf6ce4313f2","text":"{\"blocking_evidence\":null,\"headline\":\"the final perfect stands out in the small root field\",\"reader_payoff\":\"The reader notices the closing verb as a marked eventive use within a small supplied root field.\",\"reason\":\"The contextual profile marks the exact root-form as low occurrence, and the local form is a perfect verb at the final position.\",\"representative_source_ids\":[\"QF-ff554828\",\"QI-20f83841\",\"QI-537e83a0\",\"QH-1cc30197\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:1:coordination-plus-resumption","source_type":"word_analysis","support_id":"sup_99896141d1f5d5336f9f","text":"{\"blocking_evidence\":null,\"headline\":\"the boundary both joins and restarts attention\",\"reader_payoff\":\"The reader notices that the particle carries the list forward while making the ayah-opening launch feel newly focused.\",\"reason\":\"The conjunction remains coordinating, while its ayah-initial position and fusion with {{ar:مِن}} ({{tr:min}}) give the final item a renewed entry point.\",\"representative_source_ids\":[\"QS-47bd6c5e\",\"QF-d490929f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:6:subject-controlled-by-envier","source_type":"word_analysis","support_id":"sup_ab128490baaea2f1ce03","text":"{\"blocking_evidence\":null,\"headline\":\"the compact verb resolves back to the envier\",\"reader_payoff\":\"The reader sees a compact agent chain: the verb's unspoken subject is the envier already named.\",\"reason\":\"Attachment evidence marks the 3ms subject as syntactically controlled by {{ar:حَاسِدٍ}} ({{tr:ḥāsidin}}), so no new actor should be introduced.\",\"representative_source_ids\":[\"QG-485aac58\",\"QF-cc06aeca\",\"QS-fccbd035\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:3:same-surah-sharr-thread","source_type":"word_analysis","support_id":"sup_adf9b7f5312382acae9d","text":"{\"blocking_evidence\":null,\"headline\":\"the repeated harm noun binds the threat list\",\"reader_payoff\":\"The reader hears one repeated harm category carried through different sources across 113:2, 113:3, 113:4, and 113:5.\",\"reason\":\"The same-surah formula and repeated noun are directly supported by the cross-reference evidence and by the QAC phrase structure.\",\"representative_source_ids\":[\"QI-2505b64a\",\"QE-4547d83d\",\"QE-88f398da\",\"QB-cd6cf62c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:4:convergent-agent-anchor","source_type":"word_analysis","support_id":"sup_b7a7ed3b2b64f182759f","text":"{\"blocking_evidence\":null,\"headline\":\"rarity, range, and imāla converge on one agent\",\"reader_payoff\":\"The reader sees one dense agent anchor: rare, open in range, and recitationally colored without losing its referent.\",\"reason\":\"The convergence survives, while the range is limited to the local active-participle agent and its harmful envy frame.\",\"representative_source_ids\":[\"QY-d8cf3ee2\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:4:root-echo-agent-act","source_type":"word_analysis","support_id":"sup_bfaaa176f72f3fa03cca","text":"{\"blocking_evidence\":null,\"headline\":\"the noun and verb bind agent to act\",\"reader_payoff\":\"The reader hears and sees the envier's identity answered by the later act of envying.\",\"reason\":\"Both words share the {{ar:ح س د}} ({{tr:ḥ-s-d}}) root while shifting from active participle to finite verb.\",\"representative_source_ids\":[\"QE-4b0232ec\",\"QE-6eaa7192\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:6:stripping-image-narrowed","source_type":"word_analysis","support_id":"sup_c2455050e62c694f844f","text":"{\"blocking_evidence\":null,\"headline\":\"stripping imagery sharpens envy as removal-force\",\"reader_payoff\":\"The reader can feel why envy is dangerous: it is imagined as wanting-away or stripping, while the verb still means envying.\",\"reason\":\"The image survives as embodied pressure around destructive envy; it does not replace the local verbal sense or require a named object.\",\"representative_source_ids\":[\"QS-42626e87\",\"QS-d9177702\",\"QB-d56ed747\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:4:indefinite-unbounded-envier","source_type":"word_analysis","support_id":"sup_c6cc52d32f68b5480319","text":"{\"blocking_evidence\":null,\"headline\":\"tanwīn leaves the envier source open-ended\",\"reader_payoff\":\"The reader notices that the final threat is less institutionally bounded than the prior definite class in 113:4.\",\"reason\":\"The noun is indefinite and genitive, contrasting with the prior definite class while remaining locally tied to the harm phrase.\",\"representative_source_ids\":[\"QG-7b5c2914\",\"QF-8c32a7fc\",\"QI-5780e147\",\"QB-23f8f946\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:4:rare-root-agent-salience","source_type":"word_analysis","support_id":"sup_cbe3465a9cead061a064","text":"{\"blocking_evidence\":null,\"headline\":\"the small root field makes the envier salient\",\"reader_payoff\":\"The reader notices that this rare root becomes a marked final source, not a routine generic word.\",\"reason\":\"The contextual profile marks the exact root-form as low occurrence, supporting salience without creating a new sense.\",\"representative_source_ids\":[\"QI-5be632cd\",\"QH-5a540d29\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:4:boundary-to-inward-source","source_type":"word_analysis","support_id":"sup_cd664dd7d1173fe30d33","text":"{\"blocking_evidence\":null,\"headline\":\"the boundary moves from ritual medium to inward disposition\",\"reader_payoff\":\"The reader notices the shift from a visible ritual medium in 113:4 to an inward disposition as the final source.\",\"reason\":\"The current word is an indefinite active-participle agent in the harm phrase, allowing the boundary contrast without overdefining the previous ayah.\",\"representative_source_ids\":[\"QB-85ac7a83\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:6:convergence-root-ellipsis-closure","source_type":"word_analysis","support_id":"sup_cdd7463e0596c2af3dc0","text":"{\"blocking_evidence\":null,\"headline\":\"root echo, object omission, and closure converge\",\"reader_payoff\":\"The reader sees why the final verb is heavy: it repeats the envier root, omits the target, and closes on the act of envy.\",\"reason\":\"The convergence survives, while overstatements about identity fusion and cognate structure are narrowed to root echo, controlled subject, object omission, and final position.\",\"representative_source_ids\":[\"MG-37487d76\",\"QY-71660c7f\",\"QY-b76098db\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"113:5:3:1","source_type":"qac_morpheme","support_id":"sup_cf8791188d0cc6bfa937","text":"{\"lemma_ar\":\"حَاسِد\",\"morph_features\":\"STEM|POS:N|ACT|PCPL|LEM:HaAsid|ROOT:Hsd|M|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"113:5:3:1\",\"qac_word_ref\":\"113:5:3\",\"root_ar\":\"ح س د\",\"surface_ar\":\"حَاسِدٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:3:idafa-envier-specification","source_type":"word_analysis","support_id":"sup_d1d46b8cd0cbb3a4d984","text":"{\"blocking_evidence\":null,\"headline\":\"construct state makes the envier specify the evil\",\"reader_payoff\":\"The reader notices that the evil is relational: it is defined through the envier as its specifying source.\",\"reason\":\"Attachment evidence marks {{ar:حَاسِدٍ}} ({{tr:ḥāsidin}}) as the genitive complement in the construct phrase, so the evil remains dependent on its source.\",\"representative_source_ids\":[\"QG-84cf2d74\",\"QG-9af6e977\",\"QF-13ec5103\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:6:surah-closure-on-activated-envy","source_type":"word_analysis","support_id":"sup_d9e6d93d3f7eea25b08f","text":"{\"blocking_evidence\":null,\"headline\":\"the surah closes on activated envy\",\"reader_payoff\":\"The reader feels the closure land on the act itself, not merely on the named envier.\",\"reason\":\"The verb is the final word and supplies the event required by the temporal-conditional frame.\",\"representative_source_ids\":[\"QT-7ea33737\",\"QB-80cddb4b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:4:qiraat-imala-stable-referent","source_type":"word_analysis","support_id":"sup_df97fa8abd37f050da62","text":"{\"blocking_evidence\":null,\"headline\":\"imāla changes recitational color, not the agent\",\"reader_payoff\":\"The reader notices a reading-sensitive surface whose sound can shift while the harmful agent remains the same.\",\"reason\":\"The qiraat note affects vowel color only; it does not change the active participle's referent or grammar.\",\"representative_source_ids\":[\"QF-596fc923\",\"QF-74ad6f05\",\"QP-d07a1258\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:2:min-source-governance","source_type":"word_analysis","support_id":"sup_eee656a043c6cdfbe331","text":"{\"blocking_evidence\":null,\"headline\":\"the preposition governs the source of harm\",\"reader_payoff\":\"The reader sees the phrase as refuge from a source of evil, with {{ar:مِن}} ({{tr:min}}) controlling the relation before the envier is named.\",\"reason\":\"QAC and attachment support both mark {{ar:مِن}} ({{tr:min}}) as governing the genitive harm phrase and preserving the source relation.\",\"representative_source_ids\":[\"QG-787d8f1f\",\"QT-87a11a0d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:4:phonetic-clipped-texture","source_type":"word_analysis","support_id":"sup_f138363c3b22bab37732","text":"{\"blocking_evidence\":null,\"headline\":\"the consonants give the agent noun a clipped texture\",\"reader_payoff\":\"The reader notices the breath-hiss-stop texture of the agent noun as part of its final threat profile.\",\"reason\":\"The sound observation is anchored in the actual consonants and remains a phonetic payoff, not a semantic claim.\",\"representative_source_ids\":[\"QP-fa5e99ee\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:5:activation-scope","source_type":"word_analysis","support_id":"sup_f86eb1cd74e370ef49ef","text":"{\"blocking_evidence\":null,\"headline\":\"idhā scopes the harm to the envying moment\",\"reader_payoff\":\"The reader notices that the refuge turns on the activation of envy, not merely on the envier's existence.\",\"reason\":\"The attachment evidence directly links {{ar:إِذَا حَسَدَ}} ({{tr:idhā ḥasada}}) to the envier as temporal qualification; claims of inevitability are narrowed to expected or recurring activation.\",\"representative_source_ids\":[\"QG-49522fe8\",\"QG-9d65a1be\",\"MT-21293ba5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:6:destructive-envy-selected","source_type":"word_analysis","support_id":"sup_fa238da94159eafa9041","text":"{\"blocking_evidence\":null,\"headline\":\"the verb means harmful envying, not neutral admiration\",\"reader_payoff\":\"The reader distinguishes the final act from harmless admiration; it is morally harmful wishing-away.\",\"reason\":\"V4 gives a non-harmful emulative branch, but the refuge-from-harm context selects the destructive envy branch.\",\"representative_source_ids\":[\"QS-0f592f0e\",\"QS-f70ed8bd\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"113:5:3:governed-harm-source","source_type":"word_analysis","support_id":"sup_fd3ee3899cf74d9443ae","text":"{\"blocking_evidence\":null,\"headline\":\"the harm noun is governed as the refuge source\",\"reader_payoff\":\"The reader sees {{ar:شَرِّ}} ({{tr:sharri}}) as the governed harm-domain from which refuge is sought, not as a loose moral label.\",\"reason\":\"{{ar:مِن}} ({{tr:min}}) governs the genitive noun and routes the phrase back to the same refuge request.\",\"representative_source_ids\":[\"QG-52979498\",\"QT-4040caa5\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ","ayah_ref":"113:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000319/B001","root_000787/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000787","role":"Supplies the explicit harmful field whose timing the rest of the clause restricts.","root":"ش ر ر","source_ref":"113:5","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000319","role":"Supplies desire for the other's blessing to cease, functioning as the latent disposition and its enacted recurrence.","root":"ح س د","source_ref":"113:5","source_word_indices":["3","5"]}],"changed_reading":{"after":"The verse isolates the dangerous interval when a removal-directed disposition crosses into active envy.","before":"The verse labels an envier as a continuously evil type."},"confidence":"strong","focus_anchor":"The active participle حَاسِدٍ is followed by إِذَا and a finite repetition of the same root in حَسَدَ.","mechanism":"The construction separates a bearer of envy from the occasion on which removal-directed envy becomes operative. Harm is attached to an activated event, not indiscriminately to the person's bare existence.","model_id":"baseline_event_gated_envy"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_event_gated_envy","source_type":"hft","support_id":"sup_06bd1370c77bf67f0f3f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ","ayah_ref":"113:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000319/B001","root_000319/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000319","role":"Supplies admiration without removal, preserving a non-harmful starting state inside the root's range.","root":"ح س د","source_ref":"113:5","source_word_indices":["3","5"]},{"branch_id":"B001","mapped_root_id":"root_000319","role":"Supplies the subtractive turn that makes the temporally activated state harmful.","root":"ح س د","source_ref":"113:5","source_word_indices":["3","5"]}],"changed_reading":{"after":"The threat may lie in a threshold where admiration ceases to coexist with the other's good and becomes removal-seeking.","before":"Any intense regard for another's good is already the condemned harm."},"confidence":"medium","focus_anchor":"The same ح س د root occupies both the agent noun and the event verb, while its inventory preserves both subtractive envy and non-subtractive admiration.","mechanism":"The doubled root can hold a live fork: attention to another's blessing need not itself seek loss, but the إِذَا event marks the possible turn from emulative admiration into a wish that the blessing disappear.","model_id":"baseline_admiration_fork"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_admiration_fork","source_type":"hft","support_id":"sup_35613bbd5efe1eed9eb1","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ","ayah_ref":"113:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000319/B001","root_000792/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000792","role":"Supplies matching and counter-equivalence as the imagined balancing operation performed by the harm.","root":"ش ر ر","source_ref":"113:5","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000319","role":"Supplies removal of the other's blessing as the destructive means used to manufacture parity.","root":"ح س د","source_ref":"113:5","source_word_indices":["3","5"]}],"changed_reading":{"after":"Envy performs a false accounting operation that tries to make unequal shares match by reducing the other.","before":"Envy is an undirected hostile feeling."},"confidence":"exploratory","focus_anchor":"شَرِّ is directly paired with the repeated ح س د construction, and the packet's split mapping for ش ر ر includes a counterpart or equivalence image.","mechanism":"Envy can be modeled as counterfeit equalization: another's blessing is perceived as an imbalance, so the envier seeks parity by subtracting from the other rather than by gaining a comparable good.","model_id":"baseline_false_parity"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_false_parity","source_type":"hft","support_id":"sup_9816952df4200296b721","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ","ayah_ref":"113:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000319/B001","root_000792/B012"],"payload":{"activation_trace":[{"branch_id":"B012","mapped_root_id":"root_000792","role":"Supplies an invocation of misfortune as a possible outward vehicle of the focus harm.","root":"ش ر ر","source_ref":"113:5","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000319","role":"Supplies the desire for loss that gives the projected ill-wishing its motive and target.","root":"ح س د","source_ref":"113:5","source_word_indices":["3","5"]}],"changed_reading":{"after":"The dangerous event may be the projection of that emotion as directed ill-wishing.","before":"The envier's danger is exhausted by an internal emotion."},"confidence":"exploratory","focus_anchor":"The focus construction joins شَرِّ to the moment at which the حَاسِد enacts حَسَدَ.","mechanism":"A non-dominant mapped branch lets the harm take the form of projected ill-wishing. The removal-directed desire is then not merely stored inwardly; at its إِذَا moment it becomes a wish or invocation of misfortune toward the blessed person.","model_id":"baseline_maledictive_projection"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_maledictive_projection","source_type":"hft","support_id":"sup_1f51e32cf1b79883ebaa","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ","ayah_ref":"113:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000319/B001","root_000787/B009","root_000792/B009"],"payload":{"activation_trace":[{"branch_id":"B009","mapped_root_id":"root_000787","role":"Supplies gnat-like harm as an image of small, repeated, distributed injury.","root":"ش ر ر","source_ref":"113:5","source_word_indices":["2"]},{"branch_id":"B009","mapped_root_id":"root_000792","role":"Supplies a skin eruption as an image of many surface irritations appearing at activation.","root":"ش ر ر","source_ref":"113:5","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000319","role":"Keeps the outlier anchored to removal-directed envy rather than free-floating bodily imagery.","root":"ح س د","source_ref":"113:5","source_word_indices":["3","5"]}],"changed_reading":{"after":"Its activation may also be imagined as many small irritations that spread across the target's social surface.","before":"The evil of envy must be one large and legible hostile blow."},"confidence":"exploratory","containment":"This is surprising because it combines a gnat-scale harm image with a dermatological branch reached through the non-dominant ش ر ي mapping. Both remain packet-backed and attach directly to focus شَرِّ, while إِذَا حَسَدَ supplies the eruption point. Render as an analogy for distributed minor harms or irritations, never as a translation, diagnosis, or medical effect of envy.","focus_anchor":"Focus شَرِّ names the harm and the repeated ح س د construction gives it a moment of activation.","outlier_id":"outlier_distributed_irritation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:outlier_distributed_irritation","source_type":"hft","support_id":"sup_86b6ecca7eb8170531c4","trust":"legacy_unbound"}]}
</lane_packet_json>
