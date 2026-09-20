# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **32:30**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s032-regular-20260919/s032/32_30/micro.discovery.json` and modify nothing
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
  "ayah_ref": "32:30",
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
{"analysis_context":{"analysis_id":"s032-regular-20260919","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"32:30","host_surah":32,"lane_context_refs":[],"ordered_context_refs":["32:1","32:2","32:3","32:4","32:5","32:6","32:7","32:8","32:9","32:10","32:11","32:12","32:13","32:14","32:15","32:16","32:17","32:18","32:19","32:20","32:21","32:22","32:23","32:24","32:25","32:26","32:27","32:28","32:29","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Bu dal, gösterme veya yüz çevirme eylemlerini değil, en boyutunu ve yan tarafı anlatır.","branch_kind":"bare","branch_ref":"root_001001/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَعْرَضَ","morph_features":"STEM|POS:V|IMPV|(IV)|LEM:>aEoraDa|ROOT:ErD|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:1:2","qac_word_ref":"32:30:1","surface_ar":"أَعْرِضْ"}],"gloss":"en, yan ve enli kılma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesnenin uzunluğuna karşıt en boyutunu belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"En boyutunun belirlediği yan veya taraf için de kullanılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir şeyi enli duruma getirme işlemini de kapsar."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"En boyutunu, bu boyuta bağlı yanı ve ettirgen genişletmeyi birlikte anlatan genel açıklama olarak uygundur.","boundary_detail":"Bu dal, gösterme veya yüz çevirme eylemlerini değil, en boyutunu ve yan tarafı anlatır.","branch_image_ar":"العرض خلاف الطول والجانب","concept_gloss":"en, yan ve enli kılma","contextual_glosses":[{"applicability":"Bir nesnenin ölçüsü veya yan yüzü söz konusu olduğunda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir şeyi enli kılma işlemini belirtmez.","preserves":"En ölçüsünü ve yan taraf ilişkisini korur."},"facet_ids":["F001","F002"],"text":"en ve yan taraf","usage_role":"contextual"}],"definition":"Bir şeyin uzunluğuna dik uzanan en boyutu ya da bu boyutun belirlediği yan taraf; ayrıca bir şeyi bu yönde geniş duruma getirmedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesnenin uzunluğuna karşıt en boyutunu belirtir."},{"facet_id":"F002","role":"extension","statement":"En boyutunun belirlediği yan veya taraf için de kullanılır."},{"facet_id":"F003","role":"specialization","statement":"Bir şeyi enli duruma getirme işlemini de kapsar."}],"identity_rationale":"Kaynak ifadesi, uzunluğa karşıt olan en ölçüsünü ve bir şeyin yanını aynı anlam alanında açıkça verir. Bir şeyi enli kılma da bu uzamsal çekirdeğin ettirgen gerçekleşmesidir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"en; bir şeyin yanı veya tarafı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"enli, geniş"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir şeyi enli duruma getirmek"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"sütten kesilmiş, henüz erginleşmemiş güçlü oğlak"}],"lexicalization_note":"Tanım yalın dalın uzamsal anlamıyla sınırlıdır; özel tamlamalardan başka bir anlam aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en doğrudan sınır karşılaştırmasını sağlayan tek yakın anlamlı komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği uzunluk-en karşıtlığıdır; komşu dal ise yan yüzlerin ve çeşitli nesne yüzlerinin daha geniş adlandırma alanına uzanır.","focus_only":"Odak dal uzunluğa karşıt ölçüyü açıkça kurar.","gloss":"en ve yan alanında yakın anlam","neighbor_only":"Komşu dal yüz, sayfa ve genişletilmiş nesne türlerini daha ayrıntılı sayar.","neighbor_ref":"root_000867/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin enini, yanını ve enli duruma getirilmesini kapsar."}],"source_phrase_ar":"العرض خلاف الطول (maqayis;ayn;sihah;tahdhib;mufradat)؛ عرض الشيء فهو عريض (maqayis;ayn;sihah;tahdhib)؛ العرض الجانب من كل شيء (tahdhib;mufradat)","source_summary":"Kaynakların ortak çekirdeği, uzunluğa karşıt en boyutu ile bu boyuta bağlı yan kavramıdır; niteleme ve ettirgenleştirme de bu çekirdeğe dayanır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العرض الذي يخالف الطول، والعريض، وجعل الشيء عريضا، والجانب أو الناحية من الشيء.","what_is_not_ar":"لا يدخل فيه مجرد الإظهار للغير، ولا الإعراض بمعنى الصد، ولا عرض الدنيا إلا من جهة الأصل الصوري."},"support_links":[]},{"boundary":"Anlam yalnızca belirtilen sunma ve incelemeye çıkarma yapılarında geçerlidir.","branch_kind":"collocation","branch_ref":"root_001001/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَعْرَضَ","morph_features":"STEM|POS:V|IMPV|(IV)|LEM:>aEoraDa|ROOT:ErD|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:1:2","qac_word_ref":"32:30:1","surface_ar":"أَعْرِضْ"}],"gloss":"görmeye veya incelemeye sunma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir fail, bir nesneyi muhatabın görmesi veya değerlendirmesi için ortaya koyar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Malın satışa sunulması, askerin denetlenmesi ve kitabın okunup karşılaştırılması bu yapının özel gerçekleşmeleridir."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin muhataba, satışa, denetime ya da okumaya çıkarıldığı yapıların tümünü kapsar.","boundary_detail":"Anlam yalnızca belirtilen sunma ve incelemeye çıkarma yapılarında geçerlidir.","branch_image_ar":"عرض الشيء وإبرازه للنظر","concept_gloss":"görmeye veya incelemeye sunma","contextual_glosses":[{"applicability":"Bir şeyi birine göstermek veya değerlendirmesine bırakmak bağlamında doğal karşılıktır.","error_profile":{"adds":"Türkçedeki sunmak fiilinin burada bulunmayan ikram ve bildirme anlamlarını da çağrıştırabilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Bir şeyi muhataba yöneltme eylemini korur."},"facet_ids":["F001"],"text":"sunmak","usage_role":"contextual"}],"definition":"Bir şeyi başka birinin görmesi, incelemesi, okuması veya değerlendirmesi için onun önüne getirmek ya da belirli bir amaca sunmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir fail, bir nesneyi muhatabın görmesi veya değerlendirmesi için ortaya koyar."},{"facet_id":"F002","role":"specialization","statement":"Malın satışa sunulması, askerin denetlenmesi ve kitabın okunup karşılaştırılması bu yapının özel gerçekleşmeleridir."}],"identity_rationale":"Kaynak ifadesi, bir şeyi başkasının görmesine veya değerlendirmesine sunmayı; mal, asker ve kitap gibi belirli nesnelerle açıkça örnekler. Dalın kimliği kendiliğinden görünme değil, bir failin yönelttiği sunmadır.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir şeyi birine göstermek veya sunmak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"malı satışa çıkarmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"askerleri gözden geçirmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kitabı okumak veya başka bir nüshayla karşılaştırmak"}],"lexicalization_note":"Tanım, nesnenin birine, satışa veya incelemeye sunulduğu yapılara bağlıdır; yalın kök anlamı olarak genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sunma eyleminin fail ve amaç sınırını en iyi açıklayan yakın anlamlı komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın yapısı nesneyi muhataba veya incelemeye sunmaktır; komşu dalda hayvanın niteliğini hareket ettirerek ortaya çıkarma gibi daha özel bir sınama da vardır.","focus_only":"Odak dal satış, asker denetimi ve kitap incelemesi gibi yapılara bağlanır.","gloss":"gösterip değerlendirmeye sunma","neighbor_only":"Komşu dal özellikle hayvanı satış veya sınama amacıyla yürütüp yeteneğini ortaya çıkarabilir.","neighbor_ref":"root_000827/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyi başkasına göstermek ve değerlendirmeye açmak anlamında örtüşür."}],"source_phrase_ar":"عرض المتاع يعرضه عرضا (maqayis)؛ يعرض علينا المتاع عرضا للبيع والهبة (ayn)؛ عرضت عليه أمر كذا وعرضت له الشيء أظهرته له وأبرزته إليه (sihah)؛ عرضت المتاع وغيره على البيع وكذلك عرض الجند والكتاب (tahdhib)؛ عرضت الشيء على البيع وعلى فلان وعرضنا جهنم (mufradat)","source_summary":"Ortak anlam, bir nesnenin bir muhataba veya belirli bir değerlendirme alanına bilinçli biçimde sunulmasıdır; satış, denetim ve okuma bunun özel bağlamlarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه عرض الشيء أو الأمر على غيره، وعرض المتاع للبيع، وعرض الكتاب أو القرآن، وعرض الجند، وإبراز جهنم أو غيرها حتى يرى.","what_is_not_ar":"لا يدخل فيه مجرد الظهور من غير فاعل مبرز، ولا الصد والإعراض."},"support_links":[]},{"boundary":"Dal, bir failin sunduğu nesneyi değil, göz önünde beliren şeyi anlatır.","branch_kind":"bare","branch_ref":"root_001001/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَعْرَضَ","morph_features":"STEM|POS:V|IMPV|(IV)|LEM:>aEoraDa|ROOT:ErD|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:1:2","qac_word_ref":"32:30:1","surface_ar":"أَعْرِضْ"}],"gloss":"uzaktan belirme ve beliren oluşum","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey, bakan kişiye uzaktan veya bir yönden belirip görünür."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ufukta beliren bulut başta olmak üzere geniş görünen oluşumun adı olabilir."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem görünme olayını hem de özellikle ufukta beliren oluşumu birlikte temsil eder.","boundary_detail":"Dal, bir failin sunduğu nesneyi değil, göz önünde beliren şeyi anlatır.","branch_image_ar":"العارض البادي من جهة","concept_gloss":"uzaktan belirme ve beliren oluşum","contextual_glosses":[{"applicability":"Bir şeyin bakış alanında uzaktan belirdiği olay bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Beliren bulut veya başka oluşumun ad olarak kullanımını vermez.","preserves":"Uzaktan belirme olayını doğal biçimde korur."},"facet_ids":["F001"],"text":"uzaktan görünmek","usage_role":"contextual"}],"definition":"Bir şeyin uzaktan veya belli bir yönden göz önünde belirmesi; ayrıca ufukta genişçe görünen bulut, çekirge sürüsü ya da dağ gibi belirgin oluşumdur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey, bakan kişiye uzaktan veya bir yönden belirip görünür."},{"facet_id":"F002","role":"specialization","statement":"Ufukta beliren bulut başta olmak üzere geniş görünen oluşumun adı olabilir."}],"identity_rationale":"Kaynak ifadesi, bir şeyin uzaktan veya bir yönden belirip görünmesini ve bu görünüşün bulut gibi beliren bir varlık adı olmasını destekler. Burada görünme, başkasının sergileme eyleminden bağımsızdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"uzaktan belirmek, görünmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"uzaktan beliren oluşum; özellikle bulut kümesi"}],"lexicalization_note":"Tanım yalın belirme ve görünme anlamıyla sınırlıdır; sunma yapılarına taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kendiliğinden belirme ile genel görünme arasındaki sınırı en iyi gösteren aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yönlü ve uzaktan belirmeye, ayrıca beliren oluşuma bağlıdır; komşu dal daha genel görünme ve görünür kılma alanını kapsar.","focus_only":"Odak dal uzaktan veya bir yönden beliren oluşumu, özellikle bulutu adlandırabilir.","gloss":"belirme ve görünür olma","neighbor_only":"Komşu dal bir şeyi başkasına görünür kılma ettirgenliğini de kapsar.","neighbor_ref":"root_000097/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin gizlilikten ya da görünmezlikten çıkıp görünmesini anlatır."}],"source_phrase_ar":"أعرض لك الشيء من بعيد إذا ظهر لك وبدا (maqayis)؛ عرض له أمر كذا أي ظهر (sihah)؛ أعرض لك الشيء أي بدا وظهر (tahdhib)؛ العارض البادي عرضه وتارة يخص بالسحاب (mufradat)","source_summary":"Ortak çekirdek, bir şeyin bakana doğru bir yönden belirip görünmesidir; bulut bu görünüşün öne çıkan özel adlandırmasıdır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه ما بدا وظهر للإنسان، وما استقبل من بعيد، والسحاب العارض، والجراد الكثير الذي يملأ الأفق، والجبل أو الشيء البادي عرضه.","what_is_not_ar":"لا يدخل فيه العرض بفعل مبرز للغير، ولا الإعراض بمعنى التولي."},"support_links":[]},{"boundary":"Çekirdek araya girip engel oluşturmadır; müdahale ve saldırı kullanımları bu çekirdeğe bağlı özel yapılardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001001/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَعْرَضَ","morph_features":"STEM|POS:V|IMPV|(IV)|LEM:>aEoraDa|ROOT:ErD|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:1:2","qac_word_ref":"32:30:1","surface_ar":"أَعْرِضْ"}],"gloss":"araya girip engelleme ve karşısına dikilme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlık araya girerek başka bir varlığın geçişini veya ilerleyişini engeller."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin bir işe kendini sokması veya birinin karşısına dikilmesi olarak uygulanır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özel bir yapıda insanları karşılaşılan yönden ayrım gözetmeden öldürme veya yakalamayı anlatır."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel engeli, müdahaleyi ve bunlara bağlı özel saldırı yapısını aynı çekirdekte toplar.","boundary_detail":"Çekirdek araya girip engel oluşturmadır; müdahale ve saldırı kullanımları bu çekirdeğe bağlı özel yapılardır.","branch_image_ar":"الاعتراض حيلولة ومقابلة في الطريق","concept_gloss":"araya girip engelleme ve karşısına dikilme","contextual_glosses":[{"applicability":"Bir varlığın geçişi fiziksel veya mecazi olarak engellendiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İşe kendini sokma ve özel saldırı kullanımlarını kapsamaz.","preserves":"Karşıya çıkma ve engelleme ilişkisini korur."},"facet_ids":["F001"],"text":"önünü kesmek","usage_role":"contextual"}],"definition":"Bir şeyin başka bir şeyin önüne veya arasına girerek geçişini engellemesi ya da bir kişinin bir işe kendini sokup karşısına dikilmesidir. Belirli bir yapıda, karşılaşılan insanları ayrım gözetmeden öldürme veya yakalama anlamına uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlık araya girerek başka bir varlığın geçişini veya ilerleyişini engeller."},{"facet_id":"F002","role":"extension","statement":"Kişinin bir işe kendini sokması veya birinin karşısına dikilmesi olarak uygulanır."},{"facet_id":"F003","role":"associated_use","statement":"Özel bir yapıda insanları karşılaşılan yönden ayrım gözetmeden öldürme veya yakalamayı anlatır."}],"identity_rationale":"Kaynak ifadesi araya girme, önünü kesme ve engel olma çekirdeğini doğrular; ayrıca işe kendini sokma ve insanları ayrım gözetmeden öldürme gibi yapılara uzanır. Bu yüzden dal yalnızca yoldaki fiziksel karşılaşma diye daraltılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"önüne geçip engel olmak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"birinin karşısına dikilmek, ona sataşmak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"insanları ayrım gözetmeden öldürmek veya yakalamak"}],"lexicalization_note":"Yalın engel olma ile belirli müdahale ve ayrım gözetmeyen saldırı yapıları ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; araya girme koşulunu genel engellemeden ayıran komşu en yararlı karşılaştırma olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ayırıcı yanı, fiziksel ya da mecazi olarak araya girip karşıya dikilmektir; komşu dalda araya yerleşme şart olmadan genel alıkoyma yeterlidir.","focus_only":"Odak dal araya girme, işe müdahale etme ve özel saldırı yapısını kapsar.","gloss":"engelleme ve önünü kesme","neighbor_only":"Komşu dal failin birini istediği eylemden alıkoymasına ve vazgeçirmesine odaklanır.","neighbor_ref":"root_001448/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişinin veya şeyin hedefine ulaşmasını engelleme alanında örtüşür."}],"source_phrase_ar":"اعترض في الأمر إذا أدخل نفسه فيه (maqayis)؛ عرض القوم على السيف (ayn)؛ اعترض الشيء دون الشيء أي حال دونه (sihah)؛ كل مانع منعك فهو عارض (tahdhib)؛ اعترض الشيء في حلقه وقف فيه بالعرض (mufradat)","source_summary":"Kaynakların birleşik anlatımı, araya girerek engelleme çekirdeğini; işe müdahale etme ve karşılaşılan insanlara ayrım gözetmeden saldırma uzantılarıyla birlikte verir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه اعترض الشيء إذا حال ومنع، وعرض العارض، والتعرض للناس، والاعتراض في الطريق أو الأمر، واستعراض الناس قتلا أو أخذا من أي وجه.","what_is_not_ar":"لا يدخل فيه العرض الهادئ بمعنى الإظهار، ولا المعارضة بمعنى المقابلة بالمثل إلا إذا كان فيها حيلولة."},"support_links":[]},{"boundary":"Dal, dikkati ve yönelişi geri çekerek yüz çevirme eylemiyle sınırlıdır.","branch_kind":"bare","branch_ref":"root_001001/B005","candidate_links":[{"candidate_id":"cand_0735a0402999ff516706","lane":"micro"},{"candidate_id":"cand_665415f6561c99d49e10","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَعْرَضَ","morph_features":"STEM|POS:V|IMPV|(IV)|LEM:>aEoraDa|ROOT:ErD|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:1:2","qac_word_ref":"32:30:1","surface_ar":"أَعْرِضْ"}],"gloss":"yüz çevirip ilgiyi kesme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, birinden veya bir konudan yönelişini geri çekip yüz çevirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bedensel olarak yanını gösterip dönme, ilgiyi kesmenin görünür gerçekleşmesidir."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişiden veya konudan bedensel ya da tutumsal olarak uzaklaşmayı birlikte anlatır.","boundary_detail":"Dal, dikkati ve yönelişi geri çekerek yüz çevirme eylemiyle sınırlıdır.","branch_image_ar":"الإعراض تولية العرض","concept_gloss":"yüz çevirip ilgiyi kesme","contextual_glosses":[{"applicability":"Bir kişi veya konuyla ilgilenmeyi reddetme bağlamında doğal ve doğrudan karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bedensel dönmeyi ve mecazi ilgisizleşmeyi birlikte korur."},"facet_ids":["F001","F002"],"text":"yüz çevirmek","usage_role":"general"}],"definition":"Bir kişiye veya konuya yönelmeyi bırakıp ondan yüz çevirmek, ilgiyi kesmek ve yanını dönerek uzaklaşmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, birinden veya bir konudan yönelişini geri çekip yüz çevirir."},{"facet_id":"F002","role":"extension","statement":"Bedensel olarak yanını gösterip dönme, ilgiyi kesmenin görünür gerçekleşmesidir."}],"identity_rationale":"Kaynak ifadesi bir kişiden veya işten yüz çevirip uzaklaşmayı, yanını göstererek dönme imgesiyle açıkça destekler. Bu anlam görünme, sunma veya fiziksel en ölçüsü değildir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"birinden yüz çevirmek, onunla ilgiyi kesmek"}],"lexicalization_note":"Tanım yalın yüz çevirme anlamını verir; engelleme ya da gösterme yapıları eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; öznenin yüz çevirmesiyle başkasını uzaklaştırma arasındaki sınırı gösteren aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal öznenin kendi dönüşüne ve ilgisini çekmesine bağlıdır; komşu dal hem öznenin uzaklaşmasını hem de başka birini engelleyip uzaklaştırmasını içerir.","focus_only":"Odak dal öznenin kendisinin yüz çevirip ilgisini kesmesini anlatır.","gloss":"yüz çevirme ve uzaklaşma","neighbor_only":"Komşu dal başkasını bir şeyden engelleyip uzaklaştıran ettirgen kullanımı da kapsar.","neighbor_ref":"root_000848/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişi veya şeyden yönelişi kesip uzaklaşmayı anlatabilir."}],"source_phrase_ar":"أعرضت عن فلان وأعرضت عن هذا الأمر وأعرض بوجهه (maqayis)؛ الإعراض عن الشيء الصد عنه (sihah)؛ أعرض عني فمعناه ولى مبديا عرضه (mufradat)","source_summary":"Ortak çekirdek, bir kişiden veya işten yüz çevirip ilgiyi kesmektir; yanını dönme bu kopuşun bedensel görünümünü açıklar.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه أعرض عن فلان أو عن الأمر أو بوجهه، والصد عنه، والتولي مبديا الجانب.","what_is_not_ar":"لا يدخل فيه الظهور والإبراز، ولا مجرد العرض خلاف الطول."},"support_links":["sup_c4ece2b734bc5ad53914","sup_e3b5ca00b85dbf3f5ca1"]},{"boundary":"Karşılıklılık veya denklik şarttır; sırf engelleme ve genel muhalefet bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001001/B006","candidate_links":[{"candidate_id":"cand_94530876ad2ad92c9d15","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَعْرَضَ","morph_features":"STEM|POS:V|IMPV|(IV)|LEM:>aEoraDa|ROOT:ErD|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:1:2","qac_word_ref":"32:30:1","surface_ar":"أَعْرِضْ"}],"gloss":"denk karşılık verme, karşılaştırma veya değişme","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki taraf hareket veya eylem bakımından birbirinin hizasında ya da dengi olur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İki metni yan yana getirip karşılaştırma, denklik ilişkisinin özel yapısıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir malı başka bir mal karşılığında değiştirme, karşılıklı denk verme yapısıdır."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hareket ve eylem denkliğini, metin karşılaştırmasını ve mal değişimini ortak ilişkileriyle temsil eder.","boundary_detail":"Karşılıklılık veya denklik şarttır; sırf engelleme ve genel muhalefet bu dala girmez.","branch_image_ar":"المعارضة مقابلة ومماثلة ومبادلة","concept_gloss":"denk karşılık verme, karşılaştırma veya değişme","contextual_glosses":[{"applicability":"Birinin yaptığına denk bir eylemle karşılık verme bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hizada ilerleme, metin karşılaştırma ve mal değişimi kullanımlarını vermez.","preserves":"Eylemler arasındaki denklik ve karşılıklılığı korur."},"facet_ids":["F001"],"text":"aynısıyla karşılık vermek","usage_role":"contextual"}],"definition":"Başkasının hizasında ilerlemek veya yaptığına denk bir eylemle karşılık vermek; belirli yapılarda iki metni karşılaştırmak ya da bir malı başka bir malla değişmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki taraf hareket veya eylem bakımından birbirinin hizasında ya da dengi olur."},{"facet_id":"F002","role":"specialization","statement":"İki metni yan yana getirip karşılaştırma, denklik ilişkisinin özel yapısıdır."},{"facet_id":"F003","role":"specialization","statement":"Bir malı başka bir mal karşılığında değiştirme, karşılıklı denk verme yapısıdır."}],"identity_rationale":"Kaynak ifadesi geniş anlamda karşı çıkmayı değil, birinin hizasında ilerlemeyi, yaptığına denk bir karşılık vermeyi, iki metni karşılaştırmayı ve mal değişimini destekler. Bu nedenle dal, genel muhalefet veya sözlü tartışma yerine karşılıklı denklik ve eşleştirme çevresinde tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"birinin hizasında gitmek veya yaptığına denk karşılık vermek"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"iki metni karşılaştırmak"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bir malı başka bir malla değiştirmek"}],"lexicalization_note":"Hizada ilerleme çekirdeği ile metin karşılaştırma ve mal değişimi yapıları ayrı, fakat denklik ilişkisi altında tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel denklik ile bu dalın yapı bağımlı karşılıklılığı arasındaki farkı en iyi gösteren aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli karşılıklı eylem ve karşılaştırma yapılarına bağlıdır; komşu dal denklik ve eşdeğerlik durumunu daha genel bir ilişki olarak kurar.","focus_only":"Odak dal hizada ilerleme, metin karşılaştırma ve mal değişimi yapılarını birlikte taşır.","gloss":"denklik ve misliyle karşılık","neighbor_only":"Komşu dal eşlik, evlilikte denklik, savaşta denk güç ve ödüllendirme gibi daha geniş denklik alanlarını kapsar.","neighbor_ref":"root_001305/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da iki tarafın denkliği ve bir eyleme misliyle karşılık verilmesi alanında örtüşür."}],"source_phrase_ar":"عارضت فلانا في السير إذا سرت حياله وعارضته مثل ما صنع (maqayis)؛ عارضته في المسير وعارضت كتابي بكتابه (sihah)؛ عارضته بمتاع أو دابة معارضة إذا بادلته به وعارضت كتابي بكتابه (tahdhib)","source_summary":"Kaynakların ortak alanı, iki tarafı hizada veya karşılıklı denk konuma getirmedir; hareket, eyleme karşılık verme, metin karşılaştırma ve değiş tokuş bunun farklı gerçekleşmeleridir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه عارضه في السير، وعارضه بمثل صنيعه، والمعارضة في الكتاب أو الكلام، والمبادلة بالمتاع أو الدابة، والمباراة.","what_is_not_ar":"لا يدخل فيه الاعتراض المانع إذا لم تكن مقابلة أو مماثلة، ولا التعريض غير الصريح."},"support_links":["sup_9e7f9d45e9ed77136555"]},{"boundary":"Dalın ayırıcı niteliği sonradan ve çoğu kez beklenmedik biçimde ortaya çıkma ile kalıcı olmamadır.","branch_kind":"mixed_non_bare","branch_ref":"root_001001/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَعْرَضَ","morph_features":"STEM|POS:V|IMPV|(IV)|LEM:>aEoraDa|ROOT:ErD|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:1:2","qac_word_ref":"32:30:1","surface_ar":"أَعْرِضْ"}],"gloss":"sonradan ortaya çıkan kalıcı olmayan durum veya nitelik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir durum veya nitelik sonradan ortaya çıkar ve kalıcı değildir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynağı bilinmeden isabet eden ok, beklenmedik gelişin somut örneğidir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birine ansızın gönül bağlama, hazırlıksız ortaya çıkma özelliğine bağlı bir kullanımdır."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel durum ve nitelik çekirdeğini sonradan ortaya çıkma ve kalıcı olmama koşullarıyla temsil eder.","boundary_detail":"Dalın ayırıcı niteliği sonradan ve çoğu kez beklenmedik biçimde ortaya çıkma ile kalıcı olmamadır.","branch_image_ar":"العرض الطارئ الذي يعرض ثم يزول","concept_gloss":"sonradan ortaya çıkan kalıcı olmayan durum veya nitelik","contextual_glosses":[{"applicability":"Kişiye sonradan gelen ateş veya hastalık bağlamında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hastalık dışındaki olayları ve özel beklenmedik yapıları kapsamaz.","preserves":"Sonradan gelen ve kalıcı olmayan hastalık yönünü korur."},"facet_ids":["F001"],"text":"geçici rahatsızlık","usage_role":"contextual"}],"definition":"Bir şeyde sonradan ortaya çıkan ve kalıcı olmayan durum veya niteliktir. Kişi bağlamında hastalık veya başa gelen olay; belirli yapılarda ise kaynağı bilinmeden gelen bir ok ya da ansızın doğan gönül bağını anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir durum veya nitelik sonradan ortaya çıkar ve kalıcı değildir."},{"facet_id":"F002","role":"example","statement":"Kaynağı bilinmeden isabet eden ok, beklenmedik gelişin somut örneğidir."},{"facet_id":"F003","role":"associated_use","statement":"Birine ansızın gönül bağlama, hazırlıksız ortaya çıkma özelliğine bağlı bir kullanımdır."}],"identity_rationale":"Kaynak ifadesi kişiye sonradan gelen hastalık veya olay ile kalıcılığı olmayan durumu açıkça birleştirir. Beklenmedik ok ve ansızın doğan bağlanma, bu geliş ve geçicilik çekirdeğinin özel yapılarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"sonradan gelen geçici hastalık veya olay"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"nereden atıldığı bilinmeden isabet eden ok"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"birine ansızın gönül bağlamak"}],"lexicalization_note":"Geçici olay çekirdeği ile beklenmedik ok ve ansızın bağlanma yapıları birbirine karıştırılmadan tanımlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; geçicilik ile musibet niteliği arasındaki sınırı en açık gösteren komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal olayın sonradan belirmesi ve kalıcı olmamasını öne çıkarır; komşu dal ise olayın musibet niteliğini kurar ve geçicilik şartı taşımaz.","focus_only":"Odak dal geçiciliği ve ansızın ortaya çıkmayı kurucu özellik sayar.","gloss":"başa gelen olay ve geçici durum","neighbor_only":"Komşu dal başa gelen olayın özellikle bela, felaket veya nöbet oluşuna odaklanır.","neighbor_ref":"root_001562/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişinin başına gelen hastalık veya olumsuz olay alanında buluşur."}],"source_phrase_ar":"العرض من أحداث الدهر كالمرض ونحوه (maqayis)؛ عرضه عارض من الحمى ونحوها (sihah)؛ العرض الأمر يعرض للرجل يبتلى به وسهم عرض (tahdhib)؛ العرض ما لا يكون له ثبات (mufradat)","source_summary":"Ortak çekirdek, sonradan ortaya çıkan ve kalıcılığı olmayan durum veya niteliktir; hastalık, kişinin başına gelen olay, beklenmedik isabet ve ansızın bağlanma bu çekirdeğin farklı bağlamlarıdır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه العارض من الحمى أو السقم، وأحداث الدهر، والمرض والموت ونحوهما، وسهم عرض، والحب أو الرأي الذي يقع بغتة، والعرض الكلامي لما لا ثبات له.","what_is_not_ar":"لا يدخل فيه متاع الدنيا من حيث هو مال أو بدل إلا إذا أريد طروؤه وعدم ثباته."},"support_links":[]},{"boundary":"Dal maddi dünya malı ve karşılık olarak verilen eşya ile sınırlıdır; geçici olay anlamı ancak tarihsel çağrışım düzeyindedir.","branch_kind":"mixed_non_bare","branch_ref":"root_001001/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَعْرَضَ","morph_features":"STEM|POS:V|IMPV|(IV)|LEM:>aEoraDa|ROOT:ErD|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:1:2","qac_word_ref":"32:30:1","surface_ar":"أَعْرِضْ"}],"gloss":"dünya malı, nakit dışı eşya ve mal karşılığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Elde edilebilir dünyevi mal, eşya veya payı belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Nakit para dışında kalan ticari eşyalar bu dalın özel alanıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir hak veya alacak yerine eşya verme, malın karşılık işlevine bağlı bir yapıdır."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel dünyevi payı, ticari eşyayı ve hak yerine verilen malı birlikte açıklar.","boundary_detail":"Dal maddi dünya malı ve karşılık olarak verilen eşya ile sınırlıdır; geçici olay anlamı ancak tarihsel çağrışım düzeyindedir.","branch_image_ar":"العرض متاع وبدل وحظ من الدنيا","concept_gloss":"dünya malı, nakit dışı eşya ve mal karşılığı","contextual_glosses":[{"applicability":"Nakit para dışında alınıp satılan mallar söz konusu olduğunda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel dünyevi payı ve hak yerine mal verme yapısını kapsamaz.","preserves":"Nakit dışı mal ve eşya yönünü korur."},"facet_ids":["F002"],"text":"ticari eşya","usage_role":"contextual"}],"definition":"Dünyaya ait elde edilebilir mal, eşya veya pay; özellikle nakit para dışında kalan ticari eşyadır. Belirli bir yapıda, bir alacak ya da hak yerine verilen malı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Elde edilebilir dünyevi mal, eşya veya payı belirtir."},{"facet_id":"F002","role":"specialization","statement":"Nakit para dışında kalan ticari eşyalar bu dalın özel alanıdır."},{"facet_id":"F003","role":"associated_use","statement":"Bir hak veya alacak yerine eşya verme, malın karşılık işlevine bağlı bir yapıdır."}],"identity_rationale":"Kaynak ifadesi dünya malı, nakit dışı eşya ve kolay elde edilen dünyevi payı açıkça destekler. Bir hak yerine verilen mal da bu maddi değer alanındaki belirli bir değişim yapısıdır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"dünya malı ve geçici dünyevi pay"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"nakit dışındaki ticari eşyalar"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"hakkı yerine bir mal vermek"},{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"yol azığı olarak verilen yiyecek veya aileye götürülen hediye"}],"lexicalization_note":"Dünya malı ve nakit dışı eşya çekirdeği, hak yerine mal verme yapısından ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel maddi mal ile ev eşyası alanını ayıran komşu en açıklayıcı karşılaştırma olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ticari ve karşılık işlevli nakit dışı malı da kapsayan daha soyut bir sınıftır; komşu dal ev eşyası ve çokluk görünümüne bağlıdır.","focus_only":"Odak dal genel dünya malını, nakit dışı ticari eşyayı ve mal karşılığını kapsar.","gloss":"eşya ve maddi mal","neighbor_only":"Komşu dal özellikle ev eşyası, döşek ve çok miktarda mal edinme alanındadır.","neighbor_ref":"root_000010/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da sahip olunan taşınır eşya ve maddi mal alanında buluşur."}],"source_phrase_ar":"العرض طمع الدنيا والدنيا عرض حاضر (maqayis)؛ العرض المتاع والعروض الأمتعة (sihah)؛ جميع متاع الدنيا عرض وما خالف الثمنين عروض (tahdhib)؛ تريدون عرض الدنيا ولو كان عرضا قريبا أي مطلبا سهلا (mufradat)","source_summary":"Ortak anlatım, elde edilebilir dünya malını ve özellikle nakit dışı eşyayı kapsar; kolay kazanç ve hak yerine eşya verme bu maddi değer alanına bağlıdır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه عرض الدنيا، والمتاع غير النقد، والعروض، وما يعطى بدلا عن حق، وما يعرض من المال أو العطاء.","what_is_not_ar":"لا يدخل فيه الحدث العارض كالمرض إلا بجامع الطروء، ولا العرض الجسدي أو الشرف."},"support_links":[]},{"boundary":"Kişinin korunmuş benliği ve bedeni ile yüzün yan bölümü ayrı alt kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001001/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَعْرَضَ","morph_features":"STEM|POS:V|IMPV|(IV)|LEM:>aEoraDa|ROOT:ErD|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:1:2","qac_word_ref":"32:30:1","surface_ar":"أَعْرِضْ"}],"gloss":"kişinin bedeni, saygınlığı ve yüzünün yanı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin bedeni veya benliği, korunması gereken kişisel alan olarak adlandırılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin soyu ve kınanmaktan koruduğu toplumsal saygınlığı bu alana girer."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yüzün, yanağın veya ön dişlerin yan kısmı için bedensel bir adlandırma vardır."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişisel bütünlük ve itibar alanıyla yüzün yan bölümünü birlikte, fakat ayırt ederek temsil eder.","boundary_detail":"Kişinin korunmuş benliği ve bedeni ile yüzün yan bölümü ayrı alt kullanımlardır.","branch_image_ar":"عرض الإنسان حماه وبدنه وظاهر وجهه","concept_gloss":"kişinin bedeni, saygınlığı ve yüzünün yanı","contextual_glosses":[{"applicability":"Bir kişinin kınanmaktan ve aşağılanmaktan koruduğu itibarı söz konusu olduğunda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Beden, benlik ve yüzün yan bölümü kullanımlarını vermez.","preserves":"Korunan toplumsal saygınlık yönünü korur."},"facet_ids":["F002"],"text":"kişisel saygınlık","usage_role":"contextual"}],"definition":"Kişinin bedeni, benliği veya eleştiriden koruduğu toplumsal saygınlığıdır. Ayrı bir bedensel kullanımda yanağın, yüzün ya da ön dişlerin yan tarafını belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin bedeni veya benliği, korunması gereken kişisel alan olarak adlandırılır."},{"facet_id":"F002","role":"extension","statement":"Kişinin soyu ve kınanmaktan koruduğu toplumsal saygınlığı bu alana girer."},{"facet_id":"F003","role":"specialization","statement":"Yüzün, yanağın veya ön dişlerin yan kısmı için bedensel bir adlandırma vardır."}],"identity_rationale":"Kaynak ifadesi kişinin bedeni, benliği ve toplumsal saygınlığı yanında yüzün veya dişlerin yan kısmını da aynı dalda toplar. Bu nedenle dal yalnızca korunmuş onur diye daraltılamaz; bedensel ve itibari kullanımlar açıkça ayrılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"kişinin bedeni, benliği veya saygınlığı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"ayıplanacak yanı olmayan, itibarı temiz"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"yüzün veya yanağın yanı; ön dişlerin yan bölümü"}],"lexicalization_note":"Kişinin bedeni ve saygınlığına ilişkin yalın kullanım, temiz saygınlık tamlaması ve yüz yanı kullanımı ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kişisel korunma alanıyla soya dayalı itibar arasındaki sınırı en iyi gösteren komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda saygınlık, beden ve benlikle birlikte geniş bir kişisel korunma alanıdır; komşu dal ise soy ve köklülüğe dayalı itibarı özelleştirir.","focus_only":"Odak dal beden, benlik ve yüz yanı gibi bedensel kullanımları da taşır.","gloss":"saygınlık ve soy itibarı","neighbor_only":"Komşu dal saygınlığı özellikle soy kökeni, köklülük ve iffet üzerinden kurar.","neighbor_ref":"root_000875/B007","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişinin toplumsal itibarı ve korunmuş saygınlığı alanında örtüşür."}],"source_phrase_ar":"العرض عرض الإنسان حسبة أو نفسه (maqayis)؛ العرض الجسد والنفس والحسب (sihah)؛ العرض بدن كل الحيوان والنفس وحسبه (tahdhib)؛ العارض بالخد وتارة بالسن والعوارض للثنايا (mufradat)","source_summary":"Kaynaklar kişinin bedenini, benliğini ve saygınlığını korunan kişisel alan altında birleştirir; yüz ve dişlerin yan bölümü de ayrı bir bedensel adlandırma olarak verilir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه عرض الإنسان بمعنى حسبه أو نفسه أو بدنه أو ريحه، ونقاء العرض، وعارضا الوجه، والعوارض من الأسنان أو الخدود.","what_is_not_ar":"لا يدخل فيه العرض بمعنى المتاع، ولا مجرد عرض الشيء للبيع."},"support_links":[]},{"boundary":"Dal, sözün veya yazının doğrudan belirtilmeyen ikinci anlamına dayanır; genel mecazın tamamını kapsamaz.","branch_kind":"bare","branch_ref":"root_001001/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَعْرَضَ","morph_features":"STEM|POS:V|IMPV|(IV)|LEM:>aEoraDa|ROOT:ErD|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:1:2","qac_word_ref":"32:30:1","surface_ar":"أَعْرِضْ"}],"gloss":"üstü kapalı, çift yönlü anlatım","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Konuşan kişi niyetini doğrudan söylemez, sözün başka bir yönünden anlaşılmasına bırakır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sözün görünür ve örtük iki anlam taşıması dolaylı anlatımın belirgin yapısıdır."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Niyetin doğrudan söylenmeyip sözün görünür anlamı altından sezdirildiği kullanımları kapsar.","boundary_detail":"Dal, sözün veya yazının doğrudan belirtilmeyen ikinci anlamına dayanır; genel mecazın tamamını kapsamaz.","branch_image_ar":"معاريض الكلام وجه غير مصرح به","concept_gloss":"üstü kapalı, çift yönlü anlatım","contextual_glosses":[{"applicability":"Bir niyetin açıkça değil sezdirilerek anlatıldığı gündelik bağlamlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Açık söylememe ve dolaylı biçimde sezdirme işlevini korur."},"facet_ids":["F001","F002"],"text":"üstü kapalı söylemek","usage_role":"general"}],"definition":"Bir düşünceyi açıkça söylemek yerine, sözün görünür anlamı altında anlaşılabilecek başka bir yön bırakarak dolaylı biçimde anlatmadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Konuşan kişi niyetini doğrudan söylemez, sözün başka bir yönünden anlaşılmasına bırakır."},{"facet_id":"F002","role":"specialization","statement":"Sözün görünür ve örtük iki anlam taşıması dolaylı anlatımın belirgin yapısıdır."}],"identity_rationale":"Kaynak ifadesi açık söylemenin karşıtı olan, görünür sözün altında başka bir anlam taşıyan dolaylı anlatımı açıkça tanımlar. Evlilik niyetini üstü kapalı bildirme ve harfleri açık yazmama bunun bağlama bağlı örnekleridir.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"görünür anlamının altında başka bir anlam taşıyan sözler"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"açıkça söylemeyip üstü kapalı anlatma"}],"lexicalization_note":"Tanım yalın dolaylı anlatım çekirdeğini verir; belirli söz ve yazı örnekleri tüm dala genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bilinçli üstü kapalılık ile genel anlam çıkarımı arasındaki sınırı en iyi gösteren komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda konuşan kişi doğrudan söylemek yerine bilinçli bir örtük yön bırakır; komşu dalda yüzeyden anlama geçiş daha genel olup çift anlamlı söz şart değildir.","focus_only":"Odak dal açık söyleyişin karşıtı olan çift yönlü ve üstü kapalı söz yapısını şart koşar.","gloss":"sözden örtük anlamı sezdirme","neighbor_only":"Komşu dal sözün görünür biçiminden genel anlamına, niyetine veya işaretine yönelmeyi daha geniş kapsar.","neighbor_ref":"root_001349/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da sözün yüzeyinin ötesindeki anlam veya konuşma niyetine yönelir."}],"source_phrase_ar":"معاريض الكلام يخرج في معرض غير لفظه الظاهر (maqayis)؛ التعريض خلاف التصريح والمعاريض في الكلام (sihah)؛ التعريض ما كان خلاف التصريح والمعاريض من الكلام (tahdhib)؛ التعريض كلام له وجهان من صدق وكذب أو ظاهر وباطن (mufradat)","source_summary":"Ortak çekirdek, açık bildirim yerine görünür sözün altında ikinci bir anlam veya niyet bırakmaktır; farklı söz ve yazı bağlamları bu dolaylılığı örnekler.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه التعريض خلاف التصريح، والمعاريض والتورية، والكلام الذي له ظاهر وباطن أو وجهان، والتعريض في خطبة النساء، وتعريض الكاتب إذا لم يبين.","what_is_not_ar":"لا يدخل فيه المعارضة بمعنى المقابلة بالمثل، ولا العرض بمعنى الإظهار الحسي."},"support_links":[]},{"boundary":"Hedef olarak ortaya konma ile bir işe güçlü ve hazır olma ayrı kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001001/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَعْرَضَ","morph_features":"STEM|POS:V|IMPV|(IV)|LEM:>aEoraDa|ROOT:ErD|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:1:2","qac_word_ref":"32:30:1","surface_ar":"أَعْرِضْ"}],"gloss":"hedef olarak ortaya koyma veya bir işe hazır olma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya şey, belirli bir etkiye açık hedef olarak ortaya konur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ortaya konan şey bağlama göre engel veya sürekli saldırı hedefi olabilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yolculuğa ayrılan hayvanın bu işe güçlü ve hazır olması özel bir yapıdır."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Maruz bırakılma çekirdeğini ve yolculuk için güçlü-hazır olma yapısını birlikte belirtir.","boundary_detail":"Hedef olarak ortaya konma ile bir işe güçlü ve hazır olma ayrı kullanımlardır.","branch_image_ar":"العرضة نصب وقوة للتعرض","concept_gloss":"hedef olarak ortaya koyma veya bir işe hazır olma","contextual_glosses":[{"applicability":"Bir kişi veya şey başkalarının etkisine veya saldırısına açık bırakıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yolculuğa güçlü ve hazır olma yapısını kapsamaz.","preserves":"Ortaya koyma ve etkiye açık bırakma yönünü korur."},"facet_ids":["F001","F002"],"text":"hedef hâline getirmek","usage_role":"contextual"}],"definition":"Bir kişi veya şeyi başkalarının etkisine, saldırısına ya da kullanımına açık bir hedef olarak ortaya koymaktır. Belirli bir yapıda, bir hayvanın yolculuğa dayanacak güçte ve hazır olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya şey, belirli bir etkiye açık hedef olarak ortaya konur."},{"facet_id":"F002","role":"extension","statement":"Ortaya konan şey bağlama göre engel veya sürekli saldırı hedefi olabilir."},{"facet_id":"F003","role":"specialization","statement":"Yolculuğa ayrılan hayvanın bu işe güçlü ve hazır olması özel bir yapıdır."}],"identity_rationale":"Kaynak ifadesi birini veya bir şeyi belirli bir etkiye açık hedef olarak yerleştirmeyi ve yolculuk gibi bir işe güçlü veya hazır olmayı destekler. Engel olma yorumu belirli bağlama bağlıdır; dalın tamamı yalnızca engel diye tanımlanamaz.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"hedef veya engel olarak ortaya konmuş şey"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"yolculuğa dayanıklı ve hazır deve"}],"lexicalization_note":"Genel hedef veya maruz kalma kullanımı, yolculuğa güçlü olma tamlamasından ayrı tanımlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hedef olarak ortaya konma ile genel hazırlık arasındaki sınırı en iyi açıklayan komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda hazırlık, özellikle bir etkiye maruz kalacak biçimde ortaya konma ilişkisinden doğar; komşu dalda böyle bir hedef veya maruz kalma koşulu yoktur.","focus_only":"Odak dal hedef olarak ortaya konma ve etkiye açık bırakılma anlamını taşır.","gloss":"hazır ve elverişli olma","neighbor_only":"Komşu dal bir şeyi genel olarak hazırlama, hazır bulundurma veya yapabilecek güçte olma anlamındadır.","neighbor_ref":"root_001685/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir kişi veya şeyin belirli bir iş için hazır ya da elverişli olmasını anlatabilir."}],"source_phrase_ar":"فلان عرضة للناس لا يزالون يقعون فيه (maqayis)؛ فلان عرضة لذاك أي مقرن له قوي عليه وجعلت فلانا عرضة لكذا أي نصبته له (sihah)؛ لا تجعلوا الحلف بالله معترضا مانعا وجعلت فلانا عرضة أي نصبته له (tahdhib)؛ العرضة ما يجعل معرضا للشيء ولا تجعلوا الله عرضة لأيمانكم (mufradat)","source_summary":"Kaynakların ortak alanı, bir şeyi belirli bir etkiye açık biçimde ortaya koymaktır; sürekli hedef olma, engel oluşturma ve yolculuğa hazır güçte bulunma bağlama göre ayrışır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه جعل الشيء عرضة أي منصوبا أو معرضا، وعرضة للأيمان أو للشر أو للناس، والقوة على الشيء كناقة عرضة للسفر.","what_is_not_ar":"لا يدخل فيه الاعتراض المانع إلا إذا أفاد كونه نصبا أو عائقا، ولا العرض بمعنى المتاع."},"support_links":[]},{"boundary":"Dal yalnızca hareket içindeki yana sapma ve doğrultuyu koruyamama durumunu anlatır.","branch_kind":"bare","branch_ref":"root_001001/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَعْرَضَ","morph_features":"STEM|POS:V|IMPV|(IV)|LEM:>aEoraDa|ROOT:ErD|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:1:2","qac_word_ref":"32:30:1","surface_ar":"أَعْرِضْ"}],"gloss":"yana saparak ilerleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hayvan hareket ederken düz doğrultuyu korumaz ve yana sapar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu yana sapmalı yürüyüş hayvanın güç idare edilmesi veya zor yürümesiyle ilişkilidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dağda sağa sola yönelerek ilerleme, aynı doğrusal olmayan hareketin insan bağlamındaki uzantısıdır."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvanın veya yolcunun doğrultuyu korumadan sağa sola yöneldiği hareketi temsil eder.","boundary_detail":"Dal yalnızca hareket içindeki yana sapma ve doğrultuyu koruyamama durumunu anlatır.","branch_image_ar":"السير عارضا وصعوبة الاستقامة","concept_gloss":"yana saparak ilerleme","contextual_glosses":[{"applicability":"Düz bir yol tutamayan hayvan veya kişi hareketi için doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvanın zor idare edilmesi ve yanını gösterme ayrıntılarını açıkça vermez.","preserves":"Doğrultudan yana saparak ilerleme biçimini korur."},"facet_ids":["F001","F003"],"text":"sağa sola saparak gitmek","usage_role":"contextual"}],"definition":"Bir hayvanın veya kişinin düz doğrultuda ilerlemeyip yana ya da sağa sola saparak gitmesidir. Bazı hayvan kullanımlarında yanını göstererek koşma veya zor idare edilme bu harekete eşlik eder.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hayvan hareket ederken düz doğrultuyu korumaz ve yana sapar."},{"facet_id":"F002","role":"specialization","statement":"Bu yana sapmalı yürüyüş hayvanın güç idare edilmesi veya zor yürümesiyle ilişkilidir."},{"facet_id":"F003","role":"extension","statement":"Dağda sağa sola yönelerek ilerleme, aynı doğrusal olmayan hareketin insan bağlamındaki uzantısıdır."}],"identity_rationale":"Kaynak ifadesi hayvanın düz ilerlemeyip yanını göstererek veya sağa sola saparak gitmesini ve bu yürüyüşteki zorluğu açıkça destekler. Dağda sağa sola yönelme de aynı doğrusal olmayan hareket özelliğine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"atın koşarken yanını göstererek veya yana saparak gitmesi"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"yürüyüşü zor ve doğrultusunu korumayan dişi deve"}],"lexicalization_note":"Tanım yalın hareket ve yürüyüş anlamıyla sınırlıdır; durağan en ölçüsü bu dala aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yana sapmalı yürüyüşü durdurulamayan ileri hareketten ayıran komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dalda belirleyici biçim yana sapma ve düzgün yürüyememedir; komşu dalda belirleyici güç, ileri atılma ve durdurulamamadır.","focus_only":"Odak dal hareketin yana sapmasına ve doğrultusuz güçlüğüne odaklanır.","gloss":"zor denetlenen hayvan hareketi","neighbor_only":"Komşu dal hayvanın biniciyi dinlemeden güçlü ve durdurulamaz biçimde ileri gitmesini anlatır.","neighbor_ref":"root_000257/B001","relation_type":"same_field","shared_zone":"Her iki dal da hayvanın sürücünün istediği doğrultuda kolayca yönetilemeyen hareketini konu alır."}],"source_phrase_ar":"عرض الفرس في عدوه كأنه يرى الناظر عرضه (maqayis)؛ عرض الفرس في عدوه إذا مر عارضا على جنب واحد (ayn)؛ اعترض الفرس في رسنه لم يستقم لقائده وناقة عرضية فيها صعوبة (sihah)؛ تعرض فلان في الجبل أخذ يمينا وشمالا (tahdhib)؛ اعترض الفرس في مشيه وفيه عرضية أي اعتراض في مشيه من الصعوبة (mufradat)","source_summary":"Ortak çekirdek, hareket sırasında düz doğrultudan yana sapmadır; hayvanın zor idare edilmesi ve dağda sağa sola ilerleme bu hareket biçiminin bağlamlarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه عرض الفرس في عدوه، واعتراض الفرس أو البعير إذا لم يستقم، والناقة العرضية أو العروض الصعبة، والتعرض في الجبل يمينا وشمالا.","what_is_not_ar":"لا يدخل فيه العرض خلاف الطول إذا لم يدل على حركة أو صعوبة سير."},"support_links":[]},{"boundary":"Dal, somut bir nesnenin enine yerleştirilmesi veya yana yönelmesiyle sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001001/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَعْرَضَ","morph_features":"STEM|POS:V|IMPV|(IV)|LEM:>aEoraDa|ROOT:ErD|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:1:2","qac_word_ref":"32:30:1","surface_ar":"أَعْرِضْ"}],"gloss":"enine yerleştirme, enine parça ve yana giden ok","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesne, başka bir nesneye göre enine gelecek biçimde yerleştirilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kapı veya taşıma düzenindeki enine kiriş, bu yönelimin yapısal nesnesidir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yana doğru giden veya tüyü bulunmayan özel ok, yönelime bağlı bir araç adıdır."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Enine yönelimi eylem, yapısal parça ve özel araç türleriyle birlikte temsil eder.","boundary_detail":"Dal, somut bir nesnenin enine yerleştirilmesi veya yana yönelmesiyle sınırlıdır.","branch_image_ar":"الشيء الموضوع عرضا أو المعترض عرضيا","concept_gloss":"enine yerleştirme, enine parça ve yana giden ok","contextual_glosses":[{"applicability":"Bir çubuk veya benzeri nesne başka bir nesnenin üzerine enine yerleştirildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yapısal parça ve özel ok adlarını kapsamaz.","preserves":"Enine yönelimi ve yerleştirme işlemini korur."},"facet_ids":["F001"],"text":"enlemesine koymak","usage_role":"contextual"}],"definition":"Bir nesneyi başka bir nesnenin üzerine veya açıklığa enine yerleştirmek; ayrıca enine duran taşıyıcı parça ya da yana doğru giden özel ok gibi somut nesnelerdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesne, başka bir nesneye göre enine gelecek biçimde yerleştirilir."},{"facet_id":"F002","role":"specialization","statement":"Kapı veya taşıma düzenindeki enine kiriş, bu yönelimin yapısal nesnesidir."},{"facet_id":"F003","role":"specialization","statement":"Yana doğru giden veya tüyü bulunmayan özel ok, yönelime bağlı bir araç adıdır."}],"identity_rationale":"Kaynak ifadesi bir çubuğu enlemesine yerleştirme eylemini, enine duran kapı ve taşıyıcı parçaları ve yana doğru giden özel oku açıkça aynı uzamsal yönelim altında toplar.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"çubuğu kabın üzerine enlemesine koymak"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"tüysüz veya yana doğru giden özel ok"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"kapı sövelerini üstten tutan enine kiriş"}],"lexicalization_note":"Enine yerleştirme yapısı, enine taşıyıcı parça ve özel ok adlarından ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel enine yönelim ile özel taşıyıcı kiriş arasındaki sınırı gösteren aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal enine yönelime dayalı daha geniş bir eylem ve nesne alanıdır; komşu dal işlevi belirlenmiş özel bir taşıyıcı kiriş adıdır.","focus_only":"Odak dal enine yerleştirme eylemini, çeşitli enine parçaları ve özel oku kapsar.","gloss":"enine konan taşıyıcı parça","neighbor_only":"Komşu dal özellikle asma çubuklarını veya ahşap uçlarını taşıyan tek tür enine kiriştir.","neighbor_ref":"root_000243/B007","relation_type":"near_neighbor","shared_zone":"Her iki dal da başka parçaları taşıyacak biçimde enine konan ahşap öğeyi kapsar."}],"source_phrase_ar":"عرضت العود على الإناء وضعته عليه عرضا (maqayis;ayn;sihah;tahdhib;mufradat)؛ المعراض سهم يمضي عرضا (maqayis;sihah;tahdhib)؛ عارضة الباب والعوارض سقائف المحمل (maqayis;sihah;tahdhib)","source_summary":"Ortak çekirdek enine yönelimdir; yerleştirme eylemi, kapı ve taşıma kirişleri ile yana giden özel ok bu yönelimin nesne ve araç kullanımlarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه وضع العود على الإناء عرضا، وعوارض السقف أو المحمل، وعارضة الباب، والمعراض السهم الذي يمضي عرضا أو لا ريش له.","what_is_not_ar":"لا يدخل فيه الاعتراض المجازي في الكلام أو الناس إلا إذا دل على جسم موضوع بالعرض."},"support_links":[]},{"boundary":"Yön, dağ yolu, şiir ölçüsü ve belgelenen bölge adı korunur; genel yer adı sınıfı kurulmaz.","branch_kind":"bare","branch_ref":"root_001001/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَعْرَضَ","morph_features":"STEM|POS:V|IMPV|(IV)|LEM:>aEoraDa|ROOT:ErD|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:1:2","qac_word_ref":"32:30:1","surface_ar":"أَعْرِضْ"}],"gloss":"yön, dağ yolu, bölge adı ve şiir ölçüsü","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yönü, yanı veya gidilen tarafı belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dağ içindeki yol ve belirli bölge adı, yer-yön kullanımının özelleşmeleridir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Şiirin ölçü düzeni, yön ve yan kavramından türemiş teknik bir kullanımdır."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belgelenen yer-yön kullanımlarıyla teknik şiir ölçüsü kullanımını eksiksiz biçimde sıralar.","boundary_detail":"Yön, dağ yolu, şiir ölçüsü ve belgelenen bölge adı korunur; genel yer adı sınıfı kurulmaz.","branch_image_ar":"عروض ونواح وأسماء فنية أو موضعية","concept_gloss":"yön, dağ yolu, bölge adı ve şiir ölçüsü","contextual_glosses":[{"applicability":"Şiirin veznini ve ölçü düzenini inceleyen teknik alan söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yön, dağ yolu ve bölge adı kullanımlarını kapsamaz.","preserves":"Teknik şiir ölçüsü kullanımını açık biçimde korur."},"facet_ids":["F003"],"text":"şiir ölçüsü bilimi","usage_role":"contextual"}],"definition":"Bir yön veya yan, dağ içindeki bir yol ya da belirli bir bölgenin adı olabilir; teknik kullanımda şiirin veznini inceleyen ölçü düzenini belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yönü, yanı veya gidilen tarafı belirtir."},{"facet_id":"F002","role":"specialization","statement":"Dağ içindeki yol ve belirli bölge adı, yer-yön kullanımının özelleşmeleridir."},{"facet_id":"F003","role":"extension","statement":"Şiirin ölçü düzeni, yön ve yan kavramından türemiş teknik bir kullanımdır."}],"identity_rationale":"Kaynak ifadesi yön veya yan, dağ yolu, şiir ölçüsü ve belirli bölge adı kullanımlarını destekler. Geçici çerçevedeki köy ve vadi genellemesi kaynak cümlesinde kurucu içerik değildir; dal yalnızca belgelenen teknik ve yer-yön kullanımlarıyla tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"şiir ölçüsü ve vezin bilimi"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"yön, dağ yolu veya belirli bölge"}],"lexicalization_note":"Tanım yalın ve belgelenmiş çoklu adlandırmaları verir; başka yer adları veya tamlamalar eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yön kullanımını hareket bağlamındaki gelinen taraftan ayıran komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yön anlamından teknik ve yer adlarına uzanan çoklu bir adlandırmadır; komşu dal yalnızca bir yerden geliş yönünü belirten bağlamsal bir taraf adıdır.","focus_only":"Odak dal yönün yanında dağ yolu, bölge adı ve teknik şiir ölçüsü kullanımlarını kapsar.","gloss":"yön ve gelinen taraf","neighbor_only":"Komşu dal özellikle insanların geldiği yön veya tarafı anlatan hareket bağlamına bağlıdır.","neighbor_ref":"root_000065/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir yönü, yanı veya tarafı adlandırma alanında buluşur."}],"source_phrase_ar":"العروض الناحية أو ناحية من العلم (maqayis)؛ العروض ميزان الشعر والعروض طريق في الجبل ومكة والمدينة وما حولهما (sihah)؛ العروض عروض الشعر وأخذ في عروض أي ناحية واستعمل على العروض (tahdhib)","source_summary":"Kaynakların birleşik içeriği yön veya yan anlamını, dağ yolu ve belirli bölge adıyla birlikte verir; şiir ölçüsü de bu adlandırmanın teknik uzantısıdır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه العروض بمعنى الناحية أو الطريق في الجبل أو الموضع، وعروض الشعر وميزانه، والعروض اسما لمكة والمدينة وما حولهما، والأعراض للقرى أو الأودية.","what_is_not_ar":"لا يدخل فيه العرض العام خلاف الطول إلا أصل اشتقاق، ولا يعمم هذا على كل استعمال للناحية إذا كان له فرع أدق."},"support_links":[]},{"boundary":"Dal, doğrudan görmeyi, dikkatli incelemeyi ve düşünmeyi kapsar; bekleme, eşlik ve karşılıklı tartışma anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001520/B001","candidate_links":[{"candidate_id":"cand_665415f6561c99d49e10","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَنتَظِرُ","morph_features":"STEM|POS:V|IMPV|(VIII)|LEM:yantaZiru|ROOT:nZr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:3:2","qac_word_ref":"32:30:3","surface_ar":"ٱنتَظِرْ"},{"lemma_ar":"مُنتَظِرُون","morph_features":"STEM|POS:N|ACT|PCPL|(VIII)|LEM:muntaZiruwn|ROOT:nZr|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"32:30:5:1","qac_word_ref":"32:30:5","surface_ar":"مُّنتَظِرُونَ"}],"gloss":"bakıp inceleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Görme ya da anlama amacıyla göz veya zihinsel dikkat bir nesneye yöneltilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gözle bakma, nesneyi doğrudan görme ve göz önünde inceleme biçiminde gerçekleşir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir konu üzerinde düşünme, onu araştırma ve sonuçlarını tartma biçiminde zihinsel olarak gerçekleşir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Dikkatli incelemenin ardından elde edilen bilgi, yöneltilmiş incelemenin sonucu olarak adlandırılabilir."}}],"root_ar":"ن ظ ر","root_id":"root_001520","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Görsel ya da zihinsel dikkatin bir şeye yöneltilmesini birlikte anlatan en kısa genel karşılıktır.","boundary_detail":"Dal, doğrudan görmeyi, dikkatli incelemeyi ve düşünmeyi kapsar; bekleme, eşlik ve karşılıklı tartışma anlamlarını kapsamaz.","branch_image_ar":"توجيه البصر أو البصيرة لإدراك الشيء","concept_gloss":"bakıp inceleme","contextual_glosses":[{"applicability":"Gözün bir nesneye yöneltildiği ve nesnenin görülüp incelendiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Görsel yönelme ve dikkatli inceleme özelliklerini eksiksiz korur."},"facet_ids":["F001","F002"],"text":"bir şeye dikkatle bakmak","usage_role":"contextual"},{"applicability":"Bir işin ya da düşüncenin zihinsel olarak araştırılıp tartıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Zihinsel yönelme, düşünme ve araştırma özelliklerini korur."},"facet_ids":["F001","F003"],"text":"bir konuyu düşünüp incelemek","usage_role":"contextual"}],"definition":"Gözü ya da zihinsel dikkati bir şeye yönelterek onu görmeye, anlamaya veya ayrıntılı biçimde incelemeye çalışma; inceleme sonunda bilgi edinme bu sürecin sonucu olabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Görme ya da anlama amacıyla göz veya zihinsel dikkat bir nesneye yöneltilir."},{"facet_id":"F002","role":"specialization","statement":"Gözle bakma, nesneyi doğrudan görme ve göz önünde inceleme biçiminde gerçekleşir."},{"facet_id":"F003","role":"specialization","statement":"Bir konu üzerinde düşünme, onu araştırma ve sonuçlarını tartma biçiminde zihinsel olarak gerçekleşir."},{"facet_id":"F004","role":"extension","statement":"Dikkatli incelemenin ardından elde edilen bilgi, yöneltilmiş incelemenin sonucu olarak adlandırılabilir."}],"identity_rationale":"Kaynak ifadesi, bakışı ya da zihinsel dikkati bir şeye yönelterek onu görme, inceleme ve üzerinde düşünme çekirdeğini açıkça destekler. Görsel bakma ile düşünsel inceleme aynı dikkat yöneltme temelinde buluşur; inceleme sonunda edinilen bilgi ise çekirdeğin sonucu olarak kalır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bakma ve inceleme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şeye bakıp onu görmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir konuyu düşünüp incelemek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bakanlar veya seyredenler"}],"lexicalization_note":"Tanım hem yalın ad ve biçimleri hem de bir şeye bakma ile bir konuyu inceleme yapılarının ayrı kapsamlarını korur; yapıya bağlı düşünme anlamı bütün dala yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca görme ve dikkatli inceleme sınırlarını doğrudan açıklayan iki komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda dikkat yöneltme ve inceleme süreci kurucudur; komşu dalda ise görme ve algılama sonucu öne çıkar. Bu nedenle her bağlamda birbirlerinin yerine geçmezler.","focus_only":"Odak dal, görmenin yanında düşünerek incelemeyi ve araştırma sonucunda bilgi edinmeyi de kapsar.","gloss":"gözle veya zihinle görme","neighbor_only":"Komşu dalın çekirdeği, görüleni göz ya da iç kavrayış yoluyla algılama sonucuna daha doğrudan dayanır.","neighbor_ref":"root_000531/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyi gözle ya da zihinsel yetiyle kavrama alanında buluşur."},{"boundary_match":"partial","distinction":"Komşu dal dikkatli ve sağlam incelemeye daha dar biçimde bağlıdır; odak dal ise basit görsel yönelmeden zihinsel araştırmaya kadar daha geniş bir alanı kapsar.","focus_only":"Odak dal, yalnızca gözle bakma ve doğrudan görme bağlamlarını da içerir.","gloss":"dikkatle düşünüp inceleme","neighbor_only":"Komşu dal, özellikle bir şey üzerinde durup açık ve sağlam biçimde inceleme sınırı taşır.","neighbor_ref":"root_000052/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda da dikkatli inceleme ve bir şeyin anlamını kavrama amacı vardır."}],"source_phrase_ar":"تأمل الشيء ومعاينته؛ نظرت إلى الشيء إذا عاينته (maqayis)؛ النظر تأمل الشئ بالعين (sihah)؛ نظر العين ونظر القلب؛ نظرت في الأمر احتمل أن يكون تفكرا وتدبرا بالقلب (tahdhib)؛ تقليب البصر والبصيرة لإدراك الشيء ورؤيته؛ التأمل والفحص؛ المعرفة الحاصلة بعد الفحص؛ مشاهدون؛ تعتبرون (mufradat)","source_summary":"Kaynaklar gözle görme ile zihin yoluyla düşünme ve incelemeyi ortak bir dikkat yöneltme alanında birleştirir. Araştırma sonrasında oluşan bilgi, eylemin kendisi değil onun olası sonucudur.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه نظر العين إلى الشيء ومعاينته، والنظر في الأمر بالتأمل والفحص والتدبر، والمشاهدة والاعتبار حيث نص المصدر عليها.","what_is_not_ar":"لا يدخل فيه الانتظار والإمهال، ولا النظير، ولا المناظرة الاصطلاحية إلا من جهة أصل النظر."},"support_links":["sup_e3b5ca00b85dbf3f5ca1"]},{"boundary":"Bekleme, geciktirme ve iyilik umma aynı başlıkta yer alsa da eyleyenin bekleyen mi yoksa süre veren mi olduğu her kullanımda ayrı gösterilmelidir.","branch_kind":"mixed_non_bare","branch_ref":"root_001520/B002","candidate_links":[{"candidate_id":"cand_0735a0402999ff516706","lane":"micro"},{"candidate_id":"cand_665415f6561c99d49e10","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَنتَظِرُ","morph_features":"STEM|POS:V|IMPV|(VIII)|LEM:yantaZiru|ROOT:nZr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:3:2","qac_word_ref":"32:30:3","surface_ar":"ٱنتَظِرْ"},{"lemma_ar":"مُنتَظِرُون","morph_features":"STEM|POS:N|ACT|PCPL|(VIII)|LEM:muntaZiruwn|ROOT:nZr|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"32:30:5:1","qac_word_ref":"32:30:5","surface_ar":"مُّنتَظِرُونَ"}],"gloss":"bekleme veya süre tanıma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Beklenen olayın gerçekleşmesi için gelecek bir zamana yönelinir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bekleyen kişi durur, oyalanır veya birinin gelişini gözetir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yetkili kişi bir işi geciktirir ve karşı tarafa ek süre verir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Belirli bir söz yapısında kişi, bir kaynaktan gelecek iyiliği bekler ve umar."}}],"root_ar":"ن ظ ر","root_id":"root_001520","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bekleyen ile süre veren rollerinin bağlamdan anlaşılabildiği genel açıklamalarda kullanılır.","boundary_detail":"Bekleme, geciktirme ve iyilik umma aynı başlıkta yer alsa da eyleyenin bekleyen mi yoksa süre veren mi olduğu her kullanımda ayrı gösterilmelidir.","branch_image_ar":"ترقب الوقت وإمهال الطالب","concept_gloss":"bekleme veya süre tanıma","contextual_glosses":[{"applicability":"Bir kişinin ya da olayın gelişini durup gözeten katılımcı için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bekleyenin gelecek zamana yönelmesini ve geliş beklentisini korur."},"facet_ids":["F001","F002"],"text":"gelmesini beklemek","usage_role":"contextual"},{"applicability":"Bir borç, iş veya istek için karşı tarafa ek zaman tanındığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yetkili kişinin geciktirmesi ve karşı tarafa süre vermesi özelliklerini korur."},"facet_ids":["F001","F003"],"text":"süre verip ertelemek","usage_role":"contextual"},{"applicability":"Belirli bir söz yapısında bir kaynaktan gelecek iyiliğin beklendiği durumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gelecekte beklenen iyiliğe yönelme özelliğini korur."},"facet_ids":["F001","F004"],"text":"iyilik ummak","usage_role":"contextual"}],"definition":"Bir kişinin ya da zamanın gelmesini beklemek veya bir işin gerçekleşmesini ileri bir zamana bırakarak süre tanımak; belirli bir yapıda birinden gelecek iyiliği ummak da bu zaman yönelimli alana bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Beklenen olayın gerçekleşmesi için gelecek bir zamana yönelinir."},{"facet_id":"F002","role":"specialization","statement":"Bekleyen kişi durur, oyalanır veya birinin gelişini gözetir."},{"facet_id":"F003","role":"specialization","statement":"Yetkili kişi bir işi geciktirir ve karşı tarafa ek süre verir."},{"facet_id":"F004","role":"associated_use","statement":"Belirli bir söz yapısında kişi, bir kaynaktan gelecek iyiliği bekler ve umar."}],"identity_rationale":"Kaynak ifadesi bekleme, birine süre tanıma ve birinden iyilik umma kullanımlarını birlikte doğrular. Bunlar zamanın gelmesini gözetme ortaklığı taşır, ancak bekleyen kişi ile süre veren kişi farklı katılımcı rollerine sahiptir; bu yüzden dal ancak bu ayrım açık tutulursa kullanılabilir.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"onu beklemek"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bekleme"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"durup beklemek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"ona süre verip ertelemek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ondan ek süre istemek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bekleyip geleceğini gözetmek"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"erteleme ve geciktirme"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"süre verme ve erteleme"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"bekle"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"önce Tanrı'dan, sonra senden iyilik umarım"},{"lexical_unit_id":"lu_044","rendering_kind":"ordinary","target_gloss":"kendisinden iyilik umulan"}],"lexicalization_note":"Yalın bekleme ve geciktirme biçimleri ile iyilik umma yapısı ayrı tutulur; yapıya bağlı beklenti anlamı yalın biçimlerin tümüne yüklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bekleme ile süre verme sınırını en açık gösteren iki geciktirme komşusu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın kapsamı bekleme ile süre tanıma arasındaki rol değişimini içerir; komşu dalın çekirdeği ise daha genel ve çeşitli gecikme türleridir.","focus_only":"Odak dal, birinin gelişini beklemeyi ve belirli bir yapıda iyilik ummayı da kapsar.","gloss":"geciktirme ve süre uzatma","neighbor_only":"Komşu dal, borçtan takvime ve bedensel süreçlere kadar çok çeşitli gecikme alanlarına uzanır.","neighbor_ref":"root_001501/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da bir işi sonraki zamana bırakma ve birine ek süre verme alanında buluşur."},{"boundary_match":"partial","distinction":"Komşu dal doğrudan sonralık ve erteleme üzerine kuruludur; odak dal ise bekleyen kişinin zaman gözetmesini de çekirdeğe bağlar.","focus_only":"Odak dal, bir kişiyi bekleme ve ondan gelecek iyiliği umma anlamlarını da taşır.","gloss":"daha sonraya bırakma","neighbor_only":"Komşu dal, bir şeyi sona veya daha sonraki bir konuma bırakma yönünü ayrıca kapsar.","neighbor_ref":"root_000019/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir işin ya da ödemenin sonraki bir zamana ertelenmesi bulunur."}],"source_phrase_ar":"نظرته أي انتظرته؛ ينظر إلى الوقت الذي يأتي فيه (maqayis)؛ النظر الانتظار؛ النظرة التأخير؛ أنظرته أي أخرته؛ استنظره أي استمهله (sihah)؛ إنما أنظر إلى الله ثم إليك أي أتوقع فضل الله ثم فضلك؛ أنظرني أي انتظرني قليلا؛ أمهلته؛ النظرة إنظار (tahdhib)؛ النظر الانتظار؛ نظرته وانتظرته وأنظرته أي أخرته (mufradat)","source_summary":"Kaynaklar birinin gelişini bekleme, bir işi geciktirerek süre verme ve belirli bir söz kalıbında iyilik umma kullanımlarını aktarır. Bekleme ile süre verme aynı zaman yönelimini paylaşsa da katılımcı rolleri ters yöndedir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه نظرته بمعنى انتظرته، وانتظر وأنظر وأخر وأمهل، والاسم النظرة والإنظار، وتوقع الفضل.","what_is_not_ar":"لا يدخل فيه نظر العين إلى الشيء إذا تعدى بإلى، ولا المثلية في نظير."},"support_links":["sup_c4ece2b734bc5ad53914","sup_e3b5ca00b85dbf3f5ca1"]},{"boundary":"Dal yalnızca verilen yer ve yön yapılarındaki karşı karşıya olma anlamını taşır; salt benzerlik veya zamansal bekleme bu sınıra girmez.","branch_kind":"collocation","branch_ref":"root_001520/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَنتَظِرُ","morph_features":"STEM|POS:V|IMPV|(VIII)|LEM:yantaZiru|ROOT:nZr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:3:2","qac_word_ref":"32:30:3","surface_ar":"ٱنتَظِرْ"},{"lemma_ar":"مُنتَظِرُون","morph_features":"STEM|POS:N|ACT|PCPL|(VIII)|LEM:muntaZiruwn|ROOT:nZr|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"32:30:5:1","qac_word_ref":"32:30:5","surface_ar":"مُّنتَظِرُونَ"}],"gloss":"görüş doğrultusunda karşı karşıya olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki taraf aynı görüş doğrultusunda karşı karşıya bulunur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Komşu topluluklar veya evler birbirini görecek biçimde yan yana ya da karşı karşıyadır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yolda ilerleyen kişinin karşısında bir dağın belirmesi tek yönlü karşıya çıkma örneğidir."}}],"root_ar":"ن ظ ر","root_id":"root_001520","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Verilen yer ve yön yapılarında tarafların birbirini görebilecek biçimde konumlandığı durumları anlatır.","boundary_detail":"Dal yalnızca verilen yer ve yön yapılarındaki karşı karşıya olma anlamını taşır; salt benzerlik veya zamansal bekleme bu sınıra girmez.","branch_image_ar":"تواجه الأشياء حتى يرى بعضها بعضا","concept_gloss":"görüş doğrultusunda karşı karşıya olma","contextual_glosses":[{"applicability":"Toplulukların veya yerleşimlerin yakın ve karşılıklı görünür olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Komşuluk, karşılıklı görünürlük ve mekansal yakınlık özelliklerini korur."},"facet_ids":["F001","F002"],"text":"birbirini görebilecek biçimde komşu olmak","usage_role":"contextual"},{"applicability":"Bir dağın yol üzerinde ilerleyen kişinin görüş doğrultusunda belirdiği örnekte kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tek yönlü mekansal karşılaşma ve görüş doğrultusu özelliklerini korur."},"facet_ids":["F001","F003"],"text":"karşısına çıkmak","usage_role":"contextual"}],"definition":"Belirli yer ve yön yapılarında kişilerin ya da nesnelerin birbirini görebilecek veya birinin ötekine karşı çıkacağı biçimde karşı karşıya ve aynı görüş doğrultusunda bulunması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki taraf aynı görüş doğrultusunda karşı karşıya bulunur."},{"facet_id":"F002","role":"specialization","statement":"Komşu topluluklar veya evler birbirini görecek biçimde yan yana ya da karşı karşıyadır."},{"facet_id":"F003","role":"example","statement":"Yolda ilerleyen kişinin karşısında bir dağın belirmesi tek yönlü karşıya çıkma örneğidir."}],"identity_rationale":"Kaynak ifadesi komşu toplulukların birbirini görebilmesini, evlerin karşı karşıya bulunmasını ve yol üzerindeki dağın kişinin karşısına çıkmasını aynı mekansal karşılaşma altında destekler. Görünürlük bazı örneklerde karşılıklıdır, dağ örneğinde ise tek yönlü bir karşıya çıkma söz konusudur.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"birbirini görebilen komşu topluluk"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"evim onun evine bakar ve karşısındadır"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"dağ yol üzerinde karşına çıktı"}],"lexicalization_note":"Tanım yalnızca komşuluk, evlerin karşı karşıya oluşu ve dağın yolcuya karşı çıkışı gibi verilen yapılara bağlıdır; yalın kök anlamı olarak genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; karşılıklı görünürlük ile genel karşıya dönüklük sınırlarını açıklayan iki komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Karşılıklı görünürlük iki dalın güçlü ortak alanıdır; odak dal buna komşuluk ve yolcunun karşısına çıkan dağ gibi tek yönlü yapıları da ekler.","focus_only":"Odak dal, görünür komşuluğu ve dağın yolcuya tek yönlü olarak karşı çıkmasını da içerir.","gloss":"karşılıklı görünme ve karşılaşma","neighbor_only":"Komşu dal, toplulukların, konutların veya ateşlerin karşılıklı olarak birbirine görünmesini özellikle öne çıkarır.","neighbor_ref":"root_000531/B004","relation_type":"near_synonym","shared_zone":"İki dalda da yerlerin veya toplulukların karşı karşıya bulunup birbirini görebilmesi vardır."},{"boundary_match":"partial","distinction":"Komşu dal genel karşıya dönüklüğü anlatır; odak dal ise belirli yapılarda görüş doğrultusuna ve görünür komşuluğa bağlıdır.","focus_only":"Odak dal, verilen söz yapılarında birbirini görebilme koşulunu ve belirli yer örneklerini korur.","gloss":"karşı karşıya gelme","neighbor_only":"Komşu dal, yüz, yön, ön ve karşılık dahil daha genel bir karşılaşma ve karşıya dönüklük alanına yayılır.","neighbor_ref":"root_001198/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin başka bir şeyin karşısında bulunmasını anlatır."}],"source_phrase_ar":"حي حلال نظر متجاورون ينظر بعضهم إلى بعض (maqayis)؛ حي حلال ونظر أي متجاورون يرى بعضهم بعضا؛ داري تنظر إلى دار فلان؛ دورنا تناظر أي تقابل؛ فنظر إليك الجبل (sihah)؛ داري تنظر إلى دار فلان ودورنا تناظر إذا كانت متحاذية (tahdhib)؛ حي نظر أي متجاورون يرى بعضهم بعضا (mufradat)","source_summary":"Kaynaklar görünür komşuluk, evlerin karşılıklı hizası ve yolcunun karşısına çıkan dağ örneklerini verir. Ortak öğe, tarafların aynı görüş doğrultusunda mekansal olarak karşılaşmasıdır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الحي المتجاور الذي يرى بعضه بعضا، والدور المتحاذية أو المتناظرة، وما يقال في الطريق إذا قابل الجبل السالك.","what_is_not_ar":"لا يدخل فيه مجرد المماثلة من غير تقابل مكاني، ولا الانتظار الزمني."},"support_links":[]},{"boundary":"Dış görünüş ve onun değerlendirilmesi çekirdektir; toprağın bitkisini göstermesi yalnızca verilen yapıda geçerli bir görünür kılma uzantısıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001520/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَنتَظِرُ","morph_features":"STEM|POS:V|IMPV|(VIII)|LEM:yantaZiru|ROOT:nZr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:3:2","qac_word_ref":"32:30:3","surface_ar":"ٱنتَظِرْ"},{"lemma_ar":"مُنتَظِرُون","morph_features":"STEM|POS:N|ACT|PCPL|(VIII)|LEM:muntaZiruwn|ROOT:nZr|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"32:30:5:1","qac_word_ref":"32:30:5","surface_ar":"مُّنتَظِرُونَ"}],"gloss":"bakıldığında görülen dış görünüş","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin bakana görünen dış durumu veya biçimi söz konusudur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Görünen durum hoş, güzel, kötü veya aldatıcı bulunabilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Toprağın bitkisini ortaya çıkarıp görünür kılması, verilen söz yapısında görünüş alanına uzanır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bakılması ve dinlenmesi sevilen bir durumda bulunma, görünüş değerlendirmesini başka bir algı alanıyla birleştirir."}}],"root_ar":"ن ظ ر","root_id":"root_001520","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi veya şeyin dışarıdan görülen durumunu, olumlu ya da olumsuz değerlendirmeden bağımsız olarak anlatır.","boundary_detail":"Dış görünüş ve onun değerlendirilmesi çekirdektir; toprağın bitkisini göstermesi yalnızca verilen yapıda geçerli bir görünür kılma uzantısıdır.","branch_image_ar":"ظهور الشيء للناظر أو حسن مرآه","concept_gloss":"bakıldığında görülen dış görünüş","contextual_glosses":[{"applicability":"Bir kişinin veya şeyin bakıldığında hoş bulunduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dış görünüşün görülmesi ve olumlu değerlendirilmesi özelliklerini korur."},"facet_ids":["F001","F002"],"text":"görünüşü güzel olmak","usage_role":"contextual"},{"applicability":"Yalnızca toprağın bitkisini görünür duruma getirdiği yapı için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Toprağın bitkisini ortaya çıkarıp görünür kılması özelliğini korur."},"facet_ids":["F003"],"text":"bitkisini gösterip ortaya çıkarmak","usage_role":"contextual"}],"definition":"Bir kişi ya da şeyin bakıldığında görülen dış durumu ve bunun hoş ya da kötü bulunabilen görünüşü; toprağın bitkisini ortaya çıkarması bu çekirdeğe bağlı, yapısal bir görünür kılma uzantısıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin bakana görünen dış durumu veya biçimi söz konusudur."},{"facet_id":"F002","role":"specialization","statement":"Görünen durum hoş, güzel, kötü veya aldatıcı bulunabilir."},{"facet_id":"F003","role":"extension","statement":"Toprağın bitkisini ortaya çıkarıp görünür kılması, verilen söz yapısında görünüş alanına uzanır."},{"facet_id":"F004","role":"associated_use","statement":"Bakılması ve dinlenmesi sevilen bir durumda bulunma, görünüş değerlendirmesini başka bir algı alanıyla birleştirir."}],"identity_rationale":"Kaynak ifadesi bir kişinin veya şeyin bakıldığında görülen dış görünüşünü ve bu görünüşün hoş ya da kötü bulunmasını açıkça destekler. Toprağın bitkisini göstermesi ise görünür duruma gelme ilişkisine dayanan ayrı, yapıya bağlı bir uzantıdır ve görünüş çekirdeğiyle eşitlenmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"toprak bitkisini gösterdi"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"bakıldığında görülen dış görünüş"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"güzel dış görünüş"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bakılması ve dinlenmesi hoş bir durumda"}],"lexicalization_note":"Yalın görünüş adları ile toprağın bitkisini göstermesi ve bakılıp dinlenesi durum yapıları ayrılır; yapıya bağlı uzantılar genel görünüş anlamına karıştırılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel dış durum ile özellikle güzel görünüş arasındaki iki yararlı sınır seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bakışla algılanan görünüşe ve onun değerlendirilmesine bağlıdır; komşu dal ise görünürlük şartı olmadan genel durum ve biçimi de kapsar.","focus_only":"Odak dal, dış görünüşün hoş veya kötü bulunmasını ve toprağın bitkisini göstermesi uzantısını içerir.","gloss":"dış durum ve biçim","neighbor_only":"Komşu dal, giyim dahil bir şeyin içinde bulunduğu genel durum ve biçime daha geniş ölçüde uzanır.","neighbor_ref":"root_001610/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişi veya şeyin dışarıdan görülen durumunu anlatabilir."},{"boundary_match":"partial","distinction":"Komşu dal olumlu güzellik niteliğine bağlıdır; odak dal ise görünüşü olumlu veya olumsuz değerlendirmeye açık tutar ve ayrıca yapısal bir görünür kılma uzantısı taşır.","focus_only":"Odak dal kötü ya da aldatıcı görünüşü ve toprağın bitkisini göstermesi uzantısını da kapsar.","gloss":"güzel dış görünüş","neighbor_only":"Komşu dal dış görünüşü özellikle güzellik ve canlılık niteliğiyle sınırlar.","neighbor_ref":"root_000615/B009","relation_type":"near_synonym","shared_zone":"İki dalın ortak alanı, bakıldığında hoş bulunan dış görünüştür."}],"source_phrase_ar":"نظرت الأرض أرت نباتها (maqayis)؛ منظره خير من مخبره؛ حسنة المنظر والمنظرة (sihah)؛ المنظرة منظر الرجل إذا نظرت إليه فأعجبك أو ساءك؛ ذو منظرة بلا مخبرة؛ المنظر الشيء الذي يعجب الناظر إذا نظر إليه فسره؛ في منظر ومستمع (tahdhib)","source_summary":"Kaynaklar bakıldığında görülen dış durumu, bu durumun güzel veya kötü bulunmasını ve görünüş ile iç gerçekliğin karşılaştırılmasını aktarır. Toprağın bitkisini göstermesi ile bakılıp dinlenesi durum ise yapıya bağlı ayrı uzantılardır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه المنظر والمنظرة بمعنى المرأى أو الهيئة التي تعجب أو تسوء، وحسن المنظر، وإبداء الأرض نباتها.","what_is_not_ar":"لا يدخل فيه الرقيب والحارس في المنظرة، ولا النظير بمعنى المثل."},"support_links":[]},{"boundary":"Dal yalnızca zamanın kişileştirilerek bir topluluğu vurup yok ettiği verilen söz yapısına bağlıdır; genel bakma veya genel yok oluş anlamı değildir.","branch_kind":"collocation","branch_ref":"root_001520/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَنتَظِرُ","morph_features":"STEM|POS:V|IMPV|(VIII)|LEM:yantaZiru|ROOT:nZr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:3:2","qac_word_ref":"32:30:3","surface_ar":"ٱنتَظِرْ"},{"lemma_ar":"مُنتَظِرُون","morph_features":"STEM|POS:N|ACT|PCPL|(VIII)|LEM:muntaZiruwn|ROOT:nZr|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"32:30:5:1","qac_word_ref":"32:30:5","surface_ar":"مُّنتَظِرُونَ"}],"gloss":"zamanın vurup yok etmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Zaman, iradeli bir fail gibi bir topluluğa yönelmiş olarak anlatılır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu kişileştirilmiş yönelişin sonucu topluluğun aldatılması, yıkıma uğraması veya yok olmasıdır."}}],"root_ar":"ن ظ ر","root_id":"root_001520","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca zamanın kişileştirilmiş yıkıcı fail olduğu kalıplaşmış anlatım için kullanılır.","boundary_detail":"Dal yalnızca zamanın kişileştirilerek bir topluluğu vurup yok ettiği verilen söz yapısına bağlıdır; genel bakma veya genel yok oluş anlamı değildir.","branch_image_ar":"نظرة الدهر التي تصيب بالهلاك","concept_gloss":"zamanın vurup yok etmesi","contextual_glosses":[{"applicability":"Kalıplaşmış mecazın doğal bir cümle içinde açıklandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişileştirilmiş zamanı, kötülüğü ve yok oluş sonucunu korur."},"facet_ids":["F001","F002"],"text":"zaman onları aldattı ve yok etti","usage_role":"explanatory"}],"definition":"Zamanın bir topluluğa yönelmiş ve ona kötülük etmiş gibi kişileştirildiği söz yapısında, o topluluğu aldatıp yıkıma uğratması veya yok etmesi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Zaman, iradeli bir fail gibi bir topluluğa yönelmiş olarak anlatılır."},{"facet_id":"F002","role":"core","statement":"Bu kişileştirilmiş yönelişin sonucu topluluğun aldatılması, yıkıma uğraması veya yok olmasıdır."}],"identity_rationale":"Kaynak ifadesi, zamanın bir topluluğa yönelmiş gibi anlatıldığı ve bu yönelişin onları aldatıp yok etmesiyle sonuçlandığı kalıplaşmış mecazı açıkça destekler. Yok oluş genel bir kök anlamı değil, bu kişileştirilmiş zaman yapısının kurucu sonucudur.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"zaman onları vurup yok etti"}],"lexicalization_note":"Tanım yalnızca zamanın bir topluluğa yönelip onu yok etmesi biçimindeki verilen yapıyı karşılar; yalın bir bakma ya da yok etme anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; doğrudan yok oluş ile zamanın kötülüğe hazırlanması arasındaki iki açıklayıcı ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Komşu dal yok oluşu doğrudan belirtir; odak dal ise aynı sonucu ancak zamanın yönelip kötülük etmesi biçimindeki kişileştirilmiş yapıyla anlatır.","focus_only":"Odak dal, zamanı kişileştirilmiş yıkıcı fail yapan belirli bir söz yapısına bağlıdır.","gloss":"yok oluşun gelip çatması","neighbor_only":"Komşu dal, ölümün veya yıkıcı olayın gelip çatmasını doğrudan adlandırır.","neighbor_ref":"root_000382/B002","relation_type":"same_field","shared_zone":"Her iki dal da bir kişi veya topluluğun yok oluşuyla sonuçlanan olayı anlatır."},{"boundary_match":"thematic_only","distinction":"Odak dal gerçekleşmiş yıkıcı etkiyi anlatır; komşu dal ise kötü sonucun hazırlanmasını veya yaklaşmasını anlatır ve yok oluşu zorunlu kılmaz.","focus_only":"Odak dalda yıkım gerçekleşir ve zaman bu sonucun etkin faili gibi gösterilir.","gloss":"kötü olayı hazırlayan zaman","neighbor_only":"Komşu dalda zaman veya başka bir unsur, henüz ortaya çıkacak kötü olaya gebe ya da hazır olarak anlatılır.","neighbor_ref":"root_001406/B006","relation_type":"thematic","shared_zone":"İki dal da zamanı yaklaşan veya gerçekleşen kötülükle ilişkilendiren kişileştirilmiş anlatımlar kullanır."}],"source_phrase_ar":"نظر الدهر إلى بني فلان فأهلكهم (maqayis;sihah)؛ نظر الدهر إليهم فابتهل؛ خانهم فأهلكهم (mufradat)","source_summary":"Kaynaklar zamanın bir topluluğa bakmış gibi kişileştirildiği ve ardından onu aldatarak ya da vurarak yok ettiği kalıplaşmış anlatımda birleşir. Zamanın yıkıcı fail oluşu bu yapının temel koşuludur.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه التعبير المجازي أن الدهر نظر إلى قوم فأهلكهم أو خانهم.","what_is_not_ar":"لا يدخل فيه نظر الله بالإحسان، ولا إصابة العين من الجن."},"support_links":[]},{"boundary":"Dal eş veya denk karşılık olmayı anlatır; yalnızca mekansal karşı karşıya bulunma ya da karşılıklı tartışma bu anlama girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001520/B006","candidate_links":[{"candidate_id":"cand_94530876ad2ad92c9d15","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَنتَظِرُ","morph_features":"STEM|POS:V|IMPV|(VIII)|LEM:yantaZiru|ROOT:nZr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:3:2","qac_word_ref":"32:30:3","surface_ar":"ٱنتَظِرْ"},{"lemma_ar":"مُنتَظِرُون","morph_features":"STEM|POS:N|ACT|PCPL|(VIII)|LEM:muntaZiruwn|ROOT:nZr|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"32:30:5:1","qac_word_ref":"32:30:5","surface_ar":"مُّنتَظِرُونَ"}],"gloss":"eş veya denk karşılık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki şey karşılaştırıldığında benzerlik, eşlik veya denklik bakımından birbirine karşılık gelir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birden çok öğe ortak özellikleri nedeniyle birbirinin benzeri olarak sınıflandırılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli bir yasak yapısında herhangi bir şeyi başka bir şeye denk tutma eylemi reddedilir."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Hayvanların ikişer ikişer sayılması, öğelerin eşler halinde düzenlenmesi örneğidir."}}],"root_ar":"ن ظ ر","root_id":"root_001520","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki şeyin benzerlik veya denklik bakımından birbirine karşılık geldiği genel bağlamlarda kullanılır.","boundary_detail":"Dal eş veya denk karşılık olmayı anlatır; yalnızca mekansal karşı karşıya bulunma ya da karşılıklı tartışma bu anlama girmez.","branch_image_ar":"مقابلة المثل بمثله حتى يستويان","concept_gloss":"eş veya denk karşılık","contextual_glosses":[{"applicability":"İki kişi veya şeyin eşit birer karşılık sayıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı eşlik ve denklik özelliklerini korur."},"facet_ids":["F001"],"text":"birbirine denk olmak","usage_role":"general"},{"applicability":"Hayvanların ikişer ikişer düzenlenerek sayıldığı özel örnekte kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öğeleri eşler halinde düzenleme ve sayma özelliklerini korur."},"facet_ids":["F004"],"text":"ikişerli eşler halinde saymak","usage_role":"contextual"}],"definition":"Bir şeyin başka bir şeyle karşılaştırıldığında ona benzer, eş veya denk bir karşılık oluşturması; bazı yapılarda böyle bir denkliğin reddedilmesi ya da öğelerin ikişerli eşler halinde sayılması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki şey karşılaştırıldığında benzerlik, eşlik veya denklik bakımından birbirine karşılık gelir."},{"facet_id":"F002","role":"specialization","statement":"Birden çok öğe ortak özellikleri nedeniyle birbirinin benzeri olarak sınıflandırılır."},{"facet_id":"F003","role":"associated_use","statement":"Belirli bir yasak yapısında herhangi bir şeyi başka bir şeye denk tutma eylemi reddedilir."},{"facet_id":"F004","role":"example","statement":"Hayvanların ikişer ikişer sayılması, öğelerin eşler halinde düzenlenmesi örneğidir."}],"identity_rationale":"Kaynak ifadesi bir şeyin başka bir şeyle karşılaştırıldığında ona eş, denk veya benzer bir karşılık olmasını tutarlı biçimde destekler. Çoğul benzerler ve ikişerli sayılan hayvanlar bu eşleştirme çekirdeğinin özel kullanımlarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"eş, benzer veya denk karşılık"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"birbirine benzeyen eşler"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"Tanrı'nın kitabına hiçbir şeyi denk tutma"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"ikişer ikişer sayılan develer"}],"lexicalization_note":"Yalın eş ve denk adları ile hiçbir şeyi bir şeye denk tutmama ve ikişerli sayma yapıları ayrı tutulur; özel yapılar bütün dala genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel benzerlik ile karşılıklı denklik sınırlarını en iyi gösteren iki komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda karşılık oluşturan eş ya da denk öğe öne çıkar; komşu dal ise daha genel benzerlik, benzetme ve eşitleme alanını kapsar.","focus_only":"Odak dal, öğeleri karşılıklı eşler olarak düzenleme ve bir şeyi denk tutmayı reddetme yapılarını da içerir.","gloss":"genel benzerlik ve eşlik","neighbor_only":"Komşu dal, genel benzetme ve benzer kılma işlemlerine daha geniş biçimde uzanır.","neighbor_ref":"root_001397/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da iki şeyin birbirine benzer veya denk sayılmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği benzer veya eş karşılıktır; komşu dal bu çekirdeği karşılıklı eylem, karşılık verme ve özel yeterlik alanlarına taşır.","focus_only":"Odak dal, çoğul benzerleri ve öğelerin ikişerli eşler halinde sayılmasını kapsar.","gloss":"eşit ve karşılık olan denk","neighbor_only":"Komşu dal, evlilik ve savaş denkliğini, karşılık vermeyi ve yapılanın benzerini yapmayı da kapsar.","neighbor_ref":"root_001305/B001","relation_type":"near_synonym","shared_zone":"İki dalda da bir kişinin veya şeyin başka birine eş ve denk olması bulunur."}],"source_phrase_ar":"هذا نظير هذا؛ إذا نظر إليه وإلى نظيره كانا سواء (maqayis)؛ نظير الشئ مثله؛ النظر والنظير بمعنى واحد مثل الند والنديد؛ نظائر (sihah)؛ فلان نظيرك أي مثلك؛ النظائر لاشتباه بعضها ببعض؛ لا تجعل شيئا نظيرا (tahdhib)؛ النظير المثيل وأصله المناظر (mufradat)","source_summary":"Kaynaklar eş, benzer ve denk karşılık anlamında birleşir; birden çok benzer öğenin aynı grupta toplanması da bu çekirdeğe bağlıdır. Denk tutmayı yasaklayan yapı ile ikişerli sayma örneği ayrı kullanım sınırlarını korur.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه النظير بمعنى المثل والند، والنظائر لاشتباه الأشياء، وما يجعل نظيرا لشيء آخر.","what_is_not_ar":"لا يدخل فيه المجاورة المكانية وحدها، ولا المناظرة الجدلية إلا إذا أريد المشابهة."},"support_links":["sup_9e7f9d45e9ed77136555"]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001520/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَنتَظِرُ","morph_features":"STEM|POS:V|IMPV|(VIII)|LEM:yantaZiru|ROOT:nZr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:3:2","qac_word_ref":"32:30:3","surface_ar":"ٱنتَظِرْ"},{"lemma_ar":"مُنتَظِرُون","morph_features":"STEM|POS:N|ACT|PCPL|(VIII)|LEM:muntaZiruwn|ROOT:nZr|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"32:30:5:1","qac_word_ref":"32:30:5","surface_ar":"مُّنتَظِرُونَ"}],"gloss":"özel adlandırma kümesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kullanım, kısa ve hızlı bir bakışı adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başka bir kullanım, bakışla ilişkilendirilen heybeti adlandırır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir yapı kişideki solgunluğu, çirkinliği veya başka bir görünür kusuru bildirir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Başka bir yapı, görünmeyen varlıkların kem gözünden geldiği düşünülen zararı bildirir."}}],"root_ar":"ن ظ ر","root_id":"root_001520","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"أثر النظرة في اللون والعيب","concept_gloss":"özel adlandırma kümesi","contextual_glosses":[{"applicability":"Yalnızca kısa süren ve aceleyle yapılan bakış kullanımında geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bakışın kısa ve hızlı oluşunu korur."},"facet_ids":["F001"],"text":"hızlı bir bakış","usage_role":"contextual"},{"applicability":"Bir kişide renk solması, çirkinlik ya da başka bir görünür kusur bildirildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bedendeki görünür değişim ve kusur anlamını korur."},"facet_ids":["F003"],"text":"solgunluk veya görünür kusur","usage_role":"contextual"}],"definition":"Bu dal tek bir kavram tanımlamaz: hızlı bakış, bakıştan doğan heybet, bedendeki solgunluk veya kusur ve kem gözden etkilenme ayrı anlamlar olarak ayrıştırılmalıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kullanım, kısa ve hızlı bir bakışı adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Başka bir kullanım, bakışla ilişkilendirilen heybeti adlandırır."},{"facet_id":"F003","role":"source_variant","statement":"Bir yapı kişideki solgunluğu, çirkinliği veya başka bir görünür kusuru bildirir."},{"facet_id":"F004","role":"source_variant","statement":"Başka bir yapı, görünmeyen varlıkların kem gözünden geldiği düşünülen zararı bildirir."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"hızlı bir bakış"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"bakıştan doğan heybet"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"onda solgunluk, çirkinlik veya kusur var"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"görünmeyen varlıkların kem gözünden etkilenmiş"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"kem gözden zarar görmüş kişi"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"به نظرة أي شحوب (maqayis)؛ النظرة عين الجن؛ رجل فيه نظرة أي شحوب (sihah)؛ النظرة اللمحة بالعجلة؛ النظرة الهيبة؛ فيه نظرة أي شحوب؛ النظرة الشنعة والقبح؛ فيه نظرة أي قبح؛ بها إصابة عين من نظر الجن (tahdhib)؛ به نظرة؛ من أعين الجن نظرة (mufradat)","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه النظرة كاللمحة بالعجلة، وبه نظرة أي شحوب، وإصابة عين من الجن، والقبح أو العيب، والهيبة حيث صرحت بها المصادر.","what_is_not_ar":"لا يدخل فيه النظرة بمعنى التأخير أو الرحمة، ولا الناظر عضو العين."},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"bare","branch_ref":"root_001520/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَنتَظِرُ","morph_features":"STEM|POS:V|IMPV|(VIII)|LEM:yantaZiru|ROOT:nZr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:3:2","qac_word_ref":"32:30:3","surface_ar":"ٱنتَظِرْ"},{"lemma_ar":"مُنتَظِرُون","morph_features":"STEM|POS:N|ACT|PCPL|(VIII)|LEM:muntaZiruwn|ROOT:nZr|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"32:30:5:1","qac_word_ref":"32:30:5","surface_ar":"مُّنتَظِرُونَ"}],"gloss":"biçime bağlı adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir biçim gözün içindeki küçük siyah bölümü veya göz bebeğini adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir biçim doğrudan gözün kendisini adlandırır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İkili biçim, burnun iki yanında gözyaşı yolunda bulunan iki damarı adlandırır."}}],"root_ar":"ن ظ ر","root_id":"root_001520","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"العين وموضع النظر فيها","concept_gloss":"biçime bağlı adlandırmalar","contextual_glosses":[{"applicability":"Göz içindeki küçük siyah alan veya saydam merkez adlandırıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Göz içindeki küçük siyah bölüm referentini korur."},"facet_ids":["F001"],"text":"göz bebeği","usage_role":"contextual"},{"applicability":"Burnun iki yanında gözyaşı akış yolu boyunca bulunan damar çifti için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Damarların ikili oluşunu ve gözyaşı yolundaki konumunu korur."},"facet_ids":["F003"],"text":"gözyaşı yolundaki iki damar","usage_role":"contextual"}],"definition":"Bu dal tek bir anatomik referent tanımlamaz: gözün içindeki küçük siyah bölüm, gözün bütünü ve gözyaşı yolundaki iki damar ayrı adlandırmalar olarak ayrılmalıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir biçim gözün içindeki küçük siyah bölümü veya göz bebeğini adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Bir biçim doğrudan gözün kendisini adlandırır."},{"facet_id":"F003","role":"source_variant","statement":"İkili biçim, burnun iki yanında gözyaşı yolunda bulunan iki damarı adlandırır."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"göz bebeği veya gözdeki küçük siyah bölüm"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"göz"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"gözyaşı yolunda burnun iki yanındaki damarlar"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"الناظر في المقلة السواد الأصغر؛ يقال للعين الناظرة؛ الناظران عرقان في مجرى الدمع على الأنف من جانبيه (sihah)؛ ناظر العين النقطة السوداء الصافية؛ الناظر في العين كالمرآة؛ الناظران عرقان مكتنفا الأنف؛ هما عرقان في مجرى الدمع (tahdhib)","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الناظر في المقلة، سواد العين أو النقطة السوداء، وإطلاق الناظرة على العين، والناظران عرقان في مجرى الدمع.","what_is_not_ar":"لا يدخل فيه النظر كفعل إدراك، ولا النظرة كأثر عين أو شحوب."},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001520/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَنتَظِرُ","morph_features":"STEM|POS:V|IMPV|(VIII)|LEM:yantaZiru|ROOT:nZr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:3:2","qac_word_ref":"32:30:3","surface_ar":"ٱنتَظِرْ"},{"lemma_ar":"مُنتَظِرُون","morph_features":"STEM|POS:N|ACT|PCPL|(VIII)|LEM:muntaZiruwn|ROOT:nZr|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"32:30:5:1","qac_word_ref":"32:30:5","surface_ar":"مُّنتَظِرُونَ"}],"gloss":"biçime bağlı adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kullanım bağı, yeri veya topluluğu gözetip koruyan görevliyi adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kullanım bir topluluğun durumunu incelemek üzere gönderilen güvenilir görevliyi adlandırır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kullanım düşmanı gözeten bekçinin bulunduğu yüksek gözetleme yerini adlandırır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir söz yapısı kuşku altında olmayan kişinin gözünü kaçırmadan bakmasını bildirir."}}],"root_ar":"ن ظ ر","root_id":"root_001520","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"حارس ينظر ويحفظ","concept_gloss":"biçime bağlı adlandırmalar","contextual_glosses":[{"applicability":"Bir bağı gözetip koruyan görevli adlandırıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Korunan yeri ve bekçilik görevini korur."},"facet_ids":["F001"],"text":"bağ bekçisi","usage_role":"contextual"},{"applicability":"Düşmanı gözeten bekçinin bulunduğu dağ başı veya benzeri yüksek yer için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gözetleme işlevini, yeri ve yüksek konumu korur."},"facet_ids":["F003"],"text":"yüksek gözetleme yeri","usage_role":"contextual"}],"definition":"Bu dal tek bir kavram tanımlamaz: koruyan veya inceleme yapan görevli, düşmanı gözleyen yer ve suçsuz kişinin bakışını anlatan kalıp ayrı anlamlar olarak ayrıştırılmalıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kullanım bağı, yeri veya topluluğu gözetip koruyan görevliyi adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Bir kullanım bir topluluğun durumunu incelemek üzere gönderilen güvenilir görevliyi adlandırır."},{"facet_id":"F003","role":"source_variant","statement":"Bir kullanım düşmanı gözeten bekçinin bulunduğu yüksek gözetleme yerini adlandırır."},{"facet_id":"F004","role":"source_variant","statement":"Bir söz yapısı kuşku altında olmayan kişinin gözünü kaçırmadan bakmasını bildirir."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"bağ bekçisi"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"koruyucu veya inceleme için gönderilen görevli"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"yüksek gözetleme yeri"},{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"suçsuzluğundan gözünü kaçırmadan bakan"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"الناطر والناطور حافظ الكرم؛ الناظر الحافظ؛ المنظرة المرقبة (sihah)؛ المنظرة موضع في رأس جبل فيه رقيب ينظر العدو ويحرسه؛ شديد الناظر إذا كان بريئا من التهمة؛ بعث ناظرا (tahdhib)","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الناظر والناطور حافظ الكرم، والرقيب في المنظرة، والأمين المبعوث ليستبرئ أمر جماعة، ومن ينظر بملء عينيه بريئا من التهمة.","what_is_not_ar":"لا يدخل فيه المنظر بمعنى الهيئة المرئية، ولا النظير بمعنى المثل."},"support_links":[]},{"boundary":"Karşılıklı inceleme ve tartışma çekirdektir; tek kişilik araştırma yalnızca ayrı bir kaynak uzantısı olarak korunmalıdır.","branch_kind":"bare","branch_ref":"root_001520/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَنتَظِرُ","morph_features":"STEM|POS:V|IMPV|(VIII)|LEM:yantaZiru|ROOT:nZr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:3:2","qac_word_ref":"32:30:3","surface_ar":"ٱنتَظِرْ"},{"lemma_ar":"مُنتَظِرُون","morph_features":"STEM|POS:N|ACT|PCPL|(VIII)|LEM:muntaZiruwn|ROOT:nZr|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"32:30:5:1","qac_word_ref":"32:30:5","surface_ar":"مُّنتَظِرُونَ"}],"gloss":"karşılıklı tartışıp inceleme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"En az iki kişi aynı konuyu birlikte ele alır ve görüşlerini karşılıklı olarak sunar."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Taraflar konunun nasıl anlaşılacağını veya nasıl yürütüleceğini araştırıp tartışır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Daha genel kullanımda araştırma ve kanıta dayalı düşünme, karşılıklı tartışma şartı olmadan da adlandırılır."}}],"root_ar":"ن ظ ر","root_id":"root_001520","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki tarafın aynı konuyu görüşlerini karşılaştırarak birlikte araştırdığı durumlarda kullanılır.","boundary_detail":"Karşılıklı inceleme ve tartışma çekirdektir; tek kişilik araştırma yalnızca ayrı bir kaynak uzantısı olarak korunmalıdır.","branch_image_ar":"تدارس الأمر بالنظر المتبادل","concept_gloss":"karşılıklı tartışıp inceleme","contextual_glosses":[{"applicability":"İki kişinin görüşlerini ortaya koyup aynı konuyu birlikte incelediği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki tarafı, ortak konuyu ve karşılıklı görüş alışverişini korur."},"facet_ids":["F001","F002"],"text":"bir konuyu karşılıklı tartışmak","usage_role":"general"},{"applicability":"Karşılıklı tartışma şartı olmadan düşünsel araştırma ve çıkarım öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Araştırma ve kanıta dayalı düşünme uzantısını korur."},"facet_ids":["F003"],"text":"kanıtlara dayanarak araştırmak","usage_role":"contextual"}],"definition":"İki kişinin bir konuyu nasıl ele alacaklarını birlikte inceleyip kendi görüşlerini karşılıklı olarak ortaya koyması ve tartışması; daha genel araştırma ve kanıta dayalı inceleme bununla ilişkili fakat tek katılımcılı da olabilen bir uzantıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"En az iki kişi aynı konuyu birlikte ele alır ve görüşlerini karşılıklı olarak sunar."},{"facet_id":"F002","role":"core","statement":"Taraflar konunun nasıl anlaşılacağını veya nasıl yürütüleceğini araştırıp tartışır."},{"facet_id":"F003","role":"extension","statement":"Daha genel kullanımda araştırma ve kanıta dayalı düşünme, karşılıklı tartışma şartı olmadan da adlandırılır."}],"identity_rationale":"Kaynak ifadesi iki kişinin bir konuyu birlikte incelemesini, görüşlerini ortaya koymasını ve karşılıklı tartışmasını açıkça destekler. Aynı iddiadaki tek kişilik araştırma ve kanıta dayalı inceleme daha geniş bir alanı gösterir; karşılıklı görüşme çekirdeğiyle ancak ayrı bir kapsam olarak birlikte tutulabilir.","lexical_glosses":[{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"karşılıklı tartışıp inceleme"},{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"araştırma ve kanıta dayalı inceleme"}],"lexicalization_note":"Mekanik yalın kapsam korunur; karşılıklı tartışma ile daha genel araştırma biçimleri tanımda ayrı katılımcı yapıları olarak gösterilir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bilgi amaçlı görüşme ile sert çekişme sınırlarını açıklayan iki ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal öğrenme ve belirli bir bilgi alanında uzmanlaşma amacına bağlıdır; odak dal ise herhangi bir konu üzerinde karşılıklı inceleme ve tartışmayı anlatır.","focus_only":"Odak dal, konusu sınırlanmamış karşılıklı inceleme ve görüş yarışını kapsar.","gloss":"öğrenmek için bilimsel görüşme","neighbor_only":"Komşu dal, öğrenme amacıyla belirli bir hukuk bilgisi alanında uzmanlaşma ve bilginle görüşme sınırı taşır.","neighbor_ref":"root_001171/B004","relation_type":"near_neighbor","shared_zone":"İki dalda da bir bilgi konusu üzerinde karşılıklı konuşma ve araştırma bulunabilir."},{"boundary_match":"partial","distinction":"Odak dalın kurucu öğesi karşılıklı incelemedir ve çekişme zorunlu değildir; komşu dal ise sert karşı çıkış ve ağız kavgası niteliğine daha yakındır.","focus_only":"Odak dal nötr araştırma, birlikte çözüm arama ve görüşleri sakin biçimde karşılaştırma olanağı taşır.","gloss":"sert ve çekişmeli tartışma","neighbor_only":"Komşu dal sert söz, çekişme, kuşku ve karşı tarafı sıkıştırma özelliklerini öne çıkarır.","neighbor_ref":"root_001416/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da tarafların farklı görüşleri sözle karşı karşıya getirmesi vardır."}],"source_phrase_ar":"ناظره من المناظرة (sihah)؛ المناظرة أن تناظر أخاك في أمر إذا نظرتما فيه معا كيف تأتيانه؛ نظيرك أيضا الذي يناظرك وتناظره (tahdhib)؛ المناظرة المباحثة والمباراة في النظر واستحضار كل ما يراه ببصيرته؛ النظر البحث (mufradat)","source_summary":"Kaynaklar karşılıklı inceleme, görüşleri ortaya koyma ve bir konu üzerinde tartışma özelliklerinde birleşir. Tek kişilik araştırmayı da kapsayabilen daha geniş inceleme kullanımı, karşılıklı katılım şartından ayrı tutulmalıdır.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه ناظره والمناظرة، وأن ينظر اثنان في أمر كيف يأتيانه، والمباحثة والمباراة في النظر.","what_is_not_ar":"لا يدخل فيه النظير إذا أريد به مجرد المثل، ولا النظر الفردي بلا مباحثة."},"support_links":[]},{"boundary":"Merhamet genel addır; Tanrı'nın kullarına yönelişi yalnızca verilen yapıda iyilik ve bolluk sağlama olarak anlaşılır.","branch_kind":"mixed_non_bare","branch_ref":"root_001520/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَنتَظِرُ","morph_features":"STEM|POS:V|IMPV|(VIII)|LEM:yantaZiru|ROOT:nZr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:3:2","qac_word_ref":"32:30:3","surface_ar":"ٱنتَظِرْ"},{"lemma_ar":"مُنتَظِرُون","morph_features":"STEM|POS:N|ACT|PCPL|(VIII)|LEM:muntaZiruwn|ROOT:nZr|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"32:30:5:1","qac_word_ref":"32:30:5","surface_ar":"مُّنتَظِرُونَ"}],"gloss":"merhametle iyilik yöneltme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yönelişin alıcısı esirgeme ve iyilik görür."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Genel ad olarak merhamet ve acıyarak esirgeme anlamı taşır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tanrı öznesiyle kurulan yapıda kullara iyilik etme ve iyilikleri bolca verme anlamı taşır."}}],"root_ar":"ن ظ ر","root_id":"root_001520","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Esirgeme ile iyilik sağlamayı birlikte anlatan genel açıklamalarda kullanılır.","boundary_detail":"Merhamet genel addır; Tanrı'nın kullarına yönelişi yalnızca verilen yapıda iyilik ve bolluk sağlama olarak anlaşılır.","branch_image_ar":"نظر الإحسان وإفاضة النعمة","concept_gloss":"merhametle iyilik yöneltme","contextual_glosses":[{"applicability":"Bir kişiyi acıyarak esirgeme ve ona yumuşak davranma anlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Esirgeme ve yararlı yöneliş özelliklerini korur."},"facet_ids":["F001","F002"],"text":"merhamet etmek","usage_role":"general"},{"applicability":"Tanrı'nın kullarına yönelişini açıklayan özel yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kutsal özneyi, kulları ve iyiliğin bolca verilmesini korur."},"facet_ids":["F001","F003"],"text":"iyilik edip bolca vermek","usage_role":"explanatory"}],"definition":"Birine merhamet edip iyilik yöneltme; Tanrı'nın kullarına yönelmesi biçimindeki özel yapıda bu, onlara iyilik etmesi ve iyiliklerini bolca vermesi demektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yönelişin alıcısı esirgeme ve iyilik görür."},{"facet_id":"F002","role":"specialization","statement":"Genel ad olarak merhamet ve acıyarak esirgeme anlamı taşır."},{"facet_id":"F003","role":"specialization","statement":"Tanrı öznesiyle kurulan yapıda kullara iyilik etme ve iyilikleri bolca verme anlamı taşır."}],"identity_rationale":"Kaynak ifadesi bir yandan merhamet adını, öte yandan Tanrı'nın kullarına yönelişini onlara iyilik etmesi ve iyiliklerini bolca vermesi olarak açıklar. İki kullanım da zarar değil esirgeme ve iyilik sağlama sonucunda birleşir; kutsal özneye bağlı yapı kendi sınırında tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_041","rendering_kind":"ordinary","target_gloss":"merhamet"},{"lexical_unit_id":"lu_042","rendering_kind":"ordinary","target_gloss":"Tanrı kullarına iyilik etti ve iyiliklerini bolca verdi"}],"lexicalization_note":"Yalın merhamet adı ile Tanrı'nın kullarına iyilik etmesini bildiren yapı ayrı tutulur; kutsal özneye bağlı anlatım bütün kullanımlara yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dış adaylar anlam sınırını keskinleştirmediği için yalnızca aynı kökteki yıkıcı yöneliş karşıtı yayımlandı.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dalın sonucu esirgeme ve iyiliktir; komşu dalın sonucu aldatma ve yok oluştur. Ortak yöneliş yapısı karşıt değerli sonuçlarla ayrılır.","focus_only":"Odak dalda üstün güçten alıcıya merhamet, iyilik ve bolluk yönelir.","gloss":"yararlı ve yıkıcı yöneliş karşıtlığı","neighbor_only":"Komşu dalda kişileştirilmiş zaman topluluğa kötülük, yıkım ve yok oluş yöneltir.","neighbor_ref":"root_001520/B005","relation_type":"polarity_pair","shared_zone":"İki dal da insan dışı veya üstün bir failin insanlara yönelmesini sonuç doğuran mecazlı bir yapı içinde anlatır."}],"source_phrase_ar":"النظرة الرحمة (tahdhib)؛ نظر الله تعالى إلى عباده هو إحسانه إليهم وإفاضة نعمه عليهم (mufradat)","source_summary":"Kaynaklar merhamet anlamı ile Tanrı'nın kullarına iyilik etmesi ve iyiliklerini bolca vermesi açıklamasını aynı iyilik yönelimi altında destekler. Özel kutsal özne yapısı genel bakma eylemine indirgenemez.","sources":["TA","MU"],"what_is_ar":"يدخل فيه النظرة بمعنى الرحمة، ونظر الله إلى عباده بمعنى الإحسان وإفاضة النعم كما نصت المصادر.","what_is_not_ar":"لا يدخل فيه نظر العين المخلوق، ولا انتظار الوقت، ولا نظر الدهر المهلك."},"support_links":[]},{"boundary":"Bakış vardır fakat etkili görme, kavrama veya işe yarar yön bulma yoktur; genel görme ve bekleme anlamları dışarıda kalır.","branch_kind":"collocation","branch_ref":"root_001520/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَنتَظِرُ","morph_features":"STEM|POS:V|IMPV|(VIII)|LEM:yantaZiru|ROOT:nZr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:3:2","qac_word_ref":"32:30:3","surface_ar":"ٱنتَظِرْ"},{"lemma_ar":"مُنتَظِرُون","morph_features":"STEM|POS:N|ACT|PCPL|(VIII)|LEM:muntaZiruwn|ROOT:nZr|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"32:30:5:1","qac_word_ref":"32:30:5","surface_ar":"مُّنتَظِرُونَ"}],"gloss":"bakıp da görememe ve kavrayamama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi şaşkın veya kararsız halde bakışını bir yöne çevirir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bakış etkili görme, kavrama veya doğru yön bulma sonucunu üretmez."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sonuçsuz bakış, kişinin işe yarar bir şey yapamamasını ve güçsüz kalmasını gösterir."}}],"root_ar":"ن ظ ر","root_id":"root_001520","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bakışın var olduğu fakat etkili algı, kavrayış veya işe yarar sonuç üretmediği yapıda kullanılır.","boundary_detail":"Bakış vardır fakat etkili görme, kavrama veya işe yarar yön bulma yoktur; genel görme ve bekleme anlamları dışarıda kalır.","branch_image_ar":"نظر الحائر الذي لا يغني شيئا","concept_gloss":"bakıp da görememe ve kavrayamama","contextual_glosses":[{"applicability":"Kişinin gözleri açık ve yönelmiş olduğu halde gördüğünden anlam çıkaramadığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bakışın sürmesini ve buna rağmen kavrayışın oluşmamasını korur."},"facet_ids":["F001","F002"],"text":"bakıyor ama gördüğünü kavrayamıyor","usage_role":"explanatory"},{"applicability":"Şaşkınlığın kişiyi sonuçsuz ve etkisiz bir bakış içinde bıraktığı durumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Şaşkınlığı, bakışın sürmesini ve eylemsiz kalmayı korur."},"facet_ids":["F001","F003"],"text":"şaşkınlıkla bakakalmak","usage_role":"contextual"}],"definition":"Şaşkınlık içinde bir yöne bakıldığı halde görüleni kavrayamama, işe yarar bir görüş elde edememe ve bu nedenle bakıştan bir sonuç çıkaramama.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi şaşkın veya kararsız halde bakışını bir yöne çevirir."},{"facet_id":"F002","role":"core","statement":"Bakış etkili görme, kavrama veya doğru yön bulma sonucunu üretmez."},{"facet_id":"F003","role":"extension","statement":"Sonuçsuz bakış, kişinin işe yarar bir şey yapamamasını ve güçsüz kalmasını gösterir."}],"identity_rationale":"Kaynak ifadesi gözlerin bir yöne çevrilmesine rağmen etkili görme veya kavrayış oluşmamasını, şaşkınlık ve ne yapacağını bilememe haliyle açıkça bağlar. Dal sıradan görmeyi değil, sonuç vermeyen ve sahibine yarar sağlamayan bakışı anlatır.","lexical_glosses":[{"lexical_unit_id":"lu_043","rendering_kind":"ordinary","target_gloss":"bakıyorlar ama göremiyor ve kavrayamıyorlar"}],"lexicalization_note":"Tanım yalnızca bakıp da görememe veya kavrayamama biçimindeki verilen yapıya bağlıdır; yalın bakma eylemine genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dış adaylar göz rengi veya anatomisine ait olduğundan yalnızca etkili bakış dalıyla kurulan sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dalda yöneliş algı ve inceleme sağlar; odak dalda ise aynı yüzeysel bakış şaşkınlık yüzünden kavrayışa dönüşmez ve kişiye yarar sağlamaz.","focus_only":"Odak dalda bakış şaşkınlık içindedir ve görme, kavrama veya işe yarar sonuç üretmez.","gloss":"sonuçsuz ve etkili bakış ayrımı","neighbor_only":"Komşu dalda göz ya da zihinsel dikkat, nesneyi görmek, incelemek ve anlamak amacıyla etkili biçimde yöneltilir.","neighbor_ref":"root_001520/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da gözün veya dikkatin bir şeye yöneltilmesi bulunur."}],"source_phrase_ar":"يستعمل النظر في التحير في الأمور؛ ينظرون إليك وهم لا يبصرون؛ نظر عن تحير دال على قلة الغناء (mufradat)","source_qualifications":[{"kind":"sole_attestation","summary":"Şaşkın bakışın görme ve kavrama sağlamadığı, bu yüzden kişiye işe yarar bir sonuç vermediği aktarılır."}],"source_summary":"Tek kaynaklı iddia, şaşkınlıktan doğan bakışın gerçek görme ve kavrama sağlamadığını, bu nedenle sahibinin bir sonuca ulaşamadığını bildirir. Bakma eylemi sürse de algısal ve pratik başarı yoktur.","sources":["MU"],"what_is_ar":"يدخل فيه استعمال النظر في التحير في الأمور، والنظر الذي يدل على قلة الغناء أو عدم الإبصار النافع.","what_is_not_ar":"لا يدخل فيه مطلق المشاهدة النافعة، ولا الانتظار."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["32:30:1"],"branch_refs":[],"candidate_id":"cand_85a14a9400436fdbc139","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"32:30:1:causal-resumptive-launch","source_type":"word_analysis","support_ids":["sup_0f481c2d3c86d4b5cc9a","sup_30aa712ca6c1b24a2926"],"title":"final command is launched as consequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:1","qac_refs":["32:30:1:1"],"status":"accepted"}},{"anchor_refs":["32:30:1"],"branch_refs":[],"candidate_id":"cand_7c3e20d0aa03578be708","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"32:30:1:clipped-opening-cadence","source_type":"word_analysis","support_ids":["sup_0f481c2d3c86d4b5cc9a","sup_66fb9ac2ebdf7a119451"],"title":"brief particle quickens the closing onset","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:1","qac_refs":["32:30:1:1"],"status":"accepted"}},{"anchor_refs":["32:30:2"],"branch_refs":[],"candidate_id":"cand_27ec3d11628517fcc7fb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001001"],"scope":"focus_ayah","source_local_id":"32:30:2:imperative-with-separative-target","source_type":"word_analysis","support_ids":["sup_0586e9de3b71ed9ec20c","sup_6534d30f778b2413fde0"],"title":"compact command targets withdrawal from them","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:2","qac_refs":["32:30:1:2"],"status":"accepted"}},{"anchor_refs":["32:30:2"],"branch_refs":[],"candidate_id":"cand_1430b5a81c9bc6024ea1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001001"],"scope":"focus_ayah","source_local_id":"32:30:2:marked-command-register","source_type":"word_analysis","support_ids":["sup_16a86fee16bd132eb48b","sup_6534d30f778b2413fde0"],"title":"root becomes directive in the surah close","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:2","qac_refs":["32:30:1:2"],"status":"accepted"}},{"anchor_refs":["32:30:2"],"branch_refs":[],"candidate_id":"cand_391513d8477c02988ee5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001001"],"scope":"focus_ayah","source_local_id":"32:30:2:ordered-reversal-of-earlier-aversion","source_type":"word_analysis","support_ids":["sup_648ba67b930fcd4e3ace","sup_6534d30f778b2413fde0"],"title":"earlier aversion returns as commanded reversal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:2","qac_refs":["32:30:1:2"],"status":"accepted"}},{"anchor_refs":["32:30:2"],"branch_refs":[],"candidate_id":"cand_4cff78cffe94d7fbeb17","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001001"],"scope":"focus_ayah","source_local_id":"32:30:2:root-field-narrowed-to-aversion","source_type":"word_analysis","support_ids":["sup_6534d30f778b2413fde0","sup_afcdf3bbe046e9eadf72"],"title":"side and display imagery survives under aversion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:2","qac_refs":["32:30:1:2"],"status":"accepted"}},{"anchor_refs":["32:30:3"],"branch_refs":[],"candidate_id":"cand_083ca73d7a49156b12b1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"32:30:3:hum-frame-across-roles","source_type":"word_analysis","support_ids":["sup_021af097a019a60ebfe6","sup_71e88733ac3b44af989f"],"title":"same suffix frames object and subject roles","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:3","qac_refs":["32:30:2:1","32:30:2:2"],"status":"accepted"}},{"anchor_refs":["32:30:3"],"branch_refs":[],"candidate_id":"cand_893b0163112c20fdf9a2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"32:30:3:pronoun-chain-with-ambiguous-referent","source_type":"word_analysis","support_ids":["sup_021af097a019a60ebfe6","sup_6451fbebab5b1195178a"],"title":"the plural suffix carries the prior group without renaming it","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:3","qac_refs":["32:30:2:1","32:30:2:2"],"status":"accepted"}},{"anchor_refs":["32:30:3"],"branch_refs":[],"candidate_id":"cand_bc53d6d9ec3088f7d12e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"32:30:3:separative-complement","source_type":"word_analysis","support_ids":["sup_021af097a019a60ebfe6","sup_ecd1331e4f9ca49f933d"],"title":"the command is completed as separation from them","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:3","qac_refs":["32:30:2:1","32:30:2:2"],"status":"accepted"}},{"anchor_refs":["32:30:4"],"branch_refs":[],"candidate_id":"cand_7672eea3f914cf41ca22","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"32:30:4:audible-command-bridge","source_type":"word_analysis","support_ids":["sup_13dde207add95b3785f4","sup_c808dab5776ba4f12e82"],"title":"surface liaison carries the hinge into the command","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:4","qac_refs":["32:30:3:1"],"status":"accepted"}},{"anchor_refs":["32:30:4"],"branch_refs":[],"candidate_id":"cand_6d3b306bc69572bf285f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"32:30:4:coordinated-paired-imperatives","source_type":"word_analysis","support_ids":["sup_13dde207add95b3785f4","sup_cfbc87ebc0b11f4b9a42"],"title":"withdrawal and waiting become one compound directive","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:4","qac_refs":["32:30:3:1"],"status":"accepted"}},{"anchor_refs":["32:30:5"],"branch_refs":[],"candidate_id":"cand_0aa0d33328cbc2e25b31","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001520"],"scope":"focus_ayah","source_local_id":"32:30:5:compressed-command-sound","source_type":"word_analysis","support_ids":["sup_142d9a447b9478c2b5e5","sup_36122c86188069edc6f7"],"title":"short imperative compresses the waiting sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:5","qac_refs":["32:30:3:2"],"status":"accepted"}},{"anchor_refs":["32:30:5"],"branch_refs":[],"candidate_id":"cand_7350bb6c8d67a82fc466","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001520"],"scope":"focus_ayah","source_local_id":"32:30:5:internal-echo-with-final-participle","source_type":"word_analysis","support_ids":["sup_36122c86188069edc6f7","sup_cea31fa8aeefcff7eb3b"],"title":"the command is echoed by the final participle","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:5","qac_refs":["32:30:3:2"],"status":"accepted"}},{"anchor_refs":["32:30:5"],"branch_refs":[],"candidate_id":"cand_a9ef1c04a8f92c9f6e08","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001520"],"scope":"focus_ayah","source_local_id":"32:30:5:no-respite-boundary-inversion","source_type":"word_analysis","support_ids":["sup_36122c86188069edc6f7","sup_c496aec8ac142976b9e9"],"title":"denied respite becomes commanded waiting","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:5","qac_refs":["32:30:3:2"],"status":"accepted"}},{"anchor_refs":["32:30:5"],"branch_refs":[],"candidate_id":"cand_389bca4000c7192fa76c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001520"],"scope":"focus_ayah","source_local_id":"32:30:5:objectless-watchful-imperative","source_type":"word_analysis","support_ids":["sup_36122c86188069edc6f7","sup_f0dd26ae47c6d346fe03"],"title":"waiting is commanded as an active stance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:5","qac_refs":["32:30:3:2"],"status":"accepted"}},{"anchor_refs":["32:30:5"],"branch_refs":[],"candidate_id":"cand_440d676b3e3b0e9e3998","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001520"],"scope":"focus_ayah","source_local_id":"32:30:5:root-field-narrowed-to-wait-watch","source_type":"word_analysis","support_ids":["sup_36122c86188069edc6f7","sup_a007e50d6d5c149b7025"],"title":"vision and respite fields narrow into watchful waiting","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:5","qac_refs":["32:30:3:2"],"status":"accepted"}},{"anchor_refs":["32:30:6"],"branch_refs":[],"candidate_id":"cand_3e5686313f15b6ce1fd6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"32:30:6:case-role-predication","source_type":"word_analysis","support_ids":["sup_b1443a153dcf2951c190","sup_c36fee4999ea080f8be3"],"title":"particle grammar stabilizes their waiting as predication","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:6","qac_refs":["32:30:4:1","32:30:4:2"],"status":"accepted"}},{"anchor_refs":["32:30:6"],"branch_refs":[],"candidate_id":"cand_72dd8b1f9981a3dd5648","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"32:30:6:emphatic-rationale-clause","source_type":"word_analysis","support_ids":["sup_b2dfee8b238fd3b287a6","sup_c36fee4999ea080f8be3"],"title":"emphatic clause explains the command","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:6","qac_refs":["32:30:4:1","32:30:4:2"],"status":"accepted"}},{"anchor_refs":["32:30:6"],"branch_refs":[],"candidate_id":"cand_030c01ad4b2048e14e39","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"32:30:6:hum-carried-into-subject-slot","source_type":"word_analysis","support_ids":["sup_b00309aae7d576548412","sup_c36fee4999ea080f8be3"],"title":"same plural group returns as asserted subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:6","qac_refs":["32:30:4:1","32:30:4:2"],"status":"accepted"}},{"anchor_refs":["32:30:7"],"branch_refs":[],"candidate_id":"cand_6833cbcf9b54ec1a0d11","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001520"],"scope":"focus_ayah","source_local_id":"32:30:7:active-passive-qiraat-agency-contrast","source_type":"word_analysis","support_ids":["sup_9597446603a81f2aa82f","sup_c0c1cd7afe7b3b9521b7"],"title":"variant reading reverses watcher and watched roles","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:7","qac_refs":["32:30:5:1"],"status":"accepted"}},{"anchor_refs":["32:30:7"],"branch_refs":[],"candidate_id":"cand_7c68c4c06ebd6de4a58d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001520"],"scope":"focus_ayah","source_local_id":"32:30:7:echoed-waiting-surah-seal","source_type":"word_analysis","support_ids":["sup_73811a06b50b3409d62e","sup_9597446603a81f2aa82f"],"title":"command echo becomes the surah's final seal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:7","qac_refs":["32:30:5:1"],"status":"accepted"}},{"anchor_refs":["32:30:7"],"branch_refs":[],"candidate_id":"cand_832219918cbfef7b2fa0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001520"],"scope":"focus_ayah","source_local_id":"32:30:7:extended-final-cadence","source_type":"word_analysis","support_ids":["sup_37dcbe611e52a5425716","sup_9597446603a81f2aa82f"],"title":"long final sound extends the waiting state","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:7","qac_refs":["32:30:5:1"],"status":"accepted"}},{"anchor_refs":["32:30:7"],"branch_refs":[],"candidate_id":"cand_5408c18546090bcf2ca6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001520"],"scope":"focus_ayah","source_local_id":"32:30:7:no-respite-to-waiting-closure","source_type":"word_analysis","support_ids":["sup_54ce9b8953f44e581e9b","sup_9597446603a81f2aa82f"],"title":"denied respite resolves into suspended expectation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:7","qac_refs":["32:30:5:1"],"status":"accepted"}},{"anchor_refs":["32:30:7"],"branch_refs":[],"candidate_id":"cand_6336bf85b9dbe521f449","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001520"],"scope":"focus_ayah","source_local_id":"32:30:7:plural-predicate-waiting-state","source_type":"word_analysis","support_ids":["sup_9597446603a81f2aa82f","sup_a00077da695ea3c3e236"],"title":"final predicate characterizes the whole group as waiters","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"32:30:7","qac_refs":["32:30:5:1"],"status":"accepted"}},{"anchor_refs":["32:30:1"],"branch_refs":[],"candidate_id":"cand_9a6c4a61aed89b1f4b7d","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001001"],"scope":"focus_ayah","source_local_id":"32:30:1:2","source_type":"qac_morpheme","support_ids":["sup_51e60b79009a5474c2a0"],"title":"QAC root occurrence: ع ر ض","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["32:30:3"],"branch_refs":[],"candidate_id":"cand_5bbb276474d22b4a7ee1","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001520"],"scope":"focus_ayah","source_local_id":"32:30:3:2","source_type":"qac_morpheme","support_ids":["sup_bd7d6d4a5e43bd4b7fb7"],"title":"QAC root occurrence: ن ظ ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["32:30"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"32:30","branch_refs":["root_001001/B005","root_001520/B002"],"candidate_id":"cand_0735a0402999ff516706","commentary_obligation":"review","hft_ref":"hft_444f4e8371bc3461ca30","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b1_withdraw_within_shared_interval","source_type":"hft","support_ids":["sup_c4ece2b734bc5ad53914"],"title":"b1_withdraw_within_shared_interval","trust":"legacy_unbound"},{"anchor_refs":["32:30"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"32:30","branch_refs":["root_001001/B005","root_001520/B001","root_001520/B002"],"candidate_id":"cand_665415f6561c99d49e10","commentary_obligation":"review","hft_ref":"hft_85a9886dc23e3ebfa214","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b2_attentive_disengagement","source_type":"hft","support_ids":["sup_e3b5ca00b85dbf3f5ca1"],"title":"b2_attentive_disengagement","trust":"legacy_unbound"},{"anchor_refs":["32:30"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"32:30","branch_refs":["root_001001/B006","root_001520/B006"],"candidate_id":"cand_94530876ad2ad92c9d15","commentary_obligation":"review","hft_ref":"hft_05c0411acbe394e6aeab","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b3_mirrored_expectations","source_type":"hft","support_ids":["sup_9e7f9d45e9ed77136555"],"title":"b3_mirrored_expectations","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فَأَعْرِضْ عَنْهُمْ وَٱنتَظِرْ إِنَّهُم مُّنتَظِرُونَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"32:30:1:1","qac_word_ref":"32:30:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"أَعْرَضَ","morph_features":"STEM|POS:V|IMPV|(IV)|LEM:>aEoraDa|ROOT:ErD|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:1:2","qac_word_ref":"32:30:1","root_ar":"ع ر ض","surface_ar":"أَعْرِضْ"},{"lemma_ar":"عَن","morph_features":"STEM|POS:P|LEM:Ean","morpheme_role":"STEM","pos":"P","qac_ref":"32:30:2:1","qac_word_ref":"32:30:2","root_ar":"","surface_ar":"عَنْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"32:30:2:2","qac_word_ref":"32:30:2","root_ar":"","surface_ar":"هُمْ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"32:30:3:1","qac_word_ref":"32:30:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"يَنتَظِرُ","morph_features":"STEM|POS:V|IMPV|(VIII)|LEM:yantaZiru|ROOT:nZr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:3:2","qac_word_ref":"32:30:3","root_ar":"ن ظ ر","surface_ar":"ٱنتَظِرْ"},{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"32:30:4:1","qac_word_ref":"32:30:4","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"32:30:4:2","qac_word_ref":"32:30:4","root_ar":"","surface_ar":"هُم"},{"lemma_ar":"مُنتَظِرُون","morph_features":"STEM|POS:N|ACT|PCPL|(VIII)|LEM:muntaZiruwn|ROOT:nZr|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"32:30:5:1","qac_word_ref":"32:30:5","root_ar":"ن ظ ر","surface_ar":"مُّنتَظِرُونَ"}],"word_analysis_qac_refs":[["32:30:1:1"],["32:30:1:2"],["32:30:2:1","32:30:2:2"],["32:30:3:1"],["32:30:3:2"],["32:30:4:1","32:30:4:2"],["32:30:5:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["32:30:1","32:30:2","32:30:3","32:30:4","32:30:5","32:30:6","32:30:7"]},"focus_surface_evidence":{"arabic_uthmani":"فَأَعْرِضْ عَنْهُمْ وَٱنتَظِرْ إِنَّهُم مُّنتَظِرُونَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"32:30:1:1","qac_word_ref":"32:30:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"أَعْرَضَ","morph_features":"STEM|POS:V|IMPV|(IV)|LEM:>aEoraDa|ROOT:ErD|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:1:2","qac_word_ref":"32:30:1","root_ar":"ع ر ض","surface_ar":"أَعْرِضْ"},{"lemma_ar":"عَن","morph_features":"STEM|POS:P|LEM:Ean","morpheme_role":"STEM","pos":"P","qac_ref":"32:30:2:1","qac_word_ref":"32:30:2","root_ar":"","surface_ar":"عَنْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"32:30:2:2","qac_word_ref":"32:30:2","root_ar":"","surface_ar":"هُمْ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"32:30:3:1","qac_word_ref":"32:30:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"يَنتَظِرُ","morph_features":"STEM|POS:V|IMPV|(VIII)|LEM:yantaZiru|ROOT:nZr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"32:30:3:2","qac_word_ref":"32:30:3","root_ar":"ن ظ ر","surface_ar":"ٱنتَظِرْ"},{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"32:30:4:1","qac_word_ref":"32:30:4","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"32:30:4:2","qac_word_ref":"32:30:4","root_ar":"","surface_ar":"هُم"},{"lemma_ar":"مُنتَظِرُون","morph_features":"STEM|POS:N|ACT|PCPL|(VIII)|LEM:muntaZiruwn|ROOT:nZr|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"32:30:5:1","qac_word_ref":"32:30:5","root_ar":"ن ظ ر","surface_ar":"مُّنتَظِرُونَ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["32:30:1:1"],["32:30:1:2"],["32:30:2:1","32:30:2:2"],["32:30:3:1"],["32:30:3:2"],["32:30:4:1","32:30:4:2"],["32:30:5:1"]],"word_analysis_refs":["32:30:1","32:30:2","32:30:3","32:30:4","32:30:5","32:30:6","32:30:7"],"word_rows":[{"analysis_record_ref":"32:30:1","analytic_gloss_range_en":"causal-resumptive connector launching the final command as consequence of the prior verdict","analytic_root_gloss_range_en":null,"qac_refs":["32:30:1:1"],"root":{"note":"no root"},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"32:30:2","analytic_gloss_range_en":"Form IV imperative commanding active turning away from the plural group through the following separative complement","analytic_root_gloss_range_en":"broad range around side-breadth, display, confrontation, and turning aside; local Form IV plus the following preposition selects aversive turning away while leaving side/display imagery as pressure","qac_refs":["32:30:1:2"],"root":{"arabic":"ع ر ض","transliteration":"ʿ-r-ḍ"},"surface":{"arabic":"أَعْرِضْ","transliteration":"aʿriḍ"}},{"analysis_record_ref":"32:30:3","analytic_gloss_range_en":"separative prepositional phrase with a 3mp suffix, marking the group from whom withdrawal is commanded while preserving referent ambiguity","analytic_root_gloss_range_en":null,"qac_refs":["32:30:2:1","32:30:2:2"],"root":{"note":"no root"},"surface":{"arabic":"عَنْهُمْ","transliteration":"ʿanhum"}},{"analysis_record_ref":"32:30:4","analytic_gloss_range_en":"coordinating conjunction that hinges the first imperative to the second","analytic_root_gloss_range_en":null,"qac_refs":["32:30:3:1"],"root":{"note":"no root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"32:30:5","analytic_gloss_range_en":"Form VIII imperative commanding active waiting or watchful expectation without an expressed object","analytic_root_gloss_range_en":"broad range around seeing, examining, waiting, granting respite, facing, and watching; local Form VIII imperative selects watchful waiting while preserving visual expectation","qac_refs":["32:30:3:2"],"root":{"arabic":"ن ظ ر","transliteration":"n-ẓ-r"},"surface":{"arabic":"ٱنتَظِرْ","transliteration":"intaẓir"}},{"analysis_record_ref":"32:30:6","analytic_gloss_range_en":"emphatic particle plus 3mp pronoun introducing the rationale clause and making the pronoun the governed subject","analytic_root_gloss_range_en":null,"qac_refs":["32:30:4:1","32:30:4:2"],"root":{"note":"no root"},"surface":{"arabic":"إِنَّهُم","transliteration":"innahum"}},{"analysis_record_ref":"32:30:7","analytic_gloss_range_en":"Form VIII active participle, masculine plural nominative, functioning as the predicate of the emphatic clause","analytic_root_gloss_range_en":"broad range around seeing, waiting, respite, watching, facing, and counterpart relation; local active participle selects a group characterized by waiting, with a passive qiraat as agency contrast","qac_refs":["32:30:5:1"],"root":{"arabic":"ن ظ ر","transliteration":"n-ẓ-r"},"surface":{"arabic":"مُّنتَظِرُونَ","transliteration":"muntaẓirūna"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":7,"words_total":7,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["32:30"],"branch_refs":["root_001001/B005","root_001520/B002"],"candidate_id":"cand_0735a0402999ff516706","evidence_scope":"focus_ayah","hft_ref":"hft_444f4e8371bc3461ca30","item_id":"b1_withdraw_within_shared_interval","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b1_withdraw_within_shared_interval","support_id":"sup_c4ece2b734bc5ad53914"},{"anchor_refs":["32:30"],"branch_refs":["root_001001/B005","root_001520/B001","root_001520/B002"],"candidate_id":"cand_665415f6561c99d49e10","evidence_scope":"focus_ayah","hft_ref":"hft_85a9886dc23e3ebfa214","item_id":"b2_attentive_disengagement","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b2_attentive_disengagement","support_id":"sup_e3b5ca00b85dbf3f5ca1"},{"anchor_refs":["32:30"],"branch_refs":["root_001001/B006","root_001520/B006"],"candidate_id":"cand_94530876ad2ad92c9d15","evidence_scope":"focus_ayah","hft_ref":"hft_05c0411acbe394e6aeab","item_id":"b3_mirrored_expectations","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b3_mirrored_expectations","support_id":"sup_9e7f9d45e9ed77136555"}],"diagnostics":[],"lane_counts":{"global":13,"macro":8,"micro":3},"packet_summary":{"ayah_count":30,"focus_ref":"32:30","protocol":"focus-trace-pericope-lean-v1","split_root_mappings":[],"window":["32:1","32:2","32:3","32:4","32:5","32:6","32:7","32:8","32:9","32:10","32:11","32:12","32:13","32:14","32:15","32:16","32:17","32:18","32:19","32:20","32:21","32:22","32:23","32:24","32:25","32:26","32:27","32:28","32:29","32:30"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"32:30","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":14,"unstructured_record_count":0},"identity":{"ayah_ref":"32:30","lane":"micro","linguistic_source_ref":"32:30","surface_ref":"32:30","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"32:30","target_tokens":[["Öyleyse",["32:30:1"]],["onlardan",["32:30:2"]],["yüz",["32:30:1"]],["çevir",["32:30:1"]],["ve",["32:30:3"]],["bekle",["32:30:3"]],["Onlar",["32:30:4"]],["da",["32:30:4"]],["bekliyorlar",["32:30:5"]]],"text":"Öyleyse onlardan yüz çevir ve bekle. Onlar da bekliyorlar."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":21,"ayah_to":30,"id":"s032-p03-021-030","label":"Nearer punishment and signs of certainty","number":3,"refs":["32:21","32:22","32:23","32:24","32:25","32:26","32:27","32:28","32:29","32:30"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:3","source_type":"word_analysis","support_id":"sup_021af097a019a60ebfe6","text":"{\"gloss_range\":\"separative prepositional phrase with a 3mp suffix, marking the group from whom withdrawal is commanded while preserving referent ambiguity\",\"prose\":\"{{ar:عَنْهُمْ}} ({{tr:ʿanhum}}) completes the first command by marking separation from them rather than direct action upon them. The suffix carries the prior plural group into the ayah without renaming it, but the guardrail evidence keeps the referent open across the immediate opposition and broader warned audience. Its later recurrence in {{ar:إِنَّهُم}} ({{tr:innahum}}) lets the same group move from object of withdrawal to subject of the final waiting-state, and the repeated -hum sound makes that role-shift audible.\",\"root_display\":\"no root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:عَنْهُمْ}} ({{tr:ʿanhum}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:2:imperative-with-separative-target","source_type":"word_analysis","support_id":"sup_0586e9de3b71ed9ec20c","text":"{\"blocking_evidence\":null,\"headline\":\"compact command targets withdrawal from them\",\"reader_payoff\":\"The reader notices that disengagement is commanded decisively to one addressee and grammatically aimed away from a plural group.\",\"reason\":\"The word is a 2ms imperative, and the verb instance plus attachment data require the following prepositional complement as the local target of withdrawal.\",\"representative_source_ids\":[\"QG-05628684\",\"QG-32e22f66\",\"QG-c35a0feb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:1","source_type":"word_analysis","support_id":"sup_0f481c2d3c86d4b5cc9a","text":"{\"gloss_range\":\"causal-resumptive connector launching the final command as consequence of the prior verdict\",\"prose\":\"{{ar:فَ}} ({{tr:fa}}) makes the final ayah begin as consequence, not as a fresh scene. It carries the force of an implied premise from 32:29 into {{ar:أَعْرِضْ}} ({{tr:aʿriḍ}}), so the command is heard as the answer to persistent rejection and denied respite. Its short onset also clips the entry into the two-command close, making the surah's last movement start quickly and dependently.\",\"root_display\":\"no root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:4","source_type":"word_analysis","support_id":"sup_13dde207add95b3785f4","text":"{\"gloss_range\":\"coordinating conjunction that hinges the first imperative to the second\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) is the hinge between withdrawal and watchful expectation. It coordinates {{ar:ٱنتَظِرْ}} ({{tr:intaẓir}}) with {{ar:أَعْرِضْ}} ({{tr:aʿriḍ}}), so the ayah does not stop at disengagement; it turns disengagement into a compound directive. In the recitation surface, the hinge flows directly into the second imperative, making the joining audible as well as syntactic.\",\"root_display\":\"no root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:5:compressed-command-sound","source_type":"word_analysis","support_id":"sup_142d9a447b9478c2b5e5","text":"{\"blocking_evidence\":null,\"headline\":\"short imperative compresses the waiting sound\",\"reader_payoff\":\"The reader notices that the short command audibly anticipates the longer final waiting word.\",\"reason\":\"The consonant cluster in the command recurs in the final predicate, while the imperative remains shorter and more compressed.\",\"representative_source_ids\":[\"QP-32e35c48\",\"QP-3ff8f215\",\"QP-4878cfd4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:2:marked-command-register","source_type":"word_analysis","support_id":"sup_16a86fee16bd132eb48b","text":"{\"blocking_evidence\":null,\"headline\":\"root becomes directive in the surah close\",\"reader_payoff\":\"The reader notices that a varied root family is made sharp as an imperative, with a hard command texture rather than descriptive narration.\",\"reason\":\"The contextual profile shows this exact root-form class functioning in imperative contexts, and the local surface carries that command register.\",\"representative_source_ids\":[\"QH-8eb371c3\",\"QH-cb37107f\",\"QP-2a40eaf7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:1:causal-resumptive-launch","source_type":"word_analysis","support_id":"sup_30aa712ca6c1b24a2926","text":"{\"blocking_evidence\":null,\"headline\":\"final command is launched as consequence\",\"reader_payoff\":\"The reader notices that the last command is not isolated; it follows as the consequence of 32:29.\",\"reason\":\"QAC parses the particle as resumptive-causal, and the first attachment clause starts with the command sequence that follows from the prior verdict.\",\"representative_source_ids\":[\"QG-7689b7d0\",\"QG-f344b976\",\"QB-d015d3e7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:5","source_type":"word_analysis","support_id":"sup_36122c86188069edc6f7","text":"{\"gloss_range\":\"Form VIII imperative commanding active waiting or watchful expectation without an expressed object\",\"prose\":\"{{ar:ٱنتَظِرْ}} ({{tr:intaẓir}}) is a second full imperative, not a prediction. Its Form VIII shape makes waiting an adopted stance of watchful expectation, and its lack of an expressed object keeps the focus on the posture itself. The clipped n-t-ẓ-r sound lands quickly, with nasal and emphatic pressure, before it expands in the longer final participle. Across the ayah boundary, the same root answers 32:29's denied respite: what they are not granted becomes what the addressee is commanded to await, and the final predicate will echo that same waiting back onto them.\",\"root_display\":\"{{ar:ن ظ ر}} ({{tr:n-ẓ-r}})\",\"root_gloss_range\":\"broad range around seeing, examining, waiting, granting respite, facing, and watching; local Form VIII imperative selects watchful waiting while preserving visual expectation\",\"surface_display\":\"{{ar:ٱنتَظِرْ}} ({{tr:intaẓir}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:7:extended-final-cadence","source_type":"word_analysis","support_id":"sup_37dcbe611e52a5425716","text":"{\"blocking_evidence\":null,\"headline\":\"long final sound extends the waiting state\",\"reader_payoff\":\"The reader notices that the final word's sound stretches the closure in the same direction as its meaning.\",\"reason\":\"The final participial form is longer than the earlier imperative and ends the surah with an extended plural nominative cadence.\",\"representative_source_ids\":[\"QP-d5f55613\",\"QP-f3cabb28\",\"MP-07ac312e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"32:30:1:2","source_type":"qac_morpheme","support_id":"sup_51e60b79009a5474c2a0","text":"{\"lemma_ar\":\"أَعْرَضَ\",\"morph_features\":\"STEM|POS:V|IMPV|(IV)|LEM:>aEoraDa|ROOT:ErD|2MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"32:30:1:2\",\"qac_word_ref\":\"32:30:1\",\"root_ar\":\"ع ر ض\",\"surface_ar\":\"أَعْرِضْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:7:no-respite-to-waiting-closure","source_type":"word_analysis","support_id":"sup_54ce9b8953f44e581e9b","text":"{\"blocking_evidence\":null,\"headline\":\"denied respite resolves into suspended expectation\",\"reader_payoff\":\"The reader notices that the denied delay of 32:29 is not left behind; it becomes the final state in which the group is held.\",\"reason\":\"The adjacent no-respite boundary and the final participle share the root field, and no guardrail evidence blocks the boundary handoff.\",\"representative_source_ids\":[\"QI-a14f10d2\",\"QB-c103308a\",\"QY-14ddc269\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:3:pronoun-chain-with-ambiguous-referent","source_type":"word_analysis","support_id":"sup_6451fbebab5b1195178a","text":"{\"blocking_evidence\":null,\"headline\":\"the plural suffix carries the prior group without renaming it\",\"reader_payoff\":\"The reader notices that the ayah relies on carried pronoun reference, while translation should not over-specify the group beyond the live discourse candidates.\",\"reason\":\"CRITICAL rows correctly see a carried plural group, but attachment evidence marks the antecedent as ambiguous across immediate and broader discourse candidates.\",\"representative_source_ids\":[\"QG-3c4914d8\",\"QG-bfe7e3b8\",\"MT-e2922b23\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:2:ordered-reversal-of-earlier-aversion","source_type":"word_analysis","support_id":"sup_648ba67b930fcd4e3ace","text":"{\"blocking_evidence\":null,\"headline\":\"earlier aversion returns as commanded reversal\",\"reader_payoff\":\"The reader notices that the same-surah root return turns the earlier rejection of signs back upon those who rejected.\",\"reason\":\"The command is first in the ordered pair and is linked by the CRITICAL rows to 32:22; no guardrail evidence blocks that same-surah echo.\",\"representative_source_ids\":[\"QI-01570d64\",\"MI-cca542d4\",\"QY-df0a10ca\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:2","source_type":"word_analysis","support_id":"sup_6534d30f778b2413fde0","text":"{\"gloss_range\":\"Form IV imperative commanding active turning away from the plural group through the following separative complement\",\"prose\":\"{{ar:أَعْرِضْ}} ({{tr:aʿriḍ}}) is a compact Form IV command to one addressee, completed by the following separative phrase. The root's display, side, and opposition fields survive as imagery of turning one's side away, but local grammar selects aversion rather than presentation or counter-objection. The hamza/ʿayn onset and emphatic ḍ give the imperative a rough command texture suited to breaking contact. In the surah's own movement, this is also a reversal: the earlier turning away from signs at 32:22 is answered by a commanded turning away from the group.\",\"root_display\":\"{{ar:ع ر ض}} ({{tr:ʿ-r-ḍ}})\",\"root_gloss_range\":\"broad range around side-breadth, display, confrontation, and turning aside; local Form IV plus the following preposition selects aversive turning away while leaving side/display imagery as pressure\",\"surface_display\":\"{{ar:أَعْرِضْ}} ({{tr:aʿriḍ}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:1:clipped-opening-cadence","source_type":"word_analysis","support_id":"sup_66fb9ac2ebdf7a119451","text":"{\"blocking_evidence\":null,\"headline\":\"brief particle quickens the closing onset\",\"reader_payoff\":\"The reader notices the compressed sound of the transition before the longer paired commands unfold.\",\"reason\":\"The proclitic particle is fused to the first imperative in the surface sequence, so its brevity is part of the command's immediate launch.\",\"representative_source_ids\":[\"QF-c6f4c57e\",\"QP-a67cff3d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:3:hum-frame-across-roles","source_type":"word_analysis","support_id":"sup_71e88733ac3b44af989f","text":"{\"blocking_evidence\":null,\"headline\":\"same suffix frames object and subject roles\",\"reader_payoff\":\"The reader notices the same group audibly returning later as the subject of the waiting predicate.\",\"reason\":\"The suffix in this prepositional phrase and the suffix in the emphatic clause share the same surface referential form, while local syntax changes their roles.\",\"representative_source_ids\":[\"QF-661fe22e\",\"QP-5fa2bbf6\",\"QB-ccd72cb6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:7:echoed-waiting-surah-seal","source_type":"word_analysis","support_id":"sup_73811a06b50b3409d62e","text":"{\"blocking_evidence\":null,\"headline\":\"command echo becomes the surah's final seal\",\"reader_payoff\":\"The reader notices that the surah closes by echoing the command to wait as the opposing group's own suspended condition.\",\"reason\":\"The final word shares the root and Form VIII pattern of the preceding command while occupying the last position of the ayah and surah.\",\"representative_source_ids\":[\"QT-6d895a53\",\"QE-35d7c42d\",\"QY-11aa8d26\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:7","source_type":"word_analysis","support_id":"sup_9597446603a81f2aa82f","text":"{\"gloss_range\":\"Form VIII active participle, masculine plural nominative, functioning as the predicate of the emphatic clause\",\"prose\":\"{{ar:مُّنتَظِرُونَ}} ({{tr:muntaẓirūna}}) lands the ayah and surah on a plural waiting-state. As the predicate of {{ar:إِنَّهُم}} ({{tr:innahum}}), it characterizes the group as waiters rather than narrating a single event, and it mirrors the command {{ar:ٱنتَظِرْ}} ({{tr:intaẓir}}). It also carries 32:29's denied respite into the final predicate: the group not granted delay is left characterized by suspended expectation. The active reading makes them participants in expectation; the passive qiraat {{ar:مُنْتَظَرُونَ}} ({{tr:muntaẓarūna}}) usefully reverses agency by making them the awaited or watched, but the local standard predicate remains active. The long final ending leaves the closure suspended in expectation instead of resolved narration.\",\"root_display\":\"{{ar:ن ظ ر}} ({{tr:n-ẓ-r}})\",\"root_gloss_range\":\"broad range around seeing, waiting, respite, watching, facing, and counterpart relation; local active participle selects a group characterized by waiting, with a passive qiraat as agency contrast\",\"surface_display\":\"{{ar:مُّنتَظِرُونَ}} ({{tr:muntaẓirūna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:7:plural-predicate-waiting-state","source_type":"word_analysis","support_id":"sup_a00077da695ea3c3e236","text":"{\"blocking_evidence\":null,\"headline\":\"final predicate characterizes the whole group as waiters\",\"reader_payoff\":\"The reader notices that the final word declares an ongoing group-state, not a one-time act of waiting.\",\"reason\":\"The word is a masculine plural nominative active participle functioning as the predicate of the emphatic clause.\",\"representative_source_ids\":[\"QG-47eeddad\",\"QG-74ee5179\",\"MG-64c41a1d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:5:root-field-narrowed-to-wait-watch","source_type":"word_analysis","support_id":"sup_a007e50d6d5c149b7025","text":"{\"blocking_evidence\":null,\"headline\":\"vision and respite fields narrow into watchful waiting\",\"reader_payoff\":\"The reader notices that the root's visual field makes the waiting vigilant, while local Form VIII prevents a simple looking or debate reading.\",\"reason\":\"V4 confirms seeing, waiting, and respite branches, but local Form VIII and the objectless command select expectant waiting.\",\"representative_source_ids\":[\"QS-6884899a\",\"QS-cc8cd481\",\"QF-4ac2b480\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:2:root-field-narrowed-to-aversion","source_type":"word_analysis","support_id":"sup_afcdf3bbe046e9eadf72","text":"{\"blocking_evidence\":null,\"headline\":\"side and display imagery survives under aversion\",\"reader_payoff\":\"The reader notices that the command is not bare absence; it pictures a deliberate side-turn, while local Form IV blocks a simple display or objection reading.\",\"reason\":\"V4 confirms multiple root branches, but local Form IV with the separative complement selects the turning-away branch and leaves other branches only as controlled imagery.\",\"representative_source_ids\":[\"QS-199627eb\",\"QS-8e8ac1f4\",\"QF-ad7473a1\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:6:hum-carried-into-subject-slot","source_type":"word_analysis","support_id":"sup_b00309aae7d576548412","text":"{\"blocking_evidence\":null,\"headline\":\"same plural group returns as asserted subject\",\"reader_payoff\":\"The reader notices the same plural suffix crossing from separation phrase to emphatic subject, while the exact antecedent remains discourse-sensitive.\",\"reason\":\"The suffix chain is real, but attachment evidence preserves ambiguity in the plural referent rather than forcing a single explicit noun.\",\"representative_source_ids\":[\"QG-eb3f2827\",\"QP-9e482ab3\",\"QB-01774b63\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:6:case-role-predication","source_type":"word_analysis","support_id":"sup_b1443a153dcf2951c190","text":"{\"blocking_evidence\":null,\"headline\":\"particle grammar stabilizes their waiting as predication\",\"reader_payoff\":\"The reader notices that their waiting is asserted as a stable clause relation, not a loose echo.\",\"reason\":\"The pronoun is the governed subject of the emphatic particle, and the following nominative participle functions as predicate.\",\"representative_source_ids\":[\"QG-dc53e781\",\"MG-471507bc\",\"QS-e0af98c9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:6:emphatic-rationale-clause","source_type":"word_analysis","support_id":"sup_b2dfee8b238fd3b287a6","text":"{\"blocking_evidence\":null,\"headline\":\"emphatic clause explains the command\",\"reader_payoff\":\"The reader notices that the final clause grounds the imperatives instead of merely adding another description.\",\"reason\":\"Attachment evidence marks the clause as explanatory, and its emphatic particle starts directly after the waiting command without a coordinating conjunction.\",\"representative_source_ids\":[\"QG-bc787d5f\",\"QT-0318174c\",\"MT-54aa94c5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"32:30:3:2","source_type":"qac_morpheme","support_id":"sup_bd7d6d4a5e43bd4b7fb7","text":"{\"lemma_ar\":\"يَنتَظِرُ\",\"morph_features\":\"STEM|POS:V|IMPV|(VIII)|LEM:yantaZiru|ROOT:nZr|2MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"32:30:3:2\",\"qac_word_ref\":\"32:30:3\",\"root_ar\":\"ن ظ ر\",\"surface_ar\":\"ٱنتَظِرْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:7:active-passive-qiraat-agency-contrast","source_type":"word_analysis","support_id":"sup_c0c1cd7afe7b3b9521b7","text":"{\"blocking_evidence\":null,\"headline\":\"variant reading reverses watcher and watched roles\",\"reader_payoff\":\"The reader notices that the standard active predicate casts them as waiters, while the passive variant exposes a nearby agency reversal.\",\"reason\":\"The accepted variant is valid contrast, but the local QAC parse and noun instance identify the canonical surface as an active participle predicate.\",\"representative_source_ids\":[\"QS-252ea5ed\",\"QF-bab76a1e\",\"QY-58672283\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:6","source_type":"word_analysis","support_id":"sup_c36fee4999ea080f8be3","text":"{\"gloss_range\":\"emphatic particle plus 3mp pronoun introducing the rationale clause and making the pronoun the governed subject\",\"prose\":\"{{ar:إِنَّهُم}} ({{tr:innahum}}) turns the close from paired command into command-with-rationale. The emphatic particle governs the attached plural pronoun as the subject of the clause, and the following participle supplies the predicate. Because there is no new conjunction before it, the clause immediately explains why the addressee should turn away and wait, while the repeated -hum sound carries the same group from object of withdrawal into asserted subject-position.\",\"root_display\":\"no root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِنَّهُم}} ({{tr:innahum}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:5:no-respite-boundary-inversion","source_type":"word_analysis","support_id":"sup_c496aec8ac142976b9e9","text":"{\"blocking_evidence\":null,\"headline\":\"denied respite becomes commanded waiting\",\"reader_payoff\":\"The reader notices that 32:29's denial of respite is transformed into the commanded stance of 32:30.\",\"reason\":\"The CRITICAL rows give a concrete adjacent reference, and the local command follows immediately after the denied-respite verdict at 32:29.\",\"representative_source_ids\":[\"QS-2ad31b4c\",\"QI-63fbbbdb\",\"ME-04b829d0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:4:audible-command-bridge","source_type":"word_analysis","support_id":"sup_c808dab5776ba4f12e82","text":"{\"blocking_evidence\":null,\"headline\":\"surface liaison carries the hinge into the command\",\"reader_payoff\":\"The reader notices that the sound surface performs the same joining that the grammar marks.\",\"reason\":\"The conjunction is fused to the following command in the surface form, so the bridge has both syntactic and audible force.\",\"representative_source_ids\":[\"QF-8d119800\",\"QP-b5c4a282\",\"QY-0432911c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:5:internal-echo-with-final-participle","source_type":"word_analysis","support_id":"sup_cea31fa8aeefcff7eb3b","text":"{\"blocking_evidence\":null,\"headline\":\"the command is echoed by the final participle\",\"reader_payoff\":\"The reader notices that the command to wait returns in the same ayah as the group's stated waiting condition.\",\"reason\":\"The same root and Form VIII pattern recur in the final active participle, with the command and predicate occupying distinct discourse roles.\",\"representative_source_ids\":[\"QE-00fa28d7\",\"ME-96a634d8\",\"QY-aa7414ff\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:4:coordinated-paired-imperatives","source_type":"word_analysis","support_id":"sup_cfbc87ebc0b11f4b9a42","text":"{\"blocking_evidence\":null,\"headline\":\"withdrawal and waiting become one compound directive\",\"reader_payoff\":\"The reader notices that waiting is not an afterthought but the coordinated companion of turning away.\",\"reason\":\"Attachment evidence directly coordinates the second imperative with the first, making the conjunction the structural hinge.\",\"representative_source_ids\":[\"QG-42e63ddf\",\"MG-64ca9622\",\"QT-27dda0c0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:3:separative-complement","source_type":"word_analysis","support_id":"sup_ecd1331e4f9ca49f933d","text":"{\"blocking_evidence\":null,\"headline\":\"the command is completed as separation from them\",\"reader_payoff\":\"The reader notices that the grammar directs withdrawal away from a group, not an action done to them as a direct object.\",\"reason\":\"The preposition governs the pronoun as the complement of the turning-away verb, forcing a separative relation.\",\"representative_source_ids\":[\"QG-3d621a47\",\"QG-5432c177\",\"QS-d7b855b8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"32:30:5:objectless-watchful-imperative","source_type":"word_analysis","support_id":"sup_f0dd26ae47c6d346fe03","text":"{\"blocking_evidence\":null,\"headline\":\"waiting is commanded as an active stance\",\"reader_payoff\":\"The reader notices that the second imperative commands watchful posture, not passive delay or mere prediction.\",\"reason\":\"The word is a coordinated 2ms imperative and the verb frame is objectless, so the local force is command plus watchful expectation.\",\"representative_source_ids\":[\"QG-381dc7b0\",\"QG-be5eb7fb\",\"QS-064aff96\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فَأَعْرِضْ عَنْهُمْ وَٱنتَظِرْ إِنَّهُم مُّنتَظِرُونَ","ayah_ref":"32:30"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001001/B005","root_001520/B002"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_001001","role":"Turning one's side away supplies the enacted withdrawal that opens controlled distance from the group.","root":"ع ر ض","source_ref":"32:30","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001520","role":"Delay and expectation supply the shared interval occupied by both waiting forms.","root":"ن ظ ر","source_ref":"32:30","source_word_indices":["3","5"]}],"changed_reading":{"after":"Withdraw active engagement without leaving the shared countdown: both sides remain poised inside the same unresolved interval.","before":"Dismiss them and passively wait for an unspecified outcome."},"confidence":"strong","focus_anchor":"The word-1 imperative creates distance, while the same waiting root occurs at words 3 and 5 for the commanded addressee and the plural group.","mechanism":"A controlled social withdrawal and a duplicated temporal posture operate together: engagement stops, but neither side leaves the interval in which the matter will resolve.","model_id":"b1_withdraw_within_shared_interval"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b1_withdraw_within_shared_interval","source_type":"hft","support_id":"sup_c4ece2b734bc5ad53914","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَأَعْرِضْ عَنْهُمْ وَٱنتَظِرْ إِنَّهُم مُّنتَظِرُونَ","ayah_ref":"32:30"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001001/B005","root_001520/B001","root_001520/B002"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_001001","role":"Side-turning supplies cessation of direct confrontation rather than disappearance from the scene.","root":"ع ر ض","source_ref":"32:30","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001520","role":"Directed sight or insight supplies continued attentiveness during the withdrawal.","root":"ن ظ ر","source_ref":"32:30","source_word_indices":["3","5"]},{"branch_id":"B002","mapped_root_id":"root_001520","role":"Expectation supplies the temporal duration through which attention is maintained.","root":"ن ظ ر","source_ref":"32:30","source_word_indices":["3","5"]}],"changed_reading":{"after":"Cease the dispute yet remain perceptively alert; the withdrawal redirects attention from argument to disclosure.","before":"Turning away ends attention, and waiting is inert delay."},"confidence":"medium","focus_anchor":"The command to turn aside is immediately joined to a root whose inventory includes both waiting and directed perception.","mechanism":"Bodily or conversational disengagement does not require perceptual closure. The addressee can stop confronting the group while sustaining watchful discernment toward what the interval reveals.","model_id":"b2_attentive_disengagement"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b2_attentive_disengagement","source_type":"hft","support_id":"sup_e3b5ca00b85dbf3f5ca1","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَأَعْرِضْ عَنْهُمْ وَٱنتَظِرْ إِنَّهُم مُّنتَظِرُونَ","ayah_ref":"32:30"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001001/B006","root_001520/B006"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_001520","role":"Counterpart equivalence supplies a formal mirror between the two occurrences without equalizing their claims.","root":"ن ظ ر","source_ref":"32:30","source_word_indices":["3","5"]},{"branch_id":"B006","mapped_root_id":"root_001001","role":"Reciprocal opposition supplies the adversarial relation maintained across the commanded distance.","root":"ع ر ض","source_ref":"32:30","source_word_indices":["1"]}],"changed_reading":{"after":"The repeated root stages opposed counterparts: both await one event from different sides, with no implication that their grounds or outcomes are equal.","before":"The opponents merely happen to be waiting at the same time."},"confidence":"exploratory","focus_anchor":"One waiting root is repeated across a singular imperative and a plural active participle, while the turning root also admits reciprocal opposition.","mechanism":"The syntax places a singled-out addressee and a collective in formally mirrored postures. Lateral separation preserves rather than dissolves their status as opposed counterparts awaiting one contested resolution.","model_id":"b3_mirrored_expectations"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b3_mirrored_expectations","source_type":"hft","support_id":"sup_9e7f9d45e9ed77136555","trust":"legacy_unbound"}]}
</lane_packet_json>
