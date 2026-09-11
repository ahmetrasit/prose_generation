# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **101:6**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s101-regular-20260911/s101/101_6/micro.discovery.json` and modify nothing
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
  "ayah_ref": "101:6",
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
{"analysis_context":{"analysis_id":"s101-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"101:6","host_surah":101,"lane_context_refs":[],"ordered_context_refs":["101:0","101:1","101:2","101:3","101:4","101:5","101:7","101:8","101:9","101:10","101:11","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Bu dal çıplak ağırlık karşıtlığını anlatır; taşınan eşya, günah yükü ve ölçü adı ayrı dallardır.","branch_kind":"bare","branch_ref":"root_000202/B001","candidate_links":[{"candidate_id":"cand_b1b6f168af58ffd42c5d","lane":"micro"},{"candidate_id":"cand_02ad7ad02cb221fb7d5a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ثَقُلَتْ","morph_features":"STEM|POS:V|PERF|LEM:vaqulato|ROOT:vql|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"101:6:3:1","qac_word_ref":"101:6:3","surface_ar":"ثَقُلَتْ"}],"gloss":"ağırlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, hafifliğin karşıtı olan ağırlık ve ağır gelmedir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Cisimlerdeki ağırlık çekirdeği, soyut durumlara ve değer yargılarına da taşınabilir."}}],"root_ar":"ث ق ل","root_id":"root_000202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çıplak dalın maddi veya soyut hafiflik karşıtı çekirdeğini doğal biçimde verir.","boundary_detail":"Bu dal çıplak ağırlık karşıtlığını anlatır; taşınan eşya, günah yükü ve ölçü adı ayrı dallardır.","branch_image_ar":"الثقل ضد الخفة","concept_gloss":"ağırlık","contextual_glosses":[{"applicability":"Bir şeyin tartıda, bedende veya değerlendirmede hafif sayılmayacak biçimde baskın geldiği bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Baskın gelme ve hafiflik karşıtlığını korur."},"facet_ids":["F001"],"text":"ağır gelme","usage_role":"contextual"},{"applicability":"Maddi ağırlık modelinin soyut değer, söz veya sorumluluk alanına taşındığı yerlerde açıklayıcıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Maddi cisimlerdeki temel ağırlık kullanımını dışarıda bırakır.","preserves":"Soyut alana taşınan ağırlık fikrini korur."},"facet_ids":["F002"],"text":"manevi ağırlık","usage_role":"explanatory"}],"definition":"Bir şeyin hafifliğe karşı ağır gelmesi, tartıda veya değerlendirmede baskın bir ağırlık taşımasıdır; önce cisimler için, sonra soyut nitelikler için kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, hafifliğin karşıtı olan ağırlık ve ağır gelmedir."},{"facet_id":"F002","role":"extension","statement":"Cisimlerdeki ağırlık çekirdeği, soyut durumlara ve değer yargılarına da taşınabilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Taşınan eşya veya yük nesnesi anlamı ekler.","collision":"Ayrı yük ve eşya dalıyla çakışır.","fit":"displacement","loses":"Hafifliğin genel karşıtı olan çıplak ağırlık çekirdeğini kaydırır.","preserves":"Ağırlıkla ilişkili taşınabilir nesne fikrini kısmen korur."},"text":"yük"}],"identity_rationale":"Kaynak ifadesi ağırlığı hafifliğin karşıtı olarak kurar; temel alan cisimlerdeki tartı veya baskın gelme duygusudur, sonra anlam alanlarına da taşınır. Geçici çerçeve bu çekirdeği yük, günah, ölçü birimi veya özel adlandırmalarla karıştırmadan verir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyin ağır gelmesi, hafif olmaması"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"ağırlık, maddi ya da soyut ağır gelme niteliği"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"ağır, ağırlık taşıyan"}],"lexicalization_note":"Bare kapsam, tanımı çıplak ağırlık ve hafiflik karşıtlığıyla sınırlar; özel birleşim anlamları içeri alınmaz.","neighbor_coverage_note":"Komşular içinden ağırlık eksenini gerçekten keskinleştirenler yayımlandı; sertlik, doluluk veya soyut benzerlik taşıyan uzak adaylar sınırı belirginleştirmediği için dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal eksenin ağır tarafını, komşu dal ise hafif veya hafifletilmiş tarafını verir; bu yüzden aynı sahayı paylaşırlar ama yönleri karşıttır.","focus_only":"Odak dal, hafifliğe karşı ağır gelme ve baskın ağırlık alanıdır.","gloss":"ağırlık karşısında hafiflik","neighbor_only":"Komşu dal, hafiflik, yükün azalması veya ağırlaştırmanın kaldırılması alanıdır.","neighbor_ref":"root_000427/B001","relation_type":"polarity_pair","shared_zone":"İki dal aynı ağırlık ekseninde yer alır."},{"boundary_match":"partial","distinction":"Odak dal ağırlığın nitelik olarak kendisini anlatır; komşu dal bu niteliğin belirli ölçü, tartı aracı veya ağırlık miktarı olarak işlem görmesini anlatır.","focus_only":"Odak dal genel ağır gelme niteliğidir.","gloss":"ağırlık ile ölçü ağırlığı","neighbor_only":"Komşu dal ölçü, tartı birimi veya ağırlığı verme işlemiyle sınırlıdır.","neighbor_ref":"root_000202/B004","relation_type":"near_neighbor","shared_zone":"Her ikisi de ağırlığı tartı ve ölçme alanına bağlayabilir."},{"boundary_match":"partial","distinction":"Odak dal genel nitelik düzeyindedir; komşu dal bu niteliğin halsizlik, uyku baskısı, hastalık veya yavaş hareket olarak yaşanmasına bağlıdır.","focus_only":"Odak dal şeyin ağır olma niteliğini verir.","gloss":"ağırlık ile ağırlık hissi","neighbor_only":"Komşu dal bedende, uykuda, hastalıkta veya davranışta hissedilen ağırlık ve yavaşlamadır.","neighbor_ref":"root_000202/B006","relation_type":"near_neighbor","shared_zone":"Her ikisi de hafiflikten uzak ağırlaşma duygusuyla ilgilidir."}],"source_phrase_ar":"ضد الخفة (maqayis;sihah)؛ ثقل ثقلا فهو ثقيل والثقل رجحان الثقيل (ayn;tahdhib)؛ الثقل والخفة متقابلان وأصله في الأجسام ثم في المعاني (mufradat)","source_summary":"Kaynaklar bu dalda ağırlığı hafifliğin karşıtı ve ağır olanın baskın gelişi olarak toplar; maddi alanın asıl, soyut kullanımın genişletilmiş alan olduğunu bildirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"ثقل الشيء ورجحانه على ما يوزن أو يقدر به، في الأجسام ثم في المعاني","what_is_not_ar":"الأمتعة المحمولة؛ الأوزار؛ المثقال؛ الثقلان"},"support_links":["sup_478fcf78ed0e13dadaa5","sup_fe06e8d5eeb0ca1a8266"]},{"boundary":"Dal yük ve çıkarılan ağır nesnelerle sınırlıdır; ahlaki yük ve ölçü ağırlığı ayrı tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_000202/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ثَقُلَتْ","morph_features":"STEM|POS:V|PERF|LEM:vaqulato|ROOT:vql|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"101:6:3:1","qac_word_ref":"101:6:3","surface_ar":"ثَقُلَتْ"}],"gloss":"ağır yükler","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel alan, taşınan eşya, yolcu yükü ve ağır yüktür."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yerin dışarı çıkardığı gömü, beden veya ölüler de ağır çıkarılanlar olarak aynı alana katılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli taşıma ifadesinde yükleri bir yere götürme işlemi anlatılır."}}],"root_ar":"ث ق ل","root_id":"root_000202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Taşınan eşya ve yerden çıkarılan ağır nesneleri birlikte kapsayan en kısa doğal karşılıktır.","boundary_detail":"Dal yük ve çıkarılan ağır nesnelerle sınırlıdır; ahlaki yük ve ölçü ağırlığı ayrı tutulur.","branch_image_ar":"الأثقال المحمولة والمخرجة","concept_gloss":"ağır yükler","contextual_glosses":[{"applicability":"Yolcu malı ve taşınır eşya bağlamlarında doğal Türkçe karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yerden çıkarılan gömü veya beden alanını dışarıda bırakır.","preserves":"Taşınan mal ve eşya alanını korur."},"facet_ids":["F001"],"text":"eşyalar","usage_role":"contextual"},{"applicability":"Taşıma fiiliyle gelen birleşimsel kullanım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ağır yüklerin taşınması bağlamını korur."},"facet_ids":["F003"],"text":"yüklerinizi taşır","usage_role":"contextual"}],"definition":"Taşınan ağır eşya ve yükler ile yerin içinden çıkardığı gömü, beden veya ölü gibi ağır nesnelerdir; taşıma bağlamında yüklenip götürülen şeyler öne çıkar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel alan, taşınan eşya, yolcu yükü ve ağır yüktür."},{"facet_id":"F002","role":"extension","statement":"Yerin dışarı çıkardığı gömü, beden veya ölüler de ağır çıkarılanlar olarak aynı alana katılır."},{"facet_id":"F003","role":"associated_use","statement":"Belirli taşıma ifadesinde yükleri bir yere götürme işlemi anlatılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Ahlaki sorumluluk ve suç anlamı ekler.","collision":"Ayrı günah yükü dalıyla çakışır.","fit":"displacement","loses":"Taşınan eşya ve yerden çıkarılan nesne çekirdeğini kaybeder.","preserves":"Ağırlık yapan şey fikrini mecazi olarak korur."},"text":"günahlar"}],"identity_rationale":"Kaynak ifadesi hem yolcunun eşyası ve ağır yüklerini hem de yerin çıkardığı gömü, beden veya ölüleri aynı taşınan ya da çıkarılan ağırlık alanında toplar. Bu çerçeve günah yükü ve ölçü birimi anlamlarını dışarıda tutarak kullanılabilir.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yolcunun eşyası ve beraberindeki taşınır yük"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yükler, eşyalar veya yerin çıkardığı ağır şeyler"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yüklerinizi taşır"}],"lexicalization_note":"Mixed_non_bare kapsam, hem biçimsel çoğul kullanımları hem de belirli taşıma birleşimini ayırarak tanımlamayı gerektirir.","neighbor_coverage_note":"Taşıma, yer, gömme ve yük alanını paylaşan adaylar değerlendirildi; yol aşınması veya toprak yüzeyi gibi adaylar dalın nesne sınırını açıklamadığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal taşınan nesneyi anlatır; komşu dal o nesneyi taşıyan vasıta veya binek tarafında kalır.","focus_only":"Odak dal taşınan yük ve eşyadır.","gloss":"yük ile yük taşıyan binek","neighbor_only":"Komşu dal yük taşıyan binek veya taşıma aracı alanındadır.","neighbor_ref":"root_000970/B005","relation_type":"same_field","shared_zone":"İki dal taşıma ve yüklenme sahasını paylaşır."},{"boundary_match":"thematic_only","distinction":"Odak dal çıkma veya taşınma nesnesini verir; komşu dal gömme yeri ve yerleştirme işlemini verir.","focus_only":"Odak dal yerden çıkan veya taşınan ağır nesneleri kapsar.","gloss":"yerin çıkardığılar ile gömme","neighbor_only":"Komşu dal ölünün gömüldüğü yer ve gömme eylemidir.","neighbor_ref":"root_001195/B001","relation_type":"thematic","shared_zone":"İki dal ölü beden ve toprakla ilişkili sahnede karşılaşabilir."},{"boundary_match":"partial","distinction":"Odak dal ağırlığı taşınan nesne olarak somutlaştırır; komşu dal böyle bir eşya veya taşıma koşulu olmadan ağırlık niteliğini anlatır.","focus_only":"Odak dal taşınan maddi yük ve eşyalardır.","gloss":"yük ile ağırlık","neighbor_only":"Komşu dal hafifliğin karşıtı olan genel ağırlık niteliğidir.","neighbor_ref":"root_000202/B001","relation_type":"near_neighbor","shared_zone":"Her ikisi de ağır olma ve hafiflikten uzaklık fikrini paylaşır."}],"source_phrase_ar":"أثقال الأرض كنوزها وأجساد بني آدم (maqayis;sihah;mufradat)؛ متاع المسافر وحشمه وجمعه أثقال (ayn;sihah;tahdhib)؛ تحمل أثقالكم أي أحمالكم الثقيلة (mufradat)","source_summary":"Kaynaklar dalı yolcunun eşyası, yüklenen ağır mallar ve yerin dışarı çıkardığı saklı veya gömülü nesneler çevresinde toplar; taşıma örneği bu nesne alanının eylem bağlamıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الأمتعة والأحمال الثقيلة، وما في الأرض من كنوز أو أجساد أو موتى","what_is_not_ar":"الأوزار والآثام؛ المثقال؛ الثقلان؛ ثقل السمع"},"support_links":[]},{"boundary":"Dal ahlaki yük ve günah sorumluluğudur; maddi yük veya tartı anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000202/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ثَقُلَتْ","morph_features":"STEM|POS:V|PERF|LEM:vaqulato|ROOT:vql|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"101:6:3:1","qac_word_ref":"101:6:3","surface_ar":"ثَقُلَتْ"}],"gloss":"günah yükü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Günah ve suçlar sahibine yüklenen ağır sorumluluklar gibi düşünülür."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ağırlaştırılmış kişi, günahlarının yükünü taşımaya çağıran kimse olarak betimlenir."}}],"root_ar":"ث ق ل","root_id":"root_000202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ahlaki sorumlulukların yük gibi ağırlaştırdığı bağlamları tam karşılar.","boundary_detail":"Dal ahlaki yük ve günah sorumluluğudur; maddi yük veya tartı anlamı değildir.","branch_image_ar":"الأوزار المثقلة","concept_gloss":"günah yükü","contextual_glosses":[{"applicability":"Çoğul ahlaki sorumluluk bağlamında doğal ve kısa çeviridir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yük gibi ağırlaştırma imgesini açıkça söylemez.","preserves":"Suç ve günah içeriğini korur."},"facet_ids":["F001"],"text":"günahları","usage_role":"contextual"},{"applicability":"Günahlarıyla ağırlaşmış kişinin betimlendiği yerde açıklayıcıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin günah yüküyle ağırlaşmasını korur."},"facet_ids":["F002"],"text":"yükü ağır olan kişi","usage_role":"explanatory"}],"definition":"Kişiyi yük gibi ağırlaştıran günahlar, suçlar ve sorumluluklardır; kişi bunları taşır ya da bunların ağırlığıyla yardım çağırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Günah ve suçlar sahibine yüklenen ağır sorumluluklar gibi düşünülür."},{"facet_id":"F002","role":"associated_use","statement":"Ağırlaştırılmış kişi, günahlarının yükünü taşımaya çağıran kimse olarak betimlenir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Maddi taşınır nesne anlamı ekler.","collision":"Ayrı maddi yük dalıyla çakışır.","fit":"displacement","loses":"Ahlaki günah ve sorumluluk içeriğini kaybeder.","preserves":"Yük fikrini korur."},"text":"eşyalar"}],"identity_rationale":"Kaynak ifadesi bu dalı günah, suç ve sorumlulukların kişiyi ağırlaştırması olarak verir. Çerçeve maddi eşya, gebelik veya ölçü alanını dışarıda bıraktığı sürece kaynağa uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kişiyi ağırlaştıran günahlar ve sorumluluklar"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"günah yüküyle ağırlaşmış kimse"}],"lexicalization_note":"Mixed_non_bare kapsam, çoğul yük biçimini ve ağırlaştırılmış kişi kullanımını ahlaki sorumluluk sınırında tutar.","neighbor_coverage_note":"Ahlaki yük, insan hali ve sorumluluk alanındaki adaylar gözden geçirildi; övgü, erkeklik veya genel huy gibi adaylar odak anlamla yalnızca uzak tematik bağ kurdu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ağırlık imgesini ahlaki sorumluluğa bağlar; komşu dal bu özel günah koşulu olmadan genel ağırlık niteliğini verir.","focus_only":"Odak dal günah ve sorumlulukların yük oluşudur.","gloss":"günah yükü ile ağırlık","neighbor_only":"Komşu dal hafifliğin karşıtı olan genel ağırlık niteliğidir.","neighbor_ref":"root_000202/B001","relation_type":"near_neighbor","shared_zone":"İki dal ağır gelme modelini paylaşır."},{"boundary_match":"partial","distinction":"Odak dal ahlaki sorumluluk eksenindedir; komşu dal bedensel veya davranışsal ağırlık ve yavaşlama eksenindedir.","focus_only":"Odak dal suç ve günah ağırlığıdır.","gloss":"günah yükü ile halsizlik","neighbor_only":"Komşu dal hastalık, uyku, yemek veya yavaşlık kaynaklı ağırlık halidir.","neighbor_ref":"root_000202/B006","relation_type":"near_neighbor","shared_zone":"Her ikisi de kişinin üzerinde ağırlık oluşmasını anlatır."},{"boundary_match":"field_only","distinction":"Odak dal yüklenen günaha odaklanır; komşu dal kişinin izlediği yol veya karakter haliyle ilgilidir.","focus_only":"Odak dal ahlaki yükün kendisidir.","gloss":"sorumluluk yükü ile gidişat","neighbor_only":"Komşu dal kişinin gidişatı, yolu veya hali anlamındaki yaşam biçimidir.","neighbor_ref":"root_000769/B002","relation_type":"same_field","shared_zone":"İki dal insan davranışı ve ahlaki durum alanında buluşabilir."}],"source_phrase_ar":"الأثقال الآثام (ayn)؛ حاملة أوزار وخطايا (ayn)؛ أوزارهم وأوزار من أضلوا وهي الآثام (tahdhib)؛ أثقالهم آثامهم التي تثقلهم وتثبطهم (mufradat)","source_summary":"Kaynaklar dalı günah, suç ve sapıtmanın kişiye yüklediği manevi ağırlık olarak açıklar; ağırlık burada maddi nesne değil, ahlaki sorumluluğun baskısıdır.","sources":["AY","TA","MU"],"what_is_ar":"الآثام والأوزار والخطايا التي تثقل صاحبها أو تدعى نفس مثقلة إلى حملها","what_is_not_ar":"الأمتعة الحسية؛ كنوز الأرض؛ الوزن بالمثقال؛ حمل المرأة"},"support_links":[]},{"boundary":"Dal tartı ve ölçü ağırlığıdır; genel ağırlık veya değer yüceliği değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000202/B004","candidate_links":[{"candidate_id":"cand_b1b6f168af58ffd42c5d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ثَقُلَتْ","morph_features":"STEM|POS:V|PERF|LEM:vaqulato|ROOT:vql|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"101:6:3:1","qac_word_ref":"101:6:3","surface_ar":"ثَقُلَتْ"}],"gloss":"ölçü ağırlığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel alan, bilinen ağırlık ölçüsü veya tartıda kullanılan ağırlıktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyin kendi ağırlık miktarı veya ona denk tartı karşılığı ifade edilebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ağırlığını vermek veya bir hayvanı tartmak, ölçme alanının eylem kullanımlarıdır."}}],"root_ar":"ث ق ل","root_id":"root_000202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tartı aracı, ağırlık birimi ve ölçülen miktar çekirdeğini birlikte karşılar.","boundary_detail":"Dal tartı ve ölçü ağırlığıdır; genel ağırlık veya değer yüceliği değildir.","branch_image_ar":"المثقال والوزن","concept_gloss":"ölçü ağırlığı","contextual_glosses":[{"applicability":"Bir şeyin denk ağırlık miktarının anlatıldığı bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Denk tartı miktarı fikrini korur."},"facet_ids":["F002"],"text":"ağırlığı kadar","usage_role":"contextual"},{"applicability":"Tartıda kullanılan ağırlık veya ölçü birimi bağlamında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölçme ve tartı aracını korur."},"facet_ids":["F001"],"text":"tartı ağırlığı","usage_role":"general"}],"definition":"Bilinen ağırlık ölçüsü, tartıda kullanılan ağırlık veya bir şeyin ölçülen ağırlık miktarıdır; ayrıca bir şeye ağırlığını vermek ya da tartarak ağır-hafif durumunu belirlemek bu alana girer.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel alan, bilinen ağırlık ölçüsü veya tartıda kullanılan ağırlıktır."},{"facet_id":"F002","role":"specialization","statement":"Bir şeyin kendi ağırlık miktarı veya ona denk tartı karşılığı ifade edilebilir."},{"facet_id":"F003","role":"associated_use","statement":"Ağırlığını vermek veya bir hayvanı tartmak, ölçme alanının eylem kullanımlarıdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Saygınlık veya kıymet alanı ekler.","collision":"Ayrı değer ağırlığı dalıyla çakışır.","fit":"displacement","loses":"Ölçü, tartı ve nicelik belirleme çekirdeğini kaybeder.","preserves":"Ağırlığın önemle ilişkilendirilebilmesini kısmen korur."},"text":"değer"}],"identity_rationale":"Kaynak ifadesi belirli ağırlık ölçüsü, tartı aracı, bir şeyin ağırlık miktarı ve ağırlığını verme işlemini birlikte sunar. Çerçeve bu teknik ölçme alanını yük, günah ve değer ağırlığından ayırdığı için uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bilinen ağırlık ölçüsü veya tartı ağırlığı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bir şeyin ağırlığı kadar ölçü"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ona ağırlığını ver"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"hayvanı tartıp ağırlığını yokladı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ağırlığı eksik olmayan dinar"}],"lexicalization_note":"Mixed_non_bare kapsam, ölçü adını ve ölçme birleşimlerini aynı tartı sınırı içinde fakat ayrı işlevlerle açıklar.","neighbor_coverage_note":"Tartı, ölçü, eksiltme ve belirli ölçü adayları değerlendirildi; sayı artışı veya küçük mıkdara ilişkin uzak adaylar dal sınırını yeterince açıklamadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ağırlık birimi veya miktar üzerinde durur; komşu dal tartı aleti ve bunun adaletle ilişkili geniş kullanımını taşır.","focus_only":"Odak dal belirli ağırlık ölçüsü ve tartı miktarıdır.","gloss":"ölçü ağırlığı ile terazi","neighbor_only":"Komşu dal tartı aracını adalet, denge ve hesap sahasına da genişletir.","neighbor_ref":"root_001645/B002","relation_type":"near_synonym","shared_zone":"Her ikisi de tartı ve ölçme alanında kullanılabilir."},{"boundary_match":"field_only","distinction":"Odak dal ölçü ağırlığı türünü ve işlem alanını kapsar; komşu dal belli bir ölçü adında daha dar kalır.","focus_only":"Odak dal genel tartı ağırlığı ve ölçülen miktardır.","gloss":"ölçü ağırlığı ile belirli ölçü","neighbor_only":"Komşu dal belirli bir bilinen ağırlık adıdır.","neighbor_ref":"root_001677/B004","relation_type":"same_field","shared_zone":"İki dal ağırlık ölçüleri alanına aittir."},{"boundary_match":"partial","distinction":"Odak dal nicel ölçü ve tartı düzenine bağlıdır; komşu dal böyle bir teknik ölçme kısıtı olmadan ağırlık niteliğini anlatır.","focus_only":"Odak dal ölçülmüş ya da ölçen ağırlıktır.","gloss":"ölçü ağırlığı ile ağırlık","neighbor_only":"Komşu dal genel ağır olma niteliğidir.","neighbor_ref":"root_000202/B001","relation_type":"near_neighbor","shared_zone":"Tartı ve ağır gelme ortak zemindir."}],"source_phrase_ar":"المثقال وزن معلوم قدره ومثقال الشيء ميزانه من مثله (ayn;tahdhib)؛ أعطه ثقله أي وزنه وثقلت الشاة (sihah;tahdhib)؛ المثقال ما يوزن به وهو اسم لكل سنج (mufradat)","source_summary":"Kaynaklar dalı ölçü, tartı aracı, ağırlık miktarı ve tartma işlemi çevresinde toplar; kullanım teknik ve nicelik belirleyicidir, yük veya soyut değer anlamını kendiliğinden taşımaz.","sources":["AY","SI","TA","MU"],"what_is_ar":"المثقال والميزان والوزن المعلوم، وإعطاء الشيء ثقله ووزنه","what_is_not_ar":"الأحمال والأمتعة؛ الأوزار؛ الثقل بمعنى النفاسة؛ الثقلة في البدن"},"support_links":["sup_fe06e8d5eeb0ca1a8266"]},{"boundary":"Dal kıymet ve itibar ağırlığıdır; taşınan yük ya da tartı birimi değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000202/B005","candidate_links":[{"candidate_id":"cand_8b80b4f6fe8e91407782","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ثَقُلَتْ","morph_features":"STEM|POS:V|PERF|LEM:vaqulato|ROOT:vql|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"101:6:3:1","qac_word_ref":"101:6:3","surface_ar":"ثَقُلَتْ"}],"gloss":"değer ağırlığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ağırlık, değerli ve korunmaya layık şeyin kıymetini anlatır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Saygın kişi veya övülen insan için ağırlık, itibar ve mevki bildirir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ağır söz, etkisi, doğruluğu, yararı veya yüce değeri sebebiyle önemli sözdür."}}],"root_ar":"ث ق ل","root_id":"root_000202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kıymet, saygınlık ve söze verilen büyük önem alanını tek ifadede toplar.","boundary_detail":"Dal kıymet ve itibar ağırlığıdır; taşınan yük ya da tartı birimi değildir.","branch_image_ar":"الثقل النفيس ذو القدر","concept_gloss":"değer ağırlığı","contextual_glosses":[{"applicability":"Korunmuş veya değerli nesne bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Saygın kişi ve ağır söz kullanımlarını dışarıda bırakır.","preserves":"Kıymet ve korunmuşluk alanını korur."},"facet_ids":["F001"],"text":"kıymetli şey","usage_role":"contextual"},{"applicability":"Sözün yüce değer, doğruluk, açıklık veya fayda sebebiyle önemli olduğu bağlamda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözün değer ve etki ağırlığını korur."},"facet_ids":["F003"],"text":"ağır söz","usage_role":"contextual"}],"definition":"Kıymetli, korunmuş, itibarlı veya etkisi büyük olan şeyin taşıdığı değer ağırlığıdır; seçkin kimse, önemli söz ve büyük sayılan ikili adlandırmalar bu alanda yer alır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ağırlık, değerli ve korunmaya layık şeyin kıymetini anlatır."},{"facet_id":"F002","role":"extension","statement":"Saygın kişi veya övülen insan için ağırlık, itibar ve mevki bildirir."},{"facet_id":"F003","role":"associated_use","statement":"Ağır söz, etkisi, doğruluğu, yararı veya yüce değeri sebebiyle önemli sözdür."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Teknik ölçme ve tartı alanı ekler.","collision":"Ayrı ölçü ağırlığı dalıyla çakışır.","fit":"displacement","loses":"Kıymet, itibar ve sözün değeri alanını kaybeder.","preserves":"Ağırlık sözcüğünün temel alanını korur."},"text":"tartı ağırlığı"}],"identity_rationale":"Kaynak ifadesi ağırlığı fiziksel yükten çıkarıp kıymet, korunmuşluk, saygınlık ve sözü ağır kılan değer alanına taşır. Çerçeve bu değer alanını yük, hastalık ve teknik ölçü anlamlarından ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kıymetli, korunmuş veya itibarlı şey"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"büyük önemleri sebebiyle birlikte anılan iki varlık ya da değerli iki emanet"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"büyük değeri ve etkisi olan söz"}],"lexicalization_note":"Mixed_non_bare kapsam, değer bildiren biçimleri ve belirli söz birleşimini aynı mecazi değer sınırında tutar.","neighbor_coverage_note":"Yücelik, mevki, kıymet ve değer adayları değerlendirildi; takip, mal biriktirme veya genel güzellik gibi adaylar daha uzak tematik ilişkide kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kıymeti ağır olma imgesiyle anlatır; komşu dal ağırlık imgesine bağlı olmadan yücelik ve büyüklük bildirir.","focus_only":"Odak dal değeri ağırlık imgesiyle kurar.","gloss":"değer ağırlığı ile yücelik","neighbor_only":"Komşu dal doğrudan yücelik, azamet ve gözde büyüklük bildirir.","neighbor_ref":"root_000227/B001","relation_type":"near_synonym","shared_zone":"İki dal yüksek değer ve saygınlık alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal daha geniş bir kıymet ve korunmuşluk alanı taşır; komşu dal kişinin ya da şeyin değer ve mevki ölçüsüne yoğunlaşır.","focus_only":"Odak dal kıymetli şey, saygın kişi ve ağır söz alanlarını kapsar.","gloss":"değer ağırlığı ile mevki","neighbor_only":"Komşu dal değer veya mevkiyi tartı ve ağırlık imgesinden hareketle belirtir.","neighbor_ref":"root_001645/B007","relation_type":"near_synonym","shared_zone":"İki dal değeri ağırlık veya tartı mecazıyla anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal ağırlığı kıymet ve önem olarak yorumlar; komşu dal bu özel değer yorumu olmadan ağırlık niteliğini verir.","focus_only":"Odak dal kıymet ve itibar ağırlığıdır.","gloss":"değer ağırlığı ile ağırlık","neighbor_only":"Komşu dal genel maddi ya da soyut ağırlık niteliğidir.","neighbor_ref":"root_000202/B001","relation_type":"near_neighbor","shared_zone":"Odak dal, genel ağırlık fikrinin soyut değer alanına taşınmasıyla kurulur."}],"source_phrase_ar":"سمي الجن والإنس الثقلين (maqayis;sihah;tahdhib)؛ كل شيء نفيس مصون ثقل ويقال للسيد العزيز ثقل (tahdhib)؛ قولا ثقيلا يعني عظم قدره وجلالة خطره وقول له وزن (tahdhib)؛ الثقيل في الإنسان يستعمل في المدح (mufradat)","source_summary":"Kaynaklar dalı kıymetli ve korunmuş şey, itibarlı kişi, ağır ve değerli söz, ayrıca büyüklükleri sebebiyle birlikte anılan varlıklar etrafında toplar; fiziksel ağırlık burada değer ve önem metaforuna dönüşür.","sources":["MQ","SI","TA","MU"],"what_is_ar":"كل شيء نفيس مصون أو علق خطير، والسيد العزيز، والقول ذو الوزن والقدر، وما سمي ثقلين لعظم شأنه","what_is_not_ar":"الثقل بمعنى المتاع؛ الأوزار؛ ثقل المرض والنوم؛ المثقال الحسابي"},"support_links":["sup_9c0d98a092022ae15631"]},{"boundary":"Dal yaşanan ağırlık, halsizlik ve yavaşlamadır; gebelik veya ahlaki yük değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000202/B006","candidate_links":[{"candidate_id":"cand_94b5ac463666a4e5efc8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ثَقُلَتْ","morph_features":"STEM|POS:V|PERF|LEM:vaqulato|ROOT:vql|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"101:6:3:1","qac_word_ref":"101:6:3","surface_ar":"ثَقُلَتْ"}],"gloss":"ağırlık ve halsizlik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bedende, nefiste veya yemekten sonra hissedilen ağırlık ve gevşeklik vardır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Uyku veya hastalık kişiyi baskılayıp ağırlaştırabilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yavaşlama, ayak sürüme ve yere doğru ağır davranma bu alana girer."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Sözün dinleyene hoş gelmemesi, kabulde ağır gelme olarak bağlı bir kullanımdır."}}],"root_ar":"ث ق ل","root_id":"root_000202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Beden, iç hal, uyku, hastalık ve yavaşlama alanlarını birlikte karşılar.","boundary_detail":"Dal yaşanan ağırlık, halsizlik ve yavaşlamadır; gebelik veya ahlaki yük değildir.","branch_image_ar":"الثقلة والبطء","concept_gloss":"ağırlık ve halsizlik","contextual_glosses":[{"applicability":"Bedende veya içte duyulan ağırlık ve gevşeklik bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uyku, hastalık, yavaşlama ve sözün ağır gelişi ayrıntılarını dışarıda bırakır.","preserves":"Bedensel ve içsel gevşeme halini korur."},"facet_ids":["F001"],"text":"halsizlik","usage_role":"contextual"},{"applicability":"Uykunun kişiyi ağırlaştırdığı kullanımda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Baskın uykunun ağırlaştırmasını korur."},"facet_ids":["F002"],"text":"uyku bastırdı","usage_role":"contextual"},{"applicability":"Yavaşlama ve ayak sürüme bağlamlarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tembelce yavaşlama ve davranışta ağırlaşmayı korur."},"facet_ids":["F003"],"text":"ağırdan aldı","usage_role":"contextual"}],"definition":"Kişinin bedeni, iç hali, uykusu, hastalığı, yediği şey veya davranışı sebebiyle ağırlaşması, gevşemesi ve yavaşlamasıdır; bazı kullanımlarda sözün kulağa hoş gelmemesi de bu ağır gelme alanına bağlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bedende, nefiste veya yemekten sonra hissedilen ağırlık ve gevşeklik vardır."},{"facet_id":"F002","role":"specialization","statement":"Uyku veya hastalık kişiyi baskılayıp ağırlaştırabilir."},{"facet_id":"F003","role":"extension","statement":"Yavaşlama, ayak sürüme ve yere doğru ağır davranma bu alana girer."},{"facet_id":"F004","role":"associated_use","statement":"Sözün dinleyene hoş gelmemesi, kabulde ağır gelme olarak bağlı bir kullanımdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Rahimde çocuk taşıma koşulu ekler.","collision":"Ayrı gebelikte ağırlaşma dalıyla çakışır.","fit":"displacement","loses":"Halsizlik, uyku, hastalık ve yavaşlama alanını kaybeder.","preserves":"Bedende ağırlaşma fikrini korur."},"text":"gebelik"}],"identity_rationale":"Kaynak ifadesi bedende, nefiste, yemekte, uykuda, hastalıkta ve davranışta ortaya çıkan ağırlık, gevşeme, baskılanma ve yavaşlamayı toplar. Çerçeve gebelik, günah yükü ve kıymet ağırlığıyla karışmadığı sürece doğrudur.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"içte, bedende veya yemekten sonra duyulan ağırlık ve gevşeklik"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"bastıran uyku hali"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"hastalık onu ağırlaştırdı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"uyku ona ağır bastı"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"ağırlaşmış, yavaş veya gücünü aşan yük altında kalmış"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"ağırdan alma, yavaşlama ve ayak sürüme"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"sözün kulağa hoş gelmemesi veya kabulünün ağır gelmesi"}],"lexicalization_note":"Mixed_non_bare kapsam, çıplak hal bildiren biçimleri ve hastalık, uyku, söz gibi birleşimsel kullanımları ayrı tutar.","neighbor_coverage_note":"Yavaşlık, uyku, hastalık ve yere ağırlaşma adayları değerlendirildi; bağırsak, titreme veya zayıflama gibi adaylar odak sınırı için daha dolaylı kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal daha geniş bir yaşanan ağırlık alanı taşır; komşu dal özellikle görevden geri duran tembellik yönünü belirginleştirir.","focus_only":"Odak dal bedensel, uykusal, hastalıklı veya davranışsal ağırlaşmayı kapsar.","gloss":"ağırlık ve halsizlik ile tembellik","neighbor_only":"Komşu dal yapılması gereken şeyden geri durma anlamındaki tembellik ve üşenmeye odaklanır.","neighbor_ref":"root_001299/B001","relation_type":"near_synonym","shared_zone":"İki dal yavaşlama ve isteksiz hareket alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal uykuyu daha geniş ağırlaşma alanının bir gerçekleşmesi yapar; komşu dal uyku çokluğu ve uyku baskısında daralır.","focus_only":"Odak dal uyku dışında hastalık, yemek, beden ve davranış ağırlaşmasını da kapsar.","gloss":"halsizlik ile çok uyuma","neighbor_only":"Komşu dal çok uyuma veya uyku basması alanında kalır.","neighbor_ref":"root_001568/B002","relation_type":"near_neighbor","shared_zone":"İki dal baskın uyku haliyle kesişir."},{"boundary_match":"partial","distinction":"Odak dal yorgunluk, hastalık, uyku ve yavaşlık kaynaklarını kapsar; komşu dal yalnızca gebelik yüküne bağlıdır.","focus_only":"Odak dal genel bedensel veya davranışsal ağırlaşmadır.","gloss":"halsizlik ile gebelikte ağırlaşma","neighbor_only":"Komşu dal kadının gebeliği sebebiyle ağırlaşmasıdır.","neighbor_ref":"root_000202/B007","relation_type":"near_neighbor","shared_zone":"Her ikisi de bedende ağırlık oluşmasını anlatır."}],"source_phrase_ar":"أجد في نفسي ثقلة (maqayis)؛ الثقلة نعسة غالبة وأثقله المرض واستثقله النوم والمثقل البطيء والتثاقل من التباطؤ (ayn)؛ وجدت ثقلة في جسدي أي ثقلا وفتورا (sihah)؛ الثقلة ما وجد الإنسان من ثقل الطعام وأصبح ثاقلاء أثقله المرض (tahdhib)؛ اثاقلتم إلى الأرض (mufradat)","source_summary":"Kaynaklar dalı içte veya bedende duyulan ağırlık, yemek sonrası ağırlık, baskın uyku, hastalığın ağırlaştırması, yavaş hareket ve ağır gelen söz çevresinde toplar; ortak nokta kişinin hafif ve çevik halden uzaklaşmasıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الثقلة في النفس أو الجسد أو الطعام، وغلبة النعاس، وإثقال المرض أو النوم، والبطء والتباطؤ والتحامل في الوطء","what_is_not_ar":"الحمل في البطن؛ الأوزار الشرعية؛ المثقال؛ النفاسة والقدر"},"support_links":["sup_b6a80f33aa1aa71eea1b"]},{"boundary":"Dal yalnızca gebelik yüküyle ağırlaşmadır; genel halsizlik ya da beden biçimi değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000202/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ثَقُلَتْ","morph_features":"STEM|POS:V|PERF|LEM:vaqulato|ROOT:vql|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"101:6:3:1","qac_word_ref":"101:6:3","surface_ar":"ثَقُلَتْ"}],"gloss":"gebelikte ağırlaşma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadın, karnındaki gebelik yükü sebebiyle ağırlaşır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu hal, gebeliği ağırlaşmış kadın için bir niteleme oluşturur."}}],"root_ar":"ث ق ل","root_id":"root_000202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kadının hamilelik yüküyle ağırlaşması çekirdeğini açıkça verir.","boundary_detail":"Dal yalnızca gebelik yüküyle ağırlaşmadır; genel halsizlik ya da beden biçimi değildir.","branch_image_ar":"إثقال الحمل","concept_gloss":"gebelikte ağırlaşma","contextual_glosses":[{"applicability":"Kadının gebelik yükünün belirginleştiği fiil bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gebeliğe bağlı ağırlaşma olayını korur."},"facet_ids":["F001"],"text":"hamileliği ağırlaştı","usage_role":"contextual"},{"applicability":"Gebeliği ilerlemiş ve yükü ağırlaşmış kadını niteleyen kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gebeliğin kişiyi ağırlaştıran niteliğini korur."},"facet_ids":["F002"],"text":"ağır hamile kadın","usage_role":"contextual"}],"definition":"Kadının karnındaki gebelik yükü sebebiyle ağırlaşması ve bu yükle ağırlaşmış kadın olarak nitelenmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadın, karnındaki gebelik yükü sebebiyle ağırlaşır."},{"facet_id":"F002","role":"specialization","statement":"Bu hal, gebeliği ağırlaşmış kadın için bir niteleme oluşturur."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Gebelik dışı hastalık, uyku veya yorgunluk sebeplerini ekler.","collision":"Ayrı halsizlik ve yavaşlama dalıyla çakışır.","fit":"broadening","loses":null,"preserves":"Bedensel ağırlaşma hissini kısmen korur."},"text":"halsizlik"}],"identity_rationale":"Kaynak ifadesi kadının karnındaki hamilelik yükü sebebiyle ağırlaşmasına ve bu haldeki kadının nitelenmesine odaklanır. Çerçeve bunu genel hastalık ağırlığı veya iri beden betimlemesiyle karıştırmaz.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"kadının gebelik yüküyle ağırlaşması"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"gebeliği ağırlaşmış kadın"}],"lexicalization_note":"Mixed_non_bare kapsam, gebelik birleşimini ve bu haldeki kişi niteliğini aynı koşula bağlı tutar.","neighbor_coverage_note":"Gebelik, doğum, rahimde yerleşme ve kadın bedeni adayları değerlendirildi; boyun ağrısı veya benzer uzak bedensel adaylar sınırı güçlendirmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal gebeliğin oluşturduğu ağırlık sonucuna odaklanır; komşu dal gebelik durumunun kendisini ve süresini anlatır.","focus_only":"Odak dal gebelik yükünün kadını ağırlaştırmasıdır.","gloss":"gebelikte ağırlaşma ile gebelik","neighbor_only":"Komşu dal gebeliğin kendisi, karındaki çocuk ve gebelik süresi alanıdır.","neighbor_ref":"root_000291/B006","relation_type":"near_synonym","shared_zone":"İki dal kadının karnındaki gebelik alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal ağırlığın artışını söyler; komşu dal zayıflama ve yıpranma sonucunu öne çıkarır.","focus_only":"Odak dal gebelik yüküyle ağırlaşmadır.","gloss":"ağır hamilelik ile gebelik zayıflığı","neighbor_only":"Komşu dal gebeliğin kadını zayıflatması veya yıpratmasıdır.","neighbor_ref":"root_000341/B007","relation_type":"near_neighbor","shared_zone":"İki dal hamileliğin bedende oluşturduğu etkiyi paylaşır."},{"boundary_match":"field_only","distinction":"Odak dal gebelik koşuluna bağlıdır; komşu dal gebelikten bağımsız beden biçimi veya vakar betimlemesidir.","focus_only":"Odak dal hamilelik yükünden doğan ağırlaşmadır.","gloss":"hamile ağırlığı ile kadın betimi","neighbor_only":"Komşu dal kadının beden biçimi veya oturuşta ağırbaşlılığıdır.","neighbor_ref":"root_000202/B008","relation_type":"same_field","shared_zone":"İki dal kadın bedeni veya kadın niteliği alanında buluşur."}],"source_phrase_ar":"اثقلت المرأة فيه مثقل (ayn)؛ أثقلت المرأة فهي مثقل أي ثقل حملها في بطنها (sihah)؛ المثقل من النساء التي قد ثقلت من حملها (tahdhib)","source_summary":"Kaynaklar dalı kadının hamileliği nedeniyle karnında ağırlık taşıması ve bu sebeple ağırlaşmış kadın diye nitelenmesi olarak verir; anlamın belirleyici koşulu gebeliktir.","sources":["AY","SI","TA"],"what_is_ar":"إثقال المرأة بحملها في بطنها، والمثقل من النساء بسبب الحمل","what_is_not_ar":"الأوزار والخطايا؛ الأمتعة؛ ثقل المرض؛ امرأة ثقال ذات كفل"},"support_links":[]},{"boundary":"Dal belirli kadın betimidir; hamilelik veya işitme ağırlığı değildir.","branch_kind":"collocation","branch_ref":"root_000202/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ثَقُلَتْ","morph_features":"STEM|POS:V|PERF|LEM:vaqulato|ROOT:vql|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"101:6:3:1","qac_word_ref":"101:6:3","surface_ar":"ثَقُلَتْ"}],"gloss":"dolgun kalçalı ağırbaşlı kadın","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kadın, kalça ve oturak dolgunluğu sebebiyle böyle nitelenir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı niteleme mecliste ağırbaşlı ve vakur duruşa yakın açıklanabilir."}}],"root_ar":"ث ق ل","root_id":"root_000202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem beden betimini hem de bağlı vakar açıklamasını doğal Türkçeyle verir.","boundary_detail":"Dal belirli kadın betimidir; hamilelik veya işitme ağırlığı değildir.","branch_image_ar":"امرأة ثقال","concept_gloss":"dolgun kalçalı ağırbaşlı kadın","contextual_glosses":[{"applicability":"Beden biçimi açıklamasının öne çıktığı bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadına özgü beden dolgunluğu betimini korur."},"facet_ids":["F001"],"text":"dolgun kalçalı kadın","usage_role":"contextual"},{"applicability":"Mecliste vakur duruşun öne çıktığı açıklama bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Beden dolgunluğu çekirdeğini dışarıda bırakır.","preserves":"Vakur duruş uzantısını korur."},"facet_ids":["F002"],"text":"ağırbaşlı kadın","usage_role":"contextual"}],"definition":"Kadın için kullanılan, kalça ve oturak dolgunluğunu bildiren nitelemedir; bazı açıklamalarda mecliste ağırbaşlı ve vakur duruşa da yaklaşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kadın, kalça ve oturak dolgunluğu sebebiyle böyle nitelenir."},{"facet_id":"F002","role":"extension","statement":"Aynı niteleme mecliste ağırbaşlı ve vakur duruşa yakın açıklanabilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Gebelik koşulu ekler.","collision":"Ayrı gebelikte ağırlaşma dalıyla çakışır.","fit":"displacement","loses":"Kalça dolgunluğu ve vakur duruş betimini kaybeder.","preserves":"Kadınla ilgili bedensel ağırlık fikrini kısmen korur."},"text":"hamile kadın"}],"identity_rationale":"Kaynak ifadesi belirli bir kadın betimini verir: kalça ve oturak dolgunluğu, ayrıca mecliste ağırbaşlı duruşa yakın bir kullanım. Çerçeve bunu gebelikle değil beden biçimi ve vakar niteliğiyle sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"dolgun kalçalı veya mecliste ağırbaşlı kadın"}],"lexicalization_note":"Collocation kapsam, tanımı yalnızca verilen kadın nitelemesine bağlar; çıplak ağırlık anlamına genelleştirilmez.","neighbor_coverage_note":"Kadın bedeni, dolgunluk, tavır ve kadın betimi adayları değerlendirildi; at bedeni veya genç kız betimi gibi adaylar odak nitelemeyle daha uzak kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli kadın betimine bağlıdır; komşu dal cinsiyete ve belirli beden bölgesine bağlı olmayan genel semizlik alanındadır.","focus_only":"Odak dal kadın için belirli kalça ve oturak dolgunluğu nitelemesidir.","gloss":"kadın dolgunluğu ile semizlik","neighbor_only":"Komşu dal genel şişmanlık, semizlik veya semirtme alanıdır.","neighbor_ref":"root_000744/B001","relation_type":"near_neighbor","shared_zone":"İki dal bedensel dolgunluk alanında örtüşür."},{"boundary_match":"field_only","distinction":"Odak dal ağırlık ve dolgunluk imgesine bağlıdır; komşu dal naz, tavır güzelliği ve duruş çekiciliğine odaklanır.","focus_only":"Odak dal dolgunluk ve ağırbaşlı kadın betimidir.","gloss":"ağırbaşlı kadın ile tavır güzelliği","neighbor_only":"Komşu dal görünüşte zarafet, tavır ve çekicilik alanını anlatır.","neighbor_ref":"root_000484/B003","relation_type":"same_field","shared_zone":"İki dal kadın tavrı ve görünüş betiminde buluşabilir."},{"boundary_match":"field_only","distinction":"Odak dal beden biçimi veya meclis vakarını anlatır; komşu dal yalnızca gebelik yükünden doğan ağırlaşmayı anlatır.","focus_only":"Odak dal gebelikten bağımsız kadın betimidir.","gloss":"kadın betimi ile hamilelik ağırlığı","neighbor_only":"Komşu dal hamilelik yüküyle ağırlaşmadır.","neighbor_ref":"root_000202/B007","relation_type":"same_field","shared_zone":"İki dal kadın bedeniyle ilgili nitelemelerdir."}],"source_phrase_ar":"امرأة ثقال أي ذات مآكم وكفل (ayn;sihah;tahdhib)؛ هذه امرأة ثقال وهذه امرأة رزان أي رزينة في مجلسها (tahdhib)","source_summary":"Kaynaklar bu dalı kadın için bedensel dolgunluk betimi olarak verir ve bir açıklamada oturuş ya da meclis vakarına yaklaştırır; belirleyici olan gebelik değil niteleme bağlamıdır.","sources":["AY","SI","TA"],"what_is_ar":"وصف المرأة بالثقال لذات المآكم والكفل، ويقارب الرزانة في المجلس","what_is_not_ar":"المرأة المثقل من الحمل؛ الثقل في السمع؛ المتاع؛ الأوزار"},"support_links":[]},{"boundary":"Dal işitme duyusundaki ağırlık ve kabul zayıflığıdır; genel ağırlık değildir.","branch_kind":"collocation","branch_ref":"root_000202/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ثَقُلَتْ","morph_features":"STEM|POS:V|PERF|LEM:vaqulato|ROOT:vql|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"101:6:3:1","qac_word_ref":"101:6:3","surface_ar":"ثَقُلَتْ"}],"gloss":"işitme ağırlığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kulak, kendisine gelen şeyi kabul etmekte zorlanır ve işitme zayıflar."}}],"root_ar":"ث ق ل","root_id":"root_000202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kulakta ağırlık ve işitme kabulünün zayıflaması çekirdeğini açıkça karşılar.","boundary_detail":"Dal işitme duyusundaki ağırlık ve kabul zayıflığıdır; genel ağırlık değildir.","branch_image_ar":"ثقل السمع","concept_gloss":"işitme ağırlığı","contextual_glosses":[{"applicability":"Kişinin işitmesinin zayıf olduğu doğal Türkçe bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kulakta ağırlık ve işitme zayıflığını korur."},"facet_ids":["F001"],"text":"kulağı ağır işitir","usage_role":"contextual"},{"applicability":"Ağırlık imgesi yerine sonucu açıklamak gereken bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kulağın geleni kabul etmekte ağırlaşması imgesini açıkça vermez.","preserves":"İşitmenin zayıflaması sonucunu korur."},"facet_ids":["F001"],"text":"işitmesi zayıf","usage_role":"contextual"}],"definition":"Kulakta veya işitmede ağırlık, yani kulağın kendisine yöneltilen sesi veya sözü almakta zorlanması ve işitmenin zayıflamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kulak, kendisine gelen şeyi kabul etmekte zorlanır ve işitme zayıflar."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Sözün hoş karşılanmaması anlamı ekler.","collision":"Sözün ağır gelmesi, halsizlik ve ağır gelme dalındaki bağlı kullanımla çakışır.","fit":"displacement","loses":"Kulak ve işitme zayıflığı koşulunu kaybeder.","preserves":"Kabulde zorlanma fikrini kısmen korur."},"text":"söz ağır geldi"}],"identity_rationale":"Kaynak ifadesi kulakta ağırlığı, kulağın kendisine yöneltileni kabul etmekte zorlanması veya işitmenin zayıflaması olarak tanımlar. Çerçeve bunu sözün hoş gelmemesi, genel beden ağırlığı veya ölçü alanıyla karıştırmaz.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"kulağında ağırlık var, işitmesi zayıf"}],"lexicalization_note":"Collocation kapsam, anlamı kulakta ağırlık birleşimine bağlar ve çıplak ağırlık anlamına genelleştirmez.","neighbor_coverage_note":"İşitme, dinleme, sağırlaşma ve kulak verme adayları değerlendirildi; konuşma bozukluğu veya cevap verememe adayları farklı duyusal veya ifade alanlarında kaldı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Odak dal ve komşu dal aynı işitme ağırlığı sınırında kullanılabilir; komşu kartta kapanma vurgusu olsa da dal çekirdeği odak kullanımla örtüşür.","focus_only":null,"gloss":"işitme ağırlığı","neighbor_only":null,"neighbor_ref":"root_001674/B001","relation_type":"synonym","shared_zone":"İki dal kulakta ağırlık ve işitmenin kapanması ya da zorlaşması alanını paylaşır."},{"boundary_match":"partial","distinction":"Odak dal zayıflama veya ağırlık düzeyinde kalabilir; komşu dal tam sağırlığa ve mecazi dinlememe tavrına kadar genişler.","focus_only":"Odak dal işitmenin ağırlaşması ve geleni almakta zorlanmasıdır.","gloss":"ağır işitme ile sağırlık","neighbor_only":"Komşu dal işitmenin gitmesi, sağırlık ve bazen dinlememe tavrıdır.","neighbor_ref":"root_000884/B001","relation_type":"near_synonym","shared_zone":"İki dal işitme eksikliğinde örtüşür."},{"boundary_match":"opposed","distinction":"Odak dal alımın zayıflığını belirtir; komşu dal alıma yönelme ve dikkatli dinleme yönündedir.","focus_only":"Odak dal kulağın kabulde ağırlaşmasıdır.","gloss":"ağır işitme ile kulak verme","neighbor_only":"Komşu dal kulağı bir söze yöneltip dikkatle dinlemedir.","neighbor_ref":"root_000574/B004","relation_type":"polarity_pair","shared_zone":"İki dal kulağın söze yönelmesi ve sesi alma sahasını paylaşır."}],"source_phrase_ar":"في أذنه ثقل إذا لم يجد سمعه كأنه يثقل عن قبول ما يلقى إليه (mufradat)","source_summary":"Kaynak dalı tek bir işitme bağlamında verir: kulakta ağırlık vardır ve bu ağırlık, işitmenin kendisine geleni kolayca alamaması şeklinde anlaşılır.","sources":["MU"],"what_is_ar":"الثقل في الأذن، أي ضعف قبول السمع لما يلقى إليه","what_is_not_ar":"ثقل القول لسوء سماعه؛ ثقل الجسم؛ الأوزار؛ المثقال"},"support_links":[]},{"boundary":"Dal, ölçme ve ölçüyü belirleme eylemiyle sınırlıdır; adalet, hizalanma ve toplumsal değer ancak başka dallarda ele alınır.","branch_kind":"mixed_non_bare","branch_ref":"root_001645/B001","candidate_links":[{"candidate_id":"cand_b1b6f168af58ffd42c5d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مِيزَان","morph_features":"STEM|POS:N|LEM:miyzaAn|ROOT:wzn|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:6:4:1","qac_word_ref":"101:6:4","surface_ar":"مَوَٰزِينُ"}],"gloss":"tartarak veya yaklaşık ölçüp biçerek niceliği belirleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin ağırlığı veya niceliği, tartı ya da denk bir ölçü aracılığıyla belirlenir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ağaçtaki hurma ürününün miktarı, doğrudan tartılmadan yaklaşık olarak kestirilebilir."}}],"root_ar":"و ز ن","root_id":"root_001645","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem doğrudan tartmayı hem de ürün miktarını yaklaşık kestirme gibi ölçü belirleme uygulamalarını birlikte karşılar.","boundary_detail":"Dal, ölçme ve ölçüyü belirleme eylemiyle sınırlıdır; adalet, hizalanma ve toplumsal değer ancak başka dallarda ele alınır.","branch_image_ar":"تقدير الشيء بوزن أو خرْص","concept_gloss":"tartarak veya yaklaşık ölçüp biçerek niceliği belirleme","contextual_glosses":[{"applicability":"Bir nesnenin ağırlığının tartı veya denk bir ölçü kullanılarak belirlendiği somut bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Doğrudan tartmadan yapılan yaklaşık ürün kestirimini kapsamaz.","preserves":"Doğrudan ağırlık ölçme işlemini doğal ve kısa biçimde korur."},"facet_ids":["F001"],"text":"tartmak","usage_role":"general"},{"applicability":"Ağaçtaki meyvenin miktarının doğrudan tartı yapılmadan yaklaşık olarak belirlendiği bağlamlara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel tartma ve kesin ağırlık belirleme kapsamını dışarıda bırakır.","preserves":"Yaklaşık kestirim işlemini ve ürün bağlamını açıkça korur."},"facet_ids":["F002"],"text":"ürün miktarını göz kararı kestirmek","usage_role":"contextual"}],"definition":"Bir şeyin ağırlığını veya niceliğini, onu tartarak, denk bir ölçüyle karşılaştırarak ya da uygun bağlamda yaklaşık kestirerek belirlemektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin ağırlığı veya niceliği, tartı ya da denk bir ölçü aracılığıyla belirlenir."},{"facet_id":"F002","role":"specialization","statement":"Ağaçtaki hurma ürününün miktarı, doğrudan tartılmadan yaklaşık olarak kestirilebilir."}],"identity_rationale":"Kaynak anlatımı, bir şeyin ağırlığını ya da ölçüsünü tartarak, eş bir ölçüyle karşılaştırarak veya yaklaşık kestirerek belirleme çekirdeğini açıkça destekler. Hurma ürünü için yapılan yaklaşık kestirim bu çekirdeğin özel bir uygulamasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi tartmak veya ölçüsünü belirlemek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"hurma ürününün miktarını yaklaşık kestirmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir şeyin ağırlık ölçüsü"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir dirhem ağırlığında gelmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bir kimse için veya ona karşı bir şeyi tartmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kendisi için tartılanı teslim almak"}],"lexicalization_note":"Tanım, genel tartma eylemiyle birlikte yalnız belirli kalıplarda görülen ürün kestirimi ve alışveriş kullanımlarını ayırır; bu kalıplar çıplak anlama genellenmez.","neighbor_coverage_note":"Bütün adaylar ölçme, ağırlık, satış ve kökün öteki dalları bakımından karşılaştırıldı; yalnız çekirdek sınırını en açık gösteren iki karşıtlık yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda tartı veya denk ölçü temel yöntem olabilir ve yaklaşık kestirim yalnız özel bir uygulamadır; komşuda ise varsayıma dayalı kestirim kendi başına çekirdektir.","focus_only":"Bu dal, tartıyla kesin ağırlık belirlemeyi ve alışverişteki tartma rollerini de kapsar.","gloss":"tartma ile yaklaşık kestirim","neighbor_only":"Komşu dal, sayı, hacim ve meyve miktarını eksik bilgiyle sezgisel olarak kestirmeye özellikle açıktır.","neighbor_ref":"root_000403/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da önceden bilinmeyen bir niceliği belirleme alanında buluşur."},{"boundary_match":"field_only","distinction":"Buradaki çekirdek bir niceliği belirleme eylemidir; komşunun çekirdeği ise ölçülen şeyin ağır olma niteliğidir.","focus_only":"Bu dal, ağırlığı belirleyen ölçme işlemini ve bu işlemin yaklaşık kestirim uzantısını anlatır.","gloss":"ölçme işlemi ve ağırlık niteliği","neighbor_only":"Komşu dal, bir cismin ya da soyut bir şeyin ağır olma niteliğini ve hafifliğe karşı üstün gelmesini anlatır.","neighbor_ref":"root_000202/B001","relation_type":"same_field","shared_zone":"İki dal da ağırlık ve ölçü alanında yer alır."}],"source_phrase_ar":"وزنت الشيء وزنا؛ الزنة قدر وزن الشيء (maqayis)؛ الوزن ثقل شيء بشيء مثله؛ وزن الشيء إذا قدره؛ وزن ثمر النخل إذا خرصه (ayn;tahdhib)؛ وزنت الشئ وزنا وزنة؛ هذا يزن درهما (sihah)؛ الوزن معرفة قدر الشيء؛ ما يقدر بالقسط والقبان (mufradat)","source_summary":"Ortak anlatım, ağırlığı bilinen bir ölçüye göre belirleme ile daha genel nicelik belirlemeyi aynı çekirdekte toplar; ürün kestirimi bunun bağlama bağlı bir uygulamasıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه وزن الشيء بالميزان، قدر وزن الشيء، ثقل الشيء بشيء مثله، وخرص ثمر النخل أو الحزر بوصفه تقديرا.","what_is_not_ar":"لا يدخل فيه مجرد العدل أو المحاذاة أو منزلة الشخص إلا من جهة استعارة الوزن لها."},"support_links":["sup_fe06e8d5eeb0ca1a8266"]},{"boundary":"Somut tartı aracı çekirdekte, adil değerlendirme ise soyut uzantıdadır; yaklaşık ürün kestirimi ve salt hizalanma bu dala girmez.","branch_kind":"bare","branch_ref":"root_001645/B002","candidate_links":[{"candidate_id":"cand_b1b6f168af58ffd42c5d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مِيزَان","morph_features":"STEM|POS:N|LEM:miyzaAn|ROOT:wzn|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:6:4:1","qac_word_ref":"101:6:4","surface_ar":"مَوَٰزِينُ"}],"gloss":"tartı aracı ve adil değerlendirme ölçütü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesnelerin ağırlığını belirlemeye yarayan tartı aracı ve onun ölçü birimleri söz konusudur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tartı düşüncesi, insanların yaptıklarını ve haklarını adil ve denk biçimde değerlendirmeye aktarılır."}}],"root_ar":"و ز ن","root_id":"root_001645","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Somut ağırlık ölçme aracını ve ondan gelişen adil, denk değerlendirme kullanımını birlikte temsil eder.","boundary_detail":"Somut tartı aracı çekirdekte, adil değerlendirme ise soyut uzantıdadır; yaklaşık ürün kestirimi ve salt hizalanma bu dala girmez.","branch_image_ar":"ميزان العدل والقسط","concept_gloss":"tartı aracı ve adil değerlendirme ölçütü","contextual_glosses":[{"applicability":"Nesnelerin ağırlığını ölçmeye yarayan somut aracın kastedildiği bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Adil değerlendirme ve hesap görme uzantısını karşılamaz.","preserves":"Tartı aracını ve onun ağırlık ölçme işlevini eksiksiz korur."},"facet_ids":["F001"],"text":"terazi","usage_role":"general"},{"applicability":"İnsanların eylem ve haklarının doğru ve denk biçimde değerlendirildiği soyut bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Somut tartı aracını ve fiziksel ağırlık ölçümünü dışarıda bırakır.","preserves":"Adil değerlendirme ve doğru denge düşüncesini korur."},"facet_ids":["F002"],"text":"adalet ölçüsü","usage_role":"contextual"}],"definition":"Nesnelerin ağırlığını belirlemeye yarayan tartı aracıdır; soyut kullanımda ise eylem ve hakların doğru, denk ve adil biçimde değerlendirilmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesnelerin ağırlığını belirlemeye yarayan tartı aracı ve onun ölçü birimleri söz konusudur."},{"facet_id":"F002","role":"extension","statement":"Tartı düşüncesi, insanların yaptıklarını ve haklarını adil ve denk biçimde değerlendirmeye aktarılır."}],"identity_rationale":"Kaynak anlatımı hem nesneleri tartmaya yarayan aracı hem de doğru ve denk değerlendirme düşüncesini açıkça verir. İnsanların yaptıklarının adil biçimde değerlendirilmesi, ölçme aracından gelişen soyut bir uzantıdır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"terazi"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"teraziler ve tartı ağırlıkları"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"hesapta adil ve denk değerlendirme"}],"lexicalization_note":"Tanım, yalın biçimlerde tanıklanan tartı aracı ile adil ölçüt anlamını kapsar ve yalnız başka kalıplara ait okumaları içeri almaz.","neighbor_coverage_note":"Tüm adaylar araç, adalet, eksik ölçme ve kökün öteki dalları yönünden değerlendirildi; araç sınırı ile adalet uzantısını en iyi açıklayan üç ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Somut araç alanında büyük ölçüde örtüşürler; ancak bu dal adalet uzantısına açılırken komşu dal belirli araç adlarıyla sınırlanır.","focus_only":"Bu dal, tartı aracına ek olarak adil değerlendirme ve hesap görme uzantısını da içerir.","gloss":"tartı aracı","neighbor_only":"Komşu dal, tartı aracının belirli adlarını ve özel bir tartı türünü kendi söz varlığı içinde toplar.","neighbor_ref":"root_001225/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın somut çekirdeğinde ağırlık ölçmeye yarayan araç bulunur."},{"boundary_match":"thematic_only","distinction":"Burada araç ve adil ölçüt söz konusudur; komşuda ise bu ölçütün çiğnenmesi olan eksik ölçme eylemi vardır.","focus_only":"Bu dal, ölçme aracını ve ölçümün adil olmasını olumlu bir ölçüt olarak anlatır.","gloss":"adil tartı ve eksik tartma","neighbor_only":"Komşu dal, ölçüyü eksik verme ve karşı tarafın payını azaltma eylemini anlatır.","neighbor_ref":"root_000940/B003","relation_type":"thematic","shared_zone":"İki dal, alışverişte ölçü ve hakkaniyet senaryosunda buluşur."},{"boundary_match":"partial","distinction":"Bu dalın somut odağı araçtır; komşu dalın odağı o araçla ya da başka bir ölçüyle yapılan belirleme işlemidir.","focus_only":"Bu dal, tartı aracını adlandırır ve adil değerlendirme anlamına uzanır.","gloss":"terazi ve tartma","neighbor_only":"Komşu dal, aracın kendisinden çok bir şeyin ağırlığını veya niceliğini belirleme eylemini anlatır.","neighbor_ref":"root_001645/B001","relation_type":"near_neighbor","shared_zone":"İki dal, ağırlık ölçme olayının araç ve işlem yönlerini paylaşır."}],"source_phrase_ar":"بناء يدل على تعديل واستقامة (maqayis)؛ الميزان ما وزنت به (ayn)؛ الميزان معروف (sihah)؛ الموازين واحدها ميزان وهو المثاقيل؛ الآلة التي يوزن بها الأشياء ميزان؛ الميزان العدل (tahdhib)؛ مراعاة المعدلة؛ الوزن يومئذ الحق فإشارة إلى العدل في محاسبة الناس (mufradat)","source_summary":"Ortak anlatım, somut tartı aracını temel alır ve doğru denge ile adil değerlendirmenin bu araçtan gelişen soyut kullanımını da doğrular.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الميزان آلة الوزن، والموازين والمثاقيل، واستعمال الوزن والميزان في القسط والعدل ومحاسبة الأعمال.","what_is_not_ar":"لا يدخل فيه خرص الثمر المحض ولا محاذاة الشيئين ولا قام ميزان النهار إلا بقرينة العدل أو الآلة."},"support_links":["sup_fe06e8d5eeb0ca1a8266"]},{"boundary":"Dal, denklik veya karşılıklı hizalanma gerektirir; salt tartma işlemi ve genel adalet düşüncesi bu koşul olmadan kapsama girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001645/B003","candidate_links":[{"candidate_id":"cand_02ad7ad02cb221fb7d5a","lane":"micro"},{"candidate_id":"cand_94b5ac463666a4e5efc8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مِيزَان","morph_features":"STEM|POS:N|LEM:miyzaAn|ROOT:wzn|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:6:4:1","qac_word_ref":"101:6:4","surface_ar":"مَوَٰزِينُ"}],"gloss":"iki şeyi denk veya karşılıklı konumda tutma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki şey ölçü bakımından karşılaştırılır ve denk ya da karşılıklı konumda görülür."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yer bildiren kullanımda bir dağın yanı, karşısı veya onunla aynı hiza anlatılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Zihinsel değerlendirmede bir şey başka bir şeye denk sayılır."}}],"root_ar":"و ز ن","root_id":"root_001645","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ölçüsel denklik, karşılıklı hizalanma, yer bildirme ve zihinde denk sayma kullanımlarının ortak çekirdeğini karşılar.","boundary_detail":"Dal, denklik veya karşılıklı hizalanma gerektirir; salt tartma işlemi ve genel adalet düşüncesi bu koşul olmadan kapsama girmez.","branch_image_ar":"موازنة ومحاذاة بين شيئين","concept_gloss":"iki şeyi denk veya karşılıklı konumda tutma","contextual_glosses":[{"applicability":"İki şeyin ölçü veya değer bakımından karşılaştırılıp denk tutulduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Salt yer ve hiza bildiren özel kullanımı doğrudan karşılamaz.","preserves":"İki şeyi karşılaştırma ve ölçü bakımından denk tutma çekirdeğini korur."},"facet_ids":["F001","F003"],"text":"birbirine denklemek","usage_role":"general"},{"applicability":"Bir yerin, özellikle bir dağın yanı, karşısı veya aynı hizası belirtildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ölçüsel karşılaştırma ve zihinsel denklik okumalarını dışarıda bırakır.","preserves":"Karşılıklı konum ve yer bildirme uzantısını doğal biçimde korur."},"facet_ids":["F002"],"text":"hizasında veya yanında olmak","usage_role":"contextual"}],"definition":"İki şeyi ölçü, değer veya konum bakımından birbirine denk ve karşılıklı duruma getirmek ya da öyle görmek; özel yer kullanımında bir şeyin yanını veya hizasını belirtmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki şey ölçü bakımından karşılaştırılır ve denk ya da karşılıklı konumda görülür."},{"facet_id":"F002","role":"extension","statement":"Yer bildiren kullanımda bir dağın yanı, karşısı veya onunla aynı hiza anlatılır."},{"facet_id":"F003","role":"extension","statement":"Zihinsel değerlendirmede bir şey başka bir şeye denk sayılır."}],"identity_rationale":"Kaynak anlatımı, iki şeyi denk ölçüde veya karşılıklı konumda buluşturmayı açıkça destekler. Dağın yanı ya da hizası ve zihinde bir şeyi başkasına denk sayma kullanımları aynı karşılaştırma ve hizalama çekirdeğinin uzantılarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"iki şeyi karşılaştırıp birbirine denklemek"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"bu, ötekiyle aynı ölçüde veya onun hizasındadır"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"dağın yanı veya hizası"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"bu, ötekiyle zihinde denk tutulur"}],"lexicalization_note":"Tanım, karşılaştırma kalıpları ile yer bildiren özel kullanımı ayrı tutar; dağla kurulan yer kalıbı genel bir çıplak kök anlamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar denklik, benzerlik, karşılaştırma, yön ve kökün diğer dalları bakımından sınandı; en yakın iki karışma alanı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda ölçü karşılaştırması ya da karşılıklı hiza belirgindir; komşu dal daha genel bir eşitlik ve benzerlik alanına sahiptir.","focus_only":"Bu dal, denkliğin yanında karşılıklı hizalanmayı ve dağın yanı gibi özel yer kullanımlarını da içerir.","gloss":"denklik ve eşitlik","neighbor_only":"Komşu dal, kişi ve şeyler arasındaki genel eşitlik ve benzerliği konum ilişkisi aramadan anlatabilir.","neighbor_ref":"root_000991/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da iki şey arasında eşitlik veya denklik kurar."},{"boundary_match":"partial","distinction":"Buradaki hiza, ölçü ve denklik düşüncesine bağlanabilir; komşudaki çekirdek ise doğrudan karşıda bulunma yönüdür.","focus_only":"Bu dal, fiziksel hizanın yanı sıra ölçüsel ve zihinsel denklik kurmayı da kapsar.","gloss":"hizalama ve karşı karşıya bulunma","neighbor_only":"Komşu dal, evlerin karşı karşıya bulunması gibi doğrudan yönelme ve yüz yüze konum ilişkisine odaklanır.","neighbor_ref":"root_001450/B010","relation_type":"near_synonym","shared_zone":"İki dal, nesnelerin birbirinin karşısında veya hizasında bulunması alanında örtüşür."}],"source_phrase_ar":"هذا يوازن ذلك أي هو محاذيه (maqayis)؛ وازنت بين الشيئين؛ هذا يوازن هذا إذا كان على زنته أو كان محاذيه؛ هو وزن الجبل أي ناحية منه؛ هو زنة الجبل أي حذاءه (sihah)؛ هذا في وزن هذا؛ قام في النفس مساويا لغيره (tahdhib)","source_summary":"Ortak anlatım, karşılaştırılan iki şeyin aynı ölçüde ya da birbirinin hizasında bulunmasını çekirdek kabul eder; yer ve zihinsel değerlendirme kullanımları bu ilişkiden gelişir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه وازنت بين الشيئين، هذا يوازن هذا، كونه على زنته أو محاذيه، وزنة الجبل أو وزن الجبل بمعنى حذاءه أو ناحيته، وما قام في النفس مساويا لغيره.","what_is_not_ar":"لا يدخل فيه وزن البيع بالميزان ولا العدل العام إلا إذا ظهر معنى المساواة أو المقابلة."},"support_links":["sup_478fcf78ed0e13dadaa5","sup_b6a80f33aa1aa71eea1b"]},{"boundary":"Anlam yalnız günün ortasına gelmeyi bildiren kalıba bağlıdır; tartı aracı, adalet ve başka zaman dönemleri kapsama girmez.","branch_kind":"collocation","branch_ref":"root_001645/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مِيزَان","morph_features":"STEM|POS:N|LEM:miyzaAn|ROOT:wzn|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:6:4:1","qac_word_ref":"101:6:4","surface_ar":"مَوَٰزِينُ"}],"gloss":"günün tam ortasına gelmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gün yarıya ulaşmış ve öğle ortası gelmiştir."}}],"root_ar":"و ز ن","root_id":"root_001645","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kalıplaşmış sözün günün yarıya ulaşmasını bildirdiği zaman bağlamını eksiksiz karşılar.","boundary_detail":"Anlam yalnız günün ortasına gelmeyi bildiren kalıba bağlıdır; tartı aracı, adalet ve başka zaman dönemleri kapsama girmez.","branch_image_ar":"قيام ميزان النهار في وسطه","concept_gloss":"günün tam ortasına gelmesi","contextual_glosses":[{"applicability":"Günün ilk yarısının bittiğini ve öğle ortasının geldiğini akıcı cümlede bildirmek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Günün yarıya ulaşması ve öğle ortasının gelmesi anlamını korur."},"facet_ids":["F001"],"text":"gün ortalandı","usage_role":"contextual"}],"definition":"Yalnız belirli bir zaman kalıbında, günün yarısının tamamlandığını ve öğle ortasına gelindiğini bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gün yarıya ulaşmış ve öğle ortası gelmiştir."}],"identity_rationale":"Kaynak anlatımı yalnız belirli zaman kalıbını ve bu kalıbın günün yarıya ulaşıp öğle ortasının gelmesi anlamını verir. Geçici dal çerçevesi bu dar, kalıplaşmış kullanımı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"gün ortalandı"}],"lexicalization_note":"Tanım yalnız günün ortasına erişildiğini bildiren kalıplaşmış zaman sözünü açıklar ve bunu yalın kökün genel anlamına dönüştürmez.","neighbor_coverage_note":"Bütün zaman adayları yükseklik, mevsim, ay, güneş hareketi ve öğle vakti yönünden karşılaştırıldı; doğrudan gün ortası sınırını açıklayan iki aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Zaman noktası aynıdır; ancak bu dal tek bir kalıpla sınırlıyken komşu dal aynı vakti başka sözler ve güneş belirtileriyle de anlatır.","focus_only":"Bu dal, yalnız tek bir kalıpla günün yarıya ulaşmasını bildirir.","gloss":"gün ortası","neighbor_only":"Komşu dal, güneşin tepe konumu ve gölgenin çok kısalması gibi öğle ortasının gözlenebilir belirtilerini de kapsar.","neighbor_ref":"root_001273/B017","relation_type":"near_synonym","shared_zone":"Her iki dal da günün yarıya ulaştığı öğle ortasını gösterir."},{"boundary_match":"partial","distinction":"Bu dal bir anlık orta noktayı bildirir; komşu dal ise daha geniş bir vakit dilimini ve o vakitle ilişkili olayları kapsar.","focus_only":"Bu dal, günün tam yarıya ulaşma sınırını bildiren tek bir kalıba bağlıdır.","gloss":"gün ortası ve öğle vakti","neighbor_only":"Komşu dal, daha geniş öğle vaktini, o vakte girmeyi, o sıradaki ibadeti ve düzenli uğrağı kapsar.","neighbor_ref":"root_000970/B004","relation_type":"near_neighbor","shared_zone":"İki dal da öğle çevresindeki zamanı belirtir."}],"source_phrase_ar":"قام ميزان النهار إذا انتصف النهار (maqayis;mufradat)؛ قام ميزان النهار أي انتصف (sihah)","source_summary":"Kaynakların ortak anlatımı, kalıplaşmış sözü günün tam ortasına erişme ve öğle vaktinin yarılanması anlamında açıklar.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه التعبير الزمني قام ميزان النهار إذا انتصف النهار.","what_is_not_ar":"لا يدخل فيه الميزان آلة الوزن ولا ميزان العدل إلا بقرينة مستقلة."},"support_links":[]},{"boundary":"Sağlam düşünce dalın çekirdeğidir; kendini bir işe hazırlama yalnız tanıklanan kalıba bağlı uzantıdır ve genel tartma anlamı değildir.","branch_kind":"collocation","branch_ref":"root_001645/B005","candidate_links":[{"candidate_id":"cand_8b80b4f6fe8e91407782","lane":"micro"},{"candidate_id":"cand_94b5ac463666a4e5efc8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مِيزَان","morph_features":"STEM|POS:N|LEM:miyzaAn|ROOT:wzn|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:6:4:1","qac_word_ref":"101:6:4","surface_ar":"مَوَٰزِينُ"}],"gloss":"sağlam yargı ve kararlı yöneliş","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Düşünce dengeli, sağlam, ağırbaşlı ve acelecilikten uzak biçimde kararlıdır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi belirli bir işe girişmek üzere kendisini hazırlar ve kararlılıkla ona yönelir."}}],"root_ar":"و ز ن","root_id":"root_001645","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Düşüncenin dengeli ve sağlam oluşunu çekirdek, kişinin kendisini işe hazırlamasını ise kalıba bağlı uzantı olarak birlikte gösterir.","boundary_detail":"Sağlam düşünce dalın çekirdeğidir; kendini bir işe hazırlama yalnız tanıklanan kalıba bağlı uzantıdır ve genel tartma anlamı değildir.","branch_image_ar":"رأي وزين ثابت راجح","concept_gloss":"sağlam yargı ve kararlı yöneliş","contextual_glosses":[{"applicability":"Bir kişinin görüşünün dengeli, güvenilir ve acelecilikten uzak olduğunu anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin kendisini belirli bir işe hazırlaması uzantısını dışarıda bırakır.","preserves":"Düşüncenin sağlam, dengeli ve ağırbaşlı oluşunu korur."},"facet_ids":["F001"],"text":"sağlam ve ağırbaşlı düşünceli","usage_role":"general"},{"applicability":"Kişinin belirli bir işe girişmeyi kabullenip kendisini ona kararlı biçimde yönelttiği kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Düşüncenin dengeli ve sağlam oluşunu niteleyen çekirdeği kapsamaz.","preserves":"Hazırlanma ve kararlı biçimde işe yönelme uzantısını korur."},"facet_ids":["F002"],"text":"kendini o işe hazırlamak","usage_role":"contextual"}],"definition":"Bir kimsenin düşüncesinin dengeli, sağlam, ağırbaşlı ve kararlı olmasıdır; ayrı bir kalıpta kişinin kendisini bir işe hazırlayıp ona kesin biçimde yöneltmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Düşünce dengeli, sağlam, ağırbaşlı ve acelecilikten uzak biçimde kararlıdır."},{"facet_id":"F002","role":"associated_use","statement":"Kişi belirli bir işe girişmek üzere kendisini hazırlar ve kararlılıkla ona yönelir."}],"identity_rationale":"Kaynak anlatımı, dengeli, sağlam ve kararlı düşünceyi açıkça destekler; ayrıca kişinin kendisini bir işe hazırlayıp ona bağlamasını ayrı bir kalıpta verir. Bu ikinci kullanım düşüncenin niteliği değil, kararlı yöneliş olduğundan bağımlı bir uzantı olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"sağlam ve ağırbaşlı düşünceli"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"yargısı güçlü ve aklı sağlam"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kendini o işe hazırlayıp kararlılıkla yönelmek"}],"lexicalization_note":"Tanım yalnız düşünceyi niteleyen ve kişinin kendisini bir işe hazırlamasını bildiren kalıplara bağlıdır; bunlardan yalın bir kök anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar akıl, ağırbaşlılık, sağlam görüş, düşünme süreci ve karşıt akıl kaybı yönünden değerlendirildi; çekirdeği en iyi sınırlayan üç aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Düşünce niteliğinde yakınlaşırlar; bu dal ayrıca ağırbaşlı kararlılık ve işe hazırlanma uzantısına sahiptir.","focus_only":"Bu dal, sağlam düşünce yanında kararlılığı ve kişinin kendisini bir işe hazırladığı özel kalıbı da kapsar.","gloss":"sağlam düşünce","neighbor_only":"Komşu dal, doğrudan iyi ve yerinde düşünceyi niteleyen daha dar bir söz varlığına dayanır.","neighbor_ref":"root_000599/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kimsenin düşüncesini sağlam ve iyi olarak niteler."},{"boundary_match":"partial","distinction":"Bu dalın odağı düşüncenin dengesi ve kararlılığıdır; komşu dal kişinin akıl gücüyle bağlantılı daha geniş karakter niteliklerini kapsar.","focus_only":"Bu dal, düşüncenin dengeli oluşunu ve belirli işe kararlı yönelişi anlatır.","gloss":"ağırbaşlılık ve güçlü akıl","neighbor_only":"Komşu dal, güçlü aklın yanında sakınganlık, sır tutma ve ileri görüşlü davranma niteliklerini de içerir.","neighbor_ref":"root_000332/B003","relation_type":"near_synonym","shared_zone":"İki dal, sağlam akıl ve ağırbaşlı yargı alanında örtüşür."},{"boundary_match":"partial","distinction":"Burada sonuç niteliğindeki sağlam ve kararlı yargı öndedir; komşuda ise o sonuca götüren düşünme süreci çekirdektir.","focus_only":"Bu dal, düşünmenin sonucunda ortaya çıkan sağlam yargıyı ve kararlı tutumu niteler.","gloss":"sağlam yargı ve düşünüp taşınma","neighbor_only":"Komşu dal, bir konu üzerinde düşünüp inceleme sürecini ve ölçüp biçmeyi anlatır.","neighbor_ref":"root_000615/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal, karar verme ve düşünce alanında yer alır."}],"source_phrase_ar":"وزين الرأى معتدله؛ راجح الوزن إذا نسبوه إلى رجاحة الرأي وشدة العقل (maqayis)؛ رجل وزين الرأي وقد وزن وزانة إذا كان متثبتا (ayn;tahdhib)؛ فلان وزين الرأي أي رزينه (sihah)؛ أوزن فلان نفسه على الأمر إذا وطن نفسه عليه (tahdhib)","source_summary":"Ortak anlatım, düşüncedeki dengeyi sağlam yargı, güçlü kavrayış ve kararlı tutumla açıklar; kendini bir işe hazırlama kullanımı ayrı bir kalıba bağlıdır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه وزين الرأي، رزين الرأي، المتثبت، رجاحة الرأي وشدة العقل، وتوطين النفس على الأمر.","what_is_not_ar":"لا يدخل فيه مجرد وزن الأجسام أو قصر الجارية أو القدر الاجتماعي إلا إذا صرح بسياق الرأي والعقل."},"support_links":["sup_9c0d98a092022ae15631","sup_b6a80f33aa1aa71eea1b"]},{"boundary":"Dal kadın veya kız için kısa boylulukla sınırlıdır; aklı başında olma yalnız ilgili kalıpta ek niteliktir.","branch_kind":"mixed_non_bare","branch_ref":"root_001645/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مِيزَان","morph_features":"STEM|POS:N|LEM:miyzaAn|ROOT:wzn|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:6:4:1","qac_word_ref":"101:6:4","surface_ar":"مَوَٰزِينُ"}],"gloss":"kısa boylu, kimi kullanımda aklı başında kadın","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kız veya kadın kısa boylu olarak nitelenir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli kadın nitelemesinde kısa boyluluğa aklı başında olma özelliği eşlik eder."}}],"root_ar":"و ز ن","root_id":"root_001645","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kadın veya kız için kısa boyluluk çekirdeğini ve yalnız dar bir kullanımda eklenen aklı başında olma niteliğini karşılar.","boundary_detail":"Dal kadın veya kız için kısa boylulukla sınırlıdır; aklı başında olma yalnız ilgili kalıpta ek niteliktir.","branch_image_ar":"قصر موزون في الجارية أو المرأة","concept_gloss":"kısa boylu, kimi kullanımda aklı başında kadın","contextual_glosses":[{"applicability":"Bir kızın bedensel olarak kısa boylu oluşunun anlatıldığı kullanımda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kadına özgü kullanımı ve koşullu aklı başında olma niteliğini kapsamaz.","preserves":"Kız olma sınırını ve kısa boyluluk niteliğini korur."},"facet_ids":["F001"],"text":"kısa boylu kız","usage_role":"contextual"},{"applicability":"Kaynakta iki niteliğin birlikte verildiği özel kadın nitelemesinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Akıl niteliği belirtilmeyen daha geniş kız ve kadın kullanımlarını dışarıda bırakır.","preserves":"Kısa boyluluk ile aklı başında olma niteliklerini birlikte korur."},"facet_ids":["F001","F002"],"text":"kısa boylu, aklı başında kadın","usage_role":"contextual"}],"definition":"Bir kızın veya kadının kısa boylu olduğunu anlatır; yalnız belirli kadın nitelemesinde kısa boyluluğa aklı başında olma özelliği de eklenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kız veya kadın kısa boylu olarak nitelenir."},{"facet_id":"F002","role":"specialization","statement":"Belirli kadın nitelemesinde kısa boyluluğa aklı başında olma özelliği eşlik eder."}],"identity_rationale":"Kaynak anlatımı kız veya kadın için kısa boyluluğu açıkça destekler. Akıllı olma niteliği yalnız kadınla kurulan belirli tanıklıkta bulunur; bütün kısa boy kullanımlarına taşınmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kısa boylu kız"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"kısa boylu, aklı başında kadın"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"kısa boylu kadın"}],"lexicalization_note":"Tanım, kız ve kadınla kurulan niteleme kalıpları ile kadın adı olan biçimi ayırır; bu cinsiyet ve kullanım sınırı çıplak anlama genellenmez.","neighbor_coverage_note":"Bütün adaylar kısa boy, beden yapısı, kadın ve kız adlandırması, uzunluk ve düzgün yapı yönünden karşılaştırıldı; en yakın iki kısa boy dalı seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kadın ve kız nitelemesine özgüdür; komşu dal daha genel beden küçüklüğüne ve başka canlılara uzanır.","focus_only":"Bu dal, kısa boyluluğu kız veya kadınla sınırlar ve bir kalıpta aklı başında olma niteliği ekler.","gloss":"kısa boyluluk","neighbor_only":"Komşu dal, cinsiyet sınırı olmadan kısa ya da küçük gövdeli olmayı ve kimi hayvanların zayıflığını anlatabilir.","neighbor_ref":"root_000286/B010","relation_type":"near_synonym","shared_zone":"Her iki dal da bedenin kısa veya küçük oluşunu anlatır."},{"boundary_match":"partial","distinction":"Burada toplu beden yapısı gerekli değildir ve kullanım kadınlarla sınırlıdır; komşuda kısa ve toplu yapı birlikte bulunur.","focus_only":"Bu dal, kadın veya kız için yalın kısa boyluluğu ve koşullu bir akıl niteliğini anlatır.","gloss":"kısa ve toplu beden","neighbor_only":"Komşu dal, kısa boyun yanında gövdenin toplu ve sıkı yapılı olmasını da kurucu özellik yapar.","neighbor_ref":"root_000080/B006","relation_type":"near_synonym","shared_zone":"İki dalın ortak alanı kısa boylu insan betimlemesidir."}],"source_phrase_ar":"جارية موزونة فيها قصر (ayn;tahdhib)؛ امرأة موزونة قصيرة عاقلة؛ الوزنة المرأة القصيرة (tahdhib)","source_summary":"Ortak tanıklık kız veya kadın için kısa boyluluğu verir; aklı başında olma kaydı yalnız daha dar bir kadın nitelemesine bağlıdır.","sources":["AY","TA"],"what_is_ar":"يدخل فيه جارية موزونة فيها قصر، وامرأة موزونة أو الوزنة بمعنى المرأة القصيرة، مع قيد العقل حيث ذكره المصدر.","what_is_not_ar":"لا يدخل فيه وزن الشيء ولا الرأي الراجح إلا إذا كان الوصف خاصا بالمرأة أو الجارية."},"support_links":[]},{"boundary":"Toplumsal değer ve eksiksiz para ağırlığı ayrı kalıplara bağlı iki yüzdür; bunlardan genel bir çıplak anlam çıkarılmaz.","branch_kind":"collocation","branch_ref":"root_001645/B007","candidate_links":[{"candidate_id":"cand_8b80b4f6fe8e91407782","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مِيزَان","morph_features":"STEM|POS:N|LEM:miyzaAn|ROOT:wzn|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:6:4:1","qac_word_ref":"101:6:4","surface_ar":"مَوَٰزِينُ"}],"gloss":"toplumsal değer; eksiksiz ağırlıktaki para","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kimsenin toplum içindeki önemi, değeri veya saygınlığı ağırlık düşüncesiyle değerlendirilir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli para nitelemesinde bir dirhemin eksiksiz ağırlıkta olduğu belirtilir."}}],"root_ar":"و ز ن","root_id":"root_001645","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin önem ve saygınlığına ilişkin kalıpları çekirdek, tam ağırlıktaki para nitelemesini ayrı kullanım olarak gösterir.","boundary_detail":"Toplumsal değer ve eksiksiz para ağırlığı ayrı kalıplara bağlı iki yüzdür; bunlardan genel bir çıplak anlam çıkarılmaz.","branch_image_ar":"قدر ومنزلة لها وزن","concept_gloss":"toplumsal değer; eksiksiz ağırlıktaki para","contextual_glosses":[{"applicability":"Bir kimsenin önemsiz, değersiz veya saygınlıktan yoksun sayıldığı olumsuz kalıplarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tam ağırlıktaki parayı anlatan somut kullanımı kapsamaz.","preserves":"Kişiye verilen değerin ve saygınlığın yok sayılmasını korur."},"facet_ids":["F001"],"text":"hiçbir değeri ve saygınlığı yok","usage_role":"contextual"},{"applicability":"Paranın eksiksiz ve beklenen ağırlıkta olduğunu bildiren somut nitelemede kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin toplum içindeki değeri ve saygınlığı okumasını dışarıda bırakır.","preserves":"Paranın eksiksiz ağırlıkta olma niteliğini korur."},"facet_ids":["F002"],"text":"tam ağırlıktaki dirhem","usage_role":"contextual"}],"definition":"Belirli söz kalıplarında bir kimsenin önem, değer veya saygınlık taşıyıp taşımadığını anlatır; ayrı bir para nitelemesinde ise paranın eksiksiz ağırlıkta olduğunu bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kimsenin toplum içindeki önemi, değeri veya saygınlığı ağırlık düşüncesiyle değerlendirilir."},{"facet_id":"F002","role":"associated_use","statement":"Belirli para nitelemesinde bir dirhemin eksiksiz ağırlıkta olduğu belirtilir."}],"identity_rationale":"Kaynak anlatımı, kişi için ağırlık bulunmamasını değer ve saygınlık yokluğu olarak açıklar. Tam ağırlıktaki para tanıklığı ise toplumsal değerin doğrudan parçası değil, ayrı bir kalıpta eksiksiz ağırlık bildiren somut kullanımdır; iki kullanım tek yalın anlama kaynaştırılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bizim yanımızda hiçbir değeri ve saygınlığı yok"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"onlara hiçbir değer ve saygınlık tanımayız"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"tam ağırlıktaki dirhem"}],"lexicalization_note":"Tanım, kişi değerini reddeden sözler ile tam ağırlıktaki parayı niteleyen ayrı kalıbı açıkça ayırır ve ikisini yalın kök anlamı olarak genellemez.","neighbor_coverage_note":"Bütün adaylar değer, saygınlık, övgü, küçültme, sıra ve toplumsal konum yönünden değerlendirildi; kişi değerini en iyi sınırlayan iki ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kalıplaşmış kişi değerlendirmesiyle ve ayrı para nitelemesiyle sınırlıdır; komşu dal değerli varlıklar ve önemli kişiler için daha geniştir.","focus_only":"Bu dal, kişi değerini belirli ağırlık kalıplarında ifade eder ve tam ağırlıktaki parayı ayrıca kapsar.","gloss":"değer ve ağırlık","neighbor_only":"Komşu dal, değerli ve korunmaya layık nesneleri, önemli kişiyi ve etkili sözü daha geniş biçimde kapsar.","neighbor_ref":"root_000202/B005","relation_type":"near_synonym","shared_zone":"İki dal da değer, önem ve saygınlığı ağırlık düşüncesiyle ilişkilendirir."},{"boundary_match":"partial","distinction":"Buradaki çekirdek kişiye biçilen önem ve saygınlıktır; komşuda ise yer veya konum kavramı kendi başına çekirdektir.","focus_only":"Bu dal, kişiye verilen önemi ve saygınlığı değer yargısı olarak anlatır.","gloss":"değer ve konum","neighbor_only":"Komşu dal, fiziksel yer ile görev veya toplum içindeki konumu ve bir yerde yerleşik olmayı kapsar.","neighbor_ref":"root_001332/B002","relation_type":"near_neighbor","shared_zone":"İki dal, kişinin toplum içindeki yerini anlatan bağlamlarda buluşabilir."}],"source_phrase_ar":"درهم وازن أي تام (sihah)؛ ما لفلان عندنا وزن أي قدر لخسته؛ فلا نقيم لهم يوم القيامة وزنا (tahdhib)؛ فلا نقيم لهم يوم القيامة وزنا (mufradat)","source_summary":"Ortak anlatım, kişi için ağırlığı değer ve saygınlıkla ilişkilendiren olumsuz kalıpları verir; tam ağırlıktaki para ise aynı dalda yer alan ayrı ve somut bir kullanımdır.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه الوزن بمعنى قدر الشخص أو منزلته، ونفي الوزن لمن لا قدر له، والتام الوافي في مثل درهم وازن.","what_is_not_ar":"لا يدخل فيه آلة الميزان ولا الموازنة بين شيئين إلا من جهة دلالة القدر والمنزلة."},"support_links":["sup_9c0d98a092022ae15631"]},{"boundary":"Anlam yalnız ölçülü veya dengeli yaratılmayı bildiren kalıba bağlıdır; madenler olası dar yorum, bütün yaratılmışlar ise geniş yorumdur.","branch_kind":"collocation","branch_ref":"root_001645/B008","candidate_links":[{"candidate_id":"cand_02ad7ad02cb221fb7d5a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مِيزَان","morph_features":"STEM|POS:N|LEM:miyzaAn|ROOT:wzn|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:6:4:1","qac_word_ref":"101:6:4","surface_ar":"مَوَٰزِينُ"}],"gloss":"ölçülü ve dengeli yaratılmış şey","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey belirlenmiş ölçüye uygun, dengeli ve düzgün biçimde var edilmiştir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kapsam bir yorumda madenlere daralır, başka bir yorumda yaratılmış her şeye genişler."}}],"root_ar":"و ز ن","root_id":"root_001645","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaratılmış şeyin belirli ölçüye, dengeye ve düzgünlüğe sahip oluşunu, değişebilen kapsam yorumlarından bağımsız olarak karşılar.","boundary_detail":"Anlam yalnız ölçülü veya dengeli yaratılmayı bildiren kalıba bağlıdır; madenler olası dar yorum, bütün yaratılmışlar ise geniş yorumdur.","branch_image_ar":"شيء موزون مخلوق باعتدال","concept_gloss":"ölçülü ve dengeli yaratılmış şey","contextual_glosses":[{"applicability":"Bir varlığın uygun ölçü ve dengeyle meydana getirildiğinin anlatıldığı geniş yorumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaratılıştaki belirlenmiş ölçüyü, dengeyi ve düzgünlüğü korur."},"facet_ids":["F001"],"text":"ölçülü ve dengeli yaratılmış","usage_role":"general"},{"applicability":"Kapsamın gümüş ve altın gibi madenlere daraltıldığı özel yorum açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yaratılmış her şeyi kapsayan geniş yorumu dışarıda bırakır.","preserves":"Belirlenmiş ölçü düşüncesini ve madenlere özgü dar yorumu korur."},"facet_ids":["F001","F002"],"text":"ölçüsü belirlenmiş madenler","usage_role":"explanatory"}],"definition":"Bir şeyin belirlenmiş ölçüye uygun, dengeli ve düzgün biçimde var edilmiş olduğunu anlatır; bağlama göre madenlerle sınırlandırılabilir veya yaratılmış her şeyi kapsayabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey belirlenmiş ölçüye uygun, dengeli ve düzgün biçimde var edilmiştir."},{"facet_id":"F002","role":"source_variant","statement":"Kapsam bir yorumda madenlere daralır, başka bir yorumda yaratılmış her şeye genişler."}],"identity_rationale":"Kaynak anlatımı, ölçülü ve dengeli biçimde var edilmiş şeyi destekler. Belirli bir anlatım bunu madenler olarak yorumlarken daha geniş anlatım yaratılmış her şeyi kapsar; maden örneği bütün dalın zorunlu kapsamı yapılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"ölçülü ve dengeli yaratılmış şey"}],"lexicalization_note":"Tanım yalnız ölçülü ve dengeli yaratılmış şeyi bildiren kalıba bağlıdır; bu yaratılış okuması yalın kökün genel anlamına aktarılmaz.","neighbor_coverage_note":"Bütün adaylar düzgünlük, ölçüye uygunluk, yaratılış, yapı, maden ve genel ölçme yönünden karşılaştırıldı; sınırı en iyi açıklayan üç ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yaratılmış şeye ilişkin tek bir kalıpla sınırlıdır; komşu dal düzeltme eylemi ve çeşitli alanlardaki genel denge için daha geniştir.","focus_only":"Bu dal, yalnız yaratılmış bir şeyin belirlenmiş ölçü ve dengeye sahip olduğunu bildiren kalıba bağlıdır.","gloss":"yaratılışta denge ve genel düzgünlük","neighbor_only":"Komşu dal, bir şeyi düzeltip düzgün kılma eylemini ve beden, sıcaklık ya da soğukluktaki genel dengeyi de kapsar.","neighbor_ref":"root_000991/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da düzgünlük, denge ve uygun ölçü düşüncesini taşır."},{"boundary_match":"partial","distinction":"Buradaki ölçü yaratılış ve var edilme bağlamına bağlıdır; komşu dal uygun miktar, orta boy ve beden oranı gibi daha geniş kullanımlara sahiptir.","focus_only":"Bu dal, var edilmiş şeyin yaratılıştan belirli ölçü ve denge taşımasını anlatır.","gloss":"uygun ölçü ve dengeli yaratılış","neighbor_only":"Komşu dal, bir şeyin uygun miktarda gelmesini, orta boyu ve hayvan gövdesindeki belirli oranları da kapsar.","neighbor_ref":"root_001205/B006","relation_type":"near_synonym","shared_zone":"İki dal, bir şeyin kendisine uygun ölçüde ve dengede bulunması alanında örtüşür."},{"boundary_match":"partial","distinction":"Bu dalda uygun ölçü ve denge kurucudur; komşuda ise parçalı yapı ve kuruluş biçimi kurucudur.","focus_only":"Bu dal, yaratılmış şeyin ölçülü ve dengeli olma niteliğini öne çıkarır.","gloss":"dengeli yaratılış ve yapı","neighbor_only":"Komşu dal, bir şeyin parçalarının nasıl kurulup birleştiğini anlatan yapı ve kuruluş biçimine odaklanır.","neighbor_ref":"root_000156/B002","relation_type":"near_neighbor","shared_zone":"İki dal, bir varlığın yaratılış biçimini ve beden yapısını anlatırken buluşabilir."}],"source_phrase_ar":"بناء يدل على تعديل واستقامة (maqayis)؛ وأنبتنا فيها من كل شيء موزون؛ قيل هو المعادن كالفضة والذهب؛ كل ما أوجده الله وأنه خلقه باعتدال (mufradat)","source_summary":"Ortak çekirdek, var edilen şeyde belirlenmiş ölçü, denge ve düzgünlüktür; kapsamın yalnız madenler mi yoksa bütün yaratılmışlar mı olduğu konusunda dar ve geniş yorumlar bulunur.","sources":["MQ","MU"],"what_is_ar":"يدخل فيه الموزون بمعنى المقدر أو المخلوق باعتدال، وما قيل في المعادن أو كل مخلوق مقدر.","what_is_not_ar":"لا يدخل فيه وزن المعاملة بالميزان ولا قصر المرأة ولا أسماء المواضع والنجوم."},"support_links":["sup_478fcf78ed0e13dadaa5"]}],"candidate_inventory":[{"anchor_refs":["101:6:1"],"branch_refs":[],"candidate_id":"cand_15b85a7b82682d556c1e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:6:1:consequential-detailing-turn","source_type":"word_analysis","support_ids":["sup_0791d4cead6bbd9884ed","sup_f463909a8afde001fc15"],"title":"consequence opens detailed reckoning","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:1","qac_refs":["101:6:1:1"],"status":"accepted"}},{"anchor_refs":["101:6:1"],"branch_refs":[],"candidate_id":"cand_c1145ec150b97672fae7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:6:1:from-image-chain-to-sorted-outcomes","source_type":"word_analysis","support_ids":["sup_49b681142da7fc0a990b","sup_f463909a8afde001fc15"],"title":"connective starts analytic sorting","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:1","qac_refs":["101:6:1:1"],"status":"accepted"}},{"anchor_refs":["101:6:1"],"branch_refs":[],"candidate_id":"cand_96eb3a57a959e7ec9df5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:6:1:fused-fa-amma-branch-marker","source_type":"word_analysis","support_ids":["sup_ea3711a5bbd5b89b5f75","sup_f463909a8afde001fc15"],"title":"bound particle fuses to branch marker","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:1","qac_refs":["101:6:1:1"],"status":"accepted"}},{"anchor_refs":["101:6:1"],"branch_refs":[],"candidate_id":"cand_a550d73917133ba51307","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:6:1:light-sound-transition","source_type":"word_analysis","support_ids":["sup_36b72530a759c28ed390","sup_f463909a8afde001fc15"],"title":"short onset carries the transition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:1","qac_refs":["101:6:1:1"],"status":"accepted"}},{"anchor_refs":["101:6:2"],"branch_refs":[],"candidate_id":"cand_643a6df03d5e03fd7a0f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:6:2:binary-branching-pair","source_type":"word_analysis","support_ids":["sup_039d2b4de3d54c0e153b","sup_855fbc770fbc27012bd1"],"title":"first half of paired sorting","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:2","qac_refs":["101:6:1:2"],"status":"accepted"}},{"anchor_refs":["101:6:2"],"branch_refs":[],"candidate_id":"cand_7684e28a4f77c2011bcb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:6:2:held-cadence","source_type":"word_analysis","support_ids":["sup_7a297c4cb2add49cd65e","sup_855fbc770fbc27012bd1"],"title":"sound shape holds the branch open","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:2","qac_refs":["101:6:1:2"],"status":"accepted"}},{"anchor_refs":["101:6:2"],"branch_refs":[],"candidate_id":"cand_98a5988b3790b2f5816c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:6:2:suspended-jawab-branch","source_type":"word_analysis","support_ids":["sup_1c55977b9fb694f94096","sup_855fbc770fbc27012bd1"],"title":"branch waits for its answer","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:2","qac_refs":["101:6:1:2"],"status":"accepted"}},{"anchor_refs":["101:6:2"],"branch_refs":[],"candidate_id":"cand_1b04b1eb76e7a0de3773","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:6:2:topic-and-condition-together","source_type":"word_analysis","support_ids":["sup_4f72afbdac08d0540ca0","sup_855fbc770fbc27012bd1"],"title":"topic setting also conditions the case","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:2","qac_refs":["101:6:1:2"],"status":"accepted"}},{"anchor_refs":["101:6:3"],"branch_refs":[],"candidate_id":"cand_0e74f0d8e46795a0d2ac","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:6:3:conditional-relative-openness","source_type":"word_analysis","support_ids":["sup_0b51c438ae4340ea4f0a","sup_49b45c72f6eccaf01cf6"],"title":"whoever and the one who remain live","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:3","qac_refs":["101:6:2:1"],"status":"accepted"}},{"anchor_refs":["101:6:3"],"branch_refs":[],"candidate_id":"cand_338cba5107d317fb4035","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:6:3:cosmic-to-individual-contraction","source_type":"word_analysis","support_ids":["sup_49b45c72f6eccaf01cf6","sup_969721411050a5b7c11e"],"title":"cosmic scene narrows to one human case","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:3","qac_refs":["101:6:2:1"],"status":"accepted"}},{"anchor_refs":["101:6:3"],"branch_refs":[],"candidate_id":"cand_d9a43c955ac993d93ffe","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:6:3:identity-through-scale-clause","source_type":"word_analysis","support_ids":["sup_49b45c72f6eccaf01cf6","sup_ec060d6377d3a9f56ce7"],"title":"person is identified by the clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:3","qac_refs":["101:6:2:1"],"status":"accepted"}},{"anchor_refs":["101:6:3"],"branch_refs":[],"candidate_id":"cand_83713317ff8d548f08f1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:6:3:possessive-and-pronominal-resumption","source_type":"word_analysis","support_ids":["sup_49b45c72f6eccaf01cf6","sup_e497f7e12924ca60f3c7"],"title":"open referent becomes possessed and resumed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:3","qac_refs":["101:6:2:1"],"status":"accepted"}},{"anchor_refs":["101:6:4"],"branch_refs":[],"candidate_id":"cand_a65b18cdc9e1d3539f51","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000202"],"scope":"focus_ayah","source_local_id":"101:6:4:boundary-from-vanished-mass-to-real-weight","source_type":"word_analysis","support_ids":["sup_9108b152aa76e3403d43","sup_e5a27bc927c41e19a129"],"title":"real weight follows collapsed mass","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:4","qac_refs":["101:6:3:1"],"status":"accepted"}},{"anchor_refs":["101:6:4"],"branch_refs":[],"candidate_id":"cand_a7e594984004c413f6bd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000202"],"scope":"focus_ayah","source_local_id":"101:6:4:completed-judgment-after-becoming","source_type":"word_analysis","support_ids":["sup_2301718bb0818de8f7bd","sup_e5a27bc927c41e19a129"],"title":"completed state replaces unfolding becoming","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:4","qac_refs":["101:6:3:1"],"status":"accepted"}},{"anchor_refs":["101:6:4"],"branch_refs":[],"candidate_id":"cand_15addb6c34ed4a741023","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000202"],"scope":"focus_ayah","source_local_id":"101:6:4:cosmic-to-personal-heaviness","source_type":"word_analysis","support_ids":["sup_2acc3dcb4a92695bc4c8","sup_e5a27bc927c41e19a129"],"title":"same predicate shifts scale","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:4","qac_refs":["101:6:3:1"],"status":"accepted"}},{"anchor_refs":["101:6:4"],"branch_refs":[],"candidate_id":"cand_9e82f838a5b22b9b23d1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000202"],"scope":"focus_ayah","source_local_id":"101:6:4:dense-acoustic-body","source_type":"word_analysis","support_ids":["sup_290aa656a7d350cc47f3","sup_e5a27bc927c41e19a129"],"title":"consonant texture thickens the predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:4","qac_refs":["101:6:3:1"],"status":"accepted"}},{"anchor_refs":["101:6:4"],"branch_refs":[],"candidate_id":"cand_247c4751edb7e2308700","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000202"],"scope":"focus_ayah","source_local_id":"101:6:4:evaluative-weight-and-worth","source_type":"word_analysis","support_ids":["sup_cf18fcf20143b6794483","sup_e5a27bc927c41e19a129"],"title":"heaviness carries assessed worth","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:4","qac_refs":["101:6:3:1"],"status":"accepted"}},{"anchor_refs":["101:6:4"],"branch_refs":[],"candidate_id":"cand_4874610898ace71631a6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000202"],"scope":"focus_ayah","source_local_id":"101:6:4:feminine-agreement-to-postposed-scales","source_type":"word_analysis","support_ids":["sup_39c6d2ad872854832d4c","sup_e5a27bc927c41e19a129"],"title":"agreement locks the scales as subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:4","qac_refs":["101:6:3:1"],"status":"accepted"}},{"anchor_refs":["101:6:4"],"branch_refs":[],"candidate_id":"cand_887060761e6693872b60","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000202"],"scope":"focus_ayah","source_local_id":"101:6:4:heavy-scales-judgment-formula","source_type":"word_analysis","support_ids":["sup_350c3014306957847913","sup_e5a27bc927c41e19a129"],"title":"recognized heavy-scales formula","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:4","qac_refs":["101:6:3:1"],"status":"accepted"}},{"anchor_refs":["101:6:4"],"branch_refs":[],"candidate_id":"cand_ea0de6c97663ca6521dd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000202"],"scope":"focus_ayah","source_local_id":"101:6:4:not-causative-loading","source_type":"word_analysis","support_ids":["sup_e5a27bc927c41e19a129","sup_f4782a87c3df411c80e1"],"title":"actual form avoids causative loading","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:4","qac_refs":["101:6:3:1"],"status":"accepted"}},{"anchor_refs":["101:6:4"],"branch_refs":[],"candidate_id":"cand_c6bdc7eb87db42cbd7ed","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000202"],"scope":"focus_ayah","source_local_id":"101:6:4:perfect-use-in-weight-judgment-scenes","source_type":"word_analysis","support_ids":["sup_1ccbdce2995450b9dfa0","sup_e5a27bc927c41e19a129"],"title":"perfect use clusters in judgment weight","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:4","qac_refs":["101:6:3:1"],"status":"accepted"}},{"anchor_refs":["101:6:4"],"branch_refs":[],"candidate_id":"cand_75c8624a67905d833ce1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000202"],"scope":"focus_ayah","source_local_id":"101:6:4:stative-settled-heaviness","source_type":"word_analysis","support_ids":["sup_0287b56e0e936d5f3d56","sup_e5a27bc927c41e19a129"],"title":"perfect stative makes heaviness settled","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:4","qac_refs":["101:6:3:1"],"status":"accepted"}},{"anchor_refs":["101:6:4"],"branch_refs":[],"candidate_id":"cand_7f90049fc79bdde6df69","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000202"],"scope":"focus_ayah","source_local_id":"101:6:4:verb-first-evaluation","source_type":"word_analysis","support_ids":["sup_b5e5a4dcffc594b1fb0c","sup_e5a27bc927c41e19a129"],"title":"weight arrives before owner is named","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:4","qac_refs":["101:6:3:1"],"status":"accepted"}},{"anchor_refs":["101:6:5"],"branch_refs":[],"candidate_id":"cand_0ced80984351bd39d4c8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001645"],"scope":"focus_ayah","source_local_id":"101:6:5:boundary-to-structured-measure","source_type":"word_analysis","support_ids":["sup_94bd3bd38e0f19076d74","sup_a2ee099d9bf0b3da6ef1"],"title":"dispersal gives way to measure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:5","qac_refs":["101:6:4:1","101:6:4:2"],"status":"accepted"}},{"anchor_refs":["101:6:5"],"branch_refs":[],"candidate_id":"cand_34943a2e539572013e29","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001645"],"scope":"focus_ayah","source_local_id":"101:6:5:cadential-landing","source_type":"word_analysis","support_ids":["sup_371678ab8a4c8c0f467a","sup_a2ee099d9bf0b3da6ef1"],"title":"long vowels land on the scales","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:5","qac_refs":["101:6:4:1","101:6:4:2"],"status":"accepted"}},{"anchor_refs":["101:6:5"],"branch_refs":[],"candidate_id":"cand_5ac377732602f54a897c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001645"],"scope":"focus_ayah","source_local_id":"101:6:5:criterion-closes-suspended-branch","source_type":"word_analysis","support_ids":["sup_5cb360b58bef7d64dc52","sup_a2ee099d9bf0b3da6ef1"],"title":"ayah ends on the criterion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:5","qac_refs":["101:6:4:1","101:6:4:2"],"status":"accepted"}},{"anchor_refs":["101:6:5"],"branch_refs":[],"candidate_id":"cand_ffbde0bf4b4b83f8ac12","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001645"],"scope":"focus_ayah","source_local_id":"101:6:5:cross-surah-scale-verdict-formula","source_type":"word_analysis","support_ids":["sup_816d90f7cc40f2978bd3","sup_a2ee099d9bf0b3da6ef1"],"title":"scale noun enters verdict formula","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:5","qac_refs":["101:6:4:1","101:6:4:2"],"status":"accepted"}},{"anchor_refs":["101:6:5"],"branch_refs":[],"candidate_id":"cand_a836d149be493fc0efe5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001645"],"scope":"focus_ayah","source_local_id":"101:6:5:heavy-scales-root-pair","source_type":"word_analysis","support_ids":["sup_a2ee099d9bf0b3da6ef1","sup_ea670314495f065a3acf"],"title":"scale noun joins heaviness predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:5","qac_refs":["101:6:4:1","101:6:4:2"],"status":"accepted"}},{"anchor_refs":["101:6:5"],"branch_refs":[],"candidate_id":"cand_114f5408a6bb73d86730","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001645"],"scope":"focus_ayah","source_local_id":"101:6:5:instrument-apparatus-not-bare-weight","source_type":"word_analysis","support_ids":["sup_a2ee099d9bf0b3da6ef1","sup_edb3dd49a64211068e2c"],"title":"instrument noun names apparatus","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:5","qac_refs":["101:6:4:1","101:6:4:2"],"status":"accepted"}},{"anchor_refs":["101:6:5"],"branch_refs":[],"candidate_id":"cand_747907871cc684ae2b28","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001645"],"scope":"focus_ayah","source_local_id":"101:6:5:local-heavy-light-axis","source_type":"word_analysis","support_ids":["sup_872376e64464c29ec9a7","sup_a2ee099d9bf0b3da6ef1"],"title":"same noun anchors heavy and light branches","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:5","qac_refs":["101:6:4:1","101:6:4:2"],"status":"accepted"}},{"anchor_refs":["101:6:5"],"branch_refs":[],"candidate_id":"cand_1ee47dd5789a0c3f3e87","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001645"],"scope":"focus_ayah","source_local_id":"101:6:5:measure-proportion-equity","source_type":"word_analysis","support_ids":["sup_a2ee099d9bf0b3da6ef1","sup_d4ae83bb0841053103c6"],"title":"scale image carries proportion and equity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:5","qac_refs":["101:6:4:1","101:6:4:2"],"status":"accepted"}},{"anchor_refs":["101:6:5"],"branch_refs":[],"candidate_id":"cand_02dbac4aa33520249cb8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001645"],"scope":"focus_ayah","source_local_id":"101:6:5:owned-reckoning-marker","source_type":"word_analysis","support_ids":["sup_1eaa15182429efaa3a3a","sup_a2ee099d9bf0b3da6ef1"],"title":"first possession personalizes reckoning","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:5","qac_refs":["101:6:4:1","101:6:4:2"],"status":"accepted"}},{"anchor_refs":["101:6:5"],"branch_refs":[],"candidate_id":"cand_c0330bd5c6ef7b38de8d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001645"],"scope":"focus_ayah","source_local_id":"101:6:5:paired-opposite-echo","source_type":"word_analysis","support_ids":["sup_54fa422b806c5f47cb07","sup_a2ee099d9bf0b3da6ef1"],"title":"possessed form returns with opposite predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:5","qac_refs":["101:6:4:1","101:6:4:2"],"status":"accepted"}},{"anchor_refs":["101:6:5"],"branch_refs":[],"candidate_id":"cand_1ab5d86943a542b71c53","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001645"],"scope":"focus_ayah","source_local_id":"101:6:5:personal-possessive-scales","source_type":"word_analysis","support_ids":["sup_506ec16256ac80f1a38e","sup_a2ee099d9bf0b3da6ef1"],"title":"suffix makes the scales his","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:5","qac_refs":["101:6:4:1","101:6:4:2"],"status":"accepted"}},{"anchor_refs":["101:6:5"],"branch_refs":[],"candidate_id":"cand_74c0af6e1ba66cc1aa23","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001645"],"scope":"focus_ayah","source_local_id":"101:6:5:plural-instrument-comprehensive-measure","source_type":"word_analysis","support_ids":["sup_6d07fd77ac5df89f9d74","sup_a2ee099d9bf0b3da6ef1"],"title":"broken plural widens the measure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:5","qac_refs":["101:6:4:1","101:6:4:2"],"status":"accepted"}},{"anchor_refs":["101:6:5"],"branch_refs":[],"candidate_id":"cand_537689f2d07e226b6721","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001645"],"scope":"focus_ayah","source_local_id":"101:6:5:subject-of-stative-predicate","source_type":"word_analysis","support_ids":["sup_a2ee099d9bf0b3da6ef1","sup_fabc63aed5295d900495"],"title":"scales bear the heaviness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:5","qac_refs":["101:6:4:1","101:6:4:2"],"status":"accepted"}},{"anchor_refs":["101:6:5"],"branch_refs":[],"candidate_id":"cand_64bcc37d165e675cd503","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001645"],"scope":"focus_ayah","source_local_id":"101:6:5:value-and-measurable-substance","source_type":"word_analysis","support_ids":["sup_a2ee099d9bf0b3da6ef1","sup_c10f8b258e3d64024f0d"],"title":"weight implies evaluable substance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:6:5","qac_refs":["101:6:4:1","101:6:4:2"],"status":"accepted"}},{"anchor_refs":["101:6:3"],"branch_refs":[],"candidate_id":"cand_de21c9cfc721f803dd35","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000202"],"scope":"focus_ayah","source_local_id":"101:6:3:1","source_type":"qac_morpheme","support_ids":["sup_c099c29f28b9c00aafd4"],"title":"QAC root occurrence: ث ق ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["101:6:4"],"branch_refs":[],"candidate_id":"cand_df5576e50e7b911244ac","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001645"],"scope":"focus_ayah","source_local_id":"101:6:4:1","source_type":"qac_morpheme","support_ids":["sup_a91746a993e212f499e5"],"title":"QAC root occurrence: و ز ن","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["101:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:6","branch_refs":["root_000202/B001","root_000202/B004","root_001645/B001","root_001645/B002"],"candidate_id":"cand_b1b6f168af58ffd42c5d","commentary_obligation":"review","hft_ref":"hft_b3583a438554d535d124","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_assessed_preponderance","source_type":"hft","support_ids":["sup_fe06e8d5eeb0ca1a8266"],"title":"baseline_assessed_preponderance","trust":"legacy_unbound"},{"anchor_refs":["101:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:6","branch_refs":["root_000202/B001","root_001645/B003","root_001645/B008"],"candidate_id":"cand_02ad7ad02cb221fb7d5a","commentary_obligation":"review","hft_ref":"hft_d2866f8f6476d13c4f4d","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_relational_alignment","source_type":"hft","support_ids":["sup_478fcf78ed0e13dadaa5"],"title":"baseline_relational_alignment","trust":"legacy_unbound"},{"anchor_refs":["101:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:6","branch_refs":["root_000202/B005","root_001645/B005","root_001645/B007"],"candidate_id":"cand_8b80b4f6fe8e91407782","commentary_obligation":"review","hft_ref":"hft_da60b461469d32909b12","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_worth_and_standing","source_type":"hft","support_ids":["sup_9c0d98a092022ae15631"],"title":"baseline_worth_and_standing","trust":"legacy_unbound"},{"anchor_refs":["101:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:6","branch_refs":["root_000202/B006","root_001645/B003","root_001645/B005"],"candidate_id":"cand_94b5ac463666a4e5efc8","commentary_obligation":"review","hft_ref":"hft_2c1be3101164520b4ba0","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_inertial_stability","source_type":"hft","support_ids":["sup_b6a80f33aa1aa71eea1b"],"title":"baseline_inertial_stability","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"101:6:1:1","qac_word_ref":"101:6:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"أَمَّا","morph_features":"STEM|POS:EXL|LEM:>am~aA","morpheme_role":"STEM","pos":"EXL","qac_ref":"101:6:1:2","qac_word_ref":"101:6:1","root_ar":"","surface_ar":"أَمَّا"},{"lemma_ar":"مَن","morph_features":"STEM|POS:COND|LEM:man","morpheme_role":"STEM","pos":"COND","qac_ref":"101:6:2:1","qac_word_ref":"101:6:2","root_ar":"","surface_ar":"مَن"},{"lemma_ar":"ثَقُلَتْ","morph_features":"STEM|POS:V|PERF|LEM:vaqulato|ROOT:vql|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"101:6:3:1","qac_word_ref":"101:6:3","root_ar":"ث ق ل","surface_ar":"ثَقُلَتْ"},{"lemma_ar":"مِيزَان","morph_features":"STEM|POS:N|LEM:miyzaAn|ROOT:wzn|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:6:4:1","qac_word_ref":"101:6:4","root_ar":"و ز ن","surface_ar":"مَوَٰزِينُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"101:6:4:2","qac_word_ref":"101:6:4","root_ar":"","surface_ar":"هُۥ"}],"word_analysis_qac_refs":[["101:6:1:1"],["101:6:1:2"],["101:6:2:1"],["101:6:3:1"],["101:6:4:1","101:6:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["101:6:1","101:6:2","101:6:3","101:6:4","101:6:5"]},"focus_surface_evidence":{"arabic_uthmani":"فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"101:6:1:1","qac_word_ref":"101:6:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"أَمَّا","morph_features":"STEM|POS:EXL|LEM:>am~aA","morpheme_role":"STEM","pos":"EXL","qac_ref":"101:6:1:2","qac_word_ref":"101:6:1","root_ar":"","surface_ar":"أَمَّا"},{"lemma_ar":"مَن","morph_features":"STEM|POS:COND|LEM:man","morpheme_role":"STEM","pos":"COND","qac_ref":"101:6:2:1","qac_word_ref":"101:6:2","root_ar":"","surface_ar":"مَن"},{"lemma_ar":"ثَقُلَتْ","morph_features":"STEM|POS:V|PERF|LEM:vaqulato|ROOT:vql|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"101:6:3:1","qac_word_ref":"101:6:3","root_ar":"ث ق ل","surface_ar":"ثَقُلَتْ"},{"lemma_ar":"مِيزَان","morph_features":"STEM|POS:N|LEM:miyzaAn|ROOT:wzn|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:6:4:1","qac_word_ref":"101:6:4","root_ar":"و ز ن","surface_ar":"مَوَٰزِينُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"101:6:4:2","qac_word_ref":"101:6:4","root_ar":"","surface_ar":"هُۥ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["101:6:1:1"],["101:6:1:2"],["101:6:2:1"],["101:6:3:1"],["101:6:4:1","101:6:4:2"]],"word_analysis_refs":["101:6:1","101:6:2","101:6:3","101:6:4","101:6:5"],"word_rows":[{"analysis_record_ref":"101:6:1","analytic_gloss_range_en":"a resultive and sequential connective that turns the prior scene into the first detailed judgment branch","analytic_root_gloss_range_en":null,"qac_refs":["101:6:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"101:6:2","analytic_gloss_range_en":"conditional-detailing particle that opens an as-for branch, suspends its answer until 101:7, and prepares the paired branch in 101:8","analytic_root_gloss_range_en":null,"qac_refs":["101:6:1:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"أَمَّا","transliteration":"ammā"}},{"analysis_record_ref":"101:6:3","analytic_gloss_range_en":"conditional-relative human pronoun, open as whoever/the one who, whose identity is defined by the heavy-scales clause and resumed by possession and the next ayah's pronoun","analytic_root_gloss_range_en":null,"qac_refs":["101:6:2:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"مَن","transliteration":"man"}},{"analysis_record_ref":"101:6:4","analytic_gloss_range_en":"proved or became heavy as a settled stative quality of the scales; locally evaluative and intransitive rather than causative burdening","analytic_root_gloss_range_en":"range around heaviness against lightness, burdens and carried weight, assessed measure, worth, and sluggish heaviness; this local perfect stative selects assessed heaviness of the scales while allowing narrowed value and burden pressure","qac_refs":["101:6:3:1"],"root":{"arabic":"ث ق ل","transliteration":"th-q-l"},"surface":{"arabic":"ثَقُلَتْ","transliteration":"thaqulat"}},{"analysis_record_ref":"101:6:5","analytic_gloss_range_en":"his scales or measuring criteria, a possessed broken plural instrument noun that bears the heaviness and closes the branch on personal evaluative measure","analytic_root_gloss_range_en":"range around weighing, balance, measure, proportion, justice, comparison, and value; the local plural instrument selects scales or criteria of judgment while excluding unrelated idioms","qac_refs":["101:6:4:1","101:6:4:2"],"root":{"arabic":"و ز ن","transliteration":"w-z-n"},"surface":{"arabic":"مَوَٰزِينُهُۥ","transliteration":"mawāzīnuhū"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["101:6"],"branch_refs":["root_000202/B001","root_000202/B004","root_001645/B001","root_001645/B002"],"candidate_id":"cand_b1b6f168af58ffd42c5d","evidence_scope":"focus_ayah","hft_ref":"hft_b3583a438554d535d124","item_id":"baseline_assessed_preponderance","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_assessed_preponderance","support_id":"sup_fe06e8d5eeb0ca1a8266"},{"anchor_refs":["101:6"],"branch_refs":["root_000202/B001","root_001645/B003","root_001645/B008"],"candidate_id":"cand_02ad7ad02cb221fb7d5a","evidence_scope":"focus_ayah","hft_ref":"hft_d2866f8f6476d13c4f4d","item_id":"baseline_relational_alignment","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_relational_alignment","support_id":"sup_478fcf78ed0e13dadaa5"},{"anchor_refs":["101:6"],"branch_refs":["root_000202/B005","root_001645/B005","root_001645/B007"],"candidate_id":"cand_8b80b4f6fe8e91407782","evidence_scope":"focus_ayah","hft_ref":"hft_da60b461469d32909b12","item_id":"baseline_worth_and_standing","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_worth_and_standing","support_id":"sup_9c0d98a092022ae15631"},{"anchor_refs":["101:6"],"branch_refs":["root_000202/B006","root_001645/B003","root_001645/B005"],"candidate_id":"cand_94b5ac463666a4e5efc8","evidence_scope":"focus_ayah","hft_ref":"hft_2c1be3101164520b4ba0","item_id":"baseline_inertial_stability","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_inertial_stability","support_id":"sup_b6a80f33aa1aa71eea1b"}],"diagnostics":[],"lane_counts":{"global":9,"macro":12,"micro":4},"packet_summary":{"ayah_count":11,"focus_ref":"101:6","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["101:1","101:2","101:3","101:4","101:5","101:6","101:7","101:8","101:9","101:10","101:11"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"101:6","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":16,"unstructured_record_count":0},"identity":{"ayah_ref":"101:6","lane":"micro","linguistic_source_ref":"101:6","surface_ref":"101:6","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"101:6","target_tokens":[["Tartıları",["101:6:4"]],["ağır",["101:6:3"]],["gelen",["101:6:3"]],["kişiye",["101:6:2"]],["gelince",["101:6:1"]]],"text":"Tartıları ağır gelen kişiye gelince,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":11,"id":"s101-p01-001-011","label":"Whole surah","number":1,"refs":["101:1","101:2","101:3","101:4","101:5","101:6","101:7","101:8","101:9","101:10","101:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:4:stative-settled-heaviness","source_type":"word_analysis","support_id":"sup_0287b56e0e936d5f3d56","text":"{\"blocking_evidence\":null,\"headline\":\"perfect stative makes heaviness settled\",\"reader_payoff\":\"The reader notices the scales as already bearing a settled quality of heaviness, not as objects being loaded by an explicit actor.\",\"reason\":\"The Form I perfect stative and intransitive frame support proved-heavy language; broader claims about permanence or theology are narrowed to the local grammatical payoff.\",\"representative_source_ids\":[\"QG-5ce5cc31\",\"QG-be4aa13a\",\"QF-33534e3c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:2:binary-branching-pair","source_type":"word_analysis","support_id":"sup_039d2b4de3d54c0e153b","text":"{\"blocking_evidence\":null,\"headline\":\"first half of paired sorting\",\"reader_payoff\":\"The reader notices that the heavy-scales branch is built to be answered by the matching light-scales branch (101:8).\",\"reason\":\"The CRITICAL rows give the concrete same-surah recurrence in 101:8, and the attachment evidence frames 101:6 as the first conditional branch in the outcome sequence.\",\"representative_source_ids\":[\"MG-6c480ae7\",\"QT-a3a86c82\",\"QE-44e97189\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:1:consequential-detailing-turn","source_type":"word_analysis","support_id":"sup_0791d4cead6bbd9884ed","text":"{\"blocking_evidence\":null,\"headline\":\"consequence opens detailed reckoning\",\"reader_payoff\":\"The reader notices that the first branch is not detached from the preceding catastrophe; it arrives as the consequence and explanation of that scene.\",\"reason\":\"QAC marks {{ar:فَ}} ({{tr:fa}}) as ta'qib or sababiyya, and attachment support treats the following words as a dependent branch, so sequence and resultive explanation both remain locally coherent.\",\"representative_source_ids\":[\"QG-052bacd4\",\"MG-e4cc6f85\",\"QS-d9858d23\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:3:conditional-relative-openness","source_type":"word_analysis","support_id":"sup_0b51c438ae4340ea4f0a","text":"{\"blocking_evidence\":null,\"headline\":\"whoever and the one who remain live\",\"reader_payoff\":\"The reader notices that the referent is both open as a universal case and classifying as a known type.\",\"reason\":\"QAC preserves the conditional or relative reading, and attachment evidence places the pronoun inside the unresolved {{ar:أَمَّا}} ({{tr:ammā}}) branch rather than forcing only one English value.\",\"representative_source_ids\":[\"MG-12c1f67e\",\"QS-b1e179d5\",\"QY-c4cdc634\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:2:suspended-jawab-branch","source_type":"word_analysis","support_id":"sup_1c55977b9fb694f94096","text":"{\"blocking_evidence\":null,\"headline\":\"branch waits for its answer\",\"reader_payoff\":\"The reader notices that 101:6 is structurally open, with the consequence withheld until 101:7.\",\"reason\":\"QAC identifies {{ar:أَمَّا}} ({{tr:ammā}}) as a conditional-detail particle paired with a later answer, and attachment support explicitly warns that 101:7 supplies the answer clause.\",\"representative_source_ids\":[\"QG-bc8548b6\",\"QT-5eb63357\",\"QB-51bed7df\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:4:perfect-use-in-weight-judgment-scenes","source_type":"word_analysis","support_id":"sup_1ccbdce2995450b9dfa0","text":"{\"blocking_evidence\":null,\"headline\":\"perfect use clusters in judgment weight\",\"reader_payoff\":\"The reader notices that the perfect stative form is salient in judgment-weight settings, not merely adjective-like filler.\",\"reason\":\"The exact root-form is low-occurrence and strongly associated with subject frames and the scale noun, supporting the distributional payoff.\",\"representative_source_ids\":[\"QI-d1956054\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:5:owned-reckoning-marker","source_type":"word_analysis","support_id":"sup_1eaa15182429efaa3a3a","text":"{\"blocking_evidence\":null,\"headline\":\"first possession personalizes reckoning\",\"reader_payoff\":\"The reader notices the first explicit possession marker turning the spectacle into an owned reckoning.\",\"reason\":\"The suffix is locally present and syntactically linked to the human referent, so the boundary payoff is grammatically anchored.\",\"representative_source_ids\":[\"QB-4acb651a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:4:completed-judgment-after-becoming","source_type":"word_analysis","support_id":"sup_2301718bb0818de8f7bd","text":"{\"blocking_evidence\":null,\"headline\":\"completed state replaces unfolding becoming\",\"reader_payoff\":\"The reader notices the shift from unfolding cosmic transformation to settled evaluative classification.\",\"reason\":\"The local perfect stative supports the CRITICAL contrast with the preceding imperfect becoming frame.\",\"representative_source_ids\":[\"QB-c2eeff59\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:4:dense-acoustic-body","source_type":"word_analysis","support_id":"sup_290aa656a7d350cc47f3","text":"{\"blocking_evidence\":null,\"headline\":\"consonant texture thickens the predicate\",\"reader_payoff\":\"The reader hears the weight predicate as phonetically denser than the surrounding particles.\",\"reason\":\"The sound row is retained as a surface payoff supporting the weight image, not as proof of a separate lexical sense.\",\"representative_source_ids\":[\"QP-e44ed22a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:4:cosmic-to-personal-heaviness","source_type":"word_analysis","support_id":"sup_2acc3dcb4a92695bc4c8","text":"{\"blocking_evidence\":null,\"headline\":\"same predicate shifts scale\",\"reader_payoff\":\"The reader notices the same heaviness predicate moving from the Hour's cosmic pressure (7:187) to one person's scales.\",\"reason\":\"The inter-ayah contrast is concrete and not contradicted: local grammar changes the subject to the possessed scales while the same predicate surface is preserved.\",\"representative_source_ids\":[\"QI-f1bf918d\",\"QE-2c0ade03\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:4:heavy-scales-judgment-formula","source_type":"word_analysis","support_id":"sup_350c3014306957847913","text":"{\"blocking_evidence\":null,\"headline\":\"recognized heavy-scales formula\",\"reader_payoff\":\"The reader recognizes the predicate as part of a repeated judgment formula where scale-weight routes outcome (7:8; 23:102).\",\"reason\":\"The contextual profile makes {{ar:و ز ن}} ({{tr:w-z-n}}) the top partner for this verb form, and the CRITICAL rows give concrete parallels in 7:8 and 23:102.\",\"representative_source_ids\":[\"QI-898af4db\",\"QI-e708b3c9\",\"QE-ebf79025\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:1:light-sound-transition","source_type":"word_analysis","support_id":"sup_36b72530a759c28ed390","text":"{\"blocking_evidence\":null,\"headline\":\"short onset carries the transition\",\"reader_payoff\":\"The reader hears that the transition begins lightly and continuously before the heavier judgment vocabulary arrives.\",\"reason\":\"The phonetic row is retained as a surface and cadence payoff; it reinforces the particle transition without being treated as independent semantic proof.\",\"representative_source_ids\":[\"QP-8606ada6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:5:cadential-landing","source_type":"word_analysis","support_id":"sup_371678ab8a4c8c0f467a","text":"{\"blocking_evidence\":null,\"headline\":\"long vowels land on the scales\",\"reader_payoff\":\"The reader hears the phrase expand after the clipped verb and land acoustically on the possessed scales.\",\"reason\":\"The sound rows are retained as cadence and contrast payoffs that reinforce the grammatical landing on the scale noun.\",\"representative_source_ids\":[\"QP-2ebdadf3\",\"QP-d5760c49\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:4:feminine-agreement-to-postposed-scales","source_type":"word_analysis","support_id":"sup_39c6d2ad872854832d4c","text":"{\"blocking_evidence\":null,\"headline\":\"agreement locks the scales as subject\",\"reader_payoff\":\"The reader sees the final agreement marker pointing forward to the plural scales as the bearer of the state.\",\"reason\":\"Attachment evidence makes {{ar:مَوَٰزِينُهُۥ}} ({{tr:mawāzīnuhū}}) the subject of the verb, and QAC explains the feminine singular agreement with the non-rational broken plural.\",\"representative_source_ids\":[\"QG-54c16554\",\"QF-ffa880d6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:3","source_type":"word_analysis","support_id":"sup_49b45c72f6eccaf01cf6","text":"{\"gloss_range\":\"conditional-relative human pronoun, open as whoever/the one who, whose identity is defined by the heavy-scales clause and resumed by possession and the next ayah's pronoun\",\"prose\":\"{{ar:مَن}} ({{tr:man}}) introduces a human case without naming an individual. It can be heard as conditional, 'whoever,' opening the case universally, and as relative, 'the one who,' identifying a class already characterized by heavy scales; the suspended {{ar:أَمَّا}} ({{tr:ammā}}) frame lets both pressures matter until the result is supplied in 101:7. The person is then defined by the verbal scale-clause and tightened through the suffix in {{ar:مَوَٰزِينُهُۥ}} ({{tr:mawāzīnuhū}}): the open human referent becomes the owner of the scales. After the prior cosmic scene, this pronoun contracts the frame into an anonymous but personal case, which 101:7 resumes with a singular pronoun.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مَن}} ({{tr:man}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:1:from-image-chain-to-sorted-outcomes","source_type":"word_analysis","support_id":"sup_49b681142da7fc0a990b","text":"{\"blocking_evidence\":null,\"headline\":\"connective starts analytic sorting\",\"reader_payoff\":\"The reader notices the turn from piling up apocalyptic images to separating human outcomes by scales.\",\"reason\":\"The CRITICAL boundary rows are consistent with the local connective and with translation support warning that this branch should remain scoped to the judgment sequence.\",\"representative_source_ids\":[\"QT-d96698b6\",\"QB-db97f6e4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:2:topic-and-condition-together","source_type":"word_analysis","support_id":"sup_4f72afbdac08d0540ca0","text":"{\"blocking_evidence\":null,\"headline\":\"topic setting also conditions the case\",\"reader_payoff\":\"The reader notices that the particle both names a case for attention and holds that case under a condition.\",\"reason\":\"The local particle selects {{ar:مَن}} ({{tr:man}}) as its complement, so its topic-specifying and conditional force both have a grammatical host.\",\"representative_source_ids\":[\"QS-9a12a8d3\",\"QF-be227670\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:5:personal-possessive-scales","source_type":"word_analysis","support_id":"sup_506ec16256ac80f1a38e","text":"{\"blocking_evidence\":null,\"headline\":\"suffix makes the scales his\",\"reader_payoff\":\"The reader notices that the measuring apparatus is personally attached to the open human referent, not left as detached generic scales.\",\"reason\":\"Attachment evidence forces the suffix to resume {{ar:مَن}} ({{tr:man}}), and QAC identifies the surface as a possessed plural noun.\",\"representative_source_ids\":[\"QG-87499aff\",\"QG-97783a04\",\"QF-e00c0bba\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:5:paired-opposite-echo","source_type":"word_analysis","support_id":"sup_54fa422b806c5f47cb07","text":"{\"blocking_evidence\":null,\"headline\":\"possessed form returns with opposite predicate\",\"reader_payoff\":\"The reader hears 101:8 as answering this same possessed-scale form with the opposite predicate.\",\"reason\":\"The same form recurs in the source rows as an antithetical same-surah echo; it is preserved as a local structural payoff.\",\"representative_source_ids\":[\"QE-0b27036a\",\"QE-39198dc2\",\"ME-d6587041\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:5:criterion-closes-suspended-branch","source_type":"word_analysis","support_id":"sup_5cb360b58bef7d64dc52","text":"{\"blocking_evidence\":null,\"headline\":\"ayah ends on the criterion\",\"reader_payoff\":\"The reader is left at the possessed criterion until 101:7 supplies the result.\",\"reason\":\"Attachment support marks the branch as awaiting its answer, and the final local word is the possessed scale noun.\",\"representative_source_ids\":[\"QT-27181807\",\"QB-f87cb669\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:5:plural-instrument-comprehensive-measure","source_type":"word_analysis","support_id":"sup_6d07fd77ac5df89f9d74","text":"{\"blocking_evidence\":null,\"headline\":\"broken plural widens the measure\",\"reader_payoff\":\"The reader notices that the wording pictures more than one narrow balance: the assessment is formally broad and comprehensive.\",\"reason\":\"The broken plural instrument form supports multiple scales, criteria, or acts of weighing; claims that the person is the scale or that poetic and grammatical technical senses are locally active are narrowed out.\",\"representative_source_ids\":[\"MG-62a8b4a0\",\"QF-dc0a9be0\",\"QF-f54688fe\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:2:held-cadence","source_type":"word_analysis","support_id":"sup_7a297c4cb2add49cd65e","text":"{\"blocking_evidence\":null,\"headline\":\"sound shape holds the branch open\",\"reader_payoff\":\"The reader hears the particle's compressed hold as matching the grammatical suspension.\",\"reason\":\"The sound row is coherent as recitational support for a particle whose syntax demonstrably suspends the answer.\",\"representative_source_ids\":[\"QP-626bb018\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:5:cross-surah-scale-verdict-formula","source_type":"word_analysis","support_id":"sup_816d90f7cc40f2978bd3","text":"{\"blocking_evidence\":null,\"headline\":\"scale noun enters verdict formula\",\"reader_payoff\":\"The reader recognizes the noun inside a wider scale-verdict formula where scale state routes outcome (7:8; 23:102).\",\"reason\":\"The CRITICAL row supplies concrete parallels in 7:8 and 23:102, and contextual evidence supports the scale noun's judgment-register deployment.\",\"representative_source_ids\":[\"QE-30bc1833\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:2","source_type":"word_analysis","support_id":"sup_855fbc770fbc27012bd1","text":"{\"gloss_range\":\"conditional-detailing particle that opens an as-for branch, suspends its answer until 101:7, and prepares the paired branch in 101:8\",\"prose\":\"{{ar:أَمَّا}} ({{tr:ammā}}) opens the first case but does not let the ayah finish the verdict inside 101:6. It topicalizes the person whose scales are heavy and also makes that case conditional, so the reader must wait for the answer in 101:7. The same branch marker returns for the opposite light-scales case (101:8), which makes 101:6 the first half of a binary sorting pattern rather than an isolated statement. Its doubled sound and compact surface belong to that function: the particle opens, holds, and delays resolution.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:أَمَّا}} ({{tr:ammā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:5:local-heavy-light-axis","source_type":"word_analysis","support_id":"sup_872376e64464c29ec9a7","text":"{\"blocking_evidence\":null,\"headline\":\"same noun anchors heavy and light branches\",\"reader_payoff\":\"The reader notices that the repeated scale noun is the axis of the heavy branch in 101:6 and the light branch in 101:8.\",\"reason\":\"The CRITICAL rows give the same-surah recurrence in 101:8, and the contextual supplement includes same-root references for the paired scale ayahs.\",\"representative_source_ids\":[\"QI-6629e6f6\",\"QI-f95fd9f9\",\"QT-1066f6c2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:4:boundary-from-vanished-mass-to-real-weight","source_type":"word_analysis","support_id":"sup_9108b152aa76e3403d43","text":"{\"blocking_evidence\":null,\"headline\":\"real weight follows collapsed mass\",\"reader_payoff\":\"The reader notices that after the mountains lose physical solidity, the first stable weight appears in the scales.\",\"reason\":\"The boundary rows connect the prior image to the local weight predicate, and contextual evidence shows the verb strongly collocating with the scale noun in this form.\",\"representative_source_ids\":[\"QS-2e615ee8\",\"QB-a327da4f\",\"QY-ca1dd579\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:5:boundary-to-structured-measure","source_type":"word_analysis","support_id":"sup_94bd3bd38e0f19076d74","text":"{\"blocking_evidence\":null,\"headline\":\"dispersal gives way to measure\",\"reader_payoff\":\"The reader notices the boundary shift from de-structured cosmic material to ordered personal measurement.\",\"reason\":\"The boundary rows align with the local instrument noun and with the prior-to-current transition preserved by the branch opening.\",\"representative_source_ids\":[\"QB-5c66d747\",\"QB-efc12980\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:3:cosmic-to-individual-contraction","source_type":"word_analysis","support_id":"sup_969721411050a5b7c11e","text":"{\"blocking_evidence\":null,\"headline\":\"cosmic scene narrows to one human case\",\"reader_payoff\":\"The reader notices the sharp contraction from universal spectacle to a single anonymous human case.\",\"reason\":\"The boundary row is compatible with the local pronoun: after the prior scene, the first human referent appears as an open singular case in the branch.\",\"representative_source_ids\":[\"QB-0c91231c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:5","source_type":"word_analysis","support_id":"sup_a2ee099d9bf0b3da6ef1","text":"{\"gloss_range\":\"his scales or measuring criteria, a possessed broken plural instrument noun that bears the heaviness and closes the branch on personal evaluative measure\",\"prose\":\"{{ar:مَوَٰزِينُهُۥ}} ({{tr:mawāzīnuhū}}) is where the branch lands: not on the person alone and not yet on the outcome, but on the possessed measure by which the person is classified. The suffix resumes {{ar:مَن}} ({{tr:man}}), making the scales personally definite; as the first explicit possession marker in this turn, it changes the spectacle into an owned reckoning, while the nominative plural functions as the subject that bears {{ar:ثَقُلَتْ}} ({{tr:thaqulat}}). As a broken plural instrument noun, the word keeps the concrete balance image while widening the frame toward multiple measures, criteria, or acts of weighing; that breadth is comprehensive, but still local to judgment, not every idiom in the root family. The root's measure, proportion, equity, and value fields make the scales an evaluative apparatus rather than a prop, and the no-weight contrast in 18:105 sharpens the opposite condition here: this person has scales that can register substance. The same noun returns in the opposite light-scales branch (101:8), so 101:6 and 101:8 turn on one repeated measure, while cross-surah scale-verdict parallels in 7:8 and 23:102 place the phrase inside a larger judgment formula. Closing the ayah on the possessed scales leaves the reader at the criterion until 101:7 states the result, and the phrase's longer vowels let that measured object occupy the acoustic landing after the clipped verb.\",\"root_display\":\"{{ar:و ز ن}} ({{tr:w-z-n}})\",\"root_gloss_range\":\"range around weighing, balance, measure, proportion, justice, comparison, and value; the local plural instrument selects scales or criteria of judgment while excluding unrelated idioms\",\"surface_display\":\"{{ar:مَوَٰزِينُهُۥ}} ({{tr:mawāzīnuhū}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"101:6:4:1","source_type":"qac_morpheme","support_id":"sup_a91746a993e212f499e5","text":"{\"lemma_ar\":\"مِيزَان\",\"morph_features\":\"STEM|POS:N|LEM:miyzaAn|ROOT:wzn|MP|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"101:6:4:1\",\"qac_word_ref\":\"101:6:4\",\"root_ar\":\"و ز ن\",\"surface_ar\":\"مَوَٰزِينُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:4:verb-first-evaluation","source_type":"word_analysis","support_id":"sup_b5e5a4dcffc594b1fb0c","text":"{\"blocking_evidence\":null,\"headline\":\"weight arrives before owner is named\",\"reader_payoff\":\"The reader feels evaluation leading the clause before the possessed scales complete the explanation.\",\"reason\":\"The local word order places the stative verb before its explicit subject, making the weight predicate the hinge between person and scales.\",\"representative_source_ids\":[\"QT-81eb108c\",\"QT-ae4bd6ce\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"101:6:3:1","source_type":"qac_morpheme","support_id":"sup_c099c29f28b9c00aafd4","text":"{\"lemma_ar\":\"ثَقُلَتْ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:vaqulato|ROOT:vql|3FS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"101:6:3:1\",\"qac_word_ref\":\"101:6:3\",\"root_ar\":\"ث ق ل\",\"surface_ar\":\"ثَقُلَتْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:5:value-and-measurable-substance","source_type":"word_analysis","support_id":"sup_c10f8b258e3d64024f0d","text":"{\"blocking_evidence\":null,\"headline\":\"weight implies evaluable substance\",\"reader_payoff\":\"The reader notices the opposite of no-weight judgment: the person has scales that can register real evaluative substance.\",\"reason\":\"The value and no-weight contrast is valid as narrowed pressure, especially with 18:105 named by the row; it does not replace the local instrument noun sense.\",\"representative_source_ids\":[\"QS-c58df003\",\"QI-f46d14bc\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:4:evaluative-weight-and-worth","source_type":"word_analysis","support_id":"sup_cf18fcf20143b6794483","text":"{\"blocking_evidence\":null,\"headline\":\"heaviness carries assessed worth\",\"reader_payoff\":\"The reader feels heaviness as moral substance and worth, while the local verb still means that the scales prove heavy.\",\"reason\":\"Accepted root branches include assessed heaviness and worth, so the value pressure is legitimate; local syntax narrows it to evaluative heaviness of the scales rather than an independent valuables sense.\",\"representative_source_ids\":[\"QS-0972faae\",\"QS-b5718da5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:5:measure-proportion-equity","source_type":"word_analysis","support_id":"sup_d4ae83bb0841053103c6","text":"{\"blocking_evidence\":null,\"headline\":\"scale image carries proportion and equity\",\"reader_payoff\":\"The reader sees the scales as structured proportion and equitable measurement after the prior scene of de-structuring.\",\"reason\":\"V4 supports weighing, balance, equity, and proportion branches; local grammar narrows that field to the possessed plural instrument in the judgment branch.\",\"representative_source_ids\":[\"QS-4d46139d\",\"QS-6678bb8c\",\"QS-905213f8\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:3:possessive-and-pronominal-resumption","source_type":"word_analysis","support_id":"sup_e497f7e12924ca60f3c7","text":"{\"blocking_evidence\":null,\"headline\":\"open referent becomes possessed and resumed\",\"reader_payoff\":\"The reader follows the anonymous person into a possessive chain and then into the singular resumed subject of 101:7.\",\"reason\":\"Attachment cross-reference evidence forces the suffix in {{ar:مَوَٰزِينُهُۥ}} ({{tr:mawāzīnuhū}}) to resume {{ar:مَن}} ({{tr:man}}), and the CRITICAL row links the same referent forward to 101:7.\",\"representative_source_ids\":[\"QG-c536079a\",\"QB-681627ed\",\"QB-f5c8c86d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:4","source_type":"word_analysis","support_id":"sup_e5a27bc927c41e19a129","text":"{\"gloss_range\":\"proved or became heavy as a settled stative quality of the scales; locally evaluative and intransitive rather than causative burdening\",\"prose\":\"{{ar:ثَقُلَتْ}} ({{tr:thaqulat}}) is the hinge that makes the person in the branch identifiable by the state of his scales. Its perfect stative form presents the heaviness as a settled quality, not as a transitive loading performed by an expressed agent; the feminine ending anticipates {{ar:مَوَٰزِينُهُۥ}} ({{tr:mawāzīnuhū}}) as the grammatical subject. The weight is evaluative, not neutral mass: after the prior scene strips apparent physical mass away, and after an unfolding becoming gives way to completed judgment, the scales become the stable place where real substance appears. The root's worth and carried-weight fields sharpen that payoff in narrowed form, while local grammar keeps the selected sense as the scales proving heavy. The word also belongs to a recognizable heavy-scales judgment formula, with close parallels in 7:8 and 23:102, and it can contrast with the Hour's cosmic heaviness in 7:187: the same predicate moves from cosmic weight to a personal measuring scene. Even the verb-first order matters, because weight arrives before the possessed scales are fully named. Its consonant texture gives the predicate a denser acoustic body than the surrounding particles, reinforcing the weight image without adding a separate lexical sense.\",\"root_display\":\"{{ar:ث ق ل}} ({{tr:th-q-l}})\",\"root_gloss_range\":\"range around heaviness against lightness, burdens and carried weight, assessed measure, worth, and sluggish heaviness; this local perfect stative selects assessed heaviness of the scales while allowing narrowed value and burden pressure\",\"surface_display\":\"{{ar:ثَقُلَتْ}} ({{tr:thaqulat}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:1:fused-fa-amma-branch-marker","source_type":"word_analysis","support_id":"sup_ea3711a5bbd5b89b5f75","text":"{\"blocking_evidence\":null,\"headline\":\"bound particle fuses to branch marker\",\"reader_payoff\":\"The reader sees the branch beginning as a linked particle compound before the person or scales are named.\",\"reason\":\"The local first word is a proclitic attached before the conditional-detailing particle, and the clause evidence confirms that the following unit is the branch opened by that compound.\",\"representative_source_ids\":[\"QF-987e5514\",\"QT-b71277ba\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:5:heavy-scales-root-pair","source_type":"word_analysis","support_id":"sup_ea670314495f065a3acf","text":"{\"blocking_evidence\":null,\"headline\":\"scale noun joins heaviness predicate\",\"reader_payoff\":\"The reader notices the final word as part of a known weighing pair: plural possession, heaviness, and scale language converge into one assessment frame.\",\"reason\":\"Contextual collocation evidence pairs the scale noun with the heaviness verb, and the synthesis row combines that pair with the plural and possessive form.\",\"representative_source_ids\":[\"QI-70e578b6\",\"QY-c2e422ff\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:3:identity-through-scale-clause","source_type":"word_analysis","support_id":"sup_ec060d6377d3a9f56ce7","text":"{\"blocking_evidence\":null,\"headline\":\"person is identified by the clause\",\"reader_payoff\":\"The reader notices that the person is not characterized by name or biography, but by the state of the scales.\",\"reason\":\"The following verbal clause is the qualifier or condition attached to {{ar:مَن}} ({{tr:man}}), so the human referent is grammatically defined through the scale predicate.\",\"representative_source_ids\":[\"QG-edaf2bcf\",\"QT-ddf8641e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:5:instrument-apparatus-not-bare-weight","source_type":"word_analysis","support_id":"sup_edb3dd49a64211068e2c","text":"{\"blocking_evidence\":null,\"headline\":\"instrument noun names apparatus\",\"reader_payoff\":\"The reader notices that the word names the apparatus or criterion for establishing weight, not weight as an abstract noun alone.\",\"reason\":\"QAC tags the word as a noun of instrument, and V4 includes accepted scale and balance senses for the root.\",\"representative_source_ids\":[\"QF-5c0e0182\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:1","source_type":"word_analysis","support_id":"sup_f463909a8afde001fc15","text":"{\"gloss_range\":\"a resultive and sequential connective that turns the prior scene into the first detailed judgment branch\",\"prose\":\"{{ar:فَ}} ({{tr:fa}}) does more than join another sentence. Bound into {{ar:فَأَمَّا}} ({{tr:fa-ammā}}), it makes the heavy-scales branch follow as the consequence and detailing of the prior catastrophe, using a familiar conditional-branching shape also visible in outcome-sorting passages (92:5-10; 79:37-41; 69:19-25). The reader moves from accumulated cosmic description into sorted personal outcomes: the previous image-stacking stops, and the ayah opens with a connective that turns scene into reckoning. Its small sound also matters in a limited way: the light onset lets the branch begin continuously, with the transition carried first by particles before any human or scale word appears.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:4:not-causative-loading","source_type":"word_analysis","support_id":"sup_f4782a87c3df411c80e1","text":"{\"blocking_evidence\":null,\"headline\":\"actual form avoids causative loading\",\"reader_payoff\":\"The reader notices that attention stays on the proven weight of the scales rather than on an expressed loader or external act of burdening.\",\"reason\":\"V4 contains causative and burden branches, but the local surface is intransitive and stative; the valid contrast survives as a limit on translation, not as activation of causative loading.\",\"representative_source_ids\":[\"QS-2228d106\",\"QF-835727a1\",\"MF-f25cffbc\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:6:5:subject-of-stative-predicate","source_type":"word_analysis","support_id":"sup_fabc63aed5295d900495","text":"{\"blocking_evidence\":null,\"headline\":\"scales bear the heaviness\",\"reader_payoff\":\"The reader sees that the scales are not the thing being weighed as an object; they are the subject whose state decides the case.\",\"reason\":\"The attachment relation marks {{ar:مَوَٰزِينُهُۥ}} ({{tr:mawāzīnuhū}}) as the subject of {{ar:ثَقُلَتْ}} ({{tr:thaqulat}}), and QAC marks it nominative.\",\"representative_source_ids\":[\"QG-ee5f5bd0\",\"QT-8916dbad\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ","ayah_ref":"101:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000202/B001","root_000202/B004","root_001645/B001","root_001645/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000202","role":"Literal heaviness opposed to lightness supplies the force of preponderance and tipping.","root":"ث ق ل","source_ref":"101:6","source_word_indices":["3"]},{"branch_id":"B004","mapped_root_id":"root_000202","role":"Known standard-weight and the act of assigning weight bind the predicate directly to measurement.","root":"ث ق ل","source_ref":"101:6","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001645","role":"Measurement by weighing or estimation makes the plural balances multiple procedures of assessment.","root":"و ز ن","source_ref":"101:6","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_001645","role":"Justice, equity, and accounting make the registered weight consequential rather than merely physical.","root":"و ز ن","source_ref":"101:6","source_word_indices":["4"]}],"changed_reading":{"after":"The person's several measures register decisive preponderance under an equitable accounting.","before":"A person's scales are physically heavy."},"confidence":"strong","focus_anchor":"Focus word 3 predicates heaviness of the plural balance noun at word 4.","mechanism":"Physical or assessed heaviness converges with known weighing and equitable accounting: several measures register enough preponderance to tip an evaluation.","model_id":"baseline_assessed_preponderance"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_assessed_preponderance","source_type":"hft","support_id":"sup_fe06e8d5eeb0ca1a8266","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ","ayah_ref":"101:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000202/B001","root_001645/B003","root_001645/B008"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000202","role":"Heaviness gives one side of an alignment greater pull or priority.","root":"ث ق ل","source_ref":"101:6","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_001645","role":"Balancing and aligning two things supplies a relational rather than merely container-based mechanism.","root":"و ز ن","source_ref":"101:6","source_word_indices":["4"]},{"branch_id":"B008","mapped_root_id":"root_001645","role":"Measured proportion lets each balance register whether a dimension has attained fitting form.","root":"و ز ن","source_ref":"101:6","source_word_indices":["4"]}],"changed_reading":{"after":"Multiple dimensions come into comparison and proportion, with the person's side acquiring decisive relational pull.","before":"The balances hold quantities to be totaled."},"confidence":"medium","focus_anchor":"The plural balances at focus word 4 can name relations of comparison, while word 3 marks which relation acquires preponderance.","mechanism":"Balancing can align one thing with another, and proportion can be built into what is measured. The clause can therefore describe a field of correspondences reaching weighted alignment, not only objects piled in pans.","model_id":"baseline_relational_alignment"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_relational_alignment","source_type":"hft","support_id":"sup_478fcf78ed0e13dadaa5","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ","ayah_ref":"101:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000202/B005","root_001645/B005","root_001645/B007"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000202","role":"Preciousness and high worth convert heaviness from bulk into protected significance.","root":"ث ق ل","source_ref":"101:6","source_word_indices":["3"]},{"branch_id":"B007","mapped_root_id":"root_001645","role":"Standing or value that carries weight supplies the person's recognized consequence.","root":"و ز ن","source_ref":"101:6","source_word_indices":["4"]},{"branch_id":"B005","mapped_root_id":"root_001645","role":"Steady, preponderant judgment adds intellectual and dispositional gravitas to assessed worth.","root":"و ز ن","source_ref":"101:6","source_word_indices":["4"]}],"changed_reading":{"after":"What belongs to the person bears recognized worth, standing, and settled judgment.","before":"The person's side contains a large amount."},"confidence":"medium","focus_anchor":"Both the heaviness predicate and the balance noun carry focus-only branches of worth, rank, and steady judgment.","mechanism":"The two focus roots independently converge on gravitas: what is precious and consequential has weight, and a person or judgment with standing is weighty. The clause can assess significance rather than bulk.","model_id":"baseline_worth_and_standing"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_worth_and_standing","source_type":"hft","support_id":"sup_9c0d98a092022ae15631","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ","ayah_ref":"101:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000202/B006","root_001645/B003","root_001645/B005"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_000202","role":"Sluggishness and dragging motion supply inertia that can be reread as damping under disturbance.","root":"ث ق ل","source_ref":"101:6","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_001645","role":"Alignment between things supplies the orientation that inertia preserves.","root":"و ز ن","source_ref":"101:6","source_word_indices":["4"]},{"branch_id":"B005","mapped_root_id":"root_001645","role":"Steady judgment gives the mechanically stable orientation a dispositional analogue.","root":"و ز ن","source_ref":"101:6","source_word_indices":["4"]}],"changed_reading":{"after":"The balances possess enough inertia and steadiness to resist displacement.","before":"Heaviness is simply more load."},"confidence":"exploratory","focus_anchor":"Heaviness at word 3 can slow movement, while the balance at word 4 can preserve alignment and steadiness.","mechanism":"The packet supplies drag, alignment, and steady judgment; I recast drag mechanically as damping. On this reading, weight is resistance to displacement, allowing an orientation to persist under disturbance.","model_id":"baseline_inertial_stability"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_inertial_stability","source_type":"hft","support_id":"sup_b6a80f33aa1aa71eea1b","trust":"legacy_unbound"}]}
</lane_packet_json>
