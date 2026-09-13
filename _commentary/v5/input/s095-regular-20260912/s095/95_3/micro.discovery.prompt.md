# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **95:3**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s095-regular-20260912/s095/95_3/micro.discovery.json` and modify nothing
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
  "ayah_ref": "95:3",
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
{"branch_registry":[{"boundary":"Bu dal inanma ya da dua cevabi degil; korkudan emin olma, guven verme ve guvenilir sayilma alanidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000054/B001","candidate_links":[{"candidate_id":"cand_a009d145d5602a724174","lane":"micro"},{"candidate_id":"cand_ca09ef648e87c4431f4a","lane":"micro"},{"candidate_id":"cand_873f8ce9b2f179b6ca98","lane":"micro"},{"candidate_id":"cand_51a36d083402239bd41e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَمِين","morph_features":"STEM|POS:ADJ|LEM:>amiyn|ROOT:Amn|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"95:3:3:2","qac_word_ref":"95:3:3","surface_ar":"أَمِينِ"}],"gloss":"guven ve guvenilirlik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel cekirdek korkuya karsi guven, ic yatiskinligi ve tehlikeden emin olma halidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Guven verme, birini kendi koruma ve teminat alani icine alma olarak kullanilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Guvenilirlik, ihanete karsi sadakat, emanet edilen sey ve kendisine guvenilen kisi anlamlarini dogurur."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Guvenin bulundugu yer, bir kimsenin emniyet icinde oldugu mesken veya siginak olarak adlandirilir."}},{"facet_id":"F005","role":"example","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Dayanikli ve aksamasindan korkulmayan deve kullanimi, guvenilirlik niteligini canli bir ornege uygular."}}],"root_ar":"ء م ن","root_id":"root_000054","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Korkunun kalkmasi, kalbin yatismasi, guven verme ve guvenilir sayilma alanlarini birlikte tasiyan en kisa genel karsiliktir.","boundary_detail":"Bu dal inanma ya da dua cevabi degil; korkudan emin olma, guven verme ve guvenilir sayilma alanidir.","branch_image_ar":"سكون القلب في أمن وثقة","concept_gloss":"guven ve guvenilirlik","contextual_glosses":[{"applicability":"Korkunun giderilmesi ve ic yatiskinligi onde oldugunda dogal karsiliktir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Emanet, guvenilirlik ve guven verme boyutlarini disarida birakir.","preserves":"Korku karsiti guven halini korur."},"facet_ids":["F001"],"text":"korkudan emin olma","usage_role":"contextual"},{"applicability":"Birinin baskasini koruma ve teminat altina almasi anlatildiginda kullanilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Guven icinde bulunma ve guvenilirlik adlandirmalarini kapsamaz.","preserves":"Bir baskasina guven saglama iliskisini korur."},"facet_ids":["F002"],"text":"guven verme","usage_role":"contextual"},{"applicability":"Kisi, emanet ya da dayanikli nesne guvenilirlik niteliginde anlatildiginda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Korkudan emin olma halini ve guven verme eylemini kapsamaz.","preserves":"Guvenilir sayilma ve emanet edilebilir olma tarafini korur."},"facet_ids":["F003","F005"],"text":"kendisine guvenilen","usage_role":"contextual"}],"definition":"Korkunun kalkmasiyla kalbin yatismasi, birine guven verilmesi veya bir kimsenin ya da seyin guvenilir kabul edilmesidir. Bu alan guvenli yer, emanet edilen sey, kendisine guvenilen kisi ve dayanilir binek gibi bagimli uygulamalari da kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel cekirdek korkuya karsi guven, ic yatiskinligi ve tehlikeden emin olma halidir."},{"facet_id":"F002","role":"extension","statement":"Guven verme, birini kendi koruma ve teminat alani icine alma olarak kullanilir."},{"facet_id":"F003","role":"extension","statement":"Guvenilirlik, ihanete karsi sadakat, emanet edilen sey ve kendisine guvenilen kisi anlamlarini dogurur."},{"facet_id":"F004","role":"associated_use","statement":"Guvenin bulundugu yer, bir kimsenin emniyet icinde oldugu mesken veya siginak olarak adlandirilir."},{"facet_id":"F005","role":"example","statement":"Dayanikli ve aksamasindan korkulmayan deve kullanimi, guvenilirlik niteligini canli bir ornege uygular."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Tasdik ve dinî kabul alanini ekler.","collision":"Ayni kokun ayri tasdik daliyla karisir.","fit":"displacement","loses":"Korkudan guvende olma, emanet ve guvenilirlik alanlarini kaybettirir.","preserves":"Kalpte yonelme ya da kabul unsurunu ancak cok dolayli korur."},"text":"inanma"}],"identity_rationale":"Kaynak ifadeleri bu dali yalniz korkunun kalkmasi olarak degil, kalbin yatismasi, guven verme, guvenilirlik, emanet edilen sey, guvenli yer ve dayanilir nitelik alanlariyla birlikte verir. Bu nedenle dalin cercevesi, guvenlik ve guvenilirlik ekseninde hem yalın hem de yapimli ve baglamli kullanislari ayirt ederek korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ihanetin karsiti olan guvenilirlik ve emanet edilen sey"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"korkunun kalkmasi ve ic yatiskinligi"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"guven, eminlik ve yatiskinlik hali"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"guven verme, guven hali veya guvenceye birakilan sey"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"guven icinde olmak ve korkusu kalkmak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birini guven icine almak ve ona guven saglamak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"guven icinde duruma gelmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kendisine guvenilen emin kisi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"emanet edilen veya kendisine guvenilen kisi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"guven icinde olan, emin"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"guvenilir veya emanet edilebilir olan"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"kendisine bir sey emanet edilen kisi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"guven icinde, tehlikeden uzak ve yatiskin"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"insanlarin zararindan korkmadigi guvenilir kimse"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"herkese guvenen ve duydugunu dogru sayan kisi"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kisinin en degerli ve icinin yatistigi mali"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"guvenli yer veya guven icindeki mesken"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"birinin guvencesi altina girmek"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"bir seyi birine emanet etmek ve onu guvenilir saymak"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"zayiflamasindan veya surcmesinden korkulmayan saglam deve"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kullarini veya dostlarini zulümden ve azaptan guvende kilan"}],"lexicalization_note":"Yalin guven ve korkusuzluk anlamlari ile belirli yapimli ya da soz obegi kullanislari birlikte vardir; tanim bunlari tek bir dar kaliba indirgemez.","neighbor_coverage_note":"Adaylar arasinda en yararli ayrimlar guven, ic yatiskinligi, koruma ve ayni kokteki tasdik daliyla ilgilidir; digerleri uzak tematik senaryolar oldugu icin yayina alinmadi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda yatiskinlik korkudan emin olma ve guvenilirlik sonucudur; komsu dalda yatiskinlik dogru sayma ve kabul etme iliskisine baglidir.","focus_only":"Guvenlik, korkunun kalkmasi, emanet ve guvenilirlik alanlarini kurar.","gloss":"guven ile tasdik ayrimi","neighbor_only":"Bir haberin, vaadin veya hakikatin dogru sayilmasi alanini kurar.","neighbor_ref":"root_000054/B002","relation_type":"near_neighbor","shared_zone":"Ikisinde de kalbin yatismasi ve guven hissi bulunabilir."},{"boundary_match":"partial","distinction":"Komsu dal ic yakinlik ve dayanma tarafinda yogunlasir; bu dal ise korkusuzluk, teminat ve guvenilirlik kurumunu da semantik cekirdege alir.","focus_only":"Korku karsiti guvenligi, guven vermeyi ve emanet iliskisini de kapsar.","gloss":"guven ile icten dayanma","neighbor_only":"Bir seye alisma, yakinlik duyma ve ona icten dayanma tarafini one cikarir.","neighbor_ref":"root_001568/B005","relation_type":"near_synonym","shared_zone":"Her iki dalda da kalbin bir seye karsi yatismasi ve guven duymasi vardir."},{"boundary_match":"partial","distinction":"Bu dal guvenin nesnel veya iliskisel teminatini anlatabilir; komsu dal ise rahat gonullu ve genis ic durumunu anlatir.","focus_only":"Emanet, guven verme ve guvenilir sayilma gibi iliskileri de tasir.","gloss":"eminlik ile ic genisligi","neighbor_only":"Nefis, aile veya kalp genisligi ve sakin mizac alaninda durur.","neighbor_ref":"root_000691/B006","relation_type":"near_neighbor","shared_zone":"Her ikisi kisinin ic dunyasinda guven ve rahatlik tasvir edebilir."},{"boundary_match":"field_only","distinction":"Komsu dal guvenin sebebi olabilecek koruyucu yapida durur; bu dal ise guvenin hali, verilmesi ve guvenilirlik vasfini adlandirir.","focus_only":"Guven hali, guven verme ve guvenilirlik adlandirmalaridir.","gloss":"guven ile koruyucu dayanak","neighbor_only":"Koruyan engel, dayanak veya cevreden gelen himaye unsurudur.","neighbor_ref":"root_000071/B002","relation_type":"same_field","shared_zone":"Guvenli olma durumu koruma fikriyle ayni senaryoda bulusabilir."}],"source_phrase_ar":"الأمن ضد الخوف (ayn;sihah)؛ أصل الأمن طمأنينة النفس وزوال الخوف (mufradat)؛ الأمانة ضد الخيانة ومعناها سكون القلب (maqayis)؛ الأمان إعطاء الأمنة (maqayis;ayn)؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن (tahdhib)؛ استأمن إليه دخل في أمانه (sihah)؛ مأمنه منزله الذي فيه أمنه (mufradat)؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها (ayn;sihah;mufradat)","source_summary":"Kaynaklar ortak olarak bu dali korkunun ziddi olan guven, kalbin yatismasi ve guven verme alaninda toplar. Ayni iddia guvenilir kisi, emanet, guvenli yer ve dayanilir binek gibi turemis ya da baglamli kullanislari da cekirdege baglar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الأمن ضد الخوف، والأمان وإعطاء الأمنة، والأمانة ضد الخيانة وما اؤتمن عليه، والآمن والمأمن والاستئمان، والأمين والمأمون وما يوثق به، ومنه وثاقة الناقة الأمون.","what_is_not_ar":"ليس تصديق الإيمان من حيث هو تصديق، ولا صيغة آمين في الدعاء، ولا أمن المركبة من أم ومن في قوله أمن هو قانت."},"support_links":["sup_30cbc122583b0600c80a","sup_5bb61778b3096b4acc24","sup_621cb79fb9717cb35bde","sup_6721a5fa2bc4fd926de8"]},{"boundary":"Bu dal guvenlik hali degil; bir soz, haber, vaat veya hakikati dogru kabul etme alanidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000054/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَمِين","morph_features":"STEM|POS:ADJ|LEM:>amiyn|ROOT:Amn|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"95:3:3:2","qac_word_ref":"95:3:3","surface_ar":"أَمِينِ"}],"gloss":"dogru sayip kabul etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel cekirdek bir haberin, sozun veya hakikatin dogru sayilmasidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hakka yonelik ic kabul, yalniz bilmekten ziyade boyun egme ve kabullenme bicimi alir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dini alanlarda bu kabul, bildirilen yola girme ve ona baglanma adi olarak kullanilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Ilahi sifat kullaniminda vaat edilen odulu dogrulama veya guvenceyle bildirme boyutu one cikar."}}],"root_ar":"ء م ن","root_id":"root_000054","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Haber, vaat, hakikat ve dini baglanma kullanimlarini tasdik cekirdegi etrafinda birlestirir.","boundary_detail":"Bu dal guvenlik hali degil; bir soz, haber, vaat veya hakikati dogru kabul etme alanidir.","branch_image_ar":"تصديق يطمئن إليه القلب","concept_gloss":"dogru sayip kabul etme","contextual_glosses":[{"applicability":"Haber veya sozun dogrulanmasi anlatildiginda en dogal karsiliktir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dini boyun egme ve davranisla baglanma tarafini tam tasimaz.","preserves":"Tasdik cekirdegini korur."},"facet_ids":["F001"],"text":"dogru kabul etmek","usage_role":"contextual"},{"applicability":"Dini ve icten kabullenme baglamlarinda tasdikten daha genis sureci aciklar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sade haber tasdiki icin fazla agir ve ozel kalir.","preserves":"Tasdikle birlikte ic kabul ve baglanma tarafini korur."},"facet_ids":["F002","F003"],"text":"hakka boyun egerek kabul etmek","usage_role":"explanatory"},{"applicability":"Vaat edilen seyin gercek ve guvenilir kilinmasi baglaminda kullanilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel tasdik ve dini kabullenme alanlarini kapsamaz.","preserves":"Vaatle ilgili dogrulama tarafini korur."},"facet_ids":["F004"],"text":"vaadini dogrulamak","usage_role":"contextual"}],"definition":"Bir haber, vaat veya hakikati dogru sayip ona icten kabul ile yonelmektir. Dini kullanista bu kabul, kalp, dil ve davranisla baglanan bir boyun egme ya da seriate girme anlami kazanabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel cekirdek bir haberin, sozun veya hakikatin dogru sayilmasidir."},{"facet_id":"F002","role":"specialization","statement":"Hakka yonelik ic kabul, yalniz bilmekten ziyade boyun egme ve kabullenme bicimi alir."},{"facet_id":"F003","role":"extension","statement":"Dini alanlarda bu kabul, bildirilen yola girme ve ona baglanma adi olarak kullanilir."},{"facet_id":"F004","role":"associated_use","statement":"Ilahi sifat kullaniminda vaat edilen odulu dogrulama veya guvenceyle bildirme boyutu one cikar."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Korkudan emin olma ve guvenli yer alanlarini ekler.","collision":"Ayni kokun guven daliyla karisir.","fit":"displacement","loses":"Tasdik, haberin dogru sayilmasi ve dini kabul cekirdegini kaybettirir.","preserves":"Kalbin yatismasiyla baglantili bir yan anlam kalabilir."},"text":"guvenlik"}],"identity_rationale":"Kaynak ifadeleri bu dali acikca tasdik, haber ya da vaadi dogru sayma ve bazi dini kullanislarda hakka boyun egme olarak verir. Provisional cerceve guvene dokunan yanini not eder, fakat dal kimligi korkusuzluk degil tasdik ve kabul iliskisidir.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"ozellikle haber veya hakikati dogru kabul etme"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"herkese guvenen ve duydugunu dogru sayan kisi"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"kuluna vaat ettigi odulu dogrulayan"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bizi dogru sayan veya bize inanan"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bildirilen dine girme ve onu kabul etme adi"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"hakka kalp, dil ve davranisla baglanarak dogru kabul etme"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"iyi amel anlaminda namaz veya ibadet"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"guven vermeyen batil seylere guven duymak diye yerilen tutum"}],"lexicalization_note":"Hem genel tasdik adlari hem de belirli soz obekleri ve dini kullanislar vardir; tanim bunlari yalin guven anlamina genisletmez.","neighbor_coverage_note":"Yayinlanan komsular tasdik, kesin kanaat, inkar ve guvenlik ayrimlarini netlestirir; kalan adaylar cevap, bildirme, yalan, aciklama veya uzak tematik baglar olarak daha az yararli bulundu.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Bu dal dogrulama ve kabullenme kutbunda, komsu dal ise hakikati reddetme veya ortme kutbundadir; bu nedenle ayni eksende karsit dururlar.","focus_only":"Haber, hakikat veya bildirilen yolu dogru sayip kabul eder.","gloss":"kabul ile inkar","neighbor_only":"Hakikati orter, inkar eder veya yalanlar.","neighbor_ref":"root_001307/B003","relation_type":"antonym","shared_zone":"Ikisi de hakikat, bildiri ve dogruluk karsisindaki tutumu adlandirir."},{"boundary_match":"partial","distinction":"Komsu dal kesinlik derecesini ve belirtiye dayali bilgiyi vurgular; bu dal ise kabul etme ve dogrulama eylemine odaklanir.","focus_only":"Bir haber veya hakikate kabul ve tasdikle yonelir.","gloss":"tasdik ile kesin kanaat","neighbor_only":"Belirtiye dayanarak kesin bilme veya kuvvetli kanaat alanindadir.","neighbor_ref":"root_000969/B001","relation_type":"near_neighbor","shared_zone":"Her ikisi de zihinsel kabul ve dogru sayma alanina yaklasir."},{"boundary_match":"partial","distinction":"Komsu dal kanaatin baglanmis ve sabit hale gelmesini anlatir; bu dal dogrulama ve kabul iliskisini esas alir.","focus_only":"Dogru sayma, haber ya da hakikati kabul etme eylemidir.","gloss":"tasdik ile yerlesik kanaat","neighbor_only":"Kalpte veya goruste karar kilma ve sabit kanaat olusturma alanidir.","neighbor_ref":"root_001034/B006","relation_type":"near_neighbor","shared_zone":"Ikisi de kalpte tutulan kabul veya gorusle ilgili olabilir."},{"boundary_match":"partial","distinction":"Bu dalda yatiskinlik dogru sayma ve kabullenmeden gelir; komsu dalda yatiskinlik korku ve tehlike ihtimalinin kalkmasindan gelir.","focus_only":"Tasdik, haberin veya hakikatin dogru kabul edilmesidir.","gloss":"tasdik ile guvenlik","neighbor_only":"Korkudan emin olma, guven verme ve emanet guvenilirligi alanidir.","neighbor_ref":"root_000054/B001","relation_type":"near_neighbor","shared_zone":"Kalbin yatismasi iki dalda da eslik edebilir."}],"source_phrase_ar":"الإيمان التصديق (ayn;sihah)؛ وما أنت بمؤمن لنا أي مصدق لنا (maqayis;ayn;mufradat)؛ إذعان النفس للحق على سبيل التصديق (mufradat)؛ المؤمن في صفات الله يصدق ما وعد عبده (maqayis)","source_summary":"Kaynaklar dalin ortak cekirdegini tasdik olarak verir ve bir sozun dogru sayilmasini temsil eden ornegi buna baglar. Ayni iddia, daha ozel dini kullanimlarda hakka icten boyun egme, yola girme ve vaatle ilgili dogrulama boyutlarinin eklendigini de gosterir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الإيمان بمعنى التصديق، وتصديق الخبر أو الوعد، والإيمان على سبيل الشريعة أو إذعان النفس للحق حيث نصت المصادر، واستعمال مؤمن بمعنى مصدق الوعد.","what_is_not_ar":"ليس مجرد الأمن ضد الخوف، ولا الأمانة ضد الخيانة، ولا قول آمين في الدعاء، إلا حيث يصرح المصدر بأن التصديق معه أمن."},"support_links":[]},{"boundary":"Bu dal guvenlik ya da tasdik degil; duada kabul talebini bildiren sabit sozdur.","branch_kind":"mixed_non_bare","branch_ref":"root_000054/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَمِين","morph_features":"STEM|POS:ADJ|LEM:>amiyn|ROOT:Amn|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"95:3:3:2","qac_word_ref":"95:3:3","surface_ar":"أَمِينِ"}],"gloss":"duada kabul istegi sozu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel cekirdek, duada kabul istegini bildiren sabit cevap sozudur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynaklar sozun anlamini 'kabul et', 'oyle olsun' veya 'bunu yap' seklinde aciklar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu sozu soyleme eylemi de ayni dal icinde adlandirilir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bazi aktarimlarda bu sozun ilahi bir ad oldugu yorumu da dalin yan rivayeti olarak bulunur."}}],"root_ar":"ء م ن","root_id":"root_000054","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dua sonunda soylenen sabit kabul talebi ve onu soyleme eylemi icin genel karsiliktir.","boundary_detail":"Bu dal guvenlik ya da tasdik degil; duada kabul talebini bildiren sabit sozdur.","branch_image_ar":"قول آمين طلبا للاستجابة","concept_gloss":"duada kabul istegi sozu","contextual_glosses":[{"applicability":"Sozun dua icindeki anlamini eylemli bicimde cevirmek gerektiginde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sabit soz ve onu soyleme eylemi olma tarafini eksiltir.","preserves":"Duanin kabul edilmesini isteme tarafini korur."},"facet_ids":["F001","F002"],"text":"kabul et","usage_role":"contextual"},{"applicability":"Duanin sonucuna katilma ve gerceklesmesini dileme baglaminda dogal karsiliktir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ilahi muhataba yonelen talep kuvvetini ve sozu soyleme eylemini tam tasimaz.","preserves":"Kabul ve gerceklesme istegini korur."},"facet_ids":["F001","F002"],"text":"oyle olsun","usage_role":"contextual"},{"applicability":"Eylem adi olan kullanimda, yani bu sozu telaffuz etme anlatildiginda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sozun tek basina anlamini ve ad yorumu yanini kapsamaz.","preserves":"Sozu soyleme eylemini ve dua baglamini korur."},"facet_ids":["F003"],"text":"duada kabul sozu soylemek","usage_role":"explanatory"}],"definition":"Dua sonunda kabul edilme istegini bildiren ve 'kabul et', 'oyle olsun' ya da 'bunu yap' anlaminda aciklanan sabit sozdur. Dal ayrica bu sozu soyleme eylemini ve kaynaklarda aktarılan ad yorumunu da kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel cekirdek, duada kabul istegini bildiren sabit cevap sozudur."},{"facet_id":"F002","role":"source_variant","statement":"Kaynaklar sozun anlamini 'kabul et', 'oyle olsun' veya 'bunu yap' seklinde aciklar."},{"facet_id":"F003","role":"associated_use","statement":"Bu sozu soyleme eylemi de ayni dal icinde adlandirilir."},{"facet_id":"F004","role":"source_variant","statement":"Bazi aktarimlarda bu sozun ilahi bir ad oldugu yorumu da dalin yan rivayeti olarak bulunur."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Korkudan emin olma ve guvenilirlik alanlarini ekler.","collision":"Ayni kokun guven daliyla karisir.","fit":"displacement","loses":"Dua formulu, kabul talebi ve sozu soyleme eylemini kaybettirir.","preserves":"Ayni kokle bicimsel bag disinda anlam cekirdegi korumaz."},"text":"guven"},{"category":"confusable","error_profile":{"adds":"Tasdik ve dini kabul alanlarini ekler.","collision":"Ayni kokun tasdik daliyla karisir.","fit":"displacement","loses":"Dua icindeki sabit cevap sozunu ve kabul dilegini kaybettirir.","preserves":"Kabul fikrine cok dolayli temas edebilir."},"text":"inanma"}],"identity_rationale":"Kaynak ifadeleri bu dali dua icinde soylenen bir kabul istegi sozu ve bu sozu soyleme eylemi olarak verir. Cerceve, guven ve tasdik dallarindan ayrildigi ve sadece dua cevabi formuluyle ilgili oldugu icin uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"duada 'kabul et' veya 'oyle olsun' anlamina gelen soz"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"ilahi ad oldugu aktarilan dua sozu"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"duada kabul istegi bildiren sozu soyleme"}],"lexicalization_note":"Dal belirli bir dua sozu ve onu soyleme eylemiyle sinirlidir; buradan genel guven ya da tasdik anlami cikarilmaz.","neighbor_coverage_note":"Yayinlanan ayrimlar dua, dua cevabi, yalvarma ve ayni kokteki iki ayri dali kapsar; kalan adaylar ibadet, kehanet araci veya uzak dua sozleri olarak daha az dogrudan sinir bilgisi verdi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Komsu dal dua edenin duskun ve isteyen halini anlatir; bu dal ise duaya eklenen kabul dilegi sozunu adlandirir.","focus_only":"Dua sonunda soylenen sabit kabul istegi sozudur.","gloss":"cevap sozu ile yalvarma","neighbor_only":"Yalvarma, ihtiyac gostermek ve alttan yakarma halidir.","neighbor_ref":"root_000908/B002","relation_type":"same_field","shared_zone":"Ikisi de dua ve talep sahnesinde yer alabilir."},{"boundary_match":"field_only","distinction":"Komsu dal belirli sosyal durumda birine iyi dilek yoneltir; bu dal ise yapilmis duanin kabul edilmesi icin soylenen formulu anlatir.","focus_only":"Duanin kabul edilmesini isteyen sabit sozdur.","gloss":"kabul sozu ile hayir duası","neighbor_only":"Aksirana iyi dilekte bulunma ve ona hayir duasidir.","neighbor_ref":"root_000816/B003","relation_type":"same_field","shared_zone":"Ikisi de kisa dua veya dua cevabi soylemleri alanindadir."},{"boundary_match":"partial","distinction":"Komsu dal birden cok soz islevine yayilir; bu dal tekil olarak dua kabul istegi formulune baglidir.","focus_only":"Dua icinde kabul istegini bildiren belirli sozdur.","gloss":"dua onayi sozleri","neighbor_only":"Dua onayi, pekistirme ve kinama gibi daha daginik soz islevlerini kapsar.","neighbor_ref":"root_000118/B006","relation_type":"near_neighbor","shared_zone":"Ikisi de kisa sozlerle dua, onay veya pekistirme islevi gorebilir."},{"boundary_match":"field_only","distinction":"Bu dal sabit dua sozunu ve onu soylemeyi anlatir; komsu dal korkunun kalkmasi ve guvenilirlik iliskilerini anlatir.","focus_only":"Dua cevabi olarak kabul istegi bildiren sozdur.","gloss":"dua sozu ile guven","neighbor_only":"Guven, korkusuzluk, emanet ve guvenilirlik alanidir.","neighbor_ref":"root_000054/B001","relation_type":"other","shared_zone":"Ayni kok ailesinde yer alsalar da normal anlam alanlari ayridir."},{"boundary_match":"field_only","distinction":"Bu dal bir soylem formuludur; komsu dal bir haberin veya hakikatin dogrulanmasi ve benimsenmesidir.","focus_only":"Dua sonunda kabul istegi bildiren sozdur.","gloss":"dua sozu ile tasdik","neighbor_only":"Haber, vaat veya hakikati dogru sayip kabul etmektir.","neighbor_ref":"root_000054/B002","relation_type":"other","shared_zone":"Kabul fikri cok genel duzeyde ikisine de temas edebilir."}],"source_phrase_ar":"قولنا في الدعاء آمين وتفسيره اللهم افعل (maqayis)؛ التأمين من قولك آمين (ayn)؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن (sihah)؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين (mufradat)","source_summary":"Kaynaklar ortak olarak dali dua icinde soylenen ve kabul istegi tasiyan sabit bir soz olarak anlatir. Ayni iddia, bu sozu soyleme eylemini ve sozun anlamina dair 'kabul et' ya da 'oyle olsun' aciklamalarini da icerir; ad yorumu ise bu ortak malzemenin yan aktarimidir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه آمين في الدعاء بالمد والقصر، والتأمين بمعنى قول آمين، وتفسيرها باستجب أو اللهم افعل أو كذلك فليكن، مع ذكر قول من جعلها اسما من أسماء الله.","what_is_not_ar":"ليس الأمن ضد الخوف، ولا الأمانة، ولا الإيمان بمعنى التصديق، ولا أمن التي هي أم من وليست من الباب."},"support_links":[]},{"boundary":"Dal, göğüs bölgesini, kaş arası açıklığı ve göksel durağı değil, yeryüzündeki sınırlı yeri ve buna bağlı özel adlandırmaları kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000148/B001","candidate_links":[{"candidate_id":"cand_a009d145d5602a724174","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:3:2:2","qac_word_ref":"95:3:2","surface_ar":"بَلَدِ"}],"gloss":"sınırları belirli yer; ayrıca mezarlık, mezar, toprak veya açık alan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, sınırları seçilebilen ve yerleşim durumu anlamı değiştirmeyen bir yeryüzü parçasıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Mezarlık, tek bir mezar ve toprak da bu adla anılabilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yerleşim dışındaki açık ve çıplak alan da özel bir kullanım olarak kapsama girer."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın genel yer çekirdeğini ve kaynaklarda ayrıca verilen özel yer adlandırmalarını birlikte temsil eder.","boundary_detail":"Dal, göğüs bölgesini, kaş arası açıklığı ve göksel durağı değil, yeryüzündeki sınırlı yeri ve buna bağlı özel adlandırmaları kapsar.","branch_image_ar":"الموضع المحدود من الأرض","concept_gloss":"sınırları belirli yer; ayrıca mezarlık, mezar, toprak veya açık alan","contextual_glosses":[{"applicability":"Yerleşim durumundan bağımsız olarak genel coğrafi çekirdeğin anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Mezarlık, mezar, toprak ve açık alan için verilen özel kullanımları dışarıda bırakır.","preserves":"Sınırlı yeryüzü parçası olan temel anlamı korur."},"facet_ids":["F001"],"text":"sınırları belirli yeryüzü parçası","usage_role":"general"},{"applicability":"Sözcüğün yerleşim dışındaki geniş ve açık bir alanı gösterdiği özel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel sınırlı yer anlamını ve mezarlık, mezar ile toprak kullanımlarını vermez.","preserves":"Açık alan için verilen özel kullanımı korur."},"facet_ids":["F003"],"text":"açık, çıplak alan","usage_role":"contextual"}],"definition":"Bayındır veya bayındır olmayan, boş veya yerleşilmiş olabilen, sınırları belirli bir yeryüzü parçasıdır. Aynı ad mezarlık, mezar, toprak veya açık alan için de özel olarak kullanılabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, sınırları seçilebilen ve yerleşim durumu anlamı değiştirmeyen bir yeryüzü parçasıdır."},{"facet_id":"F002","role":"extension","statement":"Mezarlık, tek bir mezar ve toprak da bu adla anılabilir."},{"facet_id":"F003","role":"extension","statement":"Yerleşim dışındaki açık ve çıplak alan da özel bir kullanım olarak kapsama girer."}],"identity_rationale":"Kaynak ifade, yerleşilmiş olup olmamasına bakılmaksızın sınırları belirli bir yeryüzü parçasını çekirdek anlam olarak verir; mezarlık, mezar, toprak ve açık alan kullanımlarını da ayrıca bildirir. Bu nedenle dal korunabilir, ancak ikincil adlandırmalar genel yer anlamıyla özdeşleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yerleşilmiş ya da boş, sınırları belirli yer"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yerler, yöreler"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"mezarlık, mezar veya toprak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"açık, çıplak alan"}],"lexicalization_note":"Temel biçimler sınırlı yeryüzü parçasını gösterir; mezarlık, mezar, toprak ve açık alan anlamları ayrı sözlüksel kullanımlardır ve çekirdeğin bütün kapsamına genellenmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel yeryüzü ile işlenmemiş arazi adayları sınırı en iyi aydınlattığı için seçildi, öteki adaylar yalnızca belirli arazi türleri ya da aynı kökün ayrı anlamlarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak, sınırları belirli bir yer birimini adlandırır; komşu ise bütün yeryüzünü veya göğe göre aşağı konumu anlatır.","focus_only":"Odak dalı, çevresi belirlenmiş bir yeri ve mezar ya da açık alan gibi özel adlandırmaları içerir.","gloss":"yeryüzü ve aşağı taraf","neighbor_only":"Komşu dal, göğün karşısındaki bütün yeryüzünü ve genel olarak aşağıda olanı kapsar.","neighbor_ref":"root_000025/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da yeryüzündeki alanlardan söz edebilir."},{"boundary_match":"partial","distinction":"Komşunun bayındır veya yerleşilmiş olmama koşulu zorunludur; odakta böyle bir koşul yoktur.","focus_only":"Odak yerleşilmiş veya boş her türlü sınırlı yeri kapsar.","gloss":"bayındır veya yerleşilmiş olmayan arazi","neighbor_only":"Komşu yalnızca bayındır veya yerleşilmiş olmayan araziyi belirtir.","neighbor_ref":"root_001535/B011","relation_type":"near_synonym","shared_zone":"Bayındır veya yerleşilmiş olmayan bir arazi iki dalın da kapsamına girebilir."}],"source_phrase_ar":"البلد معروف والبلدة أيضا والبلاد جمع بلد (jamhara)؛ البلد كل موضع مستحيز من الأرض عامر أو غير عامر أو خال أو مسكون (tahdhib)؛ البلد المكان المحيط المحدود المتأثر باجتماع قطانه وإقامتهم فيه (mufradat)؛ البلد المقبرة ويقال هو نفس القبر وربما جاء البلد يعني به التراب (tahdhib)؛ من البلد وهو الفضاء البراز (maqayis)","source_summary":"Kaynaklar sınırlı yeryüzü parçası anlamında birleşir ve bu parçanın bayındır veya bayındır olmayan, boş veya yerleşilmiş olabileceğini gösterir. Toprak, mezarlık, mezar ve açık alan kullanımları çekirdeğe bağlı özel genişlemelerdir.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه البلد والبلدة والبلاد والبلدان، وكل موضع من الأرض عامر أو غير عامر أو خال أو مسكون، والمفازة، والمقبرة والقبر، والتراب، والفضاء البراز.","what_is_not_ar":"ليس فيه الصدر ولا البلجة ولا منزلة القمر إلا من جهة التشبيه أو التسمية الخاصة."},"support_links":["sup_621cb79fb9717cb35bde"]},{"boundary":"Dal genel bir yer adını değil, göğüs ve boğaz altı bölgesini; eylem kalıbında ise devenin bu bölgeyi yere koymasını kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000148/B002","candidate_links":[{"candidate_id":"cand_873f8ce9b2f179b6ca98","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:3:2:2","qac_word_ref":"95:3:2","surface_ar":"بَلَدِ"}],"gloss":"göğüs ve boğaz altındaki göğüs çukuru; devede göğsü yere koyma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, göğüs ile boğaz altındaki orta çukur ve çevresidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ad, insan göğsüne ve hayvanın göğüs altındaki etli bölümüne uygulanabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Devenin çökerken göğsünü yere koyması belirli bir söz kalıbıyla ifade edilir."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Beden bölgesini ve yalnızca ilgili eylem kalıbında görülen deve hareketini birlikte kapsar.","boundary_detail":"Dal genel bir yer adını değil, göğüs ve boğaz altı bölgesini; eylem kalıbında ise devenin bu bölgeyi yere koymasını kapsar.","branch_image_ar":"الصدر وبلدة النحر","concept_gloss":"göğüs ve boğaz altındaki göğüs çukuru; devede göğsü yere koyma","contextual_glosses":[{"applicability":"Beden bölgesinin dar ve anatomik olarak belirli merkezi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Göğsün daha geniş kullanımını ve devenin çöküş eylemini dışarıda bırakır.","preserves":"Boğaz altındaki orta göğüs bölgesini korur."},"facet_ids":["F001"],"text":"boğazın altındaki göğüs çukuru","usage_role":"contextual"}],"definition":"Göğsün, özellikle boğazın altındaki çukurun ve çevresinin bulunduğu ön beden bölgesidir. Devenin çöküşünde bu bölgeyi yere koyması ayrıca kalıplaşmış bir eylem olarak anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, göğüs ile boğaz altındaki orta çukur ve çevresidir."},{"facet_id":"F002","role":"extension","statement":"Ad, insan göğsüne ve hayvanın göğüs altındaki etli bölümüne uygulanabilir."},{"facet_id":"F003","role":"associated_use","statement":"Devenin çökerken göğsünü yere koyması belirli bir söz kalıbıyla ifade edilir."}],"identity_rationale":"Kaynak ifade, göğsü ve özellikle boğaz altındaki göğüs çukurunu temel beden bölgesi olarak verir; insan göğsüne aktarımı, hayvanın göğüs altı bölgesini ve devenin çökerken göğsünü yere koymasını da açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"boğazın altındaki göğüs çukuru ve çevresi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"göğüs"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"deve çökerken göğsünü yere koydu"}],"lexicalization_note":"Bağımsız biçim göğsü gösterebilir; boğaz altı merkezi ve devenin göğsünü yere koyması yalnız kendi kalıplarında okunmalı, bütün dala genellenmemelidir.","neighbor_coverage_note":"Bütün beden bölgesi ve kök içi adaylar değerlendirildi; boğaz önü ile genel göğüs adayları en yakın sınır karşılaştırmalarını sağladı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak göğüs çukuru merkezli ve belirli bir deve eylemine bağlıdır; komşu boğaz önü ve kesim yeri merkezlidir.","focus_only":"Odak, bütün göğse aktarılabilir ve devenin çökerken göğsünü yere koyması kullanımını içerir.","gloss":"boğaz önü ve üst göğüs","neighbor_only":"Komşu, boğaz önü ile üst göğsü, kesim yerini ve kolye bölgesini daha geniş ayrıntıyla kapsar.","neighbor_ref":"root_001479/B001","relation_type":"near_synonym","shared_zone":"İki dal boğazın altındaki üst göğüs bölgesinde örtüşür."},{"boundary_match":"partial","distinction":"Komşu genel göğüs adıdır; odak göğsün belirli merkezini ve ona bağlı kullanımları öne çıkarır.","focus_only":"Odak boğaz altındaki çukuru ve devenin çökme kalıbını ayrıca belirtir.","gloss":"göğüs","neighbor_only":"Komşu göğsü ayrıntılandırmadan genel bir beden bölgesi olarak adlandırır.","neighbor_ref":"root_001315/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da göğüs bölgesini adlandırabilir."}],"source_phrase_ar":"بلدة النحر وسطه (jamhara)؛ البلدة الصدر وفلان واسع البلدة أي واسع الصدر (sihah)؛ البلدة بلدة النحر وهي الثغرة وما حولها (tahdhib)؛ سميت الكركرة بلدة لذلك وربما استعير ذلك لصدر الإنسان (mufradat)؛ الأصل الصدر ويقال وضعت الناقة بلدتها بالأرض إذا بركت (maqayis)","source_summary":"Kaynaklar göğüs ile boğaz altındaki orta çukur çevresini aynı beden bölgesi altında toplar. İnsan göğsüne aktarım ve devenin çökerken göğsünü yere koyması, bu çekirdeğe bağlı fakat ayrı kapsamlı kullanımlardır.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الصدر، وبلدة النحر والثغرة وما حولها، والكركرة، ووضع الناقة صدرها على الأرض في البروك.","what_is_not_ar":"ليس فيه الموضع الأرضي العام ولا البلجة بين الحاجبين إلا إذا نص المصدر على التشبيه."},"support_links":["sup_5bb61778b3096b4acc24"]},{"boundary":"Dal, alın bütünü veya kaşın kendisi değil, iki kaş arasındaki açık bölge ve bu açıklığa sahip kişiyle sınırlıdır.","branch_kind":"bare","branch_ref":"root_000148/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:3:2:2","qac_word_ref":"95:3:2","surface_ar":"بَلَدِ"}],"gloss":"kaşların arasındaki açıklık ve kaşları birleşmemiş olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki kaş arasındaki temiz ve açık bölge çekirdeği oluşturur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaşları birbirine birleşmemiş kişi bu görünüş üzerinden nitelenir."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem yüz bölgesini hem de bu bölgenin görünüşüyle nitelenen kişiyi kapsar.","boundary_detail":"Dal, alın bütünü veya kaşın kendisi değil, iki kaş arasındaki açık bölge ve bu açıklığa sahip kişiyle sınırlıdır.","branch_image_ar":"البلجة بين الحاجبين","concept_gloss":"kaşların arasındaki açıklık ve kaşları birleşmemiş olma","contextual_glosses":[{"applicability":"Doğrudan yüz bölgesinin kendisi anlatıldığında kullanılan kısa karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kaşları birleşmemiş kişiye yönelik nitelemeyi dışarıda bırakır.","preserves":"İki kaş arasındaki açık bölgeyi korur."},"facet_ids":["F001"],"text":"kaş arası açıklık","usage_role":"general"}],"definition":"İki kaşın arasında kalan temiz, açık ve kılsız görünümlü bölgedir; bu açıklığa sahip, yani kaşları birleşmemiş kişi de aynı anlam alanında nitelenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki kaş arasındaki temiz ve açık bölge çekirdeği oluşturur."},{"facet_id":"F002","role":"extension","statement":"Kaşları birbirine birleşmemiş kişi bu görünüş üzerinden nitelenir."}],"identity_rationale":"Kaynak ifade, kaşların arasındaki temiz ve açık bölgeyi ve kaşları birleşmemiş kişiyi tutarlı biçimde aynı görünüş altında tanımlar. Beden iriliği ve zihinsel yavaşlık yalnızca benzer biçimli başka anlamlardır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kaşların arasındaki açık ve temiz bölge"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kaşları birleşmemiş"}],"lexicalization_note":"Tanım, çıplak biçimin kaşlar arasındaki açıklık anlamıyla sınırlıdır; aynı biçimin beden iriliği ya da zihinsel yavaşlık anlamları içeri alınmaz.","neighbor_coverage_note":"Bütün yüz ve görünüş adayları değerlendirildi; alın ve kaş, odak bölgesinin iki doğrudan anatomik sınırını gösterdiği için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak iki kaş arasındaki boşluğa, komşu ise kaşların üstündeki daha geniş alın bölgesine yönelir.","focus_only":"Odak kaşların arasındaki açıklığı ve kaşların birleşmemiş olmasını belirtir.","gloss":"alın","neighbor_only":"Komşu alın bölgesini ve alın kemiğini daha geniş olarak kapsar.","neighbor_ref":"root_000219/B001","relation_type":"near_neighbor","shared_zone":"İki dal yüzün kaşların çevresindeki ön bölümüne ilişkindir."},{"boundary_match":"field_only","distinction":"Biri kaşların arasındaki boşluğu, öteki kaş yapısının kendisini gösterir.","focus_only":"Odak, iki kaşın arasında kalan açıklığı adlandırır.","gloss":"kaş","neighbor_only":"Komşu, gözün üstündeki kıl, et ve kemikten oluşan kaşın kendisini adlandırır.","neighbor_ref":"root_000294/B005","relation_type":"near_neighbor","shared_zone":"İki dal aynı yüz bölgesinde yan yana bulunan yapılara ilişkindir."}],"source_phrase_ar":"ربما سميت البلجة بلدة (jamhara)؛ البلدة والبلدة نقاوة ما بين الحاجبين ورجل أبلد أي أبلج بين البلد (sihah)؛ الأبلد من الرجال الذي ليس بمقرون وهي البلدة والبلدة (tahdhib)؛ البلدة البلجة ما بين الحاجبين تشبيها بالبلد لتمددها (mufradat)؛ الأبلد الذي ليس بمقرون الحاجبين يقال لما بين حاجبيه بلدة (maqayis)","source_summary":"Kaynaklar iki kaş arasındaki açıklıkta ve bu açıklığın kaşları birleşmemiş kişiyi nitelemesinde birleşir. Benzetme açıklığın yayılmış görünüşüne dayanır.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه البلجة أو النقاوة بين الحاجبين، والرجل الأبلد الذي ليس بمقرون الحاجبين.","what_is_not_ar":"ليس فيه عظم الخلق ولا بلادة الذهن، وإن اشترك معها لفظ أبلد."},"support_links":[]},{"boundary":"Dal yeryüzündeki yer anlamından ayrıdır; Ay durağına verilen adın farklı göksel tasvirlerini birlikte, fakat kaynak değişkeleri olarak kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000148/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:3:2:2","qac_word_ref":"95:3:2","surface_ar":"بَلَدِ"}],"gloss":"yıldız kümesi ya da yıldızsız alan diye tasvir edilen Ay durağı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, Ay'ın konaklarından biri sayılan belirli bir gök bölgesidir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir tasvir bu durağı bir göksel yay içinde yer alan altı yıldız olarak açıklar."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başka bir tasvir onu iki belirli göksel işaret arasındaki yıldızsız alan olarak açıklar."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Göksel aslanın göğsü de bu adla anılan özel bir gök konumudur."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ortak göksel durak çekirdeğini ve birbirinden farklı iki fiziksel tasviri birlikte gösterir.","boundary_detail":"Dal yeryüzündeki yer anlamından ayrıdır; Ay durağına verilen adın farklı göksel tasvirlerini birlikte, fakat kaynak değişkeleri olarak kapsar.","branch_image_ar":"منزلة القمر والموضع السماوي الخالي","concept_gloss":"yıldız kümesi ya da yıldızsız alan diye tasvir edilen Ay durağı","contextual_glosses":[{"applicability":"Durağın yıldız düzeni hakkında hüküm vermeden yalnız ortak göksel işlevi anlatır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Altı yıldız, yıldızsız alan ve göksel aslanın göğsü tasvirlerini belirtmez.","preserves":"Ay durağı olan ortak çekirdeği korur."},"facet_ids":["F001"],"text":"Ay'ın belirli bir durağı","usage_role":"general"}],"definition":"Ay'ın konaklarından biri olarak adlandırılan bir gök bölgesidir; kaynaklarda altı yıldızlık bir küme veya iki belirli göksel işaret arasındaki yıldızsız alan olarak farklı biçimlerde tasvir edilir. Göksel aslanın göğsü için kullanılan ad da bu dala bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, Ay'ın konaklarından biri sayılan belirli bir gök bölgesidir."},{"facet_id":"F002","role":"source_variant","statement":"Bir tasvir bu durağı bir göksel yay içinde yer alan altı yıldız olarak açıklar."},{"facet_id":"F003","role":"source_variant","statement":"Başka bir tasvir onu iki belirli göksel işaret arasındaki yıldızsız alan olarak açıklar."},{"facet_id":"F004","role":"extension","statement":"Göksel aslanın göğsü de bu adla anılan özel bir gök konumudur."}],"identity_rationale":"Kaynak ifade dalı bir Ay durağı olarak destekler, fakat fiziksel tasvirler tam olarak birleşmez: bir anlatım onu altı yıldızlık bir küme, bir başkası iki göksel işaret arasındaki yıldızsız alan, bir diğeri göksel aslanın göğsü olarak verir. Dal korunabilir, ancak bu tasvirler tek bir değişmez gök biçimiymiş gibi birleştirilemez.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"Ay durağı veya yıldızsız gök bölgesi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"göksel aslanın göğüs bölgesi"}],"lexicalization_note":"Temel biçim Ay durağını veya yıldızsız gök alanını gösterir; göksel aslanın göğsü olan özel adlandırma yalnız kendi sözlüksel biriminde tutulur.","neighbor_coverage_note":"Bütün göksel adaylar karşılaştırıldı; başka bir Ay durağı ile daha geniş göksel bölümleme, durağın kimliği ve sınıf sınırını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Aynı tür göksel birimler olsalar da gökte farklı konumları ve farklı özel adları gösterirler.","focus_only":"Odak farklı kaynaklarda yıldız kümesi veya yıldızsız alan olarak tasvir edilen ayrı bir Ay durağıdır.","gloss":"başka bir Ay durağı","neighbor_only":"Komşu, başka iki göksel işaretin yanında konumlandırılan farklı bir Ay durağının özel adıdır.","neighbor_ref":"root_000925/B004","relation_type":"same_field","shared_zone":"Her ikisi de Ay'ın konaklarından birini adlandırır."},{"boundary_match":"field_only","distinction":"Odak Ay'ın hareket dizisindeki tek bir duraktır; komşu daha geniş bir göksel bölümleme sistemini anlatır.","focus_only":"Odak belirli bir Ay durağını ve onun değişken fiziksel tasvirlerini gösterir.","gloss":"göksel bölümler","neighbor_only":"Komşu göğün on iki geniş bölümünü, yıldız kümelerini veya göksel yapıları kapsar.","neighbor_ref":"root_000101/B002","relation_type":"same_field","shared_zone":"İki dal da göğün adlandırılmış bölümleriyle ilgilidir."}],"source_phrase_ar":"البلدة منزل من منازل القمر (jamhara)؛ البلدة من منازل القمر وهي ستة أنجم من القوس (sihah)؛ البلدة في السماء موضع لا نجوم فيه بين النعائم وسعد الذابح (tahdhib)؛ البلدة منزل من منازل القمر (mufradat)؛ البلدة النجم يقولون هو بلدة الأسد أي صدره (maqayis)","source_summary":"Ortak çekirdek bir Ay durağına verilen addır. Toplu kanıt, durağın altı yıldızlık bir küme ile yıldızsız bir gök alanı arasında değişen tasvirlerini ve göksel aslanın göğsü adlandırmasını birlikte aktarır; bu tasvirler tek bir fiziksel tanıma indirgenemez.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه البلدة منزلة من منازل القمر، والموضع الخالي في السماء بين النعائم وسعد الذابح، وبلدة الأسد إذا أريد صدره السماوي.","what_is_not_ar":"ليس فيه الأرض والبلد المسكون إلا من جهة الاسم المشترك أو التشبيه."},"support_links":[]},{"boundary":"Dal kalıcı zeka düşüklüğünü değil, şaşkınlıktan doğan duraksamayı; ayrı kullanımda ise metaneti yitirip boyun eğmeyi anlatır.","branch_kind":"bare","branch_ref":"root_000148/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:3:2:2","qac_word_ref":"95:3:2","surface_ar":"بَلَدِ"}],"gloss":"şaşkınlıkla duraksama; metaneti yitirip boyun eğme","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi şaşkınlık yüzünden kararsız kalır, duraksar ve ilerleyemez."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Şaşkın kişi elini göğsünün üstüne koyabilir; bu hareket durumun kendisi değil, ona eşlik eden belirtidir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Metaneti korumanın karşıtı olarak sinme, teslim olma ve boyun eğme de aynı biçimle anlatılır."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem kararsız şaşkınlık çekirdeğini hem de ayrı teslimiyet değişkesini kapsar.","boundary_detail":"Dal kalıcı zeka düşüklüğünü değil, şaşkınlıktan doğan duraksamayı; ayrı kullanımda ise metaneti yitirip boyun eğmeyi anlatır.","branch_image_ar":"الحيرة والتبلد","concept_gloss":"şaşkınlıkla duraksama; metaneti yitirip boyun eğme","contextual_glosses":[{"applicability":"Bir iş karşısında kararsızca duraksama ve yönünü bulamama öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eli göğse koyma belirtisini ve metaneti yitirip boyun eğme değişkesini dışarıda bırakır.","preserves":"Şaşkınlık ve kararsız duraksama çekirdeğini korur."},"facet_ids":["F001"],"text":"şaşkınlıktan ne yapacağını bilememek","usage_role":"general"},{"applicability":"Metaneti korumanın karşıtı olan teslimiyet ve sinme anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Şaşkınlıkla kararsız duraksamayı ve ona eşlik eden göğüs hareketini vermez.","preserves":"Sinme ve boyun eğme değişkesini korur."},"facet_ids":["F003"],"text":"sinip boyun eğmek","usage_role":"contextual"}],"definition":"Bir iş karşısında şaşkınlığa düşüp kararsızca duraksamak ve ne yapacağını bilememektir; bu durumda eli göğse koyma hareketi eşlik edebilir. Ayrı bir kullanımda metaneti yitirerek sinmek ve boyun eğmek anlamına gelir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi şaşkınlık yüzünden kararsız kalır, duraksar ve ilerleyemez."},{"facet_id":"F002","role":"associated_use","statement":"Şaşkın kişi elini göğsünün üstüne koyabilir; bu hareket durumun kendisi değil, ona eşlik eden belirtidir."},{"facet_id":"F003","role":"source_variant","statement":"Metaneti korumanın karşıtı olarak sinme, teslim olma ve boyun eğme de aynı biçimle anlatılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kaynak çekirdeğinde bulunmayan kalıcı zihinsel yetersizlik yargısını ekler.","collision":"Zihinsel yavaşlık dalıyla karışır.","fit":"displacement","loses":"Geçici şaşkınlığı, kararsız duraksamayı, göğüs hareketini ve boyun eğme değişkesini kaybeder.","preserves":"İlerleyememe görünüşünü çok genel biçimde çağrıştırır."},"text":"aptallık"}],"identity_rationale":"Kaynak ifade şaşkınlık içinde duraksama ve ne yapacağını bilememe çekirdeğini, buna eşlik eden eli göğse koyma hareketini ve metanetin karşıtı olan boyun eğmeyi destekler. Provisional çerçevedeki yoğun üzüntü koşulu kaynak ifadesinde kurulmadığı için tanımdan çıkarılmalı, boyun eğme ise ayrı bir anlam değişkesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"şaşkınlığa düşüp kararsızca duraksamak"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"bir işte şaşırıp ne yapacağını bilememek"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"metaneti yitirip sinme ve boyun eğme"}],"lexicalization_note":"Tanım çıplak biçimlerin şaşkınlık, duraksama ve boyun eğme kullanımlarını kapsar; zihinsel yetersizlik anlamı bu dala aktarılmaz.","neighbor_coverage_note":"Bütün şaşkınlık, üzüntü ve belirsizlik adayları değerlendirildi; yön bulamayan bocalama ile ani afallama en yakın iki karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak şaşkın duraksama ve teslimiyet görünüşüne, komşu ise yön ve doğru yol bulamama koşuluna ağırlık verir.","focus_only":"Odak eli göğse koyma belirtisini ve metaneti yitirip boyun eğme değişkesini içerir.","gloss":"yönünü bulamadan bocalama","neighbor_only":"Komşu şaşkınlığın yanı sıra yol, görüş veya yön bulamama ve sapkınlıkta bocalama kapsamına uzanır.","neighbor_ref":"root_001048/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir işte ne yapacağını bilemeyip kararsızca bocalamayı kapsar."},{"boundary_match":"partial","distinction":"Komşuda ani şaşkınlık ve korku daha geniştir; odakta kararsızca duraksama belirleyicidir.","focus_only":"Odak kararsız duraksamayı, göğüs hareketini ve boyun eğme değişkesini belirtir.","gloss":"afallama ve şaşkınlık","neighbor_only":"Komşu korku, ani afallama ve şaşkın kişinin başka olumsuz nitelendirmelerini de kapsar.","neighbor_ref":"root_000086/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin şaşkın ve afallamış duruma düşmesini anlatabilir."}],"source_phrase_ar":"تبلد الرجل من هذا إذا لحقته حيرة فضرب بيده على بلدة نحره (jamhara)؛ تبلد أي تردد متحيرا (sihah)؛ المتبلد الذي يتردد متحيرا (tahdhib)؛ التبلد نقيض التجلد وهو استكانة وخضوع (tahdhib)؛ قيل للمتحير بلد في أمره وأبلد وتبلد (mufradat)؛ تبلد الرجل إذا وضع يده على صدره عند تحيره في الأمر (maqayis)","source_summary":"Toplu kanıt şaşkınlıkla kararsızca duraksamayı ortak merkez yapar ve eli göğse koymayı buna eşlik eden hareket olarak verir. Metanetin karşıtı olan sinme ve boyun eğme, yoğun üzüntü koşulu gerektirmeyen ayrı bir kullanım değişkesidir.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه تبلد وبلد وأبلد إذا تردد متحيرا، ووضع يده على صدره عند الحيرة، والاستكانة والخضوع عند غلبة الحزن.","what_is_not_ar":"ليس هو البلادة بمعنى ضد الذكاء إلا حيث يصرح المصدر بانتقال المعنى إليها."},"support_links":[]},{"boundary":"Dal izin kendisini kapsar; yara, deri hastalığı, ben veya tanıtma amacıyla yapılan işaret gibi belirli nedenler zorunlu değildir.","branch_kind":"bare","branch_ref":"root_000148/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:3:2:2","qac_word_ref":"95:3:2","surface_ar":"بَلَدِ"}],"gloss":"bedende, deride veya başka bir yüzeyde kalan iz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir beden veya yüzey üzerinde seçilebilen kalıcı ya da belirgin iz çekirdeği oluşturur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Anlam yalnız deriye değil, bedenin başka bölümlerine ve başka yüzeylere de uzanabilir."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nedeni belirtilmemiş genel iz anlamını ve beden dışına uzanan kapsamı birlikte verir.","boundary_detail":"Dal izin kendisini kapsar; yara, deri hastalığı, ben veya tanıtma amacıyla yapılan işaret gibi belirli nedenler zorunlu değildir.","branch_image_ar":"الأثر في الجلد والبدن","concept_gloss":"bedende, deride veya başka bir yüzeyde kalan iz","contextual_glosses":[{"applicability":"İzin özellikle insan ya da hayvan derisinde bulunduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bedenin başka bölümlerindeki ve beden dışındaki yüzeylerdeki izleri dışarıda bırakır.","preserves":"Deride görülen iz çekirdeğini korur."},"facet_ids":["F001"],"text":"deride kalan iz","usage_role":"contextual"}],"definition":"Bedende, deride veya başka bir yüzeyde kalmış görünür izdir; tekil ya da çoğul olarak, izin nedenini zorunlu biçimde belirtmeden kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir beden veya yüzey üzerinde seçilebilen kalıcı ya da belirgin iz çekirdeği oluşturur."},{"facet_id":"F002","role":"extension","statement":"Anlam yalnız deriye değil, bedenin başka bölümlerine ve başka yüzeylere de uzanabilir."}],"identity_rationale":"Kaynak ifade, bedende, deride veya başka bir yüzeyde bulunan izi doğrudan ve tutarlı biçimde verir; çoğul biçimi de aynı izi topluca gösterir. İzin yaradan, hastalıktan veya bilinçli işaretlemeden doğması çekirdek tanımın zorunlu koşulu değildir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"bedende veya başka bir yüzeyde kalan iz; izler"}],"lexicalization_note":"Çıplak dal genel iz anlamıyla sınırlıdır; izin belirli bir yara, hastalık ya da işaretleme türünden doğduğu varsayılmaz.","neighbor_coverage_note":"Bütün iz, yara, ben ve işaretleme adayları değerlendirildi; genel kalıntı ile amaçlı tanıtma işareti, neden ve işlev sınırını en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak izin oluşumunu belirtmez; komşu önceki bir olaydan ya da yaradan geriye kalma ilişkisini daha açık taşır.","focus_only":"Odak bedende veya başka bir yüzeyde nedeni belirtilmemiş genel izi kapsar.","gloss":"geride kalan belirti","neighbor_only":"Komşu bir şeyden geriye kalan belirtiyi ve özellikle iyileşmiş yaranın deride bıraktığı kalıntıyı öne çıkarır.","neighbor_ref":"root_000287/B001","relation_type":"near_synonym","shared_zone":"İki dal da deride veya başka bir nesnede kalan görünür izi anlatabilir."},{"boundary_match":"partial","distinction":"Odakta amaç ve yapılış biçimi belirsizdir; komşuda bilinçli işaretleme ve tanıtma işlevi kurucudur.","focus_only":"Odak kendiliğinden ya da herhangi bir nedenle oluşmuş genel izi kapsar.","gloss":"tanıtıcı işaret","neighbor_only":"Komşu tanıtma veya ayırt etme amacıyla bilerek yapılan damga, yakı ya da kesik işaretini gerektirir.","neighbor_ref":"root_001650/B001","relation_type":"near_neighbor","shared_zone":"Bilerek yapılan bir işaret de yüzeyde iz bırakabilir."}],"source_phrase_ar":"البلد الأثر في البدن وغيره والجمع أبلاد (jamhara)؛ البلد الأثر والجمع أبلاد (sihah)؛ البلد الأثر بالجسد وجمعه أبلاد (tahdhib)؛ ولاعتبار الأثر قيل بجلده بلد أي أثر وجمعه أبلاد (mufradat)؛ البلد الأثر وجمعه أبلاد (maqayis)","source_summary":"Kaynaklar bedende veya başka bir yerde kalan iz anlamında birleşir ve çoğul biçimin birden çok izi gösterdiğini bildirir. İzin nedeni belirtilmediğinden anlam yara ya da işaretleme gibi tek bir oluşum yoluyla sınırlandırılamaz.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه البلد بمعنى الأثر في البدن أو الجلد أو غيره، وجمعه أبلاد.","what_is_not_ar":"ليس فيه البلد بمعنى الأرض ولا البلادة بمعنى قلة الذكاء."},"support_links":[]},{"boundary":"Dal geçici şaşkınlıktan ve sırf iri bedenden ayrılır; kalıcı yavaş kavrayış, ilerleyememe veya işte güçsüz kalma odağındadır.","branch_kind":"mixed_non_bare","branch_ref":"root_000148/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:3:2:2","qac_word_ref":"95:3:2","surface_ar":"بَلَدِ"}],"gloss":"kavrayışta, ilerlemede veya işte ağır ve yetersiz kalma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Zeka, kavrayış, nüfuz ve işleri hızla yürütme gücünün düşük olması çekirdektir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir atın öndeki atlara yetişemeyip geride kalması aynı yavaşlık niteliğiyle anlatılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli eylem kalıbında kişi çalışmada ve cömertçe vermede geriler ve güçsüzleşir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kaba ve iri bedenli kişilerde sık görülmesi anlamın nedeni olarak anılır, fakat zorunlu bir özellik değildir."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan, hayvan ve belirli iş bağlamlarındaki ortak yavaşlık ve yetersizlik çekirdeğini kapsar.","boundary_detail":"Dal geçici şaşkınlıktan ve sırf iri bedenden ayrılır; kalıcı yavaş kavrayış, ilerleyememe veya işte güçsüz kalma odağındadır.","branch_image_ar":"البلادة وضعف النفاذ","concept_gloss":"kavrayışta, ilerlemede veya işte ağır ve yetersiz kalma","contextual_glosses":[{"applicability":"Bir insanın zeka, kavrayış ve işlerde ilerleme çevikliği düşük olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Atın yarışta geri kalmasını ve iş ile vermedeki özel güçsüzleşmeyi dışarıda bırakır.","preserves":"Zihinsel ve pratik kavrayış yavaşlığını korur."},"facet_ids":["F001"],"text":"ağır kavrayışlı","usage_role":"general"},{"applicability":"Bir atın öndeki atlara yetişememesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsandaki kavrayış yavaşlığını ve işteki güçsüzleşmeyi vermez.","preserves":"İlerleme ve yarış bakımından geri kalmayı korur."},"facet_ids":["F002"],"text":"yarışta geri kalan","usage_role":"contextual"}],"definition":"Kavrayışta, karar vermede veya ilerlemede ağır ve yetersiz kalma niteliğidir; insanın zihinsel ve pratik çevikliğini, hayvanın yarışta geri kalmasını kapsayabilir. Belirli bir kullanımda işte ve vermede güçsüzleşmeyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Zeka, kavrayış, nüfuz ve işleri hızla yürütme gücünün düşük olması çekirdektir."},{"facet_id":"F002","role":"extension","statement":"Bir atın öndeki atlara yetişemeyip geride kalması aynı yavaşlık niteliğiyle anlatılır."},{"facet_id":"F003","role":"specialization","statement":"Belirli eylem kalıbında kişi çalışmada ve cömertçe vermede geriler ve güçsüzleşir."},{"facet_id":"F004","role":"associated_use","statement":"Kaba ve iri bedenli kişilerde sık görülmesi anlamın nedeni olarak anılır, fakat zorunlu bir özellik değildir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kaynakta bu dal için zorunlu olmayan geçici afallama durumunu ekler.","collision":"Şaşkınlıkla duraksama dalıyla karışır.","fit":"displacement","loses":"Kalıcı kavrayış yavaşlığını, yarışta geri kalmayı ve işte güçsüzleşmeyi kaybeder.","preserves":"Kişinin bir işte ilerleyememesi görünüşünü kısmen çağrıştırır."},"text":"şaşkın"}],"identity_rationale":"Kaynak ifade insan için zeka, kavrayış ve işlerde atılganlık eksikliğini; hayvan için yarışta geri kalmayı; belirli bir iş kalıbında çalışma ve cömertlikte güçsüzleşmeyi bildirir. İri ve kaba bedenle kurulan ilişki açıklayıcı bir çağrışımdır, anlamın zorunlu koşulu değildir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"zeka, kavrayış ve atılganlık düşüklüğü"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ağır kavrayışlı; yarışta geri kalan"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"işte ve cömertlikte gerileyip güçsüzleşti"}],"lexicalization_note":"Temel biçimler zeka ve ilerleme yavaşlığını gösterir; işte ve vermede güçsüzleşme yalnız belirtilen eylem kalıbına bağlıdır ve bütün dala yayılmaz.","neighbor_coverage_note":"Bütün yavaşlık, zayıflık ve işte geri kalma adayları değerlendirildi; genel yetersizlik ile salt yavaşlık odak dalının iki temel sınırını gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak ağır kavrayış ve yavaş ilerleme merkezlidir; komşu genel güçsüzlük ve değer ölçüsünde eksik kalmaya uzanır.","focus_only":"Odak zeka ve kavrayış düşüklüğünü, ayrıca işte güçsüzleşmeyi açıkça kapsar.","gloss":"zayıf ve hedefe erişemeyen","neighbor_only":"Komşu düşük değer, yiğitlik ve soyluluk ölçüsüne erişememe ile başını kaldıramayan atı da kapsar.","neighbor_ref":"root_001551/B005","relation_type":"near_synonym","shared_zone":"İki dal insanın yetersizliğini ve atın öndekilere yetişememesini anlatabilir."},{"boundary_match":"partial","distinction":"Komşu yalnız hız eksikliğidir; odakta kavrayış ve yeterlilik düşüklüğü de kurucudur.","focus_only":"Odak zeka ve kavrayış düşüklüğü ile işte yetersizliği içerir.","gloss":"yavaşlık ve gecikme","neighbor_only":"Komşu hareket, geliş ve yolculuk dahil her türlü salt yavaşlığı anlatır.","neighbor_ref":"root_000124/B001","relation_type":"near_neighbor","shared_zone":"Yavaş ilerleme ve geride kalma iki dalda da görülebilir."}],"source_phrase_ar":"رجل بليد بين البلادة ضد النحرير (jamhara)؛ البلادة ضد الذكاء وقد بلد بالضم فهو بليد (sihah)؛ أبلد الرجل إذا كانت دابته بليدة (sihah)؛ البلادة نقيض النفاذ والمضاء في الأمور (tahdhib)؛ فرس بليد إذا تأخر عن الخيل السوابق (tahdhib)؛ بلد إذا نكس في العمل وضعف حتى في الجود (tahdhib)؛ لكثرة وجود البلادة فيمن كان جلف البدن (mufradat)","source_summary":"Toplu kanıt zeka, kavrayış, nüfuz ve ilerleme gücündeki düşüklüğü ortaklaştırır; atın yarışta geri kalması ve kişinin işte ya da cömertlikte güçsüzleşmesi bu çekirdeğin özel gerçekleşmeleridir. Kaba bedenle bağlantı zorunlu tanım değil, açıklayıcı bir ilişkilendirmedir.","sources":["JA","SI","TA","MU"],"what_is_ar":"يدخل فيه البلادة ضد الذكاء والنفاذ والمضاء، والبليد من الناس أو الدواب، وتأخر الفرس عن الخيل السوابق، وضعف المرء في العمل والجود.","what_is_not_ar":"ليس فيه الحيرة العابرة ولا عظم الخلق إلا إذا نص المصدر على علاقة بينهما."},"support_links":[]},{"boundary":"Dal yalnız fiziksel irilik, enlilik, kabalık ve sağlamlıkla ilgilidir; kaş görünüşü veya zihinsel yavaşlık anlamlarını içermez.","branch_kind":"bare","branch_ref":"root_000148/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:3:2:2","qac_word_ref":"95:3:2","surface_ar":"بَلَدِ"}],"gloss":"iri, enli ve kaba yapılı; hayvanda sert ve dayanıklı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İri ve kaba beden yapısı çekirdek fiziksel niteliktir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İlgili bir biçim özellikle enli ve geniş bedeni anlatır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Deve için kullanılan biçim iri bedenle birlikte sertlik ve dayanıklılığı belirtir."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan ve hayvan bedenine ilişkin irilik, enlilik, kabalık ve dayanıklılık niteliklerini kapsar.","boundary_detail":"Dal yalnız fiziksel irilik, enlilik, kabalık ve sağlamlıkla ilgilidir; kaş görünüşü veya zihinsel yavaşlık anlamlarını içermez.","branch_image_ar":"غلظ الخلق وعظم الجسم","concept_gloss":"iri, enli ve kaba yapılı; hayvanda sert ve dayanıklı","contextual_glosses":[{"applicability":"İnsan bedeninin büyüklüğü ve kaba yapısı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Enlilik özel biçimini ve devedeki sert, dayanıklı yapı vurgusunu dışarıda bırakır.","preserves":"İri ve kaba beden çekirdeğini korur."},"facet_ids":["F001"],"text":"iri ve kaba yapılı","usage_role":"general"}],"definition":"Bir insanın veya hayvanın iri, enli ve kaba yapılı olmasıdır; deve söz konusu olduğunda bedenin sert ve dayanıklı oluşu da kapsama girer.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İri ve kaba beden yapısı çekirdek fiziksel niteliktir."},{"facet_id":"F002","role":"specialization","statement":"İlgili bir biçim özellikle enli ve geniş bedeni anlatır."},{"facet_id":"F003","role":"specialization","statement":"Deve için kullanılan biçim iri bedenle birlikte sertlik ve dayanıklılığı belirtir."}],"identity_rationale":"Kaynak ifade insan için iri ve kaba yapıyı, ilgili başka biçimler için enli olmayı ve devenin sağlam, sert bedenini açıkça destekler. Zihinsel yavaşlıkla kurulan açıklayıcı ilişki bu fiziksel yapının tanımına katılmaz.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"iri ve kaba yapılı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"enli; deve için sert ve dayanıklı"}],"lexicalization_note":"Çıplak biçimlerin fiziksel beden yapısı anlamı tanımlanır; zihinsel nitelik ve kaşların görünüşüyle ilgili eş biçimli anlamlar dışarıda tutulur.","neighbor_coverage_note":"Bütün irilik ve beden bölgesi adayları değerlendirildi; genel kalın yapı ile iri-ağır yapı, odaktaki enlilik ve dayanıklılık sınırını en iyi açıkladı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak bütün bedenin iriliği ve enliliğine yönelir; komşu tek tek dokuların ve beden bölümlerinin kalınlığına da uzanır.","focus_only":"Odak enli insanı ve sert, dayanıklı deveyi belirli biçimlerle kapsar.","gloss":"kalın ve kaba beden yapısı","neighbor_only":"Komşu kalınlığı deri, kemik, baş derisi ve hörgüç gibi tek tek beden bölümlerine de uygular.","neighbor_ref":"root_000217/B003","relation_type":"near_synonym","shared_zone":"İki dal iri, kalın ve kaba fiziksel yapıyı anlatır."},{"boundary_match":"partial","distinction":"Komşuda ağırlık, belirli dişi varlıklar ve hoyratlık öne çıkar; odakta bu koşullar zorunlu değildir.","focus_only":"Odak insan ve hayvanda kaba yapı ile dayanıklılığı kapsar.","gloss":"iri ve ağır yapılı","neighbor_only":"Komşu özellikle dişi deve veya kadında irilikle birlikte ağırlık ve hoyratlığı belirtir.","neighbor_ref":"root_001250/B020","relation_type":"near_synonym","shared_zone":"İki dal iri ve geniş bedenli olmayı anlatabilir."}],"source_phrase_ar":"رجل أبلد غليظ الخلق (jamhara)؛ الأبلد الرجل العظيم الخلق والبلندى العريض والمبلندى من الجمال الصلب الشديد (sihah)؛ رجل أبلد عبارة عن عظيم الخلق (mufradat)","source_summary":"Kaynaklar iri ve kaba beden yapısında birleşir; enli insan ile sert ve dayanıklı deve nitelemeleri bu fiziksel çekirdeğin özel biçimleridir. Zihinsel yavaşlık bu dalın tanımsal parçası değildir.","sources":["JA","SI","MU"],"what_is_ar":"يدخل فيه الأبلد العظيم أو الغليظ الخلق، والبلندى العريض، والمبلندى من الجمال الصلب الشديد.","what_is_not_ar":"ليس فيه الأبلد الذي ليس بمقرون الحاجبين، ولا البليد ضد الذكي إلا على جهة التعليل الذي ذكره بعض المصادر."},"support_links":[]},{"boundary":"Dal bir yerde kalıp ikamet etmeyi kapsar; yere temas edip yapışmayı, yalnızca bir yere varmayı veya oraya dönmeyi içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_000148/B009","candidate_links":[{"candidate_id":"cand_ca09ef648e87c4431f4a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:3:2:2","qac_word_ref":"95:3:2","surface_ar":"بَلَدِ"}],"gloss":"bir yerde kalıp ikamet etme ve orada oturan kişi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yerde bulunmayı sürdürmek ve orayı terk etmeden kalmak çekirdektir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu eylemi sürdüren kişi, bulunduğu yerde oturan kimse olarak adlandırılır."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yer belirten eylem kalıbını ve bu eylemden türeyen sakin adını birlikte kapsar.","boundary_detail":"Dal bir yerde kalıp ikamet etmeyi kapsar; yere temas edip yapışmayı, yalnızca bir yere varmayı veya oraya dönmeyi içermez.","branch_image_ar":"الإقامة ولزوم البلد","concept_gloss":"bir yerde kalıp ikamet etme ve orada oturan kişi","contextual_glosses":[{"applicability":"Kişinin bir yeri terk etmeyip orada ikamet etmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"O yerde oturan kişiyi adlandıran türemiş anlamı dışarıda bırakır.","preserves":"Kalma ve ikamet etme eylemini korur."},"facet_ids":["F001"],"text":"bir yerde kalıp oturmak","usage_role":"general"}],"definition":"Bir yerde kalmak, orayı terk etmeyip orada ikamet etmektir; aynı anlam alanındaki kişi adı, o yerde oturan ve kalan kimseyi gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yerde bulunmayı sürdürmek ve orayı terk etmeden kalmak çekirdektir."},{"facet_id":"F002","role":"extension","statement":"Bu eylemi sürdüren kişi, bulunduğu yerde oturan kimse olarak adlandırılır."}],"identity_rationale":"Kaynak ifade bir yerde kalmayı, orayı terk etmeyip yerleşmeyi ve bu durumda olan kişiyi tutarlı biçimde verir. Yere fiziksel olarak yapışma ve memlekete dönme isteği bu eylemin parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir yerde kalıp ikamet etmek"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"bir yerde oturan, sakin"}],"lexicalization_note":"Kalma eylemi yer belirten tamamlayıcıyla kurulur; kişi adı ise orada oturanı gösterir. Bu yapılar fiziksel yapışma anlamına genellenmez.","neighbor_coverage_note":"Bütün ikamet, varış, yurt ve dönüş adayları değerlendirildi; yerleşip oturma ile birkaç günlük kalış, süre ve süreklilik sınırlarını en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak genel olarak yerde kalma ve sakin adıdır; komşuda yerleşme ve konutu sürekli tutma görünüşü daha belirgindir.","focus_only":"Odak yerle ilişkili kişi adını ayrıca verir ve kalmayı yer adından hareketle anlatır.","gloss":"yerleşip oturma","neighbor_only":"Komşu yerleşme, sakin durma ve bir konutu sürekli tutma görünüşünü daha açık taşır.","neighbor_ref":"root_001243/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir yerde kalmayı ve orada oturmayı anlatır."},{"boundary_match":"partial","distinction":"Komşunun birkaç günlük süre sınırı vardır; odakta süre belirtilmez ve daha sürekli ikamet mümkün olabilir.","focus_only":"Odak süresi belirtilmeyen ikameti ve orada oturan kişiyi kapsar.","gloss":"birkaç gün bir yerde kalma","neighbor_only":"Komşu bir yerde birkaç gün kalmayı özellikle sınırlar.","neighbor_ref":"root_000377/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin bir yerde bir süre kalmasını anlatır."}],"source_phrase_ar":"بلد بالمكان أقام به فهو بالد (sihah)؛ بلدت بالمكان أبلد بلودا أي أقمت به (tahdhib)؛ بلد لزم البلد (mufradat)؛ البالد قياسا المقيم بالبلد (maqayis)","source_summary":"Kaynaklar bir yerde kalma ve orayı sürekli tutma anlamında birleşir; kişi biçimi de aynı yerle ilişkisini sürdüren sakini gösterir. Kalışın süresi veya yere fiziksel temas zorunlu değildir.","sources":["SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه بلد بالمكان إذا أقام به، وبلد إذا لزم البلد، والبالد المقيم بالبلد.","what_is_not_ar":"ليس فيه اللصوق بالأرض ولا الحيرة التي تحصل لمن خرج عن موطنه إلا حيث يصرح المصدر بالاشتقاق."},"support_links":["sup_30cbc122583b0600c80a"]},{"boundary":"Dal yere fiziksel olarak uzanma veya yapışmayı ve yere yapışık eski havuzu kapsar; çökme veya aynı yerde yaşamayı sürdürme anlamını içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_000148/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:3:2:2","qac_word_ref":"95:3:2","surface_ar":"بَلَدِ"}],"gloss":"kendini yere atıp yapışma; yere yapışık eski havuz","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bedenin yere atılması, uzanması veya yere sıkıca yapışması çekirdek eylemdir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yere yapışık eski havuz aynı fiziksel ilişkiyle adlandırılır."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan bedeninin yere teması ile eski havuzun yere yapışık konumunu birlikte kapsar.","boundary_detail":"Dal yere fiziksel olarak uzanma veya yapışmayı ve yere yapışık eski havuzu kapsar; çökme veya aynı yerde yaşamayı sürdürme anlamını içermez.","branch_image_ar":"اللصوق بالأرض","concept_gloss":"kendini yere atıp yapışma; yere yapışık eski havuz","contextual_glosses":[{"applicability":"Bir kişinin bedeniyle yere uzanması veya yere yapışması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eski su yapısının yere oturmuş veya çökmüş görünümünü dışarıda bırakır.","preserves":"Bedenin yere atılması ve yapışması eylemini korur."},"facet_ids":["F001"],"text":"kendini yere atıp yapışmak","usage_role":"general"}],"definition":"Bir kişinin kendini yere atarak yere uzanması veya yere yapışmasıdır. Aynı ad, yere yapışık eski havuz için de kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bedenin yere atılması, uzanması veya yere sıkıca yapışması çekirdek eylemdir."},{"facet_id":"F002","role":"extension","statement":"Yere yapışık eski havuz aynı fiziksel ilişkiyle adlandırılır."}],"identity_rationale":"Kaynak ifade kişinin kendini yere atmasını veya yere yapışmasını ve yere yapışık eski havuz kullanımını destekler. Çökme yorumu kaynak ifadesinin ötesine geçtiğinden dışarıda tutulmalı; bu fiziksel temas da bir yerde ikamet etme anlamından ayrılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"kendini yere atmak veya yere yapışmak"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yere yapışık eski havuz"}],"lexicalization_note":"Kişinin yere yapışması yer tamamlayıcılı kalıba bağlıdır; eski su yapısı için kullanılan ad ise ayrı bir nesne kullanımını gösterir ve genel ikamet anlamına açılmaz.","neighbor_coverage_note":"Bütün yapışma, yayılma, çökme ve ikamet adayları değerlendirildi; yere yayılma ile çömelip kalma, hareket ve sonuç farkını en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kendini yere atma ve belirli nesne kullanımına bağlıdır; komşu uzanma ile yüzeye yayılmayı daha geniş kapsar.","focus_only":"Odak yere yapışmış eski su yapısı için nesne adını da kapsar.","gloss":"yere uzanıp yayılma","neighbor_only":"Komşu insan ve hayvandan yere yayılan bitkiye kadar daha geniş uzanma ve yayılma örneklerini içerir.","neighbor_ref":"root_000928/B006","relation_type":"near_synonym","shared_zone":"İki dal da bedenin yere uzanmasını ve yere yapışmasını anlatır."},{"boundary_match":"partial","distinction":"Odakta yere atılma ya da yapışma, komşuda ise çömelip aynı noktada kalma belirleyicidir.","focus_only":"Odak kendini yere atma hareketini ve yere oturmuş eski su yapısını kapsar.","gloss":"yere çömelip yerinde kalma","neighbor_only":"Komşu kuş, yırtıcı, insan veya ağır nesnenin bulunduğu yeri terk etmeyip çömelerek kalmasını içerir.","neighbor_ref":"root_000222/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir varlığın yere yakın biçimde yapışık ve hareketsiz görünmesini anlatabilir."}],"source_phrase_ar":"بلد تبليدا ضرب بنفسه الأرض وأبلد لصق بالأرض (sihah)؛ المبلد الحوض القديم ههنا وأراد ملبد فقلب وهو اللاصق بالأرض (tahdhib)؛ بلد الرجل بالأرض إذا لزق بها (maqayis)؛ مبلد بين موماة يذكر حوضا لاصقا بالأرض (maqayis)","source_summary":"Kaynaklar yere atılma ve yere yapışma eyleminde birleşir. Yere yapışık eski havuza verilen ad, bu özel nesne kullanımını aynı fiziksel çekirdeğe bağlar.","sources":["SI","TA","MQ"],"what_is_ar":"يدخل فيه بلد تبليدا إذا ضرب بنفسه الأرض، وأبلد إذا لصق بالأرض، والمبلد من الحوض القديم اللاصق بالأرض أو المتداعي.","what_is_not_ar":"ليس فيه الإقامة بالمكان ولا الصدر إلا في بروك الناقة إذا نص المصدر على وضع الصدر."},"support_links":[]},{"boundary":"Dal genel savaşmayı değil, tarafların kılıç veya sopalarla karşılıklı vuruşmasını kapsar; yerde kalma yalnız türetim açıklamasıdır.","branch_kind":"bare","branch_ref":"root_000148/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:3:2:2","qac_word_ref":"95:3:2","surface_ar":"بَلَدِ"}],"gloss":"kılıç veya sopalarla karşılıklı vuruşma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tarafların kılıç veya sopalarla birbirine karşılıklı vurması çekirdek eylemdir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yerde tutunup onun üzerinde savaşma düşüncesi, eyleme ilişkin olası bir türetim açıklamasıdır."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Silahlı karşılıklılık çekirdeğini ve bunun çatışma niteliğini doğrudan temsil eder.","boundary_detail":"Dal genel savaşmayı değil, tarafların kılıç veya sopalarla karşılıklı vuruşmasını kapsar; yerde kalma yalnız türetim açıklamasıdır.","branch_image_ar":"المبالدة بالسيوف والعصي","concept_gloss":"kılıç veya sopalarla karşılıklı vuruşma","contextual_glosses":[{"applicability":"Araçların kılıç veya sopa olduğu karşılıklı çatışma bağlamında doğal eylem karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yerde tutunarak savaşmaya dayanan olası türetim açıklamasını belirtmez.","preserves":"Karşılıklı silahlı dövüşme çekirdeğini korur."},"facet_ids":["F001"],"text":"silahlarla karşılıklı dövüşmek","usage_role":"general"}],"definition":"İki tarafın kılıç veya sopalarla birbirine karşılıklı vurup çatışmasıdır. Savaşçıların yerde tutunarak dövüşmesiyle kurulan bağlantı, anlamın kendisi değil olası bir türetim açıklamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tarafların kılıç veya sopalarla birbirine karşılıklı vurması çekirdek eylemdir."},{"facet_id":"F002","role":"associated_use","statement":"Yerde tutunup onun üzerinde savaşma düşüncesi, eyleme ilişkin olası bir türetim açıklamasıdır."}],"identity_rationale":"Kaynak ifade iki tarafın kılıç veya sopalarla karşılıklı vuruşmasını doğrudan verir; yerde tutunarak savaşma açıklaması ise olası bir türetim yorumudur. Bu yorum eylemin zorunlu parçası yapılmadan dal korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"kılıç veya sopalarla karşılıklı dövüşme"}],"lexicalization_note":"Çıplak biçim karşılıklı silahlı vuruşma anlamıyla tanımlanır; olası yerle bağlantı eylemin zorunlu koşulu sayılmaz.","neighbor_coverage_note":"Bütün savaş, düello, silah ve tek yönlü vurma adayları değerlendirildi; genel karşılıklı çarpışma ile öldürme amaçlı savaş en yararlı iki sınırı verdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta belirli vurma araçları kurucudur; komşuda araç sınırlaması yoktur ve üstün gelme görünüşü öne çıkabilir.","focus_only":"Odak kılıç veya sopa araçlarını ve karşılıklı vuruşmayı açıkça sınırlar.","gloss":"rakiple çarpışma","neighbor_only":"Komşu kahramanların çarpışmasını, rakibe üstün gelmeyi ve daha genel karşılıklı mücadeleyi kapsar.","neighbor_ref":"root_001219/B002","relation_type":"near_synonym","shared_zone":"İki dal da rakip tarafların karşılıklı vuruşup mücadele etmesini anlatır."},{"boundary_match":"partial","distinction":"Komşu daha geniş savaş eylemi ve öldürme amacıyla tanımlanır; odak belirli araçlarla vuruşma biçimine dayanır.","focus_only":"Odak kılıç ve sopalarla karşılıklı vuruşma biçimini belirtir.","gloss":"karşılıklı savaşma","neighbor_only":"Komşu iki veya daha çok tarafın öldürme amacı taşıyan genel savaşmasını kapsar.","neighbor_ref":"root_001200/B011","relation_type":"near_neighbor","shared_zone":"Karşılıklı silahlı dövüş iki dalın da kapsamına girebilir."}],"source_phrase_ar":"المبالدة مثل المباطلة (sihah)؛ المبالدة كالمبالطة بالسيوف والعصي إذا تجالدوا بها (tahdhib)؛ المبالدة بالسيوف مثل المبالطة وقال بعضهم اشتق من الأول كأنهم لزموا الأرض فقاتلوا عليها (maqayis)","source_summary":"Kaynaklar kılıç ve sopalarla karşılıklı vuruşma anlamında birleşir. Eylemin yerde tutunarak savaşmadan türediği görüşü açıklayıcı bir öneridir ve çatışmanın zorunlu koşulu değildir.","sources":["SI","TA","MQ"],"what_is_ar":"يدخل فيه المبالدة بمعنى المجالدة أو المباطلة بالسيوف والعصي، واشتقاقها من لزوم الأرض في القتال إذا ذكر المصدر ذلك.","what_is_not_ar":"ليس فيه البلادة ضد الذكاء ولا مجرد الإقامة بالبلد."},"support_links":[]},{"boundary":"Dal deve kuşunun yumurta çukuru ile terk edilmiş yumurtasına özgüdür; genel yer, başka kuşların yumurtası veya yavru anlamını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000148/B012","candidate_links":[{"candidate_id":"cand_51a36d083402239bd41e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:3:2:2","qac_word_ref":"95:3:2","surface_ar":"بَلَدِ"}],"gloss":"deve kuşunun yumurta çukuru ve orada bırakılmış yumurtası","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Deve kuşunun yumurta bıraktığı çukur veya yuva çekirdektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli ad tamlaması, deve kuşunun bırakıp gittiği yumurtayı gösterir."}}],"root_ar":"ب ل د","root_id":"root_000148","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yuva niteliğindeki çukuru ve yalnız özel ad tamlamasındaki terk edilmiş yumurtayı birlikte kapsar.","boundary_detail":"Dal deve kuşunun yumurta çukuru ile terk edilmiş yumurtasına özgüdür; genel yer, başka kuşların yumurtası veya yavru anlamını kapsamaz.","branch_image_ar":"أدحي النعام","concept_gloss":"deve kuşunun yumurta çukuru ve orada bırakılmış yumurtası","contextual_glosses":[{"applicability":"Sözcük doğrudan kuşun yumurtladığı yer için kullanıldığında geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Özel ad tamlamasında gösterilen bırakılmış yumurta anlamını dışarıda bırakır.","preserves":"Deve kuşunun yumurtlama çukuru olan çekirdeği korur."},"facet_ids":["F001"],"text":"deve kuşunun yumurta çukuru","usage_role":"general"},{"applicability":"Yalnız terk edilmiş yumurtayı gösteren belirli ad tamlamasında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yumurtanın bırakıldığı çukur veya yuva anlamını vermez.","preserves":"Bırakılmış deve kuşu yumurtası anlamını korur."},"facet_ids":["F002"],"text":"deve kuşunun bırakıp gittiği yumurta","usage_role":"contextual"}],"definition":"Deve kuşunun yumurtlamak için kullandığı çukur veya yuvadır; belirli bir ad tamlamasında, deve kuşunun bu yerde bırakıp gittiği yumurtayı da gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Deve kuşunun yumurta bıraktığı çukur veya yuva çekirdektir."},{"facet_id":"F002","role":"specialization","statement":"Belirli ad tamlaması, deve kuşunun bırakıp gittiği yumurtayı gösterir."}],"identity_rationale":"Kaynak ifade aynı dalda deve kuşunun yumurtlamak için kullandığı çukuru ve bu kuşun orada bırakıp gittiği yumurtayı açıkça verir. Genel yeryüzü parçası anlamı burada yalnız ortak biçimdir ve tanıma katılmaz.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"deve kuşunun yumurta çukuru"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"deve kuşunun bırakıp gittiği yumurta"}],"lexicalization_note":"Temel biçim deve kuşunun yumurta çukurunu gösterir; terk edilmiş yumurta anlamı yalnız belirtilen ad tamlamasına bağlıdır ve genel yumurta anlamına genişletilmez.","neighbor_coverage_note":"Bütün yumurta, yavru, yuva ve çöl adayları değerlendirildi; deve kuşu çukuru ile bırakılmış yumurta adayları dalın iki kurucu unsuruna doğrudan karşılık verdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yuva anlamında büyük ölçüde örtüşürler; odak terk edilmiş yumurtaya, komşu ise çukurun hazırlanışına ve göksel kullanıma ayrıca uzanır.","focus_only":"Odak özel ad tamlamasında bırakılmış deve kuşu yumurtasını da kapsar.","gloss":"deve kuşunun yumurtlama çukuru","neighbor_only":"Komşu yuvanın kuş tarafından ayağıyla hazırlanmasını ve ayrıca göksel bir yer kullanımını bildirir.","neighbor_ref":"root_000462/B003","relation_type":"near_synonym","shared_zone":"İki dal da deve kuşunun yumurtlamak için kullandığı çukuru adlandırır."},{"boundary_match":"partial","distinction":"Odak yuva ile yumurtayı aynı dalda tutar; komşu yumurtadan benzetmeyle türeyen başka nesne adlarını kapsar.","focus_only":"Odak yumurtanın yanında deve kuşunun yumurta çukurunu da kapsar.","gloss":"bırakılmış deve kuşu yumurtası","neighbor_only":"Komşu bırakılmış yumurtadan başlık ve baş gibi benzetmeli nesnelere de genişler.","neighbor_ref":"root_000180/B008","relation_type":"near_synonym","shared_zone":"İki dal da kırda bırakılmış deve kuşu yumurtasını anlatabilir."}],"source_phrase_ar":"البلد أدحي النعام يقال هو أذل من بيضة البلد أي من بيضة النعام التي تتركها (sihah)","source_summary":"Tek kaynaklı kanıt deve kuşunun yumurta çukurunu temel kullanım, kuşun bırakıp gittiği yumurtayı ise belirli ad tamlamasına bağlı kullanım olarak verir. Yuva ile yumurta aynı varlık değildir ve tanımda ayrı tutulmalıdır.","sources":["SI"],"what_is_ar":"يدخل فيه البلد بمعنى أدحي النعام، وبيضة البلد أي بيضة النعام التي تتركها.","what_is_not_ar":"ليس فيه البلد بمعنى القرية أو الأرض العامة إلا على جهة الموضع الخاص."},"support_links":["sup_6721a5fa2bc4fd926de8"]}],"candidate_inventory":[{"anchor_refs":["95:3:1"],"branch_refs":[],"candidate_id":"cand_55a8d4f786e11e4a78b9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:1:compact-oath-onset","source_type":"word_analysis","support_ids":["sup_40bd3cbf270978f51392","sup_f8a81dd2b04a5225538b"],"title":"one-letter onset compresses the oath entry","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:1","qac_refs":["95:3:1:1"],"status":"accepted"}},{"anchor_refs":["95:3:1"],"branch_refs":[],"candidate_id":"cand_c69f8d28703d1d166e4d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:1:delayed-oath-answer","source_type":"word_analysis","support_ids":["sup_40bd3cbf270978f51392","sup_b61f0abd1a2f96b07451"],"title":"boundary-spanning oath waits for its answer","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:1","qac_refs":["95:3:1:1"],"status":"accepted"}},{"anchor_refs":["95:3:1"],"branch_refs":[],"candidate_id":"cand_e10de4e7a8394a8d8f5e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:1:oath-coordination","source_type":"word_analysis","support_ids":["sup_40bd3cbf270978f51392","sup_d4a25681e73979303ecc"],"title":"coordination and oath force stay live together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:1","qac_refs":["95:3:1:1"],"status":"accepted"}},{"anchor_refs":["95:3:1"],"branch_refs":[],"candidate_id":"cand_bad2aec56242e4699445","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:1:third-oath-escalation","source_type":"word_analysis","support_ids":["sup_40bd3cbf270978f51392","sup_5721bc13550b040ab8ac"],"title":"third oath item shifts into inhabited society","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:1","qac_refs":["95:3:1:1"],"status":"accepted"}},{"anchor_refs":["95:3:2"],"branch_refs":[],"candidate_id":"cand_c66fe497e3dd31225b45","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:2:appositional-oath-object","source_type":"word_analysis","support_ids":["sup_2a26b886332772cd163b","sup_5e7e2bd5db36866a217d"],"title":"demonstrative begins the sworn object before case appears","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:2","qac_refs":["95:3:1:2"],"status":"accepted"}},{"anchor_refs":["95:3:2"],"branch_refs":[],"candidate_id":"cand_d0a5664571376c256c54","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:2:deictic-fronting","source_type":"word_analysis","support_ids":["sup_5e7e2bd5db36866a217d","sup_cdd261afc779ca6c08f0"],"title":"presence precedes the city name","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:2","qac_refs":["95:3:1:2"],"status":"accepted"}},{"anchor_refs":["95:3:2"],"branch_refs":[],"candidate_id":"cand_fc2ea772fc68efd5b5cc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:2:extended-pointing-sound","source_type":"word_analysis","support_ids":["sup_5e7e2bd5db36866a217d","sup_7aace5cc7bed75e336df"],"title":"lengthened demonstrative opens the cadence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:2","qac_refs":["95:3:1:2"],"status":"accepted"}},{"anchor_refs":["95:3:2"],"branch_refs":[],"candidate_id":"cand_051883e6696e4e8a3a18","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:2:proximal-known-city","source_type":"word_analysis","support_ids":["sup_5e7e2bd5db36866a217d","sup_8f617991f3be5972ddf6"],"title":"proximity makes the city witnessed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:2","qac_refs":["95:3:1:2"],"status":"accepted"}},{"anchor_refs":["95:3:2"],"branch_refs":[],"candidate_id":"cand_5a4d20156a28d99ad380","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:2:scene-shift-from-mountain","source_type":"word_analysis","support_ids":["sup_5e7e2bd5db36866a217d","sup_9502930dda1ddf854cb5"],"title":"named sacred geography becomes witnessed city","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:2","qac_refs":["95:3:1:2"],"status":"accepted"}},{"anchor_refs":["95:3:3"],"branch_refs":[],"candidate_id":"cand_269b3193c090ab956233","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000148"],"scope":"focus_ayah","source_local_id":"95:3:3:boundary-from-mountain-to-city","source_type":"word_analysis","support_ids":["sup_086ab3f2ae78e4190952","sup_7c6968f3ca765e1c288a"],"title":"bounded terrain becomes inhabited bounded place","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:3","qac_refs":["95:3:2:1","95:3:2:2"],"status":"accepted"}},{"anchor_refs":["95:3:3"],"branch_refs":[],"candidate_id":"cand_1ddd334770a92260eb6b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000148"],"scope":"focus_ayah","source_local_id":"95:3:3:bounded-settled-place","source_type":"word_analysis","support_ids":["sup_086ab3f2ae78e4190952","sup_346d7fadf31febd07826"],"title":"bounded settled place is selected from a wider root field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:3","qac_refs":["95:3:2:1","95:3:2:2"],"status":"accepted"}},{"anchor_refs":["95:3:3"],"branch_refs":[],"candidate_id":"cand_27ec79c52d63f33c9ca7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000148"],"scope":"focus_ayah","source_local_id":"95:3:3:bounded-sound-profile","source_type":"word_analysis","support_ids":["sup_086ab3f2ae78e4190952","sup_45cc01c6e390cec71786"],"title":"sound marks the move into bounded place","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:3","qac_refs":["95:3:2:1","95:3:2:2"],"status":"accepted"}},{"anchor_refs":["95:3:3"],"branch_refs":[],"candidate_id":"cand_6f474ae3215849a4f600","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000148"],"scope":"focus_ayah","source_local_id":"95:3:3:cross-surah-city-oaths","source_type":"word_analysis","support_ids":["sup_086ab3f2ae78e4190952","sup_874ed92e003840fb4275"],"title":"same city term anchors other oath framing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:3","qac_refs":["95:3:2:1","95:3:2:2"],"status":"accepted"}},{"anchor_refs":["95:3:3"],"branch_refs":[],"candidate_id":"cand_86d1a0128a708518fb6d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000148"],"scope":"focus_ayah","source_local_id":"95:3:3:definite-genitive-apposition","source_type":"word_analysis","support_ids":["sup_086ab3f2ae78e4190952","sup_7a237fe72a7f70027d26"],"title":"known city noun identifies the demonstrative under oath case","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:3","qac_refs":["95:3:2:1","95:3:2:2"],"status":"accepted"}},{"anchor_refs":["95:3:3"],"branch_refs":[],"candidate_id":"cand_20ad6c4f30da30f2be5a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000148"],"scope":"focus_ayah","source_local_id":"95:3:3:deictic-layered-phrase","source_type":"word_analysis","support_ids":["sup_086ab3f2ae78e4190952","sup_0dae307dc793770f8ddf"],"title":"pointing, naming, and qualifying build the oath object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:3","qac_refs":["95:3:2:1","95:3:2:2"],"status":"accepted"}},{"anchor_refs":["95:3:3"],"branch_refs":[],"candidate_id":"cand_b30620b1b859be0597c5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000148"],"scope":"focus_ayah","source_local_id":"95:3:3:head-controls-adjective","source_type":"word_analysis","support_ids":["sup_086ab3f2ae78e4190952","sup_0931ed10bf9fb526d079"],"title":"head noun binds the final security adjective","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:3","qac_refs":["95:3:2:1","95:3:2:2"],"status":"accepted"}},{"anchor_refs":["95:3:3"],"branch_refs":[],"candidate_id":"cand_28336532d256f294fc92","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000148"],"scope":"focus_ayah","source_local_id":"95:3:3:marked-ground-and-fixedness","source_type":"word_analysis","support_ids":["sup_086ab3f2ae78e4190952","sup_e904a74c155856c36670"],"title":"marked settled ground colors the city","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:3","qac_refs":["95:3:2:1","95:3:2:2"],"status":"accepted"}},{"anchor_refs":["95:3:3"],"branch_refs":[],"candidate_id":"cand_cccd440e9ceed1694c2a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000148"],"scope":"focus_ayah","source_local_id":"95:3:3:nominal-place-anchor","source_type":"word_analysis","support_ids":["sup_086ab3f2ae78e4190952","sup_a2b16f8809b13e09d41b"],"title":"noun-only deployment makes place a given locus","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:3","qac_refs":["95:3:2:1","95:3:2:2"],"status":"accepted"}},{"anchor_refs":["95:3:3"],"branch_refs":[],"candidate_id":"cand_4f0c229690e0b5a96607","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000148"],"scope":"focus_ayah","source_local_id":"95:3:3:oath-sequence-human-turn","source_type":"word_analysis","support_ids":["sup_086ab3f2ae78e4190952","sup_cf59882a6b7d2955dfdb"],"title":"settled city is the last spatial frame before the human claim","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:3","qac_refs":["95:3:2:1","95:3:2:2"],"status":"accepted"}},{"anchor_refs":["95:3:3"],"branch_refs":[],"candidate_id":"cand_b3378d97a3a03ae23e8a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000148"],"scope":"focus_ayah","source_local_id":"95:3:3:secure-city-formula","source_type":"word_analysis","support_ids":["sup_086ab3f2ae78e4190952","sup_7db254aa55d5dab9bf3c"],"title":"city and security form a recognized Quranic pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:3","qac_refs":["95:3:2:1","95:3:2:2"],"status":"accepted"}},{"anchor_refs":["95:3:4"],"branch_refs":[],"candidate_id":"cand_8c1957c3ca397c42814a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:4:active-protector-metaphor","source_type":"word_analysis","support_ids":["sup_1262d7c89736ec18084e","sup_95da1c6b7249f232edfc"],"title":"active trust force personifies the city without replacing it","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:4","qac_refs":["95:3:3:1","95:3:3:2"],"status":"accepted"}},{"anchor_refs":["95:3:4"],"branch_refs":[],"candidate_id":"cand_0fdd39fa367ee82d71f0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:4:adjective-agreement","source_type":"word_analysis","support_ids":["sup_56d43b2501303f0a62da","sup_95da1c6b7249f232edfc"],"title":"agreement makes security part of the oath object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:4","qac_refs":["95:3:3:1","95:3:3:2"],"status":"accepted"}},{"anchor_refs":["95:3:4"],"branch_refs":[],"candidate_id":"cand_170e86645e0da7ac69a7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:4:cross-category-trustworthiness","source_type":"word_analysis","support_ids":["sup_95da1c6b7249f232edfc","sup_ad55666bbc9b6b7f117e"],"title":"same adjective can qualify messengers and city","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:4","qac_refs":["95:3:3:1","95:3:3:2"],"status":"accepted"}},{"anchor_refs":["95:3:4"],"branch_refs":[],"candidate_id":"cand_1a42be22768b8ffa4717","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:4:definite-phrase-closure","source_type":"word_analysis","support_ids":["sup_802f35bb1e1a546bbad6","sup_95da1c6b7249f232edfc"],"title":"definite adjective closes the known city phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:4","qac_refs":["95:3:3:1","95:3:3:2"],"status":"accepted"}},{"anchor_refs":["95:3:4"],"branch_refs":[],"candidate_id":"cand_e4b52537d52e815daf5a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:4:final-rhyme-closure","source_type":"word_analysis","support_ids":["sup_2ae0276f8bb9bc744312","sup_95da1c6b7249f232edfc"],"title":"final adjective seals meaning and rhyme","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:4","qac_refs":["95:3:3:1","95:3:3:2"],"status":"accepted"}},{"anchor_refs":["95:3:4"],"branch_refs":[],"candidate_id":"cand_3b10607cdad1a3ffb71f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:4:formula-declared-not-requested","source_type":"word_analysis","support_ids":["sup_95da1c6b7249f232edfc","sup_b4c2b6a68094cafa3587"],"title":"secure-city formula becomes an established attribute","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:4","qac_refs":["95:3:3:1","95:3:3:2"],"status":"accepted"}},{"anchor_refs":["95:3:4"],"branch_refs":[],"candidate_id":"cand_a75e97e7361c4e33023c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:4:grammar-meaning-sound-convergence","source_type":"word_analysis","support_ids":["sup_95da1c6b7249f232edfc","sup_9bff5a8e95fb8a75695f"],"title":"agreement, security meaning, and rhyme converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:4","qac_refs":["95:3:3:1","95:3:3:2"],"status":"accepted"}},{"anchor_refs":["95:3:4"],"branch_refs":[],"candidate_id":"cand_abcb152891c69bd79ef6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:4:nasal-soft-landing","source_type":"word_analysis","support_ids":["sup_718337884d526d431b71","sup_95da1c6b7249f232edfc"],"title":"nasal ending softens the final landing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:4","qac_refs":["95:3:3:1","95:3:3:2"],"status":"accepted"}},{"anchor_refs":["95:3:4"],"branch_refs":[],"candidate_id":"cand_c8dbd2d42416381386e9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:4:pervasive-root-narrowed-to-adjective","source_type":"word_analysis","support_ids":["sup_2ee2c6728c21cce88c16","sup_95da1c6b7249f232edfc"],"title":"pervasive security root appears as a rare city adjective","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:4","qac_refs":["95:3:3:1","95:3:3:2"],"status":"accepted"}},{"anchor_refs":["95:3:4"],"branch_refs":[],"candidate_id":"cand_d6191143b3b3d42b432e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:4:postposed-valuing-qualifier","source_type":"word_analysis","support_ids":["sup_95da1c6b7249f232edfc","sup_d4f8c07352bc1b5e4cff"],"title":"delayed adjective turns location into valued location","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:4","qac_refs":["95:3:3:1","95:3:3:2"],"status":"accepted"}},{"anchor_refs":["95:3:4"],"branch_refs":[],"candidate_id":"cand_cfc181fe50beeaeb0bfe","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:4:protection-and-trust-field","source_type":"word_analysis","support_ids":["sup_95da1c6b7249f232edfc","sup_e06b5dcc4e4b69c0d121"],"title":"derivational safety field colors the place adjective","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:4","qac_refs":["95:3:3:1","95:3:3:2"],"status":"accepted"}},{"anchor_refs":["95:3:4"],"branch_refs":[],"candidate_id":"cand_00a84ea7d088cc2fe8d0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:4:same-surah-faith-echo","source_type":"word_analysis","support_ids":["sup_57d58f8f38df61928a6b","sup_95da1c6b7249f232edfc"],"title":"place-security anticipates believing persons","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:4","qac_refs":["95:3:3:1","95:3:3:2"],"status":"accepted"}},{"anchor_refs":["95:3:4"],"branch_refs":[],"candidate_id":"cand_b03c1296b23ca66cc980","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:4:secure-trustworthy-polysemy","source_type":"word_analysis","support_ids":["sup_95da1c6b7249f232edfc","sup_cc902467ec22fed8e473"],"title":"secure and trustworthy senses coexist for the city","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:4","qac_refs":["95:3:3:1","95:3:3:2"],"status":"accepted"}},{"anchor_refs":["95:3:4"],"branch_refs":[],"candidate_id":"cand_4c4e6dae7bbd5c83d3d1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:4:security-place-pair","source_type":"word_analysis","support_ids":["sup_774b30de4623a3fb1bf9","sup_95da1c6b7249f232edfc"],"title":"security adjective answers the city noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:4","qac_refs":["95:3:3:1","95:3:3:2"],"status":"accepted"}},{"anchor_refs":["95:3:4"],"branch_refs":[],"candidate_id":"cand_4184479ce875fc3f1d6d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:4:surah-bracket-echoes","source_type":"word_analysis","support_ids":["sup_71824a6c6d3727e210a8","sup_95da1c6b7249f232edfc"],"title":"security quality helps bracket the surah argument","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:4","qac_refs":["95:3:3:1","95:3:3:2"],"status":"accepted"}},{"anchor_refs":["95:3:4"],"branch_refs":[],"candidate_id":"cand_1bc4aaf41bdc921fdc0d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"95:3:4:trust-faith-family","source_type":"word_analysis","support_ids":["sup_5a23bfc0d6565b2e574c","sup_95da1c6b7249f232edfc"],"title":"safety, entrusting, and faith compress into one adjective","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"95:3:4","qac_refs":["95:3:3:1","95:3:3:2"],"status":"accepted"}},{"anchor_refs":["95:3:2"],"branch_refs":[],"candidate_id":"cand_03566f42cde86c049477","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000148"],"scope":"focus_ayah","source_local_id":"95:3:2:2","source_type":"qac_morpheme","support_ids":["sup_bf70a66bd6f7d5d573e1"],"title":"QAC root occurrence: ب ل د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["95:3:3"],"branch_refs":[],"candidate_id":"cand_bf3788424726d8a0a7ec","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000054"],"scope":"focus_ayah","source_local_id":"95:3:3:2","source_type":"qac_morpheme","support_ids":["sup_b34b5cc597febf8229dc"],"title":"QAC root occurrence: ء م ن","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["95:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"95:3","branch_refs":["root_000054/B001","root_000148/B001"],"candidate_id":"cand_a009d145d5602a724174","commentary_obligation":"review","hft_ref":"hft_c47e90d3de459d6ecb8b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_bounded_safe_domain","source_type":"hft","support_ids":["sup_621cb79fb9717cb35bde"],"title":"base_bounded_safe_domain","trust":"legacy_unbound"},{"anchor_refs":["95:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"95:3","branch_refs":["root_000054/B001","root_000148/B009"],"candidate_id":"cand_ca09ef648e87c4431f4a","commentary_obligation":"review","hft_ref":"hft_7fcb5f2dcd38ec3d0775","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_city_as_trustee","source_type":"hft","support_ids":["sup_30cbc122583b0600c80a"],"title":"base_city_as_trustee","trust":"legacy_unbound"},{"anchor_refs":["95:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"95:3","branch_refs":["root_000054/B001","root_000148/B002"],"candidate_id":"cand_873f8ce9b2f179b6ca98","commentary_obligation":"review","hft_ref":"hft_19aa25a833596f0109a6","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_embodied_center","source_type":"hft","support_ids":["sup_5bb61778b3096b4acc24"],"title":"base_embodied_center","trust":"legacy_unbound"},{"anchor_refs":["95:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"95:3","branch_refs":["root_000054/B001","root_000148/B012"],"candidate_id":"cand_51a36d083402239bd41e","commentary_obligation":"review","hft_ref":"hft_af5aadf66906f3bc66d8","kind":"surprising_outlier","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:outlier_nesting_refuge","source_type":"hft","support_ids":["sup_6721a5fa2bc4fd926de8"],"title":"outlier_nesting_refuge","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَهَٰذَا ٱلْبَلَدِ ٱلْأَمِينِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"95:3:1:1","qac_word_ref":"95:3:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"هَٰذَا","morph_features":"STEM|POS:DEM|LEM:ha`*aA|MS","morpheme_role":"STEM","pos":"DEM","qac_ref":"95:3:1:2","qac_word_ref":"95:3:1","root_ar":"","surface_ar":"هَٰذَا"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"95:3:2:1","qac_word_ref":"95:3:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:3:2:2","qac_word_ref":"95:3:2","root_ar":"ب ل د","surface_ar":"بَلَدِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"95:3:3:1","qac_word_ref":"95:3:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"أَمِين","morph_features":"STEM|POS:ADJ|LEM:>amiyn|ROOT:Amn|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"95:3:3:2","qac_word_ref":"95:3:3","root_ar":"ء م ن","surface_ar":"أَمِينِ"}],"word_analysis_qac_refs":[["95:3:1:1"],["95:3:1:2"],["95:3:2:1","95:3:2:2"],["95:3:3:1","95:3:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["95:3:1","95:3:2","95:3:3","95:3:4"]},"focus_surface_evidence":{"arabic_uthmani":"وَهَٰذَا ٱلْبَلَدِ ٱلْأَمِينِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"95:3:1:1","qac_word_ref":"95:3:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"هَٰذَا","morph_features":"STEM|POS:DEM|LEM:ha`*aA|MS","morpheme_role":"STEM","pos":"DEM","qac_ref":"95:3:1:2","qac_word_ref":"95:3:1","root_ar":"","surface_ar":"هَٰذَا"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"95:3:2:1","qac_word_ref":"95:3:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"بَلَد","morph_features":"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"95:3:2:2","qac_word_ref":"95:3:2","root_ar":"ب ل د","surface_ar":"بَلَدِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"95:3:3:1","qac_word_ref":"95:3:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"أَمِين","morph_features":"STEM|POS:ADJ|LEM:>amiyn|ROOT:Amn|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"95:3:3:2","qac_word_ref":"95:3:3","root_ar":"ء م ن","surface_ar":"أَمِينِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["95:3:1:1"],["95:3:1:2"],["95:3:2:1","95:3:2:2"],["95:3:3:1","95:3:3:2"]],"word_analysis_refs":["95:3:1","95:3:2","95:3:3","95:3:4"],"word_rows":[{"analysis_record_ref":"95:3:1","analytic_gloss_range_en":"connective oath particle that coordinates the third oath item while also licensing oath scope","analytic_root_gloss_range_en":null,"qac_refs":["95:3:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"95:3:2","analytic_gloss_range_en":"proximal masculine singular demonstrative pointing to the immediately specified city","analytic_root_gloss_range_en":null,"qac_refs":["95:3:1:2"],"root":{},"surface":{"arabic":"هَٰذَا","transliteration":"hādhā"}},{"analysis_record_ref":"95:3:3","analytic_gloss_range_en":"the known city or bounded settled place; broader land and territory resonance remains under the local secure-city phrase","analytic_root_gloss_range_en":"bounded tract or place, inhabited land, settlement, residence and fixedness; other accepted root branches such as body marks, dullness, sky-place, and combat are not locally selected","qac_refs":["95:3:2:1","95:3:2:2"],"root":{"arabic":"ب ل د","transliteration":"b-l-d"},"surface":{"arabic":"ٱلْبَلَدِ","transliteration":"al-baladi"}},{"analysis_record_ref":"95:3:4","analytic_gloss_range_en":"secure, trustworthy, reliable, and trust-bearing as a qualitative adjective of the city","analytic_root_gloss_range_en":"safety from fear, trust, reliability, protection, entrusting, and faith; local grammar selects a city adjective rather than a verbal belief action","qac_refs":["95:3:3:1","95:3:3:2"],"root":{"arabic":"أ م ن","transliteration":"ʾ-m-n"},"surface":{"arabic":"ٱلْأَمِينِ","transliteration":"al-amīni"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["95:3"],"branch_refs":["root_000054/B001","root_000148/B001"],"candidate_id":"cand_a009d145d5602a724174","evidence_scope":"focus_ayah","hft_ref":"hft_c47e90d3de459d6ecb8b","item_id":"base_bounded_safe_domain","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_bounded_safe_domain","support_id":"sup_621cb79fb9717cb35bde"},{"anchor_refs":["95:3"],"branch_refs":["root_000054/B001","root_000148/B009"],"candidate_id":"cand_ca09ef648e87c4431f4a","evidence_scope":"focus_ayah","hft_ref":"hft_7fcb5f2dcd38ec3d0775","item_id":"base_city_as_trustee","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_city_as_trustee","support_id":"sup_30cbc122583b0600c80a"},{"anchor_refs":["95:3"],"branch_refs":["root_000054/B001","root_000148/B002"],"candidate_id":"cand_873f8ce9b2f179b6ca98","evidence_scope":"focus_ayah","hft_ref":"hft_19aa25a833596f0109a6","item_id":"base_embodied_center","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_embodied_center","support_id":"sup_5bb61778b3096b4acc24"},{"anchor_refs":["95:3"],"branch_refs":["root_000054/B001","root_000148/B012"],"candidate_id":"cand_51a36d083402239bd41e","evidence_scope":"focus_ayah","hft_ref":"hft_af5aadf66906f3bc66d8","item_id":"outlier_nesting_refuge","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_nesting_refuge","support_id":"sup_6721a5fa2bc4fd926de8"}],"diagnostics":[],"lane_counts":{"global":10,"macro":16,"micro":4},"packet_summary":{"ayah_count":8,"focus_ref":"95:3","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ر د د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000555","furuq_root_norm":"ر د د","furuq_source_root_norm":"ر د د","is_dominant":true,"target_occurrences":52,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001413","furuq_root_norm":"م ر د","furuq_source_root_norm":"م ر د","is_dominant":false,"target_occurrences":5,"target_rank":2}]}],"window":["95:1","95:2","95:3","95:4","95:5","95:6","95:7","95:8"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"95:3","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":20,"unstructured_record_count":0},"identity":{"ayah_ref":"95:3","lane":"micro","linguistic_source_ref":"95:3","surface_ref":"95:3","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"95:3","target_tokens":[["Bu",["95:3:1"]],["güvenli",["95:3:3"]],["şehre",["95:3:2"]],["de",["95:3:1"]],["andolsun",["95:3:1","95:3:2","95:3:3"]]],"text":"Bu güvenli şehre de andolsun."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":8,"id":"s095-p01-001-008","label":"Whole surah","number":1,"refs":["95:1","95:2","95:3","95:4","95:5","95:6","95:7","95:8"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:3","source_type":"word_analysis","support_id":"sup_086ab3f2ae78e4190952","text":"{\"gloss_range\":\"the known city or bounded settled place; broader land and territory resonance remains under the local secure-city phrase\",\"prose\":\"{{ar:ٱلْبَلَدِ}} ({{tr:al-baladi}}) names what {{ar:هَٰذَا}} ({{tr:hādhā}}) points to and carries the genitive trace of the oath. Its definite singular form keeps the oath on one known city, while its head-noun role locks {{ar:ٱلْأَمِينِ}} ({{tr:al-amīni}}) into the same phrase. Lexically, the active local branch is bounded settled place: the word can range through city, land, territory, and residence, but here the demonstrative and security adjective select the inhabited secure-city sense. That still leaves spatial breadth; the oath is not a mere map label but a marked, settled ground, and the compact b-l-d sound profile helps the phrase move from open pointing into bounded place. As a noun-only anchor, it presents place as a given locus rather than as an event being performed. The noun also makes the oath sequence turn from produce (95:1) and mountain (95:2) into a social place, and it becomes the final spatial frame before the human-creation claim in 95:4. Its pairing with the security root recalls secure-city formulations (14:35; 2:126), while the local construction states the city as sworn object rather than petition; the same city term also stands beside the contrasting oath frame in 90:1-2.\",\"root_display\":\"{{ar:ب ل د}} ({{tr:b-l-d}})\",\"root_gloss_range\":\"bounded tract or place, inhabited land, settlement, residence and fixedness; other accepted root branches such as body marks, dullness, sky-place, and combat are not locally selected\",\"surface_display\":\"{{ar:ٱلْبَلَدِ}} ({{tr:al-baladi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:3:head-controls-adjective","source_type":"word_analysis","support_id":"sup_0931ed10bf9fb526d079","text":"{\"blocking_evidence\":null,\"headline\":\"head noun binds the final security adjective\",\"reader_payoff\":\"The reader sees the city and its security adjective as one grammatical oath object, not as a noun plus a loose comment.\",\"reason\":\"The adjective relation is strongly licensed, and the noun instance is definite, singular, genitive, and marked as having an adjective.\",\"representative_source_ids\":[\"QG-24a2aa5f\",\"QF-0e5b2e54\",\"QF-2ad787a3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:3:deictic-layered-phrase","source_type":"word_analysis","support_id":"sup_0dae307dc793770f8ddf","text":"{\"blocking_evidence\":null,\"headline\":\"pointing, naming, and qualifying build the oath object\",\"reader_payoff\":\"The reader sees the oath object built in layers: first pointing, then city-name, then security-quality.\",\"reason\":\"The local syntax supplies exactly the demonstrative, appositional noun, and adjective stack described by the rows.\",\"representative_source_ids\":[\"QT-2191a3da\",\"QT-249b3752\",\"QP-8bc96990\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:4:active-protector-metaphor","source_type":"word_analysis","support_id":"sup_1262d7c89736ec18084e","text":"{\"blocking_evidence\":null,\"headline\":\"active trust force personifies the city without replacing it\",\"reader_payoff\":\"The reader feels the city as trust-bearing and protector-like while still reading it literally as a place.\",\"reason\":\"The adjective can carry active reliability pressure, but attachment evidence keeps it grammatically dependent on the city noun.\",\"representative_source_ids\":[\"QS-a86bab88\",\"QS-b23d9869\",\"QS-b9437a2a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:2:appositional-oath-object","source_type":"word_analysis","support_id":"sup_2a26b886332772cd163b","text":"{\"blocking_evidence\":null,\"headline\":\"demonstrative begins the sworn object before case appears\",\"reader_payoff\":\"The reader notices that the oath first points, then lets the noun apposition make the referent and case visible.\",\"reason\":\"Attachment evidence strongly licenses {{ar:ٱلْبَلَدِ}} ({{tr:al-baladi}}) as apposition to the demonstrative and warns against adding an extra explanatory noun.\",\"representative_source_ids\":[\"QG-1281dfe3\",\"QG-86814899\",\"QG-9029d91d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:4:final-rhyme-closure","source_type":"word_analysis","support_id":"sup_2ae0276f8bb9bc744312","text":"{\"blocking_evidence\":null,\"headline\":\"final adjective seals meaning and rhyme\",\"reader_payoff\":\"The reader hears security and trust as the final acoustic note of the oath triad.\",\"reason\":\"The word is final in 95:3 and the row set links its ending with the surrounding oath-section cadence.\",\"representative_source_ids\":[\"QF-a3d2910f\",\"QT-c1b788ed\",\"QP-b18df03a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:4:pervasive-root-narrowed-to-adjective","source_type":"word_analysis","support_id":"sup_2ee2c6728c21cce88c16","text":"{\"blocking_evidence\":null,\"headline\":\"pervasive security root appears as a rare city adjective\",\"reader_payoff\":\"The reader notices a major Quranic root narrowed here into a compact quality assigned to a place.\",\"reason\":\"The contextual evidence shows the local form as an adjective group, while the CRITICAL row supplies the broader root-frequency salience.\",\"representative_source_ids\":[\"MS-74f2a518\",\"QI-30efb700\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:3:bounded-settled-place","source_type":"word_analysis","support_id":"sup_346d7fadf31febd07826","text":"{\"blocking_evidence\":null,\"headline\":\"bounded settled place is selected from a wider root field\",\"reader_payoff\":\"The reader notices that the word is a city in context while still carrying land and territory breadth inside the oath.\",\"reason\":\"V4 accepts the bounded-place branch for {{ar:ب ل د}} ({{tr:b-l-d}}), while the local demonstrative and adjective narrow the range to the inhabited secure city rather than unrelated branches.\",\"representative_source_ids\":[\"QS-03706608\",\"QS-3a6cbc4a\",\"QS-dfb8efcc\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:1","source_type":"word_analysis","support_id":"sup_40bd3cbf270978f51392","text":"{\"gloss_range\":\"connective oath particle that coordinates the third oath item while also licensing oath scope\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) opens the ayah as continuation and oath at once. It links the city phrase to the earlier sworn items and also licenses the genitive oath object that follows, so the reader hears neither a loose conjunction nor an isolated invocation. Its one-letter surface compresses the connector and the omitted oath verb, giving a quick pickup before the phrase slows into {{ar:هَٰذَا ٱلْبَلَدِ ٱلْأَمِينِ}} ({{tr:hādhā l-baladi l-amīni}}). Because the answer waits until 95:4, this particle carries the ayah across its boundary as the third oath object, moving from natural produce (95:1) and mountain (95:2) toward inhabited society.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:3:bounded-sound-profile","source_type":"word_analysis","support_id":"sup_45cc01c6e390cec71786","text":"{\"blocking_evidence\":null,\"headline\":\"sound marks the move into bounded place\",\"reader_payoff\":\"The reader hears a tighter consonantal profile as the phrase moves from open pointing into bounded place.\",\"reason\":\"The row describes a phonetic effect tied to the local surface sequence and it does not conflict with the grammatical evidence.\",\"representative_source_ids\":[\"QP-c743f092\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:4:adjective-agreement","source_type":"word_analysis","support_id":"sup_56d43b2501303f0a62da","text":"{\"blocking_evidence\":null,\"headline\":\"agreement makes security part of the oath object\",\"reader_payoff\":\"The reader notices that security is built into the sworn city phrase rather than appended as a separate comment.\",\"reason\":\"QAC marks a definite genitive qualitative adjective, and attachment evidence strongly licenses it as the adjective of the city noun.\",\"representative_source_ids\":[\"QG-320ba179\",\"QG-d69f7729\",\"QG-e77cb9df\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:1:third-oath-escalation","source_type":"word_analysis","support_id":"sup_5721bc13550b040ab8ac","text":"{\"blocking_evidence\":null,\"headline\":\"third oath item shifts into inhabited society\",\"reader_payoff\":\"The reader notices that the connector makes the city the next accumulated oath object after produce (95:1) and mountain (95:2).\",\"reason\":\"The ayah begins with the same boundary particle pattern and is explicitly read as another oath-series term.\",\"representative_source_ids\":[\"QT-5fb13542\",\"MT-30bee951\",\"QB-1b7ed19d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:4:same-surah-faith-echo","source_type":"word_analysis","support_id":"sup_57d58f8f38df61928a6b","text":"{\"blocking_evidence\":null,\"headline\":\"place-security anticipates believing persons\",\"reader_payoff\":\"The reader sees the root shift from a secure place in 95:3 to believing persons in 95:6.\",\"reason\":\"The rows cite the same-surah return in 95:6, and local grammar keeps the current instance as a place adjective.\",\"representative_source_ids\":[\"MI-41f2d4a9\",\"QE-76984d59\",\"QB-7ca524bd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:4:trust-faith-family","source_type":"word_analysis","support_id":"sup_5a23bfc0d6565b2e574c","text":"{\"blocking_evidence\":null,\"headline\":\"safety, entrusting, and faith compress into one adjective\",\"reader_payoff\":\"The reader notices that the city adjective draws on trust and entrustedness as well as absence of fear.\",\"reason\":\"The broader family is useful as semantic pressure, while the local noun phrase selects the qualitative city adjective.\",\"representative_source_ids\":[\"QS-bd295e56\",\"QS-e6ecb6e2\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:2","source_type":"word_analysis","support_id":"sup_5e7e2bd5db36866a217d","text":"{\"gloss_range\":\"proximal masculine singular demonstrative pointing to the immediately specified city\",\"prose\":\"{{ar:هَٰذَا}} ({{tr:hādhā}}) makes the final oath object start with pointing before naming. The demonstrative occupies the sworn-object position, but because its form is indeclinable, {{ar:ٱلْبَلَدِ}} ({{tr:al-baladi}}) supplies the audible genitive and identifies what is being pointed to. Its proximity makes the city a witnessed, known referent rather than a remote label, unlike the more directly named oath objects in 95:1 and 95:2. The lengthened deictic shape lets the phrase open outward before it narrows into the bounded city and its security qualifier.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:هَٰذَا}} ({{tr:hādhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:4:surah-bracket-echoes","source_type":"word_analysis","support_id":"sup_71824a6c6d3727e210a8","text":"{\"blocking_evidence\":null,\"headline\":\"security quality helps bracket the surah argument\",\"reader_payoff\":\"The reader notices security at the oath close connecting backward to the place sequence in 95:2 and forward to divine judgment in 95:8.\",\"reason\":\"The rows identify concrete intra-surah links, and the local adjective is the final qualifier before the oath answer.\",\"representative_source_ids\":[\"ME-7bb3688f\",\"QB-6aea33f4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:4:nasal-soft-landing","source_type":"word_analysis","support_id":"sup_718337884d526d431b71","text":"{\"blocking_evidence\":null,\"headline\":\"nasal ending softens the final landing\",\"reader_payoff\":\"The reader hears the city phrase close on a resonant security adjective rather than on the harder place noun.\",\"reason\":\"The phonetic rows are tied to the actual final surface form and reinforce the word's closure function.\",\"representative_source_ids\":[\"QP-f877cc9f\",\"MP-dc933fe0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:4:security-place-pair","source_type":"word_analysis","support_id":"sup_774b30de4623a3fb1bf9","text":"{\"blocking_evidence\":null,\"headline\":\"security adjective answers the city noun\",\"reader_payoff\":\"The reader notices the immediate noun-adjective pair where place and security define each other.\",\"reason\":\"The local phrase directly joins the city root with the security root, and contextual evidence supports the co-occurrence as a recognized pair including 14:35 and 2:126.\",\"representative_source_ids\":[\"QI-ceea9743\",\"QE-23bb2de2\",\"ME-ff2fd533\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:3:definite-genitive-apposition","source_type":"word_analysis","support_id":"sup_7a237fe72a7f70027d26","text":"{\"blocking_evidence\":null,\"headline\":\"known city noun identifies the demonstrative under oath case\",\"reader_payoff\":\"The reader notices that the noun both names the pointed referent and shows the oath-governed genitive that the demonstrative cannot display.\",\"reason\":\"QAC gives a definite genitive concrete noun, and attachment evidence strongly licenses it as apposition to the demonstrative in the oath phrase.\",\"representative_source_ids\":[\"QG-06d5c6ca\",\"QG-4aa44447\",\"QG-5e328a86\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:2:extended-pointing-sound","source_type":"word_analysis","support_id":"sup_7aace5cc7bed75e336df","text":"{\"blocking_evidence\":null,\"headline\":\"lengthened demonstrative opens the cadence\",\"reader_payoff\":\"The reader hears the pointing gesture linger before the phrase tightens into the noun and adjective.\",\"reason\":\"The surface form has the long deictic shape described by the CRITICAL rows and is positioned immediately after the clipped particle.\",\"representative_source_ids\":[\"QF-ac8f87ff\",\"QP-d13e34df\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:3:boundary-from-mountain-to-city","source_type":"word_analysis","support_id":"sup_7c6968f3ca765e1c288a","text":"{\"blocking_evidence\":null,\"headline\":\"bounded terrain becomes inhabited bounded place\",\"reader_payoff\":\"The reader sees the oath sequence escalate from delimited sacred terrain in 95:2 to the known secure city in 95:3.\",\"reason\":\"The bounded-place branch is locally coherent and is positioned immediately after the mountain oath in 95:2.\",\"representative_source_ids\":[\"QB-254bb1b7\",\"QY-3c66d3fc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:3:secure-city-formula","source_type":"word_analysis","support_id":"sup_7db254aa55d5dab9bf3c","text":"{\"blocking_evidence\":null,\"headline\":\"city and security form a recognized Quranic pair\",\"reader_payoff\":\"The reader recognizes the noun-adjective pair as participating in secure-city language known from 14:35 and 2:126.\",\"reason\":\"The collocation profile lists the security root as a top co-occurrence for the city root, and the local phrase directly joins the two.\",\"representative_source_ids\":[\"QI-a5f79952\",\"QI-c35738d9\",\"QE-5b709881\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:4:definite-phrase-closure","source_type":"word_analysis","support_id":"sup_802f35bb1e1a546bbad6","text":"{\"blocking_evidence\":null,\"headline\":\"definite adjective closes the known city phrase\",\"reader_payoff\":\"The reader hears the adjective lock to the noun through definiteness, genitive cadence, and recitational joining.\",\"reason\":\"The local adjective agrees with the noun, and the recitational observations reinforce that same grammatical link.\",\"representative_source_ids\":[\"QF-0045013e\",\"QF-18e4b85e\",\"QP-d2eaf212\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:3:cross-surah-city-oaths","source_type":"word_analysis","support_id":"sup_874ed92e003840fb4275","text":"{\"blocking_evidence\":null,\"headline\":\"same city term anchors other oath framing\",\"reader_payoff\":\"The reader notices that the city noun belongs to a wider oath pattern, including the contrasting oath frame in 90:1-2.\",\"reason\":\"The CRITICAL rows cite the same city term in another oath environment, and the contextual supplement includes 90:1 among the sampled references.\",\"representative_source_ids\":[\"QI-40f4cc52\",\"MI-aca0d76e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:2:proximal-known-city","source_type":"word_analysis","support_id":"sup_8f617991f3be5972ddf6","text":"{\"blocking_evidence\":null,\"headline\":\"proximity makes the city witnessed\",\"reader_payoff\":\"The reader feels the city as a present known referent, not as a general class of settlements.\",\"reason\":\"The masculine singular demonstrative is immediately resolved by the definite masculine noun that follows.\",\"representative_source_ids\":[\"QG-b4199f8e\",\"QG-ce0c9fe6\",\"MG-301f9dda\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:2:scene-shift-from-mountain","source_type":"word_analysis","support_id":"sup_9502930dda1ddf854cb5","text":"{\"blocking_evidence\":null,\"headline\":\"named sacred geography becomes witnessed city\",\"reader_payoff\":\"The reader sees the oath scene shift from the mountain in 95:2 to a proximate inhabited city in 95:3.\",\"reason\":\"The demonstrative is the surface signal by which the final oath object is located in immediate reference after the preceding mountain oath.\",\"representative_source_ids\":[\"QB-5f3bf613\",\"QB-dadba219\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:4","source_type":"word_analysis","support_id":"sup_95da1c6b7249f232edfc","text":"{\"gloss_range\":\"secure, trustworthy, reliable, and trust-bearing as a qualitative adjective of the city\",\"prose\":\"{{ar:ٱلْأَمِينِ}} ({{tr:al-amīni}}) completes the oath object as an adjective, not as a separate predicate. Its definiteness, genitive case, number, and gender agree with {{ar:ٱلْبَلَدِ}} ({{tr:al-baladi}}), so security belongs inside the sworn phrase itself. The adjective keeps both secure and trustworthy pressure: the city is safe and also reliable, almost protector-like, while the local noun frame keeps that force attached to place rather than turning it into a human belief verb. Its safety field also makes the city feel like a sanctuary toward which protection-seeking can move, and its trust field includes the ability to hold what is entrusted, while the local form remains a place adjective. This makes the secure-city formula declarative in 95:3 rather than petitionary as in 14:35, with the city-security pair also resonating with 2:126. The same adjective can mark trustworthiness across categories, including messenger figures (81:21; 44:18), but here that quality is assigned to the city. As the last word before the answer in 95:4, it is the oath triad's semantic and acoustic landing point; its final cadence ties back to the earlier oath endings, forward to the later human response of belief in 95:6, and onward to the closing judgment frame in 95:8.\",\"root_display\":\"{{ar:أ م ن}} ({{tr:ʾ-m-n}})\",\"root_gloss_range\":\"safety from fear, trust, reliability, protection, entrusting, and faith; local grammar selects a city adjective rather than a verbal belief action\",\"surface_display\":\"{{ar:ٱلْأَمِينِ}} ({{tr:al-amīni}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:4:grammar-meaning-sound-convergence","source_type":"word_analysis","support_id":"sup_9bff5a8e95fb8a75695f","text":"{\"blocking_evidence\":null,\"headline\":\"agreement, security meaning, and rhyme converge\",\"reader_payoff\":\"The reader sees the final word as the place where grammatical qualification, security meaning, and oath-section sound meet.\",\"reason\":\"The convergence row is supported by local agreement, adjective meaning, and final-word position.\",\"representative_source_ids\":[\"QY-bfd9478f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:3:nominal-place-anchor","source_type":"word_analysis","support_id":"sup_a2b16f8809b13e09d41b","text":"{\"blocking_evidence\":null,\"headline\":\"noun-only deployment makes place a given locus\",\"reader_payoff\":\"The reader notices that the root contributes placehood as a nominal anchor rather than a narrated event.\",\"reason\":\"The local form is a noun, and the contextual role profile treats the exact root/form as a noun field rather than a verbal frame.\",\"representative_source_ids\":[\"MS-ea5ef3d6\",\"QF-b0ae3183\",\"QH-d71900f5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:4:cross-category-trustworthiness","source_type":"word_analysis","support_id":"sup_ad55666bbc9b6b7f117e","text":"{\"blocking_evidence\":null,\"headline\":\"same adjective can qualify messengers and city\",\"reader_payoff\":\"The reader notices that trustworthiness can be applied across categories, including angel, prophet, and place (81:21; 44:18).\",\"reason\":\"The cross-reference is concrete and does not require replacing the local city adjective with a personal referent.\",\"representative_source_ids\":[\"MI-bbfcf4c1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"95:3:3:2","source_type":"qac_morpheme","support_id":"sup_b34b5cc597febf8229dc","text":"{\"lemma_ar\":\"أَمِين\",\"morph_features\":\"STEM|POS:ADJ|LEM:>amiyn|ROOT:Amn|MS|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"ADJ\",\"qac_ref\":\"95:3:3:2\",\"qac_word_ref\":\"95:3:3\",\"root_ar\":\"ء م ن\",\"surface_ar\":\"أَمِينِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:4:formula-declared-not-requested","source_type":"word_analysis","support_id":"sup_b4c2b6a68094cafa3587","text":"{\"blocking_evidence\":null,\"headline\":\"secure-city formula becomes an established attribute\",\"reader_payoff\":\"The reader sees 95:3 present the secure city as already characterized by security, unlike the request for security in 14:35.\",\"reason\":\"The CRITICAL rows cite 14:35, and the local syntax makes security a definite adjective inside the oath object.\",\"representative_source_ids\":[\"QI-5bc7fdca\",\"QI-d1d7a3d6\",\"MI-8cfca0ad\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:1:delayed-oath-answer","source_type":"word_analysis","support_id":"sup_b61f0abd1a2f96b07451","text":"{\"blocking_evidence\":null,\"headline\":\"boundary-spanning oath waits for its answer\",\"reader_payoff\":\"The reader sees 95:3 as the final sworn item whose answer arrives only in 95:4.\",\"reason\":\"The local evidence describes 95:3 as part of a multi-ayah oath whose response is in 95:4.\",\"representative_source_ids\":[\"QI-52830569\",\"QT-5bc96a3b\",\"QB-815796ba\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"95:3:2:2","source_type":"qac_morpheme","support_id":"sup_bf70a66bd6f7d5d573e1","text":"{\"lemma_ar\":\"بَلَد\",\"morph_features\":\"STEM|POS:N|LEM:balad|ROOT:bld|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"95:3:2:2\",\"qac_word_ref\":\"95:3:2\",\"root_ar\":\"ب ل د\",\"surface_ar\":\"بَلَدِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:4:secure-trustworthy-polysemy","source_type":"word_analysis","support_id":"sup_cc902467ec22fed8e473","text":"{\"blocking_evidence\":null,\"headline\":\"secure and trustworthy senses coexist for the city\",\"reader_payoff\":\"The reader hears the city as both protected and reliable, not merely safe in a flat spatial sense.\",\"reason\":\"No V4 guardrail rows are available for this root, and the local adjective relation allows the security and trustworthiness range claimed by the CRITICAL rows.\",\"representative_source_ids\":[\"QS-7eb1e9e8\",\"QS-a4909a1a\",\"MS-492b9de7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:2:deictic-fronting","source_type":"word_analysis","support_id":"sup_cdd261afc779ca6c08f0","text":"{\"blocking_evidence\":null,\"headline\":\"presence precedes the city name\",\"reader_payoff\":\"The reader notices that the city is introduced by presence before it is named, unlike the direct naming in 95:1-2.\",\"reason\":\"The demonstrative follows the opening oath particle and precedes the noun that specifies it.\",\"representative_source_ids\":[\"QT-08b6d646\",\"QT-b03782a9\",\"MT-501666fb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:3:oath-sequence-human-turn","source_type":"word_analysis","support_id":"sup_cf59882a6b7d2955dfdb","text":"{\"blocking_evidence\":null,\"headline\":\"settled city is the last spatial frame before the human claim\",\"reader_payoff\":\"The reader notices the oath sequence move from natural and sacred geography into inhabited society before 95:4 names the human being.\",\"reason\":\"The current ayah is the final oath object before 95:4, and its noun explicitly supplies the inhabited social locus.\",\"representative_source_ids\":[\"QT-50af4c40\",\"MI-14c15b31\",\"QB-7c462dc1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:1:oath-coordination","source_type":"word_analysis","support_id":"sup_d4a25681e73979303ecc","text":"{\"blocking_evidence\":null,\"headline\":\"coordination and oath force stay live together\",\"reader_payoff\":\"The reader notices that the opening particle both joins the oath chain and gives the city phrase sworn-object force.\",\"reason\":\"The word is a conjunction in QAC, while the attachment evidence marks a formulaic omitted oath verb and the following phrase as an oath-series term.\",\"representative_source_ids\":[\"QG-ce8e498b\",\"MG-d84ab2b2\",\"QS-7bc83093\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:4:postposed-valuing-qualifier","source_type":"word_analysis","support_id":"sup_d4f8c07352bc1b5e4cff","text":"{\"blocking_evidence\":null,\"headline\":\"delayed adjective turns location into valued location\",\"reader_payoff\":\"The reader experiences the phrase closing by valuation after the city has already been identified.\",\"reason\":\"The adjective follows its noun in the licensed adjective relation and specializes the secure-city field adjectivally.\",\"representative_source_ids\":[\"QT-5220beb2\",\"QE-0c844d98\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:4:protection-and-trust-field","source_type":"word_analysis","support_id":"sup_e06b5dcc4e4b69c0d121","text":"{\"blocking_evidence\":null,\"headline\":\"derivational safety field colors the place adjective\",\"reader_payoff\":\"The reader senses the city as a place toward which safety and trust can move, while the local word remains an adjective.\",\"reason\":\"The derivative evidence supports safety and protection pressure, but the local surface is an adjective modifying a noun, not those derivative forms themselves.\",\"representative_source_ids\":[\"QS-8a319875\",\"QS-a25c7414\",\"QS-d1537a3d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:3:marked-ground-and-fixedness","source_type":"word_analysis","support_id":"sup_e904a74c155856c36670","text":"{\"blocking_evidence\":null,\"headline\":\"marked settled ground colors the city\",\"reader_payoff\":\"The reader feels the city as locatable settled ground, not as an abstract civic label.\",\"reason\":\"The fixedness and trace pressures can color the bounded-place image, but local grammar keeps the concrete city or territory branch primary.\",\"representative_source_ids\":[\"QS-2200bde5\",\"QS-d9e0b261\",\"MS-2546b29a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"95:3:1:compact-oath-onset","source_type":"word_analysis","support_id":"sup_f8a81dd2b04a5225538b","text":"{\"blocking_evidence\":null,\"headline\":\"one-letter onset compresses the oath entry\",\"reader_payoff\":\"The reader hears the ayah enter quickly through one particle before expanding into the longer city phrase.\",\"reason\":\"The surface is a single-letter proclitic, and the attachment evidence licenses the oath verb as omitted rather than explicit.\",\"representative_source_ids\":[\"QF-094188e9\",\"QP-fd3805d9\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَهَٰذَا ٱلْبَلَدِ ٱلْأَمِينِ","ayah_ref":"95:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000054/B001","root_000148/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000148","role":"The bounded-land image supplies an enclosure whose inside/outside distinction can carry protection.","root":"ب ل د","source_ref":"95:3","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000054","role":"Settled security and trust supply both freedom from fear and the reliable relation that makes the enclosure safe.","root":"ء م ن","source_ref":"95:3","source_word_indices":["3"]}],"changed_reading":{"after":"A bounded domain whose very boundary organizes a settled relation of protection and trust.","before":"A demonstrative reference to a familiar city described as safe."},"confidence":"strong","focus_anchor":"The noun at word 2 is directly qualified by the adjective at word 3.","mechanism":"A bounded tract is not merely located; settled security and trust become the condition governing its enclosure. Boundary and confidence therefore form one spatial-social mechanism.","model_id":"base_bounded_safe_domain"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_bounded_safe_domain","source_type":"hft","support_id":"sup_621cb79fb9717cb35bde","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَهَٰذَا ٱلْبَلَدِ ٱلْأَمِينِ","ayah_ref":"95:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000054/B001","root_000148/B009"],"payload":{"activation_trace":[{"branch_id":"B009","mapped_root_id":"root_000148","role":"Residence and staying supply the durable human occupancy over which a civic trust can operate.","root":"ب ل د","source_ref":"95:3","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000054","role":"The trusted or trustworthy thing image turns the adjective into a custodial capacity, not only a condition of being unharmed.","root":"ء م ن","source_ref":"95:3","source_word_indices":["3"]}],"changed_reading":{"after":"The city is a reliable civic custodian that makes residence and entrusted relations possible.","before":"The city is the passive recipient of safety."},"confidence":"medium","focus_anchor":"The resident-place branch of the noun and the trustworthy-or-trusted scope of the adjective meet in the same nominal phrase.","mechanism":"The adjective can be agentive rather than merely passive: the city is not only protected but acts as a trustee that reliably holds residents, goods, promises, and safe-conduct.","model_id":"base_city_as_trustee"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_city_as_trustee","source_type":"hft","support_id":"sup_30cbc122583b0600c80a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَهَٰذَا ٱلْبَلَدِ ٱلْأَمِينِ","ayah_ref":"95:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000054/B001","root_000148/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000148","role":"The chest and front-hollow image supplies a bodily enclosure and central receiving space.","root":"ب ل د","source_ref":"95:3","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000054","role":"Heart-settling security supplies the composure housed in that chest-like center.","root":"ء م ن","source_ref":"95:3","source_word_indices":["3"]}],"changed_reading":{"after":"The external city also resonates as a protected chest-space in which fear can settle into trust.","before":"The demonstrative points only to an external urban location."},"confidence":"exploratory","focus_anchor":"A direct branch of the noun names the chest and front hollow, while the adjective supplies heart-settling security.","mechanism":"The place can be carried as an embodied center: a chest-like front or hollow within which composure settles. Geographic enclosure and bodily interior coexist without requiring either to erase the other.","model_id":"base_embodied_center"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_embodied_center","source_type":"hft","support_id":"sup_5bb61778b3096b4acc24","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَهَٰذَا ٱلْبَلَدِ ٱلْأَمِينِ","ayah_ref":"95:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000054/B001","root_000148/B012"],"payload":{"activation_trace":[{"branch_id":"B012","mapped_root_id":"root_000148","role":"The ostrich nesting-place image supplies an exposed ground hollow that holds vulnerable life.","root":"ب ل د","source_ref":"95:3","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000054","role":"Security supplies the protection that lets vulnerability remain in an otherwise exposed nest.","root":"ء م ن","source_ref":"95:3","source_word_indices":["3"]}],"changed_reading":{"after":"The city can also be imagined as a modest ground refuge made trustworthy enough to cradle exposed and vulnerable life.","before":"The city is secure because it is massive, enclosed, and strong."},"confidence":"exploratory","containment":"This is surprising because an ostrich nesting scrape is far from the ordinary urban sense, but it remains directly anchored in a packet branch of the focus noun and in the focus adjective's security branch. Render it only as an ecological analogy for protected vulnerability, not as a replacement translation.","focus_anchor":"The focus noun has an ostrich-nest branch and is immediately qualified by settled security.","outlier_id":"outlier_nesting_refuge"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:outlier_nesting_refuge","source_type":"hft","support_id":"sup_6721a5fa2bc4fd926de8","trust":"legacy_unbound"}]}
</lane_packet_json>
