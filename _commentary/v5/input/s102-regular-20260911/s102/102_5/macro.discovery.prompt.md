# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **102:5**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s102-regular-20260911/s102/102_5/macro.discovery.json` and modify nothing
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
  "ayah_ref": "102:5",
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
{"analysis_context":{"analysis_id":"s102-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"102:5","host_surah":102,"lane_context_refs":["102:0","102:1","102:2","102:3","102:4","102:6","102:7","102:8","1:2","1:3","1:4","1:5","1:6","1:7"],"ordered_context_refs":["102:0","102:1","102:2","102:3","102:4","102:6","102:7","102:8","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Includes sensory seeing and perception by the eye or by insight","branch_kind":null,"branch_ref":"root_000531/B001","candidate_links":[{"candidate_id":"cand_7550e314f5aaffbd1c56","lane":"macro"},{"candidate_id":"cand_76e49d74dab883ea4e4a","lane":"macro"}],"focus_root_occurrences":[],"gloss":"seeing by eye or insight","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"رؤية العين والبصيرة","image_en":"seeing by eye or insight"}}],"root_ar":"ر ء ي","root_id":"root_000531","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"رؤية العين والبصيرة","image_en":"seeing by eye or insight","scope_ar":"يدخل فيه إدراك المرئي بالحاسة وما يجري مجراها والنظر بعين أو بصيرة","scope_en":"Includes sensory seeing and perception by the eye or by insight"},"support_links":["sup_1b840a54752a0d94954e","sup_85856ff21ce630f22514"]},{"boundary":"Çekirdek, bir şeyi bilme ve gerçeğiyle kavramadır; bildirme, öğretme, öğrenme ve bilgi yarışında yenme ayrı biçimlere bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001040/B001","candidate_links":[{"candidate_id":"cand_7550e314f5aaffbd1c56","lane":"macro"},{"candidate_id":"cand_5465175ae6b3ef5134aa","lane":"macro"},{"candidate_id":"cand_76e49d74dab883ea4e4a","lane":"macro"},{"candidate_id":"cand_c7e1299e0390be2b582e","lane":"macro"},{"candidate_id":"cand_e2e57017aed461a0d11a","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:5:3:1","qac_word_ref":"102:5:3","surface_ar":"تَعْلَمُ"},{"lemma_ar":"عِلْم","morph_features":"STEM|POS:N|LEM:Eilom|ROOT:Elm|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:4:1","qac_word_ref":"102:5:4","surface_ar":"عِلْمَ"}],"gloss":"bilme ve gerçeğini kavrama","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi bilme, tanıma ve gerçeğine uygun biçimde kavrama durumu bilgisizliğin karşıtıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir haberin farkına varmak veya ondan haberdar olmak, bilme çekirdeğinin belirli bir konuya uygulanmasıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bildirme, öğretme ve öğrenme biçimleri bilginin bir başkasına ulaştırılması ya da kişinin onu edinmesi süreçlerini anlatır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Karşılıklı bilgi sınamasında birini yenmek, belirli bir kuruluşta ortaya çıkan rekabetçi kullanımdır."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bilgisizliğin karşıtı olan temel zihinsel edinimi, tanımayı ve gerçeğe uygun kavrayışı birlikte karşılar.","boundary_detail":"Çekirdek, bir şeyi bilme ve gerçeğiyle kavramadır; bildirme, öğretme, öğrenme ve bilgi yarışında yenme ayrı biçimlere bağlıdır.","branch_image_ar":"انكشاف الشيء للعارف","concept_gloss":"bilme ve gerçeğini kavrama","contextual_glosses":[{"applicability":"Bir olay veya gelişme hakkındaki haberin kişinin bilgisine ulaşması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Haberin farkına varma ve ondan bilgi edinme yönünü korur."},"facet_ids":["F002"],"text":"haberinden haberdar olmak","usage_role":"contextual"},{"applicability":"Bilginin tekrar ve yönlendirmeyle bir öğrenende yerleşmesini sağlayan öğretim bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilginin aktarılması ve öğrenende kalıcı bir sonuç oluşturması sürecini korur."},"facet_ids":["F003"],"text":"öğretmek ve öğrenmesini sağlamak","usage_role":"explanatory"},{"applicability":"İki kişi arasındaki bilgi sınamasında bir tarafın ötekini yenmesi bağlamına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilgi alanındaki karşılaştırmayı ve üstün gelme sonucunu korur."},"facet_ids":["F004"],"text":"bilgide üstün gelmek","usage_role":"contextual"}],"definition":"Bir şeyi bilmek, tanımak ve onu gerçeğine uygun biçimde kavramak; böylece bilgisizlikten çıkmaktır. Haber verilmesi, öğretme, öğrenme ve bilgi bakımından üstün gelme bu çekirdekten hareket eden, belirli biçimlere bağlı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi bilme, tanıma ve gerçeğine uygun biçimde kavrama durumu bilgisizliğin karşıtıdır."},{"facet_id":"F002","role":"extension","statement":"Bir haberin farkına varmak veya ondan haberdar olmak, bilme çekirdeğinin belirli bir konuya uygulanmasıdır."},{"facet_id":"F003","role":"associated_use","statement":"Bildirme, öğretme ve öğrenme biçimleri bilginin bir başkasına ulaştırılması ya da kişinin onu edinmesi süreçlerini anlatır."},{"facet_id":"F004","role":"associated_use","statement":"Karşılıklı bilgi sınamasında birini yenmek, belirli bir kuruluşta ortaya çıkan rekabetçi kullanımdır."}],"identity_rationale":"Dalın bilme ve bilgisizliğin karşıtı olma yönündeki çekirdeği kaynak ifadesiyle uyumludur. Ancak haberden haberdar olma, öğretme, öğrenme ve bilgi bakımından üstün gelme kullanımları bu çekirdekle aynı düzeyde değil, belirli biçimlere bağlı uzantılar olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bilgi; bir şeyi gerçeğiyle kavrama"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şeyi bilmek ve tanımak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"haberinden haberdar olmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bildirmek, haberdar etmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"öğretmek, öğrenmesini sağlamak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"öğrenmek, kavramaya yönelmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bilmek; buyrukta bil ki"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bilgi yarışında yenmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bilen ve bildiğine göre davranan kişi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bilgili, bilgi sahibi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"çok bilgili, çok bilen"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"son derece bilgili kişi"}],"lexicalization_note":"Tanım çıplak bilme çekirdeğini öne alır; haber, öğretim, öğrenim ve karşılıklı bilgi sınamasıyla ilgili anlamları yalnızca ilgili biçim ve kuruluşlara bağlar.","neighbor_coverage_note":"Bilme çekirdeğini en çok açıklayan yakın kavrayış dalı, açık karşıtı olan bilgisizlik dalı ve doğru kullanım boyutu taşıyan bilgelik dalı seçildi; öteki adaylar yalnızca uzak çağrışım veya ayrı kök içi anlam alanı sunar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdekleri yakın olsa da odak dalın biçime bağlı aktarım ve edinim süreçleri ile komşunun akletme ve hızlı anlama vurgusu karşılıklı değiştirilebilirliği sınırlar.","focus_only":"Odak dal, haberden haberdar etme, öğretme, öğrenme ve bilgi yarışında üstün gelme gibi biçime bağlı uzantıları da kapsar.","gloss":"bilmek ve anlamını kavramak","neighbor_only":"Komşu dal, anlamları doğrulama, akletme ve çabuk kavrama yönlerini ayrıca öne çıkarır.","neighbor_ref":"root_001182/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyi bilme, tanıma ve zihnen kavrama alanında büyük ölçüde örtüşür."},{"boundary_match":"opposed","distinction":"Odak dal bilgiye erişmeyi ve kavramayı bildirirken komşu dal bu erişimin bulunmamasını ya da gerçeğin yanlış bilinmesini bildirir.","focus_only":"Bir şeyi tanıma, gerçeğine uygun kavrama ve bilgi sahibi olma bulunur.","gloss":"bilgi ile bilgisizlik karşıtlığı","neighbor_only":"Bilginin yokluğu, durumu tanımama veya gerçeğe aykırı bir kanaat bulunur.","neighbor_ref":"root_000271/B001","relation_type":"antonym","shared_zone":"İki dal aynı zihinsel erişim ekseninin olumlu ve olumsuz uçlarını gösterir."},{"boundary_match":"partial","distinction":"Bilmek tek başına odak dal için yeterli olabilir; komşu dal ise bilginin doğru yargı ve isabetli davranışla birleşmesini öne çıkarır.","focus_only":"Odak dalda yalın bilme ve tanıma, bilginin doğru kullanımından bağımsız olarak çekirdekte yer alabilir.","gloss":"bilgi ile bilgelik","neighbor_only":"Komşu dal doğruyu bulma, yerinde yargı ve bilgiyi isabetli kullanma niteliğini gerektirir.","neighbor_ref":"root_000348/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal bilgi sahibi olmayı ve zihinsel kavrayışı paylaşır."}],"source_phrase_ar":"العلم نقيض الجهل (maqayis;ayn;tahdhib)؛ علمت الشيء عرفته (sihah;tahdhib)؛ إدراك الشيء بحقيقته (mufradat)؛ ما علمت بخبرك أي ما شعرت به (ayn;tahdhib)؛ أعلمته بكذا وعلمته تعليما (ayn)؛ التعليم تنبيه النفس لتصور المعاني (mufradat)؛ تعلم بمعنى اعلم (maqayis;sihah;tahdhib)؛ عالمت الرجل فعلمته (sihah;tahdhib)","source_summary":"Kaynakların ortak çekirdeği, bilgiyi bilgisizliğin karşıtı sayar ve bir şeyi tanıyıp gerçeğiyle kavramayı öne çıkarır. Toplu tanıklık ayrıca haberden haberdar olmayı, bilgiyi aktarmayı, öğrenmeyi ve bilgiyle üstün gelmeyi biçime bağlı uzantılar olarak gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العلم نقيض الجهل وإدراك الشيء ومعرفته والشعور بالخبر والتعلم والتعليم والإعلام والمغالبة بالعلم","what_is_not_ar":"ليس هو العلامة الحسية ولا الجبل ولا الراية ولا الشق في الشفة ولا اسم العالمين"},"support_links":["sup_0e29f72908ca23bcdc4b","sup_1b840a54752a0d94954e","sup_73ecebd7bd63926a55c1","sup_7c7013bbc61d5a57f8f2","sup_85856ff21ce630f22514"]},{"boundary":"Dal bütün işaret türlerini sınırsızca kapsamaz; kaynakta anılan ayırt etme ve yol gösterme işlevli izlerle bunlara bağlı kullanımlarla sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001040/B002","candidate_links":[{"candidate_id":"cand_644712471f5a1351c960","lane":"macro"},{"candidate_id":"cand_a03f25769e9b19783711","lane":"macro"},{"candidate_id":"cand_432fff901f7137496e5e","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:5:3:1","qac_word_ref":"102:5:3","surface_ar":"تَعْلَمُ"},{"lemma_ar":"عِلْم","morph_features":"STEM|POS:N|LEM:Eilom|ROOT:Elm|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:4:1","qac_word_ref":"102:5:4","surface_ar":"عِلْمَ"}],"gloss":"ayırt edici ve yol gösterici işaret","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesneyi veya kişiyi başkalarından ayırıp tanınır kılan belirgin iz ya da işaret çekirdeği oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bayrak, belirgin dağ, yol belirtisi ve kumaşın kenar deseni yön bulduran veya tanıtan somut gerçekleşmelerdir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Savaşçının, kumaşın veya sarığın ayırt edici bir işaretle donatılması belirli kuruluşlara bağlı eylemsel kullanımdır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Tanınmış bir kişinin belirgin bir bayrağa benzetilmesi ve yaklaşan son zamanı gösteren belirti, işaret çekirdeğinin uzantılarıdır."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyi tanınır kılan veya ona ulaşmayı sağlayan belirgin iz ve işaretlerin ortak çekirdeğini karşılar.","boundary_detail":"Dal bütün işaret türlerini sınırsızca kapsamaz; kaynakta anılan ayırt etme ve yol gösterme işlevli izlerle bunlara bağlı kullanımlarla sınırlıdır.","branch_image_ar":"أثر يميز الشيء ويهدي إليه","concept_gloss":"ayırt edici ve yol gösterici işaret","contextual_glosses":[{"applicability":"Askerlerin çevresinde toplandığı bayrak ya da yol bulmayı sağlayan belirgin dağ ve iz bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Görünürlük ile yöneltme ve tanıtma işlevini korur."},"facet_ids":["F002"],"text":"bayrak veya uzaktan seçilen kılavuz","usage_role":"contextual"},{"applicability":"Bir savaşçıya, kumaşa veya sarığa başkalarından ayıran görünür bir belirti ekleme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşaretin sonradan konmasını ve ayırt etme amacını korur."},"facet_ids":["F003"],"text":"tanıtıcı işaret koymak","usage_role":"contextual"},{"applicability":"Belirli bir son zamanın yaklaştığını haber veren gösterge bağlamına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir olayın yakınlığını gösterme işlevini korur."},"facet_ids":["F004"],"text":"yaklaşmayı gösteren belirti","usage_role":"explanatory"}],"definition":"Bir şeyi başkalarından ayıran, tanınmasını sağlayan veya ona götüren belirgin iz ya da işarettir. Bayrak, uzaktan seçilen dağ, yol belirtisi, kumaş kenarı ve sonradan konan tanıtıcı izler bu işlevin farklı gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesneyi veya kişiyi başkalarından ayırıp tanınır kılan belirgin iz ya da işaret çekirdeği oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Bayrak, belirgin dağ, yol belirtisi ve kumaşın kenar deseni yön bulduran veya tanıtan somut gerçekleşmelerdir."},{"facet_id":"F003","role":"associated_use","statement":"Savaşçının, kumaşın veya sarığın ayırt edici bir işaretle donatılması belirli kuruluşlara bağlı eylemsel kullanımdır."},{"facet_id":"F004","role":"extension","statement":"Tanınmış bir kişinin belirgin bir bayrağa benzetilmesi ve yaklaşan son zamanı gösteren belirti, işaret çekirdeğinin uzantılarıdır."}],"identity_rationale":"Kaynak ifadesi, bir şeyi başkasından ayıran belirgin izi dalın ortak çekirdeği olarak açıkça destekler. Bayrak, belirgin dağ, yol belirtisi, kumaş deseni ve savaş işareti gibi örnekler bu çekirdeğin farklı gerçekleşmeleridir; tanınmış kişi ve son zaman belirtisi ise benzetme veya gösterme ilişkisine bağlı uzantılardır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ayırt edici işaret"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bayrak, sancak"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yol gösteren belirgin dağ"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"kumaşın kenar işareti veya deseni"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yol gösteren iz veya belirti"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"savaşta kendine ayırt edici işaret takmak"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"kumaşı işaretlemek"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"işaret olarak kullanılan kına"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"sarığı tanıtıcı bir biçimde sarmak"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"tanınmış ve öne çıkan kişi"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"son saatin yaklaştığını gösteren belirti"}],"lexicalization_note":"Ayırt edici iz çıplak çekirdektir; savaşçı, kumaş, sarık ve belirli zaman göstergesiyle kurulan anlamlar kendi kuruluşlarına bağlı tutulur.","neighbor_coverage_note":"En yararlı karşılaştırmalar geçmişten kalan iz, bilerek konan tanıtıcı işaret ve fiziksel damga ile yapıldı; bayrak adayı yalnızca tek bir alt gerçekleşmeyi, öteki adaylar ise daha uzak renk veya biçim belirtilerini karşılar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda işaret önceden konabilir veya doğal bir kılavuz olabilir; komşu dalda iz, daha önceki bir varlık ya da olayın geride kalan sonucudur.","focus_only":"Odak dal, bilerek konan bayrak ve işaretlerin yanı sıra yön bulduran belirgin dağ gibi göstergeleri de kapsar.","gloss":"işaret ile kalıntı iz","neighbor_only":"Komşu dal, geçmişte var olmuş veya gerçekleşmiş bir şeyden geriye kalan izi özellikle gerektirir.","neighbor_ref":"root_000011/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da görünür bir izin başka bir şeyi tanıtması veya ona kanıt olması bakımından örtüşür."},{"boundary_match":"partial","distinction":"Komşu dalın çekirdeği işaretleme eylemine daha sıkı bağlıdır; odak dal ise konmuş işaretlerin yanında doğal kılavuzları ve bayrağı da adlandırır.","focus_only":"Odak dal doğal dağ işaretini, bayrağı, yol belirtisini ve kumaş kenarını da içine alan daha geniş bir gösterge alanına sahiptir.","gloss":"ayırt edici işaret koyma","neighbor_only":"Komşu dal özellikle atlara, varlıklara veya nesnelere tanıtma amacıyla işaret koyma eylemini öne çıkarır.","neighbor_ref":"root_000764/B004","relation_type":"near_synonym","shared_zone":"İki dal da bir varlığı başkalarından ayıracak görünür bir işaretle tanıtmayı kapsar."},{"boundary_match":"partial","distinction":"Damga bir yüzeye bilerek bırakılan fiziksel izdir; odak dalın işareti ise doğal veya yapılmış olabilir ve yön gösterme işlevi de taşıyabilir.","focus_only":"Odak dal işaret koyma dışında bayrak, dağ, yol kılavuzu ve kumaş deseni gibi bağımsız adları da kapsar.","gloss":"işaret ile damga","neighbor_only":"Komşu dal, hayvana veya nesneye yakma, kesme ya da benzeri yolla bırakılan bedensel ve maddi damgayı gerektirir.","neighbor_ref":"root_001650/B001","relation_type":"near_synonym","shared_zone":"Her iki dal görünür bir belirti aracılığıyla tanıtma ve ayırt etme işlevini paylaşır."}],"source_phrase_ar":"أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره (maqayis)؛ العلامة وهي معروفة (maqayis)؛ العلم الراية والجمع أعلام (maqayis;sihah;tahdhib)؛ العلم الجبل الطويل والجميع الأعلام (ayn)؛ العلم الجبل (sihah;mufradat)؛ المعلم الأثر يستدل به على الطريق (sihah;tahdhib)؛ علم الثوب ورقمه في أطرافه (sihah;tahdhib;mufradat)؛ أعلم الفارس إذا كانت له علامة في الحرب (maqayis;sihah;tahdhib)؛ العلام الحناء (maqayis;sihah;tahdhib;mufradat)؛ علمت عمتي أعلمها علما (tahdhib)","source_summary":"Kaynaklar ayırt edici izi ortak temel sayar ve bayrak, yüksek ya da belirgin dağ, yol göstergesi, kumaş kenarı, kına ve sonradan yerleştirilen tanıtıcı işaretleri bu temelde toplar. Tanınmış kişi ile yaklaşan son zamanın belirtisi de görünürlük ve gösterme işlevinden doğan uzantılardır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العلامة والعلم والراية والجبل والمعلم ومعالم الطريق والحدود وعلم الثوب ورقمه وتعليم الفارس والثوب والقدح والعمامة والحناء إذا جعلت علامة","what_is_not_ar":"ليس هو إدراك العلم ولا اسم الخلق ولا شق الشفة العليا"},"support_links":["sup_07989b0d9a51f41140cb","sup_48ee5148dabc78836f11","sup_657d451ca01613003c1c"]},{"boundary":"Dal yaratılmış varlıkların bütünü veya sınıflarıyla sınırlıdır; bilme durumu ve bağımsız bir fiziksel işaret anlamına gelmez.","branch_kind":"bare","branch_ref":"root_001040/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:5:3:1","qac_word_ref":"102:5:3","surface_ar":"تَعْلَمُ"},{"lemma_ar":"عِلْم","morph_features":"STEM|POS:N|LEM:Eilom|ROOT:Elm|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:4:1","qac_word_ref":"102:5:4","surface_ar":"عِلْمَ"}],"gloss":"evren ve bütün yaratılmışlar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Evren ve içindeki yaratılmış varlıkların tamamı tek bir bütün olarak adlandırılır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ad, yaratılmışların tamamı yanında onların her bir cinsini veya sınıfını ayrı bir bütün olarak da gösterebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yaratılmış bütünün kendi yaratıcısına gösterge olması, adlandırmanın açıklayıcı dayanağı olarak sunulur."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaratılmış varlıkların tümünü tek bir düzen veya bütün olarak anlatan temel kullanım için uygundur.","boundary_detail":"Dal yaratılmış varlıkların bütünü veya sınıflarıyla sınırlıdır; bilme durumu ve bağımsız bir fiziksel işaret anlamına gelmez.","branch_image_ar":"الخلق عالم يدل على صانعه","concept_gloss":"evren ve bütün yaratılmışlar","contextual_glosses":[{"applicability":"Sözün bütün evren yerine insan, görünmeyen varlıklar veya başka bir yaratık cinsi gibi ayrı sınıflara dağıtıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Her yaratık cinsinin ayrı bir bütün sayılması yönünü korur."},"facet_ids":["F002"],"text":"varlıkların her bir sınıfı","usage_role":"explanatory"}],"definition":"Yaratılmış olanların bütünü; bağlama göre evren ile içindekilerin tamamı veya yaratıkların ayrı ayrı sınıflarıdır. Bu bütünün yaratıcıyı gösteren bir belirti sayılması, adın açıklanan dayanağıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Evren ve içindeki yaratılmış varlıkların tamamı tek bir bütün olarak adlandırılır."},{"facet_id":"F002","role":"source_variant","statement":"Ad, yaratılmışların tamamı yanında onların her bir cinsini veya sınıfını ayrı bir bütün olarak da gösterebilir."},{"facet_id":"F003","role":"associated_use","statement":"Yaratılmış bütünün kendi yaratıcısına gösterge olması, adlandırmanın açıklayıcı dayanağı olarak sunulur."}],"identity_rationale":"Kaynak ifadesi, dalı yaratılmışların bütünü, gök düzeni ve içindekiler ya da yaratıkların ayrı sınıfları olarak açıklar. Her sınıfın ve bütünün yaratıcıyı gösteren bir belirti sayılması adlandırmanın gerekçesidir; bilme eylemi veya somut işaret dalıyla özdeş değildir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"evren veya yaratılmışlar bütünü"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bütün yaratıklar veya varlık sınıfları"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"evrenler, varlık dünyaları"}],"lexicalization_note":"Tanım, çıplak dalın evren, yaratılmışların bütünü ve varlık sınıfları anlamlarını verir; başka kuruluşlardan anlam aktarmaz.","neighbor_coverage_note":"Adayların çoğu hayvan bedenindeki renk ve işaretleri ya da ilgisiz özel adları anlatır; aynı kökün bilme ve işaret dalları adlandırma gerekçesini açıklasa da bu dalın yaratılmışlar bütünü sınırını keskinleştirecek bir karşıtlık oluşturmaz.","source_phrase_ar":"العالمون كل جنس من الخلق فهو في نفسه معلم وعلم (maqayis)؛ العالم الخلق والجمع العوالم (sihah)؛ العالمين رب الجن والإنس ورب الخلق كلهم (tahdhib)؛ العالم اسم للفلك وما يحويه وهو في الأصل اسم لما يعلم به (mufradat)؛ أصناف الخلائق (mufradat)","source_summary":"Kaynaklar bu adı yaratılmışların bütünü için kullanır; kapsam bazen evren ve içindekilerin tamamı, bazen de yaratıkların her bir cinsi veya sınıfıdır. Bütünün kendi yaratıcısına işaret etmesi adlandırmayı açıklayan ortak bir düşüncedir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه العالم والعالمون بمعنى الخلق أو أصناف الخلائق أو كل جنس من الخلق لأنه معلم في نفسه ودال","what_is_not_ar":"ليس هو العلم بمعنى المعرفة ولا العلم بمعنى الراية أو الجبل"},"support_links":[]},{"boundary":"Belirti özellikle üst dudakta bulunur; genel çatlaklar, alt dudak ve ağız çevresindeki başka eğrilikler kapsam dışıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001040/B004","candidate_links":[{"candidate_id":"cand_d54671499bc005d63445","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:5:3:1","qac_word_ref":"102:5:3","surface_ar":"تَعْلَمُ"},{"lemma_ar":"عِلْم","morph_features":"STEM|POS:N|LEM:Eilom|ROOT:Elm|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:4:1","qac_word_ref":"102:5:4","surface_ar":"عِلْمَ"}],"gloss":"üst dudak yarığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Üst dudakta bulunan yarık, dalın anatomik çekirdeğini oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Üst dudağı yarık insan veya üst dudak bölgesinde bu belirti bulunan deve, özelliği taşıyan varlık olarak nitelenir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birinin üst dudağını yarmak, anatomik sonucun oluşturulmasını bildiren eylemsel kullanımdır."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan veya devenin üst dudak bölgesindeki belirgin yarığı adlandıran temel kullanım için uygundur.","boundary_detail":"Belirti özellikle üst dudakta bulunur; genel çatlaklar, alt dudak ve ağız çevresindeki başka eğrilikler kapsam dışıdır.","branch_image_ar":"شق ظاهر في الشفة العليا","concept_gloss":"üst dudak yarığı","contextual_glosses":[{"applicability":"Bir insanı veya deveyi üst dudak bölgesindeki yarıkla niteleyen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Özelliğin taşıyıcıda bulunmasını ve anatomik yerini korur."},"facet_ids":["F002"],"text":"üst dudağı yarık","usage_role":"contextual"},{"applicability":"Bir kişinin üst dudağında yarık oluşturma eylemini anlatan kuruluşta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemi, etkilenen kişiyi ve üst dudak sınırını korur."},"facet_ids":["F003"],"text":"üst dudağını yarmak","usage_role":"contextual"}],"definition":"İnsanın üst dudağında veya devenin üst dudak bölgesinde bulunan belirgin yarıktır. Aynı dal, bu özelliği taşıyanı niteleyen biçimi ve üst dudağı yarma eylemini de kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Üst dudakta bulunan yarık, dalın anatomik çekirdeğini oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Üst dudağı yarık insan veya üst dudak bölgesinde bu belirti bulunan deve, özelliği taşıyan varlık olarak nitelenir."},{"facet_id":"F003","role":"associated_use","statement":"Birinin üst dudağını yarmak, anatomik sonucun oluşturulmasını bildiren eylemsel kullanımdır."}],"identity_rationale":"Kaynak ifadesi dalı açıkça üst dudaktaki yarıkla sınırlar; insanın üst dudağının yarılmış olması, devenin üst dudak bölgesindeki aynı belirti ve üst dudağı yarma eylemi bu kimliği doğrular. Genel yarılma anlamı veya alt dudaktaki bir biçim bozukluğu bu dala dahil değildir.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"üst dudaktaki yarık"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"üst dudağı yarık kişi veya deve"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"üst dudağını yarmak"}],"lexicalization_note":"Üst dudak yarığı dalın temelidir; yarıklı kişi veya deve nitelemesi ile üst dudağı yarma eylemi ilgili biçimlere bağlı tutulur.","neighbor_coverage_note":"Genel yarılma dalı süreç ve kapsam farkını, ağız eğriliği dalı ise yakın anatomik karışmayı açıklar; öteki adaylar kırık iyileşmesi, hayvan yapısı veya daha uzak ayrılma türleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yer ve sonuç bakımından üst dudağa özelleşmiş anatomik bir addır; komşu dal ise nesne ve yüzey türü bakımından geniş bir yarılma eylemidir.","focus_only":"Odak dal belirli bir anatomik yerde, üst dudakta bulunan yarığı ve bu yarıkla niteleneni bildirir.","gloss":"üst dudak yarığı ile genel yarılma","neighbor_only":"Komşu dal nesne, deri, toprak, dağ ve başka yüzeylerdeki genel yarılma ve açılma sürecini kapsar.","neighbor_ref":"root_000807/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir yüzeyin ayrılmasıyla oluşan yarık düşüncesi bulunur."},{"boundary_match":"field_only","distinction":"Yarık, dokuda açılma veya ayrılmadır; eğrilik ise bir bölümün yana yönelmiş biçimidir ve üst dudakta bir açıklık gerektirmez.","focus_only":"Odak dalda üst dudak dokusunun yarılmış olması gerekir.","gloss":"dudak yarığı ile ağız eğriliği","neighbor_only":"Komşu dalda ağız, dudak veya gözün bir yana eğri oluşu vardır; doku yarığı gerekmez.","neighbor_ref":"root_000866/B003","relation_type":"same_field","shared_zone":"İki dal yüz ve ağız çevresindeki belirgin bir yapısal özelliği adlandırır."}],"source_phrase_ar":"العلم الشق في الشفة العليا والرجل أعلم (maqayis)؛ الأعلم الذي انشقت شفته العليا (ayn)؛ علم الرجل يعلم علما إذا صار أعلم وهو المشقوق الشفة العليا (sihah)؛ علمت الرجل أعلمه علما إذا شققت شفته العليا (tahdhib)؛ البعير يقال له أعلم لعلم في مشفره الأعلى (tahdhib)؛ الشق في الشفة العليا علم (mufradat)","source_summary":"Kaynaklar yarığın yerini üst dudak olarak ortak biçimde sınırlar ve yarıklı insanı bu özellikle niteler. Toplu tanıklık, devenin üst dudak bölgesindeki karşılığını ve üst dudağı yarma eylemini de aynı dalda gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العلم والشق في الشفة العليا ووصف الرجل أو البعير بالأعلم إذا كان الشق أو العلم في الموضع الأعلى","what_is_not_ar":"ليس هو العلم بمعنى المعرفة ولا العلامة الموضوعة اختيارا ولا الشق في الشفة السفلى"},"support_links":["sup_bee3fdfaea853392e2c5"]},{"boundary":"Deniz ile suyu bol kuyu tek bir ara nesnede birleştirilmez; bunlar aynı biçimin kaynaklarda verilen iki ayrı sözlük karşılığıdır.","branch_kind":"bare","branch_ref":"root_001040/B005","candidate_links":[{"candidate_id":"cand_9059e73d4ea0033382d3","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:5:3:1","qac_word_ref":"102:5:3","surface_ar":"تَعْلَمُ"},{"lemma_ar":"عِلْم","morph_features":"STEM|POS:N|LEM:Eilom|ROOT:Elm|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:4:1","qac_word_ref":"102:5:4","surface_ar":"عِلْمَ"}],"gloss":"deniz ya da suyu bol kuyu","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dal, aynı adın iki ayrı su varlığına verilen sözlük karşılıklarını birlikte kaydeder."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kaynak karşılığında ad, geniş tuzlu su kütlesi olan denizi gösterir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Diğer ve daha yaygın kaynak karşılığında ad, suyu çok olan kuyuyu gösterir."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözlük biçiminin kaynaklarda verilen iki ayrı karşılığını eksiltmeden birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Deniz ile suyu bol kuyu tek bir ara nesnede birleştirilmez; bunlar aynı biçimin kaynaklarda verilen iki ayrı sözlük karşılığıdır.","branch_image_ar":"ماء كثير مجتمع في عيلم","concept_gloss":"deniz ya da suyu bol kuyu","contextual_glosses":[{"applicability":"Sözlük biçiminin geniş su kütlesi karşılığıyla kullanıldığı tanıklığa özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı biçim için tanıklanan suyu bol kuyu karşılığını dışarıda bırakır.","preserves":"Deniz karşılığını doğal ve doğrudan biçimde korur."},"facet_ids":["F002"],"text":"deniz","usage_role":"contextual"},{"applicability":"Sözlük biçiminin bol su içeren kuyu karşılığıyla kullanıldığı tanıklıklara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı biçim için tanıklanan deniz karşılığını dışarıda bırakır.","preserves":"Kuyu türünü ve suyunun çokluğu koşulunu korur."},"facet_ids":["F003"],"text":"suyu bol kuyu","usage_role":"contextual"}],"definition":"Aynı sözlük biçiminin bir kullanımda denizi, başka bir kullanımda ise suyu bol kuyuyu adlandırmasıdır. İki karşılık, genel bir su birikintisi anlamında kaynaştırılmaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dal, aynı adın iki ayrı su varlığına verilen sözlük karşılıklarını birlikte kaydeder."},{"facet_id":"F002","role":"source_variant","statement":"Bir kaynak karşılığında ad, geniş tuzlu su kütlesi olan denizi gösterir."},{"facet_id":"F003","role":"source_variant","statement":"Diğer ve daha yaygın kaynak karşılığında ad, suyu çok olan kuyuyu gösterir."}],"identity_rationale":"Kaynak ifadesi tek bir su birikimi türü tanımlamaz; aynı sözlük biçimi için deniz ve suyu bol kuyu olmak üzere iki ayrı karşılık verir. Dal korunabilir, ancak geçici çerçevedeki ortak su kütlesi görüntüsü yerine bu açık seçeneklilik tanıma yazılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"deniz"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"suyu bol kuyu"}],"lexicalization_note":"Tanım çıplak sözlük biçiminin deniz ve suyu bol kuyu karşılıklarını ayrı ayrı korur; bunlardan genel bir su birikintisi anlamı türetmez.","neighbor_coverage_note":"Deniz karşılığını açıklayan geniş su dalı ile kuyu çevresindeki bol su dalı seçildi; diğer adaylar gölet, artık su, taşkın veya su tutan arazi gibi farklı taşıyıcı ve süreçlere bağlıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Örtüşme yalnızca deniz karşılığındadır; odak dalın kuyu seçeneği komşuda bulunmaz, komşunun büyük ırmak ve genel su genişliği ise odak dalın tanımına girmez.","focus_only":"Odak dal aynı sözlük biçiminin suyu bol kuyu karşılığını da bağımsız bir seçenek olarak taşır.","gloss":"deniz ve geniş su","neighbor_only":"Komşu dal deniz yanında büyük ırmak ve farklı büyüklükte su alanlarına uzanan genel bir geniş su kapsamına sahiptir.","neighbor_ref":"root_000086/B001","relation_type":"near_synonym","shared_zone":"Odak dalın deniz karşılığı, komşu dalın geniş ve çok su çekirdeğiyle örtüşür."},{"boundary_match":"partial","distinction":"Odak dal suyu taşıyan kuyuyu niteler; komşu dal ise kuyudan dökülen suyu ve taşma sürecini merkez alır.","focus_only":"Odak dal kuyunun kendisini suyunun bol olması koşuluyla adlandırır.","gloss":"suyu bol kuyu ile kuyu suyu","neighbor_only":"Komşu dal kuyudaki kovadan dökülen veya havuza taşan suyu, kokusunu ve taşma olayını anlatır.","neighbor_ref":"root_001077/B003","relation_type":"near_neighbor","shared_zone":"İki dal kuyu çevresinde suyun çokluğu ve görünür birikimiyle ilişkilidir."}],"source_phrase_ar":"العيلم يقال إنه البحر ويقال إنه البئر الكثيرة الماء (maqayis)؛ العيلم الركية الكثيرة الماء (sihah)؛ العيلم البئر الكثيرة الماء (tahdhib)","source_summary":"Toplu tanıklık iki karşılığı yan yana verir: bir aktarım sözcüğü deniz olarak açıklar, öteki tanıklıklar ise suyu bol kuyu anlamını destekler. Kaynaklara özgü ayrı claim kimlikleri bulunmadığı için bu karşıtlık ortak özet içinde, atıf uydurulmadan korunur.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه العيلم بمعنى البحر أو البئر الكثيرة الماء","what_is_not_ar":"ليس هو العالمين ولا العلم ولا العلامة ولا العيلم بمعنى آخر غير مائي"},"support_links":["sup_05cea3dcf4b9c1d1c652"]},{"boundary":"Çekirdek yırtıcı kuş adıdır; çevik ve zeki erkek nitelemesi yalnızca bu addan türeyen biçime bağlıdır.","branch_kind":"bare","branch_ref":"root_001040/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:5:3:1","qac_word_ref":"102:5:3","surface_ar":"تَعْلَمُ"},{"lemma_ar":"عِلْم","morph_features":"STEM|POS:N|LEM:Eilom|ROOT:Elm|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:4:1","qac_word_ref":"102:5:4","surface_ar":"عِلْمَ"}],"gloss":"doğan veya atmaca türü yırtıcı kuş","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ad, doğan veya atmaca türünden avcı bir kuşu gösterir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuş adından türeyen insan nitelemesi, çevik ve zeki bir erkeği belirtir."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın temel kuş adını iki kaynak karşılığı arasındaki seçenekliliği koruyarak açıklamak için uygundur.","boundary_detail":"Çekirdek yırtıcı kuş adıdır; çevik ve zeki erkek nitelemesi yalnızca bu addan türeyen biçime bağlıdır.","branch_image_ar":"طائر جارح يسمى العلام","concept_gloss":"doğan veya atmaca türü yırtıcı kuş","contextual_glosses":[{"applicability":"Kuş adından türemiş insan nitelemesinin kullanıldığı bağlama özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan oluşu ile çeviklik ve zekâ niteliklerini birlikte korur."},"facet_ids":["F002"],"text":"çevik ve zeki adam","usage_role":"contextual"}],"definition":"Doğan veya atmaca türünden bir yırtıcı kuş adıdır. Bu kuş adından türetilen bir niteleme, çevik ve zeki bir erkeği anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ad, doğan veya atmaca türünden avcı bir kuşu gösterir."},{"facet_id":"F002","role":"associated_use","statement":"Kuş adından türeyen insan nitelemesi, çevik ve zeki bir erkeği belirtir."}],"identity_rationale":"Kaynak ifadesi temel adı doğan veya atmaca türünden yırtıcı kuş için verir ve geçici dal görüntüsünü doğrular. Çevik ve zeki erkek nitelemesi ise kuş adından türetilmiş ayrı bir biçimdir; kuşun tanımına doğrudan katılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"doğan veya atmaca"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"çevik ve zeki adam"}],"lexicalization_note":"Çıplak dal doğan veya atmaca türünden kuş adını tanımlar; insan nitelemesi türemiş bir sözcüksel uzantı olarak bağımlı tutulur.","neighbor_coverage_note":"Yırtıcı kuş sınıfında en yakın iki aday seçildi; diğer adaylar kanat çırpma, beslenme, farklı hayvan adları veya yalnızca uzak bir doğan ilişkisi taşır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Aynı kuş alanını paylaşsalar da komşu dal renk ve ara tür özellikleriyle daha dar bir kuşu adlandırır; odak dalın türemiş insan nitelemesi de komşuda yoktur.","focus_only":"Odak dal doğan veya atmaca karşılığı taşıyan kuş adını ve ondan türeyen insan nitelemesini içerir.","gloss":"yırtıcı kuş adları","neighbor_only":"Komşu dal mavi renkli, doğan ile atmaca arasında tanımlanan veya beyaz doğan sayılan daha özel bir kuş adıdır.","neighbor_ref":"root_000631/B002","relation_type":"same_field","shared_zone":"Her iki dal doğan ve atmaca çevresindeki avcı kuş adlandırmaları alanındadır."},{"boundary_match":"partial","distinction":"Odak dalda zekâ kuştan türetilen insan niteliğinde belirginleşir; komşuda ise doğrudan belirli doğanların özelliğidir.","focus_only":"Odak dal doğan veya atmaca türünü genel bir adla karşılar ve bu addan insan nitelemesi türetir.","gloss":"doğan adı ile zeki doğan nitelemesi","neighbor_only":"Komşu dal özellikle zeki ve keskin bakışlı doğanlara verilen bir adı belirtir.","neighbor_ref":"root_001375/B006","relation_type":"near_neighbor","shared_zone":"İki dal doğan türünden yırtıcı kuşları adlandırır ve zekâ çağrışımını paylaşır."}],"source_phrase_ar":"العلام الصقر؛ العلامي الرجل الخفيف الذكي مأخوذ من العلام؛ العلام الباشق (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık temel adı doğan veya atmaca türünden kuş için verir ve türemiş biçimi çevik, zeki erkek olarak açıklar."}],"source_summary":"Dal tek bir sözlük tanıklığında yırtıcı kuş adı ile bu addan türetilmiş çevik ve zeki erkek nitelemesini birlikte sunar.","sources":["TA"],"what_is_ar":"يدخل فيه العلام بمعنى الصقر أو الباشق وما نسب إليه من العلامي","what_is_not_ar":"ليس هو العلام بمعنى الحناء ولا العلامة ولا العالم"},"support_links":[]},{"boundary":"Dal yalnızca erkek sırtlanı adlandırır; başka erkek hayvan adları ve benzer sesli su veya kuş adları kapsam dışıdır.","branch_kind":"bare","branch_ref":"root_001040/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:5:3:1","qac_word_ref":"102:5:3","surface_ar":"تَعْلَمُ"},{"lemma_ar":"عِلْم","morph_features":"STEM|POS:N|LEM:Eilom|ROOT:Elm|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:4:1","qac_word_ref":"102:5:4","surface_ar":"عِلْمَ"}],"gloss":"erkek sırtlan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Adlandırılan canlı, cinsiyeti erkek olan sırtlandır."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvanın türünü ve erkek oluşunu birlikte veren bütün bağlamlarda tam karşılıktır.","boundary_detail":"Dal yalnızca erkek sırtlanı adlandırır; başka erkek hayvan adları ve benzer sesli su veya kuş adları kapsam dışıdır.","branch_image_ar":"ذكر الضباع يسمى العيلام","concept_gloss":"erkek sırtlan","definition":"Erkek sırtlanı adlandıran yalın bir hayvan adıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Adlandırılan canlı, cinsiyeti erkek olan sırtlandır."}],"identity_rationale":"Kaynak ifadesinin iki tanıklığı da sözcüğü doğrudan erkek sırtlan olarak açıklar. Geçici dal görüntüsü bu yalın hayvan adıyla tam uyumludur ve başka bir tür, özellik veya mecaz eklemeyi gerektirmez.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"erkek sırtlan"}],"lexicalization_note":"Tanım çıplak hayvan adını erkek sırtlanla sınırlar ve başka türlere ya da bağlı kuruluşlara genişletmez.","neighbor_coverage_note":"Erkek sırtlanı aynı sınırlarla adlandıran aday tam eş anlamlı olarak seçildi; diğer adaylar kurt, erkek domuz, aslan, kuş veya daha geniş hayvan sınıflarıdır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Anlam çekirdeği, hayvan türü ve cinsiyet sınırı aynıdır; ayrım yalnızca kullanılan sözlük biçimindedir.","focus_only":null,"gloss":"erkek sırtlan","neighbor_only":null,"neighbor_ref":"root_001068/B007","relation_type":"synonym","shared_zone":"Her iki dal da hiçbir ek koşul getirmeden erkek sırtlanı adlandırır."}],"source_phrase_ar":"العيلام الذكر من الضباع (sihah)؛ العيلام الضبعان وهو ذكر الضباع (tahdhib)","source_summary":"Kaynaklar sözcüğün erkek sırtlanı adlandırdığı konusunda birleşir ve ek bir anlam ayrımı bildirmez.","sources":["SI","TA"],"what_is_ar":"يدخل فيه العيلام بمعنى ذكر الضباع","what_is_not_ar":"ليس هو العيلم البئر الكثيرة الماء ولا العلامة ولا العلم"},"support_links":[]},{"boundary":"Direct seeing, eyewitness presence, or manifest encounter by the eye.","branch_kind":null,"branch_ref":"root_001069/B002","candidate_links":[{"candidate_id":"cand_7550e314f5aaffbd1c56","lane":"macro"}],"focus_root_occurrences":[],"gloss":"Seeing face to face","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"المشاهدة بالعين","image_en":"Seeing face to face"}}],"root_ar":"ع ي ن","root_id":"root_001069","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"المشاهدة بالعين","image_en":"Seeing face to face","scope_ar":"العيان والمعاينة والرؤية بالعين، ولقاء الشيء أو فعله على عين ويقين.","scope_en":"Direct seeing, eyewitness presence, or manifest encounter by the eye."},"support_links":["sup_85856ff21ce630f22514"]},{"boundary":"Dalın özü kesinleşmiş bilgidir; duyulanı hemen doğru sayma ve öldürmenin kesinliğini belirtme yalnızca belirli yapılara bağlı kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001696/B001","candidate_links":[{"candidate_id":"cand_7550e314f5aaffbd1c56","lane":"macro"},{"candidate_id":"cand_644712471f5a1351c960","lane":"macro"},{"candidate_id":"cand_a03f25769e9b19783711","lane":"macro"},{"candidate_id":"cand_5465175ae6b3ef5134aa","lane":"macro"},{"candidate_id":"cand_76e49d74dab883ea4e4a","lane":"macro"},{"candidate_id":"cand_432fff901f7137496e5e","lane":"macro"},{"candidate_id":"cand_9059e73d4ea0033382d3","lane":"macro"},{"candidate_id":"cand_c7e1299e0390be2b582e","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"يَقِين","morph_features":"STEM|POS:N|LEM:yaqiyn|ROOT:yqn|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:5:2","qac_word_ref":"102:5:5","surface_ar":"يَقِينِ"}],"gloss":"kuşkunun giderilmesiyle kesinleşen bilgi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kuşku giderilir ve ele alınan şeyin doğruluğu kesinleştirilir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Anlayış yatışır, yargı sabitlenir ve bilgi kuşkuya yer bırakmayacak biçimde yerleşir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çeşitli fiil biçimleri, bir şeyin doğruluğunu kesin olarak bilme veya bu kesinliğe ulaşma eylemini anlatır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Duyduğu her şeyi hiçbir kuşku duymadan doğru sayan kişi, belirli bir söz öbeğiyle nitelenir."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Öldürme bağlamındaki belirli yapı, öldürme eyleminden çok o eylemin gerçekleştiğinin kesin olarak bilinmesini belirtir."}}],"root_ar":"ي ق ن","root_id":"root_001696","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın çıplak anlam çekirdeğini, hem kuşkunun kalkmasını hem de bilgi ile yargının sabitlenmesini birlikte anlatır.","boundary_detail":"Dalın özü kesinleşmiş bilgidir; duyulanı hemen doğru sayma ve öldürmenin kesinliğini belirtme yalnızca belirli yapılara bağlı kullanımlardır.","branch_image_ar":"ثبات العلم وزوال الشك","concept_gloss":"kuşkunun giderilmesiyle kesinleşen bilgi","contextual_glosses":[{"applicability":"Sonuç durumunun öne çıktığı ad kullanımlarında doğal ve kısa bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kuşkunun etkin biçimde giderilmesi ve doğruluğun araştırılarak belirlenmesi sürecini açıkça söylemez.","preserves":"Kuşkusuz ve sabit olma sonucunu korur."},"facet_ids":["F001","F002"],"text":"kesinlik","usage_role":"general"},{"applicability":"Fiil biçimlerinin bir şey hakkındaki kuşkunun kalkıp bilginin sabitlenmesini anlattığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilginin kuşkuya yer bırakmadan doğrulanmasını ve sabitlenmesini korur."},"facet_ids":["F001","F002","F003"],"text":"kesin olarak bilmek","usage_role":"contextual"},{"applicability":"Konuşma dilinde kuşkunun sona ermesi öne çıkarıldığında uygun bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bilginin ve yargının doğrulanıp sabitlenmesini açıkça belirtmez.","preserves":"Kuşkunun tümüyle ortadan kalkmasını korur."},"facet_ids":["F001"],"text":"kuşkusu kalmamak","usage_role":"contextual"},{"applicability":"Öldürme eyleminin gerçekleşip gerçekleşmediğine ilişkin kesinliğin anlatıldığı özel yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemin kendisiyle, o eylemin gerçekleştiğine ilişkin kesin bilgiyi birbirinden ayırır."},"facet_ids":["F005"],"text":"gerçekleştiğini kesin olarak bilmek","usage_role":"explanatory"}],"definition":"Kuşkunun ortadan kalkmasıyla anlayışın yatışması, yargının sabitlenmesi ve bir şey hakkındaki bilginin değişmez biçimde kesinleşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kuşku giderilir ve ele alınan şeyin doğruluğu kesinleştirilir."},{"facet_id":"F002","role":"core","statement":"Anlayış yatışır, yargı sabitlenir ve bilgi kuşkuya yer bırakmayacak biçimde yerleşir."},{"facet_id":"F003","role":"extension","statement":"Çeşitli fiil biçimleri, bir şeyin doğruluğunu kesin olarak bilme veya bu kesinliğe ulaşma eylemini anlatır."},{"facet_id":"F004","role":"associated_use","statement":"Duyduğu her şeyi hiçbir kuşku duymadan doğru sayan kişi, belirli bir söz öbeğiyle nitelenir."},{"facet_id":"F005","role":"associated_use","statement":"Öldürme bağlamındaki belirli yapı, öldürme eyleminden çok o eylemin gerçekleştiğinin kesin olarak bilinmesini belirtir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kesinlik düzeyi belirtilmeyen her türlü bilmeyi kapsar.","collision":"Sıradan veya değişebilir bilgiyle karışır.","fit":"broadening","loses":"Kuşkunun giderilmesini ve yargının değişmez biçimde sabitlenmesini belirtmez.","preserves":"Bir şeyin bilinmesi unsurunu korur."},"text":"bilgi"}],"identity_rationale":"Kaynak ifadesinin ortak çekirdeği, kuşkunun giderilmesiyle bilginin ve yargının değişmez biçimde yerleşmesidir. Verilen çerçeve bu çekirdeği doğru yansıtır; fiil biçimleri ile duyma ve öldürme bağlamlarındaki kullanımlar ise çekirdeğin ayrı gerçekleşmeleri olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kuşkunun kalkması ve bilginin kesinleşmesi"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kuşkusuz ve sabit bilgi"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"kesin olarak bilmek; kuşkusu kalmamak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir şeyin doğruluğunu kesin olarak bilmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kesin olarak bilme"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kesinliğe varmak; kesin olarak bilmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir şeyden kesin biçimde emin olmak; kuşkusu kalmamak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kesin olarak bilen, kuşkusu olmayan"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kesin bilen; kendisine ulaşan haberi hemen doğru sayan"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"duyduğu her şeyi kesin doğru sayan kimse"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"onun hakkında hiçbir kuşkusu olmamak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kesin bilen kimseyi bildiren küçültme biçimi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"kesin bilgi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kesinliğin bilgi diye adlandırılan mertebesi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kesinliğin göz diye adlandırılan mertebesi"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"kesinliğin hakikat diye adlandırılan mertebesi"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"öldürmenin gerçekleştiğini kesin olarak bilmek"}],"lexicalization_note":"Tanım çıplak anlam çekirdeğini verir; fiil biçimleri ve belirli söz öbekleri bu çekirdeğe bağlı ayrı yüzler olarak gösterilir ve bütün dala genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan dört karşılaştırma kesinlik sınırını doğrudan aydınlatır, kalanlar ise yalnızca aynı bilgi alanında bulunur veya çekirdekle yeterli anlam örtüşmesi göstermez.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dalda tereddüt sona erip bilgi sabitlenirken komşu dalda karşıt seçenekler dengede kalır ve kesin bir hükme ulaşılamaz.","focus_only":"Bilgi ve yargı sabitlenir, kuşku ortadan kalkar.","gloss":"kuşkunun karşıtı olan kesinlik","neighbor_only":"Karşıt olasılıklar arasında karar verilemez ve hüküm sabitlenmez.","neighbor_ref":"root_000812/B001","relation_type":"polarity_pair","shared_zone":"İki dal da bir yargının doğruluk bakımından ne ölçüde sabit olduğunu gösteren aynı eksende yer alır."},{"boundary_match":"partial","distinction":"Odak dal tam kuşkusuzluğu ve sabit bilgiyi gerektirir; komşu dal ise bir belirtiden doğan güçlü yargıyı da kapsadığı için daha düşük bir kesinlik düzeyine açık kalır.","focus_only":"Kuşkunun tümüyle giderilmesi ve bilginin sabitlenmesi için önceden bir belirtiye dayanma şartı yoktur.","gloss":"belirtiye dayalı güçlü yargı","neighbor_only":"Güçlü yargı, bir belirtiye dayanabilir ve tam kesinliğe ulaşmadan da kullanılabilir.","neighbor_ref":"root_000969/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyi doğru sayan güçlü ve yerleşmiş bir bilişsel tutumu anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalı ayıran ölçüt kuşkunun kalkmasıdır; komşu dalı ayıran ölçüt ise bilginin derinliği ve kişide kök salmasıdır.","focus_only":"Kuşkunun giderilerek belirli bir şeyin doğruluğunun kesinleşmesini öne çıkarır.","gloss":"kökleşmiş derin bilgi","neighbor_only":"Bilginin kişide derinleşip kökleşmesini ve güçlü bir bilgi birikimine dönüşmesini öne çıkarır.","neighbor_ref":"root_000561/B002","relation_type":"near_synonym","shared_zone":"İki dalda da bilgi geçici değildir ve bilen kişide sağlam biçimde yerleşmiştir."},{"boundary_match":"partial","distinction":"Derin kavrayış bir şeyi açıkça görme veya anlama yetisini anlatabilir; odak dal ise bunun ötesinde kuşkunun bitmiş ve hükmün sabitlenmiş olmasını şart koşar.","focus_only":"Belirli bir yargıda kuşkunun ortadan kalkmasını ve bilginin sabitlenmesini gerektirir.","gloss":"derin kavrayış ve içgörü","neighbor_only":"İçgörü, kanıttan ders çıkarma ve bir konuyu derinden kavrama gibi daha geniş bilişsel yetileri kapsar.","neighbor_ref":"root_000121/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal, yüzeysel sanının ötesine geçen doğrulayıcı bir kavrayışla ilişkilidir."}],"source_phrase_ar":"اليقن واليقين زوال الشك (maqayis)؛ اليقن اليقين وهو إزاحة الشك وتحقيق الأمر (ayn;tahdhib)؛ اليقين العلم وزوال الشك (sihah)؛ سكون الفهم مع ثبات الحكم (mufradat)؛ أيقن واستيقن وتيقن كله واحد (ayn;sihah;tahdhib)؛ رجل أذن يقن وهو الذي لا يسمع بشيء إلا أيقن به (tahdhib)؛ ما قتلوه يقينا أي ما قتلوه قتلا تيقنوه (mufradat)","source_summary":"Kaynakların birleşik anlatımı, kuşkunun giderilmesini, anlayışın yatışmasını ve yargıyla bilginin sabitlenmesini ortak çekirdek yapar. Aynı anlatım, kesin olarak bilme bildiren fiilleri ve kesinliğin duyma ya da öldürme bağlamında özel bir yapıyla dile getirildiği kullanımları da bu çekirdeğe bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"اليقن واليقين؛ إزاحة الشك وتحقيق الأمر؛ العلم الثابت فوق المعرفة والدراية؛ أيقن واستيقن وتيقن؛ قتل تيقنه؛ أذن يقن يوقن بما يسمعه","what_is_not_ar":"الموقونة بمعنى الجارية المصونة المخدرة"},"support_links":["sup_05cea3dcf4b9c1d1c652","sup_07989b0d9a51f41140cb","sup_0e29f72908ca23bcdc4b","sup_1b840a54752a0d94954e","sup_48ee5148dabc78836f11","sup_657d451ca01613003c1c","sup_7c7013bbc61d5a57f8f2","sup_85856ff21ce630f22514"]},{"boundary":"Anlam yalnızca örtünme veya saklanma eylemi değildir; koruma altında ve gözden uzak tutulan genç kadın kişisini belirtir.","branch_kind":"bare","branch_ref":"root_001696/B002","candidate_links":[{"candidate_id":"cand_c8ce457146fa6c4665f9","lane":"macro"},{"candidate_id":"cand_94af7dcb4e5eccdfb374","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"يَقِين","morph_features":"STEM|POS:N|LEM:yaqiyn|ROOT:yqn|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:5:2","qac_word_ref":"102:5:5","surface_ar":"يَقِينِ"}],"gloss":"korunup gözden uzak tutulan genç kadın","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderim yapılan kişi genç bir kadındır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu kişi koruma altında tutulur ve dışarıdan görülmeyecek biçimde gözden uzak yaşar."}}],"root_ar":"ي ق ن","root_id":"root_001696","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişiyi, koruma altında bulunma ve dışarıdan görülmeme nitelikleriyle birlikte eksiksiz tanımlar.","boundary_detail":"Anlam yalnızca örtünme veya saklanma eylemi değildir; koruma altında ve gözden uzak tutulan genç kadın kişisini belirtir.","branch_image_ar":"صون الجارية وخدرها","concept_gloss":"korunup gözden uzak tutulan genç kadın","contextual_glosses":[{"applicability":"Koruma ile görünür olmama durumunun tek ve doğal bir nitelemeyle anlatılabildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Korumanın fiziksel veya toplumsal kapsamını açıkça belirtmez.","preserves":"Genç kadının başkalarının gözünden uzak ve gözetilerek tutulmasını korur."},"facet_ids":["F001","F002"],"text":"gözlerden sakınılan genç kadın","usage_role":"contextual"}],"definition":"Koruma altında bulunan ve dışarıya çıkarılmayarak gözden uzak tutulan genç kadındır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderim yapılan kişi genç bir kadındır."},{"facet_id":"F002","role":"core","statement":"Bu kişi koruma altında tutulur ve dışarıdan görülmeyecek biçimde gözden uzak yaşar."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Yalnızca giysiyle örtünmüş herhangi bir kadın anlamıyla karışır.","fit":"narrowing","loses":"Koruma altında tutulmayı, gözden uzak yaşamayı ve gençlik niteliğini belirtmez.","preserves":"Kadının dışarıdan görünmemesi yönünü kısmen korur."},"text":"örtülü kadın"}],"identity_rationale":"Kaynak ifadesi, korunan ve dışarıdan gözlenmeyecek biçimde ev içinde tutulan genç bir kadını doğrudan tanımlar. Verilen dal çerçevesi hem kişi türünü hem de koruma ile gözden uzak tutma niteliklerini doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"koruma altında ve gözden uzak tutulan genç kadın"}],"lexicalization_note":"Tanım, tek başına kişi bildiren dalı kapsar; başka bir yapıya bağlı anlam veya genel bir örtme eylemi tanıma eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen karşılaştırmalar kişi, saklılık, koruma ve örtü arasındaki sınırları gösterir, kalan adaylar ise yalnızca daha uzak örtme ya da kapatma durumlarını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda koruma ve dışarı çıkarmama birlikte kurucu niteliktedir; komşu dalda ise asıl ölçüt gizli bulunmadır ve koruma zorunlu değildir.","focus_only":"Genç kadının korunma amacıyla sürekli biçimde gözden uzak tutulmasını içerir.","gloss":"saklanan kadın","neighbor_only":"Bir kadının saklanması veya görünüp yeniden gizlenmesi, koruma altında bulunmadan da gerçekleşebilir.","neighbor_ref":"root_000384/B003","relation_type":"near_synonym","shared_zone":"İki dal da görünür alanda bulunmayan bir kadın kişisini anlatır."},{"boundary_match":"field_only","distinction":"Komşu dal genel bir örtme ve koruma alanıdır; odak dal ise bu işlemin sonucu sayılabilecek özel bir durumdaki belirli kişi türünü anlatır.","focus_only":"Örtme veya koruma işlemini değil, bu durumda tutulan genç kadın kişisini adlandırır.","gloss":"genel örtme ve koruma","neighbor_only":"Herhangi bir şeyi örten, kaplayan veya koruyan genel işlemi ve araçları kapsar.","neighbor_ref":"root_001096/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda dış etkiden koruma ve görünürlüğü azaltma düşüncesi bulunur."},{"boundary_match":"field_only","distinction":"Komşu dal yalnızca kişi türünü bildirir; odak dalda ise o kişinin koruma altında bulunması ve görünür alandan uzak tutulması anlamın ayrılmaz parçasıdır.","focus_only":"Genç kadını korunma ve gözden uzak tutulma durumuyla sınırlar.","gloss":"genç kadın","neighbor_only":"Genç kadın kişi türünü, korunma veya saklı yaşama şartı olmadan genel olarak belirtir.","neighbor_ref":"root_000240/B004","relation_type":"same_field","shared_zone":"Her iki dalın gönderimi genç kadın kişi alanındadır."},{"boundary_match":"thematic_only","distinction":"Yüzü örten nesne, kişinin bütünüyle gözden uzak tutulduğunu veya koruma altında bulunduğunu göstermez; odak dalın gönderimi de örtüye değil kişiyedir.","focus_only":"Bir giysi veya araç değil, korunup gözden uzak tutulan kişiyi belirtir.","gloss":"yüz örtüsü","neighbor_only":"Kadının yüzüne taktığı belirli örtüyü ve onu takma eylemini belirtir.","neighbor_ref":"root_001539/B012","relation_type":"thematic","shared_zone":"İki dal kadınların görünürlüğünü azaltma çevresinde aynı toplumsal durumda buluşabilir."}],"source_phrase_ar":"الموقونة الجارية المصونة المخدرة (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu anlam, koruma altında ve gözden uzak tutulan genç kadın biçiminde tek kaynaktan aktarılır."}],"source_summary":"Dal, kişi türü ile onun içinde bulunduğu durumu tek bir anlamda birleştirir: genç kadın hem korunur hem de dışarıdan gözlenmeyecek biçimde gözden uzak tutulur.","sources":["TA"],"what_is_ar":"الموقونة بمعنى الجارية المصونة المخدرة","what_is_not_ar":"اليقين وزوال الشك وأفعال أيقن واستيقن وتيقن"},"support_links":["sup_28725db7daa3c1e60994","sup_799d2d44713056e346bd"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000225/B001","candidate_links":[{"candidate_id":"cand_76e49d74dab883ea4e4a","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_360b71ce9ea7700cca2c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The intensely blazing object gives the later sight material force and raises the cost of deferred disclosure.","root":"ج ح م","source_ref":"102:6","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000225","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_1b840a54752a0d94954e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000531/B012","candidate_links":[{"candidate_id":"cand_76e49d74dab883ea4e4a","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_360b71ce9ea7700cca2c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Causing something to appear makes the later stage an imposed manifestation, not merely stronger private confidence.","root":"ر ء ي","source_ref":"102:7","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000531","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_1b840a54752a0d94954e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000615/B001","candidate_links":[{"candidate_id":"cand_9059e73d4ea0033382d3","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_18b0248709c9857af23e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The non-dominant mapped branch of quenching thirst supplies the functional test for whether gathered knowledge transforms the knower.","root":"ر ء ي","source_ref":"102:6","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000615","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_05cea3dcf4b9c1d1c652"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000654/B003","candidate_links":[{"candidate_id":"cand_a03f25769e9b19783711","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_065e4c29929a255ede1b","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The visitor's directed approach supplies motion toward a place without making that place a permanent endpoint.","root":"ز و ر","source_ref":"102:2","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000654","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_657d451ca01613003c1c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000661/B001","candidate_links":[{"candidate_id":"cand_c7e1299e0390be2b582e","lane":"macro"},{"candidate_id":"cand_e2e57017aed461a0d11a","lane":"macro"},{"candidate_id":"cand_d54671499bc005d63445","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_edf0a518a919d035d048","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Question and demand convert certainty from an inward state into a relation in which a response is owed.","root":"س ء ل","source_ref":"102:8","source_word_indices":["2"]},{"hft_ref":"hft_ae5745051ed988b87e2b","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Question and demand provide the overt social mechanism by which an answer is required.","root":"س ء ل","source_ref":"102:8","source_word_indices":["2"]},{"hft_ref":"hft_d5fad5d28301ebbec06a","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Questioning redirects the oral threshold from consumption or diversion toward an owed answer.","root":"س ء ل","source_ref":"102:8","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000661","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_73ecebd7bd63926a55c1","sup_7c7013bbc61d5a57f8f2","sup_bee3fdfaea853392e2c5"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000736/B001","candidate_links":[{"candidate_id":"cand_e2e57017aed461a0d11a","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_ae5745051ed988b87e2b","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The secondary image of gently drawing something out turns questioning into exploratory extraction of what remained concealed.","root":"س ء ل","source_ref":"102:8","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000736","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_73ecebd7bd63926a55c1"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001069/B006","candidate_links":[{"candidate_id":"cand_9059e73d4ea0033382d3","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_18b0248709c9857af23e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A flowing spring supplies source and circulation, changing the focus reservoir from stored quantity into replenishing contact.","root":"ع ي ن","source_ref":"102:7","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001069","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_05cea3dcf4b9c1d1c652"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001069/B013","candidate_links":[{"candidate_id":"cand_432fff901f7137496e5e","lane":"macro"},{"candidate_id":"cand_94af7dcb4e5eccdfb374","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_79e47dbbcc4e626f9b5c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The thing itself supplies immediate presence as the later counterpart to knowledge by a pointing mark.","root":"ع ي ن","source_ref":"102:7","source_word_indices":["3"]},{"hft_ref":"hft_fab1e1970046c7e28d4e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The thing itself supplies the later presence into which guarded, pre-visual certainty can emerge.","root":"ع ي ن","source_ref":"102:7","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001069","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_07989b0d9a51f41140cb","sup_28725db7daa3c1e60994"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001195/B002","candidate_links":[{"candidate_id":"cand_a03f25769e9b19783711","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_065e4c29929a255ede1b","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Lowered concealment supplies the terrain through which the distinguishing mark must guide.","root":"ق ب ر","source_ref":"102:2","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001195","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_657d451ca01613003c1c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001286/B002","candidate_links":[{"candidate_id":"cand_644712471f5a1351c960","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_695109b1043bd917f150","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Rivalry through number supplies the seductive but defective metric governing that displaced attention.","root":"ك ث ر","source_ref":"102:1","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001286","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_48ee5148dabc78836f11"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001286/B007","candidate_links":[{"candidate_id":"cand_9059e73d4ea0033382d3","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_18b0248709c9857af23e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The gathering of a thing supplies accumulation, which can remain inert and competitive unless it becomes usable knowledge.","root":"ك ث ر","source_ref":"102:1","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001286","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_05cea3dcf4b9c1d1c652"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001382/B001","candidate_links":[{"candidate_id":"cand_644712471f5a1351c960","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_695109b1043bd917f150","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Occupation by one thing away from another supplies the attentional displacement that prevents disclosure.","root":"ل ه و","source_ref":"102:1","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001382","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_48ee5148dabc78836f11"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001382/B004","candidate_links":[{"candidate_id":"cand_d54671499bc005d63445","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_d5fad5d28301ebbec06a","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The flesh over the throat extends the image from lip to the inner threshold of intake and utterance.","root":"ل ه و","source_ref":"102:1","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001382","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_bee3fdfaea853392e2c5"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001525/B001","candidate_links":[{"candidate_id":"cand_c7e1299e0390be2b582e","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_edf0a518a919d035d048","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Good condition and benefit identify the concrete field for which the knower becomes answerable.","root":"ن ع م","source_ref":"102:8","source_word_indices":["5"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001525","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_7c7013bbc61d5a57f8f2"]}],"candidate_inventory":[{"anchor_refs":["102:3","102:5","102:6","102:7"],"branch_refs":["root_000531/B001","root_001040/B001","root_001069/B002","root_001696/B001"],"candidate_id":"cand_7550e314f5aaffbd1c56","commentary_obligation":"review","focus_branch_refs":["root_001040/B001","root_001696/B001"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000531/B001","root_001069/B002"],"root_ids":[],"scope":"pericope","source_local_id":"A:Sight Ripening into Certainty","source_type":"channel","support_ids":["sup_2fff480e326f32aaa58c","sup_60ee37c4cfc2eec781a5","sup_6b288bb5b51033784696","sup_85856ff21ce630f22514","sup_ea4a930d2ea1a20f6870"],"title":"Sight Ripening into Certainty","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["102:5","102:7"],"branch_refs":["root_001696/B002"],"candidate_id":"cand_c8ce457146fa6c4665f9","commentary_obligation":"review","focus_branch_refs":["root_001696/B002"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":[],"root_ids":[],"scope":"pericope","source_local_id":"B:Protected Seclusion","source_type":"channel","support_ids":["sup_17f4205d32ea1b1a955d","sup_1db1febc0f8f60d3f075","sup_21eb2e506919b1775722","sup_799d2d44713056e346bd","sup_bf8de0af7bd7b96c8dd9"],"title":"Protected Seclusion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["102:1","102:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"102:5","branch_refs":["root_001040/B002","root_001286/B002","root_001382/B001","root_001696/B001"],"candidate_id":"cand_644712471f5a1351c960","commentary_obligation":"review","hft_ref":"hft_695109b1043bd917f150","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_metric_reorientation","source_type":"hft","support_ids":["sup_48ee5148dabc78836f11"],"title":"d_metric_reorientation","trust":"legacy_unbound"},{"anchor_refs":["102:2","102:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"102:5","branch_refs":["root_000654/B003","root_001040/B002","root_001195/B002","root_001696/B001"],"candidate_id":"cand_a03f25769e9b19783711","commentary_obligation":"review","hft_ref":"hft_065e4c29929a255ede1b","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_hidden_waypoint","source_type":"hft","support_ids":["sup_657d451ca01613003c1c"],"title":"d_hidden_waypoint","trust":"legacy_unbound"},{"anchor_refs":["102:3","102:4","102:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"102:5","branch_refs":["root_001040/B001","root_001696/B001"],"candidate_id":"cand_5465175ae6b3ef5134aa","commentary_obligation":"review","hft_ref":"hft_35a3c57ee866ee7fe05d","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_temporal_fork","source_type":"hft","support_ids":["sup_0e29f72908ca23bcdc4b"],"title":"d_temporal_fork","trust":"legacy_unbound"},{"anchor_refs":["102:5","102:6","102:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"102:5","branch_refs":["root_000225/B001","root_000531/B001","root_000531/B012","root_001040/B001","root_001696/B001"],"candidate_id":"cand_76e49d74dab883ea4e4a","commentary_obligation":"review","hft_ref":"hft_360b71ce9ea7700cca2c","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_previsual_disclosure","source_type":"hft","support_ids":["sup_1b840a54752a0d94954e"],"title":"d_previsual_disclosure","trust":"legacy_unbound"},{"anchor_refs":["102:5","102:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"102:5","branch_refs":["root_001040/B002","root_001069/B013","root_001696/B001"],"candidate_id":"cand_432fff901f7137496e5e","commentary_obligation":"review","hft_ref":"hft_79e47dbbcc4e626f9b5c","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_sign_to_presence","source_type":"hft","support_ids":["sup_07989b0d9a51f41140cb"],"title":"d_sign_to_presence","trust":"legacy_unbound"},{"anchor_refs":["102:1","102:5","102:6","102:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"102:5","branch_refs":["root_000615/B001","root_001040/B005","root_001069/B006","root_001286/B007","root_001696/B001"],"candidate_id":"cand_9059e73d4ea0033382d3","commentary_obligation":"review","hft_ref":"hft_18b0248709c9857af23e","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_hydraulic_circuit","source_type":"hft","support_ids":["sup_05cea3dcf4b9c1d1c652"],"title":"d_hydraulic_circuit","trust":"legacy_unbound"},{"anchor_refs":["102:5","102:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"102:5","branch_refs":["root_000661/B001","root_001040/B001","root_001525/B001","root_001696/B001"],"candidate_id":"cand_c7e1299e0390be2b582e","commentary_obligation":"review","hft_ref":"hft_edf0a518a919d035d048","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_answerable_certainty","source_type":"hft","support_ids":["sup_7c7013bbc61d5a57f8f2"],"title":"d_answerable_certainty","trust":"legacy_unbound"},{"anchor_refs":["102:5","102:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"102:5","branch_refs":["root_001069/B013","root_001696/B002"],"candidate_id":"cand_94af7dcb4e5eccdfb374","commentary_obligation":"review","hft_ref":"hft_fab1e1970046c7e28d4e","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:o_guarded_certainty","source_type":"hft","support_ids":["sup_28725db7daa3c1e60994"],"title":"o_guarded_certainty","trust":"legacy_unbound"},{"anchor_refs":["102:5","102:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"102:5","branch_refs":["root_000661/B001","root_000736/B001","root_001040/B001"],"candidate_id":"cand_e2e57017aed461a0d11a","commentary_obligation":"review","hft_ref":"hft_ae5745051ed988b87e2b","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:o_knowledge_drawn_out","source_type":"hft","support_ids":["sup_73ecebd7bd63926a55c1"],"title":"o_knowledge_drawn_out","trust":"legacy_unbound"},{"anchor_refs":["102:1","102:5","102:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"102:5","branch_refs":["root_000661/B001","root_001040/B004","root_001382/B004"],"candidate_id":"cand_d54671499bc005d63445","commentary_obligation":"review","hft_ref":"hft_d5fad5d28301ebbec06a","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:o_oral_mark","source_type":"hft","support_ids":["sup_bee3fdfaea853392e2c5"],"title":"o_oral_mark","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_c2a52b64a7429a77af75","connection_ref":"conn_2d4d7f6d943903cdc13a","note":"Immediate predecessor: future knowing frames the demanded certainty; positive f01 route.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_03b5d200e1bf092a1840","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"102:3","source_note":"Defines a prior certainty that would break distraction before later direct witnessing.","source_row_role":"ranked_review","source_target_component_ref":"102:5","source_target_components":["102:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"102:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"102:3","source_target_components":["102:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"102:3","target_evidence":{"arabic_uthmani":"كَلَّا سَوْفَ تَعْلَمُونَ","ayah_ref":"102:3"},"target_ref":"102:3"},{"connection_evidence_ref":"conn_ev_9facbf69db1504a21f88","connection_ref":"conn_f537d2d37b58f0347c6e","note":"Repetition adds a later stage of disclosure, but largely repeats 102:3; positive f01 route.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_6ce89b7771fba80d990a","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"102:4","source_note":"Continues from warning to settled certainty before later witnessing.","source_row_role":"ranked_review","source_target_component_ref":"102:5","source_target_components":["102:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"102:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"102:4","source_target_components":["102:4"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"102:4","target_evidence":{"arabic_uthmani":"ثُمَّ كَلَّا سَوْفَ تَعْلَمُونَ","ayah_ref":"102:4"},"target_ref":"102:4"},{"connection_evidence_ref":"conn_ev_b827efd57f760276c2b8","connection_ref":"conn_9f00e94d202de798cc3f","note":"Immediate sequel distinguishes direct witnessing from 102:5's knowledge; positive f01/f02 routes.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_56ebb4998dc18f3be195","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"102:7","source_note":"Sets the preceding knowledge-certainty stage that 102:7 intensifies into direct witnessing.","source_row_role":"ranked_review","source_target_component_ref":"102:5","source_target_components":["102:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"102:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"102:7","source_target_components":["102:7"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"102:7","target_evidence":{"arabic_uthmani":"ثُمَّ لَتَرَوُنَّهَا عَيْنَ ٱلْيَقِينِ","ayah_ref":"102:7"},"target_ref":"102:7"},{"connection_evidence_ref":"conn_ev_96658ebec62f8fc3bfaf","connection_ref":"conn_5f267502ec0315094d21","note":"Sets the distracted conduct that certainty in 102:5 would interrupt.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_ea80f214967852271f41","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"102:1","source_note":"Immediate sequence supplies certain knowledge as the needed corrective.","source_row_role":"ranked_review","source_target_component_ref":"102:5","source_target_components":["102:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"102:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"102:1","source_target_components":["102:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"102:1","target_evidence":{"arabic_uthmani":"أَلْهَىٰكُمُ ٱلتَّكَاثُرُ","ayah_ref":"102:1"},"target_ref":"102:1"},{"connection_evidence_ref":"conn_ev_64e4657a094a433cd475","connection_ref":"conn_6b4c8a8109702a1523c3","note":"Completes the immediate distraction-to-graves setting that 102:5 interrupts.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_8dca6d772d2a895bbf87","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"102:2","source_note":"Same-surah knowledge sequence turns the endpoint into later realization.","source_row_role":"ranked_review","source_target_component_ref":"102:5","source_target_components":["102:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"102:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"102:2","source_target_components":["102:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"102:2","target_evidence":{"arabic_uthmani":"حَتَّىٰ زُرْتُمُ ٱلْمَقَابِرَ","ayah_ref":"102:2"},"target_ref":"102:2"},{"connection_evidence_ref":"conn_ev_27c1a53bdfd7d28ba75d","connection_ref":"conn_ba033029501f9c27d02f","note":"Immediate consequence after 102:5; supplies the ensuing vision stage.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_ab00d4cf4a367a3de84f","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"102:6","source_note":"Immediate prior certainty contrast explains why the announced sight matters.","source_row_role":"ranked_review","source_target_component_ref":"102:5","source_target_components":["102:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"102:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"102:6","source_target_components":["102:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"102:6","target_evidence":{"arabic_uthmani":"لَتَرَوُنَّ ٱلْجَحِيمَ","ayah_ref":"102:6"},"target_ref":"102:6"},{"connection_evidence_ref":"conn_ev_b4fcc8e7f065b422c1d2","connection_ref":"conn_5900079dec3ac27dcb50","note":"Immediate sequel turns the sequence toward questioning and accountability.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_f33c40ec2d52128173e6","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"102:8","source_note":"The immediate call for certain knowledge sets up the later vision and questioning.","source_row_role":"ranked_review","source_target_component_ref":"102:5","source_target_components":["102:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"102:5"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"102:8","source_target_components":["102:8"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"102:8","target_evidence":{"arabic_uthmani":"ثُمَّ لَتُسْـَٔلُنَّ يَوْمَئِذٍ عَنِ ٱلنَّعِيمِ","ayah_ref":"102:8"},"target_ref":"102:8"}],"focus":{"arabic_uthmani":"كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ","qac_morphemes":[{"lemma_ar":"كَلَّا","morph_features":"STEM|POS:AVR|LEM:kal~aA","morpheme_role":"STEM","pos":"AVR","qac_ref":"102:5:1:1","qac_word_ref":"102:5:1","root_ar":"","surface_ar":"كَلَّا"},{"lemma_ar":"لَو","morph_features":"STEM|POS:COND|LEM:law","morpheme_role":"STEM","pos":"COND","qac_ref":"102:5:2:1","qac_word_ref":"102:5:2","root_ar":"","surface_ar":"لَوْ"},{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:5:3:1","qac_word_ref":"102:5:3","root_ar":"ع ل م","surface_ar":"تَعْلَمُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"102:5:3:2","qac_word_ref":"102:5:3","root_ar":"","surface_ar":"ونَ"},{"lemma_ar":"عِلْم","morph_features":"STEM|POS:N|LEM:Eilom|ROOT:Elm|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:4:1","qac_word_ref":"102:5:4","root_ar":"ع ل م","surface_ar":"عِلْمَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"102:5:5:1","qac_word_ref":"102:5:5","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"يَقِين","morph_features":"STEM|POS:N|LEM:yaqiyn|ROOT:yqn|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:5:2","qac_word_ref":"102:5:5","root_ar":"ي ق ن","surface_ar":"يَقِينِ"}],"word_analysis_qac_refs":[["102:5:1:1"],["102:5:2:1"],["102:5:3:1","102:5:3:2"],["102:5:4:1"],["102:5:5:1","102:5:5:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["102:5:1","102:5:2","102:5:3","102:5:4","102:5:5"]},"focus_surface_evidence":{"arabic_uthmani":"كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ","qac_morphemes":[{"lemma_ar":"كَلَّا","morph_features":"STEM|POS:AVR|LEM:kal~aA","morpheme_role":"STEM","pos":"AVR","qac_ref":"102:5:1:1","qac_word_ref":"102:5:1","root_ar":"","surface_ar":"كَلَّا"},{"lemma_ar":"لَو","morph_features":"STEM|POS:COND|LEM:law","morpheme_role":"STEM","pos":"COND","qac_ref":"102:5:2:1","qac_word_ref":"102:5:2","root_ar":"","surface_ar":"لَوْ"},{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:5:3:1","qac_word_ref":"102:5:3","root_ar":"ع ل م","surface_ar":"تَعْلَمُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"102:5:3:2","qac_word_ref":"102:5:3","root_ar":"","surface_ar":"ونَ"},{"lemma_ar":"عِلْم","morph_features":"STEM|POS:N|LEM:Eilom|ROOT:Elm|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:4:1","qac_word_ref":"102:5:4","root_ar":"ع ل م","surface_ar":"عِلْمَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"102:5:5:1","qac_word_ref":"102:5:5","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"يَقِين","morph_features":"STEM|POS:N|LEM:yaqiyn|ROOT:yqn|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:5:2","qac_word_ref":"102:5:5","root_ar":"ي ق ن","surface_ar":"يَقِينِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["102:5:1:1"],["102:5:2:1"],["102:5:3:1","102:5:3:2"],["102:5:4:1"],["102:5:5:1","102:5:5:2"]],"word_analysis_refs":["102:5:1","102:5:2","102:5:3","102:5:4","102:5:5"],"word_rows":[{"analysis_record_ref":"102:5:1","analytic_gloss_range_en":"deterrent and corrective discourse particle that halts the preceding heedless movement and opens a new conditional frame","analytic_root_gloss_range_en":null,"qac_refs":["102:5:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"كَلَّا","transliteration":"kallā"}},{"analysis_record_ref":"102:5:2","analytic_gloss_range_en":"counterfactual conditional particle with optative pressure and an omitted answer","analytic_root_gloss_range_en":null,"qac_refs":["102:5:2:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَوْ","transliteration":"law"}},{"analysis_record_ref":"102:5:3","analytic_gloss_range_en":"second-person plural imperfect knowing, remodalized by the counterfactual particle and specified by a cognate accusative","analytic_root_gloss_range_en":"knowledge, recognition, and marking/sign branches; local sense is knowing or recognizing, with sign/mark imagery only as a narrowed root-family pressure","qac_refs":["102:5:3:1","102:5:3:2"],"root":{"arabic":"ع ل م","transliteration":"ʿ-l-m"},"surface":{"arabic":"تَعْلَمُونَ","transliteration":"taʿlamūna"}},{"analysis_record_ref":"102:5:4","analytic_gloss_range_en":"accusative maṣdar functioning as cognate measure of knowing and construct head qualified by certainty","analytic_root_gloss_range_en":"knowledge, recognition, and sign/mark branches; the local noun selects knowledge while mark imagery may color recognition only secondarily","qac_refs":["102:5:4:1"],"root":{"arabic":"ع ل م","transliteration":"ʿ-l-m"},"surface":{"arabic":"عِلْمَ","transliteration":"ʿilma"}},{"analysis_record_ref":"102:5:5","analytic_gloss_range_en":"definite genitive certainty that qualifies the knowledge phrase and closes the ayah","analytic_root_gloss_range_en":"settled knowledge with doubt removed; death resonance is possible as a narrowed lexical pressure in this surah because of 102:2, while unrelated nominal branches are inactive","qac_refs":["102:5:5:1","102:5:5:2"],"root":{"arabic":"ي ق ن","transliteration":"y-q-n"},"surface":{"arabic":"ٱلْيَقِينِ","transliteration":"al-yaqīn"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":8,"missing_anchor_refs":[],"supplied_unique_anchor_count":8},"assigned_record_count":10,"assigned_records":[{"anchor_refs":["102:1","102:5"],"branch_refs":["root_001040/B002","root_001286/B002","root_001382/B001","root_001696/B001"],"candidate_id":"cand_644712471f5a1351c960","evidence_scope":"declared_pericope","hft_ref":"hft_695109b1043bd917f150","item_id":"d_metric_reorientation","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_metric_reorientation","support_id":"sup_48ee5148dabc78836f11"},{"anchor_refs":["102:2","102:5"],"branch_refs":["root_000654/B003","root_001040/B002","root_001195/B002","root_001696/B001"],"candidate_id":"cand_a03f25769e9b19783711","evidence_scope":"declared_pericope","hft_ref":"hft_065e4c29929a255ede1b","item_id":"d_hidden_waypoint","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_hidden_waypoint","support_id":"sup_657d451ca01613003c1c"},{"anchor_refs":["102:3","102:4","102:5"],"branch_refs":["root_001040/B001","root_001696/B001"],"candidate_id":"cand_5465175ae6b3ef5134aa","evidence_scope":"declared_pericope","hft_ref":"hft_35a3c57ee866ee7fe05d","item_id":"d_temporal_fork","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_temporal_fork","support_id":"sup_0e29f72908ca23bcdc4b"},{"anchor_refs":["102:5","102:6","102:7"],"branch_refs":["root_000225/B001","root_000531/B001","root_000531/B012","root_001040/B001","root_001696/B001"],"candidate_id":"cand_76e49d74dab883ea4e4a","evidence_scope":"declared_pericope","hft_ref":"hft_360b71ce9ea7700cca2c","item_id":"d_previsual_disclosure","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_previsual_disclosure","support_id":"sup_1b840a54752a0d94954e"},{"anchor_refs":["102:5","102:7"],"branch_refs":["root_001040/B002","root_001069/B013","root_001696/B001"],"candidate_id":"cand_432fff901f7137496e5e","evidence_scope":"declared_pericope","hft_ref":"hft_79e47dbbcc4e626f9b5c","item_id":"d_sign_to_presence","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_sign_to_presence","support_id":"sup_07989b0d9a51f41140cb"},{"anchor_refs":["102:1","102:5","102:6","102:7"],"branch_refs":["root_000615/B001","root_001040/B005","root_001069/B006","root_001286/B007","root_001696/B001"],"candidate_id":"cand_9059e73d4ea0033382d3","evidence_scope":"declared_pericope","hft_ref":"hft_18b0248709c9857af23e","item_id":"d_hydraulic_circuit","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_hydraulic_circuit","support_id":"sup_05cea3dcf4b9c1d1c652"},{"anchor_refs":["102:5","102:8"],"branch_refs":["root_000661/B001","root_001040/B001","root_001525/B001","root_001696/B001"],"candidate_id":"cand_c7e1299e0390be2b582e","evidence_scope":"declared_pericope","hft_ref":"hft_edf0a518a919d035d048","item_id":"d_answerable_certainty","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_answerable_certainty","support_id":"sup_7c7013bbc61d5a57f8f2"},{"anchor_refs":["102:5","102:7"],"branch_refs":["root_001069/B013","root_001696/B002"],"candidate_id":"cand_94af7dcb4e5eccdfb374","evidence_scope":"declared_pericope","hft_ref":"hft_fab1e1970046c7e28d4e","item_id":"o_guarded_certainty","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:o_guarded_certainty","support_id":"sup_28725db7daa3c1e60994"},{"anchor_refs":["102:5","102:8"],"branch_refs":["root_000661/B001","root_000736/B001","root_001040/B001"],"candidate_id":"cand_e2e57017aed461a0d11a","evidence_scope":"declared_pericope","hft_ref":"hft_ae5745051ed988b87e2b","item_id":"o_knowledge_drawn_out","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:o_knowledge_drawn_out","support_id":"sup_73ecebd7bd63926a55c1"},{"anchor_refs":["102:1","102:5","102:8"],"branch_refs":["root_000661/B001","root_001040/B004","root_001382/B004"],"candidate_id":"cand_d54671499bc005d63445","evidence_scope":"declared_pericope","hft_ref":"hft_d5fad5d28301ebbec06a","item_id":"o_oral_mark","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:o_oral_mark","support_id":"sup_bee3fdfaea853392e2c5"}],"diagnostics":[],"lane_counts":{"global":9,"macro":10,"micro":3},"packet_summary":{"ayah_count":8,"focus_ref":"102:5","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"س ء ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000661","furuq_root_norm":"س ء ل","furuq_source_root_norm":"س أ ل","is_dominant":true,"target_occurrences":118,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000736","furuq_root_norm":"س ل ل","furuq_source_root_norm":"س ل ل","is_dominant":false,"target_occurrences":2,"target_rank":2}]}],"window":["102:1","102:2","102:3","102:4","102:5","102:6","102:7","102:8"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"102:5","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":13,"unstructured_record_count":0},"identity":{"ayah_ref":"102:5","lane":"macro","linguistic_source_ref":"102:5","surface_ref":"102:5","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"102:5","target_tokens":[["Hayır",["102:5:1"]],["Kesin",["102:5:4","102:5:5"]],["olarak",["102:5:4","102:5:5"]],["bilseydiniz",["102:5:2","102:5:3"]]],"text":"Hayır! Kesin olarak bilseydiniz."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":10,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":1,"ayah_to":8,"id":"s102-p01-001-008","label":"Whole surah","number":1,"refs":["102:1","102:2","102:3","102:4","102:5","102:6","102:7","102:8"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"102:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"102:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["102:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"102:0"},{"ayah_ref":"102:1","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"102:1","root_occurrences":[{"lemmas_ar":["أَلْهَىٰ"],"occurrence_count":1,"pos_tags":["V"],"root":"ل ه و","surfaces_ar":["أَلْهَىٰ"],"word_indices":["1"]},{"lemmas_ar":["تَّكَاثُر"],"occurrence_count":1,"pos_tags":["N"],"root":"ك ث ر","surfaces_ar":["تَّكَاثُرُ"],"word_indices":["2"]}],"root_sequence":["ل ه و","ك ث ر"],"text_ar":"أَلْهَىٰكُمُ ٱلتَّكَاثُرُ"}],"context_order":["102:1"],"context_root_cues":[{"root":"ل ه و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"شغل عن الشيء بغيره"},{"branch_id":"B002","branch_image_ar":"لعب واستمتاع يكنى به"},{"branch_id":"B003","branch_image_ar":"طرح الشيء في فم الرحى والعطاء المشبه به"},{"branch_id":"B004","branch_image_ar":"لحمة أقصى الفم المشرفة على الحلق"}],"mapped_root_id":"root_001382","mapped_root_norm":"ل ه و"}]},{"root":"ك ث ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الكثرة ونماء العدد"},{"branch_id":"B002","branch_image_ar":"المكاثرة والغلبة بالعدد"},{"branch_id":"B003","branch_image_ar":"كثرة في صاحب أو كلام أو مطالب"},{"branch_id":"B005","branch_image_ar":"كوثر الغبار وتكوثره"},{"branch_id":"B006","branch_image_ar":"الكثر جمار النخل"},{"branch_id":"B007","branch_image_ar":"الكمثرة اجتماع الشيء"}],"mapped_root_id":"root_001286","mapped_root_norm":"ك ث ر"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"102:1","surface_ref":"102:1"},{"ayah_ref":"102:2","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"102:2","root_occurrences":[{"lemmas_ar":["زُرْ"],"occurrence_count":1,"pos_tags":["V"],"root":"ز و ر","surfaces_ar":["زُرْ"],"word_indices":["2"]},{"lemmas_ar":["مَقَابِر"],"occurrence_count":1,"pos_tags":["N"],"root":"ق ب ر","surfaces_ar":["مَقَابِرَ"],"word_indices":["3"]}],"root_sequence":["ز و ر","ق ب ر"],"text_ar":"حَتَّىٰ زُرْتُمُ ٱلْمَقَابِرَ"}],"context_order":["102:2"],"context_root_cues":[{"root":"ز و ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الميل والعدول"},{"branch_id":"B002","branch_image_ar":"الزور كذب وباطل"},{"branch_id":"B003","branch_image_ar":"زيارة وقصد الزائر"},{"branch_id":"B004","branch_image_ar":"زَوْر الصدر وميله"},{"branch_id":"B005","branch_image_ar":"مرجع وزعامة يمال إليها"},{"branch_id":"B006","branch_image_ar":"تزوير الكلام وتقويمه"},{"branch_id":"B007","branch_image_ar":"سير شديد"}],"mapped_root_id":"root_000654","mapped_root_norm":"ز و ر"}]},{"root":"ق ب ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"مواراة الميت في القبر"},{"branch_id":"B002","branch_image_ar":"غموض الشيء وتطامنه"},{"branch_id":"B003","branch_image_ar":"القُبَّرة الطائر"},{"branch_id":"B004","branch_image_ar":"طرف الأنف في الغضب"}],"mapped_root_id":"root_001195","mapped_root_norm":"ق ب ر"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"102:2","surface_ref":"102:2"},{"ayah_ref":"102:3","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"102:3","root_occurrences":[{"lemmas_ar":["عَلِمَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ع ل م","surfaces_ar":["تَعْلَمُ"],"word_indices":["3"]}],"root_sequence":["ع ل م"],"text_ar":"كَلَّا سَوْفَ تَعْلَمُونَ"}],"context_order":["102:3"],"context_root_cues":[],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"102:3","surface_ref":"102:3"},{"ayah_ref":"102:4","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"102:4","root_occurrences":[{"lemmas_ar":["عَلِمَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ع ل م","surfaces_ar":["تَعْلَمُ"],"word_indices":["4"]}],"root_sequence":["ع ل م"],"text_ar":"ثُمَّ كَلَّا سَوْفَ تَعْلَمُونَ"}],"context_order":["102:4"],"context_root_cues":[],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"102:4","surface_ref":"102:4"},{"ayah_ref":"102:6","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"102:6","root_occurrences":[{"lemmas_ar":["رَءَا"],"occurrence_count":1,"pos_tags":["V"],"root":"ر ء ي","surfaces_ar":["تَرَوُ"],"word_indices":["1"]},{"lemmas_ar":["جَحِيم"],"occurrence_count":1,"pos_tags":["N"],"root":"ج ح م","surfaces_ar":["جَحِيمَ"],"word_indices":["2"]}],"root_sequence":["ر ء ي","ج ح م"],"text_ar":"لَتَرَوُنَّ ٱلْجَحِيمَ"}],"context_order":["102:6"],"context_root_cues":[{"root":"ر ء ي","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"رؤية العين والبصيرة"},{"branch_id":"B002","branch_image_ar":"رأي القلب والتفكر"},{"branch_id":"B003","branch_image_ar":"الرؤيا في المنام"},{"branch_id":"B004","branch_image_ar":"تراء وتواجه"},{"branch_id":"B005","branch_image_ar":"رياء الناس"},{"branch_id":"B006","branch_image_ar":"مرأى ومنظر ومرآة"},{"branch_id":"B007","branch_image_ar":"ترية الحيض"},{"branch_id":"B008","branch_image_ar":"رئي من الجن"},{"branch_id":"B009","branch_image_ar":"الرئة وما يصيبها"},{"branch_id":"B010","branch_image_ar":"ظهور حمل الناقة أو الشاة"},{"branch_id":"B011","branch_image_ar":"راية منصوبة"},{"branch_id":"B012","branch_image_ar":"إراءة وإظهار"},{"branch_id":"B013","branch_image_ar":"أرأيتك للتنبيه والاستخبار"}],"mapped_root_id":"root_000531","mapped_root_norm":"ر ء ي"},{"branches":[{"branch_id":"B001","branch_image_ar":"الرِّيّ وخلاف العطش"},{"branch_id":"B002","branch_image_ar":"إيراد الماء وحمله"},{"branch_id":"B003","branch_image_ar":"رواية الخبر والشعر"},{"branch_id":"B004","branch_image_ar":"الرَّوِيَّة في الأمر"},{"branch_id":"B005","branch_image_ar":"الرَّوِيَّة حاجة عند المرء"},{"branch_id":"B006","branch_image_ar":"الرَّوِيَّة بقية الشيء"},{"branch_id":"B007","branch_image_ar":"الرِّوَاء حبل الشد"},{"branch_id":"B008","branch_image_ar":"امتلاء يغلظ ويعتدل"},{"branch_id":"B009","branch_image_ar":"الرُّوَاء منظر وحسن"},{"branch_id":"B010","branch_image_ar":"الرِّيَا طيب الرائحة"},{"branch_id":"B011","branch_image_ar":"الأُرْوِيَّة من الوعول"},{"branch_id":"B012","branch_image_ar":"الرَّايَة العلم"},{"branch_id":"B013","branch_image_ar":"الرَّوِيّ حرف القافية"},{"branch_id":"B014","branch_image_ar":"الرَّوِيّ سحابة عظيمة القطر"},{"branch_id":"B015","branch_image_ar":"الرَّوَايَا سادة يحملون الثقل"}],"mapped_root_id":"root_000615","mapped_root_norm":"ر و ي"}]},{"root":"ج ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"تأجج النار وشدة حرها"},{"branch_id":"B002","branch_image_ar":"احتدام الحرب والموت"},{"branch_id":"B003","branch_image_ar":"العين المتوقدة أو الجاحظة"},{"branch_id":"B004","branch_image_ar":"تلهب الوجه بالغضب"},{"branch_id":"B005","branch_image_ar":"قلة الحياء"}],"mapped_root_id":"root_000225","mapped_root_norm":"ج ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"102:6","surface_ref":"102:6"},{"ayah_ref":"102:7","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"102:7","root_occurrences":[{"lemmas_ar":["رَءَا"],"occurrence_count":1,"pos_tags":["V"],"root":"ر ء ي","surfaces_ar":["تَرَوُ"],"word_indices":["2"]},{"lemmas_ar":["عَيْن"],"occurrence_count":1,"pos_tags":["N"],"root":"ع ي ن","surfaces_ar":["عَيْنَ"],"word_indices":["3"]},{"lemmas_ar":["يَقِين"],"occurrence_count":1,"pos_tags":["N"],"root":"ي ق ن","surfaces_ar":["يَقِينِ"],"word_indices":["4"]}],"root_sequence":["ر ء ي","ع ي ن","ي ق ن"],"text_ar":"ثُمَّ لَتَرَوُنَّهَا عَيْنَ ٱلْيَقِينِ"}],"context_order":["102:7"],"context_root_cues":[{"root":"ر ء ي","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"رؤية العين والبصيرة"},{"branch_id":"B002","branch_image_ar":"رأي القلب والتفكر"},{"branch_id":"B003","branch_image_ar":"الرؤيا في المنام"},{"branch_id":"B004","branch_image_ar":"تراء وتواجه"},{"branch_id":"B005","branch_image_ar":"رياء الناس"},{"branch_id":"B006","branch_image_ar":"مرأى ومنظر ومرآة"},{"branch_id":"B007","branch_image_ar":"ترية الحيض"},{"branch_id":"B008","branch_image_ar":"رئي من الجن"},{"branch_id":"B009","branch_image_ar":"الرئة وما يصيبها"},{"branch_id":"B010","branch_image_ar":"ظهور حمل الناقة أو الشاة"},{"branch_id":"B011","branch_image_ar":"راية منصوبة"},{"branch_id":"B012","branch_image_ar":"إراءة وإظهار"},{"branch_id":"B013","branch_image_ar":"أرأيتك للتنبيه والاستخبار"}],"mapped_root_id":"root_000531","mapped_root_norm":"ر ء ي"},{"branches":[{"branch_id":"B001","branch_image_ar":"الرِّيّ وخلاف العطش"},{"branch_id":"B002","branch_image_ar":"إيراد الماء وحمله"},{"branch_id":"B003","branch_image_ar":"رواية الخبر والشعر"},{"branch_id":"B004","branch_image_ar":"الرَّوِيَّة في الأمر"},{"branch_id":"B005","branch_image_ar":"الرَّوِيَّة حاجة عند المرء"},{"branch_id":"B006","branch_image_ar":"الرَّوِيَّة بقية الشيء"},{"branch_id":"B007","branch_image_ar":"الرِّوَاء حبل الشد"},{"branch_id":"B008","branch_image_ar":"امتلاء يغلظ ويعتدل"},{"branch_id":"B009","branch_image_ar":"الرُّوَاء منظر وحسن"},{"branch_id":"B010","branch_image_ar":"الرِّيَا طيب الرائحة"},{"branch_id":"B011","branch_image_ar":"الأُرْوِيَّة من الوعول"},{"branch_id":"B012","branch_image_ar":"الرَّايَة العلم"},{"branch_id":"B013","branch_image_ar":"الرَّوِيّ حرف القافية"},{"branch_id":"B014","branch_image_ar":"الرَّوِيّ سحابة عظيمة القطر"},{"branch_id":"B015","branch_image_ar":"الرَّوَايَا سادة يحملون الثقل"}],"mapped_root_id":"root_000615","mapped_root_norm":"ر و ي"}]},{"root":"ع ي ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العين الناظرة"},{"branch_id":"B002","branch_image_ar":"المشاهدة بالعين"},{"branch_id":"B003","branch_image_ar":"عين الحفظ والرعاية"},{"branch_id":"B004","branch_image_ar":"الإصابة بالعين"},{"branch_id":"B005","branch_image_ar":"العين الجاسوسة"},{"branch_id":"B006","branch_image_ar":"منبع الماء الجاري"},{"branch_id":"B007","branch_image_ar":"عين الجلد والسقاء"},{"branch_id":"B008","branch_image_ar":"عين الشمس"},{"branch_id":"B009","branch_image_ar":"النقرة أو الموضع العيني"},{"branch_id":"B010","branch_image_ar":"عين السحاب والمطر"},{"branch_id":"B011","branch_image_ar":"النقد الحاضر"},{"branch_id":"B012","branch_image_ar":"العينة والسلف"},{"branch_id":"B013","branch_image_ar":"عين الشيء نفسه"},{"branch_id":"B014","branch_image_ar":"العين خيار الشيء"},{"branch_id":"B015","branch_image_ar":"أعيان القوم والإخوة"},{"branch_id":"B016","branch_image_ar":"سعة العين وحسنها"},{"branch_id":"B017","branch_image_ar":"العين بمعنى الناس الحاضرون"}],"mapped_root_id":"root_001069","mapped_root_norm":"ع ي ن"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"102:7","surface_ref":"102:7"},{"ayah_ref":"102:8","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"102:8","root_occurrences":[{"lemmas_ar":["سَأَلَ"],"occurrence_count":1,"pos_tags":["V"],"root":"س ء ل","surfaces_ar":["تُسْـَٔلُ"],"word_indices":["2"]},{"lemmas_ar":["نَعِيم"],"occurrence_count":1,"pos_tags":["N"],"root":"ن ع م","surfaces_ar":["نَّعِيمِ"],"word_indices":["5"]}],"root_sequence":["س ء ل","ن ع م"],"text_ar":"ثُمَّ لَتُسْـَٔلُنَّ يَوْمَئِذٍ عَنِ ٱلنَّعِيمِ"}],"context_order":["102:8"],"context_root_cues":[{"root":"س ء ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"السؤال والطلب"},{"branch_id":"B002","branch_image_ar":"السُّؤل المطلوب"},{"branch_id":"B003","branch_image_ar":"قضاء المسألة"},{"branch_id":"B004","branch_image_ar":"السؤال المتبادل"}],"mapped_root_id":"root_000661","mapped_root_norm":"س ء ل"},{"branches":[{"branch_id":"B001","branch_image_ar":"السل برفق وخفاء"},{"branch_id":"B002","branch_image_ar":"الإسلال الخفي"},{"branch_id":"B003","branch_image_ar":"السلالة المستلة"},{"branch_id":"B004","branch_image_ar":"الانسلال خروجا"},{"branch_id":"B005","branch_image_ar":"السلسلة اتصالا"},{"branch_id":"B006","branch_image_ar":"السلاسة في الجريان"},{"branch_id":"B007","branch_image_ar":"المسال في الوادي"},{"branch_id":"B008","branch_image_ar":"السُّل هزالا"},{"branch_id":"B009","branch_image_ar":"سلة الفرس دفعة"},{"branch_id":"B010","branch_image_ar":"المسلة السالة"},{"branch_id":"B011","branch_image_ar":"السلة وعاء"},{"branch_id":"B012","branch_image_ar":"طرائق مستلة"},{"branch_id":"B013","branch_image_ar":"الرقة والتخطط من البلى"},{"branch_id":"B014","branch_image_ar":"سقوط الأسنان"},{"branch_id":"B015","branch_image_ar":"الفرجة بين النصائب"}],"mapped_root_id":"root_000736","mapped_root_norm":"س ل ل"}]},{"root":"ن ع م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"حسن الحال والنعمة"},{"branch_id":"B002","branch_image_ar":"اللين والنعومة ورفاه العيش"},{"branch_id":"B003","branch_image_ar":"مدح الشيء بنعم"},{"branch_id":"B004","branch_image_ar":"الجواب بنعم والتصديق"},{"branch_id":"B005","branch_image_ar":"مال الأنعام والإبل"},{"branch_id":"B006","branch_image_ar":"النعام والنعامة الطائر"},{"branch_id":"B007","branch_image_ar":"ما سمي نعامة تشبيها بالهيئة"},{"branch_id":"B008","branch_image_ar":"طيران النعامة وتفرق القوم"},{"branch_id":"B009","branch_image_ar":"النعامى ريح لينة"},{"branch_id":"B010","branch_image_ar":"زاد وأنعم في الفعل"},{"branch_id":"B011","branch_image_ar":"موافقة المكان وطيب المقام"},{"branch_id":"B012","branch_image_ar":"المشي على القدم وابتذالها"},{"branch_id":"B013","branch_image_ar":"نعم الله بك عينا وقرة العين"}],"mapped_root_id":"root_001525","mapped_root_norm":"ن ع م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"102:8","surface_ref":"102:8"},{"ayah_ref":"1:2","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:2","root_occurrences":[{"lemmas_ar":["حَمْد"],"occurrence_count":1,"pos_tags":["N"],"root":"ح م د","surfaces_ar":["حَمْدُ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["لَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَبّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ر ب ب","surfaces_ar":["رَبِّ"],"word_indices":["3"]},{"lemmas_ar":["عَٰلَمِين"],"occurrence_count":1,"pos_tags":["N"],"root":"ع ل م","surfaces_ar":["عَٰلَمِينَ"],"word_indices":["4"]}],"root_sequence":["ح م د","ء ل ه","ر ب ب","ع ل م"],"text_ar":"ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ"}],"context_order":["1:2"],"context_root_cues":[{"root":"ح م د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الحمد خلاف الذم"},{"branch_id":"B002","branch_image_ar":"وجود الشيء محمودا"},{"branch_id":"B003","branch_image_ar":"المحمود كثير الخصال"},{"branch_id":"B004","branch_image_ar":"حماداك الغاية المحمودة"},{"branch_id":"B005","branch_image_ar":"يتحمد بالمنة"}],"mapped_root_id":"root_000355","mapped_root_norm":"ح م د"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ب ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ربوبية وملك وسيادة"},{"branch_id":"B002","branch_image_ar":"إصلاح وتربية وإتمام"},{"branch_id":"B003","branch_image_ar":"علم رباني"},{"branch_id":"B004","branch_image_ar":"ربة وجماعات كثيرة"},{"branch_id":"B005","branch_image_ar":"ربيب وربيبة ورابة"},{"branch_id":"B006","branch_image_ar":"رُبّ خاثر وإصلاح به"},{"branch_id":"B007","branch_image_ar":"لزوم وإقامة ودوام"},{"branch_id":"B008","branch_image_ar":"رباب السحاب"},{"branch_id":"B009","branch_image_ar":"شاة رُبّى وحداثة"},{"branch_id":"B010","branch_image_ar":"ربابة تجمع القداح"},{"branch_id":"B011","branch_image_ar":"ربابة عهد وميثاق"},{"branch_id":"B012","branch_image_ar":"ربة نبات"},{"branch_id":"B013","branch_image_ar":"ماء رَبَب كثير"},{"branch_id":"B014","branch_image_ar":"رَبْرَب قطيع"},{"branch_id":"B015","branch_image_ar":"حرف رب وربما"},{"branch_id":"B016","branch_image_ar":"رُبَى حاجة وعقدة ونعمة"},{"branch_id":"B017","branch_image_ar":"رباني الملاحين"}],"mapped_root_id":"root_000532","mapped_root_norm":"ر ب ب"},{"branches":[{"branch_id":"B001","branch_image_ar":"زيادة وعلو"},{"branch_id":"B002","branch_image_ar":"أرض مرتفعة"},{"branch_id":"B003","branch_image_ar":"زيادة الربا في المعاملة"},{"branch_id":"B004","branch_image_ar":"تصعد النفس وانتفاخه"},{"branch_id":"B005","branch_image_ar":"تغذية ونشوء"},{"branch_id":"B006","branch_image_ar":"نتوء أصل الفخذ"},{"branch_id":"B007","branch_image_ar":"أهل البيت من بني الأعمام"}],"mapped_root_id":"root_000537","mapped_root_norm":"ر ب و"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:2","membership_added_ayah":true,"membership_target_surah":102,"surface_ref":"1:2"},{"ayah_ref":"1:3","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:3","root_occurrences":[{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["1","2"]}],"root_sequence":["ر ح م","ر ح م"],"text_ar":"ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"}],"context_order":["1:3"],"context_root_cues":[{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:3","membership_added_ayah":true,"membership_target_surah":102,"surface_ref":"1:3"},{"ayah_ref":"1:4","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:4","root_occurrences":[{"lemmas_ar":["مَٰلِك"],"occurrence_count":1,"pos_tags":["N"],"root":"م ل ك","surfaces_ar":["مَٰلِكِ"],"word_indices":["1"]},{"lemmas_ar":["يَوْم"],"occurrence_count":1,"pos_tags":["N"],"root":"ي و م","surfaces_ar":["يَوْمِ"],"word_indices":["2"]},{"lemmas_ar":["دِين"],"occurrence_count":1,"pos_tags":["N"],"root":"د ي ن","surfaces_ar":["دِّينِ"],"word_indices":["3"]}],"root_sequence":["م ل ك","ي و م","د ي ن"],"text_ar":"مَٰلِكِ يَوْمِ ٱلدِّينِ"}],"context_order":["1:4"],"context_root_cues":[{"root":"م ل ك","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"قوة الشيء وتماسكه"},{"branch_id":"B002","branch_image_ar":"المِلْك والتصرف"},{"branch_id":"B003","branch_image_ar":"المُلك والسلطان"},{"branch_id":"B004","branch_image_ar":"الإملاك والتزويج"},{"branch_id":"B005","branch_image_ar":"مِلاك الأمر وعِماده"},{"branch_id":"B006","branch_image_ar":"مَلَك الطريق والوادي"},{"branch_id":"B007","branch_image_ar":"الماء مَلَك الأمر"},{"branch_id":"B008","branch_image_ar":"المتقدم القائد في الحيوان"}],"mapped_root_id":"root_001444","mapped_root_norm":"م ل ك"}]},{"root":"ي و م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"وقت النهار المحدود"},{"branch_id":"B002","branch_image_ar":"مدة من الزمان"},{"branch_id":"B003","branch_image_ar":"كائنة اليوم وشدته"}],"mapped_root_id":"root_001700","mapped_root_norm":"ي و م"}]},{"root":"د ي ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الطاعة والانقياد"},{"branch_id":"B002","branch_image_ar":"الحساب والجزاء"},{"branch_id":"B003","branch_image_ar":"الدين المالي"},{"branch_id":"B004","branch_image_ar":"الإذلال والملك"},{"branch_id":"B005","branch_image_ar":"العادة والشأن"},{"branch_id":"B006","branch_image_ar":"مدينة الطاعة"},{"branch_id":"B007","branch_image_ar":"التصديق والتفويض"}],"mapped_root_id":"root_000504","mapped_root_norm":"د ي ن"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:4","membership_added_ayah":true,"membership_target_surah":102,"surface_ref":"1:4"},{"ayah_ref":"1:5","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:5","root_occurrences":[{"lemmas_ar":["عَبَدَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ع ب د","surfaces_ar":["نَعْبُدُ"],"word_indices":["2"]},{"lemmas_ar":["ٱسْتَعِينُ"],"occurrence_count":1,"pos_tags":["V"],"root":"ع و ن","surfaces_ar":["نَسْتَعِينُ"],"word_indices":["4"]}],"root_sequence":["ع ب د","ع و ن"],"text_ar":"إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ"}],"context_order":["1:5"],"context_root_cues":[{"root":"ع ب د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرق والملك"},{"branch_id":"B003","branch_image_ar":"العبادة والطاعة الخاضعة"},{"branch_id":"B004","branch_image_ar":"التعبيد والاستعباد"},{"branch_id":"B005","branch_image_ar":"التذليل والتسوية"},{"branch_id":"B006","branch_image_ar":"التكريم والتعظيم"},{"branch_id":"B007","branch_image_ar":"القوة والصلابة"},{"branch_id":"B008","branch_image_ar":"الأنفة والغضب"},{"branch_id":"B009","branch_image_ar":"قلة اللبث وسرعة العدو"},{"branch_id":"B010","branch_image_ar":"التفرق في الوجوه"},{"branch_id":"B011","branch_image_ar":"العطب والانقطاع"},{"branch_id":"B012","branch_image_ar":"صَلاءة الطيب"}],"mapped_root_id":"root_000973","mapped_root_norm":"ع ب د"}]},{"root":"ع و ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الإعانة والمظاهرة"},{"branch_id":"B002","branch_image_ar":"العَوان بين السنين"},{"branch_id":"B003","branch_image_ar":"الحرب العَوان"},{"branch_id":"B004","branch_image_ar":"النخلة العَوانة القديمة"},{"branch_id":"B005","branch_image_ar":"استواء الخلقة وتلاحق القوة"},{"branch_id":"B006","branch_image_ar":"العانة قطيع الحمر"},{"branch_id":"B007","branch_image_ar":"عانة الرجل"},{"branch_id":"B008","branch_image_ar":"النسبة إلى عانة"}],"mapped_root_id":"root_001064","mapped_root_norm":"ع و ن"},{"branches":[{"branch_id":"B001","branch_image_ar":"العين الناظرة"},{"branch_id":"B002","branch_image_ar":"المشاهدة بالعين"},{"branch_id":"B003","branch_image_ar":"عين الحفظ والرعاية"},{"branch_id":"B004","branch_image_ar":"الإصابة بالعين"},{"branch_id":"B005","branch_image_ar":"العين الجاسوسة"},{"branch_id":"B006","branch_image_ar":"منبع الماء الجاري"},{"branch_id":"B007","branch_image_ar":"عين الجلد والسقاء"},{"branch_id":"B008","branch_image_ar":"عين الشمس"},{"branch_id":"B009","branch_image_ar":"النقرة أو الموضع العيني"},{"branch_id":"B010","branch_image_ar":"عين السحاب والمطر"},{"branch_id":"B011","branch_image_ar":"النقد الحاضر"},{"branch_id":"B012","branch_image_ar":"العينة والسلف"},{"branch_id":"B013","branch_image_ar":"عين الشيء نفسه"},{"branch_id":"B014","branch_image_ar":"العين خيار الشيء"},{"branch_id":"B015","branch_image_ar":"أعيان القوم والإخوة"},{"branch_id":"B016","branch_image_ar":"سعة العين وحسنها"},{"branch_id":"B017","branch_image_ar":"العين بمعنى الناس الحاضرون"}],"mapped_root_id":"root_001069","mapped_root_norm":"ع ي ن"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:5","membership_added_ayah":true,"membership_target_surah":102,"surface_ref":"1:5"},{"ayah_ref":"1:6","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:6","root_occurrences":[{"lemmas_ar":["هَدَى"],"occurrence_count":1,"pos_tags":["V"],"root":"ه د ي","surfaces_ar":["ٱهْدِ"],"word_indices":["1"]},{"lemmas_ar":["صِرَٰط"],"occurrence_count":1,"pos_tags":["N"],"root":"ص ر ط","surfaces_ar":["صِّرَٰطَ"],"word_indices":["2"]},{"lemmas_ar":["مُّسْتَقِيم"],"occurrence_count":1,"pos_tags":["ADJ"],"root":"ق و م","surfaces_ar":["مُسْتَقِيمَ"],"word_indices":["3"]}],"root_sequence":["ه د ي","ص ر ط","ق و م"],"text_ar":"ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ"}],"context_order":["1:6"],"context_root_cues":[{"root":"ه د ي","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"دلالة بلطف إلى الطريق والحق"},{"branch_id":"B002","branch_image_ar":"جهة الأمر وسيرته وقصده"},{"branch_id":"B003","branch_image_ar":"المتقدم الهادي وأوائل الشيء"},{"branch_id":"B004","branch_image_ar":"بعثة لطف وهدية إلى ذي مودة"},{"branch_id":"B005","branch_image_ar":"الهدي المهدى إلى الحرم"},{"branch_id":"B006","branch_image_ar":"العروس المهدية إلى زوجها"},{"branch_id":"B007","branch_image_ar":"هدي الحرمة والأسير"},{"branch_id":"B008","branch_image_ar":"مشي التهادي مع الاعتماد والتمايل"},{"branch_id":"B009","branch_image_ar":"الهداء البليد الضعيف"},{"branch_id":"B010","branch_image_ar":"هدي السكون وحسن الهيئة"},{"branch_id":"B011","branch_image_ar":"إهداء الشعر ومهاداته"}],"mapped_root_id":"root_001583","mapped_root_norm":"ه د ي"}]},{"root":"ص ر ط","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الطريق المستقيم"},{"branch_id":"B002","branch_image_ar":"الغيبة في المرور والبلع"},{"branch_id":"B003","branch_image_ar":"السيف القاطع الماضي في الضربة"}],"mapped_root_id":"root_000858","mapped_root_norm":"ص ر ط"}]},{"root":"ق و م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"جماعة الناس والرجال"},{"branch_id":"B002","branch_image_ar":"انتصاب وقيام بالبدن"},{"branch_id":"B003","branch_image_ar":"عزم ونهوض إلى الأمر"},{"branch_id":"B004","branch_image_ar":"رعاية وحفظ وولاية"},{"branch_id":"B006","branch_image_ar":"مقام وإقامة في موضع"},{"branch_id":"B007","branch_image_ar":"نيابة وقيام مقام غيره"},{"branch_id":"B008","branch_image_ar":"استقامة واعتدال واستواء"},{"branch_id":"B009","branch_image_ar":"قوام وعماد ومعاش"},{"branch_id":"B010","branch_image_ar":"قيمة وتقويم وتسعير"},{"branch_id":"B011","branch_image_ar":"قامة وقوام الجسم والطول"},{"branch_id":"B012","branch_image_ar":"آلة قائمة وجزء قائم"},{"branch_id":"B013","branch_image_ar":"قيامة وبعث وقيام الساعة"},{"branch_id":"B014","branch_image_ar":"مقاومة ومنازلة"},{"branch_id":"B015","branch_image_ar":"وزن سواء ومقدار معتدل"},{"branch_id":"B016","branch_image_ar":"جمود ووقوف وكلال"},{"branch_id":"B017","branch_image_ar":"انتصاف النهار وقائم الظهيرة"},{"branch_id":"B018","branch_image_ar":"نفاق السوق"},{"branch_id":"B019","branch_image_ar":"وجع قائم بالعضو"},{"branch_id":"B020","branch_image_ar":"قوام في قوائم الشاة"},{"branch_id":"B021","branch_image_ar":"عين قائمة ذاهبة البصر"}],"mapped_root_id":"root_001273","mapped_root_norm":"ق و م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:6","membership_added_ayah":true,"membership_target_surah":102,"surface_ref":"1:6"},{"ayah_ref":"1:7","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:7","root_occurrences":[{"lemmas_ar":["صِرَٰط"],"occurrence_count":1,"pos_tags":["N"],"root":"ص ر ط","surfaces_ar":["صِرَٰطَ"],"word_indices":["1"]},{"lemmas_ar":["أَنْعَمَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ن ع م","surfaces_ar":["أَنْعَمْ"],"word_indices":["3"]},{"lemmas_ar":["غَيْر"],"occurrence_count":1,"pos_tags":["N"],"root":"غ ي ر","surfaces_ar":["غَيْرِ"],"word_indices":["5"]},{"lemmas_ar":["مَغْضُوب"],"occurrence_count":1,"pos_tags":["N"],"root":"غ ض ب","surfaces_ar":["مَغْضُوبِ"],"word_indices":["6"]},{"lemmas_ar":["ضَآلّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ض ل ل","surfaces_ar":["ضَّآلِّينَ"],"word_indices":["9"]}],"root_sequence":["ص ر ط","ن ع م","غ ي ر","غ ض ب","ض ل ل"],"text_ar":"صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ"}],"context_order":["1:7"],"context_root_cues":[{"root":"ص ر ط","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الطريق المستقيم"},{"branch_id":"B002","branch_image_ar":"الغيبة في المرور والبلع"},{"branch_id":"B003","branch_image_ar":"السيف القاطع الماضي في الضربة"}],"mapped_root_id":"root_000858","mapped_root_norm":"ص ر ط"}]},{"root":"ن ع م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"حسن الحال والنعمة"},{"branch_id":"B002","branch_image_ar":"اللين والنعومة ورفاه العيش"},{"branch_id":"B003","branch_image_ar":"مدح الشيء بنعم"},{"branch_id":"B004","branch_image_ar":"الجواب بنعم والتصديق"},{"branch_id":"B005","branch_image_ar":"مال الأنعام والإبل"},{"branch_id":"B006","branch_image_ar":"النعام والنعامة الطائر"},{"branch_id":"B007","branch_image_ar":"ما سمي نعامة تشبيها بالهيئة"},{"branch_id":"B008","branch_image_ar":"طيران النعامة وتفرق القوم"},{"branch_id":"B009","branch_image_ar":"النعامى ريح لينة"},{"branch_id":"B010","branch_image_ar":"زاد وأنعم في الفعل"},{"branch_id":"B011","branch_image_ar":"موافقة المكان وطيب المقام"},{"branch_id":"B012","branch_image_ar":"المشي على القدم وابتذالها"},{"branch_id":"B013","branch_image_ar":"نعم الله بك عينا وقرة العين"}],"mapped_root_id":"root_001525","mapped_root_norm":"ن ع م"}]},{"root":"غ ي ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الصلاح والمنفعة بالميرة والسقي والإصلاح"},{"branch_id":"B002","branch_image_ar":"الغَيْر في الدية"},{"branch_id":"B003","branch_image_ar":"تغيير الصورة أو إبدال الشيء بغيره"},{"branch_id":"B004","branch_image_ar":"الغَيْرة على الأهل"},{"branch_id":"B005","branch_image_ar":"السوى والخلاف والاستثناء والنفي"}],"mapped_root_id":"root_001119","mapped_root_norm":"غ ي ر"}]},{"root":"غ ض ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"اشتداد السخط وثورانه للانتقام"},{"branch_id":"B002","branch_image_ar":"الغضب لشخص حي أو به بعد موته"},{"branch_id":"B003","branch_image_ar":"المراغمة والمخالفة"},{"branch_id":"B004","branch_image_ar":"صلابة الصخرة وتماسكها"},{"branch_id":"B005","branch_image_ar":"غلظ الجسم وشدة الحمرة"},{"branch_id":"B006","branch_image_ar":"تورم العين وما حولها"},{"branch_id":"B007","branch_image_ar":"العبوس والضجر والعظم في وصف الحيوان أو الشخص"},{"branch_id":"B008","branch_image_ar":"جلد صلب أو مطوي كدرقة"}],"mapped_root_id":"root_001092","mapped_root_norm":"غ ض ب"}]},{"root":"ض ل ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الضلال عن الهدى والقصد"},{"branch_id":"B002","branch_image_ar":"الغيبوبة والخفاء"},{"branch_id":"B003","branch_image_ar":"فقدان الشيء"},{"branch_id":"B004","branch_image_ar":"ضياع الحفظ"},{"branch_id":"B005","branch_image_ar":"الضالّة في المضيعة"}],"mapped_root_id":"root_000913","mapped_root_norm":"ض ل ل"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:7","membership_added_ayah":true,"membership_target_surah":102,"surface_ref":"1:7"}],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Protected Seclusion","source_type":"channel","support_id":"sup_17f4205d32ea1b1a955d","text":"A young woman is kept within a protected, screened interior.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Protected Seclusion","source_type":"channel","support_id":"sup_1db1febc0f8f60d3f075","text":"102:5, 102:7 `ٱلْيَقِينِ` (`ي ق ن`)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Protected Seclusion","source_type":"channel","support_id":"sup_21eb2e506919b1775722","text":"Containment becomes a social arrangement: protection is enacted spatially by limiting exposure and access.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Sight Ripening into Certainty","source_type":"channel","support_id":"sup_2fff480e326f32aaa58c","text":"Something unavailable or uncertain becomes apprehensible through sight, inward judgment, disclosure, or certainty.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Sight Ripening into Certainty","source_type":"channel","support_id":"sup_60ee37c4cfc2eec781a5","text":"Perception begins with the act of seeing, deepens into inward insight and direct encounter, and culminates in knowledge from which doubt has been displaced.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Sight Ripening into Certainty","source_type":"channel","support_id":"sup_6b288bb5b51033784696","text":"102:3-5 `تَعْلَمُونَ` and `عِلْمَ` (`ع ل م`); 102:5, 102:7 `ٱلْيَقِينِ` (`ي ق ن`); 102:6-7 `لَتَرَوُنَّ` and `لَتَرَوُنَّهَا` (`ر ء ي`); 102:7 `عَيْنَ` (`ع ي ن`)","trust":"trusted"},{"branch_refs":["root_001696/B002"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"B:Protected Seclusion","source_type":"channel","support_id":"sup_799d2d44713056e346bd","text":"secluded protected maiden `ي ق ن:B002/m01`","trust":"trusted"},{"branch_refs":["root_000531/B001","root_001040/B001","root_001069/B002","root_001696/B001"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"A:Sight Ripening into Certainty","source_type":"channel","support_id":"sup_85856ff21ce630f22514","text":"sensory seeing `ر ء ي:B001/m01`; insight `ر ء ي:B001/m02`; direct witnessing `ع ي ن:B002/m01`; knowledge `ع ل م:B001/m01`; fixed certainty `ي ق ن:B001/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Protected Seclusion","source_type":"channel","support_id":"sup_bf8de0af7bd7b96c8dd9","text":"Matter or persons are recessed, enclosed, protected, or held behind a boundary that may also open and leak.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Sight Ripening into Certainty","source_type":"channel","support_id":"sup_ea4a930d2ea1a20f6870","text":"Sensory or inward sight yields direct witnessing, knowledge, and settled certainty.","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"أَلْهَىٰكُمُ ٱلتَّكَاثُرُ","ayah_ref":"102:1"},{"arabic_uthmani":"كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ","ayah_ref":"102:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_001040/B002","root_001286/B002","root_001382/B001","root_001696/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001040","role":"A distinguishing mark makes focus-knowledge a criterion able to sort what matters from what merely multiplies.","root":"ع ل م","source_ref":"102:5","source_word_indices":["3","4"]},{"branch_id":"B001","mapped_root_id":"root_001696","role":"Doubt-ending stability defines the endpoint of the required reclassification.","root":"ي ق ن","source_ref":"102:5","source_word_indices":["5"]},{"branch_id":"B001","mapped_root_id":"root_001382","role":"Occupation by one thing away from another supplies the attentional displacement that prevents disclosure.","root":"ل ه و","source_ref":"102:1","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001286","role":"Rivalry through number supplies the seductive but defective metric governing that displaced attention.","root":"ك ث ر","source_ref":"102:1","source_word_indices":["2"]}],"changed_reading":{"after":"They already attend and measure intensely, but by the wrong sign: knowledge of certainty would replace competitive quantity with a doubt-ending criterion.","before":"The addressees merely need more facts."},"confidence":"strong","mechanism":"Diversion relocates attention, while competitive increase supplies the metric that captures it. The focus therefore diagnoses not a blank mind but a mind using numerical superiority as its governing sign; certainty requires a change of criterion.","model_id":"d_metric_reorientation","reader_inference":"The packet supplies displaced attention, numerical rivalry, a discriminating mark, and settled knowledge; I infer that the rival count functions as a false epistemic metric. A live alternative is simple distraction without any metric-switch mechanism.","status":"revised","structural_cues":["102:1 names the diversion and its object before 102:5 presents the unrealized conditional.","The focus doubles the knowing root as verb and noun, giving its counter-criterion internal emphasis."],"trigger_roots":["ل ه و","ك ث ر"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_metric_reorientation","source_type":"hft","support_id":"sup_48ee5148dabc78836f11","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"حَتَّىٰ زُرْتُمُ ٱلْمَقَابِرَ","ayah_ref":"102:2"},{"arabic_uthmani":"كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ","ayah_ref":"102:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000654/B003","root_001040/B002","root_001195/B002","root_001696/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001040","role":"The guiding landmark lets focus-knowledge orient a reader through a place whose meaning is not visible on its surface.","root":"ع ل م","source_ref":"102:5","source_word_indices":["3","4"]},{"branch_id":"B001","mapped_root_id":"root_001696","role":"Settled certainty prevents concealed terrain from being misread as an epistemic dead end.","root":"ي ق ن","source_ref":"102:5","source_word_indices":["5"]},{"branch_id":"B003","mapped_root_id":"root_000654","role":"The visitor's directed approach supplies motion toward a place without making that place a permanent endpoint.","root":"ز و ر","source_ref":"102:2","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001195","role":"Lowered concealment supplies the terrain through which the distinguishing mark must guide.","root":"ق ب ر","source_ref":"102:2","source_word_indices":["3"]}],"changed_reading":{"after":"It is also the orientation that reads a concealed apparent endpoint as a marked passage and therefore changes how one moves toward it.","before":"Knowledge of certainty is an abstract increase in conviction."},"confidence":"medium","mechanism":"A purposeful visit enters a lowered, concealed place. Read through the focus's landmark branch, certainty becomes navigational: it recognizes a place that appears terminal as a passage whose hiddenness must be read rather than mistaken for finality.","model_id":"d_hidden_waypoint","reader_inference":"The packet supplies visitation, concealment, guidance by a mark, and settledness; I supply the arrow from temporary approach through hidden terrain to waypoint rather than terminus. The live alternative is that visitation is only a conventional description and contributes no navigational model.","status":"new","structural_cues":["102:2 couples directed visitation with a plural place of burial before the conditional focus ayah."],"trigger_roots":["ز و ر","ق ب ر"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_hidden_waypoint","source_type":"hft","support_id":"sup_657d451ca01613003c1c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّا سَوْفَ تَعْلَمُونَ","ayah_ref":"102:3"},{"arabic_uthmani":"ثُمَّ كَلَّا سَوْفَ تَعْلَمُونَ","ayah_ref":"102:4"},{"arabic_uthmani":"كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ","ayah_ref":"102:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_001040/B001","root_001696/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001040","role":"Disclosure in the focus names a presently unrealized mode that could become internally clear.","root":"ع ل م","source_ref":"102:5","source_word_indices":["3","4"]},{"branch_id":"B001","mapped_root_id":"root_001696","role":"Settled certainty distinguishes anticipatory knowing from a fleeting warning.","root":"ي ق ن","source_ref":"102:5","source_word_indices":["5"]},{"branch_id":"B001","mapped_root_id":"root_001040","role":"The first future disclosure supplies the later, unavoidable side of the temporal fork.","root":"ع ل م","source_ref":"102:3","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001040","role":"Repeated future disclosure intensifies inevitability and prevents the focus conditional from meaning permanent unknowability.","root":"ع ل م","source_ref":"102:4","source_word_indices":["4"]}],"changed_reading":{"after":"It offers a vanishing temporal alternative: settled disclosure could be received now, before the same matter becomes unavoidable future knowledge.","before":"The conditional states a static absence of certain knowledge."},"confidence":"strong","mechanism":"The same disclosure root is promised twice in the future, then the focus switches to a conditional and adds both a cognate noun and certainty. This makes the focus a temporal fork between anticipatory, conduct-changing knowledge and disclosure that will arrive later regardless.","model_id":"d_temporal_fork","reader_inference":"The packet supplies repeated future disclosure and a subsequent conditional form of the same root; I infer a choice between knowing early enough to alter conduct and knowing later by compulsion. A live alternative is that all three clauses only accumulate emphasis without contrasting temporal modes.","status":"revised","structural_cues":["102:3 and 102:4 repeat the same future knowing clause, with 102:4 adding a sequence marker.","102:5 changes from future assertion to a conditional and expands the root into a verb-noun pairing qualified by certainty."],"trigger_roots":["ع ل م"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_temporal_fork","source_type":"hft","support_id":"sup_0e29f72908ca23bcdc4b","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ","ayah_ref":"102:5"},{"arabic_uthmani":"لَتَرَوُنَّ ٱلْجَحِيمَ","ayah_ref":"102:6"},{"arabic_uthmani":"ثُمَّ لَتَرَوُنَّهَا عَيْنَ ٱلْيَقِينِ","ayah_ref":"102:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000225/B001","root_000531/B001","root_000531/B012","root_001040/B001","root_001696/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001040","role":"Internal disclosure supplies a mode of access that can precede direct ocular encounter.","root":"ع ل م","source_ref":"102:5","source_word_indices":["3","4"]},{"branch_id":"B001","mapped_root_id":"root_001696","role":"Doubt-ending stability allows pre-visual disclosure to count as certainty rather than conjecture.","root":"ي ق ن","source_ref":"102:5","source_word_indices":["5"]},{"branch_id":"B001","mapped_root_id":"root_000531","role":"Vision by eye or insight supplies the later encounter against which the focus's prior knowing is differentiated.","root":"ر ء ي","source_ref":"102:6","source_word_indices":["1"]},{"branch_id":"B012","mapped_root_id":"root_000531","role":"Causing something to appear makes the later stage an imposed manifestation, not merely stronger private confidence.","root":"ر ء ي","source_ref":"102:7","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000225","role":"The intensely blazing object gives the later sight material force and raises the cost of deferred disclosure.","root":"ج ح م","source_ref":"102:6","source_word_indices":["2"]}],"changed_reading":{"after":"It is a distinct pre-visual mode: signs may disclose and settle the reality before that reality is forcibly manifested to sight.","before":"Knowledge of certainty is simply the strongest point on one scale of confidence."},"confidence":"strong","mechanism":"The focus's clear, settled knowing is followed by repeated seeing and showing of an intensely burning object. Knowledge of certainty thus becomes a pre-visual capacity to let signs disclose what later vision will force into encounter.","model_id":"d_previsual_disclosure","reader_inference":"The packet supplies prior settled disclosure, repeated vision or showing, and an intensely burning object; I infer that knowledge can internalize the warning before vision externalizes it. A live alternative is a single escalating rhetoric in which knowledge and sight are not distinct phases.","status":"strengthened","structural_cues":["102:5 is immediately followed by two emphatic future seeing clauses in 102:6-7."],"trigger_roots":["ر ء ي","ج ح م"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_previsual_disclosure","source_type":"hft","support_id":"sup_1b840a54752a0d94954e","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ","ayah_ref":"102:5"},{"arabic_uthmani":"ثُمَّ لَتَرَوُنَّهَا عَيْنَ ٱلْيَقِينِ","ayah_ref":"102:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_001040/B002","root_001069/B013","root_001696/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001040","role":"A mark pointing beyond itself makes focus-knowledge mediated yet capable of reliable guidance.","root":"ع ل م","source_ref":"102:5","source_word_indices":["3","4"]},{"branch_id":"B001","mapped_root_id":"root_001696","role":"Settledness shows that mediation need not mean residual doubt.","root":"ي ق ن","source_ref":"102:5","source_word_indices":["5"]},{"branch_id":"B013","mapped_root_id":"root_001069","role":"The thing itself supplies immediate presence as the later counterpart to knowledge by a pointing mark.","root":"ع ي ن","source_ref":"102:7","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001696","role":"The repeated certainty root holds the epistemic endpoint constant while the mode changes from sign to presence.","root":"ي ق ن","source_ref":"102:7","source_word_indices":["4"]}],"changed_reading":{"after":"It can be fully settled certainty in a mediated mode, distinct from but coexisting with the later certainty of the thing's immediate presence.","before":"Knowledge of certainty is an inferior approximation awaiting real certainty."},"confidence":"strong","mechanism":"The same certainty qualifier attaches first to knowledge in the focus and later to the eye or the thing itself. The landmark branch of knowledge and the presence branch of eye form two coexisting modes: certainty through reliable indication and certainty through immediate presence.","model_id":"d_sign_to_presence","reader_inference":"The packet supplies a guiding mark, the thing itself, and the repeated certainty qualifier; I infer a controlled contrast between mediated and immediate access. A live alternative is that the parallel constructions only intensify one undifferentiated certainty.","status":"revised","structural_cues":["The focus construction pairs knowledge with certainty, while 102:7 replaces knowledge with eye and repeats certainty."],"trigger_roots":["ع ي ن","ي ق ن"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_sign_to_presence","source_type":"hft","support_id":"sup_07989b0d9a51f41140cb","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَلْهَىٰكُمُ ٱلتَّكَاثُرُ","ayah_ref":"102:1"},{"arabic_uthmani":"كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ","ayah_ref":"102:5"},{"arabic_uthmani":"لَتَرَوُنَّ ٱلْجَحِيمَ","ayah_ref":"102:6"},{"arabic_uthmani":"ثُمَّ لَتَرَوُنَّهَا عَيْنَ ٱلْيَقِينِ","ayah_ref":"102:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":4,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":4,"target_morphology_supplied":false},"branch_refs":["root_000615/B001","root_001040/B005","root_001069/B006","root_001286/B007","root_001696/B001"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_001040","role":"Gathered abundant water anchors the hydrological model directly in the repeated focus root.","root":"ع ل م","source_ref":"102:5","source_word_indices":["3","4"]},{"branch_id":"B001","mapped_root_id":"root_001696","role":"Settled knowledge keeps the water circuit functional as an image of doubt removed rather than free association.","root":"ي ق ن","source_ref":"102:5","source_word_indices":["5"]},{"branch_id":"B007","mapped_root_id":"root_001286","role":"The gathering of a thing supplies accumulation, which can remain inert and competitive unless it becomes usable knowledge.","root":"ك ث ر","source_ref":"102:1","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000615","role":"The non-dominant mapped branch of quenching thirst supplies the functional test for whether gathered knowledge transforms the knower.","root":"ر ء ي","source_ref":"102:6","source_word_indices":["1"]},{"branch_id":"B006","mapped_root_id":"root_001069","role":"A flowing spring supplies source and circulation, changing the focus reservoir from stored quantity into replenishing contact.","root":"ع ي ن","source_ref":"102:7","source_word_indices":["3"]}],"changed_reading":{"after":"Exploratorily, certainty distinguishes sterile accumulation from knowledge that reaches its source and quenches: a circuit, not a hoard.","before":"The reservoir image suggests only that many pieces of knowledge have accumulated."},"confidence":"exploratory","mechanism":"The focus's remote gathered-water branch becomes more than a static reservoir: context supplies accumulation, quenching, and a spring. The resulting circuit contrasts hoarded increase with knowledge that reaches a source, circulates, and actually removes thirst.","model_id":"d_hydraulic_circuit","reader_inference":"The packet supplies gathered water, accumulation, thirst's removal through a non-dominant split mapping, and a spring; I connect them into a water circuit and contrast storage with transformation. The materially live alternative is accidental lexical clustering, especially because the quenching branch belongs to the secondary mapped root.","status":"strengthened","structural_cues":["The sequence runs from accumulation in 102:1 through the repeated knowledge root in 102:5 to seeing and eye in 102:6-7."],"trigger_roots":["ك ث ر","ر ء ي","ع ي ن"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_hydraulic_circuit","source_type":"hft","support_id":"sup_05cea3dcf4b9c1d1c652","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ","ayah_ref":"102:5"},{"arabic_uthmani":"ثُمَّ لَتُسْـَٔلُنَّ يَوْمَئِذٍ عَنِ ٱلنَّعِيمِ","ayah_ref":"102:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000661/B001","root_001040/B001","root_001525/B001","root_001696/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001040","role":"Disclosure to the knower supplies the cognition that can later ground an account rather than an excuse of opacity.","root":"ع ل م","source_ref":"102:5","source_word_indices":["3","4"]},{"branch_id":"B001","mapped_root_id":"root_001696","role":"Doubt removed gives the disclosed matter enough stability to bear practical responsibility.","root":"ي ق ن","source_ref":"102:5","source_word_indices":["5"]},{"branch_id":"B001","mapped_root_id":"root_000661","role":"Question and demand convert certainty from an inward state into a relation in which a response is owed.","root":"س ء ل","source_ref":"102:8","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001525","role":"Good condition and benefit identify the concrete field for which the knower becomes answerable.","root":"ن ع م","source_ref":"102:8","source_word_indices":["5"]}],"changed_reading":{"after":"Certain knowledge is answerable knowledge: once disclosure settles, the knower stands in a response-bearing relation to the benefits that shaped conduct.","before":"Certain knowledge is a private achievement of the mind."},"confidence":"medium","mechanism":"Later questioning about a good or comfortable condition makes the focus's settled disclosure answerable. Knowledge is no longer private possession; it establishes the capacity and obligation to respond for how received ease was understood and used.","model_id":"d_answerable_certainty","reader_inference":"The packet supplies settled disclosure, questioning, and benefit; I infer that later interrogation retroactively gives focus-knowledge an ethical and relational function. A live alternative is that the question is merely a later consequence and does not characterize the knowledge in 102:5.","status":"revised","structural_cues":["102:8 follows the two seeing clauses with a sequence marker and an emphatic passive future question."],"trigger_roots":["س ء ل","ن ع م"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_answerable_certainty","source_type":"hft","support_id":"sup_7c7013bbc61d5a57f8f2","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ","ayah_ref":"102:5"},{"arabic_uthmani":"ثُمَّ لَتَرَوُنَّهَا عَيْنَ ٱلْيَقِينِ","ayah_ref":"102:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_001069/B013","root_001696/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001696","role":"Protection and seclusion image focus-certainty as guarded knowledge that need not yet be exposed to sight.","root":"ي ق ن","source_ref":"102:5","source_word_indices":["5"]},{"branch_id":"B013","mapped_root_id":"root_001069","role":"The thing itself supplies the later presence into which guarded, pre-visual certainty can emerge.","root":"ع ي ن","source_ref":"102:7","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001696","role":"Repetition of the same remote branch preserves continuity between secluded knowing and later exposure.","root":"ي ق ن","source_ref":"102:7","source_word_indices":["4"]}],"changed_reading":{"after":"Exploratorily, knowledge of certainty may be guarded pre-visual knowledge whose truth is protected before it is brought into immediate presence.","before":"Certainty means maximal exposure and cognitive openness from the outset."},"confidence":"exploratory","containment":"This is surprising because it activates a remote nominal branch of the certainty root involving protection and seclusion. It remains anchored at focus word 5 and gains a real contrast from the later eye or thing-itself construction. Downstream prose should present it as a guardedness resonance, not as the lexical gloss of certainty.","focus_anchor":"Word 5 can carry a remote image of something protected from exposure, while the same root later stands beside the eye or thing itself.","outlier_id":"o_guarded_certainty"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:o_guarded_certainty","source_type":"hft","support_id":"sup_28725db7daa3c1e60994","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ","ayah_ref":"102:5"},{"arabic_uthmani":"ثُمَّ لَتُسْـَٔلُنَّ يَوْمَئِذٍ عَنِ ٱلنَّعِيمِ","ayah_ref":"102:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000661/B001","root_000736/B001","root_001040/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001040","role":"A matter becoming clear supplies the latent content that can either be received now or elicited later.","root":"ع ل م","source_ref":"102:5","source_word_indices":["3","4"]},{"branch_id":"B001","mapped_root_id":"root_000661","role":"Question and demand provide the overt social mechanism by which an answer is required.","root":"س ء ل","source_ref":"102:8","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000736","role":"The secondary image of gently drawing something out turns questioning into exploratory extraction of what remained concealed.","root":"س ء ل","source_ref":"102:8","source_word_indices":["2"]}],"changed_reading":{"after":"Exploratorily, disclosure refused as voluntary knowing will later be drawn out under questioning, converting concealed knowledge into an answer.","before":"The hypothetical knowledge is simply absent and can remain absent."},"confidence":"exploratory","containment":"This is surprising because the extraction image belongs to the non-dominant mapped root attached to the later questioning root. It remains anchored in the focus's disclosure branch and in a packet-resolved context citation. Downstream prose should call it a split-mapping abductive echo, never an etymology or direct translation.","focus_anchor":"The disclosure root at words 3-4 leaves knowing unrealized, while the later question activates both asking and a secondary image of something quietly drawn out.","outlier_id":"o_knowledge_drawn_out"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:o_knowledge_drawn_out","source_type":"hft","support_id":"sup_73ecebd7bd63926a55c1","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَلْهَىٰكُمُ ٱلتَّكَاثُرُ","ayah_ref":"102:1"},{"arabic_uthmani":"كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ","ayah_ref":"102:5"},{"arabic_uthmani":"ثُمَّ لَتُسْـَٔلُنَّ يَوْمَئِذٍ عَنِ ٱلنَّعِيمِ","ayah_ref":"102:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000661/B001","root_001040/B004","root_001382/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001040","role":"A visible cleft at the upper lip makes knowing an embodied interruption and publicly legible mark at speech's threshold.","root":"ع ل م","source_ref":"102:5","source_word_indices":["3","4"]},{"branch_id":"B004","mapped_root_id":"root_001382","role":"The flesh over the throat extends the image from lip to the inner threshold of intake and utterance.","root":"ل ه و","source_ref":"102:1","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000661","role":"Questioning redirects the oral threshold from consumption or diversion toward an owed answer.","root":"س ء ل","source_ref":"102:8","source_word_indices":["2"]}],"changed_reading":{"after":"Exploratorily, it is a rupture that marks the body of speech: diversion at the mouth is interrupted so that the knower must become answerable.","before":"Knowledge of certainty is wholly invisible cognition."},"confidence":"exploratory","containment":"This is surprising because it joins two remote bodily branches with a later act of questioning. It remains anchored in the repeated focus root and produces an embodied change from intake to answer. Downstream prose should qualify it as a somatic branch-image constellation, not a claim about ordinary word meaning.","focus_anchor":"The repeated knowing root at words 3-4 has a branch of a visible upper-lip cleft, allowing certainty to become a bodily mark at the opening of speech.","outlier_id":"o_oral_mark"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:o_oral_mark","source_type":"hft","support_id":"sup_bee3fdfaea853392e2c5","trust":"legacy_unbound"}]}
</lane_packet_json>
