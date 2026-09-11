# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **101:7**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s101-regular-20260911/s101/101_7/micro.discovery.json` and modify nothing
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
  "ayah_ref": "101:7",
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
{"analysis_context":{"analysis_id":"s101-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"101:7","host_surah":101,"lane_context_refs":[],"ordered_context_refs":["101:0","101:1","101:2","101:3","101:4","101:5","101:6","101:8","101:9","101:10","101:11","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Temel durum, yönelinen şeyi kabul etmeyi de kapsar; karşılıklı hoşnutlaşma, başkasını hoşnut etme, yoğunluk bildiren ad ve üstün gelme kullanımı bu dalın çekirdeğine katılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000569/B001","candidate_links":[{"candidate_id":"cand_6ec3133d5c1643263ef3","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"رَاضِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:raADiyap|ROOT:rDw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:7:4:1","qac_word_ref":"101:7:4","surface_ar":"رَّاضِيَةٍ"}],"gloss":"hoşnut olma ve kabul etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hoşnutluk, öfke ve hoşnutsuzluğun karşıtı olan olumlu kabul durumudur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Durum bir şeye veya kişiye yöneldiğinde onu benimseme, uygun bulma ve kabul etme anlamı taşır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tanrı-kul ilişkisinde aynı çekirdek, taraflara göre hükme karşı çıkmama ve buyruğa uygun davranışı onaylama biçiminde ayrışır."}}],"root_ar":"ر ض و","root_id":"root_000569","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Öfke ve hoşnutsuzluğun karşıtı olan iç durumu ve bu durumun bir şeyi ya da kişiyi benimsemeye yönelmesini birlikte karşılar.","boundary_detail":"Temel durum, yönelinen şeyi kabul etmeyi de kapsar; karşılıklı hoşnutlaşma, başkasını hoşnut etme, yoğunluk bildiren ad ve üstün gelme kullanımı bu dalın çekirdeğine katılmaz.","branch_image_ar":"الرضا خلاف السخط","concept_gloss":"hoşnut olma ve kabul etme","contextual_glosses":[{"applicability":"Bir kişi ya da davranış hakkında öfkenin kalktığı ve olumlu değerlendirmenin oluştuğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yönelinen kişi hakkındaki olumlu değerlendirmeyi korur."},"facet_ids":["F001","F002"],"text":"ondan hoşnut oldu","usage_role":"contextual"},{"applicability":"Bir şeyin, seçimin veya kişinin benimsenip uygun görüldüğü geçişli bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Benimseme, kabul ve uygun bulma yönlerini korur."},"facet_ids":["F002"],"text":"onu kabul edip uygun buldu","usage_role":"contextual"},{"applicability":"Kulun Tanrı'nın hükmü karşısındaki hoşnutluğunu açıklayan özel bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kulun hüküm karşısında hoşnutsuzluk göstermemesi ölçütünü korur."},"facet_ids":["F003"],"text":"hükme içten karşı çıkmadı","usage_role":"explanatory"}],"definition":"Bir şeye ya da kimseye karşı öfke ve hoşnutsuzluk duymayı bırakıp onu benimsemek, uygun bulmak veya ondan hoşnut olmaktır. Tanrı-kul ilişkisinde bu durum, kul açısından hükme içten karşı çıkmama; Tanrı açısından ise kulun buyruğa uyup yasaktan kaçınmasını uygun bulma ölçütleriyle özelleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hoşnutluk, öfke ve hoşnutsuzluğun karşıtı olan olumlu kabul durumudur."},{"facet_id":"F002","role":"extension","statement":"Durum bir şeye veya kişiye yöneldiğinde onu benimseme, uygun bulma ve kabul etme anlamı taşır."},{"facet_id":"F003","role":"specialization","statement":"Tanrı-kul ilişkisinde aynı çekirdek, taraflara göre hükme karşı çıkmama ve buyruğa uygun davranışı onaylama biçiminde ayrışır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Belirgin bir coşku ve neşe duygusu ekler.","collision":"Hoşnutluğu geçici bir sevinç duygusuyla karıştırır.","fit":"displacement","loses":"Öfkenin karşıtı olma, uygun bulma ve kabul etme öğelerini kaybeder.","preserves":"Olumlu bir iç yöneliş bulunduğunu kısmen korur."},"text":"sevinç"}],"identity_rationale":"Yetkili ifade, anlamın merkezini hoşnutsuzluk ve öfkenin karşıtı olan hoşnutlukta kurar; bir şeyi veya kişiyi kabul etme ile kendisinden hoşnut olunan tarafı da bu merkeze bağlar. Kulun Tanrı karşısındaki ve Tanrı'nın kul karşısındaki hoşnutluğu ise katılımcıları ve ölçütleri farklı iki özel uygulama olarak verilir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"hoşnut olmak; kabul etmek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"hoşnut"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"kabul edilmiş; kendisinden hoşnut olunan"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"kendisinden hoşnut olunan kişi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"hoşnutluk"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"onu kabul edip uygun buldu"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"onu seçip uygun buldu"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"ondan hoşnut oldu; onu kabul etti"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"hoşnutluk adı"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"beğenilen bir yaşayış"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"onu arkadaş olarak kabul etti"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"ondan hoşnut oldu; onu uygun buldu"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"beğenilen; kabul edilen"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"kulun Tanrı'nın hükmünden hoşnutsuzluk duymaması"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"Tanrı'nın kulu buyruğa uyan ve yasaktan kaçınan biri olarak görmesi"}],"lexicalization_note":"Tanım, yalın hoşnutluk çekirdeğini korurken nesneye, kişiye ve Tanrı-kul ilişkisine bağlı kullanımları ayrı özel yüzler olarak gösterir; bu kullanımlar yalın anlamın tamamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; temel karşıtlık, kabul ve yetinme yakınlıkları ile karşılıklı ve ettirgen kardeş dallar sınırı en açık biçimde gösterdiği için seçildi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Bu dal olumlu kabul kutbunu, komşu ise aynı eksenin olumsuz ve öfkeli kutbunu gösterir; bu nedenle karşıtlık doğrudandır.","focus_only":"Hoşnut olma, benimseme ve uygun bulma yönünü taşır.","gloss":"hoşnutluk / öfke ve hoşnutsuzluk","neighbor_only":"Öfke, beğenmeme ve hoşnutsuzluk yönünü taşır.","neighbor_ref":"root_000686/B001","relation_type":"antonym","shared_zone":"İkisi de bir şey ya da kişi hakkındaki değerlendirme ve duygusal tutum eksenindedir."},{"boundary_match":"partial","distinction":"Komşu dal hoşnutluğu pay, geçim veya azla yetinme koşuluna bağlar; bu dalda böyle bir yeterlilik sınırı yoktur.","focus_only":"Her tür kişi veya şeye yönelen genel hoşnutluk ve kabulü kapsar.","gloss":"hoşnutluk / elindekine yetinme","neighbor_only":"Payına düşene yetinme ve azla geçinme sınırını özellikle taşır.","neighbor_ref":"root_001263/B001","relation_type":"near_synonym","shared_zone":"Her ikisinde de elde olana karşı hoşnutsuzluk göstermeme vardır."},{"boundary_match":"partial","distinction":"Kabul komşusunda alma veya geçerli sayma eylemi yeterli olabilir; bu dal ise buna hoşnutluk ve öfkesizlik durumunu da bağlar.","focus_only":"İç hoşnutluk durumunu ve öfkenin kalkmasını kurucu öğe sayar.","gloss":"hoşnut olup benimseme / kabul etme","neighbor_only":"Bir şeyi, özrü, armağanı veya işi alma ve kabul etme eylemini öne çıkarır.","neighbor_ref":"root_001198/B004","relation_type":"near_synonym","shared_zone":"Bir şeyi olumlu karşılayıp geri çevirmeme alanında örtüşürler."},{"boundary_match":"partial","distinction":"Bu dal tek yönlü veya yöneltilmiş olabilir; komşu dalda karşılıklılık kurucu bir koşuldur.","focus_only":"Tek bir tarafın bir şeyden veya kişiden hoşnut olmasını da kapsar.","gloss":"hoşnut olma / karşılıklı hoşnutlaşma","neighbor_only":"İki ya da daha çok tarafın birbirlerinden hoşnutluk göstermesini gerektirir.","neighbor_ref":"root_000569/B003","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak alanı olumlu kabul ve hoşnutluktur."},{"boundary_match":"partial","distinction":"Bu dal durum ve değerlendirmeyi, komşu dal ise o durumu başka bir kişide meydana getiren ya da isteyen eylemi merkez alır.","focus_only":"Bir öznenin mevcut hoşnutluk ve kabul durumunu anlatır.","gloss":"hoşnut olma / hoşnut etme","neighbor_only":"Başka bir kişide hoşnutluk oluşturma veya ondan hoşnutluk isteme işlemini anlatır.","neighbor_ref":"root_000569/B004","relation_type":"near_neighbor","shared_zone":"İki dal da hoşnutsuzluğun giderildiği aynı genel durum alanına katılır."}],"source_phrase_ar":"أصل واحد يدل على خلاف السخط (maqayis)؛ الرضا في الأصل من بنات الواو والرضا مقصور (ayn)؛ رضيت الشيء وارتضيته فهو مرضي ومرضو ورضيت عنه رضا (sihah)؛ رضي فلان يرضى رضى والرضي المرضي والرضا مقصور (tahdhib)؛ رضي يرضى رضا فهو مرضي ومرضو ورضا العبد عن الله ورضا الله عن العبد (mufradat)","source_summary":"Kaynakların ortak çizgisi hoşnutluğu öfke ve hoşnutsuzluğun karşıtı sayar; ayrıca kabul edilen tarafı ve hoşnutluğun yöneldiği nesne ya da kişiyi gösterir. Bir tanıklık ayrıca Tanrı-kul ilişkisindeki iki yönün ölçütlerini birbirinden ayırır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه أصل الرضا والقبول وترك الكراهة، ورضي يرضى، والراضي، والمرضي أو المرضو عنه","what_is_not_ar":"ليس هو الرضوان الكثير خاصة، ولا المراضاة من اثنين، ولا الغلبة في قولهم راضاني فرضوته"},"support_links":["sup_776c22c644f22e8b05b7"]},{"boundary":"Dal, hoşnutluğu adlandıran belirli biçimlerle sınırlıdır; yoğunluk bunlardan biri için kaynaklar arası bir anlam farkıdır, genel çekirdeğin zorunlu öğesi değildir.","branch_kind":"bare","branch_ref":"root_000569/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَاضِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:raADiyap|ROOT:rDw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:7:4:1","qac_word_ref":"101:7:4","surface_ar":"رَّاضِيَةٍ"}],"gloss":"hoşnutluk; yoğun hoşnutluk","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki ad biçimi de hoşnutluk durumunu adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ad biçimlerinden biri, bir tanıklıkta genel anlamdan daha yoğun ve bol hoşnutluk olarak yorumlanır."}}],"root_ar":"ر ض و","root_id":"root_000569","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli ad biçimlerinin genel hoşnutluğu veya kaynak yorumuna göre onun yoğun derecesini bildirdiği yerlerde kullanılır.","boundary_detail":"Dal, hoşnutluğu adlandıran belirli biçimlerle sınırlıdır; yoğunluk bunlardan biri için kaynaklar arası bir anlam farkıdır, genel çekirdeğin zorunlu öğesi değildir.","branch_image_ar":"الرضوان والمرضاة اسم للرضا الكثير أو المطلوب","concept_gloss":"hoşnutluk; yoğun hoşnutluk","contextual_glosses":[{"applicability":"Ad biçiminin temel hoşnutluk durumuyla eşdeğer kullanıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Adın temel hoşnutluk anlamını eksiksiz korur."},"facet_ids":["F001"],"text":"hoşnutluk","usage_role":"general"},{"applicability":"Ad biçiminin hoşnutluğun çokluğunu veya yoğunluğunu belirttiği özel yorumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yoğun ve bol hoşnutluk yorumunu açıkça korur."},"facet_ids":["F002"],"text":"engin hoşnutluk","usage_role":"contextual"}],"definition":"Hoşnutluk durumunu adlandıran iki ad biçimidir. Bunlardan biri kimi tanıklıkta genel hoşnutlukla eşdeğerken bir tanıklıkta hoşnutluğun çokluğu veya yoğunluğu olarak açıklanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki ad biçimi de hoşnutluk durumunu adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Ad biçimlerinden biri, bir tanıklıkta genel anlamdan daha yoğun ve bol hoşnutluk olarak yorumlanır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Karşılık olarak verilen somut veya soyut bir kazanç anlamı ekler.","collision":"Hoşnutluğun kendisini hoşnutluk sonucunda verilebilecek bir karşılıkla karıştırır.","fit":"displacement","loses":"Hoşnutluk durumunu ve onun yoğunluk ayrımını bütünüyle kaybeder.","preserves":"Olumlu değerlendirmeyle ilişkilendirilebilmesini çok dolaylı biçimde korur."},"text":"ödül"}],"identity_rationale":"Yetkili ifade iki ad biçimini hoşnutlukla ilişkilendirir ve bunlardan biri için bir kaynakta yoğunluk bildirir. Hazırlanmış çerçevedeki 'istenen' ya da 'aranan' anlamı ise kaynak ifadesinde yer almadığından tanımdan çıkarılmıştır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"hoşnutluk; yoğun hoşnutluk"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"hoşnutluk"}],"lexicalization_note":"Tanım yalnızca kanıtta verilen yalın ad biçimlerinin hoşnutluk ve bir tanıklıkta yoğun hoşnutluk bildirmesiyle sınırlıdır; karşılıklı ya da ettirgen kullanımlar eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; temel hoşnutluk dalı, geniş küme adayı ve olumlu duygu alanındaki iki komşu, ad biçimi ile yoğunluk sınırını en yararlı şekilde açtığı için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli ad biçimlerine ve olası yoğunluk farkına bağlıdır; komşu dal genel durumu ve onun yönelimli kullanımlarını anlatır.","focus_only":"Hoşnutluğu adlandıran iki belirli biçimi ve bunlardan birindeki yoğunluk yorumunu kapsar.","gloss":"hoşnutluk adı / hoşnut olma","neighbor_only":"Hoşnut olma eylemini, hoşnut kişiyi ve bir şeye yönelen kabulü daha geniş biçimde kapsar.","neighbor_ref":"root_000569/B001","relation_type":"near_synonym","shared_zone":"İki dalın ortak çekirdeği öfkenin karşıtı olan hoşnutluk durumudur."},{"boundary_match":"partial","distinction":"Komşu çok daha geniş bir türetim alanıdır; bu dalın sınırı iki ad biçimi ve bunların anlam farkıdır.","focus_only":"Belirli iki ad biçimini ve bunlardan birinin yoğunluk yorumunu ayrı bir dal olarak tutar.","gloss":"yoğun hoşnutluk adı / geniş hoşnutluk kümesi","neighbor_only":"Hoşnutlukla birlikte kabul, ettirgenlik, karşılıklılık ve başka türemiş kullanımları geniş bir kümede toplar.","neighbor_ref":"root_000570/B001","relation_type":"near_synonym","shared_zone":"Her ikisi de hoşnutluğu ve onu adlandıran biçimleri içerir."},{"boundary_match":"field_only","distinction":"Bu dal kabul edici hoşnutluk durumudur; komşu dal sevinç, iyilik görme ve onurlandırılma sonuçlarını öne çıkarır.","focus_only":"Bir değerlendirme durumu olarak hoşnutluğu ve onun yoğunluğunu bildirir.","gloss":"yoğun hoşnutluk / sevinç ve nimet","neighbor_only":"Sevinç, nimet ve onurlandırılma durumlarını bildirir.","neighbor_ref":"root_000287/B005","relation_type":"same_field","shared_zone":"İkisi de olumlu duygulanım ve iyi karşılanma alanında yer alır."},{"boundary_match":"partial","distinction":"Beğenip sevinme belirli bir tepki ve sevinç taşır; bu dalda sevinç zorunlu değildir ve asıl öğe hoşnutluktur.","focus_only":"Süreklilik gösterebilen bir hoşnutluk durumunu adlandırır.","gloss":"hoşnutluk / beğenip sevinme","neighbor_only":"Bir şey karşısında beğeni ve sevinç duymayı birlikte anlatır.","neighbor_ref":"root_000832/B004","relation_type":"near_neighbor","shared_zone":"Olumlu değerlendirme ve iyi hissetme alanında örtüşürler."}],"source_phrase_ar":"الرضوان اسم موضوع من الرضا (ayn)؛ الرضوان الرضا وكذلك الرضوان بالضم والمرضاة مثله (sihah)؛ الرضوان الرضا الكثير (mufradat)","source_summary":"Toplu tanıklık, iki ad biçimini hoşnutluk adı olarak bir araya getirir; kaynaklar arasındaki fark, bunlardan birinin genel hoşnutluk mu yoksa çok ve yoğun hoşnutluk mu bildirdiğidir.","sources":["AY","SI","MU"],"what_is_ar":"يدخل فيه الرضوان والمرضاة بوصفهما اسما أو صيغة للرضا، وخاصة الرضوان الكثير في كلام المفردات","what_is_not_ar":"ليس مطلق فعل رضي وحده، ولا المراضاة المتبادلة بين طرفين"},"support_links":[]},{"boundary":"Karşılıklılık zorunludur; tek taraflı hoşnutluk, bir başkasını hoşnut etme çabası ve çekişmede üstün gelme bu dalın dışında kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000569/B003","candidate_links":[{"candidate_id":"cand_3faf863ac4dded8d2638","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"رَاضِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:raADiyap|ROOT:rDw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:7:4:1","qac_word_ref":"101:7:4","surface_ar":"رَّاضِيَةٍ"}],"gloss":"karşılıklı hoşnutluk ve kabul","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hoşnutluk ve kabul iki taraf arasında karşılıklı olarak kurulur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tarafların her biri ötekinden hoşnut olduğunu ve onu kabul ettiğini gösterir."}}],"root_ar":"ر ض و","root_id":"root_000569","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki ya da daha çok tarafın birbirlerini uygun bulup birbirlerinden hoşnutluk gösterdiği durumların genel karşılığıdır.","boundary_detail":"Karşılıklılık zorunludur; tek taraflı hoşnutluk, bir başkasını hoşnut etme çabası ve çekişmede üstün gelme bu dalın dışında kalır.","branch_image_ar":"المراضاة والتراضي رضا متبادل","concept_gloss":"karşılıklı hoşnutluk ve kabul","contextual_glosses":[{"applicability":"Tarafların birbirlerini olumlu karşılayıp hoşnutluklarını karşılıklı biçimde gösterdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki tarafın birbirinden hoşnut olması koşulunu korur."},"facet_ids":["F001"],"text":"karşılıklı olarak hoşnut oldular","usage_role":"general"},{"applicability":"İç hoşnutluktan çok tarafların birbirlerini benimsediğini açık etmek gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı kabulü ve her tarafın ötekini uygun bulmasını korur."},"facet_ids":["F001","F002"],"text":"birbirlerini kabul edip uygun buldular","usage_role":"explanatory"}],"definition":"İki ya da daha çok tarafın birbirlerini kabul edip birbirlerinden hoşnut olduklarını karşılıklı olarak göstermeleridir. Her tarafın ötekini uygun bulması ve bu hoşnutluğu dışa vurması yapının kurucu koşuludur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hoşnutluk ve kabul iki taraf arasında karşılıklı olarak kurulur."},{"facet_id":"F002","role":"specialization","statement":"Tarafların her biri ötekinden hoşnut olduğunu ve onu kabul ettiğini gösterir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Görüş, karar veya koşullar üzerinde uzlaşma anlamını ekler.","collision":"Kişiler arası hoşnutluğu bir konu üzerindeki uzlaşmayla karıştırabilir.","fit":"broadening","loses":"Her tarafın ötekinden hoşnut olması ve bunu göstermesi koşulunu kaybeder.","preserves":"Tarafların aynı yönde buluşması düşüncesini kısmen korur."},"text":"anlaşma"}],"identity_rationale":"Yetkili ifade, iki tarafın birbirinden hoşnut olmasını ve her birinin ötekini kabul ettiğini göstermesini açıkça kurucu öğe yapar. Eylem adı ve tarafların bu durumu aralarında göstermesi aynı karşılıklı yapı içinde birleşir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"karşılıklı hoşnutluk"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"birbiriyle hoşnutlaşma"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"birbirlerinden hoşnut olduklarını karşılıklı gösterdiler"}],"lexicalization_note":"Tanım, karşılıklı eylem biçimleri ile tarafların birbirlerinden hoşnutluk gösterdiği yapıyı birlikte fakat açıkça karşılıklılık koşuluna bağlı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tek yönlü hoşnutluk ile uyuşma, iş üzerinde uzlaşma, uyma ve karşılıklı kararlaştırma adayları karşılıklılık koşulunu en net biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın kurulması için en az iki taraflı hoşnutluk gerekir; komşu dal tek yönlü bir tutumla da gerçekleşir.","focus_only":"Her tarafın ötekinden hoşnut olmasıyla kurulan karşılıklı ilişkiyi gerektirir.","gloss":"karşılıklı hoşnutluk / hoşnut olma","neighbor_only":"Tek bir tarafın bir şeyden veya kişiden hoşnut olmasını da kapsar.","neighbor_ref":"root_000569/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da olumlu kabul ve hoşnutsuzluğun kalkması alanındadır."},{"boundary_match":"partial","distinction":"Uyuşma komşusu duygu veya kabul gerektirmeden eşleşme bildirebilir; bu dalda karşılıklı hoşnutluk kurucudur.","focus_only":"Tarafların birbirlerinden hoşnut ve birbirlerini kabul eder olması gerekir.","gloss":"karşılıklı hoşnutluk / uyuşma","neighbor_only":"Nesnelerin birbirine uyması, sözlerin örtüşmesi veya kişilerin aynı görüşte buluşması yeterlidir.","neighbor_ref":"root_000927/B003","relation_type":"near_synonym","shared_zone":"Tarafların çatışmadan aynı yönde bulunması bakımından örtüşürler."},{"boundary_match":"partial","distinction":"Komşu dalda uzlaşmanın konusu belirli bir iştir; bu dalda ise ilişki tarafların birbirlerine yönelik hoşnutluğudur.","focus_only":"Tarafların birbirlerini kabul etmesine ve birbirlerinden hoşnut olmasına odaklanır.","gloss":"karşılıklı hoşnutluk / bir iş üzerinde uzlaşma","neighbor_only":"Topluluğun belirli bir iş üzerinde, özellikle kestirime dayalı biçimde uzlaşmasına odaklanır.","neighbor_ref":"root_001610/B003","relation_type":"near_synonym","shared_zone":"Birden çok tarafın gönüllü biçimde ortak bir noktaya gelmesi alanında örtüşürler."},{"boundary_match":"partial","distinction":"Uyma davranışsal bir izleme veya eşleşme olabilir; bu dal ise her iki tarafın birbirinden hoşnut olmasını gerektirir.","focus_only":"Karşılıklı hoşnutluk ve kabulün kendisini bildirir.","gloss":"karşılıklı hoşnutluk / uyma ve uyuşma","neighbor_only":"Birinin ötekine uyması, onu izlemesi veya onunla aynı yönde davranmasını bildirir.","neighbor_ref":"root_000956/B002","relation_type":"near_neighbor","shared_zone":"Tarafların çatışmayıp birbirine yönelmesi bakımından yakınlaşırlar."},{"boundary_match":"partial","distinction":"Karşılıklı kararlaştırma bir işlem veya konu çevresindedir; bu dal tarafların birbirlerini olumlu kabul etmesi çevresindedir.","focus_only":"Tarafların birbirlerine yönelik hoşnutluklarını kurucu sayar.","gloss":"karşılıklı hoşnutluk / karşılıklı kararlaştırma","neighbor_only":"Belirli bir işin koşullarını karşılıklı olarak kararlaştırmayı veya tartışmayı kurucu sayar.","neighbor_ref":"root_001657/B011","relation_type":"near_neighbor","shared_zone":"İki tarafın birlikte ve gönüllü biçimde hareket ettiği ilişkisel alanda buluşurlar."}],"source_phrase_ar":"المراضاة من اثنين (ayn)؛ مصدر راضيته رضاء ومراضاة (sihah;tahdhib)؛ إذا تراضوا بينهم أي أظهر كل واحد منهم الرضا بصاحبه ورضيه (mufradat)","source_summary":"Tanıklıklar, bu kullanımı iki taraflı hoşnutluk ilişkisi ve onun eylem adı olarak verir. Toplu ifade, tarafların birbirlerini kabul etmelerinin yanı sıra bu hoşnutluğu karşılıklı olarak göstermelerini de açıklar.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه المراضاة من اثنين، ومصدر راضيته، والتراضي بينهم حين يظهر كل واحد الرضا بصاحبه","what_is_not_ar":"ليس رضا طرف واحد فقط، ولا إرضاء الغير بعد جهد، ولا غلبة راضاني فرضوته"},"support_links":["sup_78a391a61e1c1cb0785b"]},{"boundary":"Merkez, öznenin kendi hoşnutluğu değil başka birinin hoşnut olmasını sağlama ya da istemedir; karşılıklı hoşnutluk ayrıca kurulmadıkça bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000569/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَاضِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:raADiyap|ROOT:rDw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:7:4:1","qac_word_ref":"101:7:4","surface_ar":"رَّاضِيَةٍ"}],"gloss":"başkasını hoşnut etme veya hoşnutluğunu isteme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Özne, başka bir kişiyi hoşnut duruma getirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hoşnut etme sonucu kimi biçimde ancak çaba gösterildikten sonra elde edilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özne karşı taraftan hoşnutluk ister ve karşı tarafın onu hoşnut etmesiyle sonuçlanan bir ilişki kurar."}}],"root_ar":"ر ض و","root_id":"root_000569","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin hoşnutsuzluğunu giderip onu hoşnut kılmayı veya ondan olumlu kabul istemeyi anlatan kullanımları kapsar.","boundary_detail":"Merkez, öznenin kendi hoşnutluğu değil başka birinin hoşnut olmasını sağlama ya da istemedir; karşılıklı hoşnutluk ayrıca kurulmadıkça bu dala girmez.","branch_image_ar":"الإرضاء طلب رضا الغير وإزالة سخطه","concept_gloss":"başkasını hoşnut etme veya hoşnutluğunu isteme","contextual_glosses":[{"applicability":"Öznenin karşı taraftaki hoşnutsuzluğu giderip kendisine yönelik olumlu tutum oluşturduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başkasında hoşnutluk meydana getirme sonucunu korur."},"facet_ids":["F001"],"text":"onu kendisinden hoşnut etti","usage_role":"general"},{"applicability":"Hoşnut etme sonucunun emek veya çaba sonrasında elde edildiği özel biçim için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hoşnut etme sonucunu ve öncesindeki çabayı korur."},"facet_ids":["F002"],"text":"uğraşarak onu hoşnut etti","usage_role":"contextual"},{"applicability":"Öznenin karşı taraftan kendisine yönelik hoşnutluk ve kabul istediği kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Karşı tarafın sonunda özneyi hoşnut etmesi sonucunu açıkça söylemez.","preserves":"Karşı taraftan hoşnutluk isteme aşamasını korur."},"facet_ids":["F003"],"text":"ondan hoşnutluk göstermesini istedi","usage_role":"explanatory"}],"definition":"Başka bir kişide kendisine veya bir duruma yönelik hoşnutluk oluşturmak ya da o kişiden hoşnutluk göstermesini istemektir. Bazı biçimler sonucun çabayla elde edildiğini, bazıları ise istemenin ardından karşı tarafın özneyi hoşnut ettiğini ayrıca bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Özne, başka bir kişiyi hoşnut duruma getirir."},{"facet_id":"F002","role":"specialization","statement":"Hoşnut etme sonucu kimi biçimde ancak çaba gösterildikten sonra elde edilir."},{"facet_id":"F003","role":"extension","statement":"Özne karşı taraftan hoşnutluk ister ve karşı tarafın onu hoşnut etmesiyle sonuçlanan bir ilişki kurar."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Hoşnut etmeyi yalnızca öfkeyi geçici olarak dindirmeye indirger.","fit":"narrowing","loses":"Olumlu hoşnutluk oluşturma, bunu isteme ve sonucun çabayla elde edilmesi ayrımlarını kaybeder.","preserves":"Olumsuz bir tutumu giderme çabasını kısmen korur."},"text":"yatıştırma"}],"identity_rationale":"Yetkili ifade, başka bir kişide hoşnutluk meydana getirme, bunu çaba sonunda sağlama ve karşı taraftan hoşnutluk isteme biçimlerini aynı ettirgen ve isteme alanında toplar. Hazırlanmış çerçeve bu yön değişimini doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"onu kendimden hoşnut ettim"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"onu hoşnut ettim"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"uğraşarak onu hoşnut ettim"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"ondan hoşnutluk göstermesini istedim; o da beni hoşnut etti"}],"lexicalization_note":"Tanım, başkasını hoşnut etme çekirdeği ile çaba ve isteme bildiren özel biçimleri ayrı yüzlerde tutar; bunları yalın hoşnut olma anlamına genellemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; temel durum dalı ile gönül alma, yumuşak davranma ve çatışmadan kaçınarak idare etme adayları, sonuç ile yöntem ayrımını en açık biçimde gösterdiği için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal ettirgen veya isteme yönlüdür; komşu dalda hoşnutluğu taşıyan öznenin kendi durumu merkezde kalır.","focus_only":"Başka bir kişide hoşnutluk oluşturma veya ondan hoşnutluk isteme işlemini bildirir.","gloss":"hoşnut etme / hoşnut olma","neighbor_only":"Öznenin kendisinin hoşnut olması ya da bir şeyi kabul etmesi durumunu bildirir.","neighbor_ref":"root_000569/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da hoşnutsuzluğun kalkması ve olumlu kabul alanındadır."},{"boundary_match":"partial","distinction":"Komşu dal yumuşatma ve gönlünü alma davranışlarını sonuçtan bağımsız kapsayabilir; bu dal hoşnutluk sonucunu veya onun açıkça istenmesini merkez alır.","focus_only":"Karşı tarafı gerçekten hoşnut etme sonucunu ve hoşnutluk istemeyi kapsar.","gloss":"hoşnut etme / gönlünü alma","neighbor_only":"İlgi uyandırma, yumuşatma ve gönlünü alma yoluyla birinden iyilik isteme gibi daha geniş kullanımları kapsar.","neighbor_ref":"root_001592/B006","relation_type":"near_synonym","shared_zone":"Bir kişinin olumlu tutumunu kazanma çabasında örtüşürler."},{"boundary_match":"partial","distinction":"Komşu dal bir davranış yöntemini ve yumuşaklığı öne çıkarır; bu dalın çekirdeği hoşnutluğun oluşmasıdır.","focus_only":"Başkasını hoşnut duruma getirme sonucunu bildirir.","gloss":"hoşnut etme / gönlünü hoş tutma","neighbor_only":"İstekte bulunurken kişiyi yumuşaklıkla gözetme ve iyi geçinme yöntemini bildirir.","neighbor_ref":"root_000751/B002","relation_type":"near_synonym","shared_zone":"Karşı tarafın olumsuz tepki vermemesini ve iyi ilişkiyi sağlama alanında örtüşürler."},{"boundary_match":"partial","distinction":"Yumuşak davranma komşusunda amaç zarar veya çatışmadan kaçınmak olabilir; bu dalda belirleyici sonuç karşı tarafın hoşnutluğudur.","focus_only":"Karşı tarafta hoşnutluk oluşturmayı amaç ve sonuç olarak taşır.","gloss":"hoşnut etme / çatışmadan kaçınarak idare etme","neighbor_only":"Çatışmadan korunmak için kişiye yumuşak davranmayı ve onu idare etmeyi taşır.","neighbor_ref":"root_000466/B008","relation_type":"near_neighbor","shared_zone":"Karşı tarafın olumsuz tepkisini azaltmaya yönelik kişiler arası davranış alanında buluşurlar."},{"boundary_match":"partial","distinction":"Yumuşak davranış hoşnutluk doğurmayabilir; bu dal ise davranışın biçiminden çok hoşnutluğu sağlama veya isteme ilişkisini tanımlar.","focus_only":"Hoşnutluk meydana getirme veya isteme sonucuna bağlıdır.","gloss":"hoşnut etme / yumuşak davranma","neighbor_only":"Bir kişiye nazik ve yumuşak davranma biçimine bağlıdır.","neighbor_ref":"root_000485/B006","relation_type":"near_neighbor","shared_zone":"İyi ilişki kurmaya yönelik kişiler arası eylemlerde yakınlaşırlar."}],"source_phrase_ar":"أرضيته عني ورضيته بالتشديد أيضا فرضي وترضيته أرضيته بعد جهد واسترضيته فأرضاني (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, doğrudan hoşnut etme, çabayla hoşnut etme ve hoşnutluk isteme ayrımlarını birlikte verir."}],"source_summary":"Tanıklık, başkasının hoşnutluğunu sağlama ve isteme çevresindeki kullanımları; doğrudan sonuç, çabayla elde edilen sonuç ve istemeye verilen karşılık ayrımlarıyla birlikte sunar.","sources":["SI"],"what_is_ar":"يدخل فيه أرضيته، ورضيته بالتشديد، وترضيته بعد جهد، واسترضيته فأرضاني","what_is_not_ar":"ليس هو رضا النفس ابتداء، ولا التراضي بين طرفين على سواء، ولا رضوان اسما للرضا"},"support_links":[]},{"boundary":"Anlam yalnızca verilen karşılıklı eylem kalıbında bir konuda üstün gelmeyi anlatır; genel hoşnutluk, karşılıklı kabul veya her türlü yenme anlamına genişletilemez.","branch_kind":"non_bare","branch_ref":"root_000569/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَاضِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:raADiyap|ROOT:rDw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:7:4:1","qac_word_ref":"101:7:4","surface_ar":"رَّاضِيَةٍ"}],"gloss":"karşılıklı çekişmede üstün gelme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Karşılıklı bir girişim veya çekişme içinde öteki tarafa o konuda üstün gelinir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Üstün gelme anlamı yalnızca tanıklanan sözlüksel ifadenin sınırı içinde geçerlidir."}}],"root_ar":"ر ض و","root_id":"root_000569","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca tanıklanan karşılıklı eylem ifadesinin, bir konuda karşı tarafı yenme sonucunu bildirdiği kullanım için uygundur.","boundary_detail":"Anlam yalnızca verilen karşılıklı eylem kalıbında bir konuda üstün gelmeyi anlatır; genel hoşnutluk, karşılıklı kabul veya her türlü yenme anlamına genişletilemez.","branch_image_ar":"راضاني فرضوته غلبة في ذلك","concept_gloss":"karşılıklı çekişmede üstün gelme","contextual_glosses":[{"applicability":"Karşı tarafın aynı alandaki girişimine cevap verilip onun yenildiği belirli ifade bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eylemin karşılıklı kalıba bağlı olduğunu açıkça söylemez.","preserves":"Belirli bir konuda karşı tarafa üstün gelme sonucunu korur."},"facet_ids":["F001","F002"],"text":"o konuda ona üstün geldim","usage_role":"contextual"}],"definition":"Belirli bir karşılıklı çekişme ifadesinde, öteki tarafın girişimine karşı aynı konuda ona üstün gelmektir. Anlam, ifadenin bütününe bağlıdır ve genel hoşnutluk alanından ayrıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Karşılıklı bir girişim veya çekişme içinde öteki tarafa o konuda üstün gelinir."},{"facet_id":"F002","role":"specialization","statement":"Üstün gelme anlamı yalnızca tanıklanan sözlüksel ifadenin sınırı içinde geçerlidir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Olumlu kabul ve iç hoşnutluk durumu ekler.","collision":"Kalıba bağlı üstün gelme anlamını kökün temel hoşnutluk anlamıyla karıştırır.","fit":"displacement","loses":"Karşılıklı çekişmeyi ve öteki tarafa üstün gelme sonucunu bütünüyle kaybeder.","preserves":"Aynı kök ailesiyle biçimsel bağı dışında kurucu anlamı korumaz."},"text":"hoşnut oldum"}],"identity_rationale":"Yetkili ifade, belirli bir karşılıklı eylem kalıbında birinin ötekine üstün gelmesini açıkça bildirir. Bu kullanım hoşnutluk çekirdeğinden değil, kalıbın bütününden doğduğu için ayrı ve sözlüksel olarak sınırlı dal kabul edilmiştir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"karşılıklı çekişmede ona üstün geldim"}],"lexicalization_note":"Tanım, üstün gelme anlamını yalnızca kanıtta verilen sözlüksel kalıba bağlar ve bunu kökün yalın anlamı ya da genel bir yenme fiili olarak sunmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı kullanımı veren tam eşdeğer önce, ardından sözlüksel kalıp, sayı, genel zafer ve güç yarışı sınırlarını gösteren en yakın üstün gelme dalları seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Anlam çekirdeği, katılımcılar ve sözlüksel sınır bakımından ayrım yoktur; iki dal aynı kullanımı temsil eder.","focus_only":null,"gloss":"karşılıklı çekişmede üstün gelme","neighbor_only":null,"neighbor_ref":"root_000570/B002","relation_type":"synonym","shared_zone":"İki kart da aynı sözlüksel ifade içinde aynı konuda karşı tarafa üstün gelmeyi bildirir."},{"boundary_match":"partial","distinction":"Sonuç aynıdır, ancak her anlam kendi tanıklanan sözlüksel ifadesine bağlıdır; bu nedenle ifadeler serbestçe birbirinin yerine geçmez.","focus_only":"Üstün gelmeyi yalnızca bu dala özgü karşılıklı eylem ifadesinde bildirir.","gloss":"çekişmede üstün gelme / karşı koyuşta üstün gelme","neighbor_only":"Üstün gelmeyi karşı koyma ve ayrışma alanına özgü başka bir karşılıklı eylem ifadesinde bildirir.","neighbor_ref":"root_000808/B003","relation_type":"near_synonym","shared_zone":"İki kullanım da karşılıklı bir eylem kalıbında öteki tarafa o konuda üstün gelmeyi anlatır."},{"boundary_match":"partial","distinction":"Komşu dalda sayı çokluğu kurucu araçtır; bu dalda sayı koşulu yoktur, fakat anlam belirli bir ifadeyle sınırlıdır.","focus_only":"Üstün gelmenin aracını veya ölçüsünü belirtmeden belirli bir çekişme kalıbına bağlıdır.","gloss":"çekişmede üstün gelme / sayıca üstün gelme","neighbor_only":"Üstün gelmeyi özellikle sayı çokluğu üzerinden kurar.","neighbor_ref":"root_001286/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da rakip tarafa üstün gelme sonucunu taşır."},{"boundary_match":"partial","distinction":"Komşu genel bir zafer ve yenme alanıdır; bu dalın anlamı tek bir sözlüksel kullanımdan dışarı taşmaz.","focus_only":"Yalnızca tanıklanan karşılıklı ifade içinde bir konuda üstün gelmeyi bildirir.","gloss":"kalıba bağlı üstün gelme / zafer kazanma","neighbor_only":"Zafer kazanma, ele geçirme ve rakibi yenme alanını daha genel biçimde kapsar.","neighbor_ref":"root_000965/B001","relation_type":"near_synonym","shared_zone":"Rakibin yenilmesi ve üstünlüğün elde edilmesi sonucunda örtüşürler."},{"boundary_match":"partial","distinction":"Komşu güç gösterisi ve büyüklük yarışını öne çıkarır; bu dalda böyle bir yöntem yoktur, yalnızca tanıklanan ifade sınırı vardır.","focus_only":"Belirli bir karşılıklı eylem ifadesinde o konuda üstün gelmeye bağlıdır.","gloss":"çekişmede üstün gelme / güç yarışında üstün gelme","neighbor_only":"Rakiple büyüklük ve güç yarışı içindeki karşılıklı üstünlük kurma davranışına bağlıdır.","neighbor_ref":"root_001281/B011","relation_type":"near_synonym","shared_zone":"Karşılıklı mücadelede rakibi aşma sonucunu paylaşırlar."}],"source_phrase_ar":"قال أبو عبيد راضاني فلان فرضوته (maqayis)؛ راضاني فلان فرضوته أرضوه بالضم إذا غلبته فيه لأنه من الواو (sihah)","source_summary":"Tanıklıklar aynı karşılıklı eylem ifadesini bir konuda öteki tarafa üstün gelmek diye açıklar; verilen malzeme bu anlamı tanıklanan sözlüksel kalıpla sınırlı tutar.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه قولهم راضاني فلان فرضوته أو أرضوه إذا غلبته فيه","what_is_not_ar":"ليس مطلق الرضا خلاف السخط، ولا المراضاة بمعنى رضا الطرفين"},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"bare","branch_ref":"root_000569/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَاضِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:raADiyap|ROOT:rDw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:7:4:1","qac_word_ref":"101:7:4","surface_ar":"رَّاضِيَةٍ"}],"gloss":"söz dinleyen, seven veya güvence veren","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"associated_use","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kullanım, buyruğa uyan ve söz dinleyen kişiyi niteler."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İkinci kullanım, sevgi duyan kişiyi niteler."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Üçüncü kullanım, bir yükümlülük için güvence veren kişiyi niteler."}},{"facet_id":"F004","role":"core","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Aynı sıfat biçiminin kanıtta yalnız bu üç kişi niteliğiyle sınırlı olarak kaydedilmesidir."}}],"root_ar":"ر ض و","root_id":"root_000569","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sıfat biçiminin kanıtta buyruğa uyan, sevgi duyan veya yükümlülük için güvence veren kişi anlamlarıyla kullanıldığı yerlerde uygundur.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"الرضي صفة للمطيع أو المحب أو الضامن","concept_gloss":"söz dinleyen, seven veya güvence veren","contextual_glosses":[{"applicability":"Sıfatın buyruğa uyma ve itaat etme anlamında kullanıldığı bağlam içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Buyruğa uyma ve söz dinleme anlamını korur."},"facet_ids":["F001"],"text":"söz dinleyen","usage_role":"contextual"},{"applicability":"Sıfatın birine sevgi duyan kişiyi anlattığı bağlam içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin sevgi duyan taraf olmasını korur."},"facet_ids":["F002"],"text":"seven","usage_role":"contextual"},{"applicability":"Sıfatın bir borç veya yükümlülük için güvence üstlenen kişiyi anlattığı bağlam içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Güvence üstlenme ve sorumluluk alma yönünü korur."},"facet_ids":["F003"],"text":"güvence veren","usage_role":"contextual"}],"definition":"Aynı sıfat biçimi, kanıt sınırı içinde üç ayrı kullanım için kaydedilir: buyruğa uyan kişi, seven kişi ve bir yükümlülük için güvence veren kişi. Bu kullanımlar tek bir üretken kök çekirdeği yerine sınırlı bir kayıt alanı oluşturur.","distinctive_facets":[{"facet_id":"F001","role":"associated_use","statement":"Bir kullanım, buyruğa uyan ve söz dinleyen kişiyi niteler."},{"facet_id":"F002","role":"associated_use","statement":"İkinci kullanım, sevgi duyan kişiyi niteler."},{"facet_id":"F003","role":"associated_use","statement":"Üçüncü kullanım, bir yükümlülük için güvence veren kişiyi niteler."},{"facet_id":"F004","role":"core","statement":"Aynı sıfat biçiminin kanıtta yalnız bu üç kişi niteliğiyle sınırlı olarak kaydedilmesidir."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"söz dinleyen; seven; güvence veren"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı sıfat kullanımı ve aynı üç anlamı veren tam eşdeğer komşu seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Anlam çekirdeği, kullanım sınırı ve verilen üç anlam bakımından ayrım yoktur; iki dal aynı sınırlı sıfat kullanımını temsil eder.","focus_only":null,"gloss":"söz dinleyen, seven veya güvence veren","neighbor_only":null,"neighbor_ref":"root_000570/B004","relation_type":"synonym","shared_zone":"İki kart da aynı sıfat biçimini itaat eden, seven veya güvence veren kişi anlamlarıyla sınırlar."}],"source_phrase_ar":"الرضي المطيع والرضي المحب والرضي الضامن (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, biçimi söz dinleyen, seven ve güvence veren kişi için üç ayrı biçimde açıklar."}],"source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["TA"],"what_is_ar":"يدخل فيه الرضي بمعنى المطيع، والرضي بمعنى المحب، والرضي بمعنى الضامن كما نقل التهذيب","what_is_not_ar":"ليس الرضي هنا مجرد مرضي عنه ولا أصل الرضا العام"},"support_links":[]},{"boundary":"Dal yalnızca dağ ve kişi adlarını kapsar; hoşnutluk, karşılıklı kabul veya başka kavramsal anlamlar bu özel ad kimliklerine aktarılmaz.","branch_kind":"bare","branch_ref":"root_000569/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَاضِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:raADiyap|ROOT:rDw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:7:4:1","qac_word_ref":"101:7:4","surface_ar":"رَّاضِيَةٍ"}],"gloss":"bir dağ adı ve kadın adları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir biçim belirli bir dağın özel adı olarak kullanılır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı biçim ve onunla ilişkili başka bir biçim kadın adı olarak kullanılır."}}],"root_ar":"ر ض و","root_id":"root_000569","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Biçimlerin bir coğrafi varlığı veya kişiyi özel ad olarak belirlediği kullanımların toplu karşılığıdır.","boundary_detail":"Dal yalnızca dağ ve kişi adlarını kapsar; hoşnutluk, karşılıklı kabul veya başka kavramsal anlamlar bu özel ad kimliklerine aktarılmaz.","branch_image_ar":"رضوى ورضيا أعلام من المادة","concept_gloss":"bir dağ adı ve kadın adları","contextual_glosses":[{"applicability":"Biçimin belirli bir coğrafi varlığı adlandırdığı kullanım için açıklayıcı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli bir dağı adlandırma işlevini korur."},"facet_ids":["F001"],"text":"dağın özel adı","usage_role":"explanatory"},{"applicability":"Biçimin bir kişiye verilen özel ad olduğu kullanımlar için açıklayıcı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir kadını özel adla belirleme işlevini korur."},"facet_ids":["F002"],"text":"kadın adı","usage_role":"explanatory"}],"definition":"Aynı biçim ailesinin bir üyesi belirli bir dağın adı ve kadınlara verilen bir ad olarak, başka bir üyesi de kadın adı olarak kullanılır. Bu kullanımlar kavramsal hoşnutluk anlamı değil, adlandırma işlevi taşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir biçim belirli bir dağın özel adı olarak kullanılır."},{"facet_id":"F002","role":"source_variant","statement":"Aynı biçim ve onunla ilişkili başka bir biçim kadın adı olarak kullanılır."}],"identity_rationale":"Yetkili ifade, aynı biçim ailesinde bir dağ adını ve kadınlara verilen adları açıkça kaydeder. Bunlar sözlüksel anlamdan türetilmiş açıklamalar değil, özel ad kullanımları olarak tek adlandırma dalında tutulabilir.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir dağ adı; bir kadın adı"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"o dağın adına bağlılık bildiren biçim"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"bir kadın adı"}],"lexicalization_note":"Tanım, kanıtta yalın biçimler olarak verilen özel ad kullanımlarıyla sınırlıdır; adların sözlüksel kök anlamı taşıdığı varsayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı ad kümesini veren tam eşdeğer ile dağ, yer ve kişi adları alanındaki üç karşılaştırma, gönderim kimliği ile ortak adlandırma alanını en açık biçimde ayırdığı için seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Ad kimlikleri ve kullanım sınırları bakımından anlamlı bir fark yoktur; iki dal aynı özel ad kümesini temsil eder.","focus_only":null,"gloss":"aynı dağ ve kadın adları","neighbor_only":null,"neighbor_ref":"root_000570/B003","relation_type":"synonym","shared_zone":"İki kart da aynı dağ adını, ona bağlı biçimi ve aynı kadın adlarını kaydeder."},{"boundary_match":"field_only","distinction":"Özel adlar aynı tür varlığı adlandırsa da gönderimde bulundukları dağlar farklıdır; bu nedenle eşanlamlı değildirler.","focus_only":"Bir dağ adının yanında kadınlara verilen adları da kapsar.","gloss":"dağ ve kadın adları / başka bir dağ adı","neighbor_only":"Yalnızca başka bir belirli dağın adını kapsar.","neighbor_ref":"root_000706/B006","relation_type":"same_field","shared_zone":"Her ikisinde de bir dağın özel adla belirlenmesi söz konusudur."},{"boundary_match":"field_only","distinction":"Adlandırma işlevi ortak olsa da ad biçimleri ve gönderimde bulundukları kişi ya da yerler ayrıdır.","focus_only":"Belirli bir dağ ile kadınlara verilen adları kapsar.","gloss":"dağ ve kadın adları / başka yer ve kişi adları","neighbor_only":"Başka yer, su ve kişi adlarını kapsar.","neighbor_ref":"root_000361/B005","relation_type":"same_field","shared_zone":"Sözlük biçimlerinin kişi veya yer için özel ada dönüşmesi alanını paylaşırlar."},{"boundary_match":"field_only","distinction":"Komşu dalın gönderim alanı ve ad kümesi daha geniş ve bütünüyle başkadır; ortaklık yalnızca özel ad alanındadır.","focus_only":"Tek bir dağ adı ile belirli kadın adlarını sınırlar.","gloss":"dağ ve kadın adları / geniş özel ad kümesi","neighbor_only":"Kişi, yer, soy ve tarihsel olay adlarından oluşan daha geniş bir özel ad kümesini kapsar.","neighbor_ref":"root_000364/B007","relation_type":"same_field","shared_zone":"Her iki dal da kişi ve yerleri sözlüksel biçimlerden aktarılan özel adlarla belirler."}],"source_phrase_ar":"رضوى جبل (maqayis;ayn;sihah)؛ ومن أسماء النساء رضيا وتكبيرهما رضوى وثروى (tahdhib)","source_summary":"Tanıklıklar dağ adını ortak biçimde kaydeder; toplu ifade ayrıca aynı biçimin ve ilgili başka bir biçimin kadınlara verilen adlar arasında bulunduğunu belirtir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه رضوى اسم جبل، ورضيا ورضوى في أسماء النساء كما ورد في التهذيب","what_is_not_ar":"ليس استعمالا معنويا للرضا أو الرضوان أو التراضي"},"support_links":[]},{"boundary":"Bu dal yarışta üstün gelme kalıbını, özel adları ve aynı biçimdeki buyruğa uyma, sevme ya da güvence verme anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000570/B001","candidate_links":[{"candidate_id":"cand_a916d9d07302a8482a04","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"رَاضِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:raADiyap|ROOT:rDw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:7:4:1","qac_word_ref":"101:7:4","surface_ar":"رَّاضِيَةٍ"}],"gloss":"hoşnut olup uygun bulma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kimseye, şeye veya duruma karşı kızgınlık ve hoşnutsuzluk duymamak, onu gönle uygun bulmak."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyi beğenip benimsemek veya seçenekler arasından uygun bulmak."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ad biçimleri genel hoşnutluğu, kimi kayıtta ise çok güçlü hoşnutluğu bildirir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Edilgen biçimler, uygun bulunan ya da kendisinden hoşnut olunan kimseyi veya şeyi gösterir."}}],"root_ar":"ر ض و","root_id":"root_000570","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Duygusal hoşnutluk ile bilinçli benimsemenin birlikte bulunduğu genel çekirdek için kullanılır.","boundary_detail":"Bu dal yarışta üstün gelme kalıbını, özel adları ve aynı biçimdeki buyruğa uyma, sevme ya da güvence verme anlamlarını kapsamaz.","branch_image_ar":"الرِّضا خلاف السخط والقبول","concept_gloss":"hoşnut olup uygun bulma","contextual_glosses":[{"applicability":"Bir kimse, durum veya sonuç karşısındaki olumlu gönül durumunun öne çıktığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gönle aykırı bulmama ve hoşnutluk çekirdeğini korur."},"facet_ids":["F001"],"text":"hoşnut olma","usage_role":"general"},{"applicability":"Bir şeyi değerlendirip beğenme, benimseme veya seçme bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Değerlendirme sonunda benimseme ve seçme yönünü korur."},"facet_ids":["F002"],"text":"uygun bulma","usage_role":"contextual"},{"applicability":"Bir kimsenin veya şeyin başkası tarafından uygun bulunmuş olduğunu anlatan edilgen bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uygun bulunan varlığın edilgen konumunu korur."},"facet_ids":["F004"],"text":"beğenilmiş olma","usage_role":"contextual"},{"applicability":"Kaydın özellikle yüksek derece bildirdiği ad biçiminin açıklanmasında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hoşnutluğun olağandan yüksek derecesini korur."},"facet_ids":["F003"],"text":"derin hoşnutluk","usage_role":"explanatory"}],"definition":"Bir kimseyi, şeyi veya durumu gönle aykırı görmeyip uygun bulma ve ondan hoşnut olma durumudur. Ad ve edilgen biçimleri genel ya da güçlü hoşnutluğu ve uygun bulunan varlığı anlatabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kimseye, şeye veya duruma karşı kızgınlık ve hoşnutsuzluk duymamak, onu gönle uygun bulmak."},{"facet_id":"F002","role":"extension","statement":"Bir şeyi beğenip benimsemek veya seçenekler arasından uygun bulmak."},{"facet_id":"F003","role":"source_variant","statement":"Ad biçimleri genel hoşnutluğu, kimi kayıtta ise çok güçlü hoşnutluğu bildirir."},{"facet_id":"F004","role":"source_variant","statement":"Edilgen biçimler, uygun bulunan ya da kendisinden hoşnut olunan kimseyi veya şeyi gösterir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kızgınlığın karşıtı olan gönül durumunu ve benimsemenin sürekliliğini eksiltir.","preserves":"Bir şeyi olumlu değerlendirme yönünü korur."},"text":"beğenme"},{"category":"confusable","error_profile":{"adds":"Belirgin bir neşe ve coşku olayı çağrıştırır.","collision":"Sevinme olayını, daha durgun bir hoşnutluk ve benimseme durumuyla karıştırır.","fit":"displacement","loses":"Bir kimseyi veya şeyi uygun bulup benimseme değerlendirmesini yitirir.","preserves":"Olumlu bir iç yaşantı bulunmasını korur."},"text":"sevinç"},{"category":"confusable","error_profile":{"adds":"İstek dışı uyma veya güç karşısında geri çekilme anlamı ekler.","collision":"Gönüllü benimsemeyi zorunlu uyma davranışıyla karıştırır.","fit":"displacement","loses":"İçten uygun bulma ve hoşnutluk çekirdeğini yitirir.","preserves":"Bir duruma açıkça karşı çıkmama görünümünü korur."},"text":"boyun eğme"}],"identity_rationale":"Kaynakların ortak çekirdeği, kızgınlık ve hoşnutsuzluğun karşısında bir kimseyi, şeyi ya da durumu gönle uygun bulup benimsemedir. Ad biçimleri hoşnutluk durumunu, edilgen biçimler ise uygun bulunan veya kendisinden hoşnut olunan varlığı gösterir; kimi kayıtlar hoşnutluğun yoğunluğunu ayrıca belirtir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"hoşnut olmak; gönlüne uygun bulmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"hoşnut olan"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"beğenilmiş, uygun bulunmuş"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"kendisinden hoşnut olunan"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"uygun bulunmuş; eski kök yapısını koruyan biçim"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kendisinden hoşnut olunan adam; eski kök yapısını koruyan söyleyiş"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"hoşnutluk; hoşnutsuzluğun karşıtı"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"hoşnutluğu bildiren uzatılmış ad biçimi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"hoşnutluk; çok güçlü hoşnutluk"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"hoşnutluk bildiren ad"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"iki tarafın birbirini uygun bulması"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"birbirini uygun bulma ve karşılıklı anlaşma"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"şeyi beğenip uygun buldum"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"onu beğenip seçtim"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"ondan hoşnut oldum"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"onu arkadaş olarak uygun buldum"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ondan ya da onunla olmaktan hoşnut oldum"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"beğenilen, hoşnutluk veren yaşayış"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"onu benden hoşnut ettim"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"onu hoşnut ettim"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"uğraştıktan sonra onu hoşnut ettim"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"onun gönlünü yapmaya çalıştım, sonunda benden hoşnut oldu"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"birbirlerini uygun bulup anlaştılar"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"kulun Tanrı'nın hükmünden hoşnutsuzluk duymaması"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"Tanrı'nın kulunu buyruklarına uyar ve yasaklarından kaçınır görmesi"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"beğenilmiş, uygun bulunmuş"}],"lexicalization_note":"Çekirdek yalın hoşnutluk ve benimsemedir; nesne, ilgeç, karşılıklılık, ettirme veya isteme içeren birimler yalnızca kendi yapılarında tanıklanan anlamı taşır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; karşılıklı anlaşma, yüz çevirme, hayranlık ve aynı kökün yarışta üstün gelme, özel ad ve eşsesli sıfat dalları, seçilen beş ayrımın ötesinde çekirdeği daha iyi açıklamadığı veya gereksiz tekrar oluşturduğu için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdek anlam örtüşür; odak dal komşu kartta bulunmayan karşılıklılık, ettirme, hoşnutluğu isteme ve ilgeçli kalıpları da kapsadığı için sınırlar tam olarak aynı değildir.","focus_only":"Karşılıklılık, ettirme, hoşnutluğu isteme ve çeşitli ilgeçli kalıpları da kapsayan daha geniş yapı alanı.","gloss":"hoşnutluk ve benimsemenin ortak çekirdeği","neighbor_only":null,"neighbor_ref":"root_000569/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da hoşnutsuzluğun karşıtını, uygun bulmayı ve temel etkin-edilgen biçimleri kapsar."},{"boundary_match":"partial","distinction":"Odak dal içsel hoşnutluk ve uygun bulmayı çekirdek yapar; komşu dal ise hoşnutluk şartı bulunmadan bir şeyi alma veya geçerli sayma eylemini de kapsar.","focus_only":"Gönülde hoşnutsuzluk bulunmaması ve kişiye ya da duruma yönelik içsel uygunluk.","gloss":"hoşnutlukla benimseme ile bir şeyi alma","neighbor_only":"Özür, armağan, iş veya benzeri bir şeyi teslim alıp geçerli saymaya uzanan daha geniş alma alanı.","neighbor_ref":"root_001198/B004","relation_type":"near_synonym","shared_zone":"Her ikisi de bir şeyi geri çevirmeyip uygun bulma ve benimseme alanında kesişir."},{"boundary_match":"opposed","distinction":"Odak dal olumlu gönül uygunluğunu ve benimsemeyi, komşu dal ise kızgınlıkla birleşebilen olumsuz değerlendirme ve istememeyi bildirir.","focus_only":"Gönle uygun bulma, hoşnut olma ve benimseme.","gloss":"hoşnutluk ile hoşnutsuzluk karşıtlığı","neighbor_only":"Kızma, hoşnutsuz olma, bir şeyi istemeyip geri çevirme.","neighbor_ref":"root_000686/B001","relation_type":"antonym","shared_zone":"İki dal aynı kişi, şey veya durum karşısındaki değerlendirme ekseninin karşı uçlarını gösterir."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeğinde bir nesne veya durumu uygun bulma vardır; komşu dal değerlendirme gerektirmeden haz, neşe veya rahatlık yaşantısını öne çıkarır.","focus_only":"Bir kimseyi, şeyi veya durumu uygun bulup benimseme değerlendirmesi.","gloss":"hoşnutluk ile haz duyma","neighbor_only":"Haz, neşe, rahatlık ve içinde bulunulan nimetlerden tat alma.","neighbor_ref":"root_001174/B001","relation_type":"near_neighbor","shared_zone":"Her ikisi de olumlu ve gönle iyi gelen bir iç durumu anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal uygun bulma ve benimsemeyle sınırlı kalabilir; komşu dal ise daha kalıcı sevgi ve bağlılığı çekirdek yapar.","focus_only":"Uygun bulma ve hoşnutsuzluk taşımama, kalıcı duygusal bağ gerektirmez.","gloss":"hoşnutluk ile sevgi","neighbor_only":"Kişi veya şeye yerleşik sevgi, bağlılık ve karşılıklı yakınlık.","neighbor_ref":"root_000286/B002","relation_type":"near_neighbor","shared_zone":"İki dal bir kimseye veya şeye olumlu yöneliş bildirebilir."}],"source_phrase_ar":"أصل واحد يدل على خلاف السخط (maqayis)؛ الرضا في الأصل من بنات الواو والرضوان من الرضا (ayn)؛ الرضوان الرضا والمرضاة مثله ورضيت الشيء وارتضيته (sihah)؛ رضي فلان يرضى رضى والرضي المرضي والرضا مقصور (tahdhib)؛ رضي يرضى رضا فهو مرضي ومرضو والرضوان الرضا الكثير (mufradat)","source_summary":"Kaynaklar anlamı hoşnutsuzluğun karşıtı olan gönül uygunluğu ve benimseme çevresinde birleştirir. Aynı toplu tanıklık, ad biçimlerinin genel veya yoğun hoşnutluğu, edilgen biçimlerin de uygun bulunan varlığı gösterebildiğini aktarır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الرضا والرضوان والمرضاة ورضي عن الشيء أو به أو عليه وارتضاه وأرضاه واسترضاه وترضاه والتراضي والمراضاة إذا كان المعنى إظهار القبول أو حصوله","what_is_not_ar":"ليس غلبة راضاني فرضوته ولا رضوى علما ولا الرَّضِيّ بمعانيه المفردة عند ابن الأعرابي"},"support_links":["sup_acd01348899473b536a2"]},{"boundary":"Anlam yalnızca tanıklanan çekişme ve ardından üstün gelme kalıbına bağlıdır; hoşnutluk, karşılıklı anlaşma veya genel güç kullanımı değildir.","branch_kind":"non_bare","branch_ref":"root_000570/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَاضِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:raADiyap|ROOT:rDw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:7:4:1","qac_word_ref":"101:7:4","surface_ar":"رَّاضِيَةٍ"}],"gloss":"çekişmede alt etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Karşı tarafın giriştiği çekişmede onu yenip üstün gelmek."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yenme anlamı, iki taraflı çekişmeyi ve sonucu birlikte bildiren özel söz dizisi içinde kurulur."}}],"root_ar":"ر ض و","root_id":"root_000570","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca birinin kendisiyle çekişen kişiyi aynı işte yendiğini bildiren özel kullanım için uygundur.","boundary_detail":"Anlam yalnızca tanıklanan çekişme ve ardından üstün gelme kalıbına bağlıdır; hoşnutluk, karşılıklı anlaşma veya genel güç kullanımı değildir.","branch_image_ar":"غلبة راضاني فرضوته","concept_gloss":"çekişmede alt etme","contextual_glosses":[{"applicability":"Karşılıklı yarışma görünümünün belirgin olduğu ve taraflardan birinin kazandığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki taraflı yarışmayı ve yenme sonucunu korur."},"facet_ids":["F001","F002"],"text":"yarışta yenme","usage_role":"contextual"},{"applicability":"Yarışın türü belirtilmediğinde kalıbın sonuç yönünü açıklamak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli bir karşılaşmada öteki tarafı geçme sonucunu korur."},"facet_ids":["F001","F002"],"text":"karşılaşmada üstün gelme","usage_role":"explanatory"}],"definition":"Belirli bir karşılaşmada kendisiyle çekişen kişiyi o işte alt etmeyi anlatan kalıplaşmış kullanımdır. Genel hoşnutluk veya genel zorlama anlamına genişletilemez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Karşı tarafın giriştiği çekişmede onu yenip üstün gelmek."},{"facet_id":"F002","role":"specialization","statement":"Yenme anlamı, iki taraflı çekişmeyi ve sonucu birlikte bildiren özel söz dizisi içinde kurulur."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bir başkasının gönül durumunu olumluya çevirme anlamı ekler.","collision":"Bu özel yenme kalıbını kökün hoşnutluk dalıyla karıştırır.","fit":"displacement","loses":"Çekişme ilişkisini ve karşı tarafı yenme sonucunu bütünüyle yitirir.","preserves":"Aynı kökün başka kullanımlarını yüzeysel olarak çağrıştırır."},"text":"hoşnut etme"},{"category":"alternative","error_profile":{"adds":"Çatışmanın karşılıklı uzlaşmayla sona ermesi anlamını ekler.","collision":"Yarışta üstün gelmeyi karşılıklı anlaşmayla karıştırır.","fit":"displacement","loses":"Bir tarafın ötekini yenmesi sonucunu yitirir.","preserves":"İki tarafın aynı olayda yer almasını korur."},"text":"barışma"},{"category":"alternative","error_profile":{"adds":"Yarışma olmadan güç, tehdit veya sürekli zorlama uygulanmasını da kapsar.","collision":"Belirli çekişmede yenme ile genel zorlayıcı egemenliği karıştırabilir.","fit":"broadening","loses":null,"preserves":"Bir tarafın ötekine üstün gelmesi yönünü korur."},"text":"baskı kurma"}],"identity_rationale":"Kaynak ifadesi genel bir üstünlük kökü değil, bir kişinin belirli bir işte kendisiyle çekişen kişiyi yenmesini bildiren kalıplaşmış bir söz dizisini verir. Geçici dal çerçevesi bu yapısal sınırı ve yenme sonucunu doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"o benimle çekişti, ben de onu o işte yendim"}],"lexicalization_note":"Bu dal yalın bir kök anlamı sayılmaz; karşı tarafın yarışmaya giriştiğini ve konuşanın onu aynı işte yendiğini bildiren tanıklı söz dizisiyle sınırlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; karşılık verme yarışına, genel kişi yenmeye, genel üstünlük ve tartışmada bastırmaya ayrılan adaylar seçilen ayrımlarla yinelendi, aynı kökün hoşnutluk, özel ad ve sıfat dalları ise bu kalıbın anlam sınırını keskinleştirmedi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Sunulan kartlarda yapı, katılımcılar ve sonuç bakımından hiçbir sınır farkı yoktur; dallar tam karşılık olarak değerlendirilebilir.","focus_only":null,"gloss":"aynı kalıpta çekişeni yenme","neighbor_only":null,"neighbor_ref":"root_000569/B005","relation_type":"synonym","shared_zone":"Her iki dal da aynı söz dizisini ve çekişen kişiyi o işte yenme sonucunu verir."},{"boundary_match":"partial","distinction":"Sonuç çekirdeği örtüşür, ancak her dal yenme anlamını kendi kalıplaşmış fiil yapısına bağlar; bu nedenle yalın biçimler arasında genel bir eşitlik kurulamaz.","focus_only":"Yalnızca odak köke ait tanıklı çekişme kalıbı.","gloss":"aynı işte yarışıp yenme","neighbor_only":"Karşılıklı girişme veya bir işi ele alma eylemini kendi söz kalıbıyla kurma.","neighbor_ref":"root_001028/B007","relation_type":"near_synonym","shared_zone":"İki dal da karşılıklı girişilen bir işte taraflardan birinin ötekini yenmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal çekişmenin türünü açık bırakır; komşu dal karşı çıkma ve zıtlaşma alanını kendi yapısının parçası yapar.","focus_only":"Çekişmenin türünü ayrıca adlandırmayan özel yenme kalıbı.","gloss":"çekişmede üstün gelme","neighbor_only":"Karşı çıkma ve zıtlaşma biçimindeki çekişmeye bağlı özel yenme kalıbı.","neighbor_ref":"root_000808/B003","relation_type":"near_synonym","shared_zone":"Her ikisi de iki taraflı bir çekişmede karşı tarafı yenme sonucunu bildirir."},{"boundary_match":"partial","distinction":"Odak dal iki taraflı çekişme kalıbına bağlı tekil sonucu anlatır; komşu dal güçle bastırma ve egemenlik dahil daha geniş bir üstünlük alanını kapsar.","focus_only":"Belirli bir söz dizisinde, kendisiyle çekişen kişiyi o işte yenme.","gloss":"özel yarış zaferi ile genel üstünlük","neighbor_only":"Genel güç, zorlama, egemenlik kurma ve çeşitli alanlarda üstünlük.","neighbor_ref":"root_001098/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir tarafın ötekini geçmesi veya yenmesi sonucu bulunur."},{"boundary_match":"field_only","distinction":"Odak dal sonuç olarak yenmeyi zorunlu kılar; komşu dal yarışma ve boy ölçüşme sürecini, bir kazanan bulunmasa da anlatabilir.","focus_only":"Çekişmenin kazananını ve öteki tarafın yenildiğini bildirir.","gloss":"yarışma ile yarışta kazanma","neighbor_only":"Yarışma, boy ölçüşme veya karşılaştırılma sürecini sonuç belirtmeden anlatabilir.","neighbor_ref":"root_000745/B007","relation_type":"same_field","shared_zone":"İki dal da kişilerin birbirleriyle yarıştığı veya boy ölçüştüğü alana aittir."}],"source_phrase_ar":"قال أبو عبيد راضاني فلان فرضوته (maqayis)؛ راضاني فلان فرضوته أرضوه بالضم إذا غلبته فيه (sihah)","source_summary":"Tanıklıklar aynı kalıplaşmış söz dizisini, bir kişinin kendisiyle çekişen ötekini o işte yenmesi anlamında birleştirir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه قولهم راضاني فلان فرضوته أو أرضوه إذا غلبته في الأمر","what_is_not_ar":"ليس المراضاة بمعنى التراضي والقبول المتبادل ولا الرضا خلاف السخط"},"support_links":[]},{"boundary":"Bu dal genel hoşnutluk veya üstün gelme anlamı taşımaz; yalnız tanıklanan dağ adı, kadın adı ve dağla ilişki bildiren biçimlerle sınırlıdır.","branch_kind":"bare","branch_ref":"root_000570/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَاضِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:raADiyap|ROOT:rDw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:7:4:1","qac_word_ref":"101:7:4","surface_ar":"رَّاضِيَةٍ"}],"gloss":"dağ ve kadın adı ailesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir dağın özel adı olarak kullanılan biçim."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı kökten bir biçimin kadın adı olarak kullanılması ve küçültülmemiş karşılığının da aktarılması."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dağ adından türetilen sıfatın o dağla ilişki veya köken bildirmesi."}}],"root_ar":"ر ض و","root_id":"root_000570","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tanıklanan dağ adını, kadın adını ve dağ adına bağlı ilişki biçimini yüzey adlarını üretmeden birlikte açıklamak için kullanılır.","boundary_detail":"Bu dal genel hoşnutluk veya üstün gelme anlamı taşımaz; yalnız tanıklanan dağ adı, kadın adı ve dağla ilişki bildiren biçimlerle sınırlıdır.","branch_image_ar":"رضوى ورضيا أسماء","concept_gloss":"dağ ve kadın adı ailesi","contextual_glosses":[{"applicability":"Biçim bir coğrafi yükseltinin kendine özgü adı olarak kullanıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dağ adı olma işlevini eksiksiz korur."},"facet_ids":["F001"],"text":"bir dağın özel adı","usage_role":"contextual"},{"applicability":"Aynı kökten biçim bir kadını adlandırdığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadın adı olma işlevini eksiksiz korur."},"facet_ids":["F002"],"text":"bir kadın adı","usage_role":"contextual"},{"applicability":"Dağ adına bağlı türemiş sıfatın ilişki veya köken bildirdiği bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli dağa bağlılık ve ilişki yönünü korur."},"facet_ids":["F003"],"text":"o dağla ilgili","usage_role":"explanatory"}],"definition":"Bir dağın adı olarak kullanılan biçim ile aynı kökten bir kadın adı ve bunlara bağlı adlandırma ailesidir. Dağ adından türeyen biçim, o dağla ilişkiyi bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir dağın özel adı olarak kullanılan biçim."},{"facet_id":"F002","role":"source_variant","statement":"Aynı kökten bir biçimin kadın adı olarak kullanılması ve küçültülmemiş karşılığının da aktarılması."},{"facet_id":"F003","role":"extension","statement":"Dağ adından türetilen sıfatın o dağla ilişki veya köken bildirmesi."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bir gönül durumu ve değerlendirme anlamı ekler.","collision":"Adlandırma dalını kökün genel hoşnutluk dalıyla karıştırır.","fit":"displacement","loses":"Özel ad ve ada bağlı ilişki işlevlerinin tümünü yitirir.","preserves":"Yalnızca aynı kökle yüzeysel bağı korur."},"text":"hoşnutluk"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kadın adı kullanımını ve dağa bağlı türemiş ilişki biçimini eksiltir.","preserves":"Dağın özel adla anılması yönünü korur."},"text":"yer adı"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dağ adını ve o dağla ilişki bildiren türemiş biçimi eksiltir.","preserves":"Kadını adlandırma işlevini korur."},"text":"kadın adı"}],"identity_rationale":"Kaynak ifadesi bir dağ adını, o dağla ilişki bildiren türemiş biçimi ve aynı kökten kadın adlarını birlikte tanıklar. Geçici çerçeve bunları ortak bir sözlük anlamı gibi birleştirmeden, adlandırma ailesi olarak doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bir dağın ve bir kadının adı"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"söz konusu dağla ilgili veya o dağdan olan"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"bir kadın adı"}],"lexicalization_note":"Mekanik sınıf yalındır; ancak tanıklıklar özel ad ve addan türeyen ilişki biçimleridir, bu yüzden bunlardan genel bir yalın kök anlamı çıkarılamaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; öteki yer ve kişi adı aileleri seçilen aynı-alan örneklerini yineledi, aynı kökün hoşnutluk, yarışta üstün gelme ve eşsesli sıfat dalları ise adlandırma çekirdeğiyle anlam ilişkisi kurmadığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Adlandırma çekirdeği örtüşür; odak dal verilen kanıtta dağ adına bağlı türemiş ilişki biçimini ayrıca içerdiği için sınırı biraz daha geniştir.","focus_only":"Dağ adına bağlı ilişki veya köken bildiren türemiş sıfatın açıkça kapsanması.","gloss":"aynı dağ ve kadın adları","neighbor_only":null,"neighbor_ref":"root_000569/B007","relation_type":"near_synonym","shared_zone":"İki dal da aynı kökten gelen dağ ve kadın adlarını kapsar."},{"boundary_match":"field_only","distinction":"Ortaklık yalnızca adlandırma düzenindedir; hangi kişi ve yerleri adlandırdıkları ile türemiş biçimlerin dayandığı özel adlar bütünüyle ayrıdır.","focus_only":"Belirli bir dağ adı, kadın adı ve dağa bağlı ilişki sıfatından oluşan aile.","gloss":"kişi ve yer adları","neighbor_only":"Bir kadın adıyla birlikte ülke, köy ve başka yer adları ile bunlara bağlı ilişki biçimleri.","neighbor_ref":"root_001697/B005","relation_type":"same_field","shared_zone":"Her iki dal da aynı sözcük ailesinden kişi ve yer adları ile ada bağlı biçimler üretir."},{"boundary_match":"field_only","distinction":"Ad olma işlevi ortaktır, fakat adların taşıyıcıları ve bağlı oldukları söz ailesi ayrıdır; anlam bakımından birbirlerinin yerine geçmezler.","focus_only":"Bir dağ ve kadın adlarıyla sınırlı belirli adlandırma ailesi.","gloss":"sözden türeyen özel adlar","neighbor_only":"Çeşitli kişi ve yer adlarını başka bir söz ailesi altında toplayan daha geniş ad dizisi.","neighbor_ref":"root_000943/B007","relation_type":"same_field","shared_zone":"İki dal da bir söz biçiminin kişi veya yer adı olarak kullanılmasını kaydeder."},{"boundary_match":"field_only","distinction":"Odak dal adlandırma ailesi ve türemiş ilişki biçimi kurar; komşu dal ise başka bir biçimin yer veya erkek adı olmasını tanıklar.","focus_only":"Dağ ve kadın adı ile dağa bağlı ilişki biçiminin birlikte bulunması.","gloss":"yer ve kişi adı kullanımı","neighbor_only":"Tek bir biçimin yer veya erkek adı olarak kullanılması.","neighbor_ref":"root_001013/B004","relation_type":"same_field","shared_zone":"Her iki dalda da sözlükteki biçim bir yerin veya kişinin özel adı olur."},{"boundary_match":"field_only","distinction":"Odak dal kadın adı kullanımının yanında dağ adını ve ona bağlı ilişki biçimini taşır; komşu dalın ortaklığı yalnız kadın adı olma işlevindedir.","focus_only":"Dağ adı, kadın adı ve dağa bağlı türemiş sıfat.","gloss":"kadın adı kullanımı","neighbor_only":"Yalnızca başka bir kadın adı olarak kaydedilen biçim.","neighbor_ref":"root_000848/B009","relation_type":"same_field","shared_zone":"Her iki dal bir söz biçiminin kadın adı olarak kullanılmasını içerir."}],"source_phrase_ar":"رضوى جبل (maqayis;ayn)؛ رضوى جبل بالمدينة والنسبة إليه رضوى (sihah)؛ من أسماء النساء رضيا وتكبيرهما رضوى وثروى (tahdhib)","source_summary":"Toplu tanıklık bir dağ adında birleşir; ayrıca dağla ilişki bildiren türemiş biçimi ve aynı kökten kadın adlarını kaydeder. Bu kullanımlar genel bir nitelik değil, adlandırma ve ada bağlı ilişki alanı oluşturur.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه رضوى علما للجبل وما يلحق به من النسبة إليه ورضيا اسما للنساء وتكبيره رضوى","what_is_not_ar":"ليس الرضا مصدرا ولا الرضوان ولا غلبة راضاني"},"support_links":[]},{"boundary":"Üç anlam birbirine karıştırılmaz: buyruğa uyma davranışı, sevgi yönelimi ve güvence üstlenme ayrı bağlamsal seçeneklerdir; beğenilmiş olma anlamı bu dala girmez.","branch_kind":"bare","branch_ref":"root_000570/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"رَاضِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:raADiyap|ROOT:rDw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:7:4:1","qac_word_ref":"101:7:4","surface_ar":"رَّاضِيَةٍ"}],"gloss":"buyruğa uyan, seven veya güvence veren","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Aynı sıfat biçiminin ortak bir anlamda birleşmeyen üç seçenekli okumaya sahip olması."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Buyruğa uyan ve kendisinden isteneni yerine getiren kişi."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kimseyi veya şeyi seven kişi."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir yükümlülük için güvence veren veya sorumluluğu üstlenen kişi."}}],"root_ar":"ر ض و","root_id":"root_000570","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Biçimin üç tanıklı okumasını birlikte listeler; gerçek bağlamda bunlardan yalnız uygun olanı seçilmelidir.","boundary_detail":"Üç anlam birbirine karıştırılmaz: buyruğa uyma davranışı, sevgi yönelimi ve güvence üstlenme ayrı bağlamsal seçeneklerdir; beğenilmiş olma anlamı bu dala girmez.","branch_image_ar":"الرَّضِيّ طاعة ومحبة وضمان","concept_gloss":"buyruğa uyan, seven veya güvence veren","contextual_glosses":[{"applicability":"Bir kişinin verilen buyruğu yerine getirmesi veya istenen davranışı göstermesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Buyruğa uyma ve isteneni yerine getirme yönünü korur."},"facet_ids":["F002"],"text":"buyruğa uyan","usage_role":"contextual"},{"applicability":"Sıfatın bir kimseye veya şeye sevgi duyan kişiyi gösterdiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sevgi yönelimini doğrudan ve eksiksiz korur."},"facet_ids":["F003"],"text":"seven","usage_role":"contextual"},{"applicability":"Bir kişinin başkasının yükümlülüğü için sorumluluk üstlendiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yükümlülüğe güvence olma ve sorumluluk üstlenme yönünü korur."},"facet_ids":["F004"],"text":"güvence veren","usage_role":"contextual"}],"definition":"Tek bir sıfat biçiminin bağlama göre buyruğa uyan, seven veya bir yükümlülüğe güvence veren kişiyi göstermesidir. Bu üç okuma seçeneklidir ve aynı kullanımda birlikte varsayılmaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Aynı sıfat biçiminin ortak bir anlamda birleşmeyen üç seçenekli okumaya sahip olması."},{"facet_id":"F002","role":"source_variant","statement":"Buyruğa uyan ve kendisinden isteneni yerine getiren kişi."},{"facet_id":"F003","role":"source_variant","statement":"Bir kimseyi veya şeyi seven kişi."},{"facet_id":"F004","role":"source_variant","statement":"Bir yükümlülük için güvence veren veya sorumluluğu üstlenen kişi."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Başkasının olumlu değerlendirmesine uğramış olma anlamı ekler.","collision":"Bu üçlü sıfat dalını edilgen biçimde uygun bulunma dalıyla karıştırır.","fit":"displacement","loses":"Buyruğa uyma, sevme ve güvence verme okumalarının tümünü yitirir.","preserves":"Aynı yazılı biçimin başka dalda görülen yüzeyini çağrıştırır."},"text":"beğenilmiş"},{"category":"confusable","error_profile":{"adds":"Kişinin kendi gönül durumuna ilişkin hoşnutluk anlamı ekler.","collision":"Eşsesli sıfatı kökün genel hoşnutluk dalıyla karıştırır.","fit":"displacement","loses":"Tanıklanan buyruğa uyma, sevme ve güvence verme seçeneklerini yitirir.","preserves":"Olumlu bir kişi niteliği izlenimini korur."},"text":"hoşnut olan"},{"category":"alternative","error_profile":{"adds":"Genel dürüstlük, sağlamlık ve sözünde durma gibi tanıklanmayan kişilik özelliklerini ekler.","collision":"Belirli bir yükümlülüğü üstlenmeyi genel güvenilirlikle karıştırır.","fit":"broadening","loses":null,"preserves":"Güvence veren kişiye duyulan güven yönünü kısmen korur."},"text":"güvenilir"}],"identity_rationale":"Kaynak tanıklığı aynı sıfat biçimine buyruğa uyan, seven ve bir yükümlülüğe güvence veren kişi anlamlarını yükler. Geçici çerçeve ancak bunlar tek bir birleşik kişilik niteliği değil, bağlama göre seçilen üç ayrı okuma olarak tutulursa geçerlidir.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"buyruğa uyan, seven ya da güvence veren"}],"lexicalization_note":"Mekanik sınıf yalındır; sıfat, herhangi bir ek söz kalıbına bağlı olmadan üç ayrı anlamdan birini taşır, fakat bu anlamlar ortak bir çekirdekte birleştirilemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sevgiye ayrılan ikinci aday, yükümlülük ve güvenceye yakın adaylar ile ihanet ve söz bozma alanları seçilen ayrımları yineledi veya yalnız dolaylı karşıtlık kurdu, aynı kökün diğer üç dalı da eşseslilik dışında anlam sınırını açıklamadı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Sunulan kartlarda anlam seçenekleri ve sınırlar bütünüyle aynıdır; dallar arasında ayırıcı bir içerik bulunmaz.","focus_only":null,"gloss":"aynı üç seçenekli sıfat","neighbor_only":null,"neighbor_ref":"root_000569/B006","relation_type":"synonym","shared_zone":"Her iki dal da aynı sıfatı buyruğa uyan, seven veya güvence veren kişi anlamlarıyla verir."},{"boundary_match":"partial","distinction":"Odaktaki uyma yalnız üç seçenekten biridir ve zorunlu olarak dinsel değildir; komşu dal dinsel boyun eğme ve doğru yolda kalmayı çekirdek yapar.","focus_only":"Buyruğa uyma yanında sevme ve güvence verme seçeneklerini de taşıyan eşsesli sıfat.","gloss":"buyruğa uyma ile dinsel boyun eğme","neighbor_only":"Din yolunda boyun eğme, doğru yolda kalma ve belirli toplumsal uyma ilişkileri.","neighbor_ref":"root_001260/B001","relation_type":"near_synonym","shared_zone":"Odak sıfatın bir okuması ile komşu dal, istenen buyruğa uyma davranışında kesişir."},{"boundary_match":"partial","distinction":"Odak dal sevgiyi yalnız sıfatın seçenekli bir okuması olarak verir; komşu dal sevgi ve karşılıklı yakınlığı bağımsız, geniş bir anlam alanı olarak kurar.","focus_only":"Sevmenin yanı sıra buyruğa uyma ve güvence verme okumalarını da taşıyan tek sıfat.","gloss":"seven kişi ile sevgi alanı","neighbor_only":"Sevgi, yakınlık, karşılıklı sevme ve sevginin oluşma yollarından meydana gelen geniş alan.","neighbor_ref":"root_001634/B001","relation_type":"near_synonym","shared_zone":"Odak sıfatın bir okuması, bir kimseye veya şeye sevgi duyan kişiyi gösterir."},{"boundary_match":"partial","distinction":"Odak dal yalnız sorumluluğu üstlenen kişiyi niteleyen seçenekli bir sıfat verir; komşu dal güvence kurumunu ve üstlenilen mali ya da hukuki yükü kapsar.","focus_only":"Güvence veren kişi okumasını, iki başka eşsesli okumayla aynı sıfatta taşıması.","gloss":"güvence veren kişi ile güvence yükümlülüğü","neighbor_only":"Borç, ödeme veya başka bir hakkı üstlenmeye ilişkin güvence ve yükümlülük düzeni.","neighbor_ref":"root_000357/B004","relation_type":"near_synonym","shared_zone":"Odak sıfatın bir okuması ile komşu dal, başkasının yükümlülüğü için sorumluluk üstlenmede kesişir."}],"source_phrase_ar":"الرَّضِيّ المطيع؛ الرَّضِيّ المحب؛ الرَّضِيّ الضامن (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık sıfatı, birbirinden ayrı biçimde buyruğa uyan, seven veya bir yükümlülüğe güvence veren kişi için kullanır."}],"source_summary":"Birden çok kaynağın ortaklaştırdığı bir anlam yoktur; veri, aynı sıfat için üç ayrı okuma veren tek bir tanıklığa dayanır.","sources":["TA"],"what_is_ar":"يدخل فيه الرَّضِيّ إذا استعمل بمعنى المطيع أو المحب أو الضامن كما حكاه ابن الأعرابي","what_is_not_ar":"ليس الرَّضِيّ بمعنى المرضي ولا الرضا مصدرا عاما ولا رضوانا"},"support_links":[]},{"boundary":"Bu dal, yaşamın kendisiyle yaşamın niteliğini kapsar; yiyecek, içecek, geçim kaynağı veya yaşanan yer gibi yaşamı sağlayan araçları kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001067/B001","candidate_links":[{"candidate_id":"cand_6ec3133d5c1643263ef3","lane":"micro"},{"candidate_id":"cand_3faf863ac4dded8d2638","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عِيشَة","morph_features":"STEM|POS:N|LEM:Eiy$ap|ROOT:Ey$|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"101:7:3:1","qac_word_ref":"101:7:3","surface_ar":"عِيشَةٍ"}],"gloss":"yaşam ve yaşayış durumu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, canlı olma ve yaşamı sürdürme olgusu olarak yaşamın kendisidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yaşayışın iyi, hoşnut edici, övgüye değer, kötü veya dar ve sıkıntılı oluşu belirli nitelemelerle anlatılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İyi durumda yaşayan kimse, yaşayışının elverişli oluşuna dayanılarak nitelenebilir."}}],"root_ar":"ع ي ش","root_id":"root_001067","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaşamın kendisi ile bu yaşamın iyi, kötü, hoşnut edici veya sıkıntılı oluşunu birlikte temsil eden en geniş doğal karşılıktır.","boundary_detail":"Bu dal, yaşamın kendisiyle yaşamın niteliğini kapsar; yiyecek, içecek, geçim kaynağı veya yaşanan yer gibi yaşamı sağlayan araçları kapsamaz.","branch_image_ar":"الحياة والعيشة","concept_gloss":"yaşam ve yaşayış durumu","contextual_glosses":[{"applicability":"Canlı olma ve yaşamı sürdürme olgusunun kendisinin anlatıldığı yalın bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaşamın kendisini herhangi bir geçim aracı veya nitelik eklemeden karşılar."},"facet_ids":["F001"],"text":"yaşam","usage_role":"general"},{"applicability":"Yaşam koşullarının iyi, elverişli veya övgüye değer olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaşayışın olumlu niteliğini ve bunun yaşam durumuna bağlı oluşunu korur."},"facet_ids":["F002"],"text":"iyi bir yaşayış","usage_role":"contextual"},{"applicability":"Yaşayışın darlık ve güçlükle nitelenmesi gereken olumsuz bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaşam durumundaki darlığı ve sıkıntıyı açık biçimde korur."},"facet_ids":["F002"],"text":"dar ve sıkıntılı yaşam","usage_role":"contextual"},{"applicability":"Bir kişinin iyi yaşayış durumuna dayanılarak nitelendiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiye yönelen nitelemenin iyi yaşayış durumundan doğduğunu korur."},"facet_ids":["F003"],"text":"durumu iyi olan kimse","usage_role":"explanatory"}],"definition":"Canlıların sürdürdüğü yaşamın kendisini ve bu yaşamın iyi, hoşnut edici, övgüye değer, kötü ya da dar ve sıkıntılı oluşunu belirtir. Ayrıca iyi durumda yaşayan kimseyi niteleyen bağlı bir kullanımı kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, canlı olma ve yaşamı sürdürme olgusu olarak yaşamın kendisidir."},{"facet_id":"F002","role":"specialization","statement":"Yaşayışın iyi, hoşnut edici, övgüye değer, kötü veya dar ve sıkıntılı oluşu belirli nitelemelerle anlatılır."},{"facet_id":"F003","role":"associated_use","statement":"İyi durumda yaşayan kimse, yaşayışının elverişli oluşuna dayanılarak nitelenebilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yaşamı sağlayan araç ve kaynakları öne çıkarır.","collision":"Kökün geçim araçları ve geçinme ortamıyla ilgili ikinci dalıyla karışır.","fit":"displacement","loses":"Yaşamın kendisini ve yaşayışın iyi ya da kötü niteliğini karşılamaz.","preserves":"Yaşamı sürdürme alanıyla genel bir bağlantıyı korur."},"text":"geçim"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yaşayışın niteliğini ve canlı olma olgusunun bütününü karşılamaz.","preserves":"Bir canlının yaşadığı süreyle yaşam kavramının bir yönünü korur."},"text":"ömür"}],"identity_rationale":"Kaynak ifadesi, yaşamın kendisini ve özellikle canlılara özgü yaşama durumunu temel anlam olarak verir; ayrıca bu yaşamın iyi, hoşnut edici, övgüye değer, kötü ya da dar ve sıkıntılı oluşunu belirtir. İyi durumda yaşayan kişiyi niteleyen kullanım da bu yaşam durumuna bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yaşam"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yaşadı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"Tanrı ona hoşnut olacağı bir yaşam verdi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yaşayış biçimi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"iyi bir yaşayış"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"övgüye değer bir yaşayış"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"dar ve sıkıntılı yaşam"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"durumu iyi olan kimse"}],"lexicalization_note":"Yalın kullanım yaşamın kendisini belirtir; iyi, kötü, hoşnut edici ya da sıkıntılı oluş gibi nitelikler ise belirli biçim ve söz öbeklerine bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yaşamın kendisiyle geçim araçları, genel durum iyiliği ve bulunulan durum arasındaki üç ayrım dal sınırını en açık biçimde gösterdi. Öteki adaylar yalnızca uzak bir olay alanını paylaştığı veya dar bir örnek sunduğu için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dalında anlatılan şey yaşayanın yaşamı ve bu yaşamın niteliğidir; komşu dalda ise yaşamı mümkün kılan araçlar, ortamlar ve bunları edinme uğraşıdır.","focus_only":"Yaşamın kendisini ve yaşayışın iyi, kötü veya sıkıntılı niteliğini belirtir.","gloss":"yaşam ile geçim araçları","neighbor_only":"Yaşamı sağlayan yiyecek, içecek, kaynak, yer, zaman ve edinme çabasını belirtir.","neighbor_ref":"root_001067/B002","relation_type":"same_field","shared_zone":"İki dal da yaşamı sürdürme alanıyla ilgilidir ve aynı genel yaşama çerçevesinde buluşur."},{"boundary_match":"partial","distinction":"Odak dalındaki iyi durum doğrudan yaşayışın niteliğidir ve karşıt kötü ya da sıkıntılı yaşayışı da içerir; komşu dal daha genel bir durum iyiliği ve iç rahatlığı alanındadır.","focus_only":"Yaşamın kendisini ve olumlu ya da olumsuz yaşayış durumlarını birlikte kapsar.","gloss":"iyi yaşayış ile genel esenlik","neighbor_only":"Genel durumun düzelmesini, gönül rahatlığını ve umut alanının genişlemesini kapsar.","neighbor_ref":"root_000165/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişinin durumunun iyi ve rahat oluşunu anlatan bağlamlarda yaklaşır."},{"boundary_match":"partial","distinction":"Odak dalı yaşam ve yaşayış merkezlidir; komşu dal ise kişinin bulunduğu durumun veya kalış biçiminin görünümünü merkeze alır.","focus_only":"Canlı yaşamın kendisini ve yaşayışın değer veya güçlük bakımından niteliğini kapsar.","gloss":"yaşayış durumu ile bulunulan durum","neighbor_only":"Bulunulan yerin ya da kalış durumunun iyi veya kötü görünümünü anlatır.","neighbor_ref":"root_000161/B006","relation_type":"near_neighbor","shared_zone":"İyi veya kötü bir durumda bulunmayı anlatan niteleme bağlamlarında anlam yakınlığı oluşur."}],"source_phrase_ar":"العيش الحياة (maqayis;ayn;sihah); العيش الحياة المختصة بالحيوان (mufradat); عيشة صالحة وراضية وصدق وسوء وضنك (maqayis;sihah;tahdhib;mufradat); رجل عائش حاله حسنة (maqayis;tahdhib)","source_summary":"Kaynakların ortak anlatımı yaşamın kendisini merkeze alır ve yaşayışın iyi, hoşnut edici, övgüye değer, kötü ya da sıkıntılı olabilen durumlarını buna bağlar. İyi durumda yaşayan kişiye yönelik niteleme de aynı anlam alanının bağımlı bir kullanımıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل أصل الحياة والعيش، وحال العيشة في الصلاح والرضا والضيق والسوء، وما يقال في حسن حال العائش.","what_is_not_ar":"لا يدخل ما يعاش به من مطعم ومشرب وسبب وموضع."},"support_links":["sup_776c22c644f22e8b05b7","sup_78a391a61e1c1cb0785b"]},{"boundary":"Bu dal yaşamın kendisini veya yaşayışın iyi ve kötü niteliğini değil, yaşamı sağlayan araçları, ortamı ve geçinme uğraşını kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001067/B002","candidate_links":[{"candidate_id":"cand_a916d9d07302a8482a04","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عِيشَة","morph_features":"STEM|POS:N|LEM:Eiy$ap|ROOT:Ey$|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"101:7:3:1","qac_word_ref":"101:7:3","surface_ar":"عِيشَةٍ"}],"gloss":"geçim araçları, ortamı ve geçinme uğraşı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, insanın yaşamını sürdürmesini sağlayan yiyecek, içecek, kaynak ve öteki geçim araçlarıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yaşamın sürdürüldüğü veya geçim araçlarının arandığı yer de aynı alanın kapsamına girer."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Geçim araçlarının arandığı gündüz gibi bir zaman dilimi, geçim etkinliğinin ortamı olarak anlatılabilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Geçim yollarını elde etmek için çaba gösterme ve yaşamı sürdürecek kadar olanağa sahip olma da bu alana bağlı kullanımlardır."}}],"root_ar":"ع ي ش","root_id":"root_001067","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaşamı sağlayan araçları, bunların edinildiği yer ve zamanı, ayrıca geçinmek için gösterilen çabayı birlikte temsil eder.","boundary_detail":"Bu dal yaşamın kendisini veya yaşayışın iyi ve kötü niteliğini değil, yaşamı sağlayan araçları, ortamı ve geçinme uğraşını kapsar.","branch_image_ar":"المعيشة والمعاش","concept_gloss":"geçim araçları, ortamı ve geçinme uğraşı","contextual_glosses":[{"applicability":"Yiyecek, içecek, kazanç veya başka bir olanağın yaşamı sürdürmeyi sağladığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaşamı mümkün kılan araç veya kaynak olma işlevini korur."},"facet_ids":["F001"],"text":"geçim kaynağı","usage_role":"general"},{"applicability":"Bir yerin insanların geçim araçlarını bulduğu veya yaşamını sürdürdüğü ortam olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yerin geçim sağlama ortamı oluşunu açık biçimde korur."},"facet_ids":["F002"],"text":"geçim sağlanan yer","usage_role":"contextual"},{"applicability":"Gündüz gibi bir zaman diliminin geçim için çalışma ve arama dönemi sayıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Zaman diliminin geçim etkinliğine ayrılan ortam olmasını korur."},"facet_ids":["F003"],"text":"geçim arama zamanı","usage_role":"contextual"},{"applicability":"Geçim yollarını sağlamak için çabalamayı veya yaşamı sürdürecek kadar olanağa sahip bulunmayı açıklayan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hem geçim araçlarını edinme çabasını hem de yeterli olanağa sahip olma durumunu korur."},"facet_ids":["F004"],"text":"geçinme çabası ve yeterliği","usage_role":"explanatory"}],"definition":"Yaşamı sürdürmeyi sağlayan yiyecek, içecek, kaynak ve öteki geçim araçlarını, ayrıca bunların edinildiği yer ya da zamanı kapsar. Geçim yollarını sağlama çabasını ve yaşamı sürdürecek kadar olanağa sahip olmayı da anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, insanın yaşamını sürdürmesini sağlayan yiyecek, içecek, kaynak ve öteki geçim araçlarıdır."},{"facet_id":"F002","role":"extension","statement":"Yaşamın sürdürüldüğü veya geçim araçlarının arandığı yer de aynı alanın kapsamına girer."},{"facet_id":"F003","role":"extension","statement":"Geçim araçlarının arandığı gündüz gibi bir zaman dilimi, geçim etkinliğinin ortamı olarak anlatılabilir."},{"facet_id":"F004","role":"associated_use","statement":"Geçim yollarını elde etmek için çaba gösterme ve yaşamı sürdürecek kadar olanağa sahip olma da bu alana bağlı kullanımlardır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Araçlar yerine canlı olma ve yaşama durumunu anlamın merkezine getirir.","collision":"Kökün yaşamın kendisi ve yaşayış durumuyla ilgili birinci dalıyla karışır.","fit":"displacement","loses":"Yiyecek, içecek, kaynak, yer ve geçinme çabası gibi dalın kurucu unsurlarını karşılamaz.","preserves":"Geçim araçlarının hizmet ettiği genel yaşama alanını çağrıştırır."},"text":"yaşam"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yiyecek, içecek, yaşanılan yer, geçim zamanı ve geçinme çabasını kapsamaz.","preserves":"Geçimi sağlayabilecek bir kaynak olma yönünü korur."},"text":"gelir"}],"identity_rationale":"Kaynak ifadesi bu dalı, insanın yaşamını sürdürmesini sağlayan yiyecek, içecek ve öteki kaynaklar; yaşanılan ya da geçimin arandığı yer ve zaman; geçim yollarını sağlama çabası ve yaşamı sürdürecek kadar olanağa sahip olma çevresinde kurar. Bu unsurlar yaşamın kendisi değil, onu mümkün kılan dayanaklardır.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yaşamı sağlayan yiyecek ve içecek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"geçim kaynağı"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"geçim kaynakları"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"geçim aracı veya geçinilen yer"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"gündüz, geçim arama zamanı"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yeryüzü, geçim sağlanan yer"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"geçim"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"geçinme yollarını sağlamak için çabalama"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"geçinebilecek kadar olanağa sahip olma"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"geçim"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"o topluluğun geçimliği süttür"}],"lexicalization_note":"Araç ve kaynak anlamları çeşitli yalın biçimlerde görülür; belirli yer, zaman, yiyecek veya içeceğe bağlanan okumalar ise kendi söz öbeklerinin sınırında tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yaşamın kendisi, asgari yeterlik, bedeni yaşatan besin ve genel dayanakla kurulan dört karşılaştırma dalın kapsamını en iyi sınırlar. Su kaynakları, bakmakla yükümlü olunan kişiler ve gereksinim gibi öteki adaylar yalnızca aynı yaşam sürdürme senaryosuna katıldığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dalının merkezinde yaşamı mümkün kılan kaynaklar, ortam ve çaba vardır; komşu dalın merkezinde ise yaşayanın yaşamı ve bu yaşamın niteliği bulunur.","focus_only":"Yaşamı sağlayan araçları, bunların bulunduğu yeri ve zamanı, ayrıca geçinme uğraşını belirtir.","gloss":"geçim araçları ile yaşam","neighbor_only":"Yaşamın kendisini ve yaşayışın iyi, kötü, hoşnut edici ya da sıkıntılı oluşunu belirtir.","neighbor_ref":"root_001067/B001","relation_type":"same_field","shared_zone":"İki dal da yaşamı sürdürme alanıyla ilgilidir ve aynı genel yaşama çerçevesinde buluşur."},{"boundary_match":"partial","distinction":"Odak dalı geçim araçlarının türünü, ortamını ve edinilmesini genişçe kapsar; komşu dal ise bunların ancak yetme ve yaşamı sürdürme eşiğini öne çıkarır.","focus_only":"Az ya da çok her türlü geçim aracını, geçinilen yeri ve geçim için gösterilen çabayı kapsar.","gloss":"geçim araçları ile asgari yeterlik","neighbor_only":"Yaşamı ancak sürdürmeye yetecek ölçüdeki az ve yeterli payı merkeze alır.","neighbor_ref":"root_000151/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişinin yaşamını sürdürmesini sağlayan yeterli geçim olanağında buluşur."},{"boundary_match":"partial","distinction":"Odak dalı besinden daha geniş bir geçim araçları ve ortamları alanıdır; komşu dal bedeni canlı tutan yiyecek ve bunun sağlanmasıyla sınırlıdır.","focus_only":"Yiyecek ve içeceğin yanında başka kaynakları, geçinilen yeri, zamanı ve geçinme çabasını kapsar.","gloss":"geçim kaynakları ile yaşatıcı besin","neighbor_only":"Bedeni ayakta tutan besini ve bir kişinin kendisiyle bakmakla yükümlü olduklarına sağladığı yiyeceği merkeze alır.","neighbor_ref":"root_001268/B001","relation_type":"near_neighbor","shared_zone":"Yiyeceğin yaşamı sürdürmeye yarayan temel bir geçim aracı olduğu alanda örtüşürler."},{"boundary_match":"partial","distinction":"Odak dalı yaşam ve geçim alanına bağlıdır; komşu dal ise aynı ayakta tutma düşüncesini işler, düzenler ve başka varlıklar için genel bir dayanak anlamına genişletir.","focus_only":"Somut geçim araçlarını, geçinilen ortamı ve bu araçları edinme uğraşını kapsar.","gloss":"geçim aracı ile ayakta tutan dayanak","neighbor_only":"Bir şeyin ayakta durmasını sağlayan dayanak, düzen ve ana unsur anlamlarını yaşam alanının dışına da taşır.","neighbor_ref":"root_001273/B009","relation_type":"near_neighbor","shared_zone":"Yaşamın sürmesini sağlayan temel dayanak veya geçim aracı anlamında belirgin bir örtüşme vardır."}],"source_phrase_ar":"المعيشة ما يعاش به (maqayis;ayn;tahdhib); المطعم والمشرب وما يكون به الحياة (maqayis;ayn;tahdhib); كل شيء يعاش به أو فيه فهو معاش (maqayis;ayn); كل شيء يعاش به فهو معاش (tahdhib); ما يتعيش منه (mufradat); التعيش تكلف أسباب المعيشة (sihah); يتعيشون إذا كانت لهم بلغة من عيش (maqayis;tahdhib)","source_summary":"Kaynakların ortak anlatımı, yaşamı sağlayan yiyecek ve içecekten daha geniş biçimde her türlü geçim aracını kapsar; yaşamın sürdürüldüğü veya geçimin arandığı yer de bu kapsama katılır. Geçim yollarını sağlamak için çabalama ve yaşamı sürdürecek ölçüde olanağa sahip bulunma, bu araç merkezli anlamın bağlı kullanımlarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل المعيشة والمعاش والمعايش وما يقوم به العيش من مطعم ومشرب وسبب وموضع، وما يقال في التعيش والبلغة من العيش.","what_is_not_ar":"لا يدخل نفس الحياة ولا وصف العيشة بأنها راضية أو ضنك."},"support_links":["sup_acd01348899473b536a2"]}],"candidate_inventory":[{"anchor_refs":["101:7:1"],"branch_refs":[],"candidate_id":"cand_03570dba8db654bfaf67","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:7:1:bound-launch","source_type":"word_analysis","support_ids":["sup_4678c86cb5abc6d643a8","sup_f7101d7d56cbf1fe2874"],"title":"bound form joins result and person","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:1","qac_refs":["101:7:1:1"],"status":"accepted"}},{"anchor_refs":["101:7:1"],"branch_refs":[],"candidate_id":"cand_5c128d80edfd4cefb3f8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:7:1:boundary-hinge","source_type":"word_analysis","support_ids":["sup_4678c86cb5abc6d643a8","sup_b8d4dc9fcdb478eadfb2"],"title":"ayah break remains syntactically open","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:1","qac_refs":["101:7:1:1"],"status":"accepted"}},{"anchor_refs":["101:7:1"],"branch_refs":[],"candidate_id":"cand_298a409db5525089b0d2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:7:1:conditional-result","source_type":"word_analysis","support_ids":["sup_4678c86cb5abc6d643a8","sup_bd8a7ddc370bbcf7338a"],"title":"result particle completes the condition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:1","qac_refs":["101:7:1:1"],"status":"accepted"}},{"anchor_refs":["101:7:1"],"branch_refs":[],"candidate_id":"cand_23ca7d89dfa9aa66b946","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:7:1:paired-outcomes","source_type":"word_analysis","support_ids":["sup_4678c86cb5abc6d643a8","sup_c02fb4007bc1532444a9"],"title":"same result frame has an opposite","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:1","qac_refs":["101:7:1:1"],"status":"accepted"}},{"anchor_refs":["101:7:2"],"branch_refs":[],"candidate_id":"cand_e5b00e38446ae151359e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:7:2:explicit-topic","source_type":"word_analysis","support_ids":["sup_ef14af108ef1f232652c","sup_f62f7220266089d7b8ec"],"title":"independent subject foregrounds the person","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:2","qac_refs":["101:7:1:2"],"status":"accepted"}},{"anchor_refs":["101:7:2"],"branch_refs":[],"candidate_id":"cand_e876ea26be84aefebf76","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:7:2:nominal-settled-state","source_type":"word_analysis","support_ids":["sup_40f6d633d9de071a8574","sup_f62f7220266089d7b8ec"],"title":"verbless clause makes a settled state","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:2","qac_refs":["101:7:1:2"],"status":"accepted"}},{"anchor_refs":["101:7:2"],"branch_refs":[],"candidate_id":"cand_239385ef2a1750bbf6e5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:7:2:resumptive-referent","source_type":"word_analysis","support_ids":["sup_f62f7220266089d7b8ec","sup_f6da964706c5a741a81c"],"title":"pronoun resumes the evaluated person","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:2","qac_refs":["101:7:1:2"],"status":"accepted"}},{"anchor_refs":["101:7:3"],"branch_refs":[],"candidate_id":"cand_d11ea4bb9830b9ebe297","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:7:3:containment-not-possession","source_type":"word_analysis","support_ids":["sup_7ad8a3e795d1bef89a16","sup_7c063bc7835cda45f41b"],"title":"preposition makes reward enclosing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:3","qac_refs":["101:7:2:1"],"status":"accepted"}},{"anchor_refs":["101:7:3"],"branch_refs":[],"candidate_id":"cand_8fa79e31caa6be0357d6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:7:3:measurement-to-life","source_type":"word_analysis","support_ids":["sup_7c063bc7835cda45f41b","sup_c62c8d51edb4eeb905e9"],"title":"weighing gives way to immersion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:3","qac_refs":["101:7:2:1"],"status":"accepted"}},{"anchor_refs":["101:7:3"],"branch_refs":[],"candidate_id":"cand_caff6f848e8c5ed347ad","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:7:3:spatial-state","source_type":"word_analysis","support_ids":["sup_68c5f35dd7446d0b99c6","sup_7c063bc7835cda45f41b"],"title":"spatial and state senses work together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:3","qac_refs":["101:7:2:1"],"status":"accepted"}},{"anchor_refs":["101:7:4"],"branch_refs":[],"candidate_id":"cand_99710a2adfda88ab2d93","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001067"],"scope":"focus_ayah","source_local_id":"101:7:4:adjective-binding","source_type":"word_analysis","support_ids":["sup_17e7148fb9b557d2ecf4","sup_abbe5a7700b3c7225a9f"],"title":"agreement binds satisfaction to life","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:4","qac_refs":["101:7:3:1"],"status":"accepted"}},{"anchor_refs":["101:7:4"],"branch_refs":[],"candidate_id":"cand_4abe36d18dea2f535f8d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001067"],"scope":"focus_ayah","source_local_id":"101:7:4:indefinite-specificity","source_type":"word_analysis","support_ids":["sup_17e7148fb9b557d2ecf4","sup_40eba29cd8c4044c50a0"],"title":"specific mode remains undelimited","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:4","qac_refs":["101:7:3:1"],"status":"accepted"}},{"anchor_refs":["101:7:4"],"branch_refs":[],"candidate_id":"cand_74c8a32e2a6d1ac8dca1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001067"],"scope":"focus_ayah","source_local_id":"101:7:4:lived-mode-not-bare-life","source_type":"word_analysis","support_ids":["sup_17e7148fb9b557d2ecf4","sup_bcd1b92b6e909359e6ef"],"title":"living becomes a textured mode","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:4","qac_refs":["101:7:3:1"],"status":"accepted"}},{"anchor_refs":["101:7:4"],"branch_refs":[],"candidate_id":"cand_bdf72cfa5daab969bedc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001067"],"scope":"focus_ayah","source_local_id":"101:7:4:person-to-state-progressions","source_type":"word_analysis","support_ids":["sup_17e7148fb9b557d2ecf4","sup_4eaa5447da81664267ad"],"title":"measured person enters quality of life","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:4","qac_refs":["101:7:3:1"],"status":"accepted"}},{"anchor_refs":["101:7:4"],"branch_refs":[],"candidate_id":"cand_b3d5544a53f39f2707de","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001067"],"scope":"focus_ayah","source_local_id":"101:7:4:predicate-domain","source_type":"word_analysis","support_ids":["sup_17e7148fb9b557d2ecf4","sup_c9907ad130885affb709"],"title":"life noun is the predicate domain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:4","qac_refs":["101:7:3:1"],"status":"accepted"}},{"anchor_refs":["101:7:4"],"branch_refs":[],"candidate_id":"cand_4c55db70309ef01e809f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001067"],"scope":"focus_ayah","source_local_id":"101:7:4:rare-reward-formula","source_type":"word_analysis","support_ids":["sup_1385a494a6b70186b5fb","sup_17e7148fb9b557d2ecf4"],"title":"rare phrase recurs at another reward scene","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:4","qac_refs":["101:7:3:1"],"status":"accepted"}},{"anchor_refs":["101:7:4"],"branch_refs":[],"candidate_id":"cand_aeb2fc1666cd145608bc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001067"],"scope":"focus_ayah","source_local_id":"101:7:4:reward-punishment-contrast","source_type":"word_analysis","support_ids":["sup_17e7148fb9b557d2ecf4","sup_c5bf1fb6621e2dcef233"],"title":"life-state contrasts the later opposite","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:4","qac_refs":["101:7:3:1"],"status":"accepted"}},{"anchor_refs":["101:7:5"],"branch_refs":[],"candidate_id":"cand_b89a8b639cc641e1a4ea","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:7:5:active-passive-contrast","source_type":"word_analysis","support_ids":["sup_096966a48c195ef7ae37","sup_3c10f09bce2846208f07"],"title":"active form contrasts passive approval","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:5","qac_refs":["101:7:4:1"],"status":"accepted"}},{"anchor_refs":["101:7:5"],"branch_refs":[],"candidate_id":"cand_3e79bd7a64447eba67ff","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:7:5:active-self-satisfied-life","source_type":"word_analysis","support_ids":["sup_3c10f09bce2846208f07","sup_8c15b792e15a525aa8e5"],"title":"active participle makes life satisfied","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:5","qac_refs":["101:7:4:1"],"status":"accepted"}},{"anchor_refs":["101:7:5"],"branch_refs":[],"candidate_id":"cand_23f421ae224703920204","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:7:5:agreement-bearer","source_type":"word_analysis","support_ids":["sup_3c10f09bce2846208f07","sup_7153e1c545c706436345"],"title":"concord assigns the quality to life","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:5","qac_refs":["101:7:4:1"],"status":"accepted"}},{"anchor_refs":["101:7:5"],"branch_refs":[],"candidate_id":"cand_696f0278a43a6117cc81","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:7:5:contentment-not-flat-pleasantness","source_type":"word_analysis","support_ids":["sup_3c10f09bce2846208f07","sup_8dbcce2e6d63d88054c1"],"title":"root supplies inward contentment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:5","qac_refs":["101:7:4:1"],"status":"accepted"}},{"anchor_refs":["101:7:5"],"branch_refs":[],"candidate_id":"cand_aac3719c79f887920dd8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:7:5:marked-reward-collocation","source_type":"word_analysis","support_ids":["sup_3c10f09bce2846208f07","sup_47e992d81f1bcd61bff4"],"title":"contentment joins the rare reward pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:5","qac_refs":["101:7:4:1"],"status":"accepted"}},{"anchor_refs":["101:7:5"],"branch_refs":[],"candidate_id":"cand_3ad8f4d7c9bc3049b88f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:7:5:participial-state","source_type":"word_analysis","support_ids":["sup_3c10f09bce2846208f07","sup_766d91f23cbc56c79b63"],"title":"participle carries enduring verbal force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:5","qac_refs":["101:7:4:1"],"status":"accepted"}},{"anchor_refs":["101:7:5"],"branch_refs":[],"candidate_id":"cand_a3213055d3214665bffd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:7:5:sound-and-boundary","source_type":"word_analysis","support_ids":["sup_3c10f09bce2846208f07","sup_e520a7575544260ed3d8"],"title":"sound binds and lands the outcome","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:7:5","qac_refs":["101:7:4:1"],"status":"accepted"}},{"anchor_refs":["101:7:3"],"branch_refs":[],"candidate_id":"cand_cff42c284222ab478a61","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001067"],"scope":"focus_ayah","source_local_id":"101:7:3:1","source_type":"qac_morpheme","support_ids":["sup_645554aa20e4fd4efc92"],"title":"QAC root occurrence: ع ي ش","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["101:7:4"],"branch_refs":[],"candidate_id":"cand_478c48dc806f1674042f","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000569","root_000570"],"scope":"focus_ayah","source_local_id":"101:7:4:1","source_type":"qac_morpheme","support_ids":["sup_0776fd0ff84c95b05d6c"],"title":"QAC root occurrence: ر ض و","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["101:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:7","branch_refs":["root_000569/B001","root_001067/B001"],"candidate_id":"cand_6ec3133d5c1643263ef3","commentary_obligation":"review","hft_ref":"hft_b7c0bd082b3b1cea6813","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_lived_contentment","source_type":"hft","support_ids":["sup_776c22c644f22e8b05b7"],"title":"baseline_lived_contentment","trust":"legacy_unbound"},{"anchor_refs":["101:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:7","branch_refs":["root_000570/B001","root_001067/B002"],"candidate_id":"cand_a916d9d07302a8482a04","commentary_obligation":"review","hft_ref":"hft_0d0654c36f7e0a501698","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_sustaining_livelihood","source_type":"hft","support_ids":["sup_acd01348899473b536a2"],"title":"baseline_sustaining_livelihood","trust":"legacy_unbound"},{"anchor_refs":["101:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:7","branch_refs":["root_000569/B003","root_001067/B001"],"candidate_id":"cand_3faf863ac4dded8d2638","commentary_obligation":"review","hft_ref":"hft_e8d29398ccf057a97dfa","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_reciprocal_fit","source_type":"hft","support_ids":["sup_78a391a61e1c1cb0785b"],"title":"baseline_reciprocal_fit","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:RSLT+","morpheme_role":"PREFIX","pos":"RSLT","qac_ref":"101:7:1:1","qac_word_ref":"101:7:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|3MS","morpheme_role":"STEM","pos":"PRON","qac_ref":"101:7:1:2","qac_word_ref":"101:7:1","root_ar":"","surface_ar":"هُوَ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"101:7:2:1","qac_word_ref":"101:7:2","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"عِيشَة","morph_features":"STEM|POS:N|LEM:Eiy$ap|ROOT:Ey$|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"101:7:3:1","qac_word_ref":"101:7:3","root_ar":"ع ي ش","surface_ar":"عِيشَةٍ"},{"lemma_ar":"رَاضِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:raADiyap|ROOT:rDw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:7:4:1","qac_word_ref":"101:7:4","root_ar":"ر ض و","surface_ar":"رَّاضِيَةٍ"}],"word_analysis_qac_refs":[["101:7:1:1"],["101:7:1:2"],["101:7:2:1"],["101:7:3:1"],["101:7:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["101:7:1","101:7:2","101:7:3","101:7:4","101:7:5"]},"focus_surface_evidence":{"arabic_uthmani":"فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:RSLT+","morpheme_role":"PREFIX","pos":"RSLT","qac_ref":"101:7:1:1","qac_word_ref":"101:7:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|3MS","morpheme_role":"STEM","pos":"PRON","qac_ref":"101:7:1:2","qac_word_ref":"101:7:1","root_ar":"","surface_ar":"هُوَ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"101:7:2:1","qac_word_ref":"101:7:2","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"عِيشَة","morph_features":"STEM|POS:N|LEM:Eiy$ap|ROOT:Ey$|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"101:7:3:1","qac_word_ref":"101:7:3","root_ar":"ع ي ش","surface_ar":"عِيشَةٍ"},{"lemma_ar":"رَاضِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:raADiyap|ROOT:rDw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"101:7:4:1","qac_word_ref":"101:7:4","root_ar":"ر ض و","surface_ar":"رَّاضِيَةٍ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["101:7:1:1"],["101:7:1:2"],["101:7:2:1"],["101:7:3:1"],["101:7:4:1"]],"word_analysis_refs":["101:7:1","101:7:2","101:7:3","101:7:4","101:7:5"],"word_rows":[{"analysis_record_ref":"101:7:1","analytic_gloss_range_en":"result particle introducing the consequence of the preceding conditional frame; not simple coordination","analytic_root_gloss_range_en":null,"qac_refs":["101:7:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"فَ","transliteration":"fa-"}},{"analysis_record_ref":"101:7:2","analytic_gloss_range_en":"independent third-person masculine singular pronoun resuming the one whose scales are heavy; explicit subject of a nominal result clause","analytic_root_gloss_range_en":null,"qac_refs":["101:7:1:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"هُوَ","transliteration":"huwa"}},{"analysis_record_ref":"101:7:3","analytic_gloss_range_en":"preposition of containment and state, governing the life noun and making reward an enclosing condition rather than an owned object","analytic_root_gloss_range_en":null,"qac_refs":["101:7:2:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"فِى","transliteration":"fī"}},{"analysis_record_ref":"101:7:4","analytic_gloss_range_en":"a particular mode or quality of lived existence, locally the genitive complement of {{ar:فِى}} ({{tr:fī}}) and qualified by {{ar:رَّاضِيَةٍۢ}} ({{tr:rāḍiyatin}})","analytic_root_gloss_range_en":"life and lived condition, with a related livelihood and means-of-living range; the local form selects lived condition while allowing provision-quality pressure","qac_refs":["101:7:3:1"],"root":{"arabic":"ع ي ش","transliteration":"'-y-sh"},"surface":{"arabic":"عِيشَةٍۢ","transliteration":"'īshatin"}},{"analysis_record_ref":"101:7:5","analytic_gloss_range_en":"active participial qualifier agreeing with the life noun; locally active satisfaction/contentment borne by the life-state, not passive approval by another","analytic_root_gloss_range_en":"satisfaction, acceptance, approval, and contentment as opposed to displeasure; locally the active participle selects the life-state as satisfied bearer","qac_refs":["101:7:4:1"],"root":{"arabic":"ر ض ي","transliteration":"r-ḍ-y"},"surface":{"arabic":"رَّاضِيَةٍۢ","transliteration":"rāḍiyatin"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["101:7"],"branch_refs":["root_000569/B001","root_001067/B001"],"candidate_id":"cand_6ec3133d5c1643263ef3","evidence_scope":"focus_ayah","hft_ref":"hft_b7c0bd082b3b1cea6813","item_id":"baseline_lived_contentment","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_lived_contentment","support_id":"sup_776c22c644f22e8b05b7"},{"anchor_refs":["101:7"],"branch_refs":["root_000570/B001","root_001067/B002"],"candidate_id":"cand_a916d9d07302a8482a04","evidence_scope":"focus_ayah","hft_ref":"hft_0d0654c36f7e0a501698","item_id":"baseline_sustaining_livelihood","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_sustaining_livelihood","support_id":"sup_acd01348899473b536a2"},{"anchor_refs":["101:7"],"branch_refs":["root_000569/B003","root_001067/B001"],"candidate_id":"cand_3faf863ac4dded8d2638","evidence_scope":"focus_ayah","hft_ref":"hft_e8d29398ccf057a97dfa","item_id":"baseline_reciprocal_fit","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_reciprocal_fit","support_id":"sup_78a391a61e1c1cb0785b"}],"diagnostics":[],"lane_counts":{"global":8,"macro":12,"micro":3},"packet_summary":{"ayah_count":11,"focus_ref":"101:7","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]}],"window":["101:1","101:2","101:3","101:4","101:5","101:6","101:7","101:8","101:9","101:10","101:11"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"101:7","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"101:7","lane":"micro","linguistic_source_ref":"101:7","surface_ref":"101:7","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"101:7","target_tokens":[["o",["101:7:1"]],["hoşnut",["101:7:4"]],["edici",["101:7:4"]],["bir",["101:7:3"]],["yaşam",["101:7:3"]],["içinde",["101:7:2"]],["olacaktır",["101:7:1"]]],"text":"o, hoşnut edici bir yaşam içinde olacaktır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":11,"id":"s101-p01-001-011","label":"Whole surah","number":1,"refs":["101:1","101:2","101:3","101:4","101:5","101:6","101:7","101:8","101:9","101:10","101:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"101:7:4:1","source_type":"qac_morpheme","support_id":"sup_0776fd0ff84c95b05d6c","text":"{\"lemma_ar\":\"رَاضِيَة\",\"morph_features\":\"STEM|POS:ADJ|ACT|PCPL|LEM:raADiyap|ROOT:rDw|F|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"ADJ\",\"qac_ref\":\"101:7:4:1\",\"qac_word_ref\":\"101:7:4\",\"root_ar\":\"ر ض و\",\"surface_ar\":\"رَّاضِيَةٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:5:active-passive-contrast","source_type":"word_analysis","support_id":"sup_096966a48c195ef7ae37","text":"{\"blocking_evidence\":null,\"headline\":\"active form contrasts passive approval\",\"reader_payoff\":\"The reader notices that 101:7 foregrounds active contentment without explicitly adding the passive approval counterpart seen in 89:28.\",\"reason\":\"The local word is active participle {{ar:رَّاضِيَةٍۢ}} ({{tr:rāḍiyatin}}); the CRITICAL contrast with 89:28 is valid as a form contrast, not as a claim that passive approval is locally stated.\",\"representative_source_ids\":[\"MF-e740c3c2\",\"QI-d4c82df7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:4:rare-reward-formula","source_type":"word_analysis","support_id":"sup_1385a494a6b70186b5fb","text":"{\"blocking_evidence\":null,\"headline\":\"rare phrase recurs at another reward scene\",\"reader_payoff\":\"The reader notices that the same rare life-and-satisfaction formula joins heavy scales here to the right-hand-record scene in 69:21.\",\"reason\":\"The contextual profile marks {{ar:عِيشَةٍۢ}} ({{tr:'īshatin}}) as low occurrence and its top partner as the {{ar:ر ض ي}} ({{tr:r-ḍ-y}}) active participle, while the CRITICAL rows supply the concrete parallel at 69:21.\",\"representative_source_ids\":[\"QI-646acffa\",\"QI-76430040\",\"QI-d6272c18\",\"QE-5efefb59\",\"QH-9554f87d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:4","source_type":"word_analysis","support_id":"sup_17e7148fb9b557d2ecf4","text":"{\"gloss_range\":\"a particular mode or quality of lived existence, locally the genitive complement of {{ar:فِى}} ({{tr:fī}}) and qualified by {{ar:رَّاضِيَةٍۢ}} ({{tr:rāḍiyatin}})\",\"prose\":\"{{ar:عِيشَةٍۢ}} ({{tr:'īshatin}}) is the life-state into which the evaluated person is placed. Grammatically it is genitive under {{ar:فِى}} ({{tr:fī}}), so it is the domain of the predicate rather than the actor of the whole clause. Its feminine genitive indefiniteness matches the following qualifier, and the shared -atin cadence with tanwīn liaison makes life and satisfaction sound like one state-unit. Lexically it is not bare existence; the {{ar:ع ي ش}} ({{tr:'-y-sh}}) range names lived condition and can carry livelihood or subsistence texture, so the reward feels experiential and provisioned rather than abstract. Its pattern and indefiniteness make that life both specific and open: a particular mode of living, yet not delimited as a named or exhausted object. The exact phrase recurs at 69:21, where the right-hand record leads to the same reward formula, while 101:7 specializes the formula through heavy scales. In the same surah, the later opposite at 101:9 makes this life-state the reward-side abode image against a falling-abode outcome.\",\"root_display\":\"{{ar:ع ي ش}} ({{tr:'-y-sh}})\",\"root_gloss_range\":\"life and lived condition, with a related livelihood and means-of-living range; the local form selects lived condition while allowing provision-quality pressure\",\"surface_display\":\"{{ar:عِيشَةٍۢ}} ({{tr:'īshatin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:5","source_type":"word_analysis","support_id":"sup_3c10f09bce2846208f07","text":"{\"gloss_range\":\"active participial qualifier agreeing with the life noun; locally active satisfaction/contentment borne by the life-state, not passive approval by another\",\"prose\":\"{{ar:رَّاضِيَةٍۢ}} ({{tr:rāḍiyatin}}) seals the ayah by making satisfaction the final quality of the reward scene. Its feminine genitive indefinite agreement ties it to {{ar:عِيشَةٍۢ}} ({{tr:'īshatin}}), not to the masculine pronoun, so the life-state itself is the bearer of contentment. The active participle is crucial: it presents the life as satisfied from within, not as something merely approved by an outside evaluator. That active/passive distinction is made explicit by the paired forms in 89:28, while 101:7 selects only the active side. The word also participates in the exact reward phrase repeated at 69:21, so the final adjective is both a local grammatical closure and a recognizable reward marker. The liaison from the preceding tanwīn fuses the qualifier into the life phrase, and the emphatic ḍ gives the final satisfaction a dense center; together, sound and position let the moral heaviness of 101:6 settle into contentment at the ayah's last word.\",\"root_display\":\"{{ar:ر ض ي}} ({{tr:r-ḍ-y}})\",\"root_gloss_range\":\"satisfaction, acceptance, approval, and contentment as opposed to displeasure; locally the active participle selects the life-state as satisfied bearer\",\"surface_display\":\"{{ar:رَّاضِيَةٍۢ}} ({{tr:rāḍiyatin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:4:indefinite-specificity","source_type":"word_analysis","support_id":"sup_40eba29cd8c4044c50a0","text":"{\"blocking_evidence\":null,\"headline\":\"specific mode remains undelimited\",\"reader_payoff\":\"The reader notices that the wording names a particular life-mode while leaving its fullness open-ended.\",\"reason\":\"QAC identifies the word as an indefinite feminine singular gerund on a pattern of specific mode or instance, so the bounded-form and open-indefinite payoffs both survive.\",\"representative_source_ids\":[\"QF-01650863\",\"MI-4711ae65\",\"QY-ca876571\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:2:nominal-settled-state","source_type":"word_analysis","support_id":"sup_40f6d633d9de071a8574","text":"{\"blocking_evidence\":null,\"headline\":\"verbless clause makes a settled state\",\"reader_payoff\":\"The reader notices that the outcome is presented as a standing condition, not as another event after the weighing.\",\"reason\":\"The attachment layer marks {{ar:فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ}} ({{tr:fa-huwa fī 'īshatin rāḍiyatin}}) as a nominal result clause with a prepositional predicate.\",\"representative_source_ids\":[\"QT-8e6659cd\",\"QB-55fcc698\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:1","source_type":"word_analysis","support_id":"sup_4678c86cb5abc6d643a8","text":"{\"gloss_range\":\"result particle introducing the consequence of the preceding conditional frame; not simple coordination\",\"prose\":\"{{ar:فَ}} ({{tr:fa-}}) opens the ayah as a result, not as loose coordination. It answers the suspended condition from 101:6, so the heavy scales do not merely sit beside reward; they lead into a governed consequence. Because the particle is bound directly to {{ar:هُوَ}} ({{tr:huwa}}) in {{ar:فَهُوَ}} ({{tr:fa-huwa}}), the consequence and the evaluated person enter together as one compressed launch. The ayah break therefore works as a hinge rather than a full syntactic stop. The same result-particle architecture is reversed in the opposite outcome at 101:9, where the counter-result is introduced in the same consequence frame.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa-}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:5:marked-reward-collocation","source_type":"word_analysis","support_id":"sup_47e992d81f1bcd61bff4","text":"{\"blocking_evidence\":null,\"headline\":\"contentment joins the rare reward pair\",\"reader_payoff\":\"The reader notices that the adjective is part of a constrained reward collocation with the life noun and the exact phrase at 69:21.\",\"reason\":\"The contextual profile marks the active participle as low-occurrence and paired with the {{ar:ع ي ش}} ({{tr:'-y-sh}}) gerund, while the CRITICAL rows anchor the exact recurrence at 69:21.\",\"representative_source_ids\":[\"QI-3b60664a\",\"QI-833636e4\",\"QE-5ee556e1\",\"QH-0ed07c9c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:4:person-to-state-progressions","source_type":"word_analysis","support_id":"sup_4eaa5447da81664267ad","text":"{\"blocking_evidence\":null,\"headline\":\"measured person enters quality of life\",\"reader_payoff\":\"The reader notices the transition from quantified evaluation to qualitative existence: measured scales yield a lived condition.\",\"reason\":\"The local order moves from {{ar:هُوَ}} ({{tr:huwa}}) into the prepositional life-state, matching the CRITICAL boundary claim about measurement becoming lived quality.\",\"representative_source_ids\":[\"QT-f9daa4a6\",\"QB-197a3969\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"101:7:3:1","source_type":"qac_morpheme","support_id":"sup_645554aa20e4fd4efc92","text":"{\"lemma_ar\":\"عِيشَة\",\"morph_features\":\"STEM|POS:N|LEM:Eiy$ap|ROOT:Ey$|F|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"101:7:3:1\",\"qac_word_ref\":\"101:7:3\",\"root_ar\":\"ع ي ش\",\"surface_ar\":\"عِيشَةٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:3:spatial-state","source_type":"word_analysis","support_id":"sup_68c5f35dd7446d0b99c6","text":"{\"blocking_evidence\":null,\"headline\":\"spatial and state senses work together\",\"reader_payoff\":\"The reader notices that the wording keeps both the image of being inside and the abstract sense of being in a condition.\",\"reason\":\"The preposition is locally the head of a locative-stative predicate, so spatial containment and existential state are both coherent without forcing a literal-place reading.\",\"representative_source_ids\":[\"QS-acd158ed\",\"QT-e187938f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:5:agreement-bearer","source_type":"word_analysis","support_id":"sup_7153e1c545c706436345","text":"{\"blocking_evidence\":null,\"headline\":\"concord assigns the quality to life\",\"reader_payoff\":\"The reader notices that gender, case, and indefiniteness direct the adjective to the life noun rather than to the person.\",\"reason\":\"The attachment evidence marks the word as an adjective of {{ar:عِيشَةٍۢ}} ({{tr:'īshatin}}), and the agreement features block treating it as a direct modifier of {{ar:هُوَ}} ({{tr:huwa}}).\",\"representative_source_ids\":[\"QG-5b3947e6\",\"QG-6f4c3e86\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:5:participial-state","source_type":"word_analysis","support_id":"sup_766d91f23cbc56c79b63","text":"{\"blocking_evidence\":null,\"headline\":\"participle carries enduring verbal force\",\"reader_payoff\":\"The reader notices that the final word completes the nominal scene as a durable quality rather than adding a new event clause.\",\"reason\":\"The form is an active participle in a nominal predicate phrase, so it can carry verbal force while remaining the final qualifier of the scene.\",\"representative_source_ids\":[\"QG-052da75b\",\"QT-d94c209a\",\"QT-36752232\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:3:containment-not-possession","source_type":"word_analysis","support_id":"sup_7ad8a3e795d1bef89a16","text":"{\"blocking_evidence\":null,\"headline\":\"preposition makes reward enclosing\",\"reader_payoff\":\"The reader notices that the reward is framed as an immersive condition around the person, not as a thing he merely has.\",\"reason\":\"QAC and attachment evidence show {{ar:فِى}} ({{tr:fī}}) governing {{ar:عِيشَةٍۢ}} ({{tr:'īshatin}}) as the predicate phrase, supporting containment rather than possession.\",\"representative_source_ids\":[\"QG-04d51b3b\",\"MG-a0418391\",\"QF-d9f11b45\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:3","source_type":"word_analysis","support_id":"sup_7c063bc7835cda45f41b","text":"{\"gloss_range\":\"preposition of containment and state, governing the life noun and making reward an enclosing condition rather than an owned object\",\"prose\":\"{{ar:فِى}} ({{tr:fī}}) turns the reward into containment. The person is not simply said to possess a life; he is placed within {{ar:عِيشَةٍۢ}} ({{tr:'īshatin}}), so the grammar presents the outcome as an enclosing existential state. That spatial image remains live even while the phrase functions circumstantially as the predicate of {{ar:هُوَ}} ({{tr:huwa}}). The preposition also marks the transition from the weighing frame of 101:6 into lived condition: after measurement, the judged person is surrounded by the result.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فِى}} ({{tr:fī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:5:active-self-satisfied-life","source_type":"word_analysis","support_id":"sup_8c15b792e15a525aa8e5","text":"{\"blocking_evidence\":null,\"headline\":\"active participle makes life satisfied\",\"reader_payoff\":\"The reader notices that the phrase does not merely say the person enjoys life; it casts the surrounding life-state itself as satisfied.\",\"reason\":\"QAC identifies {{ar:رَّاضِيَةٍۢ}} ({{tr:rāḍiyatin}}) as an active participle and the attachment layer binds it to {{ar:عِيشَةٍۢ}} ({{tr:'īshatin}}), so active satisfaction belongs locally to the life-state.\",\"representative_source_ids\":[\"QS-2421d3a1\",\"QS-a7ebb37d\",\"QF-57b106e4\",\"QY-c8fdc826\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:5:contentment-not-flat-pleasantness","source_type":"word_analysis","support_id":"sup_8dbcce2e6d63d88054c1","text":"{\"blocking_evidence\":null,\"headline\":\"root supplies inward contentment\",\"reader_payoff\":\"The reader notices that the adjective carries satisfaction, acceptance, and absence of displeasure rather than a thin pleasant-life label.\",\"reason\":\"V4 branch B001 supports satisfaction and acceptance as the active local range, while unrelated root branches such as overcoming or proper names do not govern this surface.\",\"representative_source_ids\":[\"QS-2ed4125d\",\"QS-8930873b\",\"QS-f4988d30\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:4:adjective-binding","source_type":"word_analysis","support_id":"sup_abbe5a7700b3c7225a9f","text":"{\"blocking_evidence\":null,\"headline\":\"agreement binds satisfaction to life\",\"reader_payoff\":\"The reader notices that the life and its satisfaction are grammatically and audibly bound into one state-unit.\",\"reason\":\"The attachment layer marks {{ar:رَّاضِيَةٍۢ}} ({{tr:rāḍiyatin}}) as the adjective of {{ar:عِيشَةٍۢ}} ({{tr:'īshatin}}), and the shared indefiniteness/genitive cadence supports the phrase-level binding.\",\"representative_source_ids\":[\"QG-b5f3baa4\",\"QP-b60b8e32\",\"QP-3f7ca85d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:1:boundary-hinge","source_type":"word_analysis","support_id":"sup_b8d4dc9fcdb478eadfb2","text":"{\"blocking_evidence\":null,\"headline\":\"ayah break remains syntactically open\",\"reader_payoff\":\"The reader notices that the ayah boundary does not isolate 101:7; it carries the unresolved movement from 101:6 into its answer.\",\"reason\":\"The attachment layer marks the clause as a syntactically forced conditional apodosis, so the connector preserves cross-ayah dependency.\",\"representative_source_ids\":[\"QT-0ff96cb3\",\"QB-aed547ba\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:4:lived-mode-not-bare-life","source_type":"word_analysis","support_id":"sup_bcd1b92b6e909359e6ef","text":"{\"blocking_evidence\":null,\"headline\":\"living becomes a textured mode\",\"reader_payoff\":\"The reader notices that the reward is a textured mode of living with condition and provision pressure, not just the fact of being alive.\",\"reason\":\"V4 keeps the local root within life/lived-condition and livelihood ranges; the local gerund and QAC grammar select a specific lived condition while allowing provision-quality pressure.\",\"representative_source_ids\":[\"QS-07d6dfc3\",\"QS-2566d0bb\",\"QS-a2d1cc1e\",\"QF-0f138a87\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:1:conditional-result","source_type":"word_analysis","support_id":"sup_bd8a7ddc370bbcf7338a","text":"{\"blocking_evidence\":null,\"headline\":\"result particle completes the condition\",\"reader_payoff\":\"The reader notices that reward is grammatically made the consequence of the heavy-scales condition in 101:6, not a detached description.\",\"reason\":\"QAC and attachment evidence identify {{ar:فَ}} ({{tr:fa-}}) as the apodosis/result particle for the preceding conditional branch, so the causal-sequential force survives.\",\"representative_source_ids\":[\"QG-1a7513a5\",\"MG-dd063ec4\",\"QS-82fac2c9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:1:paired-outcomes","source_type":"word_analysis","support_id":"sup_c02fb4007bc1532444a9","text":"{\"blocking_evidence\":null,\"headline\":\"same result frame has an opposite\",\"reader_payoff\":\"The reader notices that the reward result here and the punishment result in 101:9 are framed as paired consequences.\",\"reason\":\"The CRITICAL rows give the concrete same-surah counterpart at 101:9, and no guardrail evidence blocks reading it as a paired result frame.\",\"representative_source_ids\":[\"QE-e2061778\",\"QB-0f5bf296\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:4:reward-punishment-contrast","source_type":"word_analysis","support_id":"sup_c5bf1fb6621e2dcef233","text":"{\"blocking_evidence\":null,\"headline\":\"life-state contrasts the later opposite\",\"reader_payoff\":\"The reader notices that this life-state is the positive counterpart to the opposite outcome introduced later in the surah at 101:9.\",\"reason\":\"The same-surah contrast is anchored by the concrete 101:9 counterpart, so it can shape the local reward-side reading without controlling the grammar.\",\"representative_source_ids\":[\"MI-db08d461\",\"QE-be8b4093\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:3:measurement-to-life","source_type":"word_analysis","support_id":"sup_c62c8d51edb4eeb905e9","text":"{\"blocking_evidence\":null,\"headline\":\"weighing gives way to immersion\",\"reader_payoff\":\"The reader notices the domain shift from tribunal measurement in 101:6 to immersive living in 101:7.\",\"reason\":\"The CRITICAL boundary row is consistent with the syntactic movement from the prior weighing condition into the prepositional reward predicate.\",\"representative_source_ids\":[\"QB-7d397ed9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:4:predicate-domain","source_type":"word_analysis","support_id":"sup_c9907ad130885affb709","text":"{\"blocking_evidence\":null,\"headline\":\"life noun is the predicate domain\",\"reader_payoff\":\"The reader notices that the word supplies the architecture of the reward state in which the person is placed.\",\"reason\":\"QAC and attachment evidence mark {{ar:عِيشَةٍۢ}} ({{tr:'īshatin}}) as the genitive complement governed by {{ar:فِى}} ({{tr:fī}}) within the predicate phrase.\",\"representative_source_ids\":[\"QG-3c2d7908\",\"QG-55f84f37\",\"QG-7c9e377c\",\"QT-1f389def\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:5:sound-and-boundary","source_type":"word_analysis","support_id":"sup_e520a7575544260ed3d8","text":"{\"blocking_evidence\":null,\"headline\":\"sound binds and lands the outcome\",\"reader_payoff\":\"The reader notices that the recited binding and dense consonantal center help the heavy-scales result settle into satisfaction at the final word.\",\"reason\":\"The shadda and liaison claims are locally attached to the phrase boundary after {{ar:عِيشَةٍۢ}} ({{tr:'īshatin}}), and the semantic link back to heavy scales is anchored in 101:6.\",\"representative_source_ids\":[\"QF-de468bcc\",\"QP-b730ff69\",\"QP-2e604ea3\",\"QE-df1aae58\",\"QB-7596949f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:2:explicit-topic","source_type":"word_analysis","support_id":"sup_ef14af108ef1f232652c","text":"{\"blocking_evidence\":null,\"headline\":\"independent subject foregrounds the person\",\"reader_payoff\":\"The reader notices the movement from a person attached to scales in 101:6 to a person explicitly set before the reward state in 101:7.\",\"reason\":\"The pronoun is locally an explicit mubtada; the emphasis claim is kept as foregrounding rather than as a claim that Arabic required an omitted-pronoun alternative.\",\"representative_source_ids\":[\"MG-59e2250f\",\"QF-b77de979\",\"QT-116cb950\",\"QB-4146a683\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:2","source_type":"word_analysis","support_id":"sup_f62f7220266089d7b8ec","text":"{\"gloss_range\":\"independent third-person masculine singular pronoun resuming the one whose scales are heavy; explicit subject of a nominal result clause\",\"prose\":\"{{ar:هُوَ}} ({{tr:huwa}}) resumes the person from 101:6 and makes him the explicit subject of the result clause. The pronoun is definite in form but generic in reach: it points to whoever fits the heavy-scales condition, without naming a particular individual. Its independent shape matters because the prior person was carried in the possessive suffix of the scales phrase in 101:6; now that person stands as the topic of a full predication. With no overt verb, the clause shifts from the weighing event into a settled nominal state. The order places the evaluated person first, then locates him inside the reward condition.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:هُوَ}} ({{tr:huwa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:2:resumptive-referent","source_type":"word_analysis","support_id":"sup_f6da964706c5a741a81c","text":"{\"blocking_evidence\":null,\"headline\":\"pronoun resumes the evaluated person\",\"reader_payoff\":\"The reader notices that the result is attached to the same conditional person from 101:6 while still remaining universally applicable.\",\"reason\":\"QAC identifies {{ar:هُوَ}} ({{tr:huwa}}) as an independent third-person pronoun, and attachment evidence marks it as resuming the conditional-relative subject from 101:6.\",\"representative_source_ids\":[\"QG-626dee20\",\"QG-ab4ad0d9\",\"QS-1b27fb8e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:7:1:bound-launch","source_type":"word_analysis","support_id":"sup_f7101d7d56cbf1fe2874","text":"{\"blocking_evidence\":null,\"headline\":\"bound form joins result and person\",\"reader_payoff\":\"The reader notices that the clause begins relationally: the result marker is fused to the pronoun before the reward state is named.\",\"reason\":\"The local surface is the proclitic sequence {{ar:فَهُوَ}} ({{tr:fa-huwa}}), and the cross-reference evidence ties that launch to the prior condition.\",\"representative_source_ids\":[\"QF-e88a2800\",\"QT-dc9ed3c8\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ","ayah_ref":"101:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000569/B001","root_001067/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001067","role":"Life and lived condition supplies the encompassing state in which the person is placed.","root":"ع ي ش","source_ref":"101:7","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000569","role":"Acceptance opposed to displeasure gives that encompassing life its affective quality.","root":"ر ض و","source_ref":"101:7","source_word_indices":["4"]}],"changed_reading":{"after":"He is enclosed within a lived condition that is itself satisfied and free of aversion.","before":"He will have a pleasant life."},"confidence":"strong","focus_anchor":"The construction fahuwa fi places the person inside ʿishah, while the feminine active descriptor radiyah grammatically makes the lived condition itself the bearer of satisfaction.","mechanism":"Containment and personification combine: the subject does not merely possess a reward but inhabits a whole condition of living from which displeasure is absent.","model_id":"baseline_lived_contentment"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_lived_contentment","source_type":"hft","support_id":"sup_776c22c644f22e8b05b7","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ","ayah_ref":"101:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000570/B001","root_001067/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001067","role":"Livelihood, provision, and place of living turn ʿishah into a sustaining environment.","root":"ع ي ش","source_ref":"101:7","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000570","role":"The non-dominant mapped inventory's acceptance sense marks the sustaining environment as fully acceptable.","root":"ر ض و","source_ref":"101:7","source_word_indices":["4"]}],"changed_reading":{"after":"The verse places him within a satisfactory means-and-place of living whose supports are part of the gift.","before":"The verse promises a generically happy existence."},"confidence":"strong","focus_anchor":"The noun ʿishah can name not only life in the abstract but the means, provisions, and place by which living is sustained.","mechanism":"The phrase can describe an ecology of subsistence: food, drink, place, and support cohere as an acceptable livelihood rather than serving as decorative pleasures around an otherwise unchanged subject.","model_id":"baseline_sustaining_livelihood"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_sustaining_livelihood","source_type":"hft","support_id":"sup_acd01348899473b536a2","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ","ayah_ref":"101:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000569/B003","root_001067/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001067","role":"The lived condition provides one side of a relation rather than merely an inert possession.","root":"ع ي ش","source_ref":"101:7","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_000569","role":"Mutual consent supplies the image of reciprocal accord between the life and its inhabitant.","root":"ر ض و","source_ref":"101:7","source_word_indices":["4"]}],"changed_reading":{"after":"Person and lived condition are in reciprocal fit: he is at home in it, and it is figured as accepting him.","before":"The person likes the life awarded to him."},"confidence":"medium","focus_anchor":"Because radiyah agrees with ʿishah, the wording leaves the life grammatically active rather than stating only that its human inhabitant is pleased.","mechanism":"The mutual-consent branch activates a bilateral relation: the person fits the life and the life, personified, accepts its inhabitant. This coexists with the simpler idiom of a pleasing life.","model_id":"baseline_reciprocal_fit"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_reciprocal_fit","source_type":"hft","support_id":"sup_78a391a61e1c1cb0785b","trust":"legacy_unbound"}]}
</lane_packet_json>
