# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **114:6**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s114-regular-20260911/s114/114_6/micro.discovery.json` and modify nothing
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
  "ayah_ref": "114:6",
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
{"analysis_context":{"analysis_id":"s114-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"114:6","host_surah":114,"lane_context_refs":[],"ordered_context_refs":["114:0","114:1","114:2","114:3","114:4","114:5","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, insan türünü ve onun tekil ya da toplu üyelerini kapsar; yakınlık duygusunu, duyusal algıyı ve insana dönük yanı kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B001","candidate_links":[{"candidate_id":"cand_bc63b3f17f545819a1f6","lane":"micro"},{"candidate_id":"cand_33f022d1bd814d192802","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:3:3","qac_word_ref":"114:6:3","surface_ar":"نَّاسِ"}],"gloss":"insan türü ve bu türden bir kişi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan türünü, insanların oluşturduğu topluluğu veya bu türün tek bir üyesini görünmeyen varlıklar sınıfının karşısında adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlandırmanın insanların duyularla görünür oluşuna bağlanması, anlamın özü değil kökene ilişkin bir açıklamadır."}}],"root_ar":"ن و س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsanları bir tür veya topluluk olarak anlatırken de bu türün tek bir üyesini belirtirken de kullanılabilir.","boundary_detail":"Dal, insan türünü ve onun tekil ya da toplu üyelerini kapsar; yakınlık duygusunu, duyusal algıyı ve insana dönük yanı kapsamaz.","branch_image_ar":"ظهور الإنسان المخالف للتوحش والجن","concept_gloss":"insan türü ve bu türden bir kişi","contextual_glosses":[{"applicability":"Türün üyeleri topluca veya görünmeyen varlıklar sınıfının karşıtı olarak anıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan türünün toplu olarak adlandırılmasını açık ve doğal biçimde korur."},"facet_ids":["F001"],"text":"insanlar","usage_role":"general"},{"applicability":"Bağlam türün tek bir üyesini veya herhangi bir kimseyi gösterdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan topluluğundan tek bir üyenin belirtilmesini korur."},"facet_ids":["F001"],"text":"bir kişi","usage_role":"contextual"}],"definition":"Görünmeyen varlıklar sınıfının karşısında yer alan insan türünü, bu türün topluluğunu ya da tek bir üyesini belirtir. İnsanların görünür oluşu, bu adlandırma için aktarılan bir gerekçedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan türünü, insanların oluşturduğu topluluğu veya bu türün tek bir üyesini görünmeyen varlıklar sınıfının karşısında adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Adlandırmanın insanların duyularla görünür oluşuna bağlanması, anlamın özü değil kökene ilişkin bir açıklamadır."}],"identity_rationale":"Kaynak ifadesi, görünmeyen varlıklar sınıfının karşısındaki insan türünü, bu türün topluluğunu ve tek bir üyesini birlikte gösterir. Görünür olma açıklaması adlandırma gerekçesidir; insan olmanın kurucu tanımı değildir. Evde kimsenin bulunmadığını bildiren kalıp ise dal çekirdeğine genellenemez ve yalnızca kendi sözcüksel biriminde korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"insanlar; insan topluluğu"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"insan; insan türü"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"insan topluluğunun bir üyesi; insana veya insanlara ait"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"insanlar; insan toplulukları"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"insanlar; halk"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"evde hiç kimse yok"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"belirli bir ağızda insan ve onun çoğulu"}],"lexicalization_note":"Çıplak biçimlerdeki insan ve insan topluluğu anlamı dal çekirdeğidir; evde hiç kimse bulunmadığını anlatan kalıp ayrı tutulur ve çekirdeğe yeni bir genel anlam katmaz.","neighbor_coverage_note":"Bütün aday kartlar karşılaştırıldı. Yalnız insanı adlandırma sınırını yaratılmışlar kapsamından ve yakınlık duygusundan ayıran, okuyucu için en yararlı üç karşıtlık yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yer değiştirme yalnız insanı genel olarak adlandıran bağlamlarda mümkündür. Odak dalın görünmeyen varlıklarla sınıf karşıtlığı, komşunun ise görünür beden yönü kendi sınırında kalır.","focus_only":"Odak dal, insanları görünmeyen varlıklar sınıfının karşısında bir tür olarak kurar ve görünürlüğe dayalı bir adlandırma açıklaması taşır.","gloss":"insan türünü iki ayrı yönden adlandırma","neighbor_only":"Komşu dal, insanı görünür ten ve yaratılmış beden yönüyle adlandırır; tekil, çoğul, erkek ve kadın kapsamını özellikle öne çıkarır.","neighbor_ref":"root_000120/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da insanı hem tür hem bu türün üyesi olarak gösterebilir."},{"boundary_match":"partial","distinction":"Komşunun genel yaratılmışlar kapsamı odak dala taşınamaz; odak dal da yalnız insanları belirttiği için bütün yaratılmışların yerine kullanılamaz.","focus_only":"Odak dal yalnız insan türünü ve bu türün tekil ya da toplu üyelerini belirtir.","gloss":"insan türü ile bütün yaratılmışlar ayrımı","neighbor_only":"Komşu dal yeryüzündeki bütün yaratılmışları kapsayabilir ve bazı yorumlarda insanlarla görünmeyen varlıkları birlikte içerir.","neighbor_ref":"root_000061/B001","relation_type":"near_neighbor","shared_zone":"İnsanlar iki dalın gönderim alanında da bulunabilir."},{"boundary_match":"field_only","distinction":"Birinde insanın kim olduğu adlandırılır, diğerinde bir kişi ya da şey karşısındaki duygusal durum anlatılır; sıradan bağlamlarda birbirlerinin yerine geçmezler.","focus_only":"Odak dal insan türünü ve bu türün üyelerini adlandırır.","gloss":"insan adı ile yakınlık duygusu ayrımı","neighbor_only":"Komşu dal yabancılık ve ürkme duygusunun kalkmasını, yakınlık ve rahatlık oluşmasını anlatır.","neighbor_ref":"root_000059/B003","relation_type":"same_field","shared_zone":"Her iki dalda da insan, temel gönderim noktası veya deneyim sahibi olabilir."}],"source_phrase_ar":"الإنس خلاف الجن وسموا لظهورهم (maqayis;mufradat)؛ الإنس البشر والواحد إنسي والجمع أناسي (sihah)؛ الإنس جماعة الناس والأناسي جماع (tahdhib)","source_summary":"Aktarımlar, dalın insan türünü hem topluluk hem tek kişi olarak gösterebildiğinde ve görünmeyen varlıklar sınıfıyla karşıtlık kurduğunda birleşir. Görünürlük, ortak anlamdan çok adlandırmanın gerekçesi olarak sunulur.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الإنس والبشر والناس والأناسي والإنسان من حيث الجماعة أو الواحد، وما بالدار أنيس بمعنى أحد.","what_is_not_ar":"لا يدخل مجرد الاستئناس النفسي ولا الإيناس بمعنى الإبصار ولا الجانب الإنسي إلا بدليل."},"support_links":["sup_8b3ac0a346f5af86ab66","sup_bd0d87185e8e80075fc9"]},{"boundary":"Dal duyusal olarak fark etmeyi ve belirtilen bağlamlardaki işitme, sezme ve bakıp araştırma kullanımlarını kapsar; yakınlık ve rahatlık duygusunu kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B002","candidate_links":[{"candidate_id":"cand_e9db42b0009db1e8ac36","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:3:3","qac_word_ref":"114:6:3","surface_ar":"نَّاسِ"}],"gloss":"görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi gözle görerek fark etmeyi veya seçmeyi anlatır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli bir ses nesnesiyle kullanıldığında o sesi işitmeyi anlatır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kimsedeki olgunluk belirtisini bilip ayırt etmeyi veya kaygı veren bir durumu duyularla sezmeyi anlatabilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Çevreye bakıp dikkatle araştırarak birinin bulunup bulunmadığını anlamaya çalışma kullanımını taşır."}}],"root_ar":"ن و س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın görme çekirdeğiyle birlikte yalnız belirtilen bağlamlarda ortaya çıkan işitme, sezme ve çevreyi araştırma uzantılarını topluca verir.","boundary_detail":"Dal duyusal olarak fark etmeyi ve belirtilen bağlamlardaki işitme, sezme ve bakıp araştırma kullanımlarını kapsar; yakınlık ve rahatlık duygusunu kapsamaz.","branch_image_ar":"إيناس الشيء برؤية أو إحساس أو سماع","concept_gloss":"görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma","contextual_glosses":[{"applicability":"Nesnenin gözle seçildiği veya görüldüğü temel kullanımda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gözle görme ve görüleni fark etme işlemlerini birlikte korur."},"facet_ids":["F001"],"text":"görüp fark etmek","usage_role":"general"},{"applicability":"Nesne açıkça bir ses olduğunda kullanılan bağlama bağlı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sesin kulakla algılanması biçimindeki özel kullanımı korur."},"facet_ids":["F002"],"text":"sesi işitmek","usage_role":"contextual"},{"applicability":"Bir kimsedeki olgunluk veya kaygı uyandıran durum gibi bir belirtinin ayırt edildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Duyusal belirtiden bir durumun varlığını anlayıp ayırt etmeyi korur."},"facet_ids":["F003"],"text":"belirtiyi sezmek","usage_role":"contextual"},{"applicability":"Çevreyi gözleyip birinin bulunup bulunmadığını anlamaya çalışma kullanımında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dikkatle bakma ile birini bulmaya yönelik araştırmayı birlikte korur."},"facet_ids":["F004"],"text":"bakıp araştırmak","usage_role":"explanatory"}],"definition":"Bir şeyi görüp fark etmeyi anlatır. Belirli kullanımlarda bir sesi işitmeye, bir kimsedeki olgunluk belirtisini ya da kaygı veren bir durumu sezmeye ve çevreye bakarak birinin bulunup bulunmadığını araştırmaya uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi gözle görerek fark etmeyi veya seçmeyi anlatır."},{"facet_id":"F002","role":"extension","statement":"Belirli bir ses nesnesiyle kullanıldığında o sesi işitmeyi anlatır."},{"facet_id":"F003","role":"extension","statement":"Bir kimsedeki olgunluk belirtisini bilip ayırt etmeyi veya kaygı veren bir durumu duyularla sezmeyi anlatabilir."},{"facet_id":"F004","role":"associated_use","statement":"Çevreye bakıp dikkatle araştırarak birinin bulunup bulunmadığını anlamaya çalışma kullanımını taşır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Zamanla gelişen yakınlık ve yabancılığın kalkması anlamını ekler.","collision":"Yakınlık ve rahatlık bildiren ayrı dalla karışır.","fit":"displacement","loses":"Görme, işitme, belirtiyi sezme ve çevreye bakıp araştırma işlemlerini siler.","preserves":"Bir kişi veya şeye yönelen deneyim fikrini çok genel biçimde korur."},"text":"alışmak"}],"identity_rationale":"Kaynak ifadesi görmeyi temel alır, fakat belirli kullanımlarda işitmeyi, bir belirtiyi anlayıp ayırt etmeyi ve çevreye bakarak birini aramayı da aynı dalda aktarır. Bu yüzden dal genel ve sınırsız bir algı yetisi diye tanımlanamaz; her uzantı kendi bağlamına bağlı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir şeyi görmek ve fark etmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"sesi işitmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"onda olgunluk belirtisi görmek ve bunu anlamak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ürken yabani hayvanın birini sezip çevreye bakınması"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"çevreye bakıp birinin olup olmadığını araştırmak"}],"lexicalization_note":"Görüp fark etme çekirdeği ile ses işitme, olgunluk belirtisini ayırt etme ve çevreye bakıp araştırma kalıpları ayrı tutulur; kalıplardaki kapsam çıplak biçime genellenmez.","neighbor_coverage_note":"Bütün aday kartlar değerlendirildi. Görme, genel duyumsama ve yakınlık duygusuyla karışma olasılığı en yüksek üç sınır yayımlandı; diğer adaylar dalı açıklayan ek bir karşıtlık sağlamadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yalnız görsel algı bağlamında yakın karşılık olabilirler. Odak dalın işitme ve belirtiyi sezme uzantıları komşuya, komşunun göz organı anlamı da odak dala taşınamaz.","focus_only":"Odak dal, görmenin yanında belirli yapılarda işitme, belirti sezme ve çevreyi araştırma uzantılarını taşır.","gloss":"fark etme ile gözle görme ayrımı","neighbor_only":"Komşu dal göz organını, görme duyusunu ve göz açıp dikkatle bakma eylemini kendi başına kapsar.","neighbor_ref":"root_000121/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi göz yoluyla görüp seçme alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu daha genel bir duyu alanıdır; odak dalın uzantıları ise kanıtlanan nesne ve yapılara bağlıdır. Bu nedenle genel duyumsama her durumda odak ifadeyle karşılanamaz.","focus_only":"Odak dal görmeyi merkez alır ve yalnız belirli söz çevrelerinde işitme, sezme ve araştırmaya uzanır.","gloss":"belirli algı kullanımları ile genel duyumsama","neighbor_only":"Komşu dal herhangi bir duyu aracılığıyla algılama, bilme ve varlığını saptama alanını genel olarak kapsar.","neighbor_ref":"root_000321/B002","relation_type":"near_synonym","shared_zone":"Her ikisi de bir şeyin duyular aracılığıyla fark edilmesini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal algısal saptamayı, komşu dal ise karşılaşma sonrasındaki duygusal rahatlığı bildirir. Algı gerçekleşebilir ama yakınlık doğmayabilir.","focus_only":"Odak dal bir nesneyi görme, işitme veya belirtilerinden sezme eylemini anlatır.","gloss":"duyusal fark etme ile yakınlık hissetme","neighbor_only":"Komşu dal bir kişi ya da şey karşısında yabancılık ve ürkme duymayıp yakınlık hissetmeyi anlatır.","neighbor_ref":"root_000059/B003","relation_type":"near_neighbor","shared_zone":"Bir kişi veya şeyle karşılaşma iki anlam alanının ortak başlangıç durumu olabilir."}],"source_phrase_ar":"آنست الشيء إذا رأيته وآنسته إذا سمعته (maqayis)؛ آنسته أبصرته وآنست الصوت سمعته وآنست منه رشدا علمته (sihah)؛ آنس من جانب يعني أبصر نارا والاستئناس النظر وأحس بما رابه (tahdhib)؛ فإن آنستم منهم رشدا أي أبصرتم وآنست نارا (mufradat)","source_summary":"Aktarılan anlam alanının merkezi görüp fark etmektir. Aynı ifade ailesi belirli nesne ve yapılarda işitme, bir belirtiyi anlayıp ayırt etme, kaygı veren şeyi sezme ve bakıp araştırma yönlerinde kullanılır; bunlar sınırsız bir genel algı anlamı oluşturmaz.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه آنس الشيء إذا أبصره أو رآه، وآنس الصوت إذا سمعه، وأحس الفزع أو وجد الشيء في نفسه، والاستئناس بمعنى النظر والتبصر.","what_is_not_ar":"لا يدخل الأنس بمعنى الراحة والمؤالفة ولا الإنس بمعنى البشر إلا بقرينة."},"support_links":["sup_cfc6709aca10eec8bc5f"]},{"boundary":"Dal duygusal yakınlık, rahatlık ve bunları sağlayan varlıkları kapsar; insan türünün adı, duyusal fark etme ve insana bakan yan anlamları dışarıda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B003","candidate_links":[{"candidate_id":"cand_2abbfecf8a1aa3234623","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:3:3","qac_word_ref":"114:6:3","surface_ar":"نَّاسِ"}],"gloss":"yabancılık duymadan yakınlık ve rahatlık hissetme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi ya da şey karşısında yabancılık ve ürkme duygusunun kalkıp yakınlık, rahatlık veya sevinç oluşmasını anlatır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişiye arkadaşlık ederek veya yanında bulunarak yabancılık duygusunu gideren kişi ya da şeyi adlandırır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsana alışık ve saldırgan olmayan hayvanı, özellikle bu nitelikteki köpeği anlatabilir."}}],"root_ar":"ن و س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi veya şeyin ürkütücü ve yabancı gelmemesi, tersine yakınlık ve iç rahatlığı vermesi anlatıldığında dalın çekirdeğini karşılar.","boundary_detail":"Dal duygusal yakınlık, rahatlık ve bunları sağlayan varlıkları kapsar; insan türünün adı, duyusal fark etme ve insana bakan yan anlamları dışarıda kalır.","branch_image_ar":"الأنس الذي يزيل الوحشة","concept_gloss":"yabancılık duymadan yakınlık ve rahatlık hissetme","contextual_glosses":[{"applicability":"Bir kişi veya şey karşısındaki yabancılık duygusunun kalktığı temel durumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Alışma sonucunda yabancılığın kalkmasını ve yakınlık oluşmasını korur."},"facet_ids":["F001"],"text":"alışıp yakınlık duymak","usage_role":"general"},{"applicability":"Yalnızlığı veya ürkmeyi gideren bir arkadaş, nesne ya da başka bir dayanak adlandırıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yakınlık ve güven veren kaynağın kişiyle sınırlı olmamasını korur."},"facet_ids":["F002"],"text":"yanında rahatlık veren kişi veya şey","usage_role":"explanatory"},{"applicability":"İnsandan kaçmayan ve ısırıp saldırmayan evcil ya da alışkın hayvan için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın insana alışıklığını ve saldırgan olmama sınırını birlikte korur."},"facet_ids":["F003"],"text":"insana alışık ve saldırgan olmayan","usage_role":"contextual"}],"definition":"Bir kişi ya da şey karşısında yabancılık, ürkme veya kaçınma duymayıp yakınlık, rahatlık ve sevinç hissetmeyi anlatır. Bu duyguyu veren kişi veya şeye ve insana alışık, saldırgan olmayan hayvana da aktarılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi ya da şey karşısında yabancılık ve ürkme duygusunun kalkıp yakınlık, rahatlık veya sevinç oluşmasını anlatır."},{"facet_id":"F002","role":"extension","statement":"Kişiye arkadaşlık ederek veya yanında bulunarak yabancılık duygusunu gideren kişi ya da şeyi adlandırır."},{"facet_id":"F003","role":"specialization","statement":"İnsana alışık ve saldırgan olmayan hayvanı, özellikle bu nitelikteki köpeği anlatabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Her türlü sevincin bu dala ait olduğu izlenimini verebilir.","fit":"narrowing","loses":"Yabancılığın ve ürkmenin kalkmasını, alışmayı ve rahatlık veren kişi ya da şey kapsamını kaybeder.","preserves":"Yakınlık durumunda ortaya çıkabilen olumlu duyguyu korur."},"text":"sevinç"}],"identity_rationale":"Kaynak ifadesi, bir kişi veya şey karşısında yabancılık ve ürkme duygusunun kalkmasını çekirdek anlam olarak verir. Yakınlık ve sevinç, rahatlık veren kişi ya da şey ve insana alışık saldırgan olmayan hayvan kullanımları bu çekirdekten bağımlı biçimde açıklanabilir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yakınlık ve rahatlık; yabancılık duymama"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"birine alışıp onun yanında sevinmek"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"biriyle yakınlık kurmak ve onsuz kendini yalnız hissetmek"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"yakın arkadaş; rahatlık veren kişi veya şey"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yakınlıktan ve söyleşiden hoşlanan genç kadın"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"insana alışık, saldırgan olmayan köpek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"gece yolcusuna veya konaklayana güven veren ateş"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"sahibine güven veren bütün silahlar; zırh, miğfer, koruyucu örtü ve kalkan gibi savunma donanımları"}],"lexicalization_note":"Yabancılık duymama çekirdeği ile rahatlık veren kişi veya şey ve insana alışık hayvan gibi özelleşmiş biçimler ayrı katmanlarda tutulur; özel biçimler bütün dalı tanımlamaz.","neighbor_coverage_note":"Bütün aday kartlar karşılaştırıldı. Alışıp bağlanma, özel dostluk ve insan türünü adlandırma alanları dal sınırını en açık gösterdiği için yalnız bu üç ayrım yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın belirleyici yönü yabancılık ve ürkmenin karşıtı olan iç rahatlığıdır; komşu dal süreklilik, bağlanma ve alışkanlık yönlerini odaktan daha geniş taşır.","focus_only":"Odak dal yabancılık ve ürkmenin kalkmasıyla oluşan yakınlık ve rahatlığı, ayrıca bunu sağlayan varlığı öne çıkarır.","gloss":"yakınlık rahatlığı ile alışıp bağlanma","neighbor_only":"Komşu dal bir kişi, yer veya şeye alışmayı, ona bağlanmayı, onunla sürekli bulunmayı ve hayvanın evcilleşmesini daha geniş biçimde kapsar.","neighbor_ref":"root_000045/B005","relation_type":"near_synonym","shared_zone":"İki dal da bir kişi, yer, şey veya hayvana karşı yabancılığın azalmasını anlatabilir."},{"boundary_match":"partial","distinction":"Her rahatlık veren yakınlık özel ve arı bir dostluk değildir. Komşunun karşılıklı dostluk sınırı odak dalın nesne ve hayvan uzantılarına uygulanamaz.","focus_only":"Odak dal kişi dışındaki şeylerin verdiği rahatlığı ve insana alışık hayvanı da kapsayabilir.","gloss":"rahatlık veren yakınlık ile özel dostluk","neighbor_only":"Komşu dal seçilmiş kişiler arasındaki arı, özel ve karşılıklı dostluk bağını anlatır.","neighbor_ref":"root_000430/B007","relation_type":"near_neighbor","shared_zone":"İki dal da kişiler arasında yakınlık ve içtenlik bulunan durumlarda buluşur."},{"boundary_match":"field_only","distinction":"Odak dal bir duygusal ilişkiyi, komşu dal ise bir varlık sınıfını adlandırır. İnsan olmak yakınlık hissetmeyi gerektirmez ve iki ifade birbirinin yerine geçmez.","focus_only":"Odak dal yabancılığın kalkmasıyla doğan duygusal yakınlığı ve rahatlığı anlatır.","gloss":"yakınlık durumu ile insan adı ayrımı","neighbor_only":"Komşu dal insan türünü, insan topluluğunu veya bu türden tek bir kişiyi adlandırır.","neighbor_ref":"root_000059/B001","relation_type":"same_field","shared_zone":"İnsan, iki dalda da temel katılımcı veya gönderim noktasıdır."}],"source_phrase_ar":"الأنس أنس الإنسان بالشيء إذا لم يستوحش منه (maqayis)؛ الإيناس خلاف الإيحاش والإنس خلاف الوحشة والأنيس المؤانس وكل ما يؤنس به (sihah)؛ أنست بفلان أي فرحت به والأنس والاستئناس هو التأنس وكلب أنوس نقيض العقور (tahdhib)؛ الأنس خلاف النفور ولكل ما يؤنس به (mufradat)","source_summary":"Ortak çekirdek, yabancılık ve kaçınmanın karşıtı olan yakınlık ve rahatlıktır. Bu durum birine alışıp onun yanında sevinmeyi, rahatlık veren kişi veya şeyi ve insana alışık saldırgan olmayan hayvanı kapsayacak biçimde genişler.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه أنس الإنسان بالشيء أو بفلان، المؤانسة والتأنيس، الأنيس وكل ما يؤنس به، الفرح بالقرب والحديث، والحيوان الأنوس غير العقور.","what_is_not_ar":"لا يدخل الإنس بمعنى البشر ولا الإيناس بمعنى الإبصار ولا الجانب الإنسي إلا بدليل."},"support_links":["sup_0207b38de44bec322512"]},{"boundary":"Dal, bir nesnenin insana veya kullanıcıya bakan yanını belirtir; salt sol, salt sağ, genel ön taraf ya da insanın kendisi anlamına gelmez.","branch_kind":"bare","branch_ref":"root_000059/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:3:3","qac_word_ref":"114:6:3","surface_ar":"نَّاسِ"}],"gloss":"insana dönük yan","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin insana en yakın olan veya insana doğru bakan yanını belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvanda binicinin bulunduğu, binme ve sağma işlemlerinde insana yakın olan yanı anlatır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yayda okçuya doğru bakan ve kullanıcının karşısında bulunan yanı anlatır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İnsana yakın yan bazı aktarımda sol, başka bir aktarımda sağ diye belirlenir; yönün özü bu değişken tanımlardan bağımsızdır."}}],"root_ar":"ن و س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin yönü, ona yaklaşan veya onu kullanan insana göre belirlendiğinde dalın ortak çekirdeğini verir.","boundary_detail":"Dal, bir nesnenin insana veya kullanıcıya bakan yanını belirtir; salt sol, salt sağ, genel ön taraf ya da insanın kendisi anlamına gelmez.","branch_image_ar":"الجانب الإنسي المقبل على الإنسان","concept_gloss":"insana dönük yan","contextual_glosses":[{"applicability":"Hayvanın binme ve sağma sırasında insana yakın kalan yanı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın yanını biniciyle kurduğu işlevsel ilişkiye göre belirler."},"facet_ids":["F002"],"text":"biniciye yakın yan","usage_role":"contextual"},{"applicability":"Yayın kullanım sırasında okçuya doğru dönük olan yüzü belirtilirken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yay yüzünün yönünü okçunun konumuna göre belirleme özelliğini korur."},"facet_ids":["F003"],"text":"okçuya bakan yay yüzü","usage_role":"explanatory"}],"definition":"Bir nesnenin insana, kullanıcıya veya onun bulunduğu yöne bakan yanıdır. Hayvan ve yay üzerinde işlevsel ilişkiyle belirlenir; bu yanın sabit olarak sol ya da sağ sayılması konusunda aktarım uyuşmazlığı vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin insana en yakın olan veya insana doğru bakan yanını belirtir."},{"facet_id":"F002","role":"specialization","statement":"Hayvanda binicinin bulunduğu, binme ve sağma işlemlerinde insana yakın olan yanı anlatır."},{"facet_id":"F003","role":"specialization","statement":"Yayda okçuya doğru bakan ve kullanıcının karşısında bulunan yanı anlatır."},{"facet_id":"F004","role":"source_variant","statement":"İnsana yakın yan bazı aktarımda sol, başka bir aktarımda sağ diye belirlenir; yönün özü bu değişken tanımlardan bağımsızdır."}],"identity_rationale":"Kaynak ifadesinin güvenilir çekirdeği, bir şeyin insana veya onu kullanan kişiye dönük ve yakın olan yanıdır. Bu yanın solda mı sağda mı olduğu konusunda aktarımlar uyuşmaz; hayvan ve yay örnekleri yönü işlevsel ilişkiyle belirler. Bu nedenle sabit bir sağ-sol tanımı dalın özüne konamaz.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir şeyin insana bakan veya en yakın olan yanı"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yayın okçuya bakan yüzü"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"hayvanın biniciye yakın olan yanı"}],"lexicalization_note":"Tanım çıplak dalın insana dönük yan çekirdeğiyle sınırlıdır. Hayvan ve yay uygulamaları bu çekirdeğin örneklenmesidir; yalnız bu kullanımlardan yeni bir genel yön anlamı çıkarılmaz.","neighbor_coverage_note":"Adayların tamamı incelendi. Genel ön taraf, yönelme eylemi ve arka bölümle kurulan karşılaştırmalar insana göre belirlenen yanın sınırını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda yön, insanın nesneyle kurduğu konum veya kullanım ilişkisine bağlıdır. Komşu dalın genel ön ve yakın anlamları bu özel bağı gerektirmez.","focus_only":"Odak dal bir nesnenin insana veya onu kullanan kişiye dönük yanını ilişkiye göre belirler.","gloss":"insana dönük yan ile genel ön taraf","neighbor_only":"Komşu dal genel olarak ön, önde, yakın veya karşıda bulunma yönlerini kişiye bağlı bir kullanım ilişkisi gerektirmeden anlatır.","neighbor_ref":"root_000053/B011","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin bakana göre karşıda veya önde kalan bölümünü gösterebilir."},{"boundary_match":"partial","distinction":"Bir nesnenin insana dönük yanı bir bölüm adıdır; komşu ise dönme veya yönelme olayını anlatır. Sonuç konumu ile o konuma geçiş eylemi birbirinin yerine kullanılamaz.","focus_only":"Odak dal, yönelme tamamlandıktan sonra insana dönük olan sabit yanı adlandırır.","gloss":"dönük yan ile yönelme eylemi","neighbor_only":"Komşu dal yüz, baş, el, kap veya hayvanın bir hedefe doğru dönmesi ve yönelmesi eylemini anlatır.","neighbor_ref":"root_001263/B003","relation_type":"near_neighbor","shared_zone":"İki dal da bir kişi veya hedefe doğru bakma yönünü içerir."},{"boundary_match":"partial","distinction":"Bağlama göre karşıt görünebilseler de odak dal her zaman geometrik ön yüz değildir ve bu yüzden düzenli bir karşıt çift oluşturmaz; belirleyici ölçüt insana yakınlıktır.","focus_only":"Odak dal insana veya kullanıcıya yakın ve ona bakan yanı gösterir.","gloss":"insana bakan yan ile arka taraf","neighbor_only":"Komşu dal bir şeyin arkasında kalan, yüzünün karşıtı olan arka bölümünü gösterir.","neighbor_ref":"root_000458/B001","relation_type":"near_neighbor","shared_zone":"İki dal da bir nesnenin başka bir yöne göre belirlenen bölümünü adlandırır."}],"source_phrase_ar":"الإنسي الأيسر من كل شيء وقيل الأيمن وما أقبل منهما على الإنسان فهو إنسي وإنسي القوس ما أقبل عليك منها (sihah)؛ الإنسي من الدواب الجانب الأيسر الذي منه يركب ويحتلب ومن الإنسان الجانب الذي يلي الرجل الأخرى (tahdhib)؛ إنسي الدابة للجانب الذي يلي الراكب وإنسي القوس للجانب الذي يقبل على الرامي (mufradat)","source_summary":"Ortak anlam, nesnenin insana veya kullanıcıya dönük yanıdır; hayvanda biniciye, yayda okçuya göre belirlenir. İnsan bedenindeki tekil uygulamada öteki bacağa bakan yan kastedilir. Bu yanın solda mı sağda mı bulunduğuna ilişkin anlatımlar ayrıştığı için genel tanım sabit bir yön seçmez.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه إنسي الدابة والقوس وكل شيئين: ما يلي الإنسان أو يقبل على الراكب أو الرامي، في مقابلة الوحشي.","what_is_not_ar":"لا يدخل الإنسان نفسه ولا الأنس النفسي ولا الإبصار."},"support_links":[]},{"boundary":"Dal göz bebeğinde görülen küçük görüntüyü, ayrıca ayrı bir aktarım olarak parmak ucunu kapsar; gözün kendisini veya genel insan türünü belirtmez.","branch_kind":"bare","branch_ref":"root_000059/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:3:3","qac_word_ref":"114:6:3","surface_ar":"نَّاسِ"}],"gloss":"göz bebeğinde görülen küçük yansıma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Göz bebeğinin kara bölümünde görülen küçük insan biçimli görüntüyü veya yansımayı adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı bir aktarımda parmak ucu veya eldeki parmak ucunu anlatan kullanım da aynı adla verilir."}}],"root_ar":"ن و س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir bakanın göz bebeğinde beliren küçük insan biçimli görüntü adlandırıldığında dalın ortak ve temel anlamını karşılar.","boundary_detail":"Dal göz bebeğinde görülen küçük görüntüyü, ayrıca ayrı bir aktarım olarak parmak ucunu kapsar; gözün kendisini veya genel insan türünü belirtmez.","branch_image_ar":"إنسان العين وصورة الإنسان في السواد","concept_gloss":"göz bebeğinde görülen küçük yansıma","contextual_glosses":[{"applicability":"Yansımanın insan biçiminde algılanması özellikle belirtilmek istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Görüntünün göz bebeğinde bulunmasını ve küçük insan biçiminde görünmesini korur."},"facet_ids":["F001"],"text":"göz bebeğindeki küçük insan görüntüsü","usage_role":"explanatory"},{"applicability":"Yalnız parmak ucunu aynı adla veren ayrı kaynak kullanımında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Göz anlamından bağımsız olan parmak ucu kullanımını doğrudan korur."},"facet_ids":["F002"],"text":"parmak ucu","usage_role":"contextual"}],"definition":"Gözün kara bölümünde görülen küçük insan biçimli görüntü veya yansımadır. Ayrı bir kaynak kullanımında aynı ad parmak ucuna da verilir, ancak bu kullanım göz görüntüsü çekirdeğini değiştirmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Göz bebeğinin kara bölümünde görülen küçük insan biçimli görüntüyü veya yansımayı adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Ayrı bir aktarımda parmak ucu veya eldeki parmak ucunu anlatan kullanım da aynı adla verilir."}],"identity_rationale":"Kaynak ifadesinin ortak çekirdeği, gözün kara bölümünde görülen küçük insan biçimli görüntü veya yansımadır. Parmak ucu anlamı tek aktarım içinde eklenir ve gözdeki görüntünün kurucu parçası değildir; bağımlı bir kaynak varyantı olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"göz bebeğinde görülen küçük görüntü veya yansıma"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"göz bebeklerinde görülen küçük görüntüler"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"parmak ucu; eldeki parmak ucunu anlatan kullanım"}],"lexicalization_note":"Çıplak dalın çekirdeği gözün kara bölümündeki küçük görüntüdür. Parmak ucu aktarımı bağımlı bir varyanttır; gözle ilgili belirli biçimlerden genel görüntü veya genel insan anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün aday kartlar değerlendirildi. Anatomik göz bebeği, genel tasvir ve göz organı karşılaştırmaları görüntünün yerini ve türünü en iyi sınırladığı için bu üçü yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Komşu anatomik bölümün kendisidir; odak dal ise o bölümde görülen görüntüdür. Taşıyıcı yapı ile üzerinde beliren yansıma birbirinin yerine kullanılamaz.","focus_only":"Odak dal göz bebeğinde görülen küçük insan biçimli görüntüyü veya yansımayı adlandırır.","gloss":"göz bebeği ile göz bebeğindeki yansıma","neighbor_only":"Komşu dal göz bebeğinin kendisini, onun kara bölümünü ve anatomik yapısını adlandırır.","neighbor_ref":"root_000300/B002","relation_type":"same_field","shared_zone":"İki dal aynı göz bölgesine gönderimde bulunur."},{"boundary_match":"partial","distinction":"Odak görüntü göz bebeğindeki belirli yansımadır; komşu ise konum ve oluşum biçimi bakımından çok daha genel tasvirleri kapsar. Her tasvir gözdeki yansıma değildir.","focus_only":"Odak dal yalnız göz bebeğinde beliren küçük insan biçimli görüntüyü ve ayrı bir parmak ucu varyantını kapsar.","gloss":"gözdeki yansıma ile genel tasvir","neighbor_only":"Komşu dal resim, model, heykel veya başka bir varlığa göre biçimlendirilmiş genel örnekleri kapsar.","neighbor_ref":"root_001397/B008","relation_type":"near_neighbor","shared_zone":"Her iki dal başka bir varlığın görünüşünü taşıyan bir görüntüyü anlatabilir."},{"boundary_match":"field_only","distinction":"Göz, görmeyi sağlayan organdır; odak dal ise gözde görülen yansımadır. Organın adı yansımanın, yansımanın adı da organın genel karşılığı değildir.","focus_only":"Odak dal gören gözün içinde beliren küçük görüntüyü adlandırır.","gloss":"göz organı ile içindeki küçük görüntü","neighbor_only":"Komşu dal görme organı olan gözün kendisini ve onun görme işlevini adlandırır.","neighbor_ref":"root_001069/B001","relation_type":"same_field","shared_zone":"Her iki dal göz ve görme alanına aittir."}],"source_phrase_ar":"إنسان العين صبيها الذي في السواد (maqayis)؛ إنسان العين المثال الذي يرى في السواد أي سواد العين (sihah)؛ الإنسان أيضا إنسان العين وجمعه أناسي والإنسان الأنملة (tahdhib)","source_summary":"Ortak aktarım, göz bebeğinin kara bölümünde görülen küçük görüntüyü bir insan biçimi olarak tanımlar. Buna ek olarak parmak ucu anlamı da bildirilir, fakat bu ek kullanım gözdeki yansıma çekirdeğinden ayrı tutulur.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه إنسان العين: المثال أو الصبي الذي يرى في سواد العين، وما ألحقه تهذيب اللغة من الأنملة أو إنسان الكف.","what_is_not_ar":"لا يدخل الإنسان بمعنى البشر عموما ولا الأنس بمعنى الراحة."},"support_links":[]},{"boundary":"Dal yalnız belirtilen söz kuruluşlarında kişinin kendisini veya seçkin yakınını gösterir; genel insan, gerçek evlatlık ve her türlü arkadaşlık anlamına genişletilemez.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B006","candidate_links":[{"candidate_id":"cand_2abbfecf8a1aa3234623","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:3:3","qac_word_ref":"114:6:3","surface_ar":"نَّاسِ"}],"gloss":"belirli sözlerde kişinin kendisi veya seçilmiş yakını","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiye kendi durumunu soran belirli kuruluşta muhatabın kendisini gösterir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişiye bağlanarak söylendiğinde onun seçilmiş yakınını, özel arkadaşını veya sırdaşını belirtir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı anlam çevresindeki paralel adlar yakın dostu, içten arkadaşı ve oturup konuşulan kişiyi gösterebilir."}}],"root_ar":"ن و س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kaynakta gösterilen soru ve kişi bağlantısı kuruluşlarını topluca açıklarken kullanılabilir; genel bir kişi ya da akraba adı değildir.","boundary_detail":"Dal yalnız belirtilen söz kuruluşlarında kişinin kendisini veya seçkin yakınını gösterir; genel insan, gerçek evlatlık ve her türlü arkadaşlık anlamına genişletilemez.","branch_image_ar":"ابن الإنس للنفس والصفوة","concept_gloss":"belirli sözlerde kişinin kendisi veya seçilmiş yakını","contextual_glosses":[{"applicability":"Muhataba kendi durumunun nasıl olduğu sorulduğunda doğal Türkçe karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sorunun muhatabın kendi durumuna yönelmesini korur."},"facet_ids":["F001"],"text":"kendin; nasılsın","usage_role":"contextual"},{"applicability":"Bir kişinin seçip özel tuttuğu yakın arkadaş veya sırdaş anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yakın kişinin seçilmiş, özel ve güvenilen biri olmasını korur."},"facet_ids":["F002"],"text":"onun en yakını ve sırdaşı","usage_role":"contextual"},{"applicability":"Yakın dost, içten arkadaş ve birlikte oturup konuşulan kişi için sıralanan paralel adları açıklarken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yakınlık, dostluk ve sürekli görüşme ilişkilerini birlikte korur."},"facet_ids":["F003"],"text":"yakın dostum ve görüşme arkadaşım","usage_role":"explanatory"}],"definition":"Belirli bir soru kuruluşunda muhatabın kendisini ve durumunu, başka bir kişiyle kurulan adlandırmada ise onun seçilmiş yakınını, sırdaşını veya sürekli görüştüğü arkadaşını belirtir. İki kullanım aynı kuruluş ailesinde bulunsa da katılımcı ilişkileri ayrıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiye kendi durumunu soran belirli kuruluşta muhatabın kendisini gösterir."},{"facet_id":"F002","role":"core","statement":"Bir kişiye bağlanarak söylendiğinde onun seçilmiş yakınını, özel arkadaşını veya sırdaşını belirtir."},{"facet_id":"F003","role":"associated_use","statement":"Aynı anlam çevresindeki paralel adlar yakın dostu, içten arkadaşı ve oturup konuşulan kişiyi gösterebilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Gerçek bir baba ile erkek çocuk arasındaki soy ilişkisini ekler.","collision":"Sözün amaçlanan kişi ilişkisini gerçek akrabalıkla karıştırır.","fit":"displacement","loses":"Kişinin kendisini veya seçilmiş yakınını gösteren kalıplaşmış gönderimi kaybeder.","preserves":"Kuruluşun yüzeyindeki çocuk ve soy ilişkisi çağrışımını korur."},"text":"oğlu"}],"identity_rationale":"Kaynak ifadesi iki ayrı kalıplaşmış ilişkiyi açıkça ayırır: kişiye kendi durumunu soran sözde kişinin kendisi, bir başkasına bağlanan sözde ise seçilmiş yakın ve sırdaş kastedilir. Yakın arkadaş ve oturup konuşulan kişi için verilen paralel adlar ikinci alanı destekler.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"kendin; kendi durumun nasıl"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"onun seçkin yakını ve sırdaşı"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"yakınım, içten dostum ve görüşme arkadaşım"}],"lexicalization_note":"Kişinin kendisini soran kuruluş, seçilmiş yakını belirten kuruluş ve yakın arkadaş adları ayrı tutulur. Bunların hiçbiri çıplak biçime genel kişi veya akrabalık anlamı olarak taşınmaz.","neighbor_coverage_note":"Aday kartların tamamı incelendi. Kişinin kendisini gösteren başka kuruluş, iç çevre ve genel dostluk alanları iki ayrı gönderimi en iyi sınırlandırdığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ortak gönderim yalnız benlik anlamındadır; kuruluşlar değiştirilemez. Odak dalın seçilmiş yakın ve sırdaş anlamı komşuda bulunmaz.","focus_only":"Odak dal kişinin kendisini belirli bir soru kuruluşunda gösterir ve ayrıca seçilmiş yakın anlamını da taşır.","gloss":"kişinin kendisini gösteren iki ayrı söz","neighbor_only":"Komşu dal şiirsel bir söyleyişte yalnız kişinin kendi benliğini başka bir kalıpla belirtir.","neighbor_ref":"root_001271/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal belirli bir söz kuruluşunda kişinin kendisine gönderimde bulunur."},{"boundary_match":"partial","distinction":"Odak dal çoğunlukla tek bir yakın veya sırdaşı gösterir; komşu kişinin iç çevresini ve işlerine alınan özel kişileri daha geniş kapsar.","focus_only":"Odak dal seçilmiş yakını ve sırdaşı gösterebilir, fakat kişinin kendisini soran ayrı bir kullanım da içerir.","gloss":"seçilmiş yakın ile iç çevre","neighbor_only":"Komşu dal bir kişinin işine ve sırrına alınan bütün iç çevreyi ve özel kişileri topluluk olarak kapsayabilir.","neighbor_ref":"root_000128/B004","relation_type":"near_neighbor","shared_zone":"Güvenilen ve özel tutulan kişi iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Her dost odak daldaki özel adlandırmanın taşıdığı seçilmiş yakın değildir; odak dalın kişinin kendisine gönderimi de genel dostluk alanının dışındadır.","focus_only":"Odak dal özel kuruluşlarla kişinin kendisini ya da seçilmiş yakınını belirtir.","gloss":"seçilmiş sırdaş ile genel dostluk","neighbor_only":"Komşu dal arkadaşlık ve dostluk ilişkisini açık ya da gizli yönleriyle genel olarak anlatır.","neighbor_ref":"root_000397/B001","relation_type":"near_neighbor","shared_zone":"Seçilmiş yakın kişi aynı zamanda dost veya arkadaş olabilir."}],"source_phrase_ar":"كيف ابن إنسك إذا سأله عن نفسه (maqayis)؛ كيف ابن إنسك يعني نفسه وفلان ابن إنس فلان أي صفيه وخاصته وهذا خدني وإنسي وخلصي وجلسي (sihah)؛ كيف ترى ابن إنسك إذا خاطبت الرجل عن نفسه وفلان ابن أنس فلان أي صفيه وأنيسه (tahdhib)؛ قيل ابن إنسك للنفس (mufradat)","source_summary":"Aktarımlar, doğrudan hitapta kişinin kendi durumunu soran kullanım ile birinin seçkin yakını ve sırdaşını gösteren kullanımı birlikte verir. Yakın dost ve sürekli görüşülen arkadaş anlamındaki paralel adlar ikinci ilişki alanını genişletir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه كيف ابن إنسك للسؤال عن النفس، وفلان ابن أنس فلان لصفيه وخاصته، وما قاربه من الخدن والأنيس والخلص والجليس.","what_is_not_ar":"لا يدخل مطلق الإنسان ولا مطلق المؤانسة إلا إذا جاء بصيغة هذا الباب أو قرينته."},"support_links":["sup_0207b38de44bec322512"]},{"boundary":"Dal eve girmeden önce izin ve kabul arama durumuyla sınırlıdır; genel görme, genel yakınlık, eve yerleşme veya barınma anlamına gelmez.","branch_kind":"unresolved","branch_ref":"root_000059/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:3:3","qac_word_ref":"114:6:3","surface_ar":"نَّاسِ"}],"gloss":"girişten önce izin ve kabul arama","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eve girmeden önce selam verip girmek için izin istemeyi ve kabul beklemeyi anlatır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı açıklama, girişten önce içeridekilerden yakınlık ve kabul işareti bulmayı öne çıkarır."}}],"root_ar":"ن و س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir eve girmeden önce selam, izin sorusu veya içeridekilerin kabulünü yoklama yoluyla girişe onay arandığında kullanılır.","boundary_detail":"Dal eve girmeden önce izin ve kabul arama durumuyla sınırlıdır; genel görme, genel yakınlık, eve yerleşme veya barınma anlamına gelmez.","branch_image_ar":"الاستئناس قبل دخول البيوت","concept_gloss":"girişten önce izin ve kabul arama","contextual_glosses":[{"applicability":"Giriş izninin selam ve açık bir izin sorusuyla istendiğini belirten açıklamada uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Selam verme, izin sorma ve girişten önce bekleme işlemlerini korur."},"facet_ids":["F001"],"text":"selam verip girebilir miyim diye sormak","usage_role":"explanatory"},{"applicability":"İçeridekilerin yakınlık ve kabul gösterdiğini anlayarak girişe elverişli ortam bulma yorumunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Girişten önce kabul ve yakınlık işareti bulma yönünü korur."},"facet_ids":["F002"],"text":"girişe açık bir karşılama bulmak","usage_role":"contextual"}],"definition":"Bir eve girmeden önce selam vererek izin istemeyi ve içeridekilerin girişe açık olduğunu anlamayı anlatır. Aktarımın bir yönü doğrudan izin sorusunu, diğer yönü girişe elverişli bir kabul ve yakınlık bulmayı öne çıkarır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eve girmeden önce selam verip girmek için izin istemeyi ve kabul beklemeyi anlatır."},{"facet_id":"F002","role":"source_variant","statement":"Ayrı açıklama, girişten önce içeridekilerden yakınlık ve kabul işareti bulmayı öne çıkarır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yalnız gözle inceleme ve bir şeyi görme anlamını ekler.","collision":"Duyusal fark etme ve çevreye bakıp araştırma dalıyla karışır.","fit":"displacement","loses":"Selam verme, izin isteme ve içeridekilerin kabulünü bekleme koşullarını kaybeder.","preserves":"Girişten önce çevreyi yoklama düşüncesine sınırlı ölçüde yaklaşır."},"text":"bakıp görmek"}],"identity_rationale":"Kaynak ifadesi yalnız eve giriş öncesindeki belirli söz çevresinde açıklanır. Bir aktarım bunu selam verip izin isteme ve girebilir miyim diye sorma olarak, diğeri ise girişe elverişli bir kabul ve yakınlık bulma olarak yorumlar. Dal bu iki açıklamayı korumalı, fakat çıplak biçime genel bakma veya genel rahatlık anlamı yüklememelidir.","lexicalization_note":"Mekanik kapsam çözümlenmemiştir ve eldeki kanıt yalnız giriş öncesi kuruluşu gösterir. Bu nedenle tanım bu söz çevresine bağlanır, çıplak bir genel anlam varsayılmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı. Genel yakınlık, çevreyi gözleme ve barınma senaryosu giriş öncesi izin sınırını en iyi açıkladığı için bu üç ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir giriş davranışı ve onay koşuludur; komşu dal yer ve zamanla sınırlı olmayan duygusal durumdur. Genel yakınlık, giriş izninin yerine geçmez.","focus_only":"Odak dal eve girişten önce selam, izin sorusu ve kabul bekleme yoluyla yürütülen sınırlı bir davranışı anlatır.","gloss":"giriş kabulü ile genel yakınlık duygusu","neighbor_only":"Komşu dal kişi veya şey karşısında genel olarak yabancılık ve ürkme duymayıp yakınlık ve rahatlık hissetmeyi anlatır.","neighbor_ref":"root_000059/B003","relation_type":"near_neighbor","shared_zone":"Kabul gören kişi giriş öncesinde kendini yabancı hissetmeyebilir ve yakınlık işareti bulabilir."},{"boundary_match":"partial","distinction":"Çevreyi gözlemek yalnız bilgi edinir; odak dal içeridekilerden onay almayı amaçlar. Birini görmek veya sesini duymak, tek başına giriş izni değildir.","focus_only":"Odak dal girişten önce selam verip izin ve kabul aramayı gerektirir.","gloss":"izin arama ile çevreyi gözleme","neighbor_only":"Komşu dal görme, işitme, belirti sezme veya çevreye bakarak birini araştırma eylemlerini anlatır.","neighbor_ref":"root_000059/B002","relation_type":"near_neighbor","shared_zone":"Girişten önce içeride birinin bulunup bulunmadığını anlamaya çalışma iki alanı aynı durumda buluşturabilir."},{"boundary_match":"thematic_only","distinction":"Odak dal girişten önceki toplumsal onayı, komşu dal ise bir yere yönelip orada barınmayı anlatır; aralarında sıradan sözcüksel yer değiştirme yoktur.","focus_only":"Odak dal bir eve girmeden önce kabul ve izin arama davranışıdır.","gloss":"eve giriş izni ile barınma","neighbor_only":"Komşu dal bir yere sığınma, yerleşme, barınma veya başkasını barındırma hareketini anlatır.","neighbor_ref":"root_000070/B001","relation_type":"thematic","shared_zone":"İki dal da bir yerle insan arasındaki giriş ve bulunma senaryosunda yer alabilir."}],"source_phrase_ar":"حتى تستأنسوا معناه حتى تستأذنوا وإنما هو حتى تسلموا وتستأنسوا السلام عليكم أأدخل (tahdhib)؛ حتى تستأنسوا أي تجدوا إيناسا (mufradat)","source_summary":"Giriş öncesi davranış iki yönden açıklanır: selam verip açıkça izin istemek ve girebilir miyim diye sormak ya da içeridekilerden girişe elverişli bir kabul ve yakınlık bulmak. Her iki açıklama da eve izinsiz girmeme sınırında birleşir.","sources":["TA","MU"],"what_is_ar":"يدخل فيه تفسير حتى تستأنسوا بالاستئذان أو السلام وطلب الدخول، أو بإيجاد إيناس قبل الدخول.","what_is_not_ar":"لا يدخل مطلق الإبصار أو مطلق الأنس إلا في صيغة الدخول المذكورة."},"support_links":[]},{"boundary":"Dal yalnızca örtme ve gizlenme alanındadır; akıl yitimi, bahçe ve görünmeyen varlık anlamlarını içermez.","branch_kind":"bare","branch_ref":"root_000266/B001","candidate_links":[{"candidate_id":"cand_e9db42b0009db1e8ac36","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جِنَّة","morph_features":"STEM|POS:N|LEM:jin~ap|ROOT:jnn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:2:2","qac_word_ref":"114:6:2","surface_ar":"جِنَّةِ"}],"gloss":"örtme ve duyulardan gizleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey örtülerek ya da gizlenerek duyuların erişiminden çıkarılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir örtünün arkasına saklanma, bir şeyi içinde saklama ve insanı örten giysi aynı gizleme çekirdeğine dayanır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin örtülmesini, bir kişinin saklanmasını veya örtü işlevli bir şeyi birlikte temsil eden en geniş karşılıktır.","boundary_detail":"Dal yalnızca örtme ve gizlenme alanındadır; akıl yitimi, bahçe ve görünmeyen varlık anlamlarını içermez.","branch_image_ar":"الستر والاستتار","concept_gloss":"örtme ve duyulardan gizleme","contextual_glosses":[{"applicability":"Bir öznenin nesneyi görünmez veya algılanamaz duruma getirdiği geçişli kullanımlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geçişli örtme eylemini ve bunun doğurduğu gizlenme sonucunu eksiksiz korur."},"facet_ids":["F001"],"text":"örtüp gizlemek","usage_role":"contextual"},{"applicability":"Kişinin bir örtü veya engel aracılığıyla kendini duyulardan sakladığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Örtü aracını ve öznenin kendisini algıdan saklaması anlamını birlikte korur."},"facet_ids":["F002"],"text":"bir şeyin arkasına gizlenmek","usage_role":"contextual"}],"definition":"Bir şeyi duyuların erişiminden çıkaracak biçimde örtmek ya da gizlemek; kişinin bir şeyin arkasına saklanması, bir şeyi içinde saklaması ve insanı örten giysi bu çekirdeğin gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey örtülerek ya da gizlenerek duyuların erişiminden çıkarılır."},{"facet_id":"F002","role":"extension","statement":"Bir örtünün arkasına saklanma, bir şeyi içinde saklama ve insanı örten giysi aynı gizleme çekirdeğine dayanır."}],"identity_rationale":"Kaynak ifadesi dalı örtme, duyulardan gizleme ve bir örtünün arkasına saklanma çekirdeğinde kurar; içte saklama ile insanı örten giysi de bu çekirdeğin açık gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"örtmek; gizleyecek bir örtü sağlamak; içinde saklamak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şeyin arkasına gizlenmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"insanı örten giysi veya örtü"}],"lexicalization_note":"Tanım yalın dalı kapsar ve başka dallara ya da yalnızca belirli bir söz öbeğine bağlı anlamları içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yakın sınır karşılaştırmasını genel örtme dalı sağladığı için yalnızca bu ayrım yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın kurucu sonucu duyusal erişimden gizlenmedir; komşu dal ise genel örtme ve kaplama alanını daha geniş biçimde adlandırır.","focus_only":"Odak dal, duyulardan saklanmayı, içte gizlemeyi ve insanı örten giysiyi aynı çekirdekte toplar.","gloss":"örtme ve gizleme","neighbor_only":"Komşu dal, örtü ve örtme araçlarının genel söz varlığını daha doğrudan kapsar.","neighbor_ref":"root_000674/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyi örtme ve böylece görünmesini engelleme alanında buluşur."}],"source_phrase_ar":"الجيم والنون أصل واحد وهو الستر والتستر (maqayis)؛ أصل الجن ستر الشيء عن الحاسة (mufradat)؛ استجن فلان إذا استتر بشيء (ayn;tahdhib)؛ أجننت الشيء في صدري أكننته (sihah)؛ ما علي جنان إلا ما ترى أي ثوب يواريني (sihah;tahdhib)","source_summary":"Kaynakların ortak ekseni, bir şeyi duyusal algıdan örterek gizlemek ve bu örtünün sağladığı saklılık durumudur.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه ستر الشيء عن الحس والاستتار بشيء وإكنان الشيء في الصدر وما يواري من ثوب أو غيره","what_is_not_ar":"ليس الجنون ولا الجنة ولا الجن"},"support_links":["sup_cfc6709aca10eec8bc5f"]},{"boundary":"Sırf gece, sırf karanlık veya güneşin batması yeterli değildir; karanlığın bir şeyi örtmesi kurucudur.","branch_kind":"bare","branch_ref":"root_000266/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جِنَّة","morph_features":"STEM|POS:N|LEM:jin~ap|ROOT:jnn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:2:2","qac_word_ref":"114:6:2","surface_ar":"جِنَّةِ"}],"gloss":"gecenin karartıp örtmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gece kararır ve karanlığı bir şeyin üzerini örter."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gece karanlığının bir kişi, yer veya nesneyi kaplayıp görünmez kıldığı bütün yalın kullanımlara uygundur.","boundary_detail":"Sırf gece, sırf karanlık veya güneşin batması yeterli değildir; karanlığın bir şeyi örtmesi kurucudur.","branch_image_ar":"غشيان الليل","concept_gloss":"gecenin karartıp örtmesi","contextual_glosses":[{"applicability":"Bir yerin veya nesnenin gece bastığında karanlık içinde görünmez hale geldiği anlatımlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gecenin bastırmasını ve nesnenin karanlıkla örtülmesini birlikte korur."},"facet_ids":["F001"],"text":"gece karanlığına gömülmek","usage_role":"contextual"}],"definition":"Gecenin kararması ve bir şeyi kendi karanlığıyla örterek görünmez kılmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gece kararır ve karanlığı bir şeyin üzerini örter."}],"identity_rationale":"Kaynak ifadesi yalnızca gecenin kararıp bir şeyi karanlığıyla örtmesini bildirir; dalın gece karanlığı ile örtme işlemini birlikte tutan çerçevesi buna uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"gecenin kararıp üzerini örtmesi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"gecenin koyu karanlığı ve nesneleri örtmesi"}],"lexicalization_note":"Tanım yalın dalı verir; başka gece sözlerine veya insan topluluğu ve iç dünya anlamlarına genişletilmez.","neighbor_coverage_note":"Bütün gece, ışık ve aynı kökten gelen dal adayları değerlendirildi; örtme koşulunu en iyi sınayan kararma dalı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu için kararma yeterliyken odak dalda karanlığın bir kişi, yer veya nesneyi örtmesi anlamın kurucu parçasıdır.","focus_only":"Odak dalda gece karanlığı yalnızca artmaz, aynı zamanda bir şeyin üzerini örter.","gloss":"gecenin kararması","neighbor_only":"Komşu dal gecenin karanlık hale gelmesini örtülen bir nesne şartı olmadan kapsar.","neighbor_ref":"root_001094/B001","relation_type":"near_synonym","shared_zone":"İki dal da gecenin karanlıklaşması ve yoğun karanlık alanında örtüşür."}],"source_phrase_ar":"جنان الليل سواده وستره الأشياء (maqayis)؛ أجنه الليل وجن عليه الليل إذا أظلم حتى يستره بظلمته (ayn)؛ جن عليه الليل يجن بالضم جنونا (sihah)؛ جن عليه الليل وأجنه الليل إذا أظلم حتى يستره بظلمته (tahdhib)؛ جنه الليل وأجنه وجن عليه (mufradat)","source_summary":"Kaynaklar gecenin kararmasını, bu karanlığın nesneleri örtüp görünmez kılmasıyla birlikte anlatır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه جن الليل على الشيء إذا أظلم وستره بسواده","what_is_not_ar":"ليس سواد الناس ولا الجنان بمعنى القلب"},"support_links":[]},{"boundary":"Her çevrili alan veya her ekili toprak bu dala girmez; ağaçlı bahçe ve ağaçların örttüğü zemin esastır.","branch_kind":"bare","branch_ref":"root_000266/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جِنَّة","morph_features":"STEM|POS:N|LEM:jin~ap|ROOT:jnn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:2:2","qac_word_ref":"114:6:2","surface_ar":"جِنَّةِ"}],"gloss":"zemini ağaçlarla örtülü bahçe","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ağaçlı bahçenin zemini ağaçların oluşturduğu örtü altında kalır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ağaçların veya hurmalıkların yoğunluğu sayesinde zemini örtülen bahçe ve koruluklar için tam karşılıktır.","boundary_detail":"Her çevrili alan veya her ekili toprak bu dala girmez; ağaçlı bahçe ve ağaçların örttüğü zemin esastır.","branch_image_ar":"البستان المستور بالشجر","concept_gloss":"zemini ağaçlarla örtülü bahçe","contextual_glosses":[{"applicability":"Bağlam zeminin ağaçlarla örtülü olduğunu zaten gösterdiğinde doğal ve kısa bir çeviridir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ağaçlarla kaplı bahçe referansını bağlam desteğiyle eksiksiz korur."},"facet_ids":["F001"],"text":"ağaçlık bahçe","usage_role":"contextual"}],"definition":"Ağaçları, özellikle de sık ağaç veya hurmalıkları zemini örten bahçe ya da koruluk niteliğindeki yerdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ağaçlı bahçenin zemini ağaçların oluşturduğu örtü altında kalır."}],"identity_rationale":"Kaynak ifadesi bahçeyi ağaçları veya hurmalıkları toprağı örten ağaçlı bir yer olarak tanımlar; dalın ağaç örtüsünü merkeze alan çerçevesi kaynağa uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"zemini ağaçlarla örtülü bahçe veya koruluk"}],"lexicalization_note":"Tanım yalın ağaçlı bahçe anlamını taşır ve ölüm sonrası ödül yurdu ya da genel bitki örtüsü anlamını içeri almaz.","neighbor_coverage_note":"Bütün bahçe, hurmalık, bitki ve aynı kökten dal adayları değerlendirildi; dış sınır ile ağaç örtüsü karşıtlığı en yararlı ayrımdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta içteki ağaç örtüsü, komşuda ise alanı dıştan kuşatan sınır belirleyicidir; bu yüzden sıradan bağlamda birbirlerinin yerine geçmezler.","focus_only":"Odak dal bahçeyi ağaçların zemini örtmesiyle tanımlar.","gloss":"ağaç örtülü ve çevrili bahçe","neighbor_only":"Komşu dal bahçeyi çevresindeki duvar, engel veya yükseltiyle tanımlar.","neighbor_ref":"root_000300/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da ağaç veya bitki içeren sınırlı bir bahçe alanına gönderimde bulunabilir."}],"source_phrase_ar":"الجنة البستان (maqayis;sihah)؛ الجنة الحديقة وهي بستان ذات شجر ونزهة (ayn)؛ العرب تسمي النخيل جنة (sihah)؛ كل بستان ذي شجر يستر بأشجاره الأرض (mufradat)","source_summary":"Kaynaklar anlamı bahçe, ağaçlı bahçe ve hurmalık çevresinde birleştirir; ayırt edici özellik ağaçların zemini örtmesidir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الجنة بمعنى البستان والحديقة ذات الشجر والنخل الساتر","what_is_not_ar":"ليس الجنة الأخروية ولا الجنون"},"support_links":[]},{"boundary":"Dal ölüm sonrası ödül yurduyla sınırlıdır; dünyadaki ağaçlı bahçe veya görünmeyen varlıklar topluluğu değildir.","branch_kind":"bare","branch_ref":"root_000266/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جِنَّة","morph_features":"STEM|POS:N|LEM:jin~ap|ROOT:jnn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:2:2","qac_word_ref":"114:6:2","surface_ar":"جِنَّةِ"}],"gloss":"ölüm sonrası gizli nimetler yurdu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Müslümanların ölümden sonra varacağı ödül yurdunun nimetleri bugün kendilerinden gizlidir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlandırma ya dünyadaki ağaçlı bahçeye benzetilmekte ya da nimetlerin şimdilik gizli oluşuyla açıklanmaktadır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Müslümanların ölümden sonra ulaşacağı ödül yurdundan ve henüz görünmeyen nimetlerinden söz edilen bağlamlara uygundur.","boundary_detail":"Dal ölüm sonrası ödül yurduyla sınırlıdır; dünyadaki ağaçlı bahçe veya görünmeyen varlıklar topluluğu değildir.","branch_image_ar":"الجنة الأخروية","concept_gloss":"ölüm sonrası gizli nimetler yurdu","contextual_glosses":[{"applicability":"Nimetlerin henüz görünmediği bilgisi bağlamdan anlaşıldığında akıcı bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölüm sonrası varış yerini ve ödül olma niteliğini bağlam desteğiyle korur."},"facet_ids":["F001"],"text":"ölüm sonrası ödül yurdu","usage_role":"contextual"}],"definition":"Müslümanların ölümden sonra ulaşacağı, ödülü ve nimetleri bugün onlardan gizli olan yurttur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Müslümanların ölümden sonra varacağı ödül yurdunun nimetleri bugün kendilerinden gizlidir."},{"facet_id":"F002","role":"source_variant","statement":"Adlandırma ya dünyadaki ağaçlı bahçeye benzetilmekte ya da nimetlerin şimdilik gizli oluşuyla açıklanmaktadır."}],"identity_rationale":"Kaynak ifadesi Müslümanların ölümden sonra ulaşacağı ödül yurdunu ve bugün onlardan gizli olan nimetlerini bildirir; dünyevi bahçe benzetmesi yalnızca adlandırma açıklamasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ölüm sonrası ödül ve gizli nimetler yurdu"}],"lexicalization_note":"Tanım yalın ölüm sonrası ödül yurdu anlamını korur ve dünyadaki bahçe anlamını bu dala katmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dış adaylar bitki adlarıyla sınırlı kaldığından en açıklayıcı karşılaştırma aynı kökün dünyevi bahçe dalıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Biri ölüm sonrası ve inanç alanına ait bir varış yeridir, diğeri dünyadaki ağaçlı bir alandır; benzetme referansları özdeş kılmaz.","focus_only":"Odak dal ölüm sonrası ulaşılan ödül yurdunu ve bugün gizli olan nimetleri bildirir.","gloss":"ödül yurdu ve ağaçlı bahçe","neighbor_only":"Komşu dal dünyadaki, zemini ağaçlarla örtülü somut bir bahçeyi bildirir.","neighbor_ref":"root_000266/B003","relation_type":"near_neighbor","shared_zone":"Adlandırma, ödül yurdunu ağaçlı bahçe imgesiyle ilişkilendirebilir."}],"source_phrase_ar":"الجنة ما يصير إليه المسلمون في الآخرة وهو ثواب مستور عنهم اليوم (maqayis)؛ سميت الجنة إما تشبيها بالجنة في الأرض وإما لستره نعمها عنا (mufradat)","source_summary":"Kaynaklar ölüm sonrası ödül yurdunda birleşir; adın gerekçesini ağaçlı bahçe benzetmesi veya nimetlerin bugün gizli olmasıyla açıklar.","sources":["MQ","MU"],"what_is_ar":"يدخل فيه الجنة التي يصير إليها المسلمون وثوابها المستور عنهم","what_is_not_ar":"ليس البستان الدنيوي ولا جماعة الجن"},"support_links":[]},{"boundary":"Yılan adı ve akıl yitimi bu dalın dışında kalır; yer anlamı yalnızca çokluk bildiren belirli söz öbeğine bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000266/B005","candidate_links":[{"candidate_id":"cand_bc63b3f17f545819a1f6","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جِنَّة","morph_features":"STEM|POS:N|LEM:jin~ap|ROOT:jnn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:2:2","qac_word_ref":"114:6:2","surface_ar":"جِنَّةِ"}],"gloss":"gözle görülmeyen ruhani varlıklar topluluğu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ruhani varlıklar insan gözünden ve duyularından gizlidir; ad hem türü hem topluluğunu karşılayabilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tekil biçim bu varlıkların atasını veya bir bireyini, başka biçimler ise topluluğunu bildirir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu varlıkların çok bulunduğu yer anlamı yalın değildir ve belirli bir yer söz öbeğiyle sınırlıdır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın biçimlerin gizli ruhani varlık türünü veya bu türün topluluğunu bildirdiği genel bağlamlara uygundur.","boundary_detail":"Yılan adı ve akıl yitimi bu dalın dışında kalır; yer anlamı yalnızca çokluk bildiren belirli söz öbeğine bağlıdır.","branch_image_ar":"الجن المستترون","concept_gloss":"gözle görülmeyen ruhani varlıklar topluluğu","contextual_glosses":[{"applicability":"Söz konusu türün tek bir bireyi veya atası anlatıldığında tekil bağlama uyar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Birey olmayı, ruhani niteliği ve insan duyularından gizli oluşu korur."},"facet_ids":["F001","F002"],"text":"görünmeyen ruhani varlık","usage_role":"contextual"},{"applicability":"Yalnızca kanıtta verilen yer söz öbeğinin çokluk bildiren bağımlı kullanımında geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yer referansını, varlıkların çokluğunu ve kullanımın söz öbeğine bağlılığını korur."},"facet_ids":["F003"],"text":"görünmeyen varlıkların çok bulunduğu yer","usage_role":"explanatory"}],"definition":"İnsanların duyularından gizli kabul edilen ruhani varlıklar ve onların topluluğudur. Bu varlıklardan çok bulunan yer anlamı yalnızca ilgili yer söz öbeğine bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ruhani varlıklar insan gözünden ve duyularından gizlidir; ad hem türü hem topluluğunu karşılayabilir."},{"facet_id":"F002","role":"specialization","statement":"Tekil biçim bu varlıkların atasını veya bir bireyini, başka biçimler ise topluluğunu bildirir."},{"facet_id":"F003","role":"extension","statement":"Bu varlıkların çok bulunduğu yer anlamı yalın değildir ve belirli bir yer söz öbeğiyle sınırlıdır."}],"identity_rationale":"Kaynak ifadesi insan gözünden gizli ruhani varlıkları, onların tekil ve topluluk adlarını ve bu varlıkların çok bulunduğu yer için kullanılan bağımlı söz öbeğini birlikte verir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"gözle görülmeyen ruhani varlıklar"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"görünmeyen varlıkların atası veya bir bireyi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"görünmeyen ruhani varlıkların topluluğu"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"görünmeyen ruhani varlıkların çok bulunduğu yer"}],"lexicalization_note":"Yalın varlık ve topluluk anlamları, bu varlıkların çok bulunduğu yeri bildiren söz öbeğine bağlı kullanımdan ayrı tutulur.","neighbor_coverage_note":"Bütün varlık, canlı, yer ve aynı kökten adaylar değerlendirildi; genel tür ile ayrı alt topluluk arasındaki sınır en yararlı ayrımdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak genel tür ve topluluk adıdır; komşu ise aynı alandaki ayrı bir sınıf veya ona bağlı varlıkları bildirir, bu yüzden ikame edilemez.","focus_only":"Odak dal görünmeyen ruhani varlık türünün genel adını, bireyini ve topluluğunu kapsar.","gloss":"görünmeyen varlıklar ve bir alt topluluk","neighbor_only":"Komşu dal bu alandaki ayrı bir topluluğu, alt türü veya onlara bağlanan köpekleri bildirir.","neighbor_ref":"root_000364/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal insan gözünden gizli kabul edilen ruhani varlıklar alanındadır."}],"source_phrase_ar":"الجن سموا بذلك لأنهم متسترون عن أعين الخلق (maqayis)؛ الجن جماعة ولد الجان وجمعهم الجنة والجنان (ayn;tahdhib)؛ الجن خلاف الإنس والواحد جني (sihah)؛ الجنة جماعة الجن (mufradat)؛ أرض مجنة كثيرة الجن (ayn;sihah;tahdhib)","source_summary":"Kaynaklar insan duyularından gizli ruhani varlıklar çekirdeğinde birleşir; birey, ata, topluluk ve çok bulundukları yer için ayrı biçimler verir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الجن والجان والجنة جماعة الجن والموضع الكثير الجن","what_is_not_ar":"ليس الجان بمعنى الحية ولا الجنة بمعنى الجنون"},"support_links":["sup_8b3ac0a346f5af86ab66"]},{"boundary":"Dal gerçek ya da gösterilen akıl yitimiyle sınırlıdır; görünmeyen varlıklar ve ağaçlı bahçe anlamları dışarıda kalır.","branch_kind":"bare","branch_ref":"root_000266/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جِنَّة","morph_features":"STEM|POS:N|LEM:jin~ap|ROOT:jnn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:2:2","qac_word_ref":"114:6:2","surface_ar":"جِنَّةِ"}],"gloss":"aklı örten akıl yitimi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Akıl yitimi, aklın örtülmesi veya benlik ile akıl arasına engel girmesi olarak kavranır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin aklını yitirmesi ile bir etkenin onu bu duruma getirmesi katılımcıları farklı iki süreçtir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gerçek durumdan ayrı olarak kişi kendisini aklını yitirmiş gibi gösterebilir."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin akıl işleyişini kaybettiği veya aklı ile benliği arasına engel girdiği genel durumlara uygundur.","boundary_detail":"Dal gerçek ya da gösterilen akıl yitimiyle sınırlıdır; görünmeyen varlıklar ve ağaçlı bahçe anlamları dışarıda kalır.","branch_image_ar":"ستر العقل بالجنون","concept_gloss":"aklı örten akıl yitimi","contextual_glosses":[{"applicability":"Kişinin gerçek bir akıl yitimi durumuna girdiği geçişsiz kullanımlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin akıl işleyişini kaybetmesini ve durum değişimini korur."},"facet_ids":["F001","F002"],"text":"aklını yitirmek","usage_role":"contextual"},{"applicability":"Kişinin gerçek durumu değil, bu durumun görünüşünü isteyerek sergilediği bağlamlara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Akıl yitimini gerçek yaşamadan onun görünüşünü sergileme ayrımını korur."},"facet_ids":["F003"],"text":"aklını yitirmiş gibi davranmak","usage_role":"contextual"}],"definition":"Aklın işleyişini örten veya benlik ile akıl arasına engel koyan akıl yitimi durumudur; kişi bu duruma düşebilir, düşürülebilir ya da böyleymiş gibi davranabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Akıl yitimi, aklın örtülmesi veya benlik ile akıl arasına engel girmesi olarak kavranır."},{"facet_id":"F002","role":"extension","statement":"Kişinin aklını yitirmesi ile bir etkenin onu bu duruma getirmesi katılımcıları farklı iki süreçtir."},{"facet_id":"F003","role":"associated_use","statement":"Gerçek durumdan ayrı olarak kişi kendisini aklını yitirmiş gibi gösterebilir."}],"identity_rationale":"Kaynak ifadesi aklın örtülmesini, benlik ile akıl arasına engel girmesini, kişinin bu duruma düşmesini veya düşürülmesini bildirir; görünüşte bu hali takınma da ayrı bir kullanımdır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"aklını yitirmek; aklını yitirmiş duruma getirmek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"akıl yitimi; benlik ile akıl arasındaki engel"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"aklını yitirmiş gibi davranmak"}],"lexicalization_note":"Tanım yalın akıl yitimi dalını kapsar ve başka dalların varlık ya da yer anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün akıl, karar, görünmeyen etki ve aynı kökten adaylar değerlendirildi; kapsamı en çok çakışan bozulma dalı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak örtülme temelli akıl yitimini ve onun dilbilgisel süreçlerini öne çıkarır; komşu ise neden ve bozulma türleri bakımından daha geniştir.","focus_only":"Odak dal akıl yitimini örtülme veya benlik ile akıl arasına giren engel olarak kurar ve bu görünüşü takınmayı da kapsar.","gloss":"akıl işleyişinin bozulması","neighbor_only":"Komşu dal akıl ve yürek bozulmasını hastalık, dokunma, sevgi veya başka etkenlerle daha geniş biçimde ilişkilendirir.","neighbor_ref":"root_000390/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da aklın sağlıklı işleyişini yitirmesi alanında önemli ölçüde örtüşür."}],"source_phrase_ar":"الجنة الجنون وذلك أنه يغطي العقل (maqayis)؛ المجنة الجنون وجن الرجل وأجنه الله فهو مجنون (ayn)؛ جن الرجل جنونا وأجنه الله فهو مجنون (sihah)؛ به جنون وجنة ومجنة (tahdhib)؛ الجنون حائل بين النفس والعقل (mufradat)","source_summary":"Kaynaklar akıl işleyişinin örtülmesi ve kişinin aklını yitirmesi çekirdeğinde birleşir; ettirgen süreç ile görünüşte bu hali takınmayı da kaydeder.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الجنون والجنة والمجنة والجنن ومجنون وتجانن إذا تعلق المعنى بزوال العقل أو إظهاره","what_is_not_ar":"ليس الجن ولا الجنة البستان"},"support_links":[]},{"boundary":"Dal rahimdeki çocuk ve onun saklı bulunduğu dönemle sınırlıdır; gömülmüş kişi veya gömüt anlamına gelmez.","branch_kind":"bare","branch_ref":"root_000266/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جِنَّة","morph_features":"STEM|POS:N|LEM:jin~ap|ROOT:jnn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:2:2","qac_word_ref":"114:6:2","surface_ar":"جِنَّةِ"}],"gloss":"ana rahmindeki doğmamış çocuk","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çocuk, annesinin karnında veya rahminde bulunduğu süre boyunca doğmamış durumdadır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Annenin doğmamış çocuğu taşıması ile çocuğun rahimde saklı bulunması katılımcıları farklı bağlantılı süreçlerdir."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çocuğun doğumdan önce annesinin karnında veya rahminde bulunduğu bütün yalın bağlamlara uygundur.","boundary_detail":"Dal rahimdeki çocuk ve onun saklı bulunduğu dönemle sınırlıdır; gömülmüş kişi veya gömüt anlamına gelmez.","branch_image_ar":"الجنين المستور في البطن","concept_gloss":"ana rahmindeki doğmamış çocuk","contextual_glosses":[{"applicability":"Annenin doğmamış çocuğu karnında taşıdığı süreç özne üzerinden anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Annenin taşıyan katılımcı, çocuğun da rahimde saklı katılımcı oluşunu korur."},"facet_ids":["F002"],"text":"rahminde çocuk taşımak","usage_role":"contextual"}],"definition":"Doğmamış çocuk, annesinin karnında veya rahminde kaldığı süre boyunca bu dalın referansıdır; annenin onu taşıması ve çocuğun rahimde saklı kalması buna bağlı süreçlerdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çocuk, annesinin karnında veya rahminde bulunduğu süre boyunca doğmamış durumdadır."},{"facet_id":"F002","role":"associated_use","statement":"Annenin doğmamış çocuğu taşıması ile çocuğun rahimde saklı bulunması katılımcıları farklı bağlantılı süreçlerdir."}],"identity_rationale":"Kaynaklar çocuğu annesinin karnında veya rahminde kaldığı süre boyunca tanımlar ve annenin bu çocuğu taşımasıyla çocuğun rahimde saklı kalmasını ayrı süreçler olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"ana rahmindeki doğmamış çocuk"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"rahminde çocuk taşımak; çocuğun rahimde saklı kalması"}],"lexicalization_note":"Tanım yalın rahimdeki çocuk anlamını korur; gebelik, doğum veya gömme alanının tamamına genişletilmez.","neighbor_coverage_note":"Bütün rahim, gebelik, doğum ve aynı kökten adaylar değerlendirildi; çocuk ile gebelik durumu ayrımı en açıklayıcı sınırı verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği rahimdeki çocuktur; komşu dalın çekirdeği ise annenin taşıma durumu ve bunun süresidir.","focus_only":"Odak dal anne rahminde bulunan doğmamış çocuğu referans alır.","gloss":"doğmamış çocuk ve gebelik","neighbor_only":"Komşu dal annenin gebelik durumunu, süresini ve karındaki yükü daha geniş biçimde kapsar.","neighbor_ref":"root_000291/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da annenin karnındaki çocuk ve doğum öncesi dönem alanındadır."}],"source_phrase_ar":"الجنين الولد في بطن أمه (maqayis)؛ أجنت الحامل الجنين أي الولد في بطنها (ayn)؛ الجنين الولد ما دام في البطن (sihah)؛ الجنين الولد في الرحم (tahdhib)؛ الجنين الولد ما دام في بطن أمه (mufradat)","source_summary":"Kaynaklar rahimde veya anne karnında bulunan doğmamış çocuk tanımında birleşir; taşıma ve rahimde saklı kalma süreçlerini de kaydeder.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الجنين والولد ما دام في بطن أمه وأجنة البطون","what_is_not_ar":"ليس المقبور ولا القبر"},"support_links":[]},{"boundary":"Dal koruyucu siper veya savaş donanımıyla sınırlıdır; bahçe, akıl yitimi ve sıradan örtü anlamlarına genişlemez.","branch_kind":"bare","branch_ref":"root_000266/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جِنَّة","morph_features":"STEM|POS:N|LEM:jin~ap|ROOT:jnn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:2:2","qac_word_ref":"114:6:2","surface_ar":"جِنَّةِ"}],"gloss":"koruyucu siper veya savaş donanımı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir örtü veya savaş donanımı kişiyi tehlikeden koruyan siper işlevi görür."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kalkan ve zırh, koruyucu siper çekirdeğinin açık araç türleridir."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalkan, zırh ya da kişinin arkasına sığınıp kendini koruduğu başka bir savaş örtüsü için uygundur.","boundary_detail":"Dal koruyucu siper veya savaş donanımıyla sınırlıdır; bahçe, akıl yitimi ve sıradan örtü anlamlarına genişlemez.","branch_image_ar":"الجُنّة الواقية","concept_gloss":"koruyucu siper veya savaş donanımı","contextual_glosses":[{"applicability":"Kaynak biçim özellikle elde taşınan koruyucu savaş aracını gösterdiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Elde taşınan siper aracını ve sahibini koruma işlevini tam olarak korur."},"facet_ids":["F001","F002"],"text":"kalkan","usage_role":"contextual"}],"definition":"Kişinin tehlikeden korunmak için arkasına sığındığı veya üzerine aldığı koruyucu örtü ya da savaş donanımıdır; kalkan ve zırh bunun başlıca türleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir örtü veya savaş donanımı kişiyi tehlikeden koruyan siper işlevi görür."},{"facet_id":"F002","role":"specialization","statement":"Kalkan ve zırh, koruyucu siper çekirdeğinin açık araç türleridir."}],"identity_rationale":"Kaynak ifadesi korunmak için arkasına sığınılan silah veya örtüyü genel çekirdek, kalkanı ve zırhı ise belirgin gerçekleşmeler olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"koruyucu örtü, siper veya savaş donanımı"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kalkan"}],"lexicalization_note":"Tanım yalın koruyucu örtü ve silah anlamını kapsar; yalnızca belirli bir savaş söz öbeğine bağlanmaz.","neighbor_coverage_note":"Bütün kalkan, zırh, hazırlık, korunma ve aynı kökten adaylar değerlendirildi; giyilebilir zırh ile genel siper ayrımı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kalkan gibi giyilmeyen siperleri de kapsar; komşu ise giyilebilir zırh ve korunma giysisine daha sıkı bağlıdır.","focus_only":"Odak dal kalkanı ve korunmak için arkasına sığınılan her türlü savaş örtüsünü kapsar.","gloss":"koruyucu savaş donanımı","neighbor_only":"Komşu dal özellikle savaşta giyilen zırhı ve giyilebilir koruyucu donanımı öne çıkarır.","neighbor_ref":"root_001341/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da savaşta bedeni saldırıdan koruyan araç ve donanımları bildirir."}],"source_phrase_ar":"المجن الترس وكل ما استتر به من السلاح فهو جنة (maqayis)؛ المجن الترس والجنة الدرع وكل ما وقاك فهو جنتك (ayn)؛ الجنة ما استترت به من سلاح والجنة السترة والمجن الترس (sihah)؛ المجن الترس (tahdhib)؛ المجن والمجنة الترس الذي يجن صاحبه (mufradat)","source_summary":"Kaynaklar korunmak için kullanılan örtü veya silah çekirdeğinde birleşir ve özellikle kalkan ile zırhı bu kapsamda anar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الجنة التي يتقى بها والمجن الترس والسلاح وما وقاك","what_is_not_ar":"ليس الجنة البستان ولا الجنون"},"support_links":[]},{"boundary":"Dal ölü ve gömme alanındadır; anne rahmindeki doğmamış çocuk anlamıyla yalnızca biçim benzerliği paylaşır.","branch_kind":"bare","branch_ref":"root_000266/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جِنَّة","morph_features":"STEM|POS:N|LEM:jin~ap|ROOT:jnn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:2:2","qac_word_ref":"114:6:2","surface_ar":"جِنَّةِ"}],"gloss":"ölüyü örtüp gömme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ölü örtülerek gözden kaldırılır ve toprağa gömülür."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gömüt, ölü örtüsü ve gömülmüş kişi aynı işlemin sırasıyla yer, araç ve sonuç katılımcılarını adlandırır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ölünün gözden kaldırılarak toprağa verilmesini ve bu işlemin örtme yönünü birlikte anlatan bağlamlara uygundur.","boundary_detail":"Dal ölü ve gömme alanındadır; anne rahmindeki doğmamış çocuk anlamıyla yalnızca biçim benzerliği paylaşır.","branch_image_ar":"مواراة الميت","concept_gloss":"ölüyü örtüp gömme","contextual_glosses":[{"applicability":"Örtme ayrıntısının gömme eyleminden doğal olarak anlaşıldığı akıcı anlatımlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölü katılımcısını ve gömerek gözden kaldırma işlemini bağlam içinde korur."},"facet_ids":["F001"],"text":"ölüyü toprağa vermek","usage_role":"contextual"}],"definition":"Ölüyü örterek gözden kaldırmak ve toprağa gömmektir; gömüt, ölü örtüsü ve gömülmüş kişi bu işlemin yer, araç ve sonuç odaklı adlarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ölü örtülerek gözden kaldırılır ve toprağa gömülür."},{"facet_id":"F002","role":"extension","statement":"Gömüt, ölü örtüsü ve gömülmüş kişi aynı işlemin sırasıyla yer, araç ve sonuç katılımcılarını adlandırır."}],"identity_rationale":"Kaynak ifadesi ölüyü örterek gözden kaldırma ve gömme eylemini, gömütü, ölü örtüsünü ve gömülmüş kişiyi aynı dalda açıkça kaydeder.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"ölüyü örtmek ve gömmek"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"gömüt; ölü örtüsü; gömülmüş kişi"}],"lexicalization_note":"Tanım yalın gömme ve ölü örtme dalını kapsar; genel çukur açma veya doğmamış çocuk anlamına genişletilmez.","neighbor_coverage_note":"Bütün gömme, gömüt, örtme ve aynı kökten adaylar değerlendirildi; genel gömüt dalı en yakın fakat kapsamı farklı komşudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak örtüp gözden kaldırma çekirdeği ile ölü örtüsü sonucunu korur; komşu ise gömüt kurumu ve gömme izni gibi daha geniş işlemleri kapsar.","focus_only":"Odak dal gömmenin yanında ölü örtüsünü ve gömülmüş kişi yorumunu da aynı biçim alanında taşır.","gloss":"ölüyü gömme","neighbor_only":"Komşu dal gömüt yerini, gömme eylemini, gömüt hazırlamayı ve gömülmeye izin vermeyi daha geniş biçimde kapsar.","neighbor_ref":"root_001195/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da ölünün gömüte yerleştirilerek toprağa verilmesi alanında örtüşür."}],"source_phrase_ar":"الجنين المقبور (maqayis)؛ الجنن القبر وقيل للكفن أيضا (ayn)؛ جننت الميت وأجننته أي واريته والجنن القبر (sihah)؛ جننته في القبر وأجننته والجنن القبر والجنن الكفن (tahdhib)؛ الجنين القبر (mufradat)","source_summary":"Kaynaklar ölüyü örtüp gömme eyleminde birleşir; aynı biçim alanında gömüt, ölü örtüsü ve gömülmüş kişi yorumlarını da verir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه جن الميت وأجنه إذا واراه والجنن القبر والكفن والجنين بمعنى المقبور أو القبر","what_is_not_ar":"ليس الجنين في الرحم"},"support_links":[]},{"boundary":"Dal içte saklı yürek ve gizli yönle sınırlıdır; gece karanlığı veya insan topluluğu anlamlarını içermez.","branch_kind":"bare","branch_ref":"root_000266/B010","candidate_links":[{"candidate_id":"cand_2abbfecf8a1aa3234623","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جِنَّة","morph_features":"STEM|POS:N|LEM:jin~ap|ROOT:jnn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:2:2","qac_word_ref":"114:6:2","surface_ar":"جِنَّةِ"}],"gloss":"duyulardan saklı yürek ve gizli yön","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yürek ve onun korkuyla sarsılan iç yönü bedende duyulardan saklıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir işin gizli veya görünmeyen yanı, içte saklı olma özelliğinden türeyen soyut kullanımdır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem bedende saklı yüreği hem de bir işin görünmeyen iç yönünü kapsaması gereken genel açıklamalarda kullanılır.","boundary_detail":"Dal içte saklı yürek ve gizli yönle sınırlıdır; gece karanlığı veya insan topluluğu anlamlarını içermez.","branch_image_ar":"الجنان المستور في الصدر","concept_gloss":"duyulardan saklı yürek ve gizli yön","contextual_glosses":[{"applicability":"Bedendeki iç organ veya korkunun yerleştiği iç merkez anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bedende saklı iç organı ve duygusal iç merkez işlevini korur."},"facet_ids":["F001"],"text":"yürek","usage_role":"contextual"},{"applicability":"Somut organ değil, bir olayın görünmeyen veya saklı tarafı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Soyut iş referansını ve onun görünmeyen iç tarafını eksiksiz korur."},"facet_ids":["F002"],"text":"işin gizli yönü","usage_role":"contextual"}],"definition":"Duyulardan saklı olduğu için yürek veya yüreğin iç yönü; buradan hareketle bir işin gizli, görünmeyen yanı anlamıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yürek ve onun korkuyla sarsılan iç yönü bedende duyulardan saklıdır."},{"facet_id":"F002","role":"extension","statement":"Bir işin gizli veya görünmeyen yanı, içte saklı olma özelliğinden türeyen soyut kullanımdır."}],"identity_rationale":"Kaynak ifadesi duyulardan saklı iç organı ve onun korkuyla sarsılan iç yönünü, ayrıca gizli iş veya görünmeyen yön kullanımını açıkça ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yürek veya yüreğin saklı iç yönü"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"gizli iş veya görünmeyen yön"}],"lexicalization_note":"Tanım yalın içte saklı yürek ve gizli yön anlamlarını kapsar; başka söz öbeklerinden anlam aktarmaz.","neighbor_coverage_note":"Bütün göğüs, yürek, gizli iş ve aynı kökten adaylar değerlendirildi; iç organ ile içte saklama eylemi ayrımı en yararlı karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak bir iç organı veya gizli yönü adlandırır; komşu ise bir içeriği zihinde saklama eylemini kurar, bu nedenle çekirdekleri farklıdır.","focus_only":"Odak dal öncelikle duyulardan saklı yüreği adlandırır ve gizli iş anlamına uzanır.","gloss":"yürek ve içte saklama","neighbor_only":"Komşu dal bilgi, düşünce veya sırrın kişinin iç dünyasında saklanması eylemini bildirir.","neighbor_ref":"root_001324/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişinin iç dünyası ve duyulardan saklı içerik alanında buluşur."}],"source_phrase_ar":"الجنان القلب (maqayis)؛ الجنان روع القلب (ayn;tahdhib)؛ أراد بالجن القلب (sihah)؛ الجنان القلب لكونه مستورا عن الحاسة (mufradat)؛ الجنان الأمر الخفي (tahdhib)","source_summary":"Kaynaklar duyulardan saklı yürek anlamında birleşir; bir kaynak aynı biçimi gizli iş ve görünmeyen yön için de kaydeder.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الجنان بمعنى القلب أو روع القلب والأمر الخفي المستور","what_is_not_ar":"ليس جنان الليل ولا جنان الناس"},"support_links":["sup_0207b38de44bec322512"]},{"boundary":"Dal bitki gelişimi ve yoğunluğuyla sınırlıdır; böcek sesi veya sırf ağaçlı bahçe adı bu çekirdeğe girmez.","branch_kind":"bare","branch_ref":"root_000266/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جِنَّة","morph_features":"STEM|POS:N|LEM:jin~ap|ROOT:jnn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:2:2","qac_word_ref":"114:6:2","surface_ar":"جِنَّةِ"}],"gloss":"bitkinin güçlenip boylanması ve sıklaşması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bitki güçlenir, boy atar, sıklaşıp dolaşır veya çiçek açarak gelişimini belirginleştirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Uzun ağaç ile yoğun ve bol otlu arazi, bitkisel gelişimin sonuç veya alan odaklı uzantılarıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bol otlu arazi kullanımında bitki örtüsünün henüz otlanmamış olması ayrıca belirtilir."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bitkinin gelişerek uzadığı, yoğunlaştığı, birbirine dolaştığı veya çiçek açtığı genel bağlamlara uygundur.","boundary_detail":"Dal bitki gelişimi ve yoğunluğuyla sınırlıdır; böcek sesi veya sırf ağaçlı bahçe adı bu çekirdeğe girmez.","branch_image_ar":"التفاف النبات واندفاعه","concept_gloss":"bitkinin güçlenip boylanması ve sıklaşması","contextual_glosses":[{"applicability":"Bahçe, vadi veya ufuk gibi bir alanın yoğun bitki örtüsüyle kaplandığı bağlamlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Alan katılımcısını ve bitki örtüsünün yoğunlaşıp alanı kaplaması sonucunu korur."},"facet_ids":["F001","F002"],"text":"bitkiyle dolup sıklaşmak","usage_role":"contextual"}],"definition":"Bitkinin güçlenmesi, boy atması, sıklaşıp birbirine dolaşması veya çiçek açmasıdır; uzun ağaç ve bol, otlanmamış bitki örtüsü bu gelişimin sonuç odaklı görünümleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bitki güçlenir, boy atar, sıklaşıp dolaşır veya çiçek açarak gelişimini belirginleştirir."},{"facet_id":"F002","role":"extension","statement":"Uzun ağaç ile yoğun ve bol otlu arazi, bitkisel gelişimin sonuç veya alan odaklı uzantılarıdır."},{"facet_id":"F003","role":"specialization","statement":"Bol otlu arazi kullanımında bitki örtüsünün henüz otlanmamış olması ayrıca belirtilir."}],"identity_rationale":"Kaynak ifadesi bitkinin güçlenme, boy atma, sıklaşıp birbirine dolaşma veya çiçek açma gelişimini; uzun ağaç ve bol otlu arazi sonuçlarını da buna bağlı biçimde verir.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"bitkinin güçlenmesi, boylanması, sıklaşması veya çiçek açması"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"uzun ağaç; bol otlu ve henüz otlanmamış arazi"}],"lexicalization_note":"Tanım yalın bitki gelişimi dalını korur ve böcek sesine bağlı kullanımı ya da başka dalların yer adlarını içeri almaz.","neighbor_coverage_note":"Bütün yoğun bitki, bahçe, ot ve aynı kökten adaylar değerlendirildi; gelişim süreci ile dolaşık düzen arasındaki sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak gelişimin birden çok aşamasını ve sonucunu kapsar; komşunun çekirdeği ise bitkilerin birbirine dolaşmış düzenidir.","focus_only":"Odak dal bitkinin güçlenmesini, boy atmasını ve çiçek açmasını sıklaşmanın yanında kapsar.","gloss":"bitkinin sıklaşıp dolaşması","neighbor_only":"Komşu dal bitki veya ağaçların özellikle birbirine dolaşmış, kat kat kıvrılmış düzenini öne çıkarır.","neighbor_ref":"root_001365/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da yoğunlaşan bitkilerin birbirine girip sık bir örtü oluşturması alanında örtüşür."}],"source_phrase_ar":"جن النبت جنونا إذا اشتد وخرج زهره (maqayis)؛ جن النبت جنونا أي طال والتف وخرج زهره ونخلة مجنونة أي طويلة (sihah)؛ للنبت الملتف الكثيف مجنون وجنت الرياض جنونا إذا اعتم نبتها (tahdhib)؛ جن التلاع والآفاق أي كثر عشبها (mufradat)","source_summary":"Kaynaklar bitkinin güçlenmesi, uzaması, sıklaşması ve çiçeklenmesi çevresinde birleşir; uzun ağaç ile bol ve otlanmamış araziyi sonuç olarak ekler.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه النبات إذا اشتد أو طال أو التف أو خرج زهره والنخل الطويل والأرض الكثيرة العشب","what_is_not_ar":"ليس الذباب إذا حمل على الصوت"},"support_links":[]},{"boundary":"Dal yılan referansıyla sınırlıdır; görünmeyen ruhani varlığın atası veya bireyi anlamını içermez.","branch_kind":"bare","branch_ref":"root_000266/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جِنَّة","morph_features":"STEM|POS:N|LEM:jin~ap|ROOT:jnn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:2:2","qac_word_ref":"114:6:2","surface_ar":"جِنَّةِ"}],"gloss":"yılan, özellikle beyaz bir tür","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Referans bir yılan, kimi kaynaklarda özellikle beyaz yılan veya belirli bir yılan türüdür."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Görünmeyen varlık bireyine benzetme, yılan referansının açıklaması olup onu o varlıkla özdeşleştirmez."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Biçimin genel bir yılanı, beyaz yılanı veya belirli bir yılan türünü adlandırdığı bağlamlara uygundur.","boundary_detail":"Dal yılan referansıyla sınırlıdır; görünmeyen ruhani varlığın atası veya bireyi anlamını içermez.","branch_image_ar":"الجان حية","concept_gloss":"yılan, özellikle beyaz bir tür","contextual_glosses":[{"applicability":"Kaynağın veya bağlamın yılanın beyaz olduğunu açıkça belirttiği kullanımlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yılan türünü ve bağlamda açıkça verilen beyazlık niteliğini korur."},"facet_ids":["F001"],"text":"beyaz yılan","usage_role":"contextual"}],"definition":"Yılanı, özellikle beyaz bir yılanı veya belirli bir yılan türünü adlandıran kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Referans bir yılan, kimi kaynaklarda özellikle beyaz yılan veya belirli bir yılan türüdür."},{"facet_id":"F002","role":"source_variant","statement":"Görünmeyen varlık bireyine benzetme, yılan referansının açıklaması olup onu o varlıkla özdeşleştirmez."}],"identity_rationale":"Kaynak ifadesi biçimi yılan, beyaz yılan veya belirli bir yılan türü olarak verir; görünmeyen varlık anlamıyla bağ yalnızca benzetme açıklamasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"yılan, beyaz yılan veya belirli bir yılan türü"}],"lexicalization_note":"Tanım yalın yılan adını korur ve aynı biçimin görünmeyen varlık anlamını bu dala taşımaz.","neighbor_coverage_note":"Bütün yılan, küçük canlı ve aynı kökten adaylar değerlendirildi; beyaz yılan ortaklığı taşıyan ayrı ad en keskin karşılaştırmayı sağlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Referans özellikleri kesişse de bunlar ayrı yılan adlarıdır; odak daha geniş ve türü değişken, komşu ise ayrı benzetmeyle kurulmuş addır.","focus_only":"Odak dal genel yılanı veya beyaz ya da belirli bir yılan türünü aynı ad altında kapsar.","gloss":"beyaz yılan adları","neighbor_only":"Komşu dal beyaz yılanı bir takı parçasının biçimine benzetilen ayrı bir adla sınırlar.","neighbor_ref":"root_001248/B009","relation_type":"near_neighbor","shared_zone":"Her iki dalın referansı bazı kullanımlarda beyaz bir yılan olabilir."}],"source_phrase_ar":"الحية الذي يسمى الجان فهو تشبيه له بالواحد من الجان (maqayis)؛ الجان حية بيضاء (ayn)؛ الجان أيضا حية بيضاء (sihah)؛ الجان الحية وجمعها جوان (tahdhib)؛ الجان ضرب من الحيات (mufradat)","source_summary":"Kaynaklar yılan referansında birleşir; bazıları beyazlığı belirtir, biri bunu görünmeyen varlık bireyine benzetmeyle açıklar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الجان بمعنى الحية أو الحية البيضاء أو ضرب من الحيات","what_is_not_ar":"ليس الجان أبو الجن إلا من جهة اللفظ"},"support_links":[]},{"boundary":"Her küçük grup bu dala girmez; insanların ana gövdesi, büyük kitlesi veya çoğunluğu söz konusudur.","branch_kind":"bare","branch_ref":"root_000266/B013","candidate_links":[{"candidate_id":"cand_33f022d1bd814d192802","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جِنَّة","morph_features":"STEM|POS:N|LEM:jin~ap|ROOT:jnn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:2:2","qac_word_ref":"114:6:2","surface_ar":"جِنَّةِ"}],"gloss":"halkın büyük kitlesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanların çoğunluğu veya ana kitlesi tek bir toplumsal gövde olarak ele alınır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir topluluğun çoğunluğunu, ana gövdesini veya sıradan insanlardan oluşan geniş kesimini anlatan bağlamlara uygundur.","boundary_detail":"Her küçük grup bu dala girmez; insanların ana gövdesi, büyük kitlesi veya çoğunluğu söz konusudur.","branch_image_ar":"سواد الناس وجماعتهم","concept_gloss":"halkın büyük kitlesi","contextual_glosses":[{"applicability":"Sayısal veya toplumsal bakımdan grubun ana bölümünün kastedildiği cümlelerde doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan grubunu ve grubun büyük ana bölümünü gösterme işlevini korur."},"facet_ids":["F001"],"text":"insanların çoğunluğu","usage_role":"contextual"}],"definition":"Bir insan topluluğunun büyük çoğunluğu, sıradan kitlesi veya topluca oluşturduğu ana gövdesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanların çoğunluğu veya ana kitlesi tek bir toplumsal gövde olarak ele alınır."}],"identity_rationale":"Kaynak ifadesi insanların büyük çoğunluğunu, sıradan kitlesini veya topluca oluşturduğu ana gövdeyi bildirir; gece karanlığı ve yürek anlamları açıkça dışarıdadır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"insanların çoğunluğu veya halkın büyük kitlesi"}],"lexicalization_note":"Tanım yalın insan kitlesi anlamını korur ve başka topluluk türlerini ya da karanlık anlamını içeri almaz.","neighbor_coverage_note":"Bütün topluluk, çoğunluk, kalabalık ve aynı kökten adaylar değerlendirildi; ana kitle ile fiziksel izdiham ayrımı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta toplumsal çoğunluk veya ana gövde yeterlidir; komşuda insanların birbirini örten yoğun bir kalabalık oluşturması kurucu koşuldur.","focus_only":"Odak dal bir topluluğun ana gövdesini veya çoğunluğunu, fiziksel sıkışıklık şartı olmadan bildirir.","gloss":"insan kitlesi ve sık kalabalık","neighbor_only":"Komşu dal insanların kalabalıkta birbirini örtecek ölçüde sıkışmasını ve izdihamını gerektirir.","neighbor_ref":"root_001105/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da çok sayıda insanın oluşturduğu büyük topluluk alanında örtüşür."}],"source_phrase_ar":"جنان الناس معظمهم ويسمى السواد (maqayis)؛ جنان الناس دهماؤهم (sihah)؛ جنانهم جماعتهم وسوادهم (tahdhib)","source_summary":"Kaynaklar insanların çoğunluğu, kalabalık ana kitlesi ve sıradan toplumsal gövdesi anlamlarında birleşir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه جنان الناس بمعنى معظمهم أو دهمائهم أو سوادهم وجماعتهم","what_is_not_ar":"ليس جنان الليل ولا الجنان القلب"},"support_links":["sup_bd0d87185e8e80075fc9"]},{"boundary":"Dal bir şeyin ilk ve yeni evresiyle sınırlıdır; genel olarak başlama eylemi veya ardışık evrelerin tamamı değildir.","branch_kind":"bare","branch_ref":"root_000266/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جِنَّة","morph_features":"STEM|POS:N|LEM:jin~ap|ROOT:jnn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:2:2","qac_word_ref":"114:6:2","surface_ar":"جِنَّةِ"}],"gloss":"bir şeyin ilk ve yeni dönemi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin sürecindeki ilk, yeni ve henüz gelişmekte olan başlangıç dönemi seçilir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gençliğin veya çocukluğun ilk dönemi bu genel başlangıç evresinin belirgin örnekleridir."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gençlik, çocukluk, dönem veya başka bir sürecin henüz başlangıçta olduğu ilk evresini anlatmaya uygundur.","boundary_detail":"Dal bir şeyin ilk ve yeni evresiyle sınırlıdır; genel olarak başlama eylemi veya ardışık evrelerin tamamı değildir.","branch_image_ar":"جن الشيء في بدايته","concept_gloss":"bir şeyin ilk ve yeni dönemi","contextual_glosses":[{"applicability":"Bir kişinin gençlik döneminin başlangıç kısmı özellikle kastedildiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gençlik dönemini ve bu dönemin ilk, yeni evresini tam olarak korur."},"facet_ids":["F001","F002"],"text":"gençliğinin ilk yılları","usage_role":"contextual"}],"definition":"Gençlik, çocukluk, bir dönem veya herhangi bir şeyin henüz yeni olduğu ilk başlangıç evresidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin sürecindeki ilk, yeni ve henüz gelişmekte olan başlangıç dönemi seçilir."},{"facet_id":"F002","role":"example","statement":"Gençliğin veya çocukluğun ilk dönemi bu genel başlangıç evresinin belirgin örnekleridir."}],"identity_rationale":"Kaynak ifadesi gençlik, çocukluk, dönem veya herhangi bir şeyin ilk başlangıcını ve henüz yeni oluşunu bildirir; bu nedenle dal başlangıç evresi olarak doğru kurulmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"gençliğin, çocukluğun veya bir dönemin ilk başlangıcı"}],"lexicalization_note":"Tanım yalın ilk dönem anlamını kapsar ve belirli bir başlama söz öbeğine ya da bütün yaşam evrelerine genişletilmez.","neighbor_coverage_note":"Bütün gençlik, başlama, evre ve karşıt zaman adayları değerlendirildi; başlangıç evresi ile başlama eylemi ayrımı en yararlı olandır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak bir başlangıç evresini adlandırır; komşu ise başlama eylemini ve yeniden başlatmayı da kapsar, bu yüzden kapsamları tam çakışmaz.","focus_only":"Odak dal başlayan şeyin ilk ve yeni dönemini, yani süreç içindeki bir evreyi adlandırır.","gloss":"başlangıç ve ilk dönem","neighbor_only":"Komşu dal bir işe başlama, yeniden başlama veya yakın geçmişteki ilk zamanı da kapsayan eylemsel bir alandır.","neighbor_ref":"root_000060/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir sürecin ilk noktasına veya başlangıç bölümüne yönelir."}],"source_phrase_ar":"كان ذلك في جن شبابه أي في أول شبابه (sihah)؛ كان ذلك في جن صباه أي في حداثته وكذلك جن كل شيء أول ابتدائه (tahdhib)","source_summary":"Kaynaklar gençlik ve çocukluk örneklerinden hareketle anlamı herhangi bir şeyin ilk başlangıç ve yenilik dönemine geneller.","sources":["SI","TA"],"what_is_ar":"يدخل فيه جن الشباب أو الصبا أو العهد أو كل شيء بمعنى أول ابتدائه وحدثانه","what_is_not_ar":"ليس جنون العقل"},"support_links":[]},{"boundary":"Ses anlamı böcek yorumu şartına bağlıdır; aynı biçim bitkiyi gösterdiğinde sıklaşma anlamı bu dalın dışında kalır.","branch_kind":"bare","branch_ref":"root_000266/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جِنَّة","morph_features":"STEM|POS:N|LEM:jin~ap|ROOT:jnn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:2:2","qac_word_ref":"114:6:2","surface_ar":"جِنَّةِ"}],"gloss":"uçuş sırasında çoğalan sinek vızıltısı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sinek uçarken çıkardığı sesi veya vızıltıyı çoğaltır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İki yorumlu ad böceği gösterirse uçuş sesi, bitkiyi gösterirse sıklaşıp dolaşma anlamına gelir."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Referansın sinek veya benzeri küçük uçucu canlı olduğu ve sesin uçuşta arttığı bağlamlara uygundur.","boundary_detail":"Ses anlamı böcek yorumu şartına bağlıdır; aynı biçim bitkiyi gösterdiğinde sıklaşma anlamı bu dalın dışında kalır.","branch_image_ar":"جن الذباب وصوت الخازباز","concept_gloss":"uçuş sırasında çoğalan sinek vızıltısı","contextual_glosses":[{"applicability":"Sinek veya benzeri küçük uçucu canlının çıkardığı sesin çoğalması eylem olarak anlatıldığında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Böcek sesini ve bu sesin miktar veya yoğunluk bakımından artmasını korur."},"facet_ids":["F001"],"text":"vızıldaması artmak","usage_role":"contextual"}],"definition":"Sineğin veya sinek olarak yorumlanan küçük uçucu canlının uçuş sırasında sesini ve vızıltısını çoğaltmasıdır. Aynı ad bitkiyi gösterirse anlam ses değil, bitkinin sıklaşmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sinek uçarken çıkardığı sesi veya vızıltıyı çoğaltır."},{"facet_id":"F002","role":"source_variant","statement":"İki yorumlu ad böceği gösterirse uçuş sesi, bitkiyi gösterirse sıklaşıp dolaşma anlamına gelir."}],"identity_rationale":"Kaynak ifadesi sineğin sesinin çoğalmasını açıkça destekler, ancak ikinci biçimin hem uçarken çok ses çıkaran bir böceğe hem de sıklaşan bir bitkiye yorumlanabileceğini söyler; dal yalnızca böcek yorumu altında ses dalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"sineğin vızıltısının veya sesinin çoğalması"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"böcekse uçuş vızıltısının artması; bitkiyse sıklaşıp dolaşması"}],"lexicalization_note":"Yalın ses dalı korunur, fakat iki yorumlu biçim yalnızca böcek referansı kesin olduğunda bu tanıma bağlanır.","neighbor_coverage_note":"Bütün böcek, ses, hareket ve aynı kökten adaylar değerlendirildi; ses kaynağını sınayan genel hareket uğultusu dalı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta ses kaynağı küçük uçucu böcektir ve ses çoğalır; komşu çok çeşitli hareket kaynaklarından çıkan hışırtı ve uğultuyu kapsar.","focus_only":"Odak dal belirli bir uçucu böceğin uçarken artan vızıltısına bağlıdır.","gloss":"vızıltı ve hareket uğultusu","neighbor_only":"Komşu dal rüzgar, hareket, alay veya kaynayan kap gibi çeşitli kaynakların hışırtı ve uğultusunu kapsar.","neighbor_ref":"root_001588/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da hareket sırasında doğan sürekli veya yinelenen sesi anlatabilir."}],"source_phrase_ar":"جن الذباب أي كثر صوته (sihah)؛ جن الخازباز به جنونا يحتمل هذين الوجهين (sihah)؛ قيل هو ذباب وجنونه كثرة ترنمه في طيرانه وقيل هو نبت وجنون النبت التفافه (tahdhib)","source_summary":"Kaynaklar sineğin sesinin çoğalmasını verir; iki yorumlu adın böcek okumasında uçuş vızıltısı, bitki okumasında ise sıklaşma bildirdiğini ayrıca belirtir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه كثرة صوت الذباب أو ترنم الخازباز حيث نص المصدر على ذلك","what_is_not_ar":"ليس نبات الخازباز إذا حمل على النبات"},"support_links":[]},{"boundary":"Dal göğüs kafesinin kemik yapısıyla sınırlıdır; yürek, göğüs eti veya kalça kemikleri anlamına gelmez.","branch_kind":"bare","branch_ref":"root_000266/B016","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جِنَّة","morph_features":"STEM|POS:N|LEM:jin~ap|ROOT:jnn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:2:2","qac_word_ref":"114:6:2","surface_ar":"جِنَّةِ"}],"gloss":"göğüs kemikleri ve kaburga uçları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Referans göğüs kafesinin kemikleri veya kaburgaların göğse yakın uçlarıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir açıklama aynı anatomik adı göğsün içteki orta kemiğine kadar genişletir."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Göğüs kafesindeki kemiklerin topluca veya kaburgaların göğse yakın uçlarının özel olarak kastedildiği bağlamlara uygundur.","boundary_detail":"Dal göğüs kafesinin kemik yapısıyla sınırlıdır; yürek, göğüs eti veya kalça kemikleri anlamına gelmez.","branch_image_ar":"الجناجن عظام الصدر","concept_gloss":"göğüs kemikleri ve kaburga uçları","contextual_glosses":[{"applicability":"Anatomik anlatım genel göğüs kemiklerinden daha dar olarak kaburga uçlarını seçtiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kaburga katılımcısını, uç bölümünü ve göğse yakın konumu eksiksiz korur."},"facet_ids":["F001"],"text":"kaburgaların göğse yakın uçları","usage_role":"explanatory"}],"definition":"Göğüs kafesindeki kemikler, özellikle kaburgaların göğse yakın uçları ve kimi açıklamada göğsün içteki orta kemiğidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Referans göğüs kafesinin kemikleri veya kaburgaların göğse yakın uçlarıdır."},{"facet_id":"F002","role":"source_variant","statement":"Bir açıklama aynı anatomik adı göğsün içteki orta kemiğine kadar genişletir."}],"identity_rationale":"Kaynak ifadesi göğüs kemiklerini ve kaburgaların göğse yakın uçlarını bildirir; bir kaynak içteki orta kemiği de aynı anatomik bölgeye dahil eder.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"göğüs kemikleri veya kaburgaların göğse yakın uçları"}],"lexicalization_note":"Tanım yalın anatomik kemik adını korur ve komşu organ, et veya başka eklem adlarını içeri almaz.","neighbor_coverage_note":"Bütün göğüs, kaburga, kalça, eklem ve aynı kökten adaylar değerlendirildi; kemik grubu ile orta göğüs kemiği ayrımı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak çoğul bir kemik grubu ve kaburga uçlarıdır; komşu ise göğsün ortasındaki belirli tek kemiği adlandırır.","focus_only":"Odak dal göğüs kemiklerini topluca ve özellikle kaburgaların göğse yakın uçlarını kapsar.","gloss":"göğüs kemikleri ve orta göğüs kemiği","neighbor_only":"Komşu dal göğsün ortasındaki tek kemiği, başını ve üzerindeki kıl çıkış yerini kapsar.","neighbor_ref":"root_001232/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal göğüs kafesinin ön ve orta bölümündeki kemik yapılarıyla ilgilidir."}],"source_phrase_ar":"الجناجن عظام الصدر (maqayis)؛ الجنجن والجناجن أطراف الأضلاع مما يلي الصدر وعظم القلب (ayn)؛ الجناجن عظام الصدر الواحد جنجن (sihah)","source_summary":"Kaynaklar göğüs kemikleri tanımında birleşir; daha ayrıntılı açıklama kaburga uçlarını ve göğsün içteki orta kemiğini belirtir.","sources":["MQ","AY","SI"],"what_is_ar":"يدخل فيه الجناجن والجنجن عظام الصدر أو أطراف الأضلاع مما يلي الصدر","what_is_not_ar":"ليس الجنان القلب"},"support_links":[]},{"boundary":"Genel anlam saklanma yeridir; özel yer kullanımı belirli bir tarihsel pazar adına bağlıdır ve akıl yitimi anlamıyla karıştırılmaz.","branch_kind":"bare","branch_ref":"root_000266/B017","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جِنَّة","morph_features":"STEM|POS:N|LEM:jin~ap|ROOT:jnn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:2:2","qac_word_ref":"114:6:2","surface_ar":"جِنَّةِ"}],"gloss":"içine girilip saklanılan yer","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yer, kişinin içine girerek görünmekten saklanmasına imkan verir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı biçim kaynakta anılan kent yakınındaki belirli bir eski pazar yerinin adı olarak da kullanılır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin görünmemek veya korunmak için içine girdiği genel saklanma yerini anlatan bağlamlara uygundur.","boundary_detail":"Genel anlam saklanma yeridir; özel yer kullanımı belirli bir tarihsel pazar adına bağlıdır ve akıl yitimi anlamıyla karıştırılmaz.","branch_image_ar":"المَجَنَّة موضع الاستتار","concept_gloss":"içine girilip saklanılan yer","contextual_glosses":[{"applicability":"Özel tarihsel yer adı değil, genel olarak saklanmaya yarayan mekan kastedildiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mekan referansını ve saklanma işlevini bağlam içinde eksiksiz korur."},"facet_ids":["F001"],"text":"saklanma yeri","usage_role":"contextual"}],"definition":"Bir kişinin içine girip saklanabildiği yerdir; ayrıca kaynakta anılan kentten birkaç mil uzakta bulunan belirli bir eski pazar yerinin adı olarak kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yer, kişinin içine girerek görünmekten saklanmasına imkan verir."},{"facet_id":"F002","role":"specialization","statement":"Aynı biçim kaynakta anılan kent yakınındaki belirli bir eski pazar yerinin adı olarak da kullanılır."}],"identity_rationale":"Tek kaynaklı ifade hem kişinin saklanabildiği bir yeri hem de kaynakta anılan kentten birkaç mil uzaktaki belirli eski pazar yerinin adını verir; dal iki kullanımı da kapsar.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"saklanılan yer; ayrıca kaynakta belirli bir eski pazar yerinin adı"}],"lexicalization_note":"Tanım yalın saklanma yeri anlamını ve kanıttaki özel yer kullanımını korur; barınak eylemlerinin tamamına genişletilmez.","neighbor_coverage_note":"Bütün barınak, gizlenme, korku, yer ve aynı kökten adaylar değerlendirildi; mekan ile sığınağa girme eylemi ayrımı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak öncelikle mekanı adlandırır; komşu ise bu mekana girme ve orada gizlenme eylemlerini kurucu anlam olarak taşır.","focus_only":"Odak dal saklanmaya imkan veren yeri adlandırır ve ayrıca belirli bir tarihsel yer kullanımına sahiptir.","gloss":"saklanma yeri ve sığınağa girme","neighbor_only":"Komşu dal bir sığınağa girme, orada kalma ve yüzünü gizleme eylemlerini de kapsar.","neighbor_ref":"root_001324/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişinin bir örtü veya sığınak içinde görünmekten saklanması alanındadır."}],"source_phrase_ar":"المجنة اسم موضع على أميال من مكة؛ كانت مجنة وذو المجاز وعكاظ أسواقا في الجاهلية؛ المجنة أيضا الموضع الذي يستتر فيه (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Saklanma yeri anlamı ile belirli eski pazar yerinin adı aynı tek kaynakta birlikte tanıklanır."}],"source_summary":"Tek kaynak saklanılan yer anlamını, kent yakınındaki ve eski pazarlar arasında sayılan belirli bir yer adıyla birlikte verir.","sources":["SI"],"what_is_ar":"يدخل فيه المجنة اسم موضع أو الموضع الذي يستتر فيه","what_is_not_ar":"ليس المجنة بمعنى الجنون"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["114:6:1"],"branch_refs":[],"candidate_id":"cand_c8518ebeb378787438a8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:6:1:audible-link-into-jinnati","source_type":"word_analysis","support_ids":["sup_0766eca66af2abfada20","sup_ba49c8b53838633c763c"],"title":"recited link carries the dependency","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:1","qac_refs":["114:6:1:1"],"status":"accepted"}},{"anchor_refs":["114:6:1"],"branch_refs":[],"candidate_id":"cand_793379542600e4dd3afa","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:6:1:elliptic-cross-ayah-dependency","source_type":"word_analysis","support_ids":["sup_0766eca66af2abfada20","sup_14483ffb6de7d1705431"],"title":"elliptic closing phrase depends on prior frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:1","qac_refs":["114:6:1:1"],"status":"accepted"}},{"anchor_refs":["114:6:1"],"branch_refs":[],"candidate_id":"cand_e052274e17e574a56d19","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:6:1:origin-after-interior-vector","source_type":"word_analysis","support_ids":["sup_0766eca66af2abfada20","sup_c4502c7e029f55c4dbeb"],"title":"origin answers the prior interior","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:1","qac_refs":["114:6:1:1"],"status":"accepted"}},{"anchor_refs":["114:6:1"],"branch_refs":[],"candidate_id":"cand_4747e648ed6dad273cb2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:6:1:single-min-governs-pair","source_type":"word_analysis","support_ids":["sup_0766eca66af2abfada20","sup_941599af6ab91c987c93"],"title":"single particle governs both source nouns","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:1","qac_refs":["114:6:1:1"],"status":"accepted"}},{"anchor_refs":["114:6:1"],"branch_refs":[],"candidate_id":"cand_5e4c85f9375f4a70b215","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:6:1:three-live-min-values","source_type":"word_analysis","support_ids":["sup_0766eca66af2abfada20","sup_224bb0630e8081b392e7"],"title":"specification partition and origin remain live","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:1","qac_refs":["114:6:1:1"],"status":"accepted"}},{"anchor_refs":["114:6:2"],"branch_refs":[],"candidate_id":"cand_59a77bfc0b863e17fa04","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"114:6:2:exposed-interior-meets-concealed-source","source_type":"word_analysis","support_ids":["sup_60ca58d8a83993984d42","sup_64078f65edb9835d715e"],"title":"concealed source answers exposed interior","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:2","qac_refs":["114:6:2:1","114:6:2:2"],"status":"accepted"}},{"anchor_refs":["114:6:2"],"branch_refs":[],"candidate_id":"cand_f0e6ba7796b447d7f316","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"114:6:2:geminated-nasal-concealment-sound","source_type":"word_analysis","support_ids":["sup_60ca58d8a83993984d42","sup_dcd78fed513060181899"],"title":"geminated nasal makes hiddenness audible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:2","qac_refs":["114:6:2:1","114:6:2:2"],"status":"accepted"}},{"anchor_refs":["114:6:2"],"branch_refs":[],"candidate_id":"cand_98f934e4ff2fbf562cb8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"114:6:2:governed-collective-source-class","source_type":"word_analysis","support_ids":["sup_59701b2ebc4950645b31","sup_60ca58d8a83993984d42"],"title":"governed collective source class","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:2","qac_refs":["114:6:2:1","114:6:2:2"],"status":"accepted"}},{"anchor_refs":["114:6:2"],"branch_refs":[],"candidate_id":"cand_ffaaafdc68ddeb0d6208","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"114:6:2:hidden-beings-concealment-mechanism","source_type":"word_analysis","support_ids":["sup_60ca58d8a83993984d42","sup_d7ad92f11d1ed39f0083"],"title":"hidden beings carry concealment pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:2","qac_refs":["114:6:2:1","114:6:2:2"],"status":"accepted"}},{"anchor_refs":["114:6:2"],"branch_refs":[],"candidate_id":"cand_d26f72ca347d7864418c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"114:6:2:jinn-human-source-taxonomy","source_type":"word_analysis","support_ids":["sup_36976b4fc4ebb66cc04c","sup_60ca58d8a83993984d42"],"title":"hidden-visible source taxonomy","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:2","qac_refs":["114:6:2:1","114:6:2:2"],"status":"accepted"}},{"anchor_refs":["114:6:2"],"branch_refs":[],"candidate_id":"cand_16f4d8dc4262e5fecc5e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"114:6:2:jinna-janna-form-echo","source_type":"word_analysis","support_ids":["sup_60ca58d8a83993984d42","sup_c4ee4fae752dea6f5c1c"],"title":"hidden-being form echoes enclosed garden","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:2","qac_refs":["114:6:2:1","114:6:2:2"],"status":"accepted"}},{"anchor_refs":["114:6:2"],"branch_refs":[],"candidate_id":"cand_f19ff34ad220189e1f0d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"114:6:2:liaison-to-governed-noun","source_type":"word_analysis","support_ids":["sup_60ca58d8a83993984d42","sup_7e87d4fc602b99ba41ed"],"title":"liaison joins governor and noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:2","qac_refs":["114:6:2:1","114:6:2:2"],"status":"accepted"}},{"anchor_refs":["114:6:3"],"branch_refs":[],"candidate_id":"cand_0d2aec3c7105b00dc001","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:6:3:balanced-audible-pair","source_type":"word_analysis","support_ids":["sup_9a5cf366698984ca493e","sup_bef581da04a7cefb3747"],"title":"balanced audible source pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:3","qac_refs":["114:6:3:1"],"status":"accepted"}},{"anchor_refs":["114:6:3"],"branch_refs":[],"candidate_id":"cand_86bb6ee142e948d331ae","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:6:3:compressed-clitic-and-sound-bond","source_type":"word_analysis","support_ids":["sup_705768d11d9123e82b44","sup_bef581da04a7cefb3747"],"title":"compressed clitic sound bond","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:3","qac_refs":["114:6:3:1"],"status":"accepted"}},{"anchor_refs":["114:6:3"],"branch_refs":[],"candidate_id":"cand_4e7513451eb8b8d9650d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:6:3:coordination-under-one-min","source_type":"word_analysis","support_ids":["sup_4ed92ba2c1c0e7438ef6","sup_bef581da04a7cefb3747"],"title":"coordination under one preposition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:3","qac_refs":["114:6:3:1"],"status":"accepted"}},{"anchor_refs":["114:6:3"],"branch_refs":[],"candidate_id":"cand_d528542befba95ea526e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:6:3:explicit-two-member-taxonomy","source_type":"word_analysis","support_ids":["sup_125941818a803dcbb9ba","sup_bef581da04a7cefb3747"],"title":"explicit two-member taxonomy","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:3","qac_refs":["114:6:3:1"],"status":"accepted"}},{"anchor_refs":["114:6:3"],"branch_refs":[],"candidate_id":"cand_9aba9699823436861efa","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:6:3:hidden-to-human-hinge","source_type":"word_analysis","support_ids":["sup_7d83bf81a29c4b07f446","sup_bef581da04a7cefb3747"],"title":"hinge from hidden to human","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:3","qac_refs":["114:6:3:1"],"status":"accepted"}},{"anchor_refs":["114:6:4"],"branch_refs":[],"candidate_id":"cand_1f1250681d3cc95c6402","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:6:4:audible-nasal-fawasil-close","source_type":"word_analysis","support_ids":["sup_b74c66ddefa52f8516c9","sup_e7acec59cd2781855742"],"title":"nasal sound closes the pattern","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:4","qac_refs":["114:6:3:2","114:6:3:3"],"status":"accepted"}},{"anchor_refs":["114:6:4"],"branch_refs":[],"candidate_id":"cand_718afd65ac5491057d0c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:6:4:balanced-final-pair-cadence","source_type":"word_analysis","support_ids":["sup_691ef556e6ce47a40bed","sup_b74c66ddefa52f8516c9"],"title":"balanced final pair cadence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:4","qac_refs":["114:6:3:2","114:6:3:3"],"status":"accepted"}},{"anchor_refs":["114:6:4"],"branch_refs":[],"candidate_id":"cand_0883a172f3302f5b69e6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:6:4:collective-form-not-individual-action","source_type":"word_analysis","support_ids":["sup_2ccd0158b44c512181f8","sup_b74c66ddefa52f8516c9"],"title":"collective class noun not individual action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:4","qac_refs":["114:6:3:2","114:6:3:3"],"status":"accepted"}},{"anchor_refs":["114:6:4"],"branch_refs":[],"candidate_id":"cand_4b5ad088aefd5847dfb9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:6:4:final-closure-on-humankind","source_type":"word_analysis","support_ids":["sup_657ed1020826dde548a7","sup_b74c66ddefa52f8516c9"],"title":"final closure lands on humankind","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:4","qac_refs":["114:6:3:2","114:6:3:3"],"status":"accepted"}},{"anchor_refs":["114:6:4"],"branch_refs":[],"candidate_id":"cand_37ec70fb4e883614c98f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:6:4:generic-class-under-min","source_type":"word_analysis","support_ids":["sup_76765550062e7b33b480","sup_b74c66ddefa52f8516c9"],"title":"generic class under shared preposition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:4","qac_refs":["114:6:3:2","114:6:3:3"],"status":"accepted"}},{"anchor_refs":["114:6:4"],"branch_refs":[],"candidate_id":"cand_c553a56168837e47e67b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:6:4:jinn-human-pair-completion","source_type":"word_analysis","support_ids":["sup_88d65410784cdbb5b365","sup_b74c66ddefa52f8516c9"],"title":"jinn-human pair completed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:4","qac_refs":["114:6:3:2","114:6:3:3"],"status":"accepted"}},{"anchor_refs":["114:6:4"],"branch_refs":[],"candidate_id":"cand_25eb7b8a0eb9478a5429","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:6:4:role-reversal-within-surah","source_type":"word_analysis","support_ids":["sup_b74c66ddefa52f8516c9","sup_d7945b39f8928c301d32"],"title":"protected humans become possible source","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:4","qac_refs":["114:6:3:2","114:6:3:3"],"status":"accepted"}},{"anchor_refs":["114:6:4"],"branch_refs":[],"candidate_id":"cand_e0d9dcc9640392a19553","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:6:4:social-perceptible-and-forgetful-pressure","source_type":"word_analysis","support_ids":["sup_2e93f66a680f7ea0eb9d","sup_b74c66ddefa52f8516c9"],"title":"social perceptible and forgetful pressures","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:4","qac_refs":["114:6:3:2","114:6:3:3"],"status":"accepted"}},{"anchor_refs":["114:6:4"],"branch_refs":[],"candidate_id":"cand_48ed1c6aa7bb84687455","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"114:6:4:surah-lexical-spine","source_type":"word_analysis","support_ids":["sup_78d1d7014ef535f1a482","sup_b74c66ddefa52f8516c9"],"title":"surah-local human noun spine","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"114:6:4","qac_refs":["114:6:3:2","114:6:3:3"],"status":"accepted"}},{"anchor_refs":["114:6:2"],"branch_refs":[],"candidate_id":"cand_ed5e580e74ffc135a19c","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"114:6:2:2","source_type":"qac_morpheme","support_ids":["sup_4edc6ae655cd6fc50853"],"title":"QAC root occurrence: ج ن ن","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["114:6:3"],"branch_refs":[],"candidate_id":"cand_4049b3a5ab9ecfcd940e","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000059"],"scope":"focus_ayah","source_local_id":"114:6:3:3","source_type":"qac_morpheme","support_ids":["sup_f214866deda94fa3a614"],"title":"QAC root occurrence: ن و س","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["114:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"114:6","branch_refs":["root_000059/B001","root_000266/B005"],"candidate_id":"cand_bc63b3f17f545819a1f6","commentary_obligation":"review","hft_ref":"hft_064f978d4ebab66ee05d","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_hidden_visible_agents","source_type":"hft","support_ids":["sup_8b3ac0a346f5af86ab66"],"title":"baseline_hidden_visible_agents","trust":"legacy_unbound"},{"anchor_refs":["114:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"114:6","branch_refs":["root_000059/B002","root_000266/B001"],"candidate_id":"cand_e9db42b0009db1e8ac36","commentary_obligation":"review","hft_ref":"hft_67b32e11d5f89ecbdd68","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_perceptibility_axis","source_type":"hft","support_ids":["sup_cfc6709aca10eec8bc5f"],"title":"baseline_perceptibility_axis","trust":"legacy_unbound"},{"anchor_refs":["114:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"114:6","branch_refs":["root_000059/B003","root_000059/B006","root_000266/B010"],"candidate_id":"cand_2abbfecf8a1aa3234623","commentary_obligation":"review","hft_ref":"hft_0c01bbebc3ec089d8f81","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_inner_familiar_sources","source_type":"hft","support_ids":["sup_0207b38de44bec322512"],"title":"baseline_inner_familiar_sources","trust":"legacy_unbound"},{"anchor_refs":["114:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"114:6","branch_refs":["root_000059/B001","root_000266/B013"],"candidate_id":"cand_33f022d1bd814d192802","commentary_obligation":"review","hft_ref":"hft_753851e92ccd1df0eb0f","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_mass_person_scale","source_type":"hft","support_ids":["sup_bd0d87185e8e80075fc9"],"title":"baseline_mass_person_scale","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ","qac_morphemes":[{"lemma_ar":"مِن","morph_features":"STEM|POS:P|LEM:min","morpheme_role":"STEM","pos":"P","qac_ref":"114:6:1:1","qac_word_ref":"114:6:1","root_ar":"","surface_ar":"مِنَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"114:6:2:1","qac_word_ref":"114:6:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"جِنَّة","morph_features":"STEM|POS:N|LEM:jin~ap|ROOT:jnn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:2:2","qac_word_ref":"114:6:2","root_ar":"ج ن ن","surface_ar":"جِنَّةِ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"114:6:3:1","qac_word_ref":"114:6:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"114:6:3:2","qac_word_ref":"114:6:3","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:3:3","qac_word_ref":"114:6:3","root_ar":"ن و س","surface_ar":"نَّاسِ"}],"word_analysis_qac_refs":[["114:6:1:1"],["114:6:2:1","114:6:2:2"],["114:6:3:1"],["114:6:3:2","114:6:3:3"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["114:6:1","114:6:2","114:6:3","114:6:4"]},"focus_surface_evidence":{"arabic_uthmani":"مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ","qac_morphemes":[{"lemma_ar":"مِن","morph_features":"STEM|POS:P|LEM:min","morpheme_role":"STEM","pos":"P","qac_ref":"114:6:1:1","qac_word_ref":"114:6:1","root_ar":"","surface_ar":"مِنَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"114:6:2:1","qac_word_ref":"114:6:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"جِنَّة","morph_features":"STEM|POS:N|LEM:jin~ap|ROOT:jnn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:2:2","qac_word_ref":"114:6:2","root_ar":"ج ن ن","surface_ar":"جِنَّةِ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"114:6:3:1","qac_word_ref":"114:6:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"114:6:3:2","qac_word_ref":"114:6:3","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:6:3:3","qac_word_ref":"114:6:3","root_ar":"ن و س","surface_ar":"نَّاسِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["114:6:1:1"],["114:6:2:1","114:6:2:2"],["114:6:3:1"],["114:6:3:2","114:6:3:3"]],"word_analysis_refs":["114:6:1","114:6:2","114:6:3","114:6:4"],"word_rows":[{"analysis_record_ref":"114:6:1","analytic_gloss_range_en":"from, from among, or specifying; here a dependent source/specification particle that points back to the prior whisperer frame","analytic_root_gloss_range_en":null,"qac_refs":["114:6:1:1"],"root":{},"surface":{"arabic":"مِنَ","transliteration":"mina"}},{"analysis_record_ref":"114:6:2","analytic_gloss_range_en":"the jinn as a definite collective source class, locally selected as the hidden-beings member of the final pair","analytic_root_gloss_range_en":"covering and concealment, including hidden beings, enclosed garden, shield, fetus, veiled reason, and related coveredness images; the local form selects hidden beings while allowing concealment pressure to remain active","qac_refs":["114:6:2:1","114:6:2:2"],"root":{"arabic":"ج ن ن","transliteration":"j-n-n"},"surface":{"arabic":"ٱلْجِنَّةِ","transliteration":"al-jinnati"}},{"analysis_record_ref":"114:6:3","analytic_gloss_range_en":"coordinating conjunction joining the two genitive source nouns under the same preposition","analytic_root_gloss_range_en":null,"qac_refs":["114:6:3:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"114:6:4","analytic_gloss_range_en":"humankind or people as a definite generic class, here the final coordinated human source under the opening preposition","analytic_root_gloss_range_en":"humanity, sociability, perception, familiarity, and a contested forgetfulness derivation; locally the noun names the human class while those pressures shape its role","qac_refs":["114:6:3:2","114:6:3:3"],"root":{"arabic":"أ ن س","transliteration":"ʾ-n-s"},"surface":{"arabic":"ٱلنَّاسِ","transliteration":"al-nāsi"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["114:6"],"branch_refs":["root_000059/B001","root_000266/B005"],"candidate_id":"cand_bc63b3f17f545819a1f6","evidence_scope":"focus_ayah","hft_ref":"hft_064f978d4ebab66ee05d","item_id":"baseline_hidden_visible_agents","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_hidden_visible_agents","support_id":"sup_8b3ac0a346f5af86ab66"},{"anchor_refs":["114:6"],"branch_refs":["root_000059/B002","root_000266/B001"],"candidate_id":"cand_e9db42b0009db1e8ac36","evidence_scope":"focus_ayah","hft_ref":"hft_67b32e11d5f89ecbdd68","item_id":"baseline_perceptibility_axis","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_perceptibility_axis","support_id":"sup_cfc6709aca10eec8bc5f"},{"anchor_refs":["114:6"],"branch_refs":["root_000059/B003","root_000059/B006","root_000266/B010"],"candidate_id":"cand_2abbfecf8a1aa3234623","evidence_scope":"focus_ayah","hft_ref":"hft_0c01bbebc3ec089d8f81","item_id":"baseline_inner_familiar_sources","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_inner_familiar_sources","support_id":"sup_0207b38de44bec322512"},{"anchor_refs":["114:6"],"branch_refs":["root_000059/B001","root_000266/B013"],"candidate_id":"cand_33f022d1bd814d192802","evidence_scope":"focus_ayah","hft_ref":"hft_753851e92ccd1df0eb0f","item_id":"baseline_mass_person_scale","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_mass_person_scale","support_id":"sup_bd0d87185e8e80075fc9"}],"diagnostics":[],"lane_counts":{"global":9,"macro":10,"micro":4},"packet_summary":{"ayah_count":6,"focus_ref":"114:6","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ش ر ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000787","furuq_root_norm":"ش ر ر","furuq_source_root_norm":"ش ر ر","is_dominant":true,"target_occurrences":19,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000792","furuq_root_norm":"ش ر ي","furuq_source_root_norm":"ش ر ي","is_dominant":false,"target_occurrences":11,"target_rank":2}]}],"window":["114:1","114:2","114:3","114:4","114:5","114:6"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"114:6","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":14,"unstructured_record_count":0},"identity":{"ayah_ref":"114:6","lane":"micro","linguistic_source_ref":"114:6","surface_ref":"114:6","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"114:6","target_tokens":[["Cinlerden",["114:6:1","114:6:2"]],["ve",["114:6:3"]],["insanlardan",["114:6:1","114:6:3"]]],"text":"Cinlerden ve insanlardan."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":6,"id":"s114-p01-001-006","label":"Whole surah","number":1,"refs":["114:1","114:2","114:3","114:4","114:5","114:6"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:1","source_type":"word_analysis","support_id":"sup_0766eca66af2abfada20","text":"{\"gloss_range\":\"from, from among, or specifying; here a dependent source/specification particle that points back to the prior whisperer frame\",\"prose\":\"{{ar:مِنَ}} ({{tr:mina}}) opens the final ayah as a dependent particle, so the phrase cannot stand alone; it must be read back through the whisperer in 114:4 and the act of whispering in 114:5. Its single occurrence governs the whole coordinated pair, making {{ar:ٱلْجِنَّةِ}} ({{tr:al-jinnati}}) and {{ar:ٱلنَّاسِ}} ({{tr:al-nāsi}}) one compressed source frame rather than two separate openings. The particle keeps several local values live: it may specify what kind of whisperer has been named, mark some members from the two classes, or name the origin from which whispering proceeds. That range is productive, but it is bounded by the grammar: the ayah is an elliptical prepositional phrase recovered from the prior clause, not a new independent sentence. Even in sound, the final vowel carries {{ar:مِنَ}} ({{tr:mina}}) into {{ar:ٱلْجِنَّةِ}} ({{tr:al-jinnati}}), so dependence is heard as well as parsed.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مِنَ}} ({{tr:mina}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:3:explicit-two-member-taxonomy","source_type":"word_analysis","support_id":"sup_125941818a803dcbb9ba","text":"{\"blocking_evidence\":null,\"headline\":\"explicit two-member taxonomy\",\"reader_payoff\":\"The reader notices that hidden and human sources are held together as two coordinated members, not blurred into a single explanatory noun.\",\"reason\":\"The explicit conjunction preserves a binary source pair. The broader row's hierarchy possibilities are retained only as sequence pressure, while the grammar itself licenses coordination.\",\"representative_source_ids\":[\"QT-01f3be7c\",\"QS-ca336f74\",\"MG-93be9282\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:1:elliptic-cross-ayah-dependency","source_type":"word_analysis","support_id":"sup_14483ffb6de7d1705431","text":"{\"blocking_evidence\":null,\"headline\":\"elliptic closing phrase depends on prior frame\",\"reader_payoff\":\"The reader notices that the last ayah is deliberately lean, forcing the final phrase back through the whisperer and whispering clauses.\",\"reason\":\"Attachment support explicitly recovers the head of the phrase from the preceding whisperer description, matching the CRITICAL claim that 114:6 is syntactically dependent.\",\"representative_source_ids\":[\"QT-b32b28bd\",\"QT-cd55cce4\",\"QB-c2b81f13\",\"QY-1c7fa5ca\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:1:three-live-min-values","source_type":"word_analysis","support_id":"sup_224bb0630e8081b392e7","text":"{\"blocking_evidence\":null,\"headline\":\"specification partition and origin remain live\",\"reader_payoff\":\"The reader sees that the closing phrase can classify the whisperer, restrict blame to some members, and locate the action's source without forcing only one value.\",\"reason\":\"The grammar notes support explanatory and partitive readings and warn against over-specifying one value. The broader claim is narrowed by avoiding an unsupported assertion that the whisperer must have a single dual nature.\",\"representative_source_ids\":[\"QG-53099e73\",\"QG-a4417667\",\"QG-c39c7d7e\",\"QS-f6159ecd\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:4:collective-form-not-individual-action","source_type":"word_analysis","support_id":"sup_2ccd0158b44c512181f8","text":"{\"blocking_evidence\":null,\"headline\":\"collective class noun not individual action\",\"reader_payoff\":\"The reader notices that the closing word names the human class rather than an individual human or an action of seeking familiarity.\",\"reason\":\"The surface form is the definite collective noun {{ar:ٱلنَّاسِ}} ({{tr:al-nāsi}}), so derived action forms from the root family do not govern the local sense.\",\"representative_source_ids\":[\"QF-68528d95\",\"QF-faedb4c8\",\"QF-faf7550c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:4:social-perceptible-and-forgetful-pressure","source_type":"word_analysis","support_id":"sup_2e93f66a680f7ea0eb9d","text":"{\"blocking_evidence\":null,\"headline\":\"social perceptible and forgetful pressures\",\"reader_payoff\":\"The reader sees human whispering as socially familiar and detectable, while also hearing the contested forgetfulness pressure that makes humans vulnerable.\",\"reason\":\"QAC gives {{ar:أ ن س}} ({{tr:ʾ-n-s}}) as the local root, while the input preserves a classical dispute with the forgetfulness derivation. Because V4 is missing for this root, the dispute is not rejected, but it remains pressure rather than replacing the local noun.\",\"representative_source_ids\":[\"QS-18447d67\",\"QS-5e64c598\",\"QS-ebfbafa6\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:2:jinn-human-source-taxonomy","source_type":"word_analysis","support_id":"sup_36976b4fc4ebb66cc04c","text":"{\"blocking_evidence\":null,\"headline\":\"hidden-visible source taxonomy\",\"reader_payoff\":\"The reader sees the familiar jinn-human pairing recast here as a taxonomy of whispering sources.\",\"reason\":\"The co-occurrence rows support a known {{ar:ج ن ن}} ({{tr:j-n-n}}) and {{ar:أ ن س}} ({{tr:ʾ-n-s}}) pairing, and local coordination makes that pair a two-source frame for whispering.\",\"representative_source_ids\":[\"QI-587d7f2b\",\"QT-98b11d87\",\"QE-7cda5a87\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:3:coordination-under-one-min","source_type":"word_analysis","support_id":"sup_4ed92ba2c1c0e7438ef6","text":"{\"blocking_evidence\":null,\"headline\":\"coordination under one preposition\",\"reader_payoff\":\"The reader sees that the second noun inherits the same source frame rather than starting a new clause or phrase.\",\"reason\":\"QAC and attachment evidence identify {{ar:وَ}} ({{tr:wa}}) as coordination between two genitive nouns under {{ar:مِنَ}} ({{tr:mina}}), with no new clause introduced.\",\"representative_source_ids\":[\"QG-7b91a949\",\"QG-ba258350\",\"QG-c8f15ec2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"114:6:2:2","source_type":"qac_morpheme","support_id":"sup_4edc6ae655cd6fc50853","text":"{\"lemma_ar\":\"جِنَّة\",\"morph_features\":\"STEM|POS:N|LEM:jin~ap|ROOT:jnn|F|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"114:6:2:2\",\"qac_word_ref\":\"114:6:2\",\"root_ar\":\"ج ن ن\",\"surface_ar\":\"جِنَّةِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:2:governed-collective-source-class","source_type":"word_analysis","support_id":"sup_59701b2ebc4950645b31","text":"{\"blocking_evidence\":null,\"headline\":\"governed collective source class\",\"reader_payoff\":\"The reader notices that the noun is not an independent label but the first genitive source class governed by the opening particle.\",\"reason\":\"QAC marks the word as a definite genitive collective noun governed by {{ar:مِنَ}} ({{tr:mina}}), and attachment evidence makes it the head of the coordination with {{ar:ٱلنَّاسِ}} ({{tr:al-nāsi}}).\",\"representative_source_ids\":[\"QG-16d2d439\",\"QG-e0b2a9fd\",\"QF-055373e4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:2","source_type":"word_analysis","support_id":"sup_60ca58d8a83993984d42","text":"{\"gloss_range\":\"the jinn as a definite collective source class, locally selected as the hidden-beings member of the final pair\",\"prose\":\"{{ar:ٱلْجِنَّةِ}} ({{tr:al-jinnati}}) is the first governed source noun under {{ar:مِنَ}} ({{tr:mina}}), and its definite collective form names a class before any individual agent is counted. The root field matters because the locally selected sense is the hidden-beings branch: the danger is not just another species label, but a concealed source placed beside the visible human source; even within a garden-heavy root distribution, this closing source phrase selects the marked hidden-being lane. Other {{ar:ج ن ن}} ({{tr:j-n-n}}) images, such as shield, fetus, veiled reason, and enclosed garden, are useful only as narrowed concealment pressure; they do not replace the surface referent. The near form-echo with {{ar:ٱلْجَنَّةِ}} ({{tr:al-jannati}}) keeps enclosed-place imagery audible, and rows that connect whispering to the garden scenes (7:20; 20:120) and to Iblis as one of the jinn (18:50) remain a background echo rather than the local parse. In recitation, the liaison from {{ar:مِنَ}} ({{tr:mina}}) into {{ar:ٱلْجِنَّةِ}} ({{tr:al-jinnati}}) binds governor and source noun, and the doubled central nasal makes the concealment field audible inside the word. In the final taxonomy, {{ar:ٱلْجِنَّةِ}} ({{tr:al-jinnati}}) comes first as the concealed pole, then the phrase lands on {{ar:ٱلنَّاسِ}} ({{tr:al-nāsi}}) as the human pole.\",\"root_display\":\"{{ar:ج ن ن}} ({{tr:j-n-n}})\",\"root_gloss_range\":\"covering and concealment, including hidden beings, enclosed garden, shield, fetus, veiled reason, and related coveredness images; the local form selects hidden beings while allowing concealment pressure to remain active\",\"surface_display\":\"{{ar:ٱلْجِنَّةِ}} ({{tr:al-jinnati}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:2:exposed-interior-meets-concealed-source","source_type":"word_analysis","support_id":"sup_64078f65edb9835d715e","text":"{\"blocking_evidence\":null,\"headline\":\"concealed source answers exposed interior\",\"reader_payoff\":\"The reader notices the boundary movement from the exposed human chest in 114:5 to a concealed source class in 114:6.\",\"reason\":\"The preceding ayah locates whispering in human chests, while this genitive noun names the hidden source class that helps explain the interior vulnerability.\",\"representative_source_ids\":[\"QS-d0bd2b73\",\"MI-f2acfee6\",\"QB-758945e5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:4:final-closure-on-humankind","source_type":"word_analysis","support_id":"sup_657ed1020826dde548a7","text":"{\"blocking_evidence\":null,\"headline\":\"final closure lands on humankind\",\"reader_payoff\":\"The reader feels the surah and mushaf-order closure land on the human class itself.\",\"reason\":\"The word is last in 114:6 and is identified by the CRITICAL rows as the closing word of the surah and mushaf order, so the closure payoff is local and structural.\",\"representative_source_ids\":[\"QT-3a37e8eb\",\"QT-5b7f567e\",\"MT-c2844b7d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:4:balanced-final-pair-cadence","source_type":"word_analysis","support_id":"sup_691ef556e6ce47a40bed","text":"{\"blocking_evidence\":null,\"headline\":\"balanced final pair cadence\",\"reader_payoff\":\"The reader hears the two short definite genitives as a balanced pair before interpreting them separately.\",\"reason\":\"The local phrase places {{ar:ٱلْجِنَّةِ}} ({{tr:al-jinnati}}) and {{ar:ٱلنَّاسِ}} ({{tr:al-nāsi}}) as parallel definite genitives under one source frame.\",\"representative_source_ids\":[\"QP-1538fb74\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:3:compressed-clitic-and-sound-bond","source_type":"word_analysis","support_id":"sup_705768d11d9123e82b44","text":"{\"blocking_evidence\":null,\"headline\":\"compressed clitic sound bond\",\"reader_payoff\":\"The reader notices that the coordinate marker is visually and audibly fused to the second source noun.\",\"reason\":\"The one-letter clitic attaches to {{ar:ٱلنَّاسِ}} ({{tr:al-nāsi}}), and the recited boundary flows into the assimilated nūn.\",\"representative_source_ids\":[\"QF-3b477029\",\"QF-d75c49f0\",\"QP-c421515d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:4:generic-class-under-min","source_type":"word_analysis","support_id":"sup_76765550062e7b33b480","text":"{\"blocking_evidence\":null,\"headline\":\"generic class under shared preposition\",\"reader_payoff\":\"The reader sees humankind named as a class while the source role can still be restricted to some members.\",\"reason\":\"QAC marks the word as definite, generic, and genitive through coordination under {{ar:مِنَ}} ({{tr:mina}}); translation support preserves the ambiguity between explanatory and partitive force.\",\"representative_source_ids\":[\"QG-19a68a3c\",\"QG-574b786f\",\"QG-8f3c8a08\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:4:surah-lexical-spine","source_type":"word_analysis","support_id":"sup_78d1d7014ef535f1a482","text":"{\"blocking_evidence\":null,\"headline\":\"surah-local human noun spine\",\"reader_payoff\":\"The reader notices that a very common word becomes unusually concentrated as the surah's repeated human thread.\",\"reason\":\"The input marks this as a repeated discourse reference, and the CRITICAL rows track the recurrence from the opening title phrase (114:1) to the final source pair (114:6).\",\"representative_source_ids\":[\"QI-450823c2\",\"QI-f316c2c8\",\"MT-f2216901\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:3:hidden-to-human-hinge","source_type":"word_analysis","support_id":"sup_7d83bf81a29c4b07f446","text":"{\"blocking_evidence\":null,\"headline\":\"hinge from hidden to human\",\"reader_payoff\":\"The reader hears the ayah turn from an unseen source to the reader's own visible human class.\",\"reason\":\"The conjunction sits between the concealed source noun and the human noun, so the ordering effect is local to the coordinated phrase.\",\"representative_source_ids\":[\"QT-8dcb5dfc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:2:liaison-to-governed-noun","source_type":"word_analysis","support_id":"sup_7e87d4fc602b99ba41ed","text":"{\"blocking_evidence\":null,\"headline\":\"liaison joins governor and noun\",\"reader_payoff\":\"The reader hears the preposition and source noun as a bound unit in recitation.\",\"reason\":\"The hamzat-waṣl boundary lets {{ar:مِنَ}} ({{tr:mina}}) link directly into {{ar:ٱلْجِنَّةِ}} ({{tr:al-jinnati}}), matching the syntactic dependency.\",\"representative_source_ids\":[\"QP-12cce8af\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:4:jinn-human-pair-completion","source_type":"word_analysis","support_id":"sup_88d65410784cdbb5b365","text":"{\"blocking_evidence\":null,\"headline\":\"jinn-human pair completed\",\"reader_payoff\":\"The reader sees the familiar jinn-human pair completed with the human pole as the final landing point.\",\"reason\":\"The co-occurrence rows support the pairing, and local coordination makes {{ar:ٱلنَّاسِ}} ({{tr:al-nāsi}}) the second member of the hidden-human source taxonomy.\",\"representative_source_ids\":[\"QI-3ab18942\",\"QT-83cf7165\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:1:single-min-governs-pair","source_type":"word_analysis","support_id":"sup_941599af6ab91c987c93","text":"{\"blocking_evidence\":null,\"headline\":\"single particle governs both source nouns\",\"reader_payoff\":\"The reader notices that one small particle gathers both final source classes into a single grammatical frame.\",\"reason\":\"QAC and attachment evidence mark {{ar:مِنَ}} ({{tr:mina}}) as the governor of the following genitives, with {{ar:ٱلنَّاسِ}} ({{tr:al-nāsi}}) inheriting that government through coordination.\",\"representative_source_ids\":[\"QG-27574856\",\"QF-beb82b35\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:3:balanced-audible-pair","source_type":"word_analysis","support_id":"sup_9a5cf366698984ca493e","text":"{\"blocking_evidence\":null,\"headline\":\"balanced audible source pair\",\"reader_payoff\":\"The reader hears the two heavier definite nouns balanced around a very short hinge.\",\"reason\":\"The phonetic rows coherently track the local pair: repeated nasal texture and the short conjunction make the coordinated close compact and balanced.\",\"representative_source_ids\":[\"QE-b1fa9237\",\"QP-264b2135\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:4","source_type":"word_analysis","support_id":"sup_b74c66ddefa52f8516c9","text":"{\"gloss_range\":\"humankind or people as a definite generic class, here the final coordinated human source under the opening preposition\",\"prose\":\"{{ar:ٱلنَّاسِ}} ({{tr:al-nāsi}}) closes the phrase as the second genitive source noun, inheriting {{ar:مِنَ}} ({{tr:mina}}) through {{ar:وَ}} ({{tr:wa}}). Its definite collective shape names humankind as a class, while the possible partitive force of {{ar:مِنَ}} ({{tr:mina}}) prevents that class naming from becoming universal blame; the form is a class noun, not an individualized human term or a derived action of seeking familiarity. The word is also the surah's returning human noun: in 114:1-3 humankind is the protected community named after divine titles, in 114:5 humankind is the interior target, and here humankind can be a source of whispering. The {{ar:أ ن س}} ({{tr:ʾ-n-s}}) family makes that source socially perceptible and familiar, while the contested forgetfulness derivation remains a narrowed pressure: humans are not only visible agents but also vulnerable targets. As the last word of the ayah, the surah, and the mushaf order, {{ar:ٱلنَّاسِ}} ({{tr:al-nāsi}}) makes the refuge sequence land on the human class itself. Its assimilated article doubles the nūn, so the final class noun also completes the surah's repeated nasal close.\",\"root_display\":\"{{ar:أ ن س}} ({{tr:ʾ-n-s}})\",\"root_gloss_range\":\"humanity, sociability, perception, familiarity, and a contested forgetfulness derivation; locally the noun names the human class while those pressures shape its role\",\"surface_display\":\"{{ar:ٱلنَّاسِ}} ({{tr:al-nāsi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:1:audible-link-into-jinnati","source_type":"word_analysis","support_id":"sup_ba49c8b53838633c763c","text":"{\"blocking_evidence\":null,\"headline\":\"recited link carries the dependency\",\"reader_payoff\":\"The reader hears the particle flow into its governed noun instead of treating the source marker as detached.\",\"reason\":\"The surface form preserves a linking vowel before the hamzat-waṣl noun, and the nasal sequence binds the source-marker to {{ar:ٱلْجِنَّةِ}} ({{tr:al-jinnati}}).\",\"representative_source_ids\":[\"QF-a9525794\",\"QP-3deb22d5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:3","source_type":"word_analysis","support_id":"sup_bef581da04a7cefb3747","text":"{\"gloss_range\":\"coordinating conjunction joining the two genitive source nouns under the same preposition\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) is narrow but decisive: it coordinates {{ar:ٱلنَّاسِ}} ({{tr:al-nāsi}}) with {{ar:ٱلْجِنَّةِ}} ({{tr:al-jinnati}}) under the one preceding {{ar:مِنَ}} ({{tr:mina}}). Because the conjunction is explicit, the two nouns remain a paired taxonomy rather than one noun collapsing into apposition to the other. Its position also makes the movement audible: the ayah turns from the concealed source class to the visible human source class, with the tiny clitic carrying the second genitive into the same frame. The two heavier definite nouns balance around that one-letter hinge, and their repeated nasal texture is what lets the hidden-human pair sound bound before interpretation. In recitation, the conjunction flows directly into the assimilated boundary of {{ar:ٱلنَّاسِ}} ({{tr:al-nāsi}}), making the hinge compact rather than heavy.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:1:origin-after-interior-vector","source_type":"word_analysis","support_id":"sup_c4502c7e029f55c4dbeb","text":"{\"blocking_evidence\":null,\"headline\":\"origin answers the prior interior\",\"reader_payoff\":\"The reader sees the movement from whispering inside human chests in 114:5 to the source from which that whispering comes in 114:6.\",\"reason\":\"The local prepositional contrast is coherent: 114:5 names the interior target, while 114:6 supplies the source phrase under {{ar:مِنَ}} ({{tr:mina}}).\",\"representative_source_ids\":[\"QB-991df8b3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:2:jinna-janna-form-echo","source_type":"word_analysis","support_id":"sup_c4ee4fae752dea6f5c1c","text":"{\"blocking_evidence\":null,\"headline\":\"hidden-being form echoes enclosed garden\",\"reader_payoff\":\"The reader hears the surface word as hidden beings while also noticing the nearby enclosed-garden echo carried by the same root frame.\",\"reason\":\"The surface vocalization selects {{ar:ٱلْجِنَّةِ}} ({{tr:al-jinnati}}), not {{ar:ٱلْجَنَّةِ}} ({{tr:al-jannati}}). The garden-whispering links (7:20; 20:120) and Iblis link (18:50) are retained as echo and background, not as a replacement sense.\",\"representative_source_ids\":[\"QF-9745f1cf\",\"QE-783a9217\",\"MP-4f3f398b\",\"QY-c25981b2\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:4:role-reversal-within-surah","source_type":"word_analysis","support_id":"sup_d7945b39f8928c301d32","text":"{\"blocking_evidence\":null,\"headline\":\"protected humans become possible source\",\"reader_payoff\":\"The reader notices that the same human noun moves from protected object and target to possible source of harm.\",\"reason\":\"The attachment cross-reference marks this as a repeated {{ar:ٱلنَّاسِ}} ({{tr:al-nāsi}}) instance, and the CRITICAL rows give concrete prior anchors at 114:1-3 and 114:5.\",\"representative_source_ids\":[\"QG-841d6ce9\",\"QG-f0007d35\",\"QE-977217f8\",\"QY-9707f19e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:2:hidden-beings-concealment-mechanism","source_type":"word_analysis","support_id":"sup_d7ad92f11d1ed39f0083","text":"{\"blocking_evidence\":null,\"headline\":\"hidden beings carry concealment pressure\",\"reader_payoff\":\"The reader sees the jinn source as dangerous through imperceptibility, while the local wording still selects hidden beings rather than every branch of the root.\",\"reason\":\"V4 accepts several {{ar:ج ن ن}} ({{tr:j-n-n}}) branches, including hidden spirit beings and broader covering images. The coordinate contrast with {{ar:ٱلنَّاسِ}} ({{tr:al-nāsi}}) selects hidden beings and narrows the other branches to pressure.\",\"representative_source_ids\":[\"QS-1c544850\",\"QS-f2be8b76\",\"QI-e0859668\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:2:geminated-nasal-concealment-sound","source_type":"word_analysis","support_id":"sup_dcd78fed513060181899","text":"{\"blocking_evidence\":null,\"headline\":\"geminated nasal makes hiddenness audible\",\"reader_payoff\":\"The reader hears the doubled central nasal as part of the word's concealment effect, not as a detachable ornament.\",\"reason\":\"The local form contains the geminated root consonant, and the phonetic rows align that held nasal closure with the accepted concealment field.\",\"representative_source_ids\":[\"QF-a8f98278\",\"QP-63bb6961\",\"QP-cd5dc5eb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"114:6:4:audible-nasal-fawasil-close","source_type":"word_analysis","support_id":"sup_e7acec59cd2781855742","text":"{\"blocking_evidence\":null,\"headline\":\"nasal sound closes the pattern\",\"reader_payoff\":\"The reader hears the final class noun complete the surah's repeated nasal close.\",\"reason\":\"The article assimilates into the nūn, and the phonetic rows connect that doubled nasal landing with the repeated end-sound pattern of Surah 114.\",\"representative_source_ids\":[\"QF-3fa8adb3\",\"QP-97b8d2fb\",\"QP-e408bb71\",\"QP-f9dbdd6d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"114:6:3:3","source_type":"qac_morpheme","support_id":"sup_f214866deda94fa3a614","text":"{\"lemma_ar\":\"نَّاس\",\"morph_features\":\"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"114:6:3:3\",\"qac_word_ref\":\"114:6:3\",\"root_ar\":\"ن و س\",\"surface_ar\":\"نَّاسِ\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ","ayah_ref":"114:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000059/B001","root_000266/B005"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000266","role":"Hidden spirit beings supply the concealed agent class named by the first conjunct.","root":"ج ن ن","source_ref":"114:6","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000059","role":"Visible human presence over against hidden beings supplies the manifest agent class and the contrastive second conjunct.","root":"ن و س","source_ref":"114:6","source_word_indices":["3"]}],"changed_reading":{"after":"A single source relation spans concealed nonhuman and visible human agents; invisibility does not monopolize harmful agency.","before":"A flat list of jinn and humans."},"confidence":"strong","focus_anchor":"The coordinated nouns at words 2-3 place الجنة and الناس under one source relation introduced by من.","mechanism":"The first noun activates concealed spirit agents while the second activates visible human presence, so one harmful-source relation crosses the boundary of perceptibility.","model_id":"baseline_hidden_visible_agents"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_hidden_visible_agents","source_type":"hft","support_id":"sup_8b3ac0a346f5af86ab66","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ","ayah_ref":"114:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000059/B002","root_000266/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000266","role":"Covering from perception supplies the concealed channel and permits an inwardly hidden source.","root":"ج ن ن","source_ref":"114:6","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000059","role":"Perceiving by seeing, sensing, or hearing supplies the channel that becomes consciously detectable.","root":"ن و س","source_ref":"114:6","source_word_indices":["3"]}],"changed_reading":{"after":"The pair also distinguishes concealed pressure from signals that enter awareness, without requiring the two modes to remain separate agents.","before":"Two species of whisperer are named."},"confidence":"medium","focus_anchor":"The same coordinated roots can be read through their opposed concealment and perception branches.","mechanism":"ج ن ن supplies what is covered from perception, including what is kept in the breast, while ن و س supplies detection by sight, sensation, or hearing. The pair therefore classifies channels of influence by detectability as well as naming beings.","model_id":"baseline_perceptibility_axis"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_perceptibility_axis","source_type":"hft","support_id":"sup_cfc6709aca10eec8bc5f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ","ayah_ref":"114:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000059/B003","root_000059/B006","root_000266/B010"],"payload":{"activation_trace":[{"branch_id":"B010","mapped_root_id":"root_000266","role":"The hidden heart or inner fear supplies an affective source that can operate without an external speaker.","root":"ج ن ن","source_ref":"114:6","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000059","role":"Familiar comfort that removes estrangement supplies the trusted social route through which influence can pass unnoticed.","root":"ن و س","source_ref":"114:6","source_word_indices":["3"]},{"branch_id":"B006","mapped_root_id":"root_000059","role":"The self or intimate chosen companion keeps the human pole close to the recipient rather than limiting it to strangers.","root":"ن و س","source_ref":"114:6","source_word_indices":["3"]}],"changed_reading":{"after":"The source range can run from hidden inward agitation to one's own familiar self and intimate human company.","before":"The danger comes from external members of two populations."},"confidence":"exploratory","focus_anchor":"The first root reaches hidden heart and inner fear, while the second reaches familiarity, selfhood, and intimate companionship.","mechanism":"The coordination can stretch from an inward agitation that lacks an external face to influence arriving through one's familiar self or trusted company. The contrast becomes distance from scrutiny rather than simple distance from humanity.","model_id":"baseline_inner_familiar_sources"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_inner_familiar_sources","source_type":"hft","support_id":"sup_0207b38de44bec322512","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ","ayah_ref":"114:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000059/B001","root_000266/B013"],"payload":{"activation_trace":[{"branch_id":"B013","mapped_root_id":"root_000266","role":"The dark mass or common crowd supplies diffuse, anonymous human pressure at the first pole.","root":"ج ن ن","source_ref":"114:6","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000059","role":"Visible human presence supplies particular or recognizable people at the second pole.","root":"ن و س","source_ref":"114:6","source_word_indices":["3"]}],"changed_reading":{"after":"It can additionally separate ambient crowd force from direct influence by present people.","before":"The coordination separates jinn from humankind."},"confidence":"exploratory","focus_anchor":"A ج ن ن branch names a dark mass of people, while the ن و س inventory names present human beings.","mechanism":"Instead of only dividing nonhuman from human, the pair can distinguish anonymous collective pressure from identifiable interpersonal agency.","model_id":"baseline_mass_person_scale"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_mass_person_scale","source_type":"hft","support_id":"sup_bd0d87185e8e80075fc9","trust":"legacy_unbound"}]}
</lane_packet_json>
