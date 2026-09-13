# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **93:2**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s093-regular-20260912/s093/93_2/micro.discovery.json` and modify nothing
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
  "ayah_ref": "93:2",
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
{"branch_registry":[{"boundary":"Dal, örtme eylemini ya da doğuştan gelen yaradılışı değil, durulup sürme durumunu kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000679/B001","candidate_links":[{"candidate_id":"cand_e35a127336689712f902","lane":"micro"},{"candidate_id":"cand_64a8dd5977420cb118f7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَجَىٰ","morph_features":"STEM|POS:V|PERF|LEM:sajaY`|ROOT:sjw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"93:2:3:1","qac_word_ref":"93:2:3","surface_ar":"سَجَىٰ"}],"gloss":"durgunluk ve sürüp kalma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hareket diner ve ortaya çıkan durgunluk bir süre devam eder."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gece, durulup uzaması yanında kararıp çökmüş bir halde anlatılabilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Denizdeki gerçekleşme, dalgaların dinip denizin durgunlaşmasıdır."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Rüzgârdaki gerçekleşme, esişin kesilip havanın sakinleşmesidir."}},{"facet_id":"F005","role":"specialization","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Göz ve bakışta durgun, gevşek ve süzgün bir görünüşü belirtir."}}],"root_ar":"س ج و","root_id":"root_000679","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hareketin dinmesiyle bu durumun devam etmesini birleştiren genel çekirdeği için kullanılır.","boundary_detail":"Dal, örtme eylemini ya da doğuştan gelen yaradılışı değil, durulup sürme durumunu kapsar.","branch_image_ar":"السكون والركود مع إطباق الليل أو البحر أو الطرف","concept_gloss":"durgunluk ve sürüp kalma","contextual_glosses":[{"applicability":"Gecenin sakinleşerek uzadığı ve bağlama göre karanlığın yerleştiği anlatımlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Deniz, rüzgâr ve bakışta gerçekleşen öteki durgunluk türlerini dışarıda bırakır.","preserves":"Geceye özgü durulma, sürme ve çökme görünümünü korur."},"facet_ids":["F001","F002"],"text":"gecenin durulup çökmesi","usage_role":"contextual"},{"applicability":"Deniz dalgalarının yatışıp su yüzeyinin durgunlaştığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gece, rüzgâr ve bakışla ilgili gerçekleşmeleri kapsamaz.","preserves":"Denize özgü hareketten durgunluğa geçişi korur."},"facet_ids":["F001","F003"],"text":"denizin dalgalarının dinmesi","usage_role":"contextual"},{"applicability":"Rüzgârın esmeyi bırakıp havanın sakinleştiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gece, deniz ve bakışla ilgili gerçekleşmeleri kapsamaz.","preserves":"Rüzgârdaki hareketin kesilmesini açık biçimde korur."},"facet_ids":["F001","F004"],"text":"rüzgârın dinmesi","usage_role":"contextual"},{"applicability":"Gözün bakışındaki gevşek, sakin ve güzel sayılan görünüş anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gece, deniz ve rüzgârla ilgili durulma biçimlerini kapsamaz.","preserves":"Bakışa özgü durgunluk ve gevşeklik görünümünü korur."},"facet_ids":["F001","F005"],"text":"bakışın durgun ve süzgün olması","usage_role":"contextual"}],"definition":"Hareketin dinmesi ve oluşan durgun durumun sürmesidir; gece söz konusu olduğunda buna karanlığın çöküp yerleşmesi de eşlik edebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hareket diner ve ortaya çıkan durgunluk bir süre devam eder."},{"facet_id":"F002","role":"specialization","statement":"Gece, durulup uzaması yanında kararıp çökmüş bir halde anlatılabilir."},{"facet_id":"F003","role":"specialization","statement":"Denizdeki gerçekleşme, dalgaların dinip denizin durgunlaşmasıdır."},{"facet_id":"F004","role":"specialization","statement":"Rüzgârdaki gerçekleşme, esişin kesilip havanın sakinleşmesidir."},{"facet_id":"F005","role":"specialization","statement":"Göz ve bakışta durgun, gevşek ve süzgün bir görünüşü belirtir."}],"identity_rationale":"Kaynak sözü, anlam çekirdeğini hareketin dinmesi ve ortaya çıkan durumun sürmesi olarak verir. Gece, deniz, rüzgâr ve bakışla ilgili kullanımlar bu çekirdeğin ayrı gerçekleşmeleridir; gecenin kararması ise yalnız gece bağlamına bağlı bir özelliktir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"durgunluk"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"durulmak ve öyle kalmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"gecenin durulup çökmesi"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"durgun ve karanlık gece"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"rüzgârsız, sakin gece"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"denizin dalgalarının dinmesi"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"durgun deniz"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"durgun ve süzgün bakışlı göz"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"durgun ve gevşek bakış"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"rüzgârın dinmesi"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"sağılırken sakin duran dişi deve"}],"lexicalization_note":"Çıplak biçimdeki durgunluk çekirdeği ile gece, deniz, rüzgâr ve bakışa bağlı kullanımlar ayrı tutulur; özel kullanımlar bütün dala genellenmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yayımlanan üç komşu durgunluk, bakış ve gece karanlığı sınırlarını en açık biçimde gösteriyor, kalanlar yalnız uzak konu ortaklığı taşıyor ya da aynı ayrımları yineliyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal durgunluk çekirdeğini gece, deniz, rüzgâr ve bakışta ayrı ayrı gerçekleştirir. Komşu dal ise hareketten sonra durulma ile suyun bulunduğu yerde kalmasını daha belirgin bir sınır olarak taşır.","focus_only":"Gece, deniz, rüzgâr ve bakış gibi özel gerçekleşmeleri de kapsar.","gloss":"durulup sürme","neighbor_only":"Hareket sonrasındaki durulmayı ve suyun yerinde kalmasını özellikle belirtir.","neighbor_ref":"root_001568/B009","relation_type":"near_synonym","shared_zone":"Her iki dal da hareketin kesilmesini ve durgun durumun devamını anlatır."},{"boundary_match":"partial","distinction":"Odak dal bakışın gevşek ve durgun niteliğini anlatır; komşu dal ise gözleri açıp bakışı kesmeden yöneltme eylemini öne çıkarır. Bu nedenle sıradan kullanımda birbirlerinin yerine geçmezler.","focus_only":"Bakışın gevşek, durgun ve süzgün görünüşünü belirtir.","gloss":"durgun bakış","neighbor_only":"Gözleri açarak bakışı belirli bir noktada sürdürmeyi belirtir.","neighbor_ref":"root_000111/B001","relation_type":"near_neighbor","shared_zone":"İki dal da gözün sakin ve süreklilik gösteren bakışıyla ilişkilidir."},{"boundary_match":"field_only","distinction":"Odak dalın çekirdeği karanlık değil, durgunluk ve sürmedir; kararma geceye bağlı bir eşlikçidir. Komşu dalın çekirdeği ise siyahlık ve koyu renktir.","focus_only":"Gecenin kararmasını ancak durulup çökme durumuna bağlı olarak içerir.","gloss":"gecenin kararıp durulması","neighbor_only":"Koyu siyahlığı ve siyaha çalan renkleri hareketten bağımsız olarak kapsar.","neighbor_ref":"root_000496/B001","relation_type":"same_field","shared_zone":"Her iki dal gece karanlığının görünüşünde buluşabilir."}],"source_phrase_ar":"أصل يدل على سكون وإطباق (maqayis)؛ السجو السكون (ayn)؛ سجا الليل وغيره إذا سكن (jamhara)؛ سكن ودام (sihah)؛ إذا أظلم وركد، ومعنى ركد سكن (tahdhib)؛ أي سكن (mufradat)","source_summary":"Kaynakların ortak çizgisi durgunluk ve bu durumun sürmesidir. Gece, deniz, rüzgâr ve bakış örnekleri aynı çekirdeği kendi alanlarında gerçekleştirir; karanlık yalnız gece kullanımında öne çıkar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه سكون الليل وركوده أو إظلامه ودوامه، وسكون البحر وأمواجه، وسكون الريح، وفتور الطرف وسكونه.","what_is_not_ar":"لا يدخل فيه مجرد تغطية الميت بالثوب إلا من جهة استعارة أو صلة بالسكون، ولا الخلق والطبيعة."},"support_links":["sup_221d06da391bc93e8285","sup_55f6f5748467aa2aad0d"]},{"boundary":"Dalın kavram çekirdeği ölünün üstüne örtü sermektir; genel örtme ve gecenin kaplaması yalnız ayrı söz birimi karşılıklarında kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000679/B002","candidate_links":[{"candidate_id":"cand_b8e5e1b9c8988e10ffef","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَجَىٰ","morph_features":"STEM|POS:V|PERF|LEM:sajaY`|ROOT:sjw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"93:2:3:1","qac_word_ref":"93:2:3","surface_ar":"سَجَىٰ"}],"gloss":"ölünün üstünü örtüyle kapatma","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir örtü ölünün üzerine uzatılır ve bedeni bu örtüyle kapatılır."}}],"root_ar":"س ج و","root_id":"root_000679","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın ölünün üzerine örtü serilmesini ve bedenin bununla kapatılmasını birleştiren tam karşılığıdır.","boundary_detail":"Dalın kavram çekirdeği ölünün üstüne örtü sermektir; genel örtme ve gecenin kaplaması yalnız ayrı söz birimi karşılıklarında kalır.","branch_image_ar":"التسجية والتغطية بالثوب","concept_gloss":"ölünün üstünü örtüyle kapatma","contextual_glosses":[{"applicability":"Eylemin bir cümle içinde doğal fiil karşılığı gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Örtünün ölünün üzerine serilip bedeni kapatmasını eksiksiz korur."},"facet_ids":["F001"],"text":"ölünün üzerine örtü sermek","usage_role":"contextual"}],"definition":"Ölünün üstüne bir örtü sererek bedenini kapatmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir örtü ölünün üzerine uzatılır ve bedeni bu örtüyle kapatılır."}],"identity_rationale":"Yetkili dal sözü yalnız ölünün üzerine bir örtü sererek onu kapatmayı açıkça tanımlar. Genel olarak herhangi bir şeyi örtme ve gecenin gündüzü kaplaması ayrı söz birimlerinde bulunsa da dal iddiasının kapsamını genişletemez; bu nedenle dal tanımı ölünün örtülmesiyle sınırlandırılmıştır.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ölünün üstünü bir örtüyle kapatma"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bir şeyin üstünü örtmek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"gecenin gündüzü kaplaması"}],"lexicalization_note":"Dizelge hem genel bir söz birimi hem de bağlı kullanımlar gösterir; buna karşın dal tanımı, kanıtlanan ölüyü örtme yapısıyla sınırlıdır ve öteki birimler ayrı çevrilir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler örtme eylemini gömme, örtüye sarınma ve örtünün kendisinden ayırıyor, öteki adaylar bu sınırları daha az doğrudan gösteriyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnız örtünün beden üzerine serilmesi işlemidir. Komşu dal ölünün gizlenmesi veya gömülmesi yanında mezar ve kefen gibi sonuç ya da araçları da kapsar.","focus_only":"Ölünün üzerine bir örtü sererek bedeni kapatma eylemini belirtir.","gloss":"ölüyü örtme","neighbor_only":"Ölüyü gizleme, gömme, mezar ve kefen alanlarını da kapsar.","neighbor_ref":"root_000266/B009","relation_type":"near_neighbor","shared_zone":"İki dal da ölünün bedenini görünmez kılma alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dalda başkası üzerindeki örtme işlemi, özellikle ölünün kapatılması esastır. Komşu dalda ise kişinin örtüye sarınması veya onu kuşanması öne çıkar.","focus_only":"Örtüyü ölünün bedeni üzerine sermeye bağlıdır.","gloss":"örtüyle kaplama","neighbor_only":"Bir kişinin kumaşa sarınmasını ve örtüyü giyer gibi kuşanmasını kapsar.","neighbor_ref":"root_000819/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda kumaş türü bir örtünün bedeni kaplaması vardır."},{"boundary_match":"field_only","distinction":"Odak dal bir bedeni örtüyle kapatma işlemidir; komşu dal ise bu işte kullanılabilen kumaş parçasının adıdır. Eylem ile araç birbirinin yerine kullanılamaz.","focus_only":"Bir örtüyü ölünün üzerine serme eylemini bildirir.","gloss":"örtme ve örtü","neighbor_only":"Örtmeye yarayan kumaş parçasının kendisini bildirir.","neighbor_ref":"root_000230/B004","relation_type":"same_field","shared_zone":"İki dal örtme işinde kullanılan kumaş çevresinde birleşir."}],"source_phrase_ar":"تسجية الميت تغطيته بثوب (ayn)؛ سجيت الميت تسجية إذا مددت عليه ثوبا (sihah)؛ يسجى الميت بثوب أي يغطى به (tahdhib)؛ تسجية الميت أي تغطيته بالثوب (mufradat)","source_summary":"Kaynaklar aynı işlemi, ölünün üzerine bir örtü uzatıp bedeni onunla kapatma olarak verir.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه تسجية الميت ومد الثوب عليه، وكل استعمال صريح في تغطية شيء أو إلباسه بالثوب.","what_is_not_ar":"لا يدخل فيه السكون المجرد أو دوام الليل إلا إذا صرح المصدر بالتغطية، ولا يدخل فيه الخلق والطبيعة."},"support_links":["sup_7dd937c398797fb4eee5"]},{"boundary":"Dal, birinin doğuştan getirdiği yerleşik yaradılışı anlatır; geçici bir davranışı veya fiziksel durgunluğu anlatmaz.","branch_kind":"bare","branch_ref":"root_000679/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَجَىٰ","morph_features":"STEM|POS:V|PERF|LEM:sajaY`|ROOT:sjw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"93:2:3:1","qac_word_ref":"93:2:3","surface_ar":"سَجَىٰ"}],"gloss":"doğuştan gelen huy ve yaradılış","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nitelik sonradan edinilmiş geçici bir davranış değil, kişide yerleşik bulunan yaradılıştır."}}],"root_ar":"س ج و","root_id":"root_000679","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin sonradan edinilmeyen, yerleşik yaradılışını bir bütün olarak anlatmak için kullanılır.","boundary_detail":"Dal, birinin doğuştan getirdiği yerleşik yaradılışı anlatır; geçici bir davranışı veya fiziksel durgunluğu anlatmaz.","branch_image_ar":"السجية والخلقة والطبيعة","concept_gloss":"doğuştan gelen huy ve yaradılış","contextual_glosses":[{"applicability":"Bir kişinin değişken davranışından değil, yerleşik yaradılışından söz edildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Huyun doğuştan ve yaradılışa bağlı oluşunu korur."},"facet_ids":["F001"],"text":"yaradılıştan gelen huy","usage_role":"general"}],"definition":"Bir kişide doğuştan bulunan, yerleşik huy ve yaradılıştır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nitelik sonradan edinilmiş geçici bir davranış değil, kişide yerleşik bulunan yaradılıştır."}],"identity_rationale":"Yetkili söz, dalı doğrudan yaradılış ve doğuştan gelen huy olarak tanımlar. Bu çerçeve, geçici dal açıklamasıyla uyumludur ve durgunluk ya da örtme anlamlarından bağımsız bir insan niteliği oluşturur.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"doğuştan gelen huy ve yaradılış"}],"lexicalization_note":"Dal çıplak biçimde yerleşik yaradılışı belirtir; başka dallardaki bağlı kullanımlar bu tanıma katılmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yayımlanan iki ayrım, tam örtüşmeye yaklaşan yaradılış anlamını yöntem ve davranış çizgisine genişleyen komşudan ayırıyor, kalan adaylar bu karşıtlığı yineliyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"İnsan huyu söz konusu olduğunda çekirdekler büyük ölçüde örtüşür. Komşu dal kapsamını insan dışındaki varlıkların yaratılışına ve birden çok yaradılış türüne açıkça genişletir.","focus_only":null,"gloss":"yerleşik yaradılış","neighbor_only":"İnsan yanında başka varlıkların yaratılış biçimini ve farklı yaradılış türlerini de açıkça kapsar.","neighbor_ref":"root_000926/B002","relation_type":"near_synonym","shared_zone":"Her iki dal doğuştan gelen huyu ve yaratılıştan yerleşmiş niteliği anlatır."},{"boundary_match":"partial","distinction":"Odak dal kişinin doğuştan gelen yaradılışıdır. Komşu dal aynı alana yaklaşsa da yön, yöntem ve kişinin buna göre davranma biçimini de içerdiğinden doğrudan eş anlamlı değildir.","focus_only":"Doğuştan gelen huy ve yaradılış çekirdeğiyle sınırlıdır.","gloss":"huy ve izlenen yol","neighbor_only":"Yol, yön, tutulan yöntem ve kişinin eylem biçimini de kapsar.","neighbor_ref":"root_000813/B002","relation_type":"near_neighbor","shared_zone":"İki dal kişinin yerleşik niteliği ile davranış çizgisinin kesiştiği alanda buluşur."}],"source_phrase_ar":"السجية الخلق والطبيعة (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Anlam, tek tanıklıkta doğuştan gelen huy ve yaradılış olarak kaydedilmiştir."}],"source_summary":"Dalın tek kaynaklı tanımı, anlamı doğuştan gelen yerleşik huy ve yaradılışla sınırlar.","sources":["SI"],"what_is_ar":"يدخل فيه السجية بمعنى الخلق والطبيعة.","what_is_not_ar":"لا يدخل فيه سكون الليل والبحر والطرف، ولا تسجية الميت."},"support_links":[]},{"boundary":"Dal, genel kaçınma veya her türlü dokunmama değil, bir yemeğe el sürülmediğini söyleyen kalıptır.","branch_kind":"collocation","branch_ref":"root_000679/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَجَىٰ","morph_features":"STEM|POS:V|PERF|LEM:sajaY`|ROOT:sjw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"93:2:3:1","qac_word_ref":"93:2:3","surface_ar":"سَجَىٰ"}],"gloss":"yemeğe el sürmeme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Olumsuz yapı, sunulan yemeğe dokunulmadığını bildirir."}}],"root_ar":"س ج و","root_id":"root_000679","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sunulan bir yemeğe hiç dokunulmadığını bildiren bağlı ve olumsuz kullanım için geçerlidir.","boundary_detail":"Dal, genel kaçınma veya her türlü dokunmama değil, bir yemeğe el sürülmediğini söyleyen kalıptır.","branch_image_ar":"ترك المس والمساس","concept_gloss":"yemeğe el sürmeme","contextual_glosses":[{"applicability":"Getirilen yemeğin yenmediğini veya ona dokunulmadığını cümle içinde söylemek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Konuşan çoğulu, yemek bağlamını ve hiç temas edilmediğini korur."},"facet_ids":["F001"],"text":"yemeğe hiç el sürmedik","usage_role":"contextual"}],"definition":"Getirilen bir yemeğe hiç el sürülmediğini bildiren olumsuz anlatımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Olumsuz yapı, sunulan yemeğe dokunulmadığını bildirir."}],"identity_rationale":"Yetkili söz genel bir dokunmama anlamı değil, getirilen yemeğe el sürülmediğini bildiren olumsuz bir kalıp verir. Dal korunabilir, ancak tanımı bu yemek bağlamına ve olumsuz yapıya bağlamak gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"ona hiç el sürmedik"}],"lexicalization_note":"Anlam yalnız verilen olumsuz yemek yapısında tanımlanır; çıplak köke genel bir dokunmama anlamı yüklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen komşu temasın yokluğu ile amaçlı hafif dokunma arasındaki en açık karşıtlığı kuruyor, kalan adaylar genel kaçınma alanında daha dolaylı kalıyor.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal bağlı bir yemek anlatımında temasın olmadığını söyler. Komşu dal ise bilgi edinmek amacıyla hafif ve etkin bir dokunmayı anlatır; bu nedenle aynı temas ekseninin karşıt kutuplarındadırlar.","focus_only":"Yemek bağlamında temasın hiç gerçekleşmediğini bildirir.","gloss":"el sürmeme ve elle yoklama","neighbor_only":"Bir şeyi tanımak veya sınamak için elle hafifçe yoklamayı bildirir.","neighbor_ref":"root_000246/B001","relation_type":"polarity_pair","shared_zone":"İki dal fiziksel temasın varlığı ile yokluğu ekseninde karşılaşır."}],"source_phrase_ar":"أتانا بطعام فما ساجيناه أي ما مسسناه (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Kullanım, sunulan yemeğe hiç dokunulmadığını bildiren tek bir örnekle tanıklanmıştır."}],"source_summary":"Tek tanıklık, getirilen yemeğe el sürülmediğini bildiren olumsuz bir kullanım kaydeder.","sources":["TA"],"what_is_ar":"يدخل فيه قولهم ما ساجيناه في الطعام، أي ما مسسناه.","what_is_not_ar":"لا يدخل فيه السكون ولا التغطية ولا معالجة الضيعة."},"support_links":[]},{"boundary":"Dal, herhangi bir işle uğraşmayı değil, belirli bir toprak işletmesinin işlerini yürütmeyi anlatan yapıyla sınırlıdır.","branch_kind":"collocation","branch_ref":"root_000679/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَجَىٰ","morph_features":"STEM|POS:V|PERF|LEM:sajaY`|ROOT:sjw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"93:2:3:1","qac_word_ref":"93:2:3","surface_ar":"سَجَىٰ"}],"gloss":"toprak işletmesinin işlerini yürütme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bir toprak işletmesinin işlerini üstlenir ve düzenli biçimde yürütür."}}],"root_ar":"س ج و","root_id":"root_000679","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir toprak işletmesini ele alıp günlük işlerini üstlenme anlamındaki bağlı kullanım için geçerlidir.","boundary_detail":"Dal, herhangi bir işle uğraşmayı değil, belirli bir toprak işletmesinin işlerini yürütmeyi anlatan yapıyla sınırlıdır.","branch_image_ar":"مباشرة الضيعة ومعالجتها","concept_gloss":"toprak işletmesinin işlerini yürütme","contextual_glosses":[{"applicability":"Eylemin cümle içinde, işletmenin işlerini ele alma anlamıyla karşılanması gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli işletmeyi, sorumluluk almayı ve işlerin yürütülmesini korur."},"facet_ids":["F001"],"text":"toprak işletmesinin işlerini üstlenmek","usage_role":"contextual"}],"definition":"Bir toprak işletmesiyle ilgilenip onun işlerini üstlenerek yürütmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bir toprak işletmesinin işlerini üstlenir ve düzenli biçimde yürütür."}],"identity_rationale":"Yetkili söz, belirli bir toprak işletmesiyle ilgilenip onun işlerini yürütmeyi açıkça bildirir. Geçici dal çerçevesi bu bağlı kullanımı doğru yansıtır ve onu genel uğraşma anlamına genişletmeden korumaya elverişlidir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bir toprak işletmesinin işlerini yürütmek"}],"lexicalization_note":"Anlam yalnız toprak işletmesini nesne alan yapıda geçerlidir; çıplak biçime genel yönetme veya uğraşma anlamı taşınmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; seçilenler bağlı işletme yönetimini genel uğraşma, geniş bakım ve yöneticinin niteliğinden ayırıyor, öteki adaylar daha uzak koruma ya da tarım ortaklığı taşıyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın nesnesi ve kullanım yapısı bir toprak işletmesiyle sınırlıdır. Komşu dal ise nesne bakımından geneldir ve deneme, çabalama ya da çekişme gibi ek yönlere açılır.","focus_only":"Bir toprak işletmesinin işlerini yürütmeye bağlıdır.","gloss":"işletmeyle ilgilenme","neighbor_only":"Herhangi bir şeyi denemeyi, onunla uğraşmayı ve birine karşı çekişmeyi de kapsar.","neighbor_ref":"root_000655/B003","relation_type":"near_synonym","shared_zone":"Her iki dal bir işi ele alıp onunla etkin biçimde uğraşmayı anlatır."},{"boundary_match":"partial","distinction":"Odak dal toprak işletmesinin işlerini yürütme eylemidir. Komşu dal ise bir şeyi düzeltip geliştirmeyi ve aşamalı bakımını da içerdiği için daha geniştir.","focus_only":"Belirli bir toprak işletmesinin işlerini üstlenip yürütmeye bağlıdır.","gloss":"işleri yürütme ve bakım","neighbor_only":"Düzeltme, yetiştirme, tamamlama ve çocukla ilgilenme gibi daha geniş bakım sonuçlarını kapsar.","neighbor_ref":"root_000532/B002","relation_type":"near_synonym","shared_zone":"İki dal bir şeyin sorumluluğunu alıp işleriyle ilgilenme alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal yapılan işi, komşu dal ise bu işi iyi yapabilen kişinin bilgi ve yeterliğini öne çıkarır. Eylem ile kişisel nitelik bu nedenle yer değiştiremez.","focus_only":"İşletmenin işlerini yürütme eylemini doğrudan bildirir.","gloss":"işletme yönetimi","neighbor_only":"Mal veya deve bakımında bilgili ve iyi oluşu kişiye ait bir nitelik olarak bildirir.","neighbor_ref":"root_000853/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal mal varlığıyla ilgilenme ve onu iyi yürütme alanındadır."}],"source_phrase_ar":"هل نساجي ضيعة أي هل نعالجها (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Bağlı kullanım, bir toprak işletmesiyle ilgilenip işlerini yürütme anlamıyla tek başına tanıklanmıştır."}],"source_summary":"Tek tanıklık, bir toprak işletmesinin işlerini ele alıp yürütmeye ilişkin bağlı bir kullanım verir.","sources":["TA"],"what_is_ar":"يدخل فيه قولهم هل نساجي ضيعة، أي هل نعالجها ونباشر أمرها.","what_is_not_ar":"لا يدخل فيه ترك المس، ولا سكون الليل والبحر، ولا التغطية بالثوب."},"support_links":[]},{"boundary":"Devenin süt bolluğu açıktır; kuyu kullanımında bolluğun neye ait olduğu açıklanmadığından su bolluğu kesin anlam diye yazılamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000679/B006","candidate_links":[{"candidate_id":"cand_223098e4216d5e23bca1","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَجَىٰ","morph_features":"STEM|POS:V|PERF|LEM:sajaY`|ROOT:sjw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"93:2:3:1","qac_word_ref":"93:2:3","surface_ar":"سَجَىٰ"}],"gloss":"devenin sütünün bol gelmesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişi deve, sütünün bol gelmesiyle nitelenir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı biçim kuyu için de kullanılır, fakat kuyuyla ilgili bolluğun nesnesi belirtilmez."}}],"root_ar":"س ج و","root_id":"root_000679","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın açıkça tanımlanan deve ve süt çekirdeği için kullanılır; kuyu çeşitlemesini tek başına karşılamaz.","boundary_detail":"Devenin süt bolluğu açıktır; kuyu kullanımında bolluğun neye ait olduğu açıklanmadığından su bolluğu kesin anlam diye yazılamaz.","branch_image_ar":"الإسجاء في غزارة اللبن أو ماء البئر","concept_gloss":"devenin sütünün bol gelmesi","contextual_glosses":[{"applicability":"Dişi devenin süt veriminin bol hale geldiği cümlelerde doğal fiil karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kuyuya bağlanan belirsiz kaynak çeşitlemesini kapsamaz.","preserves":"Sütün azlıktan bolluğa geçmesi anlamını korur."},"facet_ids":["F001"],"text":"sütü bollaşmak","usage_role":"contextual"},{"applicability":"Yalnız kuyuya bağlanan kullanım açıklanırken ve neyin bollaştığının belirtilmediği açıkça korunurken kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Devenin süt bolluğunu ve bu anlamın açık nesnesini dışarıda bırakır.","preserves":"Kuyuya bağlı bolluk yönünü ve anlatımdaki belirsizliği korur."},"facet_ids":["F002"],"text":"kuyunun bol hale gelmesi","usage_role":"explanatory"}],"definition":"Dişi devenin sütünün bol gelmesidir; aynı kaynakta kuyuya bağlanan kullanım da vardır, ancak kuyuda neyin bol olduğu ayrıca açıklanmaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dişi deve, sütünün bol gelmesiyle nitelenir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı biçim kuyu için de kullanılır, fakat kuyuyla ilgili bolluğun nesnesi belirtilmez."}],"identity_rationale":"Yetkili söz, dişi devenin sütünün bol gelmesini açıkça belirtir ve kuyu kullanımını aynı cümlede buna bağlar. Ancak kuyuda neyin bollaştığını tek başına açıklamaz; bu yüzden dal korunurken açık süt bolluğu çekirdek, kuyu ise nesnesi belirtilmemiş kaynak çeşitlemesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"devenin sütünün bollaşması"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"kuyunun bol hale gelmesi; neyin bol olduğu belirtilmemiştir"}],"lexicalization_note":"Deveye bağlı açık kullanım ile açıklama bekleyen kuyu biçimi ayrı tutulur; ikisinden çıplak köke genel bir bolluk anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen iki komşu açık süt bolluğu yakınlığını ve kuyu kullanımındaki belirsizliği gösteriyor, kalan bolluk adayları aynı sınırları daha geniş alanlarda yineliyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Deve sütü bakımından anlamlar çok yakındır. Odak dal süt bolluğuna giren bir durumu ve belirsiz kuyu çeşitlemesini taşırken komşu dal bol sütlü deve niteliğini ve karşılaştırmalı üretkenliği de kapsar.","focus_only":"Kuyuya bağlanan fakat tam kapsamı açıklanmayan bir kullanım da taşır.","gloss":"devede süt bolluğu","neighbor_only":"Sütü bol olan deve türünü ve başka develerin sütünü artıran karşılaştırmalı niteliği de belirtir.","neighbor_ref":"root_000200/B005","relation_type":"near_synonym","shared_zone":"Her iki dal dişi devenin bol süt vermesini doğrudan anlatır."},{"boundary_match":"field_only","distinction":"Odak dalın kuyu kullanımında neyin bol olduğu kaynakça açıklanmamıştır; bu nedenle onu doğrudan su bolluğu saymak doğru olmaz. Komşu dal ise kuyudaki çok suyu açıkça bildirir.","focus_only":"Devenin süt bolluğunu açıkça, kuyu kullanımını ise nesnesi belirsiz biçimde bildirir.","gloss":"kuyuda bolluk","neighbor_only":"Deniz veya kuyuda birikmiş çok miktarda suyu açıkça adlandırır.","neighbor_ref":"root_001040/B005","relation_type":"same_field","shared_zone":"İki dal kuyu ve bolluk alanında yan yana gelir."}],"source_phrase_ar":"ما كانت البئر سجوا ولقد أسجت، وكذلك الناقة أسجت في الغزارة في اللبن (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kayıt, deve sütü bolluğunu açıklar; kuyuya uygulanan aynı biçimin tam kapsamını ise açık bırakır."}],"source_summary":"Tek tanıklık deve sütündeki bolluğu açıkça verir ve kuyu kullanımını buna koşut biçimde anar; kuyudaki bolluğun nesnesini ayrıca tanımlamaz.","sources":["TA"],"what_is_ar":"يدخل فيه إسجاء الناقة في غزارة اللبن، وما ألحق به المصدر من البئر في السياق نفسه.","what_is_not_ar":"لا يدخل فيه سكون الناقة عند الحلب، ولا سكون البحر أو الليل، ولا التغطية."},"support_links":["sup_3bf2e63fcd048469d7c2"]},{"boundary":"Dal genel gece zamanını ve karanlığını kapsar; şiddet, uzunluk ve ayın son gecesi anlamları yalnız ilgili söz öbeklerine bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001392/B001","candidate_links":[{"candidate_id":"cand_e35a127336689712f902","lane":"micro"},{"candidate_id":"cand_b8e5e1b9c8988e10ffef","lane":"micro"},{"candidate_id":"cand_223098e4216d5e23bca1","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"93:2:1:3","qac_word_ref":"93:2:1","surface_ar":"يْلِ"}],"gloss":"gündüzün karşıtı olan gece ve onun karanlığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gündüzün karşıtı olan zaman bölümü gecedir; tek bir gece veya birden çok gece olarak sayılabilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gece adı, bu zaman bölümüne özgü karanlığı da anlatabilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli niteleme kalıpları çok karanlık veya çetin bir geceyi anlatır."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir başka pekiştirme kalıbı gecenin uzunluğunu veya şiddetini özellikle öne çıkarır."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Özel bir söz öbeği, ayın hem en karanlık hem de son gecesini belirtir."}}],"root_ar":"ل ي ل","root_id":"root_001392","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel gece zamanını ve bu zamana bağlı karanlık anlamını birlikte temsil eder; özel nitelemeler ayrıca bağlama göre çevrilir.","boundary_detail":"Dal genel gece zamanını ve karanlığını kapsar; şiddet, uzunluk ve ayın son gecesi anlamları yalnız ilgili söz öbeklerine bağlıdır.","branch_image_ar":"الليل خلاف النهار وظلمته","concept_gloss":"gündüzün karşıtı olan gece ve onun karanlığı","contextual_glosses":[{"applicability":"Zaman bölümünden çok o zamandaki karanlığın anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geceye özgü karanlık görünümünü doğrudan korur."},"facet_ids":["F002"],"text":"gece karanlığı","usage_role":"contextual"},{"applicability":"Yalnız karanlığın şiddetini veya gecenin çetinliğini pekiştiren söz öbeklerinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gecenin yoğun karanlığını ve çetinlik vurgusunu korur."},"facet_ids":["F003"],"text":"çok karanlık ve çetin gece","usage_role":"contextual"},{"applicability":"Uzunluk ile genel şiddet arasında değişebilen özel pekiştirme kalıbını açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kalıbın uzunluk ve pekiştirilmiş şiddet seçeneklerini birlikte korur."},"facet_ids":["F004"],"text":"uzun ya da şiddeti pekiştirilmiş gece","usage_role":"explanatory"},{"applicability":"Yalnız ay içindeki özel konumu ve olağanüstü karanlığı birlikte belirten söz öbeğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ayın son gecesi olma koşulunu ve en yoğun karanlığı korur."},"facet_ids":["F005"],"text":"ayın en karanlık ve son gecesi","usage_role":"contextual"}],"definition":"Gündüzün karşıtı olan gece zamanı ve bu zamana özgü karanlıktır. Belirli söz öbekleri, temel anlamı değiştirmeden gecenin çok karanlık, çetin ya da uzun oluşunu veya ayın en karanlık son gecesini belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gündüzün karşıtı olan zaman bölümü gecedir; tek bir gece veya birden çok gece olarak sayılabilir."},{"facet_id":"F002","role":"extension","statement":"Gece adı, bu zaman bölümüne özgü karanlığı da anlatabilir."},{"facet_id":"F003","role":"specialization","statement":"Belirli niteleme kalıpları çok karanlık veya çetin bir geceyi anlatır."},{"facet_id":"F004","role":"specialization","statement":"Bir başka pekiştirme kalıbı gecenin uzunluğunu veya şiddetini özellikle öne çıkarır."},{"facet_id":"F005","role":"source_variant","statement":"Özel bir söz öbeği, ayın hem en karanlık hem de son gecesini belirtir."}],"identity_rationale":"Kaynak ifadesi, gündüzün karşıtı olan gece zamanını ve gece karanlığını açıkça temel anlam olarak verir; tekil ve çoğul biçimlerin yanında karanlığın şiddetini, gecenin uzunluğunu veya belirli bir ay gecesini anlatan kalıpları da ayrıca tanıklar. Bu nedenle dal kimliği korunabilir, ancak kalıba bağlı nitelemeler temel gece anlamıyla bir tutulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"gündüzün karşıtı olan gece"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"gece karanlığı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"tek bir gece"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"geceler"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"geceler"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"geceler"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"çok karanlık ve çetin gece"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"çok karanlık gece"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"uzun ya da şiddeti pekiştirilmiş gece"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"ayın en karanlık ve son gecesi"}],"lexicalization_note":"Dal hem genel gece adını hem de yalnız belirli söz öbeklerinde ortaya çıkan karanlık, zorluk, uzunluk ve ay sonu nitelemelerini içerir; tanım bu iki düzeyi ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel gece, geceleyin eylem, bugüne bağlı gece, yoğunlaşan karanlık ve adlandırma arasındaki sınırı en açık gösteren dört komşu seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal gecenin kendisini ve karanlığını gösterir; komşu dal ise geceyi bir eylemin gerçekleşme zamanı veya yönü olarak kodlar.","focus_only":"Geceyi bir zaman bölümü ve karanlık olarak adlandırır.","gloss":"gece ile geceleyin yapılan iş arasındaki ayrım","neighbor_only":"Geceye girme, geceleyin işlem yapma veya gece yol alma eylemlerini anlatır.","neighbor_ref":"root_001392/B002","relation_type":"same_field","shared_zone":"Her iki dal da geceyi zaman bakımından ortak eksen olarak kullanır."},{"boundary_match":"partial","distinction":"Bu dalda bugüne göre yakınlık zorunlu değildir; komşu dalın anlamı konuşma gününe ve gün içindeki söyleme anına bağlı bir gece seçimi gerektirir.","focus_only":"Herhangi bir geceyi genel zaman türü olarak kapsar.","gloss":"genel gece ile bugüne bağlı gece arasındaki ayrım","neighbor_only":"Konuşma gününe göre en yakın, geçen veya girilecek geceyi seçer.","neighbor_ref":"root_001392/B003","relation_type":"near_neighbor","shared_zone":"İki dal da gece zamanını gösterir ve belirli bağlamlarda aynı zaman dilimine işaret edebilir."},{"boundary_match":"partial","distinction":"Bu dal geceyi veya mevcut karanlığını adlandırabilir; komşu dal ise karanlığın şiddetlenmesi durumunu öne çıkarır ve genel gece adı yerine geçmez.","focus_only":"Gece zamanını, karanlığını ve bazı kalıplarda yoğun karanlık niteliğini kapsar.","gloss":"gece karanlığı ile karanlığın şiddetlenmesi arasındaki ayrım","neighbor_only":"Gecenin giderek koyulaşmasını veya karanlığının şiddetlenmesini merkez alır.","neighbor_ref":"root_001015/B004","relation_type":"near_neighbor","shared_zone":"Her ikisi de gecenin yoğun karanlığını anlatan bağlamlarda buluşur."},{"boundary_match":"thematic_only","distinction":"Bu dalın çekirdeği bir zaman bölümü ve karanlıktır; komşu dalda biçim bir kişiyi adlandırır veya daha geniş bir söz öbeği içinde şarabı örtülü biçimde anar.","focus_only":"Gece zamanını ve onun karanlığını anlatır.","gloss":"gece anlamı ile adlandırma kullanımı arasındaki ayrım","neighbor_only":"Bir kadın adını ve ayrı bir söz öbeğinde şarabın örtülü adını anlatır.","neighbor_ref":"root_001392/B004","relation_type":"thematic","shared_zone":"Dallar aynı biçim ailesiyle bağlantılıdır, fakat kavramsal alanları örtüşmez."}],"source_phrase_ar":"الليل خلاف النهار (maqayis)؛ الليل ضد النهار (jamhara;tahdhib)؛ ظلام الليل (tahdhib)؛ ليل وليلة وليلات وليال (maqayis;sihah;mufradat)؛ ليل أليل وليلة ليلاء وليل لائل (jamhara;sihah;tahdhib;mufradat)؛ ليلة ليلى أشد ليلة في الشهر ظلمة وآخر ليلة فيه (jamhara)","source_summary":"Kaynakların ortak çekirdeği geceyi gündüzün karşıtı bir zaman ve ona bağlı karanlık olarak tanımlar. Toplu kanıt ayrıca tek ve çok gece biçimlerini, karanlığı ya da uzunluğu pekiştiren kullanımları ve ayın en karanlık son gecesine özgü ifadeyi birlikte gösterir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الليل والليلة والليالي، وضده النهار، وظلام الليل وشدته وطوله في نحو ليلة ليلاء وليل أليل وليل لائل وليلة ليلى","what_is_not_ar":"لا يدخل فيه النهار ولا اليوم إلا من جهة المقابلة، ولا التسمية بليلى، ولا ولد الطائر المختلف فيه"},"support_links":["sup_221d06da391bc93e8285","sup_3bf2e63fcd048469d7c2","sup_7dd937c398797fb4eee5"]},{"boundary":"Dal gecenin kendisini değil, geceye geçişi veya geceyi zaman ve yön olarak alan işlem ile yolculuk kullanımlarını kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001392/B002","candidate_links":[{"candidate_id":"cand_64a8dd5977420cb118f7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"93:2:1:3","qac_word_ref":"93:2:1","surface_ar":"يْلِ"}],"gloss":"geceye girme ya da geceleyin iş görüp yol alma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir iş veya karşılıklı işlem, gündüz yerine geceye göre yürütülür."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Zaman akışı içinde geceye girme veya gece vaktine ulaşma anlatılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Geceleyin yol alan veya gece yolculuğuna dayanabilen kişi anlatılır."}}],"root_ar":"ل ي ل","root_id":"root_001392","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın geceye geçiş, geceye göre işlem ve gece yolculuğu alt görünümlerini birlikte açıklayan üst karşılıktır.","boundary_detail":"Dal gecenin kendisini değil, geceye geçişi veya geceyi zaman ve yön olarak alan işlem ile yolculuk kullanımlarını kapsar.","branch_image_ar":"مزاولة الأمر في الليل","concept_gloss":"geceye girme ya da geceleyin iş görüp yol alma","contextual_glosses":[{"applicability":"Bir işlemin gündüze göre yapılan benzeriyle karşılaştırılarak gece üzerinden yürütüldüğü bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı işlemin özellikle geceye göre yürütülmesini korur."},"facet_ids":["F001"],"text":"geceye göre karşılıklı işlem yapmak","usage_role":"contextual"},{"applicability":"Bir kişinin veya durumun gece vaktine ulaştığını bildiren kullanımda geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gündüzden gece vaktine geçiş ilişkisini doğrudan korur."},"facet_ids":["F002"],"text":"geceye girmek","usage_role":"contextual"},{"applicability":"Gece yolculuğu yapan veya böyle bir yolculuğa dayanabilen kişinin anlatıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gece yolculuğu yapan kişiyi ve bu yolculuğa güç yetirme koşulunu korur."},"facet_ids":["F003"],"text":"gece yol alan kimse","usage_role":"contextual"}],"definition":"Geceye girmek ya da bir işi, karşılıklı işlemi veya yolculuğu geceyi zaman ve yön olarak alarak gerçekleştirmektir. Gece yolculuğuna dayanabilen kişi de bu eylem alanına bağlı olarak adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir iş veya karşılıklı işlem, gündüz yerine geceye göre yürütülür."},{"facet_id":"F002","role":"core","statement":"Zaman akışı içinde geceye girme veya gece vaktine ulaşma anlatılır."},{"facet_id":"F003","role":"specialization","statement":"Geceleyin yol alan veya gece yolculuğuna dayanabilen kişi anlatılır."}],"identity_rationale":"Kaynak ifadesi geceyi yalın bir zaman adı olarak değil, karşılıklı bir işlemin geceye göre yapılması, geceye girilmesi ve gece yolculuğu yapılması ya da buna güç yetirilmesi üzerinden verir. Geçici dal çerçevesi bu ortak eylem yönelimini doğru yakalar.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"geceye göre karşılıklı işlem yapma"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"geceye girmek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"gece yol alan veya gece yolculuğuna dayanabilen kimse"}],"lexicalization_note":"Anlam yalnız türemiş biçimlerde ve belirli kullanım kalıplarında tanıklanır; karşılıklı işlem, geceye giriş ve gece yolculuğu ayrı alt görünümler olarak tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel gece anlamı ile gece yolculuğunun bağımsız, zorlu veya gündüzden geceye kesintisiz türleri en yararlı dört karşılaştırmayı verdi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dalda gece, girişin, işlemin veya yolculuğun yönünü belirler; komşu dalda ise eylem değil, doğrudan zaman bölümü ve karanlık adlandırılır.","focus_only":"Geceye girme veya geceyi bir eylemin zamanı olarak kullanma anlamlarını taşır.","gloss":"geceleyin eylem ile gece zamanının ayrımı","neighbor_only":"Gece zamanını ve ona bağlı karanlığı adlandırır.","neighbor_ref":"root_001392/B001","relation_type":"same_field","shared_zone":"Her iki dalın ortak zaman ekseni gecedir."},{"boundary_match":"partial","distinction":"Bu dalın yolculuk görünümü yanında geceye giriş ve işlem anlamları vardır; komşu dal ise gece yolculuğunu kendi başına merkezî bir hareket alanı olarak kurar.","focus_only":"Geceye giriş ve geceye göre karşılıklı işlem yapma anlamlarını da kapsar.","gloss":"geniş gece eylemi ile gece yolculuğu arasındaki ayrım","neighbor_only":"Gece yolculuğunu bağımsız bir hareket olarak ve yol alan topluluğu da kapsayacak biçimde merkezleştirir.","neighbor_ref":"root_000702/B001","relation_type":"near_neighbor","shared_zone":"İki dal geceleyin yol alma anlamında belirgin biçimde örtüşür."},{"boundary_match":"partial","distinction":"Bu dal için sürekli çaba ve güçlük kurucu değildir; komşu dal gece boyunca ısrarlı ilerlemeyi ve yolculuğun zahmetini anlamın merkezine alır.","focus_only":"Geceyle bağlantılı işlemi, geçişi ve olağan yolculuk yetisini kapsar.","gloss":"gece yol alma ile gece boyunca çabalayarak ilerleme ayrımı","neighbor_only":"Gece boyunca yolculuğu sürdürme ve bunun güçlüğüne katlanma yönünü özellikle öne çıkarır.","neighbor_ref":"root_001422/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal gece yolculuğu ve bu yolculuğa dayanma alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dalda gündüzden geceye kesintisiz devam şartı yoktur; komşu dalın ayırt edici sınırı, yolculuğun bir gündüz ile bir gece boyunca sürdürülmesidir.","focus_only":"Eylemin yalnız geceye göre yapılmasını veya geceye girilmesini anlatabilir.","gloss":"geceye bağlı eylem ile kesintisiz gündüz gece yolculuğu ayrımı","neighbor_only":"Yolculuğun gündüz ile gece arasında kesintisiz sürdürülmesini zorunlu kılar.","neighbor_ref":"root_001670/B006","relation_type":"near_neighbor","shared_zone":"İki dalın kesişiminde gece boyunca yol alma bulunur."}],"source_phrase_ar":"عاملته ملايلة كما تقول مياومة من اليوم (sihah)؛ أليلت صرت في الليل (tahdhib)؛ لست بليلي ولكني نهر أي أسير بالنهار ولا أطيق سرى الليل (tahdhib)","source_summary":"Toplu kanıt geceye göre yapılan karşılıklı işlemi, gece vaktine girmeyi ve gece yolculuğu yapabilen kişiyi aynı eylem alanında birleştirir. Bu kullanımların hiçbiri yalın gece zamanını tek başına adlandırmaz.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الفعل أو المعاملة على جهة الليل، مثل الملايلة، والدخول في الليل، والسير أو السرى في الليل","what_is_not_ar":"لا يدخل فيه اسم الليل نفسه ولا الليلة بوصفها زمنا مجردا"},"support_links":["sup_55f6f5748467aa2aad0d"]},{"boundary":"Dal yalnız konuşma gününe göre belirlenen en yakın geceyi kapsar; yönelim, cümlenin zamanı ve gün içindeki söyleme anına göre geçmişe veya geleceğe dönebilir.","branch_kind":"non_bare","branch_ref":"root_001392/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"93:2:1:3","qac_word_ref":"93:2:1","surface_ar":"يْلِ"}],"gloss":"bugüne göre belirlenen en yakın gece","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gece, konuşmacının içinde bulunduğu güne göre en yakın gece olarak belirlenir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gündüz söylenen ileri yönelimli kullanım, konuşmacının gireceği yaklaşan geceyi gösterir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tamamlanmış bir eylem günün ilk yarısında anlatılırken ifade önceki geceye dönebilir; gün ilerleyince geçmiş gece için başka bir zaman sözü seçilir."}}],"root_ar":"ل ي ل","root_id":"root_001392","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Geçmiş veya gelecek yönelimi cümle bağlamından anlaşılan, konuşma gününe en yakın geceyi üst düzeyde karşılar.","boundary_detail":"Dal yalnız konuşma gününe göre belirlenen en yakın geceyi kapsar; yönelim, cümlenin zamanı ve gün içindeki söyleme anına göre geçmişe veya geleceğe dönebilir.","branch_image_ar":"الليلة القريبة من اليوم","concept_gloss":"bugüne göre belirlenen en yakın gece","contextual_glosses":[{"applicability":"Gündüz söylenip konuşmacının gireceği yaklaşan geceye yönelen bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Konuşma gününe en yakın yaklaşan gece yönelimini korur."},"facet_ids":["F001","F002"],"text":"bu gece","usage_role":"contextual"},{"applicability":"Günün ilk yarısında tamamlanmış bir eylemi en yakın önceki geceye bağlayan Türkçe anlatımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tamamlanmış eylemin konuşma gününden önceki en yakın geceye bağlanmasını korur."},"facet_ids":["F001","F003"],"text":"dün gece","usage_role":"contextual"}],"definition":"Konuşma gününe en yakın olan ve bağlama göre bir önceki ya da girilecek olan gecedir. Geçmiş bir eylem anlatılırken günün ilk yarısında önceki geceyi gösterebilir; gündüzden yaklaşan gece anlatılırken sonraki geceyi seçer.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gece, konuşmacının içinde bulunduğu güne göre en yakın gece olarak belirlenir."},{"facet_id":"F002","role":"specialization","statement":"Gündüz söylenen ileri yönelimli kullanım, konuşmacının gireceği yaklaşan geceyi gösterir."},{"facet_id":"F003","role":"specialization","statement":"Tamamlanmış bir eylem günün ilk yarısında anlatılırken ifade önceki geceye dönebilir; gün ilerleyince geçmiş gece için başka bir zaman sözü seçilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Bugünle ilişkisi bulunmayan herhangi bir geceyi de kapsar.","collision":null,"fit":"broadening","loses":"Konuşma gününe göre yakınlık ve bağlama bağlı zaman yönelimini belirtmez.","preserves":"Gece zamanına yapılan temel gönderimi korur."},"text":"gece"}],"identity_rationale":"Kaynak ifadesi, genel gece türünü değil konuşma gününe en yakın geceyi seçen bağlamsal bir kullanımı açıkça tanımlar. Gündüz konuşulurken girilecek geceye yönelim ile günün ilk yarısında tamamlanmış bir eylemin önceki geceye bağlanması, geçici çerçevede belirtilen yakınlık ve söyleme zamanı sınırını doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bugüne en yakın gece; bağlama göre geçen ya da girilecek olan gece"}],"lexicalization_note":"Anlam belirli bir gece ifadesinin konuşma gününe göre yorumlanmasına bağlıdır; genel ve bağlamsız gece anlamına genişletilemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel gece, geceleyin eylem, ertesi gün ve bitişik zaman sınırı karşılaştırmaları dalın bugüne bağlı gönderimini en açık biçimde ayırdı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın gönderimi konuşma gününe göre hesaplanır; komşu dal genel gece adıdır ve bugüne yakınlık, söyleme anı veya geçmiş gelecek yönelimi gerektirmez.","focus_only":"Konuşma gününe en yakın geceyi ve bağlama bağlı geçmiş ya da gelecek yönelimini zorunlu kılar.","gloss":"bugüne en yakın gece ile genel gece arasındaki ayrım","neighbor_only":"Herhangi bir geceyi, geceleri ve gece karanlığını bağlamsız olarak kapsayabilir.","neighbor_ref":"root_001392/B001","relation_type":"near_synonym","shared_zone":"İki dal da tek bir gece zamanını gösterebilir ve uygun bağlamda aynı zaman aralığına işaret edebilir."},{"boundary_match":"field_only","distinction":"Bu dalın çekirdeği bağlam içinde seçilen gecedir; komşu dalda gece bir geçişin, işlemin veya yolculuğun gerçekleşme zamanı ve yönüdür.","focus_only":"Bugüne göre seçilen belirli bir gece zamanını gösterir.","gloss":"yakın gece göndergesi ile geceleyin eylem arasındaki ayrım","neighbor_only":"Geceye girme, geceleyin işlem yapma veya gece yolculuğu gerçekleştirme eylemini gösterir.","neighbor_ref":"root_001392/B002","relation_type":"same_field","shared_zone":"Her iki dal da geceyi konuşma veya eylem için zaman çerçevesi yapar."},{"boundary_match":"field_only","distinction":"Bu dal geceyi seçer ve yönelimi bağlama göre değişebilir; komşu dal ise gün birimini seçer ve zorunlu olarak konuşma gününün sonrasına yönelir.","focus_only":"Bugüne komşu geceyi, cümle yönelimine göre geçmişte veya gelecekte seçebilir.","gloss":"en yakın gece ile ertesi gün arasındaki ayrım","neighbor_only":"Yalnız konuşma gününden sonraki günü, yani gelecek gündüzlü zaman birimini seçer.","neighbor_ref":"root_001076/B002","relation_type":"same_field","shared_zone":"İki dal da konuşma gününü merkez alan yakın zaman ifadeleridir."},{"boundary_match":"field_only","distinction":"Bu dal belirli bir gece göndergesini seçer; komşu dal ise geceyi seçmekten çok iki zaman bölümünün birbirine değen başlangıç veya bitiş sınırını adlandırır.","focus_only":"Konuşma gününe göre en yakın gecenin hangisi olduğunu belirler.","gloss":"yakın gece seçimi ile zaman sınırı arasındaki ayrım","neighbor_only":"Bir zaman parçasının başlangıç veya bitiş sınırında başka bir zamanla karşı karşıya gelmesini anlatır.","neighbor_ref":"root_001479/B006","relation_type":"same_field","shared_zone":"Her ikisi de komşu zaman parçaları arasındaki ilişkiyi konu eder."}],"source_phrase_ar":"إلى نصف النهار تقول فعلت الليلة فإذا زالت الشمس قلت فعلت البارحة (tahdhib)؛ هذه الليلة التي في السماء أقرب الليالي من يومك وهي الليلة التي تليه (tahdhib)؛ الهلال في هذه الليلة التي في السماء يعني الليلة التي تدخلها يتكلم بهذا في النهار (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, günün ilk yarısında tamamlanmış bir eylem için önceki gecenin bu ifadeyle anılabildiğini, gün ilerleyince başka bir geçmiş zaman sözünün seçildiğini ve gündüzden bakıldığında yaklaşan gecenin de aynı yakınlık ilkesiyle belirlendiğini bildirir."}],"source_summary":"Kanıt, bu kullanımın genel gece adından farklı olarak konuşma gününe ve gün içindeki söyleme anına göre çözüldüğünü gösterir. Yaklaşan gece ile henüz yakın geçmiş sayılan önceki gece, cümlenin yönelimine göre ayrılır.","sources":["TA"],"what_is_ar":"يدخل فيه إطلاق الليلة على أقرب الليالي من اليوم أو على الليلة الداخلة، والفصل بينها وبين البارحة بحسب وقت الكلام","what_is_not_ar":"لا يدخل فيه مطلق الليل ولا الليالي المجموعة ولا أوصاف شدة الظلمة"},"support_links":[]},{"boundary":"Kadın adı temel adlandırma kullanımıdır; şarap anlamı yalnız ayrı ve tam bir söz öbeğinin örtülü ad işlevine aittir.","branch_kind":"non_bare","branch_ref":"root_001392/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"93:2:1:3","qac_word_ref":"93:2:1","surface_ar":"يْلِ"}],"gloss":"bir kadın adı; ayrıca belirli bir söz öbeğinde şarabın örtülü adı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Söz konusu biçim bir kadını adlandıran kişi adı olarak kullanılır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu adı içeren ayrı bir söz öbeği, şarabı doğrudan söylemeden anan örtülü bir ad olarak kullanılır."}}],"root_ar":"ل ي ل","root_id":"root_001392","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kişi adı çekirdeğini ve yalnız tam söz öbeğine bağlı şarap adlandırmasını sınırlarıyla birlikte açıklar.","boundary_detail":"Kadın adı temel adlandırma kullanımıdır; şarap anlamı yalnız ayrı ve tam bir söz öbeğinin örtülü ad işlevine aittir.","branch_image_ar":"التسمية بليلى","concept_gloss":"bir kadın adı; ayrıca belirli bir söz öbeğinde şarabın örtülü adı","contextual_glosses":[{"applicability":"Biçimin bir kadını adlandırdığı kişi adı kullanımında geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Biçimin kadın kişi adı olma işlevini korur."},"facet_ids":["F001"],"text":"bir kadın adı","usage_role":"contextual"},{"applicability":"Yalnız kadın adını içeren tam söz öbeğinin şarabı dolaylı biçimde andığı kullanımda geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tam söz öbeğinin şarabı örterek adlandırma işlevini korur."},"facet_ids":["F002"],"text":"şarap için kullanılan örtülü ad","usage_role":"contextual"}],"definition":"Bir biçimin kadın adı olarak kullanılmasıdır; aynı adı içeren ayrı bir söz öbeği ise şarabı anan örtülü bir ad işlevi görür. İki kullanım aynı dalda bulunsa da kadın adı ile içki anlamı birbirine eşit değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Söz konusu biçim bir kadını adlandıran kişi adı olarak kullanılır."},{"facet_id":"F002","role":"associated_use","statement":"Bu adı içeren ayrı bir söz öbeği, şarabı doğrudan söylemeden anan örtülü bir ad olarak kullanılır."}],"identity_rationale":"Kaynak ifadesi bir biçimin kadın adı olduğunu ve bu adı içeren ayrı bir söz öbeğinin şarabı örtülü biçimde anlattığını doğrular. Dal bir adlandırma kümesi olarak korunabilir; ancak kadın adının kendi başına şarap anlamına geldiği sanılmamalı, şarap anlamı yalnız tam söz öbeğine bağlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"bir kadın adı"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"şarap için kullanılan örtülü ad"}],"lexicalization_note":"Dal yalnız ad olarak kullanılan biçimi ve şarabı anan tam söz öbeğini kapsar; bunlar genel gece veya karanlık anlamına genişletilemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel gece dalı ile iki ayrı kişi adı dalı, adlandırma işlevini biçimsel yakınlıktan ve farklı ad kimliklerinden ayırmak için seçildi.","neighbor_distinctions":[{"boundary_match":"thematic_only","distinction":"Bu dalın anlamı kişi ve içki adlandırmasıdır; komşu dal ise bir zaman bölümünü ve karanlığı gösterir, dolayısıyla iki dal olağan kullanımda birbirinin yerine geçmez.","focus_only":"Bir kadın adını ve ayrı bir söz öbeğinde şarabın örtülü adını kapsar.","gloss":"adlandırma ile gece anlamı arasındaki ayrım","neighbor_only":"Gece zamanını ve gece karanlığını anlatır.","neighbor_ref":"root_001392/B001","relation_type":"thematic","shared_zone":"Dallar aynı biçim ailesiyle bağlantılıdır, fakat yalnız tarihsel ve biçimsel bir çağrışım paylaşır."},{"boundary_match":"field_only","distinction":"Adlandırma işlevleri aynı alandadır, fakat adların kimlikleri ayrıdır; ayrıca bu dalda belirli bir söz öbeğine bağlı şarap kullanımı bulunur.","focus_only":"Farklı bir kadın adını ve bu adı içeren örtülü şarap sözünü kapsar.","gloss":"iki ayrı kadın adının anlam alanı","neighbor_only":"Başka ve ayrı bir kadın adını kapsar.","neighbor_ref":"root_000848/B009","relation_type":"same_field","shared_zone":"Her iki dal da bir biçimin kadın kişi adı olarak kullanılmasını tanıklar."},{"boundary_match":"field_only","distinction":"Ortak alan adlandırmadır; ancak gösterilen adlar farklıdır ve komşu dalın erkek adı ile lakap kapsamı bu dalda bulunmaz, bu dalın şarap söz öbeği de komşuda yoktur.","focus_only":"Bir kadın adı ile ona bağlı örtülü şarap sözünü içerir.","gloss":"ayrı kişi adları ve lakaplar alanı","neighbor_only":"Başka biçimlerin erkek adı, kadın adı veya lakap olarak kullanılmasını içerir.","neighbor_ref":"root_000799/B007","relation_type":"same_field","shared_zone":"İki dal da sözlük biçimlerinin kişi adı olarak aktarılmasını konu eder."}],"source_phrase_ar":"وبه سميت ليلى (jamhara)؛ ليلى اسم امرأة (sihah)؛ أم ليلى هي الخمر (tahdhib)","source_summary":"Toplu kanıt kadın adı kullanımını ortak biçimde destekler ve ayrıca bu adı içeren tam bir söz öbeğinin şarabı örten bir ad olduğunu bildirir. İkinci kullanım bağımsız söz öbeğine bağlı tutulmalıdır.","sources":["JA","SI","TA"],"what_is_ar":"يدخل فيه ليلى اسما لامرأة، وأم ليلى كنية للخمر","what_is_not_ar":"لا يدخل فيه الليل زمنا ولا الظلمة ولا المعاملة بالليل"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["93:2:1"],"branch_refs":[],"candidate_id":"cand_25095a58b73a630f8716","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:2:1:boundary-fusion","source_type":"word_analysis","support_ids":["sup_8cedab215b50cfde05d6","sup_d7f40cc5b780a134af9c"],"title":"particle fused to its noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:2:1","qac_refs":["93:2:1:1"],"status":"accepted"}},{"anchor_refs":["93:2:1"],"branch_refs":[],"candidate_id":"cand_c6e10dfc97c7b3282be1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:2:1:compound-oath-continuation","source_type":"word_analysis","support_ids":["sup_8cedab215b50cfde05d6","sup_bb084c17228ba3e2278d"],"title":"second member of the oath pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:2:1","qac_refs":["93:2:1:1"],"status":"accepted"}},{"anchor_refs":["93:2:1"],"branch_refs":[],"candidate_id":"cand_b17846414b396f43ecd1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:2:1:oath-genitive-government","source_type":"word_analysis","support_ids":["sup_6fabbe9dcfe11f3ae5ac","sup_8cedab215b50cfde05d6"],"title":"oath particle governs night","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:2:1","qac_refs":["93:2:1:1"],"status":"accepted"}},{"anchor_refs":["93:2:2"],"branch_refs":[],"candidate_id":"cand_94bda1a6639041f82a9b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"93:2:2:audible-lateral-weight","source_type":"word_analysis","support_ids":["sup_7ace8b5d87090dc766bc","sup_a6aad91b8e9a9c1eb219"],"title":"doubled lateral gives weight","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:2:2","qac_refs":["93:2:1:2","93:2:1:3"],"status":"accepted"}},{"anchor_refs":["93:2:2"],"branch_refs":[],"candidate_id":"cand_22224becf574a9e7bf70","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"93:2:2:definite-genitive-witness","source_type":"word_analysis","support_ids":["sup_71b73f98cf967aaaf1f1","sup_a6aad91b8e9a9c1eb219"],"title":"definite night under oath","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:2:2","qac_refs":["93:2:1:2","93:2:1:3"],"status":"accepted"}},{"anchor_refs":["93:2:2"],"branch_refs":[],"candidate_id":"cand_c0715826eb75c9f736c9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"93:2:2:morning-night-antithesis","source_type":"word_analysis","support_ids":["sup_5814b04718dd052dc4eb","sup_a6aad91b8e9a9c1eb219"],"title":"bright morning versus still night","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:2:2","qac_refs":["93:2:1:2","93:2:1:3"],"status":"accepted"}},{"anchor_refs":["93:2:2"],"branch_refs":[],"candidate_id":"cand_d577b76aa0a54767a686","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"93:2:2:night-as-stable-noun","source_type":"word_analysis","support_ids":["sup_a6aad91b8e9a9c1eb219","sup_c23a8dcdf2a0a313022e"],"title":"stable noun despite root pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:2:2","qac_refs":["93:2:1:2","93:2:1:3"],"status":"accepted"}},{"anchor_refs":["93:2:2"],"branch_refs":[],"candidate_id":"cand_1e6219fd08fc5f623b4d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"93:2:2:sequence-echo","source_type":"word_analysis","support_ids":["sup_4b433ee0678720a8e728","sup_a6aad91b8e9a9c1eb219"],"title":"prior night field revoiced","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:2:2","qac_refs":["93:2:1:2","93:2:1:3"],"status":"accepted"}},{"anchor_refs":["93:2:2"],"branch_refs":[],"candidate_id":"cand_65bb78cec1d2f7400566","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"93:2:2:state-bearing-night","source_type":"word_analysis","support_ids":["sup_a6aad91b8e9a9c1eb219","sup_f7ae881ef7d39bc2a6e4"],"title":"sworn night bears the stillness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:2:2","qac_refs":["93:2:1:2","93:2:1:3"],"status":"accepted"}},{"anchor_refs":["93:2:3"],"branch_refs":[],"candidate_id":"cand_5dc95f780c4c6178c6e7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:2:3:boundary-continuation-and-sound","source_type":"word_analysis","support_ids":["sup_3792304f3f78ca1648a7","sup_de042b6e731da495bcfe"],"title":"audible hinge in the continuing oath","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:2:3","qac_refs":["93:2:2:1"],"status":"accepted"}},{"anchor_refs":["93:2:3"],"branch_refs":[],"candidate_id":"cand_4096b632482878e01f89","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:2:3:noun-to-event-pivot","source_type":"word_analysis","support_ids":["sup_3792304f3f78ca1648a7","sup_5980623168784dfc4710"],"title":"pivot from noun to scene","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:2:3","qac_refs":["93:2:2:1"],"status":"accepted"}},{"anchor_refs":["93:2:3"],"branch_refs":[],"candidate_id":"cand_918d23e2d0ebe86928a2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:2:3:qualified-oath-scope","source_type":"word_analysis","support_ids":["sup_3792304f3f78ca1648a7","sup_44ecbb83ff3ef6b502f3"],"title":"night oath is qualified","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:2:3","qac_refs":["93:2:2:1"],"status":"accepted"}},{"anchor_refs":["93:2:3"],"branch_refs":[],"candidate_id":"cand_4846acefedf4fa5c4c3e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:2:3:recurring-temporal-trigger","source_type":"word_analysis","support_ids":["sup_3792304f3f78ca1648a7","sup_c50240610843e9055e87"],"title":"when night reaches stillness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:2:3","qac_refs":["93:2:2:1"],"status":"accepted"}},{"anchor_refs":["93:2:4"],"branch_refs":[],"candidate_id":"cand_e092fa31521ba4bed0bb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000679"],"scope":"focus_ayah","source_local_id":"93:2:4:concrete-root-imagery","source_type":"word_analysis","support_ids":["sup_92ac4c9755e6b61a906d","sup_cde31e9c881e57bc9c5d"],"title":"sea eye and shroud imagery","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:2:4","qac_refs":["93:2:3:1"],"status":"accepted"}},{"anchor_refs":["93:2:4"],"branch_refs":[],"candidate_id":"cand_4db5f89a5e8b5bf51f0e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000679"],"scope":"focus_ayah","source_local_id":"93:2:4:hidden-night-subject","source_type":"word_analysis","support_ids":["sup_5271a97c5e8159238ea6","sup_92ac4c9755e6b61a906d"],"title":"night is the hidden subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:2:4","qac_refs":["93:2:3:1"],"status":"accepted"}},{"anchor_refs":["93:2:4"],"branch_refs":[],"candidate_id":"cand_f0918c452df04b1910a5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000679"],"scope":"focus_ayah","source_local_id":"93:2:4:load-bearing-hapax","source_type":"word_analysis","support_ids":["sup_02b6a7a2b04fc6adf44d","sup_92ac4c9755e6b61a906d"],"title":"only Quranic occurrence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:2:4","qac_refs":["93:2:3:1"],"status":"accepted"}},{"anchor_refs":["93:2:4"],"branch_refs":[],"candidate_id":"cand_104adea327360345f461","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000679"],"scope":"focus_ayah","source_local_id":"93:2:4:morning-and-prior-night-contrast","source_type":"word_analysis","support_ids":["sup_92ac4c9755e6b61a906d","sup_c155a2dede745372577c"],"title":"brightness answered by settled cover","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:2:4","qac_refs":["93:2:3:1"],"status":"accepted"}},{"anchor_refs":["93:2:4"],"branch_refs":[],"candidate_id":"cand_3769eade9cbb3d559a2c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000679"],"scope":"focus_ayah","source_local_id":"93:2:4:open-vowel-closure","source_type":"word_analysis","support_ids":["sup_92ac4c9755e6b61a906d","sup_f4c07a20e33f05ce1e1b"],"title":"open ending extends the close","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:2:4","qac_refs":["93:2:3:1"],"status":"accepted"}},{"anchor_refs":["93:2:4"],"branch_refs":[],"candidate_id":"cand_b71a3f1cf96c3392f6c5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000679"],"scope":"focus_ayah","source_local_id":"93:2:4:perfect-threshold","source_type":"word_analysis","support_ids":["sup_8c1e03687257557e618c","sup_92ac4c9755e6b61a906d"],"title":"completed recurring threshold","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:2:4","qac_refs":["93:2:3:1"],"status":"accepted"}},{"anchor_refs":["93:2:4"],"branch_refs":[],"candidate_id":"cand_d492680cfb60538abb59","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000679"],"scope":"focus_ayah","source_local_id":"93:2:4:predicated-oath-density","source_type":"word_analysis","support_ids":["sup_92ac4c9755e6b61a906d","sup_cc11534d776e002868b4"],"title":"verb makes a compact scene","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:2:4","qac_refs":["93:2:3:1"],"status":"accepted"}},{"anchor_refs":["93:2:4"],"branch_refs":[],"candidate_id":"cand_8b64d9da9f08db83fb2f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000679"],"scope":"focus_ayah","source_local_id":"93:2:4:still-covering-calm","source_type":"word_analysis","support_ids":["sup_92ac4c9755e6b61a906d","sup_a71ebdf369492a7e7378"],"title":"stillness with covering undertone","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:2:4","qac_refs":["93:2:3:1"],"status":"accepted"}},{"anchor_refs":["93:2:1"],"branch_refs":[],"candidate_id":"cand_eb22cde1255d33a9a6ab","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001392"],"scope":"focus_ayah","source_local_id":"93:2:1:3","source_type":"qac_morpheme","support_ids":["sup_8c5bafb20023340eb6d2"],"title":"QAC root occurrence: ل ي ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["93:2:3"],"branch_refs":[],"candidate_id":"cand_669864533c90345cc628","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000679"],"scope":"focus_ayah","source_local_id":"93:2:3:1","source_type":"qac_morpheme","support_ids":["sup_848b5a4a266323222ad5"],"title":"QAC root occurrence: س ج و","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["93:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:2","branch_refs":["root_000679/B001","root_001392/B001"],"candidate_id":"cand_e35a127336689712f902","commentary_obligation":"review","hft_ref":"hft_46e13962ebd75297cdba","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b01_settling_closure","source_type":"hft","support_ids":["sup_221d06da391bc93e8285"],"title":"b01_settling_closure","trust":"legacy_unbound"},{"anchor_refs":["93:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:2","branch_refs":["root_000679/B002","root_001392/B001"],"candidate_id":"cand_b8e5e1b9c8988e10ffef","commentary_obligation":"review","hft_ref":"hft_8030c114c7408b16e789","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b02_draped_cover","source_type":"hft","support_ids":["sup_7dd937c398797fb4eee5"],"title":"b02_draped_cover","trust":"legacy_unbound"},{"anchor_refs":["93:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:2","branch_refs":["root_000679/B001","root_001392/B002"],"candidate_id":"cand_64a8dd5977420cb118f7","commentary_obligation":"review","hft_ref":"hft_8e28a8849421b30b8c7e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b03_night_as_operation","source_type":"hft","support_ids":["sup_55f6f5748467aa2aad0d"],"title":"b03_night_as_operation","trust":"legacy_unbound"},{"anchor_refs":["93:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:2","branch_refs":["root_000679/B006","root_001392/B001"],"candidate_id":"cand_223098e4216d5e23bca1","commentary_obligation":"review","hft_ref":"hft_5130a20f0cfb3869e015","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b04_hidden_yield","source_type":"hft","support_ids":["sup_3bf2e63fcd048469d7c2"],"title":"b04_hidden_yield","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَٱلَّيْلِ إِذَا سَجَىٰ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"93:2:1:1","qac_word_ref":"93:2:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"93:2:1:2","qac_word_ref":"93:2:1","root_ar":"","surface_ar":"ٱلَّ"},{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"93:2:1:3","qac_word_ref":"93:2:1","root_ar":"ل ي ل","surface_ar":"يْلِ"},{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"93:2:2:1","qac_word_ref":"93:2:2","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"سَجَىٰ","morph_features":"STEM|POS:V|PERF|LEM:sajaY`|ROOT:sjw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"93:2:3:1","qac_word_ref":"93:2:3","root_ar":"س ج و","surface_ar":"سَجَىٰ"}],"word_analysis_qac_refs":[["93:2:1:1"],["93:2:1:2","93:2:1:3"],["93:2:2:1"],["93:2:3:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["93:2:1","93:2:2","93:2:3","93:2:4"]},"focus_surface_evidence":{"arabic_uthmani":"وَٱلَّيْلِ إِذَا سَجَىٰ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"93:2:1:1","qac_word_ref":"93:2:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"93:2:1:2","qac_word_ref":"93:2:1","root_ar":"","surface_ar":"ٱلَّ"},{"lemma_ar":"لَيْل","morph_features":"STEM|POS:N|LEM:layol|ROOT:lyl|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"93:2:1:3","qac_word_ref":"93:2:1","root_ar":"ل ي ل","surface_ar":"يْلِ"},{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"93:2:2:1","qac_word_ref":"93:2:2","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"سَجَىٰ","morph_features":"STEM|POS:V|PERF|LEM:sajaY`|ROOT:sjw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"93:2:3:1","qac_word_ref":"93:2:3","root_ar":"س ج و","surface_ar":"سَجَىٰ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["93:2:1:1"],["93:2:1:2","93:2:1:3"],["93:2:2:1"],["93:2:3:1"]],"word_analysis_refs":["93:2:1","93:2:2","93:2:3","93:2:4"],"word_rows":[{"analysis_record_ref":"93:2:1","analytic_gloss_range_en":"second oath particle with connective force; it governs the following genitive night noun while continuing the oath pair from 93:1","analytic_root_gloss_range_en":null,"qac_refs":["93:2:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"93:2:2","analytic_gloss_range_en":"the definite genitive night as a cosmic oath witness, then as the state-bearer of the following stilling clause","analytic_root_gloss_range_en":"night as the opposite of day and its darkness is locally selected; by-night actions, deictic tonight uses, naming material, and disputed bird senses remain outside the local referent","qac_refs":["93:2:1:2","93:2:1:3"],"root":{"arabic":"ل ي ل","transliteration":"l-y-l"},"surface":{"arabic":"ٱلَّيْلِ","transliteration":"al-layli"}},{"analysis_record_ref":"93:2:3","analytic_gloss_range_en":"temporal trigger introducing the condition or moment in which night has reached stillness; expected recurring when/whenever, not uncertain if","analytic_root_gloss_range_en":null,"qac_refs":["93:2:2:1"],"root":{},"surface":{"arabic":"إِذَا","transliteration":"idhā"}},{"analysis_record_ref":"93:2:4","analytic_gloss_range_en":"Form I perfect intransitive: night has grown still, settled, and quietly covered; not simply darkened and not a caused action on an object","analytic_root_gloss_range_en":"still settling and closing-in is locally selected, with covering or shrouding retained as an undertone because the subject is night; disposition, non-touching, estate-tending, and abundance branches are not active locally","qac_refs":["93:2:3:1"],"root":{"arabic":"س ج و","transliteration":"s-j-w"},"surface":{"arabic":"سَجَىٰ","transliteration":"sajā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["93:2"],"branch_refs":["root_000679/B001","root_001392/B001"],"candidate_id":"cand_e35a127336689712f902","evidence_scope":"focus_ayah","hft_ref":"hft_46e13962ebd75297cdba","item_id":"b01_settling_closure","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b01_settling_closure","support_id":"sup_221d06da391bc93e8285"},{"anchor_refs":["93:2"],"branch_refs":["root_000679/B002","root_001392/B001"],"candidate_id":"cand_b8e5e1b9c8988e10ffef","evidence_scope":"focus_ayah","hft_ref":"hft_8030c114c7408b16e789","item_id":"b02_draped_cover","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b02_draped_cover","support_id":"sup_7dd937c398797fb4eee5"},{"anchor_refs":["93:2"],"branch_refs":["root_000679/B001","root_001392/B002"],"candidate_id":"cand_64a8dd5977420cb118f7","evidence_scope":"focus_ayah","hft_ref":"hft_8e28a8849421b30b8c7e","item_id":"b03_night_as_operation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b03_night_as_operation","support_id":"sup_55f6f5748467aa2aad0d"},{"anchor_refs":["93:2"],"branch_refs":["root_000679/B006","root_001392/B001"],"candidate_id":"cand_223098e4216d5e23bca1","evidence_scope":"focus_ayah","hft_ref":"hft_5130a20f0cfb3869e015","item_id":"b04_hidden_yield","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b04_hidden_yield","support_id":"sup_3bf2e63fcd048469d7c2"}],"diagnostics":[],"lane_counts":{"global":10,"macro":13,"micro":4},"packet_summary":{"ayah_count":11,"focus_ref":"93:2","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"و ج د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001626","furuq_root_norm":"و ج د","furuq_source_root_norm":"و ج د","is_dominant":true,"target_occurrences":61,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000227","furuq_root_norm":"ج د د","furuq_source_root_norm":"ج د د","is_dominant":false,"target_occurrences":10,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ء ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000661","furuq_root_norm":"س ء ل","furuq_source_root_norm":"س أ ل","is_dominant":true,"target_occurrences":118,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000736","furuq_root_norm":"س ل ل","furuq_source_root_norm":"س ل ل","is_dominant":false,"target_occurrences":2,"target_rank":2}]}],"window":["93:1","93:2","93:3","93:4","93:5","93:6","93:7","93:8","93:9","93:10","93:11"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"93:2","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":17,"unstructured_record_count":0},"identity":{"ayah_ref":"93:2","lane":"micro","linguistic_source_ref":"93:2","surface_ref":"93:2","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"93:2","target_tokens":[["Sakinleştiğinde",["93:2:2","93:2:3"]],["geceye",["93:2:1"]],["de",["93:2:1"]],["andolsun",["93:2:1"]]],"text":"Sakinleştiğinde geceye de andolsun."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":11,"id":"s093-p01-001-011","label":"Whole surah","number":1,"refs":["93:1","93:2","93:3","93:4","93:5","93:6","93:7","93:8","93:9","93:10","93:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:4:load-bearing-hapax","source_type":"word_analysis","support_id":"sup_02b6a7a2b04fc6adf44d","text":"{\"blocking_evidence\":null,\"headline\":\"only Quranic occurrence\",\"reader_payoff\":\"The reader notices that this root has no Quranic parallel to diffuse its force, so the local morphology, scene, and sound must carry the word's value.\",\"reason\":\"Contextual evidence reports one exact-root Form I occurrence, matching the CRITICAL hapax claim and requiring local interpretation rather than parallel activation.\",\"representative_source_ids\":[\"QI-a06b24fb\",\"QH-853220ad\",\"MH-68a0a21a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:3","source_type":"word_analysis","support_id":"sup_3792304f3f78ca1648a7","text":"{\"gloss_range\":\"temporal trigger introducing the condition or moment in which night has reached stillness; expected recurring when/whenever, not uncertain if\",\"prose\":\"{{ar:إِذَا}} ({{tr:idhā}}) turns the oath by night into an oath by night at a particular recurring threshold. With the following perfect verb, it does not simply narrate a past event; it gives the sense of whenever night has reached stillness. Because the particle is indeclinable, it carries the clause architecture while {{ar:سَجَىٰ}} ({{tr:sajā}}) supplies the event content. Its position after {{ar:ٱلَّيْلِ}} ({{tr:al-layli}}) pivots the ayah from a sworn noun to an observed scene, and its initial stop is a small audible hinge between the bound night phrase and the condition.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِذَا}} ({{tr:idhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:3:qualified-oath-scope","source_type":"word_analysis","support_id":"sup_44ecbb83ff3ef6b502f3","text":"{\"blocking_evidence\":null,\"headline\":\"night oath is qualified\",\"reader_payoff\":\"The reader notices that the oath is not merely by night in general, but by night in the condition named by {{ar:سَجَىٰ}} ({{tr:sajā}}).\",\"reason\":\"The local syntax licenses {{ar:إِذَا}} ({{tr:idhā}}) plus the verb as a temporal clause, so the particle narrows the sworn object to a specific night-state.\",\"representative_source_ids\":[\"QG-cc1f5e8a\",\"QI-b54f00ae\",\"MT-69d9429d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:2:sequence-echo","source_type":"word_analysis","support_id":"sup_4b433ee0678720a8e728","text":"{\"blocking_evidence\":null,\"headline\":\"prior night field revoiced\",\"reader_payoff\":\"The reader notices that the night field carried from the preceding surah's opening (92:1) is not repeated flatly but shifted into stilled witness.\",\"reason\":\"The source rows point to the immediately preceding surah's night field; locally, the following verb gives the word a stilled rather than active covering profile.\",\"representative_source_ids\":[\"QE-4e771baf\",\"ME-dc0dee48\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:4:hidden-night-subject","source_type":"word_analysis","support_id":"sup_5271a97c5e8159238ea6","text":"{\"blocking_evidence\":null,\"headline\":\"night is the hidden subject\",\"reader_payoff\":\"The reader notices that the verb's hidden 3ms subject is the night itself, so the sworn witness becomes the state-bearer.\",\"reason\":\"Attachment evidence explicitly resolves the pro-dropped 3ms subject to the nearby masculine singular night noun, and the verb instance is intransitive Form I.\",\"representative_source_ids\":[\"QG-5794e005\",\"QG-70fcd658\",\"QF-86396911\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:2:morning-night-antithesis","source_type":"word_analysis","support_id":"sup_5814b04718dd052dc4eb","text":"{\"blocking_evidence\":null,\"headline\":\"bright morning versus still night\",\"reader_payoff\":\"The reader notices that the usual night-and-day binary is narrowed here into bright morning in 93:1 and night in its settled condition in 93:2.\",\"reason\":\"The contextual profile shows night's strong pairing with day, and the CRITICAL rows specify that this ayah replaces the broader day pole with the morning witness from 93:1, with wider pairings visible at 36:37 and 21:33.\",\"representative_source_ids\":[\"QS-2f4c515f\",\"QS-bbde056b\",\"MI-16361f26\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:3:noun-to-event-pivot","source_type":"word_analysis","support_id":"sup_5980623168784dfc4710","text":"{\"blocking_evidence\":null,\"headline\":\"pivot from noun to scene\",\"reader_payoff\":\"The reader notices the architecture of a compact scene clause embedded inside the oath, moving from named night to night in action or state.\",\"reason\":\"The indeclinable particle stands between the noun and perfect verb, carrying the clause relation without itself bearing inflection.\",\"representative_source_ids\":[\"QF-bd0d8c47\",\"QT-929e0432\",\"QT-ea38f56b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:1:oath-genitive-government","source_type":"word_analysis","support_id":"sup_6fabbe9dcfe11f3ae5ac","text":"{\"blocking_evidence\":null,\"headline\":\"oath particle governs night\",\"reader_payoff\":\"The reader notices that {{ar:وَ}} ({{tr:wa}}) makes {{ar:ٱلَّيْلِ}} ({{tr:al-layli}}) a sworn witness under genitive oath government, not an ordinary coordinated item.\",\"reason\":\"QAC identifies the particle as oath-introducing, and attachment evidence marks formulaic ellipsis plus oath scope for the second oath phrase.\",\"representative_source_ids\":[\"QG-8e4188e4\",\"MG-1a968661\",\"QI-4dc670f8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:2:definite-genitive-witness","source_type":"word_analysis","support_id":"sup_71b73f98cf967aaaf1f1","text":"{\"blocking_evidence\":null,\"headline\":\"definite night under oath\",\"reader_payoff\":\"The reader notices that the noun is the recognized night placed in genitive oath service, not an indefinite time label or ordinary subject.\",\"reason\":\"QAC and noun-instance evidence mark {{ar:ٱلَّيْلِ}} ({{tr:al-layli}}) as definite and genitive under the oath particle, and V4 selects the physical night branch locally.\",\"representative_source_ids\":[\"QG-20d61e6e\",\"QG-605b0b0b\",\"QG-9ca7c100\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:2:audible-lateral-weight","source_type":"word_analysis","support_id":"sup_7ace8b5d87090dc766bc","text":"{\"blocking_evidence\":null,\"headline\":\"doubled lateral gives weight\",\"reader_payoff\":\"The reader notices the sustained lateral sound that gives the sworn object audible weight and binds it to the oath particle.\",\"reason\":\"The local bound phrase places the oath particle immediately before the definite noun, supporting the CRITICAL sound observation without making it control the lexical sense.\",\"representative_source_ids\":[\"QP-905927d2\",\"QP-d4d32153\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"93:2:3:1","source_type":"qac_morpheme","support_id":"sup_848b5a4a266323222ad5","text":"{\"lemma_ar\":\"سَجَىٰ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:sajaY`|ROOT:sjw|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"93:2:3:1\",\"qac_word_ref\":\"93:2:3\",\"root_ar\":\"س ج و\",\"surface_ar\":\"سَجَىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:4:perfect-threshold","source_type":"word_analysis","support_id":"sup_8c1e03687257557e618c","text":"{\"blocking_evidence\":null,\"headline\":\"completed recurring threshold\",\"reader_payoff\":\"The reader notices that the perfect verb under {{ar:إِذَا}} ({{tr:idhā}}) marks night as having reached stillness whenever that phase arrives, not as a one-time past event.\",\"reason\":\"The temporal clause is strongly licensed, and the perfect verb follows {{ar:إِذَا}} ({{tr:idhā}}), preserving the completed or habitual threshold claim.\",\"representative_source_ids\":[\"QG-70ad7f82\",\"MG-5bd75f9a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"93:2:1:3","source_type":"qac_morpheme","support_id":"sup_8c5bafb20023340eb6d2","text":"{\"lemma_ar\":\"لَيْل\",\"morph_features\":\"STEM|POS:N|LEM:layol|ROOT:lyl|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"93:2:1:3\",\"qac_word_ref\":\"93:2:1\",\"root_ar\":\"ل ي ل\",\"surface_ar\":\"يْلِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:1","source_type":"word_analysis","support_id":"sup_8cedab215b50cfde05d6","text":"{\"gloss_range\":\"second oath particle with connective force; it governs the following genitive night noun while continuing the oath pair from 93:1\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) does not open a fresh sentence as a plain connector. It carries oath force into {{ar:ٱلَّيْلِ}} ({{tr:al-layli}}), making the night a second sworn witness after 93:1 while the oath answer still remains ahead. The particle therefore does two things at once: it binds this ayah to the prior morning oath and governs the following genitive noun in a compressed oath formula. Because it is attached directly to the night word in recitation and writing, the listener hears the grammatical dependency at the boundary, not a pause before an independent statement.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:4","source_type":"word_analysis","support_id":"sup_92ac4c9755e6b61a906d","text":"{\"gloss_range\":\"Form I perfect intransitive: night has grown still, settled, and quietly covered; not simply darkened and not a caused action on an object\",\"prose\":\"{{ar:سَجَىٰ}} ({{tr:sajā}}) is the point where the night-oath settles. Its hidden masculine subject is {{ar:ٱلَّيْلِ}} ({{tr:al-layli}}), so the genitive sworn witness becomes the one that reaches the state named by the verb. Under {{ar:إِذَا}} ({{tr:idhā}}), the perfect form gives a recurring completed threshold: whenever night has grown still. The Form I intransitive frame makes this a state night enters, not an action imposed on an object. Lexically, the selected force is calm settling and uniform stillness, not mere darkening; the covering branch survives as an undertone because the subject is night, but it is narrowed away from a transitive cloth-covering act. The sea-calm, steady-eye, and shroud images give the word concrete pressure: motion comes to rest, gaze stops darting, and cover lies over the scene. This completes the polarity with the exposed morning of 93:1 and also revoices the prior night-covering field (92:1) from active covering into settled calm. The verb is unusually load-bearing as the only Quranic occurrence of root {{ar:س ج و}} ({{tr:s-j-w}}), and the ayah lands on its open final vowel, so the sound closure participates in the extended stillness it names.\",\"root_display\":\"{{ar:س ج و}} ({{tr:s-j-w}})\",\"root_gloss_range\":\"still settling and closing-in is locally selected, with covering or shrouding retained as an undertone because the subject is night; disposition, non-touching, estate-tending, and abundance branches are not active locally\",\"surface_display\":\"{{ar:سَجَىٰ}} ({{tr:sajā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:2","source_type":"word_analysis","support_id":"sup_a6aad91b8e9a9c1eb219","text":"{\"gloss_range\":\"the definite genitive night as a cosmic oath witness, then as the state-bearer of the following stilling clause\",\"prose\":\"{{ar:ٱلَّيْلِ}} ({{tr:al-layli}}) is definite and genitive, so the oath invokes night as a recognized cosmic witness rather than one unspecified night. Its noun form keeps the referent stable as night itself; a noted root dispute does not change the local sense, and the V4 branch range keeps naming, deictic, and by-night action branches outside this use. Yet the noun is not static: the following {{ar:سَجَىٰ}} ({{tr:sajā}}) resumes it as the hidden masculine subject, so the sworn witness becomes the bearer of stillness. That makes the contrast with the morning witness in 93:1 more precise: the ayah does not move from day to night in general, but from exposed brightness to night as a settled, covering presence. Quranic night-and-day pairings such as 36:37 and 21:33 supply the wider binary, while this oath narrows the second pole to bright morning versus still night. The immediate sequence also keeps a memory of the preceding night opening (92:1), but here night is revoiced as stilled witness. The doubled lateral sound gives the noun audible weight before the ayah turns into the temporal clause.\",\"root_display\":\"{{ar:ل ي ل}} ({{tr:l-y-l}})\",\"root_gloss_range\":\"night as the opposite of day and its darkness is locally selected; by-night actions, deictic tonight uses, naming material, and disputed bird senses remain outside the local referent\",\"surface_display\":\"{{ar:ٱلَّيْلِ}} ({{tr:al-layli}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:4:still-covering-calm","source_type":"word_analysis","support_id":"sup_a71ebdf369492a7e7378","text":"{\"blocking_evidence\":null,\"headline\":\"stillness with covering undertone\",\"reader_payoff\":\"The reader notices that {{ar:سَجَىٰ}} ({{tr:sajā}}) names calm uniform stillness, with night-like covering retained as an undertone rather than as a transitive covering act.\",\"reason\":\"V4 accepts both still-settling and covering branches, while the local intransitive frame and night subject select stillness as primary and narrow the covering material to an undertone.\",\"representative_source_ids\":[\"QS-33a46b02\",\"QS-45159fc1\",\"MS-05fabc4c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:1:compound-oath-continuation","source_type":"word_analysis","support_id":"sup_bb084c17228ba3e2278d","text":"{\"blocking_evidence\":null,\"headline\":\"second member of the oath pair\",\"reader_payoff\":\"The reader notices that the particle both swears by night and carries forward the paired oath from the morning witness in 93:1.\",\"reason\":\"The local particle is oath-governing, while the repeated opening across 93:1 and 93:2 supports a compound oath pair rather than two detached openings.\",\"representative_source_ids\":[\"QS-f686247a\",\"MT-55cb86ca\",\"QB-4dda3b34\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:4:morning-and-prior-night-contrast","source_type":"word_analysis","support_id":"sup_c155a2dede745372577c","text":"{\"blocking_evidence\":null,\"headline\":\"brightness answered by settled cover\",\"reader_payoff\":\"The reader notices that the verb completes the move from exposed morning in 93:1 to night as settled cover in 93:2, while contrasting with the active covering field of 92:1.\",\"reason\":\"The local oath pair supplies the 93:1 contrast, and the source rows explicitly compare the preceding night-covering field at 92:1 with this settled night-state.\",\"representative_source_ids\":[\"QS-308866f8\",\"MI-8669446e\",\"QB-8b91c968\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:2:night-as-stable-noun","source_type":"word_analysis","support_id":"sup_c23a8dcdf2a0a313022e","text":"{\"blocking_evidence\":null,\"headline\":\"stable noun despite root pressure\",\"reader_payoff\":\"The reader notices that the word presents night as a unified noun phenomenon while morphology questions remain secondary to the local referent.\",\"reason\":\"The valid root dispute is preserved as morphological pressure, but QAC, contextual data, and V4 keep the local sense in the night-as-darkness noun branch rather than alternate branches.\",\"representative_source_ids\":[\"QS-4cd1aa73\",\"MS-1e193a38\",\"QF-1dca5c7d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:3:recurring-temporal-trigger","source_type":"word_analysis","support_id":"sup_c50240610843e9055e87","text":"{\"blocking_evidence\":null,\"headline\":\"when night reaches stillness\",\"reader_payoff\":\"The reader notices that the particle makes the perfect verb an expected recurring threshold, not a one-time past report or uncertain condition.\",\"reason\":\"QAC marks the word as a temporal adverb, and attachment evidence treats it with the following verb as the temporal clause attached to the night oath.\",\"representative_source_ids\":[\"QG-b29c0ce9\",\"MG-3858ce75\",\"QS-50e16f6a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:4:predicated-oath-density","source_type":"word_analysis","support_id":"sup_cc11534d776e002868b4","text":"{\"blocking_evidence\":null,\"headline\":\"verb makes a compact scene\",\"reader_payoff\":\"The reader notices that the ayah does not merely say the still night; it embeds a finite verb inside an oath whose answer is still pending.\",\"reason\":\"The local sequence compresses conjunction, sworn noun, temporal particle, and finite verb into one scene clause, and the larger oath answer remains outside this ayah.\",\"representative_source_ids\":[\"QG-7b961013\",\"QF-e432e583\",\"QT-6e4b8ae2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:4:concrete-root-imagery","source_type":"word_analysis","support_id":"sup_cde31e9c881e57bc9c5d","text":"{\"blocking_evidence\":null,\"headline\":\"sea eye and shroud imagery\",\"reader_payoff\":\"The reader notices that the verb carries concrete images of a calm surface, a steady gaze, and a covering laid over something, giving the night-scene bodily texture.\",\"reason\":\"The classical image fields are preserved as lexical pressure, but local grammar prevents them from becoming separate literal subjects or actions.\",\"representative_source_ids\":[\"QS-30b027d9\",\"QS-8dd10ca2\",\"MS-0eca1ce1\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:1:boundary-fusion","source_type":"word_analysis","support_id":"sup_d7f40cc5b780a134af9c","text":"{\"blocking_evidence\":null,\"headline\":\"particle fused to its noun\",\"reader_payoff\":\"The reader notices that the small oath particle is heard as bound directly into the night noun, making the governance audible.\",\"reason\":\"The surface particle is a bound proclitic immediately attached to the governed noun, so the phonological observation follows the local form.\",\"representative_source_ids\":[\"QF-cae9ad1e\",\"QP-2606d6e3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:3:boundary-continuation-and-sound","source_type":"word_analysis","support_id":"sup_de042b6e731da495bcfe","text":"{\"blocking_evidence\":null,\"headline\":\"audible hinge in the continuing oath\",\"reader_payoff\":\"The reader notices that the ayah boundary remains syntactically continuous while the particle creates an audible turn into observation.\",\"reason\":\"The particle follows the bound oath phrase and introduces the temporal clause, so the acoustic hinge and syntactic continuation both arise from the local sequence.\",\"representative_source_ids\":[\"QP-9d51ff02\",\"QB-6da5d0b9\",\"QB-d2df119d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:4:open-vowel-closure","source_type":"word_analysis","support_id":"sup_f4c07a20e33f05ce1e1b","text":"{\"blocking_evidence\":null,\"headline\":\"open ending extends the close\",\"reader_payoff\":\"The reader notices that the verse lands on an open sustained vowel, letting the sound of the final word linger with the stillness it names.\",\"reason\":\"The final word closes the ayah with the long final vowel, so the phonetic payoff is local and does not require importing an external semantic branch.\",\"representative_source_ids\":[\"QF-fc63fa7b\",\"QP-1e2119af\",\"MP-df731792\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:2:2:state-bearing-night","source_type":"word_analysis","support_id":"sup_f7ae881ef7d39bc2a6e4","text":"{\"blocking_evidence\":null,\"headline\":\"sworn night bears the stillness\",\"reader_payoff\":\"The reader notices that the genitive oath noun also supplies the hidden subject of {{ar:سَجَىٰ}} ({{tr:sajā}}), making night the bearer of a still-covering state.\",\"reason\":\"Attachment evidence explicitly resolves the 3ms verb subject to the nearby masculine singular night noun, so the CRITICAL claim about night as state-bearer is licensed.\",\"representative_source_ids\":[\"QS-628facd9\",\"QS-8b1c835e\",\"QS-9a355449\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلَّيْلِ إِذَا سَجَىٰ","ayah_ref":"93:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000679/B001","root_001392/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001392","role":"Night opposed to day supplies the dark temporal field in which the transition occurs.","root":"ل ي ل","source_ref":"93:2","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000679","role":"Still settling across night, water, wind, or gaze supplies the event of motion closing down.","root":"س ج و","source_ref":"93:2","source_word_indices":["3"]}],"changed_reading":{"after":"An oath by the threshold at which night actively settles, closes in, and quiets a moving field.","before":"A bare oath by nighttime."},"confidence":"strong","focus_anchor":"The night noun rooted ل ي ل is joined by إذا to a verb rooted س ج و, so the oath catches a transition rather than naming a static backdrop.","mechanism":"Darkness supplies the field while motion in night, sea, wind, and gaze subsides together; the scene closes by becoming still.","model_id":"b01_settling_closure"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b01_settling_closure","source_type":"hft","support_id":"sup_221d06da391bc93e8285","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلَّيْلِ إِذَا سَجَىٰ","ayah_ref":"93:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000679/B002","root_001392/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001392","role":"Night's darkness supplies the wide surface-like medium that can cover the visible world.","root":"ل ي ل","source_ref":"93:2","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000679","role":"Draping a cloth, including a shroud, turns nocturnal darkening into a material act of covering.","root":"س ج و","source_ref":"93:2","source_word_indices":["3"]}],"changed_reading":{"after":"Night draws itself over the scene like cloth, ambiguously concealing, sheltering, or shrouding it.","before":"Night merely becomes dark."},"confidence":"medium","focus_anchor":"The س ج و verb can carry a cloth-covering image while its grammatical subject remains the night.","mechanism":"Night behaves like a covering drawn across what was visible. The image retains an unresolved range from sheltering cloth to concealing shroud.","model_id":"b02_draped_cover"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b02_draped_cover","source_type":"hft","support_id":"sup_7dd937c398797fb4eee5","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلَّيْلِ إِذَا سَجَىٰ","ayah_ref":"93:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000679/B001","root_001392/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001392","role":"Entering or doing something by night supplies an active nocturnal mode rather than passive clock-time.","root":"ل ي ل","source_ref":"93:2","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000679","role":"Settling and closing-in gives that nocturnal mode its operative effect on the surrounding field.","root":"س ج و","source_ref":"93:2","source_word_indices":["3"]}],"changed_reading":{"after":"Night itself enters as an actor and performs the quieting of the scene.","before":"Night is the time during which something else might happen."},"confidence":"medium","focus_anchor":"The ل ي ل inventory includes entering or acting by night, and the إذا clause gives that nocturnal mode a finite onset.","mechanism":"Night is not only scenery but an operation: it arrives, takes up the field, and performs a settling upon it.","model_id":"b03_night_as_operation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b03_night_as_operation","source_type":"hft","support_id":"sup_55f6f5748467aa2aad0d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلَّيْلِ إِذَا سَجَىٰ","ayah_ref":"93:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000679/B006","root_001392/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001392","role":"Night's opacity makes the quantity held beneath the settled scene unavailable to sight.","root":"ل ي ل","source_ref":"93:2","source_word_indices":["1"]},{"branch_id":"B006","mapped_root_id":"root_000679","role":"Abundant milk or well-water supplies the latent yield hidden inside the apparent stillness.","root":"س ج و","source_ref":"93:2","source_word_indices":["3"]}],"changed_reading":{"after":"Settling may be the quiet surface of a hidden abundance capable of yielding later.","before":"Settling means that activity and production have stopped."},"confidence":"exploratory","focus_anchor":"A remote but explicit س ج و branch concerns abundant yielding from milk or a well, still attached to the focus verb.","mechanism":"The dark settled surface can be imagined as a reservoir: apparent inactivity may conceal a supply not yet visible.","model_id":"b04_hidden_yield"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b04_hidden_yield","source_type":"hft","support_id":"sup_3bf2e63fcd048469d7c2","trust":"legacy_unbound"}]}
</lane_packet_json>
