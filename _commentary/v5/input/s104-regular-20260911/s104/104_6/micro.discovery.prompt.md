# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **104:6**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s104-regular-20260911/s104/104_6/micro.discovery.json` and modify nothing
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
  "ayah_ref": "104:6",
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
{"analysis_context":{"analysis_id":"s104-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"104:6","host_surah":104,"lane_context_refs":[],"ordered_context_refs":["104:0","104:1","104:2","104:3","104:4","104:5","104:7","104:8","104:9","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, tapınma eylemi ile bundan türeyen tapınılan veya tapınılır kılınan varlık anlamlarını kapsar; şaşkınlık, yoğun üzüntü ve salt özel ad kullanımları bu sınırın dışındadır.","branch_kind":"mixed_non_bare","branch_ref":"root_000047/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"104:6:2:1","qac_word_ref":"104:6:2","surface_ar":"ٱللَّهِ"}],"gloss":"tapınma ve tapınılan varlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel eylem, bir varlığa tapınmak ve kişinin kendini bu tapınmaya vermesidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylemden türeyen varlık anlamı, kendisine tapınılan varlığı veya tapınma konusu sayılan nesneyi gösterir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen kullanım, bir varlığı başkalarınca tapınılır duruma getirme veya öyle sunma işlemini bildirir."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Güneşe kimi topluluklarca tapınılması nedeniyle ona tapınılan varlık anlamındaki bir ad verilmesi, varlık anlamının tarihsel bir örneğidir."}}],"root_ar":"ء ل ه","root_id":"root_000047","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Eylem çekirdeğiyle ondan türeyen tapınılan varlık anlamının birlikte temsil edilmesi gereken genel açıklamalarda kullanılır.","boundary_detail":"Dal, tapınma eylemi ile bundan türeyen tapınılan veya tapınılır kılınan varlık anlamlarını kapsar; şaşkınlık, yoğun üzüntü ve salt özel ad kullanımları bu sınırın dışındadır.","branch_image_ar":"التعبد والمعبود","concept_gloss":"tapınma ve tapınılan varlık","contextual_glosses":[{"applicability":"Bir kişinin tapınma eylemini veya kendini tapınmaya vermesini bildiren eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylem olarak tapınma çekirdeğini eksiksiz korur."},"facet_ids":["F001"],"text":"tapınmak","usage_role":"general"},{"applicability":"Bir topluluğun kendisine tapındığı varlık veya nesneden söz edilen ad bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tapınmanın yöneldiği varlık veya nesne anlamını korur."},"facet_ids":["F002"],"text":"tapınılan varlık","usage_role":"contextual"},{"applicability":"Bir varlığın başkalarına tapınma konusu olarak benimsetilmesini anlatan ettirgen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir varlığı tapınma konusu durumuna getirme işlemini korur."},"facet_ids":["F003"],"text":"tapınılır kılmak","usage_role":"explanatory"}],"definition":"Bir varlığa tapınma eylemini ve kişinin kendini tapınmaya vermesini anlatır. Türemiş kullanımlarda bir varlığı tapınılır kılmayı, tapınılan varlığı ve tapınma konusu sayılan varlıkları da adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel eylem, bir varlığa tapınmak ve kişinin kendini bu tapınmaya vermesidir."},{"facet_id":"F002","role":"extension","statement":"Eylemden türeyen varlık anlamı, kendisine tapınılan varlığı veya tapınma konusu sayılan nesneyi gösterir."},{"facet_id":"F003","role":"specialization","statement":"Ettirgen kullanım, bir varlığı başkalarınca tapınılır duruma getirme veya öyle sunma işlemini bildirir."},{"facet_id":"F004","role":"example","statement":"Güneşe kimi topluluklarca tapınılması nedeniyle ona tapınılan varlık anlamındaki bir ad verilmesi, varlık anlamının tarihsel bir örneğidir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Yalnızca belirli bir varlık türünü adlandırdığı için bütün dalın karşılığı sanılabilir.","fit":"narrowing","loses":"Tapınma eylemini, kişinin tapınmaya yönelmesini ve tapınılır kılma işlemini karşılamaz.","preserves":"Tapınılan varlık anlamını kısa ve doğal biçimde korur."},"text":"tanrı"}],"identity_rationale":"Kaynak ifadesi tapınma eylemini, kişinin kendini tapınmaya vermesini, bir varlığı tapınılır kılmayı ve tapınılan varlığı aynı anlam örgüsü içinde açıkça birleştirir. Geçici dal çerçevesi bu çekirdeği ve ondan türeyen varlık adlarını doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tapınmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kendini tapınmaya vermek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"tapınılır kılmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"tapınılan varlık, tanrı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"tapınılan varlık"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"tanrılar, tapınılan nesneler"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"tapınma"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kimi toplulukların tapındığı için bu adla anılan güneş"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"senin tapınman"}],"lexicalization_note":"Tanım, yalın eylem çekirdeğini türemiş eylem ve varlık adlarından ayırır; türemiş biçimlerin kapsamı yalın eylemin tamamına aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Tapınma eylemi, korkuya bağlı özel tapınma yaşayışı ve aynı kökün özel ad dalı sınırı keskinleştirdi; peygamberlik, büyücülük, belirli tapınma nesneleri, sahiplik ve tarihsel hizmet grubu adayları ise yalnızca aynı dinsel alana veya tekil örneklere temas ettiği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal eylem ve yaklaşma yönünde yoğunlaşırken bu dal aynı çekirdekten tapınılan varlık ile ettirgen kılma anlamlarını da türetir; bu yüzden yalnızca eylem bağlamında yakınlaşırlar.","focus_only":"Tapınılan varlığı ve bir varlığı tapınılır kılma işlemini de adlandırır.","gloss":"tapınma ve yaklaşarak yönelme","neighbor_only":"Tapınmayla birlikte yaklaşma ve kendini bu işe verme yönünü öne çıkarır.","neighbor_ref":"root_001498/B001","relation_type":"near_synonym","shared_zone":"İki dal da tapınma eylemini ve kişinin bu eyleme yönelmesini kapsar."},{"boundary_match":"partial","distinction":"Bu dal genel tapınma çekirdeğini ve ondan türeyen varlık anlamlarını kapsar; komşu dal ise korku, inziva ve olağanın üstündeki uygulamalarla sınırlı özel bir yaşayışı anlatır.","focus_only":"Tapınmayı korku, inziva veya aşırı uygulama koşuluna bağlamaz ve tapınılan varlığı da adlandırabilir.","gloss":"korkuyla yoğunlaşan özel tapınma yaşayışı","neighbor_only":"Korkudan doğan, inziva veya ek yüklenme biçimindeki özel bir tapınma yaşayışını bildirir.","neighbor_ref":"root_000604/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da kişinin kendini tapınmaya vermesi bulunur."},{"boundary_match":"partial","distinction":"Bu dal genel anlam örgüsünü verir; komşu dal ise o örgüden türemiş özel adı ve adın belirli söz kalıplarındaki kullanımını ayrı bir biçim alanı olarak sınırlar.","focus_only":"Genel tapınma eylemini, tapınılan varlığı ve tapınılır kılmayı kapsar.","gloss":"Yaratıcıya özgü ad ve kullanım kalıpları","neighbor_only":"Yaratıcıya özgü adı ve bu adla kurulan seslenme, dilek ve ant kalıplarını kapsar.","neighbor_ref":"root_000047/B002","relation_type":"near_neighbor","shared_zone":"Özel ad, tapınılan yüce varlık düşüncesi üzerinden bu dalın varlık anlamıyla bağlantılıdır."}],"source_phrase_ar":"أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)","source_summary":"Kaynakların ortak çizgisi, tapınmayı anlamın temeli sayar; kişinin tapınmaya yönelmesini, tapınılan varlığı ve tapınılır kılma işlemini bu temelden türetir. Tapınma konusu sayılan yontular ve güneş örneği, varlık anlamının belirli uygulamalarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه أله وتأله بمعنى عبد وتنسك، والتأليه بمعنى التعبيد، والإله والآلهة والإلاهة لما جعل معبودا.","what_is_not_ar":"لا يدخل فيه أله بمعنى تحير، ولا ألهت على فلان بمعنى اشتد جزعي عليه، ولا أسماء المواضع أو الحية أو الهلال إلا من جهة التسمية لا معنى العبادة."},"support_links":[]},{"boundary":"Dal, özel ad ile bu ada bağlı seslenme, dilek, şaşma ve ant biçimleriyle sınırlıdır; herhangi bir tapınılan varlığı gösteren genel ad anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000047/B002","candidate_links":[{"candidate_id":"cand_de2ce7935b024670a5dc","lane":"micro"},{"candidate_id":"cand_b34261ce72c71c448c83","lane":"micro"},{"candidate_id":"cand_8ceb94f94ff2133d0248","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"104:6:2:1","qac_word_ref":"104:6:2","surface_ar":"ٱللَّهِ"}],"gloss":"Yaratıcıya özgü ad ile seslenme ve ant biçimleri","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dalın merkezinde, Yaratıcıyı başkalarından ayırarak gösteren ve yalnız ona özgü sayılan özel ad bulunur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Özel adın, tapınılan varlığı bildiren genel addan ses düşmesi ve belirleyici unsur eklenmesiyle oluştuğu açıklanır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özel ad, sözün başında ant değeri taşıyarak ardından gelen yapmama bildirimini güçlendirebilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Özel adın doğrudan ya da seslenme öğesi yerine geçen bir sonla kullanılması, yakarma ve dilek bildiren seslenme biçimleri kurar."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Ses veya parçaların düşürüldüğü kısalmış biçimler, şaşma ve ant anlatan kalıplarda kullanılır."}}],"root_ar":"ء ل ه","root_id":"root_000047","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Özel adın kendisiyle ona bağlı seslenme, dilek ve ant kullanımlarının birlikte açıklanması gereken dal düzeyinde kullanılır.","boundary_detail":"Dal, özel ad ile bu ada bağlı seslenme, dilek, şaşma ve ant biçimleriyle sınırlıdır; herhangi bir tapınılan varlığı gösteren genel ad anlamına genişletilmez.","branch_image_ar":"اسم الله في القسم والنداء","concept_gloss":"Yaratıcıya özgü ad ile seslenme ve ant biçimleri","contextual_glosses":[{"applicability":"Söz konusu adın yalnız Yaratıcıyı gösteren yalın ad olarak ele alındığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Adın Yaratıcıya özgü olmasını ve ayırt edici ad işlevini korur."},"facet_ids":["F001"],"text":"Yaratıcı'nın özel adı","usage_role":"general"},{"applicability":"Yakarış veya dilek sırasında Yaratıcıya doğrudan seslenilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaratıcıya yöneltilen doğrudan seslenme işlevini doğal biçimde korur."},"facet_ids":["F004"],"text":"ey Tanrı","usage_role":"contextual"},{"applicability":"Özel adın bir bildirimin doğruluğunu pekiştiren ant değeri taşıdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaratıcıya dayanarak ant verme işlevini açık biçimde korur."},"facet_ids":["F003"],"text":"Tanrı adına ant olsun","usage_role":"contextual"},{"applicability":"Özel adın ses veya parçaları düşürülmüş tarihsel kalıplarının işlevini açıklarken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kısaltılma biçimini ve şaşma ya da ant işlevini birlikte korur."},"facet_ids":["F005"],"text":"kısaltılmış şaşma veya ant sözü","usage_role":"explanatory"}],"definition":"Yaratıcıya özgü adın kendisini ve bu adla kurulan seslenme, dilek, şaşma ve ant biçimlerini kapsar. Bu biçimler doğrudan seslenme, adın ant değeriyle kullanılması veya ses ve parçaların düşürülmesiyle kısaltılma yollarını gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dalın merkezinde, Yaratıcıyı başkalarından ayırarak gösteren ve yalnız ona özgü sayılan özel ad bulunur."},{"facet_id":"F002","role":"source_variant","statement":"Özel adın, tapınılan varlığı bildiren genel addan ses düşmesi ve belirleyici unsur eklenmesiyle oluştuğu açıklanır."},{"facet_id":"F003","role":"associated_use","statement":"Özel ad, sözün başında ant değeri taşıyarak ardından gelen yapmama bildirimini güçlendirebilir."},{"facet_id":"F004","role":"associated_use","statement":"Özel adın doğrudan ya da seslenme öğesi yerine geçen bir sonla kullanılması, yakarma ve dilek bildiren seslenme biçimleri kurar."},{"facet_id":"F005","role":"source_variant","statement":"Ses veya parçaların düşürüldüğü kısalmış biçimler, şaşma ve ant anlatan kalıplarda kullanılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Genel tür adı olarak başka tapınılan varlıklar için de kullanılabildiğinden özel adla karışır.","fit":"narrowing","loses":"Adın tek bir varlığa özgü özel ad oluşunu ve seslenme ile ant biçimlerini karşılamaz.","preserves":"Yüce bir tapınılan varlığa gönderimde bulunma yönünü korur."},"text":"tanrı"}],"identity_rationale":"Kaynak ifadesi Yaratıcıya özgü adın kendisini, genel tapınılan-varlık adından türetiliş açıklamasını ve bu özel adla kurulan seslenme ile ant biçimlerini birlikte verir. Geçici çerçeve kullanılabilir, ancak dal yalnızca seslenme ve ant kalıpları değildir; özel adın yalın kullanımı da çekirdekte tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"Yaratıcıya özgü ad"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"Tanrı adına ant olsun, bunu yapmadım"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ey Tanrı; yakarma seslenişi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ey Tanrı; doğrudan seslenme"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"Tanrı adına sen veya baban; şaşma ya da ant kalıbı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları"}],"lexicalization_note":"Yalın özel ad, doğrudan seslenme biçimleri ve ant ya da şaşma kalıpları ayrı tutulur; kalıplara özgü işlevler özel adın her kullanımına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Genel tapınma dalı, yaşam üzerine ant, genel seslenme, kısaltılmış kişi seslenmesi ve yakarışa karşılık sözü gerçek sınır karşılaştırmaları sağladı; baba hitapları, genel dışlama yapıları, başka ant sözleri ve sesçe eşlik eden kalıplar daha zayıf ya da yalnızca biçimsel temas gösterdiği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli bir özel adın biçim ve kullanım alanıdır; komşu dal ise özel adla sınırlanmayan genel tapınma eylemini ve tapınılan varlık anlamını verir.","focus_only":"Yaratıcıya özgü adı ve bu adla kurulan seslenme, dilek, şaşma ve ant biçimlerini kapsar.","gloss":"tapınma ve tapınılan varlık","neighbor_only":"Genel tapınma eylemini, tapınılan varlığı ve bir varlığı tapınılır kılma işlemini kapsar.","neighbor_ref":"root_000047/B001","relation_type":"near_neighbor","shared_zone":"Özel ad, tapınılan yüce varlığı göstermesi bakımından genel varlık anlamına dayanır."},{"boundary_match":"partial","distinction":"Ortak işlev ant vermedir, fakat bu dalın dayanağı Yaratıcıya özgü addır; komşu dal yaşam süresini bildiren sözleri kullanır ve ayrıca ısrarlı istemeye uzanabilir.","focus_only":"Ant işlevini Yaratıcıya özgü adın yalın veya kısalmış biçimleriyle kurar.","gloss":"ömür üzerine ant ve ısrarlı isteme","neighbor_only":"Ant veya ısrarlı isteme işlevini yaşam süresini bildiren sözlerle kurar.","neighbor_ref":"root_001044/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir sözü güçlendiren ant işlevli kalıplar içerir."},{"boundary_match":"field_only","distinction":"Bu dal belirli bir muhatabın özel adı çevresinde oluşur; komşu dal ise muhatabın kimliğinden bağımsız genel seslenme araçlarını ve uzaklık ayrımını konu edinir.","focus_only":"Belirli bir özel adı ve o adın yakarma ile ant kullanımlarını içerir.","gloss":"genel seslenme öğeleri","neighbor_only":"Yakın veya uzaktaki muhataba yöneltilen genel seslenme öğelerini bildirir.","neighbor_ref":"root_000074/B008","relation_type":"same_field","shared_zone":"Her iki dal da doğrudan seslenme sırasında kullanılan biçimlerle ilgilidir."},{"boundary_match":"field_only","distinction":"Bu dalın kısalmaları belirli özel adın dinsel seslenme ve ant işlevlerine bağlıdır; komşu dalın kısalmaları ise belirsiz bir kişiye seslenmenin dilbilgisel biçimleridir.","focus_only":"Yaratıcıya özgü adı ve ona bağlı seslenme ile ant biçimlerini kapsar.","gloss":"kişiye yönelik kısaltılmış seslenme","neighbor_only":"Belirsiz bir kişiye yönelen kısaltılmış seslenme biçimlerini kapsar.","neighbor_ref":"root_001178/B003","relation_type":"same_field","shared_zone":"Her iki dalda da seslenme sırasında biçimsel kısalma görülebilir."},{"boundary_match":"thematic_only","distinction":"Bu dal bir muhataba seslenir; komşu dal ise söylenmiş yakarışa kabul dileği veya onayla karşılık verir. Aynı sahnede bulunsalar da anlam çekirdekleri örtüşmez.","focus_only":"Yakarışın yöneltildiği Yaratıcıyı özel adıyla çağırır.","gloss":"yakarışın kabulünü isteyen karşılık","neighbor_only":"Yakarışın kabul edilmesini isteyen veya söyleneni onaylayan karşılık sözünü bildirir.","neighbor_ref":"root_000054/B003","relation_type":"thematic","shared_zone":"İki dal da yakarış ortamında kullanılan kısa söz biçimlerine katılır."}],"source_phrase_ar":"فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)","source_summary":"Kaynaklar özel adı Yaratıcıya özgü bir ad olarak tanımlar ve onu tapınılan varlığı gösteren genel adla köken bakımından ilişkilendirir. Aynı adın doğrudan seslenmede, yakarmada, ant bildiriminde ve parçaları düşürülmüş kalıplarda kullanıldığı birlikte gösterilir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه اسم الله والقول في أصله من إله، وصيغ الاستعمال مثل الله ما فعلت بمعنى والله، واللهم، ويا الله، ولاه أبوك أو لاه أنت ونحوها.","what_is_not_ar":"ليس فرعا مستقلا عن معنى الإله المعبود من جهة الاشتقاق، ولا يدخل فيه إطلاق إله أو آلهة على كل معبود إذا لم يكن الكلام على صيغة الاسم أو النداء أو القسم."},"support_links":["sup_57fc7c6145607013864d","sup_6f4b2f40989ea0a0f51e","sup_dadcbdd89570b13bd2ab"]},{"boundary":"Dal yalnızca ışık ve aydınlatma anlamını kapsar; ateş, çiçek ve yol işareti ayrı dallardadır.","branch_kind":"bare","branch_ref":"root_001564/B001","candidate_links":[{"candidate_id":"cand_b34261ce72c71c448c83","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:6:1:1","qac_word_ref":"104:6:1","surface_ar":"نَارُ"}],"gloss":"ışık ve aydınlatma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Görmeyi sağlayan aydınlık ve ışık, dalın ad çekirdeğini oluşturur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyin ışık vermesi, aydınlanması veya aydınlatılması eylem alanını oluşturur."}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Işığın kendisiyle ışık verme, aydınlanma ve aydınlatma eylemlerinin tamamını karşılayan genel anlatımdır.","boundary_detail":"Dal yalnızca ışık ve aydınlatma anlamını kapsar; ateş, çiçek ve yol işareti ayrı dallardadır.","branch_image_ar":"الضياء والإضاءة","concept_gloss":"ışık ve aydınlatma","contextual_glosses":[{"applicability":"Bir nesnenin ya da ortamın ışık kazanmasını anlatan geçişsiz eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Işığın ad olarak kullanımı ile başkasını aydınlatma anlamını dışarıda bırakır.","preserves":"Işık kazanma ve aydınlık duruma gelme eylemini korur."},"facet_ids":["F002"],"text":"aydınlanmak","usage_role":"contextual"},{"applicability":"Bir kaynağın başka bir nesneye ya da ortama ışık vermesini anlatan geçişli eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Işığın ad anlamını ve kendiliğinden aydınlanma kullanımını dışarıda bırakır.","preserves":"Başka bir şeyi ışıklı duruma getirme eylemini korur."},"facet_ids":["F002"],"text":"aydınlatmak","usage_role":"contextual"}],"definition":"Işığın kendisini, bir şeyin ışık vermesini ya da başka bir şeyi aydınlatmasını anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Görmeyi sağlayan aydınlık ve ışık, dalın ad çekirdeğini oluşturur."},{"facet_id":"F002","role":"extension","statement":"Bir şeyin ışık vermesi, aydınlanması veya aydınlatılması eylem alanını oluşturur."}],"identity_rationale":"Kaynak ifadesi dalı doğrudan ışık, aydınlık ve bir şeyin ışık vermesi üzerinden kurar. Geçici çerçeve bu çekirdeği doğru yansıtır ve ateşin kendisini, çiçeği ya da yalnızca belirgin bir işareti bu anlama katmaz.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ışık, aydınlık"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"ışık vermek, aydınlanmak veya aydınlatmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"aydınlatma; günün ağarması"}],"lexicalization_note":"Tanım yalın dalın ışık ve aydınlatma çekirdeğiyle sınırlıdır; başka yapılara özgü anlamlar içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca doğrudan eşdeğerlik, sabah aydınlığı sınırı ve ateşle karışma ihtimalini açıklayan üç ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kartlarda kapsamı ayıran bir koşul, katılımcı veya sonuç bulunmaz; farklı örnek dizileri dal sınırını değiştirmez.","focus_only":null,"gloss":"ışık ve ışık verme","neighbor_only":null,"neighbor_ref":"root_000919/B001","relation_type":"synonym","shared_zone":"Her iki dal da ışığın kendisini ve bir şeyin ışık vermesi ya da başka bir şeyi aydınlatması eylemini kapsar."},{"boundary_match":"partial","distinction":"Odak dal genel ışık ve aydınlatmadır; komşu dal ise sabahın ağarması gibi karanlık sonrası açılma bağlamına daha sıkı bağlıdır.","focus_only":"Her türlü ışık, ışık verme ve aydınlatma bağlamını kapsar.","gloss":"ağarma ve aydınlanma","neighbor_only":"Özellikle karanlıktan sonra beliren gün ışığına ve yüzün parlamasına uzanır.","neighbor_ref":"root_000712/B002","relation_type":"near_synonym","shared_zone":"İki dal da ışığın görünür hale gelmesi ve ortamın aydınlanması alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal ışığın kendisini ve aydınlatmayı anlatır; komşu dal ise ışığın kaynağı olan yanan ateşi ve ona bağlı damgalama kullanımını anlatır.","focus_only":"Maddi bir ateş bulunmadan da ışık ve aydınlanma gerçekleşebilir.","gloss":"ışık ile ateş","neighbor_only":"Yanma, hareketli alev ve ateşle yapılan hayvan damgasını kapsar.","neighbor_ref":"root_001564/B002","relation_type":"near_neighbor","shared_zone":"Ateş ışık verdiği için iki dal aydınlık üretme noktasında kesişir."}],"source_phrase_ar":"النور الضياء والفعل نار وأنار ونورا وإنارة واستنار أي أضاء (ayn)؛ النور: الضياء؛ أنار الشئ واستنار بمعنى أي أضاء؛ التنوير: الإنارة؛ التنوير: الإسفار (sihah)؛ أصل صحيح يدل على إضاءة واضطراب وقلة ثبات؛ النور والنار سميا بذلك من طريقة الإضاءة (maqayis)","source_summary":"Kaynaklar ışık ve aydınlık anlamında, ayrıca ışık verme ve aydınlatma eylemlerinde birleşir; günün ağarması da aydınlanmanın bağlamsal bir gerçekleşmesi olarak verilir.","sources":["AY","SI","MQ"],"what_is_ar":"يدخل فيه النور بمعنى الضياء، وأفعال نار وأنار واستنار وأضاء، والتنوير بمعنى الإنارة والإسفار.","what_is_not_ar":"لا يدخل فيه النار المتقدة، ولا نور الشجر، ولا المنارة والعلامة إلا من جهة الإضاءة."},"support_links":["sup_57fc7c6145607013864d"]},{"boundary":"Yanan ateş çekirdektir; hayvan damgası ateşle yakma işlemine bağlı özel kullanımdır, yalın ışık değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001564/B002","candidate_links":[{"candidate_id":"cand_de2ce7935b024670a5dc","lane":"micro"},{"candidate_id":"cand_b34261ce72c71c448c83","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:6:1:1","qac_word_ref":"104:6:1","surface_ar":"نَارُ"}],"gloss":"yanan ateş ve ateşle yapılan hayvan damgası","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Işık veren ve hızlı, kararsız hareket gösteren yanan ateş temel anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvan üzerinde ateşle yakılarak oluşturulan damga, ateş çekirdeğine bağlı özel anlamdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hayvanın soyu ile damgasını ilişkilendiren söz, damga anlamına bağlı kalıplaşmış kullanımdır."}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın ateş çekirdeğini ve yalnız hayvan damgası yapılarında görülen yakma temelli özel anlamı birlikte gösterir.","boundary_detail":"Yanan ateş çekirdektir; hayvan damgası ateşle yakma işlemine bağlı özel kullanımdır, yalın ışık değildir.","branch_image_ar":"النار المتقدة والسمة بها","concept_gloss":"yanan ateş ve ateşle yapılan hayvan damgası","contextual_glosses":[{"applicability":"Yanmakta olan ateşin kendisinin anlatıldığı yalın bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvan damgasını ve bu damgaya bağlı kalıplaşmış sözü dışarıda bırakır.","preserves":"Yanan ve ışık yayan ateş çekirdeğini korur."},"facet_ids":["F001"],"text":"ateş","usage_role":"general"},{"applicability":"Bir hayvanın ateşle yakılarak oluşturulmuş ayırt edici işaretinin sorulduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalın ateş anlamını ve kalıplaşmış soy-damga sözünü dışarıda bırakır.","preserves":"Hayvana ateşle yapılan damga anlamını korur."},"facet_ids":["F002"],"text":"yakma damgası","usage_role":"contextual"}],"definition":"Yanarak ışık ve ısı yayan, hareketli alevleri bulunan ateşi anlatır. Aynı dalda, hayvana ateşle yakılarak yapılan damgaya ve bu damga üzerinden kurulan bir söze bağlı özel kullanımlar da vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Işık veren ve hızlı, kararsız hareket gösteren yanan ateş temel anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Hayvan üzerinde ateşle yakılarak oluşturulan damga, ateş çekirdeğine bağlı özel anlamdır."},{"facet_id":"F003","role":"associated_use","statement":"Hayvanın soyu ile damgasını ilişkilendiren söz, damga anlamına bağlı kalıplaşmış kullanımdır."}],"identity_rationale":"Kaynak ifadesi yanan ateşi, bu adın ışık ve hızlı hareketle bağlantısını ve hayvanın ateşle yapılan damgasını birlikte verir. Geçici çerçeve bu çok parçalı yapıyı doğru yansıtır; damga kullanımı ateşin temel tanımına değil, ona bağlı ayrı bir kullanıma yerleştirilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yanan ateş"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"ateşler"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"devenin ateşle yapılmış damgası"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"hayvanın soyu damgasından belli olur"}],"lexicalization_note":"Yalın ateş anlamı ile hayvana ait damga ve atasözü yapıları ayrı tutulur; özel yapılar genel ateş anlamına yayılmaz.","neighbor_coverage_note":"Tüm adaylar incelendi; alev, hayvan damgası ve ışıkla sınır karışıklığını en açık gösteren üç komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ateşin tamamını ve damga kullanımını içerir; komşu dal ise yalnız ateşin alevlenen bölümüne odaklanır.","focus_only":"Ateşin bütünü ile hayvanın ateşle yapılan damgasını kapsar.","gloss":"ateş ve alev","neighbor_only":"Ateşin yalnız saf ve yükselen alev bölümünü anlatır.","neighbor_ref":"root_001357/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da yanma ve görünür alev alanına aittir."},{"boundary_match":"field_only","distinction":"Ortak alan damgalamadır; odak dalın belirleyici özelliği yakma aracıdır, komşu dalın belirleyici özelliği ise damganın gizli konumudur.","focus_only":"Damganın ateşle yakılarak yapılmasını ve ateş anlamıyla bağını belirtir.","gloss":"hayvan damgaları","neighbor_only":"Seçkin bir devenin gizli bir yerine konan özel damgayı belirtir.","neighbor_ref":"root_000384/B005","relation_type":"same_field","shared_zone":"İki dal da hayvanı ayırt eden kalıcı bir işaret alanındadır."},{"boundary_match":"partial","distinction":"Odak dal ışık veren fiziksel ateştir; komşu dal ise kaynağından bağımsız olarak ışığı ve aydınlatmayı anlatır.","focus_only":"Yanma, ısı, hareketli alev ve ateşle yapılan damga bulunur.","gloss":"ateş ile ışık","neighbor_only":"Ateş gerektirmeyen genel ışık, aydınlanma ve aydınlatma bulunur.","neighbor_ref":"root_001564/B001","relation_type":"near_neighbor","shared_zone":"Ateşin ışık vermesi iki dalın kesişme noktasıdır."}],"source_phrase_ar":"النار مؤنثة وهي من الواو؛ الجمع نور ونيران (sihah)؛ ما نار هذه الناقة أي ما سمتها؛ نجارها نارها؛ سماتها (sihah)؛ النور والنار سميا بذلك من طريقة الإضاءة ولأن ذلك يكون مضطربا سريع الحركة (maqayis)","source_summary":"Kaynaklar yanan ateşi ışık ve hareket niteliğiyle açıklar; çoğul biçimlerini ve hayvanın ateşle yapılan damgasına bağlı kullanımları da aynı dalda toplar.","sources":["SI","MQ"],"what_is_ar":"يدخل فيه النار وما سميت به لطريقة الإضاءة واضطراب الحركة، وجموعها، والسمة بالنار في الناقة والإبل.","what_is_not_ar":"لا يدخل فيه مجرد الضياء بلا نار، ولا تنور النار من بعيد، ولا النائرة بين القوم."},"support_links":["sup_57fc7c6145607013864d","sup_dadcbdd89570b13bd2ab"]},{"boundary":"Anlam yalnız ateşle kurulan bu yapıya aittir; uzaktan görme ve ateşe yönelme iki ayrı kaynak açıklamasıdır.","branch_kind":"collocation","branch_ref":"root_001564/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:6:1:1","qac_word_ref":"104:6:1","surface_ar":"نَارُ"}],"gloss":"ateşi uzaktan görüp ona yönelmek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Uzakta bulunan ateşi görüp seçmek, yapının algısal açıklamasıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ateşe doğru yönelmek, aynı yapının amaç ve hareket bildiren kaynak açıklamasıdır."}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ateş nesnesiyle kurulan yapının hem uzaktan seçme hem de ona doğru gitme açıklamasını birlikte gösterir.","boundary_detail":"Anlam yalnız ateşle kurulan bu yapıya aittir; uzaktan görme ve ateşe yönelme iki ayrı kaynak açıklamasıdır.","branch_image_ar":"تنور النار من بعيد","concept_gloss":"ateşi uzaktan görüp ona yönelmek","contextual_glosses":[{"applicability":"Uzakta görünen ateşin fark edilmesi ve gözle seçilmesi öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ateşe doğru yönelme ve onu amaç edinme açıklamasını dışarıda bırakır.","preserves":"Ateşin uzaktan görülmesi ve seçilmesi anlamını korur."},"facet_ids":["F001"],"text":"ateşi uzaktan seçmek","usage_role":"contextual"},{"applicability":"Bir kimsenin gördüğü ya da bildiği ateşi hedef alarak ona doğru gitmesi öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalnız uzaktan görüp seçme açıklamasını dışarıda bırakır.","preserves":"Ateşi amaç edinip ona doğru gitme anlamını korur."},"facet_ids":["F002"],"text":"ateşe yönelmek","usage_role":"contextual"}],"definition":"Ateşi uzaktan seçmeyi veya ateşe doğru yönelmeyi anlatan yapıdır. Uzaktan görme ile yönelme, aynı yapı için verilen iki yakın kaynak açıklaması olarak ayrı tutulur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Uzakta bulunan ateşi görüp seçmek, yapının algısal açıklamasıdır."},{"facet_id":"F002","role":"source_variant","statement":"Ateşe doğru yönelmek, aynı yapının amaç ve hareket bildiren kaynak açıklamasıdır."}],"identity_rationale":"Kaynak ifadesi aynı ateş yapısını iki yakın fakat özdeş olmayan biçimde açıklar: ateşe yönelmek ve ateşi uzaktan seçmek. Geçici çerçeve kullanılabilir, ancak görme ile yönelmenin birbirine indirgenmemesi gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"ateşe doğru yönelmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ateşi uzaktan görüp seçmek"}],"lexicalization_note":"Tanım yalnız ateş nesnesiyle kurulan yapıya bağlıdır; genel görme, arama veya yönelme anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; gece ateşine yönelme, gözetleme ve görünürlükle en öğretici üç sınır seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak yapı görme veya yönelme düzeyinde kalır; komşu dal gece koşulunu ve ateş ışığıyla yol bulma sonucunu da içerir.","focus_only":"Ateşi uzaktan seçme açıklaması gece veya yol bulma koşuluna bağlı değildir.","gloss":"uzaktaki ateşe yönelme","neighbor_only":"Gece görünen ateşin ışığıyla yol bulma ve o ışığı kılavuz edinme anlamını taşır.","neighbor_ref":"root_001017/B002","relation_type":"near_synonym","shared_zone":"İki dal da uzakta görülen ateşi hedef alma ve ona doğru yönelme alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal belirli bir ateş yapısıdır; komşu dal nesnesi değişebilen, süreğen izleme ve bekleme eylemidir.","focus_only":"Nesne ateştir ve bazı açıklamalarda ona doğru gitme de bulunur.","gloss":"uzaktan görme ve gözetleme","neighbor_only":"Bakılan şeyi izleme, gözetleme ve bekleme sürecini kapsar.","neighbor_ref":"root_000142/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da uzaktaki bir şeyi gözle seçme alanını paylaşır."},{"boundary_match":"field_only","distinction":"Odak dal algılayan kişinin ateşle kurduğu eylemdir; komşu dal ise görülen şeyin açıklık niteliğini tanımlar.","focus_only":"Bir kişinin ateşi görmesi veya ateşe yönelmesi eylemini anlatır.","gloss":"görünürlük ve görme","neighbor_only":"Bir şeyin kendisinin açıkça görünür ve anlaşılır hale gelmesini anlatır.","neighbor_ref":"root_001473/B002","relation_type":"same_field","shared_zone":"İki dalda da bir şeyin gözle seçilebilir olması önemlidir."}],"source_phrase_ar":"تنورت نارا قصدت إليها (ayn)؛ تنورت النار من بعيد: تبصرتها (sihah)؛ تنورت النار تبصرتها (maqayis)","source_summary":"Kaynak açıklamaları aynı ateş yapısını uzaktan görme ile ateşe yönelme arasında konumlandırır; bu iki açıklama birleştirilmeden aynı kullanım çevresinin parçaları olarak korunur.","sources":["AY","SI","MQ"],"what_is_ar":"يدخل فيه تنورت النار إذا قصدت إليها أو تبصرتها من بعد.","what_is_not_ar":"لا يدخل فيه مطلق الإضاءة، ولا النار نفسها بلا فعل التنور."},"support_links":[]},{"boundary":"Dal ağaç çiçeği ve ağacın çiçek açmasıyla sınırlıdır; genel bitki çıkışı veya ışık anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001564/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:6:1:1","qac_word_ref":"104:6:1","surface_ar":"نَارُ"}],"gloss":"ağaç çiçeği ve çiçeklenme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ağaç üzerinde açan çiçek, dalın ad anlamıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ağacın çiçek çıkarması ve çiçeklenmesi, aynı çekirdeğin eylem görünümüdür."}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ağaçta beliren çiçeği ve ağacın bu çiçeği çıkarma sürecini birlikte karşılayan genel anlatımdır.","boundary_detail":"Dal ağaç çiçeği ve ağacın çiçek açmasıyla sınırlıdır; genel bitki çıkışı veya ışık anlamı değildir.","branch_image_ar":"نور الشجر وزهره","concept_gloss":"ağaç çiçeği ve çiçeklenme","contextual_glosses":[{"applicability":"Ağaç üzerinde açmış çiçeğin ad olarak belirtildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ağacın çiçek çıkarma ve çiçeklenme eylemini dışarıda bırakır.","preserves":"Ağaç üzerinde beliren çiçek anlamını korur."},"facet_ids":["F001"],"text":"ağaç çiçeği","usage_role":"general"},{"applicability":"Ağacın çiçeklerini ortaya çıkarması ve çiçekli hale gelmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ortaya çıkan çiçeğin bağımsız ad anlamını dışarıda bırakır.","preserves":"Ağacın çiçek çıkarma sürecini korur."},"facet_ids":["F002"],"text":"çiçek açmak","usage_role":"contextual"}],"definition":"Ağaçta beliren çiçeği ve ağacın çiçek çıkararak çiçeklenmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ağaç üzerinde açan çiçek, dalın ad anlamıdır."},{"facet_id":"F002","role":"extension","statement":"Ağacın çiçek çıkarması ve çiçeklenmesi, aynı çekirdeğin eylem görünümüdür."}],"identity_rationale":"Kaynak ifadesi ağacın çiçeğini ve ağacın çiçek açmasını açıkça aynı dalda toplar. Geçici çerçeve hem ortaya çıkan çiçeği hem de çiçek çıkarma sürecini korur ve genel ışık anlamını bu dala taşımaz.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"ağaç çiçeği"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ağaç çiçekleri; tek bir ağaç çiçeği"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ağaç çiçek açtı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ağacın çiçek açması"}],"lexicalization_note":"Ağaç çiçeğini adlandıran biçimler ile ağaç öznesine bağlı çiçek açma yapıları ayrılır; kapsam genel aydınlanmaya genişletilmez.","neighbor_coverage_note":"Bütün adaylar incelendi; ağaç çiçeği, çayır çiçeği ve genel bitki çıkışı arasındaki sınırı gösteren üç ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genel ağaç çiçeği çekirdeğidir; komşu dal belirli ağaç, renk ve bitki adlarıyla daha özel bir kapsama sahiptir.","focus_only":"Ağaç çiçeğini tür ve renk sınırlaması olmadan, ayrıca çiçeklenme eylemiyle kapsar.","gloss":"ağaç çiçeği","neighbor_only":"Belirli bir ağacın çiçeklenmesine, beyaz çiçeğe ve bazı bitki adlarına uzanır.","neighbor_ref":"root_000620/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da ağaçta ortaya çıkan çiçeği ve çiçeklenmeyi kapsar."},{"boundary_match":"partial","distinction":"Odak dal ağaç ve çiçeklenme sürecine bağlıdır; komşu dal çayırın çiçekli görünümüne bağlıdır.","focus_only":"Ağaç çiçeğini ve ağacın çiçek açma eylemini kapsar.","gloss":"çiçek örtüsü","neighbor_only":"Çayırın çiçek örtüsünü anlatan özel bir adlandırmadır.","neighbor_ref":"root_001331/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da bitkinin görünen çiçeklerini adlandırır."},{"boundary_match":"field_only","distinction":"Odak dalın sonucu çiçektir; komşu dal çiçekle sınırlı olmayan sürgün ve ekin çıkışını anlatır.","focus_only":"Özellikle ağaç çiçeğinin ortaya çıkmasını anlatır.","gloss":"bitkinin belirmesi","neighbor_only":"Hurma sürgününün ve ekinin genel olarak topraktan ya da bitkiden belirmesini anlatır.","neighbor_ref":"root_000945/B005","relation_type":"same_field","shared_zone":"İki dal da bitkide yeni bir bölümün görünür hale gelmesi sürecindedir."}],"source_phrase_ar":"النور نور الشجر؛ تنوير الشجرة إزهارها؛ النوار نور الشجر (ayn)؛ تنوير الشجرة: إزهارها؛ نورت الشجرة وأنارت أي أخرجت نورها؛ النوار نور الشجر (sihah)؛ ومنه النور نور الشجر ونواره؛ أنارت الشجرة أخرجت النور (maqayis)","source_summary":"Kaynaklar ağaç çiçeğini adlandırmada ve ağacın çiçek çıkarıp çiçeklenmesini anlatan eylemlerde birleşir.","sources":["AY","SI","MQ"],"what_is_ar":"يدخل فيه نور الشجر ونواره، وتنوير الشجرة أو إنارتها بمعنى إزهارها وإخراج نورها.","what_is_not_ar":"لا يدخل فيه الضوء العام، ولا النار، ولا النُّورَة التي يطلى بها."},"support_links":[]},{"boundary":"Belirginlik yol bulma, sınır gösterme, ışık taşıma veya çağrı yeri olma işlevine bağlıdır; yalın ışık değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001564/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:6:1:1","qac_word_ref":"104:6:1","surface_ar":"نَارُ"}],"gloss":"yol gösteren belirgin işaret ve yüksek yapı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yol üzerinde kolayca görülüp yön bulmayı sağlayan işaret temel işlevdir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Arazinin belirgin sınırları ve sınır işaretleri, gösterme işlevinin özel alanıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Üstünde ışık bulunan veya çağrı yapılan yüksek ve görünür yapı, işaret işlevinin yapısal uzantısıdır."}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yol işaretini, arazi sınırını ve ışık ya da çağrı işlevli görünür yüksek yapıyı ortak işlevleriyle karşılar.","boundary_detail":"Belirginlik yol bulma, sınır gösterme, ışık taşıma veya çağrı yeri olma işlevine bağlıdır; yalın ışık değildir.","branch_image_ar":"المنار والمنارة الظاهرة","concept_gloss":"yol gösteren belirgin işaret ve yüksek yapı","contextual_glosses":[{"applicability":"Yol üzerinde yön bulmayı sağlayan görünür bir işaret anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Arazi sınırını ve ışık ya da çağrı işlevli yüksek yapıyı dışarıda bırakır.","preserves":"Belirgin olma ve yol göstermeye yarama işlevini korur."},"facet_ids":["F001"],"text":"yol gösteren işaret","usage_role":"general"},{"applicability":"Üstünde ışık taşınan veya insanlara çağrı yapılan yüksek ve görünür yapı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yol işaretini ve arazinin sınır işaretlerini dışarıda bırakır.","preserves":"Yüksek yapının görünürlük, ışık taşıma ve çağrı yeri olma işlevini korur."},"facet_ids":["F003"],"text":"ışık ya da çağrı kulesi","usage_role":"explanatory"}],"definition":"Yol bulmayı veya sınırı tanımayı sağlayan belirgin işaretleri anlatır. Ayrıca üstünde ışık taşınan ya da insanlara çağrı yapılan görünür yüksek yapı bu işlevsel çekirdeğe bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yol üzerinde kolayca görülüp yön bulmayı sağlayan işaret temel işlevdir."},{"facet_id":"F002","role":"specialization","statement":"Arazinin belirgin sınırları ve sınır işaretleri, gösterme işlevinin özel alanıdır."},{"facet_id":"F003","role":"extension","statement":"Üstünde ışık bulunan veya çağrı yapılan yüksek ve görünür yapı, işaret işlevinin yapısal uzantısıdır."}],"identity_rationale":"Kaynak ifadesi yol gösteren belirgin işareti, arazi sınır ve işaretlerini ve üstünde ışık bulunan ya da çağrı yapılan yüksek yapıyı aynı görünürlük işlevi çevresinde toplar. Geçici çerçeve bu işlevsel ortaklığı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yol gösteren belirgin işaret"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"arazinin sınırları ve belirgin işaretleri"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"yol gösteren, üstünde ışık bulunan veya çağrı yapılan yüksek yapı"}],"lexicalization_note":"Yalın belirgin yol işareti ile arazi sınırı yapısı ve yüksek yapı anlamı ayrılır; özel yapıların kapsamı her işarete yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel işaret alanı, zaman anlamına uzanan işaret ve taş yapı arasındaki üç temel sınır seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yol, arazi sınırı ve yüksek yapı çevresinde toplanır; komşu dal çok daha geniş bir işaretleme ve ayırt etme alanına yayılır.","focus_only":"Işık taşınan veya çağrı yapılan yüksek yapıyı da kapsar.","gloss":"yol ve sınır işaretleri","neighbor_only":"Bayrak, dağ, kumaş işareti, boya ve çeşitli nesnelere konan ayırt edici izleri kapsar.","neighbor_ref":"root_001040/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da yol bulmaya veya bir şeyi tanımaya yarayan görünür işaretleri kapsar."},{"boundary_match":"partial","distinction":"Odak dal görünür yapı ve sınır işlevinde kalır; komşu dal işaret anlamından belirlenmiş zamana da uzanır.","focus_only":"Arazi sınırları ile ışık veya çağrı işlevli yüksek yapıyı kapsar.","gloss":"belirgin yol işareti","neighbor_only":"Belirlenmiş zaman ve buluşma vaktini de kapsar.","neighbor_ref":"root_000051/B005","relation_type":"near_synonym","shared_zone":"İki dal da yol veya açık arazide yön bulduran işareti anlatır."},{"boundary_match":"partial","distinction":"Odak dal işlev ve görünürlük üzerinden tanımlanır; komşu dalın ayırıcı özelliği taş malzeme ve dikili yapı biçimidir.","focus_only":"Taşla sınırlı değildir ve ışık ya da çağrı işlevli yüksek yapıyı içerir.","gloss":"yüksek yol işareti","neighbor_only":"Taşlardan yapılmış veya taş olarak dikilmiş yüksek işareti özel olarak belirtir.","neighbor_ref":"root_000075/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da uzaktan görülen ve yön bulmaya yardım eden yükseltilmiş işareti kapsar."}],"source_phrase_ar":"المنارة مفعلة من الإنارة؛ كانوا ينورون في الجاهلية ليهتدى ويقتدى بها؛ المنارة الشمعة ذات السراج؛ المنارة ما يوضع عليه للمسرجة؛ المنارة للمؤذن (ayn)؛ المنار: علم الطريق؛ ضرب المنار على طريقه ليهتدى بها؛ المنارة التي يؤذن عليها؛ المنارة ما يوضع فوقها السراج (sihah)؛ المنارة مفعلة من الاستنارة؛ منار الأرض حدودها وأعلامها سميت لبيانها وظهورها (maqayis)","source_summary":"Kaynaklar belirginlik ve görünürlüğü ortak zemin yapar; yol işareti, arazi sınırı ve ışık ya da çağrı için kullanılan yüksek yapı bu zeminde birleşir.","sources":["AY","SI","MQ"],"what_is_ar":"يدخل فيه المنار علامة الطريق، ومنار الأرض حدودها وأعلامها، والمنارة التي يهتدى بها أو يوضع عليها السراج أو يؤذن عليها.","what_is_not_ar":"لا يدخل فيه أسماء الأعلام مثل ذي المنار ومنور إلا من جهة التسمية، ولا يدخل فيه النور المجرد بلا علامة."},"support_links":[]},{"boundary":"Dal kaçınma, ürkme ve uzaklaştırmayı kapsar; genel ışık ya da topluluklar arası düşmanlık anlamına girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001564/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:6:1:1","qac_word_ref":"104:6:1","surface_ar":"نَارُ"}],"gloss":"ürkmek, kaçınmak ve uzaklaştırmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyden ürkme, kaçınma ve uzaklaşma temel hareket ve tutumdur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kötülükten veya erkeklerden uzak duran kadın ile eşten kaçınan dişi hayvan, katılımcıya bağlı özel nitelemelerdir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir başkasını söz veya davranışla ürkütüp uzaklaştırmak, katılımcıyı değiştiren ettirgen uzantıdır."}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan ve hayvandaki kaçınmayı, uzaklaşmayı ve bir başkasını ürkütüp uzaklaştıran ettirgen eylemi birlikte kapsar.","boundary_detail":"Dal kaçınma, ürkme ve uzaklaştırmayı kapsar; genel ışık ya da topluluklar arası düşmanlık anlamına girmez.","branch_image_ar":"النِّفار وقلة الثبات","concept_gloss":"ürkmek, kaçınmak ve uzaklaştırmak","contextual_glosses":[{"applicability":"Bir insanın ya da hayvanın istemediği şeyden kaçınarak uzak durması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başkasını ürkütüp uzaklaştıran ettirgen kullanımı dışarıda bırakır.","preserves":"Ürkme, kaçınma ve uzaklaşma çekirdeğini korur."},"facet_ids":["F001","F002"],"text":"ürkü̈p uzaklaşmak","usage_role":"general"},{"applicability":"Bir kişinin söz veya davranışla başka birini kaçırması ya da uzak durmaya itmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öznenin kendisinin kaçınması ile insan ve hayvan nitelemelerini dışarıda bırakır.","preserves":"Başka bir katılımcıyı ürkütüp uzaklaştırma eylemini korur."},"facet_ids":["F003"],"text":"ürkü̈tüp uzaklaştırmak","usage_role":"contextual"}],"definition":"Bir insanın ya da hayvanın hoş görülmeyen bir şeyden, kişiden veya eşten ürküp kaçınmasını ve uzaklaşmasını anlatır. Ettirgen kullanımda bir başkasını söz veya davranışla ürkütüp uzaklaştırma vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyden ürkme, kaçınma ve uzaklaşma temel hareket ve tutumdur."},{"facet_id":"F002","role":"specialization","statement":"Kötülükten veya erkeklerden uzak duran kadın ile eşten kaçınan dişi hayvan, katılımcıya bağlı özel nitelemelerdir."},{"facet_id":"F003","role":"extension","statement":"Bir başkasını söz veya davranışla ürkütüp uzaklaştırmak, katılımcıyı değiştiren ettirgen uzantıdır."}],"identity_rationale":"Kaynak ifadesi insanın kötülükten veya erkeklerden uzak durmasını, hayvanın ürküp eşinden kaçınmasını, bir şeyden uzaklaşmayı ve başkasını ürkütmeyi ortak bir kaçınma çekirdeğinde toplar. Geçici çerçeve kapsamı ve ettirgen katılımcı değişimini doğru verir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kötülükten veya erkeklerden uzak duran iffetli kadın"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"ürkek ve insandan kaçan ceylanlar"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"kuşku verici durumdan uzak duran kadınlar"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"eşinden ürküp kaçınan kısrak veya inek"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir şeyden ürküp uzaklaşmak"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"birini söz veya davranışla ürkütüp uzaklaştırmak"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"ürkme, kaçınma ve uzaklaşma"}],"lexicalization_note":"İnsan ve hayvan nitelemeleri ile kaçınma ve başkasını uzaklaştırma eylemleri ayrı tutulur; özel katılımcılar bütün dala zorunlu kılınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel uzaklaşma, hayvanın dirençli ürkekliği ve hoşnutsuzluktan kaçınma sınırlarını gösteren üçü seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli insan ve eşleşme bağlamlarını içerir; komşu dal korku ve düşünsel uzaklaşma dahil daha geniş bir kapsam taşır.","focus_only":"İffetli kadının kötülükten kaçınmasını ve dişi hayvanın eşten uzak durmasını özel olarak kapsar.","gloss":"ürkmek ve uzaklaşmak","neighbor_only":"Korku, vahşi hayvanın kaçışı ve gerçekten uzaklaşma gibi daha geniş neden ve nesnelere uzanır.","neighbor_ref":"root_001532/B001","relation_type":"near_synonym","shared_zone":"İki dal da insan veya hayvanın bir şeyden ürküp uzaklaşmasını ve başkasını uzaklaştırmayı kapsar."},{"boundary_match":"partial","distinction":"Odak dal kaçınma ve uzaklaştırma çekirdeğindedir; komşu dal hayvanın binilmeye direnmesi ve zor huy gibi ek davranışları içerir.","focus_only":"İnsan için ahlaki kaçınmayı ve başkasını ürkütme eylemini kapsar.","gloss":"hayvanın ürkekliği","neighbor_only":"Hayvanın sırtını kullandırmaması ile insandaki huysuzluk ve geçimsizliği kapsar.","neighbor_ref":"root_000818/B002","relation_type":"near_synonym","shared_zone":"İki dal da hayvanın ürkmesi, yaklaşanı kabul etmemesi ve yerinde durmaması alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal ürkme ve kaçışı öne çıkarır; komşu dal hoşnutsuzluk ve tiksinme nedenlerine göre çeşitlenir.","focus_only":"Kötülükten uzak duran kadın ile bir başkasını ürkütüp uzaklaştırmayı kapsar.","gloss":"istenmeyenden kaçınma","neighbor_only":"Yemden, ülkeden, sinekten ve çeşitli isteklerden tiksinme gibi belirli hoşnutsuzluk nedenlerini kapsar.","neighbor_ref":"root_000060/B006","relation_type":"near_synonym","shared_zone":"İki dal da insan veya hayvanın istemediği bir şeye yaklaşmaması ve ondan uzak durmasıdır."}],"source_phrase_ar":"امرأة نوار وهي العفيفة النافرة عن الشر والقبيح؛ التي تكره الرجال؛ بقرة نوار تنفر من الفحل؛ نرت فلانا أي أنفرته (ayn)؛ النور أيضا: النفر من الظباء؛ نسوة نور أي نفر من الربية؛ الواحدة نوار وهي الفرور؛ فرس وديق نوار؛ نرت من الشئ؛ نرت غيري أي نفرته (sihah)؛ امرأة نوار أي عفيفة تنور أي تنفر من القبيح؛ نارت نفرت؛ نرت فلانا نفرته؛ النوار النفار (maqayis)","source_summary":"Kaynaklar ürkme ve uzak durma çekirdeğinde birleşir; insanın ahlaki ya da toplumsal kaçınmasını, hayvanın eşten uzaklaşmasını ve başkasını ürkütme eylemini aynı dalda verir.","sources":["AY","SI","MQ"],"what_is_ar":"يدخل فيه نوار للمرأة العفيفة النافرة من القبيح أو الرجال، والنور أو النوار في الظباء والنساء والفرس والبقرة النافرة، ونرت فلانا إذا أنفرته.","what_is_not_ar":"لا يدخل فيه النور بمعنى الضياء، ولا نور الشجر، ولا النائرة بمعنى العداوة."},"support_links":[]},{"boundary":"Dal topluluklar arasında var olan düşmanlık ve kine aittir; savaşın kendisini veya yalnız ilan edilmesini zorunlu kılmaz.","branch_kind":"bare","branch_ref":"root_001564/B007","candidate_links":[{"candidate_id":"cand_8ceb94f94ff2133d0248","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:6:1:1","qac_word_ref":"104:6:1","surface_ar":"نَارُ"}],"gloss":"topluluklar arası düşmanlık ve kin","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Topluluklar arasında ortaya çıkan düşmanlık ve kin, dalın ilişkisel çekirdeğidir."}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki topluluk arasında doğan ve süren düşmanlık durumunu genel olarak karşılar.","boundary_detail":"Dal topluluklar arasında var olan düşmanlık ve kine aittir; savaşın kendisini veya yalnız ilan edilmesini zorunlu kılmaz.","branch_image_ar":"النائرة بين القوم","concept_gloss":"topluluklar arası düşmanlık ve kin","contextual_glosses":[{"applicability":"İki topluluğun ilişkisindeki kin ve karşıtlık doğal bir cümle içinde anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taraflar arasında süren düşmanlık ve kin durumunu korur."},"facet_ids":["F001"],"text":"aralarında düşmanlık var","usage_role":"contextual"}],"definition":"İki topluluk arasında ortaya çıkan ve ilişkilerini bozan düşmanlık, kin ve geçimsizlik durumunu anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Topluluklar arasında ortaya çıkan düşmanlık ve kin, dalın ilişkisel çekirdeğidir."}],"identity_rationale":"Kaynak ifadesi topluluklar arasında ortaya çıkan düşmanlık ve kini açıkça belirtir. Geçici çerçeve bu ilişkisel durumu doğru yansıtır ve onu fiziksel ateş, bireysel ürkme veya yalnız açık düşmanlık ilanıyla karıştırmaz.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"topluluklar arasında çıkan düşmanlık ve kin"}],"lexicalization_note":"Tanım yalın düşmanlık durumu ile sınırlıdır; savaş, açık ilan veya çatışma gibi komşu sonuçlar zorunlu anlam yapılmaz.","neighbor_coverage_note":"Tüm adaylar incelendi; savaş, etkin çatışma ve düşmanlığı açıkça gösterme ile olan üç temel kapsam farkı seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal düşmanlık durumunda kalır; komşu dal bu durumdan fiili savaşa, yere ve katılımcıya kadar genişler.","focus_only":"Özellikle topluluklar arasında ortaya çıkan kin ve bozuk ilişkiyi anlatır.","gloss":"düşmanlık ve savaş","neighbor_only":"Savaş eylemini, savaş durumunu, savaş ülkesini ve savaşan kişiyi de kapsar.","neighbor_ref":"root_000302/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da taraflar arasındaki düşmanlık ve barış karşıtı ilişkiyi kapsar."},{"boundary_match":"partial","distinction":"Odak dal ilişkisel düşmanlık durumudur; komşu dal düşmanlığın karşılıklı mücadele ve savaş halinde gerçekleşmesini öne çıkarır.","focus_only":"Fiili çarpışma olmadan da topluluklar arasındaki kin durumunu anlatabilir.","gloss":"düşmanlık ve çatışma","neighbor_only":"Karşılıklı savaşma, dövüşme ve etkin çatışmayı özellikle kapsar.","neighbor_ref":"root_001550/B007","relation_type":"near_synonym","shared_zone":"İki dal da tarafların birbirine düşman olması alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal durumun kendisidir; komşu dal bu durumun açıkça gösterilmesi ve ilan edilmesi eylemidir.","focus_only":"Düşmanlığın varlığını anlatır ve onun açıkça ilan edilmesini gerektirmez.","gloss":"düşmanlığı açığa vurmak","neighbor_only":"Düşmanlığın gizlenmeden açıkça ortaya konması eylemini anlatır.","neighbor_ref":"root_000097/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da taraflar arasındaki düşmanlık ilişkisine dayanır."}],"source_phrase_ar":"النائرة الكائنة تقع بين القوم (ayn)؛ بينهم نائرة أي عداوة وشحناء (sihah)","source_summary":"Kaynaklar anlamı topluluklar arasında beliren düşmanlık ve kin durumu olarak ortak biçimde açıklar.","sources":["AY","SI"],"what_is_ar":"يدخل فيه النائرة الواقعة بين القوم بمعنى العداوة والشحناء.","what_is_not_ar":"لا يدخل فيه النار الحسية، ولا النِّفار، ولا الضياء."},"support_links":["sup_6f4b2f40989ea0a0f51e"]},{"boundary":"Duman maddesi yalnız göz boyası veya dövme kullanımında yer alır; genel duman ve genel ışık anlamı bu dala girmez.","branch_kind":"bare","branch_ref":"root_001564/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:6:1:1","qac_word_ref":"104:6:1","surface_ar":"نَارُ"}],"gloss":"göz boyası ve dövme için kullanılan duman karası","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Fitil veya yağ dumanından elde edilen ve göz boyası ya da dövmede kullanılan koyu madde temel nesnedir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Deri veya diş eti iğnelendikten sonra açılan yerlere koyu madde sürme işlemi, nesneye bağlı eylemdir."}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Duman kökenli koyu maddeyi ve iğneleme sonrasında bu maddeyi uygulama eylemini birlikte kapsar.","boundary_detail":"Duman maddesi yalnız göz boyası veya dövme kullanımında yer alır; genel duman ve genel ışık anlamı bu dala girmez.","branch_image_ar":"دخان الوشم والكحل","concept_gloss":"göz boyası ve dövme için kullanılan duman karası","contextual_glosses":[{"applicability":"Fitil veya yağ dumanından elde edilip göz çevresinde ya da dövmede kullanılan koyu madde anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Deriyi veya diş etini iğneleyip madde uygulama eylemini dışarıda bırakır.","preserves":"Duman kökenli koyu madde ve onun göz boyası ile dövme amaçlarını korur."},"facet_ids":["F001"],"text":"duman karası","usage_role":"explanatory"},{"applicability":"Deri ya da diş etinde iğneyle açılan yerlere koyu madde veya göz boyası uygulanması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kullanılan duman kökenli maddenin bağımsız ad anlamını dışarıda bırakır.","preserves":"İğneleme ile ardından boya maddesi uygulama aşamalarını korur."},"facet_ids":["F002"],"text":"iğneleyip boya serpmek","usage_role":"contextual"}],"definition":"Fitil ya da yağ dumanından elde edilip göz boyası veya dövme maddesi olarak kullanılan koyu ürünü anlatır. Buna bağlı eylem, deri ya da diş etini iğneleyip açılan yerlere bu ürünü veya göz boyasını serpmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Fitil veya yağ dumanından elde edilen ve göz boyası ya da dövmede kullanılan koyu madde temel nesnedir."},{"facet_id":"F002","role":"associated_use","statement":"Deri veya diş eti iğnelendikten sonra açılan yerlere koyu madde sürme işlemi, nesneye bağlı eylemdir."}],"identity_rationale":"Kaynak ifadesi fitil ya da yağ dumanından elde edilen koyu maddeyi göz boyası veya dövme malzemesi olarak tanımlar; ayrıca deriyi ya da diş etini iğneleyip bu maddeyi veya göz boyasını uygulama eylemini verir. Geçici çerçeve kullanım amacını doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"göz boyası veya dövme için kullanılan fitil ya da yağ dumanı karası"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"deriyi veya diş etini iğneleyip üzerine duman karası ya da göz boyası serpmek"}],"lexicalization_note":"Tanım yalın dalda kozmetik ve dövme amaçlı duman maddesi ile buna bağlı iğneleme işlemini kapsar; genel dumana genişlemez.","neighbor_coverage_note":"Bütün adaylar incelendi; genel siyahlık, alevsiz duman ve göz boyası alanlarıyla en güçlü üç sınır karşılaştırması seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kullanım amacıyla sınırlı bir boya maddesidir; komşu dal genel siyahlık, kömür, kül ve duman alanına yayılır.","focus_only":"Duman karasını göz boyası veya dövme maddesi olarak ve iğneleme işleminde kullanır.","gloss":"duman karası ve genel siyahlık","neighbor_only":"Kömür, yanık kül, yoğun kara duman ve insan, hayvan ya da bitkideki genel siyahlığı kapsar.","neighbor_ref":"root_000001/B001","relation_type":"near_neighbor","shared_zone":"İki dal da yanma ya da duman sonucunda oluşan koyu siyah madde alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal dumanın kullanım için elde edilen katımsı karasına odaklanır; komşu dal dumanın kendisini anlatır.","focus_only":"Duman ürünü göz boyası veya dövme maddesi olarak toplanıp uygulanır.","gloss":"alevsiz duman ve boya maddesi","neighbor_only":"Alevsiz dumanı, herhangi bir kozmetik veya dövme amacı olmadan anlatır.","neighbor_ref":"root_001480/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da alevden ayrı düşünülebilen duman alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal maddenin duman kökeni ve dövme işleviyle tanımlanır; komşu dal parlatma ve görüşü açma işlevine yönelir.","focus_only":"Duman kökenli maddeyi dövmede de kullanır ve iğneleme sonrası uygulama işlemini kapsar.","gloss":"göz boyası kullanımı","neighbor_only":"Kılıcı parlatma ve görüşü açtığı düşünülen göz boyasını kapsar.","neighbor_ref":"root_000256/B002","relation_type":"same_field","shared_zone":"İki dal da göze uygulanan koyu boya maddesi alanında kesişir."}],"source_phrase_ar":"النؤور دخان الفتيلة يتخذ كحلا أو وشما (ayn)؛ النوور: النيلج، وهو دخان الشحم يعالج به الوشم؛ وقد نور ذراعه إذا غرزها بإبرة ثم ذر عليها النوور (sihah)؛ مما شذ عن هذا الأصل النؤور دخان الفتيلة يتخذ كحلا ووشما؛ نورت اللثة غرزتها بإبرة ثم جعلت في الغرز الإثمد (maqayis)","source_summary":"Kaynaklar duman kökenli koyu maddenin göz boyası ve dövme amacıyla kullanımında birleşir; iğneleme sonrası bu maddeyi ya da göz boyasını uygulama işlemini de açıklar.","sources":["AY","SI","MQ"],"what_is_ar":"يدخل فيه النُّؤور أو النُّوور، وهو دخان الفتيلة أو الشحم المتخذ كحلا أو وشما، ويدخل فيه نور العضو إذا غرز ثم ذر عليه الإثمد أو النُّوور.","what_is_not_ar":"لا يدخل فيه ضياء النور، ولا دخان النار مطلقا بلا استعمال كحل أو وشم."},"support_links":[]},{"boundary":"Dal bedene sürülen belirli madde ve onun uygulanmasıyla sınırlıdır; her türlü yağ, boya veya yapıştırıcıyı kapsamaz.","branch_kind":"bare","branch_ref":"root_001564/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:6:1:1","qac_word_ref":"104:6:1","surface_ar":"نَارُ"}],"gloss":"bedene sürülen özel karışım ve onu sürünme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bedene sürülmek için kullanılan özel karışım, dalın nesne anlamıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin bu karışımı kendi bedenine sürmesi, nesne anlamına bağlı eylemdir."}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Özel maddenin kendisini ve kişinin onu bedenine uygulamasını birlikte karşılar.","boundary_detail":"Dal bedene sürülen belirli madde ve onun uygulanmasıyla sınırlıdır; her türlü yağ, boya veya yapıştırıcıyı kapsamaz.","branch_image_ar":"النُّورَة المطلية","concept_gloss":"bedene sürülen özel karışım ve onu sürünme","contextual_glosses":[{"applicability":"Kişisel bakım amacıyla bedene sürülen özel maddenin kendisi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin bu maddeyi kendi bedenine sürmesi eylemini dışarıda bırakır.","preserves":"Maddenin bedene sürülmek üzere hazırlanmış olmasını korur."},"facet_ids":["F001"],"text":"bedene sürülen karışım","usage_role":"explanatory"},{"applicability":"Bir kişinin söz konusu özel karışımı kendi bedenine uygulaması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uygulanan özel maddenin bağımsız ad anlamını dışarıda bırakır.","preserves":"Kişinin maddeyi kendi bedenine uygulama eylemini korur."},"facet_ids":["F002"],"text":"bedenine sürmek","usage_role":"contextual"}],"definition":"Bedene sürülen özel bir karışımı ve kişinin bu karışımı bedenine sürmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bedene sürülmek için kullanılan özel karışım, dalın nesne anlamıdır."},{"facet_id":"F002","role":"extension","statement":"Kişinin bu karışımı kendi bedenine sürmesi, nesne anlamına bağlı eylemdir."}],"identity_rationale":"Kaynak ifadesi bedene sürülen özel bir maddeyi ve kişinin bu maddeyi bedenine sürmesini açıkça verir. Geçici çerçeve nesne ile uygulama eylemini doğru bir arada tutar ve onu ışık, duman karası veya genel boya anlamına genişletmez.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bedene sürülen özel karışım"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"özel karışımı bedenine sürmek"}],"lexicalization_note":"Tanım yalın dalın bedene sürülen özel madde ve onu sürünme anlamıyla sınırlıdır; komşu kaplama maddeleri içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yağlama, metal araçla beden bakımı ve sıva benzeri kaplama arasındaki üç sınır seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal özel madde ve beden nesnesine bağlıdır; komşu dal maddenin yağ olması ve daha genel yüzeylere uygulanmasıyla tanımlanır.","focus_only":"Belirli bir karışımın insan bedenine uygulanmasıyla sınırlıdır.","gloss":"bedene sürülen madde ve yağ","neighbor_only":"Her tür yağ ve yağlama eylemini, nesnesi beden olsun olmasın kapsar.","neighbor_ref":"root_000497/B001","relation_type":"near_neighbor","shared_zone":"İki dal da bir maddeyi yüzeye sürerek kaplama eylemini kapsar."},{"boundary_match":"thematic_only","distinction":"Anlamsal çekirdekleri farklıdır: odak dal madde sürmedir, komşu dal metal araçla kesme veya keskinleştirmedir.","focus_only":"Bedene bir karışım sürerek bakım yapmayı anlatır.","gloss":"beden bakımı","neighbor_only":"Demir araç kullanmayı, kıl kesmeyi ve bıçağı keskinleştirmeyi anlatır.","neighbor_ref":"root_000002/B008","relation_type":"thematic","shared_zone":"İki dal kişisel bakım senaryosunda, özellikle beden üzerindeki uygulamalarda buluşabilir."},{"boundary_match":"field_only","distinction":"Odak dal beden uygulamasıdır; komşu dal yapı sıvası ve beyazlık belirtisi çevresinde toplanır.","focus_only":"İnsan bedenine sürülen özel karışımı ve kişinin onu uygulamasını kapsar.","gloss":"sürülen açık renkli madde","neighbor_only":"Yapı ve mezarların sıvanmasını, ayrıca bedensel bir beyazlık belirtisini kapsar.","neighbor_ref":"root_001232/B007","relation_type":"same_field","shared_zone":"İki dal yüzeye sürülen bir madde ve kaplama görüntüsü alanında ilişkilidir."}],"source_phrase_ar":"النورة يطلى بها (ayn)؛ تنور الرجل: تطلى بالنورة (sihah)","source_summary":"Kaynaklar bedene sürülen özel maddeyi ve bir kişinin bu maddeyi kendi bedenine sürmesi eylemini aynı dalda verir.","sources":["AY","SI"],"what_is_ar":"يدخل فيه النُّورَة التي يطلى بها، وتنور الرجل إذا تطلى بالنُّورَة.","what_is_not_ar":"لا يدخل فيه النور بمعنى الضوء، ولا النُّؤور دخان الفتيلة، ولا نور الشجر."},"support_links":[]},{"boundary":"Anlam yalnız kişi yöneltmeli yapıda bir işi karıştırıp yanıltmaktır; genel gizleme veya açıklama anlamına yayılmaz.","branch_kind":"collocation","branch_ref":"root_001564/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:6:1:1","qac_word_ref":"104:6:1","surface_ar":"نَارُ"}],"gloss":"bir işi karışık gösterip yanıltmak","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir işi muhataba karışık göstererek onu yanıltmak, yapının temel eylemidir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynak, bu kullanımın kökenini bütünüyle yerli saymadığını ayrıca belirtir."}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız belirli bir kişiye yönelen ve bir işi ona karışık gösteren yapı için geçerlidir.","boundary_detail":"Anlam yalnız kişi yöneltmeli yapıda bir işi karıştırıp yanıltmaktır; genel gizleme veya açıklama anlamına yayılmaz.","branch_image_ar":"التلبيس على الغير","concept_gloss":"bir işi karışık gösterip yanıltmak","contextual_glosses":[{"applicability":"Bir işi bir kişiye belirsiz veya başka türlü göstererek onun doğru anlamasını engelleme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiye yönelen karıştırma ve onu doğru anlamdan uzaklaştırma eylemini korur."},"facet_ids":["F001","F002"],"text":"kafasını karıştırmak","usage_role":"contextual"}],"definition":"Belirli bir kişiye bir işi karışık ve başka türlü göstererek onun doğru anlamasını engellemeyi anlatan yapıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir işi muhataba karışık göstererek onu yanıltmak, yapının temel eylemidir."},{"facet_id":"F002","role":"source_variant","statement":"Kaynak, bu kullanımın kökenini bütünüyle yerli saymadığını ayrıca belirtir."}],"identity_rationale":"Kaynak ifadesi belirli bir kişi yöneltmeli yapıda bir işi ona karışık gösterip onu yanıltma anlamını açıkça verir. Bununla birlikte kaynak kullanımın bütünüyle yerli olmadığını belirtir; bu nedenle anlam kabul edilirken köken açıklaması kesinleştirilmez.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"bir işi birine karışık gösterip onu yanıltmak"}],"lexicalization_note":"Tanım yalnız verilen kişi yöneltmeli yapıya bağlıdır; yalın biçime genel yanıltma anlamı yüklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel belirsizleştirme, gizleme, hile ve açıklığa çıkarma karşıtlığı en yararlı dört sınır olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal muhatabı yanıltan belirli bir yapıdır; komşu dal nesnenin karışması veya karıştırılması biçiminde daha genel bir kapsama sahiptir.","focus_only":"Belirli bir kişi yöneltmeli yapıda bir işi ona karışık gösterir.","gloss":"karıştırmak ve belirsizleştirmek","neighbor_only":"İşin, sözün veya karanlığın kendisinin karışıp belirsizleşmesini daha genel biçimde kapsar.","neighbor_ref":"root_001341/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir işin anlaşılmasını güçleştiren karışıklık ve belirsizlik yaratır."},{"boundary_match":"partial","distinction":"Odak dal yanlış veya karışık görünüm üretir; komşu dal bilginin kendisini saklar ve görünmez kılar.","focus_only":"İşi kişiye başka türlü göstererek zihinsel karışıklık yaratır.","gloss":"yanıltmak ve gizlemek","neighbor_only":"İşi doğrudan gizleyip kişinin ondan haberdar olmasını engeller.","neighbor_ref":"root_001617/B009","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişinin bir işi doğru biçimde öğrenmesini engeller."},{"boundary_match":"partial","distinction":"Odak dal anlama sürecini karıştırır; komşu dal gizli amaç taşıyan daha geniş bir hile ve davranış düzenini anlatır.","focus_only":"Kişiye belirli bir işi karışık gösterme yapısıyla sınırlıdır.","gloss":"aldatıcı karıştırma","neighbor_only":"Bir şeyi gösterip başka bir şeyi amaçlayan hileli davranışı ve kalıplaşmış sözü kapsar.","neighbor_ref":"root_000439/B008","relation_type":"near_neighbor","shared_zone":"İki dal da görünüş ile gerçek amaç arasındaki ayrılıktan yararlanarak karşı tarafı yanıltır."},{"boundary_match":"opposed","distinction":"Odak dal anlaşılabilirliği azaltır ve yanıltır; komşu dal görünürlüğü ve açıklığı artırır.","focus_only":"Bir işi anlaşılmaz veya yanlış anlaşılır hale getirir.","gloss":"karıştırma ve açıklığa çıkarma","neighbor_only":"Bir şeyin görünür, açık ve kanıtlanabilir hale gelmesini anlatır.","neighbor_ref":"root_000170/B004","relation_type":"polarity_pair","shared_zone":"İki dal da bir işin muhatap tarafından ne ölçüde açıkça anlaşılabildiği eksenindedir."}],"source_phrase_ar":"فلان ينور على فلان إذا شبه عليه أمرا؛ ليست الكلمة بعربية محضة؛ امرأة كانت تسمى نورة (ayn)","source_qualifications":[{"kind":"sole_attestation","summary":"Bir işi kişiye karışık gösterip onu yanıltan yapı tek başına tanıklanır; kullanımın bütünüyle yerli olmadığı da belirtilir."}],"source_summary":"Dalın anlamı ve köken sınırlaması tek bir kaynak tanıklığına dayanır.","sources":["AY"],"what_is_ar":"يدخل فيه قولهم نور على فلان إذا شبه عليه أمرا.","what_is_not_ar":"لا يدخل فيه الإنارة، ولا النُّورَة، ولا النار."},"support_links":[]},{"boundary":"Anlam kümesi açıklık ve belirgin çıkıntı çevresinde tutulur; incelenen köke bağlılığı olasılık düzeyindedir.","branch_kind":"mixed_non_bare","branch_ref":"root_001564/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:6:1:1","qac_word_ref":"104:6:1","surface_ar":"نَارُ"}],"gloss":"açıkça seçilen veya belirgin biçimde çıkan şey","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin açıkça seçilmesi ve çevresinden belirgin biçimde çıkması ortak anlam ilkesidir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Açık yol oluğu ve kumaştaki belirgin işaret, görünürlük ilkesinin nesne örnekleridir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çift hayvanının boynuna konan boyunduruk ve iki kat güçle nitelenen kişi, kümenin özel kullanımlarıdır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bu ses yapısının incelenen köke dönmesi kaynakta kesinlik değil, yalnız olasılık olarak sunulur."}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yol oluğu, kumaş işareti, boyunduruk ve güç nitelemesini ortak belirginlik ilkesiyle, kök bağına kesinlik vermeden kapsar.","boundary_detail":"Anlam kümesi açıklık ve belirgin çıkıntı çevresinde tutulur; incelenen köke bağlılığı olasılık düzeyindedir.","branch_image_ar":"وضوح النِّير وبروزه","concept_gloss":"açıkça seçilen veya belirgin biçimde çıkan şey","contextual_glosses":[{"applicability":"Yol üzerinde açıkça görülen uzun çukur ya da iz anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kumaş işareti, boyunduruk, güç nitelemesi ve kök belirsizliğini dışarıda bırakır.","preserves":"Yoldaki açıkça seçilen oluk ve belirginlik özelliğini korur."},"facet_ids":["F001","F002"],"text":"belirgin yol oluğu","usage_role":"contextual"},{"applicability":"Çift süren hayvanın boynuna aracıyla birlikte konan ağaç parça anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yol oluğu, kumaş işareti, güç nitelemesi ve kök belirsizliğini dışarıda bırakır.","preserves":"Hayvanın boynuna konan belirgin ağaç parça anlamını korur."},"facet_ids":["F001","F003"],"text":"çift hayvanı boyunduruğu","usage_role":"contextual"}],"definition":"Açıkça seçilen veya çevresinden belirgin biçimde çıkan şeyleri anlatan bir kümedir; açık yol oluğu, kumaştaki belirgin işaret, çift hayvanının boynundaki boyunduruk ve gücü iki kat sayılan kişi bu çerçevede verilir. Kümenin incelenen köke bağlılığı kesin değil, olasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin açıkça seçilmesi ve çevresinden belirgin biçimde çıkması ortak anlam ilkesidir."},{"facet_id":"F002","role":"example","statement":"Açık yol oluğu ve kumaştaki belirgin işaret, görünürlük ilkesinin nesne örnekleridir."},{"facet_id":"F003","role":"specialization","statement":"Çift hayvanının boynuna konan boyunduruk ve iki kat güçle nitelenen kişi, kümenin özel kullanımlarıdır."},{"facet_id":"F004","role":"source_variant","statement":"Bu ses yapısının incelenen köke dönmesi kaynakta kesinlik değil, yalnız olasılık olarak sunulur."}],"identity_rationale":"Kaynak ifadesi bu kümeyi önce ayrı bir ses yapısı altında açıklık ve çıkıntı ilkesiyle kurar; yol oluğu, kumaş işareti, boyunduruk ve iki kat güç örneklerini verir. Aynı kaynak bunun incelenen köke dönmesinin mümkün olduğunu yalnız ihtimal olarak söyler, bu yüzden dal korunur ancak kök bağı kesin gösterilemez.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"yolun belirgin oluğu"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"kumaşın belirgin işareti veya çizgisi"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"çift hayvanının boynundaki boyunduruk ve takımı"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"gücü başkasının iki katı olan adam"}],"lexicalization_note":"Yol oluğu ve boyunduruk adları ile kumaş ve kişi yapıları ayrı tutulur; olası kök bağı bütün örnekleri yalın ışık anlamına dönüştürmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yol oluğu, işaret, koşum takımı ve görünür hale gelme alanlarıyla en açıklayıcı dört sınır seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kullanım açık yol oluğuna bağlı bir alt alandır; komşu dal malzeme ve yer bakımından daha geniş uzun yarık çekirdeğine sahiptir.","focus_only":"Yol üzerindeki açık oluğun yanında kumaş işareti, boyunduruk ve güç nitelemesini de kapsar.","gloss":"belirgin oluk ve uzun yarık","neighbor_only":"Toprakta veya bedende oluşan uzun, derin yarık ve kazılmış izleri daha genel biçimde kapsar.","neighbor_ref":"root_000395/B002","relation_type":"near_synonym","shared_zone":"İki dal da zeminde uzanan, çevresinden ayrılan oluk veya yarık biçimini kapsar."},{"boundary_match":"partial","distinction":"Odak dal kumaştaki işareti genel belirginlik ilkesine bağlar; komşu dalın çekirdeği nesnelerin kenarı boyunca uzanan yan çizgidir.","focus_only":"Kumaştaki belirgin işareti yol oluğu, boyunduruk ve güç nitelemesiyle aynı açıklık kümesinde verir.","gloss":"kumaş işareti ve yan çizgi","neighbor_only":"Dizgin ve yanak üzerindeki yan çizgiyi, duvar ve vadi kenarlarını, yan yana uzanan yolları kapsar.","neighbor_ref":"root_000995/B008","relation_type":"near_neighbor","shared_zone":"İki dal da bir yüzeyde uzanan ve çevresinden belirgin biçimde ayrılan çizgi ya da işaret alanında buluşur."},{"boundary_match":"field_only","distinction":"Odak parça boyun üzerindeki sert boyunduruktur; komşu parça karın ya da bel çevresinde kullanılan bağ ve iptir.","focus_only":"Çift hayvanının boynuna konan ağaç boyunduruğu ve takımını anlatır.","gloss":"hayvan koşum takımı","neighbor_only":"Devenin karnından geçirilen eyer bağı ile bele bağlanan ipi anlatır.","neighbor_ref":"root_000345/B002","relation_type":"same_field","shared_zone":"İki dal da yük veya araç bağlantısında hayvanın bedenine yerleştirilen koşum parçası alanındadır."},{"boundary_match":"partial","distinction":"Odak dal belirgin nesneleri adlandıran bir kümedir; komşu dal görünür hale gelme ve ortaya çıkma sürecini anlatır.","focus_only":"Belirginliği somut nesne adlarına ve güç nitelemesine dönüştürür.","gloss":"belirginlik ve ortaya çıkma","neighbor_only":"Yolun, gerçeğin, işin veya topluluğun görünür hale gelmesi eylem ve durumlarını kapsar.","neighbor_ref":"root_000268/B007","relation_type":"near_neighbor","shared_zone":"İki dal da bir şeyin çevresinden ayrılarak açıkça görünmesi düşüncesini paylaşır."}],"source_phrase_ar":"النون والياء والراء كلمة تدل على وضوح شيء وبروزه؛ أخدود الطريق الواضح منه نير؛ نير الثوب علمه؛ النير الخشبة على عنق الفدان؛ ما ننكر أن يكون أصل هذا كله الواو فيرجع إلى ما ذكرناه في باب النور والنار (maqayis)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık açıklık ve belirgin çıkıntı ilkesini yol oluğu, kumaş işareti, boyunduruk ve iki kat güç örnekleriyle verir; kök bağını ise olası sayar."}],"source_summary":"Dalın bütün anlamları ve kök bağlantısına ilişkin ihtimal tek bir kaynak tanıklığına dayanır.","sources":["MQ"],"what_is_ar":"يدخل فيه النِّير في أخدود الطريق الواضح، وعلم الثوب، والخشبة على عنق الفدان، وما قيس على الوضوح والبروز في مدخل نير.","what_is_not_ar":"لا يدخل فيه جذر ن و ر إلا على احتمال رجوع الواو الذي ذكره مقاييس."},"support_links":[]},{"boundary":"Dal gerçek ateşin yanma ve yakılma süreciyle sınırlıdır; yakıt, ateş yeri, yaz sıcağı ve mecazlı kullanımlar ayrı dallardadır.","branch_kind":"mixed_non_bare","branch_ref":"root_001672/B001","candidate_links":[{"candidate_id":"cand_de2ce7935b024670a5dc","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُوقَدَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|(IV)|LEM:muwqadap|ROOT:wqd|F|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"104:6:3:2","qac_word_ref":"104:6:3","surface_ar":"مُوقَدَةُ"}],"gloss":"ateşin tutuşması, yakılması ve alevli görünümü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ateş tutuşur, yanmaya başlar ve alevli biçimde sürer."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişi ateşi yakarak onun tutuşmasını sağlar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişi ateş yakmayı ister, üstlenir ya da bu işe girişir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Ad biçimleri yanma sürecini, ateşin kendisini veya görünen alevi gösterebilir."}}],"root_ar":"و ق د","root_id":"root_001672","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yanma, yakma, yakmaya girişme ve yanma ya da alev adı olan çekirdek kapsamını birlikte anlatır.","boundary_detail":"Dal gerçek ateşin yanma ve yakılma süreciyle sınırlıdır; yakıt, ateş yeri, yaz sıcağı ve mecazlı kullanımlar ayrı dallardadır.","branch_image_ar":"اشتعال النار وإيقادها","concept_gloss":"ateşin tutuşması, yakılması ve alevli görünümü","contextual_glosses":[{"applicability":"Öznenin ateş olduğu ve yanmanın kendiliğinden gerçekleştiği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ateşi yakma, yakmaya girişme ve ad biçimlerinin kapsamını dışarıda bırakır.","preserves":"Ateşin tutuşarak yanması yönünü korur."},"facet_ids":["F001"],"text":"tutuşup yanmak","usage_role":"contextual"},{"applicability":"Bir kişinin ateşin yanmasını başlattığı geçişli kullanımlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kendiliğinden yanmayı, yakmaya girişmeyi ve ad biçimlerini kapsamaz.","preserves":"Bir etkenin ateşi tutuşturması yönünü korur."},"facet_ids":["F002"],"text":"ateşi yakmak","usage_role":"contextual"},{"applicability":"Ateşi yakmayı isteme, üstlenme veya hazırlığını yapma anlamının öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yanmanın kendisini, tamamlanmış yakma eylemini ve alev adını kapsamaz.","preserves":"Ateşi yakmaya yönelme ve bu işi üstlenme anlamını korur."},"facet_ids":["F003"],"text":"ateş yakmaya girişmek","usage_role":"explanatory"}],"definition":"Ateşin tutuşup yanması ya da birinin ateşi yakarak bu yanmayı başlatmasıdır. Aynı anlam alanında yanma süreci, ateşin kendisi ve görünen alev de adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ateş tutuşur, yanmaya başlar ve alevli biçimde sürer."},{"facet_id":"F002","role":"specialization","statement":"Bir kişi ateşi yakarak onun tutuşmasını sağlar."},{"facet_id":"F003","role":"specialization","statement":"Bir kişi ateş yakmayı ister, üstlenir ya da bu işe girişir."},{"facet_id":"F004","role":"source_variant","statement":"Ad biçimleri yanma sürecini, ateşin kendisini veya görünen alevi gösterebilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yanan malzemeyi bildirerek komşu dalın anlamını getirir.","collision":"Yakacak maddeyi anlatan root_001672/B002 ile karışır.","fit":"displacement","loses":"Yanma, yakma ve alev anlamlarının tamamını kaybeder.","preserves":"Ateş alanıyla olan genel bağlantıyı korur."},"text":"yakıt"}],"identity_rationale":"Kaynak ifadesi, ateşin tutuşup yanmasını, ateşi yakmayı, yakmaya girişmeyi ve yanma ile görünen alevi adlandıran biçimleri birlikte verir. Bu nedenle dalın ateşin yanması ve yakılması çevresindeki çerçevesi kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ateş tutuştu ve yandı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"tutuştu, yanmaya başladı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"alevlendi, harlayarak yandı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"ateşi yaktı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"ateşi yakmaya girişti veya yakılmasını istedi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yanma; ortaya çıkan alev"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ateşin kendisi veya görünen alevi"}],"lexicalization_note":"Tanım, ateşin kendiliğinden yanmasını, ateşi yaktıran geçişli kullanımları ve yanma ya da alev adlarını ayırır; belirli söz öbekleri bütün dala genellenmez.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; yalnızca yanma, alev ve yakıt sınırlarını doğrudan açıklayan üç karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yanma ile yakma sürecini ve bunların adlarını birlikte örgütler; komşu dal ise alevin görünür biçimini ve alevlenmeyi daha doğrudan merkeze alır.","focus_only":"Yanma sürecinin adlarını ve ateş yakmaya girişme anlamını da kapsar.","gloss":"tutuşma, yakma ve alev","neighbor_only":"Alev dili ve saf alev görünümü komşu dalda daha belirgin bir merkezdir.","neighbor_ref":"root_001379/B001","relation_type":"near_synonym","shared_zone":"Her iki dal ateşin tutuşmasını, yakılmasını ve görünen alevini anlatabilir."},{"boundary_match":"partial","distinction":"Bu dal temel yanma ve yakma olayını anlatır; komşu dal yanmakta olan ateşi besleyip güçlendirme gibi ek işlemleri de içerir.","focus_only":"Ateşin yanması, yakılması ve bu süreç ya da alev için kullanılan adları kapsar.","gloss":"ateşin yanması ve yakılması","neighbor_only":"Ateşi harlatma, yükseltme ve ateşe onu güçlendirecek madde atma yönlerini de kapsar.","neighbor_ref":"root_000517/B002","relation_type":"near_synonym","shared_zone":"İki dal da ateşin tutuşması, yanması ve insan eliyle yakılması alanında örtüşür."},{"boundary_match":"field_only","distinction":"Bu dal olay ve süreci, komşu dal ise o sürece giren yanıcı malzemeyi adlandırır; biri diğerinin yerine kullanılamaz.","focus_only":"Ateşin tutuşması, yanması ve bir etken tarafından yakılmasıdır.","gloss":"yanma ile yakıt ayrımı","neighbor_only":"Yanmayı sağlayan yakacak maddeyi, özellikle ateş için hazırlanmış odunu bildirir.","neighbor_ref":"root_001672/B002","relation_type":"same_field","shared_zone":"Her iki dal gerçek ateş ve onun sürdürülmesiyle ilgili aynı uygulama alanındadır."}],"source_phrase_ar":"كلمة تدل على اشتعال نار (maqayis)؛ وقدت النار واتقدت وتوقدت وأوقدتها (maqayis)؛ وقدت النار وقودا ووقدا (ayn;sihah;mufradat)؛ أوقدتها واستوقدتها (sihah;mufradat)؛ الوقود بالضم الاتقاد (sihah)؛ الوقد نفس النار أو ما ترى من لهبها (maqayis;ayn)؛ الوقود لما حصل من اللهب (mufradat)","source_summary":"Kaynakların ortak çerçevesi ateşin tutuşması ve yanmasıdır; geçişli biçimler ateşi yakmayı, başka bir biçim yakmaya girişmeyi, ad biçimleri ise yanmayı, ateşi veya görünen alevi bildirir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه وقدت النار واتقدت وتوقدت وأوقدها واستوقدها، واسم الاشتعال واللهب والوقد والوقود بمعنى الاتقاد.","what_is_not_ar":"لا يدخل الحطب نفسه ولا موضع النار ولا وقدة الصيف ولا استعارات الحرب والغضب والتلألؤ إلا بقرينة."},"support_links":["sup_dadcbdd89570b13bd2ab"]},{"boundary":"Dal yanmanın kendisini değil, ateşe malzeme olan yakacağı bildirir; ateş yeri ve sıcaklık anlamları kapsam dışıdır.","branch_kind":"bare","branch_ref":"root_001672/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُوقَدَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|(IV)|LEM:muwqadap|ROOT:wqd|F|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"104:6:3:2","qac_word_ref":"104:6:3","surface_ar":"مُوقَدَةُ"}],"gloss":"yakacak odun ve ateşlik yakıt","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Odun, ateşi yakmak ve beslemek üzere yakacak madde işlevi görür."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Anlam, odun dışında ateş için özellikle yakıt yapılmış yanıcı maddeyi de kapsayabilir."}}],"root_ar":"و ق د","root_id":"root_001672","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Odunun temel örnek olduğu, ancak ateşe yakıt yapılmış başka yanıcı maddelerin de kapsanabildiği genel karşılıktır.","boundary_detail":"Dal yanmanın kendisini değil, ateşe malzeme olan yakacağı bildirir; ateş yeri ve sıcaklık anlamları kapsam dışıdır.","branch_image_ar":"الحطب ومادة الوقود","concept_gloss":"yakacak odun ve ateşlik yakıt","contextual_glosses":[{"applicability":"Malzemenin açıkça odun olduğu ve ateş yakma amacı taşıdığı bağlamlarda en doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Odun dışındaki yakıt yapılmış yanıcı maddeleri kapsamaz.","preserves":"Odunun ateş için yakacak olmasını tam olarak korur."},"facet_ids":["F001"],"text":"yakacak odun","usage_role":"general"},{"applicability":"Maddenin türünden çok ateşi yakma veya sürdürme işlevinin önemli olduğu bağlamlarda kullanılır.","error_profile":{"adds":"Güncel kullanımda odun dışındaki çok çeşitli yakıt türlerini de düşündürebilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Ateşi besleyen yanıcı malzeme işlevini korur."},"facet_ids":["F001","F002"],"text":"ateşlik yakıt","usage_role":"contextual"}],"definition":"Ateşi yakmak veya yanmasını sürdürmek için hazırlanıp kullanılan odun ya da başka yanıcı maddedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Odun, ateşi yakmak ve beslemek üzere yakacak madde işlevi görür."},{"facet_id":"F002","role":"extension","statement":"Anlam, odun dışında ateş için özellikle yakıt yapılmış yanıcı maddeyi de kapsayabilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Malzeme yerine yanma olayını ve alevi bildirir.","collision":"Ateşin yanmasını anlatan root_001672/B001 ile karışır.","fit":"displacement","loses":"Yanıcı malzeme ve yakacak olma işlevini kaybeder.","preserves":"Yakıtın kullanıldığı temel alanı korur."},"text":"ateş"}],"identity_rationale":"Kaynak ifadesi, ateş için yakacak olarak kullanılan odunu ve yakıt yapılmış malzemeyi açıkça tanımlar. Dalın yakacak madde çerçevesi bu ortak anlamı doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"yakacak odun; ateş için hazırlanmış yakıt"}],"lexicalization_note":"Tanım yalın yakacak madde anlamına dayanır ve herhangi bir özel söz öbeğine ya da yanma eylemine bağlı değildir.","neighbor_coverage_note":"Bütün adaylar incelendi; yakacak odun, ateşe atılan madde ve yanma olayıyla en açıklayıcı sınırları kuran üç komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yakıt işlevini merkeze alır; komşu dal odunun kendisini ve onu elde etme, taşıma veya meslek edinme gibi ilişkili kullanımları daha geniş biçimde kapsar.","focus_only":"Odunu ve benzeri malzemeyi özellikle ateşin yakıtı olma işleviyle tanımlar.","gloss":"yakacak odun","neighbor_only":"Odun toplama, kesme, taşıma, odunculuk ve odunlu yer gibi geniş bir türev alanı da içerir.","neighbor_ref":"root_000335/B001","relation_type":"near_synonym","shared_zone":"İki dal da ateş yakmak üzere kullanılan odunu doğrudan kapsar."},{"boundary_match":"partial","distinction":"Bu dal nesneyi yakıt işlevine göre sınıflandırır; komşu dal ise nesnenin ateşe atılması ilişkisini öne çıkarır ve malzeme türünü daha açık bırakır.","focus_only":"Ateş için hazırlanmış yakacak maddeyi, temel olarak odunu bildirir.","gloss":"yakıt ile ateşe atılan madde","neighbor_only":"Odun olsun olmasın ateşe atılan veya ateşe fırlatılan şeyi bildirir.","neighbor_ref":"root_000325/B004","relation_type":"near_neighbor","shared_zone":"Ateşe atılan odun hem yakacak madde hem de ateşi besleyen nesne olabilir."},{"boundary_match":"field_only","distinction":"Bu dal sürece katılan malzemedir; komşu dal ise malzemenin içinde yer aldığı yanma ve yakma olayını bildirir.","focus_only":"Ateşin yanmasını sağlayan yakacak maddeyi adlandırır.","gloss":"yakıt ile yanma","neighbor_only":"Ateşin tutuşmasını, yanmasını ve yakılmasını olay olarak anlatır.","neighbor_ref":"root_001672/B001","relation_type":"same_field","shared_zone":"Yakıt, ateşin tutuşup yanması için kullanılan maddi girdidir."}],"source_phrase_ar":"الوقود الحطب (maqayis)؛ وقود النار أي حطبها (ayn)؛ الوقود بالفتح الحطب (sihah)؛ الوقود للحطب المجعول للوقود (mufradat)","source_summary":"Kaynaklar anlamı öncelikle ateşin odunu, yani yakacak odun olarak verir; daha genel anlatımda ateş için yakıt yapılmış malzeme de bu kapsama girer.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الحطب وما يجعل مادة لإيقاد النار، ومنه إطلاق الوقود على الناس والحجارة في النص المنقول.","what_is_not_ar":"لا يدخل فعل الاشتعال نفسه ولا موضع الموقد ولا الوقدة بمعنى شدة الحر."},"support_links":[]},{"boundary":"Burada adlandırılan şey ateşin kendisi ya da yakacak madde değil, ateşin yakıldığı veya bulunduğu yerdir.","branch_kind":"bare","branch_ref":"root_001672/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُوقَدَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|(IV)|LEM:muwqadap|ROOT:wqd|F|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"104:6:3:2","qac_word_ref":"104:6:3","surface_ar":"مُوقَدَةُ"}],"gloss":"ateş yakılan yer","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yer, içinde ateş bulunduğu ya da yakıldığı için ateş yeri olarak adlandırılır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı yer anlamı, ateş yakma eyleminden türemiş iki ayrı ad biçimiyle ifade edilir."}}],"root_ar":"و ق د","root_id":"root_001672","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli bir yapı türü belirtmeden, ateşin bulunduğu veya yakılması için ayrıldığı yeri karşılar.","boundary_detail":"Burada adlandırılan şey ateşin kendisi ya da yakacak madde değil, ateşin yakıldığı veya bulunduğu yerdir.","branch_image_ar":"موضع النار والموقد","concept_gloss":"ateş yakılan yer","contextual_glosses":[{"applicability":"Ateş yakılan yerin ev içindeki ya da düzenlenmiş bir ateşlik olduğu bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":"Yemek pişirme, aile, kurum veya maden gibi çağdaş yan anlamları düşündürebilir.","collision":"Bağlam verilmezse yer anlamı dışındaki yaygın ocak kullanımlarıyla karışabilir.","fit":"broadening","loses":null,"preserves":"Ateşin yakıldığı belirli yeri korur."},"facet_ids":["F001"],"text":"ocak","usage_role":"contextual"},{"applicability":"Ateşin güvenli biçimde yakılması için ayrılmış bölüm veya düzenek kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalnızca ateşin bulunduğu, özel olarak düzenlenmemiş yerleri dışarıda bırakabilir.","preserves":"Ateş yakmak için ayrılmış yer niteliğini korur."},"facet_ids":["F001"],"text":"ateşlik","usage_role":"contextual"}],"definition":"Ateşin yakıldığı, bulunduğu veya yanması için ayrılmış olan yerdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yer, içinde ateş bulunduğu ya da yakıldığı için ateş yeri olarak adlandırılır."},{"facet_id":"F002","role":"source_variant","statement":"Aynı yer anlamı, ateş yakma eyleminden türemiş iki ayrı ad biçimiyle ifade edilir."}],"identity_rationale":"Kaynak ifadesi iki yer adını doğrudan ateşin bulunduğu yer olarak açıklar. Dalın ateş yeri çerçevesi, eylemi veya yakıtı bu yer anlamına katmadan kaynağı karşılar.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ateş yakılan yer, ocak"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"ateşin bulunduğu veya yakıldığı yer"}],"lexicalization_note":"Tanım genel ateş yeri anlamını verir; onu belirli bir kap, yapı türü veya özel kullanımla sınırlandırmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; genel ateş yeri sınırını ocak, özel fırın ve yanma olayına karşı en iyi gösteren üç ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yalnızca yer ile ateş arasındaki ilişkiye dayanır; komşu dalın kapsamı belirli ocak kullanımından başka, ateş yeriyle ilgisiz adlandırmalara da uzanır.","focus_only":"Herhangi bir ateşin bulunduğu veya yakıldığı yeri genel olarak bildirir.","gloss":"ocak ve ateş yeri","neighbor_only":"Isınılan ocak yanında kış ayları ve ağır kişi gibi ayrı kullanımları da taşır.","neighbor_ref":"root_001324/B007","relation_type":"near_synonym","shared_zone":"İki dal da ateş yakılan ya da yanında ısınılan yeri ocak anlamında karşılayabilir."},{"boundary_match":"field_only","distinction":"Bu dal üst kavram niteliğinde bir ateş yeridir; komşu dal ise biçimi, yapımı ve pişirme işlevi belirlenmiş özel bir düzenektir.","focus_only":"Ateşin bulunduğu yeri yapı biçimini belirlemeden genel olarak adlandırır.","gloss":"ateş yeri ile kazılı fırın","neighbor_only":"Toprağa kazılmış ve içinde ekmek pişirilen fırın benzeri özel bir yapıyı bildirir.","neighbor_ref":"root_000708/B009","relation_type":"same_field","shared_zone":"Kazılı fırın da içinde ateş yakılan bir yer olduğu için iki alan somut olarak kesişir."},{"boundary_match":"field_only","distinction":"Bu dal olayın gerçekleştiği yerdir; komşu dal o yerde gerçekleşen yanma veya yakma sürecidir.","focus_only":"Ateşin yakıldığı veya bulunduğu mekansal konumu bildirir.","gloss":"ateş yeri ile yanma","neighbor_only":"Ateşin tutuşup yanmasını ve bir etken tarafından yakılmasını bildirir.","neighbor_ref":"root_001672/B001","relation_type":"same_field","shared_zone":"Yanma olayı çoğunlukla ateş için ayrılmış bir yerde gerçekleşir."}],"source_phrase_ar":"الموقد والمستوقد موضع النار (ayn)؛ الموضع موقد مثال مجلس (sihah)","source_summary":"Kaynakların ortak verdiği anlam ateşin bulunduğu veya yakıldığı yerdir; iki ayrı ad biçimi aynı yer kavramına bağlanır.","sources":["AY","SI"],"what_is_ar":"يدخل فيه اسم المكان الذي توقد فيه النار أو تكون فيه، مثل الموقد والمستوقد.","what_is_not_ar":"لا يدخل النار نفسها ولا الحطب ولا فعل الإيقاد."},"support_links":[]},{"boundary":"Anlam genel sıcaklık değil, özellikle yaz sıcağının en şiddetli düzeyi veya bu şiddetin sürdüğü sınırlı dönemdir.","branch_kind":"mixed_non_bare","branch_ref":"root_001672/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُوقَدَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|(IV)|LEM:muwqadap|ROOT:wqd|F|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"104:6:3:2","qac_word_ref":"104:6:3","surface_ar":"مُوقَدَةُ"}],"gloss":"yazın en şiddetli sıcağı ve sıcak dönemi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yaz sıcağı en yüksek ve en bunaltıcı şiddetine ulaşır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Şiddetli sıcak, on gün veya yarım ay süren belirli bir dönem olarak da yorumlanır."}}],"root_ar":"و ق د","root_id":"root_001672","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem sıcaklığın doruk şiddetini hem de bu şiddetle tanımlanan sınırlı yaz dönemini birlikte karşılar.","boundary_detail":"Anlam genel sıcaklık değil, özellikle yaz sıcağının en şiddetli düzeyi veya bu şiddetin sürdüğü sınırlı dönemdir.","branch_image_ar":"وقدة الصيف وشدة الحر","concept_gloss":"yazın en şiddetli sıcağı ve sıcak dönemi","contextual_glosses":[{"applicability":"Sürenin değil sıcaklığın doruk derecesinin vurgulandığı cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"On gün veya yarım ay süren dönem yorumunu dışarıda bırakır.","preserves":"Yaz sıcağının en yüksek şiddetini korur."},"facet_ids":["F001"],"text":"yazın en kavurucu sıcağı","usage_role":"general"},{"applicability":"Şiddetli sıcağın belirli bir süre devam eden dönem olarak ele alındığı bağlamlarda kullanılır.","error_profile":{"adds":"Yaz mevsimi bağlamda açık değilse başka mevsimlerdeki sıcak dönemleri de düşündürebilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Yoğun sıcağın süreli bir dönem oluşturmasını korur."},"facet_ids":["F002"],"text":"kavurucu sıcak dönemi","usage_role":"contextual"}],"definition":"Yazın ulaşılan en şiddetli sıcak veya bu yoğun sıcağın sürdüğü dönemdir. Dönem bazı aktarımlarda on gün ya da yarım ay olarak belirtilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yaz sıcağı en yüksek ve en bunaltıcı şiddetine ulaşır."},{"facet_id":"F002","role":"source_variant","statement":"Şiddetli sıcak, on gün veya yarım ay süren belirli bir dönem olarak da yorumlanır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Her derece ve mevsimdeki sıcaklığı kapsayarak yazın en şiddetli düzeyi sınırını aşar.","collision":"Genel sıcaklık bildiren çok sayıdaki kullanımla ayrımını yitirir.","fit":"broadening","loses":null,"preserves":"Yüksek ısı niteliğini genel düzeyde korur."},"text":"sıcak"}],"identity_rationale":"Kaynak ifadesi yazın en şiddetli sıcağını ortak çekirdek olarak verir ve bir aktarım bunu on gün ya da yarım ay süren sıcak dönem diye sınırlar. Dal çerçevesi hem şiddeti hem de dönem yorumunu korur.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"şiddetli sıcak; on gün ya da yarım ay süren sıcak dönem"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yazın en şiddetli sıcağı"}],"lexicalization_note":"Tanım, yalın biçimdeki şiddetli sıcak ya da sıcak dönem anlamıyla yazı açıkça belirten söz öbeğindeki en şiddetli yaz sıcağını ayrı tutar.","neighbor_coverage_note":"Tüm adaylar karşılaştırıldı; en şiddetli sıcak, sıcaklığın başlangıcı ve öğle sıcağı arasındaki sınırları gösteren üç komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yalnızca yaz sıcağına ve bazen onun süresine bağlıdır; komşu dal hem sıcak hem soğuk için kullanılabilen daha simetrik bir uç derece kavramıdır.","focus_only":"Yazın en şiddetli sıcağını ve bunun sürdüğü sınırlı dönemi bildirir.","gloss":"yazın doruk sıcağı","neighbor_only":"En şiddetli soğuğu ve kışın sertliğini de aynı uç derece çerçevesine alır.","neighbor_ref":"root_000884/B008","relation_type":"near_synonym","shared_zone":"İki dal da sıcaklığın sıradan düzeyi aşıp en şiddetli dereceye ulaşmasını anlatır."},{"boundary_match":"partial","distinction":"Bu dal doruk yaz sıcağına odaklanır; komşu dal sıcaklığın şiddeti yanında başlangıç evresini de gösterebildiği için sınırları tam örtüşmez.","focus_only":"Yazın en şiddetli sıcağını ve kimi aktarımda belirli bir sıcak dönemini bildirir.","gloss":"şiddetli yaz sıcağı","neighbor_only":"Sıcağın ilk başlamasını da anlam alanına alabilir.","neighbor_ref":"root_001142/B007","relation_type":"near_synonym","shared_zone":"Her iki dal sıcaklığın şiddetlendiği bir evreyi anlatabilir."},{"boundary_match":"partial","distinction":"Bu dal mevsim içindeki doruk şiddeti veya dönemi öne çıkarır; komşu dalın ayırt edici sınırı gün içindeki öğle vaktidir.","focus_only":"Yazın en şiddetli sıcağını, günün belli bir saatine bağlamadan bildirir.","gloss":"doruk sıcak ile öğle sıcağı","neighbor_only":"Şiddetli sıcağı özellikle gün ortası veya öğle vaktiyle ilişkilendirir.","neighbor_ref":"root_001226/B002","relation_type":"near_synonym","shared_zone":"Yazın gün ortasındaki kavurucu sıcak iki dalın da doğal olarak kesiştiği durumdur."}],"source_phrase_ar":"وقدة الصيف أشده حرا (maqayis;ayn;mufradat)؛ الوقدة أشد من الحر وهي عشرة أيام أو نصف شهر (sihah)","source_summary":"Ortak anlam yazın en şiddetli sıcağıdır; aktarımlar arasındaki ayrıntı, bunun yalnızca bir sıcaklık derecesi mi yoksa on gün ya da yarım ay süren bir dönem mi olduğundadır.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الوقدة بمعنى أشد حر الصيف أو مدة من الحر الشديد.","what_is_not_ar":"لا يدخل مطلق النار ولا الحطب ولا الموقد ولا استعارات الغضب والحرب."},"support_links":[]},{"boundary":"Bu dal genel bir şiddet veya hız anlamı değildir; hızlı tutuşma ve alevlenme imgesini taşıyan belirtilmiş kullanımlarla sınırlıdır.","branch_kind":"collocation","branch_ref":"root_001672/B005","candidate_links":[{"candidate_id":"cand_8ceb94f94ff2133d0248","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُوقَدَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|(IV)|LEM:muwqadap|ROOT:wqd|F|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"104:6:3:2","qac_word_ref":"104:6:3","surface_ar":"مُوقَدَةُ"}],"gloss":"ateş gibi hızla parlayıp şiddetlenme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ateş çıkarma çubuğu kıvılcımı kolay ve hızlı biçimde üretir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gönül, etkinlik ve kararlılıkta çabuk parlayan bir canlılığa sahip diye nitelenir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Öfke, ateşin alevlenmesine benzetilerek şiddetlenir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Savaşın başlaması veya körüklenmesi, ateş yakma imgesiyle anlatılır."}}],"root_ar":"و ق د","root_id":"root_001672","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Verilen söz öbeklerinde hızlı kıvılcım çıkarma, canlılık, öfke ve savaş kullanımlarını birleştiren açıklayıcı üst karşılıktır.","boundary_detail":"Bu dal genel bir şiddet veya hız anlamı değildir; hızlı tutuşma ve alevlenme imgesini taşıyan belirtilmiş kullanımlarla sınırlıdır.","branch_image_ar":"سرعة الاتقاد وفوران الشدة","concept_gloss":"ateş gibi hızla parlayıp şiddetlenme","contextual_glosses":[{"applicability":"Ateş çıkarma çubuğunun kolay ve hızlı biçimde kıvılcım üretmesini niteleyen kullanımda geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gönül, öfke ve savaşla ilgili mecazlı kullanımları dışarıda bırakır.","preserves":"Ateş çıkarma aracındaki hız ve kolaylığı korur."},"facet_ids":["F001"],"text":"çabuk kıvılcım çıkaran","usage_role":"contextual"},{"applicability":"Gönlün etkinlikte hızlı, enerjik ve kararında keskin oluşunu anlatan bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ateş çıkarma, öfke ve savaş kullanımlarını kapsamaz.","preserves":"Etkinlikte canlılık ve kararlılık nitelemesini korur."},"facet_ids":["F002"],"text":"canlı ve kararlı","usage_role":"contextual"},{"applicability":"Bir kişinin öfkesinin ateş gibi birden şiddetlendiği bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kıvılcım çıkarma, gönül canlılığı ve savaş kullanımlarını dışarıda bırakır.","preserves":"Öfkenin ateş imgesiyle hızlı biçimde şiddetlenmesini korur."},"facet_ids":["F003"],"text":"öfkeden parlamak","usage_role":"contextual"},{"applicability":"Savaşın ateş yakmaya benzetilerek başlatıldığı veya şiddetlendirildiği bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ateş çıkarma, gönül ve öfke kullanımlarını kapsamaz.","preserves":"Savaşı ateş gibi başlatma ve büyütme imgesini korur."},"facet_ids":["F004"],"text":"savaşı körüklemek","usage_role":"contextual"}],"definition":"Belirli kullanımlarda ateşin hızla tutuşması veya alevlenmesi imgesi, kıvılcım çıkarma kolaylığını, gönlün canlı ve kararlı oluşunu, öfkenin şiddetlenmesini ya da savaşın körüklenmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ateş çıkarma çubuğu kıvılcımı kolay ve hızlı biçimde üretir."},{"facet_id":"F002","role":"extension","statement":"Gönül, etkinlik ve kararlılıkta çabuk parlayan bir canlılığa sahip diye nitelenir."},{"facet_id":"F003","role":"associated_use","statement":"Öfke, ateşin alevlenmesine benzetilerek şiddetlenir."},{"facet_id":"F004","role":"associated_use","statement":"Savaşın başlaması veya körüklenmesi, ateş yakma imgesiyle anlatılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hızlı alevlenme imgesini, kıvılcım çıkarma, gönül ve savaş kullanımlarını kaybeder.","preserves":"Öfke durumunun ortaya çıkmasını korur."},"text":"öfkelenmek"}],"identity_rationale":"Kaynak ifadesi tek bir yalın anlam vermek yerine belirli söz öbeklerinde hızlı kıvılcım çıkarma, canlı ve kararlı olma, öfkeyle şiddetlenme ve savaşı ateş gibi düşünme kullanımlarını toplar. Dal korunabilir, ancak bunların yalnızca ateş imgesine dayalı ve söz öbeklerine bağlı olduğu açık tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"çabuk kıvılcım çıkaran ateş çubuğu"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"etkinlikte canlı ve kararlı gönül"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"öfkeden parladı, öfkesi şiddetlendi"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"savaşı başlattı veya körükledi"}],"lexicalization_note":"Tanım yalnızca verilen söz öbeklerine bağlıdır; kıvılcım çıkarma, gönül canlılığı, öfke ve savaş kullanımlarından yalın bir genel anlam türetilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; öfke ve savaş şiddetiyle gerçek ateş arasındaki sınırı en açık kuran üç komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın birleştirici imgesi ateşin hızla tutuşmasıdır ve yalnızca belirtilmiş kullanımlarda görülür; komşu dal daha genel bir sıçrayış ve taşkın şiddet alanına sahiptir.","focus_only":"Ateş imgesine bağlı hızlı kıvılcım, gönül canlılığı, öfke ve savaş kullanımlarını birleştirir.","gloss":"alevlenerek şiddetlenme","neighbor_only":"Sıçrama ve yükselme imgesiyle içki sertliği, saldırı ve başka şiddet türlerini de kapsar.","neighbor_ref":"root_000758/B001","relation_type":"near_synonym","shared_zone":"Öfkenin veya savaşın birden yükselip şiddetlenmesi iki dalda da anlatılabilir."},{"boundary_match":"partial","distinction":"Bu dal öfkeyi ateş gibi parlayan bir şiddet olarak sunar; komşu dalın çekirdeği ateş imgesinden bağımsız biçimde kabarma, hareketlenme ve taşmadır.","focus_only":"Şiddetlenmeyi ateşin tutuşması ve alevlenmesi imgesiyle sınırlar.","gloss":"parlama ile kabarma","neighbor_only":"Canlı, kan, istek veya başka bir varlığın harekete geçmesi ve kabarması gibi daha geniş süreçleri kapsar.","neighbor_ref":"root_001612/B002","relation_type":"near_synonym","shared_zone":"Öfkenin harekete geçip şiddetlenmesi her iki dalın ortak kullanım alanıdır."},{"boundary_match":"partial","distinction":"Bu dal ateş davranışını başka alanlara taşıyan sınırlı kullanımlardır; komşu dal gerçek yanma ve yakma olayının kendisidir.","focus_only":"Hızlı tutuşma imgesini araç, gönül, öfke ve savaş için söz öbeklerine bağlı olarak aktarır.","gloss":"mecazlı parlama ile gerçek ateş","neighbor_only":"Gerçek ateşin tutuşmasını, yanmasını, yakılmasını ve görünen alevini bildirir.","neighbor_ref":"root_001672/B001","relation_type":"near_neighbor","shared_zone":"İki dalın ortak imgesi ateşin tutuşması ve şiddetli biçimde alevlenmesidir."}],"source_phrase_ar":"زند ميقاد سريع الوري وقلب وقاد سريع التوقد في النشاط والمضاء (ayn)؛ اتقد فلان غضبا (mufradat)؛ يستعار وقد واتقد للحرب كاستعارة النار والاشتعال (mufradat)","source_summary":"Toplanan kullanımları birleştiren unsur hızlı tutuşma ve alevlenme imgesidir: ateş çıkarma aracında kolay kıvılcım, gönülde canlılık ve kararlılık, öfkede şiddetlenme, savaşta ise başlatma veya körükleme anlatılır.","sources":["AY","MU"],"what_is_ar":"يدخل فيه سرعة الوري في الزند، وسرعة التوقد في القلب والنشاط والمضاء، واستعارة الاتقاد للغضب والحرب.","what_is_not_ar":"لا يدخل لمعان الجواهر والذهب والحافر إلا إذا قصدت صورة التوقد العامة، ولا يدخل الحطب أو موضع النار."},"support_links":["sup_6f4b2f40989ea0a0f51e"]},{"boundary":"Burada gerçek yanma yoktur; nesnenin ışığı, ateşin parlak ve titreşen görünümüne benzetilerek anlatılır.","branch_kind":"collocation","branch_ref":"root_001672/B006","candidate_links":[{"candidate_id":"cand_b34261ce72c71c448c83","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُوقَدَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|(IV)|LEM:muwqadap|ROOT:wqd|F|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"104:6:3:2","qac_word_ref":"104:6:3","surface_ar":"مُوقَدَةُ"}],"gloss":"ateş gibi ışıldamak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne, ateşin parlak yanışını andıran canlı ve titreşen bir ışıltı verir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Toynağın küçük parıltısı ışıldayarak görünür hâle gelir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Mücevher ve altın, ateş gibi parlayan nesneler olarak nitelenir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Aynı ışıldama görüntüsü uygun başka nesneler için de kullanılabilir."}}],"root_ar":"و ق د","root_id":"root_001672","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesnenin gerçek anlamda yanmadan, ateşin canlı parıltısını andıran bir ışık verdiği kullanımların çekirdek karşılığıdır.","boundary_detail":"Burada gerçek yanma yoktur; nesnenin ışığı, ateşin parlak ve titreşen görünümüne benzetilerek anlatılır.","branch_image_ar":"تلألؤ كاتقاد النار","concept_gloss":"ateş gibi ışıldamak","contextual_glosses":[{"applicability":"Ateş benzetisinin bağlamdan anlaşılabildiği, nesnenin canlı bir ışık verdiği cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":"Genel parlama fiilleriyle biçimsel ayrımı azalabilir.","fit":"narrowing","loses":"Ateşin yanışına yapılan özel benzetiyi açıkça söylemez.","preserves":"Nesnenin görünür ve canlı bir ışık vermesini korur."},"facet_ids":["F001","F004"],"text":"parıldamak","usage_role":"general"},{"applicability":"Toynağın küçük parıltısının belirgin biçimde göründüğü özel kullanımda geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Mücevher, altın ve diğer nesnelerdeki kullanımları dışarıda bırakır.","preserves":"Toynak parıltısı örneğini doğrudan korur."},"facet_ids":["F002"],"text":"toynağı ışıldamak","usage_role":"contextual"},{"applicability":"Mücevher veya altının canlı, noktasal ve göz alıcı parıltısının anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Toynak ve başka nesnelerdeki geniş kullanım alanını kapsamaz.","preserves":"Mücevher ve altının güçlü ışıltısını korur."},"facet_ids":["F003"],"text":"mücevher gibi ışıl ışıl olmak","usage_role":"contextual"}],"definition":"Bir nesnenin yüzeyi veya küçük ışık noktaları, ateş yanıyormuş gibi canlı biçimde parlar ve ışıldar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne, ateşin parlak yanışını andıran canlı ve titreşen bir ışıltı verir."},{"facet_id":"F002","role":"example","statement":"Toynağın küçük parıltısı ışıldayarak görünür hâle gelir."},{"facet_id":"F003","role":"example","statement":"Mücevher ve altın, ateş gibi parlayan nesneler olarak nitelenir."},{"facet_id":"F004","role":"extension","statement":"Aynı ışıldama görüntüsü uygun başka nesneler için de kullanılabilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Nesnenin gerçekten ateş aldığı anlamını getirir.","collision":"Gerçek ateşin yanmasını anlatan root_001672/B001 ile karışır.","fit":"displacement","loses":"Nesnenin yalnızca ışıldadığı ve gerçek yanmanın bulunmadığı sınırını kaybeder.","preserves":"Ateşin parlak görünümüyle kurulan imgesel bağı korur."},"text":"yanmak"}],"identity_rationale":"Kaynak ifadesi, toynak parıltısını ve mücevher ile altının ışıldamasını ateşin parlak yanışına benzetir; ayrıca kullanımın başka nesnelere uzanabildiğini belirtir. Dalın ateş gibi ışıldama çerçevesi bu kapsamı doğru verir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"toynağın küçük parıltısı ışıldadı"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"mücevher ve altın ateş gibi ışıldadı"}],"lexicalization_note":"Tanım yalnızca nesne adlarıyla kurulan belirtilmiş kullanımlara bağlıdır; buradan yalın bir yanma veya genel parlaklık anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; mücevher ışıltısı, genel parlama ve gerçek yanma ile sınırı en açık gösteren üç komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Mücevher bağlamında karşılıklar çok yakındır; bu dalın ayırt edici yanı ateş benzetisi ve toynak dâhil başka nesnelere uzanan kapsamıdır.","focus_only":"Toynak ve başka nesneleri de ateş gibi ışıldayan varlıklar olarak kapsayabilir.","gloss":"mücevherin ışıldaması","neighbor_only":"Işıldamayı özellikle mücevherin kendi parlaklığı çevresinde sınırlar.","neighbor_ref":"root_001686/B002","relation_type":"near_synonym","shared_zone":"Mücevherin canlı biçimde parlayıp ışıldaması iki dalda da aynı durumu anlatır."},{"boundary_match":"partial","distinction":"Bu dal ateş gibi ışıldama görüntüsüne dayanır; komşu dal ışığın kaynağı ve benzetisi bakımından daha geniş bir genel parlama alanıdır.","focus_only":"Parlaklığı ateşin yanış görünümüne benzetir ve belirli nesne kullanımlarına bağlıdır.","gloss":"ışıldama ve parlama","neighbor_only":"Şimşek, silah, yüz ve yağlı yiyecek gibi çok çeşitli parlama türlerini, ayrıca parlatma işlemini kapsar.","neighbor_ref":"root_000108/B001","relation_type":"near_synonym","shared_zone":"Bir nesnenin yüzeyinden belirgin ve göz alıcı ışık gelmesi iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Bu dal görsel benzerliğe dayanan ışıldamadır; komşu dal gerçek ısı, yanma ve alev sürecidir.","focus_only":"Yanmayan nesnenin parıltısını ateşin görünümüne benzetir.","gloss":"ateş gibi ışık ile gerçek yanma","neighbor_only":"Ateşin gerçekten tutuşmasını, yanmasını, yakılmasını ve oluşan alevi bildirir.","neighbor_ref":"root_001672/B001","relation_type":"near_neighbor","shared_zone":"Canlı, titreşen ve alevi andıran parlak görünüm iki dal arasında imgesel bağ kurar."}],"source_phrase_ar":"وقد الحافر إذا تلألأ بصيصه وفي كل شيء (ayn)؛ يستعار ذلك للتلألؤ فيقال اتقد الجوهر والذهب (mufradat)","source_summary":"Kaynaklar ateşin yanış görünümünü nesne parıltısına aktarır: toynağın küçük ışığı, mücevher ve altının ışıltısı başlıca örneklerdir; kullanım uygun başka nesnelere de uzanabilir.","sources":["AY","MU"],"what_is_ar":"يدخل فيه لمعان الشيء وتلألؤه كالحافر والجوهر والذهب، استعارة من اتقاد النار.","what_is_not_ar":"لا يدخل شدة الحر ولا فوران الغضب والحرب إلا من جهة الاستعارة العامة."},"support_links":["sup_57fc7c6145607013864d"]}],"candidate_inventory":[{"anchor_refs":["104:6:1"],"branch_refs":[],"candidate_id":"cand_f1c265ecb7159ae6f927","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001564"],"scope":"focus_ayah","source_local_id":"104:6:1:divine-idafa-fire","source_type":"word_analysis","support_ids":["sup_e859da0502fb89e8cb3f","sup_eb7c6ad6f9dd7d9a6896"],"title":"the construct makes the fire specified","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:6:1","qac_refs":["104:6:1:1"],"status":"accepted"}},{"anchor_refs":["104:6:1"],"branch_refs":[],"candidate_id":"cand_f873711fbb7570fe2179","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001564"],"scope":"focus_ayah","source_local_id":"104:6:1:fire-light-exposure","source_type":"word_analysis","support_ids":["sup_ac2b24b4874af463217f","sup_eb7c6ad6f9dd7d9a6896"],"title":"fire keeps a light-field pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:6:1","qac_refs":["104:6:1:1"],"status":"accepted"}},{"anchor_refs":["104:6:1"],"branch_refs":[],"candidate_id":"cand_f1ea395cdec2092636d6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001564"],"scope":"focus_ayah","source_local_id":"104:6:1:kindled-fire-pairing","source_type":"word_analysis","support_ids":["sup_bad7d620a41e370ff8f8","sup_eb7c6ad6f9dd7d9a6896"],"title":"fire is paired with ignition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:6:1","qac_refs":["104:6:1:1"],"status":"accepted"}},{"anchor_refs":["104:6:1"],"branch_refs":[],"candidate_id":"cand_c881ab50d4f129de5599","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001564"],"scope":"focus_ayah","source_local_id":"104:6:1:predicate-answer","source_type":"word_analysis","support_ids":["sup_30a4f3d4a6513fdb15c6","sup_eb7c6ad6f9dd7d9a6896"],"title":"the answer begins as a predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:6:1","qac_refs":["104:6:1:1"],"status":"accepted"}},{"anchor_refs":["104:6:2"],"branch_refs":[],"candidate_id":"cand_1193267304eed548ea55","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:6:2:derivational-orientation","source_type":"word_analysis","support_ids":["sup_0ed3e5d373bd43ad7a2c","sup_278fb2b7bd101a31b384"],"title":"need and devotion color the name","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:6:2","qac_refs":["104:6:2:1"],"status":"accepted"}},{"anchor_refs":["104:6:2"],"branch_refs":[],"candidate_id":"cand_ce37ac36aecb8b79fa16","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:6:2:genitive-construct-completion","source_type":"word_analysis","support_ids":["sup_0ed3e5d373bd43ad7a2c","sup_b19d3d2f7dd2edd034f4"],"title":"the divine name completes the construct","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:6:2","qac_refs":["104:6:2:1"],"status":"accepted"}},{"anchor_refs":["104:6:2"],"branch_refs":[],"candidate_id":"cand_aacfeea9a5fac1446353","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:6:2:middle-hinge","source_type":"word_analysis","support_ids":["sup_0ed3e5d373bd43ad7a2c","sup_42ed627a8518a9004b38"],"title":"the middle word routes the definition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:6:2","qac_refs":["104:6:2:1"],"status":"accepted"}},{"anchor_refs":["104:6:2"],"branch_refs":[],"candidate_id":"cand_ef88d4bfcb24ab9d6a9f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:6:2:possession-agent-split","source_type":"word_analysis","support_ids":["sup_0ed3e5d373bd43ad7a2c","sup_70d8582551042fa66240"],"title":"attribution is explicit, agency is withheld","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:6:2","qac_refs":["104:6:2:1"],"status":"accepted"}},{"anchor_refs":["104:6:2"],"branch_refs":[],"candidate_id":"cand_b245340b6144a2ac14f3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:6:2:proper-name-domain","source_type":"word_analysis","support_ids":["sup_0ed3e5d373bd43ad7a2c","sup_7bdb0f35080e1429b366"],"title":"the proper name frames the fire","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:6:2","qac_refs":["104:6:2:1"],"status":"accepted"}},{"anchor_refs":["104:6:2"],"branch_refs":[],"candidate_id":"cand_3cdbc23d39c36298853d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:6:2:sound-and-form-binding","source_type":"word_analysis","support_ids":["sup_0ed3e5d373bd43ad7a2c","sup_a4a40ec6ed43238c7498"],"title":"recitation binds name and state","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:6:2","qac_refs":["104:6:2:1"],"status":"accepted"}},{"anchor_refs":["104:6:3"],"branch_refs":[],"candidate_id":"cand_9e031fcddf967344832f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001672"],"scope":"focus_ayah","source_local_id":"104:6:3:adjective-agreement","source_type":"word_analysis","support_ids":["sup_062dc2497481698aff58","sup_6271d0fc138dabbed428"],"title":"the adjective belongs to the fire","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:6:3","qac_refs":["104:6:3:1","104:6:3:2"],"status":"accepted"}},{"anchor_refs":["104:6:3"],"branch_refs":[],"candidate_id":"cand_141f0f17727afa21cb1f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001672"],"scope":"focus_ayah","source_local_id":"104:6:3:closure-state","source_type":"word_analysis","support_ids":["sup_55b8dc53e636e3fed760","sup_6271d0fc138dabbed428"],"title":"the verse lands on state","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:6:3","qac_refs":["104:6:3:1","104:6:3:2"],"status":"accepted"}},{"anchor_refs":["104:6:3"],"branch_refs":[],"candidate_id":"cand_ab6432b8a340badf15a7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001672"],"scope":"focus_ayah","source_local_id":"104:6:3:ignition-not-fuel","source_type":"word_analysis","support_ids":["sup_3c808f78a354f1ce8bb8","sup_6271d0fc138dabbed428"],"title":"ignition is selected over fuel","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:6:3","qac_refs":["104:6:3:1","104:6:3:2"],"status":"accepted"}},{"anchor_refs":["104:6:3"],"branch_refs":[],"candidate_id":"cand_595e07924dec47da9b3c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001672"],"scope":"focus_ayah","source_local_id":"104:6:3:inner-intensification","source_type":"word_analysis","support_ids":["sup_6271d0fc138dabbed428","sup_e081f925c827fcf536fd"],"title":"kindling presses inward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:6:3","qac_refs":["104:6:3:1","104:6:3:2"],"status":"accepted"}},{"anchor_refs":["104:6:3"],"branch_refs":[],"candidate_id":"cand_b79cc50c3e46b8be33de","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001672"],"scope":"focus_ayah","source_local_id":"104:6:3:intertext-agency-contrast","source_type":"word_analysis","support_ids":["sup_2dec301229784c5da0d4","sup_6271d0fc138dabbed428"],"title":"other kindling scenes sharpen this one","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:6:3","qac_refs":["104:6:3:1","104:6:3:2"],"status":"accepted"}},{"anchor_refs":["104:6:3"],"branch_refs":[],"candidate_id":"cand_7fa1b35d6b8408185d98","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001672"],"scope":"focus_ayah","source_local_id":"104:6:3:local-cluster","source_type":"word_analysis","support_ids":["sup_6271d0fc138dabbed428","sup_6967c29db568a792a829"],"title":"kindling locks into the local cluster","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:6:3","qac_refs":["104:6:3:1","104:6:3:2"],"status":"accepted"}},{"anchor_refs":["104:6:3"],"branch_refs":[],"candidate_id":"cand_1d3d5a0f53568c45ed14","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001672"],"scope":"focus_ayah","source_local_id":"104:6:3:passive-causative-result","source_type":"word_analysis","support_ids":["sup_6271d0fc138dabbed428","sup_9a8668365522d92facb7"],"title":"the form foregrounds completed kindling","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:6:3","qac_refs":["104:6:3:1","104:6:3:2"],"status":"accepted"}},{"anchor_refs":["104:6:3"],"branch_refs":[],"candidate_id":"cand_b3e8614faacf24839440","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001672"],"scope":"focus_ayah","source_local_id":"104:6:3:sequence-hinge","source_type":"word_analysis","support_ids":["sup_54b40ee36583ff052b54","sup_6271d0fc138dabbed428"],"title":"ignition connects crushing and rising","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:6:3","qac_refs":["104:6:3:1","104:6:3:2"],"status":"accepted"}},{"anchor_refs":["104:6:3"],"branch_refs":[],"candidate_id":"cand_d92fbf9d468abf9c72de","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001672"],"scope":"focus_ayah","source_local_id":"104:6:3:sound-impact","source_type":"word_analysis","support_ids":["sup_10d43c6c0d1c3727f807","sup_6271d0fc138dabbed428"],"title":"the root sounds harden the close","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:6:3","qac_refs":["104:6:3:1","104:6:3:2"],"status":"accepted"}},{"anchor_refs":["104:6:1"],"branch_refs":[],"candidate_id":"cand_fa58f0aded5217fc89e0","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001564"],"scope":"focus_ayah","source_local_id":"104:6:1:1","source_type":"qac_morpheme","support_ids":["sup_bae59b73d175b664b9d5"],"title":"QAC root occurrence: ن و ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["104:6:2"],"branch_refs":[],"candidate_id":"cand_c8e4d6a4299939df96e9","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000047"],"scope":"focus_ayah","source_local_id":"104:6:2:1","source_type":"qac_morpheme","support_ids":["sup_74d66f9fc897239f95a0"],"title":"QAC root occurrence: ء ل ه","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["104:6:3"],"branch_refs":[],"candidate_id":"cand_a1473075e91c6f327436","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001672"],"scope":"focus_ayah","source_local_id":"104:6:3:2","source_type":"qac_morpheme","support_ids":["sup_0cf8c033da6f855ccbf8"],"title":"QAC root occurrence: و ق د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["104:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:6","branch_refs":["root_000047/B002","root_001564/B002","root_001672/B001"],"candidate_id":"cand_de2ce7935b024670a5dc","commentary_obligation":"review","hft_ref":"hft_791013420d2a07a4876b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_kindled_divine_fire","source_type":"hft","support_ids":["sup_dadcbdd89570b13bd2ab"],"title":"baseline_kindled_divine_fire","trust":"legacy_unbound"},{"anchor_refs":["104:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:6","branch_refs":["root_000047/B002","root_001564/B001","root_001564/B002","root_001672/B006"],"candidate_id":"cand_b34261ce72c71c448c83","commentary_obligation":"review","hft_ref":"hft_77c3efe313e96e57d0e4","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_revelatory_brand","source_type":"hft","support_ids":["sup_57fc7c6145607013864d"],"title":"baseline_revelatory_brand","trust":"legacy_unbound"},{"anchor_refs":["104:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:6","branch_refs":["root_000047/B002","root_001564/B007","root_001672/B005"],"candidate_id":"cand_8ceb94f94ff2133d0248","commentary_obligation":"review","hft_ref":"hft_895015ed63b4651e90e4","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_relational_flare","source_type":"hft","support_ids":["sup_6f4b2f40989ea0a0f51e"],"title":"baseline_relational_flare","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"نَارُ ٱللَّهِ ٱلْمُوقَدَةُ","qac_morphemes":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:6:1:1","qac_word_ref":"104:6:1","root_ar":"ن و ر","surface_ar":"نَارُ"},{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"104:6:2:1","qac_word_ref":"104:6:2","root_ar":"ء ل ه","surface_ar":"ٱللَّهِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"104:6:3:1","qac_word_ref":"104:6:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"مُوقَدَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|(IV)|LEM:muwqadap|ROOT:wqd|F|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"104:6:3:2","qac_word_ref":"104:6:3","root_ar":"و ق د","surface_ar":"مُوقَدَةُ"}],"word_analysis_qac_refs":[["104:6:1:1"],["104:6:2:1"],["104:6:3:1","104:6:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["104:6:1","104:6:2","104:6:3"]},"focus_surface_evidence":{"arabic_uthmani":"نَارُ ٱللَّهِ ٱلْمُوقَدَةُ","qac_morphemes":[{"lemma_ar":"نَار","morph_features":"STEM|POS:N|LEM:naAr|ROOT:nwr|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:6:1:1","qac_word_ref":"104:6:1","root_ar":"ن و ر","surface_ar":"نَارُ"},{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"104:6:2:1","qac_word_ref":"104:6:2","root_ar":"ء ل ه","surface_ar":"ٱللَّهِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"104:6:3:1","qac_word_ref":"104:6:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"مُوقَدَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|(IV)|LEM:muwqadap|ROOT:wqd|F|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"104:6:3:2","qac_word_ref":"104:6:3","root_ar":"و ق د","surface_ar":"مُوقَدَةُ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["104:6:1:1"],["104:6:2:1"],["104:6:3:1","104:6:3:2"]],"word_analysis_refs":["104:6:1","104:6:2","104:6:3"],"word_rows":[{"analysis_record_ref":"104:6:1","analytic_gloss_range_en":"concrete fire as the predicate answer; definite through divine iḍāfa and locally colored by the root family's light/exposure field","analytic_root_gloss_range_en":"fire, burning, illumination, visible marking, and related light branches; only the fire noun is locally selected, while illumination remains a narrowed root-family pressure","qac_refs":["104:6:1:1"],"root":{"arabic":"ن و ر","transliteration":"n-w-r"},"surface":{"arabic":"نَارُ","transliteration":"nāru"}},{"analysis_record_ref":"104:6:2","analytic_gloss_range_en":"proper divine name in genitive case as the required second term of the fire construct","analytic_root_gloss_range_en":"proper divine name with supplied derivational evidence around worship, devotion, refuge, bewilderment, and need; no V4 guardrail rows are available for this root","qac_refs":["104:6:2:1"],"root":{"arabic":"أ ل ه","transliteration":"ʾ-l-h"},"surface":{"arabic":"ٱللَّهِ","transliteration":"Allāhi"}},{"analysis_record_ref":"104:6:3","analytic_gloss_range_en":"the definite feminine passive participle describing the divine-attributed fire as already caused-to-be-kindled","analytic_root_gloss_range_en":"kindling, ignition, fuel, hearth, fierce heat, flare of intensity, and gleam; the local form selects the passive result of causative ignition, not fuel or a place of fire","qac_refs":["104:6:3:1","104:6:3:2"],"root":{"arabic":"و ق د","transliteration":"w-q-d"},"surface":{"arabic":"ٱلْمُوقَدَةُ","transliteration":"al-mūqadah"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["104:6"],"branch_refs":["root_000047/B002","root_001564/B002","root_001672/B001"],"candidate_id":"cand_de2ce7935b024670a5dc","evidence_scope":"focus_ayah","hft_ref":"hft_791013420d2a07a4876b","item_id":"baseline_kindled_divine_fire","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_kindled_divine_fire","support_id":"sup_dadcbdd89570b13bd2ab"},{"anchor_refs":["104:6"],"branch_refs":["root_000047/B002","root_001564/B001","root_001564/B002","root_001672/B006"],"candidate_id":"cand_b34261ce72c71c448c83","evidence_scope":"focus_ayah","hft_ref":"hft_77c3efe313e96e57d0e4","item_id":"baseline_revelatory_brand","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_revelatory_brand","support_id":"sup_57fc7c6145607013864d"},{"anchor_refs":["104:6"],"branch_refs":["root_000047/B002","root_001564/B007","root_001672/B005"],"candidate_id":"cand_8ceb94f94ff2133d0248","evidence_scope":"focus_ayah","hft_ref":"hft_895015ed63b4651e90e4","item_id":"baseline_relational_flare","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_relational_flare","support_id":"sup_6f4b2f40989ea0a0f51e"}],"diagnostics":[],"lane_counts":{"global":10,"macro":10,"micro":3},"packet_summary":{"ayah_count":9,"focus_ref":"104:6","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"و ص د","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000036","furuq_root_norm":"ء ص د","furuq_source_root_norm":"أ ص د","is_dominant":true,"target_occurrences":2,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001653","furuq_root_norm":"و ص د","furuq_source_root_norm":"و ص د","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["104:1","104:2","104:3","104:4","104:5","104:6","104:7","104:8","104:9"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"104:6","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":13,"unstructured_record_count":0},"identity":{"ayah_ref":"104:6","lane":"micro","linguistic_source_ref":"104:6","surface_ref":"104:6","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"104:6","target_tokens":[["Allah'ın",["104:6:2"]],["tutuşturulmuş",["104:6:3"]],["ateşidir",["104:6:1"]]],"text":"Allah'ın tutuşturulmuş ateşidir."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":9,"id":"s104-p01-001-009","label":"Whole surah","number":1,"refs":["104:1","104:2","104:3","104:4","104:5","104:6","104:7","104:8","104:9"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:6:3:adjective-agreement","source_type":"word_analysis","support_id":"sup_062dc2497481698aff58","text":"{\"blocking_evidence\":null,\"headline\":\"the adjective belongs to the fire\",\"reader_payoff\":\"The reader notices that {{ar:ٱلْمُوقَدَةُ}} ({{tr:al-mūqadah}}) reaches back over the genitive name to qualify the fire itself.\",\"reason\":\"QAC and attachment evidence identify {{ar:ٱلْمُوقَدَةُ}} ({{tr:al-mūqadah}}) as a definite feminine nominative adjective modifying {{ar:نَارُ}} ({{tr:nāru}}), not the genitive divine name.\",\"representative_source_ids\":[\"QG-9959bf83\",\"QG-9bd3def4\",\"QF-a15c7c32\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"104:6:3:2","source_type":"qac_morpheme","support_id":"sup_0cf8c033da6f855ccbf8","text":"{\"lemma_ar\":\"مُوقَدَة\",\"morph_features\":\"STEM|POS:ADJ|PASS|PCPL|(IV)|LEM:muwqadap|ROOT:wqd|F|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"ADJ\",\"qac_ref\":\"104:6:3:2\",\"qac_word_ref\":\"104:6:3\",\"root_ar\":\"و ق د\",\"surface_ar\":\"مُوقَدَةُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:6:2","source_type":"word_analysis","support_id":"sup_0ed3e5d373bd43ad7a2c","text":"{\"gloss_range\":\"proper divine name in genitive case as the required second term of the fire construct\",\"prose\":\"{{ar:ٱللَّهِ}} ({{tr:Allāhi}}) is not a detached title in the middle of the ayah. Its final genitive case binds it as the second term of {{ar:نَارُ ٱللَّهِ}} ({{tr:nāru llāhi}}), so the fire is made specific by divine attribution before the final adjective arrives. That middle position matters: the name completes the construct, then {{ar:ٱلْمُوقَدَةُ}} ({{tr:al-mūqadah}}) reaches back to describe the fire, not the genitive name. The phrase therefore keeps two roles distinct: divine ownership, source, or jurisdiction is explicit, while the kindling agent remains withheld by the passive participle. The supplied derivational dispute around the divine name can add orientation, refuge-seeking, devotion, and needful bewilderment, even the concrete image of yearning dependence, but the local grammar keeps the word as the proper divine name in a construct, not a common noun. In the three-word architecture, {{ar:ٱللَّهِ}} ({{tr:Allāhi}}) is the hinge that turns fire plus kindled state into a divine-attributed definition, and the repeated l-sound with liaison into {{ar:ٱلْمُوقَدَةُ}} ({{tr:al-mūqadah}}) lets that hinge be heard as well as parsed.\",\"root_display\":\"{{ar:أ ل ه}} ({{tr:ʾ-l-h}})\",\"root_gloss_range\":\"proper divine name with supplied derivational evidence around worship, devotion, refuge, bewilderment, and need; no V4 guardrail rows are available for this root\",\"surface_display\":\"{{ar:ٱللَّهِ}} ({{tr:Allāhi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:6:3:sound-impact","source_type":"word_analysis","support_id":"sup_10d43c6c0d1c3727f807","text":"{\"blocking_evidence\":null,\"headline\":\"the root sounds harden the close\",\"reader_payoff\":\"The reader notices that the qāf-dāl stop texture gives the closing ignition word a hard impact matching its activated-fire image.\",\"reason\":\"The observation is phonetic and locally surface-based; it is retained as a small sound payoff, not as independent semantic proof.\",\"representative_source_ids\":[\"QP-84775b05\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:6:2:derivational-orientation","source_type":"word_analysis","support_id":"sup_278fb2b7bd101a31b384","text":"{\"blocking_evidence\":null,\"headline\":\"need and devotion color the name\",\"reader_payoff\":\"The reader notices that supplied derivational evidence lets devotion, refuge-seeking, and bewildered need sharpen the divine-name attachment without replacing the local proper-name function.\",\"reason\":\"No V4 rows are available for {{ar:أ ل ه}} ({{tr:ʾ-l-h}}), so the supplied CRITICAL dispute is not contradicted; the narrowing keeps it as semantic pressure around the proper name rather than a new local gloss.\",\"representative_source_ids\":[\"QS-985037ee\",\"QS-c40f5a1d\",\"QS-dff09789\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:6:3:intertext-agency-contrast","source_type":"word_analysis","support_id":"sup_2dec301229784c5da0d4","text":"{\"blocking_evidence\":null,\"headline\":\"other kindling scenes sharpen this one\",\"reader_payoff\":\"The reader notices the contrast with 2:17, 5:64, and 24:35: this ayah gives no human seeker, no extinguished human war-fire, and no lamp image, only a passive already-kindled fire.\",\"reason\":\"The CRITICAL rows supply concrete references for w-q-d echoes; they survive as contrastive parallels because they illuminate agency and form choice without overriding the local passive participle.\",\"representative_source_ids\":[\"QI-0cb82cf7\",\"QE-263216c1\",\"QE-2e098ea8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:6:1:predicate-answer","source_type":"word_analysis","support_id":"sup_30a4f3d4a6513fdb15c6","text":"{\"blocking_evidence\":null,\"headline\":\"the answer begins as a predicate\",\"reader_payoff\":\"The reader notices that {{ar:نَارُ}} ({{tr:nāru}}) fills the answer-slot opened by the prior question about {{ar:ٱلْحُطَمَةُ}} ({{tr:al-ḥuṭamah}}) (104:5), making the ayah definitional rather than episodic.\",\"reason\":\"QAC identifies {{ar:نَارُ}} ({{tr:nāru}}) as a nominative predicate of the implied subject from 104:5, and the translation support warns that the verse answers the preceding question.\",\"representative_source_ids\":[\"QG-ade3fdef\",\"QI-5abfaf38\",\"QT-adc2d3b5\",\"QE-458fbb7f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:6:3:ignition-not-fuel","source_type":"word_analysis","support_id":"sup_3c808f78a354f1ce8bb8","text":"{\"blocking_evidence\":null,\"headline\":\"ignition is selected over fuel\",\"reader_payoff\":\"The reader notices that the word marks activated ignition, while nearby root-family alternatives like fuel, seeking fire, and hearth remain contrasts rather than the local sense.\",\"reason\":\"V4 accepts branches for kindling, fuel, hearth, fierce heat, flare, and gleam under {{ar:و ق د}} ({{tr:w-q-d}}), but the local passive participle adjective selects the caused-kindled state, so the other branches serve as contrastive range.\",\"representative_source_ids\":[\"QS-0faf6aba\",\"QS-0fd6b924\",\"QS-2a87ec2f\",\"QS-a4038132\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:6:2:middle-hinge","source_type":"word_analysis","support_id":"sup_42ed627a8518a9004b38","text":"{\"blocking_evidence\":null,\"headline\":\"the middle word routes the definition\",\"reader_payoff\":\"The reader notices the sequence substance, possessor, state: the divine name in the middle routes the final kindled condition through divine attribution.\",\"reason\":\"The local word order places {{ar:ٱللَّهِ}} ({{tr:Allāhi}}) between the construct head and its post-iḍāfa adjective, while agreement assigns the adjective back to {{ar:نَارُ}} ({{tr:nāru}}).\",\"representative_source_ids\":[\"QG-126ea3e0\",\"QT-18237be3\",\"QT-898ad7a0\",\"QI-e8176d73\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:6:3:sequence-hinge","source_type":"word_analysis","support_id":"sup_54b40ee36583ff052b54","text":"{\"blocking_evidence\":null,\"headline\":\"ignition connects crushing and rising\",\"reader_payoff\":\"The reader notices that {{ar:ٱلْمُوقَدَةُ}} ({{tr:al-mūqadah}}) receives the crushing image from 104:5 and sends activated fire-motion toward 104:7.\",\"reason\":\"The CRITICAL boundary rows are coherent with the word table's identification of {{ar:نَارُ}} ({{tr:nāru}}) as the answer to 104:5 and the next ayah's uptake of the fire's motion in 104:7.\",\"representative_source_ids\":[\"QB-4afc3c18\",\"QY-2ea01bb0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:6:3:closure-state","source_type":"word_analysis","support_id":"sup_55b8dc53e636e3fed760","text":"{\"blocking_evidence\":null,\"headline\":\"the verse lands on state\",\"reader_payoff\":\"The reader notices that the ayah's final word makes the definition land on condition: the fire is not only named and attributed, but left ringing as kindled.\",\"reason\":\"The final adjective completes the nominal sequence and agrees with the fire, so closure falls on the state of kindling.\",\"representative_source_ids\":[\"QT-026d5750\",\"QT-2fca1a72\",\"QP-683f693b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:6:3","source_type":"word_analysis","support_id":"sup_6271d0fc138dabbed428","text":"{\"gloss_range\":\"the definite feminine passive participle describing the divine-attributed fire as already caused-to-be-kindled\",\"prose\":\"{{ar:ٱلْمُوقَدَةُ}} ({{tr:al-mūqadah}}) is the closing adjective, and its agreement ties it back to {{ar:نَارُ}} ({{tr:nāru}}), not to the genitive {{ar:ٱللَّهِ}} ({{tr:Allāhi}}). Its form is decisive: the article, supplied unique passive-participle shape, Form IV causative background, and feminine ending present the fire as the definite one already caused to be kindled, while the agent of that kindling is not stated. The root range supports ignition, fuel, hearth, fierce heat, flare, and gleam, but the local word selects active kindling as an achieved state, not fuel or a place of fire. That state gives the definition its landing point: substance, divine attribution, then activated condition; in pause, the -ah close also binds this landing to the surrounding short-surah cadence (104:5; 104:7). It also works as a hinge, receiving the crushing image from 104:5 and preparing the fire's rising over the hearts in 104:7. Echoes with 2:17, 5:64, and 24:35 sharpen the contrast: here there is no human seeker, no human-kindled fire being extinguished, and no lamp scene, but a defined fire standing already kindled. The qāf-dāl stop texture gives the closing ignition word a hard impact, so the sound payoff remains tied to the activated-fire image rather than floating as ornament.\",\"root_display\":\"{{ar:و ق د}} ({{tr:w-q-d}})\",\"root_gloss_range\":\"kindling, ignition, fuel, hearth, fierce heat, flare of intensity, and gleam; the local form selects the passive result of causative ignition, not fuel or a place of fire\",\"surface_display\":\"{{ar:ٱلْمُوقَدَةُ}} ({{tr:al-mūqadah}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:6:3:local-cluster","source_type":"word_analysis","support_id":"sup_6967c29db568a792a829","text":"{\"blocking_evidence\":null,\"headline\":\"kindling locks into the local cluster\",\"reader_payoff\":\"The reader notices that the kindled adjective is not isolated; it clings to the divine genitive phrase and specifies the local fire-light noun by ignition.\",\"reason\":\"The attachment evidence joins the participle to {{ar:نَارُ}} ({{tr:nāru}}), while the word boundary after {{ar:ٱللَّهِ}} ({{tr:Allāhi}}) keeps the divine attribution immediately adjacent to the kindled state.\",\"representative_source_ids\":[\"QI-e5b5f166\",\"QI-ed61187f\",\"QP-79bf0380\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:6:2:possession-agent-split","source_type":"word_analysis","support_id":"sup_70d8582551042fa66240","text":"{\"blocking_evidence\":null,\"headline\":\"attribution is explicit, agency is withheld\",\"reader_payoff\":\"The reader notices a role split: {{ar:ٱللَّهِ}} ({{tr:Allāhi}}) explicitly frames whose fire it is, while {{ar:ٱلْمُوقَدَةُ}} ({{tr:al-mūqadah}}) withholds the kindling agent.\",\"reason\":\"The genitive construction supports possession, source, or attribution, while QAC identifies the final word as a passive participle; the claim is narrowed away from saying that the genitive case itself explicitly marks the active kindler.\",\"representative_source_ids\":[\"QG-d345dcea\",\"QS-b19d0365\",\"MS-72a8c520\",\"QY-328ab395\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"104:6:2:1","source_type":"qac_morpheme","support_id":"sup_74d66f9fc897239f95a0","text":"{\"lemma_ar\":\"ٱللَّه\",\"morph_features\":\"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"PN\",\"qac_ref\":\"104:6:2:1\",\"qac_word_ref\":\"104:6:2\",\"root_ar\":\"ء ل ه\",\"surface_ar\":\"ٱللَّهِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:6:2:proper-name-domain","source_type":"word_analysis","support_id":"sup_7bdb0f35080e1429b366","text":"{\"blocking_evidence\":null,\"headline\":\"the proper name frames the fire\",\"reader_payoff\":\"The reader notices that the phrase uses the proper divine name, not a generic deity term, so the fire is framed as God's own domain or jurisdiction.\",\"reason\":\"QAC tags {{ar:ٱللَّهِ}} ({{tr:Allāhi}}) as the proper divine name, and the contextual profile confirms the dominant referent as God.\",\"representative_source_ids\":[\"QS-834b98e0\",\"QF-2fb2e55f\",\"QI-233046d7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:6:3:passive-causative-result","source_type":"word_analysis","support_id":"sup_9a8668365522d92facb7","text":"{\"blocking_evidence\":null,\"headline\":\"the form foregrounds completed kindling\",\"reader_payoff\":\"The reader notices that the form presents the fire as already caused-to-be-kindled while leaving the kindling agent grammatically unstated.\",\"reason\":\"QAC parses the word as a Form IV passive participle adjective, and the contextual profile marks this exact root/form as low occurrence, preserving the CRITICAL emphasis on the unusual completed-result form.\",\"representative_source_ids\":[\"QG-c0713893\",\"QF-fc7f041f\",\"QH-f4528939\",\"MH-a62946f2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:6:2:sound-and-form-binding","source_type":"word_analysis","support_id":"sup_a4a40ec6ed43238c7498","text":"{\"blocking_evidence\":null,\"headline\":\"recitation binds name and state\",\"reader_payoff\":\"The reader notices that the repeated l-sound and liaison into the following article make the divine genitive and kindled adjective sound continuous.\",\"reason\":\"The surface sequence moves from the divine name into a following article with hamzat waṣl, supporting the CRITICAL sound observation without changing the syntactic attachment.\",\"representative_source_ids\":[\"QE-0b9cd633\",\"QP-173e957e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:6:1:fire-light-exposure","source_type":"word_analysis","support_id":"sup_ac2b24b4874af463217f","text":"{\"blocking_evidence\":null,\"headline\":\"fire keeps a light-field pressure\",\"reader_payoff\":\"The reader notices that {{ar:نَارُ}} ({{tr:nāru}}) selects real burning fire, while the {{ar:ن و ر}} ({{tr:n-w-r}}) family keeps exposure and visibility close enough to prepare the heart-directed disclosure in 104:7.\",\"reason\":\"V4 accepts both the fire branch and light/illumination branch for {{ar:ن و ر}} ({{tr:n-w-r}}), but QAC's local form is the concrete fire noun, so illumination survives as narrowed root-family pressure rather than the selected gloss.\",\"representative_source_ids\":[\"QS-2276a766\",\"QS-abb99544\",\"QS-ede77e38\",\"MS-8c6b9f6a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:6:2:genitive-construct-completion","source_type":"word_analysis","support_id":"sup_b19d3d2f7dd2edd034f4","text":"{\"blocking_evidence\":null,\"headline\":\"the divine name completes the construct\",\"reader_payoff\":\"The reader notices that {{ar:ٱللَّهِ}} ({{tr:Allāhi}}) is grammatically required by {{ar:نَارُ}} ({{tr:nāru}}), making the fire definite and divinely specified rather than general.\",\"reason\":\"QAC and attachment evidence identify {{ar:ٱللَّهِ}} ({{tr:Allāhi}}) as the genitive complement of the iḍāfa headed by {{ar:نَارُ}} ({{tr:nāru}}).\",\"representative_source_ids\":[\"QG-22541053\",\"QG-6831a345\",\"QF-f0379ea4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:6:1:kindled-fire-pairing","source_type":"word_analysis","support_id":"sup_bad7d620a41e370ff8f8","text":"{\"blocking_evidence\":null,\"headline\":\"fire is paired with ignition\",\"reader_payoff\":\"The reader notices that the noun for fire is immediately completed by an ignition adjective, making substance and activation work together inside the three-word definition.\",\"reason\":\"Attachment evidence makes {{ar:ٱلْمُوقَدَةُ}} ({{tr:al-mūqadah}}) the adjective of {{ar:نَارُ}} ({{tr:nāru}}), and the CRITICAL rows use 2:17 and 5:64 as contrasts for fire, light, and kindling agency rather than as controls on the local parse.\",\"representative_source_ids\":[\"QI-4a3e17ee\",\"QI-278c7d69\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"104:6:1:1","source_type":"qac_morpheme","support_id":"sup_bae59b73d175b664b9d5","text":"{\"lemma_ar\":\"نَار\",\"morph_features\":\"STEM|POS:N|LEM:naAr|ROOT:nwr|F|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"104:6:1:1\",\"qac_word_ref\":\"104:6:1\",\"root_ar\":\"ن و ر\",\"surface_ar\":\"نَارُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:6:3:inner-intensification","source_type":"word_analysis","support_id":"sup_e081f925c827fcf536fd","text":"{\"blocking_evidence\":null,\"headline\":\"kindling presses inward\",\"reader_payoff\":\"The reader notices that ignition language can press beyond external flame because the next ayah gives the kindled fire motion over the hearts (104:7).\",\"reason\":\"The local word remains a fire adjective, but CRITICAL's inner-intensification payoff is narrowed by the immediate forward context in 104:7 rather than asserted as the base lexical sense.\",\"representative_source_ids\":[\"QS-88dc8625\",\"QB-10f80f40\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:6:1:divine-idafa-fire","source_type":"word_analysis","support_id":"sup_e859da0502fb89e8cb3f","text":"{\"blocking_evidence\":null,\"headline\":\"the construct makes the fire specified\",\"reader_payoff\":\"The reader notices that the fire is not introduced as an indefinite flame; the construct phrase {{ar:نَارُ ٱللَّهِ}} ({{tr:nāru llāhi}}) specifies it through divine attribution while not explicitly naming the kindler.\",\"reason\":\"The iḍāfa with {{ar:ٱللَّهِ}} ({{tr:Allāhi}}) is syntactically forced and makes the head definite; the narrowing is that possession, attribution, or source pressure should not be flattened into an explicit active-kindler claim.\",\"representative_source_ids\":[\"QG-6025f935\",\"QG-87ac7e5c\",\"QG-ba3adfac\",\"QI-6625917c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:6:1","source_type":"word_analysis","support_id":"sup_eb7c6ad6f9dd7d9a6896","text":"{\"gloss_range\":\"concrete fire as the predicate answer; definite through divine iḍāfa and locally colored by the root family's light/exposure field\",\"prose\":\"{{ar:نَارُ}} ({{tr:nāru}}) is the first word of the answer to the question in 104:5. Its nominative predicate role makes the ayah an identification: the Crusher is being defined, not narrated as a new event. The noun is concrete fire, yet it does not remain an unqualified item; as the construct head in {{ar:نَارُ ٱللَّهِ}} ({{tr:nāru llāhi}}), it loses tanwīn, becomes definite through the divine name, and names a marked divine-attributed fire without turning that attribution into an explicit kindler. The root family lets fire and illumination stand near each other, so the selected sense still burns as fire while carrying a narrowed pressure of exposure and visibility, which the next ayah's movement over the hearts (104:7) will make more pointed. The local pairing with {{ar:ٱلْمُوقَدَةُ}} ({{tr:al-mūqadah}}) also joins substance to ignition: against 2:17 and 5:64, this fire is God's by iḍāfa and already kindled, so possession and agency are redistributed rather than left in an ordinary human-kindling frame.\",\"root_display\":\"{{ar:ن و ر}} ({{tr:n-w-r}})\",\"root_gloss_range\":\"fire, burning, illumination, visible marking, and related light branches; only the fire noun is locally selected, while illumination remains a narrowed root-family pressure\",\"surface_display\":\"{{ar:نَارُ}} ({{tr:nāru}})\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"نَارُ ٱللَّهِ ٱلْمُوقَدَةُ","ayah_ref":"104:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000047/B002","root_001564/B002","root_001672/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001564","role":"Burning fire with flickering motion supplies the concrete blaze and gives it a latent capacity to mark by burning.","root":"ن و ر","source_ref":"104:6","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000047","role":"The fixed divine name supplies the attribution that locates the blaze under divine ownership, source, or authorization.","root":"ء ل ه","source_ref":"104:6","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001672","role":"Fire catching and being kindled converts the noun from a static label into an activated combustion process.","root":"و ق د","source_ref":"104:6","source_word_indices":["3"]}],"changed_reading":{"after":"A divinely attributed blaze already brought into active ignition, with its proximate agency held behind the passive form.","before":"A bare label for God's fire."},"confidence":"strong","focus_anchor":"The full construct in 104:6, especially the fire noun, its attribution to God, and the passive adjective at word 3.","mechanism":"The focus presents more than a static substance: a fire under divine attribution has been brought into active ignition. The passive form leaves the immediate kindler unexpressed while the construct supplies ultimate ownership or source.","model_id":"baseline_kindled_divine_fire"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_kindled_divine_fire","source_type":"hft","support_id":"sup_dadcbdd89570b13bd2ab","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"نَارُ ٱللَّهِ ٱلْمُوقَدَةُ","ayah_ref":"104:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000047/B002","root_001564/B001","root_001564/B002","root_001672/B006"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001564","role":"Light and illumination make the blaze disclose what had not been visible.","root":"ن و ر","source_ref":"104:6","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001564","role":"Fire used for branding makes disclosure capable of leaving an identifying and irreversible mark.","root":"ن و ر","source_ref":"104:6","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000047","role":"The fixed divine name makes the illuminating mark an attributed act rather than an accidental flare.","root":"ء ل ه","source_ref":"104:6","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_001672","role":"A gleam like kindled fire supplies the visible flash through which burning becomes revelation.","root":"و ق د","source_ref":"104:6","source_word_indices":["3"]}],"changed_reading":{"after":"The fire can also expose and brand, making its burning an act of visible identification.","before":"The fire is only an instrument of thermal destruction."},"confidence":"medium","focus_anchor":"The fire noun at word 1 can carry illumination and branding together, sharpened by the gleaming branch of the adjective at word 3.","mechanism":"One material can illuminate a surface and alter it permanently. Under divine attribution, the focus fire can therefore coexist as destructive heat, disclosure, and an identifying brand rather than functioning as heat alone.","model_id":"baseline_revelatory_brand"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_revelatory_brand","source_type":"hft","support_id":"sup_57fc7c6145607013864d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"نَارُ ٱللَّهِ ٱلْمُوقَدَةُ","ayah_ref":"104:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000047/B002","root_001564/B007","root_001672/B005"],"payload":{"activation_trace":[{"branch_id":"B007","mapped_root_id":"root_001564","role":"Enmity flaring between people supplies a social fire that can coexist with the physical blaze.","root":"ن و ر","source_ref":"104:6","source_word_indices":["1"]},{"branch_id":"B005","mapped_root_id":"root_001672","role":"Ready ignition and the flare of anger or war turn social hostility into an actively kindled force.","root":"و ق د","source_ref":"104:6","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000047","role":"The fixed divine name relocates the flare within divine attribution and judgment.","root":"ء ل ه","source_ref":"104:6","source_word_indices":["2"]}],"changed_reading":{"after":"Also a possible flare-form in which hostility and anger are brought to ignition under divine judgment.","before":"A materially burning fire with no relational dimension."},"confidence":"exploratory","focus_anchor":"The fire noun at word 1 and the ignition adjective at word 3 share branches of social enmity, anger, and warlike flare.","mechanism":"The lexical field permits a material blaze and a relational blaze to coexist. Divine attribution can transform a flare of hostility from a merely human disturbance into an exposed and adjudicated conflagration.","model_id":"baseline_relational_flare"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_relational_flare","source_type":"hft","support_id":"sup_6f4b2f40989ea0a0f51e","trust":"legacy_unbound"}]}
</lane_packet_json>
