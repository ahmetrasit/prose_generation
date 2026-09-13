# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **19:1**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s019-regular-20260912/s019/19_1/macro.discovery.json` and modify nothing
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

- Macro has explicitly added external ayat: 1:2, 1:3, 1:4, 1:5, 1:6, 1:7. Treat them as an overlay, not as the starting frame.
- Phase 1: assess the focus against the declared pericope or host-surah context and any automatic host basmala. During this phase, quarantine explicitly added external ayat: do not let them nominate, rank, suppress, or reframe native/pericope findings.
- Phase 2: review only the explicitly added external ayat and ask what genuine delta they add beyond Phase 1. Retain an external overlay finding only when it creates a specific carrier, trigger, contact, changed reading, semantic detail, and boundary. Reject external material that only restates a native/pericope finding or imports a whole-surah theme without a local contact.
- If all ayat of a surah were supplied externally, still treat them as individually listed ayat, not as an implicit whole-surah reading. Cite and land only the individual external ayat that actually trigger the finding.

## Response Schema

Return exactly these top-level fields:

```json
{
  "schema_version": "commentary-v5-scope-discovery-v1",
  "ayah_ref": "19:1",
  "lane": "macro",
  "coverage_complete": true,
  "candidate_decisions": [
    {
      "candidate_id": "exact packet candidate ID",
      "decision": "accept | narrow | represented | reject",
      "reason": "specific evidentiary reason",
      "finding_refs": ["macro:stable-key"],
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
      "finding_ref": "macro:stable-key",
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
`macro:`. Accepted/narrowed candidates own dedicated findings. A represented
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
{"analysis_context":{"analysis_id":"s019-regular-20260912","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"19:1","host_surah":19,"lane_context_refs":["19:0","19:2","19:3","19:4","19:5","19:6","19:7","19:8","19:9","19:10","19:11","19:12","19:13","19:14","19:15","1:2","1:3","1:4","1:5","1:6","1:7"],"ordered_context_refs":["19:2","19:3","19:4","19:5","19:6","19:7","19:8","19:9","19:10","19:11","19:12","19:13","19:14","19:15","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000074/B003","candidate_links":[{"candidate_id":"cand_afbc97cc69c64ac4168b","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_e0d18fbe40091b29015c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A manifest sign supplies communicative force without requiring sentential wording.","root":"ء ي ي","source_ref":"19:10","source_word_indices":["5","7"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000074","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a0e8a9ed2954e0759f54"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000129/B001","candidate_links":[{"candidate_id":"cand_fa4ab40bcd2f76378043","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b8e71281f19717a9b1bc","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Stirring what is still from repose supplies the reactivation endpoint of the analogy.","root":"ب ع ث","source_ref":"19:15","source_word_indices":["8"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000129","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_2c210bc16416ebbde294"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000428/B001","candidate_links":[{"candidate_id":"cand_168d70ed69d06cb11994","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_c7416b79e98de1c461f5","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Concealment supplies the withheld semantic side of the articulated sequence.","root":"خ ف ي","source_ref":"19:3","source_word_indices":["5"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000428","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_3eaa131517a3dd3b6361"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000434/B002","candidate_links":[{"candidate_id":"cand_fa4ab40bcd2f76378043","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b8e71281f19717a9b1bc","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Bringing creation into existence supplies emergence beyond the prior condition.","root":"خ ل ق","source_ref":"19:9","source_word_indices":["9"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000434","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_2c210bc16416ebbde294"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000478/B001","candidate_links":[{"candidate_id":"cand_168d70ed69d06cb11994","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_c7416b79e98de1c461f5","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Calling through speech links the private prayer sequence to the opener's vocal form.","root":"د ع و","source_ref":"19:4","source_word_indices":["12"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000478","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_3eaa131517a3dd3b6361"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000516/B003","candidate_links":[{"candidate_id":"cand_b6115a01e352b050b85c","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_ef55d546a9a0b176332c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Recall after absence supplies the mnemonic recovery function assigned to the opener.","root":"ذ ك ر","source_ref":"19:2","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000516","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_dde4f42cdaa505ed6402"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000516/B004","candidate_links":[{"candidate_id":"cand_b6115a01e352b050b85c","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_ef55d546a9a0b176332c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Mention moving on the tongue supplies the opener's oral and recited channel.","root":"ذ ك ر","source_ref":"19:2","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000516","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_dde4f42cdaa505ed6402"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000745/B005","candidate_links":[{"candidate_id":"cand_a1e66f956460a04a8d08","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_8b57a94c80cabff25d69","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Naming as designation makes letter-names, rather than word meaning, the operative formal unit.","root":"س م و","source_ref":"19:7","source_word_indices":["5","12"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000745","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b045ebbc5426015717a5"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000831/B001","candidate_links":[{"candidate_id":"cand_fa4ab40bcd2f76378043","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b8e71281f19717a9b1bc","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Knowable thinghood supplies the boundary crossed when bare units become an intelligible textual object.","root":"ش ي ء","source_ref":"19:9","source_word_indices":["14"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000831","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_2c210bc16416ebbde294"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001035/B004","candidate_links":[{"candidate_id":"cand_fa4ab40bcd2f76378043","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b8e71281f19717a9b1bc","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Interrupted offspring supplies the sterile-seeming starting condition of the analogy.","root":"ع ق ر","source_ref":"19:5","source_word_indices":["8"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001035","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_2c210bc16416ebbde294"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001283/B001","candidate_links":[{"candidate_id":"cand_fa4ab40bcd2f76378043","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b8e71281f19717a9b1bc","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Joining unit to unit supplies the compositional arrow from isolated letters toward discourse.","root":"ك ت ب","source_ref":"19:12","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001283","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_2c210bc16416ebbde294"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001283/B002","candidate_links":[{"candidate_id":"cand_afbc97cc69c64ac4168b","lane":"macro"},{"candidate_id":"cand_fa4ab40bcd2f76378043","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_e0d18fbe40091b29015c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Ordered letters and written text anchor the non-sentential opener to the later book-channel.","root":"ك ت ب","source_ref":"19:12","source_word_indices":["3"]},{"hft_ref":"hft_b8e71281f19717a9b1bc","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Ordering letters makes the emergence specifically textual rather than merely biological.","root":"ك ت ب","source_ref":"19:12","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001283","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_2c210bc16416ebbde294","sup_a0e8a9ed2954e0759f54"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001316/B001","candidate_links":[{"candidate_id":"cand_afbc97cc69c64ac4168b","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_e0d18fbe40091b29015c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Intelligible speech connecting speakers is the channel explicitly suspended, defining the opener's contrastive mode.","root":"ك ل م","source_ref":"19:10","source_word_indices":["9"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001316","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a0e8a9ed2954e0759f54"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001487/B001","candidate_links":[{"candidate_id":"cand_168d70ed69d06cb11994","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_c7416b79e98de1c461f5","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Raised calling supplies the audible address against which the opener's sounded form can be heard.","root":"ن د و","source_ref":"19:3","source_word_indices":["2","4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001487","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_3eaa131517a3dd3b6361"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001633/B002","candidate_links":[{"candidate_id":"cand_afbc97cc69c64ac4168b","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_e0d18fbe40091b29015c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Gesture supplies a replacement channel by which meaning passes without ordinary speech.","root":"و ح ي","source_ref":"19:11","source_word_indices":["6"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001633","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a0e8a9ed2954e0759f54"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001633/B003","candidate_links":[{"candidate_id":"cand_afbc97cc69c64ac4168b","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_e0d18fbe40091b29015c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Inscription supplies the visible-sign analogue for the opener's glyph sequence.","root":"و ح ي","source_ref":"19:11","source_word_indices":["6"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001633","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a0e8a9ed2954e0759f54"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001650/B001","candidate_links":[{"candidate_id":"cand_a1e66f956460a04a8d08","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_8b57a94c80cabff25d69","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A visible identifying mark supplies the graphic counterpart to the spoken letter-names.","root":"س م و","source_ref":"19:7","source_word_indices":["5","12"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001650","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b045ebbc5426015717a5"]}],"candidate_inventory":[{"anchor_refs":["19:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"19:1","branch_refs":["root_000516/B003","root_000516/B004"],"candidate_id":"cand_b6115a01e352b050b85c","commentary_obligation":"review","hft_ref":"hft_ef55d546a9a0b176332c","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_mnemonic_utterance","source_type":"hft","support_ids":["sup_dde4f42cdaa505ed6402"],"title":"delta_mnemonic_utterance","trust":"legacy_unbound"},{"anchor_refs":["19:3","19:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"19:1","branch_refs":["root_000428/B001","root_000478/B001","root_001487/B001"],"candidate_id":"cand_168d70ed69d06cb11994","commentary_obligation":"review","hft_ref":"hft_c7416b79e98de1c461f5","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_concealed_call","source_type":"hft","support_ids":["sup_3eaa131517a3dd3b6361"],"title":"delta_concealed_call","trust":"legacy_unbound"},{"anchor_refs":["19:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"19:1","branch_refs":["root_000745/B005","root_001650/B001"],"candidate_id":"cand_a1e66f956460a04a8d08","commentary_obligation":"review","hft_ref":"hft_8b57a94c80cabff25d69","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_names_before_naming","source_type":"hft","support_ids":["sup_b045ebbc5426015717a5"],"title":"delta_names_before_naming","trust":"legacy_unbound"},{"anchor_refs":["19:10","19:11","19:12"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"19:1","branch_refs":["root_000074/B003","root_001283/B002","root_001316/B001","root_001633/B002","root_001633/B003"],"candidate_id":"cand_afbc97cc69c64ac4168b","commentary_obligation":"review","hft_ref":"hft_e0d18fbe40091b29015c","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_sign_beyond_sentence_speech","source_type":"hft","support_ids":["sup_a0e8a9ed2954e0759f54"],"title":"delta_sign_beyond_sentence_speech","trust":"legacy_unbound"},{"anchor_refs":["19:12","19:15","19:5","19:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"19:1","branch_refs":["root_000129/B001","root_000434/B002","root_000831/B001","root_001035/B004","root_001283/B001","root_001283/B002"],"candidate_id":"cand_fa4ab40bcd2f76378043","commentary_obligation":"review","hft_ref":"hft_b8e71281f19717a9b1bc","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_textual_germination","source_type":"hft","support_ids":["sup_2c210bc16416ebbde294"],"title":"outlier_textual_germination","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_542fd9c18111b6f1074f","connection_ref":"conn_d1542a2bed31ee9d8319","note":"Immediate continuation that begins the Zechariah narrative after the opening letters.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"19:2","source_target_components":["19:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"19:2","target_evidence":{"arabic_uthmani":"ذِكْرُ رَحْمَتِ رَبِّكَ عَبْدَهُۥ زَكَرِيَّآ","ayah_ref":"19:2"},"target_ref":"19:2"}],"focus":{"arabic_uthmani":"كٓهيعٓصٓ","qac_morphemes":[{"lemma_ar":"","morph_features":"STEM|POS:INL","morpheme_role":"STEM","pos":"INL","qac_ref":"19:1:1:1","qac_word_ref":"19:1:1","root_ar":"","surface_ar":"كٓهيعٓصٓ"}],"word_analysis_qac_refs":[["19:1:1:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["19:1:1"]},"focus_surface_evidence":{"arabic_uthmani":"كٓهيعٓصٓ","qac_morphemes":[{"lemma_ar":"","morph_features":"STEM|POS:INL","morpheme_role":"STEM","pos":"INL","qac_ref":"19:1:1:1","qac_word_ref":"19:1:1","root_ar":"","surface_ar":"كٓهيعٓصٓ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["19:1:1:1"]],"word_analysis_refs":["19:1:1"],"word_rows":[{"analysis_record_ref":"19:1:1","analytic_gloss_range_en":"five recited letter-names fused into one rootless muqattaʿāt opener; its force comes through predicate-like placement, recitation, sound, distributional uniqueness, and a forward bridge into the dhikr frame rather than through an ordinary lexical gloss","analytic_root_gloss_range_en":null,"qac_refs":["19:1:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"كٓهيعٓصٓ","transliteration":"kāf hāʾ yāʾ ʿayn ṣād"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":1,"words_total":1,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":10,"missing_anchor_refs":[],"supplied_unique_anchor_count":10},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["19:2"],"branch_refs":["root_000516/B003","root_000516/B004"],"candidate_id":"cand_b6115a01e352b050b85c","evidence_scope":"declared_pericope","hft_ref":"hft_ef55d546a9a0b176332c","item_id":"delta_mnemonic_utterance","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_mnemonic_utterance","support_id":"sup_dde4f42cdaa505ed6402"},{"anchor_refs":["19:3","19:4"],"branch_refs":["root_000428/B001","root_000478/B001","root_001487/B001"],"candidate_id":"cand_168d70ed69d06cb11994","evidence_scope":"declared_pericope","hft_ref":"hft_c7416b79e98de1c461f5","item_id":"delta_concealed_call","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_concealed_call","support_id":"sup_3eaa131517a3dd3b6361"},{"anchor_refs":["19:7"],"branch_refs":["root_000745/B005","root_001650/B001"],"candidate_id":"cand_a1e66f956460a04a8d08","evidence_scope":"declared_pericope","hft_ref":"hft_8b57a94c80cabff25d69","item_id":"delta_names_before_naming","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_names_before_naming","support_id":"sup_b045ebbc5426015717a5"},{"anchor_refs":["19:10","19:11","19:12"],"branch_refs":["root_000074/B003","root_001283/B002","root_001316/B001","root_001633/B002","root_001633/B003"],"candidate_id":"cand_afbc97cc69c64ac4168b","evidence_scope":"declared_pericope","hft_ref":"hft_e0d18fbe40091b29015c","item_id":"delta_sign_beyond_sentence_speech","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_sign_beyond_sentence_speech","support_id":"sup_a0e8a9ed2954e0759f54"},{"anchor_refs":["19:12","19:15","19:5","19:9"],"branch_refs":["root_000129/B001","root_000434/B002","root_000831/B001","root_001035/B004","root_001283/B001","root_001283/B002"],"candidate_id":"cand_fa4ab40bcd2f76378043","evidence_scope":"declared_pericope","hft_ref":"hft_b8e71281f19717a9b1bc","item_id":"outlier_textual_germination","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_textual_germination","support_id":"sup_2c210bc16416ebbde294"}],"diagnostics":[{"warning":"Unrecognized HFT reader field is preserved as a global review record"}],"lane_counts":{"global":9,"macro":5,"micro":0},"packet_summary":{"ayah_count":15,"focus_ref":"19:1","protocol":"focus-trace-pericope-lean-v1","split_root_mappings":[],"window":["19:1","19:2","19:3","19:4","19:5","19:6","19:7","19:8","19:9","19:10","19:11","19:12","19:13","19:14","19:15"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"valid_pericope_packet_unbound_response"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"19:1","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":7,"source_present":true,"structured_insight_count":6,"unstructured_record_count":1},"identity":{"ayah_ref":"19:1","lane":"macro","linguistic_source_ref":"19:1","surface_ref":"19:1","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"19:1","target_tokens":[["Kâf",["19:1:1"]],["Hâ",["19:1:1"]],["Yâ",["19:1:1"]],["Ayn",["19:1:1"]],["Sâd",["19:1:1"]]],"text":"Kâf Hâ Yâ Ayn Sâd."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":1,"ayah_to":15,"id":"s019-p01-001-015","label":"Zechariah and John","number":1,"refs":["19:1","19:2","19:3","19:4","19:5","19:6","19:7","19:8","19:9","19:10","19:11","19:12","19:13","19:14","19:15"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"19:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"19:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["19:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"19:0"},{"ayah_ref":"19:2","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"19:2","root_occurrences":[{"lemmas_ar":["ذِكْر"],"occurrence_count":1,"pos_tags":["N"],"root":"ذ ك ر","surfaces_ar":["ذِكْرُ"],"word_indices":["1"]},{"lemmas_ar":["رَحْمَة"],"occurrence_count":1,"pos_tags":["N"],"root":"ر ح م","surfaces_ar":["رَحْمَتِ"],"word_indices":["2"]},{"lemmas_ar":["رَبّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ر ب ب","surfaces_ar":["رَبِّ"],"word_indices":["3"]},{"lemmas_ar":["عَبْد"],"occurrence_count":1,"pos_tags":["N"],"root":"ع ب د","surfaces_ar":["عَبْدَ"],"word_indices":["4"]}],"root_sequence":["ذ ك ر","ر ح م","ر ب ب","ع ب د"],"text_ar":"ذِكْرُ رَحْمَتِ رَبِّكَ عَبْدَهُۥ زَكَرِيَّآ"}],"context_order":["19:2"],"context_root_cues":[{"root":"ذ ك ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الذكر خلاف الأنثى"},{"branch_id":"B002","branch_image_ar":"صلابة الذكر وحدته وشدته"},{"branch_id":"B003","branch_image_ar":"استحضار الشيء بعد النسيان أو مع الحفظ"},{"branch_id":"B004","branch_image_ar":"جريان الذكر على اللسان"},{"branch_id":"B007","branch_image_ar":"ذكر المرء شرف وصيت"},{"branch_id":"B008","branch_image_ar":"ذكر الحق صك ووثيقة حق"},{"branch_id":"B009","branch_image_ar":"الذكرى والتذكرة ما يذكّر"}],"mapped_root_id":"root_000516","mapped_root_norm":"ذ ك ر"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]},{"root":"ر ب ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ربوبية وملك وسيادة"},{"branch_id":"B002","branch_image_ar":"إصلاح وتربية وإتمام"},{"branch_id":"B003","branch_image_ar":"علم رباني"},{"branch_id":"B004","branch_image_ar":"ربة وجماعات كثيرة"},{"branch_id":"B005","branch_image_ar":"ربيب وربيبة ورابة"},{"branch_id":"B006","branch_image_ar":"رُبّ خاثر وإصلاح به"},{"branch_id":"B007","branch_image_ar":"لزوم وإقامة ودوام"},{"branch_id":"B008","branch_image_ar":"رباب السحاب"},{"branch_id":"B009","branch_image_ar":"شاة رُبّى وحداثة"},{"branch_id":"B010","branch_image_ar":"ربابة تجمع القداح"},{"branch_id":"B011","branch_image_ar":"ربابة عهد وميثاق"},{"branch_id":"B012","branch_image_ar":"ربة نبات"},{"branch_id":"B013","branch_image_ar":"ماء رَبَب كثير"},{"branch_id":"B014","branch_image_ar":"رَبْرَب قطيع"},{"branch_id":"B015","branch_image_ar":"حرف رب وربما"},{"branch_id":"B016","branch_image_ar":"رُبَى حاجة وعقدة ونعمة"},{"branch_id":"B017","branch_image_ar":"رباني الملاحين"}],"mapped_root_id":"root_000532","mapped_root_norm":"ر ب ب"},{"branches":[{"branch_id":"B001","branch_image_ar":"زيادة وعلو"},{"branch_id":"B002","branch_image_ar":"أرض مرتفعة"},{"branch_id":"B003","branch_image_ar":"زيادة الربا في المعاملة"},{"branch_id":"B004","branch_image_ar":"تصعد النفس وانتفاخه"},{"branch_id":"B005","branch_image_ar":"تغذية ونشوء"},{"branch_id":"B006","branch_image_ar":"نتوء أصل الفخذ"},{"branch_id":"B007","branch_image_ar":"أهل البيت من بني الأعمام"}],"mapped_root_id":"root_000537","mapped_root_norm":"ر ب و"}]},{"root":"ع ب د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرق والملك"},{"branch_id":"B003","branch_image_ar":"العبادة والطاعة الخاضعة"},{"branch_id":"B004","branch_image_ar":"التعبيد والاستعباد"},{"branch_id":"B005","branch_image_ar":"التذليل والتسوية"},{"branch_id":"B006","branch_image_ar":"التكريم والتعظيم"},{"branch_id":"B007","branch_image_ar":"القوة والصلابة"},{"branch_id":"B008","branch_image_ar":"الأنفة والغضب"},{"branch_id":"B009","branch_image_ar":"قلة اللبث وسرعة العدو"},{"branch_id":"B010","branch_image_ar":"التفرق في الوجوه"},{"branch_id":"B011","branch_image_ar":"العطب والانقطاع"},{"branch_id":"B012","branch_image_ar":"صَلاءة الطيب"}],"mapped_root_id":"root_000973","mapped_root_norm":"ع ب د"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"19:2","surface_ref":"19:2"},{"ayah_ref":"19:3","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"19:3","root_occurrences":[{"lemmas_ar":["نَادَىٰ","نِدَآء"],"occurrence_count":2,"pos_tags":["V","N"],"root":"ن د و","surfaces_ar":["نَادَىٰ","نِدَآءً"],"word_indices":["2","4"]},{"lemmas_ar":["رَبّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ر ب ب","surfaces_ar":["رَبَّ"],"word_indices":["3"]},{"lemmas_ar":["خَفِىّ"],"occurrence_count":1,"pos_tags":["ADJ"],"root":"خ ف ي","surfaces_ar":["خَفِيًّا"],"word_indices":["5"]}],"root_sequence":["ن د و","ر ب ب","ن د و","خ ف ي"],"text_ar":"إِذْ نَادَىٰ رَبَّهُۥ نِدَآءً خَفِيًّۭا"}],"context_order":["19:3"],"context_root_cues":[{"root":"ن د و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"رفع الصوت والنداء"},{"branch_id":"B002","branch_image_ar":"مدى الصوت وبعد نداه"},{"branch_id":"B003","branch_image_ar":"مجلس القوم واجتماعهم"},{"branch_id":"B004","branch_image_ar":"تندية الإبل والخيل بين الماء والمرعى"},{"branch_id":"B005","branch_image_ar":"بلل ومطر ورطوبة"},{"branch_id":"B006","branch_image_ar":"نبت وكلأ من الندى"},{"branch_id":"B007","branch_image_ar":"شحم يسمى ندى"},{"branch_id":"B008","branch_image_ar":"جود وسخاء وعطاء"},{"branch_id":"B009","branch_image_ar":"إصابة بمكروه أو خزي"},{"branch_id":"B010","branch_image_ar":"نزوع في النسب إلى أصل كريم"},{"branch_id":"B011","branch_image_ar":"ظهور وإعلام كمناداة"},{"branch_id":"B012","branch_image_ar":"نواد وقواص متفرقة"},{"branch_id":"B013","branch_image_ar":"همز يغيره إلى طرائق وآثار"}],"mapped_root_id":"root_001487","mapped_root_norm":"ن د ي"},{"branches":[{"branch_id":"B001","branch_image_ar":"اجتماع القوم في النادي والندوة"},{"branch_id":"B002","branch_image_ar":"الصوت المرفوع والنداء"},{"branch_id":"B003","branch_image_ar":"بلل الندى والمطر"},{"branch_id":"B004","branch_image_ar":"ندى الجود والسخاء"},{"branch_id":"B005","branch_image_ar":"ابتلال بالمكروه وخزي الكلام"},{"branch_id":"B006","branch_image_ar":"تندية الإبل والخيل بين الماء والمرعى"},{"branch_id":"B007","branch_image_ar":"تنزع الناقة في النسب إلى أصل كريم"},{"branch_id":"B008","branch_image_ar":"ظهور الشيء كأنه ينادي"}],"mapped_root_id":"root_001486","mapped_root_norm":"ن د و"},{"branches":[{"branch_id":"B001","branch_image_ar":"تَمايُل وحركة"}],"mapped_root_id":"root_001563","mapped_root_norm":"ن و د"}]},{"root":"ر ب ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ربوبية وملك وسيادة"},{"branch_id":"B002","branch_image_ar":"إصلاح وتربية وإتمام"},{"branch_id":"B003","branch_image_ar":"علم رباني"},{"branch_id":"B004","branch_image_ar":"ربة وجماعات كثيرة"},{"branch_id":"B005","branch_image_ar":"ربيب وربيبة ورابة"},{"branch_id":"B006","branch_image_ar":"رُبّ خاثر وإصلاح به"},{"branch_id":"B007","branch_image_ar":"لزوم وإقامة ودوام"},{"branch_id":"B008","branch_image_ar":"رباب السحاب"},{"branch_id":"B009","branch_image_ar":"شاة رُبّى وحداثة"},{"branch_id":"B010","branch_image_ar":"ربابة تجمع القداح"},{"branch_id":"B011","branch_image_ar":"ربابة عهد وميثاق"},{"branch_id":"B012","branch_image_ar":"ربة نبات"},{"branch_id":"B013","branch_image_ar":"ماء رَبَب كثير"},{"branch_id":"B014","branch_image_ar":"رَبْرَب قطيع"},{"branch_id":"B015","branch_image_ar":"حرف رب وربما"},{"branch_id":"B016","branch_image_ar":"رُبَى حاجة وعقدة ونعمة"},{"branch_id":"B017","branch_image_ar":"رباني الملاحين"}],"mapped_root_id":"root_000532","mapped_root_norm":"ر ب ب"},{"branches":[{"branch_id":"B001","branch_image_ar":"زيادة وعلو"},{"branch_id":"B002","branch_image_ar":"أرض مرتفعة"},{"branch_id":"B003","branch_image_ar":"زيادة الربا في المعاملة"},{"branch_id":"B004","branch_image_ar":"تصعد النفس وانتفاخه"},{"branch_id":"B005","branch_image_ar":"تغذية ونشوء"},{"branch_id":"B006","branch_image_ar":"نتوء أصل الفخذ"},{"branch_id":"B007","branch_image_ar":"أهل البيت من بني الأعمام"}],"mapped_root_id":"root_000537","mapped_root_norm":"ر ب و"}]},{"root":"خ ف ي","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الستر والخفاء"},{"branch_id":"B002","branch_image_ar":"ما يستر أو يستتر"},{"branch_id":"B003","branch_image_ar":"إزالة الخفاء والإظهار"},{"branch_id":"B004","branch_image_ar":"لمع البرق الخفي"}],"mapped_root_id":"root_000428","mapped_root_norm":"خ ف ي"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"19:3","surface_ref":"19:3"},{"ayah_ref":"19:4","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"19:4","root_occurrences":[{"lemmas_ar":["قَالَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ق و ل","surfaces_ar":["قَالَ"],"word_indices":["1"]},{"lemmas_ar":["رَبّ","رَبّ"],"occurrence_count":2,"pos_tags":["N","N"],"root":"ر ب ب","surfaces_ar":["رَبِّ","رَبِّ"],"word_indices":["2","13"]},{"lemmas_ar":["وَهَنَ"],"occurrence_count":1,"pos_tags":["V"],"root":"و ه ن","surfaces_ar":["وَهَنَ"],"word_indices":["4"]},{"lemmas_ar":["عَظْم"],"occurrence_count":1,"pos_tags":["N"],"root":"ع ظ م","surfaces_ar":["عَظْمُ"],"word_indices":["5"]},{"lemmas_ar":["ٱشْتَعَلَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ش ع ل","surfaces_ar":["ٱشْتَعَلَ"],"word_indices":["7"]},{"lemmas_ar":["رَأْس"],"occurrence_count":1,"pos_tags":["N"],"root":"ر ء س","surfaces_ar":["رَّأْسُ"],"word_indices":["8"]},{"lemmas_ar":["شَيْب"],"occurrence_count":1,"pos_tags":["N"],"root":"ش ي ب","surfaces_ar":["شَيْبًا"],"word_indices":["9"]},{"lemmas_ar":["كَانَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ك و ن","surfaces_ar":["أَكُنۢ"],"word_indices":["11"]},{"lemmas_ar":["دُعَآء"],"occurrence_count":1,"pos_tags":["N"],"root":"د ع و","surfaces_ar":["دُعَآئِ"],"word_indices":["12"]},{"lemmas_ar":["شَقِيّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ش ق و","surfaces_ar":["شَقِيًّا"],"word_indices":["14"]}],"root_sequence":["ق و ل","ر ب ب","و ه ن","ع ظ م","ش ع ل","ر ء س","ش ي ب","ك و ن","د ع و","ر ب ب","ش ق و"],"text_ar":"قَالَ رَبِّ إِنِّى وَهَنَ ٱلْعَظْمُ مِنِّى وَٱشْتَعَلَ ٱلرَّأْسُ شَيْبًۭا وَلَمْ أَكُنۢ بِدُعَآئِكَ رَبِّ شَقِيًّۭا"}],"context_order":["19:4"],"context_root_cues":[{"root":"ق و ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"إخراج القول بالنطق"},{"branch_id":"B002","branch_image_ar":"اللسان آلة القول"},{"branch_id":"B003","branch_image_ar":"كثرة القول في صاحبه"},{"branch_id":"B004","branch_image_ar":"القيل صاحب القول النافذ"},{"branch_id":"B005","branch_image_ar":"قول ما لم يكن أو نسبته"},{"branch_id":"B006","branch_image_ar":"اجترار القول إلى النفس"},{"branch_id":"B007","branch_image_ar":"القول الفاشي بين الناس"},{"branch_id":"B008","branch_image_ar":"عود القال لضرب القلة"},{"branch_id":"B009","branch_image_ar":"المقاولة في الأمر"},{"branch_id":"B010","branch_image_ar":"اقتالة الحكم على غيره"},{"branch_id":"B011","branch_image_ar":"قول يجري مجرى الظن"},{"branch_id":"B012","branch_image_ar":"قول في النفس لم يظهر"},{"branch_id":"B013","branch_image_ar":"القول اعتقاد ومذهب"},{"branch_id":"B014","branch_image_ar":"قول الشيء دلالته"},{"branch_id":"B015","branch_image_ar":"العناية الصادقة بالشيء"},{"branch_id":"B016","branch_image_ar":"قول الشيء حده"}],"mapped_root_id":"root_001272","mapped_root_norm":"ق و ل"},{"branches":[{"branch_id":"B001","branch_image_ar":"القِلَّة والضآلة"},{"branch_id":"B002","branch_image_ar":"قُلَّة الشيء ورأسه"},{"branch_id":"B003","branch_image_ar":"القُلَّة الجرة الكبيرة"},{"branch_id":"B004","branch_image_ar":"الإقلال والاستقلال حملا ونهوضا"},{"branch_id":"B005","branch_image_ar":"القِلُّ رعدة واضطراب"},{"branch_id":"B006","branch_image_ar":"القلقلة اضطراب وتحرك"}],"mapped_root_id":"root_001251","mapped_root_norm":"ق ل ل"}]},{"root":"ر ب ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ربوبية وملك وسيادة"},{"branch_id":"B002","branch_image_ar":"إصلاح وتربية وإتمام"},{"branch_id":"B003","branch_image_ar":"علم رباني"},{"branch_id":"B004","branch_image_ar":"ربة وجماعات كثيرة"},{"branch_id":"B005","branch_image_ar":"ربيب وربيبة ورابة"},{"branch_id":"B006","branch_image_ar":"رُبّ خاثر وإصلاح به"},{"branch_id":"B007","branch_image_ar":"لزوم وإقامة ودوام"},{"branch_id":"B008","branch_image_ar":"رباب السحاب"},{"branch_id":"B009","branch_image_ar":"شاة رُبّى وحداثة"},{"branch_id":"B010","branch_image_ar":"ربابة تجمع القداح"},{"branch_id":"B011","branch_image_ar":"ربابة عهد وميثاق"},{"branch_id":"B012","branch_image_ar":"ربة نبات"},{"branch_id":"B013","branch_image_ar":"ماء رَبَب كثير"},{"branch_id":"B014","branch_image_ar":"رَبْرَب قطيع"},{"branch_id":"B015","branch_image_ar":"حرف رب وربما"},{"branch_id":"B016","branch_image_ar":"رُبَى حاجة وعقدة ونعمة"},{"branch_id":"B017","branch_image_ar":"رباني الملاحين"}],"mapped_root_id":"root_000532","mapped_root_norm":"ر ب ب"},{"branches":[{"branch_id":"B001","branch_image_ar":"زيادة وعلو"},{"branch_id":"B002","branch_image_ar":"أرض مرتفعة"},{"branch_id":"B003","branch_image_ar":"زيادة الربا في المعاملة"},{"branch_id":"B004","branch_image_ar":"تصعد النفس وانتفاخه"},{"branch_id":"B005","branch_image_ar":"تغذية ونشوء"},{"branch_id":"B006","branch_image_ar":"نتوء أصل الفخذ"},{"branch_id":"B007","branch_image_ar":"أهل البيت من بني الأعمام"}],"mapped_root_id":"root_000537","mapped_root_norm":"ر ب و"}]},{"root":"و ه ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ضعف القوة وفتور العزم"},{"branch_id":"B002","branch_image_ar":"ساعة من الليل تمضي"},{"branch_id":"B003","branch_image_ar":"الواهنة موضع في الأضلاع والصدر"},{"branch_id":"B004","branch_image_ar":"وجع الواهنة وداؤها"},{"branch_id":"B005","branch_image_ar":"فتور المرأة وثقل حركتها"},{"branch_id":"B006","branch_image_ar":"كثافة الإبل"},{"branch_id":"B007","branch_image_ar":"الوهين حاث الأجير"},{"branch_id":"B008","branch_image_ar":"كلام باطل يتعلل به"},{"branch_id":"B009","branch_image_ar":"ثقل الطائر عن النهوض"}],"mapped_root_id":"root_001687","mapped_root_norm":"و ه ن"}]},{"root":"ع ظ م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الكبر والقوة"},{"branch_id":"B002","branch_image_ar":"معظم الشيء"},{"branch_id":"B003","branch_image_ar":"مستغلظ العضو"},{"branch_id":"B004","branch_image_ar":"العظيمة النازلة"},{"branch_id":"B005","branch_image_ar":"العَظْم الصلب"},{"branch_id":"B006","branch_image_ar":"التعاظم والزهو"},{"branch_id":"B007","branch_image_ar":"الاستعظام والهيبة"},{"branch_id":"B008","branch_image_ar":"عظامة الردف"},{"branch_id":"B009","branch_image_ar":"خشبة الرحل"},{"branch_id":"B010","branch_image_ar":"الحرمة والشرف"}],"mapped_root_id":"root_001029","mapped_root_norm":"ع ظ م"}]},{"root":"ش ع ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"لهب يشتعل من حطب أو فتيلة"},{"branch_id":"B002","branch_image_ar":"بياض يشتعل في الرأس أو طرف الدابة"},{"branch_id":"B003","branch_image_ar":"غضب يشتعل كالنار"},{"branch_id":"B004","branch_image_ar":"انتشار في كل وجه كاشتعال النار"},{"branch_id":"B005","branch_image_ar":"سيلان أو طلاء يتفرق"},{"branch_id":"B006","branch_image_ar":"مشعل من جلود ينتبذ فيه"},{"branch_id":"B007","branch_image_ar":"أسماء مخصوصة منقولة"}],"mapped_root_id":"root_000799","mapped_root_norm":"ش ع ل"}]},{"root":"ر ء س","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرأس والأعلى"},{"branch_id":"B002","branch_image_ar":"الرئاسة والصدارة"},{"branch_id":"B003","branch_image_ar":"جمع السيل وحمله"},{"branch_id":"B004","branch_image_ar":"رِئاس الأمر ومن رأسه"},{"branch_id":"B005","branch_image_ar":"رِئاس السيف"},{"branch_id":"B006","branch_image_ar":"الرمي في الرأس"}],"mapped_root_id":"root_000529","mapped_root_norm":"ر ء س"}]},{"root":"ش ي ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"بياض الشعر والمشيب"},{"branch_id":"B002","branch_image_ar":"بياض الثلج والصقيع على الجبال والأرض"},{"branch_id":"B003","branch_image_ar":"ليلة شيباء"},{"branch_id":"B004","branch_image_ar":"حكاية صوت المشافر عند الشرب"}],"mapped_root_id":"root_000833","mapped_root_norm":"ش ي ب"}]},{"root":"ك و ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"وقوع الشيء وحضوره في زمان"},{"branch_id":"B002","branch_image_ar":"المكان والمكانة من الكون"},{"branch_id":"B003","branch_image_ar":"الكفالة والقيام على فلان"},{"branch_id":"B004","branch_image_ar":"الخضوع بالاستكانة"},{"branch_id":"B005","branch_image_ar":"الشيخ المنسوب إلى كُنْتُ"},{"branch_id":"B006","branch_image_ar":"حالة السوء بكينة"}],"mapped_root_id":"root_001332","mapped_root_norm":"ك و ن"}]},{"root":"د ع و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"النداء والإمالة بالكلام"},{"branch_id":"B002","branch_image_ar":"ادعاء الحق والانتساب"},{"branch_id":"B003","branch_image_ar":"داعية اللبن"},{"branch_id":"B004","branch_image_ar":"الدعاء بالمكروه النازل"},{"branch_id":"B005","branch_image_ar":"التداعي بالسقوط"},{"branch_id":"B006","branch_image_ar":"دواعي الدهر"},{"branch_id":"B007","branch_image_ar":"الأُدْعِيّة المعماة"},{"branch_id":"B008","branch_image_ar":"خلو الدار من داع"}],"mapped_root_id":"root_000478","mapped_root_norm":"د ع و"},{"branches":[{"branch_id":"B001","branch_image_ar":"الدَّعّ دفع شديد"},{"branch_id":"B002","branch_image_ar":"الدعدعة تحريك لامتلاء"},{"branch_id":"B003","branch_image_ar":"الدعدعة نداء وزجر"},{"branch_id":"B004","branch_image_ar":"دع دع للعاثر"},{"branch_id":"B005","branch_image_ar":"الدعدعة عدو ملتف بطيء"},{"branch_id":"B006","branch_image_ar":"الدعداع قصر الرجل"},{"branch_id":"B007","branch_image_ar":"الدعاع تفرق النخل"},{"branch_id":"B008","branch_image_ar":"الدعدع نبت مائي"},{"branch_id":"B009","branch_image_ar":"الدعاع عيال صغار"},{"branch_id":"B010","branch_image_ar":"الدعاع حبة برية"}],"mapped_root_id":"root_000477","mapped_root_norm":"د ع ع"}]},{"root":"ش ق و","targets":[{"branches":[{"branch_id":"B002","branch_image_ar":"مشقة العسر والمعاناة"},{"branch_id":"B003","branch_image_ar":"الغلبة في المشاقاة"},{"branch_id":"B004","branch_image_ar":"شاقي الجبل الطالع الطويل"}],"mapped_root_id":"root_000808","mapped_root_norm":"ش ق و"},{"branches":[{"branch_id":"B001","branch_image_ar":"الشقاوة وخلاف السعادة"},{"branch_id":"B002","branch_image_ar":"الشدة والعسر والعناء"},{"branch_id":"B003","branch_image_ar":"المشاقاة مصابرة ومعالجة"},{"branch_id":"B004","branch_image_ar":"الشاقي من حيود الجبال"}],"mapped_root_id":"root_000809","mapped_root_norm":"ش ق ي"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"19:4","surface_ref":"19:4"},{"ayah_ref":"19:5","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"19:5","root_occurrences":[{"lemmas_ar":["خَافَ"],"occurrence_count":1,"pos_tags":["V"],"root":"خ و ف","surfaces_ar":["خِفْ"],"word_indices":["2"]},{"lemmas_ar":["مَوَٰلِى","وَلِىّ"],"occurrence_count":2,"pos_tags":["N","N"],"root":"و ل ي","surfaces_ar":["مَوَٰلِىَ","وَلِيًّا"],"word_indices":["3","13"]},{"lemmas_ar":["وَرَآء"],"occurrence_count":1,"pos_tags":["N"],"root":"و ر ي","surfaces_ar":["وَرَآءِ"],"word_indices":["5"]},{"lemmas_ar":["كَانَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ك و ن","surfaces_ar":["كَانَتِ"],"word_indices":["6"]},{"lemmas_ar":["ٱمْرَأَت"],"occurrence_count":1,"pos_tags":["N"],"root":"م ر ء","surfaces_ar":["ٱمْرَأَتِ"],"word_indices":["7"]},{"lemmas_ar":["عَاقِر"],"occurrence_count":1,"pos_tags":["N"],"root":"ع ق ر","surfaces_ar":["عَاقِرًا"],"word_indices":["8"]},{"lemmas_ar":["وَهَبَ"],"occurrence_count":1,"pos_tags":["V"],"root":"و ه ب","surfaces_ar":["هَبْ"],"word_indices":["9"]},{"lemmas_ar":["لَّدُن"],"occurrence_count":1,"pos_tags":["N"],"root":"ل د ن","surfaces_ar":["لَّدُن"],"word_indices":["12"]}],"root_sequence":["خ و ف","و ل ي","و ر ي","ك و ن","م ر ء","ع ق ر","و ه ب","ل د ن","و ل ي"],"text_ar":"وَإِنِّى خِفْتُ ٱلْمَوَٰلِىَ مِن وَرَآءِى وَكَانَتِ ٱمْرَأَتِى عَاقِرًۭا فَهَبْ لِى مِن لَّدُنكَ وَلِيًّۭا"}],"context_order":["19:5"],"context_root_cues":[{"root":"خ و ف","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ذعر يتوقع المكروه"},{"branch_id":"B002","branch_image_ar":"إدخال الخوف في الغير"},{"branch_id":"B003","branch_image_ar":"مغالبة في الخوف"},{"branch_id":"B004","branch_image_ar":"نقص يأخذ من الشيء"},{"branch_id":"B005","branch_image_ar":"ظهور الخوف على الإنسان"},{"branch_id":"B006","branch_image_ar":"خافة العسال والسقاء"}],"mapped_root_id":"root_000447","mapped_root_norm":"خ و ف"}]},{"root":"و ل ي","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"قرب ودنو بلا فاصل"},{"branch_id":"B002","branch_image_ar":"تتابع شيء بعد شيء"},{"branch_id":"B003","branch_image_ar":"تولي الأمر والقيام عليه"},{"branch_id":"B004","branch_image_ar":"محبة ونصرة وموالاة"},{"branch_id":"B005","branch_image_ar":"ولاء قرابة وعتق وجوار"},{"branch_id":"B006","branch_image_ar":"تولية الوجه والإقبال"},{"branch_id":"B007","branch_image_ar":"الإدبار والإعراض"},{"branch_id":"B008","branch_image_ar":"الأولوية والاستحقاق"},{"branch_id":"B010","branch_image_ar":"مطر يلي الوسمي"},{"branch_id":"B011","branch_image_ar":"ولية تحت الرحل"},{"branch_id":"B012","branch_image_ar":"استيلاء وبلوغ غاية"},{"branch_id":"B013","branch_image_ar":"إيلاء وإسناد معروف أو شر"},{"branch_id":"B014","branch_image_ar":"تولية البيع"},{"branch_id":"B015","branch_image_ar":"موالاة صغار النعم عن كبارها"},{"branch_id":"B016","branch_image_ar":"ولي الرطب وتولى إذا هاج"}],"mapped_root_id":"root_001684","mapped_root_norm":"و ل ي"}]},{"root":"و ر ي","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"داء يأكل الجوف أو يصيب الرئة"},{"branch_id":"B002","branch_image_ar":"نار كامنة تخرج من الزند"},{"branch_id":"B003","branch_image_ar":"زند يقدح نجاحا أو نصرة"},{"branch_id":"B004","branch_image_ar":"شحم وار وسمن ظاهر"},{"branch_id":"B005","branch_image_ar":"ستر الشيء وجعله وراء الظهور"},{"branch_id":"B006","branch_image_ar":"الجانب الوراء: خلف أو أمام أو سوى"},{"branch_id":"B007","branch_image_ar":"ولد الولد يأتي من وراء الابن"},{"branch_id":"B008","branch_image_ar":"الورى: الخلق على ظهر الأرض"}],"mapped_root_id":"root_001642","mapped_root_norm":"و ر ي"}]},{"root":"ك و ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"وقوع الشيء وحضوره في زمان"},{"branch_id":"B002","branch_image_ar":"المكان والمكانة من الكون"},{"branch_id":"B003","branch_image_ar":"الكفالة والقيام على فلان"},{"branch_id":"B004","branch_image_ar":"الخضوع بالاستكانة"},{"branch_id":"B005","branch_image_ar":"الشيخ المنسوب إلى كُنْتُ"},{"branch_id":"B006","branch_image_ar":"حالة السوء بكينة"}],"mapped_root_id":"root_001332","mapped_root_norm":"ك و ن"}]},{"root":"م ر ء","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"المرء والمرأة"},{"branch_id":"B002","branch_image_ar":"المروءة"},{"branch_id":"B003","branch_image_ar":"الطعام المريء"},{"branch_id":"B004","branch_image_ar":"المريء"},{"branch_id":"B005","branch_image_ar":"الطعم والإطعام"}],"mapped_root_id":"root_001409","mapped_root_norm":"م ر ء"},{"branches":[{"branch_id":"B001","branch_image_ar":"المَرْء والمرأة"},{"branch_id":"B002","branch_image_ar":"المروءة وكمال الرجولية"},{"branch_id":"B003","branch_image_ar":"مراءة الطعام واستمراؤه"},{"branch_id":"B004","branch_image_ar":"الطعم والإطعام في مناسبة"},{"branch_id":"B005","branch_image_ar":"المَرِيء مجرى الطعام"},{"branch_id":"B006","branch_image_ar":"الرجل المَرِيء المقبول"}],"mapped_root_id":"root_001410","mapped_root_norm":"م ر ء"}]},{"root":"ع ق ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العَقْر جرح وهزم"},{"branch_id":"B002","branch_image_ar":"عَقْر قوائم الدابة"},{"branch_id":"B003","branch_image_ar":"عَقْر الظهر والحركة"},{"branch_id":"B004","branch_image_ar":"العُقْر انقطاع الولد"},{"branch_id":"B005","branch_image_ar":"بيضة العُقْر آخر لا يتلوه"},{"branch_id":"B006","branch_image_ar":"عَقْر المرأة عوض الفرج"},{"branch_id":"B007","branch_image_ar":"عَقْر النخل والطير"},{"branch_id":"B008","branch_image_ar":"عُقْرة تعقر البدن أو العلم"},{"branch_id":"B009","branch_image_ar":"رفع العَقيرة صوتا"},{"branch_id":"B010","branch_image_ar":"عَقْرا وعَقْرى دعاء"},{"branch_id":"B011","branch_image_ar":"المعاقرة منافرة وسباب"},{"branch_id":"B012","branch_image_ar":"العَقار خمر ملازمة"},{"branch_id":"B013","branch_image_ar":"عَقْر الشيء أصله"},{"branch_id":"B014","branch_image_ar":"العَقْر فرجة بين شيئين"},{"branch_id":"B015","branch_image_ar":"العَقْر قصر وملجأ"},{"branch_id":"B016","branch_image_ar":"العَقار ضيعة ومتاع"},{"branch_id":"B017","branch_image_ar":"العاقر رمل لا ينبت"},{"branch_id":"B018","branch_image_ar":"العَقْر غيم كالقصر"},{"branch_id":"B019","branch_image_ar":"العَقار ثوب أحمر"},{"branch_id":"B020","branch_image_ar":"العقرب من العَقْر"}],"mapped_root_id":"root_001035","mapped_root_norm":"ع ق ر"}]},{"root":"و ه ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"بذل الشيء هبة بلا عوض"},{"branch_id":"B002","branch_image_ar":"أخذ الهبة أو طلبها أو تبادلها"},{"branch_id":"B003","branch_image_ar":"نقرة في الصخر تمسك الماء"},{"branch_id":"B004","branch_image_ar":"ارتفاع المقدار وبلوغه"},{"branch_id":"B005","branch_image_ar":"تهيئة الشيء وإعداده"},{"branch_id":"B006","branch_image_ar":"فرض الشيء في الذهن والحسبان"},{"branch_id":"B007","branch_image_ar":"دوام الشيء وثباته"}],"mapped_root_id":"root_001685","mapped_root_norm":"و ه ب"}]},{"root":"ل د ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"اللَّدَانة واللين"},{"branch_id":"B002","branch_image_ar":"قرب من حد وابتداء نهاية"},{"branch_id":"B003","branch_image_ar":"التلبث والتلكؤ"}],"mapped_root_id":"root_004482","mapped_root_norm":"ل د ن"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"19:5","surface_ref":"19:5"},{"ayah_ref":"19:6","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"19:6","root_occurrences":[{"lemmas_ar":["وَرِثَ","وَرِثَ"],"occurrence_count":2,"pos_tags":["V","V"],"root":"و ر ث","surfaces_ar":["يَرِثُ","يَرِثُ"],"word_indices":["1","2"]},{"lemmas_ar":["ءَال"],"occurrence_count":1,"pos_tags":["N"],"root":"ء و ل","surfaces_ar":["ءَالِ"],"word_indices":["4"]},{"lemmas_ar":["جَعَلَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ج ع ل","surfaces_ar":["ٱجْعَلْ"],"word_indices":["6"]},{"lemmas_ar":["رَبّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ر ب ب","surfaces_ar":["رَبِّ"],"word_indices":["7"]},{"lemmas_ar":["رَضِيّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ر ض و","surfaces_ar":["رَضِيًّا"],"word_indices":["8"]}],"root_sequence":["و ر ث","و ر ث","ء و ل","ج ع ل","ر ب ب","ر ض و"],"text_ar":"يَرِثُنِى وَيَرِثُ مِنْ ءَالِ يَعْقُوبَ ۖ وَٱجْعَلْهُ رَبِّ رَضِيًّۭا"}],"context_order":["19:6"],"context_root_cues":[{"root":"و ر ث","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"انتقال ميراث من سابق إلى وارث"},{"branch_id":"B002","branch_image_ar":"تمليك الشيء وإخلافه بلا عقد أو كلفة"},{"branch_id":"B003","branch_image_ar":"انتقال علم أو كتاب أو فضيلة ميراثا"},{"branch_id":"B005","branch_image_ar":"إثارة جمر النار لتشتعل"}],"mapped_root_id":"root_001639","mapped_root_norm":"و ر ث"}]},{"root":"ء و ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ابتداء الشيء وتقدمه"},{"branch_id":"B002","branch_image_ar":"رجوع الشيء إلى مآله وعاقبته"},{"branch_id":"B003","branch_image_ar":"آل الرجل من يرجع إليهم ويرجعون إليه"},{"branch_id":"B004","branch_image_ar":"إيالة الأمر بإصلاحه وسياسته"},{"branch_id":"B005","branch_image_ar":"خثور السائل وانعقاده في آخر أمره"},{"branch_id":"B007","branch_image_ar":"آلة الحال التي يكون عليها الشيء"},{"branch_id":"B008","branch_image_ar":"الآلة الحاملة أو الأداة"},{"branch_id":"B009","branch_image_ar":"الأيل الذي يأوي إلى الجبل"},{"branch_id":"B010","branch_image_ar":"الإيال وعاء الشراب حتى يجود"}],"mapped_root_id":"root_000067","mapped_root_norm":"ء و ل"}]},{"root":"ج ع ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"إحداث الشيء وصنعه"},{"branch_id":"B002","branch_image_ar":"تصيير الشيء على حال"},{"branch_id":"B004","branch_image_ar":"الشروع في الفعل أو ملازمته"},{"branch_id":"B005","branch_image_ar":"أجر مجعول على عمل"},{"branch_id":"B006","branch_image_ar":"النخل الصغار أو القصار"},{"branch_id":"B007","branch_image_ar":"خرقة إنزال القدر"},{"branch_id":"B008","branch_image_ar":"دويبة الجعلان"},{"branch_id":"B009","branch_image_ar":"اشتهاء الأنثى للفحل"},{"branch_id":"B010","branch_image_ar":"فرخ النعام"},{"branch_id":"B011","branch_image_ar":"الجَعْلة اسم مكان"},{"branch_id":"B012","branch_image_ar":"قصر مع سمن ولجاج"}],"mapped_root_id":"root_000248","mapped_root_norm":"ج ع ل"}]},{"root":"ر ب ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ربوبية وملك وسيادة"},{"branch_id":"B002","branch_image_ar":"إصلاح وتربية وإتمام"},{"branch_id":"B003","branch_image_ar":"علم رباني"},{"branch_id":"B004","branch_image_ar":"ربة وجماعات كثيرة"},{"branch_id":"B005","branch_image_ar":"ربيب وربيبة ورابة"},{"branch_id":"B006","branch_image_ar":"رُبّ خاثر وإصلاح به"},{"branch_id":"B007","branch_image_ar":"لزوم وإقامة ودوام"},{"branch_id":"B008","branch_image_ar":"رباب السحاب"},{"branch_id":"B009","branch_image_ar":"شاة رُبّى وحداثة"},{"branch_id":"B010","branch_image_ar":"ربابة تجمع القداح"},{"branch_id":"B011","branch_image_ar":"ربابة عهد وميثاق"},{"branch_id":"B012","branch_image_ar":"ربة نبات"},{"branch_id":"B013","branch_image_ar":"ماء رَبَب كثير"},{"branch_id":"B014","branch_image_ar":"رَبْرَب قطيع"},{"branch_id":"B015","branch_image_ar":"حرف رب وربما"},{"branch_id":"B016","branch_image_ar":"رُبَى حاجة وعقدة ونعمة"},{"branch_id":"B017","branch_image_ar":"رباني الملاحين"}],"mapped_root_id":"root_000532","mapped_root_norm":"ر ب ب"},{"branches":[{"branch_id":"B001","branch_image_ar":"زيادة وعلو"},{"branch_id":"B002","branch_image_ar":"أرض مرتفعة"},{"branch_id":"B003","branch_image_ar":"زيادة الربا في المعاملة"},{"branch_id":"B004","branch_image_ar":"تصعد النفس وانتفاخه"},{"branch_id":"B005","branch_image_ar":"تغذية ونشوء"},{"branch_id":"B006","branch_image_ar":"نتوء أصل الفخذ"},{"branch_id":"B007","branch_image_ar":"أهل البيت من بني الأعمام"}],"mapped_root_id":"root_000537","mapped_root_norm":"ر ب و"}]},{"root":"ر ض و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرضا خلاف السخط"},{"branch_id":"B002","branch_image_ar":"الرضوان والمرضاة اسم للرضا الكثير أو المطلوب"},{"branch_id":"B003","branch_image_ar":"المراضاة والتراضي رضا متبادل"},{"branch_id":"B004","branch_image_ar":"الإرضاء طلب رضا الغير وإزالة سخطه"},{"branch_id":"B005","branch_image_ar":"راضاني فرضوته غلبة في ذلك"},{"branch_id":"B006","branch_image_ar":"الرضي صفة للمطيع أو المحب أو الضامن"},{"branch_id":"B007","branch_image_ar":"رضوى ورضيا أعلام من المادة"}],"mapped_root_id":"root_000569","mapped_root_norm":"ر ض و"},{"branches":[{"branch_id":"B001","branch_image_ar":"الرِّضا خلاف السخط والقبول"},{"branch_id":"B002","branch_image_ar":"غلبة راضاني فرضوته"},{"branch_id":"B003","branch_image_ar":"رضوى ورضيا أسماء"},{"branch_id":"B004","branch_image_ar":"الرَّضِيّ طاعة ومحبة وضمان"}],"mapped_root_id":"root_000570","mapped_root_norm":"ر ض ي"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"19:6","surface_ref":"19:6"},{"ayah_ref":"19:7","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"19:7","root_occurrences":[{"lemmas_ar":["بُشِّرَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ب ش ر","surfaces_ar":["نُبَشِّرُ"],"word_indices":["3"]},{"lemmas_ar":["غُلَٰم"],"occurrence_count":1,"pos_tags":["N"],"root":"غ ل م","surfaces_ar":["غُلَٰمٍ"],"word_indices":["4"]},{"lemmas_ar":["ٱسْم","سَمِيّ"],"occurrence_count":2,"pos_tags":["N","N"],"root":"س م و","surfaces_ar":["ٱسْمُ","سَمِيًّا"],"word_indices":["5","12"]},{"lemmas_ar":["جَعَلَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ج ع ل","surfaces_ar":["نَجْعَل"],"word_indices":["8"]},{"lemmas_ar":["قَبْل"],"occurrence_count":1,"pos_tags":["N"],"root":"ق ب ل","surfaces_ar":["قَبْلُ"],"word_indices":["11"]}],"root_sequence":["ب ش ر","غ ل م","س م و","ج ع ل","ق ب ل","س م و"],"text_ar":"يَٰزَكَرِيَّآ إِنَّا نُبَشِّرُكَ بِغُلَٰمٍ ٱسْمُهُۥ يَحْيَىٰ لَمْ نَجْعَل لَّهُۥ مِن قَبْلُ سَمِيًّۭا"}],"context_order":["19:7"],"context_root_cues":[{"root":"ب ش ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ظهور البشرة والسطح"},{"branch_id":"B002","branch_image_ar":"الإنسان الظاهر الجلد"},{"branch_id":"B003","branch_image_ar":"التقاء البشرة بالبشرة"},{"branch_id":"B004","branch_image_ar":"إزالة البشرة عن السطح"},{"branch_id":"B005","branch_image_ar":"خبر يفتح البشرة بالسرور"},{"branch_id":"B006","branch_image_ar":"طلاقة الوجه وحسن الهيئة"},{"branch_id":"B007","branch_image_ar":"طلائع الشيء وأوائله"},{"branch_id":"B008","branch_image_ar":"كمال يجمع الظاهر والباطن"}],"mapped_root_id":"root_000120","mapped_root_norm":"ب ش ر"}]},{"root":"غ ل م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"حداثة الغلام"},{"branch_id":"B002","branch_image_ar":"هيجان الشهوة"},{"branch_id":"B003","branch_image_ar":"اشتداد الشراب"},{"branch_id":"B004","branch_image_ar":"ذَكَر السلاحف"},{"branch_id":"B005","branch_image_ar":"موضع اسمه الغيلم"},{"branch_id":"B006","branch_image_ar":"المدرى المسمى الغيلم"}],"mapped_root_id":"root_001103","mapped_root_norm":"غ ل م"}]},{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ج ع ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"إحداث الشيء وصنعه"},{"branch_id":"B002","branch_image_ar":"تصيير الشيء على حال"},{"branch_id":"B004","branch_image_ar":"الشروع في الفعل أو ملازمته"},{"branch_id":"B005","branch_image_ar":"أجر مجعول على عمل"},{"branch_id":"B006","branch_image_ar":"النخل الصغار أو القصار"},{"branch_id":"B007","branch_image_ar":"خرقة إنزال القدر"},{"branch_id":"B008","branch_image_ar":"دويبة الجعلان"},{"branch_id":"B009","branch_image_ar":"اشتهاء الأنثى للفحل"},{"branch_id":"B010","branch_image_ar":"فرخ النعام"},{"branch_id":"B011","branch_image_ar":"الجَعْلة اسم مكان"},{"branch_id":"B012","branch_image_ar":"قصر مع سمن ولجاج"}],"mapped_root_id":"root_000248","mapped_root_norm":"ج ع ل"}]},{"root":"ق ب ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"مواجهة الشيء للشيء"},{"branch_id":"B002","branch_image_ar":"تقدم الشيء أو إقباله"},{"branch_id":"B003","branch_image_ar":"جهة الشيء وعنده"},{"branch_id":"B004","branch_image_ar":"قبول الشيء برضا"},{"branch_id":"B005","branch_image_ar":"جهة الصلاة المتوجه إليها"},{"branch_id":"B006","branch_image_ar":"قبلة الفم والتقبيل"},{"branch_id":"B007","branch_image_ar":"تلقي الخارج إلى اليد"},{"branch_id":"B008","branch_image_ar":"ضمان الشيء والتكفل به"},{"branch_id":"B009","branch_image_ar":"جماعة يقبل بعضها على بعض"},{"branch_id":"B010","branch_image_ar":"أجزاء موصولة يقابل بعضها بعضا"},{"branch_id":"B011","branch_image_ar":"إقبال العضو أو العلامة إلى جهة"},{"branch_id":"B012","branch_image_ar":"ريح تقابل الدبور"},{"branch_id":"B013","branch_image_ar":"طاقة على المقابلة"},{"branch_id":"B014","branch_image_ar":"سقي على أفواه الإبل"},{"branch_id":"B015","branch_image_ar":"ابتداء حاضر غير مهيأ"},{"branch_id":"B016","branch_image_ar":"خرزة تقبل وجها إلى وجه"}],"mapped_root_id":"root_001198","mapped_root_norm":"ق ب ل"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"19:7","surface_ref":"19:7"},{"ayah_ref":"19:8","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"19:8","root_occurrences":[{"lemmas_ar":["قَالَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ق و ل","surfaces_ar":["قَالَ"],"word_indices":["1"]},{"lemmas_ar":["رَبّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ر ب ب","surfaces_ar":["رَبِّ"],"word_indices":["2"]},{"lemmas_ar":["أَنَّىٰ"],"occurrence_count":1,"pos_tags":["INTG"],"root":"ء ن ي","surfaces_ar":["أَنَّىٰ"],"word_indices":["3"]},{"lemmas_ar":["كَانَ","كَانَ"],"occurrence_count":2,"pos_tags":["V","V"],"root":"ك و ن","surfaces_ar":["يَكُونُ","كَانَتِ"],"word_indices":["4","7"]},{"lemmas_ar":["غُلَٰم"],"occurrence_count":1,"pos_tags":["N"],"root":"غ ل م","surfaces_ar":["غُلَٰمٌ"],"word_indices":["6"]},{"lemmas_ar":["ٱمْرَأَت"],"occurrence_count":1,"pos_tags":["N"],"root":"م ر ء","surfaces_ar":["ٱمْرَأَتِ"],"word_indices":["8"]},{"lemmas_ar":["عَاقِر"],"occurrence_count":1,"pos_tags":["N"],"root":"ع ق ر","surfaces_ar":["عَاقِرًا"],"word_indices":["9"]},{"lemmas_ar":["بَلَغَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ب ل غ","surfaces_ar":["بَلَغْ"],"word_indices":["11"]},{"lemmas_ar":["كِبَر"],"occurrence_count":1,"pos_tags":["N"],"root":"ك ب ر","surfaces_ar":["كِبَرِ"],"word_indices":["13"]},{"lemmas_ar":["عِتِيّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ع ت و","surfaces_ar":["عِتِيًّا"],"word_indices":["14"]}],"root_sequence":["ق و ل","ر ب ب","ء ن ي","ك و ن","غ ل م","ك و ن","م ر ء","ع ق ر","ب ل غ","ك ب ر","ع ت و"],"text_ar":"قَالَ رَبِّ أَنَّىٰ يَكُونُ لِى غُلَٰمٌۭ وَكَانَتِ ٱمْرَأَتِى عَاقِرًۭا وَقَدْ بَلَغْتُ مِنَ ٱلْكِبَرِ عِتِيًّۭا"}],"context_order":["19:8"],"context_root_cues":[{"root":"ق و ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"إخراج القول بالنطق"},{"branch_id":"B002","branch_image_ar":"اللسان آلة القول"},{"branch_id":"B003","branch_image_ar":"كثرة القول في صاحبه"},{"branch_id":"B004","branch_image_ar":"القيل صاحب القول النافذ"},{"branch_id":"B005","branch_image_ar":"قول ما لم يكن أو نسبته"},{"branch_id":"B006","branch_image_ar":"اجترار القول إلى النفس"},{"branch_id":"B007","branch_image_ar":"القول الفاشي بين الناس"},{"branch_id":"B008","branch_image_ar":"عود القال لضرب القلة"},{"branch_id":"B009","branch_image_ar":"المقاولة في الأمر"},{"branch_id":"B010","branch_image_ar":"اقتالة الحكم على غيره"},{"branch_id":"B011","branch_image_ar":"قول يجري مجرى الظن"},{"branch_id":"B012","branch_image_ar":"قول في النفس لم يظهر"},{"branch_id":"B013","branch_image_ar":"القول اعتقاد ومذهب"},{"branch_id":"B014","branch_image_ar":"قول الشيء دلالته"},{"branch_id":"B015","branch_image_ar":"العناية الصادقة بالشيء"},{"branch_id":"B016","branch_image_ar":"قول الشيء حده"}],"mapped_root_id":"root_001272","mapped_root_norm":"ق و ل"},{"branches":[{"branch_id":"B001","branch_image_ar":"القِلَّة والضآلة"},{"branch_id":"B002","branch_image_ar":"قُلَّة الشيء ورأسه"},{"branch_id":"B003","branch_image_ar":"القُلَّة الجرة الكبيرة"},{"branch_id":"B004","branch_image_ar":"الإقلال والاستقلال حملا ونهوضا"},{"branch_id":"B005","branch_image_ar":"القِلُّ رعدة واضطراب"},{"branch_id":"B006","branch_image_ar":"القلقلة اضطراب وتحرك"}],"mapped_root_id":"root_001251","mapped_root_norm":"ق ل ل"}]},{"root":"ر ب ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ربوبية وملك وسيادة"},{"branch_id":"B002","branch_image_ar":"إصلاح وتربية وإتمام"},{"branch_id":"B003","branch_image_ar":"علم رباني"},{"branch_id":"B004","branch_image_ar":"ربة وجماعات كثيرة"},{"branch_id":"B005","branch_image_ar":"ربيب وربيبة ورابة"},{"branch_id":"B006","branch_image_ar":"رُبّ خاثر وإصلاح به"},{"branch_id":"B007","branch_image_ar":"لزوم وإقامة ودوام"},{"branch_id":"B008","branch_image_ar":"رباب السحاب"},{"branch_id":"B009","branch_image_ar":"شاة رُبّى وحداثة"},{"branch_id":"B010","branch_image_ar":"ربابة تجمع القداح"},{"branch_id":"B011","branch_image_ar":"ربابة عهد وميثاق"},{"branch_id":"B012","branch_image_ar":"ربة نبات"},{"branch_id":"B013","branch_image_ar":"ماء رَبَب كثير"},{"branch_id":"B014","branch_image_ar":"رَبْرَب قطيع"},{"branch_id":"B015","branch_image_ar":"حرف رب وربما"},{"branch_id":"B016","branch_image_ar":"رُبَى حاجة وعقدة ونعمة"},{"branch_id":"B017","branch_image_ar":"رباني الملاحين"}],"mapped_root_id":"root_000532","mapped_root_norm":"ر ب ب"},{"branches":[{"branch_id":"B001","branch_image_ar":"زيادة وعلو"},{"branch_id":"B002","branch_image_ar":"أرض مرتفعة"},{"branch_id":"B003","branch_image_ar":"زيادة الربا في المعاملة"},{"branch_id":"B004","branch_image_ar":"تصعد النفس وانتفاخه"},{"branch_id":"B005","branch_image_ar":"تغذية ونشوء"},{"branch_id":"B006","branch_image_ar":"نتوء أصل الفخذ"},{"branch_id":"B007","branch_image_ar":"أهل البيت من بني الأعمام"}],"mapped_root_id":"root_000537","mapped_root_norm":"ر ب و"}]},{"root":"ء ن ي","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الأناة والإبطاء"},{"branch_id":"B002","branch_image_ar":"آناء الليل"},{"branch_id":"B003","branch_image_ar":"بلوغ الإنى"},{"branch_id":"B004","branch_image_ar":"الإناء الوعاء"},{"branch_id":"B005","branch_image_ar":"أنى للسؤال"}],"mapped_root_id":"root_000063","mapped_root_norm":"ء ن ي"},{"branches":[{"branch_id":"B001","branch_image_ar":"الرِّفق والدَّعة"},{"branch_id":"B002","branch_image_ar":"جانب الحمل وعِدله"},{"branch_id":"B003","branch_image_ar":"الأوان والحين"},{"branch_id":"B004","branch_image_ar":"الإيوان والبناء المعقود"}],"mapped_root_id":"root_000068","mapped_root_norm":"ء و ن"}]},{"root":"ك و ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"وقوع الشيء وحضوره في زمان"},{"branch_id":"B002","branch_image_ar":"المكان والمكانة من الكون"},{"branch_id":"B003","branch_image_ar":"الكفالة والقيام على فلان"},{"branch_id":"B004","branch_image_ar":"الخضوع بالاستكانة"},{"branch_id":"B005","branch_image_ar":"الشيخ المنسوب إلى كُنْتُ"},{"branch_id":"B006","branch_image_ar":"حالة السوء بكينة"}],"mapped_root_id":"root_001332","mapped_root_norm":"ك و ن"}]},{"root":"غ ل م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"حداثة الغلام"},{"branch_id":"B002","branch_image_ar":"هيجان الشهوة"},{"branch_id":"B003","branch_image_ar":"اشتداد الشراب"},{"branch_id":"B004","branch_image_ar":"ذَكَر السلاحف"},{"branch_id":"B005","branch_image_ar":"موضع اسمه الغيلم"},{"branch_id":"B006","branch_image_ar":"المدرى المسمى الغيلم"}],"mapped_root_id":"root_001103","mapped_root_norm":"غ ل م"}]},{"root":"م ر ء","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"المرء والمرأة"},{"branch_id":"B002","branch_image_ar":"المروءة"},{"branch_id":"B003","branch_image_ar":"الطعام المريء"},{"branch_id":"B004","branch_image_ar":"المريء"},{"branch_id":"B005","branch_image_ar":"الطعم والإطعام"}],"mapped_root_id":"root_001409","mapped_root_norm":"م ر ء"},{"branches":[{"branch_id":"B001","branch_image_ar":"المَرْء والمرأة"},{"branch_id":"B002","branch_image_ar":"المروءة وكمال الرجولية"},{"branch_id":"B003","branch_image_ar":"مراءة الطعام واستمراؤه"},{"branch_id":"B004","branch_image_ar":"الطعم والإطعام في مناسبة"},{"branch_id":"B005","branch_image_ar":"المَرِيء مجرى الطعام"},{"branch_id":"B006","branch_image_ar":"الرجل المَرِيء المقبول"}],"mapped_root_id":"root_001410","mapped_root_norm":"م ر ء"}]},{"root":"ع ق ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العَقْر جرح وهزم"},{"branch_id":"B002","branch_image_ar":"عَقْر قوائم الدابة"},{"branch_id":"B003","branch_image_ar":"عَقْر الظهر والحركة"},{"branch_id":"B004","branch_image_ar":"العُقْر انقطاع الولد"},{"branch_id":"B005","branch_image_ar":"بيضة العُقْر آخر لا يتلوه"},{"branch_id":"B006","branch_image_ar":"عَقْر المرأة عوض الفرج"},{"branch_id":"B007","branch_image_ar":"عَقْر النخل والطير"},{"branch_id":"B008","branch_image_ar":"عُقْرة تعقر البدن أو العلم"},{"branch_id":"B009","branch_image_ar":"رفع العَقيرة صوتا"},{"branch_id":"B010","branch_image_ar":"عَقْرا وعَقْرى دعاء"},{"branch_id":"B011","branch_image_ar":"المعاقرة منافرة وسباب"},{"branch_id":"B012","branch_image_ar":"العَقار خمر ملازمة"},{"branch_id":"B013","branch_image_ar":"عَقْر الشيء أصله"},{"branch_id":"B014","branch_image_ar":"العَقْر فرجة بين شيئين"},{"branch_id":"B015","branch_image_ar":"العَقْر قصر وملجأ"},{"branch_id":"B016","branch_image_ar":"العَقار ضيعة ومتاع"},{"branch_id":"B017","branch_image_ar":"العاقر رمل لا ينبت"},{"branch_id":"B018","branch_image_ar":"العَقْر غيم كالقصر"},{"branch_id":"B019","branch_image_ar":"العَقار ثوب أحمر"},{"branch_id":"B020","branch_image_ar":"العقرب من العَقْر"}],"mapped_root_id":"root_001035","mapped_root_norm":"ع ق ر"}]},{"root":"ب ل غ","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الوصول إلى الغاية"},{"branch_id":"B002","branch_image_ar":"إيصال الرسالة"},{"branch_id":"B003","branch_image_ar":"الكفاية التي يتبلغ بها"},{"branch_id":"B004","branch_image_ar":"الفصاحة التي تبلغ المراد"},{"branch_id":"B005","branch_image_ar":"الجودة البالغة"},{"branch_id":"B006","branch_image_ar":"إدراك المراد مع الحمق"},{"branch_id":"B007","branch_image_ar":"مد الفارس عنانه لزيادة العدو"},{"branch_id":"B008","branch_image_ar":"اشتداد العلة أو القلة"},{"branch_id":"B009","branch_image_ar":"سماع المكروه بلا بلوغ"},{"branch_id":"B010","branch_image_ar":"البلاغات الوشايات"},{"branch_id":"B011","branch_image_ar":"البُلغين الداهية"}],"mapped_root_id":"root_000151","mapped_root_norm":"ب ل غ"}]},{"root":"ك ب ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العظم خلاف الصغر"},{"branch_id":"B002","branch_image_ar":"معظم الأمر"},{"branch_id":"B003","branch_image_ar":"إعظام الشيء في الصدر"},{"branch_id":"B004","branch_image_ar":"كبر السن والقدم"},{"branch_id":"B005","branch_image_ar":"رفعة الشرف والرئاسة"},{"branch_id":"B006","branch_image_ar":"العظمة والكبرياء"},{"branch_id":"B007","branch_image_ar":"الإثم الكبير والذنوب الكبائر"},{"branch_id":"B010","branch_image_ar":"الكبر مشقة وثقل"},{"branch_id":"B011","branch_image_ar":"المكابرة والغلبة"},{"branch_id":"B012","branch_image_ar":"الكَبَر طبل"},{"branch_id":"B013","branch_image_ar":"أكبر النهار"}],"mapped_root_id":"root_001281","mapped_root_norm":"ك ب ر"}]},{"root":"ع ت و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العُتُوّ عن الطاعة"},{"branch_id":"B002","branch_image_ar":"العُتِيّ من الكبر"}],"mapped_root_id":"root_000981","mapped_root_norm":"ع ت و"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"19:8","surface_ref":"19:8"},{"ayah_ref":"19:9","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"19:9","root_occurrences":[{"lemmas_ar":["قَالَ","قَالَ"],"occurrence_count":2,"pos_tags":["V","V"],"root":"ق و ل","surfaces_ar":["قَالَ","قَالَ"],"word_indices":["1","3"]},{"lemmas_ar":["رَبّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ر ب ب","surfaces_ar":["رَبُّ"],"word_indices":["4"]},{"lemmas_ar":["هَيِّن"],"occurrence_count":1,"pos_tags":["N"],"root":"ه و ن","surfaces_ar":["هَيِّنٌ"],"word_indices":["7"]},{"lemmas_ar":["خَلَقَ"],"occurrence_count":1,"pos_tags":["V"],"root":"خ ل ق","surfaces_ar":["خَلَقْ"],"word_indices":["9"]},{"lemmas_ar":["قَبْل"],"occurrence_count":1,"pos_tags":["N"],"root":"ق ب ل","surfaces_ar":["قَبْلُ"],"word_indices":["11"]},{"lemmas_ar":["كَانَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ك و ن","surfaces_ar":["تَكُ"],"word_indices":["13"]},{"lemmas_ar":["شَىْء"],"occurrence_count":1,"pos_tags":["N"],"root":"ش ي ء","surfaces_ar":["شَيْـًٔا"],"word_indices":["14"]}],"root_sequence":["ق و ل","ق و ل","ر ب ب","ه و ن","خ ل ق","ق ب ل","ك و ن","ش ي ء"],"text_ar":"قَالَ كَذَٰلِكَ قَالَ رَبُّكَ هُوَ عَلَىَّ هَيِّنٌۭ وَقَدْ خَلَقْتُكَ مِن قَبْلُ وَلَمْ تَكُ شَيْـًۭٔا"}],"context_order":["19:9"],"context_root_cues":[{"root":"ق و ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"إخراج القول بالنطق"},{"branch_id":"B002","branch_image_ar":"اللسان آلة القول"},{"branch_id":"B003","branch_image_ar":"كثرة القول في صاحبه"},{"branch_id":"B004","branch_image_ar":"القيل صاحب القول النافذ"},{"branch_id":"B005","branch_image_ar":"قول ما لم يكن أو نسبته"},{"branch_id":"B006","branch_image_ar":"اجترار القول إلى النفس"},{"branch_id":"B007","branch_image_ar":"القول الفاشي بين الناس"},{"branch_id":"B008","branch_image_ar":"عود القال لضرب القلة"},{"branch_id":"B009","branch_image_ar":"المقاولة في الأمر"},{"branch_id":"B010","branch_image_ar":"اقتالة الحكم على غيره"},{"branch_id":"B011","branch_image_ar":"قول يجري مجرى الظن"},{"branch_id":"B012","branch_image_ar":"قول في النفس لم يظهر"},{"branch_id":"B013","branch_image_ar":"القول اعتقاد ومذهب"},{"branch_id":"B014","branch_image_ar":"قول الشيء دلالته"},{"branch_id":"B015","branch_image_ar":"العناية الصادقة بالشيء"},{"branch_id":"B016","branch_image_ar":"قول الشيء حده"}],"mapped_root_id":"root_001272","mapped_root_norm":"ق و ل"},{"branches":[{"branch_id":"B001","branch_image_ar":"القِلَّة والضآلة"},{"branch_id":"B002","branch_image_ar":"قُلَّة الشيء ورأسه"},{"branch_id":"B003","branch_image_ar":"القُلَّة الجرة الكبيرة"},{"branch_id":"B004","branch_image_ar":"الإقلال والاستقلال حملا ونهوضا"},{"branch_id":"B005","branch_image_ar":"القِلُّ رعدة واضطراب"},{"branch_id":"B006","branch_image_ar":"القلقلة اضطراب وتحرك"}],"mapped_root_id":"root_001251","mapped_root_norm":"ق ل ل"}]},{"root":"ر ب ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ربوبية وملك وسيادة"},{"branch_id":"B002","branch_image_ar":"إصلاح وتربية وإتمام"},{"branch_id":"B003","branch_image_ar":"علم رباني"},{"branch_id":"B004","branch_image_ar":"ربة وجماعات كثيرة"},{"branch_id":"B005","branch_image_ar":"ربيب وربيبة ورابة"},{"branch_id":"B006","branch_image_ar":"رُبّ خاثر وإصلاح به"},{"branch_id":"B007","branch_image_ar":"لزوم وإقامة ودوام"},{"branch_id":"B008","branch_image_ar":"رباب السحاب"},{"branch_id":"B009","branch_image_ar":"شاة رُبّى وحداثة"},{"branch_id":"B010","branch_image_ar":"ربابة تجمع القداح"},{"branch_id":"B011","branch_image_ar":"ربابة عهد وميثاق"},{"branch_id":"B012","branch_image_ar":"ربة نبات"},{"branch_id":"B013","branch_image_ar":"ماء رَبَب كثير"},{"branch_id":"B014","branch_image_ar":"رَبْرَب قطيع"},{"branch_id":"B015","branch_image_ar":"حرف رب وربما"},{"branch_id":"B016","branch_image_ar":"رُبَى حاجة وعقدة ونعمة"},{"branch_id":"B017","branch_image_ar":"رباني الملاحين"}],"mapped_root_id":"root_000532","mapped_root_norm":"ر ب ب"},{"branches":[{"branch_id":"B001","branch_image_ar":"زيادة وعلو"},{"branch_id":"B002","branch_image_ar":"أرض مرتفعة"},{"branch_id":"B003","branch_image_ar":"زيادة الربا في المعاملة"},{"branch_id":"B004","branch_image_ar":"تصعد النفس وانتفاخه"},{"branch_id":"B005","branch_image_ar":"تغذية ونشوء"},{"branch_id":"B006","branch_image_ar":"نتوء أصل الفخذ"},{"branch_id":"B007","branch_image_ar":"أهل البيت من بني الأعمام"}],"mapped_root_id":"root_000537","mapped_root_norm":"ر ب و"}]},{"root":"ه و ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"حقارة وضعف في الشيء"},{"branch_id":"B002","branch_image_ar":"خدمة وحذاقة في العمل"},{"branch_id":"B003","branch_image_ar":"جذب الثوب"},{"branch_id":"B004","branch_image_ar":"حلب الإبل عند الصدر"},{"branch_id":"B005","branch_image_ar":"ابتذال الشيء بالاستخدام"},{"branch_id":"B006","branch_image_ar":"ماء قليل ضعيف لا يلقح"}],"mapped_root_id":"root_001453","mapped_root_norm":"م ه ن"},{"branches":[{"branch_id":"B001","branch_image_ar":"سكينة ووقار في لين"},{"branch_id":"B002","branch_image_ar":"خفة الأمر وسهولته"},{"branch_id":"B003","branch_image_ar":"هوان ومهانة باستخفاف"},{"branch_id":"B004","branch_image_ar":"الهاوون أداة الدق"}],"mapped_root_id":"root_001608","mapped_root_norm":"ه و ن"},{"branches":[{"branch_id":"B001","branch_image_ar":"ضعف القوة وفتور العزم"},{"branch_id":"B002","branch_image_ar":"ساعة من الليل تمضي"},{"branch_id":"B003","branch_image_ar":"الواهنة موضع في الأضلاع والصدر"},{"branch_id":"B004","branch_image_ar":"وجع الواهنة وداؤها"},{"branch_id":"B005","branch_image_ar":"فتور المرأة وثقل حركتها"},{"branch_id":"B006","branch_image_ar":"كثافة الإبل"},{"branch_id":"B007","branch_image_ar":"الوهين حاث الأجير"},{"branch_id":"B008","branch_image_ar":"كلام باطل يتعلل به"},{"branch_id":"B009","branch_image_ar":"ثقل الطائر عن النهوض"}],"mapped_root_id":"root_001687","mapped_root_norm":"و ه ن"}]},{"root":"خ ل ق","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"تقدير الشيء وقياسه"},{"branch_id":"B002","branch_image_ar":"إبداع الخلق وإيجاده"},{"branch_id":"B003","branch_image_ar":"تمام الخلقة واعتدال الصورة"},{"branch_id":"B004","branch_image_ar":"السجية والطبيعة الباطنة"},{"branch_id":"B005","branch_image_ar":"الجدارة والتهيؤ للشيء"},{"branch_id":"B007","branch_image_ar":"اختلاق الكذب والكلام"},{"branch_id":"B008","branch_image_ar":"ملاسة السطح واستواؤه"},{"branch_id":"B009","branch_image_ar":"بلى الثوب وذهاب وبره"},{"branch_id":"B010","branch_image_ar":"الخلوق والتخليق بالطيب"},{"branch_id":"B011","branch_image_ar":"نقرة أو بئر تمسك الماء"},{"branch_id":"B012","branch_image_ar":"انسداد مصمت كالصخرة"}],"mapped_root_id":"root_000434","mapped_root_norm":"خ ل ق"}]},{"root":"ق ب ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"مواجهة الشيء للشيء"},{"branch_id":"B002","branch_image_ar":"تقدم الشيء أو إقباله"},{"branch_id":"B003","branch_image_ar":"جهة الشيء وعنده"},{"branch_id":"B004","branch_image_ar":"قبول الشيء برضا"},{"branch_id":"B005","branch_image_ar":"جهة الصلاة المتوجه إليها"},{"branch_id":"B006","branch_image_ar":"قبلة الفم والتقبيل"},{"branch_id":"B007","branch_image_ar":"تلقي الخارج إلى اليد"},{"branch_id":"B008","branch_image_ar":"ضمان الشيء والتكفل به"},{"branch_id":"B009","branch_image_ar":"جماعة يقبل بعضها على بعض"},{"branch_id":"B010","branch_image_ar":"أجزاء موصولة يقابل بعضها بعضا"},{"branch_id":"B011","branch_image_ar":"إقبال العضو أو العلامة إلى جهة"},{"branch_id":"B012","branch_image_ar":"ريح تقابل الدبور"},{"branch_id":"B013","branch_image_ar":"طاقة على المقابلة"},{"branch_id":"B014","branch_image_ar":"سقي على أفواه الإبل"},{"branch_id":"B015","branch_image_ar":"ابتداء حاضر غير مهيأ"},{"branch_id":"B016","branch_image_ar":"خرزة تقبل وجها إلى وجه"}],"mapped_root_id":"root_001198","mapped_root_norm":"ق ب ل"}]},{"root":"ك و ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"وقوع الشيء وحضوره في زمان"},{"branch_id":"B002","branch_image_ar":"المكان والمكانة من الكون"},{"branch_id":"B003","branch_image_ar":"الكفالة والقيام على فلان"},{"branch_id":"B004","branch_image_ar":"الخضوع بالاستكانة"},{"branch_id":"B005","branch_image_ar":"الشيخ المنسوب إلى كُنْتُ"},{"branch_id":"B006","branch_image_ar":"حالة السوء بكينة"}],"mapped_root_id":"root_001332","mapped_root_norm":"ك و ن"}]},{"root":"ش ي ء","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الشيء المعلوم المخبر عنه"},{"branch_id":"B002","branch_image_ar":"المشيئة المتعلّقة بالشيء"},{"branch_id":"B003","branch_image_ar":"حمل الشيء إلى الأمر"},{"branch_id":"B004","branch_image_ar":"تشويه الخلق وقبحه"},{"branch_id":"B005","branch_image_ar":"انجذاب النفس إلى الشيء"},{"branch_id":"B006","branch_image_ar":"إصغاء السمع"},{"branch_id":"B007","branch_image_ar":"بعد النظر في الفرس"},{"branch_id":"B008","branch_image_ar":"صغار النخل"},{"branch_id":"B009","branch_image_ar":"نداء التلهف والتعجب"}],"mapped_root_id":"root_000831","mapped_root_norm":"ش ي ء"},{"branches":[{"branch_id":"B001","branch_image_ar":"المشيئة"},{"branch_id":"B002","branch_image_ar":"تشويه الخلق والوجه"},{"branch_id":"B003","branch_image_ar":"بعد النظر"},{"branch_id":"B004","branch_image_ar":"الإعجاب والسرور"},{"branch_id":"B005","branch_image_ar":"الاستماع"},{"branch_id":"B006","branch_image_ar":"صغار النخل"},{"branch_id":"B007","branch_image_ar":"التلهف والتعجب"}],"mapped_root_id":"root_000832","mapped_root_norm":"ش ي ء"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"19:9","surface_ref":"19:9"},{"ayah_ref":"19:10","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"19:10","root_occurrences":[{"lemmas_ar":["قَالَ","قَالَ"],"occurrence_count":2,"pos_tags":["V","V"],"root":"ق و ل","surfaces_ar":["قَالَ","قَالَ"],"word_indices":["1","6"]},{"lemmas_ar":["رَبّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ر ب ب","surfaces_ar":["رَبِّ"],"word_indices":["2"]},{"lemmas_ar":["جَعَلَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ج ع ل","surfaces_ar":["ٱجْعَل"],"word_indices":["3"]},{"lemmas_ar":["ءَايَة","ءَايَة"],"occurrence_count":2,"pos_tags":["N","N"],"root":"ء ي ي","surfaces_ar":["ءَايَةً","ءَايَتُ"],"word_indices":["5","7"]},{"lemmas_ar":["كَلَّمَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ك ل م","surfaces_ar":["تُكَلِّمَ"],"word_indices":["9"]},{"lemmas_ar":["نَّاس"],"occurrence_count":1,"pos_tags":["N"],"root":"ن و س","surfaces_ar":["نَّاسَ"],"word_indices":["10"]},{"lemmas_ar":["ثَلَٰث"],"occurrence_count":1,"pos_tags":["T"],"root":"ث ل ث","surfaces_ar":["ثَلَٰثَ"],"word_indices":["11"]},{"lemmas_ar":["لَيْل"],"occurrence_count":1,"pos_tags":["N"],"root":"ل ي ل","surfaces_ar":["لَيَالٍ"],"word_indices":["12"]},{"lemmas_ar":["سَوِيّ"],"occurrence_count":1,"pos_tags":["N"],"root":"س و ي","surfaces_ar":["سَوِيًّا"],"word_indices":["13"]}],"root_sequence":["ق و ل","ر ب ب","ج ع ل","ء ي ي","ق و ل","ء ي ي","ك ل م","ن و س","ث ل ث","ل ي ل","س و ي"],"text_ar":"قَالَ رَبِّ ٱجْعَل لِّىٓ ءَايَةًۭ ۚ قَالَ ءَايَتُكَ أَلَّا تُكَلِّمَ ٱلنَّاسَ ثَلَٰثَ لَيَالٍۢ سَوِيًّۭا"}],"context_order":["19:10"],"context_root_cues":[{"root":"ق و ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"إخراج القول بالنطق"},{"branch_id":"B002","branch_image_ar":"اللسان آلة القول"},{"branch_id":"B003","branch_image_ar":"كثرة القول في صاحبه"},{"branch_id":"B004","branch_image_ar":"القيل صاحب القول النافذ"},{"branch_id":"B005","branch_image_ar":"قول ما لم يكن أو نسبته"},{"branch_id":"B006","branch_image_ar":"اجترار القول إلى النفس"},{"branch_id":"B007","branch_image_ar":"القول الفاشي بين الناس"},{"branch_id":"B008","branch_image_ar":"عود القال لضرب القلة"},{"branch_id":"B009","branch_image_ar":"المقاولة في الأمر"},{"branch_id":"B010","branch_image_ar":"اقتالة الحكم على غيره"},{"branch_id":"B011","branch_image_ar":"قول يجري مجرى الظن"},{"branch_id":"B012","branch_image_ar":"قول في النفس لم يظهر"},{"branch_id":"B013","branch_image_ar":"القول اعتقاد ومذهب"},{"branch_id":"B014","branch_image_ar":"قول الشيء دلالته"},{"branch_id":"B015","branch_image_ar":"العناية الصادقة بالشيء"},{"branch_id":"B016","branch_image_ar":"قول الشيء حده"}],"mapped_root_id":"root_001272","mapped_root_norm":"ق و ل"},{"branches":[{"branch_id":"B001","branch_image_ar":"القِلَّة والضآلة"},{"branch_id":"B002","branch_image_ar":"قُلَّة الشيء ورأسه"},{"branch_id":"B003","branch_image_ar":"القُلَّة الجرة الكبيرة"},{"branch_id":"B004","branch_image_ar":"الإقلال والاستقلال حملا ونهوضا"},{"branch_id":"B005","branch_image_ar":"القِلُّ رعدة واضطراب"},{"branch_id":"B006","branch_image_ar":"القلقلة اضطراب وتحرك"}],"mapped_root_id":"root_001251","mapped_root_norm":"ق ل ل"}]},{"root":"ر ب ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ربوبية وملك وسيادة"},{"branch_id":"B002","branch_image_ar":"إصلاح وتربية وإتمام"},{"branch_id":"B003","branch_image_ar":"علم رباني"},{"branch_id":"B004","branch_image_ar":"ربة وجماعات كثيرة"},{"branch_id":"B005","branch_image_ar":"ربيب وربيبة ورابة"},{"branch_id":"B006","branch_image_ar":"رُبّ خاثر وإصلاح به"},{"branch_id":"B007","branch_image_ar":"لزوم وإقامة ودوام"},{"branch_id":"B008","branch_image_ar":"رباب السحاب"},{"branch_id":"B009","branch_image_ar":"شاة رُبّى وحداثة"},{"branch_id":"B010","branch_image_ar":"ربابة تجمع القداح"},{"branch_id":"B011","branch_image_ar":"ربابة عهد وميثاق"},{"branch_id":"B012","branch_image_ar":"ربة نبات"},{"branch_id":"B013","branch_image_ar":"ماء رَبَب كثير"},{"branch_id":"B014","branch_image_ar":"رَبْرَب قطيع"},{"branch_id":"B015","branch_image_ar":"حرف رب وربما"},{"branch_id":"B016","branch_image_ar":"رُبَى حاجة وعقدة ونعمة"},{"branch_id":"B017","branch_image_ar":"رباني الملاحين"}],"mapped_root_id":"root_000532","mapped_root_norm":"ر ب ب"},{"branches":[{"branch_id":"B001","branch_image_ar":"زيادة وعلو"},{"branch_id":"B002","branch_image_ar":"أرض مرتفعة"},{"branch_id":"B003","branch_image_ar":"زيادة الربا في المعاملة"},{"branch_id":"B004","branch_image_ar":"تصعد النفس وانتفاخه"},{"branch_id":"B005","branch_image_ar":"تغذية ونشوء"},{"branch_id":"B006","branch_image_ar":"نتوء أصل الفخذ"},{"branch_id":"B007","branch_image_ar":"أهل البيت من بني الأعمام"}],"mapped_root_id":"root_000537","mapped_root_norm":"ر ب و"}]},{"root":"ج ع ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"إحداث الشيء وصنعه"},{"branch_id":"B002","branch_image_ar":"تصيير الشيء على حال"},{"branch_id":"B004","branch_image_ar":"الشروع في الفعل أو ملازمته"},{"branch_id":"B005","branch_image_ar":"أجر مجعول على عمل"},{"branch_id":"B006","branch_image_ar":"النخل الصغار أو القصار"},{"branch_id":"B007","branch_image_ar":"خرقة إنزال القدر"},{"branch_id":"B008","branch_image_ar":"دويبة الجعلان"},{"branch_id":"B009","branch_image_ar":"اشتهاء الأنثى للفحل"},{"branch_id":"B010","branch_image_ar":"فرخ النعام"},{"branch_id":"B011","branch_image_ar":"الجَعْلة اسم مكان"},{"branch_id":"B012","branch_image_ar":"قصر مع سمن ولجاج"}],"mapped_root_id":"root_000248","mapped_root_norm":"ج ع ل"}]},{"root":"ء ي ي","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"تمهل وانتظار"},{"branch_id":"B002","branch_image_ar":"تعمد آية الشخص"},{"branch_id":"B003","branch_image_ar":"علامة ظاهرة"},{"branch_id":"B004","branch_image_ar":"أي للسؤال والتعيين"},{"branch_id":"B005","branch_image_ar":"إيا عماد للضمير"},{"branch_id":"B006","branch_image_ar":"أيان للزمان"},{"branch_id":"B007","branch_image_ar":"كأين لعدد كثير"},{"branch_id":"B008","branch_image_ar":"أي وأيا للنداء"},{"branch_id":"B009","branch_image_ar":"أي مفسرة"},{"branch_id":"B010","branch_image_ar":"إي افتتاح للقسم"}],"mapped_root_id":"root_000074","mapped_root_norm":"ء ي ي"}]},{"root":"ك ل م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"نطق مفهم يصل بين متكلمين"},{"branch_id":"B002","branch_image_ar":"لفظة مفهمة تتسع لعبارة أو قول"},{"branch_id":"B003","branch_image_ar":"أثر جارح في الجسد"}],"mapped_root_id":"root_001316","mapped_root_norm":"ك ل م"}]},{"root":"ن و س","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ظهور الإنسان المخالف للتوحش والجن"},{"branch_id":"B002","branch_image_ar":"إيناس الشيء برؤية أو إحساس أو سماع"},{"branch_id":"B003","branch_image_ar":"الأنس الذي يزيل الوحشة"},{"branch_id":"B004","branch_image_ar":"الجانب الإنسي المقبل على الإنسان"},{"branch_id":"B005","branch_image_ar":"إنسان العين وصورة الإنسان في السواد"},{"branch_id":"B006","branch_image_ar":"ابن الإنس للنفس والصفوة"},{"branch_id":"B007","branch_image_ar":"الاستئناس قبل دخول البيوت"}],"mapped_root_id":"root_000059","mapped_root_norm":"ء ن س"},{"branches":[{"branch_id":"B001","branch_image_ar":"تذبذب الشيء المتدلّي"},{"branch_id":"B002","branch_image_ar":"سوق الإبل"}],"mapped_root_id":"root_004965","mapped_root_norm":"ن و س"}]},{"root":"ث ل ث","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العدد ثلاثة"},{"branch_id":"B002","branch_image_ar":"الجزء الثالث"},{"branch_id":"B003","branch_image_ar":"الثالث المكمل"},{"branch_id":"B004","branch_image_ar":"شيء على ثلاثة أجزاء"},{"branch_id":"B005","branch_image_ar":"الناقة الثلوث"},{"branch_id":"B006","branch_image_ar":"يوم الثلاثاء"},{"branch_id":"B007","branch_image_ar":"ثالثة الأثافي"},{"branch_id":"B008","branch_image_ar":"المثلث من الشراب"}],"mapped_root_id":"root_000203","mapped_root_norm":"ث ل ث"}]},{"root":"ل ي ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الليل خلاف النهار وظلمته"},{"branch_id":"B002","branch_image_ar":"مزاولة الأمر في الليل"},{"branch_id":"B003","branch_image_ar":"الليلة القريبة من اليوم"},{"branch_id":"B004","branch_image_ar":"التسمية بليلى"}],"mapped_root_id":"root_001392","mapped_root_norm":"ل ي ل"}]},{"root":"س و ي","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"مساواة ومعادلة بين شيئين"},{"branch_id":"B002","branch_image_ar":"استقامة وتمام في الذات"},{"branch_id":"B003","branch_image_ar":"علو واستقرار على شيء"},{"branch_id":"B004","branch_image_ar":"إقبال وقصد إلى جهة"},{"branch_id":"B005","branch_image_ar":"بلوغ وتمام الشباب"},{"branch_id":"B006","branch_image_ar":"وسط وعدل ومكان منصف"},{"branch_id":"B007","branch_image_ar":"مباينة وكون الشيء غيره"},{"branch_id":"B008","branch_image_ar":"قصد نحو شخص أو جهة"},{"branch_id":"B009","branch_image_ar":"السِيّ واسع أملس من الأرض"},{"branch_id":"B010","branch_image_ar":"السَّويّة على ظهر البعير"},{"branch_id":"B012","branch_image_ar":"ليلة استواء القمر"},{"branch_id":"B013","branch_image_ar":"سِيّ الرأس وقدر يوازي الرأس من مال أو نعمة"}],"mapped_root_id":"root_000766","mapped_root_norm":"س و ي"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"19:10","surface_ref":"19:10"},{"ayah_ref":"19:11","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"19:11","root_occurrences":[{"lemmas_ar":["خَرَجَ"],"occurrence_count":1,"pos_tags":["V"],"root":"خ ر ج","surfaces_ar":["خَرَجَ"],"word_indices":["1"]},{"lemmas_ar":["قَوْم"],"occurrence_count":1,"pos_tags":["N"],"root":"ق و م","surfaces_ar":["قَوْمِ"],"word_indices":["3"]},{"lemmas_ar":["مِحْرَاب"],"occurrence_count":1,"pos_tags":["N"],"root":"ح ر ب","surfaces_ar":["مِحْرَابِ"],"word_indices":["5"]},{"lemmas_ar":["أَوْحَىٰٓ"],"occurrence_count":1,"pos_tags":["V"],"root":"و ح ي","surfaces_ar":["أَوْحَىٰٓ"],"word_indices":["6"]},{"lemmas_ar":["سَبَّحَ"],"occurrence_count":1,"pos_tags":["V"],"root":"س ب ح","surfaces_ar":["سَبِّحُ"],"word_indices":["9"]},{"lemmas_ar":["بُكْرَة"],"occurrence_count":1,"pos_tags":["T"],"root":"ب ك ر","surfaces_ar":["بُكْرَةً"],"word_indices":["10"]},{"lemmas_ar":["عَشِىّ"],"occurrence_count":1,"pos_tags":["T"],"root":"ع ش و","surfaces_ar":["عَشِيًّا"],"word_indices":["11"]}],"root_sequence":["خ ر ج","ق و م","ح ر ب","و ح ي","س ب ح","ب ك ر","ع ش و"],"text_ar":"فَخَرَجَ عَلَىٰ قَوْمِهِۦ مِنَ ٱلْمِحْرَابِ فَأَوْحَىٰٓ إِلَيْهِمْ أَن سَبِّحُوا۟ بُكْرَةًۭ وَعَشِيًّۭا"}],"context_order":["19:11"],"context_root_cues":[{"root":"خ ر ج","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"النفاذ إلى خارج الشيء"},{"branch_id":"B002","branch_image_ar":"إخراج الشيء من خفائه"},{"branch_id":"B003","branch_image_ar":"مال يخرج على جهة معلومة"},{"branch_id":"B004","branch_image_ar":"قُرْح يخرج في الجسد"},{"branch_id":"B005","branch_image_ar":"ظهور السحاب وانكشاف السماء"},{"branch_id":"B006","branch_image_ar":"خروج عن الأصل أو الطاعة"},{"branch_id":"B007","branch_image_ar":"اختلاف لونين في الشيء"},{"branch_id":"B008","branch_image_ar":"خروج الخلقة عن نوعها"},{"branch_id":"B009","branch_image_ar":"خرج الوعاء ذو الأونين"},{"branch_id":"B010","branch_image_ar":"لعبة إخراج ما في اليد"},{"branch_id":"B011","branch_image_ar":"ألف الخروج بعد الصلة"},{"branch_id":"B012","branch_image_ar":"تخارج الشركاء في النصيب"},{"branch_id":"B013","branch_image_ar":"عنق خارج يغتال العنان"}],"mapped_root_id":"root_000400","mapped_root_norm":"خ ر ج"}]},{"root":"ق و م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"جماعة الناس والرجال"},{"branch_id":"B002","branch_image_ar":"انتصاب وقيام بالبدن"},{"branch_id":"B003","branch_image_ar":"عزم ونهوض إلى الأمر"},{"branch_id":"B004","branch_image_ar":"رعاية وحفظ وولاية"},{"branch_id":"B006","branch_image_ar":"مقام وإقامة في موضع"},{"branch_id":"B007","branch_image_ar":"نيابة وقيام مقام غيره"},{"branch_id":"B008","branch_image_ar":"استقامة واعتدال واستواء"},{"branch_id":"B009","branch_image_ar":"قوام وعماد ومعاش"},{"branch_id":"B010","branch_image_ar":"قيمة وتقويم وتسعير"},{"branch_id":"B011","branch_image_ar":"قامة وقوام الجسم والطول"},{"branch_id":"B012","branch_image_ar":"آلة قائمة وجزء قائم"},{"branch_id":"B013","branch_image_ar":"قيامة وبعث وقيام الساعة"},{"branch_id":"B014","branch_image_ar":"مقاومة ومنازلة"},{"branch_id":"B015","branch_image_ar":"وزن سواء ومقدار معتدل"},{"branch_id":"B016","branch_image_ar":"جمود ووقوف وكلال"},{"branch_id":"B017","branch_image_ar":"انتصاف النهار وقائم الظهيرة"},{"branch_id":"B018","branch_image_ar":"نفاق السوق"},{"branch_id":"B019","branch_image_ar":"وجع قائم بالعضو"},{"branch_id":"B020","branch_image_ar":"قوام في قوائم الشاة"},{"branch_id":"B021","branch_image_ar":"عين قائمة ذاهبة البصر"}],"mapped_root_id":"root_001273","mapped_root_norm":"ق و م"}]},{"root":"ح ر ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"السلب وأخذ المال"},{"branch_id":"B002","branch_image_ar":"الحرب والعداوة"},{"branch_id":"B003","branch_image_ar":"إثارة العداوة والغضب"},{"branch_id":"B004","branch_image_ar":"الحربة وحد السنان"},{"branch_id":"B006","branch_image_ar":"الحرباء وما يشبهها"},{"branch_id":"B009","branch_image_ar":"الأعلام والمواضع"}],"mapped_root_id":"root_000302","mapped_root_norm":"ح ر ب"}]},{"root":"و ح ي","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"إلقاء علم في خفاء"},{"branch_id":"B002","branch_image_ar":"إشارة وإيماء"},{"branch_id":"B003","branch_image_ar":"كتابة ونقش"},{"branch_id":"B004","branch_image_ar":"نبأ وإلهام من الله"},{"branch_id":"B005","branch_image_ar":"صوت خفي"},{"branch_id":"B006","branch_image_ar":"سرعة وعجلة"},{"branch_id":"B007","branch_image_ar":"استيحاء طلبا"},{"branch_id":"B008","branch_image_ar":"ملك كنار"},{"branch_id":"B009","branch_image_ar":"نياحة وبكاء"},{"branch_id":"B010","branch_image_ar":"وحي في حجر"}],"mapped_root_id":"root_001633","mapped_root_norm":"و ح ي"}]},{"root":"س ب ح","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العبادة بالتسبيح والصلاة"},{"branch_id":"B002","branch_image_ar":"التنزيه والتبرئة"},{"branch_id":"B004","branch_image_ar":"السبح في الجري والعوم"},{"branch_id":"B005","branch_image_ar":"السعة للذهاب والمعاش"},{"branch_id":"B006","branch_image_ar":"خرز التسبيح"},{"branch_id":"B007","branch_image_ar":"سباح الجلود والكساء"},{"branch_id":"B008","branch_image_ar":"سبوحة الموضع"}],"mapped_root_id":"root_000666","mapped_root_norm":"س ب ح"}]},{"root":"ب ك ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"البكرة أول النهار"},{"branch_id":"B002","branch_image_ar":"أول الشيء وباكورته"},{"branch_id":"B003","branch_image_ar":"فتاء الحيوان قبل التمام"},{"branch_id":"B004","branch_image_ar":"البكارة وعدم المساس"},{"branch_id":"B005","branch_image_ar":"الولد الأول والولادة الأولى"},{"branch_id":"B006","branch_image_ar":"البَكْرَة الدوارة"},{"branch_id":"B007","branch_image_ar":"المجيء على بَكْرَة واحدة"}],"mapped_root_id":"root_000143","mapped_root_norm":"ب ك ر"}]},{"root":"ع ش و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ظلام العِشاء وقلة الوضوح"},{"branch_id":"B002","branch_image_ar":"القصد إلى نار الليل"},{"branch_id":"B003","branch_image_ar":"التعامي والإعراض"},{"branch_id":"B004","branch_image_ar":"وقت العشي والعشاء"},{"branch_id":"B005","branch_image_ar":"طعام العشاء وتعشي الراعية"},{"branch_id":"B006","branch_image_ar":"ضعف البصر والعشا"},{"branch_id":"B007","branch_image_ar":"خبط العشواء"},{"branch_id":"B008","branch_image_ar":"الرفق بالشيء"}],"mapped_root_id":"root_001017","mapped_root_norm":"ع ش و"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"19:11","surface_ref":"19:11"},{"ayah_ref":"19:12","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"19:12","root_occurrences":[{"lemmas_ar":["أَخَذَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ء خ ذ","surfaces_ar":["خُذِ"],"word_indices":["2"]},{"lemmas_ar":["كِتَٰب"],"occurrence_count":1,"pos_tags":["N"],"root":"ك ت ب","surfaces_ar":["كِتَٰبَ"],"word_indices":["3"]},{"lemmas_ar":["قُوَّة"],"occurrence_count":1,"pos_tags":["N"],"root":"ق و ي","surfaces_ar":["قُوَّةٍ"],"word_indices":["4"]},{"lemmas_ar":["آتَى"],"occurrence_count":1,"pos_tags":["V"],"root":"ء ت ي","surfaces_ar":["ءَاتَيْ"],"word_indices":["5"]},{"lemmas_ar":["حُكْم"],"occurrence_count":1,"pos_tags":["N"],"root":"ح ك م","surfaces_ar":["حُكْمَ"],"word_indices":["6"]},{"lemmas_ar":["صَبِيّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ص ب و","surfaces_ar":["صَبِيًّا"],"word_indices":["7"]}],"root_sequence":["ء خ ذ","ك ت ب","ق و ي","ء ت ي","ح ك م","ص ب و"],"text_ar":"يَٰيَحْيَىٰ خُذِ ٱلْكِتَٰبَ بِقُوَّةٍۢ ۖ وَءَاتَيْنَٰهُ ٱلْحُكْمَ صَبِيًّۭا"}],"context_order":["19:12"],"context_root_cues":[{"root":"ء خ ذ","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"حوز الشيء وتناوله"},{"branch_id":"B002","branch_image_ar":"المؤاخذة بالذنب"},{"branch_id":"B003","branch_image_ar":"القبض والأسر"},{"branch_id":"B004","branch_image_ar":"رقية تمسك وتحبس"},{"branch_id":"B005","branch_image_ar":"أرض مأخوذة للنفس"},{"branch_id":"B006","branch_image_ar":"موضع يمسك الماء"},{"branch_id":"B007","branch_image_ar":"حال تأخذ في الجسم"},{"branch_id":"B008","branch_image_ar":"أخذ القمر في منازله"},{"branch_id":"B009","branch_image_ar":"الأخذ بالسيرة والشكل"},{"branch_id":"B010","branch_image_ar":"الاتخاذ والاكتساب"},{"branch_id":"B011","branch_image_ar":"أخذة المصارعة"},{"branch_id":"B012","branch_image_ar":"مقبض الشيء المأخوذ به"}],"mapped_root_id":"root_000018","mapped_root_norm":"ء خ ذ"}]},{"root":"ك ت ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ضم شيء إلى شيء"},{"branch_id":"B002","branch_image_ar":"نظم الحروف واسم المكتوب"},{"branch_id":"B003","branch_image_ar":"إثبات يوجب حكما أو قدرا"},{"branch_id":"B004","branch_image_ar":"إدخال الاسم في سجل أو زمرة"},{"branch_id":"B005","branch_image_ar":"مكاتبة العبد على عتقه"}],"mapped_root_id":"root_001283","mapped_root_norm":"ك ت ب"}]},{"root":"ق و ي","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"شدّة مجتمعة كطاقات الحبل"},{"branch_id":"B002","branch_image_ar":"نقص أو اضطراب في قوى البيت الشعري"},{"branch_id":"B003","branch_image_ar":"قفر خال يقل فيه الخير"},{"branch_id":"B004","branch_image_ar":"تقاو في ثمن المشترك حتى يأخذه أحدهم"},{"branch_id":"B005","branch_image_ar":"تقاوي الدلو بشرب مائها"},{"branch_id":"B006","branch_image_ar":"قوي يخرج من قاوية خلت عنه"}],"mapped_root_id":"root_001274","mapped_root_norm":"ق و ي"}]},{"root":"ء ت ي","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الإتيان والمجيء"},{"branch_id":"B002","branch_image_ar":"الإيتاء والإعطاء"},{"branch_id":"B003","branch_image_ar":"مأتى الأمر وتهيؤه"},{"branch_id":"B004","branch_image_ar":"مجرى الماء وتسليك سبيله"},{"branch_id":"B005","branch_image_ar":"السيل الآتي من غير البلد"},{"branch_id":"B006","branch_image_ar":"الغريب الداخل في غير قومه"},{"branch_id":"B007","branch_image_ar":"خروج النماء والنتاج"},{"branch_id":"B008","branch_image_ar":"الإتاوة المؤداة"},{"branch_id":"B009","branch_image_ar":"رجع يدي الناقة في السير"},{"branch_id":"B010","branch_image_ar":"الميتاء طريق ومحاذاة"},{"branch_id":"B011","branch_image_ar":"إتيان البلاء والهلاك"},{"branch_id":"B012","branch_image_ar":"استئتاء الناقة"},{"branch_id":"B013","branch_image_ar":"نَفاذ الرجل"}],"mapped_root_id":"root_000009","mapped_root_norm":"ء ت ي"}]},{"root":"ح ك م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"المنع والرد للإصلاح"},{"branch_id":"B002","branch_image_ar":"الحكم والقضاء بين الناس"},{"branch_id":"B003","branch_image_ar":"الحكمة والعلم المصيب"},{"branch_id":"B004","branch_image_ar":"الإحكام والإتقان والوثاقة"},{"branch_id":"B005","branch_image_ar":"التفويض والتحكيم"},{"branch_id":"B006","branch_image_ar":"حكمة اللجام"}],"mapped_root_id":"root_000348","mapped_root_norm":"ح ك م"}]},{"root":"ص ب و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الصغر والصبيان"},{"branch_id":"B002","branch_image_ar":"ميل القلب وصبوة الفتوة"},{"branch_id":"B003","branch_image_ar":"ريح الصبا"},{"branch_id":"B004","branch_image_ar":"الإمالة والقلب حسا"},{"branch_id":"B005","branch_image_ar":"أطراف دقيقة تسمى صبيانا"}],"mapped_root_id":"root_000843","mapped_root_norm":"ص ب و"},{"branches":[{"branch_id":"B001","branch_image_ar":"إراقة الشيء وانصبابه"},{"branch_id":"B002","branch_image_ar":"حدور ومنصب"},{"branch_id":"B003","branch_image_ar":"صبابة باقية"},{"branch_id":"B004","branch_image_ar":"انصباب القلب بالهوى"},{"branch_id":"B005","branch_image_ar":"صبة مجتمعة"},{"branch_id":"B006","branch_image_ar":"صبيب أحمر أو عصارة"},{"branch_id":"B007","branch_image_ar":"ذهاب الصبابة وتفرقها"},{"branch_id":"B008","branch_image_ar":"انصباب الحية على الملدوغ"},{"branch_id":"B009","branch_image_ar":"صب في القيد"},{"branch_id":"B010","branch_image_ar":"سير صبصاب"},{"branch_id":"B011","branch_image_ar":"عثو في الغنم"}],"mapped_root_id":"root_000838","mapped_root_norm":"ص ب ب"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"19:12","surface_ref":"19:12"},{"ayah_ref":"19:13","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"19:13","root_occurrences":[{"lemmas_ar":["حَنَان"],"occurrence_count":1,"pos_tags":["N"],"root":"ح ن ن","surfaces_ar":["حَنَانًا"],"word_indices":["1"]},{"lemmas_ar":["لَّدُن"],"occurrence_count":1,"pos_tags":["N"],"root":"ل د ن","surfaces_ar":["لَّدُنَّ"],"word_indices":["3"]},{"lemmas_ar":["زَكَوٰة"],"occurrence_count":1,"pos_tags":["N"],"root":"ز ك و","surfaces_ar":["زَكَوٰةً"],"word_indices":["4"]},{"lemmas_ar":["كَانَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ك و ن","surfaces_ar":["كَانَ"],"word_indices":["5"]},{"lemmas_ar":["تَقِيّ"],"occurrence_count":1,"pos_tags":["N"],"root":"و ق ي","surfaces_ar":["تَقِيًّا"],"word_indices":["6"]}],"root_sequence":["ح ن ن","ل د ن","ز ك و","ك و ن","و ق ي"],"text_ar":"وَحَنَانًۭا مِّن لَّدُنَّا وَزَكَوٰةًۭ ۖ وَكَانَ تَقِيًّۭا"}],"context_order":["19:13"],"context_root_cues":[{"root":"ح ن ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرقة والرحمة المتحننة"},{"branch_id":"B002","branch_image_ar":"نزاع الشوق إلى المألوف"},{"branch_id":"B003","branch_image_ar":"الصوت الحاني الرنان"},{"branch_id":"B004","branch_image_ar":"الألفة الزوجية والحنانة"},{"branch_id":"B005","branch_image_ar":"الصد والصرف عن الشيء"},{"branch_id":"B006","branch_image_ar":"الحن وجنس الجن"},{"branch_id":"B007","branch_image_ar":"الأعلام والمواضع والأنساب"},{"branch_id":"B008","branch_image_ar":"الحانة والآنة في المال"},{"branch_id":"B010","branch_image_ar":"أمثال الخيبة والدعوى"}],"mapped_root_id":"root_000364","mapped_root_norm":"ح ن ن"}]},{"root":"ل د ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"اللَّدَانة واللين"},{"branch_id":"B002","branch_image_ar":"قرب من حد وابتداء نهاية"},{"branch_id":"B003","branch_image_ar":"التلبث والتلكؤ"}],"mapped_root_id":"root_004482","mapped_root_norm":"ل د ن"}]},{"root":"ز ك و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"النماء والزيادة"},{"branch_id":"B002","branch_image_ar":"الطهارة والصلاح"},{"branch_id":"B004","branch_image_ar":"الملاءمة واللياقة"},{"branch_id":"B005","branch_image_ar":"الزوج والشفع"}],"mapped_root_id":"root_000637","mapped_root_norm":"ز ك و"}]},{"root":"ك و ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"وقوع الشيء وحضوره في زمان"},{"branch_id":"B002","branch_image_ar":"المكان والمكانة من الكون"},{"branch_id":"B003","branch_image_ar":"الكفالة والقيام على فلان"},{"branch_id":"B004","branch_image_ar":"الخضوع بالاستكانة"},{"branch_id":"B005","branch_image_ar":"الشيخ المنسوب إلى كُنْتُ"},{"branch_id":"B006","branch_image_ar":"حالة السوء بكينة"}],"mapped_root_id":"root_001332","mapped_root_norm":"ك و ن"}]},{"root":"و ق ي","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"دفع الضرر بوقاية"},{"branch_id":"B002","branch_image_ar":"جعل النفس في وقاية"},{"branch_id":"B003","branch_image_ar":"توقي الدابة من وجع الحافر"},{"branch_id":"B004","branch_image_ar":"الأوقية وزن معلوم"},{"branch_id":"B005","branch_image_ar":"الواقي اسم للصرد"}],"mapped_root_id":"root_001677","mapped_root_norm":"و ق ي"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"19:13","surface_ref":"19:13"},{"ayah_ref":"19:14","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"19:14","root_occurrences":[{"lemmas_ar":["بَرّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ب ر ر","surfaces_ar":["بَرًّۢا"],"word_indices":["1"]},{"lemmas_ar":["وَٰلِدَي"],"occurrence_count":1,"pos_tags":["N"],"root":"و ل د","surfaces_ar":["وَٰلِدَيْ"],"word_indices":["2"]},{"lemmas_ar":["كَانَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ك و ن","surfaces_ar":["يَكُن"],"word_indices":["4"]},{"lemmas_ar":["جَبَّار"],"occurrence_count":1,"pos_tags":["N"],"root":"ج ب ر","surfaces_ar":["جَبَّارًا"],"word_indices":["5"]},{"lemmas_ar":["عَصِيّ"],"occurrence_count":1,"pos_tags":["ADJ"],"root":"ع ص ي","surfaces_ar":["عَصِيًّا"],"word_indices":["6"]}],"root_sequence":["ب ر ر","و ل د","ك و ن","ج ب ر","ع ص ي"],"text_ar":"وَبَرًّۢا بِوَٰلِدَيْهِ وَلَمْ يَكُن جَبَّارًا عَصِيًّۭا"}],"context_order":["19:14"],"context_root_cues":[{"root":"ب ر ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"صدق يمضي القول والعمل"},{"branch_id":"B002","branch_image_ar":"خير وطاعة متسعة"},{"branch_id":"B003","branch_image_ar":"صلة وإحسان ضد العقوق"},{"branch_id":"B004","branch_image_ar":"صوت وجلبة باللسان"},{"branch_id":"B005","branch_image_ar":"يابسة وصحراء"},{"branch_id":"B006","branch_image_ar":"حب وحنطة"},{"branch_id":"B007","branch_image_ar":"ثمر الأراك"},{"branch_id":"B008","branch_image_ar":"غلبة وعلو"}],"mapped_root_id":"root_000104","mapped_root_norm":"ب ر ر"}]},{"root":"و ل د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"مولود من نسل"},{"branch_id":"B002","branch_image_ar":"أبوان من جهة الولادة"},{"branch_id":"B003","branch_image_ar":"حدوث الولادة ووضع الحمل"},{"branch_id":"B004","branch_image_ar":"صغير قريب العهد بالولادة أو مملوك"},{"branch_id":"B005","branch_image_ar":"شيء حاصل عن شيء أو مستحدث منه"},{"branch_id":"B006","branch_image_ar":"قرين في سن الولادة"}],"mapped_root_id":"root_001683","mapped_root_norm":"و ل د"}]},{"root":"ك و ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"وقوع الشيء وحضوره في زمان"},{"branch_id":"B002","branch_image_ar":"المكان والمكانة من الكون"},{"branch_id":"B003","branch_image_ar":"الكفالة والقيام على فلان"},{"branch_id":"B004","branch_image_ar":"الخضوع بالاستكانة"},{"branch_id":"B005","branch_image_ar":"الشيخ المنسوب إلى كُنْتُ"},{"branch_id":"B006","branch_image_ar":"حالة السوء بكينة"}],"mapped_root_id":"root_001332","mapped_root_norm":"ك و ن"}]},{"root":"ج ب ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"جبر الكسر والنقص"},{"branch_id":"B003","branch_image_ar":"قهر الإجبار والإكراه"},{"branch_id":"B004","branch_image_ar":"هدر الجبار"},{"branch_id":"B005","branch_image_ar":"جبائر الشد والحلي"},{"branch_id":"B006","branch_image_ar":"تسميات الجبر وأعلامه"}],"mapped_root_id":"root_000216","mapped_root_norm":"ج ب ر"}]},{"root":"ع ص ي","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الخروج عن الطاعة"}],"mapped_root_id":"root_001022","mapped_root_norm":"ع ص ي"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"19:14","surface_ref":"19:14"},{"ayah_ref":"19:15","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"19:15","root_occurrences":[{"lemmas_ar":["سَلَٰم"],"occurrence_count":1,"pos_tags":["N"],"root":"س ل م","surfaces_ar":["سَلَٰمٌ"],"word_indices":["1"]},{"lemmas_ar":["يَوْم","يَوْم","يَوْم"],"occurrence_count":3,"pos_tags":["T","T","T"],"root":"ي و م","surfaces_ar":["يَوْمَ","يَوْمَ","يَوْمَ"],"word_indices":["3","5","7"]},{"lemmas_ar":["وَلَدَ"],"occurrence_count":1,"pos_tags":["V"],"root":"و ل د","surfaces_ar":["وُلِدَ"],"word_indices":["4"]},{"lemmas_ar":["مَّاتَ"],"occurrence_count":1,"pos_tags":["V"],"root":"م و ت","surfaces_ar":["يَمُوتُ"],"word_indices":["6"]},{"lemmas_ar":["بَعَثَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ب ع ث","surfaces_ar":["يُبْعَثُ"],"word_indices":["8"]},{"lemmas_ar":["حَيّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ح ي ي","surfaces_ar":["حَيًّا"],"word_indices":["9"]}],"root_sequence":["س ل م","ي و م","و ل د","ي و م","م و ت","ي و م","ب ع ث","ح ي ي"],"text_ar":"وَسَلَٰمٌ عَلَيْهِ يَوْمَ وُلِدَ وَيَوْمَ يَمُوتُ وَيَوْمَ يُبْعَثُ حَيًّۭا"}],"context_order":["19:15"],"context_root_cues":[{"root":"س ل م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"السلامة والبراءة من الآفات"},{"branch_id":"B004","branch_image_ar":"الصلح والمسالمة ضد الحرب"},{"branch_id":"B005","branch_image_ar":"السلم في البيع والسلف"},{"branch_id":"B006","branch_image_ar":"السلم مرقاة وسببا"},{"branch_id":"B007","branch_image_ar":"السلام حجارة صلبة"},{"branch_id":"B008","branch_image_ar":"السلم شجر وقرظ للدباغة"},{"branch_id":"B009","branch_image_ar":"السليم الملدوغ تفاؤلا أو استسلاما"},{"branch_id":"B010","branch_image_ar":"السلامى عظام ومفاصل"},{"branch_id":"B011","branch_image_ar":"السلم دلو بعروة واحدة"},{"branch_id":"B012","branch_image_ar":"تسليم الشيء وتخليته"},{"branch_id":"B013","branch_image_ar":"أخذه سلما أي أسره"}],"mapped_root_id":"root_000737","mapped_root_norm":"س ل م"}]},{"root":"ي و م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"وقت النهار المحدود"},{"branch_id":"B002","branch_image_ar":"مدة من الزمان"},{"branch_id":"B003","branch_image_ar":"كائنة اليوم وشدته"}],"mapped_root_id":"root_001700","mapped_root_norm":"ي و م"}]},{"root":"و ل د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"مولود من نسل"},{"branch_id":"B002","branch_image_ar":"أبوان من جهة الولادة"},{"branch_id":"B003","branch_image_ar":"حدوث الولادة ووضع الحمل"},{"branch_id":"B004","branch_image_ar":"صغير قريب العهد بالولادة أو مملوك"},{"branch_id":"B005","branch_image_ar":"شيء حاصل عن شيء أو مستحدث منه"},{"branch_id":"B006","branch_image_ar":"قرين في سن الولادة"}],"mapped_root_id":"root_001683","mapped_root_norm":"و ل د"}]},{"root":"م و ت","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ذهاب القوة والحياة"},{"branch_id":"B002","branch_image_ar":"إذهاب القوة بالإماتة"},{"branch_id":"B003","branch_image_ar":"أرض موات ومتاع لا روح فيه"},{"branch_id":"B004","branch_image_ar":"مُوتان واقع في الناس أو المال"},{"branch_id":"B005","branch_image_ar":"موت الولد للوالد أو الناقة"},{"branch_id":"B006","branch_image_ar":"موتان الفؤاد"},{"branch_id":"B007","branch_image_ar":"الميتة بلا ذكاة"},{"branch_id":"B008","branch_image_ar":"ميتة الحال وواحدة الموت"},{"branch_id":"B009","branch_image_ar":"الموتة جنون وغشية"},{"branch_id":"B010","branch_image_ar":"استماتة في الأمر والموت"},{"branch_id":"B011","branch_image_ar":"إظهار الموت والخشوع كذبا"},{"branch_id":"B012","branch_image_ar":"سكون وخمود كنوم أو بلى"},{"branch_id":"B013","branch_image_ar":"الخضوع للحق"},{"branch_id":"B014","branch_image_ar":"استبانة موت الصيد"}],"mapped_root_id":"root_001454","mapped_root_norm":"م و ت"}]},{"root":"ب ع ث","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"إثارة الساكن من ركوده"},{"branch_id":"B002","branch_image_ar":"إرسال المبعوث وتوجيهه"},{"branch_id":"B004","branch_image_ar":"اندفاع القوم ومضيهم"}],"mapped_root_id":"root_000129","mapped_root_norm":"ب ع ث"}]},{"root":"ح ي ي","targets":[{"branches":[{"branch_id":"B002","branch_image_ar":"حياة الأرض بالمطر والنبات"},{"branch_id":"B003","branch_image_ar":"ذو الروح والحيوان"},{"branch_id":"B004","branch_image_ar":"الحية من جنس الحياة"},{"branch_id":"B006","branch_image_ar":"استبقاء الحياة وترك القتل"},{"branch_id":"B007","branch_image_ar":"التحية دعاء بالحياة والسلام"},{"branch_id":"B009","branch_image_ar":"حي على بمعنى هلم وأقبل"},{"branch_id":"B010","branch_image_ar":"الحي جماعة النسب والقبيلة"},{"branch_id":"B011","branch_image_ar":"الحياء العضو المستور"},{"branch_id":"B012","branch_image_ar":"المحيا وجه الإنسان"},{"branch_id":"B013","branch_image_ar":"الحياة بمعنى النفع والخير"}],"mapped_root_id":"root_000383","mapped_root_norm":"ح ي ي"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"19:15","surface_ref":"19:15"},{"ayah_ref":"1:2","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:2","root_occurrences":[{"lemmas_ar":["حَمْد"],"occurrence_count":1,"pos_tags":["N"],"root":"ح م د","surfaces_ar":["حَمْدُ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["لَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَبّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ر ب ب","surfaces_ar":["رَبِّ"],"word_indices":["3"]},{"lemmas_ar":["عَٰلَمِين"],"occurrence_count":1,"pos_tags":["N"],"root":"ع ل م","surfaces_ar":["عَٰلَمِينَ"],"word_indices":["4"]}],"root_sequence":["ح م د","ء ل ه","ر ب ب","ع ل م"],"text_ar":"ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ"}],"context_order":["1:2"],"context_root_cues":[{"root":"ح م د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الحمد خلاف الذم"},{"branch_id":"B002","branch_image_ar":"وجود الشيء محمودا"},{"branch_id":"B003","branch_image_ar":"المحمود كثير الخصال"},{"branch_id":"B004","branch_image_ar":"حماداك الغاية المحمودة"},{"branch_id":"B005","branch_image_ar":"يتحمد بالمنة"}],"mapped_root_id":"root_000355","mapped_root_norm":"ح م د"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ب ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ربوبية وملك وسيادة"},{"branch_id":"B002","branch_image_ar":"إصلاح وتربية وإتمام"},{"branch_id":"B003","branch_image_ar":"علم رباني"},{"branch_id":"B004","branch_image_ar":"ربة وجماعات كثيرة"},{"branch_id":"B005","branch_image_ar":"ربيب وربيبة ورابة"},{"branch_id":"B006","branch_image_ar":"رُبّ خاثر وإصلاح به"},{"branch_id":"B007","branch_image_ar":"لزوم وإقامة ودوام"},{"branch_id":"B008","branch_image_ar":"رباب السحاب"},{"branch_id":"B009","branch_image_ar":"شاة رُبّى وحداثة"},{"branch_id":"B010","branch_image_ar":"ربابة تجمع القداح"},{"branch_id":"B011","branch_image_ar":"ربابة عهد وميثاق"},{"branch_id":"B012","branch_image_ar":"ربة نبات"},{"branch_id":"B013","branch_image_ar":"ماء رَبَب كثير"},{"branch_id":"B014","branch_image_ar":"رَبْرَب قطيع"},{"branch_id":"B015","branch_image_ar":"حرف رب وربما"},{"branch_id":"B016","branch_image_ar":"رُبَى حاجة وعقدة ونعمة"},{"branch_id":"B017","branch_image_ar":"رباني الملاحين"}],"mapped_root_id":"root_000532","mapped_root_norm":"ر ب ب"},{"branches":[{"branch_id":"B001","branch_image_ar":"زيادة وعلو"},{"branch_id":"B002","branch_image_ar":"أرض مرتفعة"},{"branch_id":"B003","branch_image_ar":"زيادة الربا في المعاملة"},{"branch_id":"B004","branch_image_ar":"تصعد النفس وانتفاخه"},{"branch_id":"B005","branch_image_ar":"تغذية ونشوء"},{"branch_id":"B006","branch_image_ar":"نتوء أصل الفخذ"},{"branch_id":"B007","branch_image_ar":"أهل البيت من بني الأعمام"}],"mapped_root_id":"root_000537","mapped_root_norm":"ر ب و"}]},{"root":"ع ل م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"انكشاف الشيء للعارف"},{"branch_id":"B002","branch_image_ar":"أثر يميز الشيء ويهدي إليه"},{"branch_id":"B004","branch_image_ar":"شق ظاهر في الشفة العليا"},{"branch_id":"B005","branch_image_ar":"ماء كثير مجتمع في عيلم"},{"branch_id":"B006","branch_image_ar":"طائر جارح يسمى العلام"},{"branch_id":"B007","branch_image_ar":"ذكر الضباع يسمى العيلام"}],"mapped_root_id":"root_001040","mapped_root_norm":"ع ل م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:2","membership_added_ayah":true,"membership_target_surah":19,"surface_ref":"1:2"},{"ayah_ref":"1:3","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:3","root_occurrences":[{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["1","2"]}],"root_sequence":["ر ح م","ر ح م"],"text_ar":"ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"}],"context_order":["1:3"],"context_root_cues":[{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:3","membership_added_ayah":true,"membership_target_surah":19,"surface_ref":"1:3"},{"ayah_ref":"1:4","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:4","root_occurrences":[{"lemmas_ar":["مَٰلِك"],"occurrence_count":1,"pos_tags":["N"],"root":"م ل ك","surfaces_ar":["مَٰلِكِ"],"word_indices":["1"]},{"lemmas_ar":["يَوْم"],"occurrence_count":1,"pos_tags":["N"],"root":"ي و م","surfaces_ar":["يَوْمِ"],"word_indices":["2"]},{"lemmas_ar":["دِين"],"occurrence_count":1,"pos_tags":["N"],"root":"د ي ن","surfaces_ar":["دِّينِ"],"word_indices":["3"]}],"root_sequence":["م ل ك","ي و م","د ي ن"],"text_ar":"مَٰلِكِ يَوْمِ ٱلدِّينِ"}],"context_order":["1:4"],"context_root_cues":[{"root":"م ل ك","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"قوة الشيء وتماسكه"},{"branch_id":"B002","branch_image_ar":"المِلْك والتصرف"},{"branch_id":"B003","branch_image_ar":"المُلك والسلطان"},{"branch_id":"B004","branch_image_ar":"الإملاك والتزويج"},{"branch_id":"B005","branch_image_ar":"مِلاك الأمر وعِماده"},{"branch_id":"B006","branch_image_ar":"مَلَك الطريق والوادي"},{"branch_id":"B007","branch_image_ar":"الماء مَلَك الأمر"},{"branch_id":"B008","branch_image_ar":"المتقدم القائد في الحيوان"}],"mapped_root_id":"root_001444","mapped_root_norm":"م ل ك"}]},{"root":"ي و م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"وقت النهار المحدود"},{"branch_id":"B002","branch_image_ar":"مدة من الزمان"},{"branch_id":"B003","branch_image_ar":"كائنة اليوم وشدته"}],"mapped_root_id":"root_001700","mapped_root_norm":"ي و م"}]},{"root":"د ي ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الطاعة والانقياد"},{"branch_id":"B002","branch_image_ar":"الحساب والجزاء"},{"branch_id":"B003","branch_image_ar":"الدين المالي"},{"branch_id":"B004","branch_image_ar":"الإذلال والملك"},{"branch_id":"B005","branch_image_ar":"العادة والشأن"},{"branch_id":"B006","branch_image_ar":"مدينة الطاعة"},{"branch_id":"B007","branch_image_ar":"التصديق والتفويض"}],"mapped_root_id":"root_000504","mapped_root_norm":"د ي ن"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:4","membership_added_ayah":true,"membership_target_surah":19,"surface_ref":"1:4"},{"ayah_ref":"1:5","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:5","root_occurrences":[{"lemmas_ar":["عَبَدَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ع ب د","surfaces_ar":["نَعْبُدُ"],"word_indices":["2"]},{"lemmas_ar":["ٱسْتَعِينُ"],"occurrence_count":1,"pos_tags":["V"],"root":"ع و ن","surfaces_ar":["نَسْتَعِينُ"],"word_indices":["4"]}],"root_sequence":["ع ب د","ع و ن"],"text_ar":"إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ"}],"context_order":["1:5"],"context_root_cues":[{"root":"ع ب د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرق والملك"},{"branch_id":"B003","branch_image_ar":"العبادة والطاعة الخاضعة"},{"branch_id":"B004","branch_image_ar":"التعبيد والاستعباد"},{"branch_id":"B005","branch_image_ar":"التذليل والتسوية"},{"branch_id":"B006","branch_image_ar":"التكريم والتعظيم"},{"branch_id":"B007","branch_image_ar":"القوة والصلابة"},{"branch_id":"B008","branch_image_ar":"الأنفة والغضب"},{"branch_id":"B009","branch_image_ar":"قلة اللبث وسرعة العدو"},{"branch_id":"B010","branch_image_ar":"التفرق في الوجوه"},{"branch_id":"B011","branch_image_ar":"العطب والانقطاع"},{"branch_id":"B012","branch_image_ar":"صَلاءة الطيب"}],"mapped_root_id":"root_000973","mapped_root_norm":"ع ب د"}]},{"root":"ع و ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الإعانة والمظاهرة"},{"branch_id":"B002","branch_image_ar":"العَوان بين السنين"},{"branch_id":"B003","branch_image_ar":"الحرب العَوان"},{"branch_id":"B004","branch_image_ar":"النخلة العَوانة القديمة"},{"branch_id":"B005","branch_image_ar":"استواء الخلقة وتلاحق القوة"},{"branch_id":"B006","branch_image_ar":"العانة قطيع الحمر"},{"branch_id":"B007","branch_image_ar":"عانة الرجل"},{"branch_id":"B008","branch_image_ar":"النسبة إلى عانة"}],"mapped_root_id":"root_001064","mapped_root_norm":"ع و ن"},{"branches":[{"branch_id":"B001","branch_image_ar":"العين الناظرة"},{"branch_id":"B002","branch_image_ar":"المشاهدة بالعين"},{"branch_id":"B003","branch_image_ar":"عين الحفظ والرعاية"},{"branch_id":"B004","branch_image_ar":"الإصابة بالعين"},{"branch_id":"B005","branch_image_ar":"العين الجاسوسة"},{"branch_id":"B006","branch_image_ar":"منبع الماء الجاري"},{"branch_id":"B007","branch_image_ar":"عين الجلد والسقاء"},{"branch_id":"B008","branch_image_ar":"عين الشمس"},{"branch_id":"B009","branch_image_ar":"النقرة أو الموضع العيني"},{"branch_id":"B010","branch_image_ar":"عين السحاب والمطر"},{"branch_id":"B011","branch_image_ar":"النقد الحاضر"},{"branch_id":"B012","branch_image_ar":"العينة والسلف"},{"branch_id":"B013","branch_image_ar":"عين الشيء نفسه"},{"branch_id":"B014","branch_image_ar":"العين خيار الشيء"},{"branch_id":"B015","branch_image_ar":"أعيان القوم والإخوة"},{"branch_id":"B016","branch_image_ar":"سعة العين وحسنها"},{"branch_id":"B017","branch_image_ar":"العين بمعنى الناس الحاضرون"}],"mapped_root_id":"root_001069","mapped_root_norm":"ع ي ن"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:5","membership_added_ayah":true,"membership_target_surah":19,"surface_ref":"1:5"},{"ayah_ref":"1:6","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:6","root_occurrences":[{"lemmas_ar":["هَدَى"],"occurrence_count":1,"pos_tags":["V"],"root":"ه د ي","surfaces_ar":["ٱهْدِ"],"word_indices":["1"]},{"lemmas_ar":["صِرَٰط"],"occurrence_count":1,"pos_tags":["N"],"root":"ص ر ط","surfaces_ar":["صِّرَٰطَ"],"word_indices":["2"]},{"lemmas_ar":["مُّسْتَقِيم"],"occurrence_count":1,"pos_tags":["ADJ"],"root":"ق و م","surfaces_ar":["مُسْتَقِيمَ"],"word_indices":["3"]}],"root_sequence":["ه د ي","ص ر ط","ق و م"],"text_ar":"ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ"}],"context_order":["1:6"],"context_root_cues":[{"root":"ه د ي","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"دلالة بلطف إلى الطريق والحق"},{"branch_id":"B002","branch_image_ar":"جهة الأمر وسيرته وقصده"},{"branch_id":"B003","branch_image_ar":"المتقدم الهادي وأوائل الشيء"},{"branch_id":"B004","branch_image_ar":"بعثة لطف وهدية إلى ذي مودة"},{"branch_id":"B005","branch_image_ar":"الهدي المهدى إلى الحرم"},{"branch_id":"B006","branch_image_ar":"العروس المهدية إلى زوجها"},{"branch_id":"B007","branch_image_ar":"هدي الحرمة والأسير"},{"branch_id":"B008","branch_image_ar":"مشي التهادي مع الاعتماد والتمايل"},{"branch_id":"B009","branch_image_ar":"الهداء البليد الضعيف"},{"branch_id":"B010","branch_image_ar":"هدي السكون وحسن الهيئة"},{"branch_id":"B011","branch_image_ar":"إهداء الشعر ومهاداته"}],"mapped_root_id":"root_001583","mapped_root_norm":"ه د ي"}]},{"root":"ص ر ط","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الطريق المستقيم"},{"branch_id":"B002","branch_image_ar":"الغيبة في المرور والبلع"},{"branch_id":"B003","branch_image_ar":"السيف القاطع الماضي في الضربة"}],"mapped_root_id":"root_000858","mapped_root_norm":"ص ر ط"}]},{"root":"ق و م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"جماعة الناس والرجال"},{"branch_id":"B002","branch_image_ar":"انتصاب وقيام بالبدن"},{"branch_id":"B003","branch_image_ar":"عزم ونهوض إلى الأمر"},{"branch_id":"B004","branch_image_ar":"رعاية وحفظ وولاية"},{"branch_id":"B006","branch_image_ar":"مقام وإقامة في موضع"},{"branch_id":"B007","branch_image_ar":"نيابة وقيام مقام غيره"},{"branch_id":"B008","branch_image_ar":"استقامة واعتدال واستواء"},{"branch_id":"B009","branch_image_ar":"قوام وعماد ومعاش"},{"branch_id":"B010","branch_image_ar":"قيمة وتقويم وتسعير"},{"branch_id":"B011","branch_image_ar":"قامة وقوام الجسم والطول"},{"branch_id":"B012","branch_image_ar":"آلة قائمة وجزء قائم"},{"branch_id":"B013","branch_image_ar":"قيامة وبعث وقيام الساعة"},{"branch_id":"B014","branch_image_ar":"مقاومة ومنازلة"},{"branch_id":"B015","branch_image_ar":"وزن سواء ومقدار معتدل"},{"branch_id":"B016","branch_image_ar":"جمود ووقوف وكلال"},{"branch_id":"B017","branch_image_ar":"انتصاف النهار وقائم الظهيرة"},{"branch_id":"B018","branch_image_ar":"نفاق السوق"},{"branch_id":"B019","branch_image_ar":"وجع قائم بالعضو"},{"branch_id":"B020","branch_image_ar":"قوام في قوائم الشاة"},{"branch_id":"B021","branch_image_ar":"عين قائمة ذاهبة البصر"}],"mapped_root_id":"root_001273","mapped_root_norm":"ق و م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:6","membership_added_ayah":true,"membership_target_surah":19,"surface_ref":"1:6"},{"ayah_ref":"1:7","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:7","root_occurrences":[{"lemmas_ar":["صِرَٰط"],"occurrence_count":1,"pos_tags":["N"],"root":"ص ر ط","surfaces_ar":["صِرَٰطَ"],"word_indices":["1"]},{"lemmas_ar":["أَنْعَمَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ن ع م","surfaces_ar":["أَنْعَمْ"],"word_indices":["3"]},{"lemmas_ar":["غَيْر"],"occurrence_count":1,"pos_tags":["N"],"root":"غ ي ر","surfaces_ar":["غَيْرِ"],"word_indices":["5"]},{"lemmas_ar":["مَغْضُوب"],"occurrence_count":1,"pos_tags":["N"],"root":"غ ض ب","surfaces_ar":["مَغْضُوبِ"],"word_indices":["6"]},{"lemmas_ar":["ضَآلّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ض ل ل","surfaces_ar":["ضَّآلِّينَ"],"word_indices":["9"]}],"root_sequence":["ص ر ط","ن ع م","غ ي ر","غ ض ب","ض ل ل"],"text_ar":"صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ"}],"context_order":["1:7"],"context_root_cues":[{"root":"ص ر ط","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الطريق المستقيم"},{"branch_id":"B002","branch_image_ar":"الغيبة في المرور والبلع"},{"branch_id":"B003","branch_image_ar":"السيف القاطع الماضي في الضربة"}],"mapped_root_id":"root_000858","mapped_root_norm":"ص ر ط"}]},{"root":"ن ع م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"حسن الحال والنعمة"},{"branch_id":"B002","branch_image_ar":"اللين والنعومة ورفاه العيش"},{"branch_id":"B003","branch_image_ar":"مدح الشيء بنعم"},{"branch_id":"B004","branch_image_ar":"الجواب بنعم والتصديق"},{"branch_id":"B005","branch_image_ar":"مال الأنعام والإبل"},{"branch_id":"B006","branch_image_ar":"النعام والنعامة الطائر"},{"branch_id":"B007","branch_image_ar":"ما سمي نعامة تشبيها بالهيئة"},{"branch_id":"B008","branch_image_ar":"طيران النعامة وتفرق القوم"},{"branch_id":"B009","branch_image_ar":"النعامى ريح لينة"},{"branch_id":"B010","branch_image_ar":"زاد وأنعم في الفعل"},{"branch_id":"B011","branch_image_ar":"موافقة المكان وطيب المقام"},{"branch_id":"B012","branch_image_ar":"المشي على القدم وابتذالها"},{"branch_id":"B013","branch_image_ar":"نعم الله بك عينا وقرة العين"}],"mapped_root_id":"root_001525","mapped_root_norm":"ن ع م"}]},{"root":"غ ي ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الصلاح والمنفعة بالميرة والسقي والإصلاح"},{"branch_id":"B002","branch_image_ar":"الغَيْر في الدية"},{"branch_id":"B003","branch_image_ar":"تغيير الصورة أو إبدال الشيء بغيره"},{"branch_id":"B004","branch_image_ar":"الغَيْرة على الأهل"},{"branch_id":"B005","branch_image_ar":"السوى والخلاف والاستثناء والنفي"}],"mapped_root_id":"root_001119","mapped_root_norm":"غ ي ر"}]},{"root":"غ ض ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"اشتداد السخط وثورانه للانتقام"},{"branch_id":"B002","branch_image_ar":"الغضب لشخص حي أو به بعد موته"},{"branch_id":"B003","branch_image_ar":"المراغمة والمخالفة"},{"branch_id":"B004","branch_image_ar":"صلابة الصخرة وتماسكها"},{"branch_id":"B005","branch_image_ar":"غلظ الجسم وشدة الحمرة"},{"branch_id":"B006","branch_image_ar":"تورم العين وما حولها"},{"branch_id":"B007","branch_image_ar":"العبوس والضجر والعظم في وصف الحيوان أو الشخص"},{"branch_id":"B008","branch_image_ar":"جلد صلب أو مطوي كدرقة"}],"mapped_root_id":"root_001092","mapped_root_norm":"غ ض ب"}]},{"root":"ض ل ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الضلال عن الهدى والقصد"},{"branch_id":"B002","branch_image_ar":"الغيبوبة والخفاء"},{"branch_id":"B003","branch_image_ar":"فقدان الشيء"},{"branch_id":"B004","branch_image_ar":"ضياع الحفظ"},{"branch_id":"B005","branch_image_ar":"الضالّة في المضيعة"}],"mapped_root_id":"root_000913","mapped_root_norm":"ض ل ل"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:7","membership_added_ayah":true,"membership_target_surah":19,"surface_ref":"1:7"}],"support_registry":[{"anchor_evidence":[{"arabic_uthmani":"ذِكْرُ رَحْمَتِ رَبِّكَ عَبْدَهُۥ زَكَرِيَّآ","ayah_ref":"19:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000516/B003","root_000516/B004"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000516","role":"Recall after absence supplies the mnemonic recovery function assigned to the opener.","root":"ذ ك ر","source_ref":"19:2","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_000516","role":"Mention moving on the tongue supplies the opener's oral and recited channel.","root":"ذ ك ر","source_ref":"19:2","source_word_indices":["1"]}],"changed_reading":{"after":"A compact vocal mnemonic that arrests attention and primes the remembrance narrated next.","before":"A formal interruption before discourse."},"confidence":"medium","mechanism":"The immediate move into remembrance/mention recasts the rootless sequence as an arresting oral-memory cue: its value can lie in prompting and voicing recollection rather than carrying lexical content.","model_id":"delta_mnemonic_utterance","reader_inference":"The packet supplies adjacency plus mnemonic and vocal branch images; I infer that the opener primes recollection through utterance. A live alternative is that it is only a formal boundary unrelated to the following act of remembrance.","status":"revised","structural_cues":["19:2 follows the rootless opener immediately and begins with a nominal framing of the ensuing account as remembrance or mention."],"trigger_roots":["ذ ك ر"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_mnemonic_utterance","source_type":"hft","support_id":"sup_dde4f42cdaa505ed6402","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِذْ نَادَىٰ رَبَّهُۥ نِدَآءً خَفِيًّۭا","ayah_ref":"19:3"},{"arabic_uthmani":"قَالَ رَبِّ إِنِّى وَهَنَ ٱلْعَظْمُ مِنِّى وَٱشْتَعَلَ ٱلرَّأْسُ شَيْبًۭا وَلَمْ أَكُنۢ بِدُعَآئِكَ رَبِّ شَقِيًّۭا","ayah_ref":"19:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000428/B001","root_000478/B001","root_001487/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001487","role":"Raised calling supplies the audible address against which the opener's sounded form can be heard.","root":"ن د و","source_ref":"19:3","source_word_indices":["2","4"]},{"branch_id":"B001","mapped_root_id":"root_000428","role":"Concealment supplies the withheld semantic side of the articulated sequence.","root":"خ ف ي","source_ref":"19:3","source_word_indices":["5"]},{"branch_id":"B001","mapped_root_id":"root_000478","role":"Calling through speech links the private prayer sequence to the opener's vocal form.","root":"د ع و","source_ref":"19:4","source_word_indices":["12"]}],"changed_reading":{"after":"A compressed mode of address whose sound is available while its propositional content stays veiled.","before":"A mnemonic vocal cue with unresolved semantics."},"confidence":"exploratory","mechanism":"A sequence that can be sounded but not lexically parsed becomes an acoustic veil: articulation is exposed while propositional content remains hidden, matching the nearby pattern of an audible yet private call.","model_id":"delta_concealed_call","reader_inference":"The packet supplies calling, concealment, and prayer; I infer a formal analogy between hidden address and sound without lexical disclosure. The alternative is that hiddenness characterizes only Zechariah's prayer and does not retrospectively shape 19:1.","status":"new","structural_cues":["19:3 repeats the call as verb and verbal noun, then qualifies it as hidden; 19:4 continues the first-person address to the Lord."],"trigger_roots":["ن د و","خ ف ي","د ع و"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_concealed_call","source_type":"hft","support_id":"sup_3eaa131517a3dd3b6361","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"يَٰزَكَرِيَّآ إِنَّا نُبَشِّرُكَ بِغُلَٰمٍ ٱسْمُهُۥ يَحْيَىٰ لَمْ نَجْعَل لَّهُۥ مِن قَبْلُ سَمِيًّۭا","ayah_ref":"19:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000745/B005","root_001650/B001"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000745","role":"Naming as designation makes letter-names, rather than word meaning, the operative formal unit.","root":"س م و","source_ref":"19:7","source_word_indices":["5","12"]},{"branch_id":"B001","mapped_root_id":"root_001650","role":"A visible identifying mark supplies the graphic counterpart to the spoken letter-names.","root":"س م و","source_ref":"19:7","source_word_indices":["5","12"]}],"changed_reading":{"after":"A sequence of names and marks whose identifiability exceeds its propositional decodability, preparing the account of unprecedented naming.","before":"Opaque units whose only evident force is interruption or sound."},"confidence":"medium","mechanism":"Because the opener is encountered as a chain of letter-names rather than as one lexical word, the later concentration on a child's unprecedented name activates it as a prelude of naming and marking: identifiable units precede a uniquely identified person.","model_id":"delta_names_before_naming","reader_inference":"The packet supplies repeated naming, uniqueness, and a mapped branch of visible marking; I infer that the formal unit of 19:1 is the name/mark of each letter. The alternative is that the naming language has no retrospective relation to the opener.","status":"new","structural_cues":["19:7 realizes the same root at both the child's name and the denial of any prior namesake; 19:1 is composed of conventionally nameable letters but supplies no lexical designation."],"trigger_roots":["س م و"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_names_before_naming","source_type":"hft","support_id":"sup_b045ebbc5426015717a5","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"قَالَ رَبِّ ٱجْعَل لِّىٓ ءَايَةًۭ ۚ قَالَ ءَايَتُكَ أَلَّا تُكَلِّمَ ٱلنَّاسَ ثَلَٰثَ لَيَالٍۢ سَوِيًّۭا","ayah_ref":"19:10"},{"arabic_uthmani":"فَخَرَجَ عَلَىٰ قَوْمِهِۦ مِنَ ٱلْمِحْرَابِ فَأَوْحَىٰٓ إِلَيْهِمْ أَن سَبِّحُوا۟ بُكْرَةًۭ وَعَشِيًّۭا","ayah_ref":"19:11"},{"arabic_uthmani":"يَٰيَحْيَىٰ خُذِ ٱلْكِتَٰبَ بِقُوَّةٍۢ ۖ وَءَاتَيْنَٰهُ ٱلْحُكْمَ صَبِيًّۭا","ayah_ref":"19:12"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000074/B003","root_001283/B002","root_001316/B001","root_001633/B002","root_001633/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000074","role":"A manifest sign supplies communicative force without requiring sentential wording.","root":"ء ي ي","source_ref":"19:10","source_word_indices":["5","7"]},{"branch_id":"B001","mapped_root_id":"root_001316","role":"Intelligible speech connecting speakers is the channel explicitly suspended, defining the opener's contrastive mode.","root":"ك ل م","source_ref":"19:10","source_word_indices":["9"]},{"branch_id":"B002","mapped_root_id":"root_001633","role":"Gesture supplies a replacement channel by which meaning passes without ordinary speech.","root":"و ح ي","source_ref":"19:11","source_word_indices":["6"]},{"branch_id":"B003","mapped_root_id":"root_001633","role":"Inscription supplies the visible-sign analogue for the opener's glyph sequence.","root":"و ح ي","source_ref":"19:11","source_word_indices":["6"]},{"branch_id":"B002","mapped_root_id":"root_001283","role":"Ordered letters and written text anchor the non-sentential opener to the later book-channel.","root":"ك ت ب","source_ref":"19:12","source_word_indices":["3"]}],"changed_reading":{"after":"A threshold sign poised between vocalization and inscription, communicating by marked units while withholding ordinary sentence speech.","before":"A rootless sequence that interrupts normal discourse."},"confidence":"strong","mechanism":"The requested sign is paired with suspended interpersonal speech, followed by communication through gesture-like revelation and then the book. This progression recasts the letter-only opener as a liminal sign-channel between voice and inscription: communicative, but not an ordinary sentence.","model_id":"delta_sign_beyond_sentence_speech","reader_inference":"The packet supplies sign, speech suspension, nonverbal transmission, and ordered writing; I infer that 19:1 formally enacts meaningful signaling outside normal sentence speech. It may instead remain an opaque opener with no narrative enactment.","status":"strengthened","structural_cues":["19:10 negates speaking to people as the sign, 19:11 nevertheless transmits an instruction to the group, and 19:12 immediately foregrounds the book.","The focus ayah contains visible and pronounceable letter units but no rooted word or proposition."],"trigger_roots":["ء ي ي","ك ل م","و ح ي","ك ت ب"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_sign_beyond_sentence_speech","source_type":"hft","support_id":"sup_a0e8a9ed2954e0759f54","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"يَٰيَحْيَىٰ خُذِ ٱلْكِتَٰبَ بِقُوَّةٍۢ ۖ وَءَاتَيْنَٰهُ ٱلْحُكْمَ صَبِيًّۭا","ayah_ref":"19:12"},{"arabic_uthmani":"وَسَلَٰمٌ عَلَيْهِ يَوْمَ وُلِدَ وَيَوْمَ يَمُوتُ وَيَوْمَ يُبْعَثُ حَيًّۭا","ayah_ref":"19:15"},{"arabic_uthmani":"وَإِنِّى خِفْتُ ٱلْمَوَٰلِىَ مِن وَرَآءِى وَكَانَتِ ٱمْرَأَتِى عَاقِرًۭا فَهَبْ لِى مِن لَّدُنكَ وَلِيًّۭا","ayah_ref":"19:5"},{"arabic_uthmani":"قَالَ كَذَٰلِكَ قَالَ رَبُّكَ هُوَ عَلَىَّ هَيِّنٌۭ وَقَدْ خَلَقْتُكَ مِن قَبْلُ وَلَمْ تَكُ شَيْـًۭٔا","ayah_ref":"19:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":4,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":4,"target_morphology_supplied":false},"branch_refs":["root_000129/B001","root_000434/B002","root_000831/B001","root_001035/B004","root_001283/B001","root_001283/B002"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001035","role":"Interrupted offspring supplies the sterile-seeming starting condition of the analogy.","root":"ع ق ر","source_ref":"19:5","source_word_indices":["8"]},{"branch_id":"B002","mapped_root_id":"root_000434","role":"Bringing creation into existence supplies emergence beyond the prior condition.","root":"خ ل ق","source_ref":"19:9","source_word_indices":["9"]},{"branch_id":"B001","mapped_root_id":"root_000831","role":"Knowable thinghood supplies the boundary crossed when bare units become an intelligible textual object.","root":"ش ي ء","source_ref":"19:9","source_word_indices":["14"]},{"branch_id":"B001","mapped_root_id":"root_001283","role":"Joining unit to unit supplies the compositional arrow from isolated letters toward discourse.","root":"ك ت ب","source_ref":"19:12","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001283","role":"Ordering letters makes the emergence specifically textual rather than merely biological.","root":"ك ت ب","source_ref":"19:12","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000129","role":"Stirring what is still from repose supplies the reactivation endpoint of the analogy.","root":"ب ع ث","source_ref":"19:15","source_word_indices":["8"]}],"changed_reading":{"after":"A dormant textual seed whose isolated units are joined and activated into discourse, analogically echoing impossible generation and renewed life.","before":"A static preface of disconnected signs."},"confidence":"exploratory","containment":"Projecting birth, creation, and reanimation onto textual composition is cross-domain and does not decode the letters. It remains anchored in the opener's isolated pre-word units and in the packet's explicit branch for ordering letters; render it only as a formal analogy by which dormant-looking units become discourse.","focus_anchor":"The opener presents isolated letters before any word, allowing joining and activation to map to its compositional form without assigning it a fabricated root.","outlier_id":"outlier_textual_germination"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_textual_germination","source_type":"hft","support_id":"sup_2c210bc16416ebbde294","trust":"legacy_unbound"}]}
</lane_packet_json>
