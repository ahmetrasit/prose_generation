# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **93:10**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s093-regular-20260912/s093/93_10/micro.discovery.json` and modify nothing
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
  "ayah_ref": "93:10",
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
{"branch_registry":[{"boundary":"Dal, sorma ve isteme eylemlerini kapsar; istenen şeyin kendisini, isteğin karşılanmasını ve karşılıklı sormayı ayrı dallara bırakır.","branch_kind":"mixed_non_bare","branch_ref":"root_000661/B001","candidate_links":[{"candidate_id":"cand_57af0f13050cb6883527","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَآئِل","morph_features":"STEM|POS:N|ACT|PCPL|LEM:saA^}il|ROOT:sAl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:10:2:2","qac_word_ref":"93:10:2","surface_ar":"سَّآئِلَ"}],"gloss":"bilgi sormak veya bir şey istemek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir muhataba yönelip bilgi edinmeye veya bir şeyi elde etmeye çalışma eylemini bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyi doğrudan muhataptan isteme ile bir konu ya da kişi hakkında bilgi sorma, eylemin farklı söz dizimsel kuruluşlarıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çok soru soran kimse ve gereksinimini bildirerek yardım isteyen yoksul, eylemi yapan kişi olarak adlandırılabilir."}}],"root_ar":"س ء ل","root_id":"root_000661","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın bir muhataptan bilgi ya da istenen bir şeyi elde etmeye yönelen eylem çekirdeğinin tamamı için uygundur.","boundary_detail":"Dal, sorma ve isteme eylemlerini kapsar; istenen şeyin kendisini, isteğin karşılanmasını ve karşılıklı sormayı ayrı dallara bırakır.","branch_image_ar":"السؤال والطلب","concept_gloss":"bilgi sormak veya bir şey istemek","contextual_glosses":[{"applicability":"Bir konu, nesne veya kişi hakkında bilgi edinmeye yönelik kullanımlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Muhataba yönelerek bilgi edinme amacını ve soru eylemini eksiksiz korur."},"facet_ids":["F001","F002"],"text":"sormak","usage_role":"contextual"},{"applicability":"Bir şeyin doğrudan muhataptan elde edilmek istendiği nesneli kuruluşlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir şeyi muhataptan elde etmeye yönelik açık isteği doğal biçimde karşılar."},"facet_ids":["F001","F002"],"text":"istemek","usage_role":"contextual"},{"applicability":"Eylemi yapan kişinin, özellikle gereksinimini bildirip yardım isteyen yoksulun adlandırıldığı kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin gereksinimini bildirerek başkasından yardım istemesi özelliğini korur."},"facet_ids":["F003"],"text":"yardım isteyen kişi","usage_role":"explanatory"}],"definition":"Bir kimseye yönelerek ondan bir şey isteme ya da bir konu, nesne veya kişi hakkında bilgi edinmeye çalışma eylemidir. Doğrudan nesneli istek ve ilgeçli bilgi sorusu bu çekirdeğin farklı kuruluşlarıdır; çok soran veya yardım isteyen kişiye verilen adlar eylemden türeyen kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir muhataba yönelip bilgi edinmeye veya bir şeyi elde etmeye çalışma eylemini bildirir."},{"facet_id":"F002","role":"specialization","statement":"Bir şeyi doğrudan muhataptan isteme ile bir konu ya da kişi hakkında bilgi sorma, eylemin farklı söz dizimsel kuruluşlarıdır."},{"facet_id":"F003","role":"associated_use","statement":"Çok soru soran kimse ve gereksinimini bildirerek yardım isteyen yoksul, eylemi yapan kişi olarak adlandırılabilir."}],"identity_rationale":"Kaynak ifadesi, bir kişiden bilgi edinmek için ona yönelmeyi ve bir şeyi ondan istemeyi aynı dalda açıkça tanımlar. Doğrudan nesne alan kullanım istek bildirmeye, bir konu ya da kişiyle kurulan ilgeçli kullanımlar ise bilgi edinmeye yönelir; çok soran kişi ve yardım isteyen yoksul için kullanılan adlar bu eylem çekirdeğine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"sormak; istemek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"sorma; soru; istekte bulunma"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"soru veya istek konusu"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"çok soru soran kimse"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"sor; iste"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"sorular veya istek konuları"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"soran ya da isteyen kimse; yardım isteyen yoksul"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ondan bir şeyi istemek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"ona bir şey hakkında soru sormak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"bir kişi hakkında soru sormak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ilk ses düşürülerek söylenen sormak biçimi"}],"lexicalization_note":"Tanım yalın eylem çekirdeğini korurken, doğrudan bir şeyi isteme ile bir konu veya kişi hakkında bilgi sorma kalıplarını ayrı uygulamalar olarak gösterir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; eylem-nesne ayrımı, karşılıklılık, ısrar derecesi ve muhataba yönelme koşulunu en açık gösteren dört komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bir kişinin yaptığı iletişimsel eylemdir; komşu dal ise bu eylemin hedefi olan istenmiş şeydir. Eylem ile nesnesi aynı bağlamda yer alsa da birbirinin yerine kullanılamaz.","focus_only":"Bir muhataba yöneltilen sorma ya da isteme eylemini belirtir.","gloss":"sorma eylemi ile istenen şey","neighbor_only":"Eylemin yöneldiği, kişi tarafından istenmiş olan şeyi belirtir.","neighbor_ref":"root_000661/B002","relation_type":"near_neighbor","shared_zone":"Her ikisi de bir isteğin kurulması ve yöneldiği içerik çevresinde buluşur."},{"boundary_match":"partial","distinction":"Genel sorma eylemi tek yönlü olabilir; karşılıklı sormada ise en az iki katılımcı sırayla veya karşılıklı biçimde soran konumuna geçer. Bu katılımcı koşulu genel dalın zorunlu parçası değildir.","focus_only":"Tek bir soranın bir muhataba yönelmesi yeterlidir ve karşılık verme koşulu yoktur.","gloss":"sormak ile birbirine sormak","neighbor_only":"Katılanların birbirlerine soru yöneltmesi ve soran rolünü karşılıklı üstlenmesi gerekir.","neighbor_ref":"root_000661/B004","relation_type":"near_neighbor","shared_zone":"İki dalda da bilgi edinmeye dönük soru yöneltme eylemi bulunur."},{"boundary_match":"partial","distinction":"Odak dal yalın bir sorma veya isteme eylemini adlandırır. Komşu dal bu eyleme süreklilik, şiddet ve muhatap üzerinde baskı kuran ısrar özelliklerini ekler.","focus_only":"Sorma veya isteme, herhangi bir yineleme ya da baskı derecesi gerektirmez.","gloss":"istemek ile ısrarla istemek","neighbor_only":"İstekte ısrar, yineleme ve muhatabı bunaltacak ölçüde baskı bulunur.","neighbor_ref":"root_001346/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir isteğin başka bir kişiye yöneltilmesini içerir."},{"boundary_match":"partial","distinction":"Odak dalda kişi isteğini sözlü ve açık biçimde muhataba yöneltir. Komşu dalda ise kişi iyilik umarak kendini gösterir veya beklentisini açık bir soru ya da istek kurmadan belli eder.","focus_only":"Bir muhataba açıkça soru ya da istek yöneltmeyi gerektirir.","gloss":"açıkça istemek ile beklentiyle görünmek","neighbor_only":"Bir iyilik umarak kendini gösterme veya açıkça istemeden beklenti içinde bulunma biçiminde gerçekleşebilir.","neighbor_ref":"root_000999/B004","relation_type":"near_neighbor","shared_zone":"İki dalda da bir başkasından yarar veya yardım elde etme yönelişi bulunabilir."}],"source_phrase_ar":"سأل يسأل سؤالا ومسألة (maqayis;ayn)؛ سألته الشيء وسألته عن الشيء سؤالا ومسألة (sihah)؛ خرجنا نسأل عن فلان وبفلان (sihah)؛ رجل سؤلة كثير السؤال (maqayis;sihah)؛ الفقير يسمى سائلا (ayn)","source_summary":"Kaynaklar sorma ve isteme eylemlerini birlikte verir; doğrudan nesneli kullanımda bir şey istenirken, bir konu veya kişi hakkında kurulan kullanımda bilgi aranır. Eylem adı, çok soran kimse ve yardım isteyen kişi de aynı tanıklık kümesinde yer alır.","sources":["MQ","AY","SI"],"what_is_ar":"يدخل فيه السؤال والطلب، والسؤال عن الشيء أو بفلان أو عن فلان، والأمر سل واسأل، والسائل والسؤلة وكثرة السؤال.","what_is_not_ar":"لا يدخل فيه التسويل وتزيين النفس، ولا البيت الذي نص المصدر على أنه ليس من سأل."},"support_links":["sup_8bf3197d0d7a31cd678b"]},{"boundary":"Kapsam, kişi tarafından istenmiş olan şeyle sınırlıdır; henüz istek olarak ortaya konmamış dilek ve isteme eyleminin kendisi kapsam dışındadır.","branch_kind":"bare","branch_ref":"root_000661/B002","candidate_links":[{"candidate_id":"cand_145e2f3d536b70286c80","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَآئِل","morph_features":"STEM|POS:N|ACT|PCPL|LEM:saA^}il|ROOT:sAl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:10:2:2","qac_word_ref":"93:10:2","surface_ar":"سَّآئِلَ"}],"gloss":"istenen şey","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin isteme eylemine konu ettiği şeyi veya karşılanmasını istediği içeriği belirtir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dileğe yaklaşır, fakat yalnızca tasarlanan olasılığı değil, kişi tarafından istek olarak ortaya konmuş şeyi anlatır."}}],"root_ar":"س ء ل","root_id":"root_000661","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin açıkça istediği nesne, sonuç veya karşılanacak içerik için dalın tamamını doğal ve kısa biçimde karşılar.","boundary_detail":"Kapsam, kişi tarafından istenmiş olan şeyle sınırlıdır; henüz istek olarak ortaya konmamış dilek ve isteme eyleminin kendisi kapsam dışındadır.","branch_image_ar":"السُّؤل المطلوب","concept_gloss":"istenen şey","contextual_glosses":[{"applicability":"Sahiplik ekiyle bir kişinin elde etmek ya da gerçekleşmesini görmek istediği şey anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiye bağlı, gerçekleşmesi veya verilmesi istenen içeriği doğal biçimde korur."},"facet_ids":["F001"],"text":"isteği","usage_role":"contextual"},{"applicability":"Dilekle yakınlığın yanında, dileğin açık bir isteğe dönüşmüş olduğu özellikle belirtilmek istendiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dileğe yakınlığı ve bunun yalnızca tasarı olarak kalmayıp istek konusu olmasını birlikte korur."},"facet_ids":["F002"],"text":"istenmiş dilek","usage_role":"explanatory"}],"definition":"Bir insanın istediği, kendisine verilmesini ya da gerçekleşmesini talep ettiği şeydir. Bir dileğe yakın olabilir, ancak burada belirleyici olan onun gerçekten istenmiş olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin isteme eylemine konu ettiği şeyi veya karşılanmasını istediği içeriği belirtir."},{"facet_id":"F002","role":"source_variant","statement":"Dileğe yaklaşır, fakat yalnızca tasarlanan olasılığı değil, kişi tarafından istek olarak ortaya konmuş şeyi anlatır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Henüz bir kimseden istenmemiş, yalnızca zihinde tasarlanmış arzuları da kapsar.","collision":null,"fit":"broadening","loses":null,"preserves":"Bir şeyin gerçekleşmesine yönelik arzu ve beklenti yönünü korur."},"text":"dilek"}],"identity_rationale":"Kaynak ifadesi dalı, bir insanın gerçekten istediği şey olarak tanımlar ve onu yalnızca zihinde tasarlanan bir dilekten ayırır. Bu nedenle dalın kimliği isteme eylemi değil, isteğin yöneldiği nesne veya karşılanması beklenen içeriktir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir kimsenin istediği şey"}],"lexicalization_note":"Tanım, herhangi bir özel kalıba bağlı olmadan, kişi tarafından istenen şeyi yalın dal anlamı olarak verir.","neighbor_coverage_note":"Adayların tümü değerlendirildi; açıkça istenmiş olma koşulunu dilek, gereksinim ve isteme eyleminden ayıran dört karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal için belirleyici sınır, içeriğin kişi tarafından istenmiş olmasıdır. Komşu dal ise kişinin içinde duyduğu gereksinim ve dilek yönünü daha güçlü taşır; bu yüzden her bağlamda açıkça yöneltilmiş bir istek gerektirmez.","focus_only":"Şeyin bir kişi tarafından gerçekten istek konusu yapılmış olmasını gerektirir.","gloss":"istenen şey ile gönülden arzulanan şey","neighbor_only":"İçten duyulan gereksinim ve yoğun arzu yönünü, açık bir istekten bağımsız olarak öne çıkarabilir.","neighbor_ref":"root_000763/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin elde etmeyi veya gerçekleşmesini görmeyi arzuladığı içeriği belirtir."},{"boundary_match":"partial","distinction":"Odak dal arzunun yöneldiği ve gerçekten istenmiş olan şeyi adlandırır; komşu dal ise o şeyin gerçekleşmesini arzulama eylemidir. Nesne ile zihinsel yöneliş birbirinin yerine geçmez.","focus_only":"Bir şeyin istek konusu yapılmış nesne veya içerik olmasını belirtir.","gloss":"istenen şey ile dilemek","neighbor_only":"Bir şeyin gerçekleşmesini arzulama eylemini, bunun istenmiş bir nesneye dönüşmesini gerektirmeden belirtir.","neighbor_ref":"root_001634/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da henüz elde bulunmayan bir şeyin gerçekleşmesine yönelen arzu vardır."},{"boundary_match":"partial","distinction":"İstenen her şey bir gereksinim değildir; kişi zorunlu olmayan bir şeyi de isteyebilir. Komşu dal ise eksikliği ve karşılanma zorunluluğunu merkeze alır.","focus_only":"İstenen şeyin zorunlu ya da ivedi olmasını gerektirmez.","gloss":"istenen şey ile gereksinim","neighbor_only":"Eksiklik, zorunluluk ve kimi kullanımlarda güçlü bir giderilme baskısı taşır.","neighbor_ref":"root_000024/B001","relation_type":"near_neighbor","shared_zone":"Bir kişinin elde etmeyi veya gidermeyi istediği içerik iki dalda da bulunabilir."},{"boundary_match":"partial","distinction":"Odak dal isteğin içeriğidir; komşu dal ise kişinin o içeriği elde etmek için gerçekleştirdiği eylemdir. Aynı olayda birlikte bulunmaları anlam bakımından özdeş oldukları anlamına gelmez.","focus_only":"İsteme eyleminin hedefindeki nesneyi veya sonucu adlandırır.","gloss":"istenen şey ile isteme eylemi","neighbor_only":"Bir muhataba yöneltilen sorma ya da isteme eylemini adlandırır.","neighbor_ref":"root_000661/B001","relation_type":"near_neighbor","shared_zone":"Her ikisi de aynı istek olayının farklı parçalarını kavramlaştırır."}],"source_phrase_ar":"السؤل ما يسأله الإنسان (sihah)؛ السؤل يقارب الأمنية والسؤل فيما طلب (mufradat)","source_summary":"Kaynaklar kavramı insanın istediği şey olarak tanımlar. Dilekle ortak bir arzu alanı bulunsa da, bu dalın ayırıcı sınırı söz konusu şeyin kişi tarafından gerçekten istenmiş olmasıdır.","sources":["SI","MU"],"what_is_ar":"يدخل فيه السؤل بوصفه ما يطلبه الإنسان، وقربه من الأمنية مع فرق الطلب، والمسألة أو الحاجة المطلوبة.","what_is_not_ar":"لا يدخل فيه الأمنية المجردة التي لم تصر طلبا."},"support_links":["sup_d20a828d3bafbe44bdf2"]},{"boundary":"Anlam yalnızca tanıklanan türemiş kuruluşta geçerlidir ve bir başkasının isteğini karşılama eylemiyle sınırlıdır.","branch_kind":"non_bare","branch_ref":"root_000661/B003","candidate_links":[{"candidate_id":"cand_145e2f3d536b70286c80","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَآئِل","morph_features":"STEM|POS:N|ACT|PCPL|LEM:saA^}il|ROOT:sAl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:10:2:2","qac_word_ref":"93:10:2","surface_ar":"سَّآئِلَ"}],"gloss":"birinin isteğini yerine getirmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin isteğini yerine getirerek onun gereksinimini karşılamayı bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Karşılama anlamı, genel sorma eylemine değil, kaynakta tanıklanan türemiş ifadeye özgüdür."}}],"root_ar":"س ء ل","root_id":"root_000661","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tanıklanan türemiş kuruluşta, başka bir kişinin istediği şeyi yapma veya gereksinimini karşılama anlamının tamamı için uygundur.","boundary_detail":"Anlam yalnızca tanıklanan türemiş kuruluşta geçerlidir ve bir başkasının isteğini karşılama eylemiyle sınırlıdır.","branch_image_ar":"قضاء المسألة","concept_gloss":"birinin isteğini yerine getirmek","contextual_glosses":[{"applicability":"İstenen şeyin belirli bir nesneden çok kişinin giderilecek gereksinimi olarak sunulduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir başkasındaki eksikliği gidermeyi ve onun beklediği sonucu sağlamayı korur."},"facet_ids":["F001"],"text":"gereksinimini karşılamak","usage_role":"contextual"}],"definition":"Bir başkasının istediği şeyi yapmak, ona gerekeni sağlamak ve böylece isteğini veya gereksinimini karşılamaktır. Bu anlam genel kök anlamı değil, tanıklanan türemiş kuruluşun özel işlevidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin isteğini yerine getirerek onun gereksinimini karşılamayı bildirir."},{"facet_id":"F002","role":"specialization","statement":"Karşılama anlamı, genel sorma eylemine değil, kaynakta tanıklanan türemiş ifadeye özgüdür."}],"identity_rationale":"Kaynak ifadesi belirli bir türemiş kuruluşu, başka bir kişinin isteğini veya gereksinimini karşılamak anlamında açıkça tanımlar. Dal, istekte bulunma eylemini ya da istenen şeyi değil, isteğe cevap veren kişinin gerçekleştirdiği karşılama sonucunu merkez alır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"birinin isteğini veya gereksinimini karşılamak"}],"lexicalization_note":"Tanım kökün genel anlamına yayılmaz; yalnızca tanıklanan türemiş ifadede bir başkasının isteğini veya gereksinimini karşılama anlamını verir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; isteği karşılama çekirdeğini verme, yeterli gelme ve istekte bulunma eylemlerinden ayıran dört ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal isteğin veya gereksinimin karşılanmasını genel sonuç olarak anlatır. Komşu dal ise bunu özellikle istenen şeyi verme ya da sağlayarak yardım etme biçiminde gerçekleştirir.","focus_only":"İsteği, yalnızca bir nesne vermekle sınırlı olmadan yerine getirmeyi kapsar.","gloss":"isteğini yerine getirmek ile istediğini vermek","neighbor_only":"İsteyene istediği şeyi verme veya onu istenen nesneyle donatma yönünü özellikle belirtir.","neighbor_ref":"root_000943/B004","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir istekte bulunana olumlu cevap verilip istediği sonuç sağlanır."},{"boundary_match":"partial","distinction":"Odak dalda bir kişi diğerinin isteğini yerine getirir; komşu dalda ise bir şeyin yeterliliği merkezdedir ve mutlaka istek üzerine davranan bir sağlayıcı bulunmaz.","focus_only":"Bir kişinin başka birinin isteğine karşılık veren eylemini gerektirir.","gloss":"isteği karşılamak ile yeterli gelmek","neighbor_only":"Bir şeyin yeterli gelmesi ve kişiyi başka bir şeye gereksinim duymaktan kurtarması durumunu belirtir.","neighbor_ref":"root_000241/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir gereksinimin giderilmesi ve eksikliğin sona ermesi sonucu bulunabilir."},{"boundary_match":"partial","distinction":"Odak dal, istek ya da gereksinimin farklı yollarla yerine getirilmesini kapsar. Komşu dalın çekirdeği ise soran kişiye somut olarak bir şey vermektir.","focus_only":"İsteğin bir eylem yapılarak veya gereksinim giderilerek karşılanmasını da kapsar.","gloss":"isteği karşılamak ile isteneni vermek","neighbor_only":"Sorana belirli bir şeyi verme eylemiyle sınırlıdır.","neighbor_ref":"root_001403/B004","relation_type":"near_neighbor","shared_zone":"İki dalda da bir kişinin istemesine karşılık ona olumlu bir sonuç sağlanır."},{"boundary_match":"thematic_only","distinction":"Dallar aynı olayın farklı katılımcı evrelerini gösterir: komşu dal isteğin yöneltilmesidir, odak dal ise istenen sonucun sağlanmasıdır. Biri gerçekleşmeden ötekinin anlamı varsayılmaz.","focus_only":"İsteğe cevap veren kişinin gereksinimi gideren eylemini anlatır.","gloss":"istemek ile isteği karşılamak","neighbor_only":"İsteyen kişinin muhataba yönelttiği sorma veya isteme eylemini anlatır.","neighbor_ref":"root_000661/B001","relation_type":"thematic","shared_zone":"Aynı istek olayında biri talepte bulunurken diğeri bu talebe cevap verebilir."}],"source_phrase_ar":"أسألته سؤلته ومسألته أي قضيت حاجته (sihah)","source_summary":"Tek kaynaklı tanıklık, türemiş ifadeyi bir başkasının isteğini veya gereksinimini karşılama şeklinde açıklar. Bu, talepte bulunanın eyleminden ayrı olarak, talebe cevap veren kişinin gerçekleştirdiği sonuçlu eylemdir.","sources":["SI"],"what_is_ar":"يدخل فيه أسألته سؤلته ومسألته بمعنى قضيت حاجته.","what_is_not_ar":"لا يدخل فيه طلب السائل نفسه ولا مجرد تسمية المطلوب سؤلا."},"support_links":["sup_d20a828d3bafbe44bdf2"]},{"boundary":"Dal karşılıklı soru yöneltmeyi gerektirir; tek kişinin başkasına yönelttiği ve karşı taraftan soru gelmeyen kullanım genel sorma dalında kalır.","branch_kind":"bare","branch_ref":"root_000661/B004","candidate_links":[{"candidate_id":"cand_7f620634b137107139cb","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَآئِل","morph_features":"STEM|POS:N|ACT|PCPL|LEM:saA^}il|ROOT:sAl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:10:2:2","qac_word_ref":"93:10:2","surface_ar":"سَّآئِلَ"}],"gloss":"birbirine soru sormak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birden çok katılımcının birbirlerine soru yöneltmesini ve soru rollerini karşılıklı üstlenmesini bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylem, yalnızca aynı ortamda soru sorulmasını değil, soruların katılımcılar arasında karşılıklı yönelmesini gerektirir."}}],"root_ar":"س ء ل","root_id":"root_000661","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki veya daha çok katılımcının soruları karşılıklı olarak birbirlerine yönelttiği dal çekirdeğinin tamamı için uygundur.","boundary_detail":"Dal karşılıklı soru yöneltmeyi gerektirir; tek kişinin başkasına yönelttiği ve karşı taraftan soru gelmeyen kullanım genel sorma dalında kalır.","branch_image_ar":"السؤال المتبادل","concept_gloss":"birbirine soru sormak","contextual_glosses":[{"applicability":"Katılımcıların birbirlerinden bilgi almak amacıyla sırayla veya karşılıklı soru yönelttiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı soru yöneltmeyi ve bu yolla bilgi edinme amacını bağlam içinde korur."},"facet_ids":["F001","F002"],"text":"karşılıklı sorup öğrenmek","usage_role":"contextual"}],"definition":"İki veya daha çok kişinin birbirlerine soru yöneltmesi, böylece her birinin ötekine göre soran ve kendisine sorulan konumlarına girmesidir. Yalnızca tek yönlü bir soru bu karşılıklılık koşulunu karşılamaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birden çok katılımcının birbirlerine soru yöneltmesini ve soru rollerini karşılıklı üstlenmesini bildirir."},{"facet_id":"F002","role":"specialization","statement":"Eylem, yalnızca aynı ortamda soru sorulmasını değil, soruların katılımcılar arasında karşılıklı yönelmesini gerektirir."}],"identity_rationale":"Kaynak ifadesi, bir topluluğun üyelerinin birbirlerine soru yöneltmesini açıkça bildirir. Karşılıklılık yalnızca aynı ortamda birden çok soru bulunması değildir; katılımcıların soran ve kendisine sorulan rollerini birbirlerine göre üstlenmesi dalın kurucu özelliğidir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"birbirlerine soru sormak"}],"lexicalization_note":"Tanım, tanıklanan biçimin yalın dal anlamını karşılıklı soru yöneltme olarak verir ve başka konuşma alışverişlerini bu anlama katmaz.","neighbor_coverage_note":"Tüm adaylar incelendi; karşılıklı soru koşulunu genel sorma, görüşme, cevaplaşma ve sırayla konuşmadan ayıran dört komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genel sormaya karşılıklılık koşulu ekler: katılımcılar birbirlerine soru yöneltir. Komşu dalda tek bir soranın tek yönlü eylemi anlamın kurulması için yeterlidir.","focus_only":"Katılımcıların birbirlerine soru yöneltmesini ve rollerin karşılıklı olmasını gerektirir.","gloss":"birbirine sormak ile sormak","neighbor_only":"Tek yönlü soru veya istek için karşı taraftan benzer bir yöneliş gerektirmez.","neighbor_ref":"root_000661/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalın merkezinde bir muhataba soru yöneltme eylemi vardır."},{"boundary_match":"partial","distinction":"Odak dalda tarafların birbirlerine soru yöneltmesi zorunludur. Komşu dal karşılıklı konuşma ve bir konuyu birlikte ele alma sürecidir; soru-cevap yapısı onun kurucu koşulu değildir.","focus_only":"Karşılıklı eylemin birimleri özellikle sorulardır.","gloss":"birbirine sormak ile görüşmek","neighbor_only":"Katılımcıların bir konu üzerinde birlikte ilerlemesi, konuşması veya görüş alışverişi yapması soru bulunmadan da gerçekleşebilir.","neighbor_ref":"root_001187/B005","relation_type":"near_neighbor","shared_zone":"İki dal da birden çok konuşanın aynı konuda karşılıklı iletişim kurmasını içerir."},{"boundary_match":"partial","distinction":"Odak dalın kurucu eylemi sorudur ve karşılıklılık soruların yönünde bulunur. Komşu dal ise verilen cevabı, sözün geri çevrilmesini ve daha geniş diyalog sürecini kapsar.","focus_only":"Her katılımcının ötekine soru yöneltmesini öne çıkarır.","gloss":"karşılıklı sormak ile cevaplaşmak","neighbor_only":"Söze, soruya veya çağrıya cevap vermeyi ve konuşmanın geri dönüşünü öne çıkarır.","neighbor_ref":"root_000273/B003","relation_type":"near_neighbor","shared_zone":"Her ikisi de konuşanlar arasında gidip gelen söz ve bilgi alışverişi içinde gerçekleşir."},{"boundary_match":"field_only","distinction":"Odak dal soru türünü ve karşılıklı yönelmeyi tanımlar; komşu dal konuşma sırasının el değiştirmesini tanımlar. Karşılıklı sorular eşzamanlı bir alışverişte bulunabilir, sırayla konuşma ise sorusuz da olabilir.","focus_only":"Söz sırasından bağımsız olarak katılımcıların birbirlerine soru yöneltmesini gerektirir.","gloss":"karşılıklı sorma ile sırayla konuşma","neighbor_only":"Bir konuşanın susup ötekinin konuşmasına dayalı sıra değişimini anlatır; söylenenlerin soru olması gerekmez.","neighbor_ref":"root_000719/B014","relation_type":"same_field","shared_zone":"İki dal da birden çok kişinin söz alıp birbirine yöneldiği konuşma alanındadır."}],"source_phrase_ar":"تساءلوا أي سأل بعضهم بعضا (sihah)","source_summary":"Tek kaynaklı tanıklık, biçimi kişilerin birbirlerine soru sorması olarak açıklar. Bu açıklama, genel soru eylemine karşılıklı katılım ve rollerin katılımcılar arasında değişmesi koşulunu ekler.","sources":["SI"],"what_is_ar":"يدخل فيه تساءلوا أي سأل بعضهم بعضا.","what_is_not_ar":"لا يدخل فيه سؤال الواحد لغيره من غير مقابلة."},"support_links":["sup_71f2d85ce6878ed9ad8b"]},{"boundary":"Dal, izinli ya da izinsiz almaya değil, ayırıp çıkarma biçimine odaklanır.","branch_kind":"mixed_non_bare","branch_ref":"root_000736/B001","candidate_links":[{"candidate_id":"cand_bbfa194f69a0f03b8698","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَآئِل","morph_features":"STEM|POS:N|ACT|PCPL|LEM:saA^}il|ROOT:sAl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:10:2:2","qac_word_ref":"93:10:2","surface_ar":"سَّآئِلَ"}],"gloss":"nazikçe ve fark ettirmeden çekip çıkarma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesneyi bağlı veya kapalı bulunduğu yerden çekerek ayırıp çıkarma işlemi vardır."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kılıcın kınından çekilmesi ve hamurdaki kılın ayıklanması bu işlemin somut örnekleridir."}}],"root_ar":"س ء ل","root_id":"root_000736","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin bulunduğu yerden incelikle ayrılıp çıkarıldığı dalın tamamı için uygundur.","boundary_detail":"Dal, izinli ya da izinsiz almaya değil, ayırıp çıkarma biçimine odaklanır.","branch_image_ar":"السل برفق وخفاء","concept_gloss":"nazikçe ve fark ettirmeden çekip çıkarma","contextual_glosses":[{"applicability":"Nesnenin bir yerden incelikle çıkarıldığı genel eylem bağlamlarında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eylemin fark ettirmeden yapılması koşulunu tek başına açıkça belirtmez.","preserves":"Çekerek çıkarma işlemini ve incelikli yapılış biçimini korur."},"facet_ids":["F001"],"text":"usulca çekip çıkarmak","usage_role":"general"},{"applicability":"Hamurdan kıl gibi istenmeyen bir parçanın ayrıldığı somut ayıklama bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kılıç gibi kapalı bir yerden çekilen nesneleri ve gizlilik özelliğini kapsamaz.","preserves":"Bir parçayı bulunduğu maddeden ayırıp çıkarma işlemini korur."},"facet_ids":["F002"],"text":"ayıklayıp çıkarmak","usage_role":"contextual"}],"definition":"Bir şeyi başka bir şeyin içinden ya da üzerinden nazikçe ve fark ettirmeden çekerek ayırıp çıkarmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesneyi bağlı veya kapalı bulunduğu yerden çekerek ayırıp çıkarma işlemi vardır."},{"facet_id":"F002","role":"example","statement":"Kılıcın kınından çekilmesi ve hamurdaki kılın ayıklanması bu işlemin somut örnekleridir."}],"identity_rationale":"Kaynak ifadesi, bir şeyi bulunduğu yerden nazikçe ve belli etmeden çekip çıkarma eylemini doğrudan verir. Kılıcı kınından çekme ile hamurdan kıl ayıklama bu çekirdek işlemin özel uygulamalarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi çekip çıkarmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kılıcı kınından çekmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"hamurdaki kılı ayıklayıp çıkarmak"}],"lexicalization_note":"Tanım genel çekip çıkarma eylemini kapsar; kılıç ve hamur kalıplarını bu genel anlamın özel uygulamaları olarak ayrı tutar.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; en keskin sınırı, genel çekip çıkarma ile kılıca özgü çıkarma arasındaki ayrım verdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal kılıç ve kın ilişkisine özgüdür; odak dal ise aynı çıkarma düzenini hamurdaki kıl gibi başka nesnelere de uygular.","focus_only":"Her tür nesnenin bulunduğu maddeden ya da kaptan incelikle çıkarılmasını kapsar.","gloss":"kılıcı kınından çekme","neighbor_only":"Yalnızca kılıcın kınından çekilmesini adlandırır.","neighbor_ref":"root_001420/B020","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir nesne, içinde bulunduğu kapalı yerden çekilerek çıkarılır."}],"source_phrase_ar":"سللت الشيء أسله سلا (maqayis;sihah;tahdhib)؛ إخراجك الشعر من العجين (ayn;tahdhib)؛ سل الشيء من الشيء نزعه (mufradat)","source_summary":"Kaynakların ortak çekirdeği, bir şeyi başka bir şeyden çekerek çıkarmadır; anlatım bu işlemin incelikli ve gizli yapılabildiğini de korur.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه نزع الشيء من غيره وإخراجه برفق وخفاء كسل السيف من الغمد وسل الشعر من العجين","what_is_not_ar":"ليس السرقة ولا الولد ولا المرض ولا السلسلة ولا الماء السلس"},"support_links":["sup_c57219c5168b9007bb0d"]},{"boundary":"Dal, sıradan çekip çıkarmadan suç amacı ve gizlilik koşuluyla ayrılır.","branch_kind":"mixed_non_bare","branch_ref":"root_000736/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَآئِل","morph_features":"STEM|POS:N|ACT|PCPL|LEM:saA^}il|ROOT:sAl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:10:2:2","qac_word_ref":"93:10:2","surface_ar":"سَّآئِلَ"}],"gloss":"gizlice çalma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Alma eylemi gizli yapılır ve hırsızlık niteliği taşır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kaynak birleşiminde aynı biçim hırsızlığın yanında rüşvetle de ilişkilendirilir."}}],"root_ar":"س ء ل","root_id":"root_000736","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gizlilik ve hırsızlık amacı taşıyan alma eyleminin çekirdek karşılığıdır.","boundary_detail":"Dal, sıradan çekip çıkarmadan suç amacı ve gizlilik koşuluyla ayrılır.","branch_image_ar":"الإسلال الخفي","concept_gloss":"gizlice çalma","contextual_glosses":[{"applicability":"Bir şeyin evden hırsızlık yoluyla alındığı açık bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ev dışındaki gizli hırsızlık bağlamlarını kapsam dışında bırakır.","preserves":"Gizli alma eylemini ve hırsızlık amacını eksiksiz korur."},"facet_ids":["F001"],"text":"evden gizlice çalmak","usage_role":"contextual"},{"applicability":"İki kullanımın birlikte bildirildiği özel biçimi açıklamak için uygundur.","error_profile":{"adds":"Dalın genel çekirdeğinde zorunlu olmayan rüşvet kullanımını ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Gizli hırsızlık çekirdeğini ve bildirilen yan kullanımı birlikte gösterir."},"facet_ids":["F001","F002"],"text":"gizli hırsızlık veya rüşvet","usage_role":"explanatory"}],"definition":"Bir şeyi, özellikle bir evden, gizlice ve hırsızlık amacıyla almaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Alma eylemi gizli yapılır ve hırsızlık niteliği taşır."},{"facet_id":"F002","role":"source_variant","statement":"Bir kaynak birleşiminde aynı biçim hırsızlığın yanında rüşvetle de ilişkilendirilir."}],"identity_rationale":"Kaynak ifadesi dalı açıkça gizli hırsızlık ve evden hırsızlık amacıyla alma olarak tanımlar. Rüşvet yalnızca bir biçimin ek kullanımında geçer ve dalın hırsızlık çekirdeğini değiştirmez.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"hırsızlık; gizli hırsızlık"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"gizli hırsızlık; ayrıca rüşvet"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"çalmak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"hırsız"}],"lexicalization_note":"Tanım türemiş biçimlerdeki gizli hırsızlık alanına bağlıdır; bu alan yalın çekip çıkarma anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; gizli hırsızlık ile hızlı kapıp alma karşıtlığı okuyucu için en yararlı sınırı sağlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ayırıcı koşulu gizliliktir; komşu dalda belirleyici özellik hızlı kapma veya zorlayıcı biçimde el koymadır.","focus_only":"Hırsızlığı gizlilik ve fark ettirmeden alma yönüyle sınırlar.","gloss":"hızla kapıp alma","neighbor_only":"Almayı hız, kapıp kaçma ve kimi zaman zor kullanma yönüyle tanımlar.","neighbor_ref":"root_000423/B001","relation_type":"near_neighbor","shared_zone":"İki dal da başkasına ait bir şeyi izinsiz alma alanında buluşur."}],"source_phrase_ar":"السلة والإسلال السرقة (maqayis)؛ الإسلال السرقة الخفية (ayn;tahdhib)؛ الإسلال الرشوة والسرقة (sihah)؛ سل الشيء من البيت على سبيل السرقة (mufradat)","source_summary":"Ortak anlatım gizli hırsızlığı merkeze alır; birleşik kaynak ifadesi, bir biçim için rüşvetle bağlantılı daha geniş bir kullanımı da bildirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه السلة والإسلال بمعنى السرقة الخفية وما قاربها من أخذ الشيء من البيت على وجه السرقة","what_is_not_ar":"ليس مجرد النزع المباح ولا الخروج من الزحام ولا المرض"},"support_links":[]},{"boundary":"Ortaklık, bir kökenden çıkmış olma ilişkisidir; kişi soyu ile maddi öz birbirine eşitlenmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000736/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَآئِل","morph_features":"STEM|POS:N|ACT|PCPL|LEM:saA^}il|ROOT:sAl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:10:2:2","qac_word_ref":"93:10:2","surface_ar":"سَّآئِلَ"}],"gloss":"kökenden çıkan yavru veya öz","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığın kendi kökeninden çıkması veya ondan türemesi temel ilişkidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsan çocuğu ile erkek ve dişi at yavrusu, canlı kökenden çıkan varlıklar olarak adlandırılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir şeyden çekilip alınan öz ve insanın üreme maddesi aynı köken ilişkisine dayalı maddi kullanımlardır."}}],"root_ar":"س ء ل","root_id":"root_000736","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Canlı soy ile bir ana maddeden ayrılmış özü ortak köken ilişkisi altında birlikte karşılar.","boundary_detail":"Ortaklık, bir kökenden çıkmış olma ilişkisidir; kişi soyu ile maddi öz birbirine eşitlenmez.","branch_image_ar":"السلالة المستلة","concept_gloss":"kökenden çıkan yavru veya öz","contextual_glosses":[{"applicability":"Bir insanın doğrudan çocuğunun kökenden çıkışı vurgulandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvan yavrusunu ve bir maddeden ayrılan öz kullanımını kapsamaz.","preserves":"Canlı kökenden doğan insan yavrusu ilişkisini korur."},"facet_ids":["F001","F002"],"text":"soyundan gelen çocuk","usage_role":"contextual"},{"applicability":"Erkek ya da dişi at yavrusunun adlandırıldığı hayvan bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsan çocuğunu ve maddi öz kullanımını kapsam dışı bırakır.","preserves":"At yavrusunun canlı kökeninden çıkması ilişkisini korur."},"facet_ids":["F001","F002"],"text":"tay veya kısrak yavrusu","usage_role":"contextual"},{"applicability":"Bir ana maddeden çekilip alınan öz veya üreme maddesi anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çocuk ve hayvan yavrusu anlamlarını kapsam dışı bırakır.","preserves":"Bir kökenden ayrılarak çıkan maddi özü korur."},"facet_ids":["F001","F003"],"text":"kök maddeden ayrılan öz","usage_role":"explanatory"}],"definition":"Bir kökenden çıkan çocuk ya da yavruyu veya bir ana maddeden çekilip ayrılan özü anlatır; ortak çekirdek, kökenden ayrılarak meydana gelmedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığın kendi kökeninden çıkması veya ondan türemesi temel ilişkidir."},{"facet_id":"F002","role":"specialization","statement":"İnsan çocuğu ile erkek ve dişi at yavrusu, canlı kökenden çıkan varlıklar olarak adlandırılır."},{"facet_id":"F003","role":"extension","statement":"Bir şeyden çekilip alınan öz ve insanın üreme maddesi aynı köken ilişkisine dayalı maddi kullanımlardır."}],"identity_rationale":"Kaynak ifadesi çocuk ve hayvan yavrusunu, ayrıca bir kökten çekilip alınan öz ya da üreme maddesini aynı çıkış ilişkisi altında toplar. Dal kullanılabilir, ancak bütün öğelerin doğrudan soy anlamına gelmediği açıkça belirtilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"oğul; çocuk"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kız evlat"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"tay ve dişi tay"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kökten ayrılan öz; üreme maddesi"}],"lexicalization_note":"Tanım türemiş adların kökenden çıkma ortaklığını verir; yavru ve maddi öz kullanımlarını ayrı alt alanlar olarak korur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; çocuk ve soy alanındaki yakın komşu, maddi öz uzantısını görünür kıldığı için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kökenden çekilip çıkmış tek yavruyu ve maddi özü öne çıkarır; komşu dal soyun çoğalması ve kuşaklar boyunca sürmesiyle daha geniştir.","focus_only":"Canlı yavrunun yanında bir ana maddeden ayrılan özü de kapsar.","gloss":"çocuk ve devam eden soy","neighbor_only":"Soyun kuşaklar boyunca sürmesi ve üreme amacıyla yetiştirilen hayvanları da kapsar.","neighbor_ref":"root_001499/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir canlıdan doğan çocuk veya yavruyu ve soy ilişkisini içerir."}],"source_phrase_ar":"السليل الولد (maqayis;sihah;tahdhib)؛ السلالة ما استل منه والنطفة سلالة الإنسان (sihah;tahdhib;mufradat)؛ السليل والسليلة المهر والمهرة (ayn;tahdhib)","source_summary":"Birleşik kaynak anlatımı, çocuk ve yavru ile kök maddeden ayrılan öz arasında kökenden çıkma bağı kurar; canlı soy ve maddi öz kapsamları ayrı tutulur.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه السليل والولد والسليلة وسلالة الشيء والنطفة وما يسل من أصل أو مادة","what_is_not_ar":"ليس السرقة ولا المرض ولا السلسلة المتصلة"},"support_links":[]},{"boundary":"Dal, elde tutulan bir nesneyi çıkarmayı değil, hareket eden öznenin aradan ayrılmasını anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000736/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَآئِل","morph_features":"STEM|POS:N|ACT|PCPL|LEM:saA^}il|ROOT:sAl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:10:2:2","qac_word_ref":"93:10:2","surface_ar":"سَّآئِلَ"}],"gloss":"aradan sıyrılıp çıkma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hareket eden özne, çevresindeki sıkışık yerden ya da topluluktan dışarı çıkar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Topluluktan gizlice ve başkasını siper ederek ayrılma, çıkışın özel bir gerçekleşmesidir."}}],"root_ar":"س ء ل","root_id":"root_000736","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dar bir yerden veya topluluğun arasından hareket ederek ayrılma çekirdeğini doğal biçimde karşılar.","boundary_detail":"Dal, elde tutulan bir nesneyi çıkarmayı değil, hareket eden öznenin aradan ayrılmasını anlatır.","branch_image_ar":"الانسلال خروجا","concept_gloss":"aradan sıyrılıp çıkma","contextual_glosses":[{"applicability":"Bir kişinin insanların arasından çıkıp uzaklaştığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsan bulunmayan dar yerlerden çıkma kapsamını içermez.","preserves":"İnsanların arasından akıcı biçimde çıkma eylemini korur."},"facet_ids":["F001"],"text":"kalabalığın arasından sıyrılmak","usage_role":"contextual"},{"applicability":"Bir topluluktan fark ettirmeden uzaklaşma bağlamında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dar yerden açık biçimde çıkma ve aradan sıyrılma kapsamını daraltır.","preserves":"Topluluktan gizlice çıkıp gitme özelliğini korur."},"facet_ids":["F002"],"text":"gizlice ayrılmak","usage_role":"contextual"}],"definition":"Bir öznenin dar bir yerden, kalabalıktan veya insanların arasından sıyrılarak çıkıp gitmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hareket eden özne, çevresindeki sıkışık yerden ya da topluluktan dışarı çıkar."},{"facet_id":"F002","role":"specialization","statement":"Topluluktan gizlice ve başkasını siper ederek ayrılma, çıkışın özel bir gerçekleşmesidir."}],"identity_rationale":"Kaynak ifadesi, dar bir yerden, kalabalıktan veya insanların arasından çıkıp gitmeyi açıkça bildirir. Gizlice ve siperlenerek ayrılma, bu çıkışın bağlamsal yapılış biçimidir.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"dar yerden veya kalabalıktan sıyrılıp çıkma"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"aralarından çıkmak"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"topluluktan gizlice ayrılma"}],"lexicalization_note":"Tanım türemiş çıkış biçimlerini ve insanlar arasından çıkma kalıbını birlikte kapsar; bunları genel nesne çıkarma anlamıyla karıştırmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; genel dışarı çıkma dalı, bu dalın aradan sıyrılma koşulunu en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel çıkışı bildirir; odak dal çıkışın sıkışık bir aralıktan veya topluluğun içinden sıyrılarak gerçekleşmesini şart koşar.","focus_only":"Dar bir yerden veya insanların arasından sıyrılarak çıkmayı gerektirir.","gloss":"dışarı çıkma","neighbor_only":"Her türlü yerden, durumdan ya da konumdan dışarı çıkmayı kapsar.","neighbor_ref":"root_000400/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir özne bulunduğu iç konumdan dışarıya geçer."}],"source_phrase_ar":"الانسلال المضي والخروج من بين مضيق أو زحام (ayn;tahdhib)؛ انسل من بينهم أي خرج (sihah)؛ يتسللون منكم لواذا (tahdhib;mufradat)","source_summary":"Kaynaklar dar yerden veya insanların arasından çıkıp gitme üzerinde birleşir; topluluktan gizlice ayrılma bu çekirdeğin özel biçimidir.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الانسلال والتسلل بمعنى الخروج والمضي من مضيق أو زحام أو من بين القوم","what_is_not_ar":"ليس نزع الشيء باليد ولا السرقة ولا السلسلة"},"support_links":[]},{"boundary":"Dal akıcı suyu değil, parçalar arasında görülen bağlantı ve dizilişi anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000736/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَآئِل","morph_features":"STEM|POS:N|ACT|PCPL|LEM:saA^}il|ROOT:sAl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:10:2:2","qac_word_ref":"93:10:2","surface_ar":"سَّآئِلَ"}],"gloss":"birbirine bağlı dizi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ayrı parçalar birbirine bağlanır ve bağlantılı bir dizi meydana getirir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Demir halkalardan oluşan zincir, çekirdek bağlantı yapısının belirgin örneğidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bulut boyunca uzanan şimşek ve birbirine eklenip kıvrılan kum çizgileri benzer görsel bağlantıyla adlandırılır."}}],"root_ar":"س ء ل","root_id":"root_000736","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Halkalar, parçalar veya çizgisel bölümlerin bağlantılı bir bütün oluşturduğu dalın tamamına uygulanır.","boundary_detail":"Dal akıcı suyu değil, parçalar arasında görülen bağlantı ve dizilişi anlatır.","branch_image_ar":"السلسلة اتصالا","concept_gloss":"birbirine bağlı dizi","contextual_glosses":[{"applicability":"Birbirine geçmiş demir halkalardan oluşan bilinen nesne için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Şimşek ve kumdaki bağlantılı uzanış gibi benzetmeli uygulamaları kapsamaz.","preserves":"Birbirine bağlı halkalardan oluşan somut diziyi korur."},"facet_ids":["F001","F002"],"text":"zincir","usage_role":"contextual"},{"applicability":"Parçaların bağlantı içinde olduğu genel niteleme bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Parçaların birbirine bağlanması ve bir bütün oluşturması çekirdeğini korur."},"facet_ids":["F001"],"text":"birbirine eklenmiş","usage_role":"general"}],"definition":"Parçaların birbirine bağlanarak ardışık ve uzanan bir bütün oluşturmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ayrı parçalar birbirine bağlanır ve bağlantılı bir dizi meydana getirir."},{"facet_id":"F002","role":"example","statement":"Demir halkalardan oluşan zincir, çekirdek bağlantı yapısının belirgin örneğidir."},{"facet_id":"F003","role":"extension","statement":"Bulut boyunca uzanan şimşek ve birbirine eklenip kıvrılan kum çizgileri benzer görsel bağlantıyla adlandırılır."}],"identity_rationale":"Kaynak ifadesi, parçaların birbirine bağlanarak bir dizi oluşturmasını çekirdek anlam olarak verir. Demir halkalar, uzayan şimşek ve birbirine eklenen kum kıvrımları bu bağlantı düzeninin somutlaşmalarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"zincir; parçaların birbirine bağlanması"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"birbirine bağlı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bulut boyunca uzanan şimşek"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"birbirine eklenen kıvrımlı kum"}],"lexicalization_note":"Tanım genel bağlantı çekirdeğini verir; şimşek ve kum kalıplarını yalnızca bu çekirdeğin özel görüntüleri olarak tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bağlantı ve zincir çekirdeğini tam paylaşan komşu tek doğrudan eş anlamlı olarak yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek sınırlar aynıdır; odak daldaki şimşek ve kum örnekleri, ortak bağlantı anlamının bağımlı uygulamalarıdır.","focus_only":null,"gloss":"bağlı parçalar ve zincir","neighbor_only":null,"neighbor_ref":"root_000731/B002","relation_type":"synonym","shared_zone":"İki dal da zinciri ve parçaların birbirine bağlanarak ardışık bütün oluşturmasını anlatır."}],"source_phrase_ar":"السلسلة اتصال الشيء بالشيء (maqayis)؛ شيء مسلسل متصل بعضه ببعض (sihah)؛ السلسلة معروفة وبرق ذو سلاسل ورمل ذو سلاسل (tahdhib)؛ ومنه السلسلة (mufradat)","source_summary":"Ortak çekirdek, parçaların birbirine bağlı olmasıdır; demir zincir gerçek nesneyi, şimşek ve kum ise bağlantılı uzanışın benzetmeli örneklerini oluşturur.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه السلسلة واتصال الشيء بالشيء والحديد والبرق والرمل المتعقد أو الممتد بعضه ببعض","what_is_not_ar":"ليس الماء العذب الجاري في الحلق ولا السلالة ولا السرقة"},"support_links":[]},{"boundary":"Kavram dalı suyla sınırlıdır; diğer içecek ve özel adlandırma kullanımları çekirdeğe genellenmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000736/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَآئِل","morph_features":"STEM|POS:N|ACT|PCPL|LEM:saA^}il|ROOT:sAl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:10:2:2","qac_word_ref":"93:10:2","surface_ar":"سَّآئِلَ"}],"gloss":"tatlı, duru ve kolay akan su","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Su, boğazdan veya eğimli bir yüzeyden kolay ve kesintisiz biçimde akar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Suyun tatlı ve duru oluşu, içimini kolaylaştıran temel niteliklerdir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir anlatımda su, bulunduğu yerde dönüp dinlenerek durulmuş su olarak açıklanır."}}],"root_ar":"س ء ل","root_id":"root_000736","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Suyun niteliği ile boğazdan veya eğimden rahat akışını birlikte karşılayan tam kavram karşılığıdır.","boundary_detail":"Kavram dalı suyla sınırlıdır; diğer içecek ve özel adlandırma kullanımları çekirdeğe genellenmez.","branch_image_ar":"السلاسة في الجريان","concept_gloss":"tatlı, duru ve kolay akan su","contextual_glosses":[{"applicability":"Suyun içim sırasında boğazdan rahat geçişinin vurgulandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eğimli yerdeki akışı ve durulma yoluyla berraklaşma açıklamasını kapsamaz.","preserves":"Suyun boğazdan kolay akıp geçmesi özelliğini korur."},"facet_ids":["F001","F002"],"text":"boğazdan kolay geçen su","usage_role":"contextual"},{"applicability":"Suyun içim niteliği ve berraklığı öne çıkarıldığında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kolay ve hızlı akış özelliğini açıkça belirtmez.","preserves":"Suyun tatlı ve duru olma niteliklerini korur."},"facet_ids":["F002","F003"],"text":"duru ve tatlı su","usage_role":"general"}],"definition":"Suyun tatlı ve duru olması sayesinde boğazdan zorlanmadan akıp geçmesi veya eğimli yerde kolayca akmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Su, boğazdan veya eğimli bir yüzeyden kolay ve kesintisiz biçimde akar."},{"facet_id":"F002","role":"specialization","statement":"Suyun tatlı ve duru oluşu, içimini kolaylaştıran temel niteliklerdir."},{"facet_id":"F003","role":"source_variant","statement":"Bir anlatımda su, bulunduğu yerde dönüp dinlenerek durulmuş su olarak açıklanır."}],"identity_rationale":"Yetkili kaynak ifadesi suyun boğazdan kolay akmasını ve tatlı, duru olmasını destekler. Geçici çerçevedeki şarap ve özel kaynak adı bu dal claiminde yer almadığından kavram tanımına taşınmamış, yalnızca ayrı sözlüksel birimlerin karşılıklarında korunmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"suyun boğazdan veya eğimden kolayca akması"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"tatlı, duru ve kolay içilen su"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"boğazdan kolay geçen duru şarap"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kolay içilen, lezzetli ve hızlı akan kaynak suyu"}],"lexicalization_note":"Tanım suya ilişkin genel nitelik ile suyun akış kalıbını ayırır; diğer sözlüksel birimlerin özel kapsamını yalın dala katmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; suyun tatlılık, duruluk ve kolay akış özelliklerini tam paylaşan komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Kavram çekirdekleri ve sınırları aynıdır; özel içecek ve adlandırma örnekleri eş anlamlılığı bozan kurucu farklar değildir.","focus_only":null,"gloss":"duru ve kolay içilen su","neighbor_only":null,"neighbor_ref":"root_000731/B001","relation_type":"synonym","shared_zone":"İki dal da tatlı, duru ve boğazdan kolay geçen suyu akış niteliğiyle birlikte tanımlar."}],"source_phrase_ar":"تسلسل الماء في الحلق إذا جرى وماء سلسل وسلسال (maqayis;sihah;tahdhib)؛ السلسل الماء العذب الصافي (ayn;tahdhib)؛ ماء سلسل متردد في مقره حتى صفا (mufradat)","source_summary":"Ortak anlatım kolay akan, tatlı ve duru suyu öne çıkarır; ek açıklama, suyun bulunduğu yerde durularak berraklaşmasını bildirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه تسلسل الماء في الحلق وماء سلسل وسلسال وسلاسل وخمر سلسل وما سهل ولذ وجرى بصفاء","what_is_not_ar":"ليس السلسلة الحديدية ولا اتصال الرمل ولا السرقة"},"support_links":[]},{"boundary":"Dal suyun kendisini değil, vadi içindeki kanal ve çukur arazi biçimlerini adlandırır.","branch_kind":"bare","branch_ref":"root_000736/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَآئِل","morph_features":"STEM|POS:N|ACT|PCPL|LEM:saA^}il|ROOT:sAl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:10:2:2","qac_word_ref":"93:10:2","surface_ar":"سَّآئِلَ"}],"gloss":"vadi içindeki su yolu veya çukur arazi","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Vadi içindeki dar su yolu veya geçit, alanın akışa bağlı arazi biçimidir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Geniş ve belirli çöl ağaçlarının yetiştiği vadi, daha geniş yer biçimi olarak adlandırılır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ağaçlı, gizli ya da çukur arazi tabanları başka bir yer biçimi olarak aynı dalda yer alır."}}],"root_ar":"س ء ل","root_id":"root_000736","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dar kanal ile geniş ya da çukur ağaçlı vadi kesimlerini yer biçimi olarak birlikte karşılar.","boundary_detail":"Dal suyun kendisini değil, vadi içindeki kanal ve çukur arazi biçimlerini adlandırır.","branch_image_ar":"المسال في الوادي","concept_gloss":"vadi içindeki su yolu veya çukur arazi","contextual_glosses":[{"applicability":"Vadi içinde suyun geçtiği dar kanal veya geçit kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Geniş ağaçlı vadiyi ve çukur arazi tabanlarını kapsamaz.","preserves":"Vadi içindeki dar akış yolunu eksiksiz korur."},"facet_ids":["F001"],"text":"vadideki dar su yolu","usage_role":"contextual"},{"applicability":"Geniş vadi ve üzerinde yetişen belirli çöl ağaçları öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dar su yolunu ve diğer çukur arazi tabanlarını kapsamaz.","preserves":"Geniş ve ağaçlı vadi biçimini korur."},"facet_ids":["F002"],"text":"geniş ve ağaçlı vadi","usage_role":"contextual"}],"definition":"Vadi içinde dar bir su yolu ile geniş, alçak ya da çukur ve ağaçlı arazi kesimlerini adlandıran yer biçimi alanıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Vadi içindeki dar su yolu veya geçit, alanın akışa bağlı arazi biçimidir."},{"facet_id":"F002","role":"source_variant","statement":"Geniş ve belirli çöl ağaçlarının yetiştiği vadi, daha geniş yer biçimi olarak adlandırılır."},{"facet_id":"F003","role":"source_variant","statement":"Ağaçlı, gizli ya da çukur arazi tabanları başka bir yer biçimi olarak aynı dalda yer alır."}],"identity_rationale":"Kaynak ifadesi dar bir vadi su yolu, geniş ve belirli ağaçların yetiştiği bir vadi ile ağaçlı çukur arazi biçimlerini birlikte verir. Geçici çerçevedeki suyun mutlaka biriktiği yer genellemesi bütün bu öğeler için desteklenmediğinden tanım arazi biçimleri üzerinden düzeltilmiştir.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"vadide dar su yolu; su toplayan alçak yer"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"vadi içindeki dar su yolları veya ağaçlı çukur yerler"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"geniş ve ağaçlı vadi"}],"lexicalization_note":"Tanım yalnızca kaynak ifadesindeki yalın arazi dalını kapsar ve komşu su veya içecek anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; su yolu komşusu ortak çekirdeği en iyi gösterirken geniş ve ağaçlı arazi uzantısının sınırını da açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal su yoluna odaklanır; odak dal ise su yolunun yanında geniş ve ağaçlı vadi veya çukur arazi adlarını da içerir.","focus_only":"Dar su yolunun yanında geniş veya çukur ağaçlı vadi kesimlerini de kapsar.","gloss":"su yolu","neighbor_only":"Doğrudan su yollarını adlandırır ve ağaçlı geniş vadi kapsamını taşımaz.","neighbor_ref":"root_000546/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da suyun arazi üzerinde geçtiği doğal kanalı adlandırabilir."}],"source_phrase_ar":"السال مسيل في مضيق الوادي (maqayis;sihah;tahdhib)؛ السليل الوادي الواسع ينبت السلم والسمر (sihah;tahdhib)؛ السلان بطون من الأرض غامضة ذات شجر (tahdhib)","source_summary":"Kaynak birleşimi vadi içindeki dar su yolunu, geniş ağaçlı vadiyi ve çukur ağaçlı arazi tabanlarını aynı yer adları alanında toplar.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه السال والسلان والمسيل الضيق في الوادي والسليل الوادي أو الموضع الذي يجتمع فيه الماء","what_is_not_ar":"ليس الماء المشروب نفسه ولا السلسلة ولا السلالة"},"support_links":[]},{"boundary":"Dal genel zayıflık değil, bedeni tüketen belirli ağır hastalıktır.","branch_kind":"bare","branch_ref":"root_000736/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَآئِل","morph_features":"STEM|POS:N|ACT|PCPL|LEM:saA^}il|ROOT:sAl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:10:2:2","qac_word_ref":"93:10:2","surface_ar":"سَّآئِلَ"}],"gloss":"tüberküloz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hastalık bedeni giderek zayıflatır, eti ve gücü azaltır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hastalığın seyri ağırdır ve ölümle sonuçlanabilir."}}],"root_ar":"س ء ل","root_id":"root_000736","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedeni zayıflatan, eti ve gücü azaltan ağır hastalığın doğal çağdaş karşılığıdır.","boundary_detail":"Dal genel zayıflık değil, bedeni tüketen belirli ağır hastalıktır.","branch_image_ar":"السُّل هزالا","concept_gloss":"tüberküloz","contextual_glosses":[{"applicability":"Tarihsel hastalık adının zayıflatıcı etkisinin açıklanması gereken bağlamlarda kullanılır.","error_profile":{"adds":"Aynı etkiyi yapan başka hastalıkları da kapsayabilecek genel bir ifade ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Eti ve gücü azaltarak bedeni tüketme etkisini korur."},"facet_ids":["F001","F002"],"text":"bedeni tüketen hastalık","usage_role":"explanatory"}],"definition":"İnsanın etini ve gücünü giderek azaltan, bedeni zayıflatıp tüketen ve ölümcül olabilen ağır hastalıktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hastalık bedeni giderek zayıflatır, eti ve gücü azaltır."},{"facet_id":"F002","role":"extension","statement":"Hastalığın seyri ağırdır ve ölümle sonuçlanabilir."}],"identity_rationale":"Kaynak ifadesi insanı zayıflatan, tüketen, etini ve gücünü azaltan, ölümcül olabilen hastalığı açıkça tanımlar. Etin çekilip alınmasına ilişkin benzetme köken açıklamasıdır, hastalığın yerine ayrı bir işlem koymaz.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"tüberküloz"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"tüberküloz"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"tüberküloz hastası"}],"lexicalization_note":"Tanım yalın hastalık dalını kapsar; çekip çıkarma, hırsızlık veya bağlantı anlamlarını bu dala taşımaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; belirli hastalık ile onun gibi nedenlerden doğan genel zayıflık arasındaki sınır en yararlı ayrımdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli hastalığın kendisidir; komşu dal ise çeşitli nedenlerle oluşabilen bedensel zayıflık ve çökme durumudur.","focus_only":"Bedeni tüketen belirli ve ölümcül olabilen hastalığı adlandırır.","gloss":"hastalık sonucu zayıflama","neighbor_only":"Hastalık veya yetersiz bakım sonucunda ortaya çıkan zayıflık durumunu adlandırır.","neighbor_ref":"root_001575/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da hastalıkla birlikte etin azalması ve bedenin zayıflaması sonucunu içerir."}],"source_phrase_ar":"السلال من المرض كأن لحمه قد سل (maqayis)؛ السل والسلال داء يأخذ الإنسان ويقتل (ayn)؛ السلال بالضم السل (sihah)؛ داء يهزل ويضني ويقتل (tahdhib)؛ مرض ينزع به اللحم والقوة (mufradat)","source_summary":"Kaynaklar bedeni tüketen ve öldürebilen ağır hastalık üzerinde birleşir; etin çekilip alınması benzetmesi hastalığın zayıflatıcı sonucunu açıklar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه السل والسلال داء يهزل ويضني ويقتل وينزع اللحم والقوة","what_is_not_ar":"ليس السل بمعنى النزع ولا السلة بمعنى السرقة ولا السلسلة"},"support_links":[]},{"boundary":"Dal genel hız ya da her türlü hamle değil, atın yarış içindeki güçlü çıkışıdır.","branch_kind":"collocation","branch_ref":"root_000736/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَآئِل","morph_features":"STEM|POS:N|ACT|PCPL|LEM:saA^}il|ROOT:sAl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:10:2:2","qac_word_ref":"93:10:2","surface_ar":"سَّآئِلَ"}],"gloss":"atın yarıştaki güçlü ileri atılımı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"At, yarış sırasında güçlü bir ileri atılım yapar."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu atılım atı öteki yarış atlarının önüne çıkarabilir."}}],"root_ar":"س ء ل","root_id":"root_000736","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"At yarışı kalıbındaki hamleyi ve öne çıkma yönünü birlikte karşılar.","boundary_detail":"Dal genel hız ya da her türlü hamle değil, atın yarış içindeki güçlü çıkışıdır.","branch_image_ar":"سلة الفرس دفعة","concept_gloss":"atın yarıştaki güçlü ileri atılımı","contextual_glosses":[{"applicability":"Atın güçlü bir hamleyle rakiplerinin önüne geçtiği koşu bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yarış bağlamını, ani güçlü atılımı ve öne geçme sonucunu korur."},"facet_ids":["F001","F002"],"text":"yarışta öne fırlamak","usage_role":"contextual"}],"definition":"Bir atın yarışta güçlü bir hamleyle ileri atılması ve öteki atların önüne çıkmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"At, yarış sırasında güçlü bir ileri atılım yapar."},{"facet_id":"F002","role":"extension","statement":"Bu atılım atı öteki yarış atlarının önüne çıkarabilir."}],"identity_rationale":"Kaynak ifadesi, atın yarış sırasında yaptığı güçlü atılımı ve diğer atların önüne çıkışını doğrudan destekler. Bu anlam yalnızca at yarışı kalıbına bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"atın yarışta ileri atılıp öne çıkması"}],"lexicalization_note":"Tanım yalnızca atın yarış atılımını bildiren kalıba bağlıdır ve genel bir yalın kök anlamı olarak sunulmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel güçlü hamle komşusu, at yarışı kalıbının zorunlu sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal atın yarıştaki hamlesine ve öne çıkmasına özgüdür; komşu dal katılımcı ve alan bakımından daha geniş bir itiş veya saldırı hareketidir.","focus_only":"At yarışı katılımcısını ve rakiplerin önüne çıkma sonucunu gerektirir.","gloss":"güçlü hamle","neighbor_only":"Savaş, koşu veya kış gibi farklı alanlardaki genel güçlü hamleyi kapsar.","neighbor_ref":"root_001278/B005","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir anda ileri yönelen güçlü bir hareket bulunur."}],"source_phrase_ar":"فرس شديد السلة وهي دفعته في سباقه (maqayis;sihah;tahdhib)؛ خرجت سلة هذا الفرس على سائر الخيل (ayn;tahdhib)","source_summary":"Kaynaklar atın yarıştaki güçlü ileri hamlesini ortak çekirdek olarak verir ve bu hamlenin diğer atlara üstün gelmesi sonucunu bildirir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه سلة الفرس ودفعته وخروجه على الخيل في السباق","what_is_not_ar":"ليس السلة بمعنى السرقة ولا السلة بمعنى الوعاء"},"support_links":[]},{"boundary":"Dal delme eyleminin kendisi değil, iplik geçiren iri dikiş aracıdır.","branch_kind":"bare","branch_ref":"root_000736/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَآئِل","morph_features":"STEM|POS:N|ACT|PCPL|LEM:saA^}il|ROOT:sAl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:10:2:2","qac_word_ref":"93:10:2","surface_ar":"سَّآئِلَ"}],"gloss":"çuvaldız","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Araç, ipliği malzemenin içinden çekip geçirmek için kullanılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sıradan iğneye göre büyük ve kalın bir dikiş iğnesidir."}}],"root_ar":"س ء ل","root_id":"root_000736","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İplik çekip geçirmek için kullanılan iri ve kalın dikiş iğnesini doğal biçimde karşılar.","boundary_detail":"Dal delme eyleminin kendisi değil, iplik geçiren iri dikiş aracıdır.","branch_image_ar":"المسلة السالة","concept_gloss":"çuvaldız","contextual_glosses":[{"applicability":"Geleneksel araç adının açıklanması gereken dikiş ve el işi bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Büyük iğne biçimini ve dikişte kullanılma işlevini korur."},"facet_ids":["F001","F002"],"text":"iri dikiş iğnesi","usage_role":"explanatory"}],"definition":"Dikişte ipliği çekip geçirmek için kullanılan büyük ve kalın iğne türüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Araç, ipliği malzemenin içinden çekip geçirmek için kullanılır."},{"facet_id":"F002","role":"specialization","statement":"Sıradan iğneye göre büyük ve kalın bir dikiş iğnesidir."}],"identity_rationale":"Kaynak ifadesi büyük iğneyi veya dikiş aracını, ipliği çekip geçirmesi işleviyle tanımlar. Geçici çerçeve bu araç kimliğini ve işlevini doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"çuvaldız; iri dikiş iğnesi"}],"lexicalization_note":"Tanım yalın araç adını kapsar ve komşu delici araçların farklı işlevlerini bu dala katmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; deri delme bizi, benzer biçime rağmen iplik taşıma işlevindeki farkı en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak araç ipliği taşıyan iri bir iğnedir; komşu araç öncelikle deriyi delik açarak hazırlayan bizdir.","focus_only":"İpliği çekip geçirmek için kullanılan iri iğnedir.","gloss":"deri delme bizi","neighbor_only":"Deri işlerinde delik açmaya yarayan biz türü sivri araçtır.","neighbor_ref":"root_000805/B007","relation_type":"near_neighbor","shared_zone":"Her iki dal da dikiş veya deri işinde kullanılan sivri el aracını anlatır."}],"source_phrase_ar":"المسلة معروفة لأنها تسل الخيط سلا (maqayis)؛ المسلة المخيط وجمعه مسال (ayn)؛ المسلة واحدة المسال وهي الإبر العظام (sihah)","source_summary":"Kaynaklar bunun büyük bir dikiş iğnesi olduğu ve ipliği çekip geçirme işlevi taşıdığı üzerinde birleşir.","sources":["MQ","AY","SI"],"what_is_ar":"يدخل فيه المسلة والمسال والإبر العظام والمخيط الذي يسل الخيط","what_is_not_ar":"ليس السلة الوعاء ولا السلسلة ولا السلالة"},"support_links":[]},{"boundary":"Dal hırsızlık veya at hamlesi değil, içine nesne konan somut kaptır.","branch_kind":"mixed_non_bare","branch_ref":"root_000736/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَآئِل","morph_features":"STEM|POS:N|ACT|PCPL|LEM:saA^}il|ROOT:sAl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:10:2:2","qac_word_ref":"93:10:2","surface_ar":"سَّآئِلَ"}],"gloss":"sepet veya kapaklı kap","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesneleri içine almaya yarayan sepet veya kap türü somut bir taşıyıcıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ekmek koyma işlevi, kabın belirli bir kullanım alanıdır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kapaklı sepet ve kilden yapılmış kap, bildirilen biçim çeşitleridir."}}],"root_ar":"س ء ل","root_id":"root_000736","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ekmek ve başka nesneleri taşımaya ya da saklamaya yarayan kap türlerini birlikte karşılar.","boundary_detail":"Dal hırsızlık veya at hamlesi değil, içine nesne konan somut kaptır.","branch_image_ar":"السلة وعاء","concept_gloss":"sepet veya kapaklı kap","contextual_glosses":[{"applicability":"Kabın özellikle ekmek koymak için kullanıldığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başka nesneler için kullanılan kapaklı veya kilden kapları kapsamaz.","preserves":"Sepet veya kap işlevini ve ekmek kullanımını korur."},"facet_ids":["F001","F002"],"text":"ekmek sepeti","usage_role":"contextual"},{"applicability":"Kapağı bulunan sepet biçimli taşıyıcı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Açık ekmek kabını ve kilden kap çeşidini kapsamaz.","preserves":"Kapaklı sepet biçimini ve taşıyıcı işlevini korur."},"facet_ids":["F001","F003"],"text":"kapaklı sepet","usage_role":"contextual"}],"definition":"Ekmek veya başka nesneleri koymak için kullanılan, sepet ya da kapaklı kap biçimindeki taşıyıcıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesneleri içine almaya yarayan sepet veya kap türü somut bir taşıyıcıdır."},{"facet_id":"F002","role":"specialization","statement":"Ekmek koyma işlevi, kabın belirli bir kullanım alanıdır."},{"facet_id":"F003","role":"source_variant","statement":"Kapaklı sepet ve kilden yapılmış kap, bildirilen biçim çeşitleridir."}],"identity_rationale":"Kaynak ifadesi ekmek kabını ve kapaklı sepet ya da benzeri kabı birlikte verir. Geçici çerçeve, nesnenin kap ve taşıyıcı olma çekirdeğini doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"ekmek sepeti"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"kapaklı sepet veya kap"}],"lexicalization_note":"Tanım genel kap biçimini kapsar; ekmek kabı kalıbını bu genel nesnenin özel kullanım alanı olarak tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel kap komşusu, sepet ve kapaklı biçim sınırlamasını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sepet ya da kapaklı kap biçiminde daha özeldir; komşu dal ise bütün kap türlerini kapsayan üst alandır.","focus_only":"Sepet veya kapaklı kap biçimini ve ekmek kullanımını öne çıkarır.","gloss":"genel kap","neighbor_only":"Biçim ve malzeme sınırlaması olmadan her türlü kabı kapsar.","neighbor_ref":"root_000063/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da içine bir şey konan somut taşıyıcı nesneleri kapsar."}],"source_phrase_ar":"سلة الخبز معروفة (sihah)؛ السلة السبذة المطبقة كالجؤنة (ayn;tahdhib)؛ سبذة الطين السلة (tahdhib)","source_summary":"Kaynak birleşimi ekmek kabını, kapaklı sepeti ve kilden yapılmış benzer kabı aynı somut taşıyıcı alanında toplar.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه السلة وعاء الخبز والسبذة المطبقة والجؤنة ونحوها","what_is_not_ar":"ليس السلة بمعنى السرقة ولا دفعة الفرس ولا المرض"},"support_links":[]},{"boundary":"Dal genel çizgi veya kalın doku değil, şerit, lif ya da ince uç görünümündeki uzantılarla sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000736/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَآئِل","morph_features":"STEM|POS:N|ACT|PCPL|LEM:saA^}il|ROOT:sAl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:10:2:2","qac_word_ref":"93:10:2","surface_ar":"سَّآئِلَ"}],"gloss":"ince uzun şerit, lif veya uç","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Parça, bağlı olduğu bütünden ayrılmış veya onun üzerinde ince ve uzun biçimde uzanmıştır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Saç, bağ doku, et, hörgüç ve burun içindeki şerit ya da doku parçaları bu biçime girer."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dilin ince ucu ile uzayan diken, aynı incelik ve uzanma görünümüne dayalı uç kullanımlarıdır."}}],"root_ar":"س ء ل","root_id":"root_000736","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Doku şeritleri, sıyrılmış lifler ve sivri uçlar arasındaki biçim ortaklığını eksiksiz karşılar.","boundary_detail":"Dal genel çizgi veya kalın doku değil, şerit, lif ya da ince uç görünümündeki uzantılarla sınırlıdır.","branch_image_ar":"طرائق مستلة","concept_gloss":"ince uzun şerit, lif veya uç","contextual_glosses":[{"applicability":"Saç, bağ doku, et, hörgüç veya burun içindeki şeritler anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dilin ucu, diken ve bitkiden sıyrılmış parça kullanımlarını kapsamaz.","preserves":"İnce uzun şerit biçimini ve bedensel doku kapsamını korur."},"facet_ids":["F001","F002"],"text":"ince uzun doku şeridi","usage_role":"explanatory"},{"applicability":"Dilin ucu veya uzayan diken gibi sivri uç bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Şerit, lif ve geniş doku parçası kullanımlarını kapsamaz.","preserves":"İnce ve uzayan uç biçimini korur."},"facet_ids":["F001","F003"],"text":"ince sivri uç","usage_role":"contextual"}],"definition":"Bir bütünden sıyrılmış ya da onun üzerinde ince ve uzun biçimde uzanan şerit, lif, doku parçası veya sivri uçtur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Parça, bağlı olduğu bütünden ayrılmış veya onun üzerinde ince ve uzun biçimde uzanmıştır."},{"facet_id":"F002","role":"specialization","statement":"Saç, bağ doku, et, hörgüç ve burun içindeki şerit ya da doku parçaları bu biçime girer."},{"facet_id":"F003","role":"extension","statement":"Dilin ince ucu ile uzayan diken, aynı incelik ve uzanma görünümüne dayalı uç kullanımlarıdır."}],"identity_rationale":"Kaynak ifadesi saç, bağ doku, et, hörgüç ve burun içindeki şeritleri; dilin ince ucunu ve uzayan dikeni bir araya getirir. Bunlar tek nesne türü değildir, ancak bir bütünden ayrılan veya ince biçimde uzanan parça ortaklığıyla aynı dalda dikkatle tutulabilir.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"saçtan veya dokudan ince uzun şerit"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"hörgüçteki uzun şeritler veya burun içi doku parçaları"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"dilin ince ucu"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"uzun ve sivri diken"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"hurma dalından sıyrılmış ince parça"}],"lexicalization_note":"Tanım türemiş parça adları ile dil ucu ve dal parçası kalıplarını ayırır; özel örnekleri yalın bir çizgi anlamına genellemez.","neighbor_coverage_note":"Bütün adaylar incelendi; ince iplik komşusu biçim benzerliğini gösterirken doku ve uç kapsamının farkını korur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal iplik veya tel gibi bağımsız çizgisel nesnedir; odak dal ise beden ya da bitki üzerindeki şerit, lif ve uçlara uzanır.","focus_only":"Doku şeridi, sivri uç ve bir bütünden sıyrılan çeşitli parçaları kapsar.","gloss":"ince uzun iplik","neighbor_only":"Bağımsız bir iplik veya çok ince telin çizgisel uzanışını adlandırır.","neighbor_ref":"root_000453/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da ince ve uzun bir biçim temel görsel ortaklıktır."}],"source_phrase_ar":"السليلة عقبة أو عصبة أو لحمة شبه طرائق (ayn;tahdhib)؛ سليلة من شعر لما استل من ضريبته (sihah)؛ سلائل السنام طرائق طوال (tahdhib)؛ أسلة اللسان الطرف الرقيق (mufradat)؛ السلاءة من الشوك لأن فيها امتدادا (maqayis)","source_summary":"Birleşik kaynak anlatımı çeşitli beden ve bitki parçalarını ince, uzun veya şerit biçiminde uzanma ortaklığı altında toplar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه السليلة والسلائل والطرائق الممتدة من الشعر واللحم والسنام والخيشوم وما شابهها من أطراف دقيقة أو ممتدة","what_is_not_ar":"ليس السلسلة المتصلة ولا الوادي ولا المرض"},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000736/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَآئِل","morph_features":"STEM|POS:N|ACT|PCPL|LEM:saA^}il|ROOT:sAl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:10:2:2","qac_word_ref":"93:10:2","surface_ar":"سَّآئِلَ"}],"gloss":"biçime bağlı adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kumaşın kullanımdan dolayı incelip gevşemesi bağımsız bir yıpranma anlamıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kılıç yüzeyindeki dalgalı parlaklık bağımsız bir yüzey görünümü anlamıdır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dokumadaki çizgili süs bağımsız bir desen anlamıdır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Etin azalıp bedende oluklar oluşması bağımsız bir zayıflama görünümüdür."}}],"root_ar":"س ء ل","root_id":"root_000736","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"الرقة والتخطط من البلى","concept_gloss":"biçime bağlı adlandırmalar","contextual_glosses":[{"applicability":"Yalnızca kumaşın kullanım sonucu incelip gevşediği ilk kullanım için geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kılıç parıltısı, çizgili dokuma ve bedensel oluklaşma kullanımlarını kapsamaz.","preserves":"Kumaşın kullanım sonucu incelmesi ve gevşemesi anlamını korur."},"facet_ids":["F001"],"text":"giyilmekten incelmiş kumaş","usage_role":"contextual"},{"applicability":"Yalnızca kılıç yüzeyindeki parlak ve dalgalı görünüm için geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kumaş incelmesi, dokuma deseni ve bedensel oluklaşmayı kapsamaz.","preserves":"Kılıç yüzeyinin parlak ve dalgalı görünümünü korur."},"facet_ids":["F002"],"text":"kılıcın dalgalı yüzey parıltısı","usage_role":"contextual"},{"applicability":"Yalnızca üzerinde çizgili süs bulunan kumaş kullanımında geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yıpranma, kılıç parıltısı ve bedensel oluklaşma kullanımlarını kapsamaz.","preserves":"Kumaş üzerindeki çizgili süs ve desen görünümünü korur."},"facet_ids":["F003"],"text":"çizgili dokuma","usage_role":"contextual"},{"applicability":"Yalnızca et kaybı nedeniyle bedende olukların belirdiği kişi için geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Üç kumaş ve kılıç yüzeyi kullanımını kapsamaz.","preserves":"Et azalmasını ve bunun oluşturduğu oluklu beden görünümünü korur."},"facet_ids":["F004"],"text":"eti azalıp bedeni oluklaşmış","usage_role":"contextual"}],"definition":"Mevcut dal tek bir kavram tanımlamaz; yıpranarak incelme, çizgili görünüm, kılıç yüzeyi parıltısı ve et kaybıyla oluklaşma ayrı anlam çekirdekleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kumaşın kullanımdan dolayı incelip gevşemesi bağımsız bir yıpranma anlamıdır."},{"facet_id":"F002","role":"source_variant","statement":"Kılıç yüzeyindeki dalgalı parlaklık bağımsız bir yüzey görünümü anlamıdır."},{"facet_id":"F003","role":"source_variant","statement":"Dokumadaki çizgili süs bağımsız bir desen anlamıdır."},{"facet_id":"F004","role":"source_variant","statement":"Etin azalıp bedende oluklar oluşması bağımsız bir zayıflama görünümüdür."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"kumaşın giyilmekten incelmesi"},{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"kılıç yüzeyinin dalgalı parıltısı"},{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"çizgili süslü kumaş"},{"lexical_unit_id":"lu_041","rendering_kind":"ordinary","target_gloss":"eti azalıp bedeni oluklaşmış kişi"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"تسلسل الثوب وتخلخل إذا لبس حتى رق؛ التسلسل بريق فرند السيف ودبيبه؛ ثوب ملسلس فيه وشي مخطط؛ المتسلسل الذي تخدد لحمه وقل","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık kumaş yıpranması, kılıç parıltısı, çizgili dokuma ve bedensel oluklaşmayı ayrı kullanımlar olarak verir."}],"source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["TA"],"what_is_ar":"يدخل فيه تسلسل الثوب إذا رق من اللبس وبريق فرند السيف ودبيبه والوشي المخطط والتخدد في اللحم","what_is_not_ar":"ليس السلسلة الحديدية ولا الماء السلس ولا المرض نفسه"},"support_links":[]},{"boundary":"Dal diş türünü veya diş çıkarma evresini değil, dişlerin düşmesiyle oluşan durumu anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000736/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَآئِل","morph_features":"STEM|POS:N|ACT|PCPL|LEM:saA^}il|ROOT:sAl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:10:2:2","qac_word_ref":"93:10:2","surface_ar":"سَّآئِلَ"}],"gloss":"dişleri düşmüş olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan veya hayvan dişlerini kaybetmiş ve dişsiz kalmıştır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yaşlılık nedeniyle dişleri düşen dişi deve bu durumun özel örneğidir."}}],"root_ar":"س ء ل","root_id":"root_000736","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan ve hayvanda diş kaybı sonucunda oluşan durumu genel olarak karşılar.","boundary_detail":"Dal diş türünü veya diş çıkarma evresini değil, dişlerin düşmesiyle oluşan durumu anlatır.","branch_image_ar":"سقوط الأسنان","concept_gloss":"dişleri düşmüş olma","contextual_glosses":[{"applicability":"İnsan veya hayvanın diş kaybı durumunu niteleyen doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Diş kaybını ve bunun sonucunda oluşan bedensel durumu korur."},"facet_ids":["F001"],"text":"dişleri dökülmüş","usage_role":"general"},{"applicability":"Özellikle yaşlı dişi devenin durumunun belirtildiği hayvan bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsan ve diğer hayvanlara yönelik genel kapsamı dışarıda bırakır.","preserves":"Yaşlılık nedenini, diş kaybını ve dişi deve katılımcısını korur."},"facet_ids":["F001","F002"],"text":"yaşlılıktan dişleri düşmüş dişi deve","usage_role":"contextual"}],"definition":"Bir insanın veya hayvanın, özellikle yaşlılık nedeniyle, dişlerinin düşmüş olması durumudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan veya hayvan dişlerini kaybetmiş ve dişsiz kalmıştır."},{"facet_id":"F002","role":"specialization","statement":"Yaşlılık nedeniyle dişleri düşen dişi deve bu durumun özel örneğidir."}],"identity_rationale":"Kaynak ifadesi insan, koyun ve özellikle yaşlı deve için dişleri düşmüş olma durumunu açıkça bildirir. Geçici çerçeve bu ortak bedensel durumu doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_042","rendering_kind":"ordinary","target_gloss":"dişleri düşmüş erkek, kadın veya koyun"},{"lexical_unit_id":"lu_043","rendering_kind":"ordinary","target_gloss":"yaşlılıktan dişleri düşmüş dişi deve"}],"lexicalization_note":"Tanım kişi ve hayvana yönelik türemiş nitelemeleri kapsar; yaşlı deve kalıbını bu ortak durumun özel uygulaması olarak tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı diş kaybı durumunu daha dar bir hayvan kapsamıyla veren komşu en yararlı karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ortak durum aynıdır, ancak komşu dal tek bir hayvan türüne özgüyken odak dal insan ve birden çok hayvan türüne uygulanır.","focus_only":"İnsan, koyun ve dişi deve gibi daha geniş bir katılımcı kümesini kapsar.","gloss":"dişleri düşmüş hayvan","neighbor_only":"Yalnızca dişleri düşmüş belirli bir sığır türü için kullanılan addır.","neighbor_ref":"root_001239/B012","relation_type":"near_synonym","shared_zone":"Her iki dal da dişlerin düşmesi sonucunda oluşan dişsizlik durumunu anlatır."}],"source_phrase_ar":"السلة الناقة التي سقطت أسنانها؛ رجل سل وامرأة سلة وشاة سلة أي ساقطة الأسنان","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, dişleri düşmüş insanı, koyunu ve yaşlı dişi deveyi aynı durum adı altında verir."}],"source_summary":"Birden çok kaynak arasında ortak özet yoktur; tek tanıklık insan ve çeşitli hayvanlarda dişlerin düşmüş olma durumunu bildirir.","sources":["TA"],"what_is_ar":"يدخل فيه السل والسلة في سقوط الأسنان من الهرم أو نحو ذلك","what_is_not_ar":"ليس السلة بمعنى وعاء ولا السرقة ولا داء السل"},"support_links":[]},{"boundary":"Dal genel boşluk değil, su teknesinin belirli yapısal parçaları arasındaki aralıktır.","branch_kind":"bare","branch_ref":"root_000736/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَآئِل","morph_features":"STEM|POS:N|ACT|PCPL|LEM:saA^}il|ROOT:sAl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:10:2:2","qac_word_ref":"93:10:2","surface_ar":"سَّآئِلَ"}],"gloss":"su teknesi destekleri arasındaki boşluk","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Açıklık, su teknesine ait iki dikili yapısal parça arasında bulunur."}}],"root_ar":"س ء ل","root_id":"root_000736","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yapı türünü, parçaları ve aralarındaki açıklığı birlikte belirten tam karşılıktır.","boundary_detail":"Dal genel boşluk değil, su teknesinin belirli yapısal parçaları arasındaki aralıktır.","branch_image_ar":"الفرجة بين النصائب","concept_gloss":"su teknesi destekleri arasındaki boşluk","contextual_glosses":[{"applicability":"Su teknesinin yapısındaki iki yan veya destek parçası arasındaki boşluk açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tekne yapısını, yan parçaları ve aradaki açıklığı korur."},"facet_ids":["F001"],"text":"tekne yanları arasındaki açıklık","usage_role":"explanatory"}],"definition":"Bir su teknesinin çevresindeki dikili destek veya yan parçalar arasında kalan açıklıktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Açıklık, su teknesine ait iki dikili yapısal parça arasında bulunur."}],"identity_rationale":"Kaynak ifadesi dalı, su teknesinin dikili yan parçaları arasındaki boşluk olarak tek ve açık biçimde tanımlar. Geçici çerçeve bu yer ve parça ilişkisini doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_044","rendering_kind":"ordinary","target_gloss":"su teknesinin dikili parçaları arasındaki boşluk"}],"lexicalization_note":"Tanım yalnızca kaynak ifadesindeki yalın yapı terimini kapsar ve genel aralık anlamını sınırsız biçimde içeri almaz.","neighbor_coverage_note":"Bütün adaylar incelendi; genel iki şey arası boşluk komşusu, su teknesine özgü yapısal sınırı en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel aralık ve geçit alanıdır; odak dal yalnızca su teknesinin belirli yapısal parçaları arasındaki boşluğu adlandırır.","focus_only":"Boşluğu su teknesinin dikili yapısal parçalarıyla sınırlar.","gloss":"iki şey arasındaki boşluk","neighbor_only":"Ev, bulut, insan topluluğu veya arazi gibi çok çeşitli şeyler arasındaki boşlukları kapsar.","neighbor_ref":"root_000435/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da iki ayrı unsur arasında kalan açık alan bulunur."}],"source_phrase_ar":"السلة الفرجة بين نصائب الحوض","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık terimi, su teknesinin dikili destekleri arasında kalan açıklıkla sınırlar."}],"source_summary":"Birden çok kaynak arasında ortak özet yoktur; tek tanıklık su teknesinin dikili parçaları arasındaki yapısal boşluğu bildirir.","sources":["TA"],"what_is_ar":"يدخل فيه السلة بمعنى الفرجة بين نصائب الحوض","what_is_not_ar":"ليس السلة بمعنى وعاء ولا السرقة ولا دفعة الفرس"},"support_links":[]},{"boundary":"Dal, aydınlık zaman dilimini veya genel açma eylemini değil, su yatağını ve ona bağlı kullanımları kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001559/B001","candidate_links":[{"candidate_id":"cand_145e2f3d536b70286c80","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَنْهَرْ","morph_features":"STEM|POS:V|IMPF|LEM:tanoharo|ROOT:nhr|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"93:10:4:1","qac_word_ref":"93:10:4","surface_ar":"تَنْهَرْ"}],"gloss":"bol su taşıyan doğal akarsu yatağı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Taşkın ya da bol suyu taşıyan ve toprağı yararak belirginleşen doğal bir su yatağıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Suyun arazide akması ve bu akışla kendine bir yatak açması anlatılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Su yatağının kendine sağlam ve yerleşik bir güzergah edinmesi yapı bağlı bir kullanımdır."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Suyun kazıp oluşturduğu belirli yatak yeri de bu dal içinde adlandırılır."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Kuyu kazısının yer altındaki su düzeyine ulaşması, suya varma sonucunu bildiren bağlı bir kullanımdır."}}],"root_ar":"ن ه ر","root_id":"root_001559","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yalın çekirdeğini, hem akan suyu taşıma hem de toprağı yararak oluşmuş yatak olma yönleriyle karşılar.","boundary_detail":"Dal, aydınlık zaman dilimini veya genel açma eylemini değil, su yatağını ve ona bağlı kullanımları kapsar.","branch_image_ar":"نهر يشق الأرض بماء جار","concept_gloss":"bol su taşıyan doğal akarsu yatağı","contextual_glosses":[{"applicability":"Suyun arazide ilerleyerek kendi akış yolunu oluşturduğu yapı bağlı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Akışı ve akış sonucunda bir su yatağı oluşmasını birlikte korur."},"facet_ids":["F002"],"text":"su akıp kendine yatak açtı","usage_role":"contextual"},{"applicability":"Kuyu kazısının yer altındaki su düzeyine vardığını anlatan özel bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kazma sürecinin suya ulaşmasıyla tamamlanan sonucu açıkça korur."},"facet_ids":["F005"],"text":"kazı suya ulaştı","usage_role":"contextual"}],"definition":"Yeryüzünü yararak açılmış, taşkın ya da bol suyu taşıyan doğal su yatağıdır. Yapıya bağlı kullanımlarda suyun akıp kendine yatak açması, yatağın sağlam bir güzergah edinmesi ve kazının suya ulaşması anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Taşkın ya da bol suyu taşıyan ve toprağı yararak belirginleşen doğal bir su yatağıdır."},{"facet_id":"F002","role":"specialization","statement":"Suyun arazide akması ve bu akışla kendine bir yatak açması anlatılır."},{"facet_id":"F003","role":"associated_use","statement":"Su yatağının kendine sağlam ve yerleşik bir güzergah edinmesi yapı bağlı bir kullanımdır."},{"facet_id":"F004","role":"specialization","statement":"Suyun kazıp oluşturduğu belirli yatak yeri de bu dal içinde adlandırılır."},{"facet_id":"F005","role":"extension","statement":"Kuyu kazısının yer altındaki su düzeyine ulaşması, suya varma sonucunu bildiren bağlı bir kullanımdır."}],"identity_rationale":"Kaynak ifadesi, taşkın ya da bol suyun aktığı yatağı; bu yatağın toprağı yarmasını ve suyun akarak kendine yol açmasını aynı dalda açıkça birleştirir. Kuyu kazısında suya ulaşma ve yatağın yerleşmesi ise bu çekirdeğe bağlı özel kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"taşkın suyun aktığı doğal akarsu yatağı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"akarsu yatakları"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"akarsular veya akarsu yatakları"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"akarsu yatağı sağlam bir güzergah edindi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"su aktı ve kendine bir yatak açtı"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bol sulu veya geniş akarsu"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"suyun kazıp açtığı yatak yeri"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kuyu kazısı suya ulaştı"}],"lexicalization_note":"Tanım, yalın su yatağı anlamını korur; suyun akması, yatağın yerleşmesi ve kazıda suya ulaşılması yalnız kendi yapılarına bağlı tutulur.","neighbor_coverage_note":"Listelenen bütün adaylar su yatağı, akış, vadi, iç dallar ve ilgisiz alanlar bakımından değerlendirildi; sınırı en açık biçimde gösteren dört karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal doğal akarsu yatağını büyüklükçe sınırlamaz ve bol suyu da kapsar; komşu dal ise küçük, uzanan veya ana yataktan ayrılan su yoluna özelleşir.","focus_only":"Taşkın ya da bol su taşıyabilen doğal yatağın genel kapsamı bulunur.","gloss":"küçük su yolu","neighbor_only":"Özellikle küçük ve uzanan bir yan su yolu olma sınırı bulunur.","neighbor_ref":"root_000229/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da akan suyu taşıyan belirgin bir arazi yatağını gösterir."},{"boundary_match":"partial","distinction":"Odak dal akışın geçtiği doğal yatağı adlandırır; komşu dal ise öncelikle yüzeyde hareket eden suyu adlandırdığı için olağan kullanımda birbirinin yerine geçmez.","focus_only":"Suyun aktığı ve toprağı yaran kalıcı yatak öne çıkar.","gloss":"yeryüzünde akan su","neighbor_only":"Yatak yerine yeryüzünde akmakta olan su kütlesi öne çıkar.","neighbor_ref":"root_000768/B002","relation_type":"near_neighbor","shared_zone":"İki dal da yeryüzündeki görünür su akışını aynı sahne içinde ele alır."},{"boundary_match":"partial","distinction":"Odak dal su akışının yatağı olarak tanımlanır; komşu dal ise su bulunmasa da varlığını sürdüren geniş bir yer şekli ve sel geçididir.","focus_only":"Bol ya da taşkın suyu taşıyan doğal su yatağıdır.","gloss":"sel yolu olan vadi","neighbor_only":"Dağlar ve tepeler arasındaki geniş arazi geçidi de kapsama girer.","neighbor_ref":"root_001637/B005","relation_type":"near_neighbor","shared_zone":"Her ikisi de suyun arazide izlediği doğal bir geçiş hattını içerebilir."},{"boundary_match":"partial","distinction":"Odak dal bu sürecin su taşıyan arazi yatağını gösterir; komşu dal ise farklı nesnelerde gerçekleşebilen açma ve genişletme işlemini gösterir.","focus_only":"Ortaya çıkmış doğal su yatağı ve onun içindeki akış bulunur.","gloss":"açıp genişletme","neighbor_only":"Bir şeyi açma, genişletme veya içeriğini akışa bırakma işlemi bulunur.","neighbor_ref":"root_001559/B003","relation_type":"near_neighbor","shared_zone":"Toprağın ya da bir açıklığın yarılması ve akışa yol verilmesi ortak imgedir."}],"source_phrase_ar":"النهر مجرى الماء الفائض (mufradat)؛ النهر واحد الأنهار وجمعه أنهار ونهر (ayn;sihah;tahdhib;maqayis)؛ سمي النهر لأنه ينهر الأرض أي يشقها (maqayis)؛ استنهر النهر أخذ مجراه (ayn;tahdhib;maqayis)؛ نهر الماء أو أنهر الماء جرى (sihah;tahdhib;maqayis)؛ نهر نهر كثير الماء (sihah;tahdhib;maqayis;mufradat)؛ حفرت البئر حتى نهرت أي بلغت الماء (tahdhib)","source_summary":"Kaynakların ortak çekirdeği, bol veya taşkın suyu taşıyan doğal yatağın toprağı yarmasıdır. Toplu kanıt ayrıca suyun akıp yatak açmasını, yatağın yerleşmesini, bol ya da geniş oluşunu ve kuyu kazısında suya ulaşmayı kapsar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"مجرى الماء الفائض؛ النهر والأنهار وجمع نهر؛ شق الأرض بالمجرى؛ جريان الماء الكثير؛ أخذ المجرى موضعا؛ بلوغ الماء في الحفر","what_is_not_ar":"لا يدخل فيه النهار الزمني؛ ولا الزجر والانتهار؛ ولا فرخ الطير"},"support_links":["sup_d20a828d3bafbe44bdf2"]},{"boundary":"Dal, yirmi dört saatlik günün tamamına zorunlu olarak yayılmaz ve su yatağı anlamından bütünüyle ayrıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001559/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَنْهَرْ","morph_features":"STEM|POS:V|IMPF|LEM:tanoharo|ROOT:nhr|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"93:10:4:1","qac_word_ref":"93:10:4","surface_ar":"تَنْهَرْ"}],"gloss":"şafaktan gün batımına aydınlık gündüz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Şafaktan güneş batımına kadar ışığın yayıldığı ve geceye karşıt olan süredir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bazı kullanımlarda aydınlık süre, bir günün adı yerine geçer."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu zaman adının belirli bir çoğul biçimi de tanıklanmıştır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Gündüz vaktine sahip olan veya gündüz baskın yapan kişi için yapı bağlı bir niteleme kullanılır."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Karanlıktan çıkıp gündüzün aydınlığına girme de yapı bağlı bir kullanımdır."}}],"root_ar":"ن ه ر","root_id":"root_001559","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın ışık, süre ve geceye karşıtlık bileşenlerini birlikte taşıyan genel karşılığıdır.","boundary_detail":"Dal, yirmi dört saatlik günün tamamına zorunlu olarak yayılmaz ve su yatağı anlamından bütünüyle ayrıdır.","branch_image_ar":"انفتاح النهار بالضياء","concept_gloss":"şafaktan gün batımına aydınlık gündüz","contextual_glosses":[{"applicability":"Geceye karşıt aydınlık zaman diliminin cümle içinde doğal ve kısa karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aydınlık zaman dilimini ve geceye karşıt oluşunu doğal biçimde korur."},"facet_ids":["F001"],"text":"gündüz","usage_role":"general"},{"applicability":"Aydınlık sürenin kaynakta bir gün adı yerine kullanıldığı sınırlı bağlamlar içindir.","error_profile":{"adds":"Bağlam dışında yirmi dört saatlik tam günü de düşündürebilir.","collision":"Tam gün ile yalnız aydınlık süre arasındaki sınır belirsizleşebilir.","fit":"broadening","loses":null,"preserves":"Belirli bir zaman birimi ve gündelik süre düşüncesini korur."},"facet_ids":["F002"],"text":"gün","usage_role":"contextual"},{"applicability":"Bir öznenin karanlıktan çıkarak gündüzün aydınlığına girdiği yapı bağlı kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gündüzün aydınlığına girme yönündeki katılımcı değişimini korur."},"facet_ids":["F005"],"text":"gündüz vaktine çıktı","usage_role":"contextual"}],"definition":"Şafağın doğuşundan güneşin batışına kadar ışığın yayıldığı, geceye karşıt zaman dilimidir. Bazı kullanımlarda gün adı, çoğul biçim, gündüz vakti hareket eden kişi veya aydınlığa çıkma anlamı kazanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Şafaktan güneş batımına kadar ışığın yayıldığı ve geceye karşıt olan süredir."},{"facet_id":"F002","role":"extension","statement":"Bazı kullanımlarda aydınlık süre, bir günün adı yerine geçer."},{"facet_id":"F003","role":"source_variant","statement":"Bu zaman adının belirli bir çoğul biçimi de tanıklanmıştır."},{"facet_id":"F004","role":"associated_use","statement":"Gündüz vaktine sahip olan veya gündüz baskın yapan kişi için yapı bağlı bir niteleme kullanılır."},{"facet_id":"F005","role":"associated_use","statement":"Karanlıktan çıkıp gündüzün aydınlığına girme de yapı bağlı bir kullanımdır."}],"identity_rationale":"Kaynak ifadesi dalı, şafağın doğuşundan güneşin batışına kadar ışığın yayıldığı ve geceye karşıt olan süre olarak kurar. Gün anlamı, çoğul kullanım, gündüz vakti hareket eden kişi ve aydınlığa çıkma bu zaman çekirdeğine bağlı yan kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"şafaktan güneş batımına kadar süren aydınlık gündüz"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"aydınlık gündüz süreleri"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"gündüz vaktinde baskın yapan kimse"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"gündüzün aydınlığına girdik"}],"lexicalization_note":"Yalın aydınlık zaman anlamı tanımın çekirdeğidir; kişi nitelemesi ve aydınlığa girme yalnız tanıklanan yapılara bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar ışık, zaman sınırı, gök cismi, sabah bölümü ve kökün diğer dalları bakımından karşılaştırıldı; en yakın üç zaman ve aydınlık komşusu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal şafaktan başlayan ışıklı süreyi ve gece karşıtlığını vurgular; komşu dal güneş doğumundan batımına ölçülen bilinen gün süresini öne çıkarır.","focus_only":"Işığın yayılması ve geceye karşıtlık tanımın kurucu parçalarıdır.","gloss":"güneş doğumundan batımına gün","neighbor_only":"Güneşin doğuşuyla başlayan ve bir gün birimi olarak sayılan süre öne çıkar.","neighbor_ref":"root_001700/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da gün içindeki aydınlık zaman aralığını sınırlarıyla gösterir."},{"boundary_match":"partial","distinction":"Odak dal aydınlık gündüzün tamamıdır; komşu dal yalnız bu sürenin ilk bölümünü ve başlangıç anını adlandırır.","focus_only":"Şafaktan gün batımına kadar uzanan bütün aydınlık süreyi kapsar.","gloss":"sabah ve günün başlangıcı","neighbor_only":"Aydınlık sürenin yalnız başlangıcı ve sabah bölümüyle sınırlıdır.","neighbor_ref":"root_000839/B001","relation_type":"near_neighbor","shared_zone":"İki dal da karanlığın ardından başlayan gündüz zamanına ilişkindir."},{"boundary_match":"partial","distinction":"Odak dal ışıklı zaman aralığını adlandırır; komşu dal ise ışığın veya yüzün aydınlanma durumunu ve belirli sabah vakitlerini kapsar.","focus_only":"Belirli başlangıç ve bitiş sınırları olan bir zaman dilimidir.","gloss":"ışığın belirginleşmesi","neighbor_only":"Yüzün parlaması ve karanlıktan sonra ışığın belirginleşmesi de kapsamdadır.","neighbor_ref":"root_000712/B002","relation_type":"near_neighbor","shared_zone":"Aydınlığın karanlıktan sonra görünür hale gelmesi iki dalın kesişimidir."}],"source_phrase_ar":"النهار ضياء ما بين طلوع الفجر إلى غروب الشمس (ayn;tahdhib;maqayis)؛ النهار ضد الليل (sihah)؛ الوقت الذي ينتشر فيه الضوء (mufradat)؛ النهار اسم لكل يوم (tahdhib)؛ النهار يجمع على نهر (sihah;tahdhib;maqayis)؛ رجل نهر صاحب نهار (ayn;sihah;tahdhib;maqayis;mufradat)","source_summary":"Kaynaklar aydınlık gündüz süresini geceye karşıt, ışığın yayıldığı zaman olarak ortaklaştırır. Toplu kanıt bu sürenin kimi yerde gün adı olmasını, çoğulunu, gündüz hareket eden kişi nitelemesini ve aydınlığa girme kullanımını da taşır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"النهار وضوء ما بين طلوع الفجر وغروب الشمس؛ ضد الليل؛ اليوم في بعض الاستعمال؛ جمع النهار على نهر؛ رجل نهر صاحب نهار","what_is_not_ar":"لا يدخل فيه مجرى الماء؛ ولا السعة المجردة؛ ولا فرخ الطير"},"support_links":[]},{"boundary":"Akış, kan ve bağırsak kullanımlarında belirgindir; açık alan ve yarık genişletmede ise kurucu öğe açıklık veya genişliktir.","branch_kind":"mixed_non_bare","branch_ref":"root_001559/B003","candidate_links":[{"candidate_id":"cand_145e2f3d536b70286c80","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَنْهَرْ","morph_features":"STEM|POS:V|IMPF|LEM:tanoharo|ROOT:nhr|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"93:10:4:1","qac_word_ref":"93:10:4","surface_ar":"تَنْهَرْ"}],"gloss":"bir şeyi açma veya genişletme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin açılması, açılması için yarılması veya mevcut açıklığının genişletilmesi temel ilişkidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kanı açılan bir yerden serbest bırakıp akıtma, çekirdeğin akış sonuçlu özel gerçekleşmesidir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir yaranın veya yarığın açıklığını büyütmek, genişletme çekirdeğinin özel gerçekleşmesidir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Evlerin önleri arasında kalan ve atıkların bırakıldığı açık alan, açıklık sonucunun adlaşmış uzantısıdır."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Bağırsağın çözülüp akarsu gibi boşalması, akış benzetmesine bağlı bedensel bir kullanımdır."}},{"facet_id":"F006","role":"source_variant","source_fields":["distinctive_facets[F006]"],"statements":{"statement":"Genişlik, kimi açıklamalarda su yatağına benzetilir; başka bir anlatımda aydınlıkla birlikte anılır."}},{"facet_id":"F007","role":"associated_use","source_fields":["distinctive_facets[F007]"],"statements":{"statement":"Tehlikeler için kullanılan bir biçim, iki ayrı söz öğesinin kaynaştırılmasıyla açıklanan tartışmalı bir türetmedir."}}],"root_ar":"ن ه ر","root_id":"root_001559","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın akış gerektirmeyen açma ve genişletme çekirdeğini temsil eder; akış yalnız uygun bağlamlardaki özel gerçekleşmelere aittir.","boundary_detail":"Akış, kan ve bağırsak kullanımlarında belirgindir; açık alan ve yarık genişletmede ise kurucu öğe açıklık veya genişliktir.","branch_image_ar":"فتح الشيء وتوسيعه حتى يسيل أو ينفسح","concept_gloss":"bir şeyi açma veya genişletme","contextual_glosses":[{"applicability":"Bir açıklık oluşturarak veya açılmış yeri serbest bırakarak kanın akmasını sağlama bağlamındadır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kanı açıp serbest bırakma işlemini ve ortaya çıkan akışı korur."},"facet_ids":["F002"],"text":"kanı akıttı","usage_role":"contextual"},{"applicability":"Yara, delik veya benzeri bir açıklığın daha geniş hale getirildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mevcut açıklığın genişletilmesi işlemini doğrudan korur."},"facet_ids":["F003"],"text":"yarığı genişletti","usage_role":"contextual"},{"applicability":"Evlerin ön bölümleri arasında kalan ve atık bırakılabilen belirli açık yeri açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yerleşim içindeki açık alanı ve evler arasındaki konumunu korur."},"facet_ids":["F004"],"text":"evler arasındaki açık alan","usage_role":"explanatory"}],"definition":"Bir şeyi açmak, yarığını genişletmek veya içindekini akacak biçimde serbest bırakmaktır. Bu çekirdek kan akıtma, yara açıklığını büyütme, açık alan, bağırsak boşalması ve genişlik ya da aydınlık benzetmelerinde özelleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin açılması, açılması için yarılması veya mevcut açıklığının genişletilmesi temel ilişkidir."},{"facet_id":"F002","role":"specialization","statement":"Kanı açılan bir yerden serbest bırakıp akıtma, çekirdeğin akış sonuçlu özel gerçekleşmesidir."},{"facet_id":"F003","role":"specialization","statement":"Bir yaranın veya yarığın açıklığını büyütmek, genişletme çekirdeğinin özel gerçekleşmesidir."},{"facet_id":"F004","role":"extension","statement":"Evlerin önleri arasında kalan ve atıkların bırakıldığı açık alan, açıklık sonucunun adlaşmış uzantısıdır."},{"facet_id":"F005","role":"associated_use","statement":"Bağırsağın çözülüp akarsu gibi boşalması, akış benzetmesine bağlı bedensel bir kullanımdır."},{"facet_id":"F006","role":"source_variant","statement":"Genişlik, kimi açıklamalarda su yatağına benzetilir; başka bir anlatımda aydınlıkla birlikte anılır."},{"facet_id":"F007","role":"associated_use","statement":"Tehlikeler için kullanılan bir biçim, iki ayrı söz öğesinin kaynaştırılmasıyla açıklanan tartışmalı bir türetmedir."}],"identity_rationale":"Kaynak ifadesinin çekirdeği bir şeyi açmak, yarığını genişletmek veya içindekini serbestçe akacak hale getirmektir. Geçici dal imgesi kullanılabilir, ancak her örnekte akış sonucu bulunmadığından genişleme ve açıklık yönü akıştan bağımsız olarak da korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"genişlik veya aydınlıkla birlikte genişlik"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kanı açıp serbest bırakarak akıttı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yaranın veya yarığın açıklığını genişletti"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"genişledi"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"evlerin önleri arasında atık bırakılan açık alan"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"bağırsağı çözüldü ve akarsu gibi boşaldı"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"tehlikeler; birleşik bir türetme olarak açıklanan biçim"}],"lexicalization_note":"Genel açılma ve genişleme çekirdeği korunur; kan, yara, açık alan ve bağırsak kullanımları kendi biçim ve yapılarına bağlanır.","neighbor_coverage_note":"Bütün adaylar açma, yayma, genişletme, tıkanma, daralma, bedensel açıklık ve kökün iç dalları bakımından değerlendirildi; dört yakın sınır seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal açmanın yanında genişlemeyi ve kimi yapılarda akışı kurucu sayar; komşu dal daha genel yarma ve açma eylemine, ayrıca kendine özgü canlı örneklerine uzanır.","focus_only":"Açıklığı büyütme ve içeriği akışa serbest bırakma yönü bulunur.","gloss":"yarıp açma","neighbor_only":"Karın yarma ve yavruyu çıkarmak için hayvanı açma gibi özel kapsamlar bulunur.","neighbor_ref":"root_000139/B002","relation_type":"near_synonym","shared_zone":"Bir nesnenin bütünlüğünü bozarak açıklık oluşturma iki dalın ortak çekirdeğidir."},{"boundary_match":"partial","distinction":"Odak dal açıklık oluşturma, yarığı büyütme ve akışa izin verme işlemlerini içerir; komşu dal ise ferahlık ve mekansal yayılma yönünde özelleşir.","focus_only":"Yarık açma ve içeriği akıtacak biçimde serbest bırakma bulunur.","gloss":"ferahlatıp genişletme","neighbor_only":"Bir yere ferahlık verme veya bir varlığa açılıp uzaklaşmasını söyleme bulunur.","neighbor_ref":"root_000549/B006","relation_type":"near_synonym","shared_zone":"Her iki dal bir şeyin alanını veya açıklığını büyütme düşüncesinde kesişir."},{"boundary_match":"partial","distinction":"Odak dal akış olmasa da açılma ve genişlemeyi kapsar; komşu dal geniş yarılma ile özellikle suyun patlayarak çıkmasını birlikte öne çıkarır.","focus_only":"Kan, yara, açık alan ve bağırsak gibi farklı yapılardaki genişleme kapsamı bulunur.","gloss":"geniş yarılıp fışkırma","neighbor_only":"Geniş yarılmayla suyun güçlü biçimde fışkırması ve bunun açıldığı yerler bulunur.","neighbor_ref":"root_001132/B001","relation_type":"near_synonym","shared_zone":"Geniş bir açıklığın oluşması ve bu açıklıktan akış çıkması ortak bölgedir."},{"boundary_match":"partial","distinction":"Odak dal işlemi ve durum değişimini anlatır; komşu dal ise bu değişimle ilişkilendirilen kalıcı su yatağını adlandırır.","focus_only":"Farklı nesnelerde gerçekleşen açma, genişletme veya serbest bırakma işlemidir.","gloss":"doğal akarsu yatağı","neighbor_only":"Bol suyu taşıyan, toprağı yarmış doğal arazi yatağıdır.","neighbor_ref":"root_001559/B001","relation_type":"near_neighbor","shared_zone":"Bir açıklığın su akışına yol vermesi ve yatağın yarılarak oluşması ortak imgedir."}],"source_phrase_ar":"أصل صحيح يدل على تفتح شيء أو فتحه (maqayis)؛ أنهرت الدم فتحته وأرسلته (maqayis)؛ أنهرت الدم أي أسلته (sihah;mufradat)؛ أنهرت الطعنة وسعتها وأنهر فتقها (sihah;tahdhib)؛ نهر من نهر الفتق (maqayis)؛ استنهر الشيء اتسع (sihah)؛ المنهرة فضاء يكون بين أفنية القوم (maqayis;sihah;mufradat)؛ أنهر بطنه إذا جاء بطنه مثل مجيء النهر (tahdhib)؛ النهر السعة تشبيها بنهر الماء وفي ضياء وسعة (mufradat;sihah;tahdhib)","source_summary":"Toplu kanıt açma ve genişletme çekirdeğini kanın akıtılması, yara açıklığının büyütülmesi ve bir şeyin genişlemesiyle kurar. Açık alan, bağırsak boşalması, genişlik ve aydınlık anlatımları ile birleşik türetme açıklaması bu çekirdeğin farklı uzantılarıdır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"فتح الشيء وتوسيعه؛ إسالة الدم؛ اتساع الطعنة والفتق؛ الفضاء بين الأفنية؛ مجيء البطن كمجيء النهر؛ تفسير النهر بالسعة أو الضياء والسعة","what_is_not_ar":"لا يدخل فيه النهر المائي بوصفه مجرى قائما؛ ولا النهار الزمني؛ ولا الزجر"},"support_links":["sup_d20a828d3bafbe44bdf2"]},{"boundary":"Dal genel kabalık, suç sayma veya salt susturma değildir; kişiye yöneltilen sert sözlü engelleme yapısıyla sınırlıdır.","branch_kind":"collocation","branch_ref":"root_001559/B004","candidate_links":[{"candidate_id":"cand_57af0f13050cb6883527","lane":"micro"},{"candidate_id":"cand_7f620634b137107139cb","lane":"micro"},{"candidate_id":"cand_bbfa194f69a0f03b8698","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَنْهَرْ","morph_features":"STEM|POS:V|IMPF|LEM:tanoharo|ROOT:nhr|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"93:10:4:1","qac_word_ref":"93:10:4","surface_ar":"تَنْهَرْ"}],"gloss":"sert sözle azarlayıp engelleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Muhataba sert ve azarlayıcı söz yönelterek onu kötü bir davranıştan caydırma eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylem, kişiyi doğrudan karşılayıp yüzüne karşı azarlama biçiminde gerçekleşebilir."}}],"root_ar":"ن ه ر","root_id":"root_001559","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiyi sert sözle karşılayıp davranışından caydırmayı amaçlayan yapı bağlı kullanımın tam karşılığıdır.","boundary_detail":"Dal genel kabalık, suç sayma veya salt susturma değildir; kişiye yöneltilen sert sözlü engelleme yapısıyla sınırlıdır.","branch_image_ar":"زجر بكلام مغلظ","concept_gloss":"sert sözle azarlayıp engelleme","contextual_glosses":[{"applicability":"Kişiye yüz yüze sert söz söylendiği, ancak caydırma amacı bağlamdan anlaşıldığı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kötü davranışı engelleme yönünü tek başına açıkça söylemez.","preserves":"Muhataba yöneltilen sert ve azarlayıcı konuşmayı korur."},"facet_ids":["F001","F002"],"text":"sertçe azarladı","usage_role":"contextual"}],"definition":"Bir kişiyi sert ve azarlayıcı sözle karşılayarak kötü bir davranıştan alıkoymaya veya caydırmaya çalışmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Muhataba sert ve azarlayıcı söz yönelterek onu kötü bir davranıştan caydırma eylemidir."},{"facet_id":"F002","role":"specialization","statement":"Eylem, kişiyi doğrudan karşılayıp yüzüne karşı azarlama biçiminde gerçekleşebilir."}],"identity_rationale":"Kaynak ifadesi, bir kişiyi sert ve azarlayıcı sözle karşılayarak kötü davranıştan caydırma eylemini tutarlı biçimde verir. Sertlik yalnız konuşma tarzı değil, muhataba yöneltilen engelleyici azarın kurucu parçasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"onu sert sözle azarlayıp engelledi"}],"lexicalization_note":"Anlam yalnız kişiye yöneltilen sert sözlü azarlama yapısında tanıklanır ve yalın bir kök anlamı olarak genellenmez.","neighbor_coverage_note":"Bütün adaylar azarlama, kınama, sözde sertlik, yüzüne karşı konuşma, susturma ve kökün diğer dalları bakımından değerlendirildi; üç işlevsel karşıtlık seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişiye yöneltilen sert sözlü azardır; komşu dal daha geniş biçimde insanı, hayvanı veya başka varlıkları sesle men etme, sürme ve ses çıkarma alanını kapsar.","focus_only":"Bir kişiyi sert ve yüzüne yöneltilen sözle caydırma sınırı bulunur.","gloss":"sesle azarlayıp uzaklaştırma","neighbor_only":"Hayvan, bulut veya başka varlıkları sesle sürme ve sesin kendisini adlandırma kapsamı bulunur.","neighbor_ref":"root_000624/B001","relation_type":"near_synonym","shared_zone":"Muhatabı ses veya söz yoluyla durdurma, caydırma ve geri çevirme ortaktır."},{"boundary_match":"partial","distinction":"Odak dal amaçlı bir azarlama eylemidir; komşu dal ise eylem gerektirmeyen genel bir sertlik ve kabalık niteliğidir.","focus_only":"Belirli bir muhatabı davranıştan caydırmaya yönelik sözlü eylemdir.","gloss":"sözde veya davranışta sertlik","neighbor_only":"Söz, davranış, buyruk veya cezanın genel sertlik niteliğini kapsar.","neighbor_ref":"root_001099/B002","relation_type":"near_neighbor","shared_zone":"Sertlik ve muhatap üzerinde baskı kuran konuşma iki dalda da bulunabilir."},{"boundary_match":"partial","distinction":"Odak dal davranışı engellemeye dönük sert azardır; komşu dal geçmiş bir suç veya kusur üzerinden kınama ve ayıplamayı öne çıkarır.","focus_only":"Sert sözle anlık olarak durdurma veya caydırma amacı bulunur.","gloss":"suçundan dolayı kınama","neighbor_only":"İşlenmiş suçu sayıp dökme, ayıplama ve uzun uzadıya kınama bulunur.","neighbor_ref":"root_000197/B001","relation_type":"near_neighbor","shared_zone":"Muhataba olumsuz değerlendirme içeren ağır söz yöneltme ortak alandır."}],"source_phrase_ar":"نهرت الرجل نهرا وانتهرته انتهارا زجرته بكلام عن شر (ayn)؛ نهره وانتهره أي زبره (sihah)؛ نهرته وانتهرته إذا استقبلته بكلام تزجره (tahdhib)؛ النهر والانتهار الزجر بمغالظة (mufradat)","source_summary":"Kaynaklar, bir kişiye sert sözle yöneltilen azarlama ve engellemeyi ortak çekirdek olarak verir. Doğrudan karşılayarak konuşma, eylemin yüz yüze gerçekleşebilen biçimini belirginleştirir.","sources":["AY","SI","TA","MU"],"what_is_ar":"نهر الرجل وانتهره إذا زجره أو زبره بكلام شديد؛ الانتهار بمعنى الاستقبال بالزجر","what_is_not_ar":"لا يدخل فيه النهر المائي؛ ولا النهار؛ ولا مجرد فتح الشيء أو توسعته"},"support_links":["sup_71f2d85ce6878ed9ad8b","sup_8bf3197d0d7a31cd678b","sup_c57219c5168b9007bb0d"]},{"boundary":"Bu ad genel olarak bütün yavruları kapsamaz; tanıklanan bazı kuşlarla sınırlıdır ve tür aktarımı kaynaklar arasında değişir.","branch_kind":"bare","branch_ref":"root_001559/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَنْهَرْ","morph_features":"STEM|POS:V|IMPF|LEM:tanoharo|ROOT:nhr|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"93:10:4:1","qac_word_ref":"93:10:4","surface_ar":"تَنْهَرْ"}],"gloss":"bazı kuşların yavrusu","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Söz, genel yavru adı değil, bazı kuşların yavrusu için kullanılan sınırlı bir addır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yavrunun ait olduğu kuş, aktarımlarda bağırtlak türleri, kartal veya toy kuşu olarak farklı biçimlerde belirtilir."}}],"root_ar":"ن ه ر","root_id":"root_001559","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Türü kaynak aktarımına göre değişen, ancak kuş yavrusu olma çekirdeği sabit kalan dalın en kısa karşılığıdır.","boundary_detail":"Bu ad genel olarak bütün yavruları kapsamaz; tanıklanan bazı kuşlarla sınırlıdır ve tür aktarımı kaynaklar arasında değişir.","branch_image_ar":"النَّهار فرخ طير","concept_gloss":"bazı kuşların yavrusu","contextual_glosses":[{"applicability":"Kuş türünün metinde ayrıca belirtildiği veya tarihsel adın yalnız yavru oluşunun önemli olduğu bağlamlarda kullanılır.","error_profile":{"adds":"Tanıklanmayan bütün kuş türlerini kapsayabilecek genel bir alan açar.","collision":"Sınırlı tarihsel ad ile genel kuş yavrusu ifadesi karışabilir.","fit":"broadening","loses":null,"preserves":"Canlının bir kuş yavrusu olduğu temel bilgiyi korur."},"facet_ids":["F001"],"text":"kuş yavrusu","usage_role":"contextual"}],"definition":"Bazı kuşların yavrusu için kullanılan bir addır; hangi kuş türünü gösterdiği konusunda aktarımlar bağırtlak türleri, kartal ve toy kuşu arasında değişir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Söz, genel yavru adı değil, bazı kuşların yavrusu için kullanılan sınırlı bir addır."},{"facet_id":"F002","role":"source_variant","statement":"Yavrunun ait olduğu kuş, aktarımlarda bağırtlak türleri, kartal veya toy kuşu olarak farklı biçimlerde belirtilir."}],"identity_rationale":"Kaynak ifadesi sözü bazı kuşların yavrusu olarak doğrular, ancak kuş türünü tekleştirmez. Aktarımlar bağırtlak türleri, kartal ve toy kuşu arasında değiştiği için dal kuş yavrusu çekirdeğinde tutulmalı, belirli bir türe indirgenmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"türü aktarıma göre değişen bir kuş yavrusu"}],"lexicalization_note":"Tanım yalın biçimin bazı kuş yavruları için kullanımını verir; komşu dallardaki belirli tür adları buraya taşınmaz.","neighbor_coverage_note":"Bütün adaylar kuş türü, genel yavruluk, başka hayvan adları ve kökün iç dalları bakımından değerlendirildi; tür sınırını açıklayan üç komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın tür aktarımı birden çok ve uyuşmaz kuşu kapsar; komşu dal ise keklik ve bağırtlak yavrularını, ayrıca cinsiyete göre biçimleriyle sınırlar.","focus_only":"Aktarıma göre kartal veya toy kuşu yavrusunu da gösterebilen değişken kapsam bulunur.","gloss":"keklik veya bağırtlak yavrusu","neighbor_only":"Erkek ve dişi için ayrı biçimler ile keklik yavrusu kapsamı bulunur.","neighbor_ref":"root_000735/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da bağırtlak türlerinin yavrularını gösterebilir."},{"boundary_match":"field_only","distinction":"Odak dalın tanıklanan türleri arasında keklik kesin biçimde yer almaz ve aktarım değişkendir; komşu dal doğrudan keklik yavrusuna özgüdür.","focus_only":"Birden fazla kuş türüne ilişkin değişken tarihsel aktarım bulunur.","gloss":"keklik yavrusu","neighbor_only":"Yalnız keklik yavrusunu gösteren belirli bir ad bulunur.","neighbor_ref":"root_000728/B007","relation_type":"same_field","shared_zone":"İki dal da belirli kuşların yavruları için kullanılan özel adlardır."},{"boundary_match":"partial","distinction":"Odak dal bazı kuş türleriyle sınırlı özel bir addır; komşu dal ise insan ve hayvan yavrularına yayılabilen genel bir yaş ve küçüklük adıdır.","focus_only":"Yalnız bazı kuş türlerinin yavrularına ait tarihsel bir ad olma sınırı bulunur.","gloss":"küçük yavru","neighbor_only":"İnsan, evcil hayvan ve yabani hayvan yavrularını kapsayan genel küçüklük alanı bulunur.","neighbor_ref":"root_000942/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da henüz yetişkin olmayan bir canlı yavrusunu gösterebilir."}],"source_phrase_ar":"النهار فرخ القطا والغطاط والعقاب ونحوه وثلاثة أنهرة (ayn)؛ النهار فرخ الحبارى (sihah;tahdhib;mufradat)؛ النهار فرخ بعض الطير مما لا يعرج على مثله ولا معنى له (maqayis)","source_summary":"Toplu kanıt sözü bazı kuşların yavrusu olarak ortaklaştırır, fakat tür konusunda ayrışır. Aktarılan türler bağırtlak benzeri kuşlardan kartala ve toy kuşuna kadar değiştiği için tek bir kuş belirlemek mümkün değildir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"النَّهار اسما لفرخ بعض الطير؛ فرخ القطا أو الغطاط أو العقاب أو الحبارى بحسب نقل المصادر","what_is_not_ar":"لا يدخل فيه النهار الزمني؛ ولا النهر المائي؛ ولا الزجر"},"support_links":[]},{"boundary":"Dalın odağı fırsatçı ve ani kapmadır; salt gizlilik, genel hırsızlık veya her türlü kandırma yeterli değildir.","branch_kind":"bare","branch_ref":"root_001559/B006","candidate_links":[{"candidate_id":"cand_bbfa194f69a0f03b8698","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَنْهَرْ","morph_features":"STEM|POS:V|IMPF|LEM:tanoharo|ROOT:nhr|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"93:10:4:1","qac_word_ref":"93:10:4","surface_ar":"تَنْهَرْ"}],"gloss":"fırsat kollayıp gizlice kapma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi karşı taraf hazırlıksızken ani bir atılışla kapma eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylem, fırsat kollama ve kapmayı fark ettirmeden gerçekleştirme yönü taşır."}}],"root_ar":"ن ه ر","root_id":"root_001559","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ani atılış, karşı tarafın hazırlıksızlığı ve fırsatçı kapma bileşenlerini birlikte karşılar.","boundary_detail":"Dalın odağı fırsatçı ve ani kapmadır; salt gizlilik, genel hırsızlık veya her türlü kandırma yeterli değildir.","branch_image_ar":"الدغرة والخلسة","concept_gloss":"fırsat kollayıp gizlice kapma","contextual_glosses":[{"applicability":"Bir şeyin karşı taraf hazırlıksızken ani ve fark ettirilmeden alındığı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kapmanın gizli, ani ve fırsattan yararlanan biçimini korur."},"facet_ids":["F001","F002"],"text":"gizlice kapıverme","usage_role":"contextual"}],"definition":"Bir fırsatı kollayıp ani bir atılışla bir şeyi gizlice veya karşı taraf hazırlıksızken kapma eylemidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi karşı taraf hazırlıksızken ani bir atılışla kapma eylemidir."},{"facet_id":"F002","role":"specialization","statement":"Eylem, fırsat kollama ve kapmayı fark ettirmeden gerçekleştirme yönü taşır."}],"identity_rationale":"Tek kaynak ifadesi anlamı ani bir atılışla, fırsattan yararlanarak gizlice kapma olarak verir. Bu çekirdek genel hırsızlıktan, uzun süreli hileden ve öldürücü gizli saldırıdan daha dardır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"fırsat kollayıp ani biçimde gizlice kapma"}],"lexicalization_note":"Tanım, yalın biçimin ani ve fırsatçı kapma anlamıyla sınırlıdır; komşu hile ve hırsızlık yapıları içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar hız, gizlilik, fırsat kollama, hile, hırsızlık, öldürücü sonuç ve kökün iç dalları bakımından değerlendirildi; üç yakın sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal fırsat kollama ve gizli ani atılışla sınırlıdır; komşu dal hızla kapma çekirdeğinden çok daha geniş nesne ve sonuçlara uzanır.","focus_only":"Karşı tarafın hazırlıksızlığından yararlanan fırsatçı atılış öne çıkar.","gloss":"hızla kapıp alma","neighbor_only":"Hızlı koparıp alma yanında işitme, görme, baş alma ve yağmalama uzantıları bulunur.","neighbor_ref":"root_000423/B001","relation_type":"near_synonym","shared_zone":"Bir şeyi hızlı ve beklenmedik biçimde ele geçirme iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal bu fırsatı ani bir kapma eylemiyle sonuçlandırır; komşu dal ise dalgınlığı kullanma yöntemini anlatır ve belirli bir alma sonucu gerektirmez.","focus_only":"Fırsat sonunda bir şeyi ani biçimde kapma sonucu bulunur.","gloss":"dalgınlıktan yararlanma","neighbor_only":"Karşı tarafın dalgınlığını kullanma, herhangi bir kapma sonucu olmadan da bulunabilir.","neighbor_ref":"root_001097/B005","relation_type":"near_neighbor","shared_zone":"Karşı tarafın hazırlıksız veya dikkatsiz anından yararlanma ortaktır."},{"boundary_match":"partial","distinction":"Odak dal ani kapmayla sınırlı kalır; komşu dal gizli ele geçirmeyi öldürme, yok etme ya da gücü giderme gibi ağır sonuçlarla birleştirir.","focus_only":"Ani ve fırsatçı kapma, öldürme veya yok etme gerektirmez.","gloss":"gizlice ele geçirip yok etme","neighbor_only":"Gizlice öldürme, yok etme veya güç ve bilinci giderme sonuçları bulunur.","neighbor_ref":"root_001115/B001","relation_type":"near_neighbor","shared_zone":"Eylemin hedefçe önceden fark edilmemesi ve gizli gerçekleşmesi ortaktır."}],"source_phrase_ar":"النهر الدغرة وهي الخلسة (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Ani atılışla fırsatçı kapma anlamı bu dalda tek kaynaklı bir tanıklığa dayanır."}],"source_summary":"Bu dal için ortaklaştırılabilecek çok kaynaklı bir anlatım yoktur; kanıt ani ve gizlice kapma anlamını tek başına tanıklar.","sources":["TA"],"what_is_ar":"النهر بمعنى الدغرة؛ الدغرة هي الخلسة","what_is_not_ar":"لا يدخل فيه الزجر؛ ولا جريان الماء؛ ولا فتح الدم أو الطعنة"},"support_links":["sup_c57219c5168b9007bb0d"]},{"boundary":"Dal yalnız belirtilen özel-ad kullanımlarını kapsar; zaman, su yatağı veya yıldızların genel tür anlamı buraya aktarılmaz.","branch_kind":"non_bare","branch_ref":"root_001559/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَنْهَرْ","morph_features":"STEM|POS:V|IMPF|LEM:tanoharo|ROOT:nhr|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"93:10:4:1","qac_word_ref":"93:10:4","surface_ar":"تَنْهَرْ"}],"gloss":"kişi, yer ve yıldızlara ait özel adlar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dal, ortak bir tür anlamı değil, belirli varlıkları gösteren sınırlı bir özel-ad kümesini temsil eder."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kümedeki kullanımlardan biri belirli bir topluluktan bir şairin adıdır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kümedeki kullanımlardan biri belirli bir yerin adıdır."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kümedeki kullanımlardan biri sularının bolluğu gerekçesiyle iki yıldız için kullanılan ortak addır."}}],"root_ar":"ن ه ر","root_id":"root_001559","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın heterojen üyelerini ortak anlam uydurmadan, yalnız belirli varlıkları gösteren adlar olarak temsil eder.","boundary_detail":"Dal yalnız belirtilen özel-ad kullanımlarını kapsar; zaman, su yatağı veya yıldızların genel tür anlamı buraya aktarılmaz.","branch_image_ar":"أعلام وأسماء خاصة","concept_gloss":"kişi, yer ve yıldızlara ait özel adlar","contextual_glosses":[{"applicability":"Kümedeki kişi adının, yazımı ayrıca üretilmeden yalnız işlevinin açıklanması gereken bağlam içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Adın belirli bir şairi gösteren kişi adı olmasını korur."},"facet_ids":["F002"],"text":"bir şairin adı","usage_role":"explanatory"},{"applicability":"Kümedeki yer adının, yüzey biçimi verilmeden yalnız adlandırma işlevinin açıklandığı bağlam içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Adın belirli bir yeri gösteren özel ad olmasını korur."},"facet_ids":["F003"],"text":"bir yer adı","usage_role":"explanatory"},{"applicability":"Sularının bolluğuyla ilişkilendirilen iki yıldız için kullanılan ortak adın işlevini açıklar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki yıldızı birlikte adlandırmayı ve ortak ad ilişkisini korur."},"facet_ids":["F004"],"text":"iki yıldızın ortak adı","usage_role":"explanatory"}],"definition":"Aynı sözlük maddesinde yer alan, bir şairi, bir yeri ve sularının bolluğu gerekçesiyle iki yıldızı gösteren birbirinden ayrı özel ad kullanımlarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dal, ortak bir tür anlamı değil, belirli varlıkları gösteren sınırlı bir özel-ad kümesini temsil eder."},{"facet_id":"F002","role":"example","statement":"Kümedeki kullanımlardan biri belirli bir topluluktan bir şairin adıdır."},{"facet_id":"F003","role":"example","statement":"Kümedeki kullanımlardan biri belirli bir yerin adıdır."},{"facet_id":"F004","role":"example","statement":"Kümedeki kullanımlardan biri sularının bolluğu gerekçesiyle iki yıldız için kullanılan ortak addır."}],"identity_rationale":"Kaynak ifadesi bir şairin adı, bir yer adı ve sularının bolluğu gerekçesiyle iki yıldız için kullanılan ortak adı aynı özel-ad kümesinde toplar. Küme geçerlidir, ancak üyeler ortak bir kavramın örnekleri değil, yalnız aynı sözlük maddesinde bulunan ayrı özel adlardır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"belirli bir topluluktan bir şairin adı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bir yer adı"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"sularının bolluğu nedeniyle iki yıldız için kullanılan ortak ad"}],"lexicalization_note":"Tanım yalnız kanıtta verilen kişi, yer ve iki yıldızın ortak adıyla sınırlıdır; bunlardan genel bir yalın anlam çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar kişi, yer, topluluk, gök adı ve kökün anlam dalları bakımından değerlendirildi; yalnız özel-ad sınıfını paylaşan üç aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Dallar yalnız özel-ad alanını paylaşır; gösterdikleri kişi, yer ve gök varlıkları bütünüyle farklı olduğundan birbirlerinin yerine kullanılamaz.","focus_only":"Belirli bir şair, belirli bir yer ve iki yıldızın ortak adından oluşan kapalı liste bulunur.","gloss":"başka kişi, yer ve gök adları","neighbor_only":"Başka kişileri, yerleri ve tek bir gök cismini gösteren ayrı bir ad kümesi bulunur.","neighbor_ref":"root_000333/B012","relation_type":"same_field","shared_zone":"Her iki dal da kişi, yer veya gök varlığı gösteren özel adları toplar."},{"boundary_match":"field_only","distinction":"Ortaklık yalnız ad türündedir; her dal farklı varlıkları gösteren kapalı bir ad listesine sahip olduğu için anlamsal ikame yoktur.","focus_only":"Bir şair, bir yer ve iki yıldıza ilişkin üç ayrı ad kullanımı bulunur.","gloss":"başka kişi ve yer adları","neighbor_only":"Başka bir yer ile şiir tanığındaki başka bir kişiye ait adlar bulunur.","neighbor_ref":"root_001694/B010","relation_type":"same_field","shared_zone":"Her iki dal kişi ve yerleri gösteren özel ad kullanımlarını içerir."},{"boundary_match":"field_only","distinction":"Odak dal üç belirli kullanımın kapalı kümesidir; komşu dal başka biçimlerden türemiş ayrı kişi ve yer adlarını kapsar.","focus_only":"İki yıldız için kullanılan ortak ad ve bu dala özgü kişi ile yer adı bulunur.","gloss":"başka türemiş kişi ve yer adları","neighbor_only":"Başka bir söz ailesinden türemiş çok sayıda kişi ve yer adı bulunur.","neighbor_ref":"root_000943/B007","relation_type":"same_field","shared_zone":"Her iki dal sözlükteki biçimlerden doğan kişi ve yer adlarını bir araya getirir."}],"source_phrase_ar":"نهار بن توسعة اسم شاعر من تميم (sihah)؛ نهروان بلد (sihah)؛ العرب تسمي العواء والسماك الأنهرين لكثرة مائهما (tahdhib)","source_summary":"Toplu kanıt üç ayrı özel-ad kullanımını bir araya getirir: bir şair, bir yer ve sularının bolluğuyla ilişkilendirilen iki yıldızın ortak adı. Bu üyeler arasında özel ad olmanın dışında ortak bir sözlük anlamı kurulmaz.","sources":["SI","TA"],"what_is_ar":"الأعلام والأسماء الخاصة الواردة في المادة؛ نهار بن توسعة اسما لشاعر؛ نهروان اسما لبلد؛ الأنهران اسما للعواء والسماك لكثرة مائهما","what_is_not_ar":"لا يدخل فيه النهار الزمن ولا النهر المجرى إلا إذا كان الاسم معللا بهما"},"support_links":[]},{"boundary":"Dal yalnız bulut adıdır; su yatağı, aydınlık gündüz veya belirli bulut türlerinin ek özellikleri tanıma girmez.","branch_kind":"bare","branch_ref":"root_001559/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَنْهَرْ","morph_features":"STEM|POS:V|IMPF|LEM:tanoharo|ROOT:nhr|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"93:10:4:1","qac_word_ref":"93:10:4","surface_ar":"تَنْهَرْ"}],"gloss":"bulut","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gökyüzündeki bulutu herhangi bir tür özelliği eklemeden adlandırır."}}],"root_ar":"ن ه ر","root_id":"root_001559","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli bir tür, büyüklük, yağış veya oluşma zamanı eklemeden dalın genel gökyüzü varlığını karşılar.","boundary_detail":"Dal yalnız bulut adıdır; su yatağı, aydınlık gündüz veya belirli bulut türlerinin ek özellikleri tanıma girmez.","branch_image_ar":"النَّاهُور سحاب","concept_gloss":"bulut","contextual_glosses":[{"applicability":"Yalın biçimin cümle içinde sayılabilir tek bir gökyüzü bulutunu gösterdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Herhangi bir tür niteliği eklemeden tek bir bulutu gösterir."},"facet_ids":["F001"],"text":"bir bulut","usage_role":"general"}],"definition":"Gökyüzünde görülen bulut için kullanılan yalın bir addır; tanıklık belirli bir bulut türü veya hava olayıyla sınır koymaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gökyüzündeki bulutu herhangi bir tür özelliği eklemeden adlandırır."}],"identity_rationale":"Tek kaynak ifadesi yalın biçimi doğrudan bulut olarak tanımlar. Bulutun inceliği, su taşıması, kalıcılığı veya günün belirli vaktinde oluşması gibi ek bir özellik verilmediğinden dal genel bulut anlamında tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"bulut"}],"lexicalization_note":"Tanım yalın biçimin genel bulut anlamını verir; komşu dallardaki incelik, büyüklük, yağış veya zaman özelliklerini içeri almaz.","neighbor_coverage_note":"Bütün adaylar bulut türü, biçim, yağış, hareket, büyüklük, oluşma zamanı ve kökün iç dalları bakımından değerlendirildi; üç yakın bulut komşusu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnız genel bulut adıdır; komşu dal bulutun parçasına, yağmura, doluya ve bunlarla ilgili türemiş kullanımlara uzanır.","focus_only":"Ek nitelik taşımayan tek ve genel bir bulut adı bulunur.","gloss":"bulut ve yağış bulutu","neighbor_only":"Bulut parçası, yağmur, dolu ve bunlardan türeyen kullanımlar da kapsama girer.","neighbor_ref":"root_001419/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın çekirdeğinde gökyüzündeki bulut bulunur."},{"boundary_match":"partial","distinction":"Odak dal genel buluttur; komşu dal ise görünüşü dağa benzeyen, ince ve çoğu aktarımda su taşımayan belirli bir bulut türüdür.","focus_only":"Bulutun inceliği, biçimi veya su taşıması konusunda bir sınırlama yoktur.","gloss":"ince ve su taşımayan bulut","neighbor_only":"İnce, dağ gibi karşıdan görünen ve çoğu anlatımda su taşımayan bulut olma sınırı vardır.","neighbor_ref":"root_000252/B005","relation_type":"near_synonym","shared_zone":"Her iki dal gökyüzünde görülen bir bulutu adlandırır."},{"boundary_match":"partial","distinction":"Odak dal niteliksiz genel addır; komşu dal bir yerde oyalanan, yavaş hareket eden ve su yüküyle ilişkilendirilen özel bulut türüdür.","focus_only":"Bulutun hareketi, kalış süresi veya su miktarı belirtilmez.","gloss":"yavaş ve kalıcı bulut","neighbor_only":"Bir yerde kalan, ağır ilerleyen ve çok su taşıyabilen bulut olma niteliği bulunur.","neighbor_ref":"root_000902/B007","relation_type":"near_synonym","shared_zone":"Her iki dal tek bir bulut varlığını gösterebilir."}],"source_phrase_ar":"الناهُور السحاب (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Genel bulut anlamı bu dalda tek kaynaklı ve ek niteliksiz bir tanıklığa dayanır."}],"source_summary":"Bu dal için ortaklaştırılabilecek çok kaynaklı bir anlatım yoktur; kanıt yalın biçimin genel bulut anlamını tek başına tanıklar.","sources":["TA"],"what_is_ar":"النَّاهُور اسما للسحاب","what_is_not_ar":"لا يدخل فيه النهر المائي؛ ولا النهار؛ ولا الأعلام الخاصة"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["93:10:1"],"branch_refs":[],"candidate_id":"cand_5071e33f4f5aea35766e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:10:1:coordinated-paired-case","source_type":"word_analysis","support_ids":["sup_318019b696cf82e658b3","sup_6e5a4187b5ecfe8728ef"],"title":"second coordinated case in the sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:1","qac_refs":["93:10:1:1"],"status":"accepted"}},{"anchor_refs":["93:10:1"],"branch_refs":[],"candidate_id":"cand_dd2ce39e707bfaed7ab7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:10:1:fused-wa-amma-onset","source_type":"word_analysis","support_ids":["sup_318019b696cf82e658b3","sup_aa5416be295c167677fa"],"title":"fused continuation and case marker","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:1","qac_refs":["93:10:1:1"],"status":"accepted"}},{"anchor_refs":["93:10:2"],"branch_refs":[],"candidate_id":"cand_293f6d89014a375b48b0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:10:2:case-response-frame","source_type":"word_analysis","support_ids":["sup_1d26178b8b6a5980bae6","sup_9f34733efd4ad8bd22e6"],"title":"case marker requiring a response","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:2","qac_refs":["93:10:1:2"],"status":"accepted"}},{"anchor_refs":["93:10:2"],"branch_refs":[],"candidate_id":"cand_db1066b88da4f768fce2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:10:2:three-case-series","source_type":"word_analysis","support_ids":["sup_1d26178b8b6a5980bae6","sup_d1573360ab2171e9b08d"],"title":"middle member of a same-surah series","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:2","qac_refs":["93:10:1:2"],"status":"accepted"}},{"anchor_refs":["93:10:3"],"branch_refs":[],"candidate_id":"cand_df49d0a3a317c6972d36","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:10:3:boundary-and-sound-marking","source_type":"word_analysis","support_ids":["sup_2f4a09a651a2adddcab9","sup_ae09893626cf781a5f84"],"title":"marked transition into the requester word","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:3","qac_refs":["93:10:2:1","93:10:2:2"],"status":"accepted"}},{"anchor_refs":["93:10:3"],"branch_refs":[],"candidate_id":"cand_2bd12d5a6d97d7947d24","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:10:3:broad-asking-register","source_type":"word_analysis","support_ids":["sup_07a230c5c582d0d7378f","sup_2f4a09a651a2adddcab9"],"title":"petitioner and questioner both remain protected","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:3","qac_refs":["93:10:2:1","93:10:2:2"],"status":"accepted"}},{"anchor_refs":["93:10:3"],"branch_refs":[],"candidate_id":"cand_5e1605ceb4d99aba945c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:10:3:daylight-setting-echo","source_type":"word_analysis","support_ids":["sup_2f4a09a651a2adddcab9","sup_f091ade4af5927dede8b"],"title":"public visibility echo from the surah opening","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:3","qac_refs":["93:10:2:1","93:10:2:2"],"status":"accepted"}},{"anchor_refs":["93:10:3"],"branch_refs":[],"candidate_id":"cand_708cf9aeb7f1f0b1dfd4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:10:3:definite-active-participle-category","source_type":"word_analysis","support_ids":["sup_2c33f4aa340ea7002a7f","sup_2f4a09a651a2adddcab9"],"title":"definite active-participle role","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:3","qac_refs":["93:10:2:1","93:10:2:2"],"status":"accepted"}},{"anchor_refs":["93:10:3"],"branch_refs":[],"candidate_id":"cand_729c0cd52f6949e3e2be","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:10:3:flow-image-narrowed","source_type":"word_analysis","support_ids":["sup_2f4a09a651a2adddcab9","sup_f2dc15fcc4d270535f95"],"title":"asking as outward movement, not selected flow sense","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:3","qac_refs":["93:10:2:1","93:10:2:2"],"status":"accepted"}},{"anchor_refs":["93:10:3"],"branch_refs":[],"candidate_id":"cand_a6130c5e2d5a1ed45ded","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:10:3:fronted-protected-object","source_type":"word_analysis","support_ids":["sup_24885614b0a539d15d88","sup_2f4a09a651a2adddcab9"],"title":"fronted object before the forbidden act","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:3","qac_refs":["93:10:2:1","93:10:2:2"],"status":"accepted"}},{"anchor_refs":["93:10:3"],"branch_refs":[],"candidate_id":"cand_47e9ab6c45174022f2ce","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:10:3:orphan-to-asker-progression","source_type":"word_analysis","support_ids":["sup_2f4a09a651a2adddcab9","sup_c7e1b49e663dae547ec7"],"title":"from deprivation to active seeking","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:3","qac_refs":["93:10:2:1","93:10:2:2"],"status":"accepted"}},{"anchor_refs":["93:10:3"],"branch_refs":[],"candidate_id":"cand_8fcf9ad86de02b2e19a5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:10:3:right-bearing-requester-echo","source_type":"word_analysis","support_ids":["sup_2f4a09a651a2adddcab9","sup_d0ad99b88cb1e3d560a1"],"title":"requester with a social right","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:3","qac_refs":["93:10:2:1","93:10:2:2"],"status":"accepted"}},{"anchor_refs":["93:10:4"],"branch_refs":[],"candidate_id":"cand_a1d3e3d13f954ad109b0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:10:4:compact-fa-la-parallel","source_type":"word_analysis","support_ids":["sup_85a900d35fc020a98a0b","sup_e234f179e61bc5d38d10"],"title":"compact repeated prohibition gateway","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:4","qac_refs":["93:10:3:1"],"status":"accepted"}},{"anchor_refs":["93:10:4"],"branch_refs":[],"candidate_id":"cand_6d4e447606190b7b7cb1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:10:4:required-apodosis-hinge","source_type":"word_analysis","support_ids":["sup_85a900d35fc020a98a0b","sup_8d2f951c60a74912373a"],"title":"required answer to the case frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:4","qac_refs":["93:10:3:1"],"status":"accepted"}},{"anchor_refs":["93:10:5"],"branch_refs":[],"candidate_id":"cand_248a1d5ec787192558d2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:10:5:compact-prohibition-cadence","source_type":"word_analysis","support_ids":["sup_537df56406ed492c4acb","sup_d628bcc4c0d66da3a6b3"],"title":"compact falling prohibition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:5","qac_refs":["93:10:3:2"],"status":"accepted"}},{"anchor_refs":["93:10:5"],"branch_refs":[],"candidate_id":"cand_5b2b4c3d446eabe04d1e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:10:5:paired-negative-boundary","source_type":"word_analysis","support_ids":["sup_537df56406ed492c4acb","sup_b5ed1b6933a2223d7861"],"title":"paired negative ethical boundary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:5","qac_refs":["93:10:3:2"],"status":"accepted"}},{"anchor_refs":["93:10:5"],"branch_refs":[],"candidate_id":"cand_916f95d6106392b80d49","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:10:5:prohibitive-la-jussive","source_type":"word_analysis","support_ids":["sup_0ff32cb75d03716930df","sup_537df56406ed492c4acb"],"title":"direct negative command","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:5","qac_refs":["93:10:3:2"],"status":"accepted"}},{"anchor_refs":["93:10:6"],"branch_refs":[],"candidate_id":"cand_c25d80c95b8e1ed55659","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001559"],"scope":"focus_ayah","source_local_id":"93:10:6:boundary-harm-shift","source_type":"word_analysis","support_ids":["sup_220e4bf6e12df41f34f1","sup_af081e0f7c8fd4ef055e"],"title":"from overpowering to harsh speech","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:6","qac_refs":["93:10:4:1"],"status":"accepted"}},{"anchor_refs":["93:10:6"],"branch_refs":[],"candidate_id":"cand_b9834b1f3baa2a389b93","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001559"],"scope":"focus_ayah","source_local_id":"93:10:6:convergence-of-grammar-image-and-sound","source_type":"word_analysis","support_ids":["sup_220e4bf6e12df41f34f1","sup_838d944caf9c8276a675"],"title":"grammar, root pressure, and rhyme converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:6","qac_refs":["93:10:4:1"],"status":"accepted"}},{"anchor_refs":["93:10:6"],"branch_refs":[],"candidate_id":"cand_679fc3b237fc28d236bd","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001559"],"scope":"focus_ayah","source_local_id":"93:10:6:direct-second-person-jussive","source_type":"word_analysis","support_ids":["sup_220e4bf6e12df41f34f1","sup_598d6fee730c4780b696"],"title":"direct addressee under prohibitive jussive","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:6","qac_refs":["93:10:4:1"],"status":"accepted"}},{"anchor_refs":["93:10:6"],"branch_refs":[],"candidate_id":"cand_9ad601200f7eb556a0d2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001559"],"scope":"focus_ayah","source_local_id":"93:10:6:fronted-object-completion","source_type":"word_analysis","support_ids":["sup_220e4bf6e12df41f34f1","sup_e418c6d970a91ac271d4"],"title":"closing verb completes the earlier object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:6","qac_refs":["93:10:4:1"],"status":"accepted"}},{"anchor_refs":["93:10:6"],"branch_refs":[],"candidate_id":"cand_9ee0accfc251b0ebde28","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001559"],"scope":"focus_ayah","source_local_id":"93:10:6:harsh-rebuke-not-mere-refusal","source_type":"word_analysis","support_ids":["sup_220e4bf6e12df41f34f1","sup_a8021d2c3bacac219926"],"title":"harsh verbal repulsion is the selected sense","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:6","qac_refs":["93:10:4:1"],"status":"accepted"}},{"anchor_refs":["93:10:6"],"branch_refs":[],"candidate_id":"cand_2a196fb2f9d658b600ca","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001559"],"scope":"focus_ayah","source_local_id":"93:10:6:negative-to-positive-speech-handoff","source_type":"word_analysis","support_ids":["sup_220e4bf6e12df41f34f1","sup_3da2c695bcd10bbd0373"],"title":"speech restraint before positive proclamation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:6","qac_refs":["93:10:4:1"],"status":"accepted"}},{"anchor_refs":["93:10:6"],"branch_refs":[],"candidate_id":"cand_4a2241fb0b676a367f92","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001559"],"scope":"focus_ayah","source_local_id":"93:10:6:prospective-command-form","source_type":"word_analysis","support_ids":["sup_220e4bf6e12df41f34f1","sup_75076ac1830a9744e90e"],"title":"possible action barred before it happens","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:6","qac_refs":["93:10:4:1"],"status":"accepted"}},{"anchor_refs":["93:10:6"],"branch_refs":[],"candidate_id":"cand_97ce808cd7fc431c627a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001559"],"scope":"focus_ayah","source_local_id":"93:10:6:rare-verbal-use-and-parent-parallel","source_type":"word_analysis","support_ids":["sup_220e4bf6e12df41f34f1","sup_d7d8dff49465e539e8ed"],"title":"rare verbal prohibition set","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:6","qac_refs":["93:10:4:1"],"status":"accepted"}},{"anchor_refs":["93:10:6"],"branch_refs":[],"candidate_id":"cand_f58ebcf14d1ac85c2c58","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001559"],"scope":"focus_ayah","source_local_id":"93:10:6:root-image-pressure-narrowed","source_type":"word_analysis","support_ids":["sup_220e4bf6e12df41f34f1","sup_5ee0b5c193d132d377fd"],"title":"river, channel, and exposure pressure around rebuke","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:6","qac_refs":["93:10:4:1"],"status":"accepted"}},{"anchor_refs":["93:10:6"],"branch_refs":[],"candidate_id":"cand_36de5a0183b0f9cee13d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001559"],"scope":"focus_ayah","source_local_id":"93:10:6:sound-and-final-closure","source_type":"word_analysis","support_ids":["sup_220e4bf6e12df41f34f1","sup_4738060eb4d1923e91ff"],"title":"final clipped near-rhyme with the prior command","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:10:6","qac_refs":["93:10:4:1"],"status":"accepted"}},{"anchor_refs":["93:10:2"],"branch_refs":[],"candidate_id":"cand_b98fc7d790695661b0ae","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000661","root_000736"],"scope":"focus_ayah","source_local_id":"93:10:2:2","source_type":"qac_morpheme","support_ids":["sup_f610a05d7765b9b79c65"],"title":"QAC root occurrence: س ء ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["93:10:4"],"branch_refs":[],"candidate_id":"cand_62deaa6cd5084e1ba9b2","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001559"],"scope":"focus_ayah","source_local_id":"93:10:4:1","source_type":"qac_morpheme","support_ids":["sup_c259eaeaac6687af2fa9"],"title":"QAC root occurrence: ن ه ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["93:10"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:10","branch_refs":["root_000661/B001","root_001559/B004"],"candidate_id":"cand_57af0f13050cb6883527","commentary_obligation":"review","hft_ref":"hft_95a59e3ee9dfc7b7f741","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_person_over_demand","source_type":"hft","support_ids":["sup_8bf3197d0d7a31cd678b"],"title":"b_person_over_demand","trust":"legacy_unbound"},{"anchor_refs":["93:10"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:10","branch_refs":["root_000661/B002","root_000661/B003","root_001559/B001","root_001559/B003"],"candidate_id":"cand_145e2f3d536b70286c80","commentary_obligation":"review","hft_ref":"hft_ba8a4197b88feecb53f1","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_request_channel","source_type":"hft","support_ids":["sup_d20a828d3bafbe44bdf2"],"title":"b_request_channel","trust":"legacy_unbound"},{"anchor_refs":["93:10"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:10","branch_refs":["root_000661/B004","root_001559/B004"],"candidate_id":"cand_7f620634b137107139cb","commentary_obligation":"review","hft_ref":"hft_2186de1ad497d250c8ec","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_reciprocal_questioning","source_type":"hft","support_ids":["sup_71f2d85ce6878ed9ad8b"],"title":"b_reciprocal_questioning","trust":"legacy_unbound"},{"anchor_refs":["93:10"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:10","branch_refs":["root_000736/B001","root_001559/B004","root_001559/B006"],"candidate_id":"cand_bbfa194f69a0f03b8698","commentary_obligation":"review","hft_ref":"hft_28a273e18f72172aaaf1","kind":"surprising_outlier","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:o_delicate_extraction","source_type":"hft","support_ids":["sup_c57219c5168b9007bb0d"],"title":"o_delicate_extraction","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَأَمَّا ٱلسَّآئِلَ فَلَا تَنْهَرْ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"93:10:1:1","qac_word_ref":"93:10:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"أَمَّا","morph_features":"STEM|POS:EXL|LEM:>am~aA","morpheme_role":"STEM","pos":"EXL","qac_ref":"93:10:1:2","qac_word_ref":"93:10:1","root_ar":"","surface_ar":"أَمَّا"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"93:10:2:1","qac_word_ref":"93:10:2","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"سَآئِل","morph_features":"STEM|POS:N|ACT|PCPL|LEM:saA^}il|ROOT:sAl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:10:2:2","qac_word_ref":"93:10:2","root_ar":"س ء ل","surface_ar":"سَّآئِلَ"},{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"93:10:3:1","qac_word_ref":"93:10:3","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:PRO|LEM:laA","morpheme_role":"STEM","pos":"PRO","qac_ref":"93:10:3:2","qac_word_ref":"93:10:3","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"تَنْهَرْ","morph_features":"STEM|POS:V|IMPF|LEM:tanoharo|ROOT:nhr|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"93:10:4:1","qac_word_ref":"93:10:4","root_ar":"ن ه ر","surface_ar":"تَنْهَرْ"}],"word_analysis_qac_refs":[["93:10:1:1"],["93:10:1:2"],["93:10:2:1","93:10:2:2"],["93:10:3:1"],["93:10:3:2"],["93:10:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["93:10:1","93:10:2","93:10:3","93:10:4","93:10:5","93:10:6"]},"focus_surface_evidence":{"arabic_uthmani":"وَأَمَّا ٱلسَّآئِلَ فَلَا تَنْهَرْ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"93:10:1:1","qac_word_ref":"93:10:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"أَمَّا","morph_features":"STEM|POS:EXL|LEM:>am~aA","morpheme_role":"STEM","pos":"EXL","qac_ref":"93:10:1:2","qac_word_ref":"93:10:1","root_ar":"","surface_ar":"أَمَّا"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"93:10:2:1","qac_word_ref":"93:10:2","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"سَآئِل","morph_features":"STEM|POS:N|ACT|PCPL|LEM:saA^}il|ROOT:sAl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"93:10:2:2","qac_word_ref":"93:10:2","root_ar":"س ء ل","surface_ar":"سَّآئِلَ"},{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"93:10:3:1","qac_word_ref":"93:10:3","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:PRO|LEM:laA","morpheme_role":"STEM","pos":"PRO","qac_ref":"93:10:3:2","qac_word_ref":"93:10:3","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"تَنْهَرْ","morph_features":"STEM|POS:V|IMPF|LEM:tanoharo|ROOT:nhr|2MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"93:10:4:1","qac_word_ref":"93:10:4","root_ar":"ن ه ر","surface_ar":"تَنْهَرْ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["93:10:1:1"],["93:10:1:2"],["93:10:2:1","93:10:2:2"],["93:10:3:1"],["93:10:3:2"],["93:10:4:1"]],"word_analysis_refs":["93:10:1","93:10:2","93:10:3","93:10:4","93:10:5","93:10:6"],"word_rows":[{"analysis_record_ref":"93:10:1","analytic_gloss_range_en":"coordinating opening that carries the second case forward from the previous prohibition and keeps the ayah inside a paired social sequence","analytic_root_gloss_range_en":null,"qac_refs":["93:10:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"93:10:2","analytic_gloss_range_en":"conditional-topicalizing particle that sets the requester as the handled case and requires a following fa-marked response","analytic_root_gloss_range_en":null,"qac_refs":["93:10:1:2"],"root":{},"surface":{"arabic":"أَمَّا","transliteration":"ammā"}},{"analysis_record_ref":"93:10:3","analytic_gloss_range_en":"the definite active-participle requester, petitioner, or questioner, fronted as the protected object before the prohibition","analytic_root_gloss_range_en":"root range around asking, requesting, inquiry, and desire, with reported flow imagery kept only as lexical pressure here because the local form selects the person who asks","qac_refs":["93:10:2:1","93:10:2:2"],"root":{"arabic":"س أ ل","transliteration":"s-ʾ-l"},"surface":{"arabic":"ٱلسَّآئِلَ","transliteration":"al-sāʾila"}},{"analysis_record_ref":"93:10:4","analytic_gloss_range_en":"required apodosis marker that pivots immediately from the named requester to the prohibition","analytic_root_gloss_range_en":null,"qac_refs":["93:10:3:1"],"root":{},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"93:10:5","analytic_gloss_range_en":"prohibitive negation governing the following jussive verb, producing a direct negative command rather than descriptive denial","analytic_root_gloss_range_en":null,"qac_refs":["93:10:3:2"],"root":{},"surface":{"arabic":"لَا","transliteration":"lā"}},{"analysis_record_ref":"93:10:6","analytic_gloss_range_en":"jussive second-person prohibition against harshly rebuking, scolding, or verbally driving back the fronted requester; not a ban on every refusal","analytic_root_gloss_range_en":"root range includes river or watercourse, daylight, opening or flow, and harsh verbal rebuke; the local Form I jussive selects the rebuke branch while concrete river, channel, and daylight fields survive only as image pressure","qac_refs":["93:10:4:1"],"root":{"arabic":"ن ه ر","transliteration":"n-h-r"},"surface":{"arabic":"تَنْهَرْ","transliteration":"tanhar"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":6,"words_total":6,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["93:10"],"branch_refs":["root_000661/B001","root_001559/B004"],"candidate_id":"cand_57af0f13050cb6883527","evidence_scope":"focus_ayah","hft_ref":"hft_95a59e3ee9dfc7b7f741","item_id":"b_person_over_demand","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_person_over_demand","support_id":"sup_8bf3197d0d7a31cd678b"},{"anchor_refs":["93:10"],"branch_refs":["root_000661/B002","root_000661/B003","root_001559/B001","root_001559/B003"],"candidate_id":"cand_145e2f3d536b70286c80","evidence_scope":"focus_ayah","hft_ref":"hft_ba8a4197b88feecb53f1","item_id":"b_request_channel","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_request_channel","support_id":"sup_d20a828d3bafbe44bdf2"},{"anchor_refs":["93:10"],"branch_refs":["root_000661/B004","root_001559/B004"],"candidate_id":"cand_7f620634b137107139cb","evidence_scope":"focus_ayah","hft_ref":"hft_2186de1ad497d250c8ec","item_id":"b_reciprocal_questioning","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_reciprocal_questioning","support_id":"sup_71f2d85ce6878ed9ad8b"},{"anchor_refs":["93:10"],"branch_refs":["root_000736/B001","root_001559/B004","root_001559/B006"],"candidate_id":"cand_bbfa194f69a0f03b8698","evidence_scope":"focus_ayah","hft_ref":"hft_28a273e18f72172aaaf1","item_id":"o_delicate_extraction","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:o_delicate_extraction","support_id":"sup_c57219c5168b9007bb0d"}],"diagnostics":[],"lane_counts":{"global":8,"macro":11,"micro":4},"packet_summary":{"ayah_count":11,"focus_ref":"93:10","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س ء ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000661","furuq_root_norm":"س ء ل","furuq_source_root_norm":"س أ ل","is_dominant":true,"target_occurrences":118,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000736","furuq_root_norm":"س ل ل","furuq_source_root_norm":"س ل ل","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"و ج د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001626","furuq_root_norm":"و ج د","furuq_source_root_norm":"و ج د","is_dominant":true,"target_occurrences":61,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000227","furuq_root_norm":"ج د د","furuq_source_root_norm":"ج د د","is_dominant":false,"target_occurrences":10,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["93:1","93:2","93:3","93:4","93:5","93:6","93:7","93:8","93:9","93:10","93:11"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"93:10","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"93:10","lane":"micro","linguistic_source_ref":"93:10","surface_ref":"93:10","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"93:10","target_tokens":[["İsteyeni",["93:10:2"]],["de",["93:10:1"]],["azarlama",["93:10:3","93:10:4"]]],"text":"İsteyeni de azarlama."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":11,"id":"s093-p01-001-011","label":"Whole surah","number":1,"refs":["93:1","93:2","93:3","93:4","93:5","93:6","93:7","93:8","93:9","93:10","93:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:3:broad-asking-register","source_type":"word_analysis","support_id":"sup_07a230c5c582d0d7378f","text":"{\"blocking_evidence\":null,\"headline\":\"petitioner and questioner both remain protected\",\"reader_payoff\":\"The reader notices that the wording protects asking across material request, inquiry, and seeking, instead of narrowing the class to only one social label.\",\"reason\":\"The local active participle licenses the asker role, and no guardrail evidence restricts the protected category to only material begging or only intellectual questioning.\",\"representative_source_ids\":[\"QS-0730b46a\",\"QS-fac23509\",\"MS-bfa1f8e7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:5:prohibitive-la-jussive","source_type":"word_analysis","support_id":"sup_0ff32cb75d03716930df","text":"{\"blocking_evidence\":null,\"headline\":\"direct negative command\",\"reader_payoff\":\"The reader notices that the clause is a binding prohibition over the following verb, not ordinary negation or advice.\",\"reason\":\"QAC and attachment evidence mark {{ar:لَا}} ({{tr:lā}}) as prohibitive and governing the jussive verb.\",\"representative_source_ids\":[\"QG-79d159b4\",\"QG-f922a8bd\",\"MG-5af06ed6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:2","source_type":"word_analysis","support_id":"sup_1d26178b8b6a5980bae6","text":"{\"gloss_range\":\"conditional-topicalizing particle that sets the requester as the handled case and requires a following fa-marked response\",\"prose\":\"{{ar:أَمَّا}} ({{tr:ammā}}) makes the requester a handled case and opens a dependency that waits for {{ar:فَ}} ({{tr:fa}}). The word is not a loose topic marker: it conditions, details, and organizes the clause so that the prohibition arrives as the required answer. Repetition across 93:9, 93:10, and 93:11 turns the local case into the middle panel of a three-case ethical series.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:أَمَّا}} ({{tr:ammā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:6","source_type":"word_analysis","support_id":"sup_220e4bf6e12df41f34f1","text":"{\"gloss_range\":\"jussive second-person prohibition against harshly rebuking, scolding, or verbally driving back the fronted requester; not a ban on every refusal\",\"prose\":\"{{ar:تَنْهَرْ}} ({{tr:tanhar}}) is the final controlled act: a second-person jussive under {{ar:لَا}} ({{tr:lā}}), aimed directly at the addressee. Its imperfect jussive form regulates possible conduct when the requester appears rather than describing a completed rebuke. Its object has already appeared as {{ar:ٱلسَّآئِلَ}} ({{tr:al-sāʾila}}), so the closing verb completes the earlier person rather than introducing a new target. The selected sense is harsh rebuke or verbal repulsion, not every refusal; because the verb is Form I, the prohibition reaches the basic act before intensified patterns. The wider {{ar:ن ه ر}} ({{tr:n-h-r}}) field of river, channel, and daylight is not the local sense, but it gives the rebuke force, cutting, and exposure pressure. The word is also rare as a verb: its only other verbal occurrence is the same kind of prohibition toward parents (17:23). At the ayah boundary it answers the prior final verb of 93:9 with a near-rhyme and a shifted harm domain, moving from overpowering the orphan to harshly repelling the requester. That negative speech restraint then prepares the forward turn to positive speech about blessing in 93:11.\",\"root_display\":\"{{ar:ن ه ر}} ({{tr:n-h-r}})\",\"root_gloss_range\":\"root range includes river or watercourse, daylight, opening or flow, and harsh verbal rebuke; the local Form I jussive selects the rebuke branch while concrete river, channel, and daylight fields survive only as image pressure\",\"surface_display\":\"{{ar:تَنْهَرْ}} ({{tr:tanhar}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:3:fronted-protected-object","source_type":"word_analysis","support_id":"sup_24885614b0a539d15d88","text":"{\"blocking_evidence\":null,\"headline\":\"fronted object before the forbidden act\",\"reader_payoff\":\"The reader notices the person who asks before hearing the forbidden response, so the human object is prioritized over the act.\",\"reason\":\"Attachment evidence marks {{ar:ٱلسَّآئِلَ}} ({{tr:al-sāʾila}}) as the fronted direct object of {{ar:تَنْهَرْ}} ({{tr:tanhar}}), preserving both priority and argument role.\",\"representative_source_ids\":[\"QG-2cda13a7\",\"MG-c5b35fce\",\"QT-359f4dd3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:3:definite-active-participle-category","source_type":"word_analysis","support_id":"sup_2c33f4aa340ea7002a7f","text":"{\"blocking_evidence\":null,\"headline\":\"definite active-participle role\",\"reader_payoff\":\"The reader notices that the protected figure is a recognizable class defined by asking, while still retaining agency inside the participle.\",\"reason\":\"QAC marks a definite active participle and the contextual profile supports a generic human referent pattern for this exact form.\",\"representative_source_ids\":[\"QG-4ee2a23e\",\"QG-60d4df61\",\"QF-2679eaf2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:3","source_type":"word_analysis","support_id":"sup_2f4a09a651a2adddcab9","text":"{\"gloss_range\":\"the definite active-participle requester, petitioner, or questioner, fronted as the protected object before the prohibition\",\"prose\":\"{{ar:ٱلسَّآئِلَ}} ({{tr:al-sāʾila}}) is placed first as the case under discussion, yet it remains the object of {{ar:تَنْهَرْ}} ({{tr:tanhar}}). The active participle makes the protected person recognizable by the act of asking, and the definite form broadens that role beyond a single incident. Its range can include the material petitioner, the questioner, and the seeker more generally; echoes with the requester who has a right in wealth (51:19; 70:25) keep that class socially concrete. Across the boundary from 93:9, the protected figure shifts from passive deprivation to need voiced as asking. In connected recitation, the requester word is joined to the preceding case particle, while the hamza after the long ā gives the word its own small arrest. The same-surah morning opening (93:1) also lets the asking register carry a public-visibility echo without changing the local noun sense. The reported flow side of {{ar:س أ ل}} ({{tr:s-ʾ-l}}) adds image pressure only: the selected local sense is still the person who asks, while the nearby river-root verb makes the answer to that small outward movement feel especially dangerous if it becomes overwhelming force.\",\"root_display\":\"{{ar:س أ ل}} ({{tr:s-ʾ-l}})\",\"root_gloss_range\":\"root range around asking, requesting, inquiry, and desire, with reported flow imagery kept only as lexical pressure here because the local form selects the person who asks\",\"surface_display\":\"{{ar:ٱلسَّآئِلَ}} ({{tr:al-sāʾila}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:1","source_type":"word_analysis","support_id":"sup_318019b696cf82e658b3","text":"{\"gloss_range\":\"coordinating opening that carries the second case forward from the previous prohibition and keeps the ayah inside a paired social sequence\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) opens the ayah as continuation, not reset. It joins this second {{ar:أَمَّا}} ({{tr:ammā}}) case to the preceding protected figure in 93:9, so the requester command is heard as the matched counterpart to the orphan command. Because the conjunction is fused directly into {{ar:وَأَمَّا}} ({{tr:wa-ammā}}), coordination and case-marking arrive as one linked discourse unit.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:6:negative-to-positive-speech-handoff","source_type":"word_analysis","support_id":"sup_3da2c695bcd10bbd0373","text":"{\"blocking_evidence\":null,\"headline\":\"speech restraint before positive proclamation\",\"reader_payoff\":\"The reader notices that restrained speech toward the requester prepares the movement toward positive speech about blessing in 93:11.\",\"reason\":\"The row gives the concrete forward reference to 93:11, and it fits the same-surah sequence without changing the local parse.\",\"representative_source_ids\":[\"QB-05d69142\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:6:sound-and-final-closure","source_type":"word_analysis","support_id":"sup_4738060eb4d1923e91ff","text":"{\"blocking_evidence\":null,\"headline\":\"final clipped near-rhyme with the prior command\",\"reader_payoff\":\"The reader notices the ayah landing on the forbidden act in a clipped sound shape that echoes the prior final verb of 93:9.\",\"reason\":\"The final position and jussive surface are local, and the CRITICAL rows give the concrete 93:9 comparison.\",\"representative_source_ids\":[\"QT-88ea4c96\",\"QE-730f3891\",\"QP-dba54d29\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:5","source_type":"word_analysis","support_id":"sup_537df56406ed492c4acb","text":"{\"gloss_range\":\"prohibitive negation governing the following jussive verb, producing a direct negative command rather than descriptive denial\",\"prose\":\"{{ar:لَا}} ({{tr:lā}}) is prohibitive here. It governs the jussive {{ar:تَنْهَرْ}} ({{tr:tanhar}}), so the clause performs a direct negative command rather than reporting that rebuke does not happen. The repeated negator with 93:9 forms the paired negative boundary of the section, and its short placement in {{ar:فَلَا تَنْهَرْ}} ({{tr:fa-lā tanhar}}) helps the prohibition land compactly.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَا}} ({{tr:lā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:6:direct-second-person-jussive","source_type":"word_analysis","support_id":"sup_598d6fee730c4780b696","text":"{\"blocking_evidence\":null,\"headline\":\"direct addressee under prohibitive jussive\",\"reader_payoff\":\"The reader notices that the addressed person is the restrained agent, carried inside the verb without an explicit pronoun.\",\"reason\":\"QAC marks a second-person masculine singular jussive, and attachment evidence resolves the implicit subject as the singular addressee.\",\"representative_source_ids\":[\"QG-2c0b2bb7\",\"QG-40f526f0\",\"QG-f20d4e68\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:6:root-image-pressure-narrowed","source_type":"word_analysis","support_id":"sup_5ee0b5c193d132d377fd","text":"{\"blocking_evidence\":null,\"headline\":\"river, channel, and exposure pressure around rebuke\",\"reader_payoff\":\"The reader notices that harsh speech is felt as force that cuts, sweeps, or exposes, while the local verb still selects verbal rebuke.\",\"reason\":\"V4 separates river, daylight, opening, and rebuke branches; the local Form I prohibition selects rebuke, so the concrete branches survive as image pressure rather than independent local senses.\",\"representative_source_ids\":[\"QS-0b5d471c\",\"QS-1961bcce\",\"QS-4c509fb0\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:1:coordinated-paired-case","source_type":"word_analysis","support_id":"sup_6e5a4187b5ecfe8728ef","text":"{\"blocking_evidence\":null,\"headline\":\"second coordinated case in the sequence\",\"reader_payoff\":\"The reader notices that 93:10 is the second member of a paired ethical sequence with 93:9, not an isolated rule.\",\"reason\":\"QAC identifies {{ar:وَ}} ({{tr:wa}}) as coordination with 93:9, and the local clause continues the same {{ar:أَمَّا}} ({{tr:ammā}}) prohibition architecture.\",\"representative_source_ids\":[\"QG-9d8b27cb\",\"MT-36ca53f0\",\"QT-af5d3f96\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:6:prospective-command-form","source_type":"word_analysis","support_id":"sup_75076ac1830a9744e90e","text":"{\"blocking_evidence\":null,\"headline\":\"possible action barred before it happens\",\"reader_payoff\":\"The reader notices that the imperfect jussive regulates the addressee's future conduct toward the requester rather than describing a completed rebuke.\",\"reason\":\"The local form is jussive after prohibitive {{ar:لَا}} ({{tr:lā}}), not an indicative statement or perfect report.\",\"representative_source_ids\":[\"MG-4dcb9445\",\"QF-6f34951e\",\"QF-97e5f0e3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:6:convergence-of-grammar-image-and-sound","source_type":"word_analysis","support_id":"sup_838d944caf9c8276a675","text":"{\"blocking_evidence\":null,\"headline\":\"grammar, root pressure, and rhyme converge\",\"reader_payoff\":\"The reader notices the final word carrying several pressures at once: command mood, rare verbal root use, concrete-force imagery, and boundary rhyme.\",\"reason\":\"The convergent rows are locally grounded by jussive grammar, V4-backed root branches used as pressure, and the same-surah final-verb position.\",\"representative_source_ids\":[\"QY-10ef5d8e\",\"QY-88918490\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:4","source_type":"word_analysis","support_id":"sup_85a900d35fc020a98a0b","text":"{\"gloss_range\":\"required apodosis marker that pivots immediately from the named requester to the prohibition\",\"prose\":\"{{ar:فَ}} ({{tr:fa}}) is the hinge that answers {{ar:أَمَّا}} ({{tr:ammā}}). It closes the case frame and moves immediately from the named requester to the ruling, so the person and the prohibition remain one syntactic movement. In {{ar:فَلَا}} ({{tr:fa-lā}}), the response marker is joined directly to prohibitive negation, repeating the prohibition gateway heard in 93:9.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:4:required-apodosis-hinge","source_type":"word_analysis","support_id":"sup_8d2f951c60a74912373a","text":"{\"blocking_evidence\":null,\"headline\":\"required answer to the case frame\",\"reader_payoff\":\"The reader notices that the prohibition is grammatically required as the answer to the requester case, not merely appended after it.\",\"reason\":\"QAC and attachment support identify {{ar:فَ}} ({{tr:fa}}) as the structural answer marker after {{ar:أَمَّا}} ({{tr:ammā}}).\",\"representative_source_ids\":[\"QG-49a68141\",\"MG-3d716140\",\"QS-7c7dd95a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:2:case-response-frame","source_type":"word_analysis","support_id":"sup_9f34733efd4ad8bd22e6","text":"{\"blocking_evidence\":null,\"headline\":\"case marker requiring a response\",\"reader_payoff\":\"The reader notices that the requester is not simply named; the particle makes that figure a case whose required answer is the prohibition.\",\"reason\":\"QAC and attachment evidence both mark an {{ar:أَمَّا}} ({{tr:ammā}}) construction whose response is introduced by {{ar:فَ}} ({{tr:fa}}).\",\"representative_source_ids\":[\"QG-5ada1c3a\",\"MG-8ca1f347\",\"QT-f34dc74a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:6:harsh-rebuke-not-mere-refusal","source_type":"word_analysis","support_id":"sup_a8021d2c3bacac219926","text":"{\"blocking_evidence\":null,\"headline\":\"harsh verbal repulsion is the selected sense\",\"reader_payoff\":\"The reader notices that the command forbids hostile rebuke that drives the requester away, while not making every refusal itself the named act.\",\"reason\":\"QAC and V4 both support the harsh verbal rebuke branch for the local verb, while the local frame does not require a broader refusal ban.\",\"representative_source_ids\":[\"QS-ed2ddfc0\",\"QF-56260fa4\",\"MF-17440a48\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:1:fused-wa-amma-onset","source_type":"word_analysis","support_id":"sup_aa5416be295c167677fa","text":"{\"blocking_evidence\":null,\"headline\":\"fused continuation and case marker\",\"reader_payoff\":\"The reader notices that the ayah begins with continuity and case-framing already bound together in the first written unit.\",\"reason\":\"The surface joins the conjunction directly to {{ar:أَمَّا}} ({{tr:ammā}}), so the formal onset supports the discourse-link topic.\",\"representative_source_ids\":[\"QF-8f6ab363\",\"QE-feecd5fa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:3:boundary-and-sound-marking","source_type":"word_analysis","support_id":"sup_ae09893626cf781a5f84","text":"{\"blocking_evidence\":null,\"headline\":\"marked transition into the requester word\",\"reader_payoff\":\"The reader notices that the requester word is both connected to the case particle in recitation and acoustically marked by the root-bearing interruption.\",\"reason\":\"The sound rows describe features visible in the local surface and compatible with the case-frame grammar.\",\"representative_source_ids\":[\"QP-500894d8\",\"QP-627be4e5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:6:boundary-harm-shift","source_type":"word_analysis","support_id":"sup_af081e0f7c8fd4ef055e","text":"{\"blocking_evidence\":null,\"headline\":\"from overpowering to harsh speech\",\"reader_payoff\":\"The reader notices the boundary shift from protecting the orphan from domination (93:9) to protecting the requester from verbal-force rejection (93:10).\",\"reason\":\"The boundary rows give concrete same-surah links, and both final verbs share the same addressed subject and prohibitive frame.\",\"representative_source_ids\":[\"QB-06357c13\",\"QB-260e32ed\",\"QB-eb8d02cf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:5:paired-negative-boundary","source_type":"word_analysis","support_id":"sup_b5ed1b6933a2223d7861","text":"{\"blocking_evidence\":null,\"headline\":\"paired negative ethical boundary\",\"reader_payoff\":\"The reader notices the repeated negator forming a two-part boundary with 93:9 before the positive speech command of 93:11.\",\"reason\":\"The CRITICAL rows give concrete same-surah references, and the local form is the same prohibitive negator.\",\"representative_source_ids\":[\"MT-d3a45d1e\",\"QE-952b95f1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"93:10:4:1","source_type":"qac_morpheme","support_id":"sup_c259eaeaac6687af2fa9","text":"{\"lemma_ar\":\"تَنْهَرْ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:tanoharo|ROOT:nhr|2MS|MOOD:JUS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"93:10:4:1\",\"qac_word_ref\":\"93:10:4\",\"root_ar\":\"ن ه ر\",\"surface_ar\":\"تَنْهَرْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:3:orphan-to-asker-progression","source_type":"word_analysis","support_id":"sup_c7e1b49e663dae547ec7","text":"{\"blocking_evidence\":null,\"headline\":\"from deprivation to active seeking\",\"reader_payoff\":\"The reader notices the shift from the orphan of 93:9 to the requester of 93:10 as a move from passive deprivation to need voiced as asking.\",\"reason\":\"The local noun is fronted as a protected object, and the same-surah boundary row gives the concrete contrast with 93:9.\",\"representative_source_ids\":[\"MT-55f503e1\",\"QY-16a9871b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:3:right-bearing-requester-echo","source_type":"word_analysis","support_id":"sup_d0ad99b88cb1e3d560a1","text":"{\"blocking_evidence\":null,\"headline\":\"requester with a social right\",\"reader_payoff\":\"The reader notices that the same requester label appears in wealth-right contexts (51:19; 70:25), so the protected figure is not treated as an intrusion.\",\"reason\":\"The CRITICAL row gives concrete same-root active-participle parallels, and they clarify the social category without changing the local object relation.\",\"representative_source_ids\":[\"MI-946c15d2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:2:three-case-series","source_type":"word_analysis","support_id":"sup_d1573360ab2171e9b08d","text":"{\"blocking_evidence\":null,\"headline\":\"middle member of a same-surah series\",\"reader_payoff\":\"The reader notices that the repeated case particle converts the neighboring commands into a distributive series spanning 93:9, 93:10, and 93:11.\",\"reason\":\"The same particle pattern is explicitly tied by the CRITICAL rows to 93:9 and 93:11, and the local grammar supports the same case-response construction.\",\"representative_source_ids\":[\"MT-48c5bf11\",\"QE-d48c581d\",\"QB-6f4f4c45\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:5:compact-prohibition-cadence","source_type":"word_analysis","support_id":"sup_d628bcc4c0d66da3a6b3","text":"{\"blocking_evidence\":null,\"headline\":\"compact falling prohibition\",\"reader_payoff\":\"The reader notices that the short particle sequence lets the ruling fall quickly into the clipped final verb.\",\"reason\":\"The cadence row follows from the local {{ar:فَ}} ({{tr:fa}}), {{ar:لَا}} ({{tr:lā}}), and jussive verb sequence.\",\"representative_source_ids\":[\"QP-2c631b84\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:6:rare-verbal-use-and-parent-parallel","source_type":"word_analysis","support_id":"sup_d7d8dff49465e539e8ed","text":"{\"blocking_evidence\":null,\"headline\":\"rare verbal prohibition set\",\"reader_payoff\":\"The reader notices that this rare verbal use belongs with the only other verbal prohibition from the same root, protecting parents from harsh speech (17:23).\",\"reason\":\"QAC and contextual evidence report only two verbal occurrences for the root, including the concrete parallel in 17:23.\",\"representative_source_ids\":[\"MI-5ebd5707\",\"QH-4fb6293b\",\"QH-56f644a8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:4:compact-fa-la-parallel","source_type":"word_analysis","support_id":"sup_e234f179e61bc5d38d10","text":"{\"blocking_evidence\":null,\"headline\":\"compact repeated prohibition gateway\",\"reader_payoff\":\"The reader notices the same compact response-plus-prohibition shape tying 93:10 to the preceding command in 93:9.\",\"reason\":\"The visible {{ar:فَلَا}} ({{tr:fa-lā}}) sequence in 93:10 matches the CRITICAL-row parallel to the same prohibition gateway in 93:9.\",\"representative_source_ids\":[\"QF-6b1856d7\",\"MT-1127ff02\",\"QE-4ec41645\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:6:fronted-object-completion","source_type":"word_analysis","support_id":"sup_e418c6d970a91ac271d4","text":"{\"blocking_evidence\":null,\"headline\":\"closing verb completes the earlier object\",\"reader_payoff\":\"The reader notices that the final verb acts on the requester already placed at the front of the clause.\",\"reason\":\"The attachment and verb-instance evidence identify the fronted requester as the explicit object of {{ar:تَنْهَرْ}} ({{tr:tanhar}}).\",\"representative_source_ids\":[\"QG-39688b5a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:3:daylight-setting-echo","source_type":"word_analysis","support_id":"sup_f091ade4af5927dede8b","text":"{\"blocking_evidence\":null,\"headline\":\"public visibility echo from the surah opening\",\"reader_payoff\":\"The reader notices a possible same-surah visibility echo with the opening morning setting (93:1), while the local noun remains the requester.\",\"reason\":\"The reference to 93:1 can function as a contextual echo, but it does not alter the local active-participle sense or object role.\",\"representative_source_ids\":[\"ME-8bab31b7\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:10:3:flow-image-narrowed","source_type":"word_analysis","support_id":"sup_f2dc15fcc4d270535f95","text":"{\"blocking_evidence\":null,\"headline\":\"asking as outward movement, not selected flow sense\",\"reader_payoff\":\"The reader notices a local image contrast: a small movement of need meets the danger of river-like verbal force, while the noun still means the one who asks.\",\"reason\":\"V4 has no guardrail rows for {{ar:س أ ل}} ({{tr:s-ʾ-l}}), so absence cannot reject the row; local grammar, however, selects the active-participle requester rather than an independent flowing adjective.\",\"representative_source_ids\":[\"QS-7bafddcd\",\"MS-1dd8d4c6\",\"QE-b417b7f1\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"93:10:2:2","source_type":"qac_morpheme","support_id":"sup_f610a05d7765b9b79c65","text":"{\"lemma_ar\":\"سَآئِل\",\"morph_features\":\"STEM|POS:N|ACT|PCPL|LEM:saA^}il|ROOT:sAl|M|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"93:10:2:2\",\"qac_word_ref\":\"93:10:2\",\"root_ar\":\"س ء ل\",\"surface_ar\":\"سَّآئِلَ\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَأَمَّا ٱلسَّآئِلَ فَلَا تَنْهَرْ","ayah_ref":"93:10"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000661/B001","root_001559/B004"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000661","role":"Asking and requesting supply the vulnerable approach and identify the person whose treatment is regulated.","root":"س ء ل","source_ref":"93:10","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_001559","role":"Harsh verbal rebuke supplies the prohibited force that can repel and demean the approaching asker.","root":"ن ه ر","source_ref":"93:10","source_word_indices":["4"]}],"changed_reading":{"after":"The command protects the asker's human standing during an asymmetrical request, even when the requested thing cannot be supplied.","before":"A narrow etiquette rule says not to use rude words."},"confidence":"strong","focus_anchor":"The fronted human noun at word 2 is paired with a second-person prohibition at word 4, so the encounter with the asker, not merely the requested object, is foregrounded.","mechanism":"An approach made through asking meets a speech act capable of driving the asker back. The prohibition protects the asker's standing at the moment of dependence; it constrains refusal and manner without by itself promising that every request will be granted.","model_id":"b_person_over_demand"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_person_over_demand","source_type":"hft","support_id":"sup_8bf3197d0d7a31cd678b","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَأَمَّا ٱلسَّآئِلَ فَلَا تَنْهَرْ","ayah_ref":"93:10"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000661/B002","root_000661/B003","root_001559/B001","root_001559/B003"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000661","role":"The sought request supplies the content that is trying to pass from need into response.","root":"س ء ل","source_ref":"93:10","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000661","role":"Fulfilling a request supplies a possible endpoint while leaving room for responses short of fulfillment.","root":"س ء ل","source_ref":"93:10","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001559","role":"A river cutting ground supplies the image of a response channel that can carry provision yet erode social ground.","root":"ن ه ر","source_ref":"93:10","source_word_indices":["4"]},{"branch_id":"B003","mapped_root_id":"root_001559","role":"Opening and widening until flow supply the alternative possibility of keeping access passable rather than closing it by rebuke.","root":"ن ه ر","source_ref":"93:10","source_word_indices":["4"]}],"changed_reading":{"after":"It also regulates the social channel through which a need becomes answer: do not make that channel cut, wound, or eject the person using it.","before":"The verse regulates the tone of one brief exchange."},"confidence":"medium","focus_anchor":"The requested-object and fulfillment branches of word 2 coexist with the river and opening branches of the prohibited verb at word 4.","mechanism":"The focus can be modeled as a channel between articulated need and possible response. The river image adds movement but also cutting and erosion, while widening-until-flow adds access; negation therefore warns against making the response channel itself wound or sweep aside the requester.","model_id":"b_request_channel"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_request_channel","source_type":"hft","support_id":"sup_d20a828d3bafbe44bdf2","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَأَمَّا ٱلسَّآئِلَ فَلَا تَنْهَرْ","ayah_ref":"93:10"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000661/B004","root_001559/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000661","role":"Reciprocal questioning supplies a two-sided exchange latent within the figure of the asker.","root":"س ء ل","source_ref":"93:10","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_001559","role":"Harsh rebuke supplies the speech act by which the stronger participant can shut that exchange down.","root":"ن ه ر","source_ref":"93:10","source_word_indices":["4"]}],"changed_reading":{"after":"The asker may also be an interlocutor whose question creates a reciprocal obligation to remain answerable without verbal expulsion.","before":"The asker is only a one-way petitioner seeking an object."},"confidence":"medium","focus_anchor":"The asker at word 2 can activate reciprocal questioning within its dominant inventory, while word 4 names the verbal act that would terminate exchange.","mechanism":"The apparently one-way petitioner can be heard as a participant in a question-and-answer relation. Rebuke is then not only discourtesy but a unilateral closure of reciprocity by the party with greater authority.","model_id":"b_reciprocal_questioning"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_reciprocal_questioning","source_type":"hft","support_id":"sup_71f2d85ce6878ed9ad8b","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَأَمَّا ٱلسَّآئِلَ فَلَا تَنْهَرْ","ayah_ref":"93:10"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000736/B001","root_001559/B004","root_001559/B006"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000736","role":"Gentle, concealed drawing-out supplies an image for a question or request bringing hidden need into speech.","root":"س ء ل","source_ref":"93:10","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_001559","role":"A sudden or stealthy snatch supplies the violent reversal by which the response seizes control of a delicate disclosure.","root":"ن ه ر","source_ref":"93:10","source_word_indices":["4"]},{"branch_id":"B004","mapped_root_id":"root_001559","role":"Harsh verbal rebuke keeps the material analogy attached to the actual prohibited speech act.","root":"ن ه ر","source_ref":"93:10","source_word_indices":["4"]}],"changed_reading":{"after":"Asking may delicately draw a concealed need into view; rebuke violates that emergence by turning it into a sudden seizure of control.","before":"A request arrives as an already explicit demand and receives either assent or refusal."},"confidence":"exploratory","containment":"This is surprising because it uses the non-dominant split mapping of the asker's root together with a remote snatching branch of the prohibited verb. It remains anchored to both focus words and clarifies the vulnerability of disclosure; downstream prose should present it as a material analogy, not as a lexical replacement for asker or rebuke.","focus_anchor":"The asker at word 2 activates a split image of gently drawing something hidden out, while the prohibited verb at word 4 activates sudden snatching as well as rebuke.","outlier_id":"o_delicate_extraction"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:o_delicate_extraction","source_type":"hft","support_id":"sup_c57219c5168b9007bb0d","trust":"legacy_unbound"}]}
</lane_packet_json>
