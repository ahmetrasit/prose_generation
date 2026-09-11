# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **100:10**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s100-regular-20260911/s100/100_10/micro.discovery.json` and modify nothing
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
  "ayah_ref": "100:10",
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
{"analysis_context":{"analysis_id":"s100-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"100:10","host_surah":100,"lane_context_refs":[],"ordered_context_refs":["100:0","100:1","100:2","100:3","100:4","100:5","100:6","100:7","100:8","100:9","100:11","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Çekirdek bir şeyi toplamadır; kalma, elde edilen sonucu bildirme, sözü özetleme ve içtekini açığa çıkarma bu çekirdeğe bağlı fakat onunla tek bir işleme indirgenmeyen ayrı kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_000330/B001","candidate_links":[{"candidate_id":"cand_b377a37b3388bccc95af","lane":"micro"},{"candidate_id":"cand_a03e4f778b8ef036281f","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حُصِّلَ","morph_features":"STEM|POS:V|PERF|PASS|(II)|LEM:HuS~ila|ROOT:HSl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"100:10:1:2","qac_word_ref":"100:10:1","surface_ar":"حُصِّلَ"}],"gloss":"toplama ve elde kalanı ortaya koyma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin unsurları bir araya getirilerek bir bütün oluşturulur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir hesap veya iş bittikten ve öteki unsurlar gittikten sonra geriye kalan sabit sonuç da bu anlam alanına girer."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Söz için kullanıldığında, anlatım ayrıntılardan arındırılarak özüne ve vardığı sonuca döndürülür."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İçte veya gizli bulunan şeylerin açığa çıkarılıp bir arada gösterilmesi de çekirdeğe bağlı bir kullanımdır."}}],"root_ar":"ح ص ل","root_id":"root_000330","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Toplama çekirdeği ile bundan ayrı kalan veya sonuç bildiren kullanımı birlikte özetleyen genel bağlamlar için uygundur.","boundary_detail":"Çekirdek bir şeyi toplamadır; kalma, elde edilen sonucu bildirme, sözü özetleme ve içtekini açığa çıkarma bu çekirdeğe bağlı fakat onunla tek bir işleme indirgenmeyen ayrı kullanımlardır.","branch_image_ar":"جمع الشيء حتى يظهر حاصله","concept_gloss":"toplama ve elde kalanı ortaya koyma","contextual_glosses":[{"applicability":"Bir hesap veya iş sonunda öteki unsurlar gittikten sonra kalan sonucun belirtilmesinde doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Toplama işlemini, sözün özüne döndürülmesini ve gizli içeriğin açığa çıkarılmasını tek başına anlatmaz.","preserves":"İşlem sonunda belirginleşen ve sabit kalan sonuç yönünü korur."},"facet_ids":["F002"],"text":"sonucu elde etme","usage_role":"contextual"},{"applicability":"Yalnız sözün ayrıntılarından arındırılıp temel sonucuna döndürülmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel toplama, hesap sonucu ve saklı içeriği açığa çıkarma yönlerini kapsamaz.","preserves":"Sözün ayrıntılardan arındırılarak özüne döndürülmesi işlemini korur."},"facet_ids":["F003"],"text":"sözü özüne indirgeme","usage_role":"contextual"},{"applicability":"İçte saklı olanların ortaya konup topluca gösterildiği bağlamlara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel toplama, kalıcı sonuç ve sözü özüne indirgeme yönlerini kapsamaz.","preserves":"Gizli içeriğin görünür ve toplu duruma getirilmesi yönünü korur."},"facet_ids":["F004"],"text":"içindekileri açığa çıkarma","usage_role":"contextual"}],"definition":"Bir şeyi veya dağınık unsurları bir araya getirip bir bütün oluşturmaktır. Buna bağlı ayrı kullanımlarda, öteki unsurlar gittikten sonra geriye kalıp sabitleşen şey, bir işin veya hesabın sonucu, sözün özüne indirgenmesi ve saklı içeriğin açığa çıkarılması anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin unsurları bir araya getirilerek bir bütün oluşturulur."},{"facet_id":"F002","role":"extension","statement":"Bir hesap veya iş bittikten ve öteki unsurlar gittikten sonra geriye kalan sabit sonuç da bu anlam alanına girer."},{"facet_id":"F003","role":"specialization","statement":"Söz için kullanıldığında, anlatım ayrıntılardan arındırılarak özüne ve vardığı sonuca döndürülür."},{"facet_id":"F004","role":"associated_use","statement":"İçte veya gizli bulunan şeylerin açığa çıkarılıp bir arada gösterilmesi de çekirdeğe bağlı bir kullanımdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Sıradan sayısal toplama işlemiyle karışarak sonucun belirginleşmesi sınırını belirsizleştirebilir.","fit":"narrowing","loses":"Ayırma sonunda kalan sonucu ve kuruluşlara bağlı öz çıkarma ile açığa çıkarma yönlerini siler.","preserves":"Dağınık unsurları bir araya getirme çekirdeğini korur."},"text":"yalnızca toplama"}],"identity_rationale":"Kaynak ifadesi, bir şeyi toplama çekirdeğinin yanında işlem sonunda geriye kalıp sabitleşen sonucu, sözü özüne döndürmeyi ve içte olanı açığa çıkarmayı birlikte verir. Dalın genel çerçevesi kullanılabilir; ancak etkin toplama ile öteki unsurların gitmesinden sonra kalan sonuç tek ve ayrışmasız bir işlem gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi derleyip sonucunu çıkarma"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"ötekiler gittikten sonra geriye kalıp sabitleşme"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"hesap veya iş sonunda ortaya çıkan sonuç"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sözü özüne ve sonucuna indirgeme"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"içindekileri açığa çıkarıp bir araya getirme"}],"lexicalization_note":"Dal hem yalın biçimleri hem de yalnız belirli söz ve içeriği açığa çıkarma kuruluşlarında görülen anlamları içerir; kuruluşlara bağlı anlamlar bütün dala yayılmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yayımlanan iki komşu, toplu bütün ve genel kalanla karışma riskini en açık biçimde gösterir, ötekiler yalnız uzak sonuç veya ortak senaryo ilişkisi sunar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı toplamanın yanında geriye kalanı veya iş sonucunu da belirtir; komşu dalda ise asıl vurgu ayrıntılandırılmamış toplu bütün üzerindedir.","focus_only":"Bir şeyi toplama yanında kalanı veya iş sonucunu belirtme kullanımlarını da içerir.","gloss":"sonuç çıkarma ile toplu bütün","neighbor_only":"Ayrıntıya açılmamış toplu bütünü, bir sonuç çıkarma şartı olmadan ifade eder.","neighbor_ref":"root_000260/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da dağınık veya çok sayıdaki unsuru tek bir toplu görünüm altında birleştirir."},{"boundary_match":"partial","distinction":"Odak dalı kalan anlamının yanında toplama, işlem sonucunu belirtme ve sözü özetleme kullanımlarını da kapsar; komşu dal ise kalmış olmayı kendi başına temel anlam yapar.","focus_only":"Toplama, hesap veya iş sonucunu belirtme ve sözü özüne döndürme kullanımlarını da içerir.","gloss":"elde edilen sonuç ile genel kalan","neighbor_only":"Herhangi bir işlem veya toplama şartı olmadan elde kalan şeyi genel olarak ifade eder.","neighbor_ref":"root_000142/B002","relation_type":"near_neighbor","shared_zone":"Öteki unsurların gitmesinden sonra geriye kalan şey iki dalın kesişme alanıdır."}],"source_phrase_ar":"أصل واحد منقاس وهو جمع الشيء (maqayis)؛ حصلت الشيء تحصيلا (maqayis;sihah)؛ حصل يحصل حصولا أي بقي وثبت وذهب ما سواه من حساب أو عمل (ayn)؛ تحصيل الكلام رده إلى محصوله (sihah)؛ أظهر ما فيها وجمع أو إظهار الحاصل من الحساب (mufradat)","source_summary":"Kaynak malzemesi, toplama çekirdeğinin yanında öteki unsurlar gittikten sonra kalıp sabitleşmeyi, hesap veya iş sonucunu, sözün özüne döndürülmesini ve gizli içeriğin açığa çıkarılmasını aynı anlam ailesindeki ayrı kullanımlar olarak verir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه حصلت الشيء تحصيلا، والحاصل والمحصول بمعنى ما بقي وثبت بعد ذهاب غيره، ورد الكلام إلى محصوله، وإظهار ما في الصدور أو حاصل الحساب.","what_is_not_ar":"ليس هو حوصلة الطائر، ولا الحصل من البلح، ولا وجع بطن الفرس."},"support_links":["sup_4b7ed36557097abb3cb9","sup_674f18cecc7526b82ee0"]},{"boundary":"Anlam, yalnız seçmeyi değil, içteki değerli kısmı çevresinden ayırıp dışarı çıkarmayı gerektirir.","branch_kind":"bare","branch_ref":"root_000330/B002","candidate_links":[{"candidate_id":"cand_0692fa16c3cce4eebb69","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حُصِّلَ","morph_features":"STEM|POS:V|PERF|PASS|(II)|LEM:HuS~ila|ROOT:HSl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"100:10:1:2","qac_word_ref":"100:10:1","surface_ar":"حُصِّلَ"}],"gloss":"özünü ayırıp çıkarma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İçteki özlü veya değerli bölüm, onu saran maddeden ayrılır ve dışarı çıkarılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Taş veya maden toprağından altın ya da gümüş çıkarma, işlemin belirgin uzmanlık örneğidir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İç kısmı kabuktan veya taneyi samandan çıkarma, aynı ayırıp çıkarma yapısını somutlaştırır."}}],"root_ar":"ح ص ل","root_id":"root_000330","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Değerli veya yararlı iç bölümün çevresindeki maddeden ayrılarak elde edildiği bütün genel bağlamlara uygundur.","boundary_detail":"Anlam, yalnız seçmeyi değil, içteki değerli kısmı çevresinden ayırıp dışarı çıkarmayı gerektirir.","branch_image_ar":"استخراج اللب أو النفيس من غلافه","concept_gloss":"özünü ayırıp çıkarma","contextual_glosses":[{"applicability":"Altın veya gümüşün taş ya da maden toprağından ayrıldığı uzmanlık bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kabuktan iç çıkarma ve samandan tane ayırma gibi metal dışı uygulamaları kapsamaz.","preserves":"Değerli maddenin çevresindeki değersiz kütleden ayrılıp çıkarılmasını korur."},"facet_ids":["F002"],"text":"madenden değerli metal çıkarma","usage_role":"contextual"},{"applicability":"Bir tanenin veya benzeri şeyin yararlı iç kısmının kabuğundan ayrılması bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Maden cevherinden metal çıkarma ve daha genel değerli bölüm seçimini kapsamaz.","preserves":"Yararlı iç bölümün onu örten kısımdan ayrılıp çıkarılmasını korur."},"facet_ids":["F003"],"text":"kabuğundan içini çıkarma","usage_role":"contextual"}],"definition":"Bir şeyin içindeki özlü, yararlı veya değerli bölümü onu saran değersiz maddeden ayırıp çıkarmaktır. İşlem, çıkarılan bölümün seçilip belirginleştirilmesini de içerir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İçteki özlü veya değerli bölüm, onu saran maddeden ayrılır ve dışarı çıkarılır."},{"facet_id":"F002","role":"specialization","statement":"Taş veya maden toprağından altın ya da gümüş çıkarma, işlemin belirgin uzmanlık örneğidir."},{"facet_id":"F003","role":"example","statement":"İç kısmı kabuktan veya taneyi samandan çıkarma, aynı ayırıp çıkarma yapısını somutlaştırır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Fiziksel çıkarma gerektirmeyen sıradan tercihlerle kolayca karışır.","fit":"narrowing","loses":"İçteki kısmın taş, toprak veya kabuk gibi çevreleyici maddeden çıkarılması işlemini siler.","preserves":"Değerli kısmın ötekilerden ayırt edilmesi yönünü korur."},"text":"seçme"}],"identity_rationale":"Kaynak ifadesi, değerli veya yararlı iç kısmın onu çevreleyen taş, toprak, kabuk ya da sap gibi maddelerden ayrılıp çıkarılmasını açıkça merkeze alır. Verilen dal çerçevesi hem çıkarma işlemini hem de elde edilen kısmın ayırt edilmesini doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"özlü veya değerli kısmı ayırıp çıkarma"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"taş veya maden toprağından değerli metal çıkaran kişi"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"maden toprağını işleyip değerli kısmını çıkaran kadın"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ayrılıp elde edilen özlü veya değerli kısım"}],"lexicalization_note":"Dal yalın anlamı tanımlar: iç veya değerli bölüm örtücü maddeden ayrılıp çıkarılır; belirli bir kuruluşun ek anlamı tanıma katılmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; seçilen iki karşılaştırma, işlemin sıradan seçmeden ve işlem sonunda bulunan metal parçasından farkını doğrudan açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalının çekirdeğinde çevreleyici maddeden fiziksel ayırma ve çıkarma vardır; komşu dalın çekirdeği ise iyi veya seçkin olanı almaktır.","focus_only":"Değerli iç kısmın bir taş, toprak, kabuk veya benzeri örtüden çıkarılmasını gerektirir.","gloss":"öz çıkarma ile seçkin kısmı alma","neighbor_only":"En iyi kısmı, onu saran bir maddeden çıkarma şartı olmadan seçebilir.","neighbor_ref":"root_000620/B007","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir bütün içinden daha değerli veya yararlı kısmı elde etmeye yönelir."},{"boundary_match":"field_only","distinction":"Odak dalı ayırıp çıkarma işlemini, komşu dal ise bu ortamda bulunan ve seçilen metal parçalarını merkeze alır.","focus_only":"Değerli metali taşı veya toprağı işleyerek çıkarma sürecini adlandırır.","gloss":"çıkarma işlemi ile seçilmiş metal parçası","neighbor_only":"Madende bulunup seçilen altın veya gümüş parçalarını nesne olarak adlandırır.","neighbor_ref":"root_001369/B004","relation_type":"same_field","shared_zone":"İki dal da maden ortamında değerli metalin değersiz maddeden ayrılması alanına aittir."}],"source_phrase_ar":"أصل التحصيل استخراج الذهب أو الفضة من الحجر أو من تراب المعدن (maqayis)؛ التحصيل تمييز ما يحصل (ayn)؛ المحصلة المرأة التي تحصل تراب المعدن (sihah)؛ التحصيل إخراج اللب من القشور كإخراج الذهب من حجر المعدن والبر من التبن (mufradat)","source_summary":"Ortak içerik, değerli kısmın taş, maden toprağı, kabuk veya saman gibi çevreleyici maddelerden ayrılıp çıkarılmasını ve çıkan kısmın seçilerek belirlenmesini anlatır. Ayrıca maden toprağını işleyerek değerli kısmını çıkaran kadın için kullanılan ayrı bir fail türevi kaydedilir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه التحصيل بمعنى إخراج اللب من القشور، وإخراج الذهب أو الفضة من حجر المعدن أو ترابه، وتمييز ما يحصل.","what_is_not_ar":"ليس كل جمع أو بقاء مجرد، ولا حوصلة الحيوان."},"support_links":["sup_2504d2d4e2312d87eca6"]},{"boundary":"Buradaki sonuç, soyut bir hesap sonucu değil, ayırma veya kaldırma sonrasında somut ya da kavramsal olarak geride kalan bölümdür.","branch_kind":"bare","branch_ref":"root_000330/B003","candidate_links":[{"candidate_id":"cand_281295ca6ef4618d9e6d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حُصِّلَ","morph_features":"STEM|POS:V|PERF|PASS|(II)|LEM:HuS~ila|ROOT:HSl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"100:10:1:2","qac_word_ref":"100:10:1","surface_ar":"حُصِّلَ"}],"gloss":"geride kalan artık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Öteki kısımlar gittikten veya ayrıldıktan sonra bir bölüm geride kalır ve varlığını sürdürür."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Harmanda tahıl kaldırıldıktan sonra kalan süprüntü, çekirdeğin tarımsal bir özelleşmesidir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Posa, tortu ve geride kalan ince değersiz parçalar da bu kalanlık ilişkisiyle adlandırılır."}}],"root_ar":"ح ص ل","root_id":"root_000330","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir ayırma, kaldırma veya tüketilme sonrasında kalan bölümün genel ve özel artık türlerini kapsamak için uygundur.","boundary_detail":"Buradaki sonuç, soyut bir hesap sonucu değil, ayırma veya kaldırma sonrasında somut ya da kavramsal olarak geride kalan bölümdür.","branch_image_ar":"البقية والحثالة بعد الرفع أو الفصل","concept_gloss":"geride kalan artık","contextual_glosses":[{"applicability":"Tahıl harmandan kaldırıldıktan sonra yerde kalan süprüntü ve döküntü için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tarım dışındaki genel kalanları, posayı ve başka ince kalıntıları kapsamaz.","preserves":"Tahıl kaldırıldıktan sonra geride kalan değersiz artık yönünü korur."},"facet_ids":["F002"],"text":"harman süprüntüsü","usage_role":"contextual"},{"applicability":"Ayırma sonrasında kalan değersiz, ince veya çökmüş artıkların anlatıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Değer yargısı taşımayan genel kalanları ve özel harman süprüntüsünü bütünüyle kapsamaz.","preserves":"Ayırma sonunda geride kalan değersiz artık ve ince kalıntı yönünü korur."},"facet_ids":["F003"],"text":"posa ve tortu","usage_role":"contextual"}],"definition":"Bir şeyin öteki kısımları gittikten, kaldırıldıktan veya ayrıldıktan sonra geride kalan bölümüdür. Özellikle tahıl kaldırıldıktan sonra kalan süprüntü, posa ve ince döküntü gibi değersiz artıklar için kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Öteki kısımlar gittikten veya ayrıldıktan sonra bir bölüm geride kalır ve varlığını sürdürür."},{"facet_id":"F002","role":"specialization","statement":"Harmanda tahıl kaldırıldıktan sonra kalan süprüntü, çekirdeğin tarımsal bir özelleşmesidir."},{"facet_id":"F003","role":"specialization","statement":"Posa, tortu ve geride kalan ince değersiz parçalar da bu kalanlık ilişkisiyle adlandırılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Geride kalma veya ayrıştırma içermeyen her türlü soyut işlem sonucunu kapsama katar.","collision":"Hesap, karar veya iş sonucu anlamlarıyla karışarak somut kalanlık sınırını siler.","fit":"broadening","loses":null,"preserves":"Bir süreçten sonra ortaya çıkan son durumla zayıf bir ilişkiyi korur."},"text":"sonuç"}],"identity_rationale":"Kaynak ifadesi, başka kısımlar gittikten, kaldırıldıktan veya ayrıldıktan sonra kalan bölümü; özellikle harman artığını, döküntüyü ve ince değersiz kalıntıyı anlatır. Verilen dal çerçevesi bu ortak kalanlık ilişkisini ve özel artık türlerini doğru biçimde bir arada tutar.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bir şeyin geriye kalan bölümü"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"geriye kalanlar, artıklar"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"tahıl kaldırıldıktan sonra harmanda kalan süprüntü"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"posa ve geride kalan ince döküntü"}],"lexicalization_note":"Dal, geride kalan bölümün yalın anlamını tanımlar; örneklerdeki harman ve döküntü türleri bu çekirdeği özelleştirir.","neighbor_coverage_note":"Tüm adaylar gözden geçirildi; seçilen üç komşu genel kalan, az miktarda kalan ve tahıla özgü kalıntı sınırlarını en yararlı biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı ayrıştırma sonrasındaki artık ve döküntü görünümünü öne çıkarır; komşu dal, kalan şeyi türü ve oluşma yolu bakımından daha geniş tutar.","focus_only":"Ayırma veya kaldırma sonrasında kalan posa, süprüntü ve ince artık türlerini özellikle içerir.","gloss":"ayrıştırma artığı ile genel kalan","neighbor_only":"Para, yükümlülük veya iyilik gibi alanlarda kalan herhangi bir bölümü daha genel biçimde kapsar.","neighbor_ref":"root_000142/B002","relation_type":"near_synonym","shared_zone":"Her iki dalın çekirdeğinde öteki kısımlar gittikten sonra varlığını sürdüren bölüm bulunur."},{"boundary_match":"partial","distinction":"Odak dalında kalanın miktarı belirleyici değildir ve değersiz artık türleri öne çıkabilir; komşu dalın ayırıcı sınırı kalanın azlığıdır.","focus_only":"Kalanın az olmasını şart koşmaz ve harman artığı ile posayı da kapsar.","gloss":"artık ile az miktarda kalan","neighbor_only":"Kapta veya elde edilen şeyde yalnız küçük bir miktarın kalmasını özellikle gerektirir.","neighbor_ref":"root_000838/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da tüketme veya ayırma sonrasında geriye kalan bir bölümü anlatır."},{"boundary_match":"partial","distinction":"Odak dalı geride kalma ilişkisini genel çekirdek yapar; komşu dal belirli tahıl parçaları ve kabuk türleriyle nesne düzeyinde sınırlıdır.","focus_only":"Tahıl dışındaki posa, tortu ve genel artıkları da kapsar.","gloss":"genel artık ile tahıl kalıntıları","neighbor_only":"Tahılın başağında kalan taneyi, tane kabuğunu veya saman diplerini özel nesneler olarak adlandırır.","neighbor_ref":"root_001231/B012","relation_type":"near_neighbor","shared_zone":"İki dal, tahılın işlenmesi veya ayrılması sonrasında kalan maddelerde kesişir."}],"source_phrase_ar":"بقي وثبت وذهب ما سواه فهو حاصل (ayn)؛ حاصل الشيء ومحصوله بقيته والحصائل البقايا (sihah)؛ الحصالة ما يبقى في الأندر من الحب بعد ما يرفع الحب وهو الكناسة (sihah)؛ قيل للحثالة الحصيل (mufradat)","source_summary":"Ortak anlatım, öteki kısımlar ayrıldığında geride kalıp duran bölümü temel alır ve bu genel kalanı harman süprüntüsü, posa, tortu ve ince döküntü türleriyle somutlaştırır.","sources":["AY","SI","MU"],"what_is_ar":"يدخل فيه الحاصل والمحصول والحصائل بمعنى البقايا، والحصالة لما يبقى في الأندر من الحب بعد رفع الحب، والحصيل بمعنى الحثالة.","what_is_not_ar":"ليس المقصود هنا نتيجة الحساب المجردة إلا من جهة الباقي، ولا الحصل من البلح."},"support_links":["sup_2d341673516eb2c2409a"]},{"boundary":"Organ anlamı çekirdektir; kuş adı, koyun betimlemesi ve organla yapılan eylemler ayrı bağlı kullanımlar olarak tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_000330/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حُصِّلَ","morph_features":"STEM|POS:V|PERF|PASS|(II)|LEM:HuS~ila|ROOT:HSl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"100:10:1:2","qac_word_ref":"100:10:1","surface_ar":"حُصِّلَ"}],"gloss":"kuş kursağı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kuşun gövdesindeki bir kese, yutulan besinin toplandığı ve tutulduğu yer işlevini görür."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuşun bu keseyi doldurması, organa bağlı bir eylem olarak aynı söz ailesinde anlatılır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı ad, iri ve uzun boyunlu bir deniz kuşu için de kullanılır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Göbeğinin üstündeki karın bölümü belirgin biçimde büyümüş koyun, bu söz ailesinden bir biçimle nitelenir."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Kuşun boynunu büküp besin kesesini dışarı doğru çıkarması da organa bağlı bir eylemdir."}}],"root_ar":"ح ص ل","root_id":"root_000330","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın çekirdeği olan, kuşta besinin toplandığı ve geçici olarak tutulduğu organı doğal biçimde adlandırır.","boundary_detail":"Organ anlamı çekirdektir; kuş adı, koyun betimlemesi ve organla yapılan eylemler ayrı bağlı kullanımlar olarak tutulur.","branch_image_ar":"موضع يجتمع فيه الطعام في جوف الطائر","concept_gloss":"kuş kursağı","contextual_glosses":[{"applicability":"Kuşun besin kesesini yiyecekle doldurması eyleminin anlatıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Organın kendi adını ve öteki bağlı adlandırma ile betimlemeleri kapsamaz.","preserves":"Besinin kuşun kursağında toplanması ve organın dolması yönünü korur."},"facet_ids":["F002"],"text":"kursağını doldurma","usage_role":"contextual"},{"applicability":"Organ adıyla ayrıca adlandırılan iri, uzun boyunlu deniz kuşunun açıklanmasında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kuşun beyaz derisine ilişkin ayrıntıyı ve organ merkezli öteki kullanımları kapsamaz.","preserves":"Adlandırılan kuşun deniz kuşu oluşunu, iriliğini ve uzun boynunu korur."},"facet_ids":["F003"],"text":"uzun boyunlu iri deniz kuşu","usage_role":"explanatory"}],"definition":"Temel anlam, kuşlarda besinin toplandığı ve geçici olarak tutulduğu kesedir. Aynı söz ailesinde keseyi doldurma veya dışarı çıkarma eylemleri ile bu addan gelişmiş bir kuş adı ve karın biçimine ilişkin bir koyun betimlemesi de yer alır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kuşun gövdesindeki bir kese, yutulan besinin toplandığı ve tutulduğu yer işlevini görür."},{"facet_id":"F002","role":"associated_use","statement":"Kuşun bu keseyi doldurması, organa bağlı bir eylem olarak aynı söz ailesinde anlatılır."},{"facet_id":"F003","role":"source_variant","statement":"Aynı ad, iri ve uzun boyunlu bir deniz kuşu için de kullanılır."},{"facet_id":"F004","role":"associated_use","statement":"Göbeğinin üstündeki karın bölümü belirgin biçimde büyümüş koyun, bu söz ailesinden bir biçimle nitelenir."},{"facet_id":"F005","role":"associated_use","statement":"Kuşun boynunu büküp besin kesesini dışarı doğru çıkarması da organa bağlı bir eylemdir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Sindirimin temel olarak yürütüldüğü farklı bir organ anlamını ekler.","collision":"Kursağı sindirim sistemindeki başka bir organla karıştırır.","fit":"displacement","loses":"Besinin kuşta önce toplandığı özel kese olma niteliğini kaybeder.","preserves":"Beslenme sistemindeki bir iç organ olma yönünü genel olarak korur."},"text":"mide"}],"identity_rationale":"Kaynak ifadesinin ana odağı kuşta besinin toplandığı kesedir ve verilen çerçeve bunu doğru yakalar. Aynı ifade ayrıca bu adla anılan iri uzun boyunlu bir deniz kuşunu, göbeğinin üstü şişkin koyun betimlemesini ve kuşun boynunu büküp kesesini çıkarması ile keseyi doldurma eylemlerini içerdiğinden bunlar organın tanımıyla eş düzeyde birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kuşlarda besinin toplandığı kursak"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kuşların kursakları"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"uzun boyunlu, iri bir deniz kuşu"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"göbeğinin üstündeki karın bölümü büyümüş koyun"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kuşun boynunu büküp kursağını dışarı çıkarması"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"kursağını doldurma"}],"lexicalization_note":"Dal organı adlandıran yalın biçimlerle organa bağlı eylem ve betimlemeleri birlikte içerir; kuş adı ile koyun betimlemesi organın genel tanımına katılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen organ adı, taşlık ve geviş getirme karşılaştırmaları anatomik ve işlevsel sınırı en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"İki dalın çekirdeği kuşun aynı besin kesesini adlandırır; odak dala bağlı türevler ve yan kullanımlar bu çekirdek eşdeğerliğini değiştirmez.","focus_only":null,"gloss":"kuş kursağının iki adlandırması","neighbor_only":null,"neighbor_ref":"root_001215/B015","relation_type":"synonym","shared_zone":"Her iki dal da kuşta besinin toplandığı aynı organı adlandırır."},{"boundary_match":"partial","distinction":"Odak dalındaki organ besini toplar; komşu dalın organı ise taşları tutması ve öğütmeye katkısıyla ayrılır.","focus_only":"Yutulan besinin toplandığı ve geçici olarak tutulduğu kursağı anlatır.","gloss":"kursak ile taşlık","neighbor_only":"Kuşun yuttuğu küçük taşları toplayan öğütücü bölümü anlatır.","neighbor_ref":"root_001369/B008","relation_type":"near_neighbor","shared_zone":"İki dal da kuşun beslenme sistemindeki, yutulan maddeleri tutabilen özel bir bölümü anlatır."},{"boundary_match":"field_only","distinction":"Odak dalı bir organı ve ona bağlı eylemleri, komşu dal ise geri getirilen besini ve çiğneme sürecini anlatır.","focus_only":"Kuşun besini topladığı anatomik keseyi merkeze alır.","gloss":"besin kesesi ile geviş getirme","neighbor_only":"Geviş getiren hayvanın geri çıkardığı lokmayı ve geviş getirme eylemini merkeze alır.","neighbor_ref":"root_000235/B007","relation_type":"same_field","shared_zone":"Her iki dal hayvanlarda yutulan besinin tutulması veya yeniden işlenmesi alanındadır."}],"source_phrase_ar":"حوصلة الطائر لأنه يجمع فيها (maqayis)؛ حوصلة الطائر معروف والحوصلة طير ويجمع حواصل والحوصل الشاة واحونصل الطير (ayn)؛ الحوصلة واحدة حواصل الطير وقد حوصل أي ملأ حوصلته (sihah)؛ حوصلة الطير ما يحصل فيه الغذاء (mufradat)","source_summary":"Ortak içerik, kuşun besin kesesini yiyeceğin toplandığı yer olarak tanımlar; ayrıca keseyi doldurma ve dışarı çıkarma eylemlerini, aynı adla anılan iri deniz kuşunu ve karın biçimiyle nitelenen koyunu kaydeder.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه حوصلة الطائر وحواصل الطير، وملء الحوصلة، والطير المسمى الحوصلة، وما ألحقته العين من الحوصل للشاة واحونصال الطير.","what_is_not_ar":"ليس هو تحصيل الحساب أو الكلام، ولا البلح، ولا مرض الفرس."},"support_links":[]},{"boundary":"Anlam bütün hurma meyvelerini değil, sertleşme ve salkım ayrıntılarının belirginleşmesinden önceki erken evreyi kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000330/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حُصِّلَ","morph_features":"STEM|POS:V|PERF|PASS|(II)|LEM:HuS~ila|ROOT:HSl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"100:10:1:2","qac_word_ref":"100:10:1","surface_ar":"حُصِّلَ"}],"gloss":"erken evredeki hurma koruğu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hurma meyvesi, sertleşmeden ve salkımın ince dalları belirginleşmeden önceki erken evresindedir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu erken evredeki meyvelerin tek bir tanesi için ayrı bir tekil biçim kullanılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hurma ağacının bu erken evredeki meyveleri oluşturmaya başlaması kurulu bir ifadeyle anlatılır."}}],"root_ar":"ح ص ل","root_id":"root_000330","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Henüz sertleşmemiş ve salkımın ince dalları belirginleşmemiş hurma meyvesini evre sınırıyla birlikte anlatır.","boundary_detail":"Anlam bütün hurma meyvelerini değil, sertleşme ve salkım ayrıntılarının belirginleşmesinden önceki erken evreyi kapsar.","branch_image_ar":"بلح حصل من النخلة قبل اشتداده","concept_gloss":"erken evredeki hurma koruğu","contextual_glosses":[{"applicability":"Meyvenin erken evresini günlük dilde açıklarken, özellikle sertleşmeme koşulunu öne çıkarmak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Salkımın ince dallarının henüz belirginleşmemiş olması koşulunu açıkça söylemez.","preserves":"Hurma meyvesini ve henüz sertleşmemiş olma koşulunu korur."},"facet_ids":["F001"],"text":"henüz sertleşmemiş hurma","usage_role":"explanatory"},{"applicability":"Hurma ağacının bu erken evredeki meyveleri vermeye başladığını anlatan ağaç merkezli bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Meyvenin kendi adını ve tekil meyve biçimini kapsamaz.","preserves":"Ağacın tanımlanan erken evrede meyve oluşturmaya başlaması yönünü korur."},"facet_ids":["F003"],"text":"hurmanın erken meyveye durması","usage_role":"contextual"}],"definition":"Hurma meyvesinin henüz sertleşmediği ve salkımın ince dallarının belirginleşmediği erken gelişim evresindeki halidir. Aynı söz ailesi bu evredeki tek meyveyi ve hurma ağacının böyle meyveler vermeye başlamasını da anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hurma meyvesi, sertleşmeden ve salkımın ince dalları belirginleşmeden önceki erken evresindedir."},{"facet_id":"F002","role":"specialization","statement":"Bu erken evredeki meyvelerin tek bir tanesi için ayrı bir tekil biçim kullanılır."},{"facet_id":"F003","role":"associated_use","statement":"Hurma ağacının bu erken evredeki meyveleri oluşturmaya başlaması kurulu bir ifadeyle anlatılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Olgunluk ve gelişim evresi ayırmadan bütün hurma meyvelerini kapsama katar.","collision":"Erken evreyi olgun veya başka gelişim basamaklarındaki hurmayla karıştırır.","fit":"broadening","loses":null,"preserves":"Söz konusu meyvenin hurma oluşunu korur."},"text":"hurma"}],"identity_rationale":"Kaynak ifadesi, hurma meyvesinin sertleşmesinden ve salkımın ince dallarının belirginleşmesinden önceki erken evresini, bu evredeki tek meyveyi ve ağacın bu meyveleri vermeye başlamasını birlikte belirtir. Verilen dal çerçevesi evreyi ve ona bağlı biçimleri doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"sertleşmemiş, salkım dalları henüz belirginleşmemiş hurma koruğu"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bu erken evredeki tek bir hurma meyvesi"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"hurma ağacının bu erken evrede meyve vermeye başlaması"}],"lexicalization_note":"Dal erken evredeki meyveyi adlandıran yalın biçimlerle ağacın bu evreye gelmesini anlatan kurulu ifadeyi ayırır; ağaç kuruluşu meyve adının çekirdeğine eklenmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; seçilen üç komşu genel koruk adını, başka bir ham hurma durumunu ve bir yanı olgunlaşmış sonraki evreyi ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı erken evreyi iki gelişim belirtisiyle daraltır; komşu dal olgunlaşmamış hurma için daha genel bir addır.","focus_only":"Meyvenin sertleşmemesi ve salkımın ince dallarının henüz belirginleşmemesi koşullarını taşır.","gloss":"erken hurma evresi ile genel hurma koruğu","neighbor_only":"Hurma koruğunu bu iki gelişim göstergesini zorunlu kılmadan daha genel adlandırır.","neighbor_ref":"root_000435/B013","relation_type":"near_synonym","shared_zone":"Her iki dal da olgunlaşmamış hurma meyvesini adlandırır."},{"boundary_match":"partial","distinction":"Odak dalı çok erken gelişim belirtileriyle tanımlanır; komşu dalın kapsamı bu belirtilere bağlı değildir ve farklı bir sonraki duruma uzanabilir.","focus_only":"Sertleşme ve salkım dallarının belirginleşmesinden önceki evreyi özellikle sınırlar.","gloss":"erken koruk ile başka ham hurma evresi","neighbor_only":"Bazı kullanımlarda buruşmuş ve kokusu güzelleşmiş daha farklı bir meyve durumunu da içerebilir.","neighbor_ref":"root_000767/B005","relation_type":"near_synonym","shared_zone":"İki dal da hurmanın olgunlaşma öncesindeki meyvesini kapsar."},{"boundary_match":"partial","distinction":"Odak dalı olgunlaşmanın belirginleşmesinden önceki basamaktır; komşu dalda ise meyvenin bir yanında olgunlaşma başlamıştır.","focus_only":"Meyvenin bütünüyle erken ve henüz sertleşmemiş evresini anlatır.","gloss":"erken koruk ile bir yanı olgunlaşan hurma","neighbor_only":"Meyvenin bir yanında olgunlaşma ve yumuşama başlamış olmasını gerektirir.","neighbor_ref":"root_001023/B012","relation_type":"near_neighbor","shared_zone":"Her iki dal hurma meyvesinin olgunlaşma sürecindeki belirli bir evresini adlandırır."}],"source_phrase_ar":"الحصل البلح قبل أن يشتد ويظهر ثفاريقه الواحدة حصلة لأنه حصل من النخلة (maqayis)؛ الحصل أيضا البلح قبل أن يشتد وتظهر ثفاريقه الواحدة حصلة وقد أحصل النخل (sihah)","source_summary":"Ortak anlatım, hurmanın sertleşme ve salkım ayrıntılarının belirginleşmesinden önceki erken meyve evresini tanımlar; tek bir meyve ile ağacın bu evreye gelmesi de aynı içerikte belirtilir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه الحصل: البلح قبل أن يشتد وتظهر ثفاريقه، وقولهم أحصل النخل.","what_is_not_ar":"ليس هو البقايا ولا الحوصلة ولا التحصيل المجرد."},"support_links":[]},{"boundary":"Bu anlam yalnız ata ve toprak yemenin yol açtığı karın rahatsızlığına bağlıdır; genel hastalanma veya genel karın ağrısı anlamına genişletilmez.","branch_kind":"collocation","branch_ref":"root_000330/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حُصِّلَ","morph_features":"STEM|POS:V|PERF|PASS|(II)|LEM:HuS~ila|ROOT:HSl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"100:10:1:2","qac_word_ref":"100:10:1","surface_ar":"حُصِّلَ"}],"gloss":"toprak yiyen atın karın ağrısı çekmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Rahatsızlanan hayvan attır ve belirti karın ağrısı ya da karın şikayetidir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Karın rahatsızlığının belirtilen nedeni, atın toprak veya bitkilerin çevresindeki toprağı yemesidir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kullanımın söz ailesinin genel anlamından türeyişi belirsiz görülür ve düzenli çekirdeğin dışında tutulur."}}],"root_ar":"ح ص ل","root_id":"root_000330","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız atın toprak yemesiyle ortaya çıkan karın rahatsızlığını bütün katılımcı ve neden koşullarıyla karşılar.","boundary_detail":"Bu anlam yalnız ata ve toprak yemenin yol açtığı karın rahatsızlığına bağlıdır; genel hastalanma veya genel karın ağrısı anlamına genişletilmez.","branch_image_ar":"وجع بطن الفرس من أكل التراب","concept_gloss":"toprak yiyen atın karın ağrısı çekmesi","contextual_glosses":[{"applicability":"Özne zaten at olarak açıkça verildiğinde, neden ile karın rahatsızlığını doğal bir yüklem olarak karşılar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"At katılımcısını karşılığın kendi içinde açıkça belirtmez.","preserves":"Toprak yeme nedenini ve bunun ardından gelişen karın ağrısını korur."},"facet_ids":["F001","F002"],"text":"toprak yemekten karnı ağrımak","usage_role":"contextual"}],"definition":"Atın toprak ya da bitkilerin çevresindeki toprağı yemesi sonucunda karın ağrısı veya karın rahatsızlığı çekmesidir. Bu kullanım, söz ailesinin genel toplama anlamına bağlanmayan kalıplaşmış bir hayvan hastalığı anlatımıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Rahatsızlanan hayvan attır ve belirti karın ağrısı ya da karın şikayetidir."},{"facet_id":"F002","role":"core","statement":"Karın rahatsızlığının belirtilen nedeni, atın toprak veya bitkilerin çevresindeki toprağı yemesidir."},{"facet_id":"F003","role":"source_variant","statement":"Kullanımın söz ailesinin genel anlamından türeyişi belirsiz görülür ve düzenli çekirdeğin dışında tutulur."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Her tür canlıyı, hastalığı, organı ve nedeni kapsayabilecek sınırsız bir anlam ekler.","collision":"At, karın ve toprak yeme koşullarını silerek genel hastalık anlatımıyla karışır.","fit":"broadening","loses":null,"preserves":"Hayvanın sağlığının bozulması yönünü çok genel biçimde korur."},"text":"hastalanmak"}],"identity_rationale":"Kaynak ifadesi, atın toprak veya bitki çevresindeki toprağı yemesi yüzünden karnından rahatsızlanmasını tutarlı biçimde anlatır ve bu kullanımın ana toplama anlamından ayrı görüldüğünü de belirtir. Verilen dal çerçevesi hayvanı, nedeni ve rahatsızlık yerini doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"atın toprak yemesi yüzünden karın ağrısı çekmesi"}],"lexicalization_note":"Dal yalnız belirtilen at merkezli kuruluşta geçerlidir; toprak yeme nedenini ve karın rahatsızlığını korur, yalın köke genel hastalanma anlamı yüklemez.","neighbor_coverage_note":"Tüm komşular değerlendirildi; seçilenler aynı olay yapısındaki deve rahatsızlığını, genel karın ağrısını ve yem kaynaklı karın şişmesini ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Olay yapıları benzerdir; odak dalında hayvan at ve neden toprakken, komşu dalda hayvan deve ve neden belirli bir çalıdır.","focus_only":"Atın toprak yemesi nedeniyle karın rahatsızlığı çekmesini gerektirir.","gloss":"atta toprak kaynaklı ve devede bitki kaynaklı karın ağrısı","neighbor_only":"Develerin belirli bir çalıyı yemesi nedeniyle karın rahatsızlığı çekmesini gerektirir.","neighbor_ref":"root_000026/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir otlama veya yeme maddesinin belirli bir hayvanda karın şikayeti doğurmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dalı tür ve neden bakımından dar bir kalıptır; komşu dal karın ağrısını bu koşullar olmadan daha genel bir hastalık adı olarak verir.","focus_only":"Rahatsızlığı ata ve toprak yeme nedenine bağlar.","gloss":"nedeni belirli at rahatsızlığı ile genel karın ağrısı","neighbor_only":"Karın ağrısını hayvan türü ve ortaya çıkış nedeni belirtmeden adlandırır.","neighbor_ref":"root_000245/B005","relation_type":"near_synonym","shared_zone":"İki dalın ortak çekirdeği karında duyulan ağrı veya rahatsızlıktır."},{"boundary_match":"partial","distinction":"Odak dalının ayırıcı belirtisi toprak kaynaklı karın ağrısıdır; komşu dalda esas belirti şişme, neden ise uygun olmayan ottur.","focus_only":"Atın toprak yemesinden sonra karın ağrısı çekmesini anlatır ve şişme şartı koymaz.","gloss":"karın ağrısı ile yem kaynaklı şişme","neighbor_only":"Uygunsuz ot yemekten doğan belirgin karın şişmesini ve ağırlaşarak ölüme yaklaşabilen durumu anlatır.","neighbor_ref":"root_000289/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal hayvanın yediği uygun olmayan madde sonrasında ortaya çıkan karın rahatsızlığı alanındadır."}],"source_phrase_ar":"مما شذ عن الباب وما أدري مم اشتقاقه قولهم حصل الفرس إذا اشتكى بطنه عن أكل التراب (maqayis)؛ حصل الفرس حصلا إذا اشتكى بطنه من أكل تراب النبت (sihah)؛ حصل الفرس إذا اشتكى بطنه عن أكله (mufradat)","source_summary":"Ortak anlatım, atın toprak yemesi yüzünden karnından rahatsızlanmasını bildirir; ayrıca bu kalıplaşmış kullanımın söz ailesinin düzenli genel anlamıyla açık bir türetim ilişkisi taşımadığı belirtilir.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه حصل الفرس إذا اشتكى بطنه من أكل التراب أو تراب النبت.","what_is_not_ar":"ليس هو أصل الجمع والتحصيل، وقد ميزته المصادر عن الباب القياسي."},"support_links":[]},{"boundary":"Dalın çekirdeği göğüs bölgesidir; giysi, damga, bağ, rahatsızlık ve güçlü göğüslü aslan kullanımları bu çekirdeğe bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000849/B001","candidate_links":[{"candidate_id":"cand_0692fa16c3cce4eebb69","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:10:4:2","qac_word_ref":"100:10:4","surface_ar":"صُّدُورِ"}],"gloss":"göğüs bölgesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan ve hayvan gövdesinin boyun altındaki ön bölgesini belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsanda göğsün üstte belirgin biçimde çıkıntı yapan kesimini gösterebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Göğsün ağrıması, bu bölgeden rahatsız olma veya göğse bir şeyle vurma bu bedensel çekirdeğe bağlı kullanımlardır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Göğsü örten giysi, hayvanın göğsündeki damga ve yükü tutan göğüs bağı aynı beden bölgesine göre adlandırılır."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Aslana verilen ad, hayvanın güçlü göğüslü oluşuna dayanan bir nitelemedir."}}],"root_ar":"ص د ر","root_id":"root_000849","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan veya hayvan gövdesindeki temel anatomik bölgeyi karşılar; dalın öteki kullanımları bu anlamdan türemiştir.","boundary_detail":"Dalın çekirdeği göğüs bölgesidir; giysi, damga, bağ, rahatsızlık ve güçlü göğüslü aslan kullanımları bu çekirdeğe bağlıdır.","branch_image_ar":"الصدر الجارحة وما يتصل بها","concept_gloss":"göğüs bölgesi","contextual_glosses":[{"applicability":"İnsan göğsünün üstte belirginleşen özel kesiminden söz edildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Göğsün üstte çıkıntı yapan kesimine yönelik dar bağlamı korur."},"facet_ids":["F002"],"text":"göğsün üst çıkıntısı","usage_role":"contextual"},{"applicability":"Bir kişinin göğsünde ağrı ya da rahatsızlık bulunmasını anlatan eylem bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Rahatsızlığın göğüs bölgesinde bulunması bilgisini korur."},"facet_ids":["F003"],"text":"göğsü ağrımak","usage_role":"contextual"},{"applicability":"Bir hayvanda yükü sabitlemek üzere göğüs çevresinden geçirilen bağ veya kemer için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesnenin göğüste bulunmasını ve yükü sabitleme görevini korur."},"facet_ids":["F004"],"text":"göğüs bağı","usage_role":"contextual"}],"definition":"İnsan ya da hayvan gövdesinin boyun ile karın arasında kalan ön ve üst bölgesidir. Bu çekirdekten, üstte kabaran kesim, buradaki ağrı veya yaralanma, bölgeyi örten ya da bağlayan nesneler, üzerindeki damga ve güçlü göğsüyle nitelenen aslan kullanımları doğar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan ve hayvan gövdesinin boyun altındaki ön bölgesini belirtir."},{"facet_id":"F002","role":"specialization","statement":"İnsanda göğsün üstte belirgin biçimde çıkıntı yapan kesimini gösterebilir."},{"facet_id":"F003","role":"associated_use","statement":"Göğsün ağrıması, bu bölgeden rahatsız olma veya göğse bir şeyle vurma bu bedensel çekirdeğe bağlı kullanımlardır."},{"facet_id":"F004","role":"associated_use","statement":"Göğsü örten giysi, hayvanın göğsündeki damga ve yükü tutan göğüs bağı aynı beden bölgesine göre adlandırılır."},{"facet_id":"F005","role":"extension","statement":"Aslana verilen ad, hayvanın güçlü göğüslü oluşuna dayanan bir nitelemedir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Zamansal ya da sırasal ilk olma anlamını ekler.","collision":"Aynı kökün ön, üst ve ilk kesim dalıyla karışır.","fit":"displacement","loses":"Anatomik göğüs bölgesini ve bedensel sınırını bütünüyle kaybeder.","preserves":"Önde bulunma çağrışımını dolaylı olarak koruyabilir."},"text":"başlangıç"}],"identity_rationale":"Kaynak ifadesi, insanın göğsünü temel beden bölgesi olarak verir ve hayvandaki karşılığını, göğsün üstte çıkıntılı kesimini, bu bölgedeki ağrı ya da yaralanmayı ve göğüsle ilişkili nesne ile adlandırmaları aynı dalda toplar. Geçici çerçeve bu çekirdek ile ona bağlı kullanımların sırasını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"göğüs"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"göğüsler"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"göğsün üstte çıkıntılı kesimi"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"göğsü örten kısa giysi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"devenin göğsündeki damga"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yükü sabitleyen göğüs bağı"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"göğsünden rahatsız olan kimse"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"birinin göğsüne bir şeyle vurmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"göğsü ağrımak"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"güçlü göğüslü aslan"}],"lexicalization_note":"Çıplak biçimin anatomik anlamı temel alınır; ağrı, yaralama, örtme, bağlama ve adlandırma anlamları yalnız kendi türemiş biçimleri içinde değerlendirilir.","neighbor_coverage_note":"Bütün adaylar anatomik kapsam ve bağımlı türetimler bakımından değerlendirildi; yalnız eşanlamlı göğüs çekirdeği ile et ve kemik sınırlarını açıklayan üç karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek anatomik sınır bakımından anlamlı bir ayrım yoktur; odak daldaki giysi, ağrı ve benzeri türemiş örnekler eşanlamlı çekirdeği değiştirmez.","focus_only":null,"gloss":"göğüs","neighbor_only":null,"neighbor_ref":"root_001315/B007","relation_type":"synonym","shared_zone":"Her iki dalın çekirdeği de gövdenin ön üst bölümündeki göğüs bölgesidir."},{"boundary_match":"partial","distinction":"Biri beden bölgesinin kendisini, öteki ise o bölgede bulunan belirli dokuyu adlandırır; bu nedenle olağan bağlamlarda birbirinin yerine geçmez.","focus_only":"Odak dalı göğüs bölgesinin tamamını anatomik bir yer olarak belirtir.","gloss":"göğüs eti","neighbor_only":"Komşu dal yalnız göğüs ve boyun çevresindeki eti belirtir.","neighbor_ref":"root_000095/B003","relation_type":"near_neighbor","shared_zone":"İki dal da göğüs çevresindeki aynı beden alanına yönelir."},{"boundary_match":"partial","distinction":"Odak geniş bir anatomik bölgedir; komşu ise bu bölgedeki kemiklere ve belirli bir yüzey konumuna özgüdür.","focus_only":"Odak dalı kemiklerle sınırlı olmayan bütün göğüs bölgesini kapsar.","gloss":"üst göğüs kemikleri","neighbor_only":"Komşu dal köprücük kemiği çevresindeki göğüs kemiklerini ve kolye yerini belirtir.","neighbor_ref":"root_000178/B005","relation_type":"near_neighbor","shared_zone":"Her ikisi de göğsün üst bölümünü bedensel konum olarak paylaşır."}],"source_phrase_ar":"الصدر للإنسان والجمع صدور (maqayis)؛ الصدر الجارحة (mufradat)؛ الصدرة من الإنسان ما أشرف من أعلى صدره (ayn;sihah;tahdhib)؛ صدر فلان إذا وجع صدره (ayn;tahdhib)؛ المصدور الذي يشتكي صدره (maqayis;sihah)؛ الصدار ثوب يغطي الصدر (maqayis;ayn;tahdhib;mufradat)؛ الصدار سمة على صدر البعير (maqayis;sihah;mufradat)؛ المصدر الأسد (maqayis;ayn;sihah)","source_summary":"Kaynakların ortak çizgisi göğsü anatomik merkez olarak kurar; üst çıkıntı, ağrı ve yaralama ile giysi, damga ve güçlü göğüslülüğe dayalı adlandırmalar bu merkezden açıklanır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"صدر الإنسان والحيوان وما أشرف من أعلاه، ووجع الصدر وإصابته، وما يغطى الصدر أو يسمه أو يشد عليه، وما سمي لقوة صدره","what_is_not_ar":"صدر الأمر؛ الصدور عن الماء؛ المصدر النحوي"},"support_links":["sup_2504d2d4e2312d87eca6"]},{"boundary":"Anatomik göğsün kendisi bu dalın çekirdeği değildir; beden bölgesinden taşınan ön, üst veya ilk konum ilişkisi belirleyicidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000849/B002","candidate_links":[{"candidate_id":"cand_a03e4f778b8ef036281f","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:10:4:2","qac_word_ref":"100:10:4","surface_ar":"صُّدُورِ"}],"gloss":"ön, üst ya da başlangıç bölümü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesne, oluş veya düzenin ön, üst ya da ilk kesimini belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Mızrak benzeri uzun bir nesnenin üst kısmını ve okun ortasından ucuna uzanan ön bölümünü gösterebilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir işin, toplantının, kitabın veya sözün ön ya da başlangıç bölümüne uygulanır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Atın göğsünü öne çıkararak rakiplerinden önce gelmesini anlatan yarış kullanımına temel olur."}}],"root_ar":"ص د ر","root_id":"root_000849","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın konumsal ve sırasal çekirdeğini birlikte vermek gereken genel açıklamalarda kullanılır.","boundary_detail":"Anatomik göğsün kendisi bu dalın çekirdeği değildir; beden bölgesinden taşınan ön, üst veya ilk konum ilişkisi belirleyicidir.","branch_image_ar":"المقدّم والأعلى والأول","concept_gloss":"ön, üst ya da başlangıç bölümü","contextual_glosses":[{"applicability":"Bir nesnenin ya da düzenlenmiş alanın öndeki kesimi söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bütün içindeki önde bulunma ilişkisini açık biçimde korur."},"facet_ids":["F001","F002"],"text":"ön kısım","usage_role":"contextual"},{"applicability":"Bir işin, kitabın veya sözün ilk bölümü anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sırasal olarak ilk bölüm olma anlamını eksiksiz korur."},"facet_ids":["F001","F003"],"text":"başlangıç","usage_role":"contextual"},{"applicability":"Bir atın yarışta göğsünü öne çıkararak önce gelmesini açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yarış üstünlüğünün atın göğsünün önde bulunmasıyla belirlenmesini korur."},"facet_ids":["F004"],"text":"göğüs farkıyla öne geçmek","usage_role":"explanatory"}],"definition":"Bir şeyin önde, üstte ya da başlangıçta bulunan kesimidir. Bu konumsal ve sırasal çekirdek uzun nesnelerin ön veya üst bölümlerinde, toplantı, kitap ve sözün başlangıcında ve atın göğsüyle öne geçmesinde özelleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesne, oluş veya düzenin ön, üst ya da ilk kesimini belirtir."},{"facet_id":"F002","role":"specialization","statement":"Mızrak benzeri uzun bir nesnenin üst kısmını ve okun ortasından ucuna uzanan ön bölümünü gösterebilir."},{"facet_id":"F003","role":"extension","statement":"Bir işin, toplantının, kitabın veya sözün ön ya da başlangıç bölümüne uygulanır."},{"facet_id":"F004","role":"associated_use","statement":"Atın göğsünü öne çıkararak rakiplerinden önce gelmesini anlatan yarış kullanımına temel olur."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Aynı kökün anatomik göğüs dalıyla karışır.","fit":"narrowing","loses":"Nesnelerin, işlerin ve metinlerin ön veya ilk bölümü olma kapsamını kaybeder.","preserves":"Önde ve üstte bulunma imgesinin bedensel kaynağını korur."},"text":"göğüs"}],"identity_rationale":"Kaynak ifadesi bir şeyin ön, üst veya ilk kesimini ortak çekirdek olarak açıkça verir; uzun nesnelerin bölümleri, işin başlangıcı, toplantı, kitap ve sözün ön kısmı ile atın göğsüyle öne geçmesi bu çekirdeğin düzenli özelleşmeleridir. Geçici çerçeve bu kapsamı doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ön, üst ya da başlangıç bölümü"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"mızrağın üst bölümü"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"işin başlangıcı"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"toplantının ön kısmı; kitabın veya sözün başlangıcı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"okun ortasından ucuna uzanan ön bölümü"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"ön gövdesi kalın ok"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"göğsüyle öne çıkıp yarışı geçmek"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kitaba giriş bölümü koymak"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"toplantının başköşesine oturmak"}],"lexicalization_note":"Çıplak biçimin ön, üst ve ilk kesim anlamı korunur; nesne, metin, toplantı ve yarış bağlamları kendi yapılarına bağlı özelleşmeler olarak tutulur.","neighbor_coverage_note":"Bütün adaylar konum, sıra ve hareket ayrımı üzerinden değerlendirildi; ön ve ilk bölümle en yakın iki dal, öne geçme olayı ve arka yön karşıtlığı sınırı en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Örtüşme ön ve ilk bölümde güçlüdür; odak dalının üstlük ve metinsel başlangıç kapsamı ile komşunun belirli beden ve nesne parçaları tam ikameyi engeller.","focus_only":"Odak dalı üst bölüm ve soyut başlangıç anlamlarını da genel çekirdeğe katar.","gloss":"ön veya ilk bölüm","neighbor_only":"Komşu dal yüz, baş, ordu, eyer, meme ve kuş tüyü gibi belirli ön parçaları ayrıca kapsar.","neighbor_ref":"root_001207/B007","relation_type":"near_synonym","shared_zone":"Her iki dal bir şeyin önde bulunan ya da ilk gelen bölümünü gösterebilir."},{"boundary_match":"partial","distinction":"Komşu başlangıç ve ilk görünüş üzerinde yoğunlaşırken odak dalı ayrıca uzamsal önlük ve üstlüğü kurucu seçenekler olarak taşır.","focus_only":"Odak dalı öndeki ve üstteki somut kesimleri de başlangıçla birlikte kapsar.","gloss":"ilk bölüm","neighbor_only":"Komşu dal bitkinin başı, yeni ay ve ayın ilk günleri gibi başlangıç örneklerine özgü uzanımlara sahiptir.","neighbor_ref":"root_001078/B005","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin başlangıcını veya ilk görünen kesimini anlatır."},{"boundary_match":"partial","distinction":"Odak ön konumu veya bölümü adlandırır; komşu ise o konuma doğru ilerleme ya da üstünlük kazanma olayını anlatır.","focus_only":"Odak dalı bir şeyin sabit ön, üst veya ilk bölümünü adlandırır.","gloss":"öne geçme","neighbor_only":"Komşu dal öne doğru ilerleme ve başkasını geçme hareketini temel alır.","neighbor_ref":"root_001207/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal önde bulunma ve başkalarından önce gelme alanında buluşur."},{"boundary_match":"opposed","distinction":"Uzamsal ön ve arka anlamları doğrudan karşıttır; odak dalındaki üst ve başlangıç uzanımları bu karşıtlığın dışında kalır.","focus_only":"Odak dalı ön tarafı ve buna bağlı üst veya ilk konumu kapsar.","gloss":"ön ve arka","neighbor_only":"Komşu dal arka tarafı ve önde olanın gerisinde kalma konumunu kapsar.","neighbor_ref":"root_000433/B002","relation_type":"antonym","shared_zone":"İki dal bir nesneye göre yön ve sıra belirleyen ortak bir eksen kurar."}],"source_phrase_ar":"الصدر أعلى مقدم كل شيء (ayn;tahdhib)؛ صدر القناة أعلاها (ayn;sihah;tahdhib;mufradat)؛ صدر الأمر أوله (ayn;tahdhib)؛ صدر كل شيء أوله (sihah)؛ صدر المجلس والكتاب والكلام (mufradat)؛ صدر السهم ما فوق نصفه إلى المراش (ayn;tahdhib)؛ صدر الفرس إذا جاء قد سبق بصدره (sihah;tahdhib;mufradat)","source_summary":"Kaynaklar ön, üst ve ilk olma ilişkisini ortak anlam olarak sunar; nesne bölümleri, metin ve toplantı başlangıçları ile göğsü öne çıkararak kazanılan yarış üstünlüğü bu ilişkinin bağlama göre görünüşleridir.","sources":["AY","SI","TA","MU"],"what_is_ar":"مقدّم الشيء وأعلاه وأوله، كصدر القناة والأمر والكتاب والمجلس والكلام، ومقدّم السهم، وسبق الفرس بصدره","what_is_not_ar":"الصدر الجارحة في نفسها؛ الانصراف عن الورد؛ المصادرة على مال"},"support_links":["sup_674f18cecc7526b82ee0"]},{"boundary":"Her ayrılma bu dala girmez; çekirdekte daha önce varılan yerden veya girilen durumdan ayrılma ve geri yönelme ilişkisi bulunur.","branch_kind":"mixed_non_bare","branch_ref":"root_000849/B003","candidate_links":[{"candidate_id":"cand_281295ca6ef4618d9e6d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:10:4:2","qac_word_ref":"100:10:4","surface_ar":"صُّدُورِ"}],"gloss":"geldiği yerden ayrılıp dönme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Daha önce varılan bir yerden veya girilen bir durumdan ayrılıp geri yönelmeyi belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Su içmek için su başına gelen insan veya hayvanların oradan ayrılması temel örnektir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen biçim, bir başkasını geri çevirip onun dönmesini sağlama anlamı taşır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Belirli söz öbeğinde yol, insanlarını su başından uzaklaştırıp geri götüren güzergah olarak nitelenir."}}],"root_ar":"ص د ر","root_id":"root_000849","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Önceki varış ile sonraki ayrılış aşamalarını birlikte belirtmek gereken genel bağlamlarda kullanılır.","boundary_detail":"Her ayrılma bu dala girmez; çekirdekte daha önce varılan yerden veya girilen durumdan ayrılma ve geri yönelme ilişkisi bulunur.","branch_image_ar":"الصُّدور عن المورد","concept_gloss":"geldiği yerden ayrılıp dönme","contextual_glosses":[{"applicability":"Su içmek üzere gelmiş insan veya hayvanların daha sonra su başını terk etmesi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Su başına gelişten sonraki ayrılma aşamasını tam olarak korur."},"facet_ids":["F001","F002"],"text":"su başından ayrılmak","usage_role":"contextual"},{"applicability":"Bir başkasının geldiği yerden ayrılıp dönmesini sağlama bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemi başkasına yaptırma ve geri yöneltme ilişkisini korur."},"facet_ids":["F003"],"text":"geri döndürmek","usage_role":"contextual"},{"applicability":"İnsanları su başından uzaklaştırıp geri götüren yolun niteliğini açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yolun su başından ayrılışa aracılık etmesi anlamını korur."},"facet_ids":["F004"],"text":"su başından dönüş yolu","usage_role":"explanatory"}],"definition":"Bir su başına, ülkeye ya da bir işe vardıktan veya girdikten sonra oradan ayrılıp geri yönelme hareketidir. Başkasını bu dönüşe yöneltme ve insanları su başından uzaklaştıran yol, bu çekirdeğe bağlı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Daha önce varılan bir yerden veya girilen bir durumdan ayrılıp geri yönelmeyi belirtir."},{"facet_id":"F002","role":"specialization","statement":"Su içmek için su başına gelen insan veya hayvanların oradan ayrılması temel örnektir."},{"facet_id":"F003","role":"associated_use","statement":"Ettirgen biçim, bir başkasını geri çevirip onun dönmesini sağlama anlamı taşır."},{"facet_id":"F004","role":"associated_use","statement":"Belirli söz öbeğinde yol, insanlarını su başından uzaklaştırıp geri götüren güzergah olarak nitelenir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Önceden varılmış bir yer ya da girilmiş bir durum bulunmayan her türlü ayrılmayı kapsama ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Bir yerden uzaklaşma hareketini genel düzeyde korur."},"text":"ayrılma"}],"identity_rationale":"Kaynak ifadesi, su başı, ülke veya başka bir işe varıştan sonra oradan ayrılmayı temel hareket olarak verir; bir başkasını geri çevirme ve insanlarını su başından uzaklaştıran yol da bu hareketin ettirgen ve yapıya bağlı uzanımlarıdır. Geçici çerçeve bu aşamaları birbirine karıştırmadan korur.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"bir yerden ya da durumdan ayrılış"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"su başından, geldikten sonra ayrılmak"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"geri döndürmek"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"su başından dönüşü sağlayan yol"}],"lexicalization_note":"Ayrılıp dönme olayı temel alınır; başkasını döndürme yalnız ettirgen biçime, su başından uzaklaştıran yol ise verilen söz öbeğine bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar önceki varış, iç-dış geçiş, geri yönelme ve yolculuk koşulları bakımından değerlendirildi; bu dört aday dalın hareket sınırını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında varıştan sonraki dönüş kurucudur; komşu dalda genel gidiş veya hızlı uzaklaşma yeterlidir.","focus_only":"Odak dalı önceden varılan yerden ayrılıp geri yönelme aşamasını gerektirir.","gloss":"ayrılıp gitme","neighbor_only":"Komşu dal yeryüzünde gitmeyi ve bir kişiden hızla uzaklaşmayı önceki varış koşulu olmadan kapsar.","neighbor_ref":"root_000325/B007","relation_type":"near_synonym","shared_zone":"İki dal da bir yerden uzaklaşma ve orayı geride bırakma hareketini anlatır."},{"boundary_match":"partial","distinction":"Çıkış, iç-dış sınırının aşılmasına dayanır; odak ise önceki varış ve ardından dönüş düzenini gerektirir.","focus_only":"Odak dalı bir yere geldikten sonra oradan ayrılıp geri yönelmeyi içerir.","gloss":"dışarı çıkma","neighbor_only":"Komşu dal yalnız bir şeyin içinden dışarı çıkmayı bildirir.","neighbor_ref":"root_001158/B004","relation_type":"near_synonym","shared_zone":"Her iki dal bir başlangıç alanını geride bırakma hareketinde örtüşür."},{"boundary_match":"partial","distinction":"Odak, varılan yerden çıkış anını adlandırır; komşu ise geri gelişin kendisini ve daha geniş gidip gelme olaylarını kapsar.","focus_only":"Odak dalı varılan kaynaktan ayrılma evresini merkeze alır.","gloss":"geri dönme","neighbor_only":"Komşu dal geri gelme, yeniden dönme ve bazı şeylerin gidip gelmesi gibi yinelenen hareketleri kapsar.","neighbor_ref":"root_000618/B004","relation_type":"near_neighbor","shared_zone":"İki dalın ortak alanı geriye yönelme ve önceki konumla yeniden ilişki kurmadır."},{"boundary_match":"thematic_only","distinction":"Odak önceki varışın ardından dönüşü, komşu ise yeni bir hedefe yönelen yolculuğu anlatır; ortaklık olay alanıyla sınırlıdır.","focus_only":"Odak dalı varıştan sonra kaynaktan veya yerden ayrılma aşamasını belirtir.","gloss":"yola çıkma","neighbor_only":"Komşu dal bir hedefe doğru yolculuğa çıkmayı ve seyahat etmeyi belirtir.","neighbor_ref":"root_000551/B001","relation_type":"thematic","shared_zone":"Her ikisi de bir yerden ayrılmayı içeren hareket senaryosunda yer alır."}],"source_phrase_ar":"صدر عن الماء وصدر عن البلاد (maqayis;sihah)؛ الصدر الانصراف عن الورد وعن كل أمر (ayn;tahdhib)؛ صدرت الإبل عن الماء (mufradat)؛ أصدرته فصدر أي رجعته فرجع (sihah)؛ طريق صادر يصدر بأهله عن الماء (ayn;sihah;tahdhib)","source_summary":"Kaynakların ortak anlamı, varılan su başından, ülkeden veya girilen bir işten ayrılıp geri yönelmektir; ettirgen dönüş ve bu ayrılışı sağlayan yol aynı hareket şemasına bağlıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الانصراف عن الماء أو البلاد أو كل أمر بعد وروده، والإصدار بمعنى الإرجاع، والطريق الصادر بأهله","what_is_not_ar":"الصدر الجارحة؛ صدر الشيء بمعنى أوله؛ المصدر النحوي"},"support_links":["sup_2d341673516eb2c2409a"]},{"boundary":"Dil bilgisel temel ana kullanımdır; çıkış yeri ve çıkış zamanı, ortak çıkma ilişkisine dayanan ayrı adlandırma seçenekleridir.","branch_kind":"bare","branch_ref":"root_000849/B004","candidate_links":[{"candidate_id":"cand_b377a37b3388bccc95af","lane":"micro"},{"candidate_id":"cand_281295ca6ef4618d9e6d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:10:4:2","qac_word_ref":"100:10:4","surface_ar":"صُّدُورِ"}],"gloss":"eylem türetme temeli; çıkış yeri veya zamanı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekimli eylem biçimlerinin türediği kabul edilen temel sözcük biçimini belirtir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı ad, çıkma olayının gerçekleştiği yer veya zamanı bildiren bir ad olarak da açıklanır."}}],"root_ar":"ص د ر","root_id":"root_000849","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın dil bilgisel çekirdeğiyle yer ve zaman uzanımını birlikte göstermek gereken sözlük açıklamasında kullanılır.","boundary_detail":"Dil bilgisel temel ana kullanımdır; çıkış yeri ve çıkış zamanı, ortak çıkma ilişkisine dayanan ayrı adlandırma seçenekleridir.","branch_image_ar":"الأصل الذي تصدر عنه الأفعال","concept_gloss":"eylem türetme temeli; çıkış yeri veya zamanı","contextual_glosses":[{"applicability":"Sözcük yapısında çekimli eylemlerin dayandırıldığı temel ad biçimi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Temel biçim ile ondan türeyen eylem biçimleri arasındaki yönü korur."},"facet_ids":["F001"],"text":"eylemlerin türediği temel biçim","usage_role":"explanatory"},{"applicability":"Bir çıkma olayının gerçekleştiği mekanın adı söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Adlandırılan unsurun çıkma olayına ait yer olması bilgisini korur."},"facet_ids":["F002"],"text":"çıkış yeri","usage_role":"contextual"},{"applicability":"Bir çıkma olayının gerçekleştiği zamanın adı söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Adlandırılan unsurun çıkma olayına ait zaman olması bilgisini korur."},"facet_ids":["F002"],"text":"çıkış zamanı","usage_role":"contextual"}],"definition":"Dil bilgisinde, çekimli eylem biçimlerinin kendisinden çıktığı kabul edilen temel sözcük biçimidir. Aynı ad, çıkma eyleminin gerçekleştiği yeri veya zamanı da gösterebilir; bu ikinci kullanım dil bilgisel temel ile özdeş değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekimli eylem biçimlerinin türediği kabul edilen temel sözcük biçimini belirtir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı ad, çıkma olayının gerçekleştiği yer veya zamanı bildiren bir ad olarak da açıklanır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Su kaynağı, bilgi belgesi ve genel köken gibi bu dala özgü olmayan çok sayıda anlamı kapsama ekler.","collision":"Genel köken ve maden ya da pınar komşularıyla kolayca karışır.","fit":"broadening","loses":null,"preserves":"Başka bir şeyin kendisinden çıkması ya da doğması ilişkisini korur."},"text":"kaynak"}],"identity_rationale":"Kaynak ifadesi, çekimli eylemlerin kendisinden çıktığı kabul edilen temel sözcük biçimi ile çıkmanın gerçekleştiği yer ve zamanı aynı ad altında anar. Geçici çerçeve kullanılabilir, ancak dil bilgisel türetme temeli ile olayın yeri veya zamanı tek bir kavrammış gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"eylemlerin türediği temel sözcük biçimi"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"çıkış yeri ya da zamanı"}],"lexicalization_note":"Dal, ad biçiminin çıplak anlam alanını tanımlar; dil bilgisel temel ile yer ve zaman anlamları ayrılır ve başka söz öbeklerinden kapsam aktarılmaz.","neighbor_coverage_note":"Bütün adaylar genel köken, somut kaynak, dil bilgisel işlev ve gerçek ayrılış bakımından değerlendirildi; seçilen dört karşılaştırma iki alt kullanımın sınırını doğrudan aydınlatır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak teknik bir sözcük biçimine ve çıkış olayının yer-zaman adlarına bağlıdır; komşu ise alan sınırlaması olmayan genel köken kavramıdır.","focus_only":"Odak dalı dil bilgisel temel biçimi ve çıkışın yer ya da zamanını adlandırır.","gloss":"köken","neighbor_only":"Komşu dal herhangi bir şeyin, kişinin veya olayın genel kökenini kapsar.","neighbor_ref":"root_000031/B002","relation_type":"near_synonym","shared_zone":"Her iki dal başka biçimlerin veya olayların kendisinden çıktığı başlangıç noktasını anlatabilir."},{"boundary_match":"partial","distinction":"Odak dil bilgisel ve olay yapısına bağlı bir adlandırmadır; komşu somut üretim veya akış kaynağını temel alır.","focus_only":"Odak dalı dil bilgisel türetme temelini ve olayın çıkış yeri ya da zamanını kapsar.","gloss":"çıktığı yer","neighbor_only":"Komşu dal maddelerin çıkarıldığı maden veya bir şeyin doğduğu somut pınar ve menba alanını kapsar.","neighbor_ref":"root_001475/B008","relation_type":"near_neighbor","shared_zone":"İki dal bir şeyin ortaya çıktığı başlangıç yerini gösterme alanında örtüşür."},{"boundary_match":"field_only","distinction":"Biri türetme yönündeki temel biçimdir, öteki cümle içindeki durum işaretidir; çekirdek işlemleri farklıdır.","focus_only":"Odak dalı eylem biçimlerinin dayandırıldığı temel sözcük biçimini belirtir.","gloss":"dil bilgisel biçim","neighbor_only":"Komşu dal sözcüğün cümledeki durumunu gösteren belirli bir dil bilgisi işaretlemesini belirtir.","neighbor_ref":"root_000582/B012","relation_type":"same_field","shared_zone":"Her iki dal sözcüklerin dil bilgisel çözümlemesi alanında kullanılır."},{"boundary_match":"partial","distinction":"Odak bir temel biçim veya yer-zaman adıdır; komşu ise katılımcının gerçekleştirdiği hareketin kendisidir.","focus_only":"Odak dalı çıkmanın dil bilgisel temelini ve olayın yer ya da zaman adını belirtir.","gloss":"çıkış ve ayrılış","neighbor_only":"Komşu dal varılan yerden gerçekten ayrılıp geri yönelme hareketini belirtir.","neighbor_ref":"root_000849/B003","relation_type":"near_neighbor","shared_zone":"İki dal çıkma ve bir başlangıç noktasından uzaklaşma düşüncesini paylaşır."}],"source_phrase_ar":"المصدر أصل الكلمة الذي تصدر عنه الأفعال (ayn;tahdhib)؛ مصادر الأفعال (sihah)؛ المصدر في الحقيقة صدر عن الماء ولموضع المصدر ولزمانه (mufradat)","source_summary":"Toplu kaynak anlatımı iki bağlı fakat ayrı kullanımı içerir: eylem biçimlerinin türediği dil bilgisel temel ve bir çıkma olayının yeri ya da zamanı. Ortak bağ, başka bir biçim veya olayın buradan çıkması düşüncesidir.","sources":["AY","SI","TA","MU"],"what_is_ar":"المصدر بوصفه أصل الكلمة أو الفعل، وما يلحق به من اسم الموضع والزمان في الصدور","what_is_not_ar":"الصدر الجارحة؛ صدر الشيء أوله؛ الصدور الحسي عن الماء"},"support_links":["sup_2d341673516eb2c2409a","sup_4b7ed36557097abb3cb9"]},{"boundary":"Anlam belirli yapılara bağlı bir ödeme ve güvence yükümlülüğüdür; malın zorla alınması tek başına bu dalı karşılamaz.","branch_kind":"non_bare","branch_ref":"root_000849/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:10:4:2","qac_word_ref":"100:10:4","surface_ar":"صُّدُورِ"}],"gloss":"para ödeme ve güvence yükümlülüğü koyma","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kimseye belirli bir para tutarını ödeme ve o tutarın güvencesini üstlenme yükümlülüğü konur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yapı, kimi açıklamada tarafların güvence altındaki para tutarı üzerinde hesaplaşması veya anlaşması olarak yorumlanır."}}],"root_ar":"ص د ر","root_id":"root_000849","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli yapı içinde bir kişiye ödeyeceği tutar için sorumluluk yüklendiğini açıklamak üzere kullanılır.","boundary_detail":"Anlam belirli yapılara bağlı bir ödeme ve güvence yükümlülüğüdür; malın zorla alınması tek başına bu dalı karşılamaz.","branch_image_ar":"المصادرة على مال","concept_gloss":"para ödeme ve güvence yükümlülüğü koyma","contextual_glosses":[{"applicability":"Bir kişiye belirlenmiş para tutarını ödeme ve güvenceye alma sorumluluğu verildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yükümlü kılınan kişiyi, belirli tutarı ve ödeme sorumluluğunu korur."},"facet_ids":["F001"],"text":"belli bir tutarı ödemekle yükümlü kılmak","usage_role":"explanatory"},{"applicability":"Tarafların güvence altına alınacak para tutarını belirleyip ayrılması veya anlaşması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli para tutarı üzerinde anlaşma ve sorumluluğu üstlenme ilişkisini korur."},"facet_ids":["F002"],"text":"ödeme tutarı üzerinde hesaplaşmak","usage_role":"contextual"}],"definition":"Belirli yapılarda, bir kimseyi belirli bir parayı ödemek ve bu tutardan sorumlu olmakla yükümlü kılmayı; kimi bağlamlarda da bu yükümlülük üzerinde hesaplaşmayı anlatır. Doğrudan malına el koyma anlamı zorunlu değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kimseye belirli bir para tutarını ödeme ve o tutarın güvencesini üstlenme yükümlülüğü konur."},{"facet_id":"F002","role":"source_variant","statement":"Yapı, kimi açıklamada tarafların güvence altındaki para tutarı üzerinde hesaplaşması veya anlaşması olarak yorumlanır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Malın doğrudan alınması ve mülkiyetin kişiden çıkarılması sonucunu ekler.","collision":"Çağdaş zorla alma anlamıyla karışarak kaynak sınırını değiştirir.","fit":"displacement","loses":"Belirli tutarı ödeme ve bu tutardan sorumlu olma ilişkisini kaybeder.","preserves":"Bir kişinin mal varlığına yönelen zorlayıcı mali işlem çağrışımını korur."},"text":"malına el koymak"}],"identity_rationale":"Kaynak ifadesi modern anlamdaki doğrudan mala el koymayı zorunlu kılmaz; belirli yapılarda bir kimseye ödeyeceği ve güvencesini üstleneceği bir tutar yüklenmesini, kimi açıklamada da bu tutar üzerinde hesaplaşmayı anlatır. Bu nedenle dal korunabilir, fakat geçici el koyma çerçevesi mali yükümlülük olarak düzeltilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"birini belli bir parayı ödemek ve güvence altına almakla yükümlü kılmak"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"kendisine para ödeme ve güvence yükümlülüğü konmak"}],"lexicalization_note":"Anlam yalnız verilen kişi ve para yapılarında geçerlidir; çıplak köke genel el koyma, vergi alma veya ödeme anlamı yüklenmez.","neighbor_coverage_note":"Bütün adaylar yükümlülük kurma, hakkı ödeme, alacak isteme ve belirli mali ödeme türleri bakımından değerlendirildi; seçilen dört aday işlem ile sonuç arasındaki sınırı gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak sorumluluğun kişiye yüklenmesini, komşu ise mevcut sorumluluğun ödeme yoluyla yerine getirilmesini temel alır.","focus_only":"Odak dalı belirli tutar için ödeme ve güvence yükümlülüğünü kurar.","gloss":"ödeme yükümlülüğü ve ödeme","neighbor_only":"Komşu dal önceden var olan borç, vergi veya emanet hakkının fiilen yerine getirilmesini anlatır.","neighbor_ref":"root_000021/B002","relation_type":"near_neighbor","shared_zone":"İki dal bir hakkın veya para borcunun ödenmesi alanında buluşur."},{"boundary_match":"partial","distinction":"Odak yükümlülüğün kurulmasına, komşu ise kurulmuş hakkın talep ve tahsiline dayanır.","focus_only":"Odak dalı kişiyi belirli bir tutardan sorumlu kılma işlemini belirtir.","gloss":"mali sorumluluk ve alacak isteme","neighbor_only":"Komşu dal hak sahibinin mevcut alacağını sürekli istemesi ve tahsil etmeye çalışmasını belirtir.","neighbor_ref":"root_000943/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal bir kişinin başkasından para veya hak istemesiyle ilişkili olabilir."},{"boundary_match":"field_only","distinction":"Odak kişi üzerinde kurulan sorumluluktur; komşu ise verilen veya çıkarılan mali değerin türünü adlandırır.","focus_only":"Odak dalı kişiye ödeme ve güvence sorumluluğu yükleyen işlemi anlatır.","gloss":"mali yükümlülük","neighbor_only":"Komşu dal belirli bir yolla çıkarılan para, ürün, vergi veya payın kendisini anlatır.","neighbor_ref":"root_000400/B003","relation_type":"same_field","shared_zone":"İki dal düzenlenmiş bir mali ödeme ve belirlenmiş tutar alanını paylaşır."},{"boundary_match":"field_only","distinction":"Odak bir yükümlü kılma işlemi ve güvencedir; komşu ise belirli hukuki bağlamdaki ödeme türüdür.","focus_only":"Odak dalı herhangi bir kişiye belirli yapı içinde yüklenen para sorumluluğunu belirtir.","gloss":"yüklenen mali ödeme","neighbor_only":"Komşu dal belirli bir topluluğa hukuki statüsü nedeniyle konan özel mali ödemeyi belirtir.","neighbor_ref":"root_000244/B004","relation_type":"same_field","shared_zone":"Her iki dal bir kişinin ya da topluluğun ödemek zorunda bırakıldığı para alanındadır."}],"source_phrase_ar":"صادره على كذا (sihah)؛ صودر فلان العامل على مال يؤديه أي فورق على مال ضمنه (tahdhib)","source_summary":"Toplu kaynak anlatımı, belirli bir para için ödeme ve güvence sorumluluğu kurulmasında birleşir; anlatım bu sorumluluğun yüklenmesi ile tarafların tutar üzerinde hesaplaşması arasında değişir.","sources":["SI","TA"],"what_is_ar":"مصادرة العامل أو غيره على مال يؤديه ويضمنه","what_is_not_ar":"الصدر الجارحة؛ الصدور عن الماء؛ صدر الشيء أوله"},"support_links":[]},{"boundary":"Dal, bütünün herhangi bir bölümünü veya kümesini belirtir; ilk bölüm, beden parçası ya da sabit oran koşulu taşımaz.","branch_kind":"bare","branch_ref":"root_000849/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:10:4:2","qac_word_ref":"100:10:4","surface_ar":"صُّدُورِ"}],"gloss":"bir şeyin bölümü ya da kümesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin belirli olmayan bölümünü veya onun içindeki bir kümeyi belirtir."}}],"root_ar":"ص د ر","root_id":"root_000849","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bütünden ayrılan parçanın veya onun içindeki grubun oranı ve konumu belirtilmediğinde kullanılır.","boundary_detail":"Dal, bütünün herhangi bir bölümünü veya kümesini belirtir; ilk bölüm, beden parçası ya da sabit oran koşulu taşımaz.","branch_image_ar":"الطائفة من الشيء","concept_gloss":"bir şeyin bölümü ya da kümesi","contextual_glosses":[{"applicability":"Bir bütünün oranı belirtilmeyen kısmından söz edildiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bütüne bağlı ve oranı belirtilmeyen parça anlamını korur."},"facet_ids":["F001"],"text":"bir bölüm","usage_role":"general"},{"applicability":"Bir şeyin içinden birlikte ele alınan topluluk veya grup kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bütün içindeki öğelerin birlikte bir grup oluşturması anlamını korur."},"facet_ids":["F001"],"text":"bir küme","usage_role":"contextual"}],"definition":"Bir bütünün içinden ayrılan veya onun kapsamında düşünülen bölüm ya da kümedir. Bölümün yeri, büyüklüğü ve oranı anlam tarafından belirlenmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin belirli olmayan bölümünü veya onun içindeki bir kümeyi belirtir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Bütünün dokuz eşit parçaya ayrılması koşulunu ekler.","collision":"Belirli kesir bildiren komşu dalla karışır.","fit":"narrowing","loses":"Bölümün herhangi bir büyüklükte veya küme niteliğinde olabilmesi kapsamını kaybeder.","preserves":"Bir bütünün parçası olma özelliğini korur."},"text":"dokuzda bir"}],"identity_rationale":"Kaynak ifadesi, biçimi doğrudan bir şeyin bölümü veya ondan ayrılan topluluk anlamında tanımlar. Geçici çerçeve bu kısa ve bağımsız anlamı ne bütünün başı anlamıyla ne de belirli bir kesirle karıştırır.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"bir şeyin bölümü ya da kümesi"}],"lexicalization_note":"Çıplak biçimin bölüm veya küme anlamı tanımlanır; bölme eylemi, belirli kesirler ve başka yapılara bağlı özel anlamlar kapsama alınmaz.","neighbor_coverage_note":"Bütün adaylar genel parça, özel organ veya pay, sabit kesir ve tam bütün sınırları bakımından değerlendirildi; yayımlanan üç karşılaştırma dalın oranı belirsiz bölüm anlamını yeterince ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ad olarak bölüm anlamında büyük ölçüde örtüşürler; komşunun bölme işlemi ve bütünün kuruluşuna ilişkin kapsamı tam eşanlamlılığı engeller.","focus_only":"Odak dalı yalnız bölümün veya kümenin adını verir ve bir işlem gerektirmez.","gloss":"bölüm veya parça","neighbor_only":"Komşu dal bölme işlemini ve parçaların bütünü kuran yapısal öğeler olmasını da kapsar.","neighbor_ref":"root_000241/B002","relation_type":"near_synonym","shared_zone":"Her iki dal bir bütünün bölümü veya içindeki topluluk anlamında kullanılabilir."},{"boundary_match":"partial","distinction":"Odak belirlenmemiş bölüm ya da kümedir; komşu organ, et parçası ve pay gibi özelleşmiş parça türlerine uzanır.","focus_only":"Odak dalı cansız veya soyut bir bütün içindeki kümeyi de genel olarak kapsar.","gloss":"parça","neighbor_only":"Komşu dal beden organı, et parçası ve kişiye düşen pay gibi daha özel bölüm türlerini kapsar.","neighbor_ref":"root_000024/B003","relation_type":"near_synonym","shared_zone":"İki dal bir bütünden ayrılan bölüm anlamında birbirine yaklaşır."},{"boundary_match":"opposed","distinction":"Odak kapsamı bütünün bir kesimiyle sınırlar; komşu aynı varlığın eksiksiz tamamını kapsar.","focus_only":"Odak dalı bütünün içindeki yalnız bir bölüm veya kümeyi belirtir.","gloss":"bölüm ve bütün","neighbor_only":"Komşu dal hiçbir bölüm dışarıda kalmadan şeyin tamamını belirtir.","neighbor_ref":"root_000030/B005","relation_type":"antonym","shared_zone":"İki dal aynı şeyin ne kadarının kapsandığını belirleyen parça-bütün eksenindedir."}],"source_phrase_ar":"الصدر الطائفة من الشيء (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu bölüm veya küme anlamı, sağlanan kanıtta tek bir sözlük tarafından kaydedilmiştir."}],"source_summary":"Dal, bir bütünün belirli olmayan bölümü veya onun içindeki bir küme anlamını taşır; konum ve oran bakımından ek koşul bildirmez.","sources":["SI"],"what_is_ar":"الصدر بمعنى طائفة من الشيء","what_is_not_ar":"صدر الشيء بمعنى أوله؛ الصدر الجارحة؛ الصدور عن الماء"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["100:10:1"],"branch_refs":[],"candidate_id":"cand_a408509ec1ad46e3a73a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:10:1:container-rhyme-bridge","source_type":"word_analysis","support_ids":["sup_86299cf6efc53ad5e108","sup_c9732b61b7fc2f6b1809"],"title":"hinge carries the grave-chest pairing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:1","qac_refs":["100:10:1:1"],"status":"accepted"}},{"anchor_refs":["100:10:1"],"branch_refs":[],"candidate_id":"cand_eef53be60d88612e34cb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:10:1:fused-verbal-onset","source_type":"word_analysis","support_ids":["sup_22d743ed453996a4428b","sup_86299cf6efc53ad5e108"],"title":"proclitic onset fuses link and action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:1","qac_refs":["100:10:1:1"],"status":"accepted"}},{"anchor_refs":["100:10:1"],"branch_refs":[],"candidate_id":"cand_91ec0e6e88bc27d9acf7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:10:1:paired-disclosure-hinge","source_type":"word_analysis","support_ids":["sup_86299cf6efc53ad5e108","sup_d5134f3f1ce213256db6"],"title":"connector keeps the second disclosure in the same frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:1","qac_refs":["100:10:1:1"],"status":"accepted"}},{"anchor_refs":["100:10:2"],"branch_refs":[],"candidate_id":"cand_c6d424323a9aca4d8daf","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000330"],"scope":"focus_ayah","source_local_id":"100:10:2:boundary-knowledge-sequence","source_type":"word_analysis","support_ids":["sup_90583f0978f02d3b7d5b","sup_e11a2128b99143c4e1e3"],"title":"interior extraction answers the boundary movement","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:2","qac_refs":["100:10:1:2"],"status":"accepted"}},{"anchor_refs":["100:10:2"],"branch_refs":[],"candidate_id":"cand_e976283064256411173a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000330"],"scope":"focus_ayah","source_local_id":"100:10:2:compressed-sound","source_type":"word_analysis","support_ids":["sup_6534486c9183e854ff71","sup_90583f0978f02d3b7d5b"],"title":"tight sound mirrors compressed processing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:2","qac_refs":["100:10:1:2"],"status":"accepted"}},{"anchor_refs":["100:10:2"],"branch_refs":[],"candidate_id":"cand_a389187e04b3d1d2800e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000330"],"scope":"focus_ayah","source_local_id":"100:10:2:hapax-specialized-choice","source_type":"word_analysis","support_ids":["sup_90583f0978f02d3b7d5b","sup_929faa708b7b30610b82"],"title":"single Quranic root occurrence marks the verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:2","qac_refs":["100:10:1:2"],"status":"accepted"}},{"anchor_refs":["100:10:2"],"branch_refs":[],"candidate_id":"cand_e012bb29567d90504612","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000330"],"scope":"focus_ayah","source_local_id":"100:10:2:passive-exposed-subject","source_type":"word_analysis","support_ids":["sup_0604e955a8dcd0bd9498","sup_90583f0978f02d3b7d5b"],"title":"passive verb foregrounds exposed contents","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:2","qac_refs":["100:10:1:2"],"status":"accepted"}},{"anchor_refs":["100:10:2"],"branch_refs":[],"candidate_id":"cand_b1a2d6dce98de75ff6e4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000330"],"scope":"focus_ayah","source_local_id":"100:10:2:sifting-extraction-range","source_type":"word_analysis","support_ids":["sup_90583f0978f02d3b7d5b","sup_c725774c99be13e6459a"],"title":"root range makes disclosure a sifting extraction","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:2","qac_refs":["100:10:1:2"],"status":"accepted"}},{"anchor_refs":["100:10:2"],"branch_refs":[],"candidate_id":"cand_48b54db2009282bc4ccc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000330"],"scope":"focus_ayah","source_local_id":"100:10:2:variant-form-contrast","source_type":"word_analysis","support_ids":["sup_267f0a15ee767dfccd6c","sup_90583f0978f02d3b7d5b"],"title":"selected passive Form II blocks self-emergence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:2","qac_refs":["100:10:1:2"],"status":"accepted"}},{"anchor_refs":["100:10:3"],"branch_refs":[],"candidate_id":"cand_f311f9f8fe2a05b65752","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:10:3:relative-passive-subject","source_type":"word_analysis","support_ids":["sup_7ca9dd05eaeb4fd017c0","sup_8fc0f41236baab2d6329"],"title":"relative pronoun becomes the passive subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:3","qac_refs":["100:10:2:1"],"status":"accepted"}},{"anchor_refs":["100:10:3"],"branch_refs":[],"candidate_id":"cand_f102a75ea272d11bac27","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:10:3:template-echo-delay","source_type":"word_analysis","support_ids":["sup_00c470d06a56b0d5693a","sup_7ca9dd05eaeb4fd017c0"],"title":"open subject repeats the container template","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:3","qac_refs":["100:10:2:1"],"status":"accepted"}},{"anchor_refs":["100:10:3"],"branch_refs":[],"candidate_id":"cand_693aca09340effbaa979","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:10:3:unspecified-interior-scope","source_type":"word_analysis","support_ids":["sup_6b41fd8557df7d0986d9","sup_7ca9dd05eaeb4fd017c0"],"title":"open scope refuses to itemize the contents","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:3","qac_refs":["100:10:2:1"],"status":"accepted"}},{"anchor_refs":["100:10:4"],"branch_refs":[],"candidate_id":"cand_be75a147e15bc977790b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:10:4:delayed-audible-completion","source_type":"word_analysis","support_ids":["sup_57cb77a7e572180ba32a","sup_647b6a0cdc07dfba0a79"],"title":"postposed phrase completes the subject at the end","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:4","qac_refs":["100:10:3:1"],"status":"accepted"}},{"anchor_refs":["100:10:4"],"branch_refs":[],"candidate_id":"cand_46e379e20260f74defe6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:10:4:interior-containment","source_type":"word_analysis","support_ids":["sup_647b6a0cdc07dfba0a79","sup_a38d6f95561e842203e9"],"title":"preposition makes inside-ness unavoidable","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:4","qac_refs":["100:10:3:1"],"status":"accepted"}},{"anchor_refs":["100:10:4"],"branch_refs":[],"candidate_id":"cand_4744a80a71577529e7fd","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"100:10:4:repeated-container-marker","source_type":"word_analysis","support_ids":["sup_647b6a0cdc07dfba0a79","sup_b3830c29a86b4c2ad8d6"],"title":"same marker transfers the container frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:4","qac_refs":["100:10:3:1"],"status":"accepted"}},{"anchor_refs":["100:10:5"],"branch_refs":[],"candidate_id":"cand_1d68e0439d3e3ddb0322","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"100:10:5:assimilated-definite-sound","source_type":"word_analysis","support_ids":["sup_13bf97d0ff5495e7e8df","sup_808805d8e06666b9917f"],"title":"assimilated article tightens the final noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:5","qac_refs":["100:10:4:1","100:10:4:2"],"status":"accepted"}},{"anchor_refs":["100:10:5"],"branch_refs":[],"candidate_id":"cand_a8aac40af66083d7a5a0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"100:10:5:definite-broken-plural","source_type":"word_analysis","support_ids":["sup_808805d8e06666b9917f","sup_aeabb2fb6d2fd7f4acd1"],"title":"definite plural makes many chests a generic class","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:5","qac_refs":["100:10:4:1","100:10:4:2"],"status":"accepted"}},{"anchor_refs":["100:10:5"],"branch_refs":[],"candidate_id":"cand_ee2a4fb18ec9f0fb3a5f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"100:10:5:familiar-word-marked-context","source_type":"word_analysis","support_ids":["sup_808805d8e06666b9917f","sup_ecb868e12c81d0a56ca5"],"title":"familiar chest vocabulary is intensified by context","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:5","qac_refs":["100:10:4:1","100:10:4:2"],"status":"accepted"}},{"anchor_refs":["100:10:5"],"branch_refs":[],"candidate_id":"cand_5656728362a832766350","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"100:10:5:final-clause-landing","source_type":"word_analysis","support_ids":["sup_34bf758fd3ef4f41405e","sup_808805d8e06666b9917f"],"title":"final noun lands the disclosure inside","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:5","qac_refs":["100:10:4:1","100:10:4:2"],"status":"accepted"}},{"anchor_refs":["100:10:5"],"branch_refs":[],"candidate_id":"cand_0e16344a704c59f5e1d7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"100:10:5:front-interior-emergence","source_type":"word_analysis","support_ids":["sup_4122ec8475fd14a2a307","sup_808805d8e06666b9917f"],"title":"chest sense keeps frontness and emergence pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:5","qac_refs":["100:10:4:1","100:10:4:2"],"status":"accepted"}},{"anchor_refs":["100:10:5"],"branch_refs":[],"candidate_id":"cand_1ab58a0dff0ff417172e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"100:10:5:governed-container","source_type":"word_analysis","support_ids":["sup_808805d8e06666b9917f","sup_bd7a901d964cc83aac8c"],"title":"genitive noun is the container, not the extracted subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:5","qac_refs":["100:10:4:1","100:10:4:2"],"status":"accepted"}},{"anchor_refs":["100:10:5"],"branch_refs":[],"candidate_id":"cand_8edfadf410cea9dc4815","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"100:10:5:grave-chest-rhyme-bridge","source_type":"word_analysis","support_ids":["sup_808805d8e06666b9917f","sup_999e2fa54c9b3082ab6c"],"title":"rhyme-paired containers shift disclosure inward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:5","qac_refs":["100:10:4:1","100:10:4:2"],"status":"accepted"}},{"anchor_refs":["100:10:5"],"branch_refs":[],"candidate_id":"cand_4f17f1c98e9769461fc7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"100:10:5:next-ayah-knowledge","source_type":"word_analysis","support_ids":["sup_808805d8e06666b9917f","sup_f6fa78254b6d0c6444fa"],"title":"exposed interiors feed the next knowledge seal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"100:10:5","qac_refs":["100:10:4:1","100:10:4:2"],"status":"accepted"}},{"anchor_refs":["100:10:1"],"branch_refs":[],"candidate_id":"cand_e90de4763fc671b2c775","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000330"],"scope":"focus_ayah","source_local_id":"100:10:1:2","source_type":"qac_morpheme","support_ids":["sup_c2cf49350bd4eae628c5"],"title":"QAC root occurrence: ح ص ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["100:10:4"],"branch_refs":[],"candidate_id":"cand_aedfe3d3849ce679d455","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"100:10:4:2","source_type":"qac_morpheme","support_ids":["sup_58892b0a6d6eaeab4ec4"],"title":"QAC root occurrence: ص د ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["100:10"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:10","branch_refs":["root_000330/B001","root_000849/B004"],"candidate_id":"cand_b377a37b3388bccc95af","commentary_obligation":"review","hft_ref":"hft_d730d7f9e0d4e822a1dc","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_resultant_gist","source_type":"hft","support_ids":["sup_4b7ed36557097abb3cb9"],"title":"base_resultant_gist","trust":"legacy_unbound"},{"anchor_refs":["100:10"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:10","branch_refs":["root_000330/B002","root_000849/B001"],"candidate_id":"cand_0692fa16c3cce4eebb69","commentary_obligation":"review","hft_ref":"hft_aae5ae66f41f1fb1f29a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_inner_assay","source_type":"hft","support_ids":["sup_2504d2d4e2312d87eca6"],"title":"base_inner_assay","trust":"legacy_unbound"},{"anchor_refs":["100:10"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:10","branch_refs":["root_000330/B003","root_000849/B003","root_000849/B004"],"candidate_id":"cand_281295ca6ef4618d9e6d","commentary_obligation":"review","hft_ref":"hft_62e600907ce342a7cf4e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_residual_source","source_type":"hft","support_ids":["sup_2d341673516eb2c2409a"],"title":"base_residual_source","trust":"legacy_unbound"},{"anchor_refs":["100:10"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"100:10","branch_refs":["root_000330/B001","root_000849/B002"],"candidate_id":"cand_a03e4f778b8ef036281f","commentary_obligation":"review","hft_ref":"hft_8bce19b7879b4b98b551","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_inside_to_fore","source_type":"hft","support_ids":["sup_674f18cecc7526b82ee0"],"title":"base_inside_to_fore","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَحُصِّلَ مَا فِى ٱلصُّدُورِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"100:10:1:1","qac_word_ref":"100:10:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"حُصِّلَ","morph_features":"STEM|POS:V|PERF|PASS|(II)|LEM:HuS~ila|ROOT:HSl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"100:10:1:2","qac_word_ref":"100:10:1","root_ar":"ح ص ل","surface_ar":"حُصِّلَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:REL|LEM:maA","morpheme_role":"STEM","pos":"REL","qac_ref":"100:10:2:1","qac_word_ref":"100:10:2","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"100:10:3:1","qac_word_ref":"100:10:3","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"100:10:4:1","qac_word_ref":"100:10:4","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:10:4:2","qac_word_ref":"100:10:4","root_ar":"ص د ر","surface_ar":"صُّدُورِ"}],"word_analysis_qac_refs":[["100:10:1:1"],["100:10:1:2"],["100:10:2:1"],["100:10:3:1"],["100:10:4:1","100:10:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["100:10:1","100:10:2","100:10:3","100:10:4","100:10:5"]},"focus_surface_evidence":{"arabic_uthmani":"وَحُصِّلَ مَا فِى ٱلصُّدُورِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"100:10:1:1","qac_word_ref":"100:10:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"حُصِّلَ","morph_features":"STEM|POS:V|PERF|PASS|(II)|LEM:HuS~ila|ROOT:HSl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"100:10:1:2","qac_word_ref":"100:10:1","root_ar":"ح ص ل","surface_ar":"حُصِّلَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:REL|LEM:maA","morpheme_role":"STEM","pos":"REL","qac_ref":"100:10:2:1","qac_word_ref":"100:10:2","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"100:10:3:1","qac_word_ref":"100:10:3","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"100:10:4:1","qac_word_ref":"100:10:4","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"100:10:4:2","qac_word_ref":"100:10:4","root_ar":"ص د ر","surface_ar":"صُّدُورِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["100:10:1:1"],["100:10:1:2"],["100:10:2:1"],["100:10:3:1"],["100:10:4:1","100:10:4:2"]],"word_analysis_refs":["100:10:1","100:10:2","100:10:3","100:10:4","100:10:5"],"word_rows":[{"analysis_record_ref":"100:10:1","analytic_gloss_range_en":"opening conjunction that coordinates the second disclosure with the prior grave-disclosure frame","analytic_root_gloss_range_en":null,"qac_refs":["100:10:1:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"100:10:2","analytic_gloss_range_en":"passive Form II extraction, collection, and discriminating disclosure of hidden contents","analytic_root_gloss_range_en":"root range includes collecting until an outcome is clear, extracting inner value from covering, and residue after separation; local grammar selects thorough passive extraction and disclosure, not animal, date-fruit, or unrelated reviewed branches","qac_refs":["100:10:1:2"],"root":{"arabic":"ح ص ل","transliteration":"ḥ-ṣ-l"},"surface":{"arabic":"حُصِّلَ","transliteration":"ḥuṣṣila"}},{"analysis_record_ref":"100:10:3","analytic_gloss_range_en":"headless relative pronoun meaning whatever or that which, functioning as the passive subject and leaving the interior contents unspecified","analytic_root_gloss_range_en":null,"qac_refs":["100:10:2:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"مَا","transliteration":"mā"}},{"analysis_record_ref":"100:10:4","analytic_gloss_range_en":"preposition of interior containment, governing the chest noun and making the extracted contents located within","analytic_root_gloss_range_en":null,"qac_refs":["100:10:3:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"فِى","transliteration":"fī"}},{"analysis_record_ref":"100:10:5","analytic_gloss_range_en":"definite broken plural chest-container, locally the generic human interior domain whose contents are extracted","analytic_root_gloss_range_en":"root range includes bodily chest or front, foremost part, issuing or departure, source, liability, and portion; local grammar selects the chest/interior container while allowing front and emergence imagery as narrowed pressure","qac_refs":["100:10:4:1","100:10:4:2"],"root":{"arabic":"ص د ر","transliteration":"ṣ-d-r"},"surface":{"arabic":"ٱلصُّدُورِ","transliteration":"aṣ-ṣudūri"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["100:10"],"branch_refs":["root_000330/B001","root_000849/B004"],"candidate_id":"cand_b377a37b3388bccc95af","evidence_scope":"focus_ayah","hft_ref":"hft_d730d7f9e0d4e822a1dc","item_id":"base_resultant_gist","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_resultant_gist","support_id":"sup_4b7ed36557097abb3cb9"},{"anchor_refs":["100:10"],"branch_refs":["root_000330/B002","root_000849/B001"],"candidate_id":"cand_0692fa16c3cce4eebb69","evidence_scope":"focus_ayah","hft_ref":"hft_aae5ae66f41f1fb1f29a","item_id":"base_inner_assay","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_inner_assay","support_id":"sup_2504d2d4e2312d87eca6"},{"anchor_refs":["100:10"],"branch_refs":["root_000330/B003","root_000849/B003","root_000849/B004"],"candidate_id":"cand_281295ca6ef4618d9e6d","evidence_scope":"focus_ayah","hft_ref":"hft_62e600907ce342a7cf4e","item_id":"base_residual_source","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_residual_source","support_id":"sup_2d341673516eb2c2409a"},{"anchor_refs":["100:10"],"branch_refs":["root_000330/B001","root_000849/B002"],"candidate_id":"cand_a03e4f778b8ef036281f","evidence_scope":"focus_ayah","hft_ref":"hft_8bce19b7879b4b98b551","item_id":"base_inside_to_fore","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_inside_to_fore","support_id":"sup_674f18cecc7526b82ee0"}],"diagnostics":[{"warning":"Unrecognized HFT reader field is preserved as a global review record"},{"warning":"Unrecognized HFT reader field is preserved as a global review record"}],"lane_counts":{"global":13,"macro":11,"micro":4},"packet_summary":{"ayah_count":11,"focus_ref":"100:10","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ع د و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000993","furuq_root_norm":"ع د و","furuq_source_root_norm":"ع د و","is_dominant":true,"target_occurrences":68,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":5,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":false,"target_occurrences":4,"target_rank":3}]},{"qac_root":"ث و ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000210","furuq_root_norm":"ث و ر","furuq_source_root_norm":"ث و ر","is_dominant":true,"target_occurrences":4,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000011","furuq_root_norm":"ء ث ر","furuq_source_root_norm":"أ ث ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["100:1","100:2","100:3","100:4","100:5","100:6","100:7","100:8","100:9","100:10","100:11"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"100:10","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v3","reader_id":"reader_hft_a","trace_kind":null}]},"reader_synthesis_count":11,"source_present":true,"structured_insight_count":15,"unstructured_record_count":2},"identity":{"ayah_ref":"100:10","lane":"micro","linguistic_source_ref":"100:10","surface_ref":"100:10","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"100:10","target_tokens":[["Ve",["100:10:1"]],["göğüslerde",["100:10:3","100:10:4"]],["olanlar",["100:10:2"]],["ortaya",["100:10:1"]],["çıkarıldığında",["100:10:1"]]],"text":"Ve göğüslerde olanlar ortaya çıkarıldığında,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":11,"id":"s100-p01-001-011","label":"Whole surah","number":1,"refs":["100:1","100:2","100:3","100:4","100:5","100:6","100:7","100:8","100:9","100:10","100:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:3:template-echo-delay","source_type":"word_analysis","support_id":"sup_00c470d06a56b0d5693a","text":"{\"blocking_evidence\":null,\"headline\":\"open subject repeats the container template\",\"reader_payoff\":\"The reader notices the phrase moving from extraction to unspecified contents to container, while also echoing the what-is-in pattern from 100:9.\",\"reason\":\"The local word order and the repeated {{ar:مَا فِى}} ({{tr:mā fī}}) frame support both the delayed reveal and the boundary echo.\",\"representative_source_ids\":[\"QT-c5eac93a\",\"QT-e113be54\",\"QE-fa5cf71a\",\"QB-84520bac\",\"QY-c1e4fd8a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:2:passive-exposed-subject","source_type":"word_analysis","support_id":"sup_0604e955a8dcd0bd9498","text":"{\"blocking_evidence\":null,\"headline\":\"passive verb foregrounds exposed contents\",\"reader_payoff\":\"The reader notices that the clause hides the extracting agent and makes the interior contents bear the event on the surface.\",\"reason\":\"QAC identifies a passive perfect Form II verb, and attachment evidence marks the agent as suppressed while the following relative phrase functions as passive subject.\",\"representative_source_ids\":[\"QG-068e4027\",\"QG-6e7fd911\",\"QG-831092ea\",\"QT-11b57fa5\",\"QT-af3b312e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:5:assimilated-definite-sound","source_type":"word_analysis","support_id":"sup_13bf97d0ff5495e7e8df","text":"{\"blocking_evidence\":null,\"headline\":\"assimilated article tightens the final noun\",\"reader_payoff\":\"The reader notices that definiteness is not only grammatical; the assimilated article is heard as a tightened onset at the ayah's close.\",\"reason\":\"The written article and sun-letter assimilation are local surface features of {{ar:ٱلصُّدُورِ}} ({{tr:aṣ-ṣudūri}}).\",\"representative_source_ids\":[\"QF-371f6133\",\"QP-849f740a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:1:fused-verbal-onset","source_type":"word_analysis","support_id":"sup_22d743ed453996a4428b","text":"{\"blocking_evidence\":null,\"headline\":\"proclitic onset fuses link and action\",\"reader_payoff\":\"The reader notices that the connector is not a detached pause-marker; it is attached to the extraction verb, so linkage and action arrive in one surface beat.\",\"reason\":\"The local surface places {{ar:وَ}} ({{tr:wa}}) directly on {{ar:حُصِّلَ}} ({{tr:ḥuṣṣila}}), supporting the fused-onset observation.\",\"representative_source_ids\":[\"QF-5c5b4289\",\"QP-19fd2503\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:2:variant-form-contrast","source_type":"word_analysis","support_id":"sup_267f0a15ee767dfccd6c","text":"{\"blocking_evidence\":null,\"headline\":\"selected passive Form II blocks self-emergence\",\"reader_payoff\":\"The reader notices that the selected form keeps imposed thorough extraction while avoiding both self-emergence and an explicitly named active extractor.\",\"reason\":\"The variant contrasts are useful as apparatus, but Hafs {{ar:حُصِّلَ}} ({{tr:ḥuṣṣila}}) governs the local parse as passive Form II.\",\"representative_source_ids\":[\"QF-1ecfd1da\",\"QF-9d93d23b\",\"QF-9e5403ed\",\"QF-a117fe83\",\"QF-e7620fd0\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:5:final-clause-landing","source_type":"word_analysis","support_id":"sup_34bf758fd3ef4f41405e","text":"{\"blocking_evidence\":null,\"headline\":\"final noun lands the disclosure inside\",\"reader_payoff\":\"The reader notices the clause narrowing from extraction, to unspecified contents, to the intimate container that closes the ayah.\",\"reason\":\"The word is final in the ayah and completes the postposed prepositional phrase, supporting both syntactic landing and sonic prominence.\",\"representative_source_ids\":[\"QT-447c5391\",\"QT-f5f5fa82\",\"QT-fd555bf3\",\"QP-90431e0a\",\"QP-9cb7e40c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:5:front-interior-emergence","source_type":"word_analysis","support_id":"sup_4122ec8475fd14a2a307","text":"{\"blocking_evidence\":null,\"headline\":\"chest sense keeps frontness and emergence pressure\",\"reader_payoff\":\"The reader notices that the chosen container is not an abstract inwardness only: it is the front-facing chest whose concealed interior is forced outward.\",\"reason\":\"V4 supports bodily chest/front and issuing-related branches for {{ar:ص د ر}} ({{tr:ṣ-d-r}}), but the local noun phrase selects the chest-container sense; frontness and emergence remain as narrowed imagery rather than replacing the local sense.\",\"representative_source_ids\":[\"QS-1d8c112c\",\"QS-6ce68f3a\",\"QS-b4924c49\",\"QS-ebed363a\",\"MS-db9348f2\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:4:delayed-audible-completion","source_type":"word_analysis","support_id":"sup_57cb77a7e572180ba32a","text":"{\"blocking_evidence\":null,\"headline\":\"postposed phrase completes the subject at the end\",\"reader_payoff\":\"The reader notices the phrase delaying the named container until the end, with the preposition and chest word heard as one dependent unit.\",\"reason\":\"The local order places the prepositional phrase after the relative head, and the recitation claim is consistent with the bound preposition-complement dependency.\",\"representative_source_ids\":[\"QT-ff3aab30\",\"QP-97b5498a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"100:10:4:2","source_type":"qac_morpheme","support_id":"sup_58892b0a6d6eaeab4ec4","text":"{\"lemma_ar\":\"صَدْر\",\"morph_features\":\"STEM|POS:N|LEM:Sador|ROOT:Sdr|MP|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"100:10:4:2\",\"qac_word_ref\":\"100:10:4\",\"root_ar\":\"ص د ر\",\"surface_ar\":\"صُّدُورِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:4","source_type":"word_analysis","support_id":"sup_647b6a0cdc07dfba0a79","text":"{\"gloss_range\":\"preposition of interior containment, governing the chest noun and making the extracted contents located within\",\"prose\":\"{{ar:فِى}} ({{tr:fī}}) makes interiority grammatical. It governs {{ar:ٱلصُّدُورِ}} ({{tr:aṣ-ṣudūri}}) and locates {{ar:مَا}} ({{tr:mā}}) within the chests, so the extraction reverses a real inside-outside relation rather than merely describing a topic about hearts or thoughts. The preposition carries both spatial containment and the conventional metaphor of hidden inner states: the contents are imagined as enclosed material and then brought out. It also repeats the same container marker from 100:9, preserving the what-is-in frame while shifting the container from graves to chests. Because the prepositional phrase comes after {{ar:مَا}} ({{tr:mā}}), the subject is completed only at the end; in recitation, the flow into {{ar:ٱلصُّدُورِ}} ({{tr:aṣ-ṣudūri}}) audibly fuses the marker with its container.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فِى}} ({{tr:fī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:2:compressed-sound","source_type":"word_analysis","support_id":"sup_6534486c9183e854ff71","text":"{\"blocking_evidence\":null,\"headline\":\"tight sound mirrors compressed processing\",\"reader_payoff\":\"The reader notices the compact, geminated verb opening into the longer chest phrase, so the sound shape reinforces concentrated extraction before expansion.\",\"reason\":\"The surface form contains the Form II gemination and precedes the longer relative-prepositional phrase, supporting the pacing observation.\",\"representative_source_ids\":[\"QP-1a537d3f\",\"QP-e35d328a\",\"QP-fb3bec22\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:3:unspecified-interior-scope","source_type":"word_analysis","support_id":"sup_6b41fd8557df7d0986d9","text":"{\"blocking_evidence\":null,\"headline\":\"open scope refuses to itemize the contents\",\"reader_payoff\":\"The reader notices that the ayah deliberately leaves the chest-contents unlisted, so every relevant inner content remains within the extraction.\",\"reason\":\"The headless relative construction avoids adding an explanatory noun, and the attachment guidance warns against narrowing the deliberately unspecified contents.\",\"representative_source_ids\":[\"QG-5b5b8f0c\",\"QG-ba417af1\",\"QS-27c0c5aa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:3","source_type":"word_analysis","support_id":"sup_7ca9dd05eaeb4fd017c0","text":"{\"gloss_range\":\"headless relative pronoun meaning whatever or that which, functioning as the passive subject and leaving the interior contents unspecified\",\"prose\":\"{{ar:مَا}} ({{tr:mā}}) is the headless relative subject of the passive verb, not a negation or a question here. It lets the extracted material stand on the surface while refusing to list its classes: intentions, secrets, beliefs, and other inner contents remain included without being individually named. The following {{ar:فِى ٱلصُّدُورِ}} ({{tr:fī aṣ-ṣudūri}}) completes the phrase, so the reader first hears extraction, then an open whatever, and only at the end the hidden container. The same {{ar:مَا فِى}} ({{tr:mā fī}}) template echoes the grave phrase in 100:9, making the new subject parallel to what was in the graves before the container changes from exterior burial-place to interior chest.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مَا}} ({{tr:mā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:5","source_type":"word_analysis","support_id":"sup_808805d8e06666b9917f","text":"{\"gloss_range\":\"definite broken plural chest-container, locally the generic human interior domain whose contents are extracted\",\"prose\":\"{{ar:ٱلصُّدُورِ}} ({{tr:aṣ-ṣudūri}}) is the governed genitive complement of {{ar:فِى}} ({{tr:fī}}), so the chests are the container, not the extracted subject itself. The definite broken plural makes that container both multiple and generic: not one person's interior, but the class of human chests as distributed hidden storehouses. The word is familiar Quranic interior vocabulary, so the marked force here comes from coupling that familiar container with the specialized extraction verb. The local sense is the chest as bodily and psychological interior, while the wider {{ar:ص د ر}} ({{tr:ṣ-d-r}}) field of frontness and issuing-forth adds a narrowed pressure: the outward-facing chest becomes the named place whose concealed contents are forced into emergence. As the ayah's final word, it gives the clause its landing after extraction and unspecified contents. Its definiteness is also heard: the article assimilates into the sun letter, tightening the onset so definiteness and sonic pressure arrive together at the close. Across 100:9-10, its cadence answers the grave-container in 100:9, so the sound-pair carries a semantic shift from public grave concealment to private interior concealment. The exposed interiors also prepare 100:11, where the next ayah seals the sequence with complete awareness.\",\"root_display\":\"{{ar:ص د ر}} ({{tr:ṣ-d-r}})\",\"root_gloss_range\":\"root range includes bodily chest or front, foremost part, issuing or departure, source, liability, and portion; local grammar selects the chest/interior container while allowing front and emergence imagery as narrowed pressure\",\"surface_display\":\"{{ar:ٱلصُّدُورِ}} ({{tr:aṣ-ṣudūri}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:1","source_type":"word_analysis","support_id":"sup_86299cf6efc53ad5e108","text":"{\"gloss_range\":\"opening conjunction that coordinates the second disclosure with the prior grave-disclosure frame\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) opens 100:10 as continuation before the new event is named. It coordinates {{ar:حُصِّلَ}} ({{tr:ḥuṣṣila}}) with the prior passive disclosure in 100:9, so the chest-extraction remains inside the same when-frame rather than starting a detached report. Its range can allow addition, sequence, and explanatory deepening, but the local evidence narrows that range to a compatible hinge: the ayah moves from exterior disclosure to interior disclosure without making the particle alone prove a single timing. Because the conjunction is proclitic on the verb, the transition is also heard as fused onset. Across the boundary, it helps the ear carry the paired container cadence from the grave-container in 100:9 to {{ar:ٱلصُّدُورِ}} ({{tr:aṣ-ṣudūri}}) here.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:3:relative-passive-subject","source_type":"word_analysis","support_id":"sup_8fc0f41236baab2d6329","text":"{\"blocking_evidence\":null,\"headline\":\"relative pronoun becomes the passive subject\",\"reader_payoff\":\"The reader notices that the word means the extracted whatever, not a negation or question, and that it carries the passive event as subject.\",\"reason\":\"QAC and attachment evidence identify {{ar:مَا}} ({{tr:mā}}) as a relative pronoun and passive subject completed by the following prepositional phrase.\",\"representative_source_ids\":[\"QG-13a5624d\",\"QS-6c24902c\",\"QF-8926a4e8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:2","source_type":"word_analysis","support_id":"sup_90583f0978f02d3b7d5b","text":"{\"gloss_range\":\"passive Form II extraction, collection, and discriminating disclosure of hidden contents\",\"prose\":\"{{ar:حُصِّلَ}} ({{tr:ḥuṣṣila}}) is a perfect passive Form II verb, so the ayah presents the extraction as already accomplished while withholding the extractor from the surface grammar. That passive shape turns {{ar:مَا فِى ٱلصُّدُورِ}} ({{tr:mā fī aṣ-ṣudūri}}) into the clause's exposed subject, not an object controlled by a named actor. The root field gives the act more than bare uncovering: it gathers, separates, and draws out what remains as the significant inner material, like a winnowing or assaying process in which essence is separated from covering. That sifting payoff survives locally, while the dictionary's animal, date-fruit, and other marginal branches remain outside the ayah's sense. The Hafs passive Form II also matters against variant possibilities: the contents neither simply emerge by themselves nor does an explicit active extractor take over the line; the event is imposed, thorough, and centered on what is exposed. Its compact sound also participates in the payoff: the geminated ṣād tightens the verb before it opens into the longer chest-content phrase, so the heard form matches compressed processing and release. In the ayah sequence, {{ar:حُصِّلَ}} ({{tr:ḥuṣṣila}}) answers the prior passive disclosure in 100:9 and prepares the next ayah's knowledge claim in 100:11, so exterior scattering gives way to interior discrimination.\",\"root_display\":\"{{ar:ح ص ل}} ({{tr:ḥ-ṣ-l}})\",\"root_gloss_range\":\"root range includes collecting until an outcome is clear, extracting inner value from covering, and residue after separation; local grammar selects thorough passive extraction and disclosure, not animal, date-fruit, or unrelated reviewed branches\",\"surface_display\":\"{{ar:حُصِّلَ}} ({{tr:ḥuṣṣila}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:2:hapax-specialized-choice","source_type":"word_analysis","support_id":"sup_929faa708b7b30610b82","text":"{\"blocking_evidence\":null,\"headline\":\"single Quranic root occurrence marks the verb\",\"reader_payoff\":\"The reader notices that this specialized extraction vocabulary carries its Quranic burden here rather than functioning as a routine disclosure verb.\",\"reason\":\"The contextual profile lists the exact root-form as a single occurrence, supporting markedness without using rarity to invent a separate local sense.\",\"representative_source_ids\":[\"QI-ff2e214f\",\"QH-d1ba1154\",\"MH-25deab85\",\"QY-4b98441a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:5:grave-chest-rhyme-bridge","source_type":"word_analysis","support_id":"sup_999e2fa54c9b3082ab6c","text":"{\"blocking_evidence\":null,\"headline\":\"rhyme-paired containers shift disclosure inward\",\"reader_payoff\":\"The reader notices that the matching cadence across 100:9-10 carries a real semantic shift: grave contents disclosed outward, then chest contents disclosed inward.\",\"reason\":\"The rows give the concrete 100:9 to 100:10 container pairing, and the local final noun provides the inward counterpart to the prior grave-container.\",\"representative_source_ids\":[\"QT-a9dcd17b\",\"QE-939030e2\",\"QE-ad0cfc11\",\"QP-1a82f8b6\",\"QY-a5d0c473\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:4:interior-containment","source_type":"word_analysis","support_id":"sup_a38d6f95561e842203e9","text":"{\"blocking_evidence\":null,\"headline\":\"preposition makes inside-ness unavoidable\",\"reader_payoff\":\"The reader notices that the hidden material is not merely associated with chests; it is grammatically placed inside them before being extracted.\",\"reason\":\"QAC and attachment evidence make {{ar:فِى}} ({{tr:fī}}) a preposition governing the genitive chest noun, supporting literal containment and the local interior metaphor.\",\"representative_source_ids\":[\"QG-1f86aa57\",\"MG-4766c310\",\"QS-f6956943\",\"QF-4cab85d8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:5:definite-broken-plural","source_type":"word_analysis","support_id":"sup_aeabb2fb6d2fd7f4acd1","text":"{\"blocking_evidence\":null,\"headline\":\"definite plural makes many chests a generic class\",\"reader_payoff\":\"The reader notices that the ayah treats inner containers as many individual chests while extending the exposure to the class as a whole.\",\"reason\":\"QAC marks the word as a definite broken plural governed by {{ar:فِى}} ({{tr:fī}}), supporting distributed plurality with generic reference.\",\"representative_source_ids\":[\"QG-cd0f21a5\",\"QF-3d82afe1\",\"QF-c76998fa\",\"QF-e2c594d6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:4:repeated-container-marker","source_type":"word_analysis","support_id":"sup_b3830c29a86b4c2ad8d6","text":"{\"blocking_evidence\":null,\"headline\":\"same marker transfers the container frame\",\"reader_payoff\":\"The reader notices that the relation of containment stays the same across 100:9-10 while the container changes from grave to chest.\",\"reason\":\"The repeated {{ar:فِى}} ({{tr:fī}}) in the container template supports the cross-boundary bridge without changing the local government relation.\",\"representative_source_ids\":[\"QT-9d38f777\",\"QE-26c325f8\",\"QB-04a90620\",\"QY-350b4ccc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:5:governed-container","source_type":"word_analysis","support_id":"sup_bd7a901d964cc83aac8c","text":"{\"blocking_evidence\":null,\"headline\":\"genitive noun is the container, not the extracted subject\",\"reader_payoff\":\"The reader notices that the chests house the extractable material; they are the interior domain from which the passive subject is drawn.\",\"reason\":\"The preposition governs the noun as a genitive complement, and the relative phrase makes the contents the passive subject.\",\"representative_source_ids\":[\"QG-29828f5e\",\"QG-96dcadcd\",\"QS-53a8a3a5\",\"QS-482f74fb\",\"QS-61973c7f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"100:10:1:2","source_type":"qac_morpheme","support_id":"sup_c2cf49350bd4eae628c5","text":"{\"lemma_ar\":\"حُصِّلَ\",\"morph_features\":\"STEM|POS:V|PERF|PASS|(II)|LEM:HuS~ila|ROOT:HSl|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"100:10:1:2\",\"qac_word_ref\":\"100:10:1\",\"root_ar\":\"ح ص ل\",\"surface_ar\":\"حُصِّلَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:2:sifting-extraction-range","source_type":"word_analysis","support_id":"sup_c725774c99be13e6459a","text":"{\"blocking_evidence\":null,\"headline\":\"root range makes disclosure a sifting extraction\",\"reader_payoff\":\"The reader notices that the hidden contents are not merely shown; they are gathered, separated, and made to yield their significant remainder.\",\"reason\":\"V4 supports collection, extraction of inner value, and residue-after-separation branches for {{ar:ح ص ل}} ({{tr:ḥ-ṣ-l}}); local passive Form II and the chest-content subject narrow that range to discriminating extraction, excluding unrelated reviewed or concrete branches.\",\"representative_source_ids\":[\"QS-2ec72fa6\",\"QS-47589885\",\"QS-4a3f7480\",\"QS-5f34f39d\",\"QS-65cf91f0\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:1:container-rhyme-bridge","source_type":"word_analysis","support_id":"sup_c9732b61b7fc2f6b1809","text":"{\"blocking_evidence\":null,\"headline\":\"hinge carries the grave-chest pairing\",\"reader_payoff\":\"The reader notices that the tiny connector helps bind two containers across 100:9-10: graves for exterior concealment and chests for interior concealment.\",\"reason\":\"The repeated container formula and the 100:9 to 100:10 boundary support the particle's role as a bridge between exterior and interior disclosure.\",\"representative_source_ids\":[\"QE-bdb56b06\",\"QP-52e0462c\",\"MP-04f07007\",\"QY-80e1ccf6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:1:paired-disclosure-hinge","source_type":"word_analysis","support_id":"sup_d5134f3f1ce213256db6","text":"{\"blocking_evidence\":null,\"headline\":\"connector keeps the second disclosure in the same frame\",\"reader_payoff\":\"The reader notices that the ayah does not restart the scene; the opening connector carries the chest-extraction as a second disclosure inside the prior timing frame.\",\"reason\":\"QAC and attachment evidence identify the word as a coordinating conjunction linked to 100:9; the broad additive, sequential, and explanatory claims are kept but narrowed because {{ar:وَ}} ({{tr:wa}}) does not by itself force only one of those relations.\",\"representative_source_ids\":[\"QG-ba7b700f\",\"QG-cf26b963\",\"QS-68dff68c\",\"QT-6786bced\",\"QB-c26c1179\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:2:boundary-knowledge-sequence","source_type":"word_analysis","support_id":"sup_e11a2128b99143c4e1e3","text":"{\"blocking_evidence\":null,\"headline\":\"interior extraction answers the boundary movement\",\"reader_payoff\":\"The reader notices the sequence moving from a question about knowing in 100:9, to completed extraction in 100:10, to full awareness in 100:11.\",\"reason\":\"The boundary rows tie this passive verb to the prior question and to the following knowledge predicate; those references are retained as sequence relations rather than independent lexical senses.\",\"representative_source_ids\":[\"QG-a970f3f6\",\"QI-704f6c99\",\"QI-acaec58d\",\"QT-8027a0b7\",\"QE-1b2f471e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:5:familiar-word-marked-context","source_type":"word_analysis","support_id":"sup_ecb868e12c81d0a56ca5","text":"{\"blocking_evidence\":null,\"headline\":\"familiar chest vocabulary is intensified by context\",\"reader_payoff\":\"The reader notices that the noun itself is familiar Quranic interior vocabulary; the marked force comes from its pairing with the specialized extraction verb.\",\"reason\":\"The contextual profile lists the noun as a common exact-root form, so the row is retained as a distributional qualifier rather than a rarity claim.\",\"representative_source_ids\":[\"QI-850e8a41\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"100:10:5:next-ayah-knowledge","source_type":"word_analysis","support_id":"sup_f6fa78254b6d0c6444fa","text":"{\"blocking_evidence\":null,\"headline\":\"exposed interiors feed the next knowledge seal\",\"reader_payoff\":\"The reader notices that the exposed chest-contents become the material for the complete awareness asserted in 100:11.\",\"reason\":\"The current ayah names the interior container and the following ayah supplies the knowledge predicate, so the forward relation is contextually licensed.\",\"representative_source_ids\":[\"QE-6d4f5080\",\"QB-d7e3f3bc\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَحُصِّلَ مَا فِى ٱلصُّدُورِ","ayah_ref":"100:10"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000330/B001","root_000849/B004"],"payload":{"activation_trace":[{"assigned_role":"Supplies the consolidating operation and the notion of an accountable gist.","branch_id":"B001","branch_image_ar":"جمع الشيء حتى يظهر حاصله","literal_contribution":"Collection or resolution continues until a resultant is clear.","mapped_root_id":"root_000330","root":"ح ص ل","source_phrase_ar":"حُصِّلَ","source_ref":"100:10"},{"assigned_role":"Makes the breasts generative sources, not merely sealed containers.","branch_id":"B004","branch_image_ar":"الأصل الذي تصدر عنه الأفعال","literal_contribution":"An origin is the place from which actions issue.","mapped_root_id":"root_000849","root":"ص د ر","source_phrase_ar":"صُّدُورِ","source_ref":"100:10"}],"changed_reading":{"after":"What issued diffusely from each inner source is consolidated there into its intelligible resultant or gist.","before":"What was privately hidden in the breasts is simply exposed."},"confidence":"strong","focus_anchor":"حُصِّلَ (ح ص ل, root_000330/B001) joined to صُّدُورِ as an origin of issue (ص د ر, root_000849/B004).","mechanism":"The packet supplies collection until a resultant becomes clear and an origin from which acts issue. I infer a reverse operation: dispersed issuances are reduced back to the governing result or gist resident at their source.","model_id":"base_resultant_gist","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_resultant_gist","source_type":"hft","support_id":"sup_4b7ed36557097abb3cb9","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَحُصِّلَ مَا فِى ٱلصُّدُورِ","ayah_ref":"100:10"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000330/B002","root_000849/B001"],"payload":{"activation_trace":[{"assigned_role":"Supplies extraction, discrimination, and assay.","branch_id":"B002","branch_image_ar":"استخراج اللب أو النفيس من غلافه","literal_contribution":"The kernel or precious substance is brought out from a covering.","mapped_root_id":"root_000330","root":"ح ص ل","source_phrase_ar":"حُصِّلَ","source_ref":"100:10"},{"assigned_role":"Supplies the covering or matrix from which an inner substance is extracted.","branch_id":"B001","branch_image_ar":"الصدر الجارحة وما يتصل بها","literal_contribution":"The chest is a bodily front and enclosure.","mapped_root_id":"root_000849","root":"ص د ر","source_phrase_ar":"صُّدُورِ","source_ref":"100:10"}],"changed_reading":{"after":"The chest is subjected to an inner assay that extracts and distinguishes its kernel, not merely displays an undifferentiated contents-list.","before":"The chest is opened and its contents become visible."},"confidence":"strong","focus_anchor":"حُصِّلَ activates extraction from a covering (ح ص ل, root_000330/B002), while صُّدُورِ supplies the bodily chest (ص د ر, root_000849/B001).","mechanism":"The packet supplies a covered bodily interior and the extraction of kernel or precious material from husk, stone, or earth. I infer an assay rather than bare opening: the interior is processed so that what has value or explanatory weight is distinguished from its covering.","model_id":"base_inner_assay","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_inner_assay","source_type":"hft","support_id":"sup_2504d2d4e2312d87eca6","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَحُصِّلَ مَا فِى ٱلصُّدُورِ","ayah_ref":"100:10"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000330/B003","root_000849/B003","root_000849/B004"],"payload":{"activation_trace":[{"assigned_role":"Supplies the enduring remainder after outward manifestations are removed.","branch_id":"B003","branch_image_ar":"البقية والحثالة بعد الرفع أو الفصل","literal_contribution":"A residue or dregs remains after lifting and separation.","mapped_root_id":"root_000330","root":"ح ص ل","source_phrase_ar":"حُصِّلَ","source_ref":"100:10"},{"assigned_role":"Supplies outward issue as a completed phase preceding inspection.","branch_id":"B003","branch_image_ar":"الصُّدور عن المورد","literal_contribution":"Departure occurs after coming to a watering-place or affair.","mapped_root_id":"root_000849","root":"ص د ر","source_phrase_ar":"صُّدُورِ","source_ref":"100:10"},{"assigned_role":"Anchors the residue specifically in the source of conduct.","branch_id":"B004","branch_image_ar":"الأصل الذي تصدر عنه الأفعال","literal_contribution":"Acts issue from an originating source.","mapped_root_id":"root_000849","root":"ص د ر","source_phrase_ar":"صُّدُورِ","source_ref":"100:10"}],"changed_reading":{"after":"Once outward conduct has departed, its inner source is separated down to the motive or residue that did not leave with the acts.","before":"Previously hidden thoughts are brought outward."},"confidence":"medium","focus_anchor":"حُصِّلَ as residue after separation (ح ص ل, root_000330/B003) intersects صُّدُورِ as both departure after arrival (ص د ر, root_000849/B003) and a source of acts (root_000849/B004).","mechanism":"The packet supplies outward departure from a source and a remainder left after removal or separation. I infer a temporal model: after conduct has gone out from the breasts, the final operation isolates what remained there as the durable motive, sediment, or dregs.","model_id":"base_residual_source","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_residual_source","source_type":"hft","support_id":"sup_2d341673516eb2c2409a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَحُصِّلَ مَا فِى ٱلصُّدُورِ","ayah_ref":"100:10"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000330/B001","root_000849/B002"],"payload":{"activation_trace":[{"assigned_role":"Moves an inward multiplicity toward one manifest result.","branch_id":"B001","branch_image_ar":"جمع الشيء حتى يظهر حاصله","literal_contribution":"Collection makes the resultant manifest.","mapped_root_id":"root_000330","root":"ح ص ل","source_phrase_ar":"حُصِّلَ","source_ref":"100:10"},{"assigned_role":"Supplies the destination-status of becoming foremost rather than merely becoming visible.","branch_id":"B002","branch_image_ar":"المقدّم والأعلى والأول","literal_contribution":"The root can image the front, upper, or first part.","mapped_root_id":"root_000849","root":"ص د ر","source_phrase_ar":"صُّدُورِ","source_ref":"100:10"}],"changed_reading":{"after":"The inside is promoted into the foremost, determining result; latent priority becomes explicit priority.","before":"An inside is disclosed to an outside."},"confidence":"medium","focus_anchor":"حُصِّلَ resolves a collected result (ح ص ل, root_000330/B001), and صُّدُورِ also names the foremost or first part (ص د ر, root_000849/B002).","mechanism":"The construction places مَا فِى, what is inside, under an operation whose destination is a clear حاصل, while the containing root also carries the image of the forepart. I infer a spatial-status reversal: what was interior is made foremost, first, and publicly determinative.","model_id":"base_inside_to_fore","status":"baseline"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_inside_to_fore","source_type":"hft","support_id":"sup_674f18cecc7526b82ee0","trust":"legacy_unbound"}]}
</lane_packet_json>
