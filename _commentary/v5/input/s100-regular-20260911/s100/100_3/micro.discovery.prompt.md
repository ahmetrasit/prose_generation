# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **100:3**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s100-regular-20260911/s100/100_3/micro.discovery.json` and modify nothing
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
  "ayah_ref": "100:3",
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
{"analysis_context":{"analysis_id":"s100-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"100:3","host_surah":100,"lane_context_refs":[],"ordered_context_refs":["100:0","100:1","100:2","100:4","100:5","100:6","100:7","100:8","100:9","100:10","100:11","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Yalın gün başlangıcıdır; içecek, lamba, güzellik, uyku ve durum değişimi anlamları dışarıda kalır.","branch_kind":"bare","branch_ref":"root_000839/B001","candidate_links":[{"candidate_id":"cand_0c7b074eb10aaa08cdf2","lane":"micro"},{"candidate_id":"cand_6e9ffb2a8a39f1b2cee0","lane":"micro"},{"candidate_id":"cand_f4cd976dd5b09f55f1e3","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صُبْح","morph_features":"STEM|POS:T|LEM:SuboH|ROOT:SbH|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"100:3:2:1","qac_word_ref":"100:3:2","surface_ar":"صُبْحًا"}],"gloss":"günün ilk aydınlığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, geceden sonraki ilk gündüz ışığı ve günün başlangıcıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Her günün ilk bölümü, bu ana girme ve bu anın yeri aynı zaman alanına bağlıdır."}}],"root_ar":"ص ب ح","root_id":"root_000839","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Günün başlangıcı, tanın belirdiği erken gündüz bölümü ve buna bağlı zaman ya da yer kullanımları için uygundur.","boundary_detail":"Yalın gün başlangıcıdır; içecek, lamba, güzellik, uyku ve durum değişimi anlamları dışarıda kalır.","concept_gloss":"günün ilk aydınlığı","contextual_glosses":[{"applicability":"İlk ışığın belirmesi anlatıldığında doğal ve kısa bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Her günün ilk bölümü, bu ana girme ve yer anlamlarını daraltır.","preserves":"Günün başındaki ilk aydınlık anını korur."},"facet_ids":["F001"],"text":"tan vakti","usage_role":"contextual"},{"applicability":"Zaman diliminin kendisi öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İlk ışık, girme ve yer uzantılarını tek başına açıkça vermez.","preserves":"Günün başı olma değerini korur."},"facet_ids":["F001","F002"],"text":"günün başlangıcı","usage_role":"general"}],"definition":"Geceden sonra günün aydınlanmaya başladığı ve günün başlangıcı sayılan ilk bölüm. Bu alana, o zamana girme ve o zamanda bulunulan yer ya da an da bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, geceden sonraki ilk gündüz ışığı ve günün başlangıcıdır."},{"facet_id":"F002","role":"extension","statement":"Her günün ilk bölümü, bu ana girme ve bu anın yeri aynı zaman alanına bağlıdır."}],"identity_rationale":"Kaynak ifadesi bu dalı geceden sonra beliren ilk gündüz ışığı, günün başlangıcı ve bu başlangıca ait zaman ya da yer çevresinde toplar. Bu nedenle tanım içecek, lamba, renk veya güzellik dallarını içeri almadan günün ilk aydınlık bölümü üzerine kurulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tan ve günün ilk aydınlığı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"günün başı, gecenin karşıtı olan erken gündüz"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"her günün ilk bölümü"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"günün ilk bölümüne girme ya da o an"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"günün ilk bölümüne varılan yer ya da o an"}],"lexicalization_note":"Yalın dal olduğu için tanım herhangi bir kalıba bağlı olmayan gün başlangıcı ve ilk aydınlık anlamını verir.","neighbor_coverage_note":"Bütün adaylar erken gün, hareket, içecek, savaş, ışık aracı, renk, uyku, hayvan ve oluş alanları bakımından gözden geçirildi; yalnız sınırı belirginleştiren ilişkiler yayınlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal günün başlangıcı ve ona bağlı zaman kullanımlarını adlandırır; komşu dal gecenin sonunda beliren ışığın yarılma ve ayırt edilme yönünü öne çıkarır.","focus_only":"Günün ilk bölümü, bu ana girme ve bu anın yeri gibi uzantıları da kapsar.","gloss":"tan ışığı","neighbor_only":"Gecenin sonunda yarılan ilk ışık ve tan ayrımı daha belirgindir.","neighbor_ref":"root_001132/B002","relation_type":"near_synonym","shared_zone":"İki dal da geceden sonra başlayan ilk aydınlığı paylaşır."},{"boundary_match":"field_only","distinction":"Odak dal zamanı adlandırır; komşu dal o zamanda yapılan içme, yeme veya sulama işini ve bunlara ait kapları adlandırır.","focus_only":"Zaman diliminin kendisini ve ilk doğal ışığı adlandırır.","gloss":"erken içecek","neighbor_only":"Günün başında içme, yeme veya hayvana su verme eylemidir.","neighbor_ref":"root_000839/B003","relation_type":"same_field","shared_zone":"İki dal da günün başlangıcıyla zaman ilişkisi kurar."},{"boundary_match":"field_only","distinction":"Odak dal zamanın doğal aydınlanmasıdır; komşu dal insanın kullandığı ışık aracı ve benzetilmiş göksel ışıklar alanındadır.","focus_only":"Doğal gün ışığının başlangıcını anlatır.","gloss":"ışık veren lamba","neighbor_only":"Aydınlatma aracı, onun konduğu yer veya gök cisimlerinin ışıklarıdır.","neighbor_ref":"root_000839/B005","relation_type":"same_field","shared_zone":"İki dalda da aydınlık ve ışık alanı vardır."}],"source_summary":"Kaynaklar anlamı günün ilk aydınlığı, günün başlangıcı ve gecenin karşısına konan erken gündüz bölümü olarak verir. Aynı ortak alanda bu zamana girme, bu zamanın kendisi ve bu zamanda bulunulan yer de yer alır."},"support_links":["sup_06261e4e0407d44d3182","sup_a4a1c9feb353945848d7","sup_d3b888abd29b6646cdfa"]},{"boundary":"Günün başında gelme, getirme ve esenlik sözüyle sınırlıdır; savaş baskını B004 dalında tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_000839/B002","candidate_links":[{"candidate_id":"cand_cd3328592ade1b49eed6","lane":"micro"},{"candidate_id":"cand_b1791aab2dede7d650cc","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صُبْح","morph_features":"STEM|POS:T|LEM:SuboH|ROOT:SbH|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"100:3:2:1","qac_word_ref":"100:3:2","surface_ar":"صُبْحًا"}],"gloss":"günün başında gelmek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, birine günün ilk bölümünde gelme eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Su gibi bir şeyi topluluğa günün ilk bölümünde getirme kalıba bağlı bir gerçekleşmedir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Günün başına özgü esenlik sözü söyleme aynı zaman bağından gelen bir kullanımdır."}}],"root_ar":"ص ب ح","root_id":"root_000839","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Birine erken gündüzde varma, aynı zamanda bir şeyi getirme veya o zamana bağlı esenlik sözü söyleme bağlamları için uygundur.","boundary_detail":"Günün başında gelme, getirme ve esenlik sözüyle sınırlıdır; savaş baskını B004 dalında tutulur.","concept_gloss":"günün başında gelmek","contextual_glosses":[{"applicability":"Yalın gelme fiili için, alıcıya veya yere varış anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Su getirme ve esenlik sözü söyleme özel kullanımlarını dışarıda bırakır.","preserves":"Günün başında gerçekleşen varma eylemini korur."},"facet_ids":["F001"],"text":"erken gündüzde varmak","usage_role":"general"},{"applicability":"Su nesnesiyle kurulan kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Getirme eylemi, su nesnesi ve gün başı koşulu korunur."},"facet_ids":["F002"],"text":"günün başında su getirmek","usage_role":"contextual"}],"definition":"Bir kişi veya topluluğa günün ilk bölümünde gelme ya da bir şeyi o zamanda getirme eylemi. Aynı zamana bağlı esenlik sözü söyleme kullanımı, çekirdeğe bağlı özel bir kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, birine günün ilk bölümünde gelme eylemidir."},{"facet_id":"F002","role":"specialization","statement":"Su gibi bir şeyi topluluğa günün ilk bölümünde getirme kalıba bağlı bir gerçekleşmedir."},{"facet_id":"F003","role":"associated_use","statement":"Günün başına özgü esenlik sözü söyleme aynı zaman bağından gelen bir kullanımdır."}],"identity_rationale":"Kaynak ifadesi birine günün ilk bölümünde gelmeyi, bu zamanda su getirmeyi ve aynı zamana bağlı esenlik sözünü destekler. Provisional açıklamadaki atla savaşta gitme ögesi bu dalın kaynak ifadesinde değil, ayrı baskın dalında yer aldığı için tanım onu dışarıda bırakır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"ona günün başında geldim ya da o bana günün başında geldi"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"onlara günün başında su getirdim"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"günün başına özgü esenlik sözü"}],"lexicalization_note":"Yalın fiil ile su getirme ve esenlik sözü kalıpları ayrılır; kalıp anlamları yalın anlama genellenmez.","neighbor_coverage_note":"Gelme, gece hareketi, su, savaş, içecek ve kökün öteki dalları gözden geçirildi; yayınlananlar zaman koşulu veya eylem türü sınırını en açık gösterenlerdir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genel gelme eylemini günün başına bağlar ve su getirme ile esenlik sözünü içerir; komşu dal zaman koşulu taşımayan geniş gelme alanıdır.","focus_only":"Varışın günün ilk bölümünde olması zorunludur.","gloss":"gelmek","neighbor_only":"Gelme ve ulaşma zaman koşulu olmadan genel biçimde anlatılır.","neighbor_ref":"root_000009/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da birine veya bir yere varma eylemi vardır."},{"boundary_match":"field_only","distinction":"Odak dal sosyal veya taşıma amaçlı gelişleri kapsar; komşu dal savaş ve baskın sahnesine bağlıdır.","focus_only":"Sıradan varma, getirme veya esenlik sözü söyleme eylemidir.","gloss":"erken baskın","neighbor_only":"Savaş bağlamında atla erken baskın ve yardım çağrısı içerir.","neighbor_ref":"root_000839/B004","relation_type":"same_field","shared_zone":"İki dal da günün başında bir yere yönelme ile ilişkilidir."}],"source_summary":"Kaynaklar dalı günün ilk bölümünde birine gelme üzerine kurar. Aynı ortak alanda o zamanda su getirme ve karşılaşmada gün başına bağlı esenlik dileme kullanımları da yer alır."},"support_links":["sup_2955648f213d1d0ae095","sup_feb6fc0376d933cc80e4"]},{"boundary":"Erken gündüzde içme, yeme, sulama ve kap alanıdır; günün ilk aydınlığı ve lamba anlamları ayrı tutulur.","branch_kind":"bare","branch_ref":"root_000839/B003","candidate_links":[{"candidate_id":"cand_cd3328592ade1b49eed6","lane":"micro"},{"candidate_id":"cand_d0d12a26184bc0eaf69c","lane":"micro"},{"candidate_id":"cand_186caec22cfe3806faaf","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صُبْح","morph_features":"STEM|POS:T|LEM:SuboH|ROOT:SbH|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"100:3:2:1","qac_word_ref":"100:3:2","surface_ar":"صُبْحًا"}],"gloss":"günün başındaki içecek ve içme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, günün ilk bölümünde içme ve kimi kullanımlarda yeme eylemidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı zaman diliminde hayvana su verme bu çekirdeğin sulama yönüdür."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İçilen şey, içiren kişi ve bu işte kullanılan kaplar bağlı kullanımlardır."}}],"root_ar":"ص ب ح","root_id":"root_000839","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Erken gündüzde içme, yeme, hayvan sulama, içilen şey ve buna ait kap bağlamlarını birlikte karşılar.","boundary_detail":"Erken gündüzde içme, yeme, sulama ve kap alanıdır; günün ilk aydınlığı ve lamba anlamları ayrı tutulur.","concept_gloss":"günün başındaki içecek ve içme","contextual_glosses":[{"applicability":"İçilen şey veya içme payı öne çıktığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yeme, içme eylemi, sulama ve kap kullanımlarını dışarıda bırakır.","preserves":"Günün başında içilen şey anlamını korur."},"facet_ids":["F001","F003"],"text":"erken gündüz içeceği","usage_role":"general"},{"applicability":"Hayvanlara su verme kullanımı için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sulama eylemi ve gün başı koşulu korunur."},"facet_ids":["F002"],"text":"günün başında su vermek","usage_role":"contextual"}],"definition":"Günün ilk bölümünde içme veya yeme eylemi, bu zamanda içirilen ya da içilen şey ve hayvana aynı zamanda su verme işi. İçme için kullanılan kaplar ve içme öncesi oyalanma bu alana bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, günün ilk bölümünde içme ve kimi kullanımlarda yeme eylemidir."},{"facet_id":"F002","role":"extension","statement":"Aynı zaman diliminde hayvana su verme bu çekirdeğin sulama yönüdür."},{"facet_id":"F003","role":"associated_use","statement":"İçilen şey, içiren kişi ve bu işte kullanılan kaplar bağlı kullanımlardır."}],"identity_rationale":"Kaynak ifadesi dalı günün ilk bölümünde içme, yeme, hayvana su verme ve bu eylemlerde kullanılan içecek ya da kap çevresinde kurar. Bu anlam gün başlangıcıyla zaman ilişkisi taşır, fakat çekirdeği beslenme ve içirme eylemidir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"günün başında içme ya da yeme; o vakitte içilen şey"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"ona günün başı içeceğini verdim"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"günün başında içti"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"günün başı içeceğini içmiş kimse"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"günün başı içeceğinin verildiği kap"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"günün başında içmek için kullanılan kadehler"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"günün başı içeceğinden önce oyalanılan şey"}],"lexicalization_note":"Yalın dal olduğu için tanım tek bir kalıba bağlanmadan erken gündüzde içme ve beslenme alanını kapsar.","neighbor_coverage_note":"İçme, su verme, yemek, kap, zaman ve kökün öteki dalları karşılaştırıldı; yalnız eylem türü veya zaman koşulu bakımından öğretici olan ayrımlar bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal erken gündüz koşulu ve içecek öğünü çevresiyle sınırlıdır; komşu dal içirme ve su sağlama eylemini genel olarak verir.","focus_only":"İçme veya su verme günün ilk bölümüne bağlıdır ve yiyecek ya da kap uzantıları da bulunur.","gloss":"su vermek","neighbor_only":"Su verme veya içirme zaman koşulu olmadan genel eylemdir.","neighbor_ref":"root_000722/B001","relation_type":"near_neighbor","shared_zone":"İki dal da birine veya hayvana içilecek şey vermeyi paylaşır."},{"boundary_match":"partial","distinction":"Odak dal erken gündüz içeceği ve kimi yeme kullanımıdır; komşu dal geç gün yemeği ve otlatma düzenine bağlıdır.","focus_only":"Günün ilk bölümündeki içme, yeme veya sulamadır.","gloss":"akşam yemeği","neighbor_only":"Günün geç bölümündeki yemek ve hayvan otlatma alanındadır.","neighbor_ref":"root_001017/B005","relation_type":"near_neighbor","shared_zone":"İki dal da günün belirli bölümüne bağlı beslenme eylemi kurar."},{"boundary_match":"thematic_only","distinction":"Odak dal zaman içinde yapılan beslenme ve sulama işidir; komşu dal bu işin gerçekleştiği gün başlangıcıdır.","focus_only":"Bu zamanda yapılan içme, yeme veya sulama işini adlandırır.","gloss":"günün ilk aydınlığı","neighbor_only":"Zaman diliminin kendisini adlandırır.","neighbor_ref":"root_000839/B001","relation_type":"thematic","shared_zone":"B003 dalındaki eylem B001 dalının zamanında gerçekleşir."}],"source_summary":"Kaynaklar anlamı günün ilk bölümünde içme üzerine toplar ve kimi anlatımlarda yeme ile hayvan sulamayı da aynı alana ekler. İçilen şey, içiren kişi, kap ve içme öncesindeki küçük oyalanma da bu ortak erken gündüz beslenme sahnesine bağlanır."},"support_links":["sup_826d14e70aa61f73702c","sup_fd5a5122ca86f0459b2b","sup_feb6fc0376d933cc80e4"]},{"boundary":"Savaşta erken baskın ve yardım çağrısıdır; sıradan gelme, içecek ve günün kendisi ayrı dallardır.","branch_kind":"mixed_non_bare","branch_ref":"root_000839/B004","candidate_links":[{"candidate_id":"cand_f44be94b687673187adf","lane":"micro"},{"candidate_id":"cand_a8a61d657d3a0abe682d","lane":"micro"},{"candidate_id":"cand_c351588bd21c2fecc21d","lane":"micro"},{"candidate_id":"cand_32f991bec03f6d64e758","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صُبْح","morph_features":"STEM|POS:T|LEM:SuboH|ROOT:SbH|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"100:3:2:1","qac_word_ref":"100:3:2","surface_ar":"صُبْحًا"}],"gloss":"günün başında baskın","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, günün ilk bölümünde yapılan savaş baskını veya düşmana varıştır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Atla veya savaş gücüyle erkenden gitme bu baskın sahnesinin özel gerçekleşmesidir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Baskın anında söylenen yardım çağrısı aynı olay çerçevesine bağlıdır."}}],"root_ar":"ص ب ح","root_id":"root_000839","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Savaşta erken varış, düşmana baskın, baskın günü ve bu sahnedeki yardım çağrısı için uygundur.","boundary_detail":"Savaşta erken baskın ve yardım çağrısıdır; sıradan gelme, içecek ve günün kendisi ayrı dallardır.","concept_gloss":"günün başında baskın","contextual_glosses":[{"applicability":"Olay gününü veya baskın vaktini adlandıran kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Baskın olayı ve gün başı koşulu korunur."},"facet_ids":["F001"],"text":"erken baskın günü","usage_role":"contextual"},{"applicability":"Savaş fiili anlatıldığında doğal bir eylem karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Baskın günü adı ve yardım çağrısı kullanımını dışarıda bırakır.","preserves":"Erken zamanda düşmana yönelen saldırı eylemini korur."},"facet_ids":["F001","F002"],"text":"günün başında saldırmak","usage_role":"general"}],"definition":"Savaş bağlamında günün ilk bölümünde düşmana yönelme veya baskın yapma eylemi ve bu olayın günü. Aynı sahnede kullanılan yardım çağrısı, baskın zamanına bağlı bir kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, günün ilk bölümünde yapılan savaş baskını veya düşmana varıştır."},{"facet_id":"F002","role":"specialization","statement":"Atla veya savaş gücüyle erkenden gitme bu baskın sahnesinin özel gerçekleşmesidir."},{"facet_id":"F003","role":"associated_use","statement":"Baskın anında söylenen yardım çağrısı aynı olay çerçevesine bağlıdır."}],"identity_rationale":"Kaynak ifadesi dalı günün ilk bölümünde yapılan savaş baskını, atla erkenden varma ve bu sahneye bağlı yardım çağrısı çevresinde kurar. Bu, sıradan gün başı gelişiyle ilişkili olsa da savaş ve baskın koşulu dalın belirleyici sınırıdır.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"günün başındaki baskın günü"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"savaşta onlara günün başında atla vardık"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"tehlike anında söylenen yardım çağrısı"}],"lexicalization_note":"Eşdizimler ile savaş fiili birlikte gelir; tanım savaş bağını korur ve bunu sıradan gelme anlamına yaymaz.","neighbor_coverage_note":"Saldırı, savaş aracı, keşif, hızlı koşu, sıradan gelme ve kökün öteki dalları değerlendirildi; yayınlanan ayrımlar savaş koşulunu en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal saldırıyı erken gündüz koşuluna bağlar; komşu dal saldırı ve hız değerini daha genel tutar.","focus_only":"Baskın günün ilk bölümünde gerçekleşir ve buna bağlı çağrı vardır.","gloss":"saldırı","neighbor_only":"Saldırı ve hızlı itiş zaman koşulu olmadan genel savaş hareketidir.","neighbor_ref":"root_001112/B006","relation_type":"near_neighbor","shared_zone":"İki dal da düşmana yönelen saldırı ve baskın alanını paylaşır."},{"boundary_match":"partial","distinction":"Odak dal savaş gününü, atla varışı ve çağrıyı birlikte tutar; komşu dal daha çok beklenmedik erken varış ve baskın yönünü öne çıkarır.","focus_only":"Baskın günü ve yardım çağrısı da kapsanır.","gloss":"erken baskın","neighbor_only":"Gaflet anında erken baskına uğratma yönü özellikle belirtilir.","neighbor_ref":"root_000269/B005","relation_type":"near_synonym","shared_zone":"İki dal da günün başında yapılan baskını anlatır."},{"boundary_match":"field_only","distinction":"Odak dalda varış saldırı olayıdır; komşu dalda varış sosyal veya taşıma amaçlıdır.","focus_only":"Savaşta düşmana erken baskın yapmayı anlatır.","gloss":"erken geliş","neighbor_only":"Savaş dışı gelme, su getirme veya esenlik sözü eylemidir.","neighbor_ref":"root_000839/B002","relation_type":"same_field","shared_zone":"İki dal da günün başında bir yere varma fikrine dokunur."}],"source_summary":"Kaynaklar dalı günün ilk bölümüne bağlanan savaş günü ve baskın eylemi olarak verir. Aynı anlatımda atla erkenden varma ve baskın sırasında kullanılan yardım çağrısı, çekirdeğe bağlı savaş sahnesi unsurlarıdır."},"support_links":["sup_676ab9ce38ab7596ff3d","sup_6a8ac57b6f912566a6a4","sup_99d1441af33b566c0ef7","sup_ede12c0b4743228f42e3"]},{"boundary":"Lamba, kandil yeri ve göksel ışıklar alanıdır; içecek kabı ve doğal gün başlangıcı ayrı tutulur.","branch_kind":"bare","branch_ref":"root_000839/B005","candidate_links":[{"candidate_id":"cand_0c7b074eb10aaa08cdf2","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صُبْح","morph_features":"STEM|POS:T|LEM:SuboH|ROOT:SbH|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"100:3:2:1","qac_word_ref":"100:3:2","surface_ar":"صُبْحًا"}],"gloss":"ışık veren lamba","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, fitil veya benzeri araçla ışık veren lambadır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Lambanın konduğu yer, taşıyıcı düzenek ve yakıt olarak kullanılan şey aynı alana bağlıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gök cisimlerinin belirgin ışıkları lamba benzeri aydınlık işaretleri olarak genişler."}}],"root_ar":"ص ب ح","root_id":"root_000839","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Lamba, lambalık, aydınlatma gereci ve gök cismi ışığına genişleyen kullanımlar için çekirdek karşılıktır.","boundary_detail":"Lamba, kandil yeri ve göksel ışıklar alanıdır; içecek kabı ve doğal gün başlangıcı ayrı tutulur.","concept_gloss":"ışık veren lamba","contextual_glosses":[{"applicability":"Fitilli veya yağlı ışık aracı bağlamında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Lambanın konduğu yer ve gök ışıkları uzantısını daraltır.","preserves":"Işık veren araç anlamını korur."},"facet_ids":["F001"],"text":"kandil","usage_role":"general"},{"applicability":"Gök cisimlerinin belirgin ışıkları anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Göksel ışık uzantısı korunur."},"facet_ids":["F003"],"text":"yıldız ışıkları","usage_role":"contextual"}],"definition":"Işık veren araç, onun konduğu ya da taşındığı düzenek ve aydınlatmak için kullanılan şey. Gök cisimlerinin belirgin ışıkları da aynı aydınlatma alanının genişletilmiş kullanımıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, fitil veya benzeri araçla ışık veren lambadır."},{"facet_id":"F002","role":"associated_use","statement":"Lambanın konduğu yer, taşıyıcı düzenek ve yakıt olarak kullanılan şey aynı alana bağlıdır."},{"facet_id":"F003","role":"extension","statement":"Gök cisimlerinin belirgin ışıkları lamba benzeri aydınlık işaretleri olarak genişler."}],"identity_rationale":"Kaynak ifadesi bu dalı ışık veren araç, fitilli ışığın konduğu yer veya gereci ve gök cisimlerinin ışıkları çevresinde toplar. Günün ilk aydınlığıyla görüntüsel bağ kurulabilir, fakat dalın tanımı insan yapımı ışık aracı alanında kalır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"lamba, kandil ya da lambalık"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"lambanın kendisi"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"onunla ışık yakmak ya da onu yakıt yapmak"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"gök cisimlerinin ışıkları"}],"lexicalization_note":"Yalın dal olduğu için tanım belirli bir kalıba bağlanmadan ışık aracı ve ona bağlı yer veya yakıt kullanımını kapsar.","neighbor_coverage_note":"Lamba, ışık, fitil, parlama, gök cismi, içecek kabı ve kökün öteki dalları değerlendirildi; nesne işlevini netleştiren ayrımlar yayınlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli lamba adı, lambalık ve gök ışıkları uzantısıyla sınırlıdır; komşu dal ışık veren veya aydınlık olan şeyleri daha genel kapsar.","focus_only":"Lambanın konduğu yer ve gök ışıkları uzantısı da bulunur.","gloss":"aydınlatan lamba","neighbor_only":"Her tür parlak ışık ve aydınlatılmış nesne alanı daha geniştir.","neighbor_ref":"root_000693/B001","relation_type":"near_synonym","shared_zone":"İki dal da lamba ve ışık veren araç anlamını paylaşır."},{"boundary_match":"partial","distinction":"Odak dal ışığı üreten veya taşıyan nesneye bağlıdır; komşu dal nesneden bağımsız ışık ve parlaklık niteliğini adlandırır.","focus_only":"Işık aracını veya onun yerini adlandırır.","gloss":"ışık","neighbor_only":"Işığın kendisini, aydınlanma niteliğini ve aydınlatma fiilini genel olarak anlatır.","neighbor_ref":"root_000920/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da aydınlatma ve ışık etkisi vardır."},{"boundary_match":"field_only","distinction":"Odak dal ışık üretme işlevine bağlıdır; komşu dal içme ve beslenme sahnesine bağlı kapları kapsar.","focus_only":"Aydınlatma aracı ve gök ışıklarıdır.","gloss":"içecek kabı","neighbor_only":"Günün başında içme ve içecek kaplarıdır.","neighbor_ref":"root_000839/B003","relation_type":"same_field","shared_zone":"Bazı biçimler kap ya da araç olarak yorumlanabilir."}],"source_summary":"Kaynaklar anlamı ışık veren lamba, lambanın konduğu yer veya düzeneği ve onunla aydınlatma eylemi çevresinde toplar. Bazı anlatımlar gök cisimlerinin ışıklarını aynı adlandırma alanına ekler ve adın parlak ya da kızıl görünüşle ilişkilendirildiğini belirtir."},"support_links":["sup_d3b888abd29b6646cdfa"]},{"boundary":"Renk, kızıllık ve güzel parlak görünüş alanıdır; gün başlangıcı ve lamba anlamları ayrı tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_000839/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"صُبْح","morph_features":"STEM|POS:T|LEM:SuboH|ROOT:SbH|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"100:3:2:1","qac_word_ref":"100:3:2","surface_ar":"صُبْحًا"}],"gloss":"kızılımsı parlak güzellik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, kızıllığa dayanan veya kızıllıkla toprak rengi arasında kalan renk niteliğidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Saçtaki güçlü kızıllık ve hayvan rengindeki kızılımsı ton özel gerçekleşmelerdir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yüz için güzel, aydınlık ve hoş görünüş değerine genişler."}}],"root_ar":"ص ب ح","root_id":"root_000839","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Renk niteliği, saç veya hayvan rengi ve yüz güzelliğine genişleyen parlak görünüş için uygundur.","boundary_detail":"Renk, kızıllık ve güzel parlak görünüş alanıdır; gün başlangıcı ve lamba anlamları ayrı tutulur.","concept_gloss":"kızılımsı parlak güzellik","contextual_glosses":[{"applicability":"Saç, hayvan veya renk niteliği öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yüz güzelliği ve parlak görünüş uzantısını daraltır.","preserves":"Kızıllığa yakın renk çekirdeğini korur."},"facet_ids":["F001","F002"],"text":"kızılımsı renk","usage_role":"general"},{"applicability":"Yüz niteliği bağlamında doğal ve açıklayıcıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yüz güzelliği ve parlak görünüş korunur."},"facet_ids":["F003"],"text":"güzel ve aydınlık yüz","usage_role":"contextual"}],"definition":"Kızıllığa yakın ya da kızıllıkla toprak rengi arasında bir renk niteliği; saç, hayvan ve benzeri varlıklarda görülen bu ton. Yüz için kullanıldığında aynı parlaklık alanı güzellik ve aydınlık görünüş değerine uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, kızıllığa dayanan veya kızıllıkla toprak rengi arasında kalan renk niteliğidir."},{"facet_id":"F002","role":"specialization","statement":"Saçtaki güçlü kızıllık ve hayvan rengindeki kızılımsı ton özel gerçekleşmelerdir."},{"facet_id":"F003","role":"extension","statement":"Yüz için güzel, aydınlık ve hoş görünüş değerine genişler."}],"identity_rationale":"Kaynak ifadesi dalı kızıllığa yakın renk, kızıllıkla toprak rengi arası ton, saçtaki güçlü kızıllık ve yüz güzelliği ya da parlak görünüş çevresinde toplar. Lexical-unit düzeyindeki metal parıltısı ayrıca çevrilir, fakat branch claim'in çekirdeği renk ve güzel parlak görünüş alanıdır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"kızıllıkla toprak rengi arası renk"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"kızılımsı ya da açık kestane renkte"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"güzel ve aydınlık yüzlü"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"saçtaki güçlü kızıllık"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"demir ve benzeri şeylerde parlaklık"}],"lexicalization_note":"Yalın renk adları ile yüz niteliği ve gözden geçirme birimi ayrılır; tanım bunları görünüş alanında tutar.","neighbor_coverage_note":"Güzellik, beyazlık, kızıllık, yüz parlaklığı, lamba ve gün ışığı adayları karşılaştırıldı; renk zemini veya nesne-nitelik sınırı belirgin olanlar yayınlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal güzelliği kızılımsı parlak renk alanından çıkarır; komşu dal güzellik ve tazeliği belirli kızıllık koşulu olmadan verir.","focus_only":"Kızıllığa yakın renk ve saçtaki güçlü kızıllık çekirdeği vardır.","gloss":"güzellik ve tazelik","neighbor_only":"Genel güzellik, tazelik ve hoş renk alanı daha geniştir.","neighbor_ref":"root_000158/B001","relation_type":"near_neighbor","shared_zone":"İki dal da hoş görünüş ve güzel renk alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal kızıllığı güzellik ve parlak görünüşle bağlar; komşu dal kızıllığın derecesini öne çıkarır.","focus_only":"Kızıllık güzellik ve aydınlık yüz uzantısına da geçer.","gloss":"şiddetli kızıllık","neighbor_only":"Şiddetli kızıllık tek başına renk yoğunluğu olarak kalır.","neighbor_ref":"root_000200/B004","relation_type":"near_neighbor","shared_zone":"İki dalda da kızıl renk alanı vardır."},{"boundary_match":"field_only","distinction":"Odak dal nitelik ve görünüş alanındadır; komşu dal ışık üreten nesne alanındadır.","focus_only":"Canlı veya nesne üzerinde renk ve güzel görünüş niteliğidir.","gloss":"ışık veren lamba","neighbor_only":"Işık veren araç veya gök cismi ışığıdır.","neighbor_ref":"root_000839/B005","relation_type":"same_field","shared_zone":"İki dalda parlaklık ve aydınlık çağrışımı vardır."}],"source_summary":"Kaynaklar anlamı öncelikle kızıllığa dayanan bir renk alanı olarak verir; bu alan saçta güçlü kızıllık ve hayvanda kızılımsı ton biçiminde görünür. Aynı kaynaklar yüz için güzellik, açıklık ve parlak görünüş değerini de bu renk ve ışıklılık alanına bağlar."},"support_links":[]},{"boundary":"Gün başında uyuma eylemidir; içecek, gelme ve gün başlangıcı anlamları dışarıda kalır.","branch_kind":"bare","branch_ref":"root_000839/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"صُبْح","morph_features":"STEM|POS:T|LEM:SuboH|ROOT:SbH|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"100:3:2:1","qac_word_ref":"100:3:2","surface_ar":"صُبْحًا"}],"gloss":"günün başı uykusu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, günün ilk bölümünde uyuma eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Uyuma, kişinin gün başına ulaştığı veya gün aydınlandığı ana bağlanır."}}],"root_ar":"ص ب ح","root_id":"root_000839","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gün aydınlandığında ya da erken gündüzde uyuma eylemi için uygundur.","boundary_detail":"Gün başında uyuma eylemidir; içecek, gelme ve gün başlangıcı anlamları dışarıda kalır.","concept_gloss":"günün başı uykusu","contextual_glosses":[{"applicability":"Eylem fiil olarak çevrildiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uyuma eylemi ve erken gündüz koşulu korunur."},"facet_ids":["F001","F002"],"text":"günün başında uyumak","usage_role":"general"}],"definition":"Kişinin günün ilk bölümünde, gün aydınlanırken veya gün başına vardığında uyuması. Çekirdek bir uyku eylemidir ve yalnız zaman koşulu bakımından gün başlangıcına bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, günün ilk bölümünde uyuma eylemidir."},{"facet_id":"F002","role":"specialization","statement":"Uyuma, kişinin gün başına ulaştığı veya gün aydınlandığı ana bağlanır."}],"identity_rationale":"Kaynak ifadesi dalı günün ilk bölümünde, kişi gün ışığına vardığında uyuma eylemi olarak verir. Bu anlam erken gündüz zamanıyla ilişkili olsa da içecek, gelme veya zaman adının kendisi değildir.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"günün başında ya da gün aydınlanınca uyuma"}],"lexicalization_note":"Yalın dal olduğu için tanım tek bir kalıba bağlı olmayan erken gündüz uykusunu verir.","neighbor_coverage_note":"Genel uyku, uyuklama, gece uykusu, öğle uykusu, uzanma ve kökün zaman dalları değerlendirildi; zaman koşulu belirgin olanlar seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal uyku eylemini erken gündüz zamanıyla sınırlar; komşu dal uyku ve durgunluğu genel olarak adlandırır.","focus_only":"Uyku özellikle günün ilk bölümüne bağlıdır.","gloss":"uyku","neighbor_only":"Uyku ve sakinlik zaman koşulu olmadan genel biçimde verilir.","neighbor_ref":"root_000585/B001","relation_type":"near_neighbor","shared_zone":"İki dal da uyuma eylemini paylaşır."},{"boundary_match":"field_only","distinction":"Odak dal erken gündüzdeki uyku; komşu dal gün ortasında gerçekleşen uyku ve dinlenmedir.","focus_only":"Günün ilk bölümündeki uykuya bağlıdır.","gloss":"öğle uykusu","neighbor_only":"Günün orta bölümündeki dinlenme ve uykuya bağlıdır.","neighbor_ref":"root_001276/B002","relation_type":"same_field","shared_zone":"İki dal da gün içindeki belirli zamanlı uyku türleridir."},{"boundary_match":"thematic_only","distinction":"Odak dal eylemdir; komşu dal eylemin içinde gerçekleştiği zaman dilimidir.","focus_only":"Bu zamanda yapılan uyuma eylemini adlandırır.","gloss":"günün ilk aydınlığı","neighbor_only":"Zamanın kendisini ve ilk aydınlığı adlandırır.","neighbor_ref":"root_000839/B001","relation_type":"thematic","shared_zone":"Odak dalın zaman koşulu B001 dalındaki gün başlangıcıdır."}],"source_summary":"Kaynaklar anlamı günün ilk bölümünde uyuma olarak verir. Bu kullanımda belirleyici olan uyku eylemiyle birlikte zaman koşuludur; günün başlangıcı yalnızca eylemin gerçekleştiği çevreyi belirler."},"support_links":[]},{"boundary":"Çökülü kalıp geç kalkmayan deve için kullanılır; lamba, içecek ve uyku dalları ayrı tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_000839/B008","candidate_links":[{"candidate_id":"cand_ac884102b47a800d9d54","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صُبْح","morph_features":"STEM|POS:T|LEM:SuboH|ROOT:SbH|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"100:3:2:1","qac_word_ref":"100:3:2","surface_ar":"صُبْحًا"}],"gloss":"gün doğana dek çöken deve","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, devenin çökülü kaldığı yerden gün başına kadar kalkmamasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Davranış özellikle dişi deve için adlandırılır ve çoğul biçimde sürü üyelerine yayılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bazı anlatımlarda kalkmama süresi gün yükselinceye ve otlamaya çıkmayıncaya kadar uzatılır."}}],"root_ar":"ص ب ح","root_id":"root_000839","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dişi deve veya deve grubu için, çökülü kalıp gün başına kadar otlamaya kalkmama anlamında uygundur.","boundary_detail":"Çökülü kalıp geç kalkmayan deve için kullanılır; lamba, içecek ve uyku dalları ayrı tutulur.","concept_gloss":"gün doğana dek çöken deve","contextual_glosses":[{"applicability":"Hayvan davranışı kısa karşılıkla anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çökülü yer, gün başı ve otlamaya çıkmama koşullarını açıkça vermez.","preserves":"Devenin kalkmayı geciktirmesini korur."},"facet_ids":["F001","F003"],"text":"geç kalkan deve","usage_role":"general"},{"applicability":"Otlamaya geç çıkma ayrıntısı gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Deve, geç kalkma ve otlamaya geç çıkma koşulu korunur."},"facet_ids":["F001","F003"],"text":"gün yükselene dek otlamayan deve","usage_role":"contextual"}],"definition":"Gece çöküp kaldığı yerde gün aydınlanıncaya veya gün yükselinceye kadar kalkmayan, bu yüzden otlamaya geç başlayan deve. Çoğul kullanım da aynı davranışa sahip hayvan grubunu gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, devenin çökülü kaldığı yerden gün başına kadar kalkmamasıdır."},{"facet_id":"F002","role":"specialization","statement":"Davranış özellikle dişi deve için adlandırılır ve çoğul biçimde sürü üyelerine yayılır."},{"facet_id":"F003","role":"extension","statement":"Bazı anlatımlarda kalkmama süresi gün yükselinceye ve otlamaya çıkmayıncaya kadar uzatılır."}],"identity_rationale":"Kaynak ifadesi dalı, deve veya dişi devenin gece konakladığı yerde çökülü kalıp gün aydınlanıncaya ya da gün yükselinceye kadar otlamaya kalkmaması biçiminde verir. Bu, lamba anlamıyla biçimsel olarak karışsa da canlı hayvan davranışı dalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"çökülü yerinden gün başına kadar kalkmayan dişi deve"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"gün başına kadar çökülü kalan dişi develer"}],"lexicalization_note":"Niteleme birimi ile çoğul biçim ayrıdır; tanım deve davranışıyla sınırlı kalır ve lamba anlamına genellenmez.","neighbor_coverage_note":"Dişi deve nitelemeleri, otlak, gebe deve, sürü hareketi, gece yayılımı ve kökün lamba-uyku dalları karşılaştırıldı; davranış sınırını gösterenler seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dalın ölçütü kalkmama ve zaman koşuludur; komşu dalın ölçütü yavrusuyla bırakılma veya engellenmeme durumudur.","focus_only":"Deve gün başına kadar çökülü kalır ve otlamaya geç çıkar.","gloss":"serbest bırakılan dişi deve","neighbor_only":"Dişi deve yavrusuyla serbest bırakılır veya engellenmez.","neighbor_ref":"root_000116/B008","relation_type":"same_field","shared_zone":"İki dal da dişi deveye ilişkin özel niteleme alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal hayvan davranışı alanında kalır; komşu dal nesne ve aydınlatma alanındadır.","focus_only":"Canlı devenin zamanlı davranışını adlandırır.","gloss":"ışık veren lamba","neighbor_only":"Işık veren araç veya gök ışıklarını adlandırır.","neighbor_ref":"root_000839/B005","relation_type":"same_field","shared_zone":"Biçimsel olarak benzer adlandırma vardır, ancak anlam alanları ayrıdır."},{"boundary_match":"field_only","distinction":"Odak dal hareketsizlik ve geç kalkmadır; komşu dal suya yönelen hareket ve acele gidiştir.","focus_only":"Devenin konak yerinde kalıp kalkmamasını anlatır.","gloss":"suya gece yönelme","neighbor_only":"Sürü veya insanların suya doğru gece hareketini anlatır.","neighbor_ref":"root_001212/B008","relation_type":"same_field","shared_zone":"İki dal da deve ve su-otlak düzeninin zamanlı hareketleriyle ilgilidir."}],"source_summary":"Kaynaklar bu dalı, deve veya dişi devenin gece yattığı yerde kalması ve gün aydınlanıncaya kadar kalkmaması olarak verir. Ortak çerçevede geç kalkma, otlamaya geç çıkma ve çoğul hayvan adlandırması aynı davranışa bağlanır."},"support_links":["sup_d26ef228057789f5d9a8"]},{"boundary":"Belirli sabit zaman kalıplarıyla sınırlıdır; yalın gün başlangıcı B001 dalında kalır.","branch_kind":"collocation","branch_ref":"root_000839/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"صُبْح","morph_features":"STEM|POS:T|LEM:SuboH|ROOT:SbH|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"100:3:2:1","qac_word_ref":"100:3:2","surface_ar":"صُبْحًا"}],"gloss":"gün başı zaman kalıbı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, gelme veya karşılaşma eylemine gün başı zaman değeri veren kalıptır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Her günün başlangıcında yapılan geliş düzenli zaman kalıbı oluşturur."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Beşinci günün başlangıcı gibi sayılı gün kalıpları belirli vade zamanını gösterir."}}],"root_ar":"ص ب ح","root_id":"root_000839","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Her günün başlangıcı, beşinci günün başlangıcı veya belirli gün başı anlamını veren eşdizimler için uygundur.","boundary_detail":"Belirli sabit zaman kalıplarıyla sınırlıdır; yalın gün başlangıcı B001 dalında kalır.","concept_gloss":"gün başı zaman kalıbı","contextual_glosses":[{"applicability":"Tekrarlanan geliş veya görüşme kalıbı için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Her gün tekrar eden gün başı zamanını korur."},"facet_ids":["F002"],"text":"her günün başında","usage_role":"contextual"},{"applicability":"Sayılı gün kalıbında, beşinci gün başlangıcı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sayılı gün ve gün başı koşulu korunur."},"facet_ids":["F003"],"text":"beşinci günün başında","usage_role":"contextual"}],"definition":"Gelme veya karşılaşma eylemini günün ilk bölümüne bağlayan sabit zaman kalıpları. Kalıp her günün başlangıcını, beşinci günün başlangıcını veya belirli bir gün başlangıcını gösterebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, gelme veya karşılaşma eylemine gün başı zaman değeri veren kalıptır."},{"facet_id":"F002","role":"specialization","statement":"Her günün başlangıcında yapılan geliş düzenli zaman kalıbı oluşturur."},{"facet_id":"F003","role":"specialization","statement":"Beşinci günün başlangıcı gibi sayılı gün kalıpları belirli vade zamanını gösterir."}],"identity_rationale":"Kaynak ifadesi dalı günün ilk bölümünü belirli kalıplar içinde zaman zarfı olarak kullanır: her günün başlangıcında gelme, beşinci günün başlangıcında gelme veya belirli bir gün başlangıcında karşılaşma. Bu yüzden dal zaman adının kendisi değil, kalıpla kurulmuş zaman belirtecidir.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"her günün başında, gelme veya görüşme zamanı olarak"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"beşinci günün başında"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"belirli bir gün başında görüşme ya da eylem zamanı"}],"lexicalization_note":"Eşdizim dalı olduğu için tanım yalnız verilen zaman kalıplarına bağlıdır ve yalın zaman adının geneline açılmaz.","neighbor_coverage_note":"Sayılı zaman, yinelenen görüşme, randevu, erken gitme, gece gelişleri ve kökün öteki dalları karşılaştırıldı; eşdizim sınırını gösterenler yayınlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sayımı gün başı kalıplarıyla sınırlar; komşu dal zaman sayımı ve yinelenmeyi daha genel ele alır.","focus_only":"Zaman kalıpları özellikle günün ilk bölümüne bağlıdır.","gloss":"sayılı zaman","neighbor_only":"Sayılı veya yinelenen zaman genel biçimde, gün başı koşulu olmadan verilir.","neighbor_ref":"root_000989/B005","relation_type":"near_neighbor","shared_zone":"İki dal da belirli veya yinelenen zaman hesabı kurar."},{"boundary_match":"field_only","distinction":"Odak dal yalnız gün başı zarf kalıbıdır; komşu dal sözleşilen zaman ya da yer kavramını çekirdek yapar.","focus_only":"Gelme veya karşılaşmanın gün başında gerçekleştiğini belirten kalıptır.","gloss":"randevu zamanı","neighbor_only":"Verilen sözün zaman veya yer sınırı olan randevu alanıdır.","neighbor_ref":"root_001662/B003","relation_type":"same_field","shared_zone":"İki dal da bir eylemin zamanını belirler."},{"boundary_match":"thematic_only","distinction":"Odak dal eşdizimsel zaman belirtecidir; komşu dal bu belirtecin dayandığı yalın zaman adıdır.","focus_only":"Yalnız belirli kalıplarda eylemin zamanını bildirir.","gloss":"günün ilk aydınlığı","neighbor_only":"Günün ilk aydınlığını ve gün başlangıcını adlandırır.","neighbor_ref":"root_000839/B001","relation_type":"thematic","shared_zone":"B009 dalındaki zaman kalıpları B001 dalındaki gün başlangıcını kullanır."}],"source_summary":"Kaynaklar bu dalı gelme ve karşılaşma eylemleriyle kurulan gün başı zaman kalıpları olarak verir. Ortak malzeme her günün başlangıcı, beşinci günün başlangıcı ve belirli bir gün başında gerçekleşen buluşma ya da geliş örneklerini içerir."},"support_links":[]},{"boundary":"Bir duruma geçme anlamıdır; gün başlangıcına girme ve zaman adları B001 dalında tutulur.","branch_kind":"bare","branch_ref":"root_000839/B010","candidate_links":[{"candidate_id":"cand_0c7b074eb10aaa08cdf2","lane":"micro"},{"candidate_id":"cand_f4cd976dd5b09f55f1e3","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صُبْح","morph_features":"STEM|POS:T|LEM:SuboH|ROOT:SbH|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"100:3:2:1","qac_word_ref":"100:3:2","surface_ar":"صُبْحًا"}],"gloss":"bir duruma gelmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, bir öznenin belirli bir duruma veya niteliğe geçmesidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Fiil adı bu duruma geçme eyleminin adlandırılması olarak kullanılır."}}],"root_ar":"ص ب ح","root_id":"root_000839","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin veya şeyin yeni bir nitelik ya da hale geçmesini anlatan kullanımlar için uygundur.","boundary_detail":"Bir duruma geçme anlamıdır; gün başlangıcına girme ve zaman adları B001 dalında tutulur.","concept_gloss":"bir duruma gelmek","contextual_glosses":[{"applicability":"Bir niteliğe erişme veya o hale gelme bağlamlarında en doğal kısa karşılıktır.","error_profile":{"adds":"Dönüşme içermeyen salt var olma kullanımlarını da çağırabilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Belirli bir halde bulunma veya o hale gelme değerini korur."},"facet_ids":["F001"],"text":"olmak","usage_role":"general"},{"applicability":"Önceki durumdan yeni nitelik veya hale geçiş vurgulandığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Duruma geçme ve sonuç niteliği korunur."},"facet_ids":["F001","F002"],"text":"hale gelmek","usage_role":"contextual"}],"definition":"Bir kişinin veya şeyin belirli bir nitelik ya da duruma geçmesi, o hale gelmesi. Fiil adı da bu duruma geçme eylemini adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, bir öznenin belirli bir duruma veya niteliğe geçmesidir."},{"facet_id":"F002","role":"associated_use","statement":"Fiil adı bu duruma geçme eyleminin adlandırılması olarak kullanılır."}],"identity_rationale":"Kaynak ifadesi bu dalı bir kimsenin veya şeyin belli bir duruma geçmesi ve bunun fiil adı olarak kullanılması biçiminde verir. Günün ilk bölümüne girme anlamıyla biçimsel bağlantı olsa da burada çekirdek zaman değil, duruma dönüşmedir.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"bir duruma geçti, o hale geldi"}],"lexicalization_note":"Yalın dal olduğu için tanım belirli bir eşdizime bağlı kalmadan bir duruma geçme anlamını verir.","neighbor_coverage_note":"Duruma gelme, biçim değiştirme, ortaya çıkma, yaptırma, geri dönme, gündüz eylemi ve kökün zaman dalları değerlendirildi; hal değişimini aydınlatan ilişkiler yayınlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genel duruma gelme fiilidir; komşu dal belirli örneklerde önceki durumu geride bırakma veya ardıllık gölgesi taşır.","focus_only":"Duruma geçme genel ve yalın yardımcı fiil değerindedir.","gloss":"hale gelmek","neighbor_only":"Birinden sonra başka bir niteliğe dönüşme veya tatma kökenli örnekler daha belirgindir.","neighbor_ref":"root_000526/B006","relation_type":"near_synonym","shared_zone":"İki dal da bir niteliğe veya hale geçmeyi paylaşır."},{"boundary_match":"partial","distinction":"Odak dal mevcut öznenin hal değişimidir; komşu dal varlığa gelme veya sonradan olma alanını çekirdek yapar.","focus_only":"Var olan öznenin bir niteliğe ya da hale geçmesi öne çıkar.","gloss":"ortaya çıkmak","neighbor_only":"Bir şeyin yokluktan sonra ortaya çıkması veya yeni olması öne çıkar.","neighbor_ref":"root_000299/B001","relation_type":"near_neighbor","shared_zone":"İki dal da yeni bir durumun gerçekleşmesini paylaşır."},{"boundary_match":"field_only","distinction":"Odak dal zaman dışı durum değişimidir; komşu dal somut zaman dilimidir.","focus_only":"Bir niteliğe ya da hale dönüşme fiilidir.","gloss":"günün ilk aydınlığı","neighbor_only":"Günün ilk aydınlığı ve gün başlangıcıdır.","neighbor_ref":"root_000839/B001","relation_type":"same_field","shared_zone":"Biçimsel olarak gün başlangıcına girme ile duruma geçme arasında kök bağı vardır."}],"source_summary":"Kaynaklar dalı, bir öznenin belirli bir hale gelmesi ve bu fiilin adının aynı eylemi karşılaması olarak verir. Burada zaman anlamı çekirdeğe girmez; belirleyici olan nitelik veya durum değişimidir."},"support_links":["sup_06261e4e0407d44d3182","sup_d3b888abd29b6646cdfa"]},{"boundary":"Dal, yarar sağlama, yağmurla sulama ve yük takımını düzeltmeyle sınırlıdır; başkalık, kan bedeli ve aileyi kıskanarak koruma anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001119/B001","candidate_links":[{"candidate_id":"cand_cd3328592ade1b49eed6","lane":"micro"},{"candidate_id":"cand_d0d12a26184bc0eaf69c","lane":"micro"},{"candidate_id":"cand_186caec22cfe3806faaf","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُغِيرَٰت","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:mugiyra`t|ROOT:gyr|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:3:1:3","qac_word_ref":"100:3:1","surface_ar":"مُغِيرَٰتِ"}],"gloss":"yarar sağlayıp durumunu iyileştirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Aileye geçimlik sağlama ve birine işine yarayacak biçimde yarar dokundurma temel anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yağmur bağlamında insanları veya toprağı sulama ve böylece durumlarını iyileştirme anlamı doğar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Konaklama ve yük hayvanı bağlamında yük takımını indirme, düzeltme ve hayvanı rahatlatma eylemini belirtir."}}],"root_ar":"غ ي ر","root_id":"root_001119","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın aileye geçimlik sağlama çekirdeğini ve sulama ya da yük takımını düzeltme yoluyla gerçekleşen özel iyileştirme biçimlerini birlikte temsil eder.","boundary_detail":"Dal, yarar sağlama, yağmurla sulama ve yük takımını düzeltmeyle sınırlıdır; başkalık, kan bedeli ve aileyi kıskanarak koruma anlamlarını kapsamaz.","branch_image_ar":"الصلاح والمنفعة بالميرة والسقي والإصلاح","concept_gloss":"yarar sağlayıp durumunu iyileştirme","contextual_glosses":[{"applicability":"Eylemin yararlanan tarafı aile ve sağlanan şey geçimlik olduğunda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yağmurla sulama ve yük takımını düzeltme kullanımlarını dışarıda bırakır.","preserves":"Aileye yarar sağlama ve onun ihtiyaçlarını karşılama yönünü korur."},"facet_ids":["F001"],"text":"ailesinin geçimini sağladı","usage_role":"contextual"},{"applicability":"Yağmurun insanlara veya toprağa ulaşarak su ve yarar sağlaması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aileye geçimlik sağlama ile yük takımını düzeltme kullanımlarını kapsamaz.","preserves":"Sulama aracını ve bunun doğurduğu iyileşme sonucunu korur."},"facet_ids":["F002"],"text":"yağmurla sulayıp iyileştirdi","usage_role":"contextual"},{"applicability":"Yük hayvanının üzerindeki takımın indirilip düzenlenmesi ve hayvanın rahatlatılması bağlamına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Geçimlik sağlama ve yağmurla sulama anlamlarını dışarıda bırakır.","preserves":"Yük takımına yapılan işlemi ve hayvanı rahatlatma sonucunu korur."},"facet_ids":["F003"],"text":"yükünü indirip takımını düzeltti","usage_role":"explanatory"}],"definition":"Bir kimsenin ailesine geçimlik sağlayarak yarar dokundurmasıdır; belirli yapılarda yağmurun insanları ya da toprağı sulayıp durumlarını iyileştirmesini ve yük takımının indirilip düzeltilmesini de anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Aileye geçimlik sağlama ve birine işine yarayacak biçimde yarar dokundurma temel anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Yağmur bağlamında insanları veya toprağı sulama ve böylece durumlarını iyileştirme anlamı doğar."},{"facet_id":"F003","role":"associated_use","statement":"Konaklama ve yük hayvanı bağlamında yük takımını indirme, düzeltme ve hayvanı rahatlatma eylemini belirtir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Yiyecek verme anlamına çekilerek genel yarar sağlama sınırını daraltabilir.","fit":"narrowing","loses":"Sulama dışındaki iyileştirme ile yük takımını düzeltme işlemlerini karşılamaz.","preserves":"Bir canlıya ihtiyacını sağlayarak yarar dokundurma yönünü korur."},"text":"beslemek"}],"identity_rationale":"Kaynak sözü, aileye geçimlik sağlama ve yarar dokundurmayı temel alırken yağmurla sulama ile yük takımını düzeltme kullanımlarını da açıkça kapsar. Verilen dal çerçevesi bu ortak yarar ve iyileştirme alanını, birbirinden ayrı gerçekleşme biçimlerini karıştırmadan yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"aileyi geçindiren azık ve ihtiyaç payı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"aileye geçimlik ve yarar sağlama"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"ailesine geçimlik sağladı ve yarar dokundurdu"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"ona yarar sağladı ve ihtiyacını giderdi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"Tanrı onlara yağmur verip durumlarını iyileştirdi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yağmur toprağı suladı"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"sulanmış toprak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"sulanmış toprak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yük takımlarını düzeltiyorlar"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"devesinin yükünü indirip durumunu düzeltti"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"hayvanı rahatlatmak için yük takımını düzenleyen kişi"}],"lexicalization_note":"Tanım hem yalın biçimlerdeki yarar ve geçimlik anlamını hem de aile, yağmur, toprak ve yük hayvanıyla kurulan yapılara bağlı özel kullanımları ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan dört karşılaştırma geçim sağlama, sulama, bakım ve değişim sınırlarını en açık biçimde gösterir, kalan adaylar ise yalnızca uzak bir yarar veya aynı senaryo bağlantısı sunar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sağlanan geçimliği veya belirli iyileştirme yollarını anlatır; komşu dal ise hizmet edip işi yürütme ve bir şeyi sunma eylemine dayanır.","focus_only":"Geçimlik sağlama, yağmurla sulama ve yük takımını düzeltme kullanımlarını içerir.","gloss":"yarar sağlama ile hizmet etme","neighbor_only":"Bir kişiye hizmet etme, işini görme ve istediğini eline verme eylemlerini kapsar.","neighbor_ref":"root_001028/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir kişinin ihtiyacını karşılayarak ona yarar dokunduran bir eyleyen vardır."},{"boundary_match":"partial","distinction":"Odak daldaki sulama yağmurla ve yarar sağlama sonucuyla bağlıdır; komşu dal suyu ulaştırma ya da dökme işleminin kendisini daha geniş kapsamda anlatır.","focus_only":"Sulamayı yağmurun sağladığı yarar ve iyileşme çerçevesinde, öteki yarar türleriyle birlikte taşır.","gloss":"yağmurla sulama ile su ulaştırma","neighbor_only":"Suyu herhangi bir insana, kaba, havuza veya ağaca ulaştırma ve dökme işlemini genel olarak kapsar.","neighbor_ref":"root_001458/B003","relation_type":"near_neighbor","shared_zone":"İki dal da suyun bir alıcıya ulaşması ve onu sulaması olayında örtüşür."},{"boundary_match":"field_only","distinction":"Odak dal su ve yararın sağlanmasına odaklanır; komşu dal bunun ardından toprağın canlı ve verimli duruma gelmesini çekirdek edinir.","focus_only":"Yağmurun insanları ya da toprağı sulayarak yarar sağlaması eylemini belirtir.","gloss":"sulama ile toprağın canlanması","neighbor_only":"Yağmurun ardından toprağın canlanması, verimlenmesi ve taze bitkinin ortaya çıkmasını belirtir.","neighbor_ref":"root_000383/B002","relation_type":"same_field","shared_zone":"Yağmur, toprak ve iyileşen doğal durum iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal yarar sağlama sonucunu gerektirir; komşu dal değişimin yönünü iyiye gitmeyle sınırlamaz ve yerine koymayı da içerir.","focus_only":"Bir alıcıya geçimlik, su veya bakım sağlayıp onun durumunu iyiye götürür.","gloss":"iyileştirme ile değiştirme","neighbor_only":"Bir şeyin biçimini ya da durumunu değiştirme veya onu başka bir şeyle değiştirme işlemini anlatır.","neighbor_ref":"root_001119/B003","relation_type":"near_neighbor","shared_zone":"Yük takımının düzeltilmesi gibi bağlamlarda bir durumun önceki halinden farklı ve daha uygun hale gelmesi ortaktır."}],"source_phrase_ar":"الغِيرة بالكسر: الميرة (sihah)؛ يميرهم وينفعهم (sihah)؛ غارهم الله تعالى بالغيث أي أصلح شأنهم ونفعهم (maqayis)؛ سقاهم (sihah)؛ يصلحون الرحال (sihah)؛ حط عنه رحله وأصلح من شأنه (tahdhib)","source_summary":"Kaynaklar aileye geçimlik ve yarar sağlamayı, yağmurla sulayıp iyileştirmeyi ve yük takımını düzelterek hayvanı rahatlatmayı aynı dal altında toplar. Bunlar genel bir yarar çekirdeğinin farklı katılımcı ve yapılarda gerçekleşen kullanımlarıdır.","sources":["SI","TA","MQ"],"what_is_ar":"يدخل فيه ميرة الأهل ونفعهم، وسقي الأرض أو القوم بالغيث، وإصلاح الرحال أو شأن الراحلة.","what_is_not_ar":"لا يدخل فيه مجرد السوى والاستثناء، ولا الدية الخاصة، ولا الغَيْرة على الأهل إلا من جهة الأصل العام عند مقاييس."},"support_links":["sup_826d14e70aa61f73702c","sup_fd5a5122ca86f0459b2b","sup_feb6fc0376d933cc80e4"]},{"boundary":"Bu dal yalnızca kan bedelinin adı, ödenmesi ve cana karşılık ceza yerine kabul edilmesiyle ilgilidir; genel yarar, başkalık veya değişim anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001119/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُغِيرَٰت","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:mugiyra`t|ROOT:gyr|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:3:1:3","qac_word_ref":"100:3:1","surface_ar":"مُغِيرَٰتِ"}],"gloss":"cana karşılık ceza yerine kabul edilen kan bedeli","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Öldürme veya yaralama karşılığında hak sahibine ödenen bedelin kendisini adlandırır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin bu bedeli ödemesini ve hak sahiplerinin onu cana karşılık ceza yerine kabul etmesini anlatır."}}],"root_ar":"غ ي ر","root_id":"root_001119","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem özel bedelin adını hem de onun cana karşılık cezanın yerine kabul edilme işlevini eksiksiz belirtir.","boundary_detail":"Bu dal yalnızca kan bedelinin adı, ödenmesi ve cana karşılık ceza yerine kabul edilmesiyle ilgilidir; genel yarar, başkalık veya değişim anlamı değildir.","branch_image_ar":"الغَيْر في الدية","concept_gloss":"cana karşılık ceza yerine kabul edilen kan bedeli","contextual_glosses":[{"applicability":"Bir kişinin öldürme veya yaralama nedeniyle hak sahibine gereken bedeli verdiği eylem bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bedelin adı ve onun cana karşılık ceza yerine kabul edilmesi ayrıca belirtilmez.","preserves":"Yükümlü kişinin özel bedeli hak sahibine ödeme eylemini korur."},"facet_ids":["F002"],"text":"kan bedelini ödedi","usage_role":"contextual"},{"applicability":"Hak sahiplerinin cana karşılık ceza istemek yerine parasal ya da mal biçimindeki karşılığı kabul ettiği bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bedelin sözlükteki özel adı ve ödeme eyleminin ayrıntısı dışarıda kalır.","preserves":"Bedelin başka bir yaptırım yerine kabul edilmesi seçimini korur."},"facet_ids":["F001","F002"],"text":"kan bedelini kabul ettiler","usage_role":"contextual"}],"definition":"Öldürme ya da yaralama karşılığında hak sahibine ödenen kan bedeli ve bu bedelin cana karşılık uygulanacak cezanın yerine kabul edilmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Öldürme veya yaralama karşılığında hak sahibine ödenen bedelin kendisini adlandırır."},{"facet_id":"F002","role":"associated_use","statement":"Bir kişinin bu bedeli ödemesini ve hak sahiplerinin onu cana karşılık ceza yerine kabul etmesini anlatır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Ölüm ve yaralama dışındaki zararlar için ödenen çok çeşitli karşılıkları da kapsar.","collision":"Genel özel hukuk ödemeleriyle karışarak cana karşılık ceza seçeneği sınırını silebilir.","fit":"broadening","loses":null,"preserves":"Bir zararın karşılığında hak sahibine bedel ödenmesi yönünü korur."},"text":"tazminat"}],"identity_rationale":"Kaynak sözü, öldürme ya da yaralama karşılığında ödenen bedelin adını ve bu bedelin cana karşılık ceza uygulamak yerine kabul edilmesini birlikte bildirir. Verilen dal kimliği bu özel hukuk bağlamını doğru biçimde sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bana kan bedelini ödedi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"kan bedeli"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"cana karşılık ceza yerine kabul edilen kan bedeli"}],"lexicalization_note":"Tanım kan bedelini adlandıran biçimleri ve birinin bu bedeli ödemesini anlatan yapıyı birlikte, fakat yalnızca bu hukuk bağlamında ele alır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan karşılaştırmalar kan bedelinin ödenmesi, kurumsal karşılanması, yara bedeli ve yaptırım yerine geçirilmesi sınırlarını gösterir, diğer adaylar daha uzak hukuk veya karşılık ilişkileridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bedelin adlandırılması ile yaptırım yerine kabulünü de kapsar; komşu dal ödeme ve alma eylemine daha doğrudan bağlıdır.","focus_only":"Kan bedelinin özel adını ve onun cana karşılık ceza yerine kabul edilmesini birlikte içerir.","gloss":"kan bedeli ve bedeli ödeme","neighbor_only":"Bedeli verme ve alma eylemlerini doğrudan fiil olarak anlatır.","neighbor_ref":"root_001637/B002","relation_type":"near_synonym","shared_zone":"İki dal da öldürme veya yaralama karşılığında kan bedelinin hak sahibine verilmesini anlatır."},{"boundary_match":"partial","distinction":"Komşu dal ödeme yükünün topluluk içinde üstlenilmesi gibi kurumsal katılımcıları kapsar; odak dalda bu düzen kurucu değildir.","focus_only":"Özel adlandırmayı ve bedelin cana karşılık ceza yerine kabul edilmesini öne çıkarır.","gloss":"kan bedeli ve ortak ödeme düzeni","neighbor_only":"Bedeli ödeyen dayanışma grubunu ve suçlarda bedelin paylaşılarak karşılanmasını da kapsar.","neighbor_ref":"root_001036/B004","relation_type":"near_synonym","shared_zone":"Her iki dalda da kan bedeli, onun ödenmesi ve cana karşılık ceza yerine seçilebilmesi ortaktır."},{"boundary_match":"partial","distinction":"Odak dal ölüm durumunu ve cana karşılık cezanın bırakılmasını da kapsar; komşu dal belirli yara türlerine bağlı daha dar bir borçtur.","focus_only":"Ölüm veya yaralama karşılığındaki genel kan bedelini ve kabulünü kapsar.","gloss":"kan bedeli ile yara bedeli","neighbor_only":"Özellikle belirli yaraların doğurduğu zorunlu bedel payına odaklanır.","neighbor_ref":"root_001488/B003","relation_type":"near_neighbor","shared_zone":"Yaralamanın mağdur lehine parasal ya da mal biçiminde bir ödeme yükümlülüğü doğurması ortaktır."},{"boundary_match":"partial","distinction":"Odak dal seçilen karşılığın kan bedeli olmasını gerektirir; komşu dal yerine koymayı bu özel hukuk bağlamıyla sınırlamaz.","focus_only":"Kan bedelinin özel hukuk anlamını ve hak sahibince kabulünü taşır.","gloss":"kan bedeli ile yerine koyma","neighbor_only":"Her türlü biçim, durum veya nesne değişikliğini ve bir şeyi başkasıyla değiştirmeyi kapsar.","neighbor_ref":"root_001119/B003","relation_type":"near_neighbor","shared_zone":"Cana karşılık cezanın bırakılıp yerine kan bedelinin seçilmesi, iki dalın kesiştiği değiştirme olayıdır."}],"source_phrase_ar":"غارني الرجل إذا وداك من الدية والاسم الغِيرة (sihah)؛ الدية فإنها تسمى الغير (maqayis)؛ تقبلوا الغيرا (maqayis;sihah)","source_summary":"Kaynaklar, kan bedelinin özel adını bu bedeli ödeme ve cana karşılık ceza yerine kabul etme uygulamasıyla birlikte verir. Dalın sınırı genel bir karşılık veya değiş tokuş değil, ölüm ya da yaralama doğuran olayın bedelidir.","sources":["SI","MQ"],"what_is_ar":"يدخل فيه اسم الغَيْر أو الغِيرة للدية، وأخذ الدية بدل القود.","what_is_not_ar":"لا يدخل فيه مطلق النفع والميرة، ولا التغيير العام، ولا غير بمعنى سوى إلا بقدر تعليل مقاييس."},"support_links":[]},{"boundary":"Dal değişme ve yerine başkasını koyma işlemleriyle sınırlıdır; salt başkalık bildiren dil bilgisel kullanım veya kan bedelinin kendi adı bu dalın çekirdeği değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001119/B003","candidate_links":[{"candidate_id":"cand_f44be94b687673187adf","lane":"micro"},{"candidate_id":"cand_0c7b074eb10aaa08cdf2","lane":"micro"},{"candidate_id":"cand_c351588bd21c2fecc21d","lane":"micro"},{"candidate_id":"cand_32f991bec03f6d64e758","lane":"micro"},{"candidate_id":"cand_f4cd976dd5b09f55f1e3","lane":"micro"},{"candidate_id":"cand_b1791aab2dede7d650cc","lane":"micro"},{"candidate_id":"cand_ac884102b47a800d9d54","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُغِيرَٰت","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:mugiyra`t|ROOT:gyr|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:3:1:3","qac_word_ref":"100:3:1","surface_ar":"مُغِيرَٰتِ"}],"gloss":"biçimini değiştirme veya yerine başkasını koyma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin biçimini veya durumunu öncekinden farklı hale getirme ve bunun sonucunda şeyin değişmesi temel işlemdir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyi kaldırıp onun yerine başka bir şeyi koyma, değiştirmenin ikinci temel yoludur."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yanlış veya kabul edilemez olanı, onu giderecek doğru bir uygulamayla değiştirme özel bir gerçekleşmedir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Alışverişte iki tarafın karşılıkları değiş tokuş etmesi ve bir bedelin ötekinin yerine geçmesi bu çekirdeğe bağlıdır."}},{"facet_id":"F005","role":"example","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Cana karşılık ceza kararının kan bedeline çevrilmesi, yerine koyarak değiştirmenin hukuk bağlamındaki örneğidir."}}],"root_ar":"غ ي ر","root_id":"root_001119","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın aynı şey üzerinde farklılık oluşturma ve bir şeyi başka bir şeyle değiştirme biçimindeki iki kurucu işlemini birlikte taşır.","boundary_detail":"Dal değişme ve yerine başkasını koyma işlemleriyle sınırlıdır; salt başkalık bildiren dil bilgisel kullanım veya kan bedelinin kendi adı bu dalın çekirdeği değildir.","branch_image_ar":"تغيير الصورة أو إبدال الشيء بغيره","concept_gloss":"biçimini değiştirme veya yerine başkasını koyma","contextual_glosses":[{"applicability":"Nesnenin özü korunurken görünüşünün veya düzeninin önceki halinden farklılaştırıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nesnenin başka bir nesneyle değiştirilmesi yolunu kapsamaz.","preserves":"Aynı nesne üzerinde yeni bir biçim oluşturma işlemini korur."},"facet_ids":["F001"],"text":"biçimini değiştirdi","usage_role":"contextual"},{"applicability":"İlk nesne, uygulama veya karşılık kaldırılıp onun işlevine başka biri getirildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı nesnenin yalnız biçim veya durum bakımından değişmesini kapsamaz.","preserves":"İlk unsurun kaldırılması ile başka bir unsurun onun yerini alması ilişkisini korur."},"facet_ids":["F002"],"text":"yerine başkasını koydu","usage_role":"contextual"},{"applicability":"Kabul edilemez bir uygulamanın uzaklaştırılıp onun yerine doğru bir uygulamanın getirildiği yapıya özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Değiştirmenin değer yargısı içermeyen öteki biçimlerini dışarıda bırakır.","preserves":"Yanlış unsurun giderilmesini, doğru unsurun onun yerine konmasını ve düzeltici sonucu korur."},"facet_ids":["F003"],"text":"yanlışı doğru olanla giderdi","usage_role":"explanatory"},{"applicability":"İki kişinin alışverişte karşılıklı olarak bir malı veya bedeli ötekiyle değiştirdiği bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek taraflı biçim değişikliği ile alışveriş dışındaki yerine koymaları kapsamaz.","preserves":"İki taraflı değiştirme işlemini ve karşılıkların yer değiştirmesini korur."},"facet_ids":["F004"],"text":"onunla değiş tokuş yaptı","usage_role":"contextual"}],"definition":"Bir şeyin özü aynı kalsa da biçiminin ya da durumunun öncekinden farklı hale getirilmesi veya bir şeyin kaldırılıp yerine başka bir şeyin konmasıdır. Belirli yapılarda yanlış olanı doğru olanla giderme, alışverişte karşılıklı değiştirme ve cana karşılık cezadan kan bedeline dönme biçiminde gerçekleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin biçimini veya durumunu öncekinden farklı hale getirme ve bunun sonucunda şeyin değişmesi temel işlemdir."},{"facet_id":"F002","role":"core","statement":"Bir şeyi kaldırıp onun yerine başka bir şeyi koyma, değiştirmenin ikinci temel yoludur."},{"facet_id":"F003","role":"specialization","statement":"Yanlış veya kabul edilemez olanı, onu giderecek doğru bir uygulamayla değiştirme özel bir gerçekleşmedir."},{"facet_id":"F004","role":"associated_use","statement":"Alışverişte iki tarafın karşılıkları değiş tokuş etmesi ve bir bedelin ötekinin yerine geçmesi bu çekirdeğe bağlıdır."},{"facet_id":"F005","role":"example","statement":"Cana karşılık ceza kararının kan bedeline çevrilmesi, yerine koyarak değiştirmenin hukuk bağlamındaki örneğidir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir eyleyenin şeyi değiştirmesini ve bir unsuru başkasıyla değiştirmesini karşılamaz.","preserves":"Bir şeyin önceki durumundan farklı bir duruma geçmesini korur."},"text":"dönüşmek"}],"identity_rationale":"Kaynak sözü bir şeyin biçim veya durumunun farklılaşmasını, şeyin başka bir şeyle değiştirilmesini ve bunun alışveriş, yanlış olanı doğru olanla giderme ya da kan bedeline dönme gibi özel gerçekleşmelerini açıkça bir araya getirir. Dal çerçevesi bu iki temel değişim yolunu ve bağımlı örneklerini doğru ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"şeyi değiştirdi ve öncekinden farklı hale getirdi"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"biçimini değiştirme veya yerine başkasını koyma"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"durumundan ayrılıp farklı hale geldi"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yanlış olanı doğru olanla değiştirip giderdi"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"onunla alışverişte karşılıklı değiş tokuş yaptı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"yerine konan karşılık"}],"lexicalization_note":"Tanım yalın değişme ve değiştirme biçimlerini kapsar; yanlış olanı doğruyla giderme, alışverişte karşılıklı değiştirme ve kan bedeline dönme okumalarını yalnız kendi yapılarında tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen karşılaştırmalar biçim değişikliği, yerine geçme, kendiliğinden hal değiştirme ve salt başkalıkla temel sınırları kurar, kalanlar dar örnek veya uzak alan bağlantısıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal aynı nesnedeki biçim değişikliğiyle sınırlıdır; odak dal ayrıca nesnenin başka bir nesneyle değiştirilmesini ve karşılıklı değiş tokuşu kapsar.","focus_only":"Biçim değişikliğine ek olarak bir şeyi kaldırıp yerine başka bir şey koymayı da içerir.","gloss":"genel değiştirme ile biçim değiştirme","neighbor_only":"Aynı özün korunarak yalnız halinin veya biçiminin değiştirilmesini çekirdek edinir.","neighbor_ref":"root_000095/B002","relation_type":"near_synonym","shared_zone":"Bir şeyin özü korunurken biçiminin veya durumunun öncekinden farklı hale getirilmesi iki dalda ortaktır."},{"boundary_match":"partial","distinction":"Odak dal değişiklik meydana getirme işlemini de taşır; komşu dal yeni unsurun öncekinin yerini veya görevini üstlenmesine odaklanır.","focus_only":"Aynı nesnenin biçim veya durum bakımından farklılaştırılmasını da içerir.","gloss":"değiştirme ile yerine geçme","neighbor_only":"Bir şeyin ya da kişinin ötekinin görevini veya yerini üstlenmesini daha geniş biçimde kapsar.","neighbor_ref":"root_000095/B001","relation_type":"near_synonym","shared_zone":"Bir unsurun kaldırılıp başka bir unsurun onun yerine getirilmesi iki dalın ortak çekirdeğidir."},{"boundary_match":"partial","distinction":"Odak dal geçişli değiştirmeyi ve yerine koymayı içerir; komşu dal varlığın kendi hareketi veya dönüşümü üzerinde daha geniştir.","focus_only":"Bir eyleyenin şeyi değiştirmesini ve onun yerine başka bir şey koymasını kapsar.","gloss":"değiştirme ile hal değiştirme","neighbor_only":"Bir varlığın yer veya durum değiştirerek hareket etmesini ve kimi özel fiziksel sapmaları kapsar.","neighbor_ref":"root_000373/B001","relation_type":"near_synonym","shared_zone":"Bir varlığın önceki halinden başka bir hale geçmesi iki dalda da bulunur."},{"boundary_match":"partial","distinction":"Odak dal bir olay ve sonuç içerir; komşu dal başkalık ilişkisini veya dışta bırakmayı olay gerçekleşmeden de kurabilir.","focus_only":"Bir farklılık meydana getiren süreç veya bir şeyi başkasıyla değiştirme işlemini gerektirir.","gloss":"değiştirme ile başkalık","neighbor_only":"Herhangi bir değişim olmasa da iki şeyin ayrı, başka veya birbirine aykırı olduğunu ve dil bilgisel dışta bırakmayı bildirir.","neighbor_ref":"root_001119/B005","relation_type":"near_neighbor","shared_zone":"Değiştirme sonucunda ilk halden ya da ilk nesneden başka bir hal veya nesne ortaya çıkması ortak alandır."}],"source_phrase_ar":"الاسم من قولك غيرت الشيء فتغير (sihah)؛ تغير فلان عن حاله (tahdhib)؛ تغيير صورة الشيء دون ذاته (mufradat)؛ تبديله بغيره (mufradat)؛ يدفعون ذلك المنكر بغيره من الحق (tahdhib)؛ قود فغير إلى الدية (maqayis)؛ غايرت الرجل أي عارضته بالبيع وبادلته والغيار البدال (sihah)","source_summary":"Kaynaklar değişimi iki ana biçimde sunar: aynı şeyin biçim veya durumunun farklılaşması ve bir şeyin yerini başka bir şeyin alması. Yanlış olanı doğruyla giderme, alışverişte değiş tokuş ve cana karşılık cezadan kan bedeline dönme bu iki işlemin bağlama bağlı gerçekleşmeleridir.","sources":["SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه تغيير الشيء فتغيره، وتغير الحال، وتبديل الشيء بغيره، ودفع المنكر بغيره من الحق، والمبادلة والبدل.","what_is_not_ar":"لا يدخل فيه غير النحوية بمعنى سوى أو لا إلا إذا كان الكلام في الإبدال بغيره، ولا يدخل فيه الغَيْر للدية إلا من جهة التعليل."},"support_links":["sup_06261e4e0407d44d3182","sup_2955648f213d1d0ae095","sup_6a8ac57b6f912566a6a4","sup_99d1441af33b566c0ef7","sup_d26ef228057789f5d9a8","sup_d3b888abd29b6646cdfa","sup_ede12c0b4743228f42e3"]},{"boundary":"Dal aile veya eşe yönelik kıskanç koruma duygusudur; geçimlik sağlama, kan bedeli, genel değişim ve salt başkalık anlamlarından ayrıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001119/B004","candidate_links":[{"candidate_id":"cand_a8a61d657d3a0abe682d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُغِيرَٰت","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:mugiyra`t|ROOT:gyr|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:3:1:3","qac_word_ref":"100:3:1","surface_ar":"مُغِيرَٰتِ"}],"gloss":"eşini veya ailesini kıskanarak koruma duygusu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin eşini veya ailesini başkasının ilgisinden sakınarak bağlılığı korumaya yönelen kıskançlık duygusudur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu duyguyu taşıyan erkek veya kadın, cinsiyete ve yoğunluğa göre çeşitli niteleme biçimleriyle adlandırılır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Duygu adı için aynı anlamı taşıyan ayrı bir söyleyiş biçimi de aktarılır."}}],"root_ar":"غ ي ر","root_id":"root_001119","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Duygunun hedefini, kıskançlık unsurunu ve aile bağını koruma yönelimini birlikte açıklar.","boundary_detail":"Dal aile veya eşe yönelik kıskanç koruma duygusudur; geçimlik sağlama, kan bedeli, genel değişim ve salt başkalık anlamlarından ayrıdır.","branch_image_ar":"الغَيْرة على الأهل","concept_gloss":"eşini veya ailesini kıskanarak koruma duygusu","contextual_glosses":[{"applicability":"Bir kişinin eşine yönelik ilgiyi kıskanarak onu başkasından sakınmaya çalıştığı eylem bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Duygunun bütün aileye yönelebilmesini ve kişi nitelemelerini kapsamaz.","preserves":"Eşe yönelen kıskançlığı ve onu başkasının ilgisinden sakınma tutumunu korur."},"facet_ids":["F001"],"text":"eşini kıskanıp sakındı","usage_role":"contextual"},{"applicability":"Kişinin aile bağını korumaya yönelik kıskançlığının sürekli veya yoğun bir özellik olarak anlatıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Duygunun ayrı adı ile söyleyiş çeşidini dışarıda bırakır.","preserves":"Aileye yönelen kıskançlığı ve bunun kişide güçlü bir özellik oluşunu korur."},"facet_ids":["F001","F002"],"text":"ailesine karşı çok kıskanç","usage_role":"explanatory"}],"definition":"Bir kişinin eşini veya ailesini başkasının ilgisinden sakınma, bağlılığını koruma ve bu nedenle kıskançlık duyma eğilimidir; aynı alan bu eğilimi güçlü biçimde taşıyan kişiyi de niteler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin eşini veya ailesini başkasının ilgisinden sakınarak bağlılığı korumaya yönelen kıskançlık duygusudur."},{"facet_id":"F002","role":"extension","statement":"Bu duyguyu taşıyan erkek veya kadın, cinsiyete ve yoğunluğa göre çeşitli niteleme biçimleriyle adlandırılır."},{"facet_id":"F003","role":"source_variant","statement":"Duygu adı için aynı anlamı taşıyan ayrı bir söyleyiş biçimi de aktarılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Başarı, mal, konum veya aile dışındaki ilişkilere yönelen bütün kıskançlık türlerini de kapsar.","collision":"Aile bağını koruma yönü bulunmayan genel kıskançlıkla karışır.","fit":"broadening","loses":null,"preserves":"Başkasının ilgisi karşısında duyulan kıskançlığı korur."},"text":"kıskançlık"}],"identity_rationale":"Kaynak sözü aileye, özellikle eşe yönelik kıskanç koruma duygusunu; bu duyguyu taşıyan erkek ve kadın nitelemelerini ve aynı anlamdaki bir söyleyiş çeşidini birlikte verir. Dal çerçevesi duyguyu, taşıyıcısını ve dilsel çeşidini doğru biçimde sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"eşini veya ailesini kıskanarak koruma duygusu"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"eşini veya ailesini kıskanıp sakındı"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"eşine veya ailesine karşı kıskanç ve korumacı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"eşine veya ailesine karşı kıskanç erkek"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"eşine veya ailesine karşı kıskanç kadın"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"eşine veya ailesine karşı çok kıskanç kişi"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"eşini veya ailesini kıskanarak koruma duygusunun bir başka söylenişi"}],"lexicalization_note":"Tanım duygu adını, bu duyguyu taşıyan kişiyi bildiren biçimleri ve aile üzerine kurulan eylem yapısını ayırır; aile bağını bütün kullanımlarda korur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen dört komşu koruma, evlilik dokunulmazlığı, şefkat ve aile topluluğu ile gerçek karışma noktalarını gösterir, diğerleri yalnız uzak evlilik veya ilişki çağrışımları taşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal aile ilişkisi ve kıskançlık duygusuyla sınırlıdır; komşu dal aynı engelleyiciliği aile kıskançlığı bulunmadan cesaret niteliği olarak da taşır.","focus_only":"Eş veya aile bağına yönelen kıskanç koruma duygusunu gerektirir.","gloss":"kıskanç koruyuculuk ile engelleyici cesaret","neighbor_only":"Koruyucu engellemenin yanında savaşçı cesareti de aynı niteleme alanına alır.","neighbor_ref":"root_000778/B007","relation_type":"near_neighbor","shared_zone":"Değer verilen kişiyi veya geride kalanı dış müdahaleden korumak için engelleyici davranma iki dalda ortaktır."},{"boundary_match":"field_only","distinction":"Odak dal kişinin yaşadığı duygu ve tutumdur; komşu dal bir bağ veya konumun sağladığı korunmuş hukuki ve toplumsal durumdur.","focus_only":"Aile bağını kıskançlık ve sakınma duygusuyla korumayı anlatır.","gloss":"kıskanç koruma ile evlilik dokunulmazlığı","neighbor_only":"Evlilik bağı, dokunulmazlık ve toplumsal saygınlığın sağladığı korunmuş durumu anlatır.","neighbor_ref":"root_000331/B003","relation_type":"same_field","shared_zone":"Eş, evlilik ve aile bağının dış müdahaleye karşı korunması ortak alandır."},{"boundary_match":"field_only","distinction":"Odak dal dış ilgiyi engelleyen kıskançlığı gerektirir; komşu dal kıskançlık olmadan şefkat ve merhamete dayanır.","focus_only":"Sevilen aile üyesini başkasının ilgisinden sakınan kıskanç bir koruma taşır.","gloss":"kıskanç koruma ile şefkat","neighbor_only":"Birine şefkat, merhamet ve yakınlıkla yönelmeyi anlatır.","neighbor_ref":"root_000298/B003","relation_type":"same_field","shared_zone":"Bir yakına güçlü bağlılık duyup onun iyiliğini gözetme iki dalın ortak ilişki alanıdır."},{"boundary_match":"thematic_only","distinction":"Odak dal aile hakkında yaşanan bir duygudur; komşu dal herhangi bir duygu veya davranış gerektirmeden bağlı insan kümesini belirtir.","focus_only":"Aileye yönelen belirli bir kıskançlık ve koruma tutumudur.","gloss":"aileyi koruma ile aile topluluğu","neighbor_only":"Aile üyeleri ile din, meslek, yer veya soy bağıyla oluşan topluluğun kendisini adlandırır.","neighbor_ref":"root_000064/B001","relation_type":"thematic","shared_zone":"Aile, odak duygunun hedefi ve komşu dalın adlandırdığı topluluktur."}],"source_phrase_ar":"الغَيرة بالفتح مصدر قولك غار الرجل على أهله (sihah)؛ رجل غيور وغيران وامرأة غيور وغيرى (sihah)؛ غيرة الرجل على أهله (maqayis)؛ الغار لغة في الغيرة (maqayis)","source_summary":"Kaynaklar aileye yönelik kıskanç koruma duygusunu, bu duyguya sahip erkek ve kadınların nitelendirilmesini ve duygu adının bir söyleyiş çeşidini birlikte kaydeder. Duygunun hedefi aile bağıdır; genel cesaret veya yalnız sevgi değildir.","sources":["SI","MQ"],"what_is_ar":"يدخل فيه الغَيْرة المفتوحة على الأهل، ووصف الرجل أو المرأة بالغيور وغيران وغيرى، ولغة الغار في الغيرة.","what_is_not_ar":"لا يدخل فيه الغِيرة بالكسر بمعنى الميرة أو الدية، ولا غير بمعنى سوى."},"support_links":["sup_676ab9ce38ab7596ff3d"]},{"boundary":"Dal bir şeyin başka veya aykırı oluşunu ve bundan türeyen dışta bırakma ile olumsuzlama işlevlerini kapsar; bir şeyi fiilen değiştirme olayını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001119/B005","candidate_links":[{"candidate_id":"cand_6e9ffb2a8a39f1b2cee0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُغِيرَٰت","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:mugiyra`t|ROOT:gyr|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:3:1:3","qac_word_ref":"100:3:1","surface_ar":"مُغِيرَٰتِ"}],"gloss":"başka olma, dışta bırakma veya olumsuzlama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin belirtilen başka bir şeyle aynı olmayıp ondan ayrı, başka veya ona aykırı olması temel ilişkidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir niteleyici ya da ad olarak kullanıldığında belirli bir varlığı veya biçimi dışlar ve başkasını gösterir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir küme içinden belirtilen unsuru hükmün dışında bırakma görevinde kullanılır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir nitelik, biçim veya varlık için yalın olumsuzluk bildiren görev üstlenir."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"İki şeyin birbirinden farklılaşması başkalık ilişkisini karşılıklı olarak kurar; başkalık, yalnız görüş ayrılığından daha geniştir."}}],"root_ar":"غ ي ر","root_id":"root_001119","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Başkalık çekirdeğini ve onun dil içindeki dışta bırakma ile olumsuzlama görevlerini birlikte temsil eder.","boundary_detail":"Dal bir şeyin başka veya aykırı oluşunu ve bundan türeyen dışta bırakma ile olumsuzlama işlevlerini kapsar; bir şeyi fiilen değiştirme olayını kapsamaz.","branch_image_ar":"السوى والخلاف والاستثناء والنفي","concept_gloss":"başka olma, dışta bırakma veya olumsuzlama","contextual_glosses":[{"applicability":"Bir varlığın belirtilen varlıkla aynı olmadığını veya onun dışında kalan bir varlığı gösterdiği ad ve niteleme bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dışta bırakma ve yalın olumsuzlama görevlerini tek başına açıkça göstermez.","preserves":"Aynı olmama, ayrılık ve başka bir varlığı gösterme ilişkisini korur."},"facet_ids":["F001","F002"],"text":"başka","usage_role":"general"},{"applicability":"Belirtilen unsurun bir hükme giren kümeden çıkarıldığı dışta bırakma bağlamında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Salt başkalık, aykırılık ve yalın olumsuzlama anlamlarını kapsamaz.","preserves":"Belirtilen unsurun genel hükmün kapsamından çıkarılması işlevini korur."},"facet_ids":["F003"],"text":"dışında","usage_role":"contextual"},{"applicability":"Bir niteliğin, biçimin veya varlığın bulunmadığını bildiren olumsuz niteleme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başka bir varlığı gösterme ve kümeden dışta bırakma işlevlerini kapsamaz.","preserves":"Belirtilen niteliğin veya varlığın olumsuzlanmasını korur."},"facet_ids":["F004"],"text":"olmayan","usage_role":"contextual"},{"applicability":"Birden çok şeyin nitelik veya durum bakımından birbirinden ayrı hale geldiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dışta bırakma ve yalın olumsuzlama görevlerini kapsamaz.","preserves":"Karşılıklı farklılık oluşmasını ve şeylerin artık aynı sayılmamasını korur."},"facet_ids":["F005"],"text":"birbirinden farklılaştı","usage_role":"contextual"}],"definition":"Bir şeyin ötekinden ayrı, başka veya ona aykırı olmasıdır; bu ilişki dil içinde bir unsuru kümenin dışında bırakmak, bir niteliği ya da varlığı olumsuzlamak ve iki şeyin birbirinden farklı olduğunu bildirmek için de kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin belirtilen başka bir şeyle aynı olmayıp ondan ayrı, başka veya ona aykırı olması temel ilişkidir."},{"facet_id":"F002","role":"specialization","statement":"Bir niteleyici ya da ad olarak kullanıldığında belirli bir varlığı veya biçimi dışlar ve başkasını gösterir."},{"facet_id":"F003","role":"associated_use","statement":"Bir küme içinden belirtilen unsuru hükmün dışında bırakma görevinde kullanılır."},{"facet_id":"F004","role":"associated_use","statement":"Bir nitelik, biçim veya varlık için yalın olumsuzluk bildiren görev üstlenir."},{"facet_id":"F005","role":"extension","statement":"İki şeyin birbirinden farklılaşması başkalık ilişkisini karşılıklı olarak kurar; başkalık, yalnız görüş ayrılığından daha geniştir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Yalnız nitelik ayrılığı anlaşılırsa daha geniş başkalık ilişkisi görünmez.","fit":"narrowing","loses":"Bir unsuru dışta bırakma ve yalın olumsuzlama görevlerini karşılamaz.","preserves":"İki şeyin aynı nitelik veya durumda olmadığını korur."},"text":"farklı"}],"identity_rationale":"Kaynak sözü başkalık ve aykırılık ilişkisini, bir unsuru dışta bırakma işlevini, yalın olumsuzlamayı, belirli bir varlık ya da biçimin yokluğunu ve şeylerin birbirinden farklılaşmasını birlikte açıkça bildirir. Dal çerçevesi bu ad, niteleme ve dil bilgisel işlevleri tek başkalık alanında doğru biçimde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"başka, aynı olmayan veya aykırı"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"dışında, dışta bırakarak"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"değil, olmayan"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"doğru olmayan, yanlış"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"biri öteki olmayan iki şey"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"şeyler birbirinden farklılaştı"}],"lexicalization_note":"Tanım yalın başkalık bildiren biçimleri, dışta bırakma ve olumsuzlama görevlerini ve belirli yapılardaki aykırılık ifadelerini ayrı tutar; yapı görevlerini yalın kökün tek anlamına indirgemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan beş karşılaştırma başkalık, dışta bırakma, aşma, görüş ayrılığı ve değiştirme arasındaki en önemli sınırları kurar, diğer adaylar işlevce uzak veya yalnız tematiktir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dil bilgisel olumsuzlama ve farklılaşmaya uzanır; komşu dal ayrı yer veya yerine geçen unsur okumalarını ayrıca taşır.","focus_only":"Başkalığın yanında olumsuzlama görevini ve karşılıklı farklılaşmayı da kapsar.","gloss":"başka olma ve ayrı unsur","neighbor_only":"Konuşulana göre ayrı bir yerde bulunan veya onun yerini alan unsuru belirten kullanımları kapsar.","neighbor_ref":"root_000766/B007","relation_type":"near_synonym","shared_zone":"Bir şeyin belirtilen şeyle aynı olmayıp onun dışında kalan başka bir şey olması iki dalda ortaktır."},{"boundary_match":"partial","distinction":"Komşu dal yalnız dışta bırakma aracıdır; odak dal aynı işlevi daha geniş bir başkalık ve olumsuzluk ağının bir kullanımı olarak taşır.","focus_only":"Dışta bırakmanın yanında genel başkalık, aykırılık ve olumsuzlamayı da kapsar.","gloss":"genel başkalık ile dışta bırakma","neighbor_only":"Belirtilen unsuru bir hükmün kapsamından çıkarma işleviyle sınırlıdır.","neighbor_ref":"root_000436/B004","relation_type":"near_synonym","shared_zone":"Bir unsurun genel hükme giren kümeden ayrılıp kapsam dışında tutulması iki dalda aynıdır."},{"boundary_match":"partial","distinction":"Odak dal dışta bırakmayı başkalık ilişkisiyle kurar; komşu dal aynı işleve aşma ve ötesine geçme çekirdeğinden ulaşır.","focus_only":"Başkalık ve olumsuzlama anlamlarını, herhangi bir aşma hareketi olmadan da bildirir.","gloss":"dışta bırakma ile ötesine geçme","neighbor_only":"Bir şeyi geçip ötesine gitme ve bir konudan başka yöne sapma hareketlerini de kapsar.","neighbor_ref":"root_000993/B004","relation_type":"near_synonym","shared_zone":"Belirtilen unsurun genel kapsamın dışında tutulması iki dalın dil bilgisel kesişimidir."},{"boundary_match":"partial","distinction":"Odak dal çatışma gerektirmeyen genel ayrılığı bildirir; komşu dal farklı yönelim ve uyuşmazlık içeren daha belirgin bir ayrışmadır.","focus_only":"İki şeyin yalnız ayrı veya aynı olmayan varlıklar olmasını da kapsar.","gloss":"başkalık ile görüş ayrılığı","neighbor_only":"Tarafların ayrı yol, görüş veya tutum benimseyerek uyuşmazlığa düşmesini kapsar.","neighbor_ref":"root_000433/B004","relation_type":"near_neighbor","shared_zone":"İki tarafın nitelik, durum veya tutum bakımından aynı olmaması ortak alandır."},{"boundary_match":"partial","distinction":"Odak dal statik bir ilişki veya dil bilgisel işlev olabilir; komşu dal katılımcıları ve sonucu bulunan bir değişme ya da değiştirme olayıdır.","focus_only":"Değişim gerçekleşmeden de iki varlık arasında başkalık kurabilir ve dil bilgisel görev üstlenir.","gloss":"başkalık ile değiştirme","neighbor_only":"Bir şeyi farklı hale getiren süreç veya onun yerine başkasını koyan eylem gerektirir.","neighbor_ref":"root_001119/B003","relation_type":"near_neighbor","shared_zone":"Bir değiştirme sonucunda ilk halden veya nesneden başka bir hal ya da nesne ortaya çıkması ortak noktadır."}],"source_phrase_ar":"هذا الشيء غير ذاك أي هو سواه وخلافه (maqayis)؛ غير بمعنى سوى (sihah;tahdhib)؛ يوصف بها ويستثنى (sihah)؛ يكون استثناء (tahdhib)؛ يكون غير اسما (tahdhib)؛ معنى غير معنى لا (tahdhib)؛ للنفي المجرد (mufradat)؛ بمعنى إلا (mufradat)؛ لنفي صورة من غير مادتها (mufradat)؛ متناولا لذات (mufradat)؛ الغيرين أعم من المختلفين (mufradat)؛ تغايرت الأشياء اختلف (sihah)","source_summary":"Kaynaklar başkalığı aynı olmama ve aykırılık ilişkisi olarak verir; bu temel ilişki ad ve niteleyici kullanımına, bir unsuru dışta bırakmaya ve yalın olumsuzlamaya uzanır. Ayrıca karşılıklı farklılaşmayı kapsar ve yalnız anlaşmazlık bildiren daha dar ilişkiyle sınırlı değildir.","sources":["SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه كون الشيء سوى غيره وخلافه، واستعمال غير صفة أو اسما أو أداة استثناء، ومعنى لا، ونفي صورة أو ذات، وعموم الغيرين على المختلفين.","what_is_not_ar":"لا يدخل فيه فعل التغيير والتبديل إلا من جهة نشوء صورة أو بدل آخر، ولا الغِيرة بمعنى الميرة أو الحمية."},"support_links":["sup_a4a1c9feb353945848d7"]}],"candidate_inventory":[{"anchor_refs":["100:3:1"],"branch_refs":[],"candidate_id":"cand_148305864c2f0fde112f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:3:1:attached-boundary","source_type":"word_analysis","support_ids":["sup_55769b3e60fb453a12bc","sup_9f0b78f147ed8eb2c0c0"],"title":"bound particle makes the boundary thin","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:1","qac_refs":["100:3:1:1"],"status":"accepted"}},{"anchor_refs":["100:3:1"],"branch_refs":[],"candidate_id":"cand_1b3c506679e972c7c577","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:3:1:immediate-sequence-chain","source_type":"word_analysis","support_ids":["sup_2fe2fe48cf2a91b25036","sup_9f0b78f147ed8eb2c0c0"],"title":"immediate sequence in one oath chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:1","qac_refs":["100:3:1:1"],"status":"accepted"}},{"anchor_refs":["100:3:1"],"branch_refs":[],"candidate_id":"cand_2cf1e429c89cb343b21c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:3:1:opening-launch-frame","source_type":"word_analysis","support_ids":["sup_6b81bbc060303f30e7a1","sup_9f0b78f147ed8eb2c0c0"],"title":"opening particle launches the third phase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:1","qac_refs":["100:3:1:1"],"status":"accepted"}},{"anchor_refs":["100:3:1"],"branch_refs":[],"candidate_id":"cand_331f234b0aea390c97c3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:3:1:repeated-fa-reprise","source_type":"word_analysis","support_ids":["sup_69981af290bfe17e6fbe","sup_9f0b78f147ed8eb2c0c0"],"title":"repeated fāʾ reprises and projects the chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:1","qac_refs":["100:3:1:1"],"status":"accepted"}},{"anchor_refs":["100:3:2"],"branch_refs":[],"candidate_id":"cand_f2e8917aaf23e6360c1e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001119"],"scope":"focus_ayah","source_local_id":"100:3:2:agent-before-time","source_type":"word_analysis","support_ids":["sup_400335da821cf602ebdf","sup_4a70754603da60ce1205"],"title":"agent label arrives before dawn frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:2","qac_refs":["100:3:1:2","100:3:1:3"],"status":"accepted"}},{"anchor_refs":["100:3:2"],"branch_refs":[],"candidate_id":"cand_61f75eba6749d636daea","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001119"],"scope":"focus_ayah","source_local_id":"100:3:2:depth-image-incursion","source_type":"word_analysis","support_ids":["sup_400335da821cf602ebdf","sup_449c97268e8d5402ec0b"],"title":"depth image turns attack into incursion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:2","qac_refs":["100:3:1:2","100:3:1:3"],"status":"accepted"}},{"anchor_refs":["100:3:2"],"branch_refs":[],"candidate_id":"cand_85ff5d8b1ec27204361f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001119"],"scope":"focus_ayah","source_local_id":"100:3:2:form-echo-with-previous-oath","source_type":"word_analysis","support_ids":["sup_400335da821cf602ebdf","sup_5bffda9037acf6275395"],"title":"participial echo carries changed action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:2","qac_refs":["100:3:1:2","100:3:1:3"],"status":"accepted"}},{"anchor_refs":["100:3:2"],"branch_refs":[],"candidate_id":"cand_4903e79d7cd2f19261d3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001119"],"scope":"focus_ayah","source_local_id":"100:3:2:oath-governed-participle","source_type":"word_analysis","support_ids":["sup_400335da821cf602ebdf","sup_ccd3120d638e62df7a60"],"title":"genitive participle remains under oath governance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:2","qac_refs":["100:3:1:2","100:3:1:3"],"status":"accepted"}},{"anchor_refs":["100:3:2"],"branch_refs":[],"candidate_id":"cand_07b0eb348d24caa78927","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001119"],"scope":"focus_ayah","source_local_id":"100:3:2:plural-agent-continuity","source_type":"word_analysis","support_ids":["sup_400335da821cf602ebdf","sup_a949d6bb7f44fb84c0e9"],"title":"feminine plural participle carries the same agents","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:2","qac_refs":["100:3:1:2","100:3:1:3"],"status":"accepted"}},{"anchor_refs":["100:3:2"],"branch_refs":[],"candidate_id":"cand_91fc862d53f99fa50a28","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001119"],"scope":"focus_ayah","source_local_id":"100:3:2:raid-descent-root-dispute","source_type":"word_analysis","support_ids":["sup_400335da821cf602ebdf","sup_5e854536b27aa7a6e899"],"title":"raid descent selected over change","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:2","qac_refs":["100:3:1:2","100:3:1:3"],"status":"accepted"}},{"anchor_refs":["100:3:2"],"branch_refs":[],"candidate_id":"cand_30912afad1318b453602","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001119"],"scope":"focus_ayah","source_local_id":"100:3:2:rare-form-iv","source_type":"word_analysis","support_ids":["sup_0615a314e0348df503e5","sup_400335da821cf602ebdf"],"title":"rare Form IV raid participle","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:2","qac_refs":["100:3:1:2","100:3:1:3"],"status":"accepted"}},{"anchor_refs":["100:3:2"],"branch_refs":[],"candidate_id":"cand_3c72343f21dfd08bfa1f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001119"],"scope":"focus_ayah","source_local_id":"100:3:2:sound-texture-descent","source_type":"word_analysis","support_ids":["sup_10ff96816b0cb2e3e186","sup_400335da821cf602ebdf"],"title":"sound texture enacts descent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:2","qac_refs":["100:3:1:2","100:3:1:3"],"status":"accepted"}},{"anchor_refs":["100:3:2"],"branch_refs":[],"candidate_id":"cand_30baaae75399de18ce43","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001119"],"scope":"focus_ayah","source_local_id":"100:3:2:transition-from-sparks-to-raid","source_type":"word_analysis","support_ids":["sup_400335da821cf602ebdf","sup_526547b2da9cee89ba43"],"title":"spark impact becomes directed assault","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:2","qac_refs":["100:3:1:2","100:3:1:3"],"status":"accepted"}},{"anchor_refs":["100:3:3"],"branch_refs":[],"candidate_id":"cand_de3fc4fea4cd29824ff3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000839"],"scope":"focus_ayah","source_local_id":"100:3:3:brightness-pressure","source_type":"word_analysis","support_ids":["sup_d032b16887e2812e6615","sup_f110c9cced1a2cda89b8"],"title":"dawn time carries brightness pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:3","qac_refs":["100:3:2:1"],"status":"accepted"}},{"anchor_refs":["100:3:3"],"branch_refs":[],"candidate_id":"cand_9b78b5442280e332b9f8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000839"],"scope":"focus_ayah","source_local_id":"100:3:3:cadence-and-sound","source_type":"word_analysis","support_ids":["sup_1f2f9a5e11d97283bb0f","sup_f110c9cced1a2cda89b8"],"title":"short ending binds the oath beats","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:3","qac_refs":["100:3:2:1"],"status":"accepted"}},{"anchor_refs":["100:3:3"],"branch_refs":[],"candidate_id":"cand_bca1f57ddd64a3b92343","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000839"],"scope":"focus_ayah","source_local_id":"100:3:3:convergence-summary","source_type":"word_analysis","support_ids":["sup_a254b952b3ce70cfe051","sup_f110c9cced1a2cda89b8"],"title":"grammar brightness cadence and boundary converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:3","qac_refs":["100:3:2:1"],"status":"accepted"}},{"anchor_refs":["100:3:3"],"branch_refs":[],"candidate_id":"cand_eb4d379c46926b43dd58","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000839"],"scope":"focus_ayah","source_local_id":"100:3:3:emphatic-sound-release","source_type":"word_analysis","support_ids":["sup_f110c9cced1a2cda89b8","sup_f3756e7d84e1db1e5a8e"],"title":"sound texture opens into visibility","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:3","qac_refs":["100:3:2:1"],"status":"accepted"}},{"anchor_refs":["100:3:3"],"branch_refs":[],"candidate_id":"cand_b1c8003ed2e3a5d55cbd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000839"],"scope":"focus_ayah","source_local_id":"100:3:3:indefinite-dawn-slot","source_type":"word_analysis","support_ids":["sup_5397df8a5ace1e1aeadc","sup_f110c9cced1a2cda89b8"],"title":"indefinite dawn as reusable threshold","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:3","qac_refs":["100:3:2:1"],"status":"accepted"}},{"anchor_refs":["100:3:3"],"branch_refs":[],"candidate_id":"cand_e6063385513daf6103fc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000839"],"scope":"focus_ayah","source_local_id":"100:3:3:marked-adverbial-form","source_type":"word_analysis","support_ids":["sup_9a230854852cdd228440","sup_f110c9cced1a2cda89b8"],"title":"common root in marked adverbial slot","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:3","qac_refs":["100:3:2:1"],"status":"accepted"}},{"anchor_refs":["100:3:3"],"branch_refs":[],"candidate_id":"cand_f880c8228ddc26c54979","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000839"],"scope":"focus_ayah","source_local_id":"100:3:3:morning-sinking-root-pair","source_type":"word_analysis","support_ids":["sup_a40b1074ed02539bf502","sup_f110c9cced1a2cda89b8"],"title":"morning sinking root-pair echo","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:3","qac_refs":["100:3:2:1"],"status":"accepted"}},{"anchor_refs":["100:3:3"],"branch_refs":[],"candidate_id":"cand_45eea3ac92c500c7a8a2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000839"],"scope":"focus_ayah","source_local_id":"100:3:3:structural-closure","source_type":"word_analysis","support_ids":["sup_9114dd85b094432e6cd7","sup_f110c9cced1a2cda89b8"],"title":"closing word grounds the scene","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:3","qac_refs":["100:3:2:1"],"status":"accepted"}},{"anchor_refs":["100:3:3"],"branch_refs":[],"candidate_id":"cand_a9f88121cbf65304f3f1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000839"],"scope":"focus_ayah","source_local_id":"100:3:3:tanwin-rhyme-openness","source_type":"word_analysis","support_ids":["sup_cc210d3f27e317e69d31","sup_f110c9cced1a2cda89b8"],"title":"tanwīn joins openness and rhyme","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:3","qac_refs":["100:3:2:1"],"status":"accepted"}},{"anchor_refs":["100:3:3"],"branch_refs":[],"candidate_id":"cand_0f69047d7b7931b02f60","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000839"],"scope":"focus_ayah","source_local_id":"100:3:3:temporal-adverb-pivot","source_type":"word_analysis","support_ids":["sup_2000c03f0548fd1422ed","sup_f110c9cced1a2cda89b8"],"title":"first explicit time marker","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:3","qac_refs":["100:3:2:1"],"status":"accepted"}},{"anchor_refs":["100:3:3"],"branch_refs":[],"candidate_id":"cand_9fd496fdc574a25cebe3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000839"],"scope":"focus_ayah","source_local_id":"100:3:3:visibility-boundary","source_type":"word_analysis","support_ids":["sup_464c972a92d6a2e62f1b","sup_f110c9cced1a2cda89b8"],"title":"hidden sparks open into visible aftermath","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:3:3","qac_refs":["100:3:2:1"],"status":"accepted"}},{"anchor_refs":["100:3:1"],"branch_refs":[],"candidate_id":"cand_a71de77cc84b6aff66d0","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001119"],"scope":"focus_ayah","source_local_id":"100:3:1:3","source_type":"qac_morpheme","support_ids":["sup_9f81639abb40a4e054ab"],"title":"QAC root occurrence: غ ي ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["100:3:2"],"branch_refs":[],"candidate_id":"cand_a5bb54ca99339a4ca7e5","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000839"],"scope":"focus_ayah","source_local_id":"100:3:2:1","source_type":"qac_morpheme","support_ids":["sup_4a3fd2b8418af77b0dda"],"title":"QAC root occurrence: ص ب ح","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["100:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:3","branch_refs":["root_000839/B004","root_001119/B003"],"candidate_id":"cand_f44be94b687673187adf","commentary_obligation":"review","hft_ref":"hft_f44272ddf26d73323f2d","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_dawn_incursion","source_type":"hft","support_ids":["sup_ede12c0b4743228f42e3"],"title":"b_dawn_incursion","trust":"legacy_unbound"},{"anchor_refs":["100:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:3","branch_refs":["root_000839/B001","root_000839/B005","root_000839/B010","root_001119/B003"],"candidate_id":"cand_0c7b074eb10aaa08cdf2","commentary_obligation":"review","hft_ref":"hft_e3cb0a2da07b327a2bad","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_threshold_illumination","source_type":"hft","support_ids":["sup_d3b888abd29b6646cdfa"],"title":"b_threshold_illumination","trust":"legacy_unbound"},{"anchor_refs":["100:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:3","branch_refs":["root_000839/B002","root_000839/B003","root_001119/B001"],"candidate_id":"cand_cd3328592ade1b49eed6","commentary_obligation":"review","hft_ref":"hft_9bdadae5c4e9098d2eb2","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_morning_provision_repair","source_type":"hft","support_ids":["sup_feb6fc0376d933cc80e4"],"title":"b_morning_provision_repair","trust":"legacy_unbound"},{"anchor_refs":["100:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:3","branch_refs":["root_000839/B004","root_001119/B004"],"candidate_id":"cand_a8a61d657d3a0abe682d","commentary_obligation":"review","hft_ref":"hft_9125841937c99d5de37f","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_alarm_protection","source_type":"hft","support_ids":["sup_676ab9ce38ab7596ff3d"],"title":"b_alarm_protection","trust":"legacy_unbound"},{"anchor_refs":["100:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:3","branch_refs":["root_000839/B004","root_001119/B003"],"candidate_id":"cand_c351588bd21c2fecc21d","commentary_obligation":"review","hft_ref":"hft_46ef1c4f0b1b5e41f265","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:5.5-high:B_FOCUS_RAID_AS_STATE_CHANGE_AT_DAWN","source_type":"hft","support_ids":["sup_99d1441af33b566c0ef7"],"title":"B_FOCUS_RAID_AS_STATE_CHANGE_AT_DAWN","trust":"legacy_unbound"},{"anchor_refs":["100:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:3","branch_refs":["root_000839/B001","root_001119/B005"],"candidate_id":"cand_6e9ffb2a8a39f1b2cee0","commentary_obligation":"review","hft_ref":"hft_345c7684e16f103deeb5","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:5.5-high:B_FOCUS_OTHERNESS_THRESHOLD","source_type":"hft","support_ids":["sup_a4a1c9feb353945848d7"],"title":"B_FOCUS_OTHERNESS_THRESHOLD","trust":"legacy_unbound"},{"anchor_refs":["100:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:3","branch_refs":["root_000839/B003","root_001119/B001"],"candidate_id":"cand_d0d12a26184bc0eaf69c","commentary_obligation":"review","hft_ref":"hft_d76384e40c77070ec4be","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:5.5-high:B_FOCUS_PROVISIONING_MORNING","source_type":"hft","support_ids":["sup_fd5a5122ca86f0459b2b"],"title":"B_FOCUS_PROVISIONING_MORNING","trust":"legacy_unbound"},{"anchor_refs":["100:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:3","branch_refs":["root_000839/B004","root_001119/B003"],"candidate_id":"cand_32f991bec03f6d64e758","commentary_obligation":"review","hft_ref":"hft_a17576d317d8f85eaf23","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:5.6-sol-high:base_dawn_incursion","source_type":"hft","support_ids":["sup_6a8ac57b6f912566a6a4"],"title":"base_dawn_incursion","trust":"legacy_unbound"},{"anchor_refs":["100:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:3","branch_refs":["root_000839/B001","root_000839/B010","root_001119/B003"],"candidate_id":"cand_f4cd976dd5b09f55f1e3","commentary_obligation":"review","hft_ref":"hft_456434b46663694bdfc1","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:5.6-sol-high:base_threshold_transformation","source_type":"hft","support_ids":["sup_06261e4e0407d44d3182"],"title":"base_threshold_transformation","trust":"legacy_unbound"},{"anchor_refs":["100:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:3","branch_refs":["root_000839/B002","root_001119/B003"],"candidate_id":"cand_b1791aab2dede7d650cc","commentary_obligation":"review","hft_ref":"hft_7b5be23d8a002983d758","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:5.6-sol-high:base_morning_arrival","source_type":"hft","support_ids":["sup_2955648f213d1d0ae095"],"title":"base_morning_arrival","trust":"legacy_unbound"},{"anchor_refs":["100:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:3","branch_refs":["root_000839/B003","root_001119/B001"],"candidate_id":"cand_186caec22cfe3806faaf","commentary_obligation":"review","hft_ref":"hft_caf5c8688c2abf5b77b3","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:5.6-sol-high:base_provisioning_counterreading","source_type":"hft","support_ids":["sup_826d14e70aa61f73702c"],"title":"base_provisioning_counterreading","trust":"legacy_unbound"},{"anchor_refs":["100:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:3","branch_refs":["root_000839/B008","root_001119/B003"],"candidate_id":"cand_ac884102b47a800d9d54","commentary_obligation":"review","hft_ref":"hft_59b0c86d69db714cda7d","kind":"surprising_outlier","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:5.6-sol-high:outlier_morning_stasis_breached","source_type":"hft","support_ids":["sup_d26ef228057789f5d9a8"],"title":"outlier_morning_stasis_breached","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فَٱلْمُغِيرَٰتِ صُبْحًۭا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"100:3:1:1","qac_word_ref":"100:3:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"100:3:1:2","qac_word_ref":"100:3:1","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"مُغِيرَٰت","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:mugiyra`t|ROOT:gyr|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:3:1:3","qac_word_ref":"100:3:1","root_ar":"غ ي ر","surface_ar":"مُغِيرَٰتِ"},{"lemma_ar":"صُبْح","morph_features":"STEM|POS:T|LEM:SuboH|ROOT:SbH|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"100:3:2:1","qac_word_ref":"100:3:2","root_ar":"ص ب ح","surface_ar":"صُبْحًا"}],"word_analysis_qac_refs":[["100:3:1:1"],["100:3:1:2","100:3:1:3"],["100:3:2:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["100:3:1","100:3:2","100:3:3"]},"focus_surface_evidence":{"arabic_uthmani":"فَٱلْمُغِيرَٰتِ صُبْحًۭا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"100:3:1:1","qac_word_ref":"100:3:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"100:3:1:2","qac_word_ref":"100:3:1","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"مُغِيرَٰت","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:mugiyra`t|ROOT:gyr|FP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:3:1:3","qac_word_ref":"100:3:1","root_ar":"غ ي ر","surface_ar":"مُغِيرَٰتِ"},{"lemma_ar":"صُبْح","morph_features":"STEM|POS:T|LEM:SuboH|ROOT:SbH|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"100:3:2:1","qac_word_ref":"100:3:2","root_ar":"ص ب ح","surface_ar":"صُبْحًا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["100:3:1:1"],["100:3:1:2","100:3:1:3"],["100:3:2:1"]],"word_analysis_refs":["100:3:1","100:3:2","100:3:3"],"word_rows":[{"analysis_record_ref":"100:3:1","analytic_gloss_range_en":"immediate-sequence connective that keeps the third oath beat joined to the prior spark-striking beat and pushes the action forward","analytic_root_gloss_range_en":null,"qac_refs":["100:3:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"فَ","transliteration":"fa-"}},{"analysis_record_ref":"100:3:2","analytic_gloss_range_en":"definite feminine plural Form IV active participle naming raiding or descending agents; the local oath scene selects the raid/descent reading while keeping the homophonous change derivation as a constrained contrast","analytic_root_gloss_range_en":"contested homophonous range: one side carries depth, sinking, caves, and sudden raiding or descent; the other carries change or otherness, which is contrastive here rather than the selected local sense","qac_refs":["100:3:1:2","100:3:1:3"],"root":{"arabic":"غ و ر / غ ي ر","transliteration":"gh-w-r / gh-y-r"},"surface":{"arabic":"ٱلْمُغِيرَٰتِ","transliteration":"al-mughīrāti"}},{"analysis_record_ref":"100:3:3","analytic_gloss_range_en":"indefinite accusative dawn-time adverb locating the raid at a repeatable threshold of morning visibility, with brightness pressure retained but wider root branches locally constrained","analytic_root_gloss_range_en":"root range around dawn and morning opening, coming in the morning, morning raid, light, brightness or beauty, morning drink, and becoming; local grammar selects dawn as the temporal frame","qac_refs":["100:3:2:1"],"root":{"arabic":"ص ب ح","transliteration":"ṣ-b-ḥ"},"surface":{"arabic":"صُبْحًۭا","transliteration":"ṣubḥan"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":12,"assigned_records":[{"anchor_refs":["100:3"],"branch_refs":["root_000839/B004","root_001119/B003"],"candidate_id":"cand_f44be94b687673187adf","evidence_scope":"focus_ayah","hft_ref":"hft_f44272ddf26d73323f2d","item_id":"b_dawn_incursion","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_dawn_incursion","support_id":"sup_ede12c0b4743228f42e3"},{"anchor_refs":["100:3"],"branch_refs":["root_000839/B001","root_000839/B005","root_000839/B010","root_001119/B003"],"candidate_id":"cand_0c7b074eb10aaa08cdf2","evidence_scope":"focus_ayah","hft_ref":"hft_e3cb0a2da07b327a2bad","item_id":"b_threshold_illumination","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_threshold_illumination","support_id":"sup_d3b888abd29b6646cdfa"},{"anchor_refs":["100:3"],"branch_refs":["root_000839/B002","root_000839/B003","root_001119/B001"],"candidate_id":"cand_cd3328592ade1b49eed6","evidence_scope":"focus_ayah","hft_ref":"hft_9bdadae5c4e9098d2eb2","item_id":"b_morning_provision_repair","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_morning_provision_repair","support_id":"sup_feb6fc0376d933cc80e4"},{"anchor_refs":["100:3"],"branch_refs":["root_000839/B004","root_001119/B004"],"candidate_id":"cand_a8a61d657d3a0abe682d","evidence_scope":"focus_ayah","hft_ref":"hft_9125841937c99d5de37f","item_id":"b_alarm_protection","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_alarm_protection","support_id":"sup_676ab9ce38ab7596ff3d"},{"anchor_refs":["100:3"],"branch_refs":["root_000839/B004","root_001119/B003"],"candidate_id":"cand_c351588bd21c2fecc21d","evidence_scope":"focus_ayah","hft_ref":"hft_46ef1c4f0b1b5e41f265","item_id":"B_FOCUS_RAID_AS_STATE_CHANGE_AT_DAWN","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a:5.5-high","source_local_id":"reader_hft_a:5.5-high:B_FOCUS_RAID_AS_STATE_CHANGE_AT_DAWN","support_id":"sup_99d1441af33b566c0ef7"},{"anchor_refs":["100:3"],"branch_refs":["root_000839/B001","root_001119/B005"],"candidate_id":"cand_6e9ffb2a8a39f1b2cee0","evidence_scope":"focus_ayah","hft_ref":"hft_345c7684e16f103deeb5","item_id":"B_FOCUS_OTHERNESS_THRESHOLD","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a:5.5-high","source_local_id":"reader_hft_a:5.5-high:B_FOCUS_OTHERNESS_THRESHOLD","support_id":"sup_a4a1c9feb353945848d7"},{"anchor_refs":["100:3"],"branch_refs":["root_000839/B003","root_001119/B001"],"candidate_id":"cand_d0d12a26184bc0eaf69c","evidence_scope":"focus_ayah","hft_ref":"hft_d76384e40c77070ec4be","item_id":"B_FOCUS_PROVISIONING_MORNING","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a:5.5-high","source_local_id":"reader_hft_a:5.5-high:B_FOCUS_PROVISIONING_MORNING","support_id":"sup_fd5a5122ca86f0459b2b"},{"anchor_refs":["100:3"],"branch_refs":["root_000839/B004","root_001119/B003"],"candidate_id":"cand_32f991bec03f6d64e758","evidence_scope":"focus_ayah","hft_ref":"hft_a17576d317d8f85eaf23","item_id":"base_dawn_incursion","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a:5.6-sol-high","source_local_id":"reader_hft_a:5.6-sol-high:base_dawn_incursion","support_id":"sup_6a8ac57b6f912566a6a4"},{"anchor_refs":["100:3"],"branch_refs":["root_000839/B001","root_000839/B010","root_001119/B003"],"candidate_id":"cand_f4cd976dd5b09f55f1e3","evidence_scope":"focus_ayah","hft_ref":"hft_456434b46663694bdfc1","item_id":"base_threshold_transformation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a:5.6-sol-high","source_local_id":"reader_hft_a:5.6-sol-high:base_threshold_transformation","support_id":"sup_06261e4e0407d44d3182"},{"anchor_refs":["100:3"],"branch_refs":["root_000839/B002","root_001119/B003"],"candidate_id":"cand_b1791aab2dede7d650cc","evidence_scope":"focus_ayah","hft_ref":"hft_7b5be23d8a002983d758","item_id":"base_morning_arrival","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a:5.6-sol-high","source_local_id":"reader_hft_a:5.6-sol-high:base_morning_arrival","support_id":"sup_2955648f213d1d0ae095"},{"anchor_refs":["100:3"],"branch_refs":["root_000839/B003","root_001119/B001"],"candidate_id":"cand_186caec22cfe3806faaf","evidence_scope":"focus_ayah","hft_ref":"hft_caf5c8688c2abf5b77b3","item_id":"base_provisioning_counterreading","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a:5.6-sol-high","source_local_id":"reader_hft_a:5.6-sol-high:base_provisioning_counterreading","support_id":"sup_826d14e70aa61f73702c"},{"anchor_refs":["100:3"],"branch_refs":["root_000839/B008","root_001119/B003"],"candidate_id":"cand_ac884102b47a800d9d54","evidence_scope":"focus_ayah","hft_ref":"hft_59b0c86d69db714cda7d","item_id":"outlier_morning_stasis_breached","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a:5.6-sol-high","source_local_id":"reader_hft_a:5.6-sol-high:outlier_morning_stasis_breached","support_id":"sup_d26ef228057789f5d9a8"}],"diagnostics":[{"warning":"Unrecognized HFT reader field is preserved as a global review record"},{"warning":"Unrecognized HFT reader field is preserved as a global review record"},{"warning":"Unrecognized HFT reader field is preserved as a global review record"},{"warning":"Unrecognized HFT reader field is preserved as a global review record"},{"warning":"Unrecognized HFT reader field is preserved as a global review record"},{"warning":"Unrecognized HFT reader field is preserved as a global review record"}],"lane_counts":{"global":34,"macro":37,"micro":12},"packet_summary":{"ayah_count":11,"focus_ref":"100:3","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ع د و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000993","furuq_root_norm":"ع د و","furuq_source_root_norm":"ع د و","is_dominant":true,"target_occurrences":68,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":5,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":false,"target_occurrences":4,"target_rank":3}]},{"qac_root":"ث و ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000210","furuq_root_norm":"ث و ر","furuq_source_root_norm":"ث و ر","is_dominant":true,"target_occurrences":4,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000011","furuq_root_norm":"ء ث ر","furuq_source_root_norm":"أ ث ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["100:1","100:2","100:3","100:4","100:5","100:6","100:7","100:8","100:9","100:10","100:11"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"100:3","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v3","reader_id":"reader_hft_a","trace_kind":null},{"focus_ref":"100:3","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v3","reader_id":"reader_hft_a:5.5-high","trace_kind":null},{"focus_ref":"100:3","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v3","reader_id":"reader_hft_a:5.6-sol-high","trace_kind":null}]},"reader_synthesis_count":28,"source_present":true,"structured_insight_count":49,"unstructured_record_count":6},"identity":{"ayah_ref":"100:3","lane":"micro","linguistic_source_ref":"100:3","surface_ref":"100:3","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"100:3","target_tokens":[["Ardından",["100:3:1"]],["sabah",["100:3:2"]],["vakti",["100:3:2"]],["baskın",["100:3:1"]],["yapanlara",["100:3:1"]]],"text":"Ardından sabah vakti baskın yapanlara,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":12,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":11,"id":"s100-p01-001-011","label":"Whole surah","number":1,"refs":["100:1","100:2","100:3","100:4","100:5","100:6","100:7","100:8","100:9","100:10","100:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:2:rare-form-iv","source_type":"word_analysis","support_id":"sup_0615a314e0348df503e5","text":"{\"blocking_evidence\":null,\"headline\":\"rare Form IV raid participle\",\"reader_payoff\":\"The reader notices that the oath concentrates the raid sense in a marked Form IV participial choice rather than in repeated ordinary vocabulary.\",\"reason\":\"The contextual profile marks the exact root/form as low-occurrence, and no guardrail contradicts the CRITICAL claim that the local Form IV participle is distributionally marked.\",\"representative_source_ids\":[\"QI-550e2d74\",\"QI-7e6a4884\",\"QH-685cf619\",\"QH-9a86a55f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:2:sound-texture-descent","source_type":"word_analysis","support_id":"sup_10ff96816b0cb2e3e186","text":"{\"blocking_evidence\":null,\"headline\":\"sound texture enacts descent\",\"reader_payoff\":\"The reader notices the word's heavy-to-flowing sound as part of the felt rush into arrival.\",\"reason\":\"The phonetic rows do not override grammar; they add a distinct sound payoff that coheres with the selected raid/descent reading.\",\"representative_source_ids\":[\"QP-55111839\",\"QP-6acf9371\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:3:cadence-and-sound","source_type":"word_analysis","support_id":"sup_1f2f9a5e11d97283bb0f","text":"{\"blocking_evidence\":null,\"headline\":\"short ending binds the oath beats\",\"reader_payoff\":\"The reader hears the third oath line as acoustically bound to the first two while its meaning advances from breath and impact to time.\",\"reason\":\"The final tanwīn and short cadence create a distinct sound payoff that supports, but does not replace, the grammatical time role.\",\"representative_source_ids\":[\"QF-95f69d06\",\"QE-a5dded4e\",\"QE-b2f88f4f\",\"QP-503bf22b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:3:temporal-adverb-pivot","source_type":"word_analysis","support_id":"sup_2000c03f0548fd1422ed","text":"{\"blocking_evidence\":null,\"headline\":\"first explicit time marker\",\"reader_payoff\":\"The reader notices the oath sequence pivoting from manner and impact into a concrete time frame.\",\"reason\":\"QAC and attachment evidence identify the word as an accusative time adverb locating the raid, so the temporal-adverb reading is strongly licensed while looser specification is secondary.\",\"representative_source_ids\":[\"QG-a1c1c619\",\"QS-0e833d8c\",\"QT-3c3b378e\",\"QY-dc8160a8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:1:immediate-sequence-chain","source_type":"word_analysis","support_id":"sup_2fe2fe48cf2a91b25036","text":"{\"blocking_evidence\":null,\"headline\":\"immediate sequence in one oath chain\",\"reader_payoff\":\"The reader notices that 100:3 is not a flat new list item but the next phase produced by the motion and sparks of 100:1-2.\",\"reason\":\"QAC identifies the particle as a conjunction with immediate-sequence force, and the CRITICAL rows coherently read the repeated fāʾ as narrative escalation inside the oath sequence.\",\"representative_source_ids\":[\"QG-d4fc80d9\",\"MG-94bb73a9\",\"QS-21c025d9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:2","source_type":"word_analysis","support_id":"sup_400335da821cf602ebdf","text":"{\"gloss_range\":\"definite feminine plural Form IV active participle naming raiding or descending agents; the local oath scene selects the raid/descent reading while keeping the homophonous change derivation as a constrained contrast\",\"prose\":\"{{ar:ٱلْمُغِيرَٰتِ}} ({{tr:al-mughīrāti}}) is the lexical payload of the ayah: a definite feminine plural Form IV active participle, still genitive under the oath governance that began in 100:1. The article and long plural ending name an acting class through morphology rather than a separate noun, keeping the same agents moving from the previous feminine plural oath terms. The repeated participial shape lets the listener hear continuity while the action changes from kindling sparks to raiding, and the word order gives the acting class before the dawn frame. The root dispute is locally narrowed by the scene: the selected reading is raiding or descending upon, not a free change sense. That matters because the word turns the spark-impact of 100:2 into organized incursion, and the depth/descent pressure makes the raid feel like a sudden movement out of concealment onto a target. Its rare Form IV deployment and heavy-to-flowing sound, from deep onset through long vowel into the plural ending, concentrate the oath line around one charged descent word.\",\"root_display\":\"{{ar:غ و ر / غ ي ر}} ({{tr:gh-w-r / gh-y-r}})\",\"root_gloss_range\":\"contested homophonous range: one side carries depth, sinking, caves, and sudden raiding or descent; the other carries change or otherness, which is contrastive here rather than the selected local sense\",\"surface_display\":\"{{ar:ٱلْمُغِيرَٰتِ}} ({{tr:al-mughīrāti}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:2:depth-image-incursion","source_type":"word_analysis","support_id":"sup_449c97268e8d5402ec0b","text":"{\"blocking_evidence\":null,\"headline\":\"depth image turns attack into incursion\",\"reader_payoff\":\"The reader feels the raid as a descent from concealment onto a target, not merely as a generic attack.\",\"reason\":\"The selected raid reading is locally licensed, and the depth/descent pressure survives as image-pressure without replacing the participle's grammatical role.\",\"representative_source_ids\":[\"QS-45759a65\",\"QY-377b25f8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:3:visibility-boundary","source_type":"word_analysis","support_id":"sup_464c972a92d6a2e62f1b","text":"{\"blocking_evidence\":null,\"headline\":\"hidden sparks open into visible aftermath\",\"reader_payoff\":\"The reader sees the lighting of the sequence change from sparks in darkness to visible dawn and then to visible dust in 100:4.\",\"reason\":\"The dawn-time role and brightness branch support the boundary payoff, and the bundle explicitly allows reading this ayah within the 100:4-100:5 window.\",\"representative_source_ids\":[\"QB-0773b960\",\"QB-8aaf7c13\",\"QB-be13ffd4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"100:3:2:1","source_type":"qac_morpheme","support_id":"sup_4a3fd2b8418af77b0dda","text":"{\"lemma_ar\":\"صُبْح\",\"morph_features\":\"STEM|POS:T|LEM:SuboH|ROOT:SbH|M|INDEF|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"T\",\"qac_ref\":\"100:3:2:1\",\"qac_word_ref\":\"100:3:2\",\"root_ar\":\"ص ب ح\",\"surface_ar\":\"صُبْحًا\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:2:agent-before-time","source_type":"word_analysis","support_id":"sup_4a70754603da60ce1205","text":"{\"blocking_evidence\":null,\"headline\":\"agent label arrives before dawn frame\",\"reader_payoff\":\"The reader first receives the acting class and only afterward learns the time of the raid.\",\"reason\":\"Attachment evidence makes the following word an adverbial dependent of this participle, confirming the local order from agent label to time frame.\",\"representative_source_ids\":[\"QT-eece8186\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:2:transition-from-sparks-to-raid","source_type":"word_analysis","support_id":"sup_526547b2da9cee89ba43","text":"{\"blocking_evidence\":null,\"headline\":\"spark impact becomes directed assault\",\"reader_payoff\":\"The reader sees the scene scale up from localized impact in 100:2 to a directed incursion in 100:3.\",\"reason\":\"The participle names the raiding agents before the dawn adverb attaches to it, so the boundary shift from spark production to raiding is locally coherent.\",\"representative_source_ids\":[\"QT-c49a415f\",\"QB-243b8f0b\",\"QB-e61aba94\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:3:indefinite-dawn-slot","source_type":"word_analysis","support_id":"sup_5397df8a5ace1e1aeadc","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite dawn as reusable threshold\",\"reader_payoff\":\"The reader notices dawn as a kind of repeated threshold, not as one named morning on a calendar.\",\"reason\":\"The indefinite accusative noun functions adverbially, and V4's dawn/morning branch supports the local temporal frame.\",\"representative_source_ids\":[\"QG-0e9fb5ad\",\"QF-4d6c5168\",\"QF-8dbe2db2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:1:attached-boundary","source_type":"word_analysis","support_id":"sup_55769b3e60fb453a12bc","text":"{\"blocking_evidence\":null,\"headline\":\"bound particle makes the boundary thin\",\"reader_payoff\":\"The reader hears the verse boundary as joined, because the particle attaches to the following word instead of letting the ayah feel like a fresh start.\",\"reason\":\"The local surface is a proclitic connector before an article-bearing participle, so the row's thin-boundary and liaison payoff is locally licensed.\",\"representative_source_ids\":[\"QF-e243c91b\",\"QT-09554875\",\"QP-a083aca9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:2:form-echo-with-previous-oath","source_type":"word_analysis","support_id":"sup_5bffda9037acf6275395","text":"{\"blocking_evidence\":null,\"headline\":\"participial echo carries changed action\",\"reader_payoff\":\"The reader hears continuity in the repeated participial shape while the root action changes from kindling to raiding.\",\"reason\":\"The neighboring oath terms share a definite feminine plural participial frame, making the formal echo locally visible.\",\"representative_source_ids\":[\"QE-aa220e8f\",\"QE-b1e69196\",\"QF-bd78f252\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:2:raid-descent-root-dispute","source_type":"word_analysis","support_id":"sup_5e854536b27aa7a6e899","text":"{\"blocking_evidence\":null,\"headline\":\"raid descent selected over change\",\"reader_payoff\":\"The reader notices a real derivational ambiguity, but the local scene channels it toward sudden raiding and descent rather than letting the change-root govern the word.\",\"reason\":\"The Form IV active participle is homophonous across the two proposed roots, but the local sequence of running, sparks, and dawn raid selects the raiding/descent reading; missing V4 rows for this root are not evidence against the coherent CRITICAL topic.\",\"representative_source_ids\":[\"MG-8eb28d82\",\"QS-cc65bf62\",\"QS-e4e25381\",\"QS-f53701f7\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:1:repeated-fa-reprise","source_type":"word_analysis","support_id":"sup_69981af290bfe17e6fbe","text":"{\"blocking_evidence\":null,\"headline\":\"repeated fāʾ reprises and projects the chain\",\"reader_payoff\":\"The reader notices the repeated connector as a rhythmic and structural device carrying the agents from 100:2 through 100:3 and toward 100:4.\",\"reason\":\"The same connective opens the adjacent oath beats, and the bundle's translation-support note warns that the ayah should be read in its surrounding sequence.\",\"representative_source_ids\":[\"QE-82a1348c\",\"QB-31c7b5db\",\"QB-c145021c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:1:opening-launch-frame","source_type":"word_analysis","support_id":"sup_6b81bbc060303f30e7a1","text":"{\"blocking_evidence\":null,\"headline\":\"opening particle launches the third phase\",\"reader_payoff\":\"The reader receives the verse first as continuation inside the qasam frame before any lexical image appears.\",\"reason\":\"The particle is the first word of the ayah and locally precedes the agentive participle, so it sets the launch frame before the lexical payload.\",\"representative_source_ids\":[\"QT-54c670dd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:3:structural-closure","source_type":"word_analysis","support_id":"sup_9114dd85b094432e6cd7","text":"{\"blocking_evidence\":null,\"headline\":\"closing word grounds the scene\",\"reader_payoff\":\"The reader feels the verse land at dawn only after the agentive raid word has already arrived.\",\"reason\":\"The time adverb follows and depends on the raiding participle, so the ayah delays temporal grounding until its final word.\",\"representative_source_ids\":[\"QI-da0d07f0\",\"QT-176fe261\",\"QT-5ab546ae\",\"QB-b651c6d5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:3:marked-adverbial-form","source_type":"word_analysis","support_id":"sup_9a230854852cdd228440","text":"{\"blocking_evidence\":null,\"headline\":\"common root in marked adverbial slot\",\"reader_payoff\":\"The reader notices that a broad root family is narrowed here into a compact oath-framing time adverb.\",\"reason\":\"The contextual and role profiles mark the exact form as low-occurrence and adverbial; V4 branch breadth supports narrowing broad root material to the local time use.\",\"representative_source_ids\":[\"QI-84bf0662\",\"QI-a8222d07\",\"QH-3e2a7527\",\"QH-aea73b9f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:1","source_type":"word_analysis","support_id":"sup_9f0b78f147ed8eb2c0c0","text":"{\"gloss_range\":\"immediate-sequence connective that keeps the third oath beat joined to the prior spark-striking beat and pushes the action forward\",\"prose\":\"{{ar:فَ}} ({{tr:fa-}}) makes the ayah continue rather than restart. As the first word, before any noun appears, it launches the third phase inside the already-opened oath frame. It carries the action from the spark-striking of 100:2 into the dawn raid as immediate sequence, with a consequential feel: the prior motion has produced this next phase. Because the particle is bound to the following agent label in pronunciation and spelling, the reader hears connection before receiving the new image. Its repetition from 100:2 and anticipation of the next fāʾ-driven action in 100:4 make this small particle a hinge in one accelerating oath chain.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa-}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"100:3:1:3","source_type":"qac_morpheme","support_id":"sup_9f81639abb40a4e054ab","text":"{\"lemma_ar\":\"مُغِيرَٰت\",\"morph_features\":\"STEM|POS:N|ACT|PCPL|(IV)|LEM:mugiyra`t|ROOT:gyr|FP|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"100:3:1:3\",\"qac_word_ref\":\"100:3:1\",\"root_ar\":\"غ ي ر\",\"surface_ar\":\"مُغِيرَٰتِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:3:convergence-summary","source_type":"word_analysis","support_id":"sup_a254b952b3ce70cfe051","text":"{\"blocking_evidence\":null,\"headline\":\"grammar brightness cadence and boundary converge\",\"reader_payoff\":\"The reader notices the word doing several coordinated jobs at once: framing time, brightening the scene, closing the cadence, and pivoting the oath sequence.\",\"reason\":\"The summary rows synthesize locally licensed features already supported by the grammar, attachment, and V4 guardrail evidence.\",\"representative_source_ids\":[\"MS-661cf387\",\"QY-ca8ac131\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:3:morning-sinking-root-pair","source_type":"word_analysis","support_id":"sup_a40b1074ed02539bf502","text":"{\"blocking_evidence\":null,\"headline\":\"morning sinking root-pair echo\",\"reader_payoff\":\"The reader can register a root-pair echo where morning and sinking/descent meet elsewhere, while the local word still functions as dawn-time.\",\"reason\":\"The concrete echo is preserved with its references (18:41; 67:30), but it is narrowed to intertextual pressure because local grammar selects the accusative dawn-time frame.\",\"representative_source_ids\":[\"QE-4ff70607\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:2:plural-agent-continuity","source_type":"word_analysis","support_id":"sup_a949d6bb7f44fb84c0e9","text":"{\"blocking_evidence\":null,\"headline\":\"feminine plural participle carries the same agents\",\"reader_payoff\":\"The reader notices continuity of agents through morphology even where no explicit pronoun names them again.\",\"reason\":\"The definite feminine plural active participle and repeated participial pattern license the agent-continuity payoff.\",\"representative_source_ids\":[\"QG-6f8becfa\",\"QF-cea00215\",\"QI-96d72051\",\"QB-c54105e3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:3:tanwin-rhyme-openness","source_type":"word_analysis","support_id":"sup_cc210d3f27e317e69d31","text":"{\"blocking_evidence\":null,\"headline\":\"tanwīn joins openness and rhyme\",\"reader_payoff\":\"The reader notices that the same ending both leaves dawn indefinite and locks the word into the oath cadence.\",\"reason\":\"The row combines a real grammatical feature, indefiniteness, with the audible oath-ending cadence.\",\"representative_source_ids\":[\"QP-8aec9f88\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:2:oath-governed-participle","source_type":"word_analysis","support_id":"sup_ccd3120d638e62df7a60","text":"{\"blocking_evidence\":null,\"headline\":\"genitive participle remains under oath governance\",\"reader_payoff\":\"The reader notices that the word is not a stand-alone finite clause but a third sworn image still governed by the earlier oath frame.\",\"reason\":\"QAC and attachment evidence both identify the word as a definite feminine plural active participle in genitive case under the oath governance.\",\"representative_source_ids\":[\"QG-0740af78\",\"QT-87af4a2b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:3:brightness-pressure","source_type":"word_analysis","support_id":"sup_d032b16887e2812e6615","text":"{\"blocking_evidence\":null,\"headline\":\"dawn time carries brightness pressure\",\"reader_payoff\":\"The reader notices that dawn is not a neutral timestamp; it is the moment when hidden motion becomes visible.\",\"reason\":\"The local accusative role selects dawn as time, while V4 confirms adjacent dawn, light, and brightness branches; those branches survive as sensory pressure rather than as independent local senses.\",\"representative_source_ids\":[\"QS-7671e16a\",\"QS-c584eb43\",\"QS-e72dc106\",\"QS-ec46ba3c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:3","source_type":"word_analysis","support_id":"sup_f110c9cced1a2cda89b8","text":"{\"gloss_range\":\"indefinite accusative dawn-time adverb locating the raid at a repeatable threshold of morning visibility, with brightness pressure retained but wider root branches locally constrained\",\"prose\":\"{{ar:صُبْحًۭا}} ({{tr:ṣubḥan}}) closes the ayah by giving the raid its first explicit time coordinate. Its accusative role makes dawn the frame of the action, not a new object or agent, so the oath sequence pivots from how the agents move to when their movement arrives. Because it comes after the agentive raid word, the time frame lands as a small verse-end reveal. The tanwīn leaves it as a dawn-type rather than a named dawn and also joins the surrounding oath cadence, while the root field lets that time carry brightness: concealed sparks from 100:2 open into visible daybreak. The wider morning, lamp, beauty, drink, and becoming branches do not replace the local temporal sense, but they explain why the time feels bright and revelatory. Its short -ḥan cadence binds the third oath beat to the earlier breath-and-strike endings even as the meaning advances into time, and its emphatic opening with breathy release fits the movement from threshold pressure into visibility. Dawn also prepares the raised dust in 100:4, so the lighting change carries forward into the next visible effect. The root-pair echo with morning-sinking scenes (18:41; 67:30) remains a narrowed intertextual pressure, not control of the local parse.\",\"root_display\":\"{{ar:ص ب ح}} ({{tr:ṣ-b-ḥ}})\",\"root_gloss_range\":\"root range around dawn and morning opening, coming in the morning, morning raid, light, brightness or beauty, morning drink, and becoming; local grammar selects dawn as the temporal frame\",\"surface_display\":\"{{ar:صُبْحًۭا}} ({{tr:ṣubḥan}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:3:3:emphatic-sound-release","source_type":"word_analysis","support_id":"sup_f3756e7d84e1db1e5a8e","text":"{\"blocking_evidence\":null,\"headline\":\"sound texture opens into visibility\",\"reader_payoff\":\"The reader hears a hard opening and breathy release that matches the semantic movement into daybreak.\",\"reason\":\"The sound observation is kept as a modest phonetic payoff that coheres with the dawn sense without governing the parse.\",\"representative_source_ids\":[\"QP-fd210d90\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُغِيرَٰتِ صُبْحًۭا","ayah_ref":"100:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000839/B004","root_001119/B003"],"payload":{"activation_trace":[{"assigned_role":"Defines the incursion by the state-change it produces.","branch_id":"B003","branch_image_ar":"تغيير الصورة أو إبدال الشيء بغيره","literal_contribution":"altering a form or replacing one thing with another","mapped_root_id":"root_001119","mapped_root_norm":"غ ي ر","root":"غ ي ر","source_phrase_ar":"مُغِيرَٰتِ","source_ref":"100:3"},{"assigned_role":"Supplies the dawn-incursion frame rather than bare clock time.","branch_id":"B004","branch_image_ar":"يوم الصباح","literal_contribution":"a morning raid and its alarm","mapped_root_id":"root_000839","mapped_root_norm":"ص ب ح","root":"ص ب ح","source_phrase_ar":"صُبْحًا","source_ref":"100:3"}],"changed_reading":{"after":"A dawn-incursion collective identified by its power to alter the configuration it enters.","before":"A feminine plural doing something in the morning."},"confidence":"strong","focus_anchor":"The plural active form مُغِيرَٰتِ is held to the change/substitution range of غ ي ر, while صُبْحًا carries an attested morning-raid and alarm image.","mechanism":"A collective arrives at the vulnerable opening of day and changes an already arranged situation. Dawn is both timing and tactical threshold; alteration is the event's functional result.","model_id":"b_dawn_incursion","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_dawn_incursion","source_type":"hft","support_id":"sup_ede12c0b4743228f42e3","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُغِيرَٰتِ صُبْحًۭا","ayah_ref":"100:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000839/B001","root_000839/B005","root_000839/B010","root_001119/B003"],"payload":{"activation_trace":[{"assigned_role":"Provides the transition from one state to another.","branch_id":"B003","branch_image_ar":"تغيير الصورة أو إبدال الشيء بغيره","literal_contribution":"change of form, condition, or occupant","mapped_root_id":"root_001119","mapped_root_norm":"غ ي ر","root":"غ ي ر","source_phrase_ar":"مُغِيرَٰتِ","source_ref":"100:3"},{"assigned_role":"Marks a boundary at which a new state opens.","branch_id":"B001","branch_image_ar":"الصبح وأول النهار","literal_contribution":"dawn and the opening of day","mapped_root_id":"root_000839","mapped_root_norm":"ص ب ح","root":"ص ب ح","source_phrase_ar":"صُبْحًا","source_ref":"100:3"},{"assigned_role":"Turns the temporal boundary into a visibility mechanism.","branch_id":"B005","branch_image_ar":"المصباح والسراج","literal_contribution":"lamp and source of light","mapped_root_id":"root_000839","mapped_root_norm":"ص ب ح","root":"ص ب ح","source_phrase_ar":"صُبْحًا","source_ref":"100:3"},{"assigned_role":"Makes becoming, not just morning, available as the phrase's temporal logic.","branch_id":"B010","branch_image_ar":"أصبح بمعنى صار","literal_contribution":"coming to be in a state","mapped_root_id":"root_000839","mapped_root_norm":"ص ب ح","root":"ص ب ح","source_phrase_ar":"صُبْحًا","source_ref":"100:3"}],"changed_reading":{"after":"The incursion itself is a dawn-like conversion from concealment to a newly visible condition.","before":"Morning is an adverbial timestamp for an incursion."},"confidence":"medium","focus_anchor":"مُغِيرَٰتِ anchors a change of state, and صُبْحًا anchors the opening of day, illumination, and becoming.","mechanism":"The phrase can stage a phase transition: an obscured state is replaced by a lit, manifest one. Morning is not merely when the agents act; its opening and lamp imagery specify what their changing achieves.","model_id":"b_threshold_illumination","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_threshold_illumination","source_type":"hft","support_id":"sup_d3b888abd29b6646cdfa","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُغِيرَٰتِ صُبْحًۭا","ayah_ref":"100:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000839/B002","root_000839/B003","root_001119/B001"],"payload":{"activation_trace":[{"assigned_role":"Supplies the reparative result of the morning action.","branch_id":"B001","branch_image_ar":"الصلاح والمنفعة بالميرة والسقي والإصلاح","literal_contribution":"benefit and repair through provision and watering","mapped_root_id":"root_001119","mapped_root_norm":"غ ي ر","root":"غ ي ر","source_phrase_ar":"مُغِيرَٰتِ","source_ref":"100:3"},{"assigned_role":"Makes morning arrival the delivery phase.","branch_id":"B002","branch_image_ar":"الإتيان صباحا","literal_contribution":"coming or bringing in the morning","mapped_root_id":"root_000839","mapped_root_norm":"ص ب ح","root":"ص ب ح","source_phrase_ar":"صُبْحًا","source_ref":"100:3"},{"assigned_role":"Specifies the provision that changes the receiving field.","branch_id":"B003","branch_image_ar":"الصبوح","literal_contribution":"morning drink, food, or watering","mapped_root_id":"root_000839","mapped_root_norm":"ص ب ح","root":"ص ب ح","source_phrase_ar":"صُبْحًا","source_ref":"100:3"}],"changed_reading":{"after":"Dawn actors arrive with water, provision, or repair and change a depleted field into a sustained one.","before":"Dawn actors invade and disrupt."},"confidence":"exploratory","focus_anchor":"A branch of غ ي ر joins provision, watering, and repair, while branches of ص ب ح join morning arrival with morning drink or watering.","mechanism":"Instead of hostile entrants, the feminine plural can be carried experimentally as morning bringers whose arrival changes lack into supply or disrepair into fitness. The model is branch-distant from the raid reading but has a two-root functional circuit: arrive, water or provision, and thereby alter.","model_id":"b_morning_provision_repair","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_morning_provision_repair","source_type":"hft","support_id":"sup_feb6fc0376d933cc80e4","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُغِيرَٰتِ صُبْحًۭا","ayah_ref":"100:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000839/B004","root_001119/B004"],"payload":{"activation_trace":[{"assigned_role":"Supplies the motive for rapid protective intervention.","branch_id":"B004","branch_image_ar":"الغَيْرة على الأهل","literal_contribution":"protective jealousy over one's family","mapped_root_id":"root_001119","mapped_root_norm":"غ ي ر","root":"غ ي ر","source_phrase_ar":"مُغِيرَٰتِ","source_ref":"100:3"},{"assigned_role":"Supplies the alarm that flips repose into defense.","branch_id":"B004","branch_image_ar":"يوم الصباح","literal_contribution":"morning raid and alarm","mapped_root_id":"root_000839","mapped_root_norm":"ص ب ح","root":"ص ب ح","source_phrase_ar":"صُبْحًا","source_ref":"100:3"}],"changed_reading":{"after":"The plural may instead be responders changed into protective motion by a dawn alarm.","before":"The plural initiates a dawn attack."},"confidence":"exploratory","focus_anchor":"The protective-jealousy branch of غ ي ر can meet the morning alarm branch of ص ب ح without losing contact with مُغِيرَٰتِ صُبْحًا.","mechanism":"An alarm at dawn mobilizes a protective collective. On this reading, the change is a rapid switch from ordinary repose to guarding those within a threatened boundary.","model_id":"b_alarm_protection","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_alarm_protection","source_type":"hft","support_id":"sup_676ab9ce38ab7596ff3d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُغِيرَٰتِ صُبْحًۭا","ayah_ref":"100:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000839/B004","root_001119/B003"],"payload":{"activation_trace":[{"assigned_role":"makes the feminine plural agents into change-makers, not merely movers","branch_id":"B003","branch_image_ar":"تغيير الصورة أو إبدال الشيء بغيره","literal_contribution":"altering form or replacing one state with another","mapped_root_id":"root_001119","mapped_root_norm":"غ ي ر","root":"غ ي ر","source_phrase_ar":"مُغِيرَٰتِ","source_ref":"100:3"},{"assigned_role":"sets the time as tactical exposure and sudden morning incursion","branch_id":"B004","branch_image_ar":"يوم الصباح","literal_contribution":"dawn raid and alarm","mapped_root_id":"root_000839","mapped_root_norm":"ص ب ح","root":"ص ب ح","source_phrase_ar":"صُبْحًا","source_ref":"100:3"}],"changed_reading":{"after":"Dawn is the moment when active agents convert a prior state into another state through incursion.","before":"A bare phrase: the ones changing/raiding at morning."},"confidence":"strong","focus_anchor":"مُغِيرَٰتِ + صُبْحًا","mechanism":"The participial plural supplies agents; غ ي ر supplies alteration/substitution, while ص ب ح supplies the morning-raid alarm. Focus-only, the line reads as agents whose arrival at dawn changes a situation.","model_id":"B_FOCUS_RAID_AS_STATE_CHANGE_AT_DAWN","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:5.5-high:B_FOCUS_RAID_AS_STATE_CHANGE_AT_DAWN","source_type":"hft","support_id":"sup_99d1441af33b566c0ef7","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُغِيرَٰتِ صُبْحًۭا","ayah_ref":"100:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000839/B001","root_001119/B005"],"payload":{"activation_trace":[{"assigned_role":"lets the action be a production of difference","branch_id":"B005","branch_image_ar":"السوى والخلاف والاستثناء والنفي","literal_contribution":"otherness, opposition, and negation","mapped_root_id":"root_001119","mapped_root_norm":"غ ي ر","root":"غ ي ر","source_phrase_ar":"مُغِيرَٰتِ","source_ref":"100:3"},{"assigned_role":"supplies a threshold where one condition becomes another","branch_id":"B001","branch_image_ar":"الصبح وأول النهار","literal_contribution":"dawn and the opening of day","mapped_root_id":"root_000839","mapped_root_norm":"ص ب ح","root":"ص ب ح","source_phrase_ar":"صُبْحًا","source_ref":"100:3"}],"changed_reading":{"after":"Morning is itself the hinge of alterity: the agents enact the world's becoming otherwise.","before":"Morning is only the time of an action."},"confidence":"medium","focus_anchor":"غ ي ر as otherness + ص ب ح as first opening","mechanism":"The focus can be heard less as battle and more as transition: morning makes night other than itself, and the agents belong to that boundary-change.","model_id":"B_FOCUS_OTHERNESS_THRESHOLD","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:5.5-high:B_FOCUS_OTHERNESS_THRESHOLD","source_type":"hft","support_id":"sup_a4a1c9feb353945848d7","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُغِيرَٰتِ صُبْحًۭا","ayah_ref":"100:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000839/B003","root_001119/B001"],"payload":{"activation_trace":[{"assigned_role":"keeps a non-martial change-by-benefit model alive","branch_id":"B001","branch_image_ar":"الصلاح والمنفعة بالميرة والسقي والإصلاح","literal_contribution":"provision, watering, and repair","mapped_root_id":"root_001119","mapped_root_norm":"غ ي ر","root":"غ ي ر","source_phrase_ar":"مُغِيرَٰتِ","source_ref":"100:3"},{"assigned_role":"turns dawn into a time of supply rather than attack","branch_id":"B003","branch_image_ar":"الصبوح","literal_contribution":"morning drink, food, or watering","mapped_root_id":"root_000839","mapped_root_norm":"ص ب ح","root":"ص ب ح","source_phrase_ar":"صُبْحًا","source_ref":"100:3"}],"changed_reading":{"after":"A weaker but anchored baseline sees morning agents that alter a condition by provisioning or watering.","before":"The phrase seems to require raiders."},"confidence":"exploratory","focus_anchor":"غ ي ر B001 + ص ب ح B003","mechanism":"A branch-distant focus-only reading joins غ ي ر's provision/repair/watering with ص ب ح's morning drink or watering. The participle can then carry morning arrival that changes need into supply.","model_id":"B_FOCUS_PROVISIONING_MORNING","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:5.5-high:B_FOCUS_PROVISIONING_MORNING","source_type":"hft","support_id":"sup_fd5a5122ca86f0459b2b","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُغِيرَٰتِ صُبْحًۭا","ayah_ref":"100:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000839/B004","root_001119/B003"],"payload":{"activation_trace":[{"assigned_role":"Event-result: the incursion changes the encountered state.","branch_id":"B003","branch_image_ar":"تغيير الصورة أو إبدال الشيء بغيره","literal_contribution":"Alteration or substitution supplies the result imposed by the acting plural.","mapped_root_id":"root_001119","mapped_root_norm":"غ ي ر","root":"غ ي ر","source_phrase_ar":"مُغِيرَٰتِ","source_ref":"100:3"},{"assigned_role":"Temporal-event frame: dawn is tactically charged rather than neutral clock time.","branch_id":"B004","branch_image_ar":"يوم الصباح","literal_contribution":"The branch explicitly supplies morning raid and alarm.","mapped_root_id":"root_000839","mapped_root_norm":"ص ب ح","root":"ص ب ح","source_phrase_ar":"صُبْحًا","source_ref":"100:3"}],"changed_reading":{"after":"Coordinated dawn-incursors whose arrival abruptly changes the state of what they enter.","before":"Those going forth in the morning."},"confidence":"strong","focus_anchor":"The feminine active plural مُغِيرَٰتِ plus accusative temporal صُبْحًا anchors coordinated agents acting at dawn.","mechanism":"The agents make a sudden incursive alteration at the conventional time of a morning raid: motion is encoded as an event that changes the condition of a place or group, not merely as travel.","model_id":"base_dawn_incursion","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:5.6-sol-high:base_dawn_incursion","source_type":"hft","support_id":"sup_6a8ac57b6f912566a6a4","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُغِيرَٰتِ صُبْحًۭا","ayah_ref":"100:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000839/B001","root_000839/B010","root_001119/B003"],"payload":{"activation_trace":[{"assigned_role":"Causal operator: the agents bring one condition into another.","branch_id":"B003","branch_image_ar":"تغيير الصورة أو إبدال الشيء بغيره","literal_contribution":"Supplies change of form, state, or replacement.","mapped_root_id":"root_001119","mapped_root_norm":"غ ي ر","root":"غ ي ر","source_phrase_ar":"مُغِيرَٰتِ","source_ref":"100:3"},{"assigned_role":"Threshold: a new visible phase begins.","branch_id":"B001","branch_image_ar":"الصبح وأول النهار","literal_contribution":"Supplies the opening boundary of the day.","mapped_root_id":"root_000839","mapped_root_norm":"ص ب ح","root":"ص ب ح","source_phrase_ar":"صُبْحًا","source_ref":"100:3"},{"assigned_role":"State-transition analogue joined to the agents' altering action.","branch_id":"B010","branch_image_ar":"أصبح بمعنى صار","literal_contribution":"Supplies becoming or entering a condition.","mapped_root_id":"root_000839","mapped_root_norm":"ص ب ح","root":"ص ب ح","source_phrase_ar":"صُبْحًا","source_ref":"100:3"}],"changed_reading":{"after":"Agents of a threshold event: as morning becomes, they make another state become.","before":"Agents active at a time called morning."},"confidence":"medium","focus_anchor":"مُغِيرَٰتِ is anchored in change, while صُبْحًا names the opening of day and also activates coming-to-be in a state.","mechanism":"Dawn is read as a threshold and the plural agents as operators of transition: their action and the world's passage into morning are superposed, so temporal change becomes causal change.","model_id":"base_threshold_transformation","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:5.6-sol-high:base_threshold_transformation","source_type":"hft","support_id":"sup_06261e4e0407d44d3182","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُغِيرَٰتِ صُبْحًۭا","ayah_ref":"100:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000839/B002","root_001119/B003"],"payload":{"activation_trace":[{"assigned_role":"Consequence of arrival.","branch_id":"B003","branch_image_ar":"تغيير الصورة أو إبدال الشيء بغيره","literal_contribution":"Arrival is marked by the new condition it produces.","mapped_root_id":"root_001119","mapped_root_norm":"غ ي ر","root":"غ ي ر","source_phrase_ar":"مُغِيرَٰتِ","source_ref":"100:3"},{"assigned_role":"Motion-time frame.","branch_id":"B002","branch_image_ar":"الإتيان صباحا","literal_contribution":"Supplies coming or arriving in the morning.","mapped_root_id":"root_000839","mapped_root_norm":"ص ب ح","root":"ص ب ح","source_phrase_ar":"صُبْحًا","source_ref":"100:3"}],"changed_reading":{"after":"A coordinated first-light arrival recognized by the change it effects.","before":"A generic morning action."},"confidence":"medium","focus_anchor":"The active plural can be heard as arrivals, and صُبْحًا has a supplied branch for coming in the morning.","mechanism":"The line foregrounds timed arrival: a group reaches its object at first light, with the change-root making arrival consequential rather than merely locative.","model_id":"base_morning_arrival","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:5.6-sol-high:base_morning_arrival","source_type":"hft","support_id":"sup_2955648f213d1d0ae095","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُغِيرَٰتِ صُبْحًۭا","ayah_ref":"100:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000839/B003","root_001119/B001"],"payload":{"activation_trace":[{"assigned_role":"Beneficial action performed by the plural agents.","branch_id":"B001","branch_image_ar":"الصلاح والمنفعة بالميرة والسقي والإصلاح","literal_contribution":"Supplies provision, watering, benefit, and setting gear or a mount right.","mapped_root_id":"root_001119","mapped_root_norm":"غ ي ر","root":"غ ي ر","source_phrase_ar":"مُغِيرَٰتِ","source_ref":"100:3"},{"assigned_role":"Material delivered or shared at morning.","branch_id":"B003","branch_image_ar":"الصبوح","literal_contribution":"Supplies morning food, drink, or watering.","mapped_root_id":"root_000839","mapped_root_norm":"ص ب ح","root":"ص ب ح","source_phrase_ar":"صُبْحًا","source_ref":"100:3"}],"changed_reading":{"after":"Exploratorily, morning agents who alter conditions through provision, watering, and repair.","before":"A hostile dawn incursion."},"confidence":"exploratory","focus_anchor":"The supplied غ ي ر inventory includes provision, watering, benefit, and repair, while ص ب ح includes morning arrival, food, drink, and watering.","mechanism":"A formally available but context-free counter-reading treats the plural as morning providers or repairers: they arrive with sustenance, water, or restored travel equipment and thereby improve a household, land, or company.","model_id":"base_provisioning_counterreading","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:5.6-sol-high:base_provisioning_counterreading","source_type":"hft","support_id":"sup_826d14e70aa61f73702c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَٱلْمُغِيرَٰتِ صُبْحًۭا","ayah_ref":"100:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000839/B008","root_001119/B003"],"payload":{"activation_trace":[{"assigned_role":"Background condition of delayed movement or vulnerable stasis.","branch_id":"B008","branch_image_ar":"الناقة المصباح","literal_contribution":"Supplies an animal remaining kneeling in its resting place into morning.","mapped_root_id":"root_000839","mapped_root_norm":"ص ب ح","root":"ص ب ح","source_phrase_ar":"صُبْحًا","source_ref":"100:3"},{"assigned_role":"Disruptive force breaching morning stasis.","branch_id":"B003","branch_image_ar":"تغيير الصورة أو إبدال الشيء بغيره","literal_contribution":"Supplies reversal of the resting condition.","mapped_root_id":"root_001119","mapped_root_norm":"غ ي ر","root":"غ ي ر","source_phrase_ar":"مُغِيرَٰتِ","source_ref":"100:3"}],"changed_reading":{"after":"The active dawn agents are legible against a latent morning stasis that their arrival abruptly breaks.","before":"Everything in the scene is pure acceleration."},"confidence":"exploratory","focus_anchor":"صُبْحًا supplies a possible image of remaining kneeling into morning; مُغِيرَٰتِ supplies the agents that rupture or reverse that condition.","outlier_id":"outlier_morning_stasis_breached","rendering_caution":"Use only as a contrastive branch activation; do not identify مُغِيرَٰتِ with the kneeling camel or override the temporal syntax.","why_still_valid":"The branch belongs directly to ص ب ح, and its delayed rising forms a precise opposition to the active plural's sudden state-changing arrival.","why_surprising":"It retains the focus inventory's morning-staying camel branch, usually too remote for a conservative synthesis, and uses it as a stasis contrast rather than an identification."},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:5.6-sol-high:outlier_morning_stasis_breached","source_type":"hft","support_id":"sup_d26ef228057789f5d9a8","trust":"legacy_unbound"}]}
</lane_packet_json>
