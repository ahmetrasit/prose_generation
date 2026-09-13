# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **99:4**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s099-regular-20260912/s099/99_4/micro.discovery.json` and modify nothing
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
  "ayah_ref": "99:4",
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
{"branch_registry":[{"boundary":"Dal, salt yenilik niteliğini ya da söz aktarmayı değil, yokluktan sonra varlık kazanma veya gerçekleşme geçişini anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000299/B001","candidate_links":[{"candidate_id":"cand_58b9fbb478d211e8ea25","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تُحَدِّثُ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:tuHad~ivu|ROOT:Hdv|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:4:2:1","qac_word_ref":"99:4:2","surface_ar":"تُحَدِّثُ"}],"gloss":"yokken var olma, var etme veya gerçekleşme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey, daha önce yokken varlık kazanır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ettirgen yönde bir şey var edilir veya ortaya çıkarılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir iş ya da durum, daha önce yokken gerçekleşir."}}],"root_ar":"ح د ث","root_id":"root_000299","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kendiliğinden oluş, ettirgen oldurma ve bir işin meydana gelmesi yönlerini birlikte karşılayan üst anlatımdır.","boundary_detail":"Dal, salt yenilik niteliğini ya da söz aktarmayı değil, yokluktan sonra varlık kazanma veya gerçekleşme geçişini anlatır.","branch_image_ar":"كون الشيء بعد أن لم يكن","concept_gloss":"yokken var olma, var etme veya gerçekleşme","contextual_glosses":[{"applicability":"Öznenin daha önce yokken varlık kazandığı bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir şeyi var etme ve bir işin gerçekleşmesi yönlerini tek başına belirtmez.","preserves":"Bir şeyin yokken varlık kazanması yönünü korur."},"facet_ids":["F001"],"text":"ortaya çıkmak","usage_role":"general"},{"applicability":"Bir failin daha önce bulunmayan bir şeyi ortaya çıkardığı ettirgen bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kendiliğinden oluşu ve bir işin yalnızca gerçekleşmesini dışarıda bırakır.","preserves":"Failin bir şeyi yokluktan varlığa çıkarması yönünü korur."},"facet_ids":["F002"],"text":"var etmek","usage_role":"contextual"},{"applicability":"Bir işin, durumun veya gelişmenin meydana geldiğini bildiren kullanımlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nesnenin varlık kazanmasını ve failce var edilmesini açıkça taşımaz.","preserves":"Bir işin daha önce yokken meydana gelmesi yönünü korur."},"facet_ids":["F003"],"text":"gerçekleşmek","usage_role":"contextual"}],"definition":"Bir şeyin daha önce yokken varlık kazanması; ettirgen kullanımda var edilmesi, bir iş ya da durum içinse gerçekleşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey, daha önce yokken varlık kazanır."},{"facet_id":"F002","role":"extension","statement":"Ettirgen yönde bir şey var edilir veya ortaya çıkarılır."},{"facet_id":"F003","role":"specialization","statement":"Bir iş ya da durum, daha önce yokken gerçekleşir."}],"identity_rationale":"Kaynak ifadesi, bir şeyin daha önce yokken var olmasını, ettirgen kullanımda var edilmesini ve bir işin gerçekleşmesini aynı anlam çekirdeğinin yönleri olarak açıkça verir. Sunulan dal çerçevesi bu oluş, oldurma ve gerçekleşme ayrımını doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"sonradan var olma"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"var etmek, ortaya çıkarmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir iş gerçekleşti"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sonradan var edilmiş şey"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"eskiden beri olanlarla sonradan gerçekleşenlerin tümü"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"inanç ve uygulamalara sonradan eklenen yenilikler"}],"lexicalization_note":"Tanım, yalın oluş ve oldurma biçimlerini kapsar; belirli söz öbeklerindeki gerçekleşme ve sonradan eklenme anlamlarını yalnız kendi yapıları içinde tutar.","neighbor_coverage_note":"Adayların tümü değerlendirildi; en yararlı sınırlar örneksiz ilk yapım, zamanda bulunma ve eskilik karşıtlığı üzerinden verildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği yokluktan sonra oluş ve gerçekleşmedir; komşu dalda ise yeniliğin örneksiz ve ilk kez kurulmuş olması belirleyicidir.","focus_only":"Odak dal, örneksiz ilk yapımı şart koşmadan her türlü sonradan var olmayı ve gerçekleşmeyi kapsar.","gloss":"var olma ile örneksiz yaratım","neighbor_only":"Komşu dal, bir şeyi önceden örneği bulunmadan ilk kez kurma ve yapma sınırını öne çıkarır.","neighbor_ref":"root_000094/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da daha önce bulunmayan bir şeyin ortaya çıkmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal için önce yokken sonra var olma geçişi zorunludur; komşu dal yalnızca bir zamanda bulunmayı da anlatabilir.","focus_only":"Odak dal, önceki yokluk ile sonraki varlık arasındaki geçişi ve oldurmayı bildirir.","gloss":"oluş ile zamanda bulunma","neighbor_only":"Komşu dal, bir şeyin belirli bir zamanda bulunmasını, hazır oluşunu ve dilbilgisel kullanımları da kapsar.","neighbor_ref":"root_001332/B001","relation_type":"near_neighbor","shared_zone":"İki dal da bir şeyin belli bir zamanda gerçekleşmesi veya bulunmasıyla ilişkilidir."},{"boundary_match":"opposed","distinction":"Odak dal başlangıç ve sonradan var oluş kutbundadır; komşu dal ise başlangıcı geçmişe uzanan eskilik kutbundadır.","focus_only":"Odak dal, bir şeyin önce yokken sonradan varlık kazanmasını temel alır.","gloss":"sonradan oluş ile eskilik","neighbor_only":"Komşu dal, uzun zamandır var olmayı, geçmiş zamana dayanmayı ve sonradan oluşun karşıtını anlatır.","neighbor_ref":"root_001207/B003","relation_type":"polarity_pair","shared_zone":"İki dal, bir şeyin zaman içindeki başlangıcı ve süresi bakımından aynı eksende karşılaşır."}],"source_phrase_ar":"كون الشيء لم يكن (maqayis)؛ الحديث نقيض القديم والحدوث كون شيء لم يكن وأحدثه الله فحدث وحدث أمر أي وقع (sihah)؛ الحدوث كون الشيء بعد أن لم يكن وإحداثه إيجاده والمحدث ما أوجد بعد أن لم يكن (mufradat)","source_summary":"Kaynakların ortak çizgisi, yok olanın varlık kazanmasını, bir şeyi var etmeyi ve bir işin meydana gelmesini aynı temel geçiş çevresinde birleştirir.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه الحدوث والإحداث ووقوع الأمر وكون الشيء جديدا أو محدثا بعد عدمه.","what_is_not_ar":"ليس المراد هنا مجرد الكلام والخبر ولا صفة الشاب الفتي إلا من جهة قرب العهد."},"support_links":["sup_03cc034ce401c5f322b2"]},{"boundary":"Dal, genel oluşu değil, yaşça gençliği, başlangıca yakınlığı, yeniliği veya somut tazeliği anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000299/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تُحَدِّثُ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:tuHad~ivu|ROOT:Hdv|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:4:2:1","qac_word_ref":"99:4:2","surface_ar":"تُحَدِّثُ"}],"gloss":"genç, yeni ya da taze olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya şey, başlangıcına ya da ortaya çıkışına yakın olduğu için yenidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsan için yaşça genç ve yetişkinliğin erken döneminde olmayı anlatır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir işin veya gençlik döneminin ilk ve taze evresini gösterir."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Meyve gibi somut şeylerde kurumamış ve taze olmayı niteler."}}],"root_ar":"ح د ث","root_id":"root_000299","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaş, zaman içindeki yenilik, başlangıç evresi ve somut tazelik yönlerini birlikte gösteren üst karşılıktır.","boundary_detail":"Dal, genel oluşu değil, yaşça gençliği, başlangıca yakınlığı, yeniliği veya somut tazeliği anlatır.","branch_image_ar":"طراوة السن وقرب العهد","concept_gloss":"genç, yeni ya da taze olma","contextual_glosses":[{"applicability":"Bir kişinin yaşça genç olduğunu belirten insan nitelemelerinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nesnelerin yeniliğini, süreç başlangıcını ve somut tazeliği kapsamaz.","preserves":"İnsanla ilgili genç yaş ve erken dönem anlamını korur."},"facet_ids":["F002"],"text":"yaşı genç","usage_role":"contextual"},{"applicability":"Bir işin, dönemin veya gelişmenin henüz ilk evresinde bulunduğu bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yaşça gençliği ve meyve gibi şeylerin tazeliğini tek başına belirtmez.","preserves":"Sürecin ilk ve taze evresinde bulunma yönünü korur."},"facet_ids":["F003"],"text":"daha başlangıcında","usage_role":"contextual"},{"applicability":"Meyve gibi somut bir şeyin yeni ve kurumamış olduğunu anlatan bağlamlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsan yaşını ve bir sürecin başlangıç evresini açıkça taşımaz.","preserves":"Somut şeyin tazeliğini ve yeniliğini korur."},"facet_ids":["F004"],"text":"taze","usage_role":"contextual"}],"definition":"Yaş bakımından genç, bir sürecin başında, kısa süre önce ortaya çıkmış ya da tazeliğini koruyan olma durumudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya şey, başlangıcına ya da ortaya çıkışına yakın olduğu için yenidir."},{"facet_id":"F002","role":"specialization","statement":"İnsan için yaşça genç ve yetişkinliğin erken döneminde olmayı anlatır."},{"facet_id":"F003","role":"extension","statement":"Bir işin veya gençlik döneminin ilk ve taze evresini gösterir."},{"facet_id":"F004","role":"example","statement":"Meyve gibi somut şeylerde kurumamış ve taze olmayı niteler."}],"identity_rationale":"Kaynak ifadesi genç yaşı, bir şeyin yeniliğini, bir dönemin ilk ve taze evresini, kısa süre önce oluşmayı ve meyvenin tazeliğini birlikte gösterir. Dal çerçevesi bunları yakın geçmiş ve tazelik çekirdeği çevresinde doğru biçimde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"yeni"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"genç, yaşı küçük"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yaşı genç"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"gençler, delikanlılar"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"gençliğin ilk çağı"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"daha başlangıcındayken"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"taze meyve"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yakın zamanda yapılmış ya da söylenmiş"}],"lexicalization_note":"Tanım yalın yeni ve genç nitelemelerini kapsar; gençliğin ilk çağı ve bir işin başlangıcı gibi yapı bağımlı anlamları ayrı tutar.","neighbor_coverage_note":"Bütün adaylar gözden geçirildi; gençlik, başlangıç yakınlığı ve yenilenmişlik sınırlarını en açık gösteren üç komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yakın geçmiş ve tazelik çevresinde genişlerken komşu dalın belirgin sınırı hayvanların olgunlaşma öncesi yaş basamağıdır.","focus_only":"Odak dal, insan yaşı yanında yeni şeyleri, başlangıç evresini ve meyvenin tazeliğini de birlikte kapsar.","gloss":"gençlik ve tazelik","neighbor_only":"Komşu dal, özellikle hayvanın olgunlaşma öncesi yaş basamağını ve kendine özgü adlarını içerir.","neighbor_ref":"root_000231/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da yaşça gençliği, erken evreyi ve henüz olgunlaşmamış olmayı anlatır."},{"boundary_match":"partial","distinction":"Odak dal gençlik ve tazeliği de kapsar; komşu dalın çekirdeği ilk oluş, ilk ürün ve erkencilik sınırıdır.","focus_only":"Odak dal, genç insanı ve taze meyveyi de niteleyerek yeniliği yaş ve dirilik alanlarına taşır.","gloss":"başlangıç yakınlığı","neighbor_only":"Komşu dal, bir şeyin ilk ürünü veya erkenden erişmiş ilk örneği olmasına ağırlık verir.","neighbor_ref":"root_000143/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin başlangıca yakın, yeni veya erken evrede olmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dalın sınırı gençlik ve tazeliğe uzanır; komşu dal ise yeni nesne ve yeniden yeni hale gelme çevresinde kurulur.","focus_only":"Odak dal, yeniliğin yanında genç yaş ve somut tazelik anlamlarını da taşır.","gloss":"yenilik ile yenilenme","neighbor_only":"Komşu dal, yenilenmiş veya yeni yapılmış nesneye ve yenilenme sürecine odaklanır.","neighbor_ref":"root_000227/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da eski olmayan veya kısa süre önce ortaya çıkmış şeyi niteleyebilir."}],"source_phrase_ar":"الرجل الحدث الطري السن (maqayis)؛ شاب حدث وشابة حدثة فتية في السن والحديث الجديد من الأشياء (ayn)؛ رجل حدث السن وحديث السن (jamhara)؛ رجل حدث أي شاب وهؤلاء غلمان حدثان وأوله وطراءته (sihah)؛ شاب حدث فتي السن وحدثان شبابه وحديث شبابه (tahdhib)؛ الحديث الطري من الثمار ورجل حدث وحديث السن بمعنى (mufradat)","source_summary":"Kaynaklar genç yaş, yenilik, başlangıca yakınlık ve somut tazelik kullanımlarını ortak biçimde bildirir; bunların tümünde geçmişi kısa veya ilk evresinde olma özelliği vardır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الشاب الحدث وحديث السن والحدثان من الغلمان، وما كان في أوله وحداثته وقريب العهد أو طريا.","what_is_not_ar":"لا يدخل فيه الخبر المروي ولا النازلة العارضة إلا إذا أريد قرب عهدها."},"support_links":[]},{"boundary":"Dalın çekirdeği var etme değil, sözlü içeriğin oluşması, aktarılması veya kişiler arasında paylaşılmasıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000299/B003","candidate_links":[{"candidate_id":"cand_8830cab18946c219b3ae","lane":"micro"},{"candidate_id":"cand_58b9fbb478d211e8ea25","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تُحَدِّثُ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:tuHad~ivu|ROOT:Hdv|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:4:2:1","qac_word_ref":"99:4:2","surface_ar":"تُحَدِّثُ"}],"gloss":"söz, anlatım ve karşılıklı konuşma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiye işitme veya bildirim yoluyla ulaşan söz ve aktarılan içeriktir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İçeriği anlatma, konuşma ve karşılıklı söz alışverişinde bulunma eylemlerini kapsar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kimseyi güzel veya çok konuşan kişi olarak niteler."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir kimseyi kadınların ya da yöneticilerin konuşma ve oturma arkadaşı olarak belirtir."}}],"root_ar":"ح د ث","root_id":"root_000299","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Aktarılan içeriği, anlatma eylemini ve karşılıklı konuşmayı birlikte temsil eden, kişi nitelemelerine de temel olan üst karşılıktır.","boundary_detail":"Dalın çekirdeği var etme değil, sözlü içeriğin oluşması, aktarılması veya kişiler arasında paylaşılmasıdır.","branch_image_ar":"كلام يتجدد خبرا وحديثا","concept_gloss":"söz, anlatım ve karşılıklı konuşma","contextual_glosses":[{"applicability":"Bir kişiye aktarılan sözlü içerik veya anlatılan bilgi söz konusu olduğunda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Karşılıklı konuşmayı ve konuşkan kişi nitelemelerini dışarıda bırakır.","preserves":"Aktarılan sözlü içeriği ve anlatılabilir bilgi yönünü korur."},"facet_ids":["F001"],"text":"anlatı","usage_role":"general"},{"applicability":"İki veya daha çok kişinin birbirine söz söylediği etkileşim bağlamlarına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek yönlü aktarılmış içeriği ve konuşkan kişi nitelemelerini kapsamaz.","preserves":"Kişiler arasındaki söz alışverişi yönünü korur."},"facet_ids":["F002"],"text":"karşılıklı konuşma","usage_role":"contextual"},{"applicability":"Bir kişinin konuşma miktarını veya konuşmadaki ustalığını niteleyen kullanımlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sözlü içeriğin kendisini ve karşılıklı konuşma eylemini kapsamaz.","preserves":"Konuşma özelliğinin kişiye yüklenen nitelik olmasını korur."},"facet_ids":["F003"],"text":"çok konuşan kimse","usage_role":"explanatory"}],"definition":"İnsana işitme ya da bildirim yoluyla ulaşan sözlü içerik ve bunun anlatılması veya karşılıklı konuşulmasıdır; ayrıca güzel ya da çok konuşan kimseyi ve belirli çevrelerin konuşma arkadaşını niteleyebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiye işitme veya bildirim yoluyla ulaşan söz ve aktarılan içeriktir."},{"facet_id":"F002","role":"extension","statement":"İçeriği anlatma, konuşma ve karşılıklı söz alışverişinde bulunma eylemlerini kapsar."},{"facet_id":"F003","role":"specialization","statement":"Bir kimseyi güzel veya çok konuşan kişi olarak niteler."},{"facet_id":"F004","role":"associated_use","statement":"Bir kimseyi kadınların ya da yöneticilerin konuşma ve oturma arkadaşı olarak belirtir."}],"identity_rationale":"Kaynak ifadesi işitme ya da bildirim yoluyla ulaşan sözü, aktarılan bilgiyi, konuşmayı ve karşılıklı konuşmayı birlikte verir; ayrıca çok veya güzel konuşan kimseyi ve belirli çevrelerin konuşma arkadaşını niteler. Sunulan çerçeve bu söz ve anlatım alanını doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"söz, aktarılan bilgi"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"anlatılar, aktarılan sözler"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"düşte insana söylenenler"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"bilgi verme, anlatma"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"karşılıklı konuşma"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"güzel ya da çok konuşan adam"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"çok konuşan adam"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kadınlarla konuşup görüşen kimse"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"hükümdarların konuşma ve gece oturma arkadaşı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"güzel söz söyleme niteliği"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"tek bir anlatı veya konuşma konusu"}],"lexicalization_note":"Tanım söz ve aktarma çekirdeğini korur; çok konuşan kişi ile belirli toplulukların konuşma arkadaşı gibi yalın olmayan nitelemeleri ayrı yönler olarak sınırlar.","neighbor_coverage_note":"Adayların tümü incelendi; konuşmanın kendisi, aktarım zinciri ve karşılıklı yanıt yapısı en açıklayıcı üç sınır olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sözlü içeriği ve bu içerikle nitelenen kişiyi de içerir; komşu dalın çekirdeği anlaşılır söz söyleme ve muhatapla konuşmadır.","focus_only":"Odak dal, aktarılan sözlü içeriği ve çok ya da güzel konuşan kişiye ilişkin nitelemeleri de kapsar.","gloss":"anlatı ile konuşma","neighbor_only":"Komşu dal, anlaşılır söz söyleme eylemini ve konuşanlar arasındaki doğrudan bağı temel alır.","neighbor_ref":"root_001316/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da insanın anlam taşıyan söz söylemesini ve kişiler arası konuşmayı kapsar."},{"boundary_match":"partial","distinction":"Odak dalda sözlü içerik ve konuşma yeterlidir; komşu dalda içeriğin önceki kaynağa dayanması ve aktarım yoluyla korunması belirleyicidir.","focus_only":"Odak dal, sözün kendisini, anlatmayı ve canlı karşılıklı konuşmayı kapsar.","gloss":"söz ile aktarım zinciri","neighbor_only":"Komşu dal, aktarılan sözün önceki bir kaynaktan devralınıp korunarak sonraya iletilmesine odaklanır.","neighbor_ref":"root_000011/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir sözün veya bilginin bir kişiden başkasına ulaşmasını içerir."},{"boundary_match":"partial","distinction":"Odak dalın kapsamı her türlü sözlü içerik ve anlatıma açıktır; komşu dalda karşılıklı yanıt verme yapısı çekirdeğin parçasıdır.","focus_only":"Odak dal tek yönlü anlatıyı, aktarılan içeriği ve konuşan kişiye ilişkin nitelikleri de içine alır.","gloss":"konuşma ile söz alışverişi","neighbor_only":"Komşu dal sözün karşılıklı gidip gelmesini, yanıta ve sözün geri çevrilmesine dayanan alışverişi gerektirir.","neighbor_ref":"root_000369/B006","relation_type":"near_neighbor","shared_zone":"Her ikisinde de birden çok kişi arasında karşılıklı söz söyleme bulunabilir."}],"source_phrase_ar":"الحديث لأنه كلام يحدث منه الشيء بعد الشيء ورجل حدث حسن الحديث وحدث نساء (maqayis)؛ الأحدوثة الحديث نفسه ورجل حدث كثير الحديث (ayn)؛ رجل حدث حسن الحديث وحدث نساء (jamhara)؛ الحديث الخبر والمحادثة والتحدث والتحادث والتحديث معروفات ورجل حديث كثير الحديث (sihah)؛ الحديث ما يحدث به المحدث تحديثا ورجل حدث أي كثير الحديث والأحاديث في الفقه وغيره معروفة (tahdhib)؛ كل كلام يبلغ الإنسان من جهة السمع أو الوحي يقال له حديث وحادثته وحدثته وتحادثوا (mufradat)","source_summary":"Kaynaklar sözlü içeriği, onun aktarılmasını ve karşılıklı konuşmayı ortak anlam alanında birleştirir; kişi nitelemeleri bu çekirdeğe bağlı olarak güzel, çok veya belirli çevrelerle konuşmayı gösterir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحديث بمعنى الكلام والخبر وما يحدث به الإنسان، والمحادثة والتحدث والتحديث، والرجل الحسن أو الكثير الحديث، وصاحب حديث النساء أو الملوك.","what_is_not_ar":"لا يدخل فيه مجرد إيجاد الشيء بعد عدمه ولا حداثة السن، إلا من جهة أن الكلام يحدث شيئا بعد شيء في تعليل بعض المصادر."},"support_links":["sup_03cc034ce401c5f322b2","sup_8cef1235becdf6a8de51"]},{"boundary":"Burada çekirdek, sözün kendisi değil, kişi veya topluluğun insanların dilinde dolaşan anlatının konusu haline gelmesidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000299/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تُحَدِّثُ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:tuHad~ivu|ROOT:Hdv|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:4:2:1","qac_word_ref":"99:4:2","surface_ar":"تُحَدِّثُ"}],"gloss":"insanların dilinde anlatı konusu olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, topluluk veya durum insanların hakkında konuştuğu konu haline gelir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hakkındaki anlatılar çoğalır ve dilden dile aktarılan sözlü içeriğe dönüşür."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Geçmiş bir topluluk, başkalarının ders çıkarması için anlatılan bir örnek haline gelebilir."}}],"root_ar":"ح د ث","root_id":"root_000299","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişi veya topluluğun hakkında konuşulan ve aktarılıp örnek gösterilebilen bir konu haline gelmesini karşılar.","boundary_detail":"Burada çekirdek, sözün kendisi değil, kişi veya topluluğun insanların dilinde dolaşan anlatının konusu haline gelmesidir.","branch_image_ar":"صيرورة المرء حديث الناس","concept_gloss":"insanların dilinde anlatı konusu olma","contextual_glosses":[{"applicability":"Bir kişi veya olay hakkında çokça konuşulmaya başlandığını anlatan bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir topluluğun sonraki kuşaklara aktarılan örneğe dönüşmesini açıkça belirtmez.","preserves":"Birinin yaygın konuşma konusu haline gelmesini korur."},"facet_ids":["F001","F002"],"text":"insanların diline düşmek","usage_role":"general"},{"applicability":"Geçmiş kişi veya toplulukların başkalarına örnek olarak anlatıldığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalnızca hakkında çokça konuşulup örnek niteliği kazanmayan kullanımları kapsamaz.","preserves":"Anlatının başkalarına örnek gösterilen kalıcı yönünü korur."},"facet_ids":["F003"],"text":"ders çıkarılan bir anlatıya dönüşmek","usage_role":"explanatory"}],"definition":"Bir kişi veya topluluğun hakkında çokça konuşulan, dilden dile aktarılan ve kimi zaman örnek gösterilen bir anlatı konusu haline gelmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, topluluk veya durum insanların hakkında konuştuğu konu haline gelir."},{"facet_id":"F002","role":"extension","statement":"Hakkındaki anlatılar çoğalır ve dilden dile aktarılan sözlü içeriğe dönüşür."},{"facet_id":"F003","role":"specialization","statement":"Geçmiş bir topluluk, başkalarının ders çıkarması için anlatılan bir örnek haline gelebilir."}],"identity_rationale":"Kaynak ifadesi bir kişi veya topluluğun yalnızca konuşmasını değil, hakkında çokça konuşulan ve anlatılarda örnek gösterilen kişi veya topluluk haline gelmesini anlatır. Dal çerçevesi konuşmanın içeriği ile konuşulan hedef arasındaki bu ayrımı doğru kurar.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"hakkında konuşulan kişi, olay veya anlatı"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"insanların diline düşmek"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"onları dilden dile aktarılan örneklere çevirdik"}],"lexicalization_note":"Tanım hakkında konuşulan konu anlamını kapsar; birinin insanların diline düşmesi ve bir topluluğun örnek anlatıya dönüşmesi gibi yapı bağımlı kullanımları kendi sınırlarında tutar.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; genel ün, görünür tanınma ve sözlü içeriğin kendisiyle kurulan üç ayrım dal sınırını yeterince açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda tanınma, hakkında anlatılan sözlere ve örnekleşmeye bağlıdır; komşu dalda genel ün kazanmak tek başına yeterlidir.","focus_only":"Odak dal, ün kazanmanın özel olarak anlatı konusu olmaktan ve hakkında sözlerin çoğalmasından doğmasını gerektirir.","gloss":"anlatı konusu olma ile ün","neighbor_only":"Komşu dal, anlatı konusu olma yolu aranmadan bir kişi veya topluluğun genel ün kazanmasını kapsar.","neighbor_ref":"root_000500/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişi veya topluluğun insanlar arasında yaygın biçimde tanınmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği insanlarca anlatılmaktır; komşu dalın çekirdeği ise anlatı bulunmasa da genel görünürlük ve yaygın tanınmadır.","focus_only":"Odak dal, kişinin veya topluluğun hakkında anlatılan sözlerin doğrudan konusu haline gelmesini anlatır.","gloss":"anlatılma ile tanınma","neighbor_only":"Komşu dal, iyi ya da kötü herhangi bir yolla görünür ve yaygın biçimde bilinir olmayı kapsar.","neighbor_ref":"root_000823/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da kişi veya durum geniş bir topluluğun dikkatine ve bilgisine girer."},{"boundary_match":"partial","distinction":"Komşu dal sözün veya konuşmanın kendisidir; odak dal ise o sözlerde anılan kişi ya da topluluğun konuşma konusu haline gelmesidir.","focus_only":"Odak dal, hakkında konuşulan kişi veya topluluğun kendisini anlamın merkezine yerleştirir.","gloss":"anlatı ile anlatının konusu","neighbor_only":"Komşu dal, konuşulan sözlü içeriği, onu anlatma eylemini ve konuşan kişiyi anlamın merkezine yerleştirir.","neighbor_ref":"root_000299/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da insanların konuştuğu ve birbirine aktardığı sözlü içerikle ilişkilidir."}],"source_phrase_ar":"صار فلان أحدوثة أي كثروا فيه الأحاديث (ayn)؛ الأحدوثة ما يتحدث به (sihah)؛ صار فلان أحدوثة أي أكثروا فيه الأحاديث (tahdhib)؛ فجعلناهم أحاديث أي أخبارا يتمثل بهم وصار أحدوثة (mufradat)","source_summary":"Kaynaklar, bir kişi veya topluluk hakkında anlatıların çoğalmasını ve o kişi ya da topluluğun dilden dile aktarılan, bazen örnek gösterilen bir anlatı konusuna dönüşmesini ortak biçimde belirtir.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الأحدوثة وما يتحدث الناس به عن شخص أو قوم حتى يصيروا أخبارا وأحاديث يتمثل بها.","what_is_not_ar":"ليس كل كلام أو خبر داخلا هنا؛ المقصود كون الشخص أو الجماعة نفسها مادة الحديث."},"support_links":[]},{"boundary":"Dal her gerçekleşmeyi değil, insanı veya topluluğu etkileyen beklenmedik ve çoğunlukla sarsıcı olayı anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000299/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تُحَدِّثُ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:tuHad~ivu|ROOT:Hdv|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:4:2:1","qac_word_ref":"99:4:2","surface_ar":"تُحَدِّثُ"}],"gloss":"baş gösteren ağır olay","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir insanın veya topluluğun karşısına beklenmedik bir olay çıkar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Olay, zamanın getirdiği sıkıntı veya sarsıcı gelişme olarak kavranır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tek bir ağır olayın çoğulu, zaman içinde karşılaşılan sıkıntılı olaylar bütününü anlatır."}}],"root_ar":"ح د ث","root_id":"root_000299","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsanın karşısına çıkan, zamanla ilişkilendirilen ve sıkıntı doğuran olayı kısa biçimde karşılar.","boundary_detail":"Dal her gerçekleşmeyi değil, insanı veya topluluğu etkileyen beklenmedik ve çoğunlukla sarsıcı olayı anlatır.","branch_image_ar":"نازلة الدهر وحادثته","concept_gloss":"baş gösteren ağır olay","contextual_glosses":[{"applicability":"Bir kişinin beklenmedik ve sarsıcı bir gelişmeyle karşılaştığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Zamana bağlanan toplu sıkıntılar ve olaylar bütününü açıkça belirtmez.","preserves":"Ağır olayın bir kişinin karşısına çıkması yönünü korur."},"facet_ids":["F001"],"text":"başına ağır bir olay gelmek","usage_role":"general"},{"applicability":"Bir dönem boyunca insanların karşısına çıkan sarsıcı olayların topluca anlatıldığı yapıya uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek bir beklenmedik olayın yalın adlandırmasını kapsamaz.","preserves":"Ağır olayların zamana bağlanan çoğul görünümünü korur."},"facet_ids":["F002","F003"],"text":"zamanın getirdiği sıkıntılar","usage_role":"contextual"}],"definition":"İnsanın veya topluluğun başına gelen, zaman içinde ortaya çıkan ve çoğunlukla sıkıntı ya da sarsıntı doğuran ağır olaydır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir insanın veya topluluğun karşısına beklenmedik bir olay çıkar."},{"facet_id":"F002","role":"specialization","statement":"Olay, zamanın getirdiği sıkıntı veya sarsıcı gelişme olarak kavranır."},{"facet_id":"F003","role":"extension","statement":"Tek bir ağır olayın çoğulu, zaman içinde karşılaşılan sıkıntılı olaylar bütününü anlatır."}],"identity_rationale":"Kaynak ifadesi zamanın getirdiği sarsıcı olayları, insanın başına gelen sıkıntıları ve ortaya çıkan ağır durumu aynı dalda toplar. Sunulan çerçeve, genel meydana gelmeden farklı olan bu olumsuz olay niteliğini doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"beklenmedik ağır olay"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"zamanın getirdiği sıkıntılı olaylar"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"ortaya çıkan ağır olay"}],"lexicalization_note":"Tanım yalın ağır olay anlamını korur; zamanın getirdiği sıkıntılar biçimindeki yapı bağımlı kullanımı bu özel çevreyle sınırlar.","neighbor_coverage_note":"Adayların tamamı incelendi; kişiye yönelen sıkıntı, yıkıcı gelişme ve genel gerçekleşme ile karşılaştırmalar dalın olumsuz olay sınırını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal zamanın ağır olayları için daha genel bir adlandırmadır; komşu dalda olayın belirli bir kişiye ya da topluluğa yönelmesi daha belirgindir.","focus_only":"Odak dal, zamanın olaylarını çoğul olarak ve tekil olarak ortaya çıkan ağır gelişmeyi birlikte adlandırır.","gloss":"ağır olay ile başa gelen sıkıntı","neighbor_only":"Komşu dal, olayın özellikle bir insanın veya topluluğun başına gelmesini ve yeniden uğramasını öne çıkarır.","neighbor_ref":"root_001571/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da insanın veya topluluğun başına gelen sarsıcı ve istenmeyen olayı anlatır."},{"boundary_match":"partial","distinction":"Odak dalın kapsamı beklenmedik ağır olaydır; komşu dal daha dar biçimde yıkıcı ve kayıp doğuran gelişmeye yönelir.","focus_only":"Odak dal, yıkıcı olmak zorunda bulunmayan ama sıkıntı ve sarsıntı doğuran beklenmedik olayları da kapsar.","gloss":"sarsıcı olay ile yıkım","neighbor_only":"Komşu dal, zamanın insana yönelttiği açık yıkım ve ağır kayıp sonucunu öne çıkarır.","neighbor_ref":"root_001546/B008","relation_type":"near_synonym","shared_zone":"İki dal da zamanın getirdiği ve insanı olumsuz etkileyen ağır gelişmeleri anlatır."},{"boundary_match":"partial","distinction":"Komşu dal genel meydana gelmedir; odak dal ise meydana gelenin başa gelen, sıkıntı doğuran ağır bir olay olmasıyla sınırlıdır.","focus_only":"Odak dal, gerçekleşen şeyin insanı etkileyen ağır ve sıkıntılı bir olay olmasını gerektirir.","gloss":"gerçekleşme ile ağır olay","neighbor_only":"Komşu dal, olumlu veya olumsuz ayrımı yapmadan herhangi bir şeyin yokken var olmasını ya da gerçekleşmesini kapsar.","neighbor_ref":"root_000299/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da daha önce bulunmayan bir olayın zaman içinde meydana gelmesiyle ilişkilidir."}],"source_phrase_ar":"الحدث من أحداث الدهر شبه النازلة (ayn)؛ حدثان الدهر نوائبه (jamhara)؛ الحدث والحدثى والحادثة والحدثان كلها بمعنى (sihah)؛ حدثان الدهر حوادثه والحدثان إذا ألمت بنا (tahdhib)؛ الحادثة النازلة العارضة وجمعها حوادث (mufradat)","source_summary":"Kaynaklar ortaya çıkan ağır olayı, zamanın getirdiği sıkıntıyı ve bunların çoğulunu aynı anlam alanında birleştirir; ortak vurgu olayın kişiye veya topluluğa yönelen sarsıcı niteliğidir.","sources":["AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحدث والحادثة والحدثان بمعنى حوادث الدهر ونوائبه والنوازل العارضة.","what_is_not_ar":"لا يدخل فيه مطلق الحدوث الفلسفي أو الكلام والخبر إلا عند ذكر الحادثة بوصفها واقعة."},"support_links":[]},{"boundary":"Dal, bir şeyi yoktan var etmeyi değil, var olan veya kavranan şeyi açığa çıkarıp görünür hale getirmeyi anlatır.","branch_kind":"bare","branch_ref":"root_000299/B006","candidate_links":[{"candidate_id":"cand_2148948467ba4ed8ccf8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تُحَدِّثُ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:tuHad~ivu|ROOT:Hdv|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:4:2:1","qac_word_ref":"99:4:2","surface_ar":"تُحَدِّثُ"}],"gloss":"ortaya koyma ve görünür kılma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey ortaya konur veya görünür hale getirilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ortaya konan şey başkalarınca görülebilir veya anlaşılabilir hale gelir."}}],"root_ar":"ح د ث","root_id":"root_000299","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin açığa çıkarılıp görülebilir veya anlaşılabilir duruma getirildiği yalın anlamı karşılar.","boundary_detail":"Dal, bir şeyi yoktan var etmeyi değil, var olan veya kavranan şeyi açığa çıkarıp görünür hale getirmeyi anlatır.","branch_image_ar":"إبداء الشيء وإظهاره","concept_gloss":"ortaya koyma ve görünür kılma","contextual_glosses":[{"applicability":"Kapalı veya görünmeyen bir şeyin ortaya çıkarıldığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir şeyi ortaya koymayı ve görünür duruma getirmeyi birlikte korur."},"facet_ids":["F001","F002"],"text":"açığa çıkarmak","usage_role":"general"}],"definition":"Bir şeyi ortaya koymak, açığa çıkarmak veya başkalarınca görülebilir hale getirmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey ortaya konur veya görünür hale getirilir."},{"facet_id":"F002","role":"extension","statement":"Ortaya konan şey başkalarınca görülebilir veya anlaşılabilir hale gelir."}],"identity_rationale":"Kaynak ifadesi bu dalı doğrudan bir şeyi ortaya koyma ve görünür kılma anlamıyla tanımlar. Sunulan çerçeve, bunu genel var etme anlamına genişletmeden aynı yalın anlamı korur.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"ortaya koyma, görünür kılma"}],"lexicalization_note":"Bu yalın dal yalnızca ortaya koyma ve görünür kılma çekirdeğiyle tanımlanır; başka yapılara bağlı oluş veya konuşma anlamları içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; önceki gizlilik, gören kişi ilişkisi ve kendiliğinden görünme ayrımları dalın yalın sınırını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genel ortaya koymadır; komşu dalda önceki gizlilikten sonra açılma veya örtünün kaldırılması belirleyicidir.","focus_only":"Odak dal, önceden gizli olma şartı aramadan bir şeyi ortaya koyma ve görünür kılmayı anlatır.","gloss":"gösterme ile gizliyi açma","neighbor_only":"Komşu dal, görünür hale gelen şeyin daha önce gizli veya örtülü bulunmasını sınırın parçası yapar.","neighbor_ref":"root_000105/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin görünür veya bilinir hale gelmesini ve gösterilmesini kapsar."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği açığa çıkarmaktır; komşu dalda gösteren, gösterilen şey ve gören kişi arasındaki ilişki daha belirgindir.","focus_only":"Odak dal, belirli bir izleyici veya görme eylemi bulunmadan da bir şeyi ortaya koymayı kapsar.","gloss":"ortaya koyma ile gösterme","neighbor_only":"Komşu dal, bir şeyi başka birinin görmesini sağlama ve ona gösterme ilişkisini açıkça gerektirir.","neighbor_ref":"root_000531/B012","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi görünür duruma getirip başkasının algısına açabilir."},{"boundary_match":"partial","distinction":"Odak dalda bir şeyi ortaya koyan eylem öndedir; komşu dal görünür olma durumunu ve görünüşe dayalı kullanımları da içerir.","focus_only":"Odak dal yalnız ettirgen ortaya koyma ve görünür kılma eylemine odaklanır.","gloss":"görünür kılma ile görünme","neighbor_only":"Komşu dal, bir şeyin kendiliğinden görünür hale gelmesini ve görünüşe dayalı değerlendirmeyi de kapsar.","neighbor_ref":"root_000097/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak alanı bir şeyin gizli kalmayıp görünür duruma gelmesidir."}],"source_phrase_ar":"الحدث الإبداء (ayn)؛ الحدث الإبداء (tahdhib)","source_summary":"Kaynaklar yalın biçimi bir şeyi ortaya koyma ve görünür kılma olarak aynı kısa tanımla açıklar; bu dalda başka bir kullanım ayrılığı verilmez.","sources":["AY","TA"],"what_is_ar":"يدخل فيه الحدث بمعنى الإبداء والإظهار كما نصت عليه المصادر.","what_is_not_ar":"لا يدخل فيه الإحداث بمعنى الإيجاد العام إلا إذا كان النص يفسره بالإبداء."},"support_links":["sup_5228e92c4e5d19966f17"]},{"boundary":"Dal konuşma alışverişini değil, kılıcı cilalama işlemini ve bunun öğütle iç dünyayı arındırmaya taşınan kullanımını anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000299/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تُحَدِّثُ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:tuHad~ivu|ROOT:Hdv|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:4:2:1","qac_word_ref":"99:4:2","surface_ar":"تُحَدِّثُ"}],"gloss":"parlatıp arındırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kılıcın yüzeyi cilalanarak parlak ve temiz hale getirilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Somut cilalama, öğütlerle yürekteki birikmiş kiri giderme ve iç dünyayı yenileme anlatımına taşınır."}}],"root_ar":"ح د ث","root_id":"root_000299","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kılıcın somut olarak cilalanmasını ve yüreğin öğütlerle benzetmeli biçimde temizlenmesini birlikte taşır.","boundary_detail":"Dal konuşma alışverişini değil, kılıcı cilalama işlemini ve bunun öğütle iç dünyayı arındırmaya taşınan kullanımını anlatır.","branch_image_ar":"جلاء السيف والقلب بالصقال","concept_gloss":"parlatıp arındırma","contextual_glosses":[{"applicability":"Metal yüzeyin işlenerek parlak ve temiz hale getirildiği somut kullanımlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öğütlerle yüreği arındıran benzetmeli kullanımı kapsamaz.","preserves":"Kılıç üzerindeki somut cilalama ve parlatma işlemini korur."},"facet_ids":["F001"],"text":"kılıcı parlatıp cilalamak","usage_role":"contextual"},{"applicability":"İç dünyadaki körelme ve birikmiş kirin öğütlerle giderildiğini anlatan benzetmeli kullanıma uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kılıç üzerindeki gerçek parlatma işlemini doğrudan belirtmez.","preserves":"Somut cilalamanın iç temizliğe aktarılan arındırma yönünü korur."},"facet_ids":["F002"],"text":"yürekleri öğütlerle arındırmak","usage_role":"explanatory"}],"definition":"Kılıcı parlatıp cilalama işlemidir; yürekler için benzetmeli olarak, öğütlerle biriken kiri giderip iç dünyayı arındırmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kılıcın yüzeyi cilalanarak parlak ve temiz hale getirilir."},{"facet_id":"F002","role":"extension","statement":"Somut cilalama, öğütlerle yürekteki birikmiş kiri giderme ve iç dünyayı yenileme anlatımına taşınır."}],"identity_rationale":"Kaynak ifadesi kılıcı parlatıp cilalamayı açıkça verir ve aynı eylemi yüreğin biriken kirini öğütlerle giderme anlatımına taşır. Dal çerçevesi metal üzerindeki somut işlemi ve buna bağlı iç arınma benzetmesini doğru ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"kılıcı parlatıp cilalama"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"adam kılıcını parlattı ve cilaladı"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"bu yürekleri öğütlerle arındırın"}],"lexicalization_note":"Tanım kılıçla kurulan yapıdaki cilalamayı ve yüreklerle kurulan yapıdaki benzetmeli arındırmayı ayrı yönler olarak korur; bunlardan genel bir konuşma anlamı çıkarmaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; aynı kılıç işlemi, genel arıtma, doğrudan iç temizliği ve bileme karşılaştırmaları dalın iki yönünü açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Kılıç bakımından anlamlar örtüşür; odak dal iç arınma benzetmesine, komşu dal ise görmeyi açan göz sürmesine doğru genişler.","focus_only":"Odak dal, kılıç cilalamayı yüreğin öğütlerle arındırılması yönüne de taşır.","gloss":"kılıç cilalama","neighbor_only":"Komşu dal, kılıcın yanında gözü daha iyi görür hale getiren sürme kullanımını da kapsar.","neighbor_ref":"root_000256/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da kılıcın yüzeyini işleyip parlak hale getirme eylemini aynı çekirdekte taşır."},{"boundary_match":"partial","distinction":"Odak dalın somut temeli kılıç yüzeyini cilalamaktır; komşu dal nesne türü ve işlem yolu bakımından daha genel temizleme ve arıtmadır.","focus_only":"Odak dal, somut işlemi özellikle kılıç cilalamayla sınırlar ve yüreğe benzetme yoluyla taşır.","gloss":"cilalama ile genel arıtma","neighbor_only":"Komşu dal, herhangi bir şeyi karışım, kir veya bulanıklıktan ayırıp genel olarak arıtmayı kapsar.","neighbor_ref":"root_000430/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da kir veya donukluğu gidererek daha temiz ve parlak bir duruma ulaştırır."},{"boundary_match":"partial","distinction":"Odak dal iç temizliğini kılıç cilalamadan taşınan bir benzetmeyle kurar; komşu dalda temizleme ve kusurdan kurtarma doğrudan çekirdektir.","focus_only":"Odak dalda kılıç cilalama asıl işlemdir ve iç arınma bu somut işlemin benzetmeli uzantısıdır.","gloss":"cilalama ile iç temizliği","neighbor_only":"Komşu dal, kusurdan, karışımdan veya yanlış davranışın yükünden kurtarıp temizlemeyi doğrudan anlatır.","neighbor_ref":"root_001400/B001","relation_type":"near_neighbor","shared_zone":"İki dal da kir, kusur veya iç yükün giderilmesi sonucunda arınmayı anlatabilir."},{"boundary_match":"field_only","distinction":"Cilalama yüzeyin temizliği ve parlaklığıyla, bileme ise kesici ağzın inceltilip keskinleştirilmesiyle ilgilidir.","focus_only":"Odak dal, kılıcın yüzeyini parlatıp cilalar; keskinlik kazandırmak zorunlu değildir.","gloss":"cilalama ile bileme","neighbor_only":"Komşu dal, demirin veya bıçağın ağzını işleyerek keskin hale getirmeye odaklanır.","neighbor_ref":"root_001675/B009","relation_type":"same_field","shared_zone":"Her iki dal da kılıç veya başka bir metal aracın yüzeyine uygulanan bakım işlemleridir."}],"source_phrase_ar":"محادثة السيف جلاؤه (sihah)؛ أحدث الرجل سيفه وحادثه إذا جلاه وحادثوا هذه القلوب أي اجلوها بالمواعظ (tahdhib)","source_summary":"Kaynaklar kılıcı cilalayıp parlatma anlamında birleşir; ayrıca aynı işlemi, çabuk körelen yürekleri öğütlerle temizleme ve yeniden canlı tutma anlatımına uygular.","sources":["SI","TA"],"what_is_ar":"يدخل فيه محادثة السيف أو إحداثه بمعنى جلائه وصقله، واستعماله في القلوب بمعنى تنقيتها بالمواعظ من الدثور والصدأ.","what_is_not_ar":"لا يدخل فيه الحديث بمعنى المحاورة، رغم اشتراك صيغة حادث."},"support_links":[]},{"boundary":"Dal, genel zekâyı veya konuşkanlığı değil, doğru çıkan güçlü sezişi ve insanın içine kendiliğinden doğan doğru yönlendirmeyi anlatır.","branch_kind":"bare","branch_ref":"root_000299/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تُحَدِّثُ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:tuHad~ivu|ROOT:Hdv|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:4:2:1","qac_word_ref":"99:4:2","surface_ar":"تُحَدِّثُ"}],"gloss":"doğru sezişli, içine esin doğan kimse","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin sezisi güvenilir ve çoğu kez doğru çıkar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin içine göksel bir kaynaktan doğru bir düşünce veya yönlendirme doğar."}}],"root_ar":"ح د ث","root_id":"root_000299","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem doğru sezme niteliğini hem de insanın içine kendiliğinden doğan doğru yönlendirmeyi birlikte karşılar.","boundary_detail":"Dal, genel zekâyı veya konuşkanlığı değil, doğru çıkan güçlü sezişi ve insanın içine kendiliğinden doğan doğru yönlendirmeyi anlatır.","branch_image_ar":"إلقاء معنى صادق في الروع","concept_gloss":"doğru sezişli, içine esin doğan kimse","contextual_glosses":[{"applicability":"Bir kişinin sezilerinin güvenilir ve doğru çıktığını anlatan nitelemelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İçine göksel kaynaktan doğru düşünce doğması açıklamasını açıkça taşımaz.","preserves":"Kişinin güçlü ve doğru çıkan sezişini korur."},"facet_ids":["F001"],"text":"sezgisi doğru kimse","usage_role":"general"},{"applicability":"Kişinin içine dışarıdan öğretilmeden doğru bir yönlendirme doğduğunun anlatıldığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin genel olarak güvenilir ve doğru sezili olmasını tek başına belirtmez.","preserves":"Doğru düşüncenin kişinin içine kendiliğinden doğması yönünü korur."},"facet_ids":["F002"],"text":"içine doğru bir düşünce doğan kimse","usage_role":"explanatory"}],"definition":"Güçlü ve doğru seziş sahibi olan ya da içine göksel bir kaynaktan doğru bir düşünce doğan kimsedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin sezisi güvenilir ve çoğu kez doğru çıkar."},{"facet_id":"F002","role":"specialization","statement":"Kişinin içine göksel bir kaynaktan doğru bir düşünce veya yönlendirme doğar."}],"identity_rationale":"Kaynak ifadesi doğru sezişli kişiyi ve içine göksel bir kaynaktan doğru bir anlam doğan kimseyi aynı nitelemede birleştirir. Dal çerçevesi bunu yeni yaratılmış olma veya çok konuşma anlamlarından ayırarak doğru biçimde sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"doğru sezili veya içine doğru düşünce doğan kimse"}],"lexicalization_note":"Bu yalın dal doğru sezişli ve içine doğru düşünce doğan kişiyi niteler; aynı biçimin yenilik, yaratılmışlık veya konuşma anlamları buraya alınmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; hiçbiri doğru seziş ile içe doğan göksel yönlendirme sınırını anlamlı bir karşıtlıkla keskinleştirmedi.","source_phrase_ar":"الرجل الصادق الظن محدث بفتح الدال مشددة (sihah)؛ إن يكن في هذه الأمة محدث فهو عمر وإنما يعني من يلقى في روعه من جهة الملإ الأعلى شيء (mufradat)","source_summary":"Kaynaklar doğru çıkan güçlü sezişi ve insanın içine yüce bir kaynaktan doğru düşünce doğmasını aynı kişi niteliğinin iki açıklaması olarak verir.","sources":["SI","MU"],"what_is_ar":"يدخل فيه المحدث بمعنى الصادق الظن أو من يلقى في روعه شيء من جهة الملإ الأعلى.","what_is_not_ar":"ليس المراد المحدث بمعنى المخلوق أو الجديد، ولا المتكلم الكثير الحديث."},"support_links":[]},{"boundary":"Çekirdek, bilgi edinme ve iletmenin yanı sıra sınayarak iç yüzü tanımayı kapsar; arazi, tarım ve öteki eş sesli dallar buna girmez.","branch_kind":"bare","branch_ref":"root_000387/B001","candidate_links":[{"candidate_id":"cand_8830cab18946c219b3ae","lane":"micro"},{"candidate_id":"cand_2148948467ba4ed8ccf8","lane":"micro"},{"candidate_id":"cand_58b9fbb478d211e8ea25","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَخْبَار","morph_features":"STEM|POS:N|LEM:>axobaAr|ROOT:xbr|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:4:3:1","qac_word_ref":"99:4:3","surface_ar":"أَخْبَارَ"}],"gloss":"bilgi edinme, bildirme ve deneyerek iç yüzü tanıma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey veya olay hakkında edinilen ve aktarılabilen bilgiyi belirtir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Edinilen bilgiyi bir başkasına bildirme ve onun bilgilenmesini sağlama eylemini kapsar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Soru sorarak bilgi aramayı ve bir şeyi sınayıp deneyerek tanımayı kapsar."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir işin iç yüzünü bilen kişiyi ve dış görünüşün karşısındaki gerçek iç niteliği belirtir."}}],"root_ar":"خ ب ر","root_id":"root_000387","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın bilgi, aktarım, araştırma, sınama ve iç niteliği bilme yönlerinin birlikte kastedildiği genel açıklamalarda uygundur.","boundary_detail":"Çekirdek, bilgi edinme ve iletmenin yanı sıra sınayarak iç yüzü tanımayı kapsar; arazi, tarım ve öteki eş sesli dallar buna girmez.","branch_image_ar":"العلم بالخبر وباطن الأمر","concept_gloss":"bilgi edinme, bildirme ve deneyerek iç yüzü tanıma","contextual_glosses":[{"applicability":"Bir kişinin öğrendiği şeyi başkasına iletmesi bağlamında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bilgi arama, sınama, deneyim ve iç niteliği tanıma yönlerini kapsamaz.","preserves":"Bilginin başkasına aktarılması yönünü açık biçimde korur."},"facet_ids":["F002"],"text":"bilgi vermek","usage_role":"contextual"},{"applicability":"Deneyim veya sınama sonucunda bir konunun görünmeyen gerçekliğine hakim olmayı anlatan bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel bilgi aktarımını ve soru sorarak bilgi edinme eylemini dışarıda bırakır.","preserves":"Deneyimle kazanılan derin bilgi ve iç niteliği tanıma yönünü korur."},"facet_ids":["F003","F004"],"text":"işin iç yüzünü bilmek","usage_role":"contextual"}],"definition":"Bir şey hakkında bilgi edinme veya edinilen bilgiyi başkasına iletme; ayrıca sorarak öğrenme, sınama ve deneyim yoluyla bir işin iç yüzünü tanıma alanıdır. Bir kimsenin ya da şeyin dış görünüşünden ayrılan gerçek niteliği de bu bilgi alanının uzantısı olarak belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey veya olay hakkında edinilen ve aktarılabilen bilgiyi belirtir."},{"facet_id":"F002","role":"core","statement":"Edinilen bilgiyi bir başkasına bildirme ve onun bilgilenmesini sağlama eylemini kapsar."},{"facet_id":"F003","role":"specialization","statement":"Soru sorarak bilgi aramayı ve bir şeyi sınayıp deneyerek tanımayı kapsar."},{"facet_id":"F004","role":"extension","statement":"Bir işin iç yüzünü bilen kişiyi ve dış görünüşün karşısındaki gerçek iç niteliği belirtir."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":null,"collision":"Güncel kullanımda çoğunlukla olay bildirimi veya medya içeriğiyle anlaşılır.","fit":"drifted_loanword","loses":"Sınama, deneyim, uzman bilgi ve dış görünüşten ayrılan iç nitelik yönlerini siler.","preserves":"Bir olay hakkında alınan veya iletilen bilgi yönünü korur."},"text":"haber"}],"identity_rationale":"Dalın bilgi ve iç yüz eksenli çerçevesi kaynak ifadesini genel olarak karşılar; ancak anlam yalnızca edinilmiş bilgi değildir. Bilgiyi başkasına iletme, soru sorarak bilgi edinme, sınama ve deneyim yoluyla bir işin iç yüzünü tanıma ile dış görünüşten ayrılan gerçek nitelik de dalın sınırları içinde tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir olay veya durum hakkında edinilen ve aktarılan bilgi"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bilgi vermek; bildirmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir konuyu sorup bilgi edinmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sınama ve deneyimle kazanılan bilgi; iç yüzü tanıma"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"sınayıp deneyerek bilgi sahibi olmuş kişi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bilgili; bir işin iç yüzüne hakim"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"dış görünüşün karşısındaki iç yüz ve gerçek nitelik"}],"lexicalization_note":"Dal yalın biçimlere dayanır; tanım herhangi bir kalıba bağlanmadan bilgi edinme, bildirme, sınama ve iç niteliği bilme alanını kapsar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel bilme, araştırarak bilgi edinme ve gizli olana ulaşma sınırlarını en iyi açıklayan üç karşıtlık yayımlandı, yalnızca aynı senaryoda bulunan veya öteki eş sesli dallara ait adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal, genel bilme ve bildirmeye ek olarak soruşturma, deneyip sınama ve iç yüzü tanıma sınırlarını taşır; bu nedenle tam ikame kurulamaz.","focus_only":"Soruşturma, sınama, deneyimle iç yüzü tanıma ve dış görünüşten ayrılan iç niteliği adlandırma kapsamı vardır.","gloss":"bilmek ve bildirmek","neighbor_only":"Komşu kartı bilgiyi edinme ve başkasına iletme çekirdeğini daha genel bir bilme alanı olarak verir.","neighbor_ref":"root_000473/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyi bilme ve edinilen bilgiyi başkasına aktarma alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu dalın çekirdeği bilgi arama sürecidir; odak dal ise aranan bilginin kendisini, aktarımını ve deneyimle oluşan derin bilgiyi de adlandırır.","focus_only":"Edinilmiş bilgiyi, onu bildirmeyi, deneyime dayalı uzmanlığı ve iç niteliği de kapsar.","gloss":"sorup araştırarak bilgi arama","neighbor_only":"Bilgiye ulaşmak için araştırma, yoklama, gizliyi açığa çıkarma ve soruşturma sürecini öne çıkarır.","neighbor_ref":"root_000085/B002","relation_type":"near_neighbor","shared_zone":"İki dal, soru sorarak veya araştırarak bilinmeyen bir konu hakkında bilgi edinmede buluşur."},{"boundary_match":"partial","distinction":"Odak dalda iç yüz bilgisi geniş bilgi ve deneyim alanının bir uzantısıdır; komşu dalda belirleyici özellik gizli olana ulaşmaktır.","focus_only":"Genel bilgi, bildirme, sınama ve deneyimle öğrenme kapsamı bulunur.","gloss":"gizli olana vakıf olma","neighbor_only":"Özellikle gizli bir şeyi keşfetme ve onu başkasına gösterme yönü bulunur.","neighbor_ref":"root_000982/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da görünmeyen veya içte kalan bir gerçeğin bilinmesiyle ilişkilidir."}],"source_phrase_ar":"الخبر العلم بالشيء (maqayis)؛ الخبر النبأ (ayn)؛ الخبر معروف أخبرت بكذا (jamhara)؛ الاستخبار السؤال عن الخبر (sihah)؛ الخبرة الاختبار (ayn)؛ الخبرة المعرفة ببواطن الأمر (mufradat)؛ الخبير العالم (maqayis;ayn;sihah;mufradat)؛ المخبر خلاف المنظر (sihah)","source_summary":"Kaynakların birleşen tanıklığı, bilgi edinme ve bildirme çekirdeğini soruşturma, sınama, deneyime dayalı bilme ve iç niteliği tanıma yönleriyle genişletir.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الخبر والنبأ والإخبار والاستخبار والخبرة بمعنى الاختبار والمعرفة ببواطن الأمر والخبير العالم والمخبر الباطن لا المنظر","what_is_not_ar":"الأرض اللينة والمخابرة والمزادة والناقة الغزيرة والزبد والوبر والخبرة في الشاة"},"support_links":["sup_03cc034ce401c5f322b2","sup_5228e92c4e5d19966f17","sup_8cef1235becdf6a8de51"]},{"boundary":"Dal, gevşek veya alçak araziyi, bitkili-sulu yeri ve akışla oluşan su birikintisini ayrı fakat bağlantılı yer biçimleri olarak tutar.","branch_kind":"bare","branch_ref":"root_000387/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْبَار","morph_features":"STEM|POS:N|LEM:>axobaAr|ROOT:xbr|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:4:3:1","qac_word_ref":"99:4:3","surface_ar":"أَخْبَارَ"}],"gloss":"gevşek, alçak ve su tutan arazi veya su birikintisi","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gevşek, yumuşak ya da alçak ve yağmur suyunun toplanabildiği araziyi belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sıcak, ağaçlı ve suyu bol bir yer niteliğini belirtir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Akışın oluşturduğu ve insanların içine girip geçebildiği bir su birikintisini belirtir."}}],"root_ar":"خ ب ر","root_id":"root_000387","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Arazi niteliğiyle akışta oluşan su birikintisinin birlikte temsil edilmesi gereken dal düzeyi açıklamalarda uygundur.","boundary_detail":"Dal, gevşek veya alçak araziyi, bitkili-sulu yeri ve akışla oluşan su birikintisini ayrı fakat bağlantılı yer biçimleri olarak tutar.","branch_image_ar":"لين الأرض ومائها","concept_gloss":"gevşek, alçak ve su tutan arazi veya su birikintisi","contextual_glosses":[{"applicability":"Toprağın yumuşaklığı, gevşekliği veya alçaklığı nedeniyle su topladığı arazi bağlamlarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sıcak ve ağaçlı yer ile bağımsız su birikintisi gerçekleşmelerini kapsamaz.","preserves":"Arazinin gevşek, alçak ve su toplayan niteliğini korur."},"facet_ids":["F001"],"text":"gevşek ve su tutan arazi","usage_role":"contextual"},{"applicability":"Suyun bir akış yatağında toplanıp insanların içinden geçebildiği birikinti bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gevşek arazi ile sıcak, ağaçlı ve suyu bol yer niteliklerini dışarıda bırakır.","preserves":"Akışın oluşturduğu geçilebilir su birikintisi yönünü korur."},"facet_ids":["F003"],"text":"akış yatağındaki su birikintisi","usage_role":"contextual"}],"definition":"Gevşek, yumuşak veya alçak olup su toplayabilen araziyi ve sıcak, ağaçlı, suyu bol bir yeri belirtir. Ayrıca akış yatağında oluşup insanların içinden geçebildiği su birikintisini adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gevşek, yumuşak ya da alçak ve yağmur suyunun toplanabildiği araziyi belirtir."},{"facet_id":"F002","role":"specialization","statement":"Sıcak, ağaçlı ve suyu bol bir yer niteliğini belirtir."},{"facet_id":"F003","role":"extension","statement":"Akışın oluşturduğu ve insanların içine girip geçebildiği bir su birikintisini belirtir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kalıcı çamurluluk ve batma tehlikesi gibi kaynakta bulunmayan özellikler ekler.","collision":"Gevşek araziyi ve geçilebilir su birikintisini tek bir sulak alan türüyle karıştırır.","fit":"broadening","loses":null,"preserves":"Alçak ve su toplayan arazi çağrışımını kısmen korur."},"text":"bataklık"}],"identity_rationale":"Kaynak ifadesi yalnızca yumuşak araziyi ve onun suyunu anlatmaz. Gevşek ya da alçak arazi, sıcak ve ağaçlı-sulu yer ile akışın oluşturduğu su birikintisi ayrı gerçekleşmelerdir; dal korunabilir, fakat su birikintisi arazi niteliğinin içine eritilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"gevşek, yumuşak veya alçak olup su toplayan arazi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"sıcak, ağaçlı ve suyu bol yer"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"akış yatağında oluşan geçilebilir su birikintisi"}],"lexicalization_note":"Dal yalın kullanımlara dayanır; tanım belirli bir söz öbeğine bağlanmadan arazi, yer ve su birikintisi gerçekleşmelerini ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; su toplanan çöküntü, alçak-bitkili arazi ve düz-verimli arazi en açıklayıcı sınırları verdi, yağışsızlık veya sulama eylemi gibi karşıt senaryolar ile öteki eş sesli dallar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda su birikintisi daha geniş bir gevşek ve su tutan arazi alanının uzantısıdır; komşu dalın çekirdeği ise belirli çukurlaşmalardaki su toplanmasıdır.","focus_only":"Gevşek veya yumuşak arazi ile sıcak, ağaçlı ve suyu bol yer kapsamı bulunur.","gloss":"çöküntüde toplanan su","neighbor_only":"Suyun özellikle kale çevresi, çöküntü veya büyük çukur gibi yerlerde toplanmasını belirtir.","neighbor_ref":"root_000282/B002","relation_type":"near_neighbor","shared_zone":"İki dal da alçak bir yerde biriken suyu veya böyle bir su birikme alanını kapsar."},{"boundary_match":"partial","distinction":"Odak dalın sınırı gevşeklik ve su tutma çevresinde kurulur; komşu dalda alçaklığın yanında bitki yetiştirme özelliği öne çıkar.","focus_only":"Toprağın gevşekliği, su toplaması ve ayrı bir su birikintisini adlandırma kapsamı vardır.","gloss":"alçak ve bitki bitiren arazi","neighbor_only":"Alçak arazinin bitki yetiştirmesi belirleyici özelliktir.","neighbor_ref":"root_000965/B008","relation_type":"near_neighbor","shared_zone":"Her iki dal da alçalmış ve bitkiyle ilişkili bir arazi biçimini anlatabilir."},{"boundary_match":"field_only","distinction":"Odak dal su ve gevşeklik özellikleriyle, komşu dal ise düzlük ve verimlilik özellikleriyle tanımlanır; olağan bağlamda birbirinin yerine geçmez.","focus_only":"Gevşeklik, alçaklık, su toplama ve akışta oluşan birikinti anlamlarını taşır.","gloss":"düz ve verimli arazi","neighbor_only":"Düzgün ve verimli olup bitkiyi iyi yetiştiren araziyi belirtir.","neighbor_ref":"root_001521/B006","relation_type":"same_field","shared_zone":"İki dal da toprağın yapısını ve bitki yetişmesine elverişli araziyi betimler."}],"source_phrase_ar":"الخبراء الأرض اللينة (maqayis)؛ الخبار أرض رخوة (ayn;sihah)؛ الخبراء الأرض السهلة المنخفضة يجتمع فيها ماء السماء (jamhara)؛ الخبار والخبراء الأرض اللينة (mufradat)؛ مكان خَبِر دفيء كثير الشجر والماء (maqayis)؛ الخبر من مناقع الماء (ayn)","source_summary":"Birleşik tanıklık, yumuşak veya gevşek arazi çekirdeğine alçak ve su tutan yer, sıcak-ağaçlı-sulu mekan ve akışta oluşan su birikintisi gerçekleşmelerini ekler.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الخبراء والخبار والأرض الرخوة أو اللينة أو المنخفضة وما يجتمع فيها من ماء وشجر ومكان خَبِر","what_is_not_ar":"العلم والنبأ والمخابرة والمزادة والناقة الغزيرة والزبد والوبر والخبرة في الشاة"},"support_links":[]},{"boundary":"Dal, çiftçi rolünü ve üründen belirli pay karşılığı yapılan ortakçılığı kapsar; genel ekim, toprak işleme veya ücretli çalışma bununla özdeş değildir.","branch_kind":"bare","branch_ref":"root_000387/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْبَار","morph_features":"STEM|POS:N|LEM:>axobaAr|ROOT:xbr|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:4:3:1","qac_word_ref":"99:4:3","surface_ar":"أَخْبَارَ"}],"gloss":"üründen pay karşılığı ortakçılık ve bunu yapan çiftçi","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Toprağı işleyen ve tarımsal üretimi yürüten çiftçiyi belirtir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Toprağın, elde edilen ürünün yarısı, üçte biri veya belirli bir payı karşılığında işlenmesi düzenini belirtir."}}],"root_ar":"خ ب ر","root_id":"root_000387","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem tarımsal ortakçılık düzeninin hem de toprağı işleyen katılımcının dal düzeyinde birlikte gösterilmesi gerektiğinde uygundur.","boundary_detail":"Dal, çiftçi rolünü ve üründen belirli pay karşılığı yapılan ortakçılığı kapsar; genel ekim, toprak işleme veya ücretli çalışma bununla özdeş değildir.","branch_image_ar":"إصلاح الأرض بالمخابرة","concept_gloss":"üründen pay karşılığı ortakçılık ve bunu yapan çiftçi","contextual_glosses":[{"applicability":"Toprağın, elde edilecek ürünün önceden belirlenen bölümü karşılığında işletilmesi bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Toprağı işleyen kişinin ayrıca adlandırılması yönünü kapsamaz.","preserves":"Tarımsal üretimi ve ürün payına dayalı karşılık koşulunu korur."},"facet_ids":["F002"],"text":"üründen pay karşılığı ortakçılık","usage_role":"contextual"},{"applicability":"Söz konusu üretim düzeninde araziyi ekip biçen kişinin adlandırıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Üründen belirli bir pay karşılığında kurulan ortakçılık düzenini belirtmez.","preserves":"Toprağı işleyen tarımsal üretici rolünü korur."},"facet_ids":["F001"],"text":"toprağı işleyen çiftçi","usage_role":"contextual"}],"definition":"Toprağı işleyip tarımsal üretimi yapan çiftçiyi ve emeğin ya da kullanımın karşılığının topraktan çıkan ürünün yarısı, üçte biri veya önceden belirlenmiş başka bir payı olduğu ortakçılık düzenini belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Toprağı işleyen ve tarımsal üretimi yürüten çiftçiyi belirtir."},{"facet_id":"F002","role":"core","statement":"Toprağın, elde edilen ürünün yarısı, üçte biri veya belirli bir payı karşılığında işlenmesi düzenini belirtir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Karşılığın sabit kira bedeli olduğu farklı bir sözleşme türünü düşündürür.","collision":"Ürün ortakçılığını sıradan arazi kirasıyla karıştırır.","fit":"displacement","loses":"Karşılığın elde edilen üründen belirli bir pay olması koşulunu siler.","preserves":"Arazinin başka bir kişi tarafından işletilmesi ilişkisini kısmen korur."},"text":"tarla kiralama"}],"identity_rationale":"Kaynak ifadesinin çekirdeği genel olarak toprağı iyileştirmek değil, toprağı işleyen çiftçi ile ürünün yarısı, üçte biri veya başka belirli bir payı karşılığında yapılan tarımsal ortakçılıktır. Dal korunabilir, ancak tanım işleme eyleminden çok paya dayalı üretim düzenine bağlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"toprağı işleyen çiftçi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ürünün belirli bir payı karşılığında yapılan tarımsal ortakçılık"}],"lexicalization_note":"Dal yalın biçimlere dayanır; çiftçi adını ve belirli ürün payına bağlı tarımsal ortakçılığı özel bir kalıba genellemeden birlikte açıklar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel tarımsal ortakçılık, çiftçi adı ve toprağı işleme eylemiyle kurulan üç sınır yayımlandı, ücret, ürün artışı ve genel edinme gibi daha uzak ilişkiler elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal, genel ortakçılık alanını ürün payının belirlenmesi ve toprağı işleyen kişiyle sınırlar; komşu kart bu ayrıntıları zorunlu kılmaz.","focus_only":"Toprağı işleyen kişiyi adlandırır ve karşılığın üründen yarım, üçte bir veya belirlenmiş bir pay olmasını açıkça içerir.","gloss":"tarımsal ortakçılık","neighbor_only":"Tarımsal ortakçılığı bilinen genel adıyla verir, fakat kartta belirli pay koşulu veya çiftçi rolü açıklanmaz.","neighbor_ref":"root_000630/B003","relation_type":"near_synonym","shared_zone":"İki dal da tarımsal üretimin paylaşım ilişkisi içinde yürütülmesini anlatır."},{"boundary_match":"field_only","distinction":"Odak dalın ayırıcı yönü ürün paylaşımına dayalı üretim ilişkisidir; komşu dal yalnızca çiftçi grubunu veya üyesini adlandırır.","focus_only":"Ürün payına dayalı ortakçılık düzenini ve bu düzende toprağı işleyen tekil rolü kapsar.","gloss":"çiftçiler","neighbor_only":"Bir çiftçi topluluğunu ve topluluğun bir üyesini adlandıran ayrı bir kişi adıdır.","neighbor_ref":"root_001003/B012","relation_type":"same_field","shared_zone":"Her iki dal tarımsal üretimi yapan çiftçileri adlandırma alanında buluşur."},{"boundary_match":"field_only","distinction":"Komşu dal fiziksel toprak işleme eylemine, odak dal ise bu işi yapan kişi ile ürün paylaşımına dayalı toplumsal düzene odaklanır.","focus_only":"Çiftçi rolünü ve üründen pay karşılığı kurulan üretim düzenini belirtir.","gloss":"toprağı sürüp ekime hazırlama","neighbor_only":"Toprağı sürme, kabartma ve ekime hazırlama eylemini belirtir.","neighbor_ref":"root_000384/B007","relation_type":"same_field","shared_zone":"İki dal toprağın tarımsal üretim amacıyla işlenmesi alanında yer alır."}],"source_phrase_ar":"الخبير الأكار (maqayis;ayn;sihah;mufradat)؛ المخابرة المزارعة بالنصف أو الثلث (maqayis)؛ الخبر والمخابرة أن تزرع على النصف أو الثلث (ayn)؛ المخابرة مزارعة الخبار بشيء معلوم (mufradat)؛ المزارعة ببعض ما يخرج من الأرض (sihah)","source_summary":"Birleşik tanıklık, toprağı işleyen kişi adını ürünün yarısı, üçte biri veya belirlenmiş başka bir payı karşılığında yapılan tarımsal ortakçılıkla ilişkilendirir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الخبير بمعنى الأكار والمخابرة والمؤاكرة والمزارعة بجزء معلوم مما يخرج من الأرض","what_is_not_ar":"الخبر بمعنى العلم والأرض نفسها والمزادة والناقة والزبد والوبر والخبرة في الشاة"},"support_links":[]},{"boundary":"Çekirdek büyük su tulumudur; bol verimli dişi deve, kabın genişlik ve doluluk özelliğine dayanan benzetmeli uzantıdır.","branch_kind":"bare","branch_ref":"root_000387/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْبَار","morph_features":"STEM|POS:N|LEM:>axobaAr|ROOT:xbr|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:4:3:1","qac_word_ref":"99:4:3","surface_ar":"أَخْبَارَ"}],"gloss":"büyük su tulumu ve bolluğuyla ona benzetilen dişi deve","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Büyük ve geniş bir su tulumunu belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bol sütü veya verimi nedeniyle büyük su tulumuna benzetilen dişi deveyi belirtir."}}],"root_ar":"خ ب ر","root_id":"root_000387","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Temel kap anlamı ile benzetmeye dayalı dişi deve uzantısının birlikte gösterildiği dal düzeyi açıklamada uygundur.","boundary_detail":"Çekirdek büyük su tulumudur; bol verimli dişi deve, kabın genişlik ve doluluk özelliğine dayanan benzetmeli uzantıdır.","branch_image_ar":"الغزر في المزادة والناقة","concept_gloss":"büyük su tulumu ve bolluğuyla ona benzetilen dişi deve","contextual_glosses":[{"applicability":"Suyun taşındığı veya saklandığı büyük ve geniş deri kabın doğrudan adlandırıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bolluk benzetmesiyle adlandırılan dişi deve uzantısını kapsamaz.","preserves":"Dalın temel büyük kap anlamını eksiksiz korur."},"facet_ids":["F001"],"text":"büyük su tulumu","usage_role":"contextual"},{"applicability":"Dişi devenin verimi ve içindeki bolluk bakımından büyük kaba benzetildiği hayvancılık bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Benzetmenin temelindeki büyük su tulumunu doğrudan adlandırmaz.","preserves":"Benzetmeye dayanan bol verimli dişi deve anlamını korur."},"facet_ids":["F002"],"text":"bol sütlü dişi deve","usage_role":"contextual"}],"definition":"Büyük ve geniş bir su tulumunu belirtir. Çok verimli ve bol sütlü dişi deve, içindeki bolluk ve genişlik bakımından bu kaba benzetilerek aynı adla anılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Büyük ve geniş bir su tulumunu belirtir."},{"facet_id":"F002","role":"extension","statement":"Bol sütü veya verimi nedeniyle büyük su tulumuna benzetilen dişi deveyi belirtir."}],"identity_rationale":"Kaynak ifadesi büyük ve geniş bir su tulumunu temel referent olarak verir; bol verimli dişi deve de içindeki bolluk bakımından bu kaba benzetilerek aynı adla anılır. Sağlanan çerçeve hem temel nesneyi hem benzetmeye dayalı uzantıyı doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"büyük ve geniş su tulumu"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bolluğu ve verimiyle büyük su tulumuna benzetilen dişi deve"}],"lexicalization_note":"Dal yalın adlandırmalara dayanır; tanım büyük su tulumunu temel alır ve dişi deve anlamını benzetmeye bağlı bir uzantı olarak sınırlar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; büyük su kabı, bol sütlü dişi deve ve genel dolulukla kurulan üç yakın sınır yayımlandı, yalnızca bitki yoğunluğu veya süt çıkışı gibi daha uzak adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın kabı geniş bir su tulumudur ve deve uzantısı benzetmelidir; komşu dal büyük kova ile su taşıyıcısı çevresinde kurulur.","focus_only":"Büyük deri su tulumunu ve ona benzetilen bol verimli dişi deveyi kapsar.","gloss":"büyük su kovası ve su taşıyıcısı","neighbor_only":"Büyük kova ile su taşıyan hayvan veya taşıma düzeneği anlamlarını kapsar.","neighbor_ref":"root_001077/B002","relation_type":"near_neighbor","shared_zone":"İki dal da su taşımaya yarayan büyük bir kabı adlandırır."},{"boundary_match":"partial","distinction":"Odak dalda bolluk büyük su tulumu benzetmesiyle ifade edilir; komşu dalda belirleyici özellik sütün uzun süre birikmiş olmasıdır.","focus_only":"Dişi deveyi büyük su tulumuna benzetir ve temel olarak bu kabı da adlandırır.","gloss":"uzun süre süt biriktiren dişi deve","neighbor_only":"Sütün uzun süre birikmesiyle memesi dolu kalan dişi deveyi belirtir.","neighbor_ref":"root_000752/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da süt bolluğu veya uzun süreli dolulukla nitelenen dişi deveyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal belirli bir kap türü ile benzetmeli hayvan adıdır; komşu dal ise çeşitli nesnelere uygulanabilen genel doluluk niteliğidir.","focus_only":"Belirli bir büyük su kabını ve bu kaba benzetilen dişi deveyi adlandırır.","gloss":"bütünüyle dolu olma","neighbor_only":"Kabın türünden bağımsız olarak bir yerin veya nesnenin bütünüyle dolu olmasını belirtir.","neighbor_ref":"root_000945/B007","relation_type":"near_neighbor","shared_zone":"İki dal geniş bir kabın doluluğu ve çok miktarda içerik taşıması düşüncesinde kesişir."}],"source_phrase_ar":"الخبر المزادة العظيمة (maqayis;sihah;mufradat)؛ المزادة العظيمة والجمع خبور (jamhara)؛ الناقة الغزيرة خَبْر (maqayis;jamhara)؛ تشبه بها الناقة في غزرها فتسمى خبراء (sihah)؛ شبهت بها الناقة فسميت خَبْرا (mufradat)","source_summary":"Kaynakların birleşen tanıklığı büyük su tulumunu temel anlam olarak verir ve bol verimli dişi deve adını bu kabın genişliği ile doluluğuna dayanan bir benzetme olarak açıklar.","sources":["MQ","JA","SI","MU"],"what_is_ar":"يدخل فيه الخَبْر للمزادة العظيمة وتشبيه الناقة الغزيرة بها في السعة والغزر","what_is_not_ar":"العلم والنبأ والأرض والمخابرة والزبد والوبر والخبرة في الشاة"},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"bare","branch_ref":"root_000387/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْبَار","morph_features":"STEM|POS:N|LEM:>axobaAr|ROOT:xbr|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:4:3:1","qac_word_ref":"99:4:3","surface_ar":"أَخْبَارَ"}],"gloss":"yumuşak bitki, yün veya ince kıl ve deve ağzı köpüğü","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kesilip yenebilen yumuşak bitkiyi belirtir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yünü veya ince ve yumuşak hayvan kılını belirtir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Devenin ağzında oluşan ya da ağzından attığı köpüğü belirtir."}}],"root_ar":"خ ب ر","root_id":"root_000387","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kanıttaki sınırlı adlandırma kümesinin üç referentini birlikte göstermek gerektiğinde uygundur; tek üretken çekirdek iddiası taşımaz.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"اللِّين في النبات والوبر والزبد","concept_gloss":"yumuşak bitki, yün veya ince kıl ve deve ağzı köpüğü","contextual_glosses":[{"applicability":"Sözcüğün yumuşak ve yenebilir bitkiyi adlandırdığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yün veya ince kıl ile deve ağzı köpüğü referentlerini kapsamaz.","preserves":"Yumuşak bitki referentini ve yenebilme bağlamını korur."},"facet_ids":["F001"],"text":"kesilip yenebilen yumuşak bitki","usage_role":"contextual"},{"applicability":"Sözcüğün hayvan üzerindeki yün ya da ince kılı adlandırdığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yumuşak bitki ile deve ağzı köpüğü referentlerini kapsamaz.","preserves":"Yün veya ince hayvan kılı referentini korur."},"facet_ids":["F002"],"text":"yün veya ince hayvan kılı","usage_role":"contextual"},{"applicability":"Sözcüğün devenin ağzında oluşan veya ağzından atılan köpüğü adlandırdığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yumuşak bitki ile yün veya ince hayvan kılı referentlerini kapsamaz.","preserves":"Deve ağzındaki köpük referentini açık biçimde korur."},"facet_ids":["F003"],"text":"devenin ağzından çıkan köpük","usage_role":"contextual"}],"definition":"Kaynak tanıklığında aynı yalın biçim, yumuşak bitkiyi, yün veya ince hayvan kılını ve devenin ağzından çıkan köpüğü ayrı ayrı adlandırır. Bu referentler için kaynakça desteklenen tek bir ortak kavramsal çekirdek kurulamaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kesilip yenebilen yumuşak bitkiyi belirtir."},{"facet_id":"F002","role":"source_variant","statement":"Yünü veya ince ve yumuşak hayvan kılını belirtir."},{"facet_id":"F003","role":"source_variant","statement":"Devenin ağzında oluşan ya da ağzından attığı köpüğü belirtir."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kesilip yenebilen yumuşak bitki"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"yün veya ince hayvan kılı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"devenin ağzında oluşan veya ağzından çıkan köpük"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"الخبير النبات اللين (maqayis)؛ الخبير النبات (sihah)؛ الخبير الوبر (maqayis;sihah)؛ الخبير زبد أفواه الإبل (sihah)؛ الخبير الزبد الذي يلقيه البعير من فيه (jamhara)","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["MQ","JA","SI"],"what_is_ar":"يدخل فيه الخبير للنبات اللين والوبر وزبد أفواه الإبل أو ما يلقيه البعير من فيه","what_is_not_ar":"العلم والنبأ والأرض والمخابرة والمزادة والناقة والخبرة في الشاة"},"support_links":[]},{"boundary":"Dal, ortak alım-kesim-bölüşüm sürecine konu olan koyunu ve bu tür bölüşümden alınan et veya balık payını kapsar.","branch_kind":"bare","branch_ref":"root_000387/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَخْبَار","morph_features":"STEM|POS:N|LEM:>axobaAr|ROOT:xbr|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:4:3:1","qac_word_ref":"99:4:3","surface_ar":"أَخْبَارَ"}],"gloss":"ortak alınıp kesilen koyun veya bölüşülen et-balık payı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun ortaklaşa satın alıp kestiği ve etini kendi arasında bölüştüğü koyunu belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir bölüşüm sonucunda kişiye düşen et veya balık payını belirtir."}}],"root_ar":"خ ب ر","root_id":"root_000387","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ortak alım, kesim ve bölüşüme konu olan koyunla bundan doğan yiyecek payının birlikte gösterildiği dal düzeyi açıklamada uygundur.","boundary_detail":"Dal, ortak alım-kesim-bölüşüm sürecine konu olan koyunu ve bu tür bölüşümden alınan et veya balık payını kapsar.","branch_image_ar":"القسمة في الشاة واللحم","concept_gloss":"ortak alınıp kesilen koyun veya bölüşülen et-balık payı","contextual_glosses":[{"applicability":"Bir topluluğun koyunu birlikte satın alıp kesmesi ve etini kendi arasında paylaşması bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Etten veya balıktan alınan genel pay uzantısını kapsamaz.","preserves":"Ortak alım, kesim ve etin katılımcılar arasında bölüşülmesi sürecini korur."},"facet_ids":["F001"],"text":"ortak alınıp eti bölüşülen koyun","usage_role":"contextual"},{"applicability":"Bir bölüşüm sonunda kişiye düşen et ya da balık bölümünün adlandırıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Koyunun ortaklaşa satın alınması, kesilmesi ve bütün etinin paylaşılması olayını kapsamaz.","preserves":"Bölüşüm sonucunda alınan yiyecek payını korur."},"facet_ids":["F002"],"text":"et veya balıktan alınan pay","usage_role":"contextual"}],"definition":"Bir topluluğun ortaklaşa satın aldığı, kestiği ve etini aralarında paylaştığı koyunu belirtir. Bununla bağlantılı olarak, bölüşümde bir kişinin etten veya balıktan aldığı payı da adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun ortaklaşa satın alıp kestiği ve etini kendi arasında bölüştüğü koyunu belirtir."},{"facet_id":"F002","role":"extension","statement":"Bir bölüşüm sonucunda kişiye düşen et veya balık payını belirtir."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":"Mülkiyet, şirket ortaklığı veya soyut hak payı gibi çok daha geniş kullanım alanları ekler.","collision":"Ortak kesim olayını ve payın et ya da balık olması koşulunu belirsizleştirir.","fit":"broadening","loses":null,"preserves":"Bir bölüşümde kişiye düşen pay yönünü korur."},"text":"hisse"}],"identity_rationale":"Kaynak ifadesi, bir topluluğun ortaklaşa satın alıp kestiği ve etini bölüştüğü koyunu temel olaylı referent olarak verir; etten veya balıktan alınan pay bunun bölüşüm sonucunu genelleştiren bağlantılı anlamıdır. Sağlanan çerçeve süreç, nesne ve sonuç ayrımını korumaya elverişlidir.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"ortaklaşa alınıp kesilen ve eti bölüşülen koyun"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"et veya balıktan alınan pay"}],"lexicalization_note":"Dal yalın biçimlere dayanır; tanım ortaklaşa alınan koyun ile bölüşümden doğan et veya balık payını aşamalı olarak ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel belirlenmiş pay, kesimde ilk ayrılan et payı ve oranlı bölümle kurulan üç sınır yayımlandı, yalnızca et türü veya miras bölüşümüyle ilgili daha uzak adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yiyecek payını ortak koyun kesimiyle bağlantılı olarak sınırlar; komşu dal nesne türünden ve kesim sürecinden bağımsız genel pay kavramıdır.","focus_only":"Ortak alınan koyun, kesim ve payın özellikle etten veya balıktan alınması koşulları bulunur.","gloss":"kişiye ayrılan belirli pay","neighbor_only":"Herhangi bir şeyden bir kişiye ayrılmış belirli hakkı veya bölümü genel olarak belirtir.","neighbor_ref":"root_001507/B005","relation_type":"near_synonym","shared_zone":"İki dal da bölüşülen bir şeyden belirli bir kişiye düşen bölümü adlandırır."},{"boundary_match":"partial","distinction":"Odak dalda payın ilk olması veya büyük bir parça olması gerekmez ve balığı da kapsar; komşu dal ilk ayrılma ve deve eti özellikleriyle sınırlıdır.","focus_only":"Ortak satın alınan koyunun tamamını ve et ya da balık payını kapsar.","gloss":"bölüşümde ilk ayrılan et payı","neighbor_only":"Bölüşümde ilk ayrılan payı ve özellikle büyük bir deve eti parçasını belirtir.","neighbor_ref":"root_000090/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da kesilmiş hayvan etinin bölüşümünde bir kişiye ayrılan payı anlatır."},{"boundary_match":"field_only","distinction":"Odak dal yiyecek türü ve ortak kesim süreciyle, komşu dal ise payın kesin oranıyla tanımlanır; biri diğerinin yerine geçmez.","focus_only":"Ortak koyun kesimi ile et veya balık olarak alınan payı belirtir.","gloss":"üçte birlik bölüm","neighbor_only":"Herhangi bir şeyin tam üçte birini veya üçte ikisini oran olarak belirtir.","neighbor_ref":"root_000203/B002","relation_type":"same_field","shared_zone":"İki dal da bir bütünün bölünmesi ve bir bölümün ayrılması alanında yer alır."}],"source_phrase_ar":"الخُبْرة الشاة يشتريها القوم يذبحونها ويقتسمون لحمها (maqayis)؛ تخبر القوم بينهم خبرة إذا اشتروا شاة فذبحوها واقتسموا لحمها (jamhara)؛ الخبرة النصيب تأخذه من سمك أو لحم (sihah)","source_summary":"Birleşik tanıklık ortaklaşa koyun satın alma, kesme ve eti bölüşme sürecini verir; etten veya balıktan alınan pay da bu bölüşüm çekirdeğinin sonuçsal uzantısıdır.","sources":["MQ","JA","SI"],"what_is_ar":"يدخل فيه الخُبْرة للشاة المشتركة التي يذبحها القوم ويقتسمون لحمها أو للنصيب من اللحم والسمك","what_is_not_ar":"العلم والنبأ والأرض والمخابرة والمزادة والناقة والزبد والوبر"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["99:4:1"],"branch_refs":[],"candidate_id":"cand_9b996f4c9aa88c3a5e02","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:4:1:backward-deictic-compression","source_type":"word_analysis","support_ids":["sup_235bf1dab9eb6d5cc8a3","sup_ce2dffe4b089ccb5fc82"],"title":"compressed pointer to the prior event","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:4:1","qac_refs":["99:4:1:1"],"status":"accepted"}},{"anchor_refs":["99:4:1"],"branch_refs":[],"candidate_id":"cand_11ed1c4e1c15c526bc83","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:4:1:day-disclosure-formula","source_type":"word_analysis","support_ids":["sup_9a6141904b49e79fd827","sup_ce2dffe4b089ccb5fc82"],"title":"Day-scene formula and same-surah hinge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:4:1","qac_refs":["99:4:1:1"],"status":"accepted"}},{"anchor_refs":["99:4:1"],"branch_refs":[],"candidate_id":"cand_df496375f3b3abcf6fcb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:4:1:decisive-interval-range","source_type":"word_analysis","support_ids":["sup_27272902f9d1900b4e00","sup_ce2dffe4b089ccb5fc82"],"title":"event-day range becomes a disclosure interval","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:4:1","qac_refs":["99:4:1:1"],"status":"accepted"}},{"anchor_refs":["99:4:1"],"branch_refs":[],"candidate_id":"cand_6fbc4419eb1181a97b9b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:4:1:fronted-temporal-frame","source_type":"word_analysis","support_ids":["sup_b22f029a1077e5aa6da9","sup_ce2dffe4b089ccb5fc82"],"title":"fronted time-adverb governs the clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:4:1","qac_refs":["99:4:1:1"],"status":"accepted"}},{"anchor_refs":["99:4:1"],"branch_refs":[],"candidate_id":"cand_b5931a0a8294c5af1d77","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:4:1:sound-and-boundary-reset","source_type":"word_analysis","support_ids":["sup_9944c96899f3154993be","sup_ce2dffe4b089ccb5fc82"],"title":"audible hinge from question to disclosure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:4:1","qac_refs":["99:4:1:1"],"status":"accepted"}},{"anchor_refs":["99:4:2"],"branch_refs":[],"candidate_id":"cand_ea0c5196f86ca6c47756","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000299"],"scope":"focus_ayah","source_local_id":"99:4:2:boundary-and-forward-bridge","source_type":"word_analysis","support_ids":["sup_38f5592cd2be67b30119","sup_b1fb9381f15da025e058"],"title":"earth takes over and points to the next cause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:4:2","qac_refs":["99:4:2:1"],"status":"accepted"}},{"anchor_refs":["99:4:2"],"branch_refs":[],"candidate_id":"cand_d9d7b587855f9b265d60","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000299"],"scope":"focus_ayah","source_local_id":"99:4:2:compact-disclosure-clause","source_type":"word_analysis","support_ids":["sup_8def9c9c357ba755711c","sup_b1fb9381f15da025e058"],"title":"verb binds telling to report-content","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:4:2","qac_refs":["99:4:2:1"],"status":"accepted"}},{"anchor_refs":["99:4:2"],"branch_refs":[],"candidate_id":"cand_3c30109a43504ec2c7f7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000299"],"scope":"focus_ayah","source_local_id":"99:4:2:feminine-prodrop-earth-subject","source_type":"word_analysis","support_ids":["sup_6786a83be450098be4cc","sup_b1fb9381f15da025e058"],"title":"feminine agreement carries the earth as subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:4:2","qac_refs":["99:4:2:1"],"status":"accepted"}},{"anchor_refs":["99:4:2"],"branch_refs":[],"candidate_id":"cand_cb3cfb6682f90aaf40d0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000299"],"scope":"focus_ayah","source_local_id":"99:4:2:forceful-sound-texture","source_type":"word_analysis","support_ids":["sup_03cad2a44ee0d7a227e2","sup_b1fb9381f15da025e058"],"title":"doubled middle sound reinforces intensity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:4:2","qac_refs":["99:4:2:1"],"status":"accepted"}},{"anchor_refs":["99:4:2"],"branch_refs":[],"candidate_id":"cand_1d445495dd13873a29c2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000299"],"scope":"focus_ayah","source_local_id":"99:4:2:form-ii-event-to-report","source_type":"word_analysis","support_ids":["sup_4f1f7ecb57c6986086f5","sup_b1fb9381f15da025e058"],"title":"Form II turns occurrence into narration","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:4:2","qac_refs":["99:4:2:1"],"status":"accepted"}},{"anchor_refs":["99:4:2"],"branch_refs":[],"candidate_id":"cand_6ee730eb16ca81eca63f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000299"],"scope":"focus_ayah","source_local_id":"99:4:2:imperfect-unfolding-answer","source_type":"word_analysis","support_ids":["sup_4226544125256173fb10","sup_b1fb9381f15da025e058"],"title":"imperfect narration follows completed question","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:4:2","qac_refs":["99:4:2:1"],"status":"accepted"}},{"anchor_refs":["99:4:2"],"branch_refs":[],"candidate_id":"cand_8cb640fa997b53cbdf6c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000299"],"scope":"focus_ayah","source_local_id":"99:4:2:rare-reporting-field","source_type":"word_analysis","support_ids":["sup_b1fb9381f15da025e058","sup_b34ffaac87c7281955b8"],"title":"finite reporting joins wider disclosure field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:4:2","qac_refs":["99:4:2:1"],"status":"accepted"}},{"anchor_refs":["99:4:2"],"branch_refs":[],"candidate_id":"cand_e966475a8cade6e91c7e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000299"],"scope":"focus_ayah","source_local_id":"99:4:2:selected-narration-over-announcement","source_type":"word_analysis","support_ids":["sup_b1fb9381f15da025e058","sup_deb5d30bdf52e3a443fe"],"title":"canonical narration contrasted with apparatus reading","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:4:2","qac_refs":["99:4:2:1"],"status":"accepted"}},{"anchor_refs":["99:4:3"],"branch_refs":[],"candidate_id":"cand_f327e0e35179a90a726f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000387"],"scope":"focus_ayah","source_local_id":"99:4:3:broken-plural-archive","source_type":"word_analysis","support_ids":["sup_13065d5bfda1a457aa39","sup_71bf4c14dd66e37bc161"],"title":"broken plural makes many stored reports","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:4:3","qac_refs":["99:4:3:1","99:4:3:2"],"status":"accepted"}},{"anchor_refs":["99:4:3"],"branch_refs":[],"candidate_id":"cand_3392b3a5a1906ee5082f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000387"],"scope":"focus_ayah","source_local_id":"99:4:3:day-report-formula","source_type":"word_analysis","support_ids":["sup_698f520bbf0205824739","sup_71bf4c14dd66e37bc161"],"title":"report noun joins Day-disclosure parallels","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:4:3","qac_refs":["99:4:3:1","99:4:3:2"],"status":"accepted"}},{"anchor_refs":["99:4:3"],"branch_refs":[],"candidate_id":"cand_1ec91a0912ccdd49ac88","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000387"],"scope":"focus_ayah","source_local_id":"99:4:3:direct-object-content","source_type":"word_analysis","support_ids":["sup_353704b368771ff28020","sup_71bf4c14dd66e37bc161"],"title":"accusative object fixes what is narrated","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:4:3","qac_refs":["99:4:3:1","99:4:3:2"],"status":"accepted"}},{"anchor_refs":["99:4:3"],"branch_refs":[],"candidate_id":"cand_09908a3f97aa64d7e1a8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000387"],"scope":"focus_ayah","source_local_id":"99:4:3:earth-owned-reports","source_type":"word_analysis","support_ids":["sup_3b3cd52a806b0f466522","sup_71bf4c14dd66e37bc161"],"title":"possessive suffix makes the reports earth-owned","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:4:3","qac_refs":["99:4:3:1","99:4:3:2"],"status":"accepted"}},{"anchor_refs":["99:4:3"],"branch_refs":[],"candidate_id":"cand_b83b32c7d7b6333386c2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000387"],"scope":"focus_ayah","source_local_id":"99:4:3:experience-derived-knowledge","source_type":"word_analysis","support_ids":["sup_71bf4c14dd66e37bc161","sup_cc978afd6aac3912399d"],"title":"reports carry tested witness-knowledge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:4:3","qac_refs":["99:4:3:1","99:4:3:2"],"status":"accepted"}},{"anchor_refs":["99:4:3"],"branch_refs":[],"candidate_id":"cand_3d4a5f04b476ff6c492c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000387"],"scope":"focus_ayah","source_local_id":"99:4:3:marked-awareness-root-form","source_type":"word_analysis","support_ids":["sup_71bf4c14dd66e37bc161","sup_fd62485cb21e10b0afe4"],"title":"awareness field becomes concrete report noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:4:3","qac_refs":["99:4:3:1","99:4:3:2"],"status":"accepted"}},{"anchor_refs":["99:4:3"],"branch_refs":[],"candidate_id":"cand_6bc9f37dfb95b2486402","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000387"],"scope":"focus_ayah","source_local_id":"99:4:3:object-cadence","source_type":"word_analysis","support_ids":["sup_71bf4c14dd66e37bc161","sup_c21a7c48286f91ad87cc"],"title":"object cadence lets reports expand","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:4:3","qac_refs":["99:4:3:1","99:4:3:2"],"status":"accepted"}},{"anchor_refs":["99:4:3"],"branch_refs":[],"candidate_id":"cand_b158c4ba556ddbfd1470","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000387"],"scope":"focus_ayah","source_local_id":"99:4:3:question-to-answer-bridge","source_type":"word_analysis","support_ids":["sup_71bf4c14dd66e37bc161","sup_91cae19b2a92156c539a"],"title":"possessed reports answer the prior question","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:4:3","qac_refs":["99:4:3:1","99:4:3:2"],"status":"accepted"}},{"anchor_refs":["99:4:2"],"branch_refs":[],"candidate_id":"cand_0d378f3fe47ad3bfe5ee","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000299"],"scope":"focus_ayah","source_local_id":"99:4:2:1","source_type":"qac_morpheme","support_ids":["sup_c39b30b45616fb57c0dc"],"title":"QAC root occurrence: ح د ث","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["99:4:3"],"branch_refs":[],"candidate_id":"cand_c4f95575ee88d0da7aee","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000387"],"scope":"focus_ayah","source_local_id":"99:4:3:1","source_type":"qac_morpheme","support_ids":["sup_20a0c53f94290543865b"],"title":"QAC root occurrence: خ ب ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["99:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"99:4","branch_refs":["root_000299/B003","root_000387/B001"],"candidate_id":"cand_8830cab18946c219b3ae","commentary_obligation":"review","hft_ref":"hft_b00f878696dbaac0a140","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_firsthand_report","source_type":"hft","support_ids":["sup_8cef1235becdf6a8de51"],"title":"baseline_firsthand_report","trust":"legacy_unbound"},{"anchor_refs":["99:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"99:4","branch_refs":["root_000299/B006","root_000387/B001"],"candidate_id":"cand_2148948467ba4ed8ccf8","commentary_obligation":"review","hft_ref":"hft_f280d5466227279afe03","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_inside_out_disclosure","source_type":"hft","support_ids":["sup_5228e92c4e5d19966f17"],"title":"baseline_inside_out_disclosure","trust":"legacy_unbound"},{"anchor_refs":["99:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"99:4","branch_refs":["root_000299/B001","root_000299/B003","root_000387/B001"],"candidate_id":"cand_58b9fbb478d211e8ea25","commentary_obligation":"review","hft_ref":"hft_06cda625d1ab8cb75339","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_report_as_reoccurrence","source_type":"hft","support_ids":["sup_03cc034ce401c5f322b2"],"title":"baseline_report_as_reoccurrence","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"يَوْمَئِذٍۢ تُحَدِّثُ أَخْبَارَهَا","qac_morphemes":[{"lemma_ar":"يَوْمَئِذ","morph_features":"STEM|POS:T|LEM:yawoma}i*","morpheme_role":"STEM","pos":"T","qac_ref":"99:4:1:1","qac_word_ref":"99:4:1","root_ar":"","surface_ar":"يَوْمَئِذٍ"},{"lemma_ar":"تُحَدِّثُ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:tuHad~ivu|ROOT:Hdv|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:4:2:1","qac_word_ref":"99:4:2","root_ar":"ح د ث","surface_ar":"تُحَدِّثُ"},{"lemma_ar":"أَخْبَار","morph_features":"STEM|POS:N|LEM:>axobaAr|ROOT:xbr|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:4:3:1","qac_word_ref":"99:4:3","root_ar":"خ ب ر","surface_ar":"أَخْبَارَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"99:4:3:2","qac_word_ref":"99:4:3","root_ar":"","surface_ar":"هَا"}],"word_analysis_qac_refs":[["99:4:1:1"],["99:4:2:1"],["99:4:3:1","99:4:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["99:4:1","99:4:2","99:4:3"]},"focus_surface_evidence":{"arabic_uthmani":"يَوْمَئِذٍۢ تُحَدِّثُ أَخْبَارَهَا","qac_morphemes":[{"lemma_ar":"يَوْمَئِذ","morph_features":"STEM|POS:T|LEM:yawoma}i*","morpheme_role":"STEM","pos":"T","qac_ref":"99:4:1:1","qac_word_ref":"99:4:1","root_ar":"","surface_ar":"يَوْمَئِذٍ"},{"lemma_ar":"تُحَدِّثُ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:tuHad~ivu|ROOT:Hdv|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:4:2:1","qac_word_ref":"99:4:2","root_ar":"ح د ث","surface_ar":"تُحَدِّثُ"},{"lemma_ar":"أَخْبَار","morph_features":"STEM|POS:N|LEM:>axobaAr|ROOT:xbr|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:4:3:1","qac_word_ref":"99:4:3","root_ar":"خ ب ر","surface_ar":"أَخْبَارَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"99:4:3:2","qac_word_ref":"99:4:3","root_ar":"","surface_ar":"هَا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["99:4:1:1"],["99:4:2:1"],["99:4:3:1","99:4:3:2"]],"word_analysis_refs":["99:4:1","99:4:2","99:4:3"],"word_rows":[{"analysis_record_ref":"99:4:1","analytic_gloss_range_en":"compressed temporal hinge meaning at that time, with the prior earthquake frame retained and the following disclosure clause placed inside that appointed interval","analytic_root_gloss_range_en":"day or time-span ranging from ordinary day to event-day or decisive period; the local compound selects the contextual day-then construction rather than a bare calendar date","qac_refs":["99:4:1:1"],"root":{"arabic":"ي و م","transliteration":"y-w-m"},"surface":{"arabic":"يَوْمَئِذٍۢ","transliteration":"yawmaʾidhin"}},{"analysis_record_ref":"99:4:2","analytic_gloss_range_en":"Form II imperfect reporting: the earth actively makes its stored events known through narration, with feminine agreement carrying the omitted subject","analytic_root_gloss_range_en":"root range includes occurrence, newness, report, narration, disclosure, and becoming a tale; the local Form II verb selects active causative narration rather than every branch","qac_refs":["99:4:2:1"],"root":{"arabic":"ح د ث","transliteration":"ḥ-d-th"},"surface":{"arabic":"تُحَدِّثُ","transliteration":"tuḥaddithu"}},{"analysis_record_ref":"99:4:3","analytic_gloss_range_en":"the earth's own plural reports: possessed, accusative report-content that communicates experience-derived knowledge rather than generic news","analytic_root_gloss_range_en":"root range includes report, informing, inquiry, tested knowledge, and inner awareness, with unrelated land, cultivation, abundance, softness, and portion branches not locally selected","qac_refs":["99:4:3:1","99:4:3:2"],"root":{"arabic":"خ ب ر","transliteration":"kh-b-r"},"surface":{"arabic":"أَخْبَارَهَا","transliteration":"akhbārahā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["99:4"],"branch_refs":["root_000299/B003","root_000387/B001"],"candidate_id":"cand_8830cab18946c219b3ae","evidence_scope":"focus_ayah","hft_ref":"hft_b00f878696dbaac0a140","item_id":"baseline_firsthand_report","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_firsthand_report","support_id":"sup_8cef1235becdf6a8de51"},{"anchor_refs":["99:4"],"branch_refs":["root_000299/B006","root_000387/B001"],"candidate_id":"cand_2148948467ba4ed8ccf8","evidence_scope":"focus_ayah","hft_ref":"hft_f280d5466227279afe03","item_id":"baseline_inside_out_disclosure","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_inside_out_disclosure","support_id":"sup_5228e92c4e5d19966f17"},{"anchor_refs":["99:4"],"branch_refs":["root_000299/B001","root_000299/B003","root_000387/B001"],"candidate_id":"cand_58b9fbb478d211e8ea25","evidence_scope":"focus_ayah","hft_ref":"hft_06cda625d1ab8cb75339","item_id":"baseline_report_as_reoccurrence","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_report_as_reoccurrence","support_id":"sup_03cc034ce401c5f322b2"}],"diagnostics":[],"lane_counts":{"global":7,"macro":7,"micro":3},"packet_summary":{"ayah_count":8,"focus_ref":"99:4","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ذ ر ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000511","furuq_root_norm":"ذ ر ر","furuq_source_root_norm":"ذ ر ر","is_dominant":true,"target_occurrences":2,"target_rank":1}]},{"qac_root":"ش ر ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000787","furuq_root_norm":"ش ر ر","furuq_source_root_norm":"ش ر ر","is_dominant":true,"target_occurrences":19,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000792","furuq_root_norm":"ش ر ي","furuq_source_root_norm":"ش ر ي","is_dominant":false,"target_occurrences":11,"target_rank":2}]}],"window":["99:1","99:2","99:3","99:4","99:5","99:6","99:7","99:8"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"99:4","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":7,"source_present":true,"structured_insight_count":10,"unstructured_record_count":0},"identity":{"ayah_ref":"99:4","lane":"micro","linguistic_source_ref":"99:4","surface_ref":"99:4","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"99:4","target_tokens":[["O",["99:4:1"]],["gün",["99:4:1"]],["yer",["99:4:2"]],["haberlerini",["99:4:3"]],["anlatır",["99:4:2"]]],"text":"O gün yer haberlerini anlatır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":8,"id":"s099-p01-001-008","label":"Whole surah","number":1,"refs":["99:1","99:2","99:3","99:4","99:5","99:6","99:7","99:8"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:2:forceful-sound-texture","source_type":"word_analysis","support_id":"sup_03cad2a44ee0d7a227e2","text":"{\"blocking_evidence\":null,\"headline\":\"doubled middle sound reinforces intensity\",\"reader_payoff\":\"The reader notices that the verb's sound pressure matches its intensive reporting function.\",\"reason\":\"The phonetic rows align with the visible doubled middle radical and Form II force, without creating an independent semantic branch.\",\"representative_source_ids\":[\"QP-89463664\",\"QP-b5c88561\",\"MP-4cf4dc1b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:3:broken-plural-archive","source_type":"word_analysis","support_id":"sup_13065d5bfda1a457aa39","text":"{\"blocking_evidence\":null,\"headline\":\"broken plural makes many stored reports\",\"reader_payoff\":\"The reader notices a many-item archive of reports rather than one undifferentiated statement.\",\"reason\":\"QAC marks the word as a plural noun with a possessive suffix, supporting the row family's distributed-report payoff.\",\"representative_source_ids\":[\"MG-fb4d32eb\",\"QF-a559b11d\",\"QF-fa2ded81\",\"QT-064f57cd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"99:4:3:1","source_type":"qac_morpheme","support_id":"sup_20a0c53f94290543865b","text":"{\"lemma_ar\":\"أَخْبَار\",\"morph_features\":\"STEM|POS:N|LEM:>axobaAr|ROOT:xbr|MP|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"99:4:3:1\",\"qac_word_ref\":\"99:4:3\",\"root_ar\":\"خ ب ر\",\"surface_ar\":\"أَخْبَارَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:1:backward-deictic-compression","source_type":"word_analysis","support_id":"sup_235bf1dab9eb6d5cc8a3","text":"{\"blocking_evidence\":null,\"headline\":\"compressed pointer to the prior event\",\"reader_payoff\":\"The reader notices that the time word depends on the already narrated earthquake scene instead of starting a new temporal setting.\",\"reason\":\"QAC and attachment evidence identify the word as a compressed temporal deictic that resumes the earlier event frame introduced in 99:1.\",\"representative_source_ids\":[\"QG-19a08b94\",\"QG-36a78f0d\",\"QF-1b3a0779\",\"QF-ca54303d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:1:decisive-interval-range","source_type":"word_analysis","support_id":"sup_27272902f9d1900b4e00","text":"{\"blocking_evidence\":null,\"headline\":\"event-day range becomes a disclosure interval\",\"reader_payoff\":\"The reader notices the word as a decisive disclosure interval, not as a neutral calendar label.\",\"reason\":\"V4 supports broad time-span and event-day branches for the root, while the local compound and adverbial syntax narrow that range to the contextual time of this disclosure.\",\"representative_source_ids\":[\"QS-378ec086\",\"QS-a7cdcb40\",\"QS-cb57b60f\",\"MS-41bc4f58\",\"QI-01423893\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:3:direct-object-content","source_type":"word_analysis","support_id":"sup_353704b368771ff28020","text":"{\"blocking_evidence\":null,\"headline\":\"accusative object fixes what is narrated\",\"reader_payoff\":\"The reader notices that the earth's speech has determinate content, with telling and report-content bound together in one clause.\",\"reason\":\"Attachment evidence marks this word as the explicit accusative object of the reporting verb, and the clause remains structurally complete even while 99:5 explains its cause.\",\"representative_source_ids\":[\"QG-fea65e94\",\"QT-0b0b6b8f\",\"MT-80e3816d\",\"QI-85baff29\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:2:boundary-and-forward-bridge","source_type":"word_analysis","support_id":"sup_38f5592cd2be67b30119","text":"{\"blocking_evidence\":null,\"headline\":\"earth takes over and points to the next cause\",\"reader_payoff\":\"The reader notices that agency shifts from the bewildered human observer to the speaking earth, while the next ayah explains why the earth can report.\",\"reason\":\"The boundary rows coherently connect the prior human question in 99:3, the earth's morphologically carried subjecthood in 99:4, and the explanatory revelation statement in 99:5.\",\"representative_source_ids\":[\"QB-8a90fe1a\",\"QB-ba49cd6a\",\"QB-bf35292d\",\"QY-7ef2fefa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:3:earth-owned-reports","source_type":"word_analysis","support_id":"sup_3b3cd52a806b0f466522","text":"{\"blocking_evidence\":null,\"headline\":\"possessive suffix makes the reports earth-owned\",\"reader_payoff\":\"The reader notices that the reports are grammatically attached to the earth, not presented as generic information.\",\"reason\":\"QAC and attachment evidence identify a feminine possessive suffix referring back to the earth, with an idafa relation inside the word.\",\"representative_source_ids\":[\"QG-68e4c592\",\"QG-eef95294\",\"QF-79b695fe\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:2:imperfect-unfolding-answer","source_type":"word_analysis","support_id":"sup_4226544125256173fb10","text":"{\"blocking_evidence\":null,\"headline\":\"imperfect narration follows completed question\",\"reader_payoff\":\"The reader notices a shift from a completed human utterance in 99:3 to an unfolding earth-disclosure in 99:4.\",\"reason\":\"The local form is an imperfect indicative, and the boundary rows coherently contrast it with the prior completed human speech event in 99:3.\",\"representative_source_ids\":[\"QG-f5b80c2a\",\"QB-fa686584\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:2:form-ii-event-to-report","source_type":"word_analysis","support_id":"sup_4f1f7ecb57c6986086f5","text":"{\"blocking_evidence\":null,\"headline\":\"Form II turns occurrence into narration\",\"reader_payoff\":\"The reader notices that the verb makes hidden events emerge as communicated knowledge, not merely as ordinary speech.\",\"reason\":\"QAC tags the verb as Form II, and V4 supports occurrence, narration, and disclosure branches; local grammar selects causative-intensive reporting rather than all root branches.\",\"representative_source_ids\":[\"QS-8d326b3a\",\"QS-ff10673e\",\"MS-0c14b287\",\"QF-5a5ed643\",\"MF-3ea68290\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:2:feminine-prodrop-earth-subject","source_type":"word_analysis","support_id":"sup_6786a83be450098be4cc","text":"{\"blocking_evidence\":null,\"headline\":\"feminine agreement carries the earth as subject\",\"reader_payoff\":\"The reader notices that the earth remains grammatically present as speaker even though it is not renamed in the ayah.\",\"reason\":\"QAC and attachment evidence identify third-feminine singular agreement with an omitted subject continuing the earth as discourse topic.\",\"representative_source_ids\":[\"QG-466eb0ed\",\"QG-c03213b3\",\"MG-808935d9\",\"QF-823b8a67\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:3:day-report-formula","source_type":"word_analysis","support_id":"sup_698f520bbf0205824739","text":"{\"blocking_evidence\":null,\"headline\":\"report noun joins Day-disclosure parallels\",\"reader_payoff\":\"The reader notices that the earth's reports participate in a wider Day-knowledge and report-formula field while remaining locally possessed by the earth.\",\"reason\":\"The listed parallels support a report-disclosure field, but they do not control the local possessive object construction (100:11; 35:14; 47:31; 9:94).\",\"representative_source_ids\":[\"QI-30585a09\",\"QE-8f3c8a91\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:3","source_type":"word_analysis","support_id":"sup_71bf4c14dd66e37bc161","text":"{\"gloss_range\":\"the earth's own plural reports: possessed, accusative report-content that communicates experience-derived knowledge rather than generic news\",\"prose\":\"{{ar:أَخْبَارَهَا}} ({{tr:akhbārahā}}) gives the earth's speech concrete content. The possessive suffix makes the reports belong to the earth, and the same referent has already supplied the verb's subject, so the object is best heard as the earth's own disclosures rather than generic news about it. As an accusative object, the word prevents the speech from remaining vague: there are reports being narrated. The broken plural makes those reports multiple and distributed, like entries in an archive. The root pressure adds more than information-transfer; it carries knowledge gained through encounter or testing, so the earth's reports feel like witness-records. Distributional rows about the root's awareness field survive only as background: they mark the plural report noun as a concrete form choice from a field often associated with divine awareness, without importing a divine attribute into the local noun (100:11; 35:31). The Day-knowledge and report-formula parallels keep the reports within a disclosure field while the local suffix keeps the archive earth-owned (100:11; 35:14; 47:31; 9:94). The object also opens out in cadence after the compressed verb, with longer vowel movement and final suffix closure letting the reports expand sonically. Positioned at the ayah's close, the word answers the prior question in 99:3 and points forward to 99:5, where the reason for the earth's speech is given.\",\"root_display\":\"{{ar:خ ب ر}} ({{tr:kh-b-r}})\",\"root_gloss_range\":\"root range includes report, informing, inquiry, tested knowledge, and inner awareness, with unrelated land, cultivation, abundance, softness, and portion branches not locally selected\",\"surface_display\":\"{{ar:أَخْبَارَهَا}} ({{tr:akhbārahā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:2:compact-disclosure-clause","source_type":"word_analysis","support_id":"sup_8def9c9c357ba755711c","text":"{\"blocking_evidence\":null,\"headline\":\"verb binds telling to report-content\",\"reader_payoff\":\"The reader notices that the ayah is not speech in the abstract; the verb arrives inside a complete disclosure clause with explicit content.\",\"reason\":\"Attachment evidence marks a single verbal clause headed by this verb with an explicit direct object, after the fronted time-adverb.\",\"representative_source_ids\":[\"QI-057b159e\",\"QT-697bed20\",\"QT-ce76e720\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:3:question-to-answer-bridge","source_type":"word_analysis","support_id":"sup_91cae19b2a92156c539a","text":"{\"blocking_evidence\":null,\"headline\":\"possessed reports answer the prior question\",\"reader_payoff\":\"The reader notices that what was asked about the earth in 99:3 becomes the earth's own report-content in 99:4 and is explained in 99:5.\",\"reason\":\"The boundary rows coherently track the stable feminine referent from the prior question in 99:3 to the possessed reports in 99:4 and the explanatory address in 99:5.\",\"representative_source_ids\":[\"QB-7f21d500\",\"QB-edb8fc4a\",\"QB-fbf336d4\",\"QY-4cab5f79\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:1:sound-and-boundary-reset","source_type":"word_analysis","support_id":"sup_9944c96899f3154993be","text":"{\"blocking_evidence\":null,\"headline\":\"audible hinge from question to disclosure\",\"reader_payoff\":\"The reader notices a scene reset from the human question to the earth's answer without leaving the same event-frame.\",\"reason\":\"The boundary rows coherently connect 99:3 and 99:4, and the sound rows add a local cadence observation without changing the grammar.\",\"representative_source_ids\":[\"QP-1cbfc138\",\"QP-966416bc\",\"QB-3ae3fc0e\",\"QB-784331f5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:1:day-disclosure-formula","source_type":"word_analysis","support_id":"sup_9a6141904b49e79fd827","text":"{\"blocking_evidence\":null,\"headline\":\"Day-scene formula and same-surah hinge\",\"reader_payoff\":\"The reader notices that the time marker belongs to a wider Day-disclosure pattern while still serving the local earthquake report.\",\"reason\":\"The cross-surah formula claim is coherent for parallels such as 77:35, 78:18, and 79:8; the same-surah refrain is preserved with the corrected later hinge at 99:6 rather than the misstated 99:5.\",\"representative_source_ids\":[\"QI-0b8be68f\",\"QI-f74ab114\",\"MI-eb2767fe\",\"MT-d8898258\",\"QE-8d540646\",\"QE-90af14f4\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:2","source_type":"word_analysis","support_id":"sup_b1fb9381f15da025e058","text":"{\"gloss_range\":\"Form II imperfect reporting: the earth actively makes its stored events known through narration, with feminine agreement carrying the omitted subject\",\"prose\":\"{{ar:تُحَدِّثُ}} ({{tr:tuḥaddithu}}) makes the earth present inside the verb rather than by repeating the noun. Its feminine agreement keeps the earth as the speaking subject, and its imperfect form lets the answer unfold after the completed human question in 99:3. Form II is the main lexical pressure: the earth is not merely a place where events occurred, but the agent that causes those events to become communicable report. The canonical reporting verb is more intimate than a formal announcement reading preserved only as apparatus, so the local payoff is narration from witness-contact. Structurally the verb arrives after the fronted time-frame and takes explicit report-content, binding the act of telling to what is told. Its rare finite use and parallels place it in a Day-speech field (4:42; 4:87), recall a Form II speech duty elsewhere (93:11), and shift report-opening formulas from heard report into earth narration (88:1; 79:15). The breathy opening and doubled middle consonant make that intensive reporting feel compressed and forceful. The verb also creates a forward question that 99:5 answers: the earth can report because it has been addressed by revelation.\",\"root_display\":\"{{ar:ح د ث}} ({{tr:ḥ-d-th}})\",\"root_gloss_range\":\"root range includes occurrence, newness, report, narration, disclosure, and becoming a tale; the local Form II verb selects active causative narration rather than every branch\",\"surface_display\":\"{{ar:تُحَدِّثُ}} ({{tr:tuḥaddithu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:1:fronted-temporal-frame","source_type":"word_analysis","support_id":"sup_b22f029a1077e5aa6da9","text":"{\"blocking_evidence\":null,\"headline\":\"fronted time-adverb governs the clause\",\"reader_payoff\":\"The reader notices that the clause is framed by the appointed time before the reporting verb appears.\",\"reason\":\"The attachment rows mark the word as the syntactically forced adverbial dependent of the reporting verb, and QAC marks the accusative time-adverbial role.\",\"representative_source_ids\":[\"QG-52d82dbb\",\"MG-db64de92\",\"QT-8ac2e075\",\"QT-8fa2b989\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:2:rare-reporting-field","source_type":"word_analysis","support_id":"sup_b34ffaac87c7281955b8","text":"{\"blocking_evidence\":null,\"headline\":\"finite reporting joins wider disclosure field\",\"reader_payoff\":\"The reader notices that this finite reporting event is marked within a wider Quranic field of report and Day-speech.\",\"reason\":\"The contextual profile shows low occurrence for this exact root-form, and the intertext rows are kept as parallels rather than controls over the local parse (4:42; 4:87; 93:11; 88:1; 79:15).\",\"representative_source_ids\":[\"QI-45d5deb9\",\"QI-e694280b\",\"MI-86ab98fa\",\"QE-05c1c297\",\"QE-8bbd58cd\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:3:object-cadence","source_type":"word_analysis","support_id":"sup_c21a7c48286f91ad87cc","text":"{\"blocking_evidence\":null,\"headline\":\"object cadence lets reports expand\",\"reader_payoff\":\"The reader notices the object opening out after the compressed reporting verb, making the reports feel sonically expanded.\",\"reason\":\"The sound observation is local to the verb-object sequence and supports cadence without changing the lexical selection.\",\"representative_source_ids\":[\"QP-15d7c98d\",\"QP-b6985fa4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"99:4:2:1","source_type":"qac_morpheme","support_id":"sup_c39b30b45616fb57c0dc","text":"{\"lemma_ar\":\"تُحَدِّثُ\",\"morph_features\":\"STEM|POS:V|IMPF|(II)|LEM:tuHad~ivu|ROOT:Hdv|3FS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"99:4:2:1\",\"qac_word_ref\":\"99:4:2\",\"root_ar\":\"ح د ث\",\"surface_ar\":\"تُحَدِّثُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:3:experience-derived-knowledge","source_type":"word_analysis","support_id":"sup_cc978afd6aac3912399d","text":"{\"blocking_evidence\":null,\"headline\":\"reports carry tested witness-knowledge\",\"reader_payoff\":\"The reader notices that the reports are not hearsay but knowledge communicated from experienced contact with events.\",\"reason\":\"V4 supports the root branch of report, inquiry, tested knowledge, and inner knowledge; local grammar keeps that pressure within the plural report-object.\",\"representative_source_ids\":[\"QS-25ee57c9\",\"QS-7e3a1135\",\"QS-acf6c6f2\",\"QS-bdc7723f\",\"MS-6edfd312\",\"MS-84d223f8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:1","source_type":"word_analysis","support_id":"sup_ce2dffe4b089ccb5fc82","text":"{\"gloss_range\":\"compressed temporal hinge meaning at that time, with the prior earthquake frame retained and the following disclosure clause placed inside that appointed interval\",\"prose\":\"{{ar:يَوْمَئِذٍۢ}} ({{tr:yawmaʾidhin}}) does not open a new, free-floating date. It compresses the earlier earthquake sequence into a temporal hinge and makes the reporting clause arrive as the consequence of that marked moment. Because the word is fronted as an accusative time-adverb, the reader receives the event-window before the earth's speech is parsed. The root range leaves room for a decisive interval rather than only a calendar day, while the local compound keeps that range tied to the already introduced scene. After the human question in 99:3, this temporal opener resets the view toward the earth's answer without leaving the earthquake-day. Its repeated use as a Day-scene marker, returning later in the surah at 99:6 and appearing in parallels such as 77:35, 78:18, and 79:8, makes the timing feel formulaic and eschatological, not merely chronological. The internal catch and final nasal tanwīn make the hinge audible: the word turns from general time to pointed then and carries the recitation into disclosure.\",\"root_display\":\"{{ar:ي و م}} ({{tr:y-w-m}})\",\"root_gloss_range\":\"day or time-span ranging from ordinary day to event-day or decisive period; the local compound selects the contextual day-then construction rather than a bare calendar date\",\"surface_display\":\"{{ar:يَوْمَئِذٍۢ}} ({{tr:yawmaʾidhin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:2:selected-narration-over-announcement","source_type":"word_analysis","support_id":"sup_deb5d30bdf52e3a443fe","text":"{\"blocking_evidence\":null,\"headline\":\"canonical narration contrasted with apparatus reading\",\"reader_payoff\":\"The reader notices that the canonical verb presents eyewitness-like narration rather than only formal announcement.\",\"reason\":\"The supplied noncanonical announcement reading is useful as contrast, but it cannot replace the aligned canonical reporting verb.\",\"representative_source_ids\":[\"QS-0171f32d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:4:3:marked-awareness-root-form","source_type":"word_analysis","support_id":"sup_fd62485cb21e10b0afe4","text":"{\"blocking_evidence\":null,\"headline\":\"awareness field becomes concrete report noun\",\"reader_payoff\":\"The reader notices that a root often associated with awareness is here realized as plural report-content owned by the earth.\",\"reason\":\"The distributional contrast can mark the selected report noun, but it must not import the divine attribute itself into the local possessed plural; the awareness-field parallels remain background (100:11; 35:31).\",\"representative_source_ids\":[\"QI-6565b48b\",\"QI-7897b1f6\",\"MI-da995569\",\"QE-a26678f3\",\"QH-3d4d4788\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"يَوْمَئِذٍۢ تُحَدِّثُ أَخْبَارَهَا","ayah_ref":"99:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000299/B003","root_000387/B001"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000299","role":"Speech arising as report or conversation supplies the literal recounting and serves as the mechanism's public channel.","root":"ح د ث","source_ref":"99:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000387","role":"Report joined to tested knowledge of an affair's interior makes the possessed content first-hand rather than hearsay.","root":"خ ب ر","source_ref":"99:4","source_word_indices":["3"]}],"changed_reading":{"after":"She recounts reports that belong to her and carry her own inward, experiential knowledge.","before":"An unspecified feminine subject simply speaks."},"confidence":"strong","focus_anchor":"The focus couples the act of recounting at word 2 with plural reports possessed by the feminine speaker at word 3.","mechanism":"The speaker turns her own tested inward knowledge into report: speech is the public channel, while direct acquaintance with what lies in her domain gives it evidentiary force.","model_id":"baseline_firsthand_report"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_firsthand_report","source_type":"hft","support_id":"sup_8cef1235becdf6a8de51","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"يَوْمَئِذٍۢ تُحَدِّثُ أَخْبَارَهَا","ayah_ref":"99:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000299/B006","root_000387/B001"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_000299","role":"Disclosure and bringing out supply the outward motion and make speaking an act of exposure.","root":"ح د ث","source_ref":"99:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000387","role":"Tested inward knowledge supplies the concealed content that the disclosure makes available.","root":"خ ب ر","source_ref":"99:4","source_word_indices":["3"]}],"changed_reading":{"after":"The line stages exposure: concealed contents of the speaker's domain are brought outward as evidence.","before":"The line is only an announcement of information."},"confidence":"strong","focus_anchor":"The reporting verb and the possessive 'her reports' jointly anchor an inside-to-outside movement.","mechanism":"Disclosure brings what was unavailable into view, while the reports name knowledge of an interior; the utterance therefore exposes contents from within the speaker's own domain.","model_id":"baseline_inside_out_disclosure"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_inside_out_disclosure","source_type":"hft","support_id":"sup_5228e92c4e5d19966f17","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"يَوْمَئِذٍۢ تُحَدِّثُ أَخْبَارَهَا","ayah_ref":"99:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000299/B001","root_000299/B003","root_000387/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000299","role":"Coming into being after nonbeing supplies the eventive renewal by which an absent occurrence becomes present again.","root":"ح د ث","source_ref":"99:4","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000299","role":"Arising speech or report specifies that the renewed presence occurs through narration rather than physical repetition.","root":"ح د ث","source_ref":"99:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000387","role":"Report grounded in inward knowledge gives the re-presented occurrence determinate evidentiary content.","root":"خ ب ر","source_ref":"99:4","source_word_indices":["3"]}],"changed_reading":{"after":"Her reporting makes absent events newly present as report, so narration is itself a fresh occurrence.","before":"The speaker refers retrospectively to completed events."},"confidence":"medium","focus_anchor":"The eventive range of the word-2 root remains active inside its explicit speech construction.","mechanism":"Recounting does more than refer backward: speech lets an absent occurrence arise anew as a report, making narration itself a fresh event.","model_id":"baseline_report_as_reoccurrence"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_report_as_reoccurrence","source_type":"hft","support_id":"sup_03cc034ce401c5f322b2","trust":"legacy_unbound"}]}
</lane_packet_json>
