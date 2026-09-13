# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **95:2**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s095-regular-20260912/s095/95_2/micro.discovery.json` and modify nothing
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
  "ayah_ref": "95:2",
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
{"branch_registry":[{"boundary":"Dal, bir şeyin yanında aynı hizada uzanan avlu ya da yapı bölümüyle sınırlıdır.","branch_kind":"bare","branch_ref":"root_000955/B001","candidate_links":[{"candidate_id":"cand_2d8149c440b4fb812b82","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طُور","morph_features":"STEM|POS:N|LEM:Tuwr|ROOT:Twr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:2:1:2","qac_word_ref":"95:2:1","surface_ar":"طُورِ"}],"gloss":"yanı boyunca aynı hizada uzanan bölüm","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bölüm, dayandığı şeyin yanı boyunca onunla aynı hizada ve kesintisiz bir doğrultuda uzanır."}}],"root_ar":"ط و ر","root_id":"root_000955","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir evin, duvarın ya da benzeri bir şeyin yanında onun doğrultusunu izleyen avlu veya yapı bölümünü karşılar.","boundary_detail":"Dal, bir şeyin yanında aynı hizada uzanan avlu ya da yapı bölümüyle sınırlıdır.","branch_image_ar":"امتداد الحافة والفناء بمحاذاة الشيء","concept_gloss":"yanı boyunca aynı hizada uzanan bölüm","contextual_glosses":[{"applicability":"Söz konusu bölüm özellikle bir evin avlusundan evin yanı boyunca uzanıyorsa doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ev bağlamındaki hizalı uzanmayı ve avlu bölümünü birlikte korur."},"facet_ids":["F001"],"text":"ev boyunca uzanan avlu şeridi","usage_role":"contextual"}],"definition":"Bir evin ya da başka bir yapının avlusundan veya yapı kısmından, o şeyin yanı boyunca aynı hizada ve aynı doğrultuda uzanan bölüm.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bölüm, dayandığı şeyin yanı boyunca onunla aynı hizada ve kesintisiz bir doğrultuda uzanır."}],"identity_rationale":"Kaynak ifadesi, bir evin ya da başka bir şeyin avlusundan veya yapısından onunla aynı doğrultuda uzanan bölümü açıkça tanımlar. Bu nedenle durağan bir çevre şeridi anlamı korunmalı, yakınlaşma, sınır aşma veya dağ anlamları bu dala katılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ev ya da yapıyla aynı hizada uzanan avlu veya yapı bölümü"}],"lexicalization_note":"Tanım yalın biçimin uzanma ve hizalanma anlamını verir; başka yapılara bağlı anlamları içermez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan iki komşu avlu ve çevre kenarıyla en yakın karışma noktalarını gösterirken ötekiler yalnızca uzak alan benzerliği taşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal avlunun bütününü değil, evle aynı doğrultuda uzanan bölümünü belirler; komşu dal ise avlu veya ev sahasını genel olarak adlandırır.","focus_only":"Bir yapı boyunca aynı hizada uzanan belirli avlu ya da yapı bölümünü gösterir.","gloss":"avlu ve yanı boyunca uzanan bölüm","neighbor_only":"Avlunun veya açık ev alanının bütününü gösterir; yana koşut bir uzanma şartı taşımaz.","neighbor_ref":"root_000756/B001","relation_type":"near_neighbor","shared_zone":"İki dal da evin çevresindeki açık alanla ilgilidir."},{"boundary_match":"partial","distinction":"Odak dalda temel ilişki yan yana ve aynı doğrultuda uzanmadır; komşu dalda ise merkezin çevresini sarma ya da kenar oluşturma öne çıkar.","focus_only":"Bir şeyin yanında onun doğrultusunu izleyen uzunlamasına bölümü anlatır.","gloss":"hizalı uzantı ve çevre kenarı","neighbor_only":"Bir merkezin çevresini saran kenarı ya da iki yan sınırı anlatır.","neighbor_ref":"root_000343/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir şeyin yanındaki veya çevresindeki sınır alanını konu eder."}],"source_phrase_ar":"طوار الدار وهو الذي يمتد معها من فنائها (maqayis)؛ الطوار ما كان على حذو الشيء أو بحذائه (ayn)؛ طوار الدار ما كان ممتدا معها من الفناء (sihah)؛ طوار الدار وطواره ما امتد منها من البناء (mufradat)","source_summary":"Kaynaklar, anlamı evin avlusundan ya da yapısından onun yanı boyunca uzanan ve başka bir şeyle aynı hizada bulunan bölüm üzerinde birleştirir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"ما كان طوارا للدار أو الحائط: امتداد الفناء أو البناء أو الطول بمحاذاة الشيء وعلى نسق واحد","what_is_not_ar":"ليس الجبل ولا التارة ولا مجاوزة الحد بعد ثبوته."},"support_links":["sup_64ab3685906542b0f920"]},{"boundary":"Çevrede dolanarak yaklaşma ile belirli olumsuz yapılardaki yaklaşmama anlamları ayrı tutulmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000955/B002","candidate_links":[{"candidate_id":"cand_2d8149c440b4fb812b82","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طُور","morph_features":"STEM|POS:N|LEM:Tuwr|ROOT:Twr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:2:1:2","qac_word_ref":"95:2:1","surface_ar":"طُورِ"}],"gloss":"çevresinde dolanıp yaklaşmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eylem, bir şeyin çevresinde dolanmayı ve ona doğru yakınlaşmayı birleştirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Olumsuz bağlı kullanımlar, bir kişiye, onun avlusuna veya çevredeki korunaklı alana yaklaşmamayı bildirir."}}],"root_ar":"ط و ر","root_id":"root_000955","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yalın eylem çekirdeğini verir; olumsuz yapılarda aynı eylem yaklaşmama biçiminde çevrilir.","boundary_detail":"Çevrede dolanarak yaklaşma ile belirli olumsuz yapılardaki yaklaşmama anlamları ayrı tutulmalıdır.","branch_image_ar":"الدنو من حريم الشيء وما حوله","concept_gloss":"çevresinde dolanıp yaklaşmak","contextual_glosses":[{"applicability":"Bir kişiye ya da onun avlusuna yaklaşmama bildiren olumsuz yapıların doğal karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Olumsuzluğu ve hedefin yakınına gelmeme koşulunu korur."},"facet_ids":["F002"],"text":"yakınına uğramamak","usage_role":"contextual"},{"applicability":"Konuşanların çevresindeki alanı veya korunaklı bölgeyi yaklaşılmaması gereken yer olarak gösteren kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yasağı, konuşanlara ait çevre alanını ve yaklaşma eylemini korur."},"facet_ids":["F002"],"text":"çevremize yaklaşma","usage_role":"contextual"}],"definition":"Bir şeyin çevresinde dolanarak ona doğru yaklaşmak. Olumsuz yapılar içinde, o şeye, onun avlusuna ya da çevresindeki korunaklı alana yaklaşmamak anlamını verir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eylem, bir şeyin çevresinde dolanmayı ve ona doğru yakınlaşmayı birleştirir."},{"facet_id":"F002","role":"specialization","statement":"Olumsuz bağlı kullanımlar, bir kişiye, onun avlusuna veya çevredeki korunaklı alana yaklaşmamayı bildirir."}],"identity_rationale":"Kaynak ifadesi hem bir şeyin çevresinde dolanıp ona yaklaşma eylemini hem de olumsuz yapılarda kişiye, avluya veya çevredeki korunaklı alana yaklaşmamayı bildirir. Çerçeve bu ortak yakınlaşma çekirdeğini doğru verir.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"ona ya da avlusuna yaklaşmam"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"çevremize veya korunaklı alanımıza yaklaşma"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"çevresinde dolanıp ona yaklaşmak"}],"lexicalization_note":"Yalın eylem çevrede dolanıp yaklaşmayı, bağlı olumsuz yapılar ise kişiye, avluya veya çevredeki alana yaklaşmamayı anlatır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler genel yakınlaşma ve fiziksel çevreleme ile gerçek sınır karışmalarını gösterir, kalanlar yalnızca aynı uzamsal sahneyi paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal uzamsal hedefin çevresinde hareket etmeyi ve ona yaklaşmayı gerektirir; komşu dal genel yakınlığı ve zamanın yaklaşmasını da kapsar.","focus_only":"Çevrede dolanma bileşenini ve avlu ya da çevre alanına bağlı olumsuz kullanımları içerir.","gloss":"çevrede dolanarak yaklaşma ve genel yakınlaşma","neighbor_only":"Bir olayın zamanının yaklaşması gibi daha genel ve zamansal yakınlaşmaları da içerir.","neighbor_ref":"root_000029/B001","relation_type":"near_synonym","shared_zone":"İki dalın ortak çekirdeği bir şeye veya zamana göre yakın duruma gelmektir."},{"boundary_match":"partial","distinction":"Odak dalın sonucu yakınlıktır ve tam çevreleme gerekmez; komşu dalda temel işlem hedefin çevresini kapatmak veya kuşatmaktır.","focus_only":"Hedefin çevresinde dolanıp ona doğru yaklaşan bir hareketi anlatır.","gloss":"yaklaşarak dolanma ve çevreleme","neighbor_only":"Hedefi çevreleme, duvarla çevirme veya kuşatma sonucunu anlatır.","neighbor_ref":"root_000372/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir hedefin çevresiyle kurulan uzamsal ilişki bulunur."}],"source_phrase_ar":"طار فلان يطور طورا أي كأنه يحوم حواليه ويدنو منه (ayn)؛ لا أطور به أي لا أقربه (sihah)؛ لا تطر حرانا أي لا تقرب ما حولنا (sihah)؛ لا أطور به أي لا أقرب فناءه (mufradat)","source_summary":"Toplu kanıt, çevrede dolanarak yaklaşma eylemiyle bundan türeyen yaklaşmama bildiren olumsuz kullanımları aynı dalda birleştirir.","sources":["AY","SI","MU"],"what_is_ar":"الدخول في معنى القرب من الفناء أو الحريم، أو الحومان حول الشيء والدنو منه","what_is_not_ar":"ليس مجرد امتداد الطوار، ولا مجاوزة الحد، ولا اسم الجبل."},"support_links":["sup_64ab3685906542b0f920"]},{"boundary":"Sınırın kendisi, onu aşma eylemi ve iki ucuna ulaşma kullanımı birbirine indirgenmemelidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000955/B003","candidate_links":[{"candidate_id":"cand_2d8149c440b4fb812b82","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طُور","morph_features":"STEM|POS:N|LEM:Tuwr|ROOT:Twr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:2:1:2","qac_word_ref":"95:2:1","surface_ar":"طُورِ"}],"gloss":"kişiye veya şeye ait sınır","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi ya da şey için geçerli olan ve davranışın veya kapsamın durması beklenen sınırı gösterir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli bir bağlı kullanım, kişinin kendisi için geçerli sınırı veya ölçüyü aşmasını anlatır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İkili biçim, bir alanın ilk ve son uçlarına, yani iki sınırına ulaşmayı anlatır."}}],"root_ar":"ط و ر","root_id":"root_000955","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın sınır çekirdeğini karşılar; aşma ve iki uca ulaşma, bağlam içinde ayrıca eylemle belirtilmelidir.","boundary_detail":"Sınırın kendisi, onu aşma eylemi ve iki ucuna ulaşma kullanımı birbirine indirgenmemelidir.","branch_image_ar":"الحد الذي يوقف عنده أو يتجاوز","concept_gloss":"kişiye veya şeye ait sınır","contextual_glosses":[{"applicability":"Bir kişinin kendisi için geçerli davranış veya ölçü sınırını geçtiği yapı için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiye ait sınırı ve o sınırın ötesine geçme eylemini korur."},"facet_ids":["F001","F002"],"text":"kendine düşen sınırı aşmak","usage_role":"contextual"},{"applicability":"Bir bilgi alanının hem başlangıç hem bitiş sınırına erişmeyi anlatan kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Alanı iki ucuyla kavramayı ve her iki sınıra ulaşmayı korur."},"facet_ids":["F001","F003"],"text":"başından sonuna dek ulaşmak","usage_role":"contextual"}],"definition":"Bir kişi ya da şey için geçerli olan sınır. Bağlı kullanımlarda bu sınırın aşılmasını veya bir alanın başlangıç ve bitiş uçlarına ulaşılmasını anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi ya da şey için geçerli olan ve davranışın veya kapsamın durması beklenen sınırı gösterir."},{"facet_id":"F002","role":"associated_use","statement":"Belirli bir bağlı kullanım, kişinin kendisi için geçerli sınırı veya ölçüyü aşmasını anlatır."},{"facet_id":"F003","role":"extension","statement":"İkili biçim, bir alanın ilk ve son uçlarına, yani iki sınırına ulaşmayı anlatır."}],"identity_rationale":"Kaynak ifadesi bir kişiye veya şeye ait sınırı, bu sınırın aşılmasını ve bir bilgi alanının başlangıç ile bitiş uçlarına varmayı birlikte tanıklar. Dal çerçevesi sınır çekirdeğini ve iki ayrı bağlı gerçekleşmesini doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kendine düşen sınırı ya da ölçüyü aşmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bir alanın başlangıç ve bitiş uçları"}],"lexicalization_note":"Tanım sınır çekirdeğini verir; sınırı aşma ve başlangıç ile bitiş uçlarına ulaşma anlamlarını yalnızca tanıklanan yapılara bağlar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen iki komşu genel sınır ile olumsuz değerlendirilen sınır aşımını ayırır, öteki adayların paylaştığı alan daha uzaktır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sınırı belirli bir kişi ya da şeye ait ölçü olarak kurar ve bağlı yapılarda aşılmasını anlatır; komşu dal ayırma, bitiş ve kural sınırlarını daha geniş kapsar.","focus_only":"Kişiye veya şeye düşen sınırı ve bir alanın iki ucuna ulaşma kullanımını içerir.","gloss":"kişisel sınır ve ayırıcı sınır","neighbor_only":"İki şeyi ayıran çizgiyi, arazi sınırlarını ve çiğnenmemesi gereken kuralları da kapsar.","neighbor_ref":"root_000002/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin sona erdiği veya ötesine geçilmemesi gereken sınırı bildirir."},{"boundary_match":"partial","distinction":"Odak dalda sınır ve aşma kendi başına yansızdır; komşu dal sınır aşımına olumsuz bir değer ve aşırılık niteliği ekler.","focus_only":"Sınırı yansız biçimde adlandırır ve alanın iki ucuna varmayı da kapsar.","gloss":"sınır ve ölçüyü aşan aşırılık","neighbor_only":"Sınır aşımını hoş görülmeyen, çirkin veya aşırı bir nitelik olarak değerlendirir.","neighbor_ref":"root_001134/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da geçerli bir sınırın veya ölçünün ötesine geçme düşüncesi vardır."}],"source_phrase_ar":"عدا طوره أي جاز الحد الذي هو له من داره (maqayis)؛ عدا طوره أي جاوز حده (sihah)؛ بلغ فلان في العلم أطوريه أي حديه أوله وآخره (sihah)؛ عدا فلان طوره أي تجاوز حده (mufradat)","source_summary":"Toplu kanıt, kişiye veya şeye ait sınırı temel alır; sınırı aşma ve bir alanın ilk ile son uçlarına varma kullanımlarını bu çekirdeğe bağlar.","sources":["MQ","SI","MU"],"what_is_ar":"الطور بمعنى الحد، وما يقال في تعديه أو بلوغ طرفيه وأقصاه","what_is_not_ar":"ليس الطوار المكاني نفسه ولا التارة بعد التارة ولا الجبل."},"support_links":["sup_64ab3685906542b0f920"]},{"boundary":"Ayrı kez veya evre çekirdeği korunmalı; farklı durum ve türler her zaman zaman sıralı sayılmamalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000955/B004","candidate_links":[{"candidate_id":"cand_5fe217ed9166afb1876c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طُور","morph_features":"STEM|POS:N|LEM:Tuwr|ROOT:Twr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:2:1:2","qac_word_ref":"95:2:1","surface_ar":"طُورِ"}],"gloss":"ayrı kez, durum veya evre","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir eylem veya oluşum içindeki ayrı bir kez, süre ya da evreyi gösterir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bağlı yineleme yapısı, bir kezden veya süreden sonra başka bir kez ya da sürenin gelmesini anlatır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çoğul biçim, yaratılışın peş peşe evrelerini veya insanların farklı durum ve türlerini gösterebilir."}}],"root_ar":"ط و ر","root_id":"root_000955","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın bir kezlik gerçekleşme, farklı durum ve süreç evresi çekirdeğini kısa biçimde birlikte karşılar.","boundary_detail":"Ayrı kez veya evre çekirdeği korunmalı; farklı durum ve türler her zaman zaman sıralı sayılmamalıdır.","branch_image_ar":"تتابع الأطوار والحالات","concept_gloss":"ayrı kez, durum veya evre","contextual_glosses":[{"applicability":"Bir eylemin veya sürenin art arda ayrı gerçekleşmeler halinde yinelendiği bağlı yapı içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ayrı gerçekleşmeleri ve bunların peş peşe gelmesini korur."},"facet_ids":["F001","F002"],"text":"bir kezden sonra bir kez daha","usage_role":"contextual"},{"applicability":"İnsanların veya başka varlıkların birbirinden farklı durum ya da türlerde olduğunu bildiren çoğul kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çoğulluğu ve zaman sırası gerektirmeyen durum veya tür farklılığını korur."},"facet_ids":["F003"],"text":"çeşitli durumlar ve türler","usage_role":"contextual"},{"applicability":"Bir oluşumun başlangıçtan sonraki farklı durumlarının sıra içinde geliştiği çoğul kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Evre ayrımını ve evrelerin zaman içinde peş peşe gelmesini korur."},"facet_ids":["F001","F003"],"text":"birbiri ardınca gelen evreler","usage_role":"contextual"}],"definition":"Bir eylemin ya da oluşumun ayrı bir kezini, süresini veya evresini anlatır. Çoğulda peş peşe evreleri ya da zaman sırası gerektirmeden birbirinden farklı durum ve türleri gösterebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir eylem veya oluşum içindeki ayrı bir kez, süre ya da evreyi gösterir."},{"facet_id":"F002","role":"specialization","statement":"Bağlı yineleme yapısı, bir kezden veya süreden sonra başka bir kez ya da sürenin gelmesini anlatır."},{"facet_id":"F003","role":"extension","statement":"Çoğul biçim, yaratılışın peş peşe evrelerini veya insanların farklı durum ve türlerini gösterebilir."}],"identity_rationale":"Kaynak ifadesi yalnızca art arda gelen evreleri değil, bir eylemin ayrı kezlerini veya sürelerini ve çoğulda farklı durum ya da türleri de içerir. Verilen çerçeve kullanılabilir, ancak ardışıklığın farklı türlerden oluşma kullanımında zorunlu olmadığı açıkça belirtilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kez veya evre"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir kezden sonra bir kez daha; dönem dönem"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"çeşitli durumlar, türler veya ardışık evreler"}],"lexicalization_note":"Yalın biçimler kez, evre, durum veya tür bildirir; art arda gelme anlamı yalnızca ilgili çoğul ve bağlı yapılarda açıkça taşınır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler evre geçişi ve yinelenen kez anlamlarıyla en güçlü örtüşmeyi gösterir, kalanlar yalnızca ardışıklık veya yenilik temasını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal tek bir kez anlamına ve sınıf farklılığına kadar uzanır; komşu dalın çekirdeği bir durumdan sonraki duruma geçiş ve evre konumudur.","focus_only":"Ayrı kez veya süreyi ve zaman sırası olmadan farklı durum ya da türleri de gösterebilir.","gloss":"ayrı kez veya evre ve durumdan duruma geçiş","neighbor_only":"Bir durumdan başka bir duruma geçişi ve süreç içindeki konumu doğrudan öne çıkarır.","neighbor_ref":"root_000927/B004","relation_type":"near_synonym","shared_zone":"İki dal da süreç içindeki durumları, evreleri ve bunların birbirini izlemesini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalda her bir kez ayrı bir evre veya farklı durum olabilir; komşu dalda geri dönüş ve aynı şeyin yeniden yapılması daha belirgindir.","focus_only":"Süreç evresi ile farklı durum veya tür anlamlarını da taşır.","gloss":"ayrı kez ve yeniden gerçekleşme","neighbor_only":"Aynı şeyin geri dönmesi veya yeniden yapılması anlamını özellikle içerir.","neighbor_ref":"root_000171/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir eylemin ayrı bir kez gerçekleşmesini ve bunun yinelenmesini anlatabilir."}],"source_phrase_ar":"فعل ذلك طورا بعد طور كأنه فعله مدة بعد مدة (maqayis)؛ الطور التارة يقال طورا بعد طور (ayn)؛ الناس أطوار أي أصناف على حالات شتى (ayn)؛ الطور التارة (sihah)؛ خلقكم أطوارا طورا علقة وطورا مضغة (sihah)؛ فعل كذا طورا بعد طور أي تارة بعد تارة (mufradat)؛ خلقكم أطوارا (mufradat)","source_summary":"Kaynaklar ayrı kez veya süre anlamını, art arda yineleme yapısını ve çoğul biçimin farklı durum, tür ya da oluşum evreleri göstermesini birlikte tanıklar.","sources":["MQ","AY","SI","MU"],"what_is_ar":"التارة بعد التارة، والمرحلة بعد المرحلة، والأحوال أو الأصناف المتعددة كأطوار الخلق","what_is_not_ar":"ليس الحد المكاني ولا الجبل ولا الوحشي."},"support_links":["sup_cbdfb0007f811a519a1d"]},{"boundary":"Dağ çekirdeği sabittir; genel dağ adı ile belirli bir dağın adı arasındaki kapsam farkı korunmalıdır.","branch_kind":"bare","branch_ref":"root_000955/B005","candidate_links":[{"candidate_id":"cand_badae2b9209c3cdc0db0","lane":"micro"},{"candidate_id":"cand_5fe217ed9166afb1876c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طُور","morph_features":"STEM|POS:N|LEM:Tuwr|ROOT:Twr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:2:1:2","qac_word_ref":"95:2:1","surface_ar":"طُورِ"}],"gloss":"dağ veya belirli bir dağın adı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözcük, yüksek bir yer biçimi olarak dağı gösterir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kapsam, belirli ve tanınmış bir dağın adından bütün dağlara uygulanabilen genel ada kadar değişir."}}],"root_ar":"ط و ر","root_id":"root_000955","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dağ çekirdeğini ve kaynaklarda görülen genel ad ile belirli ad arasındaki kapsam farkını birlikte gösterir.","boundary_detail":"Dağ çekirdeği sabittir; genel dağ adı ile belirli bir dağın adı arasındaki kapsam farkı korunmalıdır.","branch_image_ar":"الطور جبلا أو علما على جبل","concept_gloss":"dağ veya belirli bir dağın adı","contextual_glosses":[{"applicability":"Bağlam sözcüğün belirli ve bilinen bir dağı gösterdiğini ortaya koyduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dağ olmayı ve bağlamca belirlenmiş tanınmış bir yeri göstermeyi korur."},"facet_ids":["F001","F002"],"text":"tanınmış dağ","usage_role":"contextual"},{"applicability":"Sözcüğün herhangi bir dağı gösteren genel ad sayıldığı görüş veya bağlam için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Genel yer biçimi olarak dağ anlamını doğrudan korur."},"facet_ids":["F001","F002"],"text":"dağ","usage_role":"general"}],"definition":"Dağ; kaynakların bir bölümünde tanınmış veya belirli bir dağın adı, başka bir görüşte ise her dağ için kullanılabilen bir ad.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözcük, yüksek bir yer biçimi olarak dağı gösterir."},{"facet_id":"F002","role":"source_variant","statement":"Kapsam, belirli ve tanınmış bir dağın adından bütün dağlara uygulanabilen genel ada kadar değişir."}],"identity_rationale":"Kaynak ifadesi dağ anlamında birleşir, ancak bunun tanınmış belirli bir dağ, belirli bir dağın adı veya her dağ için kullanılabilen bir ad olup olmadığı konusunda kapsam farkı bildirir. Verilen çerçeve bu ortak çekirdeği ve kaynak içi kapsam ayrılığını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"dağ; bağlama göre belirli bir dağın adı"}],"lexicalization_note":"Tanım yalın biçimin dağ anlamını verir ve belirli ad ile genel ad arasındaki kaynak farkını açıkça korur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler dağın yükseklik niteliği ve belirli yer adıyla karışmasını açıklar, kalan adaylar başka dağ veya yer adlarının örnekleridir.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal bir nesne türünü veya onun adını bildirir; komşu dal ise nesnenin türünden bağımsız olarak yükseklik niteliğini bildirir.","focus_only":"Bir yer biçimini dağ olarak adlandırır ve belirli bir dağa ad olabilme kapsamını taşır.","gloss":"dağ ve yükseklik","neighbor_only":"Dağ olsun olmasın bir şeyin yüksek ve uzun oluşunu nitelendirir.","neighbor_ref":"root_000824/B001","relation_type":"same_field","shared_zone":"Dağlar tipik olarak yüksek olduğundan iki dal aynı yükselti alanında buluşur."},{"boundary_match":"field_only","distinction":"Odak dalın genel olarak dağ anlamına gelebilmesi mümkündür; komşu dalın çekirdeği ise belirli bir yere verilen özel addır.","focus_only":"Genel dağ adı ile belirli bir dağın adı arasında değişebilen bir kapsama sahiptir.","gloss":"dağ adı ve belirli yer adı","neighbor_only":"Tek tek belirlenmiş bir dağ veya yer için kullanılan özel adı gösterir.","neighbor_ref":"root_001066/B008","relation_type":"same_field","shared_zone":"Her iki dal da bir dağın veya yüksek yerin adlandırılmasıyla ilgilidir."}],"source_phrase_ar":"الطور جبل (maqayis)؛ الطور جبل معروف (ayn)؛ الطور الجبل (sihah)؛ الطور اسم جبل مخصوص وقيل اسم لكل جبل (mufradat)","source_summary":"Kaynakların ortak noktası dağ anlamıdır; toplu ifade bunun tanınmış ya da belirli bir dağın adı mı, yoksa her dağa uygulanabilen genel bir ad mı olduğu konusunda kapsam farkı taşır.","sources":["MQ","AY","SI","MU"],"what_is_ar":"الطور اسما للجبل، إما جبلا معروفا مخصوصا أو اسما يقال للجبل في بعض النقل","what_is_not_ar":"لا يدخل فيه طور بمعنى تارة، ولا طوار الدار، ولا عدا طوره."},"support_links":["sup_cbdfb0007f811a519a1d","sup_d65462b5e8ff61b51226"]},{"boundary":"Dal yabanıllık ve insanlara alışmamışlıkla sınırlıdır; sırf uzaklık veya yalnızlık yeterli değildir.","branch_kind":"bare","branch_ref":"root_000955/B006","candidate_links":[{"candidate_id":"cand_e9e697807537e9325d9d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طُور","morph_features":"STEM|POS:N|LEM:Tuwr|ROOT:Twr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:2:1:2","qac_word_ref":"95:2:1","surface_ar":"طُورِ"}],"gloss":"yabanıl ve insanlara alışmamış","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Canlının yabanıl, yabanıllaşmış veya insanlarla yakınlığa alışmamış olduğunu bildirir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Niteliğin açıklaması, insanlarla alışıklığın olağan sınırından uzaklaşma düşüncesine bağlanır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kuşlar, başka hayvanlar ve insanlar bu nitelikle betimlenebilir."}}],"root_ar":"ط و ر","root_id":"root_000955","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kuş, başka hayvan veya insanın insanlarla yakınlığa alışmamış yabanıl durumunu karşılar.","boundary_detail":"Dal yabanıllık ve insanlara alışmamışlıkla sınırlıdır; sırf uzaklık veya yalnızlık yeterli değildir.","branch_image_ar":"التوحش والخروج عن حد الأنس","concept_gloss":"yabanıl ve insanlara alışmamış","contextual_glosses":[{"applicability":"Nitelik özellikle kuş veya benzeri bir hayvan için kullanıldığında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Canlının kuş oluşunu, yabanıllığını ve insana alışmamışlığını korur."},"facet_ids":["F001","F003"],"text":"insana alışmamış yabanıl kuş","usage_role":"contextual"},{"applicability":"Nitelik bir insanın alışılmadık ölçüde yabanıl ve insan yakınlığından uzak oluşunu bildirdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsana uygulanmayı, yabanıllığı ve alışılmış yakınlıktan uzaklığı korur."},"facet_ids":["F001","F002","F003"],"text":"insanlardan uzak duran yabanıl kimse","usage_role":"contextual"}],"definition":"Kuş, başka bir hayvan veya insan için yabanıl, yabanıllaşmış ya da insanlara alışmamış olma niteliği. Bir açıklamada bu durum, alışıklığın olağan sınırından uzaklaşmış sayılmaya bağlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Canlının yabanıl, yabanıllaşmış veya insanlarla yakınlığa alışmamış olduğunu bildirir."},{"facet_id":"F002","role":"associated_use","statement":"Niteliğin açıklaması, insanlarla alışıklığın olağan sınırından uzaklaşma düşüncesine bağlanır."},{"facet_id":"F003","role":"example","statement":"Kuşlar, başka hayvanlar ve insanlar bu nitelikle betimlenebilir."}],"identity_rationale":"Kaynak ifadesi kuşlar, başka hayvanlar ve insanlar için yabanıl ya da insanlara alışmamış olma niteliğini açıkça tanıklar. Bir açıklama bu niteliği alışıklığın olağan sınırından uzaklaşmayla ilişkilendirir; bu, çekirdeği değiştirmeyen bağımlı bir gerekçelendirmedir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yabanıl, yabanıllaşmış veya insanlara alışmamış"}],"lexicalization_note":"Tanım tanıklanan niteleme biçimlerinin yalın yabanıllık anlamını verir ve başka yapılardan anlam aktarmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler genel yabanıllık ile yabanıllaşma sürecini ayırır, kalan adaylar uzaklık, yalnızlık veya yabancılık bakımından daha gevşek ilişkilidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli niteleme biçimlerinin kuş, hayvan ve insana uygulanışıdır; komşu dal yabanıl canlı ve nesne alanını daha genel kurar.","focus_only":"Belirli niteleme biçimleriyle özellikle kuşlara ve insanlara uygulanır ve alışıklık sınırından uzaklaşma açıklamasını taşır.","gloss":"insana alışmamış ve genel yabanıl","neighbor_only":"Genel olarak bütün kara hayvanlarını ve insanlardan uzak duran her şeyi kapsayabilir.","neighbor_ref":"root_001632/B001","relation_type":"near_synonym","shared_zone":"İki dalın ortak çekirdeği insanlara alışmama ve evcil ya da yakın olunan durumun dışında kalmadır."},{"boundary_match":"partial","distinction":"Odak dal öncelikle kalıcı ya da gözlenen bir niteliği verir; komşu dal ürkme, kaçınma ve yabanıllaşma eylemini daha belirgin taşır.","focus_only":"Canlının yabanıl veya alışmamış durumunu niteleme olarak bildirir.","gloss":"yabanıl durum ve yabanıllaşıp ürkme","neighbor_only":"Canlının insanlardan ürküp uzaklaşması ve yabanıllaşması sürecini özellikle anlatır.","neighbor_ref":"root_000004/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da insan yakınlığından uzaklaşan veya insana alışmamış canlıları konu eder."}],"source_phrase_ar":"للوحشي من الطير وغيرها طوري وطوارني فهو من هذا كأنه توحش فعدا الطور (maqayis)؛ رجل طوري وطوراني (ayn)؛ الطوري الوحشي من الطير والناس (sihah)؛ حمام طوري وطوراني (sihah)","source_summary":"Toplu kanıt nitelemeyi yabanıl veya insanlara alışmamış kuş, hayvan ve insanlara uygular; ayrıca bir açıklama bunu alışıklık sınırından uzaklaşma düşüncesiyle ilişkilendirir.","sources":["MQ","AY","SI"],"what_is_ar":"وصف طوري وطوراني للوحشي أو المتوحش من الطير والناس، وما تباعد عن حد الأنس","what_is_not_ar":"ليس النسبة إلى الجبل هنا، ولا معنى التارة، ولا نفي وجود أحد."},"support_links":["sup_00c4dd648bee505a9f6d"]},{"boundary":"Anlam yalnızca tanıklanan yokluk bildiren yapıya bağlıdır; yalın bir sözcük anlamı değildir.","branch_kind":"non_bare","branch_ref":"root_000955/B007","candidate_links":[{"candidate_id":"cand_e9e697807537e9325d9d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طُور","morph_features":"STEM|POS:N|LEM:Tuwr|ROOT:Twr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:2:1:2","qac_word_ref":"95:2:1","surface_ar":"طُورِ"}],"gloss":"orada hiç kimsenin bulunmaması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Olumsuz yapı, belirtilen yerde tek bir kişinin bile bulunmadığını bildirir."}}],"root_ar":"ط و ر","root_id":"root_000955","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca belirli olumsuz yapı içinde bir yerin insan bakımından bütünüyle boş olduğunu bildirir.","boundary_detail":"Anlam yalnızca tanıklanan yokluk bildiren yapıya bağlıdır; yalın bir sözcük anlamı değildir.","branch_image_ar":"نفي وجود أحد في الموضع","concept_gloss":"orada hiç kimsenin bulunmaması","contextual_glosses":[{"applicability":"Tanıklanan olumsuz yapının doğal ve doğrudan cümle karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yeri ve hiç kimsenin bulunmaması yargısını eksiksiz korur."},"facet_ids":["F001"],"text":"orada hiç kimse yok","usage_role":"contextual"}],"definition":"Belirli bir olumsuz yapı içinde, söz konusu yerde hiç kimsenin bulunmadığını bildiren kalıplaşmış kullanım.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Olumsuz yapı, belirtilen yerde tek bir kişinin bile bulunmadığını bildirir."}],"identity_rationale":"Tek kaynak ifadesi, belirli bir olumsuz yapı içinde bir yerde hiç kimsenin bulunmadığını açıkça bildirir. Dalın dar kalıp anlamı bu kanıtla tam uyumludur ve yabanıllık ya da dağ anlamına genişletilemez.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"orada hiç kimse yok"}],"lexicalization_note":"Tanım yalnızca bir yerde hiç kimse bulunmadığını bildiren tanıklanmış yapıyı kapsar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eşdeğer yapı ile daha geniş yokluk alanı yayımlandı, kalan adaylar aynı yargıyı başka dar sözcüklerle yineler veya genel boşluğu anlatır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Kavramsal çekirdek ve yapı sınırı aynıdır; ayrım yalnızca kaynak dilde kullanılan sözcük biçimindedir.","focus_only":null,"gloss":"bir yerde hiç kimsenin bulunmaması","neighbor_only":null,"neighbor_ref":"root_000622/B007","relation_type":"synonym","shared_zone":"İki dal da olumsuz bir yapı içinde belirtilen yerde hiç kimse bulunmadığını bildirir."},{"boundary_match":"partial","distinction":"Odak dal tek yapıya ve insan yokluğuna bağlıdır; komşu dal farklı biçimlere ve insan dışındaki belirti veya bilgi yokluğuna genişleyebilir.","focus_only":"Tek bir dar yapı içinde yalnızca hiç kimsenin bulunmamasını bildirir.","gloss":"hiç kimsenin olmaması ve genel iz yokluğu","neighbor_only":"Birden çok olumsuz biçimi ve kimi kullanımlarda hiçbir belirti ya da bilgi bulunmamasını da kapsar.","neighbor_ref":"root_000075/B008","relation_type":"near_synonym","shared_zone":"İki dal da bir yerde insan bulunmadığını olumsuz bir yapı aracılığıyla bildirebilir."}],"source_phrase_ar":"ما بها طوري أي أحد (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Tanıklanan olumsuz yapı, söz konusu yerde hiç kimsenin bulunmadığını bildirir."}],"source_summary":"Ortak kaynak özeti yoktur; bu dar yapı ve yokluk anlamı tek bir kaynağın tanıklığına dayanır.","sources":["SI"],"what_is_ar":"الاستعمال الضيق في قولهم ما بها طوري، أي ليس بها أحد","what_is_not_ar":"ليس الوحشي طوري ولا الطور الجبل ولا التارة."},"support_links":["sup_00c4dd648bee505a9f6d"]}],"candidate_inventory":[{"anchor_refs":["95:2:1"],"branch_refs":[],"candidate_id":"cand_63b025aea9aa98ff6664","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:2:1:ayah-boundary-continuation","source_type":"word_analysis","support_ids":["sup_984452e9d2c106748b77","sup_d2ac158b174927e4d0d6"],"title":"boundary falls inside the sworn list","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:2:1","qac_refs":["95:2:1:1"],"status":"accepted"}},{"anchor_refs":["95:2:1"],"branch_refs":[],"candidate_id":"cand_6f305675ebd1dd93501d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:2:1:botany-to-geography-link","source_type":"word_analysis","support_ids":["sup_a496c6cbec4e594090ad","sup_d2ac158b174927e4d0d6"],"title":"particle carries the move from trees to mountain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:2:1","qac_refs":["95:2:1:1"],"status":"accepted"}},{"anchor_refs":["95:2:1"],"branch_refs":[],"candidate_id":"cand_6a55c3e24a474d0c506f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:2:1:oath-scope-and-deferred-answer","source_type":"word_analysis","support_ids":["sup_808a42eb55182b6d1f67","sup_d2ac158b174927e4d0d6"],"title":"oath force governs a deferred qasam frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:2:1","qac_refs":["95:2:1:1"],"status":"accepted"}},{"anchor_refs":["95:2:1"],"branch_refs":[],"candidate_id":"cand_57e7649e890f4050c29c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:2:1:visible-proclitic-fusion","source_type":"word_analysis","support_ids":["sup_92f3c4e56d4a0d2f7791","sup_d2ac158b174927e4d0d6"],"title":"written attachment compresses oath and noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:2:1","qac_refs":["95:2:1:1"],"status":"accepted"}},{"anchor_refs":["95:2:2"],"branch_refs":[],"candidate_id":"cand_72a2b53f69d72be27383","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000955"],"scope":"focus_ayah","source_local_id":"95:2:2:acoustic-weight","source_type":"word_analysis","support_ids":["sup_36f76b59eb2a59876cad","sup_e6f94e9aca18222df343"],"title":"heavy sound matches the mountain image","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:2:2","qac_refs":["95:2:1:2"],"status":"accepted"}},{"anchor_refs":["95:2:2"],"branch_refs":[],"candidate_id":"cand_28104e6436d2b0e81fd5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000955"],"scope":"focus_ayah","source_local_id":"95:2:2:botany-to-elevated-landscape","source_type":"word_analysis","support_ids":["sup_36f76b59eb2a59876cad","sup_6bb525d2974e8a8d4051"],"title":"tree-bearing mountain bridges the oath images","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:2:2","qac_refs":["95:2:1:2"],"status":"accepted"}},{"anchor_refs":["95:2:2"],"branch_refs":[],"candidate_id":"cand_9551a68076bbf036f6e7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000955"],"scope":"focus_ayah","source_local_id":"95:2:2:construct-sinai-specificity","source_type":"word_analysis","support_ids":["sup_36f76b59eb2a59876cad","sup_3ca887077d748944ddee"],"title":"construct grammar specifies the Mount","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:2:2","qac_refs":["95:2:1:2"],"status":"accepted"}},{"anchor_refs":["95:2:2"],"branch_refs":[],"candidate_id":"cand_67de30f251f04286ca02","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000955"],"scope":"focus_ayah","source_local_id":"95:2:2:content-word-pivot","source_type":"word_analysis","support_ids":["sup_36f76b59eb2a59876cad","sup_a13508f1f216ab3be345"],"title":"first content word turns the oath scene","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:2:2","qac_refs":["95:2:1:2"],"status":"accepted"}},{"anchor_refs":["95:2:2"],"branch_refs":[],"candidate_id":"cand_cfa0046920e9957206ca","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000955"],"scope":"focus_ayah","source_local_id":"95:2:2:dense-hinge-convergence","source_type":"word_analysis","support_ids":["sup_36f76b59eb2a59876cad","sup_4af5a20c49190234f903"],"title":"grammar, image, and sound converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:2:2","qac_refs":["95:2:1:2"],"status":"accepted"}},{"anchor_refs":["95:2:2"],"branch_refs":[],"candidate_id":"cand_8eaf92b847bbad041c66","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000955"],"scope":"focus_ayah","source_local_id":"95:2:2:genitive-sworn-witness","source_type":"word_analysis","support_ids":["sup_34ca42c1f9d87f938c3b","sup_36f76b59eb2a59876cad"],"title":"genitive case makes the mountain sworn-by","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:2:2","qac_refs":["95:2:1:2"],"status":"accepted"}},{"anchor_refs":["95:2:2"],"branch_refs":[],"candidate_id":"cand_7b336646b1c485099401","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000955"],"scope":"focus_ayah","source_local_id":"95:2:2:loanword-versus-arabic-field","source_type":"word_analysis","support_ids":["sup_36f76b59eb2a59876cad","sup_54cacb51a252165359a0"],"title":"borrowed name and Arabic root field both press","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:2:2","qac_refs":["95:2:1:2"],"status":"accepted"}},{"anchor_refs":["95:2:2"],"branch_refs":[],"candidate_id":"cand_122f707e44a6d9a615a7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000955"],"scope":"focus_ayah","source_local_id":"95:2:2:mountain-with-stage-pressure","source_type":"word_analysis","support_ids":["sup_36f76b59eb2a59876cad","sup_b8a2e107c7b1a27a536a"],"title":"stage field remains secondary to the Mount","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:2:2","qac_refs":["95:2:1:2"],"status":"accepted"}},{"anchor_refs":["95:2:2"],"branch_refs":[],"candidate_id":"cand_a0e877b98f12f760a559","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000955"],"scope":"focus_ayah","source_local_id":"95:2:2:sacred-geography-and-intertexts","source_type":"word_analysis","support_ids":["sup_2fa38a6a2e3c7f301af4","sup_36f76b59eb2a59876cad"],"title":"Sinai cluster frames the mountain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:2:2","qac_refs":["95:2:1:2"],"status":"accepted"}},{"anchor_refs":["95:2:3"],"branch_refs":[],"candidate_id":"cand_e7e6caf51853109ad9d7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:2:3:dense-place-name-convergence","source_type":"word_analysis","support_ids":["sup_4579a2d3ebefcc550c1b","sup_c884b0749a03c3199d49"],"title":"form, rarity, variants, and sound converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:2:3","qac_refs":["95:2:2:1"],"status":"accepted"}},{"anchor_refs":["95:2:3"],"branch_refs":[],"candidate_id":"cand_7d3e361274f16420db9b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:2:3:qiraat-and-sinai-form-variants","source_type":"word_analysis","support_ids":["sup_ae4564e9a6bee628e39f","sup_c884b0749a03c3199d49"],"title":"variant forms test the Sinai naming pattern","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:2:3","qac_refs":["95:2:2:1"],"status":"accepted"}},{"anchor_refs":["95:2:3"],"branch_refs":[],"candidate_id":"cand_78d761efe1ee45e4d6ae","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:2:3:radiance-and-provenance-pressure","source_type":"word_analysis","support_ids":["sup_91cc8d06e912ee8a8dd6","sup_c884b0749a03c3199d49"],"title":"radiance and origin claims remain secondary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:2:3","qac_refs":["95:2:2:1"],"status":"accepted"}},{"anchor_refs":["95:2:3"],"branch_refs":[],"candidate_id":"cand_8d9672d3b0a9051fbf21","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:2:3:serrated-variant-image","source_type":"word_analysis","support_ids":["sup_9a3cc3104e393df60bb6","sup_c884b0749a03c3199d49"],"title":"edge image is apparatus, not the local sense","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:2:3","qac_refs":["95:2:2:1"],"status":"accepted"}},{"anchor_refs":["95:2:3"],"branch_refs":[],"candidate_id":"cand_fa4cb20926352a68d949","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:2:3:sinai-complement-specificity","source_type":"word_analysis","support_ids":["sup_2c986bcea3f1418bd275","sup_c884b0749a03c3199d49"],"title":"Sinai complement specifies the mount","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:2:3","qac_refs":["95:2:2:1"],"status":"accepted"}},{"anchor_refs":["95:2:3"],"branch_refs":[],"candidate_id":"cand_a36321c45184c1ad5566","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:2:3:sound-cadence-continuity","source_type":"word_analysis","support_ids":["sup_32b0dad08329a70f4768","sup_c884b0749a03c3199d49"],"title":"nasal cadence sustains the oath phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:2:3","qac_refs":["95:2:2:1"],"status":"accepted"}},{"anchor_refs":["95:2:3"],"branch_refs":[],"candidate_id":"cand_cdf9a53eaa558705e4b2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:2:3:years-variant-pressure","source_type":"word_analysis","support_ids":["sup_c884b0749a03c3199d49","sup_f7e75971e0a85f00f28f"],"title":"near form can shift place toward years","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:2:3","qac_refs":["95:2:2:1"],"status":"accepted"}},{"anchor_refs":["95:2:1"],"branch_refs":[],"candidate_id":"cand_53f54349192ce2e9b6ae","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000955"],"scope":"focus_ayah","source_local_id":"95:2:1:2","source_type":"qac_morpheme","support_ids":["sup_7bdaca026a155fd75195"],"title":"QAC root occurrence: ط و ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["95:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"95:2","branch_refs":["root_000955/B005"],"candidate_id":"cand_badae2b9209c3cdc0db0","commentary_obligation":"review","hft_ref":"hft_f0f5c811760f47f82065","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_named_mount","source_type":"hft","support_ids":["sup_d65462b5e8ff61b51226"],"title":"b_named_mount","trust":"legacy_unbound"},{"anchor_refs":["95:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"95:2","branch_refs":["root_000955/B001","root_000955/B002","root_000955/B003"],"candidate_id":"cand_2d8149c440b4fb812b82","commentary_obligation":"review","hft_ref":"hft_10ef311d944ca1ef23bf","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_precinct_edge","source_type":"hft","support_ids":["sup_64ab3685906542b0f920"],"title":"b_precinct_edge","trust":"legacy_unbound"},{"anchor_refs":["95:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"95:2","branch_refs":["root_000955/B004","root_000955/B005"],"candidate_id":"cand_5fe217ed9166afb1876c","commentary_obligation":"review","hft_ref":"hft_6de481963375d5d2c29d","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_successive_states","source_type":"hft","support_ids":["sup_cbdfb0007f811a519a1d"],"title":"b_successive_states","trust":"legacy_unbound"},{"anchor_refs":["95:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"95:2","branch_refs":["root_000955/B006","root_000955/B007"],"candidate_id":"cand_e9e697807537e9325d9d","commentary_obligation":"review","hft_ref":"hft_6df1c867f065d0bc01b8","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_wild_empty_margin","source_type":"hft","support_ids":["sup_00c4dd648bee505a9f6d"],"title":"b_wild_empty_margin","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَطُورِ سِينِينَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"95:2:1:1","qac_word_ref":"95:2:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"طُور","morph_features":"STEM|POS:N|LEM:Tuwr|ROOT:Twr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:2:1:2","qac_word_ref":"95:2:1","root_ar":"ط و ر","surface_ar":"طُورِ"},{"lemma_ar":"سِينِين","morph_features":"STEM|POS:PN|LEM:siyniyn|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"95:2:2:1","qac_word_ref":"95:2:2","root_ar":"","surface_ar":"سِينِينَ"}],"word_analysis_qac_refs":[["95:2:1:1"],["95:2:1:2"],["95:2:2:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["95:2:1","95:2:2","95:2:3"]},"focus_surface_evidence":{"arabic_uthmani":"وَطُورِ سِينِينَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"95:2:1:1","qac_word_ref":"95:2:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"طُور","morph_features":"STEM|POS:N|LEM:Tuwr|ROOT:Twr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:2:1:2","qac_word_ref":"95:2:1","root_ar":"ط و ر","surface_ar":"طُورِ"},{"lemma_ar":"سِينِين","morph_features":"STEM|POS:PN|LEM:siyniyn|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"95:2:2:1","qac_word_ref":"95:2:2","root_ar":"","surface_ar":"سِينِينَ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["95:2:1:1"],["95:2:1:2"],["95:2:2:1"]],"word_analysis_refs":["95:2:1","95:2:2","95:2:3"],"word_rows":[{"analysis_record_ref":"95:2:1","analytic_gloss_range_en":"oath-and-coordination particle that carries the oath series forward and governs the following genitive phrase","analytic_root_gloss_range_en":null,"qac_refs":["95:2:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"95:2:2","analytic_gloss_range_en":"construct head naming the Mount in the Sinai phrase; locally a genitive sworn object rather than an abstract stage noun","analytic_root_gloss_range_en":"root range includes mountain, successive stages or turns, boundary, surrounding precinct, and limit imagery; the local construct selects the Mount while allowing some secondary stage and elevation pressure","qac_refs":["95:2:1:2"],"root":{"arabic":"ط و ر","transliteration":"ṭ-w-r"},"surface":{"arabic":"طُورِ","transliteration":"ṭūri"}},{"analysis_record_ref":"95:2:3","analytic_gloss_range_en":"Sinai place-name as genitive complement to the Mount; variant and etymological pressures remain secondary to the local proper-name reading","analytic_root_gloss_range_en":"root range includes the Sinai/Sinin place-name cluster and separate letter or future-marker material; local construct selects the Sinai expression, with radiance, years, and variant-form pressures only as apparatus","qac_refs":["95:2:2:1"],"root":{"arabic":"س ي ن","transliteration":"s-y-n"},"surface":{"arabic":"سِينِينَ","transliteration":"sīnīna"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["95:2"],"branch_refs":["root_000955/B005"],"candidate_id":"cand_badae2b9209c3cdc0db0","evidence_scope":"focus_ayah","hft_ref":"hft_f0f5c811760f47f82065","item_id":"b_named_mount","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_named_mount","support_id":"sup_d65462b5e8ff61b51226"},{"anchor_refs":["95:2"],"branch_refs":["root_000955/B001","root_000955/B002","root_000955/B003"],"candidate_id":"cand_2d8149c440b4fb812b82","evidence_scope":"focus_ayah","hft_ref":"hft_10ef311d944ca1ef23bf","item_id":"b_precinct_edge","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_precinct_edge","support_id":"sup_64ab3685906542b0f920"},{"anchor_refs":["95:2"],"branch_refs":["root_000955/B004","root_000955/B005"],"candidate_id":"cand_5fe217ed9166afb1876c","evidence_scope":"focus_ayah","hft_ref":"hft_6de481963375d5d2c29d","item_id":"b_successive_states","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_successive_states","support_id":"sup_cbdfb0007f811a519a1d"},{"anchor_refs":["95:2"],"branch_refs":["root_000955/B006","root_000955/B007"],"candidate_id":"cand_e9e697807537e9325d9d","evidence_scope":"focus_ayah","hft_ref":"hft_6df1c867f065d0bc01b8","item_id":"b_wild_empty_margin","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_wild_empty_margin","support_id":"sup_00c4dd648bee505a9f6d"}],"diagnostics":[],"lane_counts":{"global":9,"macro":12,"micro":4},"packet_summary":{"ayah_count":8,"focus_ref":"95:2","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ر د د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000555","furuq_root_norm":"ر د د","furuq_source_root_norm":"ر د د","is_dominant":true,"target_occurrences":52,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001413","furuq_root_norm":"م ر د","furuq_source_root_norm":"م ر د","is_dominant":false,"target_occurrences":5,"target_rank":2}]}],"window":["95:1","95:2","95:3","95:4","95:5","95:6","95:7","95:8"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"95:2","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":16,"unstructured_record_count":0},"identity":{"ayah_ref":"95:2","lane":"micro","linguistic_source_ref":"95:2","surface_ref":"95:2","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"95:2","target_tokens":[["Sina",["95:2:2"]],["Dağı'na",["95:2:1","95:2:2"]],["da",["95:2:1"]],["andolsun",["95:2:1","95:2:2"]]],"text":"Sina Dağı'na da andolsun."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":8,"id":"s095-p01-001-008","label":"Whole surah","number":1,"refs":["95:1","95:2","95:3","95:4","95:5","95:6","95:7","95:8"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:3:sinai-complement-specificity","source_type":"word_analysis","support_id":"sup_2c986bcea3f1418bd275","text":"{\"blocking_evidence\":null,\"headline\":\"Sinai complement specifies the mount\",\"reader_payoff\":\"The reader notices that the second word is not a separate noun beside the mountain; it is the genitive complement that identifies and classifies the Mount as Sinaitic.\",\"reason\":\"QAC and attachment evidence make the word the genitive complement in a construct phrase, and V4 preserves the Sinai/Sinin expression branch as the locally compatible sense.\",\"representative_source_ids\":[\"QG-71427135\",\"QG-987635e2\",\"QG-b132827f\",\"QG-c0f734a2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:2:sacred-geography-and-intertexts","source_type":"word_analysis","support_id":"sup_2fa38a6a2e3c7f301af4","text":"{\"blocking_evidence\":null,\"headline\":\"Sinai cluster frames the mountain\",\"reader_payoff\":\"The reader notices that this is a marked sacred-geography use tied to Sinai passages, including 20:80, 23:20, 28:46, and the Mount oath in 52:1.\",\"reason\":\"The contextual profile treats this exact root and form as low-occurrence and proper-name aligned, and the CRITICAL row supplies concrete Sinai references (20:80, 23:20, 28:46, 52:1).\",\"representative_source_ids\":[\"MI-2d520246\",\"QI-b8290960\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:3:sound-cadence-continuity","source_type":"word_analysis","support_id":"sup_32b0dad08329a70f4768","text":"{\"blocking_evidence\":null,\"headline\":\"nasal cadence sustains the oath phrase\",\"reader_payoff\":\"The reader notices that the sibilant, repeated nasals, and long vowels make the place-name sound continuous with both the mount word and the prior oath cadence in 95:1.\",\"reason\":\"The phonetic claims match the local surface and reinforce the construct phrase without changing the selected Sinai sense.\",\"representative_source_ids\":[\"QE-8d88eb5c\",\"QP-15d027ab\",\"QP-2ee26308\",\"MP-0ac90fc1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:2:genitive-sworn-witness","source_type":"word_analysis","support_id":"sup_34ca42c1f9d87f938c3b","text":"{\"blocking_evidence\":null,\"headline\":\"genitive case makes the mountain sworn-by\",\"reader_payoff\":\"The reader notices that the mountain is not merely named as scenery; its genitive role makes it the entity by which the coming claim is solemnized.\",\"reason\":\"The word is genitive under the oath particle and also heads the construct phrase, so its case is part of both oath governance and local phrase structure.\",\"representative_source_ids\":[\"QG-cce2ae26\",\"QI-afa85473\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:2","source_type":"word_analysis","support_id":"sup_36f76b59eb2a59876cad","text":"{\"gloss_range\":\"construct head naming the Mount in the Sinai phrase; locally a genitive sworn object rather than an abstract stage noun\",\"prose\":\"{{ar:طُورِ}} ({{tr:ṭūri}}) is the head of the construct phrase, so the word does not remain a free mountain noun: {{ar:سِينِينَ}} ({{tr:sīnīna}}) specifies it as the Sinai mount, and the oath particle makes the whole phrase a sworn-by witness. The genitive form therefore carries two pressures at once, construct binding and oath role. The broader {{ar:ط و ر}} ({{tr:ṭ-w-r}}) field includes stages and turns, and that field is especially audible beside {{ar:أَطْوَارًا}} ({{tr:aṭwāran}}) in 71:14, but local grammar keeps the selected sense as the Mount rather than an abstract phase. That same pressure leaves the inherited or borrowed sacred-geography name in conversation with Arabic stage, boundary, and limit imagery, without making those branches the local referent. The mountain image gives the oath a raised, durable landscape after the cultivated trees of 95:1; reports of a tree-bearing mountain and the Sinai tree association in 23:20 make that transition continuous rather than abrupt. The word also belongs to a wider Sinai set, including 20:80, 23:20, 28:46, and the unqualified oath by the Mount in 52:1, while the heavy opening sound gives this content-word pivot acoustic weight.\",\"root_display\":\"{{ar:ط و ر}} ({{tr:ṭ-w-r}})\",\"root_gloss_range\":\"root range includes mountain, successive stages or turns, boundary, surrounding precinct, and limit imagery; the local construct selects the Mount while allowing some secondary stage and elevation pressure\",\"surface_display\":\"{{ar:طُورِ}} ({{tr:ṭūri}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:2:construct-sinai-specificity","source_type":"word_analysis","support_id":"sup_3ca887077d748944ddee","text":"{\"blocking_evidence\":null,\"headline\":\"construct grammar specifies the Mount\",\"reader_payoff\":\"The reader notices that the unarticled noun becomes a specified Sinai mount through construct binding, not an indefinite mountain image.\",\"reason\":\"QAC and attachment evidence make the word the construct head governing the Sinai complement, and V4 includes the Mount or mountain branch as the locally compatible branch.\",\"representative_source_ids\":[\"QG-0b6e004e\",\"QG-182560f2\",\"MG-fae53cc5\",\"QF-1791ba12\",\"QF-3e0ad28d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:3:dense-place-name-convergence","source_type":"word_analysis","support_id":"sup_4579a2d3ebefcc550c1b","text":"{\"blocking_evidence\":null,\"headline\":\"form, rarity, variants, and sound converge\",\"reader_payoff\":\"The reader notices that the place-name is analytically dense because rarity, etymology, variant morphology, and sound texture all gather around one short complement.\",\"reason\":\"The synthesis row is retained because its parts are either locally selected, such as the Sinai complement, or explicitly narrowed as variant and provenance pressure.\",\"representative_source_ids\":[\"QY-9196a3cf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:2:dense-hinge-convergence","source_type":"word_analysis","support_id":"sup_4af5a20c49190234f903","text":"{\"blocking_evidence\":null,\"headline\":\"grammar, image, and sound converge\",\"reader_payoff\":\"The reader notices that construct grammar, oath role, mountain imagery, secondary stage pressure, and sound texture converge in one hinge word.\",\"reason\":\"The synthesis row is retained as a convergence topic because its component claims are individually supported or narrowed elsewhere in the same word analysis.\",\"representative_source_ids\":[\"QY-ee159645\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:2:loanword-versus-arabic-field","source_type":"word_analysis","support_id":"sup_54cacb51a252165359a0","text":"{\"blocking_evidence\":null,\"headline\":\"borrowed name and Arabic root field both press\",\"reader_payoff\":\"The reader notices that the word can be heard as inherited sacred-geography nomenclature while Arabic root branches still create stage and boundary pressure around it.\",\"reason\":\"V4 lists Arabic root branches including mountain, stages, boundaries, and limits, while the CRITICAL row preserves a loanword provenance claim; local grammar chooses the Mount rather than deciding etymology.\",\"representative_source_ids\":[\"QS-b00d145b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:2:botany-to-elevated-landscape","source_type":"word_analysis","support_id":"sup_6bb525d2974e8a8d4051","text":"{\"blocking_evidence\":null,\"headline\":\"tree-bearing mountain bridges the oath images\",\"reader_payoff\":\"The reader notices that the move from fig and olive in 95:1 to Sinai in 95:2 can remain thematically continuous through tree-bearing mountain imagery and the Sinai tree association in 23:20.\",\"reason\":\"The local word still names the Mount, so vegetation does not become the selected sense; it survives as a lexical and inter-ayah bridge to the prior tree imagery and to 23:20.\",\"representative_source_ids\":[\"QS-fd3d348a\",\"MS-044a88b4\",\"MT-6fc92b5b\",\"QE-594f9a25\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"95:2:1:2","source_type":"qac_morpheme","support_id":"sup_7bdaca026a155fd75195","text":"{\"lemma_ar\":\"طُور\",\"morph_features\":\"STEM|POS:N|LEM:Tuwr|ROOT:Twr|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"95:2:1:2\",\"qac_word_ref\":\"95:2:1\",\"root_ar\":\"ط و ر\",\"surface_ar\":\"طُورِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:1:oath-scope-and-deferred-answer","source_type":"word_analysis","support_id":"sup_808a42eb55182b6d1f67","text":"{\"blocking_evidence\":null,\"headline\":\"oath force governs a deferred qasam frame\",\"reader_payoff\":\"The reader notices that this particle is not a loose connective; it governs the genitive sworn phrase and leaves the oath answer pending until 95:4.\",\"reason\":\"QAC and attachment evidence identify the particle as the oath governor before the genitive phrase, with the oath verb compressed and the response supplied later in the surah.\",\"representative_source_ids\":[\"QG-856e0d6c\",\"QG-ed2bfbf6\",\"MG-5ab065c6\",\"QS-c9970bbb\",\"QI-cc06e918\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:3:radiance-and-provenance-pressure","source_type":"word_analysis","support_id":"sup_91cc8d06e912ee8a8dd6","text":"{\"blocking_evidence\":null,\"headline\":\"radiance and origin claims remain secondary\",\"reader_payoff\":\"The reader notices that the place-name may carry beauty or radiance explanations and foreign-name provenance questions, while the local grammar still selects Sinai as the referent.\",\"reason\":\"V4 centers the local branch on the Mount Sinai/Sinin cluster and contextual evidence shows constrained occurrence, so radiance and provenance claims survive as interpretive pressure rather than replacing the place-name.\",\"representative_source_ids\":[\"QS-47c93c69\",\"QS-546e434e\",\"QS-b4546872\",\"MS-5d86d353\",\"MS-e6ffdc6a\",\"QI-4ab13fb6\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:1:visible-proclitic-fusion","source_type":"word_analysis","support_id":"sup_92f3c4e56d4a0d2f7791","text":"{\"blocking_evidence\":null,\"headline\":\"written attachment compresses oath and noun\",\"reader_payoff\":\"The reader notices that the oath relation is encountered as an attached written form before the noun can be processed independently.\",\"reason\":\"The particle is proclitic to the following noun in the written surface, while the grammar still separates its oath-governing function from the content word.\",\"representative_source_ids\":[\"QF-7095294b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:1:ayah-boundary-continuation","source_type":"word_analysis","support_id":"sup_984452e9d2c106748b77","text":"{\"blocking_evidence\":null,\"headline\":\"boundary falls inside the sworn list\",\"reader_payoff\":\"The reader notices that 95:2 begins as continuation, so the ayah division does not close the oath sequence opened in 95:1.\",\"reason\":\"The initial particle explicitly links the new genitive sworn phrase to the preceding oath items, and translation support recommends reading the surrounding oath window.\",\"representative_source_ids\":[\"QT-073336d6\",\"QT-fad0025a\",\"QB-af82a850\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:3:serrated-variant-image","source_type":"word_analysis","support_id":"sup_9a3cc3104e393df60bb6","text":"{\"blocking_evidence\":null,\"headline\":\"edge image is apparatus, not the local sense\",\"reader_payoff\":\"The reader notices that a variant-linked edge or serration image can make the mountain profile feel more concrete, while the received local word remains the Sinai place-name.\",\"reason\":\"The local root and V4 guardrail do not make a serration branch the selected sense, so the claim is limited to variant-linked imagery around the place-name.\",\"representative_source_ids\":[\"QS-52742a2e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:2:content-word-pivot","source_type":"word_analysis","support_id":"sup_a13508f1f216ab3be345","text":"{\"blocking_evidence\":null,\"headline\":\"first content word turns the oath scene\",\"reader_payoff\":\"The reader notices that this first content word after the boundary turns the oath field from cultivated plant products in 95:1 to enduring prophetic landscape.\",\"reason\":\"The surrounding oath sequence and ayah boundary make the mountain noun the local pivot from one class of sworn object to another.\",\"representative_source_ids\":[\"QT-50374eb2\",\"QB-ec833998\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:1:botany-to-geography-link","source_type":"word_analysis","support_id":"sup_a496c6cbec4e594090ad","text":"{\"blocking_evidence\":null,\"headline\":\"particle carries the move from trees to mountain\",\"reader_payoff\":\"The reader notices that the connective does not only add another item; it carries the oath list from cultivated plant imagery in 95:1 to mountain geography in 95:2.\",\"reason\":\"The grammatical continuation licensed by the particle supports reading the second ayah as the next step in the same sworn sequence.\",\"representative_source_ids\":[\"MT-69fb1215\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:3:qiraat-and-sinai-form-variants","source_type":"word_analysis","support_id":"sup_ae4564e9a6bee628e39f","text":"{\"blocking_evidence\":null,\"headline\":\"variant forms test the Sinai naming pattern\",\"reader_payoff\":\"The reader notices that the Sinai referent can be carried through different recitational shapes, especially the alignment with the 23:20 form, while each shape changes cadence and closure.\",\"reason\":\"The 23:20 parallel supports the Sinai-place cluster, but the alternate endings and closures are variant apparatus rather than a replacement of the local form.\",\"representative_source_ids\":[\"QF-239bcd90\",\"QF-5f2ee70b\",\"QF-c51a8dec\",\"MI-941a1605\",\"QP-c5eddca9\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:2:mountain-with-stage-pressure","source_type":"word_analysis","support_id":"sup_b8a2e107c7b1a27a536a","text":"{\"blocking_evidence\":null,\"headline\":\"stage field remains secondary to the Mount\",\"reader_payoff\":\"The reader notices that the selected Mount sense can still resonate with ordered development through the same root field and the stages wording in 71:14.\",\"reason\":\"V4 preserves both the Mount branch and successive-stage branch, while the local construct with Sinai selects the Mount; the 71:14 echo can color the oath but cannot replace the local referent.\",\"representative_source_ids\":[\"QS-3c5d449e\",\"QS-73a9fc26\",\"QS-7a4319aa\",\"MS-e1a83c8c\",\"ME-15543832\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:3","source_type":"word_analysis","support_id":"sup_c884b0749a03c3199d49","text":"{\"gloss_range\":\"Sinai place-name as genitive complement to the Mount; variant and etymological pressures remain secondary to the local proper-name reading\",\"prose\":\"{{ar:سِينِينَ}} ({{tr:sīnīna}}) completes the construct phrase by identifying the mount: as genitive complement, it makes {{ar:طُورِ}} ({{tr:ṭūri}}) a specified Sinai expression rather than a loose mountain title. The genitive relation can be heard as locative or descriptive, but in either case the second word constrains the first. Its form is analytically charged: the local reading selects the proper place-name, while the {{ar:سِنِينَ}} ({{tr:sinīna}}) variant can reopen a years reading, and the {{ar:سَيْنَاءَ}} ({{tr:saynāʾa}}) form in 23:20 pulls the phrase toward the other Quranic Sinai construct. The same variant apparatus can add a rugged edge or serration image to the mountain profile, but only as coloring around the received place-name. The rare distribution of {{ar:س ي ن}} ({{tr:s-y-n}}) in this cluster makes the word feel like a constrained place-name marker, while Arabic radiance or beauty explanations and foreign-name provenance remain interpretive pressures rather than the selected sense. Its long vowels, sibilant opening, and repeated nasal sound bind the phrase together and echo the nasal cadence of the prior oath items in 95:1; variant endings can shift that flow toward diphthong or hamza-like closure while keeping the Sinai referent.\",\"root_display\":\"{{ar:س ي ن}} ({{tr:s-y-n}})\",\"root_gloss_range\":\"root range includes the Sinai/Sinin place-name cluster and separate letter or future-marker material; local construct selects the Sinai expression, with radiance, years, and variant-form pressures only as apparatus\",\"surface_display\":\"{{ar:سِينِينَ}} ({{tr:sīnīna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:1","source_type":"word_analysis","support_id":"sup_d2ac158b174927e4d0d6","text":"{\"gloss_range\":\"oath-and-coordination particle that carries the oath series forward and governs the following genitive phrase\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) does two jobs at once: it connects the phrase to the prior sworn items in 95:1 and, as oath-particle, governs the genitive object that follows. Because the oath answer is not inside 95:2 but comes in 95:4, the particle makes this short ayah visibly dependent on a larger qasam frame. Its attachment in {{ar:وَطُورِ}} ({{tr:wa-ṭūri}}) also compresses connector and oath-governor into the first written shape, so the reader meets continuation and oath force before the mountain noun stands on its own. Across the ayah boundary, the particle keeps the list cumulative and lets the sequence move from cultivated trees in 95:1 toward sacred geography in 95:2.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:2:acoustic-weight","source_type":"word_analysis","support_id":"sup_e6f94e9aca18222df343","text":"{\"blocking_evidence\":null,\"headline\":\"heavy sound matches the mountain image\",\"reader_payoff\":\"The reader notices that the emphatic opening and long vowel give the sworn mountain audible weight inside a very brief phrase.\",\"reason\":\"The phonetic observation is consistent with the local surface and reinforces the selected mountain image without changing the lexical sense.\",\"representative_source_ids\":[\"QP-74caed49\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:2:3:years-variant-pressure","source_type":"word_analysis","support_id":"sup_f7e75971e0a85f00f28f","text":"{\"blocking_evidence\":null,\"headline\":\"near form can shift place toward years\",\"reader_payoff\":\"The reader notices that a small vowel-length and ending pressure can move the phrase from Sinai geography toward a years or ages reading, even though the local construct selects place.\",\"reason\":\"The local QAC form is a Sinai complement, but the CRITICAL rows preserve variant-form pressure around the plural-like ending; that pressure is apparatus, not the governing parse.\",\"representative_source_ids\":[\"MG-c95c3b2c\",\"MG-e047002d\",\"QS-3448bf26\",\"QF-5418b5f7\",\"QF-b08433e8\",\"QE-b37d6225\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَطُورِ سِينِينَ","ayah_ref":"95:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000955/B005"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000955","role":"The mountain or named-Mount image supplies the concrete landmark and makes the proper-name reading primary.","root":"ط و ر","source_ref":"95:2","source_word_indices":["1"]}],"changed_reading":{"after":"A specific mountain is made present as a concrete oath-landmark.","before":"A bare opaque place-name is invoked."},"confidence":"strong","focus_anchor":"The noun طُورِ, specified by سِينِينَ and governed by the opening oath coordination, can denote a particular mountain.","mechanism":"The phrase first presents a concrete named height: a geographically locatable landmark is selected as the object of attention and oath.","model_id":"b_named_mount"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_named_mount","source_type":"hft","support_id":"sup_d65462b5e8ff61b51226","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَطُورِ سِينِينَ","ayah_ref":"95:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000955/B001","root_000955/B002","root_000955/B003"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000955","role":"The extended perimeter or frontage image turns the Mount into a continuous spatial edge.","root":"ط و ر","source_ref":"95:2","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000955","role":"The image of nearing a surrounding precinct gives that edge an approach-path and an inside/outside relation.","root":"ط و ر","source_ref":"95:2","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000955","role":"The reached or exceeded limit makes the approached edge a threshold rather than neutral scenery.","root":"ط و ر","source_ref":"95:2","source_word_indices":["1"]}],"changed_reading":{"after":"The Mount is also a perimeter, approach-zone, and limit that organizes passage.","before":"The Mount is visualized mainly as a central mass or summit."},"confidence":"medium","focus_anchor":"طُورِ can carry edge, approach-to-precinct, and limit images alongside its mountain reference.","mechanism":"The named mountain is spatially refigured as an extended frontage whose approach ends at a consequential boundary; attention shifts from the peak's center to the line and surrounding zone one nears.","model_id":"b_precinct_edge"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_precinct_edge","source_type":"hft","support_id":"sup_64ab3685906542b0f920","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَطُورِ سِينِينَ","ayah_ref":"95:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000955/B004","root_000955/B005"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000955","role":"The successive-stage image supplies temporal iteration and lets the place-name double as a phase marker.","root":"ط و ر","source_ref":"95:2","source_word_indices":["1"]},{"branch_id":"B005","mapped_root_id":"root_000955","role":"The concrete mountain image contains the temporal activation so that it remains a reading of this named place.","root":"ط و ر","source_ref":"95:2","source_word_indices":["1"]}],"changed_reading":{"after":"The fixed mountain also intimates succession through states or stages.","before":"The named mountain is a fixed object."},"confidence":"exploratory","focus_anchor":"The same root at طُورِ has an explicit branch of repeated turns, stages, and states.","mechanism":"A static landform can carry a latent temporal diagram: one phase gives way to another while the named Mount holds the phases together as a single sign.","model_id":"b_successive_states"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_successive_states","source_type":"hft","support_id":"sup_cbdfb0007f811a519a1d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَطُورِ سِينِينَ","ayah_ref":"95:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000955/B006","root_000955/B007"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_000955","role":"The wildness-beyond-domestic-limit image supplies remoteness from ordinary human familiarity.","root":"ط و ر","source_ref":"95:2","source_word_indices":["1"]},{"branch_id":"B007","mapped_root_id":"root_000955","role":"The narrow no-one-present image intensifies the remote margin into a potentially empty witness-space.","root":"ط و ر","source_ref":"95:2","source_word_indices":["1"]}],"changed_reading":{"after":"The Mount can also register as the wild, sparsely inhabited margin beyond domestic company.","before":"The Mount is presumed to be an inhabited or socially familiar sacred site."},"confidence":"exploratory","focus_anchor":"طُورِ has branches for what lies beyond familiar human company and, more narrowly, for a place with no one present.","mechanism":"The mountain's distance from domesticated company makes it a marginal zone: a place whose remoteness and possible emptiness expose rather than shelter the visitor.","model_id":"b_wild_empty_margin"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_wild_empty_margin","source_type":"hft","support_id":"sup_00c4dd648bee505a9f6d","trust":"legacy_unbound"}]}
</lane_packet_json>
