# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **112:3**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s112-regular-20260911/s112/112_3/macro.discovery.json` and modify nothing
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
  "ayah_ref": "112:3",
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
{"analysis_context":{"analysis_id":"s112-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"112:3","host_surah":112,"lane_context_refs":["112:0","112:1","112:2","112:4","1:2","1:3","1:4","1:5","1:6","1:7"],"ordered_context_refs":["112:0","112:1","112:2","112:4","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Includes the annual produce or offspring of palms or camels, asking or granting a year's use of milk, wool, offspring, or fruit, and dividing camels into two alternating breeding lots.","branch_kind":null,"branch_ref":"root_001305/B005","candidate_links":[{"candidate_id":"cand_18f343d1fe4e908c6e1f","lane":"macro"},{"candidate_id":"cand_af81ed11c24bc90ef3a9","lane":"macro"}],"focus_root_occurrences":[],"gloss":"yearly produce and breeding lot","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"كفأة السنة والنتاج","image_en":"yearly produce and breeding lot"}}],"root_ar":"ك ف ء","root_id":"root_001305","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"كفأة السنة والنتاج","image_en":"yearly produce and breeding lot","scope_ar":"يدخل فيه الكفأة لحمل النخلة أو نتاج الإبل سنة؛ سؤال نتاج الإبل أو ثمر النخل سنة؛ إعطاء اللبن والوبر والأولاد سنة؛ جعل الإبل كفأتين يتناوب نتاجهما","scope_en":"Includes the annual produce or offspring of palms or camels, asking or granting a year's use of milk, wool, offspring, or fruit, and dividing camels into two alternating breeding lots."},"support_links":["sup_c34bf28f536ea0b97ab2","sup_ddcd1316fccf6f46df9f"]},{"boundary":"Includes a thing occurring or being present, being reported in past or present time, the verbal noun of kana, kaynuna, ka'inah, and grammatical uses of kana for predication, emphasis, or exception.","branch_kind":null,"branch_ref":"root_001332/B001","candidate_links":[{"candidate_id":"cand_47712604fc245f2251ea","lane":"macro"},{"candidate_id":"cand_88754fa993d5f8b5c6e7","lane":"macro"},{"candidate_id":"cand_af81ed11c24bc90ef3a9","lane":"macro"}],"focus_root_occurrences":[],"gloss":"being, occurrence, or temporal predication","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"وقوع الشيء وحضوره في زمان","image_en":"being, occurrence, or temporal predication"}}],"root_ar":"ك و ن","root_id":"root_001332","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"وقوع الشيء وحضوره في زمان","image_en":"being, occurrence, or temporal predication","scope_ar":"يدخل فيه وقوع الشيء وحضوره وحدوثه في زمان ماض أو راهن، ومصدر كان والكينونة والكائنة، واستعمال كان خبرا أو توكيدا أو في الاستثناء.","scope_en":"Includes a thing occurring or being present, being reported in past or present time, the verbal noun of kana, kaynuna, ka'inah, and grammatical uses of kana for predication, emphasis, or exception."},"support_links":["sup_2adb47d33bb33f9e59d2","sup_82274133c09b5f1d387d","sup_c34bf28f536ea0b97ab2"]},{"boundary":"Includes the idiom kunti for a man who has grown old, as if named from saying \"I used to\" about his youth.","branch_kind":null,"branch_ref":"root_001332/B005","candidate_links":[{"candidate_id":"cand_3be7d189f8e1be7ebd07","lane":"macro"}],"focus_root_occurrences":[],"gloss":"the old \"I used to\" man","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الشيخ المنسوب إلى كُنْتُ","image_en":"the old \"I used to\" man"}}],"root_ar":"ك و ن","root_id":"root_001332","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الشيخ المنسوب إلى كُنْتُ","image_en":"the old \"I used to\" man","scope_ar":"يدخل فيه الكُنْتِيّ للرجل إذا شاخ كأنه نسب إلى قوله كُنْتُ في شبابي.","scope_en":"Includes the idiom kunti for a man who has grown old, as if named from saying \"I used to\" about his youth."},"support_links":["sup_fe093f4d486a5c43d87a"]},{"boundary":"Dal, doğuran ana babayı ve doğurma olayını değil, bu olay sonucunda dünyaya gelen kişiyi gösterir.","branch_kind":"mixed_non_bare","branch_ref":"root_001683/B001","candidate_links":[{"candidate_id":"cand_9cc13c6030a926737000","lane":"macro"},{"candidate_id":"cand_db40421a83be74842e42","lane":"macro"},{"candidate_id":"cand_cb54df7ea405145b835f","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:2:1","qac_word_ref":"112:3:2","surface_ar":"يَلِدْ"},{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:4:1","qac_word_ref":"112:3:4","surface_ar":"يُولَدْ"}],"gloss":"ana babadan doğan kişi veya kişiler","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim, bir ana babadan doğmuş kişidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlandırma sayı, cinsiyet ve yaş bakımından sınırlı değildir; bir veya çok kişiyi, kız veya erkeği, küçüğü veya yetişkini gösterebilir."}}],"root_ar":"و ل د","root_id":"root_001683","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın bütün çekirdeğini karşılar; tek ve çok kişi ile kız, erkek, küçük ve yetişkin kullanımlarının hepsine açıktır.","boundary_detail":"Dal, doğuran ana babayı ve doğurma olayını değil, bu olay sonucunda dünyaya gelen kişiyi gösterir.","branch_image_ar":"مولود من نسل","concept_gloss":"ana babadan doğan kişi veya kişiler","contextual_glosses":[{"applicability":"Tek bir kişinin ana babasına göre konumunu anlatan doğal cümlelerde kullanılır; kişinin yaşını veya cinsiyetini sınırlamaz.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ana babadan doğmuş kişi olma bağını bağlam içinde eksiksiz korur."},"facet_ids":["F001","F002"],"text":"birinin çocuğu","usage_role":"general"},{"applicability":"Bir ana babadan doğan birden çok kişiden söz edilen çoğul bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doğum bağını ve çoğul gönderimi ilgili bağlamda korur."},"facet_ids":["F001","F002"],"text":"çocukları","usage_role":"contextual"}],"definition":"Bir ana babadan doğan kişi; bu kişi tek ya da birden çok, kız ya da erkek, küçük ya da yetişkin olabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim, bir ana babadan doğmuş kişidir."},{"facet_id":"F002","role":"extension","statement":"Adlandırma sayı, cinsiyet ve yaş bakımından sınırlı değildir; bir veya çok kişiyi, kız veya erkeği, küçüğü veya yetişkini gösterebilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kızları ve cinsiyetten bağımsız genel kullanımı dışarıda bırakır.","preserves":"Ana babadan doğan kişi olma bağını korur."},"text":"oğul"},{"category":"confusable","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Daha büyük çocuklar ile yetişkin çocuklara uzanan yaş kapsamını kaybeder.","preserves":"Doğmuş ve küçük bir kişi olma yönünü korur."},"text":"bebek"}],"identity_rationale":"Kaynak ifadesi, ana babadan doğan çocuğu temel alır ve bu adlandırmanın tek ya da çok kişi, kız ya da erkek, küçük ya da yetişkin için kullanılabildiğini açıkça belirtir. Verilen dal çerçevesi bu kapsamı doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"birinin çocuğu; bir veya birden çok doğmuş kişi"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"çocuklar"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"doğmuş çocuk; yeni doğan"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"kim olduğunu bilmiyorum"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"birbirlerinden çocuk sahibi olup çoğaldılar"}],"lexicalization_note":"Tanım, doğan kişiye ilişkin yalın çekirdeği temel alır; listedeki kalıba bağlı ve türemiş kullanımlar ayrı sözlük karşılıklarında tutulur.","neighbor_coverage_note":"Verilen bütün komşu adayları değerlendirildi; yayımlanan dört karşılaştırma doğrudan çocuk, geniş çocukluk bağı, yeni doğmuşluk ve süren soy sınırlarını en açık biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın çekirdeği doğmuş kişidir; komşu dal ise çocuk yanında karşılıklı çoğalma sürecini ve hayvanların üretim amacını da anlamın içine alır.","focus_only":"Bu dal, insan çocuğunun sayı, cinsiyet ve yaş bakımından geniş adlandırılmasını öne çıkarır.","gloss":"çocuk ve çoğalan soy","neighbor_only":"Komşu dal, birbirinden çoğalmayı ve soy üretmek için tutulan hayvanları da kapsar.","neighbor_ref":"root_001499/B001","relation_type":"near_synonym","shared_zone":"İki dal da doğan çocuk ve soyun sürmesi alanında örtüşür."},{"boundary_match":"partial","distinction":"Bu dal gerçek doğum sonucundaki kişiye dayanır; komşu dal çocukluk bağını doğum dışındaki edinme, yetiştirme ve kaynaktan gelme ilişkilerine genişletir.","focus_only":"Bu dal, doğmuş kişinin kendisini sayı, cinsiyet ve yaştan bağımsız biçimde adlandırır.","gloss":"çocuk ve çocukluk bağı","neighbor_only":"Komşu dal evlat edinmeyi, yetiştirmeyi, hizmeti ve bir kaynaktan gelme benzetmelerini de kapsar.","neighbor_ref":"root_000156/B007","relation_type":"near_synonym","shared_zone":"İki dal da oğul, kız ve çocuk olma bağında örtüşür."},{"boundary_match":"partial","distinction":"Bu dal çocukluk bağını yaş sınırlaması olmadan verir; komşu dal yeni doğmuşluk çevresinde daralır ve ayrıca yaşla sınırlı olmayan köle anlamını taşır.","focus_only":"Bu dal her yaştaki çocuğu kapsar ve kölelik konumunu anlamın parçası yapmaz.","gloss":"çocuk / yeni doğmuş çocuk veya köle","neighbor_only":"Komşu dal yakın zamanda doğmuş çocuğa ve ayrıca erkek ya da kadın köleye özgü kullanımları kapsar.","neighbor_ref":"root_001683/B004","relation_type":"near_neighbor","shared_zone":"Yakın zamanda doğmuş çocuk, iki dalın kesiştiği alandır."},{"boundary_match":"field_only","distinction":"Bu dalın çekirdeği doğmuş çocukken komşu dal kuşaklar boyunca geride kalan soyun devamına ve torunlara yönelir.","focus_only":"Bu dal doğrudan ana babadan doğan kişiyi ve genel çocuk adlandırmasını öne çıkarır.","gloss":"çocuk / ardından gelen soy","neighbor_only":"Komşu dal kişinin ardından kalan çocukları, çocuklarının çocuklarını ve süren soy çizgisini kapsar.","neighbor_ref":"root_001033/B004","relation_type":"same_field","shared_zone":"Her iki dal da çocuk ve soy bağı alanındadır."}],"source_phrase_ar":"أصل صحيح وهو دليل النجل والنسل؛ الولد وهو للواحد والجميع (maqayis)؛ الولد قد يكون واحدا وجمعا؛ الوليد الصبي (sihah)؛ الولد اسم يجمع الواحد والكثير والذكر والأنثى؛ الوليد الصبي حين يولد (tahdhib)؛ الولد المولود؛ الابن والابنة؛ جمع الولد أولاد (mufradat)","source_summary":"Kaynakların ortak çekirdeği, ana babadan doğan kişidir. Kullanımın tekillik, çoğulluk, cinsiyet ve yaş sınırlarını aşabildiği de aynı toplu kanıtta belirtilir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الولد والمولود والابن والابنة والأولاد، ويستعمل للواحد والجمع وللصغير والكبير وللذكر والأنثى بحسب نصوص المصادر.","what_is_not_ar":"لا يدخل هنا خصوص الأب أو الأم، ولا نفس فعل الولادة، ولا معنى العبد أو الأمة للوليد والوليدة إلا من جهة تسمية الصغير."},"support_links":["sup_136fe31b0a49d0faa228","sup_ee925618c6c64515cd7e","sup_ff13cb8d0dabf85f3ac2"]},{"boundary":"Buradaki ana baba, çocuğa göre doğum bağı taşıyan iki kişidir; çocuk, bakıcı veya daha uzak büyükler bu dalın çekirdeği değildir.","branch_kind":"bare","branch_ref":"root_001683/B002","candidate_links":[{"candidate_id":"cand_9cc13c6030a926737000","lane":"macro"},{"candidate_id":"cand_c27d7d8e1b77ecc928c6","lane":"macro"},{"candidate_id":"cand_b1c6e29f4b3f4ba943bc","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:2:1","qac_word_ref":"112:3:2","surface_ar":"يَلِدْ"},{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:4:1","qac_word_ref":"112:3:4","surface_ar":"يُولَدْ"}],"gloss":"öz ana baba","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Erkek yönündeki kişi, çocuğun öz babasıdır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kadın yönündeki kişi, çocuğun öz anasıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İki kişi birlikte çocuğun ana babası olarak adlandırılır."}}],"root_ar":"و ل د","root_id":"root_001683","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çocuğun doğum bağıyla bağlı olduğu babayı, anayı veya ikisini birlikte anlatan genel karşılıktır.","boundary_detail":"Buradaki ana baba, çocuğa göre doğum bağı taşıyan iki kişidir; çocuk, bakıcı veya daha uzak büyükler bu dalın çekirdeği değildir.","branch_image_ar":"أبوان من جهة الولادة","concept_gloss":"öz ana baba","contextual_glosses":[{"applicability":"Doğum bağının erkek tarafındaki tek kişiden söz edildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Baba yönündeki doğum bağını ilgili tekil bağlamda tam olarak korur."},"facet_ids":["F001"],"text":"öz baba","usage_role":"contextual"},{"applicability":"Doğum bağının kadın tarafındaki tek kişiden söz edildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ana yönündeki doğum bağını ilgili tekil bağlamda tam olarak korur."},"facet_ids":["F002"],"text":"öz ana","usage_role":"contextual"},{"applicability":"İki doğum bağı kişisinin birlikte anıldığı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ana ve babayı birlikte gösteren çift kapsamını korur."},"facet_ids":["F001","F002","F003"],"text":"anası ile babası","usage_role":"general"}],"definition":"Bir çocuğun doğum bağıyla bağlı olduğu öz babası, öz anası ve bu ikisinin birlikte oluşturduğu ana baba çifti.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Erkek yönündeki kişi, çocuğun öz babasıdır."},{"facet_id":"F002","role":"core","statement":"Kadın yönündeki kişi, çocuğun öz anasıdır."},{"facet_id":"F003","role":"extension","statement":"İki kişi birlikte çocuğun ana babası olarak adlandırılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Doğum bağı bulunmayan koruyucu ve bakım veren kişileri de kapsama ekler.","collision":"Bakım görevi ile doğumdan gelen ana babalık bağını birbirine karıştırır.","fit":"broadening","loses":null,"preserves":"Çocukla ilgilenen yetişkinler çevresini çağrıştırır."},"text":"bakıcılar"}],"identity_rationale":"Kaynak ifadesi, babayı doğum bağı yönünden baba, anayı da aynı yönden ana olarak adlandırır ve ikisini birlikte bir çift halinde verir. Dal çerçevesi bu üçlü dağılımı doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"öz baba"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"öz ana"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ana baba"}],"lexicalization_note":"Tanım yalın ana, baba ve ikisini birlikte gösteren adlandırmayla sınırlıdır; başka aile veya bakım ilişkileri içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; seçilen karşılaştırmalar çocukla karşılıklı konumu, baba ve ana yönündeki genişlemeleri ve kuşak sınırını en yararlı biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Bir dal doğuran ana baba yönünü, öteki dal doğan çocuk yönünü adlandırır; aynı ilişkinin karşılıklı uçlarıdır.","focus_only":"Bu dal doğum bağının ana ve baba yönündeki kişilerini gösterir.","gloss":"ana baba / çocuk","neighbor_only":"Komşu dal aynı bağın doğan çocuk yönündeki kişisini gösterir.","neighbor_ref":"root_001683/B001","relation_type":"polarity_pair","shared_zone":"İki dal aynı doğum bağındaki karşılıklı aile konumlarını paylaşır."},{"boundary_match":"partial","distinction":"Bu dal ana ile babayı doğum bağı içinde birlikte düzenler; komşu dal baba adını doğum dışındaki neden olma ve bakım işlevlerine de genişletir.","focus_only":"Bu dal öz ana ile öz babayı birlikte kapsar ve doğum bağını temel alır.","gloss":"öz ana baba / babalık ve bakım","neighbor_only":"Komşu dal yalnız baba yönünden başlayıp var etmeye, yetiştirmeye ve koruyup beslemeye de uzanır.","neighbor_ref":"root_000007/B001","relation_type":"near_neighbor","shared_zone":"Öz baba, iki dalın doğrudan kesiştiği kişidir."},{"boundary_match":"partial","distinction":"Bu dal doğum bağındaki ana babayı gösterir; komşu dal yalnız ana yönünü ele alır ve analığı bakım ile kalıplaşmış söyleyişlere taşır.","focus_only":"Bu dal öz babayı da içerir ve ana babayı çift olarak kurar.","gloss":"öz ana baba / analık ve bakım","neighbor_only":"Komşu dal ana adını yakın ve uzak analara, ana gibi besleyip yetiştirmeye ve kalıp sözlere genişletir.","neighbor_ref":"root_000053/B001","relation_type":"near_neighbor","shared_zone":"Öz ana, iki dalın doğrudan kesiştiği kişidir."}],"source_phrase_ar":"الوالد الأب والوالدة الأم وهما الوالدان (sihah)؛ يقال لأم الرجل هذه والدة (tahdhib)؛ الأب يقال له والد والأم والدة ويقال لهما والدان (mufradat)","source_summary":"Kaynaklar babayı, anayı ve ikisini birlikte gösteren ana baba çiftini aynı doğum bağı içinde ortak biçimde tanımlar.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه الوالد بمعنى الأب، والوالدة بمعنى الأم، والوالدان للأب والأم.","what_is_not_ar":"لا يدخل هنا الولد نفسه ولا الصبي ولا المولد موضعا أو زمانا."},"support_links":["sup_27044d6c1a701830e136","sup_9cf5708e78cbe077450c","sup_ff13cb8d0dabf85f3ac2"]},{"boundary":"Dal, doğmuş çocuğun kendisini değil doğurma olayını ve kaynakta açıkça verilen olaya bağlı kullanımları kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001683/B003","candidate_links":[{"candidate_id":"cand_9cc13c6030a926737000","lane":"macro"},{"candidate_id":"cand_18f343d1fe4e908c6e1f","lane":"macro"},{"candidate_id":"cand_db40421a83be74842e42","lane":"macro"},{"candidate_id":"cand_88754fa993d5f8b5c6e7","lane":"macro"},{"candidate_id":"cand_2c19842431d6276d7278","lane":"macro"},{"candidate_id":"cand_af81ed11c24bc90ef3a9","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:2:1","qac_word_ref":"112:3:2","surface_ar":"يَلِدْ"},{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:4:1","qac_word_ref":"112:3:4","surface_ar":"يُولَدْ"}],"gloss":"çocuğu dünyaya getirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek olay, kadının çocuğunu dünyaya getirmesidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir dişinin doğum zamanının gelmesi ayrıca belirtilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hayvan bağlamında gebe koyun bu söz alanındaki özel bir nitelemeyle gösterilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir koyunun doğumunu üstlenmek veya doğumuna yardım etmek ayrıca anlatılır."}},{"facet_id":"F005","role":"example","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Bir kişinin doğduğu gün, olayın zamanını belirten kullanım örneğidir."}}],"root_ar":"و ل د","root_id":"root_001683","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın temel doğurma olayını karşılar; zaman, hayvan ve yardım kullanımları bağlama göre ayrıca açıklanır.","boundary_detail":"Dal, doğmuş çocuğun kendisini değil doğurma olayını ve kaynakta açıkça verilen olaya bağlı kullanımları kapsar.","branch_image_ar":"حدوث الولادة ووضع الحمل","concept_gloss":"çocuğu dünyaya getirme","contextual_glosses":[{"applicability":"Kadının çocuğunu dünyaya getirdiği olayın eylem olarak anlatıldığı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doğurma olayını eylem bağlamında eksiksiz korur."},"facet_ids":["F001"],"text":"doğurmak","usage_role":"general"},{"applicability":"Bir dişinin doğum zamanının geldiği veya çok yaklaştığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doğum vaktinin gelmesi yönünü ilgili bağlamda korur."},"facet_ids":["F002"],"text":"doğumu yaklaşmak","usage_role":"contextual"},{"applicability":"Bir koyunun doğurma sürecini üstlenen kişinin eylemini açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doğuran hayvana yardım eden kişinin katılımını açıkça korur."},"facet_ids":["F004"],"text":"doğumuna yardım etmek","usage_role":"explanatory"}],"definition":"Bir kadının çocuğunu bedeninden çıkararak dünyaya getirmesi. Buna bağlı kullanımlar doğum zamanının gelmesini, gebe koyunu, koyunun doğumunu üstlenmeyi ve doğulan günü de anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek olay, kadının çocuğunu dünyaya getirmesidir."},{"facet_id":"F002","role":"associated_use","statement":"Bir dişinin doğum zamanının gelmesi ayrıca belirtilir."},{"facet_id":"F003","role":"specialization","statement":"Hayvan bağlamında gebe koyun bu söz alanındaki özel bir nitelemeyle gösterilir."},{"facet_id":"F004","role":"associated_use","statement":"Bir koyunun doğumunu üstlenmek veya doğumuna yardım etmek ayrıca anlatılır."},{"facet_id":"F005","role":"example","statement":"Bir kişinin doğduğu gün, olayın zamanını belirten kullanım örneğidir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Çiftleşme ve çoğalma gibi doğurma anından önceki veya daha geniş süreçleri kapsama ekler.","collision":"Doğurma olayı ile bütün çoğalma sürecini birbirine karıştırabilir.","fit":"broadening","loses":null,"preserves":"Yeni bir canlının ortaya çıkması yönünü genel olarak korur."},"text":"üreme"}],"identity_rationale":"Kaynak ifadesi kadının çocuğunu dünyaya getirmesini çekirdek yapar; doğum zamanının gelmesi, gebe koyun, koyunun doğumunu üstlenme ve doğulan gün kullanımlarını da aynı dalda bildirir. Verilen çerçeve bu olay ile ona bağlı kullanımları ayırt etmeye elverişlidir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kadın çocuğunu dünyaya getirdi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"doğum; çocuğu dünyaya getirme"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"doğum zamanı geldi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"gebe koyun"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"koyunun doğumunu üstlendik"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"birbirlerinden çocuk sahibi olup çoğaldılar"}],"lexicalization_note":"Yalın çekirdek doğurma olayıdır; zaman, gebe koyun ve doğuma yardım bildiren kalıba bağlı kullanımlar ayrı yüzler olarak tutulur.","neighbor_coverage_note":"Bütün komşular değerlendirildi; seçilenler genel doğumun gebeliği bırakma, güç doğum, erken doğum ve doğmuş çocuktan ayrıldığı sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"İki dal doğurma olayında yaklaşır; bu dal olay çevresindeki hayvan ve yardım kullanımlarını toplarken komşu dal gebeliğin bırakılması ile özel döngü zamanlamasını öne çıkarır.","focus_only":"Bu dal genel doğurma olayının yanında doğum vaktini, gebe koyunu ve doğuma yardımı da kapsar.","gloss":"doğurma / gebeliği doğumla bırakma","neighbor_only":"Komşu dal gebeliğin doğumla bırakılmasını ve kadın döngüsünün sonuyla ilgili özel zamanlamayı da içerir.","neighbor_ref":"root_001657/B002","relation_type":"near_synonym","shared_zone":"Kadının taşıdığı çocuğu doğumla bedeninden çıkarması iki dalın ortak çekirdeğidir."},{"boundary_match":"partial","distinction":"Bu dal doğumun genel gerçekleşmesini gösterir; komşu dal aynı olayın güçlükle gerçekleşen özel durumuna daralır.","focus_only":"Bu dal doğurmanın kendisini güçlük şartı olmadan anlatır.","gloss":"doğurma / güç doğum","neighbor_only":"Komşu dal yalnız doğumun güçleşmesi durumunu ve bu güçlükle ilgili dilek söyleyişlerini anlatır.","neighbor_ref":"root_001012/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da doğum olayını ve doğuran kadını içerir."},{"boundary_match":"partial","distinction":"Bu dal zaman bakımından yansız doğurma olayıdır; komşu dal süre dolmadan gerçekleşip yavrunun yaşadığı doğumla sınırlıdır.","focus_only":"Bu dal doğumun zamanından önce olmasını şart koşmaz ve genel olayı anlatır.","gloss":"doğurma / erken doğurma","neighbor_only":"Komşu dal yavrunun süresi tamamlanmadan doğduğu ve yaşamayı sürdürdüğü özel erken doğumu anlatır.","neighbor_ref":"root_000987/B007","relation_type":"near_neighbor","shared_zone":"Her iki dalda da gebe dişi yavrusunu dünyaya getirir."},{"boundary_match":"partial","distinction":"Bu dal süreç ve olaydır; komşu dal o sürecin katılımcısı ve sonucu olan doğmuş kişidir.","focus_only":"Bu dal çocuğu dünyaya getiren olay ve bu olaya bağlı kullanımları gösterir.","gloss":"doğurma / doğan çocuk","neighbor_only":"Komşu dal olay tamamlandıktan sonra doğmuş kişinin kendisini gösterir.","neighbor_ref":"root_001683/B001","relation_type":"near_neighbor","shared_zone":"Doğum olayı ile bu olay sonucunda ortaya çıkan çocuk aynı sahneyi paylaşır."}],"source_phrase_ar":"ولدت المرأة تلد ولادا وولادة؛ أولدت حان ولادها (sihah)؛ الولادة فهو وضع الوالدة ولدها؛ شاة والد وهي الحامل؛ ولدناها أي ولينا ولادتها (tahdhib)؛ يوم ولدت؛ يوم ولد (mufradat)","source_summary":"Toplu kanıt doğurma olayını merkeze alır; doğum vaktinin gelmesini, gebe koyunu, doğuma yardım etmeyi ve kişinin doğduğu günü bu olay çevresindeki kullanımlar olarak verir.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه ولدت المرأة، والولادة بوضع الوالدة ولدها، وما قرب من وقت الولادة أو حان ولاده في أولدت، وولادة الحيوان إذا نصت المصادر عليها.","what_is_not_ar":"لا يدخل هنا مجرد الولد بعد ولادته، ولا الوالدين كعلاقة اسمية، ولا المولد إذا أريد به المكان أو الوقت."},"support_links":["sup_1ea4761bfcd99d1b059f","sup_2adb47d33bb33f9e59d2","sup_c34bf28f536ea0b97ab2","sup_ddcd1316fccf6f46df9f","sup_ee925618c6c64515cd7e","sup_ff13cb8d0dabf85f3ac2"]},{"boundary":"Erkek biçimin çocuk yönü yeni doğmuş çocuk yanında ergenlik öncesi oğlanı da kapsar; kadın biçimi kız çocuğu ve kadın köle için kullanılır, köle anlamı özellikle kadın biçiminde yaş şartına bağlı değildir.","branch_kind":"bare","branch_ref":"root_001683/B004","candidate_links":[{"candidate_id":"cand_9cc13c6030a926737000","lane":"macro"},{"candidate_id":"cand_4de10fe62eace07e34f4","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:2:1","qac_word_ref":"112:3:2","surface_ar":"يَلِدْ"},{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:4:1","qac_word_ref":"112:3:4","surface_ar":"يُولَدْ"}],"gloss":"yeni doğmuş çocuk veya köle","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Erkek biçimi yakın zamanda doğmuş çocuk veya ergenlik öncesi oğlan için kullanılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Erkek biçimi bir erkek köleyi de gösterebilir."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kadın biçimi kız çocuğunu gösterebilir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kadın biçimi kadın köleyi gösterir ve bu kullanım ileri yaşta da geçerli olabilir."}}],"root_ar":"و ل د","root_id":"root_001683","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Erkek ve kadın biçimlerinin çocuk ile köle yönlerini birlikte özetler; kadın kölede yaş sınırlaması bulunmadığını açıklama tamamlar.","boundary_detail":"Erkek biçimin çocuk yönü yeni doğmuş çocuk yanında ergenlik öncesi oğlanı da kapsar; kadın biçimi kız çocuğu ve kadın köle için kullanılır, köle anlamı özellikle kadın biçiminde yaş şartına bağlı değildir.","branch_image_ar":"صغير قريب العهد بالولادة أو مملوك","concept_gloss":"yeni doğmuş çocuk veya köle","contextual_glosses":[{"applicability":"Erkek biçimin yakın zamanda doğmuş çocuk anlamıyla kullanıldığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Erkek çocuk ve yakın zamanda doğmuşluk özelliklerini birlikte korur."},"facet_ids":["F001"],"text":"yeni doğmuş erkek çocuk","usage_role":"contextual"},{"applicability":"Kadın biçimin köle anlamında, yaştan bağımsız kullanıldığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadın oluşu, kölelik konumunu ve yaş bağımsızlığını korur."},"facet_ids":["F004"],"text":"kadın köle","usage_role":"contextual"}],"definition":"Erkek biçimde yakın zamanda doğmuş çocuk veya ergenlik öncesi oğlan; kadın biçimde kız çocuk; ayrıca erkek ya da kadın köle. Kadın köle anlamı kişinin ileri yaşta olmasına karşın sürebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Erkek biçimi yakın zamanda doğmuş çocuk veya ergenlik öncesi oğlan için kullanılır."},{"facet_id":"F002","role":"extension","statement":"Erkek biçimi bir erkek köleyi de gösterebilir."},{"facet_id":"F003","role":"core","statement":"Kadın biçimi kız çocuğunu gösterebilir."},{"facet_id":"F004","role":"extension","statement":"Kadın biçimi kadın köleyi gösterir ve bu kullanım ileri yaşta da geçerli olabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Erkek ve kadın köle anlamlarını, ayrıca yaştan bağımsız kadın köle kullanımını kaybeder.","preserves":"Yakın zamanda doğmuş küçük çocuk yönünü korur."},"text":"bebek"},{"category":"confusable","error_profile":{"adds":"Özgür ve ücretli çalışanları da kapsama sokabilir.","collision":"Hizmet görevi ile kişinin kölelik konumunu birbirine karıştırır.","fit":"displacement","loses":"Yeni doğmuş çocuk anlamını ve kölelik konumunun açık sınırını kaybeder.","preserves":"Bir başkasına hizmet eden kişi çağrışımını kısmen korur."},"text":"hizmetçi"}],"identity_rationale":"Kaynak ifadesi erkek biçimi için yeni doğmuş çocuk, ergenlik öncesi oğlan ve erkek köleyi; kadın biçimi için kız çocuk ile kadın köleyi birlikte verir. Dal çerçevesindeki çocuk ve köle yönleri uygundur, ancak çocuk yönü yalnız yeni doğmuşlukla sınırlandırılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yeni doğmuş erkek çocuk; erkek köle"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kız çocuk; kadın köle"}],"lexicalization_note":"Tanım, yalın biçimlerin çocuk ve köle yönlerini birlikte korur; genel çocuk anlamı veya herhangi bir hizmetçilik ilişkisi içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler kadın köle, küçük yavru, gençlik adıyla köle ve genel çocuk sınırlarını açıkça karşılaştırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal çocuk ve köle yönlerini cinsiyet biçimleriyle birlikte taşır; komşu dal bu çoklu yapıdan yalnız kadın köle anlamını ayırır.","focus_only":"Bu dal erkek çocuk, özellikle yeni doğmuş çocuk veya ergenlik öncesi oğlan, kız çocuk ve erkek köleyi de kapsar.","gloss":"çocuk veya köle / kadın köle","neighbor_only":"Komşu dal yalnız kadın köle anlamına odaklanır.","neighbor_ref":"root_000053/B014","relation_type":"near_neighbor","shared_zone":"Kadın köle anlamı iki dalın doğrudan kesişimidir."},{"boundary_match":"partial","distinction":"Bu dal köle anlamına uzanır ve insan kullanımlarında kalır; komşu dal köleliği içermez, küçük olmayı hayvan yavrularına kadar genişletir.","focus_only":"Bu dal insan çocuğunun yanında erkek veya kadın köle anlamını da taşır.","gloss":"çocuk veya köle / küçük yavru","neighbor_only":"Komşu dal küçük insan çocuğuyla birlikte evcil ve yabani hayvan yavrularını da kapsar.","neighbor_ref":"root_000942/B001","relation_type":"near_neighbor","shared_zone":"Küçük insan çocuğu iki dalın kesiştiği alandır; bu dal erkek biçimde yeni doğmuş veya ergenlik öncesi oğlanı, kadın biçimde kız çocuğunu kapsar."},{"boundary_match":"partial","distinction":"Bu dalın çocuk yönü erkek biçimde yeni doğmuş veya ergenlik öncesi oğlanı, kadın biçimde kız çocuğunu kapsar; komşu dal genç kişi adlarını köle ve hizmetçi için örtülü bir söyleyiş olarak kullanır.","focus_only":"Bu dal erkek çocuk, özellikle yeni doğmuş veya ergenlik öncesi oğlan, ve kız çocuk anlamını taşır; köle kullanımını da bu adlandırma alanıyla birlikte verir.","gloss":"çocuk veya köle / genç diye anılan köle","neighbor_only":"Komşu dal genç erkek ve kız adlarını köle veya hizmetçi için örtülü biçimde kullanır.","neighbor_ref":"root_001130/B002","relation_type":"near_neighbor","shared_zone":"Erkek ve kadın kölenin yaş bildiren bir adla gösterilmesi iki dalı yaklaştırır."},{"boundary_match":"partial","distinction":"Bu dal biçime bağlı çocuk kapsamıyla köle anlamını birleştirir; komşu dal köleliği dışarıda bırakıp çocukluk bağını yaş ve sayı bakımından geniş tutar.","focus_only":"Bu dal erkek biçimde yeni doğmuş veya ergenlik öncesi oğlanı, kadın biçimde kız çocuğunu kapsar ve ayrıca köle anlamı taşır.","gloss":"çocuk veya köle / genel çocuk","neighbor_only":"Komşu dal çocuğu her yaşta, her cinsiyette ve tek ya da çok kişi olarak kapsar.","neighbor_ref":"root_001683/B001","relation_type":"near_neighbor","shared_zone":"İnsan çocuğu iki dalda da yer alır; bu dal erkek biçimde yeni doğmuş veya ergenlik öncesi oğlanı, kadın biçimde kız çocuğunu gösterir."}],"source_phrase_ar":"الوليدة الأنثى والجمع ولائد (maqayis)؛ الوليد الصبي والعبد والجمع ولدان وولدة؛ الوليد الصبية والأمة والجمع الولائد (sihah)؛ الوليد الصبي حين يولد؛ يقال للأمة وليدة وإن كانت مسنة (tahdhib)؛ الوليد يقال لمن قرب عهده بالولادة؛ الوليدة مختصة بالإماء في عامة كلامهم (mufradat)","source_summary":"Toplu kanıt erkek biçimi yeni doğmuş çocuk, ergenlik öncesi oğlan ve erkek köleye; kadın biçimi kız çocuk ile kadın köleye dağıtır. Kadın köle adlandırmasının ileri yaşta da kullanılabildiği ayrıca belirtilir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الوليد للصبي أو الغلام القريب العهد بالولادة، والوليدة للصبية أو الأمة، وما جمعه ولدان أو ولائد بحسب النص.","what_is_not_ar":"لا يدخل هنا الولد العام للصغير والكبير، ولا التليدة أو المولدة إلا إذا دل السياق على الجارية أو العبد المولود في الملك."},"support_links":["sup_29d0715678f072f17c40","sup_ff13cb8d0dabf85f3ac2"]},{"boundary":"Dal gerçek doğurma olayını değil nedene bağlı ortaya çıkmayı, sonradan oluşturulmayı, uydurulmayı ve katışıksız sayılmamayı anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001683/B005","candidate_links":[{"candidate_id":"cand_47712604fc245f2251ea","lane":"macro"},{"candidate_id":"cand_20ffed477d857859f751","lane":"macro"},{"candidate_id":"cand_88754fa993d5f8b5c6e7","lane":"macro"},{"candidate_id":"cand_d041590365f665c0313e","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:2:1","qac_word_ref":"112:3:2","surface_ar":"يَلِدْ"},{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:4:1","qac_word_ref":"112:3:4","surface_ar":"يُولَدْ"}],"gloss":"bir şeyden nedenle türeme veya sonradan oluşturulma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli söz biriminde bir şey, başka bir şeyden bir neden aracılığıyla ortaya çıkar."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sonradan oluşturulan söz bu ortaya çıkma düşüncesinin bir uzantısıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Uydurulmuş kitap ve doğrulanmamış, üretilmiş kanıt aynı niteleme alanındadır."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Katışıksız sayılmayan dil veya kişi için de bu niteleme kullanılır."}}],"root_ar":"و ل د","root_id":"root_001683","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nedene bağlı ortaya çıkma çekirdeğiyle sonradan oluşturulmuş, uydurulmuş ve katışıksız olmayan uzantıları birlikte temsil eder.","boundary_detail":"Dal gerçek doğurma olayını değil nedene bağlı ortaya çıkmayı, sonradan oluşturulmayı, uydurulmayı ve katışıksız sayılmamayı anlatır.","branch_image_ar":"شيء حاصل عن شيء أو مستحدث منه","concept_gloss":"bir şeyden nedenle türeme veya sonradan oluşturulma","contextual_glosses":[{"applicability":"Bir sonucun başka bir şeyden belirli bir nedenle çıktığı süreçlerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kaynak, neden ve ortaya çıkan sonuç arasındaki bağı korur."},"facet_ids":["F001"],"text":"bir şeyden ortaya çıkmak","usage_role":"general"},{"applicability":"Daha önce bulunmayıp sonradan üretilen bir söz veya benzeri oluşum için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sonradan ortaya çıkarılmış olma özelliğini korur."},"facet_ids":["F002"],"text":"sonradan oluşturulmuş","usage_role":"contextual"},{"applicability":"Gerçekliği bulunmayan veya doğrulanmamış kitap ve kanıt gibi örneklerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gerçek olmayıp sonradan üretilmiş olma yönünü korur."},"facet_ids":["F003"],"text":"uydurulmuş","usage_role":"contextual"}],"definition":"Belirli söz biriminde bir şeyin başka bir şeyden bir neden aracılığıyla ortaya çıkması. Buna bağlı olarak sonradan oluşturulan söz, uydurulan kitap veya kanıt ve katışıksız sayılmayan dil ya da kişi de kendi biçim ve kalıplarında nitelenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli söz biriminde bir şey, başka bir şeyden bir neden aracılığıyla ortaya çıkar."},{"facet_id":"F002","role":"extension","statement":"Sonradan oluşturulan söz bu ortaya çıkma düşüncesinin bir uzantısıdır."},{"facet_id":"F003","role":"extension","statement":"Uydurulmuş kitap ve doğrulanmamış, üretilmiş kanıt aynı niteleme alanındadır."},{"facet_id":"F004","role":"specialization","statement":"Katışıksız sayılmayan dil veya kişi için de bu niteleme kullanılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ortaya çıkışın neden bağını, sürecini ve sonradan oluşturulmuş ya da uydurulmuş nitelemelerini kaybeder.","preserves":"Başka bir şeyden ortaya çıkan son ürünü gösterir."},"text":"sonuç"},{"category":"confusable","error_profile":{"adds":"Başka bir kaynaktan türemeyen ve örneksiz başlayan oluşturma türlerini de kapsama ekler.","collision":"Bir kaynaktan nedenle türeme ile kaynaksız başlatmayı karıştırabilir.","fit":"broadening","loses":null,"preserves":"Daha önce bulunmayan bir şeyin ortaya çıkması yönünü korur."},"text":"yaratma"}],"identity_rationale":"Kaynak ifadesi bir şeyin başka bir şeyden bir nedenle ortaya çıkmasını çekirdek yapar; sonradan oluşturulmuş söz, uydurulmuş kitap veya kanıt ve katışıksız sayılmayan dil ya da kişi kullanımlarını buna bağlar. Verilen dal bu çekirdek ile uzantıları doğru biçimde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bir şeyin başka bir şeyden bir nedenle ortaya çıkması"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"sonradan oluşturulmuş, uydurulmuş veya katışıksız olmayan"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"katışıksız sayılmayan dil veya kişi"}],"lexicalization_note":"Nedene bağlı ortaya çıkma yalnız ilgili söz biriminde çekirdektir; sonradan oluşturulmuş, uydurulmuş ve katışıksız olmayan anlamlar kendi biçim ve kalıplarıyla ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen dört komşu uydurma, örneksiz başlatma, yararlı sonuç ve genel var etme karşısındaki sınırları açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın çekirdeği başka bir şeyden nedenle ortaya çıkmadır ve uydurma yalnız bir uzantıdır; komşu dal gerçeğe aykırı ürün kurmayı doğrudan merkezine alır.","focus_only":"Bu dal uydurma yanında nedene bağlı ortaya çıkmayı, sonradan oluşturulmayı ve katışıksız olmamayı kapsar.","gloss":"türeme veya sonradan üretme / düzmece kurma","neighbor_only":"Komşu dal yalan, düzmece anlatı, şiir ve ezgi gibi gerçeğe aykırı biçimde kurulmuş ürünlere yoğunlaşır.","neighbor_ref":"root_001167/B004","relation_type":"near_neighbor","shared_zone":"Uydurulmuş bir söz ya da metin iki dalın kesiştiği alandır."},{"boundary_match":"partial","distinction":"Bu dalda ortaya çıkan şeyin bir kaynağı ve nedeni vardır; komşu dalda yenilik, önceki bir örnek bulunmamasına dayanır.","focus_only":"Bu dal başka bir şeyden neden yoluyla çıkmayı ve türetilmiş olmayı temel alır.","gloss":"türeme / örneksiz başlatma","neighbor_only":"Komşu dal önceden örneği bulunmayan bir şeyi ilk kez başlatmayı veya yapmayı temel alır.","neighbor_ref":"root_000094/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da yeni bir şeyin ortaya çıkması alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dal çıkış ilişkisini ve sonradan üretilmişliği anlatır; komşu dal çıkan şeyin yararlı bir ürün veya kazanç olmasını öne çıkarır.","focus_only":"Bu dal bir şeyin başka bir şeyden çıkma sürecini ve sonradan oluşturulmuş ürünleri kapsar.","gloss":"türeme / yararlı ürün","neighbor_only":"Komşu dal ortaya çıkan yararlı sonucu ve bir şeyin verdiği ürünü öne çıkarır.","neighbor_ref":"root_000205/B003","relation_type":"near_neighbor","shared_zone":"Bir kaynaktan çıkan sonuç düşüncesi iki dalı birbirine yaklaştırır."},{"boundary_match":"partial","distinction":"Bu dal kaynak ile sonuç arasındaki türeme bağını gerektirir; komşu dal bu bağı şart koşmadan genel var etme ve başlatmayı anlatır.","focus_only":"Bu dal başka bir kaynaktan neden aracılığıyla türemeyi şart koşar ve uydurma uzantıları taşır.","gloss":"türeme / var etme","neighbor_only":"Komşu dal bir şeyi var etmeyi, başlatmayı, bulmayı ve yapıtını ortaya koymayı genel olarak kapsar.","neighbor_ref":"root_001165/B002","relation_type":"near_neighbor","shared_zone":"Yeni bir varlık veya ürünün ortaya çıkması iki dalın ortak alanıdır."}],"source_phrase_ar":"تولد الشيء عن الشيء حصل عنه (maqayis)؛ عربية مولدة ورجل مولد إذا كان عربيا غير محض (sihah)؛ المولد من الكلام مولدا إذا استحدثوه؛ كتاب مولد أي مفتعل؛ بينة مولدة وليست بمحققة (tahdhib)؛ تولد الشيء من الشيء حصوله عنه بسبب من الأسباب (mufradat)","source_summary":"Kaynakların toplu anlatımı nedene bağlı türemeyi merkeze alır; sonradan oluşturulmuş söz, uydurulmuş metin veya kanıt ve katışıksız sayılmayan dil ya da kişi bu çekirdeğin yerleşmiş uzantılarıdır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه تولد الشيء من الشيء إذا حصل عنه بسبب، والمولد من الكلام إذا استحدث، وما كان غير محض أو ناشئا في بيئة معينة مثل عربية مولدة ورجل مولد.","what_is_not_ar":"لا يدخل هنا النسل الآدمي المباشر إلا من جهة القياس العام، ولا الولادة الحسية نفسها."},"support_links":["sup_275e90aed4baeedc437d","sup_2adb47d33bb33f9e59d2","sup_65ba6ff6a2db25255487","sup_82274133c09b5f1d387d"]},{"boundary":"Dal genel benzerlik veya arkadaşlık değil, özellikle aynı yaşta olma bakımından denk kişiyi gösterir.","branch_kind":"bare","branch_ref":"root_001683/B006","candidate_links":[{"candidate_id":"cand_3be7d189f8e1be7ebd07","lane":"macro"},{"candidate_id":"cand_cb54df7ea405145b835f","lane":"macro"},{"candidate_id":"cand_af81ed11c24bc90ef3a9","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:2:1","qac_word_ref":"112:3:2","surface_ar":"يَلِدْ"},{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:4:1","qac_word_ref":"112:3:4","surface_ar":"يُولَدْ"}],"gloss":"yaşıt","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki kişi arasındaki belirleyici bağ aynı yaşta olmalarıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adın tekil, ikili ve çoğul biçimleri bir veya birden çok yaştaşı gösterebilir."}}],"root_ar":"و ل د","root_id":"root_001683","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiyle aynı yaşta olan kimseyi, başka benzerlik veya arkadaşlık şartı eklemeden karşılar.","boundary_detail":"Dal genel benzerlik veya arkadaşlık değil, özellikle aynı yaşta olma bakımından denk kişiyi gösterir.","branch_image_ar":"قرين في سن الولادة","concept_gloss":"yaşıt","contextual_glosses":[{"applicability":"Yaştaşlık ilişkisinin bir cümle içinde açıkça çözülmesi gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılaştırılan iki kişinin yaş eşitliğini açıkça korur."},"facet_ids":["F001"],"text":"onunla aynı yaşta","usage_role":"explanatory"}],"definition":"Başka bir kişiyle aynı yaşta olan kimse; yaş bakımından onun dengi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki kişi arasındaki belirleyici bağ aynı yaşta olmalarıdır."},{"facet_id":"F002","role":"source_variant","statement":"Adın tekil, ikili ve çoğul biçimleri bir veya birden çok yaştaşı gösterebilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yaş eşitliği gerektirmeyen kişisel yakınlık ve birlikte bulunma ilişkisini ekler.","collision":"Yaştaşlık ile kişisel dostluğu birbirine karıştırır.","fit":"displacement","loses":"Aynı yaşta olma şartını bütünüyle kaybeder.","preserves":"İki kişi arasında yakın bir bağ bulunduğu çağrışımını korur."},"text":"arkadaş"}],"identity_rationale":"Kaynak ifadesi bir kişiyi başka bir kişinin yaştaşı ve dengi olarak tanımlar; biçimin kökenine ve çoğul kullanımına ilişkin bilgiler de bu çekirdeği değiştirmez. Verilen dal çerçevesi yaş eşitliğini doğru biçimde merkeze alır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"yaşıt; aynı yaşta olan kimse"}],"lexicalization_note":"Tanım yalın yaştaş anlamıyla sınırlıdır; güç, tür, arkadaşlık veya genel benzerlik gibi ek ölçütler içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; yayımlanan üç komşu yaş eşitliğine arkadaşlık, güç denkliği veya genel benzerlik ekleyen sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yaş eşitliğini tek belirleyici sınır yapar; komşu dal aynı yaş çevresine arkadaşlık veya birlikte yetişme bağını da katabilir.","focus_only":"Bu dal için aynı yaşta olmak yeterlidir; birlikte büyüme veya arkadaşlık şart değildir.","gloss":"yaşıt / yaşıt ve birlikte büyüyen","neighbor_only":"Komşu dal yaş eşitliğinin yanında arkadaşlığı, yakınlığı ve birlikte büyümeyi de çağrıştırabilir.","neighbor_ref":"root_000178/B004","relation_type":"near_synonym","shared_zone":"Aynı yaşta olan iki kişi iki dalın ortak çekirdeğidir."},{"boundary_match":"partial","distinction":"Bu dal aynı yaş koşulundan ayrılmaz; komşu dal denkliği güç ve yiğitlik gibi başka karşılaştırma ölçülerine genişletir.","focus_only":"Bu dal denkliği yalnız yaş ölçüsüne göre kurar.","gloss":"yaşıt / yaşta veya güçte denk","neighbor_only":"Komşu dal yaş yanında yiğitlik, güç ve dayanıklılık bakımından denk rakibi de kapsar.","neighbor_ref":"root_001221/B003","relation_type":"near_neighbor","shared_zone":"Yaş bakımından denk kişi iki dalın kesiştiği alandır."},{"boundary_match":"partial","distinction":"Bu dal denklik ölçüsünü yaş olarak sabitler; komşu dal benzerlik ve denkliği belirli bir ölçüyle sınırlamaz.","focus_only":"Bu dal benzerliği yalnız iki kişinin aynı yaşta olmasına bağlar.","gloss":"yaşıt / genel benzer","neighbor_only":"Komşu dal yaş şartı olmadan tür, durum veya başka özelliklerde benzer ve denk olanı gösterir.","neighbor_ref":"root_000906/B008","relation_type":"near_neighbor","shared_zone":"Bir kişinin başka bir kişiye denk sayılması iki dalı yakınlaştırır."}],"source_phrase_ar":"اللدة نقصانه الواو لأن أصله ولدة (maqayis)؛ لدة الرجل تربه؛ وهما لدان والجمع لدات ولدون (sihah)؛ اللدة مختصة بالترب يقال فلان لدة فلان وتربه (mufradat)","source_summary":"Kaynakların ortak çekirdeği aynı yaşta olan denk kişidir; tekil, ikili ve çoğul biçim bilgileri bu yaştaşlık ilişkisini sayı bakımından çeşitlendirir.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه اللدة أو لدة الرجل بمعنى تربه ومثيله في السن.","what_is_not_ar":"لا يدخل هنا الولد بمعنى الابن ولا الوالد ولا التولد."},"support_links":["sup_136fe31b0a49d0faa228","sup_c34bf28f536ea0b97ab2","sup_fe093f4d486a5c43d87a"]},{"boundary":"Anlam yalnız verilen kalıp sözde geçerlidir; tek başına çocuk adını veya bu kalıp dışında kalan her büyüklük ve bolluk durumunu kapsamaz.","branch_kind":"collocation","branch_ref":"root_001683/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:2:1","qac_word_ref":"112:3:2","surface_ar":"يَلِدْ"},{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:4:1","qac_word_ref":"112:3:4","surface_ar":"يُولَدْ"}],"gloss":"çok büyük bir durum ya da pek bol bir şey","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kalıp söz çok büyük, önemli veya ağır bir durumu anlatır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı kalıp söz çok bol bir şeyi anlatmak için de kullanılır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Söyleyişin çıkışı, baskın sırasında yaşanan ağır duruma bağlanır."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Çok yiyecek ve çok otlak, bolluk yönünün açık örnekleridir."}}],"root_ar":"و ل د","root_id":"root_001683","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kanıtta verilen sabit söyleyişin anlamını karşılar; yalın bir sözcük anlamı olarak kullanılamaz.","boundary_detail":"Anlam yalnız verilen kalıp sözde geçerlidir; tek başına çocuk adını veya bu kalıp dışında kalan her büyüklük ve bolluk durumunu kapsamaz.","branch_image_ar":"أمر لا ينادى وليده","concept_gloss":"çok büyük bir durum ya da pek bol bir şey","contextual_glosses":[{"applicability":"Kalıp söz büyük, önemli ve ağır bir olay veya durum için söylendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Durumun olağanüstü büyüklük ve ağırlık derecesini korur."},"facet_ids":["F001","F003"],"text":"çok ağır bir durum","usage_role":"contextual"},{"applicability":"Kalıp söz yiyecek veya otlak gibi bir şeyin çokluğunu anlatırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir şeyin olağanüstü bolluk derecesini ilgili bağlamda korur."},"facet_ids":["F002","F004"],"text":"pek bol","usage_role":"contextual"}],"definition":"Yalnız belirli bir kalıp söz içinde, çok büyük veya ağır bir durumu ya da çok bol bir şeyi anlatır. Söyleyişin kökeni baskına bağlanır; çok yiyecek ve çok otlak bolluk örnekleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kalıp söz çok büyük, önemli veya ağır bir durumu anlatır."},{"facet_id":"F002","role":"extension","statement":"Aynı kalıp söz çok bol bir şeyi anlatmak için de kullanılır."},{"facet_id":"F003","role":"source_variant","statement":"Söyleyişin çıkışı, baskın sırasında yaşanan ağır duruma bağlanır."},{"facet_id":"F004","role":"example","statement":"Çok yiyecek ve çok otlak, bolluk yönünün açık örnekleridir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Gerçek bir çocuğun çağrılmadığı sıradan bir olayı anlamın içine ekler.","collision":"Sabit söyleyişin yerleşmiş anlamını sözcüğü sözcüğüne bir olayla karıştırır.","fit":"displacement","loses":"Çok büyük veya ağır durum ile çok bol şey bildiren yerleşmiş anlamı kaybeder.","preserves":"Kalıbın sözcük düzeyindeki çağırma ve çocuk görüntüsünü korur."},"text":"çocuk çağrılmaz"}],"identity_rationale":"Kaynak ifadesi yalnız sabit bir söyleyiş içinde çok büyük veya ağır bir durumu ve çok bol bir şeyi anlatır; kökeni baskına bağlar, yiyecek ve otlağı bolluk örnekleri olarak verir. Ön çerçevedeki süt örneği yetkili kaynak ifadesinde bulunmadığından tanım bu örneği dışarıda bırakacak biçimde yeniden kurulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"çok büyük veya ağır bir durum yahut çok bol bir şey için söylenen kalıp söz"}],"lexicalization_note":"Tanım yalnız verilen sabit söyleyişe bağlıdır; buradaki büyüklük, ağırlık ve bolluk anlamları yalın kök anlamına genellenmez.","neighbor_coverage_note":"Verilen bütün komşu adayları değerlendirildi; hiçbiri bu sabit söyleyişin büyük olay ve bolluk sınırını doğrudan paylaşmadığından yayımlanacak yararlı bir karşılaştırma bulunmadı.","source_phrase_ar":"أمر لا ينادى وليده؛ قيل ذلك لكل أمر عظيم ولكل شيء كثير (sihah)؛ هو أمر لا ينادى وليده؛ أمر جليل شديد؛ أصله في الغارة؛ طعام لا ينادى وليده؛ عشب لا ينادى وليده (tahdhib)","source_summary":"Toplu kanıt, sabit söyleyişi büyük veya ağır durum ile bolluk arasında açıklar; çıkışını baskına bağlar ve yiyecek ile otlağı bolluk örnekleri olarak verir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه المثل لا ينادى وليده وما فسرته المصادر من أمر عظيم أو شديد، أو شيء كثير، أو غارة تذهل الأم عن ولدها، أو طعام ولبن وعشب كثير لا يحتاج فيه إلى نداء الوليد.","what_is_not_ar":"لا يدخل هنا معنى الوليد المفرد خارج هذا التركيب، ولا كل شدة أو كثرة بلا هذا المثل."},"support_links":[]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000017/B001","candidate_links":[{"candidate_id":"cand_db40421a83be74842e42","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2c793329971140344a17","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Oneness and unity supply the positive frame against which multiplying lineage positions becomes incongruent.","root":"ء ح د","source_ref":"112:1","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000017","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_ee925618c6c64515cd7e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000017/B002","candidate_links":[{"candidate_id":"cand_db40421a83be74842e42","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2c793329971140344a17","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Exhaustive negation closes the domain after the focus so that no unmentioned lineage or counterpart participant remains.","root":"ء ح د","source_ref":"112:4","source_word_indices":["5"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000017","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_ee925618c6c64515cd7e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000047/B001","candidate_links":[{"candidate_id":"cand_b1c6e29f4b3f4ba943bc","lane":"macro"},{"candidate_id":"cand_4de10fe62eace07e34f4","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_01a32f975f9b9c2298cf","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Worship and the worshipped supply a distinct relational axis through which the subject is first identified.","root":"ء ل ه","source_ref":"112:1","source_word_indices":["3"]},{"hft_ref":"hft_01a32f975f9b9c2298cf","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The repeated worshipped-name immediately before the focus keeps that non-genealogical relation active as both birth directions are denied.","root":"ء ل ه","source_ref":"112:2","source_word_indices":["1"]},{"hft_ref":"hft_3a099ea35c50144f6e57","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Worship and the worshipped supply a live asymmetrical relation that need not be modeled as ownership or inherited subordination.","root":"ء ل ه","source_ref":"112:1","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000047","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_27044d6c1a701830e136","sup_29d0715678f072f17c40"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000882/B001","candidate_links":[{"candidate_id":"cand_20ffed477d857859f751","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_89a1a438ab2653082b02","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Directed recourse toward a dependable objective supplies an asymmetrical center at which dependence terminates.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000882","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_65ba6ff6a2db25255487"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000882/B002","candidate_links":[{"candidate_id":"cand_2c19842431d6276d7278","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2e4a3de081338c2ec561","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Dense solidity without a cavity supplies an image of no interior from which offspring could emerge and no interior through which the subject emerged.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000882","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_1ea4761bfcd99d1b059f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000882/B003","candidate_links":[{"candidate_id":"cand_2c19842431d6276d7278","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2e4a3de081338c2ec561","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A tightly sealing stopper supplies closure of an opening, reinforcing the image of blocked ingress and egress for birth.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000882","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_1ea4761bfcd99d1b059f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000882/B007","candidate_links":[{"candidate_id":"cand_20ffed477d857859f751","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_89a1a438ab2653082b02","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Persistence and remaining firm supply continuity that contrasts with generational replacement.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000882","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_65ba6ff6a2db25255487"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001251/B004","candidate_links":[{"candidate_id":"cand_d041590365f665c0313e","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_e11b4acb73615dc05d73","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The non-dominant split branch supplies bearing a load and rising independently; obliquely, it activates a self-standing rather than carried-or-derived reading.","root":"ق و ل","source_ref":"112:1","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001251","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_275e90aed4baeedc437d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001272/B001","candidate_links":[{"candidate_id":"cand_c27d7d8e1b77ecc928c6","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_9d5c76d9d01fee745c8d","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Producing speech by vocal utterance makes the later negations part of an enacted public saying rather than only an inward conclusion.","root":"ق و ل","source_ref":"112:1","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001272","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_9cf5708e78cbe077450c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001272/B005","candidate_links":[{"candidate_id":"cand_c27d7d8e1b77ecc928c6","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_9d5c76d9d01fee745c8d","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Saying or attributing what was not supplies the danger of fictive lineage attribution that the focus verbally blocks.","root":"ق و ل","source_ref":"112:1","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001272","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_9cf5708e78cbe077450c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001272/B016","candidate_links":[{"candidate_id":"cand_c27d7d8e1b77ecc928c6","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_9d5c76d9d01fee745c8d","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A saying that states a thing's limit makes the paired negations function as a verbal delimitation of the subject.","root":"ق و ل","source_ref":"112:1","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001272","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_9cf5708e78cbe077450c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001305/B001","candidate_links":[{"candidate_id":"cand_cb54df7ea405145b835f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a6e625f4f45e23f10482","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Matching and like-for-like correspondence supply the counterpart test applied to parent, offspring, and birth-peer positions.","root":"ك ف ء","source_ref":"112:4","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001305","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_136fe31b0a49d0faa228"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001305/B002","candidate_links":[{"candidate_id":"cand_cb54df7ea405145b835f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a6e625f4f45e23f10482","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Tilting, turning, and reversing supply a formal image for the active-to-passive flip of the same focus root.","root":"ك ف ء","source_ref":"112:4","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001305","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_136fe31b0a49d0faa228"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001332/B004","candidate_links":[{"candidate_id":"cand_4de10fe62eace07e34f4","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_3a099ea35c50144f6e57","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Submission through abasement supplies the social state that the slave-term branch brings into tension with the named worship relation.","root":"ك و ن","source_ref":"112:4","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001332","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_29d0715678f072f17c40"]}],"candidate_inventory":[{"anchor_refs":["112:3"],"branch_refs":["root_001683/B001","root_001683/B002","root_001683/B003","root_001683/B004"],"candidate_id":"cand_9cc13c6030a926737000","commentary_obligation":"review","focus_branch_refs":["root_001683/B001","root_001683/B002","root_001683/B003","root_001683/B004"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":[],"root_ids":[],"scope":"pericope","source_local_id":"A:Parents, Parturition, and Offspring","source_type":"channel","support_ids":["sup_0ae5250ace42bebf196c","sup_2505070386b259fcc144","sup_40d74c6625010ac638ba","sup_414e7aa2c5d331af2f37","sup_ff13cb8d0dabf85f3ac2"],"title":"Parents, Parturition, and Offspring","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["112:3","112:4"],"branch_refs":["root_001332/B001","root_001683/B005"],"candidate_id":"cand_47712604fc245f2251ea","commentary_obligation":"review","focus_branch_refs":["root_001683/B005"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_001332/B001"],"root_ids":[],"scope":"pericope","source_local_id":"B:Causal Products and Coming-to-be","source_type":"channel","support_ids":["sup_15373a899e6983f4a62a","sup_6a85671d3c9a94fdcf1a","sup_82274133c09b5f1d387d","sup_d2fdf7a6c9a26b013235","sup_f6c293402aab6ed1f84d"],"title":"Causal Products and Coming-to-be","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["112:3","112:4"],"branch_refs":["root_001332/B005","root_001683/B006"],"candidate_id":"cand_3be7d189f8e1be7ebd07","commentary_obligation":"review","focus_branch_refs":["root_001683/B006"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_001332/B005"],"root_ids":[],"scope":"pericope","source_local_id":"C:Coevality and Remembered Youth","source_type":"channel","support_ids":["sup_174c07130052f7513af3","sup_1d6f9dba0f68852ecf8b","sup_ac0fbf87ce4a004ef541","sup_cf45a9a22b1117ac7423","sup_fe093f4d486a5c43d87a"],"title":"Coevality and Remembered Youth","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["112:3","112:4"],"branch_refs":["root_001305/B005","root_001683/B003"],"candidate_id":"cand_18f343d1fe4e908c6e1f","commentary_obligation":"review","focus_branch_refs":["root_001683/B003"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_001305/B005"],"root_ids":[],"scope":"pericope","source_local_id":"D:Annual Birth and Alternating Yield","source_type":"channel","support_ids":["sup_2e94b5c040701d771c20","sup_3f49098278575a4cef03","sup_4bb98b6baae8f886f41e","sup_ddcd1316fccf6f46df9f","sup_fa9a8f93857fa4261471"],"title":"Annual Birth and Alternating Yield","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["112:1","112:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:3","branch_refs":["root_001272/B001","root_001272/B005","root_001272/B016","root_001683/B002"],"candidate_id":"cand_c27d7d8e1b77ecc928c6","commentary_obligation":"review","hft_ref":"hft_9d5c76d9d01fee745c8d","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_spoken_predicate_boundary","source_type":"hft","support_ids":["sup_9cf5708e78cbe077450c"],"title":"delta_spoken_predicate_boundary","trust":"legacy_unbound"},{"anchor_refs":["112:1","112:2","112:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:3","branch_refs":["root_000047/B001","root_001683/B002"],"candidate_id":"cand_b1c6e29f4b3f4ba943bc","commentary_obligation":"review","hft_ref":"hft_01a32f975f9b9c2298cf","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_worship_relation_not_birth_relation","source_type":"hft","support_ids":["sup_27044d6c1a701830e136"],"title":"delta_worship_relation_not_birth_relation","trust":"legacy_unbound"},{"anchor_refs":["112:1","112:3","112:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:3","branch_refs":["root_000017/B001","root_000017/B002","root_001683/B001","root_001683/B003"],"candidate_id":"cand_db40421a83be74842e42","commentary_obligation":"review","hft_ref":"hft_2c793329971140344a17","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_unity_exhausts_lineage","source_type":"hft","support_ids":["sup_ee925618c6c64515cd7e"],"title":"delta_unity_exhausts_lineage","trust":"legacy_unbound"},{"anchor_refs":["112:2","112:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:3","branch_refs":["root_000882/B001","root_000882/B007","root_001683/B005"],"candidate_id":"cand_20ffed477d857859f751","commentary_obligation":"review","hft_ref":"hft_89a1a438ab2653082b02","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_samad_terminal_not_relay","source_type":"hft","support_ids":["sup_65ba6ff6a2db25255487"],"title":"delta_samad_terminal_not_relay","trust":"legacy_unbound"},{"anchor_refs":["112:3","112:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:3","branch_refs":["root_001332/B001","root_001683/B003","root_001683/B005"],"candidate_id":"cand_88754fa993d5f8b5c6e7","commentary_obligation":"review","hft_ref":"hft_1e7c89846ee5691de4bf","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_no_temporal_becoming","source_type":"hft","support_ids":["sup_2adb47d33bb33f9e59d2"],"title":"delta_no_temporal_becoming","trust":"legacy_unbound"},{"anchor_refs":["112:3","112:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:3","branch_refs":["root_001305/B001","root_001305/B002","root_001683/B001","root_001683/B006"],"candidate_id":"cand_cb54df7ea405145b835f","commentary_obligation":"review","hft_ref":"hft_a6e625f4f45e23f10482","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_reversed_relation_without_counterpart","source_type":"hft","support_ids":["sup_136fe31b0a49d0faa228"],"title":"delta_reversed_relation_without_counterpart","trust":"legacy_unbound"},{"anchor_refs":["112:2","112:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:3","branch_refs":["root_000882/B002","root_000882/B003","root_001683/B003"],"candidate_id":"cand_2c19842431d6276d7278","commentary_obligation":"review","hft_ref":"hft_2e4a3de081338c2ec561","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_solid_without_birth_passage","source_type":"hft","support_ids":["sup_1ea4761bfcd99d1b059f"],"title":"outlier_solid_without_birth_passage","trust":"legacy_unbound"},{"anchor_refs":["112:3","112:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:3","branch_refs":["root_001305/B005","root_001332/B001","root_001683/B003","root_001683/B006"],"candidate_id":"cand_af81ed11c24bc90ef3a9","commentary_obligation":"review","hft_ref":"hft_ead57acb420536f2b42e","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_outside_reproductive_cycle","source_type":"hft","support_ids":["sup_c34bf28f536ea0b97ab2"],"title":"outlier_outside_reproductive_cycle","trust":"legacy_unbound"},{"anchor_refs":["112:1","112:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:3","branch_refs":["root_001251/B004","root_001683/B005"],"candidate_id":"cand_d041590365f665c0313e","commentary_obligation":"review","hft_ref":"hft_e11b4acb73615dc05d73","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_split_root_self_standing","source_type":"hft","support_ids":["sup_275e90aed4baeedc437d"],"title":"outlier_split_root_self_standing","trust":"legacy_unbound"},{"anchor_refs":["112:1","112:3","112:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:3","branch_refs":["root_000047/B001","root_001332/B004","root_001683/B004"],"candidate_id":"cand_4de10fe62eace07e34f4","commentary_obligation":"review","hft_ref":"hft_3a099ea35c50144f6e57","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_birth_and_subjection","source_type":"hft","support_ids":["sup_29d0715678f072f17c40"],"title":"outlier_birth_and_subjection","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_5d7a9b05bf4679d227bd","connection_ref":"conn_dfd04a50e3aa1620a284","note":"Immediate boundary evidence: no equal counterpart accompanies the denial of birth.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_95fb8123952e1d87204e","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"112:4","source_note":"Immediately precedes the verse by excluding generative and generated relations.","source_row_role":"ranked_review","source_target_component_ref":"112:3","source_target_components":["112:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"112:3"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"112:4","source_target_components":["112:4"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"112:4","target_evidence":{"arabic_uthmani":"وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ","ayah_ref":"112:4"},"target_ref":"112:4"},{"connection_evidence_ref":"conn_ev_b93ddc2ef1722bfbe930","connection_ref":"conn_ae1dc85e372ae586e7db","note":"Immediate unity frame for the two-sided denial in 112:3.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_505d26b117e1bfa71cf5","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"112:1","source_note":"Direct sequel: negates begetting and being begotten as boundaries for the identity in 112:1.","source_row_role":"ranked_review","source_target_component_ref":"112:3","source_target_components":["112:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"112:3"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"112:1","source_target_components":["112:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"112:1","target_evidence":{"arabic_uthmani":"قُلْ هُوَ ٱللَّهُ أَحَدٌ","ayah_ref":"112:1"},"target_ref":"112:1"},{"connection_evidence_ref":"conn_ev_ba13996f9ce41f360777","connection_ref":"conn_6ff53d856957d539c22c","note":"Immediate self-sufficiency context for the denial in 112:3.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":true,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_9806aa8bfc5e41b68acd","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"112:2","source_note":"Immediate sibling boundary on begetting and birth; indispensable for f02 and the f03 boundary reading.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"112:3","source_target_components":["112:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"112:3"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"112:2","source_target_components":["112:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"112:2","target_evidence":{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","ayah_ref":"112:2"},"target_ref":"112:2"}],"focus":{"arabic_uthmani":"لَمْ يَلِدْ وَلَمْ يُولَدْ","qac_morphemes":[{"lemma_ar":"لَم","morph_features":"STEM|POS:NEG|LEM:lam","morpheme_role":"STEM","pos":"NEG","qac_ref":"112:3:1:1","qac_word_ref":"112:3:1","root_ar":"","surface_ar":"لَمْ"},{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:2:1","qac_word_ref":"112:3:2","root_ar":"و ل د","surface_ar":"يَلِدْ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"112:3:3:1","qac_word_ref":"112:3:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"لَم","morph_features":"STEM|POS:NEG|LEM:lam","morpheme_role":"STEM","pos":"NEG","qac_ref":"112:3:3:2","qac_word_ref":"112:3:3","root_ar":"","surface_ar":"لَمْ"},{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:4:1","qac_word_ref":"112:3:4","root_ar":"و ل د","surface_ar":"يُولَدْ"}],"word_analysis_qac_refs":[["112:3:1:1"],["112:3:2:1"],["112:3:3:1"],["112:3:3:2"],["112:3:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["112:3:1","112:3:2","112:3:3","112:3:4","112:3:5"]},"focus_surface_evidence":{"arabic_uthmani":"لَمْ يَلِدْ وَلَمْ يُولَدْ","qac_morphemes":[{"lemma_ar":"لَم","morph_features":"STEM|POS:NEG|LEM:lam","morpheme_role":"STEM","pos":"NEG","qac_ref":"112:3:1:1","qac_word_ref":"112:3:1","root_ar":"","surface_ar":"لَمْ"},{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:2:1","qac_word_ref":"112:3:2","root_ar":"و ل د","surface_ar":"يَلِدْ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"112:3:3:1","qac_word_ref":"112:3:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"لَم","morph_features":"STEM|POS:NEG|LEM:lam","morpheme_role":"STEM","pos":"NEG","qac_ref":"112:3:3:2","qac_word_ref":"112:3:3","root_ar":"","surface_ar":"لَمْ"},{"lemma_ar":"وَلَدَ","morph_features":"STEM|POS:V|IMPF|PASS|LEM:walada|ROOT:wld|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"112:3:4:1","qac_word_ref":"112:3:4","root_ar":"و ل د","surface_ar":"يُولَدْ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["112:3:1:1"],["112:3:2:1"],["112:3:3:1"],["112:3:3:2"],["112:3:4:1"]],"word_analysis_refs":["112:3:1","112:3:2","112:3:3","112:3:4","112:3:5"],"word_rows":[{"analysis_record_ref":"112:3:1","analytic_gloss_range_en":"jussive negator governing the following imperfect verb, locally giving the first denial categorical scope rather than a mere report of one past non-event","analytic_root_gloss_range_en":null,"qac_refs":["112:3:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَمْ","transliteration":"lam"}},{"analysis_record_ref":"112:3:2","analytic_gloss_range_en":"active Form I begetting or generating, locally negated without an object so that outward generative sourcehood is denied absolutely","analytic_root_gloss_range_en":"birth, offspring, parentage, delivery, and generated-or-derived production; locally the active verb selects the begetting/generating branch while broader noun and derivative branches remain guardrails rather than separate active senses","qac_refs":["112:3:2:1"],"root":{"arabic":"و ل د","transliteration":"w-l-d"},"surface":{"arabic":"يَلِدْ","transliteration":"yalid"}},{"analysis_record_ref":"112:3:3","analytic_gloss_range_en":"coordinating conjunction that links two separately scoped negated verbal clauses and pivots the ayah from active sourcehood to passive originatedness","analytic_root_gloss_range_en":null,"qac_refs":["112:3:3:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"112:3:4","analytic_gloss_range_en":"second jussive negator, independently governing the passive verb and making non-origin a complete denial rather than an ellipsis after the conjunction","analytic_root_gloss_range_en":null,"qac_refs":["112:3:3:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَمْ","transliteration":"lam"}},{"analysis_record_ref":"112:3:5","analytic_gloss_range_en":"passive Form I being begotten, generated, or brought forth, locally negated as originatedness without naming any source or agent","analytic_root_gloss_range_en":"birth, offspring, parentage, delivery, generated derivation, and origin-point language; locally the passive verb selects generated-origin as the denied branch while derivative and place-or-time senses contribute bounded origin pressure","qac_refs":["112:3:4:1"],"root":{"arabic":"و ل د","transliteration":"w-l-d"},"surface":{"arabic":"يُولَدْ","transliteration":"yūlad"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":4,"missing_anchor_refs":[],"supplied_unique_anchor_count":4},"assigned_record_count":10,"assigned_records":[{"anchor_refs":["112:1","112:3"],"branch_refs":["root_001272/B001","root_001272/B005","root_001272/B016","root_001683/B002"],"candidate_id":"cand_c27d7d8e1b77ecc928c6","evidence_scope":"declared_pericope","hft_ref":"hft_9d5c76d9d01fee745c8d","item_id":"delta_spoken_predicate_boundary","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_spoken_predicate_boundary","support_id":"sup_9cf5708e78cbe077450c"},{"anchor_refs":["112:1","112:2","112:3"],"branch_refs":["root_000047/B001","root_001683/B002"],"candidate_id":"cand_b1c6e29f4b3f4ba943bc","evidence_scope":"declared_pericope","hft_ref":"hft_01a32f975f9b9c2298cf","item_id":"delta_worship_relation_not_birth_relation","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_worship_relation_not_birth_relation","support_id":"sup_27044d6c1a701830e136"},{"anchor_refs":["112:1","112:3","112:4"],"branch_refs":["root_000017/B001","root_000017/B002","root_001683/B001","root_001683/B003"],"candidate_id":"cand_db40421a83be74842e42","evidence_scope":"declared_pericope","hft_ref":"hft_2c793329971140344a17","item_id":"delta_unity_exhausts_lineage","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_unity_exhausts_lineage","support_id":"sup_ee925618c6c64515cd7e"},{"anchor_refs":["112:2","112:3"],"branch_refs":["root_000882/B001","root_000882/B007","root_001683/B005"],"candidate_id":"cand_20ffed477d857859f751","evidence_scope":"declared_pericope","hft_ref":"hft_89a1a438ab2653082b02","item_id":"delta_samad_terminal_not_relay","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_samad_terminal_not_relay","support_id":"sup_65ba6ff6a2db25255487"},{"anchor_refs":["112:3","112:4"],"branch_refs":["root_001332/B001","root_001683/B003","root_001683/B005"],"candidate_id":"cand_88754fa993d5f8b5c6e7","evidence_scope":"declared_pericope","hft_ref":"hft_1e7c89846ee5691de4bf","item_id":"delta_no_temporal_becoming","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_no_temporal_becoming","support_id":"sup_2adb47d33bb33f9e59d2"},{"anchor_refs":["112:3","112:4"],"branch_refs":["root_001305/B001","root_001305/B002","root_001683/B001","root_001683/B006"],"candidate_id":"cand_cb54df7ea405145b835f","evidence_scope":"declared_pericope","hft_ref":"hft_a6e625f4f45e23f10482","item_id":"delta_reversed_relation_without_counterpart","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_reversed_relation_without_counterpart","support_id":"sup_136fe31b0a49d0faa228"},{"anchor_refs":["112:2","112:3"],"branch_refs":["root_000882/B002","root_000882/B003","root_001683/B003"],"candidate_id":"cand_2c19842431d6276d7278","evidence_scope":"declared_pericope","hft_ref":"hft_2e4a3de081338c2ec561","item_id":"outlier_solid_without_birth_passage","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_solid_without_birth_passage","support_id":"sup_1ea4761bfcd99d1b059f"},{"anchor_refs":["112:3","112:4"],"branch_refs":["root_001305/B005","root_001332/B001","root_001683/B003","root_001683/B006"],"candidate_id":"cand_af81ed11c24bc90ef3a9","evidence_scope":"declared_pericope","hft_ref":"hft_ead57acb420536f2b42e","item_id":"outlier_outside_reproductive_cycle","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_outside_reproductive_cycle","support_id":"sup_c34bf28f536ea0b97ab2"},{"anchor_refs":["112:1","112:3"],"branch_refs":["root_001251/B004","root_001683/B005"],"candidate_id":"cand_d041590365f665c0313e","evidence_scope":"declared_pericope","hft_ref":"hft_e11b4acb73615dc05d73","item_id":"outlier_split_root_self_standing","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_split_root_self_standing","support_id":"sup_275e90aed4baeedc437d"},{"anchor_refs":["112:1","112:3","112:4"],"branch_refs":["root_000047/B001","root_001332/B004","root_001683/B004"],"candidate_id":"cand_4de10fe62eace07e34f4","evidence_scope":"declared_pericope","hft_ref":"hft_3a099ea35c50144f6e57","item_id":"outlier_birth_and_subjection","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_birth_and_subjection","support_id":"sup_29d0715678f072f17c40"}],"diagnostics":[],"lane_counts":{"global":11,"macro":10,"micro":3},"packet_summary":{"ayah_count":4,"focus_ref":"112:3","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]}],"window":["112:1","112:2","112:3","112:4"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"112:3","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":11,"source_present":true,"structured_insight_count":13,"unstructured_record_count":0},"identity":{"ayah_ref":"112:3","lane":"macro","linguistic_source_ref":"112:3","surface_ref":"112:3","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"112:3","target_tokens":[["Doğurmadı",["112:3:1","112:3:2"]],["ve",["112:3:3"]],["doğurulmadı",["112:3:3","112:3:4"]]],"text":"Doğurmadı ve doğurulmadı."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":10,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":1,"ayah_to":4,"id":"s112-p01-001-004","label":"Whole surah","number":1,"refs":["112:1","112:2","112:3","112:4"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"112:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"112:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["112:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"112:0"},{"ayah_ref":"112:1","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"112:1","root_occurrences":[{"lemmas_ar":["قَالَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ق و ل","surfaces_ar":["قُلْ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهُ"],"word_indices":["3"]},{"lemmas_ar":["أَحَد"],"occurrence_count":1,"pos_tags":["N"],"root":"ء ح د","surfaces_ar":["أَحَدٌ"],"word_indices":["4"]}],"root_sequence":["ق و ل","ء ل ه","ء ح د"],"text_ar":"قُلْ هُوَ ٱللَّهُ أَحَدٌ"}],"context_order":["112:1"],"context_root_cues":[{"root":"ق و ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"إخراج القول بالنطق"},{"branch_id":"B002","branch_image_ar":"اللسان آلة القول"},{"branch_id":"B003","branch_image_ar":"كثرة القول في صاحبه"},{"branch_id":"B004","branch_image_ar":"القيل صاحب القول النافذ"},{"branch_id":"B005","branch_image_ar":"قول ما لم يكن أو نسبته"},{"branch_id":"B006","branch_image_ar":"اجترار القول إلى النفس"},{"branch_id":"B007","branch_image_ar":"القول الفاشي بين الناس"},{"branch_id":"B008","branch_image_ar":"عود القال لضرب القلة"},{"branch_id":"B009","branch_image_ar":"المقاولة في الأمر"},{"branch_id":"B010","branch_image_ar":"اقتالة الحكم على غيره"},{"branch_id":"B011","branch_image_ar":"قول يجري مجرى الظن"},{"branch_id":"B012","branch_image_ar":"قول في النفس لم يظهر"},{"branch_id":"B013","branch_image_ar":"القول اعتقاد ومذهب"},{"branch_id":"B014","branch_image_ar":"قول الشيء دلالته"},{"branch_id":"B015","branch_image_ar":"العناية الصادقة بالشيء"},{"branch_id":"B016","branch_image_ar":"قول الشيء حده"}],"mapped_root_id":"root_001272","mapped_root_norm":"ق و ل"},{"branches":[{"branch_id":"B001","branch_image_ar":"القِلَّة والضآلة"},{"branch_id":"B002","branch_image_ar":"قُلَّة الشيء ورأسه"},{"branch_id":"B003","branch_image_ar":"القُلَّة الجرة الكبيرة"},{"branch_id":"B004","branch_image_ar":"الإقلال والاستقلال حملا ونهوضا"},{"branch_id":"B005","branch_image_ar":"القِلُّ رعدة واضطراب"},{"branch_id":"B006","branch_image_ar":"القلقلة اضطراب وتحرك"}],"mapped_root_id":"root_001251","mapped_root_norm":"ق ل ل"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ء ح د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الأَحَدِيَّة والوَحْدَة"},{"branch_id":"B002","branch_image_ar":"استغراق النفي"},{"branch_id":"B003","branch_image_ar":"الواحد في العد والتركيب"},{"branch_id":"B004","branch_image_ar":"الأول والإضافة"},{"branch_id":"B005","branch_image_ar":"الانفراد والتفرق آحادا"},{"branch_id":"B006","branch_image_ar":"جبل أُحُد"}],"mapped_root_id":"root_000017","mapped_root_norm":"ء ح د"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"112:1","surface_ref":"112:1"},{"ayah_ref":"112:2","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"112:2","root_occurrences":[{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهُ"],"word_indices":["1"]},{"lemmas_ar":["صَّمَد"],"occurrence_count":1,"pos_tags":["N"],"root":"ص م د","surfaces_ar":["صَّمَدُ"],"word_indices":["2"]}],"root_sequence":["ء ل ه","ص م د"],"text_ar":"ٱللَّهُ ٱلصَّمَدُ"}],"context_order":["112:2"],"context_root_cues":[{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ص م د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"القصد إلى المعتمد المقصود"},{"branch_id":"B002","branch_image_ar":"الصلابة المكتنزة بلا جوف"},{"branch_id":"B003","branch_image_ar":"سدادة القارورة المحكمة"},{"branch_id":"B004","branch_image_ar":"شد الرأس بصماد"},{"branch_id":"B005","branch_image_ar":"الإشراف على الأمر مع الحفل به"},{"branch_id":"B006","branch_image_ar":"إيقاع الضرب بالعصا"},{"branch_id":"B007","branch_image_ar":"الدوام والبقاء على الشدة"}],"mapped_root_id":"root_000882","mapped_root_norm":"ص م د"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"112:2","surface_ref":"112:2"},{"ayah_ref":"112:4","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"112:4","root_occurrences":[{"lemmas_ar":["كَانَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ك و ن","surfaces_ar":["يَكُن"],"word_indices":["2"]},{"lemmas_ar":["كُفُو"],"occurrence_count":1,"pos_tags":["N"],"root":"ك ف ء","surfaces_ar":["كُفُوًا"],"word_indices":["4"]},{"lemmas_ar":["أَحَد"],"occurrence_count":1,"pos_tags":["N"],"root":"ء ح د","surfaces_ar":["أَحَدٌۢ"],"word_indices":["5"]}],"root_sequence":["ك و ن","ك ف ء","ء ح د"],"text_ar":"وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ"}],"context_order":["112:4"],"context_root_cues":[{"root":"ك و ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"وقوع الشيء وحضوره في زمان"},{"branch_id":"B002","branch_image_ar":"المكان والمكانة من الكون"},{"branch_id":"B003","branch_image_ar":"الكفالة والقيام على فلان"},{"branch_id":"B004","branch_image_ar":"الخضوع بالاستكانة"},{"branch_id":"B005","branch_image_ar":"الشيخ المنسوب إلى كُنْتُ"},{"branch_id":"B006","branch_image_ar":"حالة السوء بكينة"}],"mapped_root_id":"root_001332","mapped_root_norm":"ك و ن"}]},{"root":"ك ف ء","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"المماثلة والمقابلة بالمثل"},{"branch_id":"B002","branch_image_ar":"الإمالة والقلب والصرف"},{"branch_id":"B003","branch_image_ar":"اختلاف القوافي"},{"branch_id":"B004","branch_image_ar":"كِفاء الخباء"},{"branch_id":"B005","branch_image_ar":"كفأة السنة والنتاج"}],"mapped_root_id":"root_001305","mapped_root_norm":"ك ف ء"}]},{"root":"ء ح د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الأَحَدِيَّة والوَحْدَة"},{"branch_id":"B002","branch_image_ar":"استغراق النفي"},{"branch_id":"B003","branch_image_ar":"الواحد في العد والتركيب"},{"branch_id":"B004","branch_image_ar":"الأول والإضافة"},{"branch_id":"B005","branch_image_ar":"الانفراد والتفرق آحادا"},{"branch_id":"B006","branch_image_ar":"جبل أُحُد"}],"mapped_root_id":"root_000017","mapped_root_norm":"ء ح د"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"112:4","surface_ref":"112:4"},{"ayah_ref":"1:2","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:2","root_occurrences":[{"lemmas_ar":["حَمْد"],"occurrence_count":1,"pos_tags":["N"],"root":"ح م د","surfaces_ar":["حَمْدُ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["لَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَبّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ر ب ب","surfaces_ar":["رَبِّ"],"word_indices":["3"]},{"lemmas_ar":["عَٰلَمِين"],"occurrence_count":1,"pos_tags":["N"],"root":"ع ل م","surfaces_ar":["عَٰلَمِينَ"],"word_indices":["4"]}],"root_sequence":["ح م د","ء ل ه","ر ب ب","ع ل م"],"text_ar":"ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ"}],"context_order":["1:2"],"context_root_cues":[{"root":"ح م د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الحمد خلاف الذم"},{"branch_id":"B002","branch_image_ar":"وجود الشيء محمودا"},{"branch_id":"B003","branch_image_ar":"المحمود كثير الخصال"},{"branch_id":"B004","branch_image_ar":"حماداك الغاية المحمودة"},{"branch_id":"B005","branch_image_ar":"يتحمد بالمنة"}],"mapped_root_id":"root_000355","mapped_root_norm":"ح م د"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ب ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ربوبية وملك وسيادة"},{"branch_id":"B002","branch_image_ar":"إصلاح وتربية وإتمام"},{"branch_id":"B003","branch_image_ar":"علم رباني"},{"branch_id":"B004","branch_image_ar":"ربة وجماعات كثيرة"},{"branch_id":"B005","branch_image_ar":"ربيب وربيبة ورابة"},{"branch_id":"B006","branch_image_ar":"رُبّ خاثر وإصلاح به"},{"branch_id":"B007","branch_image_ar":"لزوم وإقامة ودوام"},{"branch_id":"B008","branch_image_ar":"رباب السحاب"},{"branch_id":"B009","branch_image_ar":"شاة رُبّى وحداثة"},{"branch_id":"B010","branch_image_ar":"ربابة تجمع القداح"},{"branch_id":"B011","branch_image_ar":"ربابة عهد وميثاق"},{"branch_id":"B012","branch_image_ar":"ربة نبات"},{"branch_id":"B013","branch_image_ar":"ماء رَبَب كثير"},{"branch_id":"B014","branch_image_ar":"رَبْرَب قطيع"},{"branch_id":"B015","branch_image_ar":"حرف رب وربما"},{"branch_id":"B016","branch_image_ar":"رُبَى حاجة وعقدة ونعمة"},{"branch_id":"B017","branch_image_ar":"رباني الملاحين"}],"mapped_root_id":"root_000532","mapped_root_norm":"ر ب ب"},{"branches":[{"branch_id":"B001","branch_image_ar":"زيادة وعلو"},{"branch_id":"B002","branch_image_ar":"أرض مرتفعة"},{"branch_id":"B003","branch_image_ar":"زيادة الربا في المعاملة"},{"branch_id":"B004","branch_image_ar":"تصعد النفس وانتفاخه"},{"branch_id":"B005","branch_image_ar":"تغذية ونشوء"},{"branch_id":"B006","branch_image_ar":"نتوء أصل الفخذ"},{"branch_id":"B007","branch_image_ar":"أهل البيت من بني الأعمام"}],"mapped_root_id":"root_000537","mapped_root_norm":"ر ب و"}]},{"root":"ع ل م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"انكشاف الشيء للعارف"},{"branch_id":"B002","branch_image_ar":"أثر يميز الشيء ويهدي إليه"},{"branch_id":"B004","branch_image_ar":"شق ظاهر في الشفة العليا"},{"branch_id":"B005","branch_image_ar":"ماء كثير مجتمع في عيلم"},{"branch_id":"B006","branch_image_ar":"طائر جارح يسمى العلام"},{"branch_id":"B007","branch_image_ar":"ذكر الضباع يسمى العيلام"}],"mapped_root_id":"root_001040","mapped_root_norm":"ع ل م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:2","membership_added_ayah":true,"membership_target_surah":112,"surface_ref":"1:2"},{"ayah_ref":"1:3","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:3","root_occurrences":[{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["1","2"]}],"root_sequence":["ر ح م","ر ح م"],"text_ar":"ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"}],"context_order":["1:3"],"context_root_cues":[{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:3","membership_added_ayah":true,"membership_target_surah":112,"surface_ref":"1:3"},{"ayah_ref":"1:4","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:4","root_occurrences":[{"lemmas_ar":["مَٰلِك"],"occurrence_count":1,"pos_tags":["N"],"root":"م ل ك","surfaces_ar":["مَٰلِكِ"],"word_indices":["1"]},{"lemmas_ar":["يَوْم"],"occurrence_count":1,"pos_tags":["N"],"root":"ي و م","surfaces_ar":["يَوْمِ"],"word_indices":["2"]},{"lemmas_ar":["دِين"],"occurrence_count":1,"pos_tags":["N"],"root":"د ي ن","surfaces_ar":["دِّينِ"],"word_indices":["3"]}],"root_sequence":["م ل ك","ي و م","د ي ن"],"text_ar":"مَٰلِكِ يَوْمِ ٱلدِّينِ"}],"context_order":["1:4"],"context_root_cues":[{"root":"م ل ك","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"قوة الشيء وتماسكه"},{"branch_id":"B002","branch_image_ar":"المِلْك والتصرف"},{"branch_id":"B003","branch_image_ar":"المُلك والسلطان"},{"branch_id":"B004","branch_image_ar":"الإملاك والتزويج"},{"branch_id":"B005","branch_image_ar":"مِلاك الأمر وعِماده"},{"branch_id":"B006","branch_image_ar":"مَلَك الطريق والوادي"},{"branch_id":"B007","branch_image_ar":"الماء مَلَك الأمر"},{"branch_id":"B008","branch_image_ar":"المتقدم القائد في الحيوان"}],"mapped_root_id":"root_001444","mapped_root_norm":"م ل ك"}]},{"root":"ي و م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"وقت النهار المحدود"},{"branch_id":"B002","branch_image_ar":"مدة من الزمان"},{"branch_id":"B003","branch_image_ar":"كائنة اليوم وشدته"}],"mapped_root_id":"root_001700","mapped_root_norm":"ي و م"}]},{"root":"د ي ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الطاعة والانقياد"},{"branch_id":"B002","branch_image_ar":"الحساب والجزاء"},{"branch_id":"B003","branch_image_ar":"الدين المالي"},{"branch_id":"B004","branch_image_ar":"الإذلال والملك"},{"branch_id":"B005","branch_image_ar":"العادة والشأن"},{"branch_id":"B006","branch_image_ar":"مدينة الطاعة"},{"branch_id":"B007","branch_image_ar":"التصديق والتفويض"}],"mapped_root_id":"root_000504","mapped_root_norm":"د ي ن"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:4","membership_added_ayah":true,"membership_target_surah":112,"surface_ref":"1:4"},{"ayah_ref":"1:5","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:5","root_occurrences":[{"lemmas_ar":["عَبَدَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ع ب د","surfaces_ar":["نَعْبُدُ"],"word_indices":["2"]},{"lemmas_ar":["ٱسْتَعِينُ"],"occurrence_count":1,"pos_tags":["V"],"root":"ع و ن","surfaces_ar":["نَسْتَعِينُ"],"word_indices":["4"]}],"root_sequence":["ع ب د","ع و ن"],"text_ar":"إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ"}],"context_order":["1:5"],"context_root_cues":[{"root":"ع ب د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرق والملك"},{"branch_id":"B003","branch_image_ar":"العبادة والطاعة الخاضعة"},{"branch_id":"B004","branch_image_ar":"التعبيد والاستعباد"},{"branch_id":"B005","branch_image_ar":"التذليل والتسوية"},{"branch_id":"B006","branch_image_ar":"التكريم والتعظيم"},{"branch_id":"B007","branch_image_ar":"القوة والصلابة"},{"branch_id":"B008","branch_image_ar":"الأنفة والغضب"},{"branch_id":"B009","branch_image_ar":"قلة اللبث وسرعة العدو"},{"branch_id":"B010","branch_image_ar":"التفرق في الوجوه"},{"branch_id":"B011","branch_image_ar":"العطب والانقطاع"},{"branch_id":"B012","branch_image_ar":"صَلاءة الطيب"}],"mapped_root_id":"root_000973","mapped_root_norm":"ع ب د"}]},{"root":"ع و ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الإعانة والمظاهرة"},{"branch_id":"B002","branch_image_ar":"العَوان بين السنين"},{"branch_id":"B003","branch_image_ar":"الحرب العَوان"},{"branch_id":"B004","branch_image_ar":"النخلة العَوانة القديمة"},{"branch_id":"B005","branch_image_ar":"استواء الخلقة وتلاحق القوة"},{"branch_id":"B006","branch_image_ar":"العانة قطيع الحمر"},{"branch_id":"B007","branch_image_ar":"عانة الرجل"},{"branch_id":"B008","branch_image_ar":"النسبة إلى عانة"}],"mapped_root_id":"root_001064","mapped_root_norm":"ع و ن"},{"branches":[{"branch_id":"B001","branch_image_ar":"العين الناظرة"},{"branch_id":"B002","branch_image_ar":"المشاهدة بالعين"},{"branch_id":"B003","branch_image_ar":"عين الحفظ والرعاية"},{"branch_id":"B004","branch_image_ar":"الإصابة بالعين"},{"branch_id":"B005","branch_image_ar":"العين الجاسوسة"},{"branch_id":"B006","branch_image_ar":"منبع الماء الجاري"},{"branch_id":"B007","branch_image_ar":"عين الجلد والسقاء"},{"branch_id":"B008","branch_image_ar":"عين الشمس"},{"branch_id":"B009","branch_image_ar":"النقرة أو الموضع العيني"},{"branch_id":"B010","branch_image_ar":"عين السحاب والمطر"},{"branch_id":"B011","branch_image_ar":"النقد الحاضر"},{"branch_id":"B012","branch_image_ar":"العينة والسلف"},{"branch_id":"B013","branch_image_ar":"عين الشيء نفسه"},{"branch_id":"B014","branch_image_ar":"العين خيار الشيء"},{"branch_id":"B015","branch_image_ar":"أعيان القوم والإخوة"},{"branch_id":"B016","branch_image_ar":"سعة العين وحسنها"},{"branch_id":"B017","branch_image_ar":"العين بمعنى الناس الحاضرون"}],"mapped_root_id":"root_001069","mapped_root_norm":"ع ي ن"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:5","membership_added_ayah":true,"membership_target_surah":112,"surface_ref":"1:5"},{"ayah_ref":"1:6","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:6","root_occurrences":[{"lemmas_ar":["هَدَى"],"occurrence_count":1,"pos_tags":["V"],"root":"ه د ي","surfaces_ar":["ٱهْدِ"],"word_indices":["1"]},{"lemmas_ar":["صِرَٰط"],"occurrence_count":1,"pos_tags":["N"],"root":"ص ر ط","surfaces_ar":["صِّرَٰطَ"],"word_indices":["2"]},{"lemmas_ar":["مُّسْتَقِيم"],"occurrence_count":1,"pos_tags":["ADJ"],"root":"ق و م","surfaces_ar":["مُسْتَقِيمَ"],"word_indices":["3"]}],"root_sequence":["ه د ي","ص ر ط","ق و م"],"text_ar":"ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ"}],"context_order":["1:6"],"context_root_cues":[{"root":"ه د ي","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"دلالة بلطف إلى الطريق والحق"},{"branch_id":"B002","branch_image_ar":"جهة الأمر وسيرته وقصده"},{"branch_id":"B003","branch_image_ar":"المتقدم الهادي وأوائل الشيء"},{"branch_id":"B004","branch_image_ar":"بعثة لطف وهدية إلى ذي مودة"},{"branch_id":"B005","branch_image_ar":"الهدي المهدى إلى الحرم"},{"branch_id":"B006","branch_image_ar":"العروس المهدية إلى زوجها"},{"branch_id":"B007","branch_image_ar":"هدي الحرمة والأسير"},{"branch_id":"B008","branch_image_ar":"مشي التهادي مع الاعتماد والتمايل"},{"branch_id":"B009","branch_image_ar":"الهداء البليد الضعيف"},{"branch_id":"B010","branch_image_ar":"هدي السكون وحسن الهيئة"},{"branch_id":"B011","branch_image_ar":"إهداء الشعر ومهاداته"}],"mapped_root_id":"root_001583","mapped_root_norm":"ه د ي"}]},{"root":"ص ر ط","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الطريق المستقيم"},{"branch_id":"B002","branch_image_ar":"الغيبة في المرور والبلع"},{"branch_id":"B003","branch_image_ar":"السيف القاطع الماضي في الضربة"}],"mapped_root_id":"root_000858","mapped_root_norm":"ص ر ط"}]},{"root":"ق و م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"جماعة الناس والرجال"},{"branch_id":"B002","branch_image_ar":"انتصاب وقيام بالبدن"},{"branch_id":"B003","branch_image_ar":"عزم ونهوض إلى الأمر"},{"branch_id":"B004","branch_image_ar":"رعاية وحفظ وولاية"},{"branch_id":"B006","branch_image_ar":"مقام وإقامة في موضع"},{"branch_id":"B007","branch_image_ar":"نيابة وقيام مقام غيره"},{"branch_id":"B008","branch_image_ar":"استقامة واعتدال واستواء"},{"branch_id":"B009","branch_image_ar":"قوام وعماد ومعاش"},{"branch_id":"B010","branch_image_ar":"قيمة وتقويم وتسعير"},{"branch_id":"B011","branch_image_ar":"قامة وقوام الجسم والطول"},{"branch_id":"B012","branch_image_ar":"آلة قائمة وجزء قائم"},{"branch_id":"B013","branch_image_ar":"قيامة وبعث وقيام الساعة"},{"branch_id":"B014","branch_image_ar":"مقاومة ومنازلة"},{"branch_id":"B015","branch_image_ar":"وزن سواء ومقدار معتدل"},{"branch_id":"B016","branch_image_ar":"جمود ووقوف وكلال"},{"branch_id":"B017","branch_image_ar":"انتصاف النهار وقائم الظهيرة"},{"branch_id":"B018","branch_image_ar":"نفاق السوق"},{"branch_id":"B019","branch_image_ar":"وجع قائم بالعضو"},{"branch_id":"B020","branch_image_ar":"قوام في قوائم الشاة"},{"branch_id":"B021","branch_image_ar":"عين قائمة ذاهبة البصر"}],"mapped_root_id":"root_001273","mapped_root_norm":"ق و م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:6","membership_added_ayah":true,"membership_target_surah":112,"surface_ref":"1:6"},{"ayah_ref":"1:7","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:7","root_occurrences":[{"lemmas_ar":["صِرَٰط"],"occurrence_count":1,"pos_tags":["N"],"root":"ص ر ط","surfaces_ar":["صِرَٰطَ"],"word_indices":["1"]},{"lemmas_ar":["أَنْعَمَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ن ع م","surfaces_ar":["أَنْعَمْ"],"word_indices":["3"]},{"lemmas_ar":["غَيْر"],"occurrence_count":1,"pos_tags":["N"],"root":"غ ي ر","surfaces_ar":["غَيْرِ"],"word_indices":["5"]},{"lemmas_ar":["مَغْضُوب"],"occurrence_count":1,"pos_tags":["N"],"root":"غ ض ب","surfaces_ar":["مَغْضُوبِ"],"word_indices":["6"]},{"lemmas_ar":["ضَآلّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ض ل ل","surfaces_ar":["ضَّآلِّينَ"],"word_indices":["9"]}],"root_sequence":["ص ر ط","ن ع م","غ ي ر","غ ض ب","ض ل ل"],"text_ar":"صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ"}],"context_order":["1:7"],"context_root_cues":[{"root":"ص ر ط","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الطريق المستقيم"},{"branch_id":"B002","branch_image_ar":"الغيبة في المرور والبلع"},{"branch_id":"B003","branch_image_ar":"السيف القاطع الماضي في الضربة"}],"mapped_root_id":"root_000858","mapped_root_norm":"ص ر ط"}]},{"root":"ن ع م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"حسن الحال والنعمة"},{"branch_id":"B002","branch_image_ar":"اللين والنعومة ورفاه العيش"},{"branch_id":"B003","branch_image_ar":"مدح الشيء بنعم"},{"branch_id":"B004","branch_image_ar":"الجواب بنعم والتصديق"},{"branch_id":"B005","branch_image_ar":"مال الأنعام والإبل"},{"branch_id":"B006","branch_image_ar":"النعام والنعامة الطائر"},{"branch_id":"B007","branch_image_ar":"ما سمي نعامة تشبيها بالهيئة"},{"branch_id":"B008","branch_image_ar":"طيران النعامة وتفرق القوم"},{"branch_id":"B009","branch_image_ar":"النعامى ريح لينة"},{"branch_id":"B010","branch_image_ar":"زاد وأنعم في الفعل"},{"branch_id":"B011","branch_image_ar":"موافقة المكان وطيب المقام"},{"branch_id":"B012","branch_image_ar":"المشي على القدم وابتذالها"},{"branch_id":"B013","branch_image_ar":"نعم الله بك عينا وقرة العين"}],"mapped_root_id":"root_001525","mapped_root_norm":"ن ع م"}]},{"root":"غ ي ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الصلاح والمنفعة بالميرة والسقي والإصلاح"},{"branch_id":"B002","branch_image_ar":"الغَيْر في الدية"},{"branch_id":"B003","branch_image_ar":"تغيير الصورة أو إبدال الشيء بغيره"},{"branch_id":"B004","branch_image_ar":"الغَيْرة على الأهل"},{"branch_id":"B005","branch_image_ar":"السوى والخلاف والاستثناء والنفي"}],"mapped_root_id":"root_001119","mapped_root_norm":"غ ي ر"}]},{"root":"غ ض ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"اشتداد السخط وثورانه للانتقام"},{"branch_id":"B002","branch_image_ar":"الغضب لشخص حي أو به بعد موته"},{"branch_id":"B003","branch_image_ar":"المراغمة والمخالفة"},{"branch_id":"B004","branch_image_ar":"صلابة الصخرة وتماسكها"},{"branch_id":"B005","branch_image_ar":"غلظ الجسم وشدة الحمرة"},{"branch_id":"B006","branch_image_ar":"تورم العين وما حولها"},{"branch_id":"B007","branch_image_ar":"العبوس والضجر والعظم في وصف الحيوان أو الشخص"},{"branch_id":"B008","branch_image_ar":"جلد صلب أو مطوي كدرقة"}],"mapped_root_id":"root_001092","mapped_root_norm":"غ ض ب"}]},{"root":"ض ل ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الضلال عن الهدى والقصد"},{"branch_id":"B002","branch_image_ar":"الغيبوبة والخفاء"},{"branch_id":"B003","branch_image_ar":"فقدان الشيء"},{"branch_id":"B004","branch_image_ar":"ضياع الحفظ"},{"branch_id":"B005","branch_image_ar":"الضالّة في المضيعة"}],"mapped_root_id":"root_000913","mapped_root_norm":"ض ل ل"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:7","membership_added_ayah":true,"membership_target_surah":112,"surface_ref":"1:7"}],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Parents, Parturition, and Offspring","source_type":"channel","support_id":"sup_0ae5250ace42bebf196c","text":"The two surface verbs evoke a complete generational frame even while negating it: progenitors, delivery, its temporal threshold, and offspring. The newborn designation also reaches into household status through its use for a young female slave, carrying an age-marked term beyond the biological event.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Causal Products and Coming-to-be","source_type":"channel","support_id":"sup_15373a899e6983f4a62a","text":"A source gives rise to an outcome through biological birth, causal production, or derivation.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"C:Coevality and Remembered Youth","source_type":"channel","support_id":"sup_174c07130052f7513af3","text":"Discrete units are counted, ordered, distributed, compared by age, or arranged in recurring time.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"C:Coevality and Remembered Youth","source_type":"channel","support_id":"sup_1d6f9dba0f68852ecf8b","text":"People are positioned in time either as age-peers or through an elder’s contrast between present age and former youth.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Parents, Parturition, and Offspring","source_type":"channel","support_id":"sup_2505070386b259fcc144","text":"Parent roles, the act and timing of birth, and the resulting child form one generational scene.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"D:Annual Birth and Alternating Yield","source_type":"channel","support_id":"sup_2e94b5c040701d771c20","text":"Animal birth and agricultural or pastoral products are organized into yearly, alternating production cycles.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"D:Annual Birth and Alternating Yield","source_type":"channel","support_id":"sup_3f49098278575a4cef03","text":"112:3 `يلد`, `يولد`; 112:4 `كفوا`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Parents, Parturition, and Offspring","source_type":"channel","support_id":"sup_40d74c6625010ac638ba","text":"A source gives rise to an outcome through biological birth, causal production, or derivation.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Parents, Parturition, and Offspring","source_type":"channel","support_id":"sup_414e7aa2c5d331af2f37","text":"112:3 `يلد`, `يولد`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"D:Annual Birth and Alternating Yield","source_type":"channel","support_id":"sup_4bb98b6baae8f886f41e","text":"Discrete units are counted, ordered, distributed, compared by age, or arranged in recurring time.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Causal Products and Coming-to-be","source_type":"channel","support_id":"sup_6a85671d3c9a94fdcf1a","text":"Birth is generalized into source-to-result causation. A thing may be produced by another, a saying may be newly coined, and a person or language may emerge in a mixed or local form; the existence root supplies the outcome as an event that has come to be.","trust":"trusted"},{"branch_refs":["root_001332/B001","root_001683/B005"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"B:Causal Products and Coming-to-be","source_type":"channel","support_id":"sup_82274133c09b5f1d387d","text":"causal generation `و ل د:B005/m01`; coined speech `و ل د:B005/m02`; derived or locally formed provenance `و ل د:B005/m03`; occurrence and presence `ك و ن:B001/m01`; temporal coming-to-be `ك و ن:B001/m02`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"C:Coevality and Remembered Youth","source_type":"channel","support_id":"sup_ac0fbf87ce4a004ef541","text":"One relation synchronizes two lives at the same age, while the other folds a single life across past and present. Together they form a temporal comparison scene of co-presence and retrospection.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"C:Coevality and Remembered Youth","source_type":"channel","support_id":"sup_cf45a9a22b1117ac7423","text":"112:3 `يلد`, `يولد`; 112:4 `يكن`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Causal Products and Coming-to-be","source_type":"channel","support_id":"sup_d2fdf7a6c9a26b013235","text":"112:3 `يلد`, `يولد`; 112:4 `يكن`","trust":"trusted"},{"branch_refs":["root_001305/B005","root_001683/B003"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"D:Annual Birth and Alternating Yield","source_type":"channel","support_id":"sup_ddcd1316fccf6f46df9f","text":"animal parturition `و ل د:B003/m03`; annual crop or camel yield `ك ف ء:B005/m01`; yearly milk, wool, and offspring return `ك ف ء:B005/m02`; alternating camel birth cohorts `ك ف ء:B005/m03`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Causal Products and Coming-to-be","source_type":"channel","support_id":"sup_f6c293402aab6ed1f84d","text":"Something arises from a source, enters occurrence, and may bear the marks of innovation or mixed provenance.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"D:Annual Birth and Alternating Yield","source_type":"channel","support_id":"sup_fa9a8f93857fa4261471","text":"Reproduction becomes scheduled yield. Births, fruit, milk, wool, and offspring are reckoned by year, while dividing camels into two cohorts turns recurrence into an alternating management system.","trust":"trusted"},{"branch_refs":["root_001332/B005","root_001683/B006"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"C:Coevality and Remembered Youth","source_type":"channel","support_id":"sup_fe093f4d486a5c43d87a","text":"coeval or age-peer `و ل د:B006/m01`; elder defined by “I was in my youth” `ك و ن:B005/m01`","trust":"trusted"},{"branch_refs":["root_001683/B001","root_001683/B002","root_001683/B003","root_001683/B004"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"A:Parents, Parturition, and Offspring","source_type":"channel","support_id":"sup_ff13cb8d0dabf85f3ac2","text":"offspring or descendant `و ل د:B001/m01`; father `و ل د:B002/m01`; mother `و ل د:B002/m02`; parental pair `و ل د:B002/m03`; human parturition `و ل د:B003/m01`; impending birth `و ل د:B003/m02`; newborn child `و ل د:B004/m01`; birth-age term extended to a young female slave `و ل د:B004/m02`","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"قُلْ هُوَ ٱللَّهُ أَحَدٌ","ayah_ref":"112:1"},{"arabic_uthmani":"لَمْ يَلِدْ وَلَمْ يُولَدْ","ayah_ref":"112:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_001272/B001","root_001272/B005","root_001272/B016","root_001683/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001683","role":"Parent roles by birth give the concrete relational attribution that the commanded utterance rejects in both directions.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]},{"branch_id":"B001","mapped_root_id":"root_001272","role":"Producing speech by vocal utterance makes the later negations part of an enacted public saying rather than only an inward conclusion.","root":"ق و ل","source_ref":"112:1","source_word_indices":["1"]},{"branch_id":"B005","mapped_root_id":"root_001272","role":"Saying or attributing what was not supplies the danger of fictive lineage attribution that the focus verbally blocks.","root":"ق و ل","source_ref":"112:1","source_word_indices":["1"]},{"branch_id":"B016","mapped_root_id":"root_001272","role":"A saying that states a thing's limit makes the paired negations function as a verbal delimitation of the subject.","root":"ق و ل","source_ref":"112:1","source_word_indices":["1"]}],"changed_reading":{"after":"A publicly enacted rule against assigning either side of generative lineage to the subject.","before":"A descriptive denial of two facts about the subject."},"confidence":"medium","mechanism":"The command to utter, together with branches for attribution and definition, turns the focus from an unframed biographical report into a performed boundary on what may be said of the subject. The two birth directions identify the prohibited attribution precisely.","model_id":"delta_spoken_predicate_boundary","reader_inference":"The packet supplies vocal utterance, false attribution, definition, and the two denied birth roles; I infer that the imperative makes those negations police predication. A live alternative is that the command merely transmits content without changing its function.","status":"revised","structural_cues":["The imperative at 112:1 governs the sequence before the focus appears, placing 112:3 inside an ordered act of saying."],"trigger_roots":["ق و ل"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_spoken_predicate_boundary","source_type":"hft","support_id":"sup_9cf5708e78cbe077450c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"قُلْ هُوَ ٱللَّهُ أَحَدٌ","ayah_ref":"112:1"},{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","ayah_ref":"112:2"},{"arabic_uthmani":"لَمْ يَلِدْ وَلَمْ يُولَدْ","ayah_ref":"112:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000047/B001","root_001683/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001683","role":"Parent roles by birth supply the reciprocal family relation that is denied as a model for the named subject.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]},{"branch_id":"B001","mapped_root_id":"root_000047","role":"Worship and the worshipped supply a distinct relational axis through which the subject is first identified.","root":"ء ل ه","source_ref":"112:1","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000047","role":"The repeated worshipped-name immediately before the focus keeps that non-genealogical relation active as both birth directions are denied.","root":"ء ل ه","source_ref":"112:2","source_word_indices":["1"]}],"changed_reading":{"after":"The verse preserves worship relation while refusing to recode that relation as parenthood or offspring.","before":"The verse isolates its subject by removing family relations."},"confidence":"medium","mechanism":"Naming the subject through the worshipped relation keeps a real subject-other relation in view while the focus rejects genealogy as its grammar. The change is not from relation to isolation, but from reproductive reciprocity to worship orientation.","model_id":"delta_worship_relation_not_birth_relation","reader_inference":"The packet supplies worship relation, repeated naming, and denied parentage; I infer a contrast between two ways of relating subject and others. The alternative is that the divine name only fixes reference and contributes no relational contrast.","status":"revised","structural_cues":["The same divine name occurs in both 112:1 and 112:2, with the second occurrence immediately preceding the focus."],"trigger_roots":["ء ل ه"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_worship_relation_not_birth_relation","source_type":"hft","support_id":"sup_27044d6c1a701830e136","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"قُلْ هُوَ ٱللَّهُ أَحَدٌ","ayah_ref":"112:1"},{"arabic_uthmani":"لَمْ يَلِدْ وَلَمْ يُولَدْ","ayah_ref":"112:3"},{"arabic_uthmani":"وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ","ayah_ref":"112:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000017/B001","root_000017/B002","root_001683/B001","root_001683/B003"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001683","role":"Born offspring supplies one distinct lineage participant whose emergence from the subject is denied.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]},{"branch_id":"B003","mapped_root_id":"root_001683","role":"Birth as an event supplies the differentiating transition that would establish separate lineage positions.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]},{"branch_id":"B001","mapped_root_id":"root_000017","role":"Oneness and unity supply the positive frame against which multiplying lineage positions becomes incongruent.","root":"ء ح د","source_ref":"112:1","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000017","role":"Exhaustive negation closes the domain after the focus so that no unmentioned lineage or counterpart participant remains.","root":"ء ح د","source_ref":"112:4","source_word_indices":["5"]}],"changed_reading":{"after":"Undivided unity admits no lineage slot, and exhaustive negation leaves no one available as a concealed ascendant or descendant.","before":"No particular parent or offspring is asserted."},"confidence":"strong","mechanism":"Unity before the focus and exhaustive negation after it bracket the mirrored birth clauses. A birth relation requires distinct relata occupying source and offspring slots; the bracket closes both slots and then refuses any residual member who could fill a counterpart position.","model_id":"delta_unity_exhausts_lineage","reader_inference":"The packet supplies unity, exhaustive negation, and a two-place birth event; I infer that birth would establish distinct lineage slots and that the bracketing closes them. The alternative is that unity identifies uniqueness without itself supplying a metaphysical argument against birth.","status":"strengthened","structural_cues":["The two occurrences of أحد stand on opposite sides of the focus window, one positive in 112:1 and one inside negation in 112:4."],"trigger_roots":["ء ح د"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_unity_exhausts_lineage","source_type":"hft","support_id":"sup_ee925618c6c64515cd7e","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","ayah_ref":"112:2"},{"arabic_uthmani":"لَمْ يَلِدْ وَلَمْ يُولَدْ","ayah_ref":"112:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000882/B001","root_000882/B007","root_001683/B005"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_001683","role":"Generated or derived existence supplies the backward provenance and forward production that would make the subject one link in a chain.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]},{"branch_id":"B001","mapped_root_id":"root_000882","role":"Directed recourse toward a dependable objective supplies an asymmetrical center at which dependence terminates.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]},{"branch_id":"B007","mapped_root_id":"root_000882","role":"Persistence and remaining firm supply continuity that contrasts with generational replacement.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]}],"changed_reading":{"after":"The subject is a stable terminus of recourse, not a derived relay between an origin behind it and a successor after it.","before":"The subject has no biological lineage."},"confidence":"medium","mechanism":"The one toward whom recourse is directed and who persists under severity becomes a terminal, stable center rather than a relay in a chain of derivation and succession. Passive birth would put a source behind the subject; active begetting would put a successor beyond it. The focus blocks both extensions.","model_id":"delta_samad_terminal_not_relay","reader_inference":"The packet supplies directed recourse, persistence, derivation, and both voice directions; I infer a topology in which reliance ends at the subject rather than passing through it along lineage. A live alternative is that صمد contributes physical firmness only, without a dependency arrow.","status":"revised","structural_cues":["The صمد predicate immediately precedes the paired birth negations."],"trigger_roots":["ص م د"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_samad_terminal_not_relay","source_type":"hft","support_id":"sup_65ba6ff6a2db25255487","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَمْ يَلِدْ وَلَمْ يُولَدْ","ayah_ref":"112:3"},{"arabic_uthmani":"وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ","ayah_ref":"112:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_001332/B001","root_001683/B003","root_001683/B005"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001683","role":"Birth and delivery supply bounded events whose occurrence for or from the subject is denied.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]},{"branch_id":"B005","mapped_root_id":"root_001683","role":"Generation and derivation supply changes of provenance or status that can be tested against temporal becoming.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]},{"branch_id":"B001","mapped_root_id":"root_001332","role":"A thing's occurrence and presence in time supplies the temporal field over which the focus's denied birth states are extended.","root":"ك و ن","source_ref":"112:4","source_word_indices":["2"]}],"changed_reading":{"after":"At no temporal point does the subject come to be as a generated result or enter a generative lineage role.","before":"Two birth events did not happen."},"confidence":"medium","mechanism":"The later denial of occurrence or presence in time echoes the focus's negating construction and temporalizes its two voices. Birth and generation become states the subject never enters: neither arriving as generated nor becoming a generator in a lineage sequence.","model_id":"delta_no_temporal_becoming","reader_inference":"The packet supplies temporal occurrence and denied birth events; I infer that the echo widens event denial into non-entry into a state across time. The alternative is that يكن functions only as a local copular support for 112:4.","status":"strengthened","structural_cues":["The negating construction with يكن in 112:4 follows and formally echoes the two negated verbs in 112:3."],"trigger_roots":["ك و ن"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_no_temporal_becoming","source_type":"hft","support_id":"sup_2adb47d33bb33f9e59d2","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَمْ يَلِدْ وَلَمْ يُولَدْ","ayah_ref":"112:3"},{"arabic_uthmani":"وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ","ayah_ref":"112:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_001305/B001","root_001305/B002","root_001683/B001","root_001683/B006"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001683","role":"Born offspring supplies the counterpart produced when the birth relation is read outward from the subject.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]},{"branch_id":"B006","mapped_root_id":"root_001683","role":"A same-birth-age peer supplies the latent comparison class that the later denial of an equivalent sharpens.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]},{"branch_id":"B001","mapped_root_id":"root_001305","role":"Matching and like-for-like correspondence supply the counterpart test applied to parent, offspring, and birth-peer positions.","root":"ك ف ء","source_ref":"112:4","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_001305","role":"Tilting, turning, and reversing supply a formal image for the active-to-passive flip of the same focus root.","root":"ك ف ء","source_ref":"112:4","source_word_indices":["4"]}],"changed_reading":{"after":"The verse turns one relation around the subject and cancels it in both orientations, leaving neither reciprocal counterpart nor birth-defined peer.","before":"The two clauses list unrelated absences of child and parent."},"confidence":"medium","mechanism":"The focus itself flips the same relation from active to passive. The context branches for like-for-like correspondence and turning-over make that grammatical reversal visible as a relational test: whichever way the birth relation is turned, no matching counterparty appears.","model_id":"delta_reversed_relation_without_counterpart","reader_inference":"The packet supplies reversal, equivalence, peerhood, and the mirrored voice pair; I infer that syntax enacts a flipped-relation test whose two orientations both fail. The alternative is that the voice symmetry is rhetorical and the reversal branch has no semantic force here.","status":"strengthened","structural_cues":["Words 2 and 4 of the focus mirror one root across active and passive voice, and the following ayah denies a counterpart."],"trigger_roots":["ك ف ء"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_reversed_relation_without_counterpart","source_type":"hft","support_id":"sup_136fe31b0a49d0faa228","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","ayah_ref":"112:2"},{"arabic_uthmani":"لَمْ يَلِدْ وَلَمْ يُولَدْ","ayah_ref":"112:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000882/B002","root_000882/B003","root_001683/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001683","role":"Birth and delivery supply the passage-event that the material images recast spatially.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]},{"branch_id":"B002","mapped_root_id":"root_000882","role":"Dense solidity without a cavity supplies an image of no interior from which offspring could emerge and no interior through which the subject emerged.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000882","role":"A tightly sealing stopper supplies closure of an opening, reinforcing the image of blocked ingress and egress for birth.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]}],"changed_reading":{"after":"In a contained material image, there is no cavity or passage by which another emerges from the subject or the subject emerges from another.","before":"No genealogical relation exists."},"confidence":"exploratory","containment":"This is surprising because it maps compact solidity and a sealed vessel onto bodily delivery. It remains anchored through the focus branch for birth as an event and the immediately preceding material branches of صمد. Downstream prose should present it only as a material analogy activated by the packet, not as a lexical gloss or an anatomical claim.","focus_anchor":"The focus denies birth as an event in both active and passive orientations.","outlier_id":"outlier_solid_without_birth_passage"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_solid_without_birth_passage","source_type":"hft","support_id":"sup_1ea4761bfcd99d1b059f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَمْ يَلِدْ وَلَمْ يُولَدْ","ayah_ref":"112:3"},{"arabic_uthmani":"وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ","ayah_ref":"112:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_001305/B005","root_001332/B001","root_001683/B003","root_001683/B006"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001683","role":"Birth as an event supplies reproduction as the transition by which a new generation appears.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]},{"branch_id":"B006","mapped_root_id":"root_001683","role":"A same-birth-age peer supplies the cohort created by recurrence of birth within a cycle.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]},{"branch_id":"B001","mapped_root_id":"root_001332","role":"Occurrence in time supplies the temporal dimension needed for recurring generations.","root":"ك و ن","source_ref":"112:4","source_word_indices":["2"]},{"branch_id":"B005","mapped_root_id":"root_001305","role":"The turn of a year and its produce supply a recurrent yield-cycle against which the focus's nonparticipation in reproductive succession can be pictured.","root":"ك ف ء","source_ref":"112:4","source_word_indices":["4"]}],"changed_reading":{"after":"Exploratorily, the subject stands outside recurrent cycles that produce, date, and replace one generation with another.","before":"The subject lacks a family line."},"confidence":"exploratory","containment":"This is surprising because the annual-turn and produce branch is remote from the ordinary counterpart sense in 112:4. It remains packet-licensed and focus-anchored through birth-event and birth-cohort branches, with temporal occurrence as a bridge. Downstream prose should call it a seasonal or ecological analogy, not the direct meaning of the focus or of كفوا.","focus_anchor":"The paired focus verbs deny both entering a generation by birth and issuing a later generation.","outlier_id":"outlier_outside_reproductive_cycle"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_outside_reproductive_cycle","source_type":"hft","support_id":"sup_c34bf28f536ea0b97ab2","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"قُلْ هُوَ ٱللَّهُ أَحَدٌ","ayah_ref":"112:1"},{"arabic_uthmani":"لَمْ يَلِدْ وَلَمْ يُولَدْ","ayah_ref":"112:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_001251/B004","root_001683/B005"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_001683","role":"Generated or derived existence supplies the provenance relation against which self-standing can contrast.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]},{"branch_id":"B004","mapped_root_id":"root_001251","role":"The non-dominant split branch supplies bearing a load and rising independently; obliquely, it activates a self-standing rather than carried-or-derived reading.","root":"ق و ل","source_ref":"112:1","source_word_indices":["1"]}],"changed_reading":{"after":"As a deliberately contained split-root echo, the subject is not carried into derived being by another but stands without transferred provenance.","before":"The subject was not biologically born."},"confidence":"exploratory","containment":"This is surprising because it uses the packet's non-dominant ق ل ل mapping for the surface قل, not the surface's normal contextual root sense. It remains a permitted split-root activation and returns to the focus through the generated-or-derived branch. Downstream prose must label it a mapping-induced echo, never a translation of قل.","focus_anchor":"The passive focus verb can be tested as derivation from another, while the active verb tests production of another.","outlier_id":"outlier_split_root_self_standing"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_split_root_self_standing","source_type":"hft","support_id":"sup_275e90aed4baeedc437d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"قُلْ هُوَ ٱللَّهُ أَحَدٌ","ayah_ref":"112:1"},{"arabic_uthmani":"لَمْ يَلِدْ وَلَمْ يُولَدْ","ayah_ref":"112:3"},{"arabic_uthmani":"وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ","ayah_ref":"112:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000047/B001","root_001332/B004","root_001683/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001683","role":"A young born one or slave term supplies a form-distant overlap between birth status, youth, and social dependency.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]},{"branch_id":"B001","mapped_root_id":"root_000047","role":"Worship and the worshipped supply a live asymmetrical relation that need not be modeled as ownership or inherited subordination.","root":"ء ل ه","source_ref":"112:1","source_word_indices":["3"]},{"branch_id":"B004","mapped_root_id":"root_001332","role":"Submission through abasement supplies the social state that the slave-term branch brings into tension with the named worship relation.","root":"ك و ن","source_ref":"112:4","source_word_indices":["2"]}],"changed_reading":{"after":"As a form-distant social echo, it also resists imagining the subject as born into subjection or as producing dependents whose relation is ownership-like.","before":"The focus denies biological reproduction."},"confidence":"exploratory","containment":"This is surprising because the youth-or-slave sense belongs to a form-distant nominal branch while the focus uses birth verbs. It remains anchored in the packet's و ل د inventory and is activated by separate worship and subjection branches. Downstream prose should retain it only as a social-relation resonance distinguishing worship from ownership or inherited dependency, not as the clause's lexical meaning.","focus_anchor":"Both focus verbs use the root whose inventory includes a young born person or slave term.","outlier_id":"outlier_birth_and_subjection"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_birth_and_subjection","source_type":"hft","support_id":"sup_29d0715678f072f17c40","trust":"legacy_unbound"}]}
</lane_packet_json>
