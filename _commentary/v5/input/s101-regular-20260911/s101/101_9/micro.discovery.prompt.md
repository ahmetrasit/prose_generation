# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **101:9**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s101-regular-20260911/s101/101_9/micro.discovery.json` and modify nothing
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
  "ayah_ref": "101:9",
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
{"analysis_context":{"analysis_id":"s101-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"101:9","host_surah":101,"lane_context_refs":[],"ordered_context_refs":["101:0","101:1","101:2","101:3","101:4","101:5","101:6","101:7","101:8","101:10","101:11","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Çekirdek annelik ve annelik işleviyle sınırlıdır; aynı kökün topluluk, inanç yolu ve soru bağlacı anlamları buraya girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000053/B001","candidate_links":[{"candidate_id":"cand_806fdff7f00274cc81b6","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أُمّ","morph_features":"STEM|POS:N|LEM:>um~|ROOT:Amm|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:1:2","qac_word_ref":"101:9:1","surface_ar":"أُمُّ"}],"gloss":"anne ve annelik işlevi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Doğuran anne ile yakın veya uzak kadın ata aynı temel annelik konumunda adlandırılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kadının anne olması ve birini anne gibi besleyip büyütmesi annelik işlevinin uzantısıdır."}}],"root_ar":"ء م م","root_id":"root_000053","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Doğuran kadın, kadın ata veya anne gibi bakım veren kişi söz konusu olduğunda çekirdeğin tamamını karşılar.","boundary_detail":"Çekirdek annelik ve annelik işleviyle sınırlıdır; aynı kökün topluluk, inanç yolu ve soru bağlacı anlamları buraya girmez.","branch_image_ar":"الأم الوالدة والمربية","concept_gloss":"anne ve annelik işlevi","contextual_glosses":[{"applicability":"Doğuran kadın veya kadın ata için doğal ve kısa karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Temel annelik bağını ve kadın ata kapsamını korur."},"facet_ids":["F001"],"text":"anne","usage_role":"general"},{"applicability":"Bir kişinin biyolojik bağdan bağımsız olarak annelik bakımını üstlenmesini anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Besleme, bakım ve büyütme yoluyla annelik işlevini üstlenmeyi korur."},"facet_ids":["F002"],"text":"anne gibi besleyip büyütmek","usage_role":"contextual"}],"definition":"Doğuran kadın ya da soy bakımından daha uzaktaki kadın ata ve onun üstlendiği annelik konumudur. Bir kadının anne hâline gelmesini ve birini anne gibi besleyip büyütmesini de kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Doğuran anne ile yakın veya uzak kadın ata aynı temel annelik konumunda adlandırılır."},{"facet_id":"F002","role":"extension","statement":"Bir kadının anne olması ve birini anne gibi besleyip büyütmesi annelik işlevinin uzantısıdır."}],"identity_rationale":"Kaynak sözü, doğuran anneyi yakın ve uzak soy çizgisinde kapsar; ayrıca bir kadının anne oluşunu ve birini anne gibi besleyip büyütmesini açıkça belirtir. Bu nedenle annelik, yalnız biyolojik bağ değil, annelik işlevini üstlenmeyi de içeren tek bir çekirdek çevresinde kurulabilir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"anne"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"anneler"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"anneler; özellikle insan dışı canlılar için kullanılan çoğul"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"anne yokluğu üzerinden öven ya da yeren kalıp söz"}],"lexicalization_note":"Tanım yalın anne anlamını ve ona bağlı biçimleri kapsar; övgü ya da yergi bildiren kalıp söz yalnız kendi kullanım sınırında tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yakın karışma anne adını aynı biçimlerle veren komşu kolda görüldüğü için yalnız bu ayrım yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu kol anne adını ve biçimlerini öne çıkarırken odak kol annelik konumuna geçişi ve annelik bakımını da anlam alanına katar.","focus_only":"Anne olma ve birini anne gibi besleyip büyütme süreçleri de bu kolda açıkça yer alır.","gloss":"anne ve annelik","neighbor_only":null,"neighbor_ref":"root_000055/B004","relation_type":"near_synonym","shared_zone":"Her iki kol da doğuran anneyi ve anne çoğullarını temel alır."}],"source_phrase_ar":"الأم الواحد والجمع أمهات وربما قالوا أم وأمات وفلانة تؤم فلانا أي تغذوه وتربيه (maqayis)؛ الأم معروفة (jamhara)؛ الأم الوالدة والجمع أمات وأصل الأم أمهة لذلك تجمع على أمهات وأمت المرأة صارت أما (sihah)؛ الأم بإزاء الأب وهي الوالدة القريبة والبعيدة (mufradat)","source_summary":"Kaynaklarda ortak çekirdek temel anne anlamıdır; çoğul biçimler, anne olma, yakın ve uzak kadın ata kapsamı ve anne gibi besleyip büyütme ayrıntıları kaynak kümesinde ayrı katkılar olarak tanıklanır.","sources":["MQ","JA","SI","MU"],"what_is_ar":"يدخل فيه الأم الوالدة القريبة والبعيدة، وجموع أمهات وأمات، وصيرورة المرأة أما، والتغذية والتربية على صورة الأم، وما جرى من صيغ لا أم لك وويل أمه وهوت أمه في المدح أو الذم.","what_is_not_ar":"لا يدخل فيه معنى الأمة للجماعة أو الدين، ولا الإمام، ولا حرف أم."},"support_links":["sup_468cd99ebff6e6d8d1ec"]},{"boundary":"Anlam, bir şeyin kaynağı veya çevresindekileri toplayan odağıyla sınırlıdır; doğuran anne doğrudan bu dalın konusu değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000053/B002","candidate_links":[{"candidate_id":"cand_e5df16ecbc308492da67","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أُمّ","morph_features":"STEM|POS:N|LEM:>um~|ROOT:Amm|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:1:2","qac_word_ref":"101:9:1","surface_ar":"أُمُّ"}],"gloss":"ana kaynak ve toplayıcı odak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin başlangıcı ve varlık kaynağı bu adlandırmanın temelidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Çevresindeki veya kendisine bağlı unsurları toplayan merkez de aynı kaynak ilişkisiyle adlandırılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yetiştirme ve düzeltmenin dayandığı başlangıç noktası da kaynak kapsamına girer."}}],"root_ar":"ء م م","root_id":"root_000053","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin başlangıcı ile ona bağlı unsurların toplandığı yer veya dayanak birlikte anlatıldığında uygundur.","boundary_detail":"Anlam, bir şeyin kaynağı veya çevresindekileri toplayan odağıyla sınırlıdır; doğuran anne doğrudan bu dalın konusu değildir.","branch_image_ar":"الأم أصلا وجامعا ومرجعا","concept_gloss":"ana kaynak ve toplayıcı odak","contextual_glosses":[{"applicability":"Bir şeyin varlık veya başlangıç noktası öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çevredeki bağlı unsurları kendinde toplama yönünü tek başına belirtmez.","preserves":"Başlangıç ve varlık dayanağı olma yönünü korur."},"facet_ids":["F001","F003"],"text":"kaynak","usage_role":"general"},{"applicability":"Çevresindeki yerleri veya parçaları kendinde toplayan odak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Varlık ve yetişme kaynağı olma yönünü zorunlu olarak anlatmaz.","preserves":"Bağlı unsurları toplama ve merkez olma yönünü korur."},"facet_ids":["F002"],"text":"ana merkez","usage_role":"contextual"}],"definition":"Bir şeyin doğduğu, başladığı, yetiştiği veya düzeldiği kaynak ya da çevresindeki bağlı unsurları kendinde toplayan ana odaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin başlangıcı ve varlık kaynağı bu adlandırmanın temelidir."},{"facet_id":"F002","role":"extension","statement":"Çevresindeki veya kendisine bağlı unsurları toplayan merkez de aynı kaynak ilişkisiyle adlandırılır."},{"facet_id":"F003","role":"extension","statement":"Yetiştirme ve düzeltmenin dayandığı başlangıç noktası da kaynak kapsamına girer."}],"identity_rationale":"Kaynak sözü, çevresindeki şeyleri kendinde toplayan şeyi ve bir şeyin varlık, yetişme veya düzelme bakımından kaynağını aynı adlandırma altında birleştirir. Dalın kaynak, başlangıç, toplayıcı odak ve dönüş noktası çerçevesi bu ortak ilişkiyi doğru temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bir şeyin kaynağı, başlangıcı veya parçalarının döndüğü odak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"Mekke; bağlama göre çevresindeki yerleşimleri toplayan ana kent"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kitabın ana kaynağı; bağlama göre başlangıç bölümü veya korunmuş ana kayıt"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir şeyin kaynağını, odağını veya ana bölümünü gösteren adlandırma"}],"lexicalization_note":"Genel kaynak ve toplayıcı odak ilişkisi korunur; şehir, kitap ve başka ad tamlamalarındaki özel karşılıklar yalnız bağlı oldukları yapılarda geçerlidir.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel kaynak anlamıyla en güçlü örtüşme köklü ve sabit temel bildiren komşuda bulundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kol başlangıçla birlikte toplayıcı ve üretici ilişkiyi kurar; komşu kol ise eski, sabit ve birikmiş temel olmayı öne çıkarır.","focus_only":"Bağlı unsurları kendinde toplama, yetiştirme ve düzeltmeye kaynaklık etme kapsamı vardır.","gloss":"kaynak ve köklü temel","neighbor_only":"Komşu anlam, köklü biçimde sabit kalma, eskilik ve birikerek dayanak oluşturma özelliklerini taşır.","neighbor_ref":"root_000012/B001","relation_type":"near_synonym","shared_zone":"Her iki kol da bir şeyin dayandığı başlangıç veya temel noktasını anlatır."}],"source_phrase_ar":"كل شيء يضم إليه ما سواه مما يليه فإن العرب تسمى ذلك الشيء أما (maqayis)؛ كل شيء يضم إليه سائر ما يليه فإن العرب تسمي ذلك الشيء أما (ayn)؛ كل شيء انضمت إليه أشياء فهو أم (jamhara)؛ أم الشيء أصله ومكة أم القرى (sihah)؛ كل ما كان أصلا لوجود شيء أو تربيته أو إصلاحه أو مبدئه أم (mufradat)","source_summary":"Kaynak kümesinde köken ve başlangıç yönü ile çevredeki veya bağlı unsurları toplayan merkez yönü birlikte tanıklanır; bu yönler her kaynakta zorunlu ortak bileşim olarak verilmez.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه أم الشيء بمعنى أصله أو مبدئه أو ما يضم إليه ما حوله، ومنه أم القرى وأم الكتاب وأم النجوم وأم الطريق وأمثال كنى أم التي تجعل الشيء مركزا أو مجمعا أو أصلا.","what_is_not_ar":"لا يدخل فيه الأم الوالدة بذاتها، ولا الشجة الآمة إلا من جهة اسم أم الدماغ، ولا الأمة بمعنى جماعة أو دين."},"support_links":["sup_fe446e14ae20f3850177"]},{"boundary":"Dal, beyin veya onu saran bölüm ile bu bölgeye ulaşan baş yarasına özgüdür; genel baş yaraları ve genel kaynak anlamı dışarıda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000053/B003","candidate_links":[{"candidate_id":"cand_0bad8584d81324f0b419","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أُمّ","morph_features":"STEM|POS:N|LEM:>um~|ROOT:Amm|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:1:2","qac_word_ref":"101:9:1","surface_ar":"أُمُّ"}],"gloss":"beyin bölgesi ve ona ulaşan baş yarası","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Baş içindeki beyin veya beyni kuşatan bölüm özel anatomik odaktır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu anatomik odağa ulaşan darbe ve baş yarası, odaktan türeyen yaralanma anlamını oluşturur."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yaralanmış kişi, aynı ağır baş yarası alanındaki bağlı adlandırmadır."}}],"root_ar":"ء م م","root_id":"root_000053","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Anatomik odak ile o odağa kadar ilerleyen ağır yaralanma birlikte anlatıldığında tam karşılıktır.","boundary_detail":"Dal, beyin veya onu saran bölüm ile bu bölgeye ulaşan baş yarasına özgüdür; genel baş yaraları ve genel kaynak anlamı dışarıda kalır.","branch_image_ar":"أم الدماغ وما يصيبه","concept_gloss":"beyin bölgesi ve ona ulaşan baş yarası","contextual_glosses":[{"applicability":"Bir darbenin baş içindeki beyin bölgesine kadar ulaştığı yaralanma için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaranın baş içindeki belirli anatomik odağa ulaşma koşulunu korur."},"facet_ids":["F002"],"text":"beyne ulaşan baş yarası","usage_role":"contextual"}],"definition":"Başın içindeki beyin ya da beyni kuşatan bölüm ve bir darbenin bu bölgeye kadar ulaştığı ağır baş yarasıdır. Bu yaraya uğrayan kişi de bağlı adlandırmalar arasındadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Baş içindeki beyin veya beyni kuşatan bölüm özel anatomik odaktır."},{"facet_id":"F002","role":"extension","statement":"Bu anatomik odağa ulaşan darbe ve baş yarası, odaktan türeyen yaralanma anlamını oluşturur."},{"facet_id":"F003","role":"associated_use","statement":"Yaralanmış kişi, aynı ağır baş yarası alanındaki bağlı adlandırmadır."}],"identity_rationale":"Kaynak sözü başın içindeki beyin bölgesini kimi yerde beynin kendisi, kimi yerde onu toplayan zar olarak açıklar ve yarayı bu bölgeye ulaşmasıyla tanımlar. Bu nedenle dal korunabilir, ancak yalnız beyin adı değil, beyin bölgesi ile ona ulaşan ağır baş yarası birlikte ve açık sınırla verilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"beyin veya baş içindeki beyin bölgesi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"beyne ulaşan baş yarası"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"başından beyin bölgesine ulaşan darbeyle yaralanmış kişi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ağır baş yaralısı; baş ezmeye yarayan taş"}],"lexicalization_note":"Beyin bölgesi ile ona ulaşan yarayı kapsayan yalın ve bağlı biçimler ayrılır; özel baş bölgesi dışındaki yaralara genellenmez.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; yalnız beyne ulaşma koşulunu aynı biçimde taşıyan ağır baş yarası komşusu yayımlanmaya değer görüldü.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kol yaradan yaralı kişiye ve bağlı araç adına uzanan bir adlandırma ailesidir; komşu kolun çekirdeği kırma ve beyne ulaşan darbedir.","focus_only":"Yaralanan kişiyi ve başı ezmekte kullanılan bağlı araç adını da kapsar.","gloss":"beyne ulaşan ağır baş yarası","neighbor_only":"Komşu kol kırma ve yaranın beyne erişmesi eylemini doğrudan öne çıkarır.","neighbor_ref":"root_000489/B001","relation_type":"near_synonym","shared_zone":"Her iki kol da beyin bölgesini ve baş yarasının bu bölgeye kadar ulaşmasını temel sınır sayar."}],"source_phrase_ar":"أم الرأس وهو الدماغ والشجة الآمة التي تبلغ أم الدماغ (maqayis)؛ أم الرأس وهو الدماغ ورجل مأموم والشجة الآمة التي تبلغ أم الدماغ (ayn)؛ أم رأسه بالعصا إذا أصاب أم رأسه وهي أم الدماغ (jamhara)؛ أم الدماع الجلدة التي تجمع الدماغ ويقال أيضا أم الرأس وأمه أي شجه آمة (sihah)؛ أمه شجه فحقيقته أن يصيب أم دماغه (mufradat)","source_summary":"Kaynaklar beyin bölgesi ve oraya ulaşan ağır baş yarasında birleşir; anatomik odağın beyin ya da onu toplayan zar diye açıklanması birlikte korunur.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه أم الرأس أو أم الدماغ، والشجة الآمة أو المأمومة التي تبلغها، والرجل الأميم أو المأموم، والحجر أو الآلة التي يشدخ بها الرأس.","what_is_not_ar":"لا يدخل فيه عموم الأم بمعنى الأصل إلا من جهة تسمية الدماغ أما، ولا يدخل فيه القصد أو الإمامة."},"support_links":["sup_337d33c3c239c33b49eb"]},{"boundary":"Salt inanç yolu, zaman süresi veya kadın köle anlamı bu topluluk ve tür çekirdeğine katılmaz.","branch_kind":"bare","branch_ref":"root_000053/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أُمّ","morph_features":"STEM|POS:N|LEM:>um~|ROOT:Amm|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:1:2","qac_word_ref":"101:9:1","surface_ar":"أُمُّ"}],"gloss":"ortak bağla birleşen topluluk veya tür","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ortak bir bağ veya aidiyet, insanları tek bir topluluk olarak birleştirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir insan kuşağı veya aynı cinsten hayvanlar da topluluk düşüncesinin kapsamına girer."}}],"root_ar":"ء م م","root_id":"root_000053","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan grupları, kuşaklar veya bir canlı cinsi ortak bir bütün olarak ele alındığında uygundur.","boundary_detail":"Salt inanç yolu, zaman süresi veya kadın köle anlamı bu topluluk ve tür çekirdeğine katılmaz.","branch_image_ar":"الأمة جماعة أو نوعا","concept_gloss":"ortak bağla birleşen topluluk veya tür","contextual_glosses":[{"applicability":"Ortak aidiyetle birleşen insan grubu için doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsan kuşağı ve hayvan cinsi kapsamını tek başına açıkça göstermez.","preserves":"Ortak bir bağla birleşen insan grubunu korur."},"facet_ids":["F001"],"text":"topluluk","usage_role":"general"},{"applicability":"Aynı cinsten hayvanların ortak bir bütün sayıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aynı cinsten canlıları ortak bir bütün olarak görme yönünü korur."},"facet_ids":["F002"],"text":"canlı türü","usage_role":"contextual"}],"definition":"Ortak bir bağ, aidiyet veya özellik çevresinde birleşen insan topluluğu, insan kuşağı ya da aynı cinsten canlılar topluluğudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ortak bir bağ veya aidiyet, insanları tek bir topluluk olarak birleştirir."},{"facet_id":"F002","role":"extension","statement":"Bir insan kuşağı veya aynı cinsten hayvanlar da topluluk düşüncesinin kapsamına girer."}],"identity_rationale":"Kaynak sözü, ortak bir şeye bağlanan insan topluluklarını, insan kuşaklarını ve hayvan cinslerini aynı üst anlamda toplar. Dalın topluluk veya tür çerçevesi bu genişliği ve birleştirici bağı doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ortak bir bağla birleşen topluluk veya canlı türü"}],"lexicalization_note":"Tanım yalın topluluk ve tür anlamını verir; aynı biçimin başka dallardaki inanç, zaman ve kişi anlamları içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; topluluk çekirdeğine en çok yaklaşan kabile ve sınıf alanı, daha dar örgütlenme sınırı nedeniyle seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kolun birleştirici ölçütü çok geneldir ve canlı türlerine uzanır; komşu kol soy ve kabile örgütlenmesine daha sıkı bağlıdır.","focus_only":"İnsan dışı canlı cinslerini ve herhangi bir ortak bağla birleşen insan kuşağını da kapsar.","gloss":"topluluk ve kabile","neighbor_only":"Komşu kol soy, kabile düzeni, karşılıklı yöneliş ve topluluk temsilcisi gibi daha özel örgütlenme özellikleri taşır.","neighbor_ref":"root_001198/B009","relation_type":"near_synonym","shared_zone":"Her iki kol da insan gruplarını ve bunların alt türlerini topluluk olarak adlandırır."}],"source_phrase_ar":"كل قوم نسبوا إلى شيء وأضيفوا إليه فهم أمة وكل جيل من الناس أمة (maqayis)؛ كل قوم في دينهم من أمتهم وكل جيل من الناس هم أمة وكل جنس من السباع أمة (ayn)؛ الأمة القرن من الناس (jamhara)؛ الأمة الجماعة وكل جنس من الحيوان أمة (sihah)؛ الأمة كل جماعة يجمعهم أمر ما (mufradat)","source_summary":"Kaynaklar ortak bir bağla birleşen insan topluluğunu temel alır ve kapsamı insan kuşakları ile hayvan cinslerine kadar genişletir.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الأمة بمعنى جماعة يجمعها أمر، أو قوم منسوبون إلى شيء، أو جيل من الناس، أو جنس من الحيوان، أو صنف واحد.","what_is_not_ar":"لا يدخل فيه الأمة بمعنى الدين وحده، ولا الحين، ولا الوليدة."},"support_links":[]},{"boundary":"Burada adlandırılan şey insan grubu değil, benimsenip izlenen inanç ve yaşayış yoludur.","branch_kind":"bare","branch_ref":"root_000053/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أُمّ","morph_features":"STEM|POS:N|LEM:>um~|ROOT:Amm|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:1:2","qac_word_ref":"101:9:1","surface_ar":"أُمُّ"}],"gloss":"benimsenen inanç ve yaşayış yolu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Benimsenen inanç düzeni ve ortak yol bu dalın temel anlamıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yerleşmiş uygulama biçimi ve izlenen davranış yolu aynı çekirdeğin kapsamındadır."}}],"root_ar":"ء م م","root_id":"root_000053","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi veya topluluğun bağlı kaldığı inanç düzeni ile izlenen yol birlikte kastedildiğinde uygundur.","boundary_detail":"Burada adlandırılan şey insan grubu değil, benimsenip izlenen inanç ve yaşayış yoludur.","branch_image_ar":"الأمة دينا وطريقة","concept_gloss":"benimsenen inanç ve yaşayış yolu","contextual_glosses":[{"applicability":"Dinsel bağlılık ve o bağlılığın izlenen yolu öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dinsel olmayan yerleşmiş uygulama biçimini açıkça kapsamaz.","preserves":"İnanç düzeni ve ona bağlı izlenen yol yönlerini korur."},"facet_ids":["F001"],"text":"inanç yolu","usage_role":"general"},{"applicability":"Yerleşmiş davranış ve uygulama biçiminin anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnanç düzeni olma yönünü zorunlu olarak belirtmez.","preserves":"Benimsenip sürdürülen yol ve uygulama yönünü korur."},"facet_ids":["F002"],"text":"izlenen yol","usage_role":"contextual"}],"definition":"Bir topluluğun veya kişinin benimseyip izlediği inanç düzeni, yaşayış yolu ya da yerleşmiş uygulama biçimidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Benimsenen inanç düzeni ve ortak yol bu dalın temel anlamıdır."},{"facet_id":"F002","role":"extension","statement":"Yerleşmiş uygulama biçimi ve izlenen davranış yolu aynı çekirdeğin kapsamındadır."}],"identity_rationale":"Kaynak sözü bu dalı din, benimsenen yol ve birlikte izlenen düzen olarak açıklar. Topluluğu değil, topluluğun üzerinde birleştiği inanç ve yaşayış yolunu öne çıkardığı için ayrı dal kimliği sağlamdır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"benimsenen inanç veya yaşayış yolu"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"inanç veya izlenen yol anlamındaki değişik söyleyiş"}],"lexicalization_note":"Yalın biçimin inanç ve izlenen yol anlamı tanımlanır; topluluk veya kişisel önder anlamı bu dala taşınmaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; düzenlenmiş inanç yolu bildiren komşu, çekirdeğe en yakın fakat kapsamı daha dar adaydır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kol genel olarak izlenen yol ve uygulamaya açılır; komşu kol daha belirli ve kurallı bir inanç geleneğine bağlıdır.","focus_only":"İnanç dışındaki yerleşmiş yol ve uygulama biçimine daha açık biçimde uzanır.","gloss":"inanç ve izlenen yol","neighbor_only":"Komşu kol özellikle bir bildiriciye veya düzenlenmiş inanç kurallarına bağlanan belirli inanç yolunu öne çıkarır.","neighbor_ref":"root_001445/B003","relation_type":"near_synonym","shared_zone":"Her iki kol da benimsenen dinsel yolu ve toplu inanç düzenini anlatabilir."}],"source_phrase_ar":"الأمة الدين (maqayis)؛ الأمة كل قوم في دينهم من أمتهم (ayn)؛ الأمة الملة (jamhara)؛ الأمة الطريقة والدين والإمة أيضا لغة في الأمة وهي الطريقة والدين (sihah)؛ إنا وجدنا آباءنا على أمة أي على دين مجتمع (mufradat)","source_summary":"Kaynaklar inanç düzeni, ortaklaşa benimsenen yol ve izlenen uygulama biçimini tek bir yol gösterici düzen altında birleştirir.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الأمة أو الإمة بمعنى الدين أو الملة أو الطريقة أو السنة المتبعة والطاعة.","what_is_not_ar":"لا يدخل فيه الجماعة بمجردها، ولا الإمام الشخصي إلا من جهة الاقتداء."},"support_links":[]},{"boundary":"Anlam insanın boyu ve görünür beden yapısıyla sınırlıdır; topluluk ve inanç yolu anlamları dışarıda kalır.","branch_kind":"bare","branch_ref":"root_000053/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أُمّ","morph_features":"STEM|POS:N|LEM:>um~|ROOT:Amm|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:1:2","qac_word_ref":"101:9:1","surface_ar":"أُمُّ"}],"gloss":"boy ve beden görünüşü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanın boyu ve beden ölçüsü temel fiziksel görünüşü oluşturur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Beden, yüz ve güzel yaratılış görünüşü boy anlamını bütün beden biçimine genişletir."}}],"root_ar":"ء م م","root_id":"root_000053","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir insanın uzunluğu, beden yapısı ve genel dış görünüşü birlikte değerlendirildiğinde uygundur.","boundary_detail":"Anlam insanın boyu ve görünür beden yapısıyla sınırlıdır; topluluk ve inanç yolu anlamları dışarıda kalır.","branch_image_ar":"القامة والهيئة","concept_gloss":"boy ve beden görünüşü","contextual_glosses":[{"applicability":"İnsanın uzunluğu veya kısalığı öne çıktığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yüzü ve genel beden görünüşünü tek başına kapsamaz.","preserves":"İnsanın dikey beden ölçüsünü ve uzunluk yönünü korur."},"facet_ids":["F001"],"text":"boy","usage_role":"contextual"},{"applicability":"Boyla birlikte yüz ve bütün fiziksel görünüş kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Beden ölçüsü, biçimi ve genel görünüşü bir arada korur."},"facet_ids":["F001","F002"],"text":"beden yapısı","usage_role":"general"}],"definition":"İnsanın boyu, beden yapısı, yüzü ve bunların oluşturduğu genel görünüş ya da yaratılış biçimidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanın boyu ve beden ölçüsü temel fiziksel görünüşü oluşturur."},{"facet_id":"F002","role":"extension","statement":"Beden, yüz ve güzel yaratılış görünüşü boy anlamını bütün beden biçimine genişletir."}],"identity_rationale":"Kaynak sözü insanın boyunu, bedenini, yüzünü ve yaratılış görünüşünü birlikte verir. Dalın boy ve beden görünüşü çerçevesi, yalnız uzunluğu değil bütün bedensel biçimi de koruduğu sürece kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"insanın boyu, beden yapısı veya görünüşü"}],"lexicalization_note":"Yalın biçimin boy, beden ve görünüş anlamı tanımlanır; özel bir yapı veya kalıptan gelen ek anlam alınmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; boy ve beden ölçüsünü doğrudan paylaşan komşu, yüz ve genel görünüş sınırıyla ayrıldığı için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kol yüz ve genel görünüşe kadar genişler; komşu kol boy ölçüsü, diklik ve doğrulma üzerinde yoğunlaşır.","focus_only":"Yüzü ve genel yaratılış görünüşünü de beden yapısına katar.","gloss":"boy ve beden yapısı","neighbor_only":"Komşu kol dik duruşu, bedenin doğrulmasını ve ölçülebilir uzunluğu daha belirgin biçimde içerir.","neighbor_ref":"root_001273/B011","relation_type":"near_synonym","shared_zone":"Her iki kol da insan boyunu ve bedenin uzunluk bakımından kuruluşunu anlatır."}],"source_phrase_ar":"الأمة القامة وطوال الأمم وبدنه ووجهه وما أحسن أمته أي خلقه (maqayis)؛ طوال الأمم يعني القامة والجسم (ayn)؛ الأمة قامة الإنسان والأمة الطول (jamhara)؛ الأمة القامة (sihah)","source_summary":"Kaynaklarda ortak çekirdek insanın boyu veya boy ölçüsüdür; beden, yüz ve güzel yaratılış görünüşü kaynak kümesinde ek kapsamlar olarak tanıklanır.","sources":["MQ","AY","JA","SI"],"what_is_ar":"يدخل فيه الأمة بمعنى القامة والطول، وبدن الرجل ووجهه، وحسن الخلق أو الهيئة.","what_is_not_ar":"لا يدخل فيه الجماعة أو الدين، ولا الأم الوالدة."},"support_links":[]},{"boundary":"Çekirdek okuma ve yazma becerisinin bulunmamasıdır; doğal yaratılış ve topluluk bağı yalnız açıklayıcı köken görüşleridir.","branch_kind":"bare","branch_ref":"root_000053/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أُمّ","morph_features":"STEM|POS:N|LEM:>um~|ROOT:Amm|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:1:2","qac_word_ref":"101:9:1","surface_ar":"أُمُّ"}],"gloss":"okuma yazma bilmeyen","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin yazamaması ve yazılı bir metni okuyamaması belirleyici niteliktir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Nitelik doğal başlangıç hâli, yazı kullanmayan topluluk veya bir kent adına bağlanan farklı köken açıklamalarıyla yorumlanır."}}],"root_ar":"ء م م","root_id":"root_000053","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin yazamadığı ve yazılı metni okuyamadığı açıkça kastedildiğinde tam karşılıktır.","boundary_detail":"Çekirdek okuma ve yazma becerisinin bulunmamasıdır; doğal yaratılış ve topluluk bağı yalnız açıklayıcı köken görüşleridir.","branch_image_ar":"الأمي على الجبلة غير الكاتب","concept_gloss":"okuma yazma bilmeyen","contextual_glosses":[{"applicability":"Yazılı metni okuyup yazamayan kişiyi yansız biçimde belirtir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Okuma ve yazma yeterliğinin yokluğunu birlikte korur."},"facet_ids":["F001"],"text":"okuryazar olmayan","usage_role":"general"}],"definition":"Yazamayan ve yazılı bir metni okuyamayan kişidir. Bu nitelik insanların öğrenim öncesi doğal hâline veya yazı kullanmayan bir topluluğa bağlanmış, ayrıca bir kent adına dayandırılan ayrı bir açıklama da aktarılmıştır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin yazamaması ve yazılı bir metni okuyamaması belirleyici niteliktir."},{"facet_id":"F002","role":"source_variant","statement":"Nitelik doğal başlangıç hâli, yazı kullanmayan topluluk veya bir kent adına bağlanan farklı köken açıklamalarıyla yorumlanır."}],"identity_rationale":"Kaynak sözü çekirdeği yazamayan ve bir kitaptan okuyamayan kişi olarak verir; bunu insanların ilk yaratılış hâline, yazı kullanmayan bir topluluğa veya bir kent adına bağlayan farklı açıklamalar da sunar. Dal kimliği okuryazarlık yokluğu üzerinden kurulmalı, köken açıklamalarından biri tek doğru anlam gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"okuma yazma bilmeyen kişi"}],"lexicalization_note":"Yalın kişi niteliği olarak okuryazarlık yokluğu tanımlanır; farklı köken açıklamaları çekirdeğin yerine geçirilmez.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; en yararlı sınır, okuryazarlık yokluğunu doğrudan okuma eyleminden ayıran karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak kol bir beceri yokluğunu kişiye yükler; komşu kol ise okuma ve okutma eylemlerini, dolayısıyla becerinin kullanımını anlatır.","focus_only":"Okuma ve yazma becerisinin kişide bulunmamasını bir nitelik olarak bildirir.","gloss":"okuryazarlık yokluğu ve okuma","neighbor_only":"Komşu kol metni seslendirme, okuma, başkasına okutma ve okuyarak öğrenme eylemlerini kapsar.","neighbor_ref":"root_001211/B001","relation_type":"same_field","shared_zone":"Her iki kol da yazılı metinle ilişki ve okuma yeterliği alanında yer alır."}],"source_phrase_ar":"الأمي في اللغة المنسوب إلى ما عليه جبلة الناس لا يكتب (maqayis)؛ الأمي هو الذي لا يكتب ولا يقرأ من كتاب وقيل منسوب إلى الأمة الذين لم يكتبوا وقيل لنسبته إلى أم القرى (mufradat)","source_summary":"Kaynaklarda ortak çekirdek yazamamadır; yazılı metni okuyamama ile doğal hâl, yazısız topluluk ve kent adı köken açıklamaları kaynak kümesinde ayrı tanıklıklar olarak yer alır.","sources":["MQ","MU"],"what_is_ar":"يدخل فيه الأمي المنسوب إلى ما عليه جبلة الناس أو إلى أمة لا تكتب، أي من لا يكتب ولا يقرأ من كتاب، مع ذكر احتمال النسبة إلى أم القرى.","what_is_not_ar":"لا يدخل فيه الأمة بمعنى جماعة مطلقا، ولا الأم الوالدة إلا من جهة أصل النسبة اللغوية."},"support_links":[]},{"boundary":"Çekirdek belirli olmayan bir zaman süresidir; insan topluluğu veya inanç düzeni yalnız bir kaynak yorumunda süreyi açıklayan arka plandır.","branch_kind":"bare","branch_ref":"root_000053/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أُمّ","morph_features":"STEM|POS:N|LEM:>um~|ROOT:Amm|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:1:2","qac_word_ref":"101:9:1","surface_ar":"أُمُّ"}],"gloss":"bir süre, zaman dilimi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirsiz uzunlukta geçen zaman veya araya giren süre temel anlamdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sürenin bir çağın insanlarının veya bir inanç çevresinin sona ermesiyle açıklanması kaynak yorumudur."}}],"root_ar":"ء م م","root_id":"root_000053","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Uzunluğu açıkça belirlenmeyen bir zaman aralığı veya dönem kastedildiğinde uygundur.","boundary_detail":"Çekirdek belirli olmayan bir zaman süresidir; insan topluluğu veya inanç düzeni yalnız bir kaynak yorumunda süreyi açıklayan arka plandır.","branch_image_ar":"الأمة حينا وزمانا","concept_gloss":"bir süre, zaman dilimi","contextual_glosses":[{"applicability":"Bir olayın belirsiz bir zaman aralığından sonra gerçekleştiği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Araya giren belirsiz sürenin ardından gerçekleşme ilişkisini korur."},"facet_ids":["F001"],"text":"bir süre sonra","usage_role":"contextual"}],"definition":"Geçen veya araya giren belirsiz bir zaman süresi, bir dönemdir. Bu süre kimi açıklamada bir çağın insanlarının ya da bir inanç çevresinin sona ermesiyle belirginleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirsiz uzunlukta geçen zaman veya araya giren süre temel anlamdır."},{"facet_id":"F002","role":"source_variant","statement":"Sürenin bir çağın insanlarının veya bir inanç çevresinin sona ermesiyle açıklanması kaynak yorumudur."}],"identity_rationale":"Kaynak sözü yalın anlamı bir süre veya zaman dilimi olarak verir. Bir açıklama bu süreyi bir çağın insanlarının ya da bir inanç çevresinin sona ermesi üzerinden yorumladığı için dal zaman anlamında korunmalı, bu yorum çekirdeğin zorunlu parçası yapılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"bir süre veya zaman dilimi"}],"lexicalization_note":"Yalın zaman süresi anlamı tanımlanır; topluluk veya inanç anlamı doğrudan bu dala karıştırılmaz.","neighbor_coverage_note":"Bütün zaman adayları değerlendirildi; hem süre hem zaman bildiren komşu, kapsam farkını en açık biçimde gösterdiği için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kol, komşunun süre anlamıyla örtüşür; komşu kol ayrıca zaman noktasını, yakın veya gerçekleşmiş zamanı ve ek zaman kullanımlarını kapsar.","focus_only":null,"gloss":"süre ve zaman","neighbor_only":"Komşu kol hem zaman noktasını hem süreyi, yakın veya gerçekleşmiş zamanı ve çeşitli zaman çoğullarını kapsar.","neighbor_ref":"root_000382/B001","relation_type":"near_synonym","shared_zone":"Her iki kol da belirsiz bir zaman aralığını veya dönemi anlatabilir."}],"source_phrase_ar":"الأمة في قوله وادكر بعد أمة أي بعد حين (maqayis)؛ الأمة الحين (sihah)؛ وادكر بعد أمة أي حين وحقيقة ذلك بعد انقضاء أهل عصر أو أهل دين (mufradat)","source_summary":"Kaynaklar bir süre geçtikten sonra anlamında birleşir; ek yorum, sürenin bir çağ veya inanç çevresinin sona ermesiyle kavranabileceğini belirtir.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه الأمة بمعنى الحين أو المدة أو الزمن المؤخر.","what_is_not_ar":"لا يدخل فيه جماعة الناس أو الدين إلا إذا صرح المصدر بأن الزمن مفهوم من انقضاء أهل عصر أو دين."},"support_links":[]},{"boundary":"Belirleyici ilişki önde bulunmak ve başkalarınca izlenmektir; salt bir hedefe yönelmek bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000053/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أُمّ","morph_features":"STEM|POS:N|LEM:>um~|ROOT:Amm|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:1:2","qac_word_ref":"101:9:1","surface_ar":"أُمُّ"}],"gloss":"öne konulan ve izlenen kılavuz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Öne konulma ve başkalarınca izlenme, insan ve insan dışı kılavuzları birleştiren çekirdektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir topluluğun veya toplu tapınmanın önüne geçerek yönetmek kişisel önderlik uygulamasıdır."}}],"root_ar":"ء م م","root_id":"root_000053","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi, metin, yol veya çizgi başkalarına yön verip izleniyorsa çekirdeğin tamamını karşılar.","boundary_detail":"Belirleyici ilişki önde bulunmak ve başkalarınca izlenmektir; salt bir hedefe yönelmek bu dala girmez.","branch_image_ar":"الإمام ومن يقتدى به","concept_gloss":"öne konulan ve izlenen kılavuz","contextual_glosses":[{"applicability":"İnsanların önüne geçip davranış veya düzen bakımından izlenen kişi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kitap, yol ve yapı çizgisi gibi insan dışı kılavuzları kapsamaz.","preserves":"Kişisel öne geçme ve izlenme ilişkisini korur."},"facet_ids":["F001","F002"],"text":"önder","usage_role":"general"},{"applicability":"Metin, yol veya ölçü çizgisi gibi insan dışı bir şey izleniyorsa kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan dışı bir dayanağın öne konulup izlenmesi ilişkisini korur."},"facet_ids":["F001"],"text":"yol gösterici","usage_role":"contextual"}],"definition":"İnsan, kitap, yol veya yapı doğrultusu olsun, öne konulan ve başkalarının kendisini izlediği kılavuzdur. Bir topluluğun önüne geçip onu yönetmek bu ilişkinin kişisel uygulamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Öne konulma ve başkalarınca izlenme, insan ve insan dışı kılavuzları birleştiren çekirdektir."},{"facet_id":"F002","role":"specialization","statement":"Bir topluluğun veya toplu tapınmanın önüne geçerek yönetmek kişisel önderlik uygulamasıdır."}],"identity_rationale":"Kaynak sözü öne geçirilip izlenen insanı, kitabı, yolu ve yapı doğrultusunu aynı izlenme ilişkisi altında toplar; toplu tapınmada öne geçmeyi de bu çekirdeğe bağlar. Dalın önder ve kendisine uyulan örnek çerçevesi bu geniş katılımcı yapısını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"önder veya izlenen kılavuz"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"birlikte kılınan namazda öne geçip önderlik etmek"}],"lexicalization_note":"Genel olarak izlenen kişi veya şey tanımlanır; toplu tapınmada öne geçme yalnız kendi bağlı kullanımında tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; izlenme çekirdeğini en yakından paylaşan örnek olma kolu, yön ve katılımcı farkını göstermek için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kol izlenen varlığı önde duran kılavuz olarak adlandırır; komşu kol ise izleyenin örnek alma ve benzeme tutumunu öne çıkarır.","focus_only":"İnsan dışında kitap, yol ve yapı doğrultusu gibi izlenen kılavuzları da kapsar.","gloss":"önder ve örnek","neighbor_only":"Komşu kol daha çok bir kişinin durumunu veya davranışını örnek alıp ona benzemeyi anlatır.","neighbor_ref":"root_000034/B003","relation_type":"near_synonym","shared_zone":"Her iki kol da başkasını izleme ve kendine örnek alma ilişkisini içerir."}],"source_phrase_ar":"الإمام كل من اقتدي به وقدم في الأمور والخيط الذي يقوم عليه البناء إمام (maqayis)؛ كل من اقتدي به وقدم في الأمور فهو إمام والإمام الطريق (ayn)؛ إن إبراهيم كان أمة أي إماما ورئيس القوم أما لهم (jamhara)؛ أممت القوم في الصلاة إمامة والإمام الذي يقتدى به والإمام الطريق (sihah)؛ الإمام المؤتم به إنسانا أو كتابا أو غير ذلك (mufradat)","source_summary":"Kaynaklar öne geçirilen ve izlenen kişi veya şeyi ortak çekirdek sayar; insan önder, kitap, yol ve yapı doğrultusu bu ilişkinin farklı taşıyıcılarıdır. Tek bir önderin bir topluluk yerine geçebildiğini gösteren bir örnek de verilir.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الإمام وكل من اقتدي به أو قدم في الأمور، إمام الصلاة والرعية والكتاب والطريق والخيط أو الخشبة التي يقام عليها البناء، ومن قام مقام جماعة كإبراهيم أمة.","what_is_not_ar":"لا يدخل فيه القصد المجرد إلى مكان، ولا الأم الوالدة، ولا الأمة بمعنى جماعة فقط."},"support_links":[]},{"boundary":"Bu dal iyi durum ve bağışlanmış iyilikle sınırlıdır; inanç yolu ve topluluk anlamları buraya girmez.","branch_kind":"bare","branch_ref":"root_000053/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أُمّ","morph_features":"STEM|POS:N|LEM:>um~|ROOT:Amm|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:1:2","qac_word_ref":"101:9:1","surface_ar":"أُمُّ"}],"gloss":"iyilik ve iyi durum","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ulaşılan iyilik ve iyi durumda bulunma bu dalın çekirdeğidir."}}],"root_ar":"ء م م","root_id":"root_000053","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiye ulaşan iyilik veya elverişli yaşam durumu anlatıldığında uygundur.","boundary_detail":"Bu dal iyi durum ve bağışlanmış iyilikle sınırlıdır; inanç yolu ve topluluk anlamları buraya girmez.","branch_image_ar":"الإمة نعمة","concept_gloss":"iyilik ve iyi durum","contextual_glosses":[{"applicability":"Kişiye ulaşan yararlı ve iyi şey öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Süreklilik taşıyan iyi yaşam durumunu tek başına belirtmez.","preserves":"Kişiye ulaşan yararlı ve iyi şeyi korur."},"facet_ids":["F001"],"text":"iyilik","usage_role":"general"}],"definition":"Kişiye ulaşan iyilik, bolluk veya içinde bulunulan iyi ve elverişli durumdur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ulaşılan iyilik ve iyi durumda bulunma bu dalın çekirdeğidir."}],"identity_rationale":"Kaynak sözü bu biçimi doğrudan iyilik, bağışlanmış iyi durum veya esenlik anlamında verir. Dalın iyilik ve iyi durum çerçevesi kaynak kapsamını taşır ve aynı yazılışın inanç yolu anlamından ayrıdır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"iyilik, bolluk veya iyi durum"}],"lexicalization_note":"Yalın biçimin iyilik ve iyi durum anlamı korunur; benzer yazılan inanç yolu anlamıyla birleştirilmez.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; iyi durum ve kişiye ulaşan iyilik çekirdeğini en geniş biçimde paylaşan komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kol kısa bir iyilik ve iyi durum adıdır; komşu kol bağışlama, yarar ulaştırma ve rahat yaşam gibi daha geniş ilişki ve eylemleri içerir.","focus_only":null,"gloss":"iyilik ve esenlik","neighbor_only":"Komşu kol iyi durum yanında güzel yaşamı, bağışı, başkasına yarar ulaştırmayı ve iyilikte bulunma eylemini kapsar.","neighbor_ref":"root_001525/B001","relation_type":"near_synonym","shared_zone":"Her iki kol da iyi durum, bolluk ve kişiye ulaşan yararı anlatır."}],"source_phrase_ar":"الأمة النعمة (maqayis)؛ الإمة النعمة (ayn)؛ الإمة النعمة (jamhara)؛ الإمة بالكسر النعمة (sihah)","source_summary":"Kaynaklar biçimi iyilik ve iyi durum anlamında ortaklaşa tanımlar; başka dallardaki benzer yazılışlar bu anlamı değiştirmez.","sources":["MQ","AY","JA","SI"],"what_is_ar":"يدخل فيه الإمة بالكسر بمعنى النعمة والحال الحسنة.","what_is_not_ar":"لا يدخل فيه الأمة بمعنى الدين وإن وافقها الرسم في بعض المصادر."},"support_links":[]},{"boundary":"Anlam mekânsal ön ve göreli yakınlıkla sınırlıdır; bilinçli olarak bir hedefe yönelme ayrı daldır.","branch_kind":"bare","branch_ref":"root_000053/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أُمّ","morph_features":"STEM|POS:N|LEM:>um~|ROOT:Amm|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:1:2","qac_word_ref":"101:9:1","surface_ar":"أُمُّ"}],"gloss":"ön taraf ve yakın konum","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığın önünde veya ileride bulunan mekânsal konum temel anlamdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yakın, erişilebilir veya yakınla uzak arasında bulunan konum, ön alanından gelişen kapsamdır."}}],"root_ar":"ء م م","root_id":"root_000053","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin önü ile erişilebilir yakınlıktaki yer birlikte kapsanmak istendiğinde uygundur.","boundary_detail":"Anlam mekânsal ön ve göreli yakınlıkla sınırlıdır; bilinçli olarak bir hedefe yönelme ayrı daldır.","branch_image_ar":"الأمام قدام وقربا","concept_gloss":"ön taraf ve yakın konum","contextual_glosses":[{"applicability":"Bir varlığın ön tarafındaki yeri belirtmek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir varlığa göre ön tarafta bulunma ilişkisini korur."},"facet_ids":["F001"],"text":"önünde","usage_role":"general"},{"applicability":"Konumun erişilebilir veya uzak olmayan oluşu öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Göreli yakınlık ve kolay erişilebilirlik yönünü korur."},"facet_ids":["F002"],"text":"yakında","usage_role":"contextual"}],"definition":"Bir kişi veya şeyin ön tarafı, ilerisi ya da önünde bulunan yerdir. Ayrıca yakın, erişilebilir veya yakınla uzak arasında sayılan bir konumu anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığın önünde veya ileride bulunan mekânsal konum temel anlamdır."},{"facet_id":"F002","role":"extension","statement":"Yakın, erişilebilir veya yakınla uzak arasında bulunan konum, ön alanından gelişen kapsamdır."}],"identity_rationale":"Kaynak sözü bir şeyin önünde bulunmayı temel alır ve buna yakın, erişilebilir veya yakınla uzak arası konumu ekler. Dalın ön taraf ve yakınlık çerçevesi bu iki mekânsal yönü birbirine karıştırmadan koruyabilir.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"ön, ön taraf veya ilerisi"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"yakın, erişilebilir veya orta uzaklıkta olan"}],"lexicalization_note":"Yalın mekânsal ön ve yakınlık anlamları tanımlanır; hedef seçme ve yönelme eylemi içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ön konumu doğrudan paylaşan komşu, zaman ve yakınlık kapsamlarındaki ayrımı en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kol mekânsal yakınlığı ayrı bir uzantı olarak taşır; komşu kol ön konumu yaklaşan zaman ve öncelik ilişkisine de genişletir.","focus_only":"Ön konum yanında erişilebilir yakınlığı ve yakınla uzak arasındaki mesafeyi de kapsar.","gloss":"ön ve yakın","neighbor_only":"Komşu kol ön konumu zamansal olarak yaklaşan olay veya hemen önceki durum için de kullanır.","neighbor_ref":"root_001693/B008","relation_type":"near_synonym","shared_zone":"Her iki kol da bir şeyin önünde veya ondan ileride bulunan konumu anlatır."}],"source_phrase_ar":"الأمام القدام وامض يمامي في معنى امض أمامي والأمم الشيء القريب المتناول (maqayis)؛ الأمام بمنزلة القدام والأمم الشيء القريب (ayn)؛ سرت أمام الرجل وأمامته ويمامته (jamhara)؛ كنت أمامه أي قدامه والأمم بين القريب والبعيد وأخذت ذلك من أمم أي من قرب (sihah)","source_summary":"Kaynaklar ön taraf ve ileride bulunma anlamında birleşir; yakın, erişilebilir ve orta uzaklıktaki konum bu mekânsal alanı genişletir.","sources":["MQ","AY","JA","SI"],"what_is_ar":"يدخل فيه أمام بمعنى قدام، وأمام الرجل وأمامته ويمامته، والأمم بمعنى القريب أو المقارب أو المقابل.","what_is_not_ar":"لا يدخل فيه القصد والتوجه إلى مقصد إلا إذا كان المعنى موضعيا أماميا."},"support_links":[]},{"boundary":"Salt önde bulunma veya yön bildirme yeterli değildir; seçilmiş bir hedefe bilinçli yönelme gerekir.","branch_kind":"mixed_non_bare","branch_ref":"root_000053/B012","candidate_links":[{"candidate_id":"cand_f21f98910b05ab991010","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أُمّ","morph_features":"STEM|POS:N|LEM:>um~|ROOT:Amm|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:1:2","qac_word_ref":"101:9:1","surface_ar":"أُمُّ"}],"gloss":"amaçlayıp yönelmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Seçilmiş bir hedefi amaç edinip ona doğru yönelmek temel eylemdir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyi özellikle seçmek, gözetmek ve bilerek istemek amaçlı yönelmenin irade yönüdür."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kutsal eve yönelen kişiler, belirli bir hedefe doğru gitme eyleminin örneğidir."}}],"root_ar":"ء م م","root_id":"root_000053","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir hedef hem bilinçli olarak seçiliyor hem de ona doğru hareket veya yöneliş gerçekleşiyorsa tam karşılıktır.","boundary_detail":"Salt önde bulunma veya yön bildirme yeterli değildir; seçilmiş bir hedefe bilinçli yönelme gerekir.","branch_image_ar":"القصد والتوجه والتيمم","concept_gloss":"amaçlayıp yönelmek","contextual_glosses":[{"applicability":"Hedefin bağlamda açık olduğu ve bilinçli seçimin zaten bilindiği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hedefi özellikle seçme ve amaç edinme bileşenini tek başına açık etmez.","preserves":"Seçilen hedefe doğru gitme veya doğrultu değiştirme yönünü korur."},"facet_ids":["F001"],"text":"yönelmek","usage_role":"general"},{"applicability":"Eylemin iradeli seçim ve amaç edinme yönü açıklanmak istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilinçli seçimi, amaç edinmeyi ve hedefe yönelmeyi birlikte korur."},"facet_ids":["F001","F002"],"text":"bilerek seçip hedeflemek","usage_role":"explanatory"}],"definition":"Bir şeyi bilinçli olarak hedef seçmek, onu amaçlamak ve doğruca ona yönelmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Seçilmiş bir hedefi amaç edinip ona doğru yönelmek temel eylemdir."},{"facet_id":"F002","role":"specialization","statement":"Bir şeyi özellikle seçmek, gözetmek ve bilerek istemek amaçlı yönelmenin irade yönüdür."},{"facet_id":"F003","role":"example","statement":"Kutsal eve yönelen kişiler, belirli bir hedefe doğru gitme eyleminin örneğidir."}],"identity_rationale":"Kaynak sözü bir şeyi amaç edinip ona doğru yönelmeyi, onu bilerek seçmeyi ve doğruca hedefe gitmeyi aynı eylem yapısında birleştirir. Dalın amaçlı yönelme çerçevesi, hem niyeti hem yön değişimini koruduğu için kaynağa uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bir şeyi amaçlayıp ona yönelmek"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bir şeyi bilerek seçmek ve hedeflemek"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"kutsal eve yönelenler"}],"lexicalization_note":"Genel amaçlı yönelme tanımlanır; belirli kutsal hedefe yönelenleri bildiren kullanım yalnız kendi bağlı yapısında tutulur.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; hedef seçme, bilinçli isteme ve yönelmeyi aynı sınırlarla veren komşu tam eş anlamlı olarak yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek işlem, katılımcılar ve amaçlılık sınırı aynıdır; verilen özel örnekler bu tam örtüşmeyi bozmaz.","focus_only":null,"gloss":"bilerek hedefleyip yönelmek","neighbor_only":null,"neighbor_ref":"root_001697/B001","relation_type":"synonym","shared_zone":"Her iki kol da bir şeyi bilinçli hedef seçme ve ona doğru yönelme çekirdeğini taşır."}],"source_phrase_ar":"الأمم القصد وآمين البيت الحرام أي يقصدونه والتيمم يجري مجرى التوخي أي تعمدوا (maqayis)؛ أم يؤم أما إذا قصد للشيء (jamhara)؛ الأم بالفتح القصد أمة وأممه وتأممه إذا قصده (sihah)؛ الأم القصد المستقيم وهو التوجه نحو مقصود (mufradat)","source_summary":"Kaynaklar hedef seçme, bilinçli isteme ve seçilen hedefe doğru yönelme aşamalarını tek bir amaçlı hareket çekirdeğinde birleştirir.","sources":["MQ","JA","SI","MU"],"what_is_ar":"يدخل فيه أم يؤم إذا قصد، والأم أو الأمم بمعنى القصد، وآمين البيت الحرام، والتيمم بمعنى التوخي والتعمد، وتوجيه السهم أو الرمح إلى مقصود.","what_is_not_ar":"لا يدخل فيه الأمام بمعنى قدام إذا خلا من قصد، ولا الإمامة بمعنى الاقتداء."},"support_links":["sup_8214ecc5a71b35d0b2d4"]},{"boundary":"Temel anlam azlık, küçüklük ve önemsizliktir; büyük anlamı yalnız kaydedilmiş karşıt varyanttır, mekânsal yakınlık ise ayrı daldır.","branch_kind":"bare","branch_ref":"root_000053/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أُمّ","morph_features":"STEM|POS:N|LEM:>um~|ROOT:Amm|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:1:2","qac_word_ref":"101:9:1","surface_ar":"أُمُّ"}],"gloss":"az, küçük veya önemsiz şey","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Azlık, küçüklük, kolaylık ve önemsizlik ortak değerlendirme çekirdeğini oluşturur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı biçimin büyük anlamında kullanılması, çekirdeğe karşıt sınırlı bir kaynak varyantıdır."}}],"root_ar":"ء م م","root_id":"root_000053","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şey miktar, boyut, güçlük veya değer bakımından düşük sayıldığında çekirdeği karşılar.","boundary_detail":"Temel anlam azlık, küçüklük ve önemsizliktir; büyük anlamı yalnız kaydedilmiş karşıt varyanttır, mekânsal yakınlık ise ayrı daldır.","branch_image_ar":"الأمم اليسير الحقير","concept_gloss":"az, küçük veya önemsiz şey","contextual_glosses":[{"applicability":"Düşük değer veya dikkate alınmayacak ölçü öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Salt miktar azlığını veya kolaylığı her bağlamda açıkça göstermez.","preserves":"Değersizlik ve dikkate alınmayacak küçüklük yönünü korur."},"facet_ids":["F001"],"text":"önemsiz bir şey","usage_role":"general"}],"definition":"Miktarı veya değeri az, küçük, kolay ya da önemsiz sayılan şeydir. Bir aktarımda aynı biçimin karşıt olarak büyük anlamına da geldiği belirtilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Azlık, küçüklük, kolaylık ve önemsizlik ortak değerlendirme çekirdeğini oluşturur."},{"facet_id":"F002","role":"source_variant","statement":"Aynı biçimin büyük anlamında kullanılması, çekirdeğe karşıt sınırlı bir kaynak varyantıdır."}],"identity_rationale":"Kaynak sözü ortak çekirdeği az, küçük, kolay veya değersiz şey olarak verir; aynı biçimin bir aktarımda karşıt biçimde büyük anlamına da gelebileceğini kaydeder. Dal küçük ve önemsiz çekirdeğiyle korunmalı, karşıt büyük anlamı düzenli çekirdeğe değil kaynak varyantına yerleştirilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"az, küçük ya da değersiz şey"}],"lexicalization_note":"Yalın biçimin az, küçük ve değersiz şey anlamı tanımlanır; karşıt büyük anlamı yalnız sınırlı kaynak varyantı olarak tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; azlık ile değersizliği birlikte taşıyan komşu, kaynak varyantı ve nitelik farkını göstermek için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kol kolaylığı da çekirdek kapsama alır; komşu kol düşük nitelik ve yetersizlik değerlendirmesine daha güçlü biçimde açılır.","focus_only":"Azlık ve önemsizliğin yanında kolaylık yönünü de açıkça kapsar.","gloss":"az ve önemsiz","neighbor_only":"Komşu kol azlık yanında düşük nitelik, bayağılık ve hesaba katılmayacak yetersizlik değerlendirmelerini daha açık taşır.","neighbor_ref":"root_000940/B001","relation_type":"near_synonym","shared_zone":"Her iki kol da az, küçük, değersiz veya dikkate alınmayacak şeyi anlatır."}],"source_phrase_ar":"الأمم الشيء اليسير الحقير وأمم أي صغير وعظيم من الأضداد (maqayis)؛ الأمم الشيء اليسر الهين الحقير (ayn)؛ الامم الشئ اليسير يقال ما سألت إلا أمما (sihah)","source_summary":"Kaynak kümesinde azlık, küçüklük, kolaylık ve değersizlik yönleri tanıklanır; büyük anlamı ise tekil ve karşıt bir kaynak aktarımı olarak ayrı durur.","sources":["MQ","AY","SI"],"what_is_ar":"يدخل فيه الأمم بمعنى الشيء اليسير أو الهين أو الحقير، وما قيل فيه من الصغر وربما التضاد مع العظيم.","what_is_not_ar":"لا يدخل فيه القرب المكاني، ولا القامة."},"support_links":[]},{"boundary":"Dal genç kadın köleye yönelik kişi adıyla sınırlıdır; topluluk, din ve zaman anlamları dışarıda kalır.","branch_kind":"bare","branch_ref":"root_000053/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أُمّ","morph_features":"STEM|POS:N|LEM:>um~|ROOT:Amm|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:1:2","qac_word_ref":"101:9:1","surface_ar":"أُمُّ"}],"gloss":"genç kız veya kadın köle","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadın köle olma, kişi adının çekirdek sınırıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Genç kız karşılığı, çekirdekle zorunlu birleşmeyen alternatif bir kaynak eşdeğeridir."}}],"root_ar":"ء م م","root_id":"root_000053","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genç kız ya da kadın köle kastedildiğinde, iki kapsamı zorunlu olarak birleştirmeden karşılar.","boundary_detail":"Dal genç kadın köleye yönelik kişi adıyla sınırlıdır; topluluk, din ve zaman anlamları dışarıda kalır.","branch_image_ar":"الأمة الوليدة","concept_gloss":"genç kız veya kadın köle","contextual_glosses":[{"applicability":"Yaşın bağlamdan bilindiği veya gençlik ayrımının önemli olmadığı yerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gençlik veya yeni yetişmişlik yönünü açıkça belirtmez.","preserves":"Kadın olma ve köle durumunda bulunma özelliklerini korur."},"facet_ids":["F001"],"text":"kadın köle","usage_role":"general"}],"definition":"Kadın köle için kullanılan addır. Genç kız karşılığı ise kölelikle zorunlu olarak birleşmeyen alternatif bir kaynak eşdeğeridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadın köle olma, kişi adının çekirdek sınırıdır."},{"facet_id":"F002","role":"source_variant","statement":"Genç kız karşılığı, çekirdekle zorunlu birleşmeyen alternatif bir kaynak eşdeğeridir."}],"identity_rationale":"Kaynak sözü tek başına genç kadın veya kadın köle için kullanılan adı verir ve dal çerçevesi bunu doğrudan korur. Topluluk, inanç ve zaman anlamlarıyla biçim benzerliği bu kişi anlamını değiştirmez.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"genç kız veya kadın köle"}],"lexicalization_note":"Yalın kişi adı genç kadın köle anlamında tanımlanır; aynı yazılışın başka dallardaki soyut anlamları içeri alınmaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; kadın köle anlamını doğrudan paylaşan komşu, yaş kapsamındaki ayrımı göstermek için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kol kadın köle alanıyla örtüşür, ancak genç kız karşılığını da seçenekli olarak taşır; komşu kol kadın köle alanıyla sınırlıdır.","focus_only":"Kölelikle zorunlu birleşmeyen genç kız kapsamını da taşır.","gloss":"kadın köle","neighbor_only":null,"neighbor_ref":"root_000056/B001","relation_type":"near_synonym","shared_zone":"Her iki kol da kadın köle için kullanılan kişi adını aynı çekirdekle verir."}],"source_phrase_ar":"الأمة الوليدة (jamhara)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, biçimi genç kadın veya kadın köle için kullanılan ad olarak açıklar."}],"source_summary":"Ortak kaynak özeti yoktur; bu kişi anlamı tek bir sözlük tanıklığıyla sınırlı olarak verilmiştir.","sources":["JA"],"what_is_ar":"يدخل فيه الأمة بمعنى الوليدة.","what_is_not_ar":"لا يدخل فيه الأمة بمعنى الجماعة أو الدين أو الحين."},"support_links":[]},{"boundary":"Kusurun taşıyıcısı insandır; belirli baş yarası, genel nesne kusuru ve biçim bozukluğu ayrıca kanıtlanmadıkça bu dala girmez.","branch_kind":"bare","branch_ref":"root_000053/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أُمّ","morph_features":"STEM|POS:N|LEM:>um~|ROOT:Amm|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:1:2","qac_word_ref":"101:9:1","surface_ar":"أُمُّ"}],"gloss":"insandaki kusur","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsana yüklenen kusur veya eksiklik bu dalın bütün çekirdeğini oluşturur."}}],"root_ar":"ء م م","root_id":"root_000053","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişide bulunan eksiklik veya ayıp adlandırıldığında tam karşılıktır.","boundary_detail":"Kusurun taşıyıcısı insandır; belirli baş yarası, genel nesne kusuru ve biçim bozukluğu ayrıca kanıtlanmadıkça bu dala girmez.","branch_image_ar":"الأمة أو الآمة عيبا","concept_gloss":"insandaki kusur","contextual_glosses":[{"applicability":"Taşıyıcının insan olduğu bağlamda kısa ve doğal karşılıktır.","error_profile":{"adds":"Tek başına kullanıldığında insan dışındaki nesne ve durumların kusurlarını da kapsayabilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Eksiklik ve olumsuz değerlendirme çekirdeğini korur."},"facet_ids":["F001"],"text":"kusur","usage_role":"general"}],"definition":"Bir insanda bulunan ayıp, eksiklik veya kusurdur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsana yüklenen kusur veya eksiklik bu dalın bütün çekirdeğini oluşturur."}],"identity_rationale":"Kaynak sözü biçimi doğrudan insandaki kusur olarak tanımlar. Dalın insan kusuru çerçevesi bu sınırlı anlamı doğru taşır ve beyne ulaşan baş yarasıyla yalnız biçim benzerliği gösterir.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"insandaki kusur veya ayıp"}],"lexicalization_note":"Yalın biçimin insandaki kusur anlamı korunur; ağır baş yarası bildiren benzer biçim bu tanıma katılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel kusur alanını ve türeyen eylemleri kapsayan komşu, insanla sınırlı odağı en açık biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kol insandaki kusurun adıyla sınırlıdır; komşu kol taşıyıcıyı genişletir ve kusurlu hâle gelme ya da kusur yükleme eylemlerini de içerir.","focus_only":"Kusuru yalnız insan taşıyıcıyla sınırlı bir ad olarak verir.","gloss":"insandaki kusur","neighbor_only":"Komşu kol her türlü şeyde kusurun bulunmasını, ortaya çıkmasını, kusurlu kılmayı ve sözle kusur yüklemeyi kapsar.","neighbor_ref":"root_001065/B001","relation_type":"near_synonym","shared_zone":"Her iki kol da bir eksikliği veya ayıbı kusur olarak değerlendirir."}],"source_phrase_ar":"الآمة العيب (ayn)؛ الأمة العيب في الإنسان (jamhara)","source_summary":"Kaynaklarda ortak çekirdek kusur veya ayıp anlamıdır; insanla sınırlama ayrıntısı kaynak kümesindeki özel bir kayıt olarak yer alır.","sources":["AY","JA"],"what_is_ar":"يدخل فيه الأمة أو الآمة بمعنى العيب في الإنسان.","what_is_not_ar":"لا يدخل فيه الشجة الآمة التي تبلغ أم الدماغ إلا إذا أريد بها الجرح لا العيب."},"support_links":[]},{"boundary":"Dal soru içindeki seçenek bağlama ve kopuk düzeltmeli soru işlevleriyle sınırlıdır; desteklenmeyen dolgu kullanımı dışarıda bırakılır.","branch_kind":"non_bare","branch_ref":"root_000053/B016","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أُمّ","morph_features":"STEM|POS:N|LEM:>um~|ROOT:Amm|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:1:2","qac_word_ref":"101:9:1","surface_ar":"أُمُّ"}],"gloss":"seçenek veya düzeltme bildiren soru bağlacı","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Soru içindeki iki seçeneği karşılaştırmalı biçimde bağlamak temel dilbilgisel işlevdir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Önceki sözden kopuk kullanım, karşıt düzeltme ile yeni bir soru anlamını birleştirir."}}],"root_ar":"ء م م","root_id":"root_000053","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki soru seçeneği bağlandığında veya önceki söz düzeltilip yeni soru açıldığında uygundur.","boundary_detail":"Dal soru içindeki seçenek bağlama ve kopuk düzeltmeli soru işlevleriyle sınırlıdır; desteklenmeyen dolgu kullanımı dışarıda bırakılır.","branch_image_ar":"أم حرف استفهام وإضراب","concept_gloss":"seçenek veya düzeltme bildiren soru bağlacı","contextual_glosses":[{"applicability":"Türkçede iki soru seçeneğini bağlarken veya düzeltmeli yeni soru açarken doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Seçenekleri karşılaştırma ve kopuk kullanımda yeni soru açma işlevlerini korur."},"facet_ids":["F001","F002"],"text":"yoksa","usage_role":"general"}],"definition":"Soru içinde iki seçeneği birbirine bağlayıp hangisinin geçerli olduğunu sorduran bağlaçtır. Önceki sözden kopuk kullanıldığında ise karşıt bir düzeltme yaparak yeni bir soru başlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Soru içindeki iki seçeneği karşılaştırmalı biçimde bağlamak temel dilbilgisel işlevdir."},{"facet_id":"F002","role":"specialization","statement":"Önceki sözden kopuk kullanım, karşıt düzeltme ile yeni bir soru anlamını birleştirir."}],"identity_rationale":"Kaynak sözü iki kullanımı destekler: soru seçeneklerini karşılaştıran bağlaç ve önceki sözden koparak karşıt düzeltme ile yeni soru başlatan kullanım. Geçici çerçevedeki dolgu sözcüğü olma iddiası kaynak sözünde yer almadığından tanımdan çıkarılmalı, dal yalnız bu iki işlevle yeniden çerçevelenmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"iki soru seçeneğini bağlayan veya düzeltmeli yeni soru açan \"yoksa\""}],"lexicalization_note":"Bu dilbilgisel dal yalnız soru yapısındaki seçenek bağlacı ve kopuk düzeltmeli soru kullanımına bağlıdır; yalın kök anlamı sayılmaz.","neighbor_coverage_note":"Bütün dilbilgisel adaylar değerlendirildi; düzeltme işlevini paylaşan bağlaç, soru ve seçenek koşulundaki temel sınırı göstermek için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak bağlaç soru yapısına bağlıdır ve seçenek sunar; komşu bağlaç genel düzeltme ve karşıt geçiş işlevi görür, soru kurması gerekmez.","focus_only":"Seçenekli soru kurar ve kopuk kullanımda düzeltmeyi yeni bir soruyla birleştirir.","gloss":"yoksa ve oysa","neighbor_only":"Komşu bağlaç soru gerektirmeden önceki sözü bırakıp düzeltme veya karşıt geçiş yapabilir.","neighbor_ref":"root_000152/B008","relation_type":"near_synonym","shared_zone":"Her iki bağlaç da önceki söylemden ayrılıp karşıt veya düzeltici bir devam kurabilir."}],"source_phrase_ar":"أم مخففة حرف عطف في الاستفهام تقع معادلة لألف الاستفهام بمعنى أي وتكون منقطعة (sihah)؛ أم إذا قوبل به ألف الاستفهام فمعناه أي وإذا جرد عن ذلك يقتضي معنى ألف الاستفهام مع بل (mufradat)","source_summary":"Kaynaklar seçenekli soruda karşılaştırmalı bağlama ile önceki sözden kopup karşıt düzeltmeli soru başlatma işlevlerini birlikte verir.","sources":["SI","MU"],"what_is_ar":"يدخل فيه أم المخففة حرفا يعادل همزة الاستفهام بمعنى أي، أو يأتي منقطعا بمعنى بل مع استفهام أو إضراب، وقد يذكر زائدا.","what_is_not_ar":"لا يدخل فيه أي اسم مشتق من الأم أو الأمة أو الإمام."},"support_links":[]},{"boundary":"Hava ve fiziksel boşluk çekirdektir; kalbin boşluğu ile yüreksizlik yalnız belirtilen kullanımlarda bu çekirdeğe bağlanır.","branch_kind":"mixed_non_bare","branch_ref":"root_001609/B001","candidate_links":[{"candidate_id":"cand_e5df16ecbc308492da67","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"هَاوِيَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:haAwiyap|ROOT:hwy|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:2:1","qac_word_ref":"101:9:2","surface_ar":"هَاوِيَةٌ"}],"gloss":"hava ve boşluk; kalpte boşluk ve yüreksizlik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yer ile gök arasındaki hava ya da iki şey arasında bulunan boş alan."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kalbin veya göğsün akıl, kavrayış ya da sebat bakımından boş olması."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yüreği zayıf ve korkak bir kişinin boşluk imgesiyle nitelenmesi."}}],"root_ar":"ه و ي","root_id":"root_001609","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel çekirdeği ve insanla ilgili iki açık uzantıyı birlikte temsil eden genel kavram karşılığıdır.","boundary_detail":"Hava ve fiziksel boşluk çekirdektir; kalbin boşluğu ile yüreksizlik yalnız belirtilen kullanımlarda bu çekirdeğe bağlanır.","branch_image_ar":"الهَواء والخلاء","concept_gloss":"hava ve boşluk; kalpte boşluk ve yüreksizlik","contextual_glosses":[{"applicability":"Yer ile gök arasındaki ortam veya iki şey arasındaki açık alan söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Fiziksel ortam ve boş alan çekirdeğini bağlama uygun biçimde korur."},"facet_ids":["F001"],"text":"hava ya da boşluk","usage_role":"general"},{"applicability":"Kalbin büyük korku karşısında anlayamaz ve kararlı duramaz oluşunu anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kalbin kavrayış ve sebat bakımından boş kalması anlamını korur."},"facet_ids":["F002"],"text":"aklı başından gitmiş, kavrayışsız","usage_role":"contextual"}],"definition":"Yer ile gök arasındaki hava ve iki şey arasındaki boş alanı anlatır. Belirli kullanımlarda kalbin akıl, kavrayış ya da sebattan yoksun kalmasını ve yüreği zayıf, korkak kişiyi de boşluk imgesiyle niteler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yer ile gök arasındaki hava ya da iki şey arasında bulunan boş alan."},{"facet_id":"F002","role":"extension","statement":"Kalbin veya göğsün akıl, kavrayış ya da sebat bakımından boş olması."},{"facet_id":"F003","role":"extension","statement":"Yüreği zayıf ve korkak bir kişinin boşluk imgesiyle nitelenmesi."}],"identity_rationale":"Kaynak ifadesi yer ile gök arasındaki havayı ve iki şey arasındaki boşluğu temel alır; kalbin kavrayış ve sebat bakımından boş kalmasını ve yüreksiz kişiyi de bu boşluk imgesine bağlı kullanımlar olarak açıkça verir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"hava; boşluk veya aralık"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kalpleri bomboş, kavrayışsız ve kararsızdır"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yüreksiz, korkak ya da akılsız kimse"}],"lexicalization_note":"Tanım yalın hava ve boşluk anlamını, kalp ve kişiyle kurulan kullanımlardan ayırır; bu bağlı kullanımlar bütün kola genellenmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; hava ve boşluk sınırını en iyi açıklayan üç yakın anlamlı dal seçildi, yalnız yazım benzerliği veya uzak tema ortaklığı taşıyanlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol fiziksel boşluğun yanında atmosferik havayı ve insanın iç durumuna aktarılan anlamları taşır; komşu ise yerin sakinlerinden boş olması ve genel boşluk üzerinde durur.","focus_only":"Atmosferik hava, kalbin boşluğu ve yüreksiz kişi uzantıları bu kolda bulunur.","gloss":"boşluk ve ıssızlık","neighbor_only":"Ev veya yerin sakinlerinden boşalması ve geniş açıklık anlamları komşuda ayrıca yer alır.","neighbor_ref":"root_000450/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir yerde ya da iki şey arasında doluluğun bulunmamasını anlatır."},{"boundary_match":"partial","distinction":"Ortak atmosfer anlamına rağmen bu kol boşluk kavramını iki şey arasındaki aralığa ve insani yoksunluğa genişletir; komşu göğün hava ortamıyla sınırlıdır.","focus_only":"Her tür boş aralık ile kalbe ve yüreksiz kişiye aktarılan kullanımlar bu kola özgüdür.","gloss":"gökyüzü havası","neighbor_only":"Göğü yeryüzünün üstünü çepeçevre saran bir ortam olarak ele alma komşuda belirgindir.","neighbor_ref":"root_000280/B001","relation_type":"near_synonym","shared_zone":"Her iki dal yer ile gök arasındaki hava ortamını doğrudan adlandırır."},{"boundary_match":"partial","distinction":"Bu kol hava ve aralık çekirdeğinden hareket eder; komşu ise çeşitli kap ve alanların içeriksizliğini, maddi yoksunluğu ve akıl yokluğunu daha geniş biçimde kapsar.","focus_only":"Yer ile gök arasındaki hava ve yüreksiz kişi nitelemesi yalnız bu kolda bulunur.","gloss":"boş ve yoksun olma","neighbor_only":"Kap, ev, el, hesap ve yoksulluk gibi yokluk alanları komşunun daha geniş kullanım alanıdır.","neighbor_ref":"root_000869/B002","relation_type":"near_synonym","shared_zone":"Her ikisi de nesnenin ya da zihnin beklenen içerikten yoksun olmasını ifade eder."}],"source_phrase_ar":"الهَواء ممدود هو الجو (ayn)؛ قلبه هَواء (ayn)؛ هَواء الجو ممدود (jamhara)؛ الهَواء ما بين السماء والأرض وكل خال هواء (sihah)؛ الهَواء والخواء واحد (tahdhib)؛ الهَواء كل فرجة بين شيئين (tahdhib)؛ هوى صدره أي خلا (tahdhib)؛ الهوهاءة الضعيف الفؤاد الجبان (tahdhib)؛ الهَواء ما بين الأرض والسماء (mufradat)؛ أصل صحيح يدل على خلو وسقوط (maqayis)؛ أصله الهَواء بين الأرض والسماء سمي لخلوه (maqayis)","source_summary":"Kaynakların ortak çerçevesinde fiziksel hava ve boşluk temel anlamdır; kalbin kavrayışsız ya da kararsız oluşu ile kişinin yüreksizliği bu temel anlamın insana aktarılan uzantılarıdır.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الهَواء بين السماء والأرض، وكل خال، وخلو القلب أو الصدر من عقل أو ثبات، والجبان أو الضعيف الفؤاد إذا صرح المصدر بذلك.","what_is_not_ar":"ليس هو الهَوَى بمعنى ميل النفس، ولا السقوط في المهواة، ولا الهواهي من القول."},"support_links":["sup_fe446e14ae20f3850177"]},{"boundary":"Aşağı düşme merkezde tutulur; yükseliş yönündeki gidiş ayrı bir kaynak çeşitlemesi, ölüm ve yas ise bağlı kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001609/B002","candidate_links":[{"candidate_id":"cand_806fdff7f00274cc81b6","lane":"micro"},{"candidate_id":"cand_e5df16ecbc308492da67","lane":"micro"},{"candidate_id":"cand_f21f98910b05ab991010","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"هَاوِيَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:haAwiyap|ROOT:hwy|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:2:1","qac_word_ref":"101:9:2","surface_ar":"هَاوِيَةٌ"}],"gloss":"yukarıdan düşme; yönlü gidiş, derin çukur, düşürme, ölüm ve yas bağlantıları","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin veya kuşun yukarıdan aşağı düşmesi ve aşağı yönlü ilerlemesi."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yönlü gidişin bir kaynakta inişin yanında yükseliş için de kullanılması."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Derin çukurun, düşme yerinin ve dibi erişilmez uçurumun adlandırılması; ayrıca ateş azabının adı olması."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir şeyi yukarıdan düşürme, kişinin ölmesi ve insanların bir çukura art arda düşmesi."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Ölen kişinin annesinin evlat acısı çekmiş olarak nitelenmesi."}}],"root_ar":"ه و ي","root_id":"root_001609","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Düşme çekirdeğini, yön çeşitlemesini ve kaynakta ona bağlanan yer, ettirgenlik, ölüm ve yas kullanımlarını birlikte özetler.","boundary_detail":"Aşağı düşme merkezde tutulur; yükseliş yönündeki gidiş ayrı bir kaynak çeşitlemesi, ölüm ve yas ise bağlı kullanımlardır.","branch_image_ar":"هُوِيّ وسقوط إلى مهواة","concept_gloss":"yukarıdan düşme; yönlü gidiş, derin çukur, düşürme, ölüm ve yas bağlantıları","contextual_glosses":[{"applicability":"Bir nesnenin, kişinin veya kuşun yüksek bir yerden aşağıya indiği fiziksel düşüş bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yüksekten aşağı gerçekleşen fiziksel düşüş çekirdeğini tam olarak korur."},"facet_ids":["F001"],"text":"yukarıdan aşağı düştü","usage_role":"general"},{"applicability":"Dibi görülemeyen derin bir çukurun ya da düşme yerinin adı olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Derinliği kavranamayan düşme yeri anlamını doğal Türkçeyle korur."},"facet_ids":["F003"],"text":"dipsiz uçurum","usage_role":"contextual"}],"definition":"Temel olarak bir şeyin yukarıdan aşağı düşmesini, aşağı yönlü gidişi ve art arda düşüşü anlatır; derin düşme yeri, dibi erişilmez çukur, ateş azabının adı, düşürme ve düşüş imgesiyle ölüm de bu kola bağlıdır. Bir kaynak yönlü gidişi yükselme için de kullanır; başka bir kullanım ölen kişinin annesini evlat acısı çekmiş olarak niteler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin veya kuşun yukarıdan aşağı düşmesi ve aşağı yönlü ilerlemesi."},{"facet_id":"F002","role":"source_variant","statement":"Yönlü gidişin bir kaynakta inişin yanında yükseliş için de kullanılması."},{"facet_id":"F003","role":"extension","statement":"Derin çukurun, düşme yerinin ve dibi erişilmez uçurumun adlandırılması; ayrıca ateş azabının adı olması."},{"facet_id":"F004","role":"associated_use","statement":"Bir şeyi yukarıdan düşürme, kişinin ölmesi ve insanların bir çukura art arda düşmesi."},{"facet_id":"F005","role":"associated_use","statement":"Ölen kişinin annesinin evlat acısı çekmiş olarak nitelenmesi."}],"identity_rationale":"Kaynak ifadesinin baskın çekirdeği yukarıdan aşağı düşmedir; derin düşme yeri, art arda düşme, düşürme ve ölüm bunun açık uzantılarıdır. Bununla birlikte bir kaynak aynı hareket adını inişin yanında yükseliş yönündeki gidiş için de kullandığından kol yalnız aşağı düşüşle sınırlandırılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yukarıdan aşağı düştü veya indi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"dipsiz uçurum; ateş azabının adı"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"derin çukur veya düşme yeri"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"topluluk derin çukura birbiri ardınca düştü"}],"lexicalization_note":"Yalın düşme anlamı, derin çukur adlarından, art arda düşme kuruluşundan ve düşürme ya da ölüm uzantılarından ayrı gösterilir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yakın üç düşme dalı yön, biçim ve sonuç bakımından ayrıştırıldı, yalnız aynı senaryoya katılan çukur ve hareket adayları dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol yüksekten aşağı yönü ve derin düşme yerini öne çıkarır; komşu düşmenin yönünü daha az sınırlar ve batma, çökme, yorgunluk gibi başka sonuçları da kapsar.","focus_only":"Yüksekten aşağı yön, dipsiz düşme yeri ve yönlü gidişin yükseliş çeşitlemesi bu kolda belirgindir.","gloss":"düşme ve yere varma","neighbor_only":"Güneşin batması, yana düşme, devenin çökmesi ve yorgunluk gibi geniş sonuçlar komşuda bulunur.","neighbor_ref":"root_001625/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bir varlığın düşmesini, yere varmasını ve ölümle ilişkilendirilen düşüşü kapsar."},{"boundary_match":"partial","distinction":"Bu kol düşüş yönü ve düşme yeri çevresinde örgütlenir; komşu ise düşüşün sarsıntılı ve sesli gerçekleşmesine ve yere kapanmaya kadar uzanır.","focus_only":"Dipsiz çukur, art arda düşme ve bir kaynakta yükseliş yönünde gidiş bu kola özgüdür.","gloss":"yüksekten düşmek","neighbor_only":"Düşüşün sarsıntılı ya da sesli olması ve yere kapanma kullanımı komşuda öne çıkar.","neighbor_ref":"root_000402/B001","relation_type":"near_synonym","shared_zone":"Her iki dal yüksekten düşmeyi, düşürmeyi ve düşüş imgesiyle ölümü ifade edebilir."},{"boundary_match":"partial","distinction":"Bu kolun çekirdeği sonuçtan bağımsız fiziksel düşüştür; komşu ise düşüşü yok olma ve bilinmez biçimde ortadan kaybolma sonucuyla sınırlar.","focus_only":"Zararsız fiziksel düşüş, derin çukur adları ve yükseliş yönündeki gidiş çeşitlemesi bu kolda vardır.","gloss":"düşerek yok olmak","neighbor_only":"Kaybolup nereye gittiği bilinmeme ve doğrudan yok olma sonucu komşuya özgüdür.","neighbor_ref":"root_000558/B003","relation_type":"near_synonym","shared_zone":"Her iki dal derin bir yere düşüşü ve düşüşün ölüm ya da yok oluşla sonuçlanmasını anlatır."}],"source_phrase_ar":"هوى الطائر يهوي هويا (ayn)؛ هاوية من أسماء جهنم والهاوية كل مهواة لا يدرك قعرها (ayn)؛ هوى فلان أي مات (ayn)؛ هوى الشيء يهوي إذا خر من علو إلى سفل (jamhara)؛ هوى بالفتح يهوي هويا أي سقط إلى أسفل (sihah)؛ الهاوية اسم من أسماء النار والهاوية المهواة (sihah)؛ هوت أمه فهي هاوية أي ثاكلة (sihah)؛ هويت أهوي هويا إذا سقطت من علو إلى أسفل (tahdhib)؛ المؤتفكة أهوى أي أسقطها (tahdhib)؛ الهاوية كل مهواة لا يدرك قعرها والهوة كل وهدة معمقة (tahdhib)؛ الهوي سقوط من علو إلى سفل (mufradat)؛ الهوي ذهاب في انحدار والهوي ذهاب في ارتفاع (mufradat)؛ هوى الشيء يهوي سقط (maqayis)؛ تهاوى القوم في المهواة سقط بعضهم في إثر بعض (maqayis)","source_summary":"Ortak çekirdek yüksekten aşağı düşmedir ve derin düşme yerleri, düşürme, art arda düşme ile ölüm bu çekirdeğe bağlanır. Toplu ifade ayrıca yönlü gidişin yükselme kullanımını ve ölümün anne üzerindeki yas sonucunu da kaydeder.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه سقوط الشيء أو الطائر من علو إلى سفل، والهُوِيّ في الانحدار أو الارتفاع إذا صرحت به المصادر، والهاوية والهوة والمهواة، والتهاوي، وإهلاك الشيء أو موته على صورة السقوط.","what_is_not_ar":"ليس هو الهَوَى النفسي، ولا مجرد خلو الهَواء، ولا إهواء اليد للتناول إلا إذا كان بمعنى الإلقاء من فوق."},"support_links":["sup_468cd99ebff6e6d8d1ec","sup_8214ecc5a71b35d0b2d4","sup_fe446e14ae20f3850177"]},{"boundary":"Kişinin kendi kendine düşmesi bu kola girmez; burada el ya da nesne bir hedefe doğru gönderilir veya yukarıdan atılır.","branch_kind":"mixed_non_bare","branch_ref":"root_001609/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هَاوِيَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:haAwiyap|ROOT:hwy|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:2:1","qac_word_ref":"101:9:2","surface_ar":"هَاوِيَةٌ"}],"gloss":"eli ya da nesneyi hedefe yöneltmek; yukarıdan atmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Elin bir şeyi almak amacıyla ona doğru uzatılması ve gönderilmesi."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir nesne veya kılıçla birine doğru işaret edilmesi ya da vurulması."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir şeyin yukarıdan aşağı atılması veya bırakılması."}}],"root_ar":"ه و ي","root_id":"root_001609","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"El uzatma, nesneyle işaret veya vuruş ve yukarıdan atma biçimlerini ortak yöneltme çekirdeği altında gösterir.","boundary_detail":"Kişinin kendi kendine düşmesi bu kola girmez; burada el ya da nesne bir hedefe doğru gönderilir veya yukarıdan atılır.","branch_image_ar":"إهواء اليد والشيء","concept_gloss":"eli ya da nesneyi hedefe yöneltmek; yukarıdan atmak","contextual_glosses":[{"applicability":"Bir kişinin elini belirli bir nesneye ulaşıp onu almak amacıyla gönderdiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Elin hedefe yönelmesini ve bu hareketin alma amacını tam olarak korur."},"facet_ids":["F001"],"text":"almak için elini uzattı","usage_role":"contextual"},{"applicability":"Kılıç ya da başka bir nesnenin bir hedefe doğru işaret veya vuruş hareketi yaptığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taşınan nesnenin hedefe doğru yöneltilen hareketini ve vuruş olanağını korur."},"facet_ids":["F002"],"text":"kılıcı ona doğru savurdu","usage_role":"contextual"}],"definition":"Elin bir şeyi almak için hedefe doğru uzatılıp gönderilmesini, bir nesne ya da kılıçla işaret veya vuruş yapılmasını ve bir şeyin yukarıdan atılmasını anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Elin bir şeyi almak amacıyla ona doğru uzatılması ve gönderilmesi."},{"facet_id":"F002","role":"specialization","statement":"Bir nesne veya kılıçla birine doğru işaret edilmesi ya da vurulması."},{"facet_id":"F003","role":"extension","statement":"Bir şeyin yukarıdan aşağı atılması veya bırakılması."}],"identity_rationale":"Kaynak ifadesi elin almak üzere bir hedefe uzatılmasını, bir nesne ya da kılıçla işaret veya vuruş yapılmasını ve bir şeyin yukarıdan atılmasını ayrı fakat aynı gönderme hareketine bağlı kullanımlar olarak açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"almak için elini ona uzattı"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"nesneyle işaret etti veya kılıçla vurdu"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"onu yukarıdan aşağı attı"}],"lexicalization_note":"El uzatma ve nesneyle işaret ya da vuruş kuruluşları ayrı tutulur; yukarıdan atma yalın ettirgen biçimin anlamıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; el uzatma, gönderme ve kılıç hareketiyle doğrudan kesişen üç dal seçildi, yalnız araç adı veya uzak senaryo ortaklığı taşıyanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol el uzatmayı alma amacıyla bağlar ve başka araç hareketlerine genişler; komşu yalnız elin yere doğru uzatılmasını ifade eder.","focus_only":"Bir şeyi alma amacı, nesne veya kılıçla işaret ya da vuruş ve yukarıdan atma bu kolda bulunur.","gloss":"eli uzatmak","neighbor_only":"Elin özellikle yere doğru uzatılması komşunun dar yön koşuludur.","neighbor_ref":"root_000092/B007","relation_type":"near_synonym","shared_zone":"Her iki dal elin bedenden uzağa, belirli bir hedef yönüne doğru hareket ettirilmesini anlatır."},{"boundary_match":"partial","distinction":"Bu kol bedensel yöneltme ve yukarıdan bırakma çevresindedir; komşu ise atışın aracını, hedefini ve fırlatma eylemini merkez alır.","focus_only":"Elin alma amacıyla uzatılması ve kılıçla işaret ya da vuruş yapılması bu kola özgüdür.","gloss":"göndermek ve atmak","neighbor_only":"Yay, ok, taş ve belirli hedefe yapılan atış türleri komşuda açıkça yer alır.","neighbor_ref":"root_000603/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal bir şeyi elden çıkarıp belirli bir yöne doğru gönderme hareketinde buluşur."},{"boundary_match":"partial","distinction":"Bu kol kılıç hareketini daha genel yöneltme ailesinin bir üyesi yapar; komşu uzaktan ve hafif vuruş biçimiyle sınırlıdır.","focus_only":"El uzatma, nesneyle işaret etme ve yukarıdan atma anlamları bu kolda vardır.","gloss":"kılıcı hedefe yöneltmek","neighbor_only":"Kılıçla özellikle uzaktan ve hafifçe vurma koşulu komşuya özgüdür.","neighbor_ref":"root_001528/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal kılıcın bir hedefe doğru uzatılması ve onunla vuruş yapılması alanını paylaşır."}],"source_phrase_ar":"أهوى إليه فأخذه أي أهوى إليه يده (ayn)؛ أهوى إليه بيده ليأخذه (sihah)؛ أهويت بالشيء إذا أومأت به (sihah)؛ أهويت له بالسيف (sihah)؛ أهويت له بالسيف وغيره (tahdhib)؛ أهويته إذا ألقيته من فوق (tahdhib)؛ هوت العقاب إذا انقضت فإذا أراغته قيل أهوت له إهواء (tahdhib)؛ أهوى إليه بيده ليأخذه كأنه رمى إليه بيده إذا أرسلها (maqayis)","source_summary":"Kaynaklar hareketin hedefe yöneltilmesini ortaklaştırır: el alma amacıyla uzatılır, taşınan nesne işaret ya da vuruş için gönderilir ve ettirgen biçim bir şeyi yukarıdan atmayı anlatır.","sources":["AY","SI","TA","MQ"],"what_is_ar":"يدخل فيه أهوى إليه بيده ليأخذ، وأهوى بالشيء أو بالسيف إذا أومأ أو ضرب، وأهواه إذا ألقاه من فوق.","what_is_not_ar":"ليس هو هوى النفس، ولا سقوط الشيء بنفسه، ولا السير السريع."},"support_links":[]},{"boundary":"İçsel sevgi ve istek yönelimi esastır; fiziksel düşme, hava ve yalnızca şaşkınlığa sürüklenme bu kola girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001609/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هَاوِيَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:haAwiyap|ROOT:hwy|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:2:1","qac_word_ref":"101:9:2","surface_ar":"هَاوِيَةٌ"}],"gloss":"benliğin sevgi ve isteğe yönelmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Benliğin sevgiye, isteğe veya haz veren bir şeye doğru içsel olarak yönelmesi."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişiyi veya şeyi sevmek, istemek ve ona gönülden yönelmek."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir şeyi başka bir seçeneğe göre daha sevimli ve tercih edilir bulmak."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Farklı kişisel eğilimleri benimseyip izleyen kimselerin topluluk olarak adlandırılması."}}],"root_ar":"ه و ي","root_id":"root_001609","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sevgi, istek, yeğleme ve benimsenen kişisel eğilimler için ortak içsel yönelim çekirdeğini temsil eder.","boundary_detail":"İçsel sevgi ve istek yönelimi esastır; fiziksel düşme, hava ve yalnızca şaşkınlığa sürüklenme bu kola girmez.","branch_image_ar":"الهَوَى وميل النفس","concept_gloss":"benliğin sevgi ve isteğe yönelmesi","contextual_glosses":[{"applicability":"Bir kişiye veya şeye sevgi ve istekle yönelme söz konusu olduğunda doğal bir anlatım olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Benliğin sevilen veya istenen hedefe doğru içsel yönelimini korur."},"facet_ids":["F001","F002"],"text":"gönlü ona yöneldi","usage_role":"general"},{"applicability":"İki seçenek arasında birinin daha sevimli ve tercih edilir bulunduğu karşılaştırmalı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sevginin karşılaştırmalı tercih olarak ifade edilmesini eksiksiz korur."},"facet_ids":["F003"],"text":"bunu ötekinden daha çok seviyorum","usage_role":"contextual"}],"definition":"Benliğin sevilen veya istenen bir şeye yönelmesini, sevgi ya da istek duymasını anlatır. Bir şeyi başkasına yeğleme ve farklı kişisel eğilimleri izleyen topluluklar da bu içsel yönelime bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Benliğin sevgiye, isteğe veya haz veren bir şeye doğru içsel olarak yönelmesi."},{"facet_id":"F002","role":"specialization","statement":"Bir kişiyi veya şeyi sevmek, istemek ve ona gönülden yönelmek."},{"facet_id":"F003","role":"associated_use","statement":"Bir şeyi başka bir seçeneğe göre daha sevimli ve tercih edilir bulmak."},{"facet_id":"F004","role":"extension","statement":"Farklı kişisel eğilimleri benimseyip izleyen kimselerin topluluk olarak adlandırılması."}],"identity_rationale":"Kaynak ifadesi benliğin sevgiye veya isteğe yönelmesini çekirdek yapar; sevmek, istemek, bir şeyi başkasına yeğlemek ve farklı eğilimlerin izleyicilerini adlandırmak bu çekirdeğin açık kullanımlarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"benliğin sevgiye veya isteğe yönelmesi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"sevdi, gönlü ona yöneldi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ötekinden daha çok sevilen"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"çeşitli kişisel eğilimlerin izleyicileri"}],"lexicalization_note":"Yalın içsel eğilim ile sevme, yeğleme ve eğilim sahiplerini adlandıran kuruluşlar ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; sevgi, istek ve gönül eğilimi çekirdeğine en yakın üç dal seçildi, yalnız duygu alanını paylaşan karşıt veya uzak durumlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol sevgiyi ve genel içsel tercihi kapsar; komşu isteğin iştah yönünü, arzulanan nesneyi ve bu isteği taşıyan yetiyi daha belirgin işler.","focus_only":"Sevgi, karşılaştırmalı tercih ve eğilimleri izleyen topluluklar bu kolda ayrıca bulunur.","gloss":"istek ve arzu","neighbor_only":"İştah yetisi, arzulanan nesnenin adı ve iştahlı olma niteliği komşuya özgüdür.","neighbor_ref":"root_000825/B001","relation_type":"near_synonym","shared_zone":"Her iki dal benliğin haz veren veya istenen bir şeye doğru yönelmesini anlatır."},{"boundary_match":"partial","distinction":"Bu kol sevginin yanında istek ve tercihi de kapsayan daha geniş içsel eğilimdir; komşu yoğun sevgi, incelik ve özlem durumuna odaklanır.","focus_only":"Hazza yönelen istek, yeğleme ve farklı eğilimlerin izleyicileri bu kola özgüdür.","gloss":"sevgiyle gönül verme","neighbor_only":"İnce duygulanım, özlem ve sevilen kişiye kendini bütünüyle verme komşuda belirgindir.","neighbor_ref":"root_000838/B004","relation_type":"near_synonym","shared_zone":"Her iki dal gönlün sevilen bir kişiye veya şeye doğru yönelmesini ifade eder."},{"boundary_match":"partial","distinction":"Bu kol içsel eğilimi yaş ve davranış koşulu olmadan verir; komşu bunu gençlik özlemi, oyun ve düşüncesizlik alanlarına genişletir.","focus_only":"Genel istek, karşılaştırmalı tercih ve eğilim toplulukları bu kolda bulunur.","gloss":"gönlün eğilmesi","neighbor_only":"Gençlik taşkınlığı, özlem, oyun ve düşüncesizce davranma uzantıları komşuda bulunur.","neighbor_ref":"root_000843/B002","relation_type":"near_synonym","shared_zone":"Her iki dal kalbin veya benliğin sevilen bir hedefe doğru eğilmesi ve özlem duymasını kapsar."}],"source_phrase_ar":"الهَوَى مقصور الحب (ayn)؛ هوى النفس مقصور (jamhara)؛ الهَوَى مقصور هوى النفس والجمع الأهواء (sihah)؛ هوى بالكسر يهوى هوى أي أحب (sihah)؛ هذا الشيء أهوى إلى من كذا أي أحب إلي (sihah)؛ أفئدة من الناس تهوى إليهم يقول تريدهم (tahdhib)؛ وتهوي إليهم تهواهم (tahdhib)؛ الهَوَى مقصور هوى الضمير (tahdhib)؛ أهل الأهواء واحدها هوى (tahdhib)؛ الهَوَى ميل النفس إلى الشهوة (mufradat)؛ الهوى هوى النفس فمن المعنيين جميعا (maqayis)؛ هويت أهوى هوى (maqayis)","source_summary":"Kaynakların ortak noktası benliğin sevgi ve istek doğrultusunda eğilmesidir. Sevme fiili, bir seçeneği daha çok isteme ve çeşitli eğilimleri izleyenleri adlandırma bu çekirdeğin ayrı gerçekleşmeleridir.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الهَوَى المقصور بمعنى حب النفس وميلها إلى الشهوة، وأهل الأهواء، واتباع الهوى، وتهوى إليه أو تهواه إذا كان المعنى تريد أو تحب.","what_is_not_ar":"ليس هو الهَواء الممدود، ولا السقوط الحسي، ولا الاستهواء إذا أريد به الإذهاب والحيرة وحدهما."},"support_links":[]},{"boundary":"Anlam belirli ayartılma kuruluşuna bağlıdır; yalın istek, fiziksel düşüş veya genel şaşkınlık olarak genişletilemez.","branch_kind":"collocation","branch_ref":"root_001609/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هَاوِيَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:haAwiyap|ROOT:hwy|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:2:1","qac_word_ref":"101:9:2","surface_ar":"هَاوِيَةٌ"}],"gloss":"ayartıp şaşkınlığa ve isteklerinin peşine sürüklemek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ayartıcı güçlerin kişiyi yoldan çıkararak şaşkınlığa düşürmesi, alıp götürmesi ve isteklerinin peşinden sürüklemesi."}}],"root_ar":"ه و ي","root_id":"root_001609","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız ayartıcı güçlerin bir kişiyi yoldan çıkarıp yönsüz bıraktığı belirtilen kuruluşun bütün sonuçlarını karşılar.","boundary_detail":"Anlam belirli ayartılma kuruluşuna bağlıdır; yalın istek, fiziksel düşüş veya genel şaşkınlık olarak genişletilemez.","branch_image_ar":"استهواء يورث حيرة","concept_gloss":"ayartıp şaşkınlığa ve isteklerinin peşine sürüklemek","contextual_glosses":[{"applicability":"Ayartıcı güçlerin bir kişiyi yolundan çıkarıp ne yapacağını bilemez hale getirdiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dış etkenle yoldan çıkarılma ve şaşkınlığa düşürülme sonucunu korur."},"facet_ids":["F001"],"text":"onu ayartıp şaşkınlığa sürüklediler","usage_role":"contextual"}],"definition":"Belirtilen kuruluşta ayartıcı güçlerin bir kişiyi yoldan çıkarıp şaşkın ve yönsüz bırakmasını, alıp götürmesini veya kendi isteklerinin peşinden sürüklemesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ayartıcı güçlerin kişiyi yoldan çıkararak şaşkınlığa düşürmesi, alıp götürmesi ve isteklerinin peşinden sürüklemesi."}],"identity_rationale":"Kaynak ifadesi yalnız belirli kuruluşta ayartıcı güçlerin kişiyi şaşkın ve yönsüz bırakmasını, onu alıp götürmesini veya kişisel eğilimlerinin peşinden sürüklemesini anlatır; geçici dal çerçevesi bu sınırı doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"ayartıcı güçler onu yoldan çıkarıp şaşkınlığa sürükledi"}],"lexicalization_note":"Tanım yalnız ayartıcı güçlerin özneyi şaşkınlığa ve kişisel eğilimlerinin peşine sürüklediği belirtilen kuruluş için geçerlidir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnız içsel isteğin dıştan ayartılmayla ilişkisini açıklayan kök içi komşu yararlı bulundu, öteki adaylar anlam çekirdeğini paylaşmadığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol dış bir gücün kişiyi isteklerine uymaya itmesi ve şaşkın bırakmasıdır; komşu ise kişinin kendi içsel sevgi ve istek yönelimini adlandırır.","focus_only":"Dış bir ayartıcının kişiyi yoldan çıkarıp şaşkın ve yönsüz bırakması bu kola özgüdür.","gloss":"isteğin peşine sürüklenme","neighbor_only":"Kişinin içinden doğan sevgi, istek, yeğleme ve eğilim toplulukları komşu kolda bulunur.","neighbor_ref":"root_001609/B004","relation_type":"near_neighbor","shared_zone":"İki dal da kişinin istek ve eğilimlerinin davranış yönünü belirlemesi senaryosuna katılır."}],"source_phrase_ar":"استهوته الشياطين فهو حيران هائم (ayn)؛ استهواه الشيطان أي استهامه (sihah)؛ استهوته الشياطين فهو حيران هائم (tahdhib)؛ كالذي زينت له الشياطين هواه حيران (tahdhib)؛ استهوته الشياطين هوت به وأذهبته (tahdhib)؛ استهوته الشياطين أي حملته على اتباع الهوى (mufradat)","source_summary":"Toplu kaynak ifadesi aynı kuruluşu, şaşkın ve başıboş bırakma, alıp götürme ve kişinin kendi isteklerini izlemesine yol açma yönleriyle açıklar.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه استهوته الشياطين، والمستهام الحيران الهائم، وحملته الشياطين على اتباع الهوى أو هوت به وأذهبته بحسب عبارة المصدر.","what_is_not_ar":"ليس هو مطلق هوى النفس بلا صيغة استفعال، ولا مجرد السقوط الحسي في مهواة."},"support_links":[]},{"boundary":"Uzun zaman ile gecenin bir bölümü ayrı kullanımlardır; biri ötekinin ölçüsüne indirgenmez ve hareket anlamları bu kola alınmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001609/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هَاوِيَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:haAwiyap|ROOT:hwy|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:2:1","qac_word_ref":"101:9:2","surface_ar":"هَاوِيَةٌ"}],"gloss":"uzun bir zaman veya gecenin bir bölümü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Uzun süren bir zaman aralığının adlandırılması."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Geçip giden gecenin bir parçasının veya diliminin adlandırılması."}}],"root_ar":"ه و ي","root_id":"root_001609","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Uzun süre bildiren biçimi ve gece dilimi bildiren kuruluşu birlikte, fakat seçenekli olarak temsil eder.","boundary_detail":"Uzun zaman ile gecenin bir bölümü ayrı kullanımlardır; biri ötekinin ölçüsüne indirgenmez ve hareket anlamları bu kola alınmaz.","branch_image_ar":"هُوِيّ من الزمان أو الليل","concept_gloss":"uzun bir zaman veya gecenin bir bölümü","contextual_glosses":[{"applicability":"Başlangıç ve bitişi kesinleştirilmemiş, uzun devam eden bir zaman aralığı için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Zaman aralığının uzun sürmesi ve belirsiz bir bütün olması anlamını korur."},"facet_ids":["F001"],"text":"uzun bir süre","usage_role":"general"},{"applicability":"Bir olayın gece içinde belirli olmayan bir dilimde gerçekleştiğini anlatan kuruluşta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gecenin bütünü içindeki sınırlı zaman parçasını eksiksiz korur."},"facet_ids":["F002"],"text":"gecenin bir bölümü","usage_role":"contextual"}],"definition":"Bir kullanımda uzun bir zaman süresini, başka bir kuruluşta ise gecenin belirli olmayan bir parçasını veya dilimini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Uzun süren bir zaman aralığının adlandırılması."},{"facet_id":"F002","role":"specialization","statement":"Geçip giden gecenin bir parçasının veya diliminin adlandırılması."}],"identity_rationale":"Kaynak ifadesi iki zaman kullanımını açıkça ayırır: uzun bir zaman süresi ve gecenin bir parçası ya da dilimi. Geçici çerçeve bu iki kullanımı düşme, içsel istek ve hava anlamlarından doğru biçimde ayırmaktadır.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"uzun bir zaman"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"gecenin bir bölümü veya dilimi"}],"lexicalization_note":"Uzun zaman bildiren biçim ile gecenin bir bölümünü bildiren kuruluş birbirine karıştırılmadan ayrı tanımlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; uzun süre ve gece parçası sınırını doğrudan karşılaştıran üç zaman dalı seçildi, yalnız gece teması veya belirli vakit ortaklığı taşıyanlar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol uzun zaman anlamını gecenin bir dilimiyle birlikte taşır; komşu zamanın yanında genel uzunluğu ve uzun günü de kapsar.","focus_only":"Gecenin bir parçasını bildiren özel kuruluş bu kolda ayrıca bulunur.","gloss":"uzun zaman","neighbor_only":"Zamansal olmayan uzunluk ve özellikle uzun gün anlatımı komşuda bulunur.","neighbor_ref":"root_001477/B007","relation_type":"near_synonym","shared_zone":"Her iki dal uzun süren bir zaman aralığını veya süre kavramını ifade eder."},{"boundary_match":"partial","distinction":"Bu kol gece parçasını özel bir kuruluşta verir ve ayrıca uzun zaman anlamı taşır; komşu geceyle gündüzü birlikte kapsar ve parçayı büyük bölüm ya da saat olarak sınırlar.","focus_only":"Genel olarak uzun zaman süresi bu kolda bağımsız bir anlamdır.","gloss":"gece dilimi","neighbor_only":"Gündüzün bir parçası ve gece ya da gündüzün büyük bölümü komşuda ayrıca bulunur.","neighbor_ref":"root_000927/B010","relation_type":"near_synonym","shared_zone":"Her iki dal gecenin bütünü içindeki bir zaman parçasını adlandırır."},{"boundary_match":"partial","distinction":"Bu kol uzun süreyi gece parçasıyla eşlenen iki kullanımdan biri olarak verir; komşu bir çağ ya da dönem ölçüsüne kadar genişleyebilir.","focus_only":"Gecenin belirli olmayan bir dilimini anlatan kullanım bu kola özgüdür.","gloss":"uzun dönem","neighbor_only":"Bütün çağ veya dönem olarak kullanılabilme komşunun daha geniş zaman ölçeğidir.","neighbor_ref":"root_000665/B006","relation_type":"near_synonym","shared_zone":"Her iki dal sınırları kesin verilmeyen uzun bir zaman parçasını ifade edebilir."}],"source_phrase_ar":"الهوي الملي الحين الطويل من الزمان (ayn)؛ مر هوي من الليل أي قطعة منه وكذلك تهواء من الليل (jamhara)؛ مضى هوى من الليل أي هزيع منه (sihah)؛ الهوي الملي الحين الطويل من الزمان (tahdhib)","source_summary":"Toplu ifade uzun zaman süresini bir anlam, gecenin bir bölümünü ise belirli kuruluşlara bağlı ikinci anlam olarak kaydeder; her ikisinde de odak zamanın bir kesitidir.","sources":["AY","JA","SI","TA"],"what_is_ar":"يدخل فيه الهوي الملي بمعنى الحين الطويل، والهوي أو التهواء من الليل بمعنى قطعة أو هزيع منه.","what_is_not_ar":"ليس هو الهَوَى النفسي، ولا الهُوِيّ بمعنى السقوط، ولا الهَواء."},"support_links":[]},{"boundary":"Anlam yalnız belirtilen yara ve gövde kuruluşlarında geçerlidir; genel hava, her türlü boşluk veya her türlü iç yara anlamına gelmez.","branch_kind":"collocation","branch_ref":"root_001609/B007","candidate_links":[{"candidate_id":"cand_0bad8584d81324f0b419","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"هَاوِيَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:haAwiyap|ROOT:hwy|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:2:1","qac_word_ref":"101:9:2","surface_ar":"هَاوِيَةٌ"}],"gloss":"yaranın açılması veya gövdenin boşalıp oyuklaşması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Saplama yarasının ağzının açılması ve yara açıklığının genişlemesi."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gövdenin böğür bölgesinin zayıflıktan boşalıp oyuklaşarak açılması."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Göğsün içinin boş kalması veya boşalması."}}],"root_ar":"ه و ي","root_id":"root_001609","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yara ağzı, böğür bölgesi ve göğsün içiyle kurulan özel boşalma ve açılma kullanımlarını birlikte temsil eder.","boundary_detail":"Anlam yalnız belirtilen yara ve gövde kuruluşlarında geçerlidir; genel hava, her türlü boşluk veya her türlü iç yara anlamına gelmez.","branch_image_ar":"فغر الطعنة وخلو الجوف","concept_gloss":"yaranın açılması veya gövdenin boşalıp oyuklaşması","contextual_glosses":[{"applicability":"Kesici veya delici darbenin oluşturduğu yaranın ağzının açıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yara ağzının açılmasını ve açıklığın genişlemesini tam olarak korur."},"facet_ids":["F001"],"text":"saplama yarası açılıp genişledi","usage_role":"contextual"},{"applicability":"Gövdenin yan bölümünün aşırı zayıflık nedeniyle içe çöküp boş görünmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gövde bölgesinin zayıflıktan boşalıp açılması anlamını korur."},"facet_ids":["F002"],"text":"böğrü zayıflıktan oyuklaştı","usage_role":"contextual"}],"definition":"Belirtilen gövde kuruluşlarında saplama yarasının ağzının açılıp genişlemesini, böğür bölgesinin zayıflıktan oyuklaşıp açılmasını veya göğsün içinin boş kalmasını anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Saplama yarasının ağzının açılması ve yara açıklığının genişlemesi."},{"facet_id":"F002","role":"specialization","statement":"Gövdenin böğür bölgesinin zayıflıktan boşalıp oyuklaşarak açılması."},{"facet_id":"F003","role":"associated_use","statement":"Göğsün içinin boş kalması veya boşalması."}],"identity_rationale":"Kaynak ifadesi saplama yarasının ağzının açılmasını, gövdenin böğür bölgesinin zayıflıktan oyuklaşıp açılmasını ve göğsün içinin boş kalmasını açıkça aynı boşalma ve açılma imgesine bağlar.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"saplama yarası açılıp genişledi"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"böğür bölgesi zayıflıktan oyuklaşıp açıldı"}],"lexicalization_note":"Tanım saplama yarası, böğür bölgesi ve göğüsle kurulan özel kullanımlara bağlıdır; yalın bir boşluk anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yara derinliği ve genel boşlukla sınırı en iyi gösteren üç dal seçildi, yalnız beden bölgesi veya çıplaklık alanını paylaşan adaylar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol yaranın ağzının açılıp genişlemesine odaklanır; komşu yaranın iç boşluğa kadar ulaşmasını ya da onu delmesini gerekli kılar.","focus_only":"Yara ağzının genişlemesi ile böğür ve göğüsteki boşalma bu kola özgüdür.","gloss":"derine işleyen saplama yarası","neighbor_only":"Yaranın beden boşluğuna ulaşması, karışması veya onu bütünüyle delmesi komşuya özgüdür.","neighbor_ref":"root_000279/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal saplama yarasını ve yaranın bedenin iç kısmıyla ilişkisini ele alır."},{"boundary_match":"partial","distinction":"Bu kol açıklığın biçimini ve gövdedeki boşluğu anlatır; komşu yaranın iç organa ya da boşluğa erişme derecesini anlatır.","focus_only":"Böğür bölgesinin zayıflıktan oyuklaşması ve göğsün boş kalması bu kolda bulunur.","gloss":"içe ulaşan yara","neighbor_only":"Yaranın beyne veya beden boşluğuna yaklaşması ve hayvanın bu yarayla nitelenmesi komşuda bulunur.","neighbor_ref":"root_001518/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal bir yaranın açılması ve bedenin iç kısmına yaklaşması alanında kesişir."},{"boundary_match":"partial","distinction":"Bu kol yalnız yara ve gövde kuruluşlarında bedensel açıklığı anlatır; komşu genel hava ve boşluk anlamından başlayarak daha geniş bir alanı kapsar.","focus_only":"Yara ve gövdeyle sınırlı açılma ve oyuklaşma kuruluşları bu kola özgüdür.","gloss":"bedende boşalma","neighbor_only":"Atmosferik hava, iki nesne arasındaki genel aralık ve yüreksizlik uzantısı komşu kolda bulunur.","neighbor_ref":"root_001609/B001","relation_type":"near_neighbor","shared_zone":"İki dal da içi dolu olması beklenen bir yerin boş veya açık hale gelmesi imgesini paylaşır."}],"source_phrase_ar":"هوت الطعنة تهوى فتحت فاها (sihah)؛ هوى بين الكلى والكراكر (sihah)؛ هوت الطعنة إذا فتحت فاها (tahdhib)؛ خلا وانفتح من الضمر (tahdhib)؛ هوى صدره يهوي هواء إذا خلا (tahdhib)؛ هوت الطعنة فتحت فاها تهوى وهو من الهواء الخالي (maqayis)","source_summary":"Kaynaklar yarada açılan ağız ile zayıflıktan oyuklaşan gövde bölgesini boşalma ve açılma bakımından birleştirir; göğsün boş kalması da aynı imgenin bağlı kullanımıdır.","sources":["SI","TA","MQ"],"what_is_ar":"يدخل فيه هوت الطعنة إذا فتحت فاها، وما خلا أو انفتح من الضمر بين الكلى والكراكر، وما كان جوفه خاليا كالقصب في الشاهد.","what_is_not_ar":"ليس هو مطلق الهَواء بين السماء والأرض، ولا السقوط في مهواة، ولا الهواهي."},"support_links":["sup_337d33c3c239c33b49eb"]},{"boundary":"Burada hareketin hızlı ve atılımlı oluşu esastır; kendiliğinden düşme, içsel istek ve karşılıklı çekişme bu kola girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001609/B008","candidate_links":[{"candidate_id":"cand_f21f98910b05ab991010","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"هَاوِيَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:haAwiyap|ROOT:hwy|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:2:1","qac_word_ref":"101:9:2","surface_ar":"هَاوِيَةٌ"}],"gloss":"hızlı yönlü ilerleme, atılımlı koşu ve sert yol alma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Aşağı veya yukarı yönde hızlı ilerleme ve sert yol alışta bedenin ileri atılması."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yırtıcı kuşun avına hızla dalması ve devenin güçlü, yüksek tempolu koşusu."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yolculukta çok hızlı ve sert biçimde ilerleme."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Belirli çoğul biçimin çeşitli yol alış ve ilerleme tarzlarını adlandırması."}}],"root_ar":"ه و ي","root_id":"root_001609","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel hızlı gidişi, hayvanların özel atılışlarını, zorlu yolculuğu ve yol alış türlerini birlikte temsil eder.","boundary_detail":"Burada hareketin hızlı ve atılımlı oluşu esastır; kendiliğinden düşme, içsel istek ve karşılıklı çekişme bu kola girmez.","branch_image_ar":"مضي سريع وترامي في السير","concept_gloss":"hızlı yönlü ilerleme, atılımlı koşu ve sert yol alma","contextual_glosses":[{"applicability":"Bir varlığın aşağı ya da yukarı yönlü olarak süratle yol aldığı genel hareket bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yönlü hareketin hızlı ve kesintisiz ilerleme niteliğini korur."},"facet_ids":["F001"],"text":"hızla ilerledi","usage_role":"general"},{"applicability":"Yırtıcı kuşun yukarıdan hedefe doğru süratli bir atılış yaptığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kuşun hedefe doğru hızlı ve aşağı yönlü atılışını tam olarak korur."},"facet_ids":["F002"],"text":"kuş avına hızla daldı","usage_role":"contextual"}],"definition":"Bir varlığın aşağı ya da yukarı yönde hızla ilerlemesini ve sert yol alırken bedenini ileri atmasını anlatır. Yırtıcı kuşun dalışı, devenin hızlı koşusu, zorlu yol alma ve belirli çoğul biçimde çeşitli yol alış tarzları bu çekirdeğin özel gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Aşağı veya yukarı yönde hızlı ilerleme ve sert yol alışta bedenin ileri atılması."},{"facet_id":"F002","role":"specialization","statement":"Yırtıcı kuşun avına hızla dalması ve devenin güçlü, yüksek tempolu koşusu."},{"facet_id":"F003","role":"associated_use","statement":"Yolculukta çok hızlı ve sert biçimde ilerleme."},{"facet_id":"F004","role":"source_variant","statement":"Belirli çoğul biçimin çeşitli yol alış ve ilerleme tarzlarını adlandırması."}],"identity_rationale":"Kaynak ifadesi hızlı ve güçlü ilerlemeyi, iniş ya da yükseliş yönündeki süratli gidişi, yırtıcı kuşun dalışını, devenin hızlı koşusunu, sert yol almayı ve belirli çoğul biçimin yol alış türleri anlamını birlikte destekler.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"hızlı veya güçlü ilerleme"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yırtıcı kuş hızla daldı veya deve güçlü biçimde koştu"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"sert ve hızlı yol alma"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"çeşitli yol alış biçimleri"}],"lexicalization_note":"Genel hızlı ilerleme, hayvanlarla kurulan özel hareketler, sert yol alma ve yol alış türleri birbirinden ayrılarak tanımlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel hız, atılımlı koşu ve düşüşle sınırı en iyi gösteren üç dal seçildi, yalnız hayvan veya yolculuk alanını paylaşan adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol hareketin yönünü ve atılımlı beden hareketini vurgular; komşu hafif koşu, hızlı yürüyüş ve belirli hayvan yürüyüşü çevresinde daha geniştir.","focus_only":"Yukarı ve aşağı yön, kuşun dalışı, bedenin ileri atılması ve yol alış türleri bu kolda bulunur.","gloss":"hızla ilerlemek","neighbor_only":"Hafif koşu ve kurdun belirli yürüyüş biçimi komşuya özgüdür.","neighbor_ref":"root_001499/B002","relation_type":"near_synonym","shared_zone":"Her iki dal yürüme, koşma veya genel gidişte hızlı biçimde ilerlemeyi anlatır."},{"boundary_match":"partial","distinction":"Bu kol bedeni ileri atma ve yönlü hareket üzerinde durur; komşu genel yürüme, koşma ve yanlış işte acele etme alanlarına yayılır.","focus_only":"Yönlü iniş ve yükseliş, kuş dalışı ve çeşitli yol alış biçimleri bu kolda ayrıca bulunur.","gloss":"hızlı ve atılımlı gidiş","neighbor_only":"Hızın yanlış işte acele etmeye aktarılması komşuda açık bir uzantıdır.","neighbor_ref":"root_000481/B003","relation_type":"near_synonym","shared_zone":"Her iki dal deve ve başka varlıkların hızlı koşmasını veya yol almasını ifade eder."},{"boundary_match":"partial","distinction":"Bu kolda belirleyici özellik süratli ilerlemedir ve yere varma gerekmez; komşu kolda hareketin düşüş olması ve çoğu kez yüksekten aşağı gerçekleşmesi esastır.","focus_only":"Hız ve atılımlı yol alma, aşağı yön kadar yukarı yönü de kapsayan çekirdektir.","gloss":"hızlı iniş ile düşüş","neighbor_only":"Düşüşün kendisi, derin çukur, düşürme, ölüm ve art arda düşme komşu kolda bulunur.","neighbor_ref":"root_001609/B002","relation_type":"near_neighbor","shared_zone":"İki dal aşağı yönlü hareketi ve bir varlığın yukarıdan aşağı doğru gitmesini paylaşabilir."}],"source_phrase_ar":"الهوي في السير إذا مضى (sihah)؛ المهاواة شدة السير (sihah)؛ الهوي في السير إذا مضى (tahdhib)؛ الهوي السريع إلى أسفل والهوي السريع إلى فوق (tahdhib)؛ هوت العقاب إذا انقضت (tahdhib)؛ هوت الناقة تهوي إذا عدت عدوا أرفع العدو (tahdhib)؛ الهواهي ضروب من السير (tahdhib)؛ الهوي ذهاب في انحدار والهوي ذهاب في ارتفاع (mufradat)؛ الهوي ذهاب في انحدار والهوى في الارتفاع (maqayis)؛ شدة السير لما في ذلك من الترامي بالأبدان عند السير (maqayis)","source_summary":"Kaynaklar yönlü gidişin hızlı ve atılımlı oluşunu ortak çekirdek yapar; kuşun dalışı, devenin hızlı koşusu ve sert yolculuk bunun özel örnekleridir. Toplu ifade ayrıca bir çoğul biçimi çeşitli yol alış tarzları olarak kaydeder.","sources":["SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الهوي في السير إذا مضى أو أسرع، والهوي السريع إلى أسفل أو فوق، وانقضاض العقاب، وعدو الناقة أو الأتان، والمهاواة بمعنى شدة السير، والهواهي إذا فسرت بضروب السير.","what_is_not_ar":"ليس هو سقوط الشيء في مهواة فقط، ولا الهَوَى النفسي، ولا المهاواة بمعنى الملاجة."},"support_links":["sup_8214ecc5a71b35d0b2d4"]},{"boundary":"Çekişmenin karşılıklı ve ısrarlı olması esastır; hızlı yol alma, tek kişinin içsel isteği veya genel düşmanlık bu kola girmez.","branch_kind":"bare","branch_ref":"root_001609/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هَاوِيَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:haAwiyap|ROOT:hwy|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:2:1","qac_word_ref":"101:9:2","surface_ar":"هَاوِيَةٌ"}],"gloss":"karşılıklı inatlaşma ve çekişme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki tarafın bir anlaşmazlıkta karşılıklı biçimde inatlaşması ve çekişmeyi sürdürmesi."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Karşılıklılığın, her tarafın ötekinin yönelişine takılmasıyla açıklanması."}}],"root_ar":"ه و ي","root_id":"root_001609","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki tarafın birbirine bağlı biçimde sürdürdüğü ısrarlı anlaşmazlığın yalın biçim karşılığıdır.","boundary_detail":"Çekişmenin karşılıklı ve ısrarlı olması esastır; hızlı yol alma, tek kişinin içsel isteği veya genel düşmanlık bu kola girmez.","branch_image_ar":"مهاواة وملاجّة","concept_gloss":"karşılıklı inatlaşma ve çekişme","contextual_glosses":[{"applicability":"İki tarafın bir anlaşmazlığı karşılıklı ısrarla sürdürdüğü bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çekişmenin karşılıklı, inatçı ve devam eden niteliğini korur."},"facet_ids":["F001","F002"],"text":"birbirleriyle inatlaşıp çekiştiler","usage_role":"general"}],"definition":"İki tarafın bir anlaşmazlıkta birbirinin yönelişine takılarak karşılıklı ve ısrarlı biçimde çekişmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki tarafın bir anlaşmazlıkta karşılıklı biçimde inatlaşması ve çekişmeyi sürdürmesi."},{"facet_id":"F002","role":"associated_use","statement":"Karşılıklılığın, her tarafın ötekinin yönelişine takılmasıyla açıklanması."}],"identity_rationale":"Kaynak ifadesi biçimi doğrudan karşılıklı inatlaşma ve çekişme olarak açıklar; her tarafın tartışmada ötekinin yönelişine takılması bu karşılıklılığın gerekçesi olarak verilir. Geçici çerçeve bu yalın biçim anlamını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"karşılıklı inatlaşma ve çekişme"}],"lexicalization_note":"Tanım yalın biçimin karşılıklı inatlaşma ve çekişme anlamıyla sınırlıdır; yol alma kuruluşundan anlam aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; karşılıklılık, sözlü sıkıştırma ve sertlik sınırlarını gösteren üç çekişme dalı seçildi, alay ve genel düşmanlık gibi farklı çekirdekler dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol iki tarafın birbirine bağlı biçimde inatlaşmasını gerektirir; komşu genel çekişmeyi karşılıklılığın yapısını belirtmeden adlandırır.","focus_only":"Tarafların birbirinin yönelişine takılması ve karşılıklı ısrar bu kolda kurucu özelliktir.","gloss":"karşılıklı çekişme","neighbor_only":"Karşılıklılık ya da belirli bir inat gerekmeden genel kavga ve tartışma komşuda yeterlidir.","neighbor_ref":"root_000787/B011","relation_type":"near_synonym","shared_zone":"Her iki dal insanlar arasındaki sözlü veya davranışsal anlaşmazlık ve çekişmeyi anlatır."},{"boundary_match":"partial","distinction":"Bu kol karşılıklı ısrarın yapısını anlatır; komşu tartışmada rakibi sözle sıkıştırma ve sözünü eğip bükme biçimine odaklanır.","focus_only":"Her iki tarafın karşılıklı yönelişi ve inatlaşması bu kola özgüdür.","gloss":"tartışmada inatlaşma","neighbor_only":"Rakibi sözle eğip bükerek sıkıştırma biçimi komşuda ayrıca bulunur.","neighbor_ref":"root_001037/B012","relation_type":"near_synonym","shared_zone":"Her iki dal tarafların bir anlaşmazlığı sözlü çekişmeyle sürdürmesini ifade eder."},{"boundary_match":"partial","distinction":"Bu kol karşılıklılığı öne çıkarır; komşu çekişmenin sertliğini, üstün gelmeyi ve savunma yönünü ayrıca kapsar.","focus_only":"Tarafların birbirinin yönelişine takılarak karşılıklı çekişmesi bu kolda belirgindir.","gloss":"inatçı tartışma","neighbor_only":"Aşırı sertlik, tartışmada üstün gelme ve birini savunma kullanımları komşuda bulunur.","neighbor_ref":"root_001351/B001","relation_type":"near_synonym","shared_zone":"Her iki dal güçlü inat ve ısrarla sürdürülen bir anlaşmazlığı anlatır."}],"source_phrase_ar":"المهاواة الملاجة (sihah)؛ المهاواة فذكر أبو عمرو أنها الملاجة (maqayis)؛ أما الملاجة فلأن كل واحد منهما يحب هوى صاحبه (maqayis)","source_summary":"Kaynaklar yalın biçimi karşılıklı inatlaşma ve çekişme olarak verir; toplu ifade bu sürekliliği tarafların birbirinin yönelişine takılmasıyla açıklar.","sources":["SI","MQ"],"what_is_ar":"يدخل فيه المهاواة بمعنى الملاجة، وما علله المصدر بأن كل واحد يحب هوى صاحبه في المنازعة.","what_is_not_ar":"ليس هو شدة السير المسماة مهاواة، ولا الهَوَى النفسي المفرد، ولا السقوط."},"support_links":[]},{"boundary":"Odak, söylenen şeyin asılsız veya boş oluşudur; yalnız yanlış iddia, süslü aldatma ya da hareket biçimi bu kola girmez.","branch_kind":"bare","branch_ref":"root_001609/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هَاوِيَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:haAwiyap|ROOT:hwy|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:2:1","qac_word_ref":"101:9:2","surface_ar":"هَاوِيَةٌ"}],"gloss":"asılsız ve boş sözler","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gerçek dayanağı olmayan asılsız sözler ve uydurma anlatımlar."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bilgi veya anlam taşımayan boş ve gereksiz konuşmalar."}}],"root_ar":"ه و ي","root_id":"root_001609","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gerçek dayanağı bulunmayan veya anlam ve yarar taşımayan sözlerin yalın biçim karşılığıdır.","boundary_detail":"Odak, söylenen şeyin asılsız veya boş oluşudur; yalnız yanlış iddia, süslü aldatma ya da hareket biçimi bu kola girmez.","branch_image_ar":"هواهي القول الباطل","concept_gloss":"asılsız ve boş sözler","contextual_glosses":[{"applicability":"Bir söz yığınının hem gerçek dayanağı bulunmadığını hem de anlamlı içerik taşımadığını belirtmek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözlerin asılsız ve içeriksiz oluşunu doğal Türkçe anlatımla korur."},"facet_ids":["F001","F002"],"text":"asılsız ve boş laflar","usage_role":"general"}],"definition":"Gerçek dayanağı bulunmayan asılsız sözleri, boş konuşmayı ve anlam taşımayan lafları topluca anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gerçek dayanağı olmayan asılsız sözler ve uydurma anlatımlar."},{"facet_id":"F002","role":"extension","statement":"Bilgi veya anlam taşımayan boş ve gereksiz konuşmalar."}],"identity_rationale":"Kaynak ifadesi biçimi doğrudan asılsız sözler, boş konuşma ve anlamsız laf olarak verir. Geçici çerçeve bu söz alanını yol alış türleri, fiziksel boşluk ve yüreksiz kişi anlamlarından doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"asılsız ve boş sözler"}],"lexicalization_note":"Tanım yalın biçimin asılsız ve boş sözler anlamını korur; aynı biçimin yol alış türleri kullanımı bu kola taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eşdeğer dal ile yalan ve gösterişli boş konuşma sınırlarını açıklayan iki yakın dal seçildi, yalnız yanlış iddia veya süslü aldatma çekirdeği taşıyanlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Kanıttaki çekirdek ve kapsam bakımından anlamlı bir ayrım görünmez; iki dal aynı asılsız ve boş sözler alanında birbirinin yerine kullanılabilir.","focus_only":null,"gloss":"asılsız ve boş sözler","neighbor_only":null,"neighbor_ref":"root_000664/B014","relation_type":"synonym","shared_zone":"Her iki dal da gerçek dayanağı ve anlamlı içeriği bulunmayan asılsız sözleri topluca adlandırır."},{"boundary_match":"partial","distinction":"Bu kol asılsızlığın yanında genel boş lafı da kapsar; komşu sözün yalan ve temelsiz masal olmasını daha belirgin biçimde öne çıkarır.","focus_only":"Yalan olmasa bile anlamsız ve yararsız boş konuşmayı kapsama bu kolda daha açıktır.","gloss":"temelsiz yalanlar","neighbor_only":"Özellikle gerçek temeli olmayan yalan ve saçma masal niteliği komşuda daha belirgindir.","neighbor_ref":"root_000115/B004","relation_type":"near_synonym","shared_zone":"Her iki dal gerçek dayanağı bulunmayan asılsız sözleri ve saçma anlatımları kapsar."},{"boundary_match":"partial","distinction":"Bu kol içeriğin asılsız veya boş oluşuna odaklanır; komşu buna konuşanın gösterişli ve şişkin söyleyiş biçimini ekler.","focus_only":"Gerçek dışı sözlerin toplu adı olma bu kolda bulunur ve belirli bir söyleyiş tavrı gerektirmez.","gloss":"anlamsız gösterişli konuşma","neighbor_only":"Şişkin ve gösterişli konuşma tavrı komşunun gerekli anlatım özelliğidir.","neighbor_ref":"root_001170/B007","relation_type":"near_synonym","shared_zone":"Her iki dal anlamlı içerikten yoksun, boş konuşmayı anlatır."}],"source_phrase_ar":"الهواهي الباطل واللغو من القول (sihah)؛ الهواهي الأباطيل (tahdhib)","source_summary":"Kaynaklar biçimi asılsız sözler ve boş konuşma olarak ortaklaştırır; böylece hem gerçeklikten yoksunluğu hem de anlam ve yarar taşımayan lafı kapsar.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الهواهي إذا فسرت بالأباطيل أو الباطل واللغو من القول.","what_is_not_ar":"ليس هو الهواهي إذا فسرت بضروب السير، ولا الهَواء الخالي، ولا الهوهاءة بمعنى ضعف الفؤاد."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["101:9:1"],"branch_refs":[],"candidate_id":"cand_d5fd1453d9f3b4ca083d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:9:1:abrupt-verdict-sound","source_type":"word_analysis","support_ids":["sup_c8e5a6cfec1c68e3c32f","sup_cabd72232c6500db6230"],"title":"onset gives the result a sharp catch","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:1","qac_refs":["101:9:1:1"],"status":"accepted"}},{"anchor_refs":["101:9:1"],"branch_refs":[],"candidate_id":"cand_de5225995822a0353e74","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:9:1:consequence-fused-to-subject","source_type":"word_analysis","support_ids":["sup_80edaf53fb018cd09023","sup_cabd72232c6500db6230"],"title":"bound connector fuses result to the subject pivot","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:1","qac_refs":["101:9:1:1"],"status":"accepted"}},{"anchor_refs":["101:9:1"],"branch_refs":[],"candidate_id":"cand_21934dfc1cc9df22024c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:9:1:parallel-branch-shift","source_type":"word_analysis","support_ids":["sup_cabd72232c6500db6230","sup_f018203413b5ff31c4b7"],"title":"parallel opening exposes the subject shift","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:1","qac_refs":["101:9:1:1"],"status":"accepted"}},{"anchor_refs":["101:9:1"],"branch_refs":[],"candidate_id":"cand_bc2f58b5370306f76958","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:9:1:required-apodosis-link","source_type":"word_analysis","support_ids":["sup_29f883b75bae0826a5c7","sup_cabd72232c6500db6230"],"title":"required answer-particle completes the condition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:1","qac_refs":["101:9:1:1"],"status":"accepted"}},{"anchor_refs":["101:9:2"],"branch_refs":[],"candidate_id":"cand_c2d9887695bdd2215a31","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:9:2:compressed-refuge-ellipsis","source_type":"word_analysis","support_ids":["sup_580227251e2da8a29d68","sup_6fd46dfae2826f4ea6f4"],"title":"refuge meaning is compressed into the noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:2","qac_refs":["101:9:1:2","101:9:1:3"],"status":"accepted"}},{"anchor_refs":["101:9:2"],"branch_refs":[],"candidate_id":"cand_c8eb254ac25464227a6b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:9:2:measurement-to-identity-boundary","source_type":"word_analysis","support_ids":["sup_1b2d30849122845ff52a","sup_6fd46dfae2826f4ea6f4"],"title":"weighing result becomes source identity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:2","qac_refs":["101:9:1:2","101:9:1:3"],"status":"accepted"}},{"anchor_refs":["101:9:2"],"branch_refs":[],"candidate_id":"cand_22dbf3539dff3b30855b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:9:2:mother-source-refuge-reversal","source_type":"word_analysis","support_ids":["sup_31cc00496cfe97156af4","sup_6fd46dfae2826f4ea6f4"],"title":"mother-source shelter is reversed into abyss","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:2","qac_refs":["101:9:1:2","101:9:1:3"],"status":"accepted"}},{"anchor_refs":["101:9:2"],"branch_refs":[],"candidate_id":"cand_b34812235aba46f8666c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:9:2:possessive-antecedent-binding","source_type":"word_analysis","support_ids":["sup_6fd46dfae2826f4ea6f4","sup_d359b9067e05c130b4c0"],"title":"suffix binds scales and source to one person","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:2","qac_refs":["101:9:1:2","101:9:1:3"],"status":"accepted"}},{"anchor_refs":["101:9:2"],"branch_refs":[],"candidate_id":"cand_c74afe4a443ab8be5319","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:9:2:root-family-source-orientation","source_type":"word_analysis","support_ids":["sup_6fd46dfae2826f4ea6f4","sup_b794f81894a82b228854"],"title":"root family supplies source and orientation pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:2","qac_refs":["101:9:1:2","101:9:1:3"],"status":"accepted"}},{"anchor_refs":["101:9:2"],"branch_refs":[],"candidate_id":"cand_08f9b47426335534b077","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:9:2:sound-weight-after-light-scales","source_type":"word_analysis","support_ids":["sup_0d5b7673fefd43ffa511","sup_6fd46dfae2826f4ea6f4"],"title":"heavy nasal source follows light scales","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:2","qac_refs":["101:9:1:2","101:9:1:3"],"status":"accepted"}},{"anchor_refs":["101:9:2"],"branch_refs":[],"candidate_id":"cand_5844f57768d3f46cb3c1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:9:2:subject-pivot-not-object","source_type":"word_analysis","support_ids":["sup_6fd46dfae2826f4ea6f4","sup_e87ec7ad9f0a9d5b06d2"],"title":"possessed source becomes the subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:2","qac_refs":["101:9:1:2","101:9:1:3"],"status":"accepted"}},{"anchor_refs":["101:9:2"],"branch_refs":[],"candidate_id":"cand_05ac3564d214b8e489ad","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:9:2:variant-scope-test","source_type":"word_analysis","support_ids":["sup_56be953577bb80748302","sup_6fd46dfae2826f4ea6f4"],"title":"variant forms test vowel and scope","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:2","qac_refs":["101:9:1:2","101:9:1:3"],"status":"accepted"}},{"anchor_refs":["101:9:3"],"branch_refs":[],"candidate_id":"cand_c0d8e7ce7e242dcb9f60","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001609"],"scope":"focus_ayah","source_local_id":"101:9:3:active-participle-motion","source_type":"word_analysis","support_ids":["sup_0980cbfc8b4591450504","sup_44e18deb46ea0a1ef322"],"title":"active form keeps falling in motion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:3","qac_refs":["101:9:2:1"],"status":"accepted"}},{"anchor_refs":["101:9:3"],"branch_refs":[],"candidate_id":"cand_3e1f2cb7d67353f9bf03","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001609"],"scope":"focus_ayah","source_local_id":"101:9:3:closure-vertical-descent","source_type":"word_analysis","support_ids":["sup_0980cbfc8b4591450504","sup_2c9a850fb8b6c7d19f4f"],"title":"final word turns weighing into descent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:3","qac_refs":["101:9:2:1"],"status":"accepted"}},{"anchor_refs":["101:9:3"],"branch_refs":[],"candidate_id":"cand_13371861bf9afe1fb69e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001609"],"scope":"focus_ayah","source_local_id":"101:9:3:deep-abyss-verdict","source_type":"word_analysis","support_ids":["sup_0980cbfc8b4591450504","sup_c96640e1e5b88b0c30fa"],"title":"abyss image supplies the negative endpoint","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:3","qac_refs":["101:9:2:1"],"status":"accepted"}},{"anchor_refs":["101:9:3"],"branch_refs":[],"candidate_id":"cand_67a7431ba5e4e5f68f17","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001609"],"scope":"focus_ayah","source_local_id":"101:9:3:desire-void-root-pressure","source_type":"word_analysis","support_ids":["sup_0980cbfc8b4591450504","sup_ce9e2af1f83e11f6ad60"],"title":"desire and void pressure qualify the falling-place","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:3","qac_refs":["101:9:2:1"],"status":"accepted"}},{"anchor_refs":["101:9:3"],"branch_refs":[],"candidate_id":"cand_024ead9d31ca773d32af","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001609"],"scope":"focus_ayah","source_local_id":"101:9:3:forward-fire-gloss","source_type":"word_analysis","support_ids":["sup_0980cbfc8b4591450504","sup_98020f08ff8873b07854"],"title":"abyss-name is answered by hot fire","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:3","qac_refs":["101:9:2:1"],"status":"accepted"}},{"anchor_refs":["101:9:3"],"branch_refs":[],"candidate_id":"cand_3947aaface1d18e0620d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001609"],"scope":"focus_ayah","source_local_id":"101:9:3:hawi-hami-sound-bridge","source_type":"word_analysis","support_ids":["sup_07cdfc33ce22fd4193e1","sup_0980cbfc8b4591450504"],"title":"similar cadence links abyss to fire","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:3","qac_refs":["101:9:2:1"],"status":"accepted"}},{"anchor_refs":["101:9:3"],"branch_refs":[],"candidate_id":"cand_40e4ed8752de754aec84","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001609"],"scope":"focus_ayah","source_local_id":"101:9:3:mother-container-abyss","source_type":"word_analysis","support_ids":["sup_0980cbfc8b4591450504","sup_8dee83dcba0a2ea9c885"],"title":"abyss borrows the mother-container role","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:3","qac_refs":["101:9:2:1"],"status":"accepted"}},{"anchor_refs":["101:9:3"],"branch_refs":[],"candidate_id":"cand_cff5b4c428f0b14d05d4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001609"],"scope":"focus_ayah","source_local_id":"101:9:3:predicate-identity","source_type":"word_analysis","support_ids":["sup_0980cbfc8b4591450504","sup_99a641c6c638376fe4b0"],"title":"predicate makes abyss an identity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:3","qac_refs":["101:9:2:1"],"status":"accepted"}},{"anchor_refs":["101:9:3"],"branch_refs":[],"candidate_id":"cand_4c30415957f57893f841","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001609"],"scope":"focus_ayah","source_local_id":"101:9:3:root-analysis-boundary","source_type":"word_analysis","support_ids":["sup_0980cbfc8b4591450504","sup_59d29d1b988f0824bf47"],"title":"root dispute limits etymological overreach","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:3","qac_refs":["101:9:2:1"],"status":"accepted"}},{"anchor_refs":["101:9:3"],"branch_refs":[],"candidate_id":"cand_7b44add0ee8dd3cad18e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001609"],"scope":"focus_ayah","source_local_id":"101:9:3:sound-and-rarity-concentration","source_type":"word_analysis","support_ids":["sup_0980cbfc8b4591450504","sup_78bb517064f8b7e2627e"],"title":"rare form and breathy sound concentrate the root field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:3","qac_refs":["101:9:2:1"],"status":"accepted"}},{"anchor_refs":["101:9:3"],"branch_refs":[],"candidate_id":"cand_1dc4594d76d2fa4e0a3e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001609"],"scope":"focus_ayah","source_local_id":"101:9:3:tanwin-description-name","source_type":"word_analysis","support_ids":["sup_0980cbfc8b4591450504","sup_a73a527eed0d7e6efe81"],"title":"tanwīn holds description and name together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:9:3","qac_refs":["101:9:2:1"],"status":"accepted"}},{"anchor_refs":["101:9:1"],"branch_refs":[],"candidate_id":"cand_eeac2a9a40b5570faef0","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000053"],"scope":"focus_ayah","source_local_id":"101:9:1:2","source_type":"qac_morpheme","support_ids":["sup_efa3bb1890de724609b0"],"title":"QAC root occurrence: ء م م","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["101:9:2"],"branch_refs":[],"candidate_id":"cand_c659c64ecc8b6f650158","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001609"],"scope":"focus_ayah","source_local_id":"101:9:2:1","source_type":"qac_morpheme","support_ids":["sup_01a8357d1d550e062e95"],"title":"QAC root occurrence: ه و ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["101:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:9","branch_refs":["root_000053/B001","root_001609/B002"],"candidate_id":"cand_806fdff7f00274cc81b6","commentary_obligation":"review","hft_ref":"hft_22a78adbecf25c096a3c","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_maternal_reversal","source_type":"hft","support_ids":["sup_468cd99ebff6e6d8d1ec"],"title":"baseline_maternal_reversal","trust":"legacy_unbound"},{"anchor_refs":["101:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:9","branch_refs":["root_000053/B002","root_001609/B001","root_001609/B002"],"candidate_id":"cand_e5df16ecbc308492da67","commentary_obligation":"review","hft_ref":"hft_bc81668c9279eb241a42","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_void_as_return_center","source_type":"hft","support_ids":["sup_fe446e14ae20f3850177"],"title":"baseline_void_as_return_center","trust":"legacy_unbound"},{"anchor_refs":["101:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:9","branch_refs":["root_000053/B012","root_001609/B002","root_001609/B008"],"candidate_id":"cand_f21f98910b05ab991010","commentary_obligation":"review","hft_ref":"hft_3c862a0d35a0bdda5c77","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_compressed_trajectory","source_type":"hft","support_ids":["sup_8214ecc5a71b35d0b2d4"],"title":"baseline_compressed_trajectory","trust":"legacy_unbound"},{"anchor_refs":["101:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:9","branch_refs":["root_000053/B003","root_001609/B007"],"candidate_id":"cand_0bad8584d81324f0b419","commentary_obligation":"review","hft_ref":"hft_f82bd348af87c651b300","kind":"surprising_outlier","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:outlier_cranial_hollow","source_type":"hft","support_ids":["sup_337d33c3c239c33b49eb"],"title":"outlier_cranial_hollow","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فَأُمُّهُۥ هَاوِيَةٌۭ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:RSLT+","morpheme_role":"PREFIX","pos":"RSLT","qac_ref":"101:9:1:1","qac_word_ref":"101:9:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"أُمّ","morph_features":"STEM|POS:N|LEM:>um~|ROOT:Amm|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:1:2","qac_word_ref":"101:9:1","root_ar":"ء م م","surface_ar":"أُمُّ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"101:9:1:3","qac_word_ref":"101:9:1","root_ar":"","surface_ar":"هُۥ"},{"lemma_ar":"هَاوِيَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:haAwiyap|ROOT:hwy|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:2:1","qac_word_ref":"101:9:2","root_ar":"ه و ي","surface_ar":"هَاوِيَةٌ"}],"word_analysis_qac_refs":[["101:9:1:1"],["101:9:1:2","101:9:1:3"],["101:9:2:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["101:9:1","101:9:2","101:9:3"]},"focus_surface_evidence":{"arabic_uthmani":"فَأُمُّهُۥ هَاوِيَةٌۭ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:RSLT+","morpheme_role":"PREFIX","pos":"RSLT","qac_ref":"101:9:1:1","qac_word_ref":"101:9:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"أُمّ","morph_features":"STEM|POS:N|LEM:>um~|ROOT:Amm|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:1:2","qac_word_ref":"101:9:1","root_ar":"ء م م","surface_ar":"أُمُّ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"101:9:1:3","qac_word_ref":"101:9:1","root_ar":"","surface_ar":"هُۥ"},{"lemma_ar":"هَاوِيَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:haAwiyap|ROOT:hwy|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:9:2:1","qac_word_ref":"101:9:2","root_ar":"ه و ي","surface_ar":"هَاوِيَةٌ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["101:9:1:1"],["101:9:1:2","101:9:1:3"],["101:9:2:1"]],"word_analysis_refs":["101:9:1","101:9:2","101:9:3"],"word_rows":[{"analysis_record_ref":"101:9:1","analytic_gloss_range_en":"causal and apodosis connector introducing the consequence of the light-scales condition","analytic_root_gloss_range_en":null,"qac_refs":["101:9:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"فَ","transliteration":"fa-"}},{"analysis_record_ref":"101:9:2","analytic_gloss_range_en":"his mother, source, origin, or refuge; locally a possessed source/refuge subject identified by the following predicate","analytic_root_gloss_range_en":"broad family of mother, source, foundation, community, and orientation; the local clause selects the possessed source/refuge layer while keeping the mother shock audible","qac_refs":["101:9:1:2","101:9:1:3"],"root":{"arabic":"أ م م","transliteration":"ʾ-m-m"},"surface":{"arabic":"أُمُّهُۥ","transliteration":"ummuhu"}},{"analysis_record_ref":"101:9:3","analytic_gloss_range_en":"plunging abyss or Hāwiya as predicate; active-participle form preserves falling motion inside the nominal verdict","analytic_root_gloss_range_en":"accepted branches include falling into an abyss, void or empty air, desire and inclination, hand-motion, bewilderment, time-span, hollowness, swift travel, contention, and idle speech; the local predicate selects the abyss/falling branch while allowing desire and void pressure as qualified root-field resonance","qac_refs":["101:9:2:1"],"root":{"arabic":"ه و ي","transliteration":"h-w-y"},"surface":{"arabic":"هَاوِيَةٌۭ","transliteration":"hāwiyatun"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["101:9"],"branch_refs":["root_000053/B001","root_001609/B002"],"candidate_id":"cand_806fdff7f00274cc81b6","evidence_scope":"focus_ayah","hft_ref":"hft_22a78adbecf25c096a3c","item_id":"baseline_maternal_reversal","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_maternal_reversal","support_id":"sup_468cd99ebff6e6d8d1ec"},{"anchor_refs":["101:9"],"branch_refs":["root_000053/B002","root_001609/B001","root_001609/B002"],"candidate_id":"cand_e5df16ecbc308492da67","evidence_scope":"focus_ayah","hft_ref":"hft_bc81668c9279eb241a42","item_id":"baseline_void_as_return_center","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_void_as_return_center","support_id":"sup_fe446e14ae20f3850177"},{"anchor_refs":["101:9"],"branch_refs":["root_000053/B012","root_001609/B002","root_001609/B008"],"candidate_id":"cand_f21f98910b05ab991010","evidence_scope":"focus_ayah","hft_ref":"hft_3c862a0d35a0bdda5c77","item_id":"baseline_compressed_trajectory","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_compressed_trajectory","support_id":"sup_8214ecc5a71b35d0b2d4"},{"anchor_refs":["101:9"],"branch_refs":["root_000053/B003","root_001609/B007"],"candidate_id":"cand_0bad8584d81324f0b419","evidence_scope":"focus_ayah","hft_ref":"hft_f82bd348af87c651b300","item_id":"outlier_cranial_hollow","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_cranial_hollow","support_id":"sup_337d33c3c239c33b49eb"}],"diagnostics":[],"lane_counts":{"global":10,"macro":14,"micro":4},"packet_summary":{"ayah_count":11,"focus_ref":"101:9","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["101:1","101:2","101:3","101:4","101:5","101:6","101:7","101:8","101:9","101:10","101:11"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"101:9","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":18,"unstructured_record_count":0},"identity":{"ayah_ref":"101:9","lane":"micro","linguistic_source_ref":"101:9","surface_ref":"101:9","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"101:9","target_tokens":[["onun",["101:9:1"]],["anası",["101:9:1"]],["bir",["101:9:2"]],["uçurumdur",["101:9:2"]]],"text":"onun anası bir uçurumdur."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":11,"id":"s101-p01-001-011","label":"Whole surah","number":1,"refs":["101:1","101:2","101:3","101:4","101:5","101:6","101:7","101:8","101:9","101:10","101:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"101:9:2:1","source_type":"qac_morpheme","support_id":"sup_01a8357d1d550e062e95","text":"{\"lemma_ar\":\"هَاوِيَة\",\"morph_features\":\"STEM|POS:N|ACT|PCPL|LEM:haAwiyap|ROOT:hwy|F|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"101:9:2:1\",\"qac_word_ref\":\"101:9:2\",\"root_ar\":\"ه و ي\",\"surface_ar\":\"هَاوِيَةٌ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:3:hawi-hami-sound-bridge","source_type":"word_analysis","support_id":"sup_07cdfc33ce22fd4193e1","text":"{\"blocking_evidence\":null,\"headline\":\"similar cadence links abyss to fire\",\"reader_payoff\":\"The reader notices that the similar ending of {{ar:هَاوِيَةٌۭ}} ({{tr:hāwiyatun}}) and {{ar:حَامِيَةٌۢ}} ({{tr:ḥāmiyah}}) binds the abyss-name to its fiery explanation in 101:11.\",\"reason\":\"The CRITICAL rows give a concrete 101:11 anchor, and the similar terminal forms are visible in the local and forward-glossed wording.\",\"representative_source_ids\":[\"MI-13a7ba85\",\"QE-7ae17206\",\"QP-8b3e1b8d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:3","source_type":"word_analysis","support_id":"sup_0980cbfc8b4591450504","text":"{\"gloss_range\":\"plunging abyss or Hāwiya as predicate; active-participle form preserves falling motion inside the nominal verdict\",\"prose\":\"{{ar:هَاوِيَةٌۭ}} ({{tr:hāwiyatun}}) is the predicate of {{ar:أُمُّهُۥ}} ({{tr:ummuhu}}), so the clause equates his source/refuge with an abyss rather than narrating that he is sent toward one. Its active-participle shape keeps motion inside the noun: the verdict names a falling or plunging reality, not a static label only. The predicate also borrows the mother-container role from its subject, so the place that should shelter or receive becomes the swallowing relation itself. The tanwīn lets the predicate be heard both qualitatively, as a plunging abyss, and almost as a name, Hāwiya, while the following question in 101:10 and answer {{ar:نَارٌ حَامِيَةٌۢ}} ({{tr:nārun ḥāmiyah}}) in 101:11 specify it as burning fire without erasing the falling image; the similar cadence between the abyss-name and the hot-fire answer binds the name to its explanation. The root field supports the selected abyss branch, and it also gives qualified pressure from desire and void: the same field can name pull, empty air, and descent, but local syntax selects the falling-place sense, and the accepted root analysis keeps that etymological pressure bounded. At the ayah's close, the scene turns from the horizontal weighing of 101:8 into vertical plunge, and the marked, rare participial form plus the open, breathy sound of {{ar:هَاوِيَةٌۭ}} ({{tr:hāwiyatun}}) leave the result clause landing on descent.\",\"root_display\":\"{{ar:ه و ي}} ({{tr:h-w-y}})\",\"root_gloss_range\":\"accepted branches include falling into an abyss, void or empty air, desire and inclination, hand-motion, bewilderment, time-span, hollowness, swift travel, contention, and idle speech; the local predicate selects the abyss/falling branch while allowing desire and void pressure as qualified root-field resonance\",\"surface_display\":\"{{ar:هَاوِيَةٌۭ}} ({{tr:hāwiyatun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:2:sound-weight-after-light-scales","source_type":"word_analysis","support_id":"sup_0d5b7673fefd43ffa511","text":"{\"blocking_evidence\":null,\"headline\":\"heavy nasal source follows light scales\",\"reader_payoff\":\"The reader notices the sound movement from the prior possessive ending into the doubled nasal core of the source word after the light-scales condition.\",\"reason\":\"The surface shares the {{ar:ـهُ}} ({{tr:-hu}}) suffix with {{ar:مَوَازِينُهُۥ}} ({{tr:mawāzīnuhu}}), and {{ar:أُمّ}} ({{tr:umm}}) contains the doubled nasal that the CRITICAL rows identify.\",\"representative_source_ids\":[\"QP-b539582f\",\"QP-e704c8b2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:2:measurement-to-identity-boundary","source_type":"word_analysis","support_id":"sup_1b2d30849122845ff52a","text":"{\"blocking_evidence\":null,\"headline\":\"weighing result becomes source identity\",\"reader_payoff\":\"The reader notices the boundary shift from evaluated scales to a standing nominal identity: what the scales disclose determines what his refuge is.\",\"reason\":\"The attachment evidence treats 101:9 as a nominal result clause, so the boundary from the preceding light-scales condition to an identity statement is structurally supported.\",\"representative_source_ids\":[\"QB-79fb10dc\",\"QB-a96553a8\",\"QB-acfbdbbe\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:1:required-apodosis-link","source_type":"word_analysis","support_id":"sup_29f883b75bae0826a5c7","text":"{\"blocking_evidence\":null,\"headline\":\"required answer-particle completes the condition\",\"reader_payoff\":\"The reader notices that 101:8 remains grammatically suspended until this first particle supplies the required consequence in 101:9.\",\"reason\":\"QAC and attachment evidence identify {{ar:فَ}} ({{tr:fa-}}) as the answer to the immediately preceding {{ar:أَمَّا مَنْ}} ({{tr:ammā man}}) condition, so the cross-ayah dependency is locally forced.\",\"representative_source_ids\":[\"QG-9d2c171b\",\"QG-b80f3aca\",\"QB-dd4f06f9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:3:closure-vertical-descent","source_type":"word_analysis","support_id":"sup_2c9a850fb8b6c7d19f4f","text":"{\"blocking_evidence\":null,\"headline\":\"final word turns weighing into descent\",\"reader_payoff\":\"The reader notices the spatial turn: the horizontal balance scene of 101:8 closes in 101:9 on a vertical plunge.\",\"reason\":\"The final predicate carries the accepted falling branch of {{ar:ه و ي}} ({{tr:h-w-y}}) and occupies the closure position of the result clause.\",\"representative_source_ids\":[\"QT-601c862f\",\"QT-cc673845\",\"QB-fb02adc8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:2:mother-source-refuge-reversal","source_type":"word_analysis","support_id":"sup_31cc00496cfe97156af4","text":"{\"blocking_evidence\":null,\"headline\":\"mother-source shelter is reversed into abyss\",\"reader_payoff\":\"The reader notices the word's double force: the intimate mother shock remains while the local predicate makes source and refuge the selected sense.\",\"reason\":\"The local predication to {{ar:هَاوِيَةٌۭ}} ({{tr:hāwiyatun}}) licenses source/refuge readings of {{ar:أُمّ}} ({{tr:umm}}), while the surface noun still preserves the mother layer.\",\"representative_source_ids\":[\"QG-5f13e8b4\",\"QS-0c5d1e3b\",\"QS-ea65c1c4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:3:active-participle-motion","source_type":"word_analysis","support_id":"sup_44e18deb46ea0a1ef322","text":"{\"blocking_evidence\":null,\"headline\":\"active form keeps falling in motion\",\"reader_payoff\":\"The reader notices that the abyss is worded as a falling or plunging participial reality, so motion survives inside the nominal verdict.\",\"reason\":\"QAC identifies the form as an active participle, and V4 accepts the falling-into-an-abyss branch for {{ar:ه و ي}} ({{tr:h-w-y}}).\",\"representative_source_ids\":[\"QG-2338c467\",\"QF-dcd79090\",\"QY-66e66f0b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:2:variant-scope-test","source_type":"word_analysis","support_id":"sup_56be953577bb80748302","text":"{\"blocking_evidence\":null,\"headline\":\"variant forms test vowel and scope\",\"reader_payoff\":\"The reader notices how much the canonical suffix does: vowel variation leaves the possessed source intact, but the community variant changes the scale of the subject.\",\"reason\":\"The variants are useful as contrast, while the local canonical parse remains the possessed singular subject {{ar:أُمُّهُۥ}} ({{tr:ummuhu}}).\",\"representative_source_ids\":[\"QF-1113e39e\",\"QF-349cdd83\",\"QE-297d11cd\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:2:compressed-refuge-ellipsis","source_type":"word_analysis","support_id":"sup_580227251e2da8a29d68","text":"{\"blocking_evidence\":null,\"headline\":\"refuge meaning is compressed into the noun\",\"reader_payoff\":\"The reader notices that the surface keeps one compact noun where an explicit refuge or resting-place term could have made the destination easier but less charged.\",\"reason\":\"The grammar supports the source/refuge reading inside the nominal clause without requiring an added explicit refuge noun in the surface wording.\",\"representative_source_ids\":[\"QT-a12ab79e\",\"QY-bae9a9a1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:3:root-analysis-boundary","source_type":"word_analysis","support_id":"sup_59d29d1b988f0824bf47","text":"{\"blocking_evidence\":null,\"headline\":\"root dispute limits etymological overreach\",\"reader_payoff\":\"The reader notices that the falling/desire reading depends on the accepted {{ar:ه و ي}} ({{tr:h-w-y}}) analysis, so etymological pressure should be used with a clear boundary.\",\"reason\":\"The disputed analysis does not overturn the local predicate, but it cautions against making every etymological claim stronger than the accepted {{ar:ه و ي}} ({{tr:h-w-y}}) evidence permits.\",\"representative_source_ids\":[\"QS-8f09ce4e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:2","source_type":"word_analysis","support_id":"sup_6fd46dfae2826f4ea6f4","text":"{\"gloss_range\":\"his mother, source, origin, or refuge; locally a possessed source/refuge subject identified by the following predicate\",\"prose\":\"{{ar:أُمُّهُۥ}} ({{tr:ummuhu}}) carries the judged person forward by suffix rather than by an independent pronoun. The final {{ar:ـهُ}} ({{tr:-hu}}) resumes the person from 101:8 and repeats the possessive ending of {{ar:مَوَازِينُهُۥ}} ({{tr:mawāzīnuhu}}), so the measured scales and the named source belong to the same antecedent. Grammatically the noun is the nominative subject of a verbless clause, not an object of an omitted action; the ayah does not say simply that he is in a place, but makes his possessed {{ar:أُمّ}} ({{tr:umm}}) the pivot of the verdict. The word's range lets mother, source, and refuge operate together: the surface shock of mother remains, while the predicate {{ar:هَاوِيَةٌۭ}} ({{tr:hāwiyatun}}) selects the source/refuge layer and reverses shelter into abyss. That refuge force is compressed into the single possessed noun rather than spelled out with an explicit refuge or resting-place term, and the wider family pressure of source, community, and orientation is narrowed into this singular possessed source. Variant pressure sharpens the Hafs form: {{ar:فَإِمُّهُ}} ({{tr:fa-immuhu}}) changes the vowel without changing the possessed source analysis, while {{ar:فَأُمَّةٌ}} ({{tr:fa-ummatun}}) shows how different the clause becomes when the suffix disappears and a community becomes the subject. The doubled {{ar:مّ}} ({{tr:mm}}) also matters: after the light scales of 101:8, the source word lands with a heavy nasal center.\",\"root_display\":\"{{ar:أ م م}} ({{tr:ʾ-m-m}})\",\"root_gloss_range\":\"broad family of mother, source, foundation, community, and orientation; the local clause selects the possessed source/refuge layer while keeping the mother shock audible\",\"surface_display\":\"{{ar:أُمُّهُۥ}} ({{tr:ummuhu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:3:sound-and-rarity-concentration","source_type":"word_analysis","support_id":"sup_78bb517064f8b7e2627e","text":"{\"blocking_evidence\":null,\"headline\":\"rare form and breathy sound concentrate the root field\",\"reader_payoff\":\"The reader notices that the marked final form is not routine root usage; its breathy open sound and rarity concentrate the falling effect at closure.\",\"reason\":\"QAC supports the active-participle form, and the contextual profile marks the local root/form as a limited distribution where this predicate is not a routine occurrence.\",\"representative_source_ids\":[\"QI-a92d13ea\",\"QP-e54b5335\",\"QH-23e306b9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:1:consequence-fused-to-subject","source_type":"word_analysis","support_id":"sup_80edaf53fb018cd09023","text":"{\"blocking_evidence\":null,\"headline\":\"bound connector fuses result to the subject pivot\",\"reader_payoff\":\"The reader notices that the result marker is not merely nearby; it is bound to the word that names the unexpected subject of the verdict.\",\"reason\":\"The surface begins with a proclitic connector on {{ar:أُمُّهُۥ}} ({{tr:ummuhu}}), and the attachment evidence treats the whole clause as the result of the prior condition.\",\"representative_source_ids\":[\"QS-81ecbaee\",\"QF-976a0067\",\"QT-35a8edad\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:3:mother-container-abyss","source_type":"word_analysis","support_id":"sup_8dee83dcba0a2ea9c885","text":"{\"blocking_evidence\":null,\"headline\":\"abyss borrows the mother-container role\",\"reader_payoff\":\"The reader notices that the abyss receives the role expected of mother/source: the place that should shelter is the thing that swallows.\",\"reason\":\"The syntactically forced predication between {{ar:أُمُّهُۥ}} ({{tr:ummuhu}}) and {{ar:هَاوِيَةٌۭ}} ({{tr:hāwiyatun}}) supports the container/source reversal without needing to invent a separate topic from context evidence.\",\"representative_source_ids\":[\"QS-f629896a\",\"QI-8b16e5f8\",\"QE-8903cde0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:3:forward-fire-gloss","source_type":"word_analysis","support_id":"sup_98020f08ff8873b07854","text":"{\"blocking_evidence\":null,\"headline\":\"abyss-name is answered by hot fire\",\"reader_payoff\":\"The reader notices that {{ar:هَاوِيَةٌۭ}} ({{tr:hāwiyatun}}) creates a forward question in 101:10 and receives the fiery specification {{ar:نَارٌ حَامِيَةٌۢ}} ({{tr:nārun ḥāmiyah}}) in 101:11.\",\"reason\":\"The context-window evidence explicitly points from {{ar:هَاوِيَةٌۭ}} ({{tr:hāwiyatun}}) to the clarification question in 101:10 and answer in 101:11.\",\"representative_source_ids\":[\"QI-e94dc084\",\"QE-3a4d6312\",\"QB-ad55e3dd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:3:predicate-identity","source_type":"word_analysis","support_id":"sup_99a641c6c638376fe4b0","text":"{\"blocking_evidence\":null,\"headline\":\"predicate makes abyss an identity\",\"reader_payoff\":\"The reader notices that the grammar does not merely locate the person near an abyss; it identifies his source/refuge with it.\",\"reason\":\"QAC and attachment evidence mark {{ar:هَاوِيَةٌۭ}} ({{tr:hāwiyatun}}) as the nominative khabar of {{ar:أُمُّهُۥ}} ({{tr:ummuhu}}), not an object or governed destination.\",\"representative_source_ids\":[\"QG-06a33133\",\"QG-bcc90199\",\"QT-40c6eba2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:3:tanwin-description-name","source_type":"word_analysis","support_id":"sup_a73a527eed0d7e6efe81","text":"{\"blocking_evidence\":null,\"headline\":\"tanwīn holds description and name together\",\"reader_payoff\":\"The reader notices that the ending allows both a qualitative abyss and a name-like destination to be heard before the next ayahs identify it.\",\"reason\":\"QAC notes the tanwīn can be heard as indefiniteness or proper-name tanwīn, and the context-window warning says the following question and answer should be kept in view.\",\"representative_source_ids\":[\"QG-44b21693\",\"QF-b1df62b5\",\"QY-d783267a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:2:root-family-source-orientation","source_type":"word_analysis","support_id":"sup_b794f81894a82b228854","text":"{\"blocking_evidence\":null,\"headline\":\"root family supplies source and orientation pressure\",\"reader_payoff\":\"The reader notices that a frequent root family of source, community, and orientation is narrowed here into a singular possessed source.\",\"reason\":\"QAC supports a broad range for {{ar:أُمّ}} ({{tr:umm}}), and contextual data shows frequent root use, but no V4 rows are available for {{ar:أ م م}} ({{tr:ʾ-m-m}}); the local payoff should therefore stay with source/refuge orientation rather than activating every side branch.\",\"representative_source_ids\":[\"QS-677fded4\",\"QI-79894904\",\"QI-b9ff2da3\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:1:abrupt-verdict-sound","source_type":"word_analysis","support_id":"sup_c8e5a6cfec1c68e3c32f","text":"{\"blocking_evidence\":null,\"headline\":\"onset gives the result a sharp catch\",\"reader_payoff\":\"The reader notices the sound of the result as abrupt, with the connector meeting the hamza at the start of {{ar:أُمُّهُۥ}} ({{tr:ummuhu}}).\",\"reason\":\"The local surface has {{ar:فَـ}} ({{tr:fa-}}) immediately before the hamza of {{ar:أُمُّهُۥ}} ({{tr:ummuhu}}), so the phonetic observation is locally anchored.\",\"representative_source_ids\":[\"QP-b95fd55a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:3:deep-abyss-verdict","source_type":"word_analysis","support_id":"sup_c96640e1e5b88b0c30fa","text":"{\"blocking_evidence\":null,\"headline\":\"abyss image supplies the negative endpoint\",\"reader_payoff\":\"The reader notices that the predicate is not a generic bad outcome but a deep falling-place that converts light scales into ruinous descent.\",\"reason\":\"The local predicate selects the abyss/falling-place branch, and V4 lists {{ar:الهاوية}} ({{tr:al-hāwiyah}}) under the accepted abyss or Hell sense.\",\"representative_source_ids\":[\"QS-889e47c5\",\"QS-c5dba478\",\"QS-d3d5bc90\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:1","source_type":"word_analysis","support_id":"sup_cabd72232c6500db6230","text":"{\"gloss_range\":\"causal and apodosis connector introducing the consequence of the light-scales condition\",\"prose\":\"{{ar:فَ}} ({{tr:fa-}}) does not open a detached sentence; it supplies the required answer to the preceding {{ar:أَمَّا}} ({{tr:ammā}}) condition from 101:8. The particle therefore makes the whole nominal clause a consequence: once the scales are light, the result arrives immediately as {{ar:فَأُمُّهُۥ هَاوِيَةٌۭ}} ({{tr:fa-ummuhu hāwiyatun}}). Because the connector is prefixed to {{ar:أُمُّهُۥ}} ({{tr:ummuhu}}), consequence and subject pivot are heard together. It also echoes the positive branch opening {{ar:فَهُوَ}} ({{tr:fa-huwa}}) in 101:7, so the negative branch sounds parallel before it sharply replaces direct person-reference with the possessed source, {{ar:أُمُّهُۥ}} ({{tr:ummuhu}}). Even the onset has force: {{ar:فَـ}} ({{tr:fa-}}) runs into the hamza of {{ar:أُمُّهُۥ}} ({{tr:ummuhu}}), giving the verdict a clipped hinge rather than a loose narrative transition.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa-}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:3:desire-void-root-pressure","source_type":"word_analysis","support_id":"sup_ce9e2af1f83e11f6ad60","text":"{\"blocking_evidence\":null,\"headline\":\"desire and void pressure qualify the falling-place\",\"reader_payoff\":\"The reader notices that the selected abyss sense is surrounded by root-field pressure from desire and empty air, making descent feel like pull into emptiness.\",\"reason\":\"V4 accepts desire and void branches for {{ar:ه و ي}} ({{tr:h-w-y}}), but local syntax and lexical sense select the abyss/falling-place branch; desire and void therefore survive as qualified root-field resonance, not as the direct local gloss.\",\"representative_source_ids\":[\"QS-ab3d28c1\",\"QS-fd0b3686\",\"QE-6b873ef4\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:2:possessive-antecedent-binding","source_type":"word_analysis","support_id":"sup_d359b9067e05c130b4c0","text":"{\"blocking_evidence\":null,\"headline\":\"suffix binds scales and source to one person\",\"reader_payoff\":\"The reader notices that the judged person is carried into the result by possession: his scales and his source/refuge are linked by the same suffix.\",\"reason\":\"Attachment evidence marks the suffix on {{ar:أُمُّهُۥ}} ({{tr:ummuhu}}) as a possessive resumptive reference to the conditional person from 101:8.\",\"representative_source_ids\":[\"QG-4cdf7ec4\",\"QG-7b74f7ba\",\"QE-911d6776\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:2:subject-pivot-not-object","source_type":"word_analysis","support_id":"sup_e87ec7ad9f0a9d5b06d2","text":"{\"blocking_evidence\":null,\"headline\":\"possessed source becomes the subject\",\"reader_payoff\":\"The reader notices that the negative branch pivots away from an expected direct pronoun and makes the possessed source/refuge the grammatical topic.\",\"reason\":\"QAC and attachment evidence place {{ar:أُمُّهُۥ}} ({{tr:ummuhu}}) as the nominative mubtada of the nominal result clause, with {{ar:هَاوِيَةٌۭ}} ({{tr:hāwiyatun}}) as its predicate.\",\"representative_source_ids\":[\"QG-9968a19a\",\"QG-b1f3ece9\",\"QT-0f0c7420\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"101:9:1:2","source_type":"qac_morpheme","support_id":"sup_efa3bb1890de724609b0","text":"{\"lemma_ar\":\"أُمّ\",\"morph_features\":\"STEM|POS:N|LEM:>um~|ROOT:Amm|FS|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"101:9:1:2\",\"qac_word_ref\":\"101:9:1\",\"root_ar\":\"ء م م\",\"surface_ar\":\"أُمُّ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:9:1:parallel-branch-shift","source_type":"word_analysis","support_id":"sup_f018203413b5ff31c4b7","text":"{\"blocking_evidence\":null,\"headline\":\"parallel opening exposes the subject shift\",\"reader_payoff\":\"The reader notices that the branch echoes the positive result in 101:7, then breaks expectation by moving from {{ar:فَهُوَ}} ({{tr:fa-huwa}}) to {{ar:فَأُمُّهُۥ}} ({{tr:fa-ummuhu}}).\",\"reason\":\"The connector links rather than detaches the nominal verdict, and the CRITICAL rows' comparison with the positive branch is coherent with the repeated result-opening pattern.\",\"representative_source_ids\":[\"MG-3033e8e6\",\"QE-291636f8\",\"QT-feeab612\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فَأُمُّهُۥ هَاوِيَةٌۭ","ayah_ref":"101:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000053/B001","root_001609/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000053","role":"Supplies the intimate bearer and nurturer whose expected shelter is reversed.","root":"ء م م","source_ref":"101:9","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001609","role":"Supplies the abyss and destructive downward reception that takes the maternal role.","root":"ه و ي","source_ref":"101:9","source_word_indices":["2"]}],"changed_reading":{"after":"The abyss is made his mother: expected refuge becomes the very receiver that destroys him.","before":"A mother and an abyss are two independent referents joined by a startling equation."},"confidence":"strong","focus_anchor":"The possessive nominal clause directly predicates هَاوِيَةٌ of أُمُّهُ.","mechanism":"The bearer-nurturer relation is reassigned to a destructive vertical receiver: what should bear, gather, and shelter the person instead receives him by engulfing him.","model_id":"baseline_maternal_reversal"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_maternal_reversal","source_type":"hft","support_id":"sup_468cd99ebff6e6d8d1ec","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَأُمُّهُۥ هَاوِيَةٌۭ","ayah_ref":"101:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000053/B002","root_001609/B001","root_001609/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000053","role":"Makes the first term an origin, gathering center, and point of reference.","root":"ء م م","source_ref":"101:9","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001609","role":"Makes the predicate an empty or hollow spatial field.","root":"ه و ي","source_ref":"101:9","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001609","role":"Gives that hollow center terminal depth and downward force.","root":"ه و ي","source_ref":"101:9","source_word_indices":["2"]}],"changed_reading":{"after":"Haawiyah becomes the empty origin-home that gathers him back and defines where he belongs.","before":"Haawiyah is only the place to which he will go."},"confidence":"medium","focus_anchor":"أُمُّهُ can activate origin, gathering point, and reference while هَاوِيَةٌ activates both hollow space and abyss.","mechanism":"A void becomes the person's governing center of return and belonging. The clause does more than name a destination; it relocates origin, home, and reference into emptiness.","model_id":"baseline_void_as_return_center"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_void_as_return_center","source_type":"hft","support_id":"sup_fe446e14ae20f3850177","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَأُمُّهُۥ هَاوِيَةٌۭ","ayah_ref":"101:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000053/B012","root_001609/B002","root_001609/B008"],"payload":{"activation_trace":[{"branch_id":"B012","mapped_root_id":"root_000053","role":"Contributes aiming and deliberate heading as a secondary directional resonance.","root":"ء م م","source_ref":"101:9","source_word_indices":["1"]},{"branch_id":"B008","mapped_root_id":"root_001609","role":"Contributes swift, thrown travel rather than a motionless location.","root":"ه و ي","source_ref":"101:9","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001609","role":"Fixes the rapid trajectory as a descent into an abyss.","root":"ه و ي","source_ref":"101:9","source_word_indices":["2"]}],"changed_reading":{"after":"The clause also compresses an assigned vector: his heading, rapid passage, and terminal plunge coincide.","before":"The clause supplies a static kinship metaphor for a place."},"confidence":"exploratory","focus_anchor":"The focus roots themselves contain heading toward a target and rapid thrown motion into depth.","mechanism":"The static nominal equation can be heard as a compressed motion-script: his appointed heading is the plunge, so destination and movement are packed into the two-word clause.","model_id":"baseline_compressed_trajectory"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_compressed_trajectory","source_type":"hft","support_id":"sup_8214ecc5a71b35d0b2d4","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَأُمُّهُۥ هَاوِيَةٌۭ","ayah_ref":"101:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000053/B003","root_001609/B007"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000053","role":"Moves the maternal noun toward the head-core and a wound that reaches it.","root":"ء م م","source_ref":"101:9","source_word_indices":["1"]},{"branch_id":"B007","mapped_root_id":"root_001609","role":"Opens that core into a gaping wound or hollowed interior.","root":"ه و ي","source_ref":"101:9","source_word_indices":["2"]}],"changed_reading":{"after":"A secondary bodily horror appears: the person's own core is imaged as opened into the cavity that receives him.","before":"The horror is exclusively spatial: a person is received by a pit."},"confidence":"exploratory","containment":"This is surprising because the surface clause strongly presents mother and abyss, while these are remote anatomical branches. It remains anchored because both focus roots directly supply a head-core reached by injury and a gaping hollow body-space. Downstream prose should carry it only as a grotesque somatic echo, never as a replacement translation.","focus_anchor":"The two focus words can jointly activate a damaged inner core and an opened bodily cavity.","outlier_id":"outlier_cranial_hollow"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:outlier_cranial_hollow","source_type":"hft","support_id":"sup_337d33c3c239c33b49eb","trust":"legacy_unbound"}]}
</lane_packet_json>
