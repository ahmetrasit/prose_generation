# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **104:4**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s104-regular-20260911/s104/104_4/micro.discovery.json` and modify nothing
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
  "ayah_ref": "104:4",
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
{"analysis_context":{"analysis_id":"s104-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"104:4","host_surah":104,"lane_context_refs":[],"ordered_context_refs":["104:0","104:1","104:2","104:3","104:5","104:6","104:7","104:8","104:9","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Anlam, genel yok etmeden ziyade kuru veya sert bir nesnenin kırılıp ufalanmasına bağlıdır.","branch_kind":"bare","branch_ref":"root_000337/B001","candidate_links":[{"candidate_id":"cand_48f791e38f8a434e20ec","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حُطَمَة","morph_features":"STEM|POS:N|LEM:HuTamap|ROOT:HTm|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:4:4:2","qac_word_ref":"104:4:4","surface_ar":"حُطَمَةِ"}],"gloss":"kuru ya da sert şeyi kırıp ufalama ve bundan kalan kuru döküntü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kuru ya da sert bir nesne, bütünlüğü bozulacak ve parçalara ayrılacak biçimde kırılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kırılma sonunda ortaya çıkan kuru parçalar ve döküntüler, işlemin sonuç ürünü olarak adlandırılır."}}],"root_ar":"ح ط م","root_id":"root_000337","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kırma işlemi ile kırılmış kuru maddenin parçalanma sonucunu birlikte temsil eden genel karşılıktır.","boundary_detail":"Anlam, genel yok etmeden ziyade kuru veya sert bir nesnenin kırılıp ufalanmasına bağlıdır.","branch_image_ar":"كسر الشيء اليابس حتى يتفتت","concept_gloss":"kuru ya da sert şeyi kırıp ufalama ve bundan kalan kuru döküntü","contextual_glosses":[{"applicability":"Nesnenin kemik, kabuk veya başka bir kuru sert madde olduğu eylem bağlamlarında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bağlamın verdiği kuru sert nesne ile kırıp parçalara ayırma işlemini korur."},"facet_ids":["F001"],"text":"ufalayıp kırmak","usage_role":"contextual"}],"definition":"Kuru ya da sert bir nesneyi kırarak ufak parçalara ayırmak veya böyle bir nesnenin kırılıp parçalanmasıdır. Bunun sonucu olan kuru kırık döküntüler de aynı anlam alanına girer.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kuru ya da sert bir nesne, bütünlüğü bozulacak ve parçalara ayrılacak biçimde kırılır."},{"facet_id":"F002","role":"extension","statement":"Kırılma sonunda ortaya çıkan kuru parçalar ve döküntüler, işlemin sonuç ürünü olarak adlandırılır."}],"identity_rationale":"Kaynak ifadesi, kuru ya da sert bir nesneyi kırarak parçalara ayırma eylemini ve bu eylem sonucunda ortaya çıkan kırıntıları birlikte doğrular. Geçici çerçeve bu temel işlem ile sonucunu doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kuru ya da sert bir şeyi kırıp parçalamak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kırılıp parçalanmış"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"kırıp parçalama"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"kuru şeylerin kırık döküntüsü"}],"lexicalization_note":"Çıplak dal, herhangi bir özel tamlamadan anlam taşımadan kırma, parçalanma ve kırık döküntü çekirdeğiyle tanımlanır.","neighbor_coverage_note":"Verilen bütün komşu adayları değerlendirildi; yayımlanan üç karşılaştırma kırılma, ufalanma ve genel yok etme arasındaki en yararlı sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kuru veya sert nesnenin ufalanmasına ve çıkan döküntüye bağlıdır; komşu dal ise kırılmayı daha genel tutar ve hızlı kırılma ile rüzgarın verdiği hasarı da kapsar.","focus_only":"Kuru ya da sert nesnenin ufalanması ve geride bıraktığı döküntü özellikle öne çıkar.","gloss":"kırılıp ufalanma","neighbor_only":"Kırılma, rüzgarın yapı, ağaç veya taşıtı kırması gibi daha geniş olaylara da uzanır.","neighbor_ref":"root_001233/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir nesnenin kırılarak bütünlüğünü yitirmesini ve parçalara ayrılmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dalın sınırı kuru ya da sert nesnedir; komşu dal ise parçaların dağılıp saçılmasını öne çıkarır ve nesne türünü aynı biçimde sınırlamaz.","focus_only":"Kuru veya sert nesne sınırlaması ile sonuçtaki kuru döküntü açıkça anlamın parçasıdır.","gloss":"kırıntıya dönüştürme","neighbor_only":"Parçaların dağılıp saçılması ve belirli hayvan kemiklerinin kırılması ayrıca belirtilir.","neighbor_ref":"root_000578/B001","relation_type":"near_synonym","shared_zone":"Her iki dal kırma, ufalama ve kırılan şeyden geriye parça kalması alanında geniş ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal somut kırılma ve ufalanmadır; komşu dalın çekirdeği daha geniş bir yok etme ve geçersiz bırakma alanına yayılır.","focus_only":"Somut ve kuru bir nesnenin kırılarak küçük parçalara ayrılması temel işlemdir.","gloss":"kırma ve yok etme","neighbor_only":"Öldürme, geçersiz kılma, eksiltme ve genel yıkım gibi fiziksel kırılmayı aşan sonuçlar bulunur.","neighbor_ref":"root_000174/B001","relation_type":"near_neighbor","shared_zone":"İki dal da bir şeyin önceki bütünlüğünü veya işlerliğini ortadan kaldıran zarar verici bir değişimi içerir."}],"source_phrase_ar":"حطمت الشيء حَطْما كسرته (maqayis;sihah;mufradat)؛ الحَطْم كسرك الشيء اليابس كالعظام ونحوها (ayn;tahdhib)؛ الحُطام ما تكسر من اليبس (sihah;tahdhib;mufradat)","source_summary":"Kaynakların ortak çekirdeği, özellikle kuru ya da sert şeylerin kırılıp ufalanmasıdır; kırılmış kuru maddeden kalan döküntü de bu çekirdeğin sonuç anlamıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه حَطْم الشيء اليابس والعظم وقشر البيض وتحطمه والحُطام مما تكسر من اليبس","what_is_not_ar":"ليس اسم النار ولا السنة الشديدة ولا الراعي العنيف ولا الموضع"},"support_links":["sup_c190bb38923e1f1d4bba"]},{"boundary":"Dal her ateşi değil, parçalayıp yok etme niteliğiyle adlandırılan şiddetli ateşi kapsar.","branch_kind":"bare","branch_ref":"root_000337/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حُطَمَة","morph_features":"STEM|POS:N|LEM:HuTamap|ROOT:HTm|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:4:4:2","qac_word_ref":"104:4:4","surface_ar":"حُطَمَةِ"}],"gloss":"karşısına çıkanı parçalayan şiddetli ateş","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Şiddetli ateş, değdiği şeyi kırıp parçalayarak yok eden etkisi üzerinden adlandırılır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gönderge, kaynaklarda ateşin bütünü, çok şiddetli ateş, Cehennem veya onun bir kapısı olarak değişir."}}],"root_ar":"ح ط م","root_id":"root_000337","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yıkıcı etkiyi ve ateş göndergesini birlikte taşıyan, kaynaklardaki gönderge çeşitliliğine açık karşılıktır.","boundary_detail":"Dal her ateşi değil, parçalayıp yok etme niteliğiyle adlandırılan şiddetli ateşi kapsar.","branch_image_ar":"نار تحطم ما تلقى","concept_gloss":"karşısına çıkanı parçalayan şiddetli ateş","contextual_glosses":[{"applicability":"Adın neden verildiğini açıklayan ve belirli bir inanç göndergesini adlandırmadan ateşin etkisini öne çıkaran bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kaynaklarda değişen özel ateş ve Cehennem kapısı göndergelerini tek tek belirtmez.","preserves":"Şiddetli ateşin karşısına çıkanı yok eden etkisini açık biçimde korur."},"facet_ids":["F001"],"text":"yakıp yok eden ateş","usage_role":"explanatory"}],"definition":"Karşısına çıkan şeyi parçalayıp yok eden şiddetli ateş için kullanılan addır. Kaynaklar bunu genel bir ateş, çok şiddetli ateş, Cehennem veya onun bir kapısı biçiminde sınırlar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Şiddetli ateş, değdiği şeyi kırıp parçalayarak yok eden etkisi üzerinden adlandırılır."},{"facet_id":"F002","role":"source_variant","statement":"Gönderge, kaynaklarda ateşin bütünü, çok şiddetli ateş, Cehennem veya onun bir kapısı olarak değişir."}],"identity_rationale":"Kaynak ifadesi, karşısına çıkan şeyi parçalayıp yok ettiği düşünüldüğü için böyle adlandırılan ateşi açıkça tanımlar. Ateşin şiddeti ile parçalayıcı etkisi dal kimliğinin ayrılmaz iki yönüdür.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"karşısına çıkanı parçalayan şiddetli ateş"}],"lexicalization_note":"Çıplak dal, özel bir tamlamaya bağlı olmadan yıkıcı etkisiyle adlandırılan şiddetli ateş anlamını taşır.","neighbor_coverage_note":"Bütün adaylar incelendi; ateşin fiziksel kırma anlamıyla bağı ve başka bir ateş adından farkı dışındaki adaylar sınırı keskinleştirmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bir ateş adıdır ve kırma onun adlandırma gerekçesidir; komşu dal ise doğrudan nesne kırma işlemini ve sonucunu anlatır.","focus_only":"Gönderge, parçalayıcı etkisi üzerinden adlandırılan şiddetli ateştir.","gloss":"parçalayan ateş","neighbor_only":"Kuru ya da sert bir nesnenin gerçek anlamda kırılması ve oluşan döküntü bulunur.","neighbor_ref":"root_000337/B001","relation_type":"near_neighbor","shared_zone":"Ateş adı, fiziksel kırıp parçalama çekirdeğinden kurulan yıkıcı etki tasarımını paylaşır."},{"boundary_match":"field_only","distinction":"Odak dalın anlamı ateşin parçalayıcı etkisine dayanır; komşu dal ise belirli bir kullanım geleneğine ait dolaylı adlandırmadır.","focus_only":"Ateş, karşısına çıkanı parçalayan şiddeti ve yıkıcı işleviyle tanımlanır.","gloss":"ateş adı","neighbor_only":"Ateş için belirli bir bitki bağlamında kullanılan geleneksel bir dolaylı ad söz konusudur.","neighbor_ref":"root_000698/B011","relation_type":"same_field","shared_zone":"Her iki dalın göndergesi ateştir ve ikisi de ateşe doğrudan temel adından farklı bir ad verir."}],"source_phrase_ar":"سميت النار الحُطَمَة لحطمها ما تلقى (maqayis;sihah)؛ الحُطَمَة النار وقيل باب من جهنم (ayn)؛ للنار الشديدة حُطَمَة (tahdhib)؛ سميت الجحيم حُطَمَة (mufradat)","source_summary":"Ortak açıklama, ateşin karşılaştığı şeyi parçalayıp yok etmesi nedeniyle adlandırıldığıdır; gönderge geniş ateş anlamından Cehennem'e veya onun bir kapısına kadar değişir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه اسم النار الحُطَمَة والجحيم أو النار الشديدة لأنها تحطم ما تلقى","what_is_not_ar":"ليس كل نار بلا معنى التحطيم ولا حُطام النبات"},"support_links":[]},{"boundary":"Dal sıradan bir takvim yılını değil, kuraklık ve yıkıcı sıkıntıyla belirlenen ağır yılı anlatır.","branch_kind":"bare","branch_ref":"root_000337/B003","candidate_links":[{"candidate_id":"cand_f3204c6924368a8ca114","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حُطَمَة","morph_features":"STEM|POS:N|LEM:HuTamap|ROOT:HTm|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:4:4:2","qac_word_ref":"104:4:4","surface_ar":"حُطَمَةِ"}],"gloss":"insanı ve malı çökerten ağır kıtlık yılı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yıl, kuraklık ve ağır geçim sıkıntısıyla insanları ve malları çökerten bir dönemdir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dönemin yıkıcı etkisi, karşısına çıkan şeyi kırıp parçalayan bir güç gibi düşünülür."}}],"root_ar":"ح ط م","root_id":"root_000337","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kurak yıl göndergesini ve onun insanlar ile mal üzerindeki yıkıcı sonucunu birlikte veren genel karşılıktır.","boundary_detail":"Dal sıradan bir takvim yılını değil, kuraklık ve yıkıcı sıkıntıyla belirlenen ağır yılı anlatır.","branch_image_ar":"سنة شديدة تكسر الناس والمال","concept_gloss":"insanı ve malı çökerten ağır kıtlık yılı","contextual_glosses":[{"applicability":"Bir topluluğun yaşadığı kurak ve yıkıcı dönemi doğal Türkçeyle adlandıran bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsanları ve malları kırıp geçirircesine çökerten etkiyi açıkça söylemez.","preserves":"Yılın ağır ve kıtlıkla belirlenen dönem olmasını açıkça korur."},"facet_ids":["F001"],"text":"ağır kıtlık yılı","usage_role":"general"}],"definition":"İnsanları ve mallarını ağır biçimde yıpratan, kuraklık ve kıtlıkla geçen sert yıldır. Parçalama düşüncesi burada fiziksel kırmadan, yaşam koşullarını çökerten etkiye aktarılmıştır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yıl, kuraklık ve ağır geçim sıkıntısıyla insanları ve malları çökerten bir dönemdir."},{"facet_id":"F002","role":"associated_use","statement":"Dönemin yıkıcı etkisi, karşısına çıkan şeyi kırıp parçalayan bir güç gibi düşünülür."}],"identity_rationale":"Kaynak ifadesi ağır yıl ile kuraklığı bir arada verir ve bu dönemin insanları, malları ve genel olarak karşısına çıkanları çökertici etkisini adlandırma gerekçesi yapar. Geçici çerçeve bu çekirdeği doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"insanı ve malı çökerten ağır kuraklık yılı"}],"lexicalization_note":"Çıplak dal, özel bir söz dizimine bağlı olmadan ağır ve kurak yıl adı olarak tanımlanır.","neighbor_coverage_note":"Bütün komşular değerlendirildi; seçilenler kurak yıl çekirdeğini, göç ettiren kuraklık ve daha geniş felaket anlamlarından ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yıkıcı etkiyi genel olarak insan ve mala bağlar; komşu dal ise özellikle kuraklığın insanları yaşadıkları bölgeden yerleşimlere itmesi sonucunu taşır.","focus_only":"Kurak yılın insanları ve malları kırıp geçirircesine çökerten etkisi adın merkezindedir.","gloss":"ağır kuraklık yılı","neighbor_only":"Kuraklığın kır insanlarını verimli bölgelere veya yerleşimlere sürüklemesi özellikle belirtilir.","neighbor_ref":"root_001202/B003","relation_type":"near_synonym","shared_zone":"İki dal da toplumu ağır sıkıntıya düşüren şiddetli ve kurak bir yılı adlandırır."},{"boundary_match":"partial","distinction":"Odak dal ağır yılın kırıp geçirircesine yıkıcı olmasını vurgular; komşu dal yağış ve verim durumunun farklı görünümlerini daha ayrıntılı sınırlar.","focus_only":"Yılın insan ve mal üzerindeki ezici, çökertici etkisi açık bir anlam bileşenidir.","gloss":"kurak yıl","neighbor_only":"Yağmurun hiç olmaması veya aynı yıl içinde verimlilik ile kuraklığın birlikte bulunması seçenekleri vardır.","neighbor_ref":"root_000140/B007","relation_type":"near_synonym","shared_zone":"Her iki dal kuraklık ve ürün yokluğuyla belirlenen sıkıntılı bir yılı anlatır."},{"boundary_match":"partial","distinction":"Odak dal bir yıl türünü adlandırır; komşu dal ise kurak yıl örneğini de içeren daha geniş yok oluş, yoksulluk ve felaket sonuçlarını kapsar.","focus_only":"Belirli gönderge, kuraklık ve kıtlıkla geçen ağır bir yıldır.","gloss":"kuraklık felaketi","neighbor_only":"Öldürme, topluluğu veya malı tümden yok etme, yoksulluk ve genel felaket daha geniş biçimde bulunur.","neighbor_ref":"root_000598/B006","relation_type":"near_neighbor","shared_zone":"İki dal da kuraklık döneminin topluluğa ve mala verdiği ağır kayıp alanında buluşur."}],"source_phrase_ar":"الحُطَمَة السنة الشديدة لأنها تحطم كل شيء (maqayis)؛ الحُطَمَة السنة الشديدة (ayn;tahdhib)؛ أصابتهم حُطَمَة أي سنة وجدب (sihah)","source_summary":"Kaynaklar ağır yılı ve kuraklığı ortak gönderge olarak verir; adlandırma, bu dönemin insanları ve malları kırıp geçirircesine yıpratmasına dayanır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الحُطَمَة بمعنى السنة الشديدة والجدب","what_is_not_ar":"ليس اسم النار ولا كسر الأجسام مباشرة"},"support_links":["sup_bb908782094e8de50ec0"]},{"boundary":"Dal sürünün kendi verdiği zararı değil, onu acımasızca süren veya güden kişinin davranışını anlatır.","branch_kind":"bare","branch_ref":"root_000337/B004","candidate_links":[{"candidate_id":"cand_83f15fc7c30c038e778b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حُطَمَة","morph_features":"STEM|POS:N|LEM:HuTamap|ROOT:HTm|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:4:4:2","qac_word_ref":"104:4:4","surface_ar":"حُطَمَةِ"}],"gloss":"sürüyü sertçe sürüp hayvanları birbirine ezen acımasız sürücü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sürücü veya çoban, bakımındaki hayvanlara karşı merhametsiz ve aşırı sert davranır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sert sürüş hayvanları birbirine çarptırıp ezer ve sürünün yeterince otlamasını engelleyebilir."}}],"root_ar":"ح ط م","root_id":"root_000337","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin rolünü, merhametsiz tutumunu ve sert sürüşün hayvanlar üzerindeki sonucunu birlikte veren karşılıktır.","boundary_detail":"Dal sürünün kendi verdiği zararı değil, onu acımasızca süren veya güden kişinin davranışını anlatır.","branch_image_ar":"سائق أو راع يعنف بالماشية","concept_gloss":"sürüyü sertçe sürüp hayvanları birbirine ezen acımasız sürücü","contextual_glosses":[{"applicability":"Kişinin sürüye karşı tutumunun öne çıktığı ve sert sürüş biçiminin bağlamdan anlaşıldığı kullanımlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvanları birbirine çarptırma ve yeterince otlatmama biçimindeki özel sonuçları söylemez.","preserves":"Çoban rolünü ve hayvanlara karşı merhametsiz tutumu korur."},"facet_ids":["F001"],"text":"acımasız çoban","usage_role":"contextual"}],"definition":"Hayvanları aşırı sert süren veya güden, onları birbirine çarptırıp ezen ve gereği gibi otlamalarına izin vermeyen merhametsiz sürücü ya da çobandır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sürücü veya çoban, bakımındaki hayvanlara karşı merhametsiz ve aşırı sert davranır."},{"facet_id":"F002","role":"specialization","statement":"Sert sürüş hayvanları birbirine çarptırıp ezer ve sürünün yeterince otlamasını engelleyebilir."}],"identity_rationale":"Kaynak ifadesi sürücü ya da çobanın hayvanlara karşı merhametsiz ve aşırı sert davranmasını, onları birbirine çarptırmasını ve iyi otlamalarına engel olmasını aynı kişi niteliğinin görünümleri olarak verir. Geçici çerçeve bu kişi ve davranış bağını doğru kurar.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"hayvanları birbirine çarptıracak kadar sert süren acımasız sürücü"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"sürüsüne acımayan ve onu iyi otlatmayan çoban"}],"lexicalization_note":"Çıplak dal, özel bir tamlamaya bağlı olmadan hayvanlara sert davranan sürücü veya çoban niteliğini taşır.","neighbor_coverage_note":"Bütün adaylar gözden geçirildi; yayımlanan ilişkiler sert sürüşü genel sertlikten ve yalnızca sesle yönlendirmeden ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bu davranışı yapan kişiyi ve hayvanların birbirine ezilmesini öne çıkarır; komşu dal ise sürüyü yoran ve yemeyi engelleyen sert sürme eylemidir.","focus_only":"Kişi merhametsiz bir sürücü veya çoban olarak nitelenir ve hayvanları birbirine ezdirebilir.","gloss":"sürüyü sert sürme","neighbor_only":"Hayvanların yorulması ve sürüş sırasında yemelerine izin verilmemesi eylemin doğrudan sonucudur.","neighbor_ref":"root_000251/B006","relation_type":"near_synonym","shared_zone":"İki dal da hayvanları dinlenme ve beslenme gereksinimlerini gözetmeden aşırı sert sürmeyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal hayvan refahını bozan acımasız sürücü veya çobandır; komşu dalın sert kişi niteliği daha geniş görev ve davranış alanlarına uzanır.","focus_only":"Sertlik özellikle sürüye karşı merhametsizlik ve hayvanların zarar görmesiyle sınırlandırılır.","gloss":"sert sürücü","neighbor_only":"Sertlik, sürücülüğün yanında savaş ve çalışma alanlarında da görülebilen genel bir kişi niteliğidir.","neighbor_ref":"root_000316/B008","relation_type":"near_neighbor","shared_zone":"Her iki dal sürme işinde aşırı sert ve zorlayıcı davranan kişiyi kapsayabilir."},{"boundary_match":"thematic_only","distinction":"Odak dal yönetimin sertliği ve verdiği fiziksel zarardır; komşu dal ise çağırma ya da azarlama sesiyle ilgilidir ve merhametsizlik gerektirmez.","focus_only":"Hayvanlara zarar veren acımasız sürüş ve gütme biçimi temel anlamdır.","gloss":"sürüyü azarlama","neighbor_only":"Keçi veya koyunu çağırmak ve belirli seslerle azarlamak temel anlamdır.","neighbor_ref":"root_000477/B003","relation_type":"thematic","shared_zone":"İki dal da çoban veya sürücünün küçükbaş hayvanları yönlendirdiği aynı gütme ortamında yer alır."}],"source_phrase_ar":"الحَطِم السواق يعنف يحطم بعض الإبل ببعض (maqayis)؛ رجل حَطِم وحُطَمَة إذا كان قليل الرحمة للماشية يهشم بعضها ببعض (sihah)؛ شر الرعاء الحُطَمَة (sihah;tahdhib)؛ سائق حَطِم يحطم الإبل لفرط سوقه (mufradat)","source_summary":"Kaynaklarda kişi, sürüyü ölçüsüz sertlikle yöneten ve hayvanlara acımayan sürücü veya çobandır; bu sertlik birbirine çarpma, ezilme ve otlatmama sonuçlarıyla açıklanır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه السائق أو الراعي الحَطِم والحُطَمَة الذي يعنف بالماشية ويهشم بعضها ببعض أو لا يتركها ترعى","what_is_not_ar":"ليس الأكول ولا عيث القطيع الكثير بنفسه"},"support_links":["sup_bdfe0ae4d4049c76fe0f"]},{"boundary":"Yaşlılık ve bedensel çöküş çekirdektir; uzun birliktelik yalnızca belirli kişi tamlamasında yaşlanmanın ortamıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000337/B005","candidate_links":[{"candidate_id":"cand_f3204c6924368a8ca114","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حُطَمَة","morph_features":"STEM|POS:N|LEM:HuTamap|ROOT:HTm|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:4:4:2","qac_word_ref":"104:4:4","surface_ar":"حُطَمَةِ"}],"gloss":"yaşlılıkla çöküp güçten düşmek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yaşlanma veya zayıflama, insan ya da hayvanın bedenini çökmüş ve güçsüz duruma getirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"At, ileri yaş veya zayıflık nedeniyle çökmüş ve güçten düşmüş olarak nitelenir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli tamlamalarda yaş veya yakınları arasında geçirilen uzun süre, kişinin yaşlanıp çökmüş duruma gelmesinin nedeni olarak sunulur."}}],"root_ar":"ح ط م","root_id":"root_000337","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan ve hayvandaki yaşlanma kaynaklı bedensel çöküş çekirdeğini verir; özel tamlamaların katılımcıları ayrıca belirtilmelidir.","boundary_detail":"Yaşlılık ve bedensel çöküş çekirdektir; uzun birliktelik yalnızca belirli kişi tamlamasında yaşlanmanın ortamıdır.","branch_image_ar":"سن أو طول صحبة يحطم البدن","concept_gloss":"yaşlılıkla çöküp güçten düşmek","contextual_glosses":[{"applicability":"Yaşın insanı veya hayvanı bedence zayıflattığı bağlamlarda doğal bir eylem karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalnızca zayıflıktan çökmüş atı ve yakınlar arasında geçen uzun süreye bağlı özel kullanımı kapsamaz.","preserves":"Yaşlanma ile ortaya çıkan bedensel çöküş ve güç kaybını korur."},"facet_ids":["F001"],"text":"yaşlılıktan çökmek","usage_role":"general"}],"definition":"İnsan ya da hayvanın yaşlılık, uzun ömür veya zayıflık yüzünden bedence çökmesi ve güçten düşmesidir. Atı doğrudan niteleyen kullanım ile yaşın, hayvanın yaşlanmasının veya yakınları arasında geçirilen uzun sürenin bu sonucu doğurduğu tamlamalar birbirine genellenmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yaşlanma veya zayıflama, insan ya da hayvanın bedenini çökmüş ve güçsüz duruma getirir."},{"facet_id":"F002","role":"specialization","statement":"At, ileri yaş veya zayıflık nedeniyle çökmüş ve güçten düşmüş olarak nitelenir."},{"facet_id":"F003","role":"associated_use","statement":"Belirli tamlamalarda yaş veya yakınları arasında geçirilen uzun süre, kişinin yaşlanıp çökmüş duruma gelmesinin nedeni olarak sunulur."}],"identity_rationale":"Kaynak ifadesi yaşlanıp güçten düşme çekirdeğini destekler, ancak bunu tek bir yalın anlam gibi vermez: yaşlı ve zayıf at betimlemesi ile hayvanın yaşlanması, yaşın kişiyi çökertmesi ve kişinin yakınları arasında uzun süre yaşlanması ayrı söz dizimlerinde gerçekleşir. Bu nedenle dal korunabilir, fakat her kullanımın sınırı belirtilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yaşlılıktan veya zayıflıktan çökmüş at"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"hayvan yaşlanıp güçten düştü"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yaş onu yaşlandırıp güçsüzleştirdi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yakınları arasında uzun süre yaşayıp iyice yaşlandı"}],"lexicalization_note":"Dal, yaşlı ve güçsüz atı belirten biçim ile hayvanın, yaşın veya yakınlar arasında geçen uzun sürenin özne olduğu tamlamalı kullanımları ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen üç komşu yaşa bağlı çöküşü genel zayıflık, sırt hasarı ve onarılamaz son evreden ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yaşlanmayı ve onu doğuran belirli söz dizimlerini merkez alır; komşu dal genel bedensel zayıflık ve zayıflamaya daha geniş biçimde açıktır.","focus_only":"Yaşın veya uzun yaşamın bedeni kırılmış gibi çökertmesi ve belirli tamlamalardaki neden yapısı bulunur.","gloss":"yaşlı ve güçsüz","neighbor_only":"İnsan ve hayvanda genel güçsüzlük ile hızlı zayıflama, yaşlılık nedeni olmadan da kapsanır.","neighbor_ref":"root_001592/B004","relation_type":"near_synonym","shared_zone":"İki dal insan veya hayvan bedeninin zayıf, çökmüş ve ileri yaşla tükenmiş durumunu anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalın ana nedeni yaş ve zayıflıktır; komşu dal ayrıca sırt yarası bulunan yük hayvanlarını kapsadığı için tam ikame kurulamaz.","focus_only":"Yaşlılığın bedeni kırılmış gibi çökertmesi ve atı niteleyen özel kullanım öne çıkar.","gloss":"yaşlılıktan çökmüş","neighbor_only":"Sırt yarası veya yük vurmasıyla bozulmuş eşek ve deve anlamları yaşlılık dışında da bulunur.","neighbor_ref":"root_000172/B003","relation_type":"near_synonym","shared_zone":"Her iki dal yaşlı veya güçsüz insan ve hayvanın bedensel olarak çökmüş durumunda örtüşür."},{"boundary_match":"partial","distinction":"Odak dal bedensel çöküşü anlatır; komşu dal ise yaşlılığın yanında herhangi bir şeyin onarılamaz son evresini de kapsar.","focus_only":"İleri yaşın doğurduğu bedensel zayıflama ve çökmüş görünüm temel sonuçtur.","gloss":"ileri yaşın çöküşü","neighbor_only":"Bir şeyin artık düzeltilemeyecek son aşamaya ulaşması insan yaşlılığından daha geniş bir kapsam taşır.","neighbor_ref":"root_000981/B002","relation_type":"near_neighbor","shared_zone":"İki dal ileri yaşın kişiyi son ve güçsüz bir duruma getirmesi alanında kesişir."}],"source_phrase_ar":"يقال للفرس إذا تهدم لطول عمره حَطِم (maqayis;sihah)؛ حطمت الدابة أي أسنت (sihah)؛ حطمته السن إذا أسن وضعف (sihah;tahdhib)؛ حطم فلانا أهله إذا كبر فيهم كأنهم صيروه شيخا محطوما (tahdhib)؛ فرس حَطِم إذا هزل أو أسن فضعف (tahdhib)","source_summary":"Toplu kanıt, yaşlılık ve zayıflığın atı, başka bir hayvanı veya insanı çökmüş ve güçsüz hale getirmesini ortaklaştırır; özne ve neden, her söz diziminde ayrıca korunmalıdır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه الدابة أو الفرس أو الإنسان إذا أسن أو هزل أو ضعف كالمحطوم","what_is_not_ar":"ليس المرض الخاص في القوائم إلا على جهة الاحتمال ولا كسر الشيء الخارجي"},"support_links":["sup_bb908782094e8de50ec0"]},{"boundary":"Sürünün ezici kalabalığı ile aslanın mala saldırısı, ortak yıkıcı etkiye bağlı fakat ayrı kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_000337/B006","candidate_links":[{"candidate_id":"cand_83f15fc7c30c038e778b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حُطَمَة","morph_features":"STEM|POS:N|LEM:HuTamap|ROOT:HTm|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:4:4:2","qac_word_ref":"104:4:4","surface_ar":"حُطَمَةِ"}],"gloss":"karşısına çıkanı ezen kalabalık sürü veya aslanın mala saldırısı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kalabalık deve veya koyun sürüsü, ilerlerken karşısına çıkanları ve otlağı ezip tüketir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kısıtlı bir söz öbeğinde aslanın mala saldırması, zarar vermesi ve kırıp geçirmesi anlatılır."}}],"root_ar":"ح ط م","root_id":"root_000337","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalabalık sürü anlamı ile aslanın mala saldırısını ortak yıkıcı etki üzerinden, kapsamlarını ayırarak temsil eder.","boundary_detail":"Sürünün ezici kalabalığı ile aslanın mala saldırısı, ortak yıkıcı etkiye bağlı fakat ayrı kullanımlardır.","branch_image_ar":"جماعة أو عيث يحطم ما يلقى","concept_gloss":"karşısına çıkanı ezen kalabalık sürü veya aslanın mala saldırısı","contextual_glosses":[{"applicability":"Kalabalık hayvan topluluğunun karşısına çıkan bitki örtüsünü ezip tükettiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aslanın mala saldırıp kırıp geçirmesini anlatan kısıtlı kullanımı dışarıda bırakır.","preserves":"Kalabalık sürünün otlağı ezip tüketen yıkıcı hareketini korur."},"facet_ids":["F001"],"text":"otlağı silip süpüren sürü","usage_role":"contextual"}],"definition":"Karşısına çıkan şeyi, özellikle otlağı ezip tüketen kalabalık deve veya koyun sürüsüdür. Ayrı ve söz öbeğine bağlı kullanımda, aslanın mala saldırıp kırıp geçirmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kalabalık deve veya koyun sürüsü, ilerlerken karşısına çıkanları ve otlağı ezip tüketir."},{"facet_id":"F002","role":"associated_use","statement":"Kısıtlı bir söz öbeğinde aslanın mala saldırması, zarar vermesi ve kırıp geçirmesi anlatılır."}],"identity_rationale":"Kaynak ifadesi iki ayrı gerçekleşmeyi aynı yıkıcı hareket altında toplar: kalabalık deve veya koyun sürüsü karşılaştığını ve otlağı ezer, aslan ise mala saldırıp kırıp geçirir. Dal korunabilir, ancak hayvan topluluğu ile yırtıcı saldırısı tek bir göndergeymiş gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"karşısına çıkanı ve otu ezen kalabalık deve veya koyun sürüsü"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"aslanın mala saldırıp kırıp geçirmesi"}],"lexicalization_note":"Dal, kalabalık sürüyü adlandıran biçimi aslanın mala verdiği zararı bildiren kısıtlı söz öbeğinden ayrı tanımlar.","neighbor_coverage_note":"Bütün adaylar incelendi; seçilenler yıkıcı sürüyü yalnızca hayvan topluluğu bildiren dallardan ve genel yok etmeden ayırır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dalda topluluğun ezip tüketen davranışı kurucudur; komşu dal yalnızca topluluğun veya sürünün varlığını bildirir.","focus_only":"Hayvan topluluğu, kalabalığının etkisiyle karşısına çıkanı ve otlağı ezer.","gloss":"kalabalık sürü","neighbor_only":"İnsan veya koyun topluluğu yalnızca bir arada bulunan kalabalık olarak adlandırılır.","neighbor_ref":"root_000204/B001","relation_type":"same_field","shared_zone":"İki dal da çok sayıda koyun veya başka hayvanın oluşturduğu topluluğu gönderebilir."},{"boundary_match":"field_only","distinction":"Odak dal sürünün yıkıcı hareketini gerektirir; komşu dal ise sayıca çok deve topluluğunu davranış koşulu olmadan belirtir.","focus_only":"Deve sürüsünün kalabalığı ve karşılaştığı şeyi ezip tüketmesi anlamın parçasıdır.","gloss":"deve sürüsü","neighbor_only":"Belirli sayı tartışmalarıyla birlikte yalnızca çok sayıda deveden oluşan parça veya sürü anlatılır.","neighbor_ref":"root_000997/B005","relation_type":"same_field","shared_zone":"Her iki dal kalabalık bir deve topluluğunu adlandırabilir."},{"boundary_match":"partial","distinction":"Odak dal belirli hayvan katılımcılarını ve ezme ya da saldırı biçimini gerektirir; komşu dal genel yok etme ve kökünü kazıma sonucuna odaklanır.","focus_only":"Yok edici etki, kalabalık sürünün ilerleyişine veya aslanın mala saldırısına bağlıdır.","gloss":"ezip tüketme","neighbor_only":"Öldürme, kökünü kazıma ve soğuk ya da zararlının bitkiyi yok etmesi daha genel biçimde kapsanır.","neighbor_ref":"root_000321/B001","relation_type":"near_neighbor","shared_zone":"İki dal canlıların veya bitkinin ağır zarar görüp ortadan kalkması sonucunda kesişir."}],"source_phrase_ar":"العكرة من الإبل حُطَمَة لأنها تحطم كل شيء تلقاه (maqayis;sihah)؛ للعكرة من الإبل حُطَمَة لحطمها الكلأ وكذلك الغنم إذا كثرت (tahdhib)؛ حُطَمَة الأسد في المال عيثه وفرسه (ayn;tahdhib)","source_summary":"Toplu kanıt kalabalık sürünün karşılaştığı şeyi ve otlağı ezmesini temel görünüm olarak verir; aynı yıkıcı hareket alanında aslanın mala saldırısı için kısıtlı bir kullanım da bulunur.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه عكرة الإبل أو كثرة الغنم التي تحطم ما تلقاه أو الكلأ ويدخل فيه عيث الأسد في المال","what_is_not_ar":"ليس الراعي العنيف الذي يحطم الماشية بسوقه"},"support_links":["sup_bdfe0ae4d4049c76fe0f"]},{"boundary":"Dal genel bir kırık ya da kalabalık yer değil, kutsal yapıya bitişik belirli mimari bölümdür.","branch_kind":"bare","branch_ref":"root_000337/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حُطَمَة","morph_features":"STEM|POS:N|LEM:HuTamap|ROOT:HTm|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:4:4:2","qac_word_ref":"104:4:4","surface_ar":"حُطَمَةِ"}],"gloss":"kutsal yapının yağmur oluğu yanındaki belirli bölümü veya duvarı","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderge, kutsal yapının yağmur oluğu tarafındaki belirli bölüm veya bu bölümün duvarıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynaklar yeri kimi zaman belirli bölüm, kimi zaman onun duvarı veya yağmur oluğunun bulunduğu bölüm diye sınırlar."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Adın kökeni, bölümün ana yapının dışında ve eksik bırakılmasıyla ya da ziyaretçi kalabalığının sıkıştırıcı etkisiyle açıklanır."}}],"root_ar":"ح ط م","root_id":"root_000337","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli yeri konumu ve kaynaklarda değişen bölüm veya duvar sınırıyla tanımlar; tartışmalı adlandırma açıklamalarını yer kimliğine katmaz.","boundary_detail":"Dal genel bir kırık ya da kalabalık yer değil, kutsal yapıya bitişik belirli mimari bölümdür.","branch_image_ar":"موضع مكسور أو مزحوم عند الكعبة","concept_gloss":"kutsal yapının yağmur oluğu yanındaki belirli bölümü veya duvarı","contextual_glosses":[{"applicability":"Özel yer adının kullanılmadığı açıklayıcı metinlerde konumu okura doğrudan bildirmek için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kaynaklarda değişen bölüm veya duvar göndergesini açıkça belirtmez.","preserves":"Kutsal yapıyla ilişkiyi ve yağmur oluğu tarafındaki belirli konumu korur."},"facet_ids":["F001"],"text":"yağmur oluğu yanındaki kutsal bölüm","usage_role":"explanatory"}],"definition":"Kutsal yapının yağmur oluğu tarafındaki belirli bölüm veya bu bölümün duvarıdır. Yapının dışında bırakılmış bölüm olması ve ziyaretçi kalabalığının sıkışması, adlandırmaya ilişkin farklı açıklamalardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderge, kutsal yapının yağmur oluğu tarafındaki belirli bölüm veya bu bölümün duvarıdır."},{"facet_id":"F002","role":"source_variant","statement":"Kaynaklar yeri kimi zaman belirli bölüm, kimi zaman onun duvarı veya yağmur oluğunun bulunduğu bölüm diye sınırlar."},{"facet_id":"F003","role":"source_variant","statement":"Adın kökeni, bölümün ana yapının dışında ve eksik bırakılmasıyla ya da ziyaretçi kalabalığının sıkıştırıcı etkisiyle açıklanır."}],"identity_rationale":"Kaynak ifadesinin güvenilir kimliği, kutsal yapının yağmur oluğu tarafındaki belirli bölüm veya bu bölümün duvarıdır. Yapının eksik bırakılması veya kalabalığın birbirini sıkıştırması, yerin kendisi değil, adın kaynağına ilişkin farklı açıklamalardır; bu nedenle geçici görüntü yer kimliği merkez alınarak yeniden çerçevelenmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kutsal yapının yağmur oluğu tarafındaki belirli bölüm veya onun duvarı"}],"lexicalization_note":"Çıplak dal, özel bir tamlamaya bağlı olmadan belirli yerin geleneksel adı olarak tanımlanır; adın köken açıklamaları kimliğe dönüştürülmez.","neighbor_coverage_note":"Bütün aday yer kartları değerlendirildi; seçilenler belirli mimari bölümü genel çevrili mekan, kutsal yapının bütünü ve yol üzerindeki başka yerden ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnızca o belirli kutsal yerin adıdır; komşu dal aynı yeri de kapsayabilen fakat genel çevrili mekanlara yayılan daha geniş bir alandır.","focus_only":"Tek ve belirli bir kutsal bölüm, yağmur oluğu tarafındaki konumuyla sınırlandırılır.","gloss":"duvarla çevrili kutsal bölüm","neighbor_only":"Duvarla çevrili yer, oda, bahçe ve yerleşim çevresi gibi genel ve çok sayıda gönderge bulunur.","neighbor_ref":"root_000296/B004","relation_type":"near_synonym","shared_zone":"İki dal, kutsal yapının belirli bölümü veya onun duvarı göndergesinde örtüşür."},{"boundary_match":"field_only","distinction":"Odak dal yapıya bitişik belirli bölümü gösterir; komşu dal ise yapının tamamını veya daha geniş yerleşimi adlandırır.","focus_only":"Gönderge, kutsal yapının tamamı değil, yağmur oluğu yanındaki çevrili bölümüdür.","gloss":"kutsal yapı ve bölümü","neighbor_only":"Kutsal yapının bütünü veya onu barındıran kutsal şehir adlandırılır.","neighbor_ref":"root_000156/B003","relation_type":"same_field","shared_zone":"İki dal aynı kutsal yapı ve onun bulunduğu kutsal yer alanına aittir."},{"boundary_match":"thematic_only","distinction":"Odak dal kutsal yapının mimari bir parçasına bitişiktir; komşu dal uzaktaki bir geçiş ve hazırlık noktasıdır, anlamsal ikame yoktur.","focus_only":"Kutsal yapıya doğrudan bitişik mimari bölüm söz konusudur.","gloss":"kutsal yol üzerindeki yer","neighbor_only":"Başka bir bölgede bulunan ve belirli yönden gelenlerin geçiş sınırı sayılan ayrı bir yer söz konusudur.","neighbor_ref":"root_001378/B010","relation_type":"thematic","shared_zone":"İki dal aynı kutsal yolculuk ve kutsal bölge senaryosunda anılan belirli yer adlarıdır."}],"source_phrase_ar":"الحَطِيم حجر مكة (ayn)؛ الحَطِيم الجدر يعني جدار حجر الكعبة (sihah)؛ الحَطِيم الذي فيه الميزاب وإنما سمي حطيما لأن البيت رفع وترك ذاك محطوما (tahdhib)؛ الحَطِيم وزمزم مكانان (mufradat)؛ الحَطِيم ممكن أن يكون من هذا وهو الحجر لكثرة من ينتابه كأنه يحطم (maqayis)","source_summary":"Toplu kanıt belirli kutsal bölgeyi ortak gönderge yapar; bölüm, onun duvarı ve yağmur oluğu tarafı betimleri aynı yerin sınırlarını gösterirken iki ayrı adlandırma açıklaması sunulur.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الحَطِيم موضع حجر مكة أو جدار حجر الكعبة مما يلي الميزاب","what_is_not_ar":"ليس زمزم ولا كل موضع مكسور"},"support_links":[]},{"boundary":"Aşırı yiyen kişi ile öğüten veya sindiren şey birbirinin yerine geçmez; yalnızca tüketme görüntüsünü paylaşır.","branch_kind":"bare","branch_ref":"root_000337/B008","candidate_links":[{"candidate_id":"cand_83fac0b5c240df2acaa0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حُطَمَة","morph_features":"STEM|POS:N|LEM:HuTamap|ROOT:HTm|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:4:4:2","qac_word_ref":"104:4:4","surface_ar":"حُطَمَةِ"}],"gloss":"aşırı yiyen kişi veya yiyeceği öğütüp sindiren şey","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, çok miktarda ve önünde kalanı tüketircesine yemekle nitelenir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Öğütücü diş, sindirim organı veya benzer şey, yiyeceği parçalama ve sindirme işleviyle adlandırılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çok yiyen kişi, önüne geleni yok eden şiddetli ateşe benzetilerek açıklanır."}}],"root_ar":"ح ط م","root_id":"root_000337","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişi ve araç ya da organ göndergelerini ayrı seçenekler olarak koruyan açıklayıcı üst karşılıktır.","boundary_detail":"Aşırı yiyen kişi ile öğüten veya sindiren şey birbirinin yerine geçmez; yalnızca tüketme görüntüsünü paylaşır.","branch_image_ar":"أكول يهضم كأنه نار أو جارسة","concept_gloss":"aşırı yiyen kişi veya yiyeceği öğütüp sindiren şey","contextual_glosses":[{"applicability":"Yalnızca çok yiyen kişinin niteliğini veren insan bağlamlarında kısa ve doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öğütücü diş veya sindirim organı anlamını ve ateşe benzetme gerekçesini taşımaz.","preserves":"Kişinin aşırı ve çok yemek yeme niteliğini doğal biçimde korur."},"facet_ids":["F001"],"text":"obur","usage_role":"contextual"},{"applicability":"Dişin veya sindirimle görevli bir organın yiyecek üzerindeki işlevinin anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çok yiyen kişi anlamını ve onun şiddetli ateşe benzetilmesini dışarıda bırakır.","preserves":"Yiyeceği parçalama, öğütme ve sindirme işlevini korur."},"facet_ids":["F002"],"text":"öğütüp sindiren","usage_role":"contextual"}],"definition":"Bir kullanımda çok ve durmaksızın yiyen kişiyi, başka bir kullanımda ise yiyeceği öğütüp sindiren diş, organ veya şeyi anlatır. İki görünüm, önüne geleni yok edercesine tüketme düşüncesinde birleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, çok miktarda ve önünde kalanı tüketircesine yemekle nitelenir."},{"facet_id":"F002","role":"extension","statement":"Öğütücü diş, sindirim organı veya benzer şey, yiyeceği parçalama ve sindirme işleviyle adlandırılır."},{"facet_id":"F003","role":"associated_use","statement":"Çok yiyen kişi, önüne geleni yok eden şiddetli ateşe benzetilerek açıklanır."}],"identity_rationale":"Kaynak ifadesi çok yiyen kişiyi ve yiyeceği öğütüp sindiren diş ya da organı aynı tüketme benzetmesi çevresinde toplar, fakat bunlar aynı gönderge değildir. Dal ortak işlevsel görüntüyle korunabilir; kişi niteliği ile öğütücü veya sindirici araç anlamı ayrı yüzler olarak yazılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"çok yiyen, obur kimse"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"yiyeceği öğüten diş veya sindiren organ"}],"lexicalization_note":"Çıplak dalda bulunan iki biçimin kişi ve öğütücü organ göndergeleri ayrı tutulur; biri ötekinin genel tanımı yapılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen üç yakın dal kişi anlamındaki örtüşmeyi ve odak dalın öğütücü veya sindirici uzantısını en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Kişi anlamında yakın karşılık vardır, ancak odak dalın ateş benzetmesi ve öğütücü ya da sindirici şey uzantısı komşu dalda bulunmaz.","focus_only":"Çok yiyen kişi ateş gibi tüketici oluşuyla açıklanır ve dal ayrıca öğütücü ya da sindirici şeyi kapsar.","gloss":"çok yiyen kişi","neighbor_only":"Çok yeme niteliği özellikle yutma eylemi çevresindeki çeşitli kişi biçimleriyle anlatılır.","neighbor_ref":"root_000150/B005","relation_type":"near_synonym","shared_zone":"İki dal insanı olağandan çok yiyen ve önündeki yiyeceği hızla tüketen kişi olarak niteler."},{"boundary_match":"partial","distinction":"Odak dal kişi anlamından öğütme ve sindirme işlevine uzanır; komşu dal ise yoğun yeme davranışını insan dışı yiyicilere genişletir.","focus_only":"Öğütücü veya sindirici organ uzantısı ve ateş gibi tüketme benzetmesi bulunur.","gloss":"hiçbir şey bırakmadan yemek","neighbor_only":"Her şeyi yiyen hayvan ve ağaçları kırarak yiyen deve gibi insan dışı yiyici örnekleri bulunur.","neighbor_ref":"root_000236/B003","relation_type":"near_synonym","shared_zone":"İki dal çok güçlü iştahı ve önündeki yiyeceği geride bir şey bırakmadan tüketen kişiyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal ayrıca öğütücü ve sindirici göndergeleri kapsar; komşu dal kişi üzerindeki silip süpürürcesine yeme biçimiyle sınırlıdır.","focus_only":"Ateşe benzetilen oburluk ve yiyeceği öğütüp sindiren şey anlamı vardır.","gloss":"silip süpüren yiyici","neighbor_only":"Yiyenin geride hiçbir şey bırakmaması, sürükleyip götüren bir güç görüntüsüyle özellikle vurgulanır.","neighbor_ref":"root_000238/B004","relation_type":"near_synonym","shared_zone":"İki dal da çok yiyen ve önündeki yiyeceği bütünüyle tüketen kişiyi niteler."}],"source_phrase_ar":"رجل حُطَمَة للكثير الأكل (sihah;tahdhib)؛ قيل للأكول حُطَمَة تشبيها بالجحيم (mufradat)؛ يقال للجوارس حاطوم وهاضوم (tahdhib)","source_summary":"Toplu kanıt çok yiyen kişi anlamını ve yiyeceği öğütüp sindiren şey anlamını verir; bunları birbirine bağlayan nokta, karşısındakini tüketen parçalayıcı işlevdir.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه الرجل الأكول والحاطوم للجوارس أو الهاضوم","what_is_not_ar":"ليس الراعي العنيف ولا اسم النار نفسه"},"support_links":["sup_65416a2aba224274a831"]},{"boundary":"Dal maddi kırık döküntüyü değil, yalnızca dünya malı ve süsünün geçiciliğini bildiren kısıtlı kullanımı kapsar.","branch_kind":"non_bare","branch_ref":"root_000337/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حُطَمَة","morph_features":"STEM|POS:N|LEM:HuTamap|ROOT:HTm|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:4:4:2","qac_word_ref":"104:4:4","surface_ar":"حُطَمَةِ"}],"gloss":"dünyanın yok olup gidecek malı ve süsü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderge, dünyada sahip olunan mal, görünür süs ve diğer dünyalıklardır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu dünyalıkların ayırt edici niteliği, kalıcı olmamaları ve sonunda yok olup gitmeleridir."}}],"root_ar":"ح ط م","root_id":"root_000337","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kısıtlı söz öbeğinin maddi dünya varlıkları ile onların geçicilik niteliğini birlikte veren tam karşılığıdır.","boundary_detail":"Dal maddi kırık döküntüyü değil, yalnızca dünya malı ve süsünün geçiciliğini bildiren kısıtlı kullanımı kapsar.","branch_image_ar":"حطام الدنيا الزائل","concept_gloss":"dünyanın yok olup gidecek malı ve süsü","contextual_glosses":[{"applicability":"Dünyada edinilen varlıkların kalıcı olmadığını vurgulayan doğal ve kısa metin bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Görünür süs ve diğer geçici dünya mallarını ayrı ayrı belirtmez.","preserves":"Dünya malı göndergesini ve onun geçici oluşunu açık biçimde korur."},"facet_ids":["F001","F002"],"text":"geçici dünya malı","usage_role":"general"}],"definition":"Dünyada edinilen mal, görünür süs ve diğer dünyalıkların kalıcı olmayıp sonunda yok olacak bütünü için kullanılan kısıtlı anlatımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderge, dünyada sahip olunan mal, görünür süs ve diğer dünyalıklardır."},{"facet_id":"F002","role":"core","statement":"Bu dünyalıkların ayırt edici niteliği, kalıcı olmamaları ve sonunda yok olup gitmeleridir."}],"identity_rationale":"Kaynak ifadesi dünyanın malını, süsünü ve geçici dünyalıklarını kalıcı olmayıp yok olacak şeyler olarak tanımlar. Geçici çerçeve hem göndergeyi hem de geçicilik sınırını doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"dünyanın geçici malı ve süsü"}],"lexicalization_note":"Anlam yalnızca dünya malını ve süsünü belirten kısıtlı söz öbeğine aittir; çıplak biçime genel bir soyut anlam olarak taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler geçici dünya malını genel mal ve eşya ile özellikle değer verilen nesneden ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dünyalıkların geçiciliğini zorunlu kılar; komşu dal mal türü, bedel ve pay anlamlarına açılır ve yok olma değerlendirmesini gerektirmez.","focus_only":"Dünya malının kalıcı olmayıp yok olması, anlamın zorunlu değerlendirmesidir.","gloss":"dünya malı","neighbor_only":"Nakit dışı mal, bir hakkın karşılığında verilen bedel ve kişiye düşen pay gibi işlemsel anlamlar bulunur.","neighbor_ref":"root_001001/B008","relation_type":"near_synonym","shared_zone":"İki dal dünyada edinilen malı ve maddi varlığı adlandırma alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal malın geçici ve yok olacak oluşunu bildirir; komşu dal eşya türlerini ve mal çokluğunu değer yargısı eklemeden anlatır.","focus_only":"Mal ve süs, sonunda yok olacak geçici dünyalıklar olarak değerlendirilir.","gloss":"mal ve eşya","neighbor_only":"Ev eşyası, döşeme ve çok miktarda mal, kalıcılığına ilişkin bir yargı olmadan adlandırılır.","neighbor_ref":"root_000010/B002","relation_type":"near_neighbor","shared_zone":"İki dal kişinin sahip olduğu maddi mallar ve görünür eşyalar alanında kesişir."},{"boundary_match":"field_only","distinction":"Odak dal bütün dünyalıkları geçicilik açısından küçültür; komşu dal belirli bir nesnenin nadirliği ve sahibince korunması üzerinde durur.","focus_only":"Dünya malının yok olup gideceği ve kalıcı değer taşımadığı vurgulanır.","gloss":"değer verilen mal","neighbor_only":"Nadir, değerli ve sahibinin bırakmak istemediği belirli bir mal veya nesne öne çıkar.","neighbor_ref":"root_001039/B007","relation_type":"same_field","shared_zone":"İki dal insanın sahip olduğu ve değer biçtiği maddi şeyler alanına aittir."}],"source_phrase_ar":"حُطام الدنيا عرضها وأثرها وزينتها (tahdhib)؛ حُطام الدنيا كل ما فيها من مال يفنى ولا يبقى (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu kısıtlı kullanım, dünyanın malını ve süsünü kalıcı olmayıp yok olacak şeyler diye açıklar."}],"source_summary":"Kanıt, dünya malı ve süsünü geçici ve yok olmaya yazgılı şeyler olarak sunan kısıtlı kullanımı tek başına doğrular.","sources":["TA"],"what_is_ar":"يدخل فيه حُطام الدنيا أي عرضها وزينتها ومالها الفاني","what_is_not_ar":"ليس حُطام اليبس الحسي ولا اسم النار"},"support_links":[]},{"boundary":"Dal, yana çekilme, az miktar, özel satış biçimi, içecek, bırakılmış çocuk ve yere konan yastık anlamlarını kapsamaz.","branch_kind":"bare","branch_ref":"root_001466/B001","candidate_links":[{"candidate_id":"cand_48f791e38f8a434e20ec","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَبَذَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:naba*a|ROOT:nb*|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:4:2:2","qac_word_ref":"104:4:2","surface_ar":"يُنۢبَذَ"}],"gloss":"elden atma veya değersiz sayıp bir yana bırakma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel işlem, bir nesneyi elden çıkararak öne ya da arkaya doğru atmaktır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Atma işlemi, nesneyi önemsememe ve onu gözden çıkarma tutumunu da taşıyabilir."}}],"root_ar":"ن ب ذ","root_id":"root_001466","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem somut elden atma işlemini hem de bu işleme eşlik edebilen önemsememe yönünü birlikte temsil eder.","boundary_detail":"Dal, yana çekilme, az miktar, özel satış biçimi, içecek, bırakılmış çocuk ve yere konan yastık anlamlarını kapsamaz.","branch_image_ar":"الطرح والإلقاء","concept_gloss":"elden atma veya değersiz sayıp bir yana bırakma","contextual_glosses":[{"applicability":"Bir nesnenin gerçekten elden öne veya arkaya atıldığı somut bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nesneyi değersiz sayma veya gözden çıkarma tutumunu zorunlu olarak anlatmaz.","preserves":"Somut elden atma işlemini açık ve doğal biçimde korur."},"facet_ids":["F001"],"text":"elinden atmak","usage_role":"contextual"},{"applicability":"Atma eyleminin bir şeyi önemsememeyi özellikle bildirdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Önemsememe içermeyen yalın fiziksel atma kullanımını kapsamaz.","preserves":"Değersiz sayma tutumunu ve ona bağlı uzaklaştırmayı korur."},"facet_ids":["F002"],"text":"gözden çıkarıp bir yana atmak","usage_role":"contextual"}],"definition":"Bir şeyi elden öne ya da arkaya doğru atmak veya fırlatmak; bazı bağlamlarda bunu, o şeyi değersiz sayıp bir yana bırakma tutumuyla yapmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel işlem, bir nesneyi elden çıkararak öne ya da arkaya doğru atmaktır."},{"facet_id":"F002","role":"extension","statement":"Atma işlemi, nesneyi önemsememe ve onu gözden çıkarma tutumunu da taşıyabilir."}],"identity_rationale":"Kaynak ifadesi, bir şeyi elden öne ya da arkaya atma eylemini temel anlam olarak verir ve bu eylemin kimi kullanımlarda o şeyi önemsememeyi gösterdiğini belirtir. Sunulan dal çerçevesi bu fiziksel işlem ile ona bağlı değersiz sayma yönünü birlikte doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi elinden atmak veya önemsemeyip bir yana bırakmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şeyi tekrar tekrar ya da çokça atmak"}],"lexicalization_note":"Tanım yalın atma eylemine bağlıdır; öteki dallardaki söz öbeklerine özgü savaş, satış veya miktar anlamları buraya taşınmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; elden atma çekirdeğini en iyi sınayan iki yakın anlamlı komşu seçildi, yalnızca aynı sahneyi paylaşan uzak adaylar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği failin nesneyi elinden atmasıdır; komşu dal ise düşürme, üzerinden atma ve kırılıp düşme gibi daha geniş sonuç türlerine uzanır.","focus_only":"Odak dal, elden atmayı ve kimi bağlamlarda değersiz sayarak bir yana bırakmayı öne çıkarır.","gloss":"atıp düşürme","neighbor_only":"Komşu dal, bir şeyden düşürmeyi ve diş ucunun kırılıp düşmesi gibi kendiliğinden sonuçları da kapsar.","neighbor_ref":"root_000513/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyi bulunduğu yerden atma veya düşürme yoluyla uzaklaştırma alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu dal genel bir atma ve dışlama alanıdır; odak dal ise elden çıkarma sahnesini ve buna bağlanabilen önemsememe tutumunu merkez alır.","focus_only":"Odak dal, nesnenin elden öne ya da arkaya atılmasını belirgin bir işlem olarak sınırlar.","gloss":"atıp uzağa bırakma","neighbor_only":"Komşu dal, el kullanımı şart olmadan fırlatma, uzağa kaldırma ve değersiz bir durumda bırakılmayı daha geniş biçimde kapsar.","neighbor_ref":"root_000929/B001","relation_type":"near_synonym","shared_zone":"İki dal da atma ve bir şeyi önem alanının dışına çıkarma anlamlarında güçlü biçimde örtüşür."}],"source_phrase_ar":"أصل صحيح يدل على طرح وإلقاء (maqayis)؛ نبذت الشيء أنبذه نبذا إذا ألقيته من يدك (jamhara;sihah)؛ النبذ طرحك الشيء من يدك أمامك أو خلفك (tahdhib)؛ النبذ إلقاء الشيء وطرحه لقلة الاعتداد به (mufradat)","source_summary":"Kaynaklar elden atma işlemini ortak çekirdek olarak verir; bazıları yönün öne veya arkaya olabileceğini, biri de eylemin az önem verme tutumunu gösterebildiğini açıklar.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"إلقاء الشيء وطرحه من اليد أو عن الاعتداد به","what_is_not_ar":"الانتحاء إلى ناحية؛ القلة اليسيرة؛ النبيذ؛ المنابذة في العهد أو الحرب أو البيع"},"support_links":["sup_c190bb38923e1f1d4bba"]},{"boundary":"Her açık düşmanlık bu dala girmez; anlaşmayı sona erdirme okumasında karşı tarafa açık bildirim ve eşit bilgilenme koşulu korunmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001466/B002","candidate_links":[{"candidate_id":"cand_83f15fc7c30c038e778b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَبَذَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:naba*a|ROOT:nb*|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:4:2:2","qac_word_ref":"104:4:2","surface_ar":"يُنۢبَذَ"}],"gloss":"ilişkiyi açıkça kesip karşı tarafa çatışmayı bildirme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Taraflardan biri ötekinden düşmanlıkla ayrılır ve aralarındaki karşıtlığı gizli olmaktan çıkarır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Anlaşma veya barışın sona erdirilmesi, karşı tarafa açıkça bildirilerek iki tarafın da durumdan eşit ölçüde haberdar olması sağlanır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Açık ayrışmanın sonucu olarak taraflar çatışma veya savaş durumuna geri döner."}}],"root_ar":"ن ب ذ","root_id":"root_001466","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Düşmanlıkla ayrılma çekirdeğini ve anlaşma bağlamındaki açık, eşit bilgili bildirim koşulunu birlikte gösterir.","boundary_detail":"Her açık düşmanlık bu dala girmez; anlaşmayı sona erdirme okumasında karşı tarafa açık bildirim ve eşit bilgilenme koşulu korunmalıdır.","branch_image_ar":"مناجزة الخصم بالنبذ","concept_gloss":"ilişkiyi açıkça kesip karşı tarafa çatışmayı bildirme","contextual_glosses":[{"applicability":"Bir kişinin hasmından düşmanlıkla ayrıldığı ve karşıtlığını açıkça ortaya koyduğu kullanım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Anlaşmanın eşit bilgi koşulunda sona erdirilmesine özgü bildirim aşamasını kapsamaz.","preserves":"Düşmanlıkla ayrılma ve karşıtlığı açık etme çekirdeğini korur."},"facet_ids":["F001"],"text":"düşmanlığını açık edip ayrılmak","usage_role":"contextual"},{"applicability":"Karşı tarafa anlaşmanın bittiğinin açıkça bildirildiği ve iki tarafın eşit bilgiyle çatışma durumuna döndüğü özel kalıp içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Açık bildirim, eşit bilgilenme ve çatışmaya dönüş aşamalarını korur."},"facet_ids":["F002","F003"],"text":"anlaşmayı açıkça bozup çatışmaya dönmek","usage_role":"explanatory"}],"definition":"Bir hasımla ilişkiyi düşmanlık içinde kesip karşıtlığı açık hale getirmektir. Anlaşma veya barış bağlamındaki özel kalıpta, sona erdirme kararını karşı tarafa eşit bilgi sağlayacak biçimde bildirip çatışma durumuna dönmeyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Taraflardan biri ötekinden düşmanlıkla ayrılır ve aralarındaki karşıtlığı gizli olmaktan çıkarır."},{"facet_id":"F002","role":"specialization","statement":"Anlaşma veya barışın sona erdirilmesi, karşı tarafa açıkça bildirilerek iki tarafın da durumdan eşit ölçüde haberdar olması sağlanır."},{"facet_id":"F003","role":"associated_use","statement":"Açık ayrışmanın sonucu olarak taraflar çatışma veya savaş durumuna geri döner."}],"identity_rationale":"Kaynak ifadesi hem bir hasımdan düşmanlıkla ayrılıp karşıtlığı açığa vurmayı hem de barış veya anlaşma durumunu karşı tarafla eşit bilgi koşulunda sona erdirerek çatışmaya dönmeyi anlatır. Dalın genel çerçevesi kullanılabilir, ancak yalın karşı çıkış ile belirli bildirim kalıbı birbirine karıştırılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"birinden düşmanlıkla ayrılıp karşısına açıkça çıkmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"anlaşmanın bittiğini eşit bilgi koşulunda bildirip çatışmaya dönmek"}],"lexicalization_note":"Yalın olmayan karşılıklı ayrışma biçimi ile anlaşmayı açık bildirimle sona erdiren söz öbeği ayrı yüzler olarak tanımlanır; özel koşul bütün dala yayılmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; açık düşmanlığı başlatan yakın komşu ile anlaşmayı kuran tematik karşı yön, dalın ayrılma ve bildirim sınırını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ayrılma ya da anlaşmayı bildirerek sona erdirme üzerinden çatışmaya geçer; komşu dalın çekirdeği ise düşmanlığı doğrudan başlatmaktır.","focus_only":"Odak dal, mevcut ilişki veya anlaşmanın açıkça kesilmesini ve kimi kullanımda eşit bilgili bildirimi içerir.","gloss":"açık düşmanlığı başlatma","neighbor_only":"Komşu dal, daha önceki bir anlaşmayı sona erdirme koşulu olmadan düşmanlığı ilk kez açıkça başlatmayı anlatır.","neighbor_ref":"root_001302/B004","relation_type":"near_neighbor","shared_zone":"İki dalda da düşmanlık gizli olmaktan çıkar ve karşı taraf açık bir karşıtlıkla yüz yüze gelir."},{"boundary_match":"thematic_only","distinction":"Komşu dal anlaşmayı kurar veya pekiştirir; odak dal ise belirli koşullarda onu açıkça sona erdirip çatışma durumuna geçer.","focus_only":"Odak dal, bağlayıcı ilişkiyi açık bildirimle sona erdirme ve karşıtlığa geçme yönündedir.","gloss":"sağlam anlaşma kurma","neighbor_only":"Komşu dal, yemin veya sözle güçlendirilmiş bir anlaşmayı kurma ve sağlamlaştırma yönündedir.","neighbor_ref":"root_001623/B004","relation_type":"thematic","shared_zone":"Her iki dal taraflar arasındaki anlaşmanın durumu ve karşılıklı yükümlülük sahnesiyle ilgilidir."}],"source_phrase_ar":"نابذ فلان فلانا إذا فارقه عن قلى (jamhara)؛ نابذه الحرب كاشفه (sihah)؛ نابذناهم الحرب ونبذنا إليهم الحرب على سواء (tahdhib)؛ فانبذ إليهم على سواء فمعناه ألق إليهم السلم (mufradat)","source_summary":"Kaynaklar düşmanlıkla ayrılma ve karşıtlığı açık etme noktasında birleşir; anlaşma bağlamındaki kullanım, karşı tarafın da aynı bilgi düzeyine getirildiği açık bir sona erdirme bildirimiyle sınırlandırılır.","sources":["JA","SI","TA","MU"],"what_is_ar":"نبذ العهد أو الحرب إلى الطرف الآخر على سواء؛ والمفارقة والمكاشفة في الخصومة","what_is_not_ar":"مطلق طرح الأجسام؛ الانتحاء المكاني؛ بيع المنابذة"},"support_links":["sup_bdfe0ae4d4049c76fe0f"]},{"boundary":"Anlam yalnızca atma hareketinin satışı kesinleştiren işaret sayıldığı özel işlem için geçerlidir; genel satış veya genel atma anlamına genişletilemez.","branch_kind":"collocation","branch_ref":"root_001466/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَبَذَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:naba*a|ROOT:nb*|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:4:2:2","qac_word_ref":"104:4:2","surface_ar":"يُنۢبَذَ"}],"gloss":"atma işaretinin satışı kesinleştirdiği satış biçimi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir nesneyi karşı tarafa atma hareketi, satış iradesini gösteren işlem işlevi görür."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Atma gerçekleştiğinde satış tamamlanmış ve taraflar için bağlayıcı sayılır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Atılan şey kumaş, başka bir ticaret malı veya bu amaçla kullanılan bir taş olabilir."}}],"root_ar":"ن ب ذ","root_id":"root_001466","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Atılan nesnenin yalnızca teslim edilmediği, aynı zamanda satışın bağlayıcılık işareti olduğu özel işlem için kullanılır.","boundary_detail":"Anlam yalnızca atma hareketinin satışı kesinleştiren işaret sayıldığı özel işlem için geçerlidir; genel satış veya genel atma anlamına genişletilemez.","branch_image_ar":"إيجاب البيع بالنبذ","concept_gloss":"atma işaretinin satışı kesinleştirdiği satış biçimi","contextual_glosses":[{"applicability":"Kısa adlandırmanın yeterli olduğu ve atışın hangi nesneyle yapıldığının bağlamdan anlaşıldığı durumlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kumaş, mal veya taş seçeneklerini ve karşı tarafa yönelme ayrıntısını açıkça söylemez.","preserves":"Atma hareketinin satışı kesinleştiren işlevini korur."},"facet_ids":["F001","F002"],"text":"atışla kesinleşen satış","usage_role":"general"}],"definition":"Taraflardan birinin kumaşı, başka bir malı ya da bir taşı ötekine atmasının satışın tamamlandığını ve bağlayıcı olduğunu gösterdiği özel bir satış biçimidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir nesneyi karşı tarafa atma hareketi, satış iradesini gösteren işlem işlevi görür."},{"facet_id":"F002","role":"specialization","statement":"Atma gerçekleştiğinde satış tamamlanmış ve taraflar için bağlayıcı sayılır."},{"facet_id":"F003","role":"example","statement":"Atılan şey kumaş, başka bir ticaret malı veya bu amaçla kullanılan bir taş olabilir."}],"identity_rationale":"Kaynak ifadesi, kumaşın, başka bir malın ya da bir taşın atılmasını satışın bağlayıcı hale geldiğini gösteren işlem olarak tanımlar. Dal çerçevesi bu özel satış düzenini doğru verir ve onu genel atma anlamından ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kumaş, mal veya taş atılınca bağlayıcı hale gelen satış"}],"lexicalization_note":"Tanım yalnızca belirli satış söz öbeğine bağlıdır; atma eylemine veya bütün satış türlerine yalın bir kök anlamı olarak yüklenmez.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; genel satış dalı ile koşul ve işaret dalı, bu kullanımın yalnızca atışla bağlayıcılık kazanan özel bir satış olduğunu en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Komşu dal satışın genel kavramıdır; odak dal yalnızca atma hareketinin işlemi kesinleştirdiği tarihsel ve özel satış düzenidir.","focus_only":"Odak dalda belirli bir nesneyi atma hareketi satışın bağlayıcılık işaretidir.","gloss":"genel alım satım","neighbor_only":"Komşu dal, bedel ile malın değiştirilmesine dayanan genel alım satım işlemini kapsar.","neighbor_ref":"root_000169/B001","relation_type":"same_field","shared_zone":"Her iki dal da alıcı ile satıcı arasındaki mal değişimi ve satışın kurulması alanında yer alır."},{"boundary_match":"partial","distinction":"Odak dalda işaret belirli bir atma eylemidir ve doğrudan satış sonucunu doğurur; komşu dalın koşul ve işaret alanı bundan çok daha geniştir.","focus_only":"Odak dal, atılan nesnenin işaret sayılmasıyla satışın kendiliğinden bağlayıcı hale gelmesini gerektirir.","gloss":"satış koşulu veya işareti","neighbor_only":"Komşu dal, satışta tarafların koyduğu koşulları ve daha genel işaret kavramını birlikte kapsar.","neighbor_ref":"root_000788/B001","relation_type":"near_neighbor","shared_zone":"İki dal da bir satışın nasıl tanındığı veya hangi işlemle hüküm kazandığı sorusuna dokunur."}],"source_phrase_ar":"المنابذة أن يقول الرجل لصاحبه انبذ إلي الثوب أو غيره من المتاع أو أنبذه إليك وقد وجب البيع؛ إذا نبذت الحصاة إليك فقد وجب البيع","source_qualifications":[{"kind":"sole_attestation","summary":"Kumaşın, malın veya taşın atılması satışın kesinleşme işareti sayılır ve işlem bu hareketle bağlayıcı hale gelir."}],"source_summary":"Ortak kaynak özeti yoktur; bu özel satış işlemi eldeki kanıtta tek bir sözlükçe tanıklanmıştır.","sources":["TA"],"what_is_ar":"بيع يجعل نبذ الثوب أو المتاع أو الحصاة علامة لوجوب البيع","what_is_not_ar":"منابذة العهد والحرب؛ مطلق الطرح؛ الانتحاء إلى ناحية"},"support_links":[]},{"boundary":"Dal, genel ayrılmayı değil yana yönelme veya yan tarafta bulunma ilişkisini gerektirir; gizlilik, hız ya da topluluktan kopma zorunlu değildir.","branch_kind":"bare","branch_ref":"root_001466/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَبَذَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:naba*a|ROOT:nb*|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:4:2:2","qac_word_ref":"104:4:2","surface_ar":"يُنۢبَذَ"}],"gloss":"bir yana çekilme veya kenarda bulunma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bir yana yönelir ve yan taraftaki bir konuma çekilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hareketin sonucu olan yan konum, bir kenarda oturma veya bulunma yeri olarak da adlandırılır."}}],"root_ar":"ن ب ذ","root_id":"root_001466","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem yan tarafa doğru hareketi hem de bu hareketin ulaştığı kenar konumunda oturma veya bulunmayı kapsar.","boundary_detail":"Dal, genel ayrılmayı değil yana yönelme veya yan tarafta bulunma ilişkisini gerektirir; gizlilik, hız ya da topluluktan kopma zorunlu değildir.","branch_image_ar":"الانتحاء إلى ناحية","concept_gloss":"bir yana çekilme veya kenarda bulunma","contextual_glosses":[{"applicability":"Kişinin bulunduğu yerden yan tarafa gittiği hareket bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yan tarafta oturulan yer veya kalıcı konum anlamını kapsamaz.","preserves":"Bir yana yönelme ve merkezden yan tarafa geçme işlemini korur."},"facet_ids":["F001"],"text":"bir yana çekilmek","usage_role":"contextual"},{"applicability":"Bir kişinin yan taraftaki bir yerde oturup bulunduğu durumlar için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"O konuma doğru gitme veya çekilme hareketini kapsamaz.","preserves":"Yan konumda oturma ve orada bulunma sonucunu korur."},"facet_ids":["F002"],"text":"kenarda oturmak","usage_role":"contextual"}],"definition":"Bulunulan çizgiden veya merkezden bir yana gidip yan tarafa çekilmek ya da yan taraftaki bir yerde oturup orada bulunmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bir yana yönelir ve yan taraftaki bir konuma çekilir."},{"facet_id":"F002","role":"extension","statement":"Hareketin sonucu olan yan konum, bir kenarda oturma veya bulunma yeri olarak da adlandırılır."}],"identity_rationale":"Kaynak ifadesi hem bir yana gidip çekilmeyi hem de yan taraftaki bir yerde oturmayı açıkça tanıklar. Sunulan dal bu ortak yan konuma yönelme veya orada bulunma çekirdeğini doğru biçimde bir araya getirir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bir yana gitmek veya kenara çekilmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"yan tarafta oturulan yer veya kenar"}],"lexicalization_note":"Tanım yalın yan tarafa yönelme ve yan konumda bulunma alanında tutulur; özel savaş, satış veya miktar kalıpları buraya alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızlaşmayı ekleyen yakın anlamlı dal ile gizliliği ekleyen yakın komşu, yalın yan konum sınırını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal için yan konum yeterlidir ve yalnızlık gerekmez; komşu dalda gruptan ayrılma ve tek başına kalma belirleyici olabilir.","focus_only":"Odak dal yan tarafa yönelmeyi ve yan konumda oturmayı birlikte kapsar.","gloss":"kenara çekilip yalnızlaşma","neighbor_only":"Komşu dal topluluktan ayrılma ve tek başına kalma sonucunu ayrıca öne çıkarır.","neighbor_ref":"root_000305/B004","relation_type":"near_synonym","shared_zone":"İki dal da merkezden veya topluluktan yana doğru çekilme hareketinde örtüşür."},{"boundary_match":"partial","distinction":"Komşu dalın çekirdeğinde gizlilik ve fark ettirmeden ayrılma vardır; odak dal yalnızca yana yönelme ve yan konumla sınırlıdır.","focus_only":"Odak dal açıkça bir yana gitmeyi veya kenarda bulunmayı anlatır ve gizlilik koşulu taşımaz.","gloss":"gizlice sıyrılıp gitme","neighbor_only":"Komşu dal kişinin topluluğundan gizlice sıyrılıp gitmesini veya kendini onlardan saklamasını gerektirir.","neighbor_ref":"root_000700/B004","relation_type":"near_neighbor","shared_zone":"Her iki dalda da kişi bir topluluğun veya başlangıç konumunun dışına doğru hareket eder."}],"source_phrase_ar":"جلس فلان نبذة ونبذة أي ناحية (sihah;tahdhib)؛ انتبذ فلان أي ذهب ناحية (sihah)؛ انتبذ فلان ناحية إذا انتحى ناحية (tahdhib)","source_summary":"Kaynaklar bir yana gitme veya yönelme ile yan taraftaki bir yerde oturma kullanımlarını aynı yan konum çekirdeği altında birlikte verir.","sources":["SI","TA"],"what_is_ar":"الجلوس في ناحية أو الذهاب والانتحاء إلى ناحية","what_is_not_ar":"طرح الشيء من اليد؛ نقض العهد؛ القلة اليسيرة"},"support_links":[]},{"boundary":"Anlam genel küçüklük değildir; belirli söz öbeklerinde az miktarı, yalın ad kullanımında ise belirli maddelerden küçük bir parçayı bildirir.","branch_kind":"mixed_non_bare","branch_ref":"root_001466/B005","candidate_links":[{"candidate_id":"cand_f3204c6924368a8ca114","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَبَذَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:naba*a|ROOT:nb*|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:4:2:2","qac_word_ref":"104:4:2","surface_ar":"يُنۢبَذَ"}],"gloss":"az miktar veya küçük parça","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığın bütününe göre az ve sınırlı bir miktarı belirtilir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Az miktar kullanımı mal, otlak, saçtaki aklık, yağmur ve salkımdaki yaş meyve için tanıklanır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ad biçimi, güzel kokulu maddelerden küçük bir parça için de kullanılır."}}],"root_ar":"ن ب ذ","root_id":"root_001466","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tamlayıcılı kullanımlarda az miktarı, yalın ad kullanımında ise tanıklanan maddelerden küçük bir parçayı karşılar.","boundary_detail":"Anlam genel küçüklük değildir; belirli söz öbeklerinde az miktarı, yalın ad kullanımında ise belirli maddelerden küçük bir parçayı bildirir.","branch_image_ar":"النَّبْذ اليسير","concept_gloss":"az miktar veya küçük parça","contextual_glosses":[{"applicability":"Mal, otlak, saçtaki aklık, yağmur veya yaş meyvenin az miktarını bildiren söz öbeklerinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Belirli maddelerden küçük bir parça bildiren yalın ad kullanımını kapsamaz.","preserves":"Bir varlığın az ve sınırlı miktarını doğal biçimde korur."},"facet_ids":["F001","F002"],"text":"biraz","usage_role":"contextual"},{"applicability":"Güzel kokulu maddelerden kesilmiş veya ayrılmış küçük parçanın anlatıldığı kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Mal, yağmur veya saç ağarması gibi sayılamayan şeylerin az miktarını kapsamaz.","preserves":"Sınırlı büyüklükteki parça anlamını açık biçimde korur."},"facet_ids":["F003"],"text":"küçük bir parça","usage_role":"contextual"}],"definition":"Belirli söz öbeklerinde mal, otlak, saç ağarması, yağmur veya yaş meyve gibi bir şeyin az miktarını belirtir. Yalın ad kullanımında ise güzel kokulu maddelerden küçük bir parçayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığın bütününe göre az ve sınırlı bir miktarı belirtilir."},{"facet_id":"F002","role":"example","statement":"Az miktar kullanımı mal, otlak, saçtaki aklık, yağmur ve salkımdaki yaş meyve için tanıklanır."},{"facet_id":"F003","role":"specialization","statement":"Ad biçimi, güzel kokulu maddelerden küçük bir parça için de kullanılır."}],"identity_rationale":"Kaynak ifadesi mal, otlak, saç ağarması, yağmur ve yaş meyve gibi varlıkların az miktarını; ayrıca güzel kokulu maddelerden küçük bir parçayı anlatır. Dal çerçevesi doğrudur, ancak az miktar bildiren söz öbekleri ile küçük parça bildiren ad kullanımı ayrı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"az miktarda mal, otlak veya küçük bir topluluk"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"biraz saç ağarması veya az yağmur"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"güzel kokulu bir maddeden küçük parça"}],"lexicalization_note":"Az miktar anlamı çoğunlukla belirli tamlayıcılı söz öbeklerine bağlıdır; küçük parça anlamındaki yalın ad yüzü bunlarla karıştırılmadan ayrıca korunur.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; genel azlık ile az kalıntı dalları, bu dalın yapıya bağlı miktar ve küçük parça sınırlarını en yararlı biçimde ortaya koydu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel azlık niteliğidir; odak dal ise belirli yapılarla sınırlı az miktar adı ve küçük parça kullanımından oluşur.","focus_only":"Odak dal belirli söz öbeklerindeki az miktarı ve belirli maddelerin küçük parçasını adlandırır.","gloss":"genel azlık","neighbor_only":"Komşu dal, para, yiyecek ve bağış dahil bir şeyin genel olarak az olmasını ya da az diye nitelenmesini kapsar.","neighbor_ref":"root_000649/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin miktar bakımından sınırlı ve az oluşunu ifade eder."},{"boundary_match":"partial","distinction":"Komşu dalda kalıntı ve sonradan alma ilişkisi belirgindir; odak dal için önceden bir alma işlemi ya da geride kalma koşulu yoktur.","focus_only":"Odak dal yağmur, mal, otlak ve saç ağarması gibi farklı şeylerin az miktarını da kapsar.","gloss":"az kalıntı","neighbor_only":"Komşu dal özellikle sağım sonrasında memede kalan az sütü, kalıntıyı veya art arda alınan küçük miktarı öne çıkarır.","neighbor_ref":"root_001031/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bütünün küçük bir bölümünü veya geriye kalan az miktarı anlatabilir."}],"source_phrase_ar":"نبذ من مال أي شيء يسير (maqayis)؛ نبذ من الشيب أي يسير (maqayis)؛ نبذ من بني فلان أي فرق يسيرة (jamhara)؛ نبذ من مطر أي قليل (jamhara)؛ نبذ من مال ومن كلأ وفي رأسه نبذ من شيب وأصاب الأرض نبذ من مطر أي شيء يسير (sihah)؛ نبذة قسط وأظفار يعني قطعة منه (tahdhib)؛ في هذا العذق نبذ قليل من الرطب (tahdhib)","source_summary":"Kaynaklar az miktar anlamını çeşitli varlıklarla kurulan söz öbeklerinde ortaklaştırır; kanıt ayrıca güzel kokulu maddelerden küçük bir parça kullanımını da içerir.","sources":["MQ","JA","SI","TA"],"what_is_ar":"القدر اليسير من مال أو كلأ أو شيب أو مطر أو رطب؛ والقطعة من القسط والأظفار","what_is_not_ar":"مطلق الطرح؛ النبيذ؛ الولد المنبوذ"},"support_links":["sup_bb908782094e8de50ec0"]},{"boundary":"Dal her türlü suda bekletme veya her meyveli içecek için kullanılmaz; hurma ya da kuru üzümün kaba konup su eklenmesiyle hazırlanan ürün ve eylemle sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001466/B006","candidate_links":[{"candidate_id":"cand_83fac0b5c240df2acaa0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَبَذَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:naba*a|ROOT:nb*|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:4:2:2","qac_word_ref":"104:4:2","surface_ar":"يُنۢبَذَ"}],"gloss":"hurma ya da kuru üzümün suda bekletilmesiyle yapılan içecek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ürün, hurma veya kuru üzümün suyla bir kap içinde bekletilmesiyle elde edilen içecektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hazırlama işlemi meyveyi kaba veya su tulumuna koyma ve üzerine su dökme aşamalarından oluşur."}}],"root_ar":"ن ب ذ","root_id":"root_001466","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Meyve türlerini, su ekleme işlemini ve ortaya çıkan içeceği birlikte gösteren tam açıklayıcı karşılıktır.","boundary_detail":"Dal her türlü suda bekletme veya her meyveli içecek için kullanılmaz; hurma ya da kuru üzümün kaba konup su eklenmesiyle hazırlanan ürün ve eylemle sınırlıdır.","branch_image_ar":"النبيذ المطروح في الوعاء","concept_gloss":"hurma ya da kuru üzümün suda bekletilmesiyle yapılan içecek","contextual_glosses":[{"applicability":"Ad değil, hurma veya kuru üzümü kaba koyup su ekleyerek içeceği hazırlama eylemi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Meyveyi suyla kaba koyma sürecini ve içecek hazırlama sonucunu korur."},"facet_ids":["F002"],"text":"meyveyi suda bekleterek içecek hazırlamak","usage_role":"explanatory"}],"definition":"Hurma veya kuru üzümün bir kaba ya da su tulumuna konup üzerine su dökülerek bekletilmesiyle hazırlanan içecektir; aynı anlam alanı bu işlemi yapıp içeceği hazırlama eylemini de kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ürün, hurma veya kuru üzümün suyla bir kap içinde bekletilmesiyle elde edilen içecektir."},{"facet_id":"F002","role":"specialization","statement":"Hazırlama işlemi meyveyi kaba veya su tulumuna koyma ve üzerine su dökme aşamalarından oluşur."}],"identity_rationale":"Kaynak ifadesi hurma veya kuru üzümün bir kaba ya da su tulumuna bırakılıp üzerine su dökülmesiyle hazırlanan içeceği ve onu hazırlama eylemini verir. Dal çerçevesi ürün ile hazırlama sürecini doğru biçimde birlikte taşır.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"hurma ya da kuru üzümün suda bekletilmesiyle yapılan içecek"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"hurma veya kuru üzümü suya koyarak içecek hazırlamak"}],"lexicalization_note":"İçeceği adlandıran biçim ile onu hazırlama anlamındaki söz öbeği ayrı yüzlerdir; hazırlama kalıbı genel atma veya genel içecek anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar incelendi; genel suda bekletme alanı ile işlem veya bileşimi farklı iki içecek dalı, bu kullanımın malzeme ve hazırlama sınırlarını en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel bekletme ve su birikmesi alanıdır; odak dal belirli meyveler, su ekleme işlemi ve içecek sonucuyla sınırlandırılmıştır.","focus_only":"Odak dal, hurma veya kuru üzümden su eklenerek hazırlanan belirli bir içeceği ve hazırlama eylemini kapsar.","gloss":"suda bekletme ve su birikmesi","neighbor_only":"Komşu dal, suyun bir yerde birikmesi, herhangi bir şeyin suda beklemesi ve ilaç, boya ya da başka karışımların bekletilmesi gibi daha geniş süreçleri kapsar.","neighbor_ref":"root_001544/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da bir maddenin su içinde kalması ve suya geçen bir karışımın oluşması sahnesi bulunur."},{"boundary_match":"field_only","distinction":"Odak dalın belirleyici işlemi su içinde bekletmedir; komşu dal pişirme ve suyla ezme aşamalarını gerektirir.","focus_only":"Odak dalda hurma veya kuru üzüm kaba konur, üzerine su dökülür ve bekletilir.","gloss":"pişmiş hurmanın suyla ezildiği içecek","neighbor_only":"Komşu dalda hurma önce pişirilir, ardından suyla ezilip yoğrularak başka bir içecek hazırlanır.","neighbor_ref":"root_000483/B005","relation_type":"same_field","shared_zone":"Her iki dal hurma ve su kullanılarak hazırlanan geleneksel bir içecek alanına girer."},{"boundary_match":"field_only","distinction":"Odak dalda temel sıvı sudur ve bekletme işlemi kurucudur; komşu dalın ayırt edici bileşeni baldır.","focus_only":"Odak dal hurma veya kuru üzümün doğrudan su içinde bekletilmesine dayanır.","gloss":"kuru üzüm ve bal içeceği","neighbor_only":"Komşu dal kuru üzüm ile balın birlikte kullanıldığı farklı bir içecek bileşimine dayanır.","neighbor_ref":"root_001168/B003","relation_type":"same_field","shared_zone":"İki dal da kuru üzümden hazırlanabilen içecekleri adlandırır."}],"source_phrase_ar":"النبيذ التمر يلقى في الآنية ويصب عليه الماء (maqayis)؛ سمي النبيذ لأن التمر كان يلقى في الجر وفي غيره (jamhara)؛ النبيذ واحد الأنبذة يقال نبذت نبيذا أي اتخذته (sihah)؛ يأخذ تمرا أو زبيبا فينبذه أي يلقيه في وعاء أو سقاء ويصب عليه الماء (tahdhib)","source_summary":"Kaynaklar içeceğin hurma veya kuru üzümün kaba konup su eklenmesiyle hazırlandığında birleşir; kanıt hem ürün adını hem de onu hazırlama eylemini destekler.","sources":["MQ","JA","SI","TA"],"what_is_ar":"النبيذ واتخاذه بإلقاء تمر أو زبيب في إناء أو سقاء وصب الماء عليه","what_is_not_ar":"مطلق الطرح؛ الولد المنبوذ؛ القلة اليسيرة"},"support_links":["sup_65416a2aba224274a831"]},{"boundary":"Bu adlandırma çocuğun annesi tarafından bırakılmış olmasına dayanır; evlilik dışı doğum, babanın ölümü veya soyun bilinmemesi tek başına yeterli değildir.","branch_kind":"bare","branch_ref":"root_001466/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَبَذَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:naba*a|ROOT:nb*|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:4:2:2","qac_word_ref":"104:4:2","surface_ar":"يُنۢبَذَ"}],"gloss":"annesi tarafından bırakılıp başkalarınca bulunan çocuk","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Anne, yeni doğan veya küçük çocuğu yola ya da başkalarının bulabileceği bir yere bırakır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bırakılan çocuk daha sonra başka bir kişi veya topluluk tarafından bulunup alınır."}}],"root_ar":"ن ب ذ","root_id":"root_001466","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bırakanın anne, bırakılanın çocuk ve sonraki aşamanın başkalarınca bulunup alınma olduğu tam sahneyi karşılar.","boundary_detail":"Bu adlandırma çocuğun annesi tarafından bırakılmış olmasına dayanır; evlilik dışı doğum, babanın ölümü veya soyun bilinmemesi tek başına yeterli değildir.","branch_image_ar":"الولد المنبوذ","concept_gloss":"annesi tarafından bırakılıp başkalarınca bulunan çocuk","contextual_glosses":[{"applicability":"Çocuğun bulunmuş olmasının öne çıktığı kısa kullanımda uygundur; tam tanım gerektiğinde açıklayıcı karşılık tercih edilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çocuğu bırakanın annesi olduğunu ve bırakma eylemini açıkça belirtmez.","preserves":"Çocuğun başkaları tarafından bulunup alınması sonucunu korur."},"facet_ids":["F002"],"text":"buluntu çocuk","usage_role":"contextual"}],"definition":"Annesinin doğumdan sonra yola veya insanların bulabileceği bir yere bıraktığı ve başka bir kişi ya da topluluk tarafından bulunup alınan çocuktur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Anne, yeni doğan veya küçük çocuğu yola ya da başkalarının bulabileceği bir yere bırakır."},{"facet_id":"F002","role":"core","statement":"Bırakılan çocuk daha sonra başka bir kişi veya topluluk tarafından bulunup alınır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kaynak ifadesinde bulunmayan bir doğum ve soy durumu yükler.","collision":"Bırakılmış çocuk ile doğum durumu kavramlarını yanlış biçimde özdeşleştirir.","fit":"displacement","loses":"Anne tarafından bırakılma ve başkalarınca bulunup alınma aşamalarını siler.","preserves":"Çocuk kişisini korur ancak bırakılma olayını doğrudan karşılamaz."},"text":"evlilik dışı doğmuş çocuk"}],"identity_rationale":"Kaynak ifadesi, annesi tarafından doğumdan sonra yola bırakılan ve başka bir kişi ya da topluluk tarafından bulunan çocuğu tanımlar. Çerçeve bu katılımcıları ve bırakılma ile bulunma sırasını doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"annesi tarafından bırakılıp başkalarınca bulunan çocuk"}],"lexicalization_note":"Tanım çocuğu adlandıran yalın biçime bağlıdır ve genel terk etme eylemine ya da başka bakım kaybı türlerine genişletilmez.","neighbor_coverage_note":"Adayların tümü değerlendirildi; daha geniş soy belirsizliği dalı ile baba kaybı dalı, bu kullanımın anne tarafından bırakılma ve bulunma koşullarını en iyi ayırdı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir bırakma ve bulunma olayına dayanır; komşu dal soy belirsizliği ve yabancılık gibi daha geniş durumları da içerir.","focus_only":"Odak dal, annenin çocuğu bırakması ve çocuğun başkalarınca bulunması olay dizisini gerektirir.","gloss":"soyu belirsiz veya sonradan taşınmış çocuk","neighbor_only":"Komşu dal bırakılmış çocuğun yanında yabancı kişiyi, taşınmış çocuğu ve soyu doğrulanamayan kişiyi de kapsar.","neighbor_ref":"root_000357/B005","relation_type":"near_synonym","shared_zone":"İki dal bırakılmış veya asıl aile bağından kopmuş bir çocuk için örtüşebilir."},{"boundary_match":"field_only","distinction":"Komşu dal ölüm nedeniyle baba bakımının kaybıdır; odak dal annenin etkin bırakma eylemi ve ardından başkasının bulmasıyla kurulur.","focus_only":"Odak dalda çocuk annesi tarafından bir yere bırakılır ve başka biri onu bulur.","gloss":"babasını küçük yaşta kaybetmiş çocuk","neighbor_only":"Komşu dalda çocuk erginlikten önce babasını kaybeder; annenin bırakması veya bulunma olayı gerekmez.","neighbor_ref":"root_001692/B001","relation_type":"same_field","shared_zone":"Her iki dal aile bakım bağında ciddi bir kopuş yaşayan çocuğu konu eder."}],"source_phrase_ar":"الصبي المنبوذ الذي تلقيه أمه (maqayis;jamhara)؛ المنبوذ الصبي تلقيه أمه في الطريق (sihah)؛ المنبوذ الولد الذي تنبذه والدته حين تلده فيلتقطه الرجل أو جماعة من المسلمين (tahdhib)","source_summary":"Kaynaklar annenin çocuğu bırakması konusunda birleşir; daha ayrıntılı anlatım, bırakılan çocuğun bir kişi veya topluluk tarafından bulunup alınmasını da açıkça belirtir.","sources":["MQ","JA","SI","TA"],"what_is_ar":"الصبي أو الولد الذي تطرحه أمه فيلتقطه غيرها","what_is_not_ar":"ليس لازمه ولد الزنى؛ وليس هو النبيذ ولا النبذ اليسير"},"support_links":[]},{"boundary":"Her yastık bu dala girmez; nesnenin oturmak amacıyla yere atılıp konan bir yastık olması gerekir.","branch_kind":"bare","branch_ref":"root_001466/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَبَذَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:naba*a|ROOT:nb*|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:4:2:2","qac_word_ref":"104:4:2","surface_ar":"يُنۢبَذَ"}],"gloss":"oturmak için yere atılan yastık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne, otururken bedeni destekleyen bir yastık veya minderdir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayırt edici kullanımında yastık oturmak için doğrudan yere atılıp konur."}}],"root_ar":"ن ب ذ","root_id":"root_001466","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesnenin hem yastık işlevini hem de oturmak üzere yere atılıp konma biçimini eksiksiz karşılar.","boundary_detail":"Her yastık bu dala girmez; nesnenin oturmak amacıyla yere atılıp konan bir yastık olması gerekir.","branch_image_ar":"الوسادة المنبوذة","concept_gloss":"oturmak için yere atılan yastık","contextual_glosses":[{"applicability":"Yere konarak üzerinde oturulan yastığın kısa ve doğal biçimde adlandırılması gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nesnenin yere atılarak konması biçimini açıkça belirtmez.","preserves":"Yerde kullanılan oturma desteği işlevini korur."},"facet_ids":["F001"],"text":"yer minderi","usage_role":"contextual"}],"definition":"Oturacak kişinin altına gelmesi için yere atılıp konan bir yastık veya oturma minderidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne, otururken bedeni destekleyen bir yastık veya minderdir."},{"facet_id":"F002","role":"specialization","statement":"Ayırt edici kullanımında yastık oturmak için doğrudan yere atılıp konur."}],"identity_rationale":"Kaynak ifadesi bu nesneyi yastık olarak tanımlar ve adlandırmanın, oturmak için yere atılıp konmasından geldiğini açıklar. Dal çerçevesi hem nesne türünü hem de ayırt edici kullanım biçimini doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"oturmak için yere atılıp konan yastık"}],"lexicalization_note":"Tanım nesneyi adlandıran yalın biçime bağlıdır; genel yastık, genel oturma veya yere serilen her eşya anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar incelendi; küçük yastık alanındaki iki yakın anlamlı dal, odak kullanımın yere atma ve yerde oturma koşullarını doğrudan sınadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı belirleyen yer ve amaç yerde oturmadır; komşu dal küçük boyutu veya eyer üzerindeki kullanımı öne çıkarır.","focus_only":"Odak dalın yastığı özellikle oturmak için yere atılıp konur.","gloss":"küçük yastık veya eyer üstü örtü","neighbor_only":"Komşu dal küçük yastığı ve özellikle eyerin üzerine serilen yastıklı örtüyü de kapsar.","neighbor_ref":"root_001555/B001","relation_type":"near_synonym","shared_zone":"İki dal küçük, yumuşak bir destek veya oturma yastığı nesnesinde örtüşebilir."},{"boundary_match":"partial","distinction":"Komşu dal nesnenin küçüklüğü ve kullandırılması çevresinde genişler; odak dalın ayırt edici sınırı yastığın yere atılmasıdır.","focus_only":"Odak dal, yastığın yere atılıp üzerinde oturulması biçimini zorunlu kılar.","gloss":"küçük oturma yastığı","neighbor_only":"Komşu dal küçük yastığı ve bir kişiyi o yastığa oturtma veya yaslandırma eylemini daha genel biçimde kapsar.","neighbor_ref":"root_000318/B008","relation_type":"near_synonym","shared_zone":"Her iki dal otururken destek sağlayan küçük bir yastığı adlandırabilir."}],"source_phrase_ar":"المنبذة الوسادة (sihah;tahdhib)؛ المنبذة الوسادة سميت منبذة لأنها تنبذ بالأرض أي تطرح للجلوس عليها (tahdhib)","source_summary":"Kaynaklar nesnenin yastık olduğu konusunda birleşir; ayrıntılı açıklama, adın oturmak üzere yere atılıp konma biçimine dayandığını belirtir.","sources":["SI","TA"],"what_is_ar":"الوسادة التي تطرح بالأرض للجلوس","what_is_not_ar":"الولد المنبوذ؛ النبيذ؛ المنابذة في العهد أو البيع"},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"bare","branch_ref":"root_001466/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَبَذَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:naba*a|ROOT:nb*|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:4:2:2","qac_word_ref":"104:4:2","surface_ar":"يُنۢبَذَ"}],"gloss":"özel adlandırma kümesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kullanım, sahiplerinin bakımsız bıraktığı cılız koyunu adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı bir kullanım, çukur kazılırken çıkarılıp çevreye saçılan toprağı adlandırır."}}],"root_ar":"ن ب ذ","root_id":"root_001466","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"النبيذة المهملة أو المنبثة","concept_gloss":"özel adlandırma kümesi","contextual_glosses":[{"applicability":"Sahiplerinin bakımını bıraktığı zayıf koyunu adlandıran ilk bağımsız kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çukurdan çevreye saçılan toprağı adlandıran ayrı kullanımı kapsamaz.","preserves":"Cılız koyun ile sahiplerinin onu ihmal etmesi durumunu korur."},"facet_ids":["F001"],"text":"ihmal edilmiş cılız koyun","usage_role":"contextual"},{"applicability":"Çukur kazısından çıkıp çevreye dağılan toprağı adlandıran ikinci bağımsız kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sahiplerince ihmal edilen cılız koyunu adlandıran ayrı kullanımı kapsamaz.","preserves":"Kazı çukurundan çıkan toprağın çevreye saçılması durumunu korur."},"facet_ids":["F002"],"text":"çukurdan saçılan toprak","usage_role":"contextual"}],"definition":"Eldeki dal tek bir kavram tanımlamaz: bir kullanım sahiplerince ihmal edilmiş cılız koyunu, öteki kullanım ise çukurdan çevreye saçılan toprağı adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kullanım, sahiplerinin bakımsız bıraktığı cılız koyunu adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Ayrı bir kullanım, çukur kazılırken çıkarılıp çevreye saçılan toprağı adlandırır."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"sahiplerinin ihmal ettiği cılız koyun"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"çukurdan çıkarak çevreye saçılan toprak"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"يقال للشاة المهزولة التي يهملها أهلها نبيذة؛ لما ينبث من تراب الحفرة نبيثة ونبيذة وجمعها النبائت والنبائذ","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık hem sahiplerince ihmal edilmiş cılız koyunu hem de çukurdan saçılan toprağı aynı ad biçimi altında verir."}],"source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["TA"],"what_is_ar":"النبيذة للشاة المهزولة المهملة؛ والنبيذة لما ينبث من تراب الحفرة","what_is_not_ar":"النبيذ الشراب؛ الولد المنبوذ؛ الوسادة المنبوذة"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["104:4:1"],"branch_refs":[],"candidate_id":"cand_0b8a12e35eb5ec056218","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:4:1:audible-isolated-refusal","source_type":"word_analysis","support_ids":["sup_0101610c15d216f68bc9","sup_0f75c56dcb92e1571358"],"title":"rebuke is heard as a separate beat","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:1","qac_refs":["104:4:1:1"],"status":"accepted"}},{"anchor_refs":["104:4:1"],"branch_refs":[],"candidate_id":"cand_f9b307bde4d168b03d1a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:4:1:opening-boundary-shift","source_type":"word_analysis","support_ids":["sup_0101610c15d216f68bc9","sup_0abdc37180acf7972fe2"],"title":"first word ruptures the prior scene","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:1","qac_refs":["104:4:1:1"],"status":"accepted"}},{"anchor_refs":["104:4:1"],"branch_refs":[],"candidate_id":"cand_952c8017d412a80d74e9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:4:1:performative-meccan-confrontation","source_type":"word_analysis","support_ids":["sup_0101610c15d216f68bc9","sup_d884edaee758ad2a6edd"],"title":"confrontational speech act","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:1","qac_refs":["104:4:1:1"],"status":"accepted"}},{"anchor_refs":["104:4:1"],"branch_refs":[],"candidate_id":"cand_4865ba7d12c133208310","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:4:1:rebuke-and-verdict-pivot","source_type":"word_analysis","support_ids":["sup_0101610c15d216f68bc9","sup_e374ebbbc389a3a312af"],"title":"rebuke opens into verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:1","qac_refs":["104:4:1:1"],"status":"accepted"}},{"anchor_refs":["104:4:2"],"branch_refs":[],"candidate_id":"cand_fd25fa5e595d2496977f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:4:2:bound-verb-architecture","source_type":"word_analysis","support_ids":["sup_331a60afbef6ea6a8b08","sup_b718aa5cb1c3022d5d29"],"title":"certainty is fused to the verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:2","qac_refs":["104:4:2:1"],"status":"accepted"}},{"anchor_refs":["104:4:2"],"branch_refs":[],"candidate_id":"cand_21d7ebb607bee741c15d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:4:2:oath-response-certainty","source_type":"word_analysis","support_ids":["sup_b718aa5cb1c3022d5d29","sup_feaee77cc60fd7d38555"],"title":"oath lām fixes certainty","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:2","qac_refs":["104:4:2:1"],"status":"accepted"}},{"anchor_refs":["104:4:2"],"branch_refs":[],"candidate_id":"cand_4bca4946cd3eaf9e2c54","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:4:2:rebuttal-to-sentence-bridge","source_type":"word_analysis","support_ids":["sup_38ac920a790e6d8ddf7e","sup_b718aa5cb1c3022d5d29"],"title":"rebuke becomes sworn adjudication","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:2","qac_refs":["104:4:2:1"],"status":"accepted"}},{"anchor_refs":["104:4:3"],"branch_refs":[],"candidate_id":"cand_021d438ad9f6866d5c15","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001466"],"scope":"focus_ayah","source_local_id":"104:4:3:audible-emphatic-closure","source_type":"word_analysis","support_ids":["sup_359b90831b3517edfa11","sup_505af7f038fa027d6cea"],"title":"sound reinforces the sealed verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:3","qac_refs":["104:4:2:2","104:4:2:3"],"status":"accepted"}},{"anchor_refs":["104:4:3"],"branch_refs":[],"candidate_id":"cand_cb808774f112bd7c5f5b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001466"],"scope":"focus_ayah","source_local_id":"104:4:3:contained-casting-image-pressure","source_type":"word_analysis","support_ids":["sup_505af7f038fa027d6cea","sup_9e76a415356925dcba84"],"title":"vessel and separation images support containment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:3","qac_refs":["104:4:2:2","104:4:2:3"],"status":"accepted"}},{"anchor_refs":["104:4:3"],"branch_refs":[],"candidate_id":"cand_60f8d0be11ca894d981d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001466"],"scope":"focus_ayah","source_local_id":"104:4:3:destination-directed-argument-frame","source_type":"word_analysis","support_ids":["sup_505af7f038fa027d6cea","sup_65f4068f9e7915ffdd59"],"title":"discard becomes trajectory into containment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:3","qac_refs":["104:4:2:2","104:4:2:3"],"status":"accepted"}},{"anchor_refs":["104:4:3"],"branch_refs":[],"candidate_id":"cand_c7f8ad2bbc465779aeba","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001466"],"scope":"focus_ayah","source_local_id":"104:4:3:discard-root-pressure","source_type":"word_analysis","support_ids":["sup_3c2a230a84738a975b87","sup_505af7f038fa027d6cea"],"title":"throwing is contemptuous disposal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:3","qac_refs":["104:4:2:2","104:4:2:3"],"status":"accepted"}},{"anchor_refs":["104:4:3"],"branch_refs":[],"candidate_id":"cand_34c775a8a4d64626f5b2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001466"],"scope":"focus_ayah","source_local_id":"104:4:3:oath-bound-passive-future","source_type":"word_analysis","support_ids":["sup_505af7f038fa027d6cea","sup_8778870f9d668c27a7b9"],"title":"passive verdict is sealed by emphasis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:3","qac_refs":["104:4:2:2","104:4:2:3"],"status":"accepted"}},{"anchor_refs":["104:4:3"],"branch_refs":[],"candidate_id":"cand_b2778097be186e8b0e7a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001466"],"scope":"focus_ayah","source_local_id":"104:4:3:passive-patient-reversal","source_type":"word_analysis","support_ids":["sup_48962cbb7f20f21c2371","sup_505af7f038fa027d6cea"],"title":"active reckoner becomes passive patient","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:3","qac_refs":["104:4:2:2","104:4:2:3"],"status":"accepted"}},{"anchor_refs":["104:4:3"],"branch_refs":[],"candidate_id":"cand_6dac979211f5d7aef643","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001466"],"scope":"focus_ayah","source_local_id":"104:4:3:qiraat-agency-and-number-contrast","source_type":"word_analysis","support_ids":["sup_505af7f038fa027d6cea","sup_ff2b14139fa1369fa77e"],"title":"variants expose the canonical routing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:3","qac_refs":["104:4:2:2","104:4:2:3"],"status":"accepted"}},{"anchor_refs":["104:4:3"],"branch_refs":[],"candidate_id":"cand_b80acc05bc0d7626a4ba","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001466"],"scope":"focus_ayah","source_local_id":"104:4:3:rare-passive-root-deployment","source_type":"word_analysis","support_ids":["sup_3dd4d7e2af3ac71af95e","sup_505af7f038fa027d6cea"],"title":"rare root-form choice marks reversal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:3","qac_refs":["104:4:2:2","104:4:2:3"],"status":"accepted"}},{"anchor_refs":["104:4:3"],"branch_refs":[],"candidate_id":"cand_b683e287d6442b607b5a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001466"],"scope":"focus_ayah","source_local_id":"104:4:3:referent-continuity-without-renaming","source_type":"word_analysis","support_ids":["sup_505af7f038fa027d6cea","sup_8e15351db026ce952f02"],"title":"the prior person is carried into the passive","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:3","qac_refs":["104:4:2:2","104:4:2:3"],"status":"accepted"}},{"anchor_refs":["104:4:3"],"branch_refs":[],"candidate_id":"cand_c6187ba2231a32ccb1f1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001466"],"scope":"focus_ayah","source_local_id":"104:4:3:stark-form-i-passive","source_type":"word_analysis","support_ids":["sup_11b08ec675b553ddb6ba","sup_505af7f038fa027d6cea"],"title":"simple stem keeps the act stark","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:3","qac_refs":["104:4:2:2","104:4:2:3"],"status":"accepted"}},{"anchor_refs":["104:4:3"],"branch_refs":[],"candidate_id":"cand_2b1035aa2987649d213f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001466"],"scope":"focus_ayah","source_local_id":"104:4:3:verdict-scene-pivot","source_type":"word_analysis","support_ids":["sup_505af7f038fa027d6cea","sup_646978f252dc49f7f886"],"title":"the middle verb converts thought into scene","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:3","qac_refs":["104:4:2:2","104:4:2:3"],"status":"accepted"}},{"anchor_refs":["104:4:4"],"branch_refs":[],"candidate_id":"cand_cfa8d2864c98a326dbea","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:4:4:audible-liaison","source_type":"word_analysis","support_ids":["sup_91903819919d9a579874","sup_9df1441a24ac0de94052"],"title":"sound links preposition and destination","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:4","qac_refs":["104:4:3:1"],"status":"accepted"}},{"anchor_refs":["104:4:4"],"branch_refs":[],"candidate_id":"cand_be5308e036fd0d267aaf","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:4:4:directed-containment","source_type":"word_analysis","support_ids":["sup_6f9e2897c26559f610dd","sup_91903819919d9a579874"],"title":"preposition turns motion into enclosure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:4","qac_refs":["104:4:3:1"],"status":"accepted"}},{"anchor_refs":["104:4:4"],"branch_refs":[],"candidate_id":"cand_9f92c633ad4b4f3fab59","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:4:4:fire-and-sealed-containment-anticipation","source_type":"word_analysis","support_ids":["sup_3492a56db69e8cbcf82f","sup_91903819919d9a579874"],"title":"containment points forward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:4","qac_refs":["104:4:3:1"],"status":"accepted"}},{"anchor_refs":["104:4:4"],"branch_refs":[],"candidate_id":"cand_fc95da5da1a11d4f9f53","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:4:4:visible-destination-beat","source_type":"word_analysis","support_ids":["sup_21114db8076159cc0758","sup_91903819919d9a579874"],"title":"separate preposition stages the destination","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:4","qac_refs":["104:4:3:1"],"status":"accepted"}},{"anchor_refs":["104:4:5"],"branch_refs":[],"candidate_id":"cand_3926b25aa94e8782eea8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000337"],"scope":"focus_ayah","source_local_id":"104:4:5:active-participle-variant-contrast","source_type":"word_analysis","support_ids":["sup_305650569da68281c0f1","sup_f7a2ffb0c7e1364331bd"],"title":"variant clarifies identity-force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:5","qac_refs":["104:4:4:1","104:4:4:2"],"status":"accepted"}},{"anchor_refs":["104:4:5"],"branch_refs":[],"candidate_id":"cand_a5e99008ac244a2e5dc1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000337"],"scope":"focus_ayah","source_local_id":"104:4:5:ayah-final-destination-closure","source_type":"word_analysis","support_ids":["sup_305650569da68281c0f1","sup_eafa93ff0fb6a85cfb71"],"title":"the destination is the final beat","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:5","qac_refs":["104:4:4:1","104:4:4:2"],"status":"accepted"}},{"anchor_refs":["104:4:5"],"branch_refs":[],"candidate_id":"cand_fd718c2e2e071ac8164a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000337"],"scope":"focus_ayah","source_local_id":"104:4:5:crusher-over-debris","source_type":"word_analysis","support_ids":["sup_305650569da68281c0f1","sup_ca31810e8772e5104356"],"title":"debris field sharpens the selected name","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:5","qac_refs":["104:4:4:1","104:4:4:2"],"status":"accepted"}},{"anchor_refs":["104:4:5"],"branch_refs":[],"candidate_id":"cand_19e700d60425b0671731","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000337"],"scope":"focus_ayah","source_local_id":"104:4:5:fire-defined-by-crushing","source_type":"word_analysis","support_ids":["sup_305650569da68281c0f1","sup_c79231072aacbdb7f930"],"title":"crushing name anticipates fire definition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:5","qac_refs":["104:4:4:1","104:4:4:2"],"status":"accepted"}},{"anchor_refs":["104:4:5"],"branch_refs":[],"candidate_id":"cand_e65c35780f7b4332de72","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000337"],"scope":"focus_ayah","source_local_id":"104:4:5:genitive-destination-role","source_type":"word_analysis","support_ids":["sup_154d9bfe92ee10d242f7","sup_305650569da68281c0f1"],"title":"case binds the name to the trajectory","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:5","qac_refs":["104:4:4:1","104:4:4:2"],"status":"accepted"}},{"anchor_refs":["104:4:5"],"branch_refs":[],"candidate_id":"cand_548884380ba961eed84c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000337"],"scope":"focus_ayah","source_local_id":"104:4:5:immediate-return-and-definition","source_type":"word_analysis","support_ids":["sup_305650569da68281c0f1","sup_c329e9f476fdef28556a"],"title":"first mention sets up the question","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:5","qac_refs":["104:4:4:1","104:4:4:2"],"status":"accepted"}},{"anchor_refs":["104:4:5"],"branch_refs":[],"candidate_id":"cand_767948a19868e8b8816a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000337"],"scope":"focus_ayah","source_local_id":"104:4:5:intensive-producer-not-product","source_type":"word_analysis","support_ids":["sup_305650569da68281c0f1","sup_42c35ac46868eacabdad"],"title":"the form makes crushing identity-defining","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:5","qac_refs":["104:4:4:1","104:4:4:2"],"status":"accepted"}},{"anchor_refs":["104:4:5"],"branch_refs":[],"candidate_id":"cand_b5cb1a84213e271aab82","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000337"],"scope":"focus_ayah","source_local_id":"104:4:5:permanence-meets-fragmentation","source_type":"word_analysis","support_ids":["sup_305650569da68281c0f1","sup_6e63aaec1d22ba911cee"],"title":"wealth permanence is answered by breaking","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:5","qac_refs":["104:4:4:1","104:4:4:2"],"status":"accepted"}},{"anchor_refs":["104:4:5"],"branch_refs":[],"candidate_id":"cand_9dc8f11f9fa164fe1a04","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000337"],"scope":"focus_ayah","source_local_id":"104:4:5:proper-name-definite-crusher","source_type":"word_analysis","support_ids":["sup_305650569da68281c0f1","sup_e5630c37323b6c7f45cf"],"title":"definite form names a crushing entity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:5","qac_refs":["104:4:4:1","104:4:4:2"],"status":"accepted"}},{"anchor_refs":["104:4:5"],"branch_refs":[],"candidate_id":"cand_64e6ee542e8c02c9027d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000337"],"scope":"focus_ayah","source_local_id":"104:4:5:rare-local-signature","source_type":"word_analysis","support_ids":["sup_305650569da68281c0f1","sup_bfb561fc832e720ecfd5"],"title":"rare root and name concentrate locally","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:5","qac_refs":["104:4:4:1","104:4:4:2"],"status":"accepted"}},{"anchor_refs":["104:4:5"],"branch_refs":[],"candidate_id":"cand_82561b6eecfc9975a2d1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000337"],"scope":"focus_ayah","source_local_id":"104:4:5:sound-and-fawasil-pressure","source_type":"word_analysis","support_ids":["sup_1346c95132bf3ab258fd","sup_305650569da68281c0f1"],"title":"sound reinforces the named closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:4:5","qac_refs":["104:4:4:1","104:4:4:2"],"status":"accepted"}},{"anchor_refs":["104:4:2"],"branch_refs":[],"candidate_id":"cand_891ba21d0d6c29ba9fee","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001466"],"scope":"focus_ayah","source_local_id":"104:4:2:2","source_type":"qac_morpheme","support_ids":["sup_d5757a53e4ae823313b3"],"title":"QAC root occurrence: ن ب ذ","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["104:4:4"],"branch_refs":[],"candidate_id":"cand_5d7aa6e1afaccb94d098","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000337"],"scope":"focus_ayah","source_local_id":"104:4:4:2","source_type":"qac_morpheme","support_ids":["sup_3b5600ca14fc7982e99b"],"title":"QAC root occurrence: ح ط م","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["104:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:4","branch_refs":["root_000337/B001","root_001466/B001"],"candidate_id":"cand_48f791e38f8a434e20ec","commentary_obligation":"review","hft_ref":"hft_8089ee59aea165302b8a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_discard_to_comminution","source_type":"hft","support_ids":["sup_c190bb38923e1f1d4bba"],"title":"baseline_discard_to_comminution","trust":"legacy_unbound"},{"anchor_refs":["104:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:4","branch_refs":["root_000337/B003","root_000337/B005","root_001466/B005"],"candidate_id":"cand_f3204c6924368a8ca114","commentary_obligation":"review","hft_ref":"hft_8bf1764ee25940c1e7b8","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_attritional_reduction","source_type":"hft","support_ids":["sup_bb908782094e8de50ec0"],"title":"baseline_attritional_reduction","trust":"legacy_unbound"},{"anchor_refs":["104:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:4","branch_refs":["root_000337/B004","root_000337/B006","root_001466/B002"],"candidate_id":"cand_83f15fc7c30c038e778b","commentary_obligation":"review","hft_ref":"hft_1d64662891ae8ebabd20","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_adversarial_excommunication","source_type":"hft","support_ids":["sup_bdfe0ae4d4049c76fe0f"],"title":"baseline_adversarial_excommunication","trust":"legacy_unbound"},{"anchor_refs":["104:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:4","branch_refs":["root_000337/B008","root_001466/B006"],"candidate_id":"cand_83fac0b5c240df2acaa0","commentary_obligation":"review","hft_ref":"hft_bac5a81cea8c9c221380","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_vessel_grinder","source_type":"hft","support_ids":["sup_65416a2aba224274a831"],"title":"baseline_vessel_grinder","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"كَلَّا ۖ لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ","qac_morphemes":[{"lemma_ar":"كَلَّا","morph_features":"STEM|POS:AVR|LEM:kal~aA","morpheme_role":"STEM","pos":"AVR","qac_ref":"104:4:1:1","qac_word_ref":"104:4:1","root_ar":"","surface_ar":"كَلَّا"},{"lemma_ar":"","morph_features":"PREFIX|l:EMPH+","morpheme_role":"PREFIX","pos":"EMPH","qac_ref":"104:4:2:1","qac_word_ref":"104:4:2","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"نَبَذَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:naba*a|ROOT:nb*|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:4:2:2","qac_word_ref":"104:4:2","root_ar":"ن ب ذ","surface_ar":"يُنۢبَذَ"},{"lemma_ar":"","morph_features":"SUFFIX|+n:EMPH","morpheme_role":"SUFFIX","pos":"EMPH","qac_ref":"104:4:2:3","qac_word_ref":"104:4:2","root_ar":"","surface_ar":"نَّ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"104:4:3:1","qac_word_ref":"104:4:3","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"104:4:4:1","qac_word_ref":"104:4:4","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"حُطَمَة","morph_features":"STEM|POS:N|LEM:HuTamap|ROOT:HTm|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:4:4:2","qac_word_ref":"104:4:4","root_ar":"ح ط م","surface_ar":"حُطَمَةِ"}],"word_analysis_qac_refs":[["104:4:1:1"],["104:4:2:1"],["104:4:2:2","104:4:2:3"],["104:4:3:1"],["104:4:4:1","104:4:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["104:4:1","104:4:2","104:4:3","104:4:4","104:4:5"]},"focus_surface_evidence":{"arabic_uthmani":"كَلَّا ۖ لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ","qac_morphemes":[{"lemma_ar":"كَلَّا","morph_features":"STEM|POS:AVR|LEM:kal~aA","morpheme_role":"STEM","pos":"AVR","qac_ref":"104:4:1:1","qac_word_ref":"104:4:1","root_ar":"","surface_ar":"كَلَّا"},{"lemma_ar":"","morph_features":"PREFIX|l:EMPH+","morpheme_role":"PREFIX","pos":"EMPH","qac_ref":"104:4:2:1","qac_word_ref":"104:4:2","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"نَبَذَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:naba*a|ROOT:nb*|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"104:4:2:2","qac_word_ref":"104:4:2","root_ar":"ن ب ذ","surface_ar":"يُنۢبَذَ"},{"lemma_ar":"","morph_features":"SUFFIX|+n:EMPH","morpheme_role":"SUFFIX","pos":"EMPH","qac_ref":"104:4:2:3","qac_word_ref":"104:4:2","root_ar":"","surface_ar":"نَّ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"104:4:3:1","qac_word_ref":"104:4:3","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"104:4:4:1","qac_word_ref":"104:4:4","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"حُطَمَة","morph_features":"STEM|POS:N|LEM:HuTamap|ROOT:HTm|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:4:4:2","qac_word_ref":"104:4:4","root_ar":"ح ط م","surface_ar":"حُطَمَةِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["104:4:1:1"],["104:4:2:1"],["104:4:2:2","104:4:2:3"],["104:4:3:1"],["104:4:4:1","104:4:4:2"]],"word_analysis_refs":["104:4:1","104:4:2","104:4:3","104:4:4","104:4:5"],"word_rows":[{"analysis_record_ref":"104:4:1","analytic_gloss_range_en":"deterrent rebuke particle that rejects the prior immortality claim while opening the sworn punishment verdict","analytic_root_gloss_range_en":null,"qac_refs":["104:4:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"كَلَّا","transliteration":"kallā"}},{"analysis_record_ref":"104:4:2","analytic_gloss_range_en":"oath-response prefix that binds the following passive verb into sworn certainty","analytic_root_gloss_range_en":null,"qac_refs":["104:4:2:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَ","transliteration":"la-"}},{"analysis_record_ref":"104:4:3","analytic_gloss_range_en":"oath-bound passive flinging away, with contemptuous discard and destination-directed motion into the following prepositional phrase","analytic_root_gloss_range_en":"root range includes casting away, repudiating, withdrawing aside, remnants, and vessel-infusion senses; the local passive oath frame selects contemptuous disposal while some separation and containment pressures survive only as image or constructional support","qac_refs":["104:4:2:2","104:4:2:3"],"root":{"arabic":"ن ب ذ","transliteration":"n-b-dh"},"surface":{"arabic":"يُنۢبَذَنَّ","transliteration":"yunbadhanna"}},{"analysis_record_ref":"104:4:4","analytic_gloss_range_en":"preposition marking directed containment into the named destination, not static location alone","analytic_root_gloss_range_en":null,"qac_refs":["104:4:3:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"فِى","transliteration":"fī"}},{"analysis_record_ref":"104:4:5","analytic_gloss_range_en":"definite proper-name-like intensive noun, the Crusher, functioning as the genitive destination and as a forward setup for definition","analytic_root_gloss_range_en":"root range includes breaking dry or hard things into fragments, a fire named for crushing what it meets, severe breaking conditions, harsh crushing masses, and debris of worldly goods; the local noun selects the named fire-crusher sense with debris and fragmentation pressure","qac_refs":["104:4:4:1","104:4:4:2"],"root":{"arabic":"ح ط م","transliteration":"ḥ-ṭ-m"},"surface":{"arabic":"ٱلْحُطَمَةِ","transliteration":"al-ḥuṭamah"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["104:4"],"branch_refs":["root_000337/B001","root_001466/B001"],"candidate_id":"cand_48f791e38f8a434e20ec","evidence_scope":"focus_ayah","hft_ref":"hft_8089ee59aea165302b8a","item_id":"baseline_discard_to_comminution","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_discard_to_comminution","support_id":"sup_c190bb38923e1f1d4bba"},{"anchor_refs":["104:4"],"branch_refs":["root_000337/B003","root_000337/B005","root_001466/B005"],"candidate_id":"cand_f3204c6924368a8ca114","evidence_scope":"focus_ayah","hft_ref":"hft_8bf1764ee25940c1e7b8","item_id":"baseline_attritional_reduction","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_attritional_reduction","support_id":"sup_bb908782094e8de50ec0"},{"anchor_refs":["104:4"],"branch_refs":["root_000337/B004","root_000337/B006","root_001466/B002"],"candidate_id":"cand_83f15fc7c30c038e778b","evidence_scope":"focus_ayah","hft_ref":"hft_1d64662891ae8ebabd20","item_id":"baseline_adversarial_excommunication","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_adversarial_excommunication","support_id":"sup_bdfe0ae4d4049c76fe0f"},{"anchor_refs":["104:4"],"branch_refs":["root_000337/B008","root_001466/B006"],"candidate_id":"cand_83fac0b5c240df2acaa0","evidence_scope":"focus_ayah","hft_ref":"hft_bac5a81cea8c9c221380","item_id":"baseline_vessel_grinder","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_vessel_grinder","support_id":"sup_65416a2aba224274a831"}],"diagnostics":[],"lane_counts":{"global":11,"macro":14,"micro":4},"packet_summary":{"ayah_count":9,"focus_ref":"104:4","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"و ص د","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000036","furuq_root_norm":"ء ص د","furuq_source_root_norm":"أ ص د","is_dominant":true,"target_occurrences":2,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001653","furuq_root_norm":"و ص د","furuq_source_root_norm":"و ص د","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["104:1","104:2","104:3","104:4","104:5","104:6","104:7","104:8","104:9"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"104:4","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":11,"source_present":true,"structured_insight_count":18,"unstructured_record_count":0},"identity":{"ayah_ref":"104:4","lane":"micro","linguistic_source_ref":"104:4","surface_ref":"104:4","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"104:4","target_tokens":[["Hayır",["104:4:1"]],["Kesinlikle",["104:4:2"]],["Ezici'ye",["104:4:3","104:4:4"]],["atılacaktır",["104:4:2"]]],"text":"Hayır! Kesinlikle Ezici'ye atılacaktır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":9,"id":"s104-p01-001-009","label":"Whole surah","number":1,"refs":["104:1","104:2","104:3","104:4","104:5","104:6","104:7","104:8","104:9"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:1","source_type":"word_analysis","support_id":"sup_0101610c15d216f68bc9","text":"{\"gloss_range\":\"deterrent rebuke particle that rejects the prior immortality claim while opening the sworn punishment verdict\",\"prose\":\"{{ar:كَلَّا}} ({{tr:kallā}}) is not a loose connective. It first shuts down the previous claim that wealth has made the person lasting, then it turns the ayah toward the oath-backed verdict {{ar:لَيُنۢبَذَنَّ}} ({{tr:la-yunbadhanna}}). The reader hears the discourse break before the punishment verb appears: private reckoning is interrupted by a public rebuke, and the particle performs that stopping rather than merely reporting it. Its force is both semantic and acoustic, because the separate pause-beat and the doubled middle consonant make the refusal stand as its own compressed blow before the clause moves on.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:كَلَّا}} ({{tr:kallā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:1:opening-boundary-shift","source_type":"word_analysis","support_id":"sup_0abdc37180acf7972fe2","text":"{\"blocking_evidence\":null,\"headline\":\"first word ruptures the prior scene\",\"reader_payoff\":\"The reader notices that the ayah begins by crossing from the hoarder's inner calculation into an imposed judgment.\",\"reason\":\"The cross-reference evidence makes the previous proposition the active target of the particle, so its initial position marks a discourse boundary.\",\"representative_source_ids\":[\"QT-32ac9981\",\"QT-edb743f0\",\"QB-606d3b19\",\"QB-af03408a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:1:audible-isolated-refusal","source_type":"word_analysis","support_id":"sup_0f75c56dcb92e1571358","text":"{\"blocking_evidence\":null,\"headline\":\"rebuke is heard as a separate beat\",\"reader_payoff\":\"The reader notices that the pause-beat and tightened sound make the refusal audible before the passive verdict unfolds.\",\"reason\":\"The surface word is a standalone particle before the oath-verb frame, and the recitational note preserves it as a distinct beat.\",\"representative_source_ids\":[\"QF-78927104\",\"QP-e224926b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:3:stark-form-i-passive","source_type":"word_analysis","support_id":"sup_11b08ec675b553ddb6ba","text":"{\"blocking_evidence\":null,\"headline\":\"simple stem keeps the act stark\",\"reader_payoff\":\"The reader notices that the morphology leaves a direct imposed flinging, not self-withdrawal or causative manipulation.\",\"reason\":\"The reference row identifies the local form as passive Form I and gives no local licensing for a causative or reflexive reading.\",\"representative_source_ids\":[\"QF-0361fd75\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:5:sound-and-fawasil-pressure","source_type":"word_analysis","support_id":"sup_1346c95132bf3ab258fd","text":"{\"blocking_evidence\":null,\"headline\":\"sound reinforces the named closure\",\"reader_payoff\":\"The reader notices that the word's onset, consonant weight, and repeated ending make the Crusher heard as a strong closing name.\",\"reason\":\"The sound observations track the local surface and same-word recurrence without adding a separate lexical sense.\",\"representative_source_ids\":[\"QP-5c057177\",\"QP-64bf3bbc\",\"QP-aae4d252\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:5:genitive-destination-role","source_type":"word_analysis","support_id":"sup_154d9bfe92ee10d242f7","text":"{\"blocking_evidence\":null,\"headline\":\"case binds the name to the trajectory\",\"reader_payoff\":\"The reader notices that {{ar:ٱلْحُطَمَةِ}} ({{tr:al-ḥuṭamah}}) completes the motion as a governed endpoint rather than floating as an appositional title.\",\"reason\":\"The noun is genitive under {{ar:فِى}} ({{tr:fī}}), and the attachment evidence makes it the destination complement of the passive verb.\",\"representative_source_ids\":[\"QG-77cd233f\",\"QG-a98c4712\",\"QT-65c91ece\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:4:visible-destination-beat","source_type":"word_analysis","support_id":"sup_21114db8076159cc0758","text":"{\"blocking_evidence\":null,\"headline\":\"separate preposition stages the destination\",\"reader_payoff\":\"The reader notices the syntax pushing forward from verdict into scene, with the destination arriving as a distinct beat.\",\"reason\":\"The independent preposition forms the hinge between the passive verb and the named endpoint.\",\"representative_source_ids\":[\"QF-e5e64d8d\",\"QT-879d16b3\",\"QT-c6e91e9a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:5","source_type":"word_analysis","support_id":"sup_305650569da68281c0f1","text":"{\"gloss_range\":\"definite proper-name-like intensive noun, the Crusher, functioning as the genitive destination and as a forward setup for definition\",\"prose\":\"{{ar:ٱلْحُطَمَةِ}} ({{tr:al-ḥuṭamah}}) is the ayah's landing word. Governed by {{ar:فِى}} ({{tr:fī}}), it is the containing endpoint into which the passive patient is flung, not the object being thrown. Its definite, feminine, intensive shape makes it feel like a named entity whose identity is crushing, not a one-time act or a pile of fragments; the active-participle variant clarifies that contrast by showing a possible shift from identity-defining crusher to one actively crushing. The root {{ar:ح ط م}} ({{tr:ḥ-ṭ-m}}) answers the prior fantasy of permanence with fragmentation: accumulated wealth meets a name built from breaking structured things apart. The noun also creates forward pressure, because the same name returns as the question in 104:5 and is specified as fire in 104:6. Rarity, closure, and sound converge: the ayah ends on the Crusher, the repeated terminal shape binds 104:4 to 104:5, and the heavy consonant texture reinforces crushing and enclosure so the destination, not the act alone, stays in the reader's ear.\",\"root_display\":\"{{ar:ح ط م}} ({{tr:ḥ-ṭ-m}})\",\"root_gloss_range\":\"root range includes breaking dry or hard things into fragments, a fire named for crushing what it meets, severe breaking conditions, harsh crushing masses, and debris of worldly goods; the local noun selects the named fire-crusher sense with debris and fragmentation pressure\",\"surface_display\":\"{{ar:ٱلْحُطَمَةِ}} ({{tr:al-ḥuṭamah}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:2:bound-verb-architecture","source_type":"word_analysis","support_id":"sup_331a60afbef6ea6a8b08","text":"{\"blocking_evidence\":null,\"headline\":\"certainty is fused to the verb\",\"reader_payoff\":\"The reader notices that the oath force is not commentary outside the clause; it is carried by the beginning and ending of the verb-frame.\",\"reason\":\"The segmentation gives the prefix separately, but the grammar treats it with the heavy ending as one emphatic verbal architecture.\",\"representative_source_ids\":[\"QF-db42b841\",\"QT-dc041b1d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:4:fire-and-sealed-containment-anticipation","source_type":"word_analysis","support_id":"sup_3492a56db69e8cbcf82f","text":"{\"blocking_evidence\":null,\"headline\":\"containment points forward\",\"reader_payoff\":\"The reader notices that the preposition prepares the later definition as fire (104:6) and sealed enclosure (104:8).\",\"reason\":\"The local phrase is containment into the named destination, and the same surah later identifies and closes that destination.\",\"representative_source_ids\":[\"QS-b15cd0f8\",\"MG-ad05c023\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:3:audible-emphatic-closure","source_type":"word_analysis","support_id":"sup_359b90831b3517edfa11","text":"{\"blocking_evidence\":null,\"headline\":\"sound reinforces the sealed verdict\",\"reader_payoff\":\"The reader notices the verdict's closure as audible pressure around the root and at the heavy ending.\",\"reason\":\"The heavy ending is grammatically real; more detailed phonetic texture and pausal variant pressure are retained as sound support rather than as independent semantic claims.\",\"representative_source_ids\":[\"QE-a1fb00b4\",\"QP-8c0ab6d4\",\"QP-c7d3ee89\",\"QP-db77b39e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:2:rebuttal-to-sentence-bridge","source_type":"word_analysis","support_id":"sup_38ac920a790e6d8ddf7e","text":"{\"blocking_evidence\":null,\"headline\":\"rebuke becomes sworn adjudication\",\"reader_payoff\":\"The reader notices the transition from rejected thought to externally imposed oath-verdict.\",\"reason\":\"The prior particle rejects the earlier claim, and the oath prefix starts the sworn verbal sentence that adjudicates it.\",\"representative_source_ids\":[\"QT-ec134e40\",\"QB-09fdd41b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"104:4:4:2","source_type":"qac_morpheme","support_id":"sup_3b5600ca14fc7982e99b","text":"{\"lemma_ar\":\"حُطَمَة\",\"morph_features\":\"STEM|POS:N|LEM:HuTamap|ROOT:HTm|F|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"104:4:4:2\",\"qac_word_ref\":\"104:4:4\",\"root_ar\":\"ح ط م\",\"surface_ar\":\"حُطَمَةِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:3:discard-root-pressure","source_type":"word_analysis","support_id":"sup_3c2a230a84738a975b87","text":"{\"blocking_evidence\":null,\"headline\":\"throwing is contemptuous disposal\",\"reader_payoff\":\"The reader notices that the action is not neutral transfer but discard, treating the subject as refuse-like after the hoarding scene.\",\"reason\":\"V4 supports the casting-away branch for {{ar:ن ب ذ}} ({{tr:n-b-dh}}); the local passive frame selects disposal into a destination and does not activate every other root branch.\",\"representative_source_ids\":[\"QS-2a64fa98\",\"QS-4e6385f1\",\"QS-55cffec9\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:3:rare-passive-root-deployment","source_type":"word_analysis","support_id":"sup_3dd4d7e2af3ac71af95e","text":"{\"blocking_evidence\":null,\"headline\":\"rare root-form choice marks reversal\",\"reader_payoff\":\"The reader notices that the root field is being deployed in a marked passive oath-verdict rather than a routine active casting scene.\",\"reason\":\"The contextual profile gives this exact form as low occurrence with one passive instance, supporting the marked local deployment without turning rarity into a separate sense.\",\"representative_source_ids\":[\"QI-45d18789\",\"QI-4d26af5d\",\"QH-70945c6f\",\"QH-9019c960\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:5:intensive-producer-not-product","source_type":"word_analysis","support_id":"sup_42c35ac46868eacabdad","text":"{\"blocking_evidence\":null,\"headline\":\"the form makes crushing identity-defining\",\"reader_payoff\":\"The reader notices that the word names the entity that makes fragments, not merely the fragments left behind.\",\"reason\":\"The local noun is built on the intensive pattern and V4 includes the accepted fire/crusher sense for the same lexical item.\",\"representative_source_ids\":[\"QS-bc2249b3\",\"QF-7b289e6f\",\"QF-ee23d584\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:3:passive-patient-reversal","source_type":"word_analysis","support_id":"sup_48962cbb7f20f21c2371","text":"{\"blocking_evidence\":null,\"headline\":\"active reckoner becomes passive patient\",\"reader_payoff\":\"The reader notices that the person who actively calculated permanence is grammatically reduced to the patient of disposal.\",\"reason\":\"The local verb is passive with an implicit patient-subject and no expressed agent, so the agency reversal is grammatically forced.\",\"representative_source_ids\":[\"QG-3b62c15b\",\"QS-09aac761\",\"QY-cdbfedaf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:3","source_type":"word_analysis","support_id":"sup_505af7f038fa027d6cea","text":"{\"gloss_range\":\"oath-bound passive flinging away, with contemptuous discard and destination-directed motion into the following prepositional phrase\",\"prose\":\"{{ar:يُنۢبَذَنَّ}} ({{tr:yunbadhanna}}) is where the rebuttal becomes an enacted sentence. The passive form suppresses the thrower and leaves the former wealth-counter as the one being flung away; the same referent from the prior claim is carried forward without being renamed. The root {{ar:ن ب ذ}} ({{tr:n-b-dh}}) makes the motion evaluative, not neutral: the person is treated as discard after having treated wealth as permanence. The simple Form I passive keeps the act stark, with no self-withdrawal or causative layer taking over the local sense. The oath prefix and heavy ending make this disposal certain, while the heavy final closure makes that certainty audible around the root. {{ar:فِى ٱلْحُطَمَةِ}} ({{tr:fī l-ḥuṭamah}}) turns the casting into a trajectory into containment; the vessel-infusion and withdrawal branches remain secondary image pressure, sharpening containment and separation without replacing passive disposal. Variant readings sharpen the canonical choice: active, plural, or dual routings show other possible agency and patient structures, while the base reading keeps one condemned figure as passive patient. In the wider root field, this oath-bound passive deployment is marked rather than routine. Concrete echoes of casting into overwhelming media (28:40; 51:40) illuminate the construction without replacing the local destination.\",\"root_display\":\"{{ar:ن ب ذ}} ({{tr:n-b-dh}})\",\"root_gloss_range\":\"root range includes casting away, repudiating, withdrawing aside, remnants, and vessel-infusion senses; the local passive oath frame selects contemptuous disposal while some separation and containment pressures survive only as image or constructional support\",\"surface_display\":\"{{ar:يُنۢبَذَنَّ}} ({{tr:yunbadhanna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:3:verdict-scene-pivot","source_type":"word_analysis","support_id":"sup_646978f252dc49f7f886","text":"{\"blocking_evidence\":null,\"headline\":\"the middle verb converts thought into scene\",\"reader_payoff\":\"The reader notices the structural turn from an inner calculation to a kinetic punishment scene.\",\"reason\":\"The clause structure places the passive verb between the rebuke and destination, making it the local conversion point.\",\"representative_source_ids\":[\"QT-a2f156ca\",\"QB-5dd9aa4c\",\"QB-64289448\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:3:destination-directed-argument-frame","source_type":"word_analysis","support_id":"sup_65f4068f9e7915ffdd59","text":"{\"blocking_evidence\":null,\"headline\":\"discard becomes trajectory into containment\",\"reader_payoff\":\"The reader notices that the verb opens a path toward {{ar:فِى ٱلْحُطَمَةِ}} ({{tr:fī l-ḥuṭamah}}), so the disposal is directed into a containing destination.\",\"reason\":\"The forced attachment makes {{ar:فِى ٱلْحُطَمَةِ}} ({{tr:fī l-ḥuṭamah}}) the destination complement of the passive verb; the echoes at 28:40 and 51:40 are structural parallels, not replacements for the local scene.\",\"representative_source_ids\":[\"QG-f56af7da\",\"QT-29102a43\",\"QE-793b090a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:5:permanence-meets-fragmentation","source_type":"word_analysis","support_id":"sup_6e63aaec1d22ba911cee","text":"{\"blocking_evidence\":null,\"headline\":\"wealth permanence is answered by breaking\",\"reader_payoff\":\"The reader notices that the root image answers the previous claim of permanence with the logic of fragmentation.\",\"reason\":\"The prior claim supplies the discourse target, while the accepted root branches support breaking and debris pressure; the local sense remains the named Crusher.\",\"representative_source_ids\":[\"QS-3c49035a\",\"QS-9971cc95\",\"QB-cfa6255b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:4:directed-containment","source_type":"word_analysis","support_id":"sup_6f9e2897c26559f610dd","text":"{\"blocking_evidence\":null,\"headline\":\"preposition turns motion into enclosure\",\"reader_payoff\":\"The reader notices that the flinging is directed into containment, not left as disposal without an endpoint.\",\"reason\":\"The attachment evidence makes the following noun the prepositional complement and destination of the passive verb.\",\"representative_source_ids\":[\"QG-ff302d80\",\"QS-cdb82d7c\",\"MG-ad05c023\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:3:oath-bound-passive-future","source_type":"word_analysis","support_id":"sup_8778870f9d668c27a7b9","text":"{\"blocking_evidence\":null,\"headline\":\"passive verdict is sealed by emphasis\",\"reader_payoff\":\"The reader notices that the verb is not merely future passive; it is the compressed answer to an unstated oath.\",\"reason\":\"The oath lām and heavy energetic ending are both identified in the reference evidence, and the ellipsis evidence marks the oath expression as compressed.\",\"representative_source_ids\":[\"QG-65e515e2\",\"QF-59e71f91\",\"QI-17636190\",\"QT-276487b6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:3:referent-continuity-without-renaming","source_type":"word_analysis","support_id":"sup_8e15351db026ce952f02","text":"{\"blocking_evidence\":null,\"headline\":\"the prior person is carried into the passive\",\"reader_payoff\":\"The reader notices that the passive is not anonymous; it carries forward the person whose wealth claim was just rejected.\",\"reason\":\"The attachment evidence marks a 3ms implicit subject with a discourse candidate available, continuing the condemned individual.\",\"representative_source_ids\":[\"QG-7c4a6fa5\",\"QB-e185f53f\",\"QB-0b5af217\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:4","source_type":"word_analysis","support_id":"sup_91903819919d9a579874","text":"{\"gloss_range\":\"preposition marking directed containment into the named destination, not static location alone\",\"prose\":\"{{ar:فِى}} ({{tr:fī}}) keeps the punishment from ending as a bare act of flinging. Because it governs {{ar:ٱلْحُطَمَةِ}} ({{tr:al-ḥuṭamah}}), the motion becomes directed containment: the subject is flung into the named Crusher, not merely described as located there. The independent preposition also gives the ayah a staged beat, action first and destination second. Its construction recalls casting into overwhelming media (28:40; 51:40), while the local surah later confirms closed containment (104:8) and fire-definition (104:6).\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فِى}} ({{tr:fī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:4:audible-liaison","source_type":"word_analysis","support_id":"sup_9df1441a24ac0de94052","text":"{\"blocking_evidence\":null,\"headline\":\"sound links preposition and destination\",\"reader_payoff\":\"The reader notices that recitation can make the preposition and destination sound like one directed movement while grammar keeps them distinct.\",\"reason\":\"The row is a coherent recitational observation about the local word boundary and does not conflict with the grammatical separation.\",\"representative_source_ids\":[\"QP-1dea9dcb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:3:contained-casting-image-pressure","source_type":"word_analysis","support_id":"sup_9e76a415356925dcba84","text":"{\"blocking_evidence\":null,\"headline\":\"vessel and separation images support containment\",\"reader_payoff\":\"The reader notices a secondary pressure of being cast away into a containing place and separated from imagined permanence.\",\"reason\":\"The local sense remains passive disposal; infusion and withdrawal branches survive only as image pressure because the local construction supplies actual containment through the prepositional phrase.\",\"representative_source_ids\":[\"QS-3e799e85\",\"QS-d05fe172\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:2","source_type":"word_analysis","support_id":"sup_b718aa5cb1c3022d5d29","text":"{\"gloss_range\":\"oath-response prefix that binds the following passive verb into sworn certainty\",\"prose\":\"{{ar:لَ}} ({{tr:la-}}) is the oath-response prefix, not a free-standing intensifier. Its force is completed by the heavy ending on {{ar:يُنۢبَذَنَّ}} ({{tr:yunbadhanna}}), so the punishment arrives as sworn certainty even though the oath formula itself is left unspoken. After {{ar:كَلَّا}} ({{tr:kallā}}), this prefix raises the register from rebuttal into sentence: the clause is compressed, but its certainty is built into the verb-frame.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَ}} ({{tr:la-}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:5:rare-local-signature","source_type":"word_analysis","support_id":"sup_bfb561fc832e720ecfd5","text":"{\"blocking_evidence\":null,\"headline\":\"rare root and name concentrate locally\",\"reader_payoff\":\"The reader notices that this scarce crushing root and surah-confined name become a local signature of the threat sequence.\",\"reason\":\"The rarity and local recurrence are supported; broader analogies in the source row are treated only as background and do not control the local parse.\",\"representative_source_ids\":[\"QI-39c3a8aa\",\"QH-09359ca6\",\"MH-28ad6ee0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:5:immediate-return-and-definition","source_type":"word_analysis","support_id":"sup_c329e9f476fdef28556a","text":"{\"blocking_evidence\":null,\"headline\":\"first mention sets up the question\",\"reader_payoff\":\"The reader notices that the final name in 104:4 is not self-contained; it returns in 104:5 as the object of definition.\",\"reason\":\"The reference evidence points to the immediate same-surah recurrence at 104:5, where the name becomes the queried topic.\",\"representative_source_ids\":[\"QG-53df8735\",\"QI-1099856e\",\"QE-5084e054\",\"QE-a868a49a\",\"QH-e684a5a6\",\"QB-c0cf5dca\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:5:fire-defined-by-crushing","source_type":"word_analysis","support_id":"sup_c79231072aacbdb7f930","text":"{\"blocking_evidence\":null,\"headline\":\"crushing name anticipates fire definition\",\"reader_payoff\":\"The reader notices that the fire later named in 104:6 is introduced first through the action of crushing.\",\"reason\":\"V4 accepts the named fire/crusher sense for the local lexical item, and the following ayah sequence defines the name as fire in 104:6.\",\"representative_source_ids\":[\"QS-ccab7061\",\"QB-422e5c28\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:5:crusher-over-debris","source_type":"word_analysis","support_id":"sup_ca31810e8772e5104356","text":"{\"blocking_evidence\":null,\"headline\":\"debris field sharpens the selected name\",\"reader_payoff\":\"The reader notices the produced-fragment field behind the name while the local noun remains the active Crusher.\",\"reason\":\"The root field supports debris and breaking, but the local form selects the proper-name-like crushing entity rather than the debris product alone.\",\"representative_source_ids\":[\"QS-214640c4\",\"QS-902e5549\",\"QI-b46d8f46\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"104:4:2:2","source_type":"qac_morpheme","support_id":"sup_d5757a53e4ae823313b3","text":"{\"lemma_ar\":\"نَبَذَ\",\"morph_features\":\"STEM|POS:V|IMPF|PASS|LEM:naba*a|ROOT:nb*|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"104:4:2:2\",\"qac_word_ref\":\"104:4:2\",\"root_ar\":\"ن ب ذ\",\"surface_ar\":\"يُنۢبَذَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:1:performative-meccan-confrontation","source_type":"word_analysis","support_id":"sup_d884edaee758ad2a6edd","text":"{\"blocking_evidence\":null,\"headline\":\"confrontational speech act\",\"reader_payoff\":\"The reader notices that the particle does the work of rebuke in a confrontation register, not merely reporting that the previous idea is false.\",\"reason\":\"The local grammar supports the deterrent function; the Meccan distribution is retained only as register support, not as an independent local meaning.\",\"representative_source_ids\":[\"MG-143bee46\",\"QS-54b32a3c\",\"QI-52a5e8b7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:1:rebuke-and-verdict-pivot","source_type":"word_analysis","support_id":"sup_e374ebbbc389a3a312af","text":"{\"blocking_evidence\":null,\"headline\":\"rebuke opens into verdict\",\"reader_payoff\":\"The reader notices that {{ar:كَلَّا}} ({{tr:kallā}}) simultaneously cancels the prior immortality claim and opens the certain punishment sentence.\",\"reason\":\"QAC identifies the word as a deterrent rebuke particle, and the attachment cross-reference links it to the immediately preceding proposition while the following clause supplies the verdict.\",\"representative_source_ids\":[\"QG-c61e07f5\",\"QS-1b8d8af8\",\"QY-23baf353\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:5:proper-name-definite-crusher","source_type":"word_analysis","support_id":"sup_e5630c37323b6c7f45cf","text":"{\"blocking_evidence\":null,\"headline\":\"definite form names a crushing entity\",\"reader_payoff\":\"The reader notices that the destination is presented as a specific named Crusher, not an indefinite crushing force.\",\"reason\":\"QAC identifies the word as definite, feminine, genitive, and proper-name-like, while the contextual evidence shows same-surah confinement.\",\"representative_source_ids\":[\"QG-0a4a24d6\",\"QF-321d0bf2\",\"QH-09359ca6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:5:ayah-final-destination-closure","source_type":"word_analysis","support_id":"sup_eafa93ff0fb6a85cfb71","text":"{\"blocking_evidence\":null,\"headline\":\"the destination is the final beat\",\"reader_payoff\":\"The reader notices that the ayah lands on the destination itself, making the Crusher the take-away of the scene.\",\"reason\":\"The local clause ends with the governed destination after the passive verb and preposition, so closure falls on the named endpoint.\",\"representative_source_ids\":[\"QT-6ca0ccad\",\"QT-a0ede7cd\",\"QY-a6101af8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:5:active-participle-variant-contrast","source_type":"word_analysis","support_id":"sup_f7a2ffb0c7e1364331bd","text":"{\"blocking_evidence\":null,\"headline\":\"variant clarifies identity-force\",\"reader_payoff\":\"The reader notices by contrast that the base form presents identity-defining crushing rather than only an active participial action.\",\"reason\":\"The variant is useful contrast, but the aligned local surface remains the intensive noun.\",\"representative_source_ids\":[\"QF-bf0c1461\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:2:oath-response-certainty","source_type":"word_analysis","support_id":"sup_feaee77cc60fd7d38555","text":"{\"blocking_evidence\":null,\"headline\":\"oath lām fixes certainty\",\"reader_payoff\":\"The reader notices that the following passive event is oath-backed certainty, not ordinary prediction.\",\"reason\":\"QAC and attachment evidence identify the prefix as lām al-qasam paired with the heavy energetic ending and as the answer of an implicit oath.\",\"representative_source_ids\":[\"QG-3be9c90e\",\"QS-0e0bc55c\",\"QI-a0c6732d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:4:3:qiraat-agency-and-number-contrast","source_type":"word_analysis","support_id":"sup_ff2b14139fa1369fa77e","text":"{\"blocking_evidence\":null,\"headline\":\"variants expose the canonical routing\",\"reader_payoff\":\"The reader notices by contrast that the base reading keeps the condemned figure singular and passive rather than active, plural, or dual.\",\"reason\":\"Variant readings are useful apparatus for agency and number contrast, while the canonical local parse remains passive 3ms.\",\"representative_source_ids\":[\"QG-2ed7428d\",\"QG-4349d64b\",\"QF-3b35434a\",\"QF-370fab9b\",\"QF-9efa17b3\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّا ۖ لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ","ayah_ref":"104:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000337/B001","root_001466/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001466","role":"Casting away contributes both physical ejection and removal from regard, making the subject discarded input.","root":"ن ب ذ","source_ref":"104:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000337","role":"Fracture of hard matter contributes the destination's comminuting action and its debris-producing result.","root":"ح ط م","source_ref":"104:4","source_word_indices":["4"]}],"changed_reading":{"after":"He will be discarded as valueless input into a comminuting process that reduces a whole to debris.","before":"He will be thrown into a punitive place."},"confidence":"strong","focus_anchor":"The emphatic passive verb at word 2 supplies forced disposal, while fi plus the definite noun at word 4 places the subject inside the named operation or domain.","mechanism":"The subject is first removed from hand and regard, then deposited into a process that fractures hard matter into debris. The sequence is devaluation followed by loss of integrity, not merely relocation followed by an unrelated penalty.","model_id":"baseline_discard_to_comminution"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_discard_to_comminution","source_type":"hft","support_id":"sup_c190bb38923e1f1d4bba","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّا ۖ لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ","ayah_ref":"104:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000337/B003","root_000337/B005","root_001466/B005"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_001466","role":"The slight scattered remainder supplies the end-state of reduction rather than only the initiating throw.","root":"ن ب ذ","source_ref":"104:4","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000337","role":"A devastating season contributes an environmental regime that breaks people and property by sustained scarcity.","root":"ح ط م","source_ref":"104:4","source_word_indices":["4"]},{"branch_id":"B005","mapped_root_id":"root_000337","role":"Bodily wearing-down through age or prolonged exposure supplies the temporal mode of the breaking.","root":"ح ط م","source_ref":"104:4","source_word_indices":["4"]}],"changed_reading":{"after":"The casting enters the subject into a severe condition that keeps wearing him down toward remnant-status.","before":"The casting leads to one catastrophic blow."},"confidence":"medium","focus_anchor":"Fi permits entry into a condition as well as a bounded place, and the two focus roots carry remnant and long-wearing branches.","mechanism":"The casting places the subject within an attritional regime: severity wears down body and property over time until only a slight scattered remainder is left. Al-Hutamah can therefore operate by duration and deprivation alongside sudden impact.","model_id":"baseline_attritional_reduction"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_attritional_reduction","source_type":"hft","support_id":"sup_bb908782094e8de50ec0","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّا ۖ لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ","ayah_ref":"104:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000337/B004","root_000337/B006","root_001466/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001466","role":"Open repudiation contributes a declared severance of relation and status, not a furtive disposal.","root":"ن ب ذ","source_ref":"104:4","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_000337","role":"The violent handler contributes coercive driving and compression of those under control.","root":"ح ط م","source_ref":"104:4","source_word_indices":["4"]},{"branch_id":"B006","mapped_root_id":"root_000337","role":"A crushing mass contributes collective pressure as the medium into which the expelled subject is delivered.","root":"ح ط م","source_ref":"104:4","source_word_indices":["4"]}],"changed_reading":{"after":"An individual is publicly expelled from standing and transferred into coercive collective pressure.","before":"An individual is physically hurled away."},"confidence":"medium","focus_anchor":"The passive n-b-d form can carry open repudiation and separation, while al-Hutamah can name a coercive handler or crushing mass.","mechanism":"The event is social and adversarial before it is material: the subject is openly severed from standing or compact, then handed over to a force that crowds, drives, and crushes. Physical casting and de-recognition coexist.","model_id":"baseline_adversarial_excommunication"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_adversarial_excommunication","source_type":"hft","support_id":"sup_bdfe0ae4d4049c76fe0f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّا ۖ لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ","ayah_ref":"104:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000337/B008","root_001466/B006"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_001466","role":"Casting material into a vessel contributes an ingredient-and-container relation to the passive placement.","root":"ن ب ذ","source_ref":"104:4","source_word_indices":["2"]},{"branch_id":"B008","mapped_root_id":"root_000337","role":"The consuming grinder contributes an internal processing function rather than a passive destination.","root":"ح ط م","source_ref":"104:4","source_word_indices":["4"]}],"changed_reading":{"after":"The subject is inserted into al-Hutamah as material enters a containing grinder or digestor.","before":"The subject crosses into a place called al-Hutamah."},"confidence":"exploratory","focus_anchor":"The construction places the subject in al-Hutamah, and focus branches independently supply casting an ingredient into a vessel and a consuming grinder.","mechanism":"The verse can be carried as a processing image: something is dropped into a containing medium and then consumed or ground there. This is branch-distant but gives fi a functional, not merely locative, role.","model_id":"baseline_vessel_grinder"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_vessel_grinder","source_type":"hft","support_id":"sup_65416a2aba224274a831","trust":"legacy_unbound"}]}
</lane_packet_json>
