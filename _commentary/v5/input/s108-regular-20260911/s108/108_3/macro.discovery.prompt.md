# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **108:3**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s108-regular-20260911/s108/108_3/macro.discovery.json` and modify nothing
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
  "ayah_ref": "108:3",
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
{"analysis_context":{"analysis_id":"s108-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"108:3","host_surah":108,"lane_context_refs":["108:0","108:1","108:2","1:2","1:3","1:4","1:5","1:6","1:7"],"ordered_context_refs":["108:0","108:1","108:2","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, fiziksel veya dogrudan kesme-koparma cekirdegindedir; soy, itibar, acilis eksigi ve akrabalik kopusu ayri dallardir.","branch_kind":"mixed_non_bare","branch_ref":"root_000080/B001","candidate_links":[{"candidate_id":"cand_7dd89cf2b1d9006b91f3","lane":"macro"},{"candidate_id":"cand_fa682536bb92a87acd69","lane":"macro"},{"candidate_id":"cand_7ddcda5da4144d111e47","lane":"macro"},{"candidate_id":"cand_86938f2928d0cebcf722","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَبْتَر","morph_features":"STEM|POS:N|LEM:>abotar|ROOT:btr|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"108:3:4:2","qac_word_ref":"108:3:4","surface_ar":"أَبْتَرُ"}],"gloss":"tamamlanmadan kesip koparma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir seyin tam olmadan kesilmesi veya kesme isleminin kokten ayirma sonucuna varmasi esastir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuyruk ve benzeri bir parcanin koparilip kesilmesi bu cekirdegin belirgin uygulamasidir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kesen kilic nitelemesi, kesme gucunu araca yukleyen bagli bir kullanimdir."}}],"root_ar":"ب ت ر","root_id":"root_000080","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel kesme cekirdegini, kokten ayirma sonucunu ve kesici arac nitelemesini birlikte tasir.","boundary_detail":"Dal, fiziksel veya dogrudan kesme-koparma cekirdegindedir; soy, itibar, acilis eksigi ve akrabalik kopusu ayri dallardir.","branch_image_ar":"قطع الشيء قبل تمامه","concept_gloss":"tamamlanmadan kesip koparma","contextual_glosses":[{"applicability":"Kuyruk veya benzeri bir parcanin kesilip ayrildigi baglamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel tamamlanmadan kesme alanini yalniz kuyruk benzeri parcalara daraltir.","preserves":"Kesme ve koparma sonucunu korur."},"facet_ids":["F002"],"text":"kuyrugunu kesip koparmak","usage_role":"contextual"},{"applicability":"Kilic gibi kesici aracin nitelendigi baglamlarda kullanilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Seyin kendisinin tamamlanmadan kesilmesi cekirdegini arka plana iter.","preserves":"Kesme gucu ve arac nitelemesini korur."},"facet_ids":["F003"],"text":"keskin, kesip gecen kilic","usage_role":"contextual"}],"definition":"Bir seyi tamamlanmadan ya da parcasini kokten ayiracak bicimde kesip koparmadir; bunun sonucu olarak kesilme veya kesen arac nitelemesi de bu cekirdege baglidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir seyin tam olmadan kesilmesi veya kesme isleminin kokten ayirma sonucuna varmasi esastir."},{"facet_id":"F002","role":"specialization","statement":"Kuyruk ve benzeri bir parcanin koparilip kesilmesi bu cekirdegin belirgin uygulamasidir."},{"facet_id":"F003","role":"associated_use","statement":"Kesen kilic nitelemesi, kesme gucunu araca yukleyen bagli bir kullanimdir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Soy veya itibar alanini ekler.","collision":"Bu anlam ayri dalin konusudur.","fit":"displacement","loses":"Fiziksel kesme ve parca koparma cekirdegini kaybeder.","preserves":"Kesilme imgesinden gelen kopus fikrini korur."},"text":"soyu kesilmis"}],"identity_rationale":"Kaynak ifadesi, bir seyi tamamlanmadan kesmeyi, kesilme durumunu, ozellikle kuyruk benzeri bir parcayi kokten ayirmayi ve kesen kilic nitelemesini birlikte verir. Saglanan dal cercevesi bu fiziksel kesme ve koparma cekirdegini dogru temsil eder; sosyal soy, hayir, soz acilisi ve akrabalik kullanimlari bu dalin kapsamina alinmamalidir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir seyi tamamlanmadan kesmek veya kokten koparmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kuyruk gibi bir parcayi kesip koparma"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"kesilip kopma, ayrilma"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"keskin, kesip gecen kilic"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kuyrugu kesilmis"}],"lexicalization_note":"Ciplak kesme anlamini, kuyruk gibi parcalara ve kesen kilic tamlamasina bagli kullanimlardan ayirarak tanimlar.","neighbor_coverage_note":"En yararli ayrimlar fiziksel kesme, soyut kesilme ve akrabalik kopusu arasindadir; diger kesme komsulari ayni genel alani tekrarlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda kesme maddi bir nesneye, parcaya veya kesici araca baglidir; komsu dalda ise nesil, anilma veya hayir etkisi gibi sosyal ve soyut sureklilikler kesilir.","focus_only":"Fiziksel bir seyin ya da parcanin kesilip koparilmasini anlatir.","gloss":"fiziksel kesme ile soy-etki kesilmesi","neighbor_only":"Soy, ad, hayir veya etki alaninda kaliciligin kesilmesini anlatir.","neighbor_ref":"root_000080/B002","relation_type":"near_neighbor","shared_zone":"Ikisinde de bir devam surecinin kesilmesi veya tamamlanmadan kalmasi vardir."},{"boundary_match":"field_only","distinction":"Bu dal nesne uzerindeki kesme eylemini veya kesici nitelemeyi verir; komsu dal, sosyal yukumluluk alaninda akrabalik bagini kesen kisiye ozgudur.","focus_only":"Nesnenin veya parcanin kesilmesi fiziksel cekirdektir.","gloss":"nesne kesme ile akrabalik koparma","neighbor_only":"Kisi kendi akrabalik bagini koparan fail olarak nitelenir.","neighbor_ref":"root_000080/B004","relation_type":"same_field","shared_zone":"Her iki dal koparma imgesini kullanir."},{"boundary_match":"partial","distinction":"Komsu dal daha genel bir kokten kesme alanina sahiptir; bu dal tamam olmadan kesme, kuyruk benzeri parca ve kesen kilic kullanimlariyla sinirlidir.","focus_only":"Tamamlanmadan kesme ve kuyruk gibi parcanin kesilmesi ozellikle belirtilir.","gloss":"kokten kesme","neighbor_only":"Kokten kesme ve hadim etme gibi daha genis koparma uygulamalarini kapsar.","neighbor_ref":"root_000214/B001","relation_type":"near_synonym","shared_zone":"Ikisi de bir seyi kesip aslindan ayirma alaninda bulusur."}],"source_phrase_ar":"بترت الشيء بترا قطعته قبل الإتمام (sihah); الانبتار الانقطاع (sihah); البتر قطع الذنب ونحوه إذا استأصلته (tahdhib); البتر استئصال القطع (tahdhib); سيف باتر وبتار قطاع (tahdhib); يستعمل في قطع الذنب (mufradat); أصل واحد وهو القطع قبل أن تتمه، والسيف الباتر القطاع (maqayis)","source_summary":"Kaynaklar, bu dali kesme ve koparma cekirdeginde toplar: seyin tamamlanmadan kesilmesi, kuyruk gibi bir parcanin kokten ayrilmasi, kesilme durumu ve kesen kilic nitelemesi ayni alana baglanir.","sources":["SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه بتر الشيء وقطعه قبل الإتمام، والانبتار والانقطاع، وقطع الذنب ونحوه باستئصال، والسيف الباتر أو البتار القاطع","what_is_not_ar":"لا يدخل فيه انقطاع العقب والذكر والخير، ولا خطبة أو أمر ناقص الافتتاح، ولا قطع الرحم، ولا البتيراء للشمس أو وقت الضحى، ولا بحتر المركب من بتر وحتر"},"support_links":["sup_1cd967015b08216ed1f4","sup_3e5f5601c4e099e3207c","sup_e7edf6676a6d0470ba4d","sup_fc287cfced1a3677c692"]},{"boundary":"Dal, soy, anilma ve hayir etkisinin kesilmesiyle ilgilidir; maddi kesme veya akrabalik bagini bilerek koparma degildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000080/B002","candidate_links":[{"candidate_id":"cand_992e44dc4e2f7c847564","lane":"macro"},{"candidate_id":"cand_63a150ab0ea61644e363","lane":"macro"},{"candidate_id":"cand_20d3e6a98f8ea91a473b","lane":"macro"},{"candidate_id":"cand_3b48b16627f3d533a3fb","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَبْتَر","morph_features":"STEM|POS:N|LEM:>abotar|ROOT:btr|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"108:3:4:2","qac_word_ref":"108:3:4","surface_ar":"أَبْتَرُ"}],"gloss":"soyu veya iyi etkisi kesilmis olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Soyun veya ardil neslin bulunmamasi dalin temel kullanimidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kisinin anilma izi ya da hayirla bagli etkisi kesilmis sayilabilir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hayri az gorulen iki varlik icin kullanilan ikili adlandirma bu degerlendirmeye ornektir."}}],"root_ar":"ب ت ر","root_id":"root_000080","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Soy, anilma izi ve hayir etkisinin devam etmedigi soyut kullanimlari kapsar.","boundary_detail":"Dal, soy, anilma ve hayir etkisinin kesilmesiyle ilgilidir; maddi kesme veya akrabalik bagini bilerek koparma degildir.","branch_image_ar":"انقطاع العقب والذكر والخير","concept_gloss":"soyu veya iyi etkisi kesilmis olma","contextual_glosses":[{"applicability":"Cocugu veya ardil nesli bulunmayan kisi icin dogaldir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Anilma, hayir etkisi ve islerin olumlu sonucunun kesilmesi alanlarini disarida birakir.","preserves":"Soyun devam etmemesi anlamini korur."},"facet_ids":["F001"],"text":"soyu kalmamis","usage_role":"contextual"},{"applicability":"Hayir etkisi veya olumlu sonucu kesilmis kisi ya da is icin uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Soyun bulunmamasi anlamini kapsamaz.","preserves":"Hayir etkisinin kesilmesini korur."},"facet_ids":["F002","F003"],"text":"iyi izi kalmayan","usage_role":"contextual"}],"definition":"Bir kisi, is veya durum icin soyun, anilmanin ya da hayir etkisinin devam etmemesi; ardil iz veya olumlu sonucun kesilmis sayilmasidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Soyun veya ardil neslin bulunmamasi dalin temel kullanimidir."},{"facet_id":"F002","role":"extension","statement":"Kisinin anilma izi ya da hayirla bagli etkisi kesilmis sayilabilir."},{"facet_id":"F003","role":"example","statement":"Hayri az gorulen iki varlik icin kullanilan ikili adlandirma bu degerlendirmeye ornektir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Fiziksel parca kesme anlamini ekler.","collision":"Bu anlam baska dalin fiziksel kesme alanidir.","fit":"displacement","loses":"Soy, anilma ve hayir etkisi alanini kaybeder.","preserves":"Kesilmislik imgesini korur."},"text":"kuyrugu kesilmis"}],"identity_rationale":"Kaynak ifadesi, cocuk veya ardil soyun bulunmamasini, kisinin anilma izinin ya da hayir etkisinin kesilmesini ve kimi kaliplarda hayrinin az gorulmesini birlikte verir. Dal cercevesi bu soyut ve toplumsal kesilme alanini fiziksel kesmeden ayri tutarak dogru sinirlar.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"soyu, adi veya hayir etkisi kesilmis"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"hayri az sayilan iki varlik"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"hayir etkisi kesilmis is"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"onu soyu veya iyi izi kesilmis duruma getirdi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"hayirla anilmasi kesilmis adam"}],"lexicalization_note":"Hem niteleyici bicimler hem kalipli kullanimlar vardir; tanim bunlari soy ve etki kesilmesi cekirdeginde ayri tutar.","neighbor_coverage_note":"Yayimlanan komsular soy ve iz devami ekseninde siniri aciklar; diger adaylar nesil, bereket veya sohrete ait daha dolayli alanlardir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal, kisinin ardinda soy veya iyi iz birakmamasini anlatir; komsu dal maddi nesne veya parcanin kesilmesine dayanir.","focus_only":"Soy, ad ve hayir etkisi gibi soyut devamlar kesilir.","gloss":"soyut devam kesilmesi","neighbor_only":"Nesne veya parca fiziksel olarak kesilip koparilir.","neighbor_ref":"root_000080/B001","relation_type":"near_neighbor","shared_zone":"Ikisinde de bir surekliligin kesilmesi imgesi bulunur."},{"boundary_match":"opposed","distinction":"Bu dal soy devam etmeyince kullanilir; komsu dal ise devam eden ardil soyu ve nesli adlandirir.","focus_only":"Ardil soyun yoklugu veya kesilmisligi vurgulanir.","gloss":"soy yoklugu ile soy devami","neighbor_only":"Kisiden sonra kalan cocuk ve soy zinciri adlandirilir.","neighbor_ref":"root_001033/B004","relation_type":"polarity_pair","shared_zone":"Her iki dal insanin ardindan gelen nesil alanindadir."},{"boundary_match":"opposed","distinction":"Bu dal olumlu izin kalmamasini belirtir; komsu dal ise bir izin veya hatiranin birakilmasini anlatir.","focus_only":"Anilma veya hayir etkisinin kesilmesi esastir.","gloss":"iz kesilmesi ile iz birakma","neighbor_only":"Kisiden sonra iyi bir iz veya kalinti birakilmasi esastir.","neighbor_ref":"root_000180/B002","relation_type":"polarity_pair","shared_zone":"Ikisi de kisiden veya isten sonra kalan etki alanini paylasir."}],"source_phrase_ar":"الأبتر الذي لا عقب له (sihah); كل أمر انقطع من الخير أثره فهو أبتر (sihah); الأبتران العبد والعير لقلة خيرهما (sihah); المنقطع العقب والمنقطع عنه كل خير (tahdhib); أجري قطع العقب مجراه فقيل فلان أبتر إذا لم يكن له عقب (mufradat); إن شانئك هو الأبتر أي المقطوع الذكر (mufradat); الرجل الذي لا عقب له أبتر وكل من انقطع من الخير أثره فهو أبتر (maqayis)","source_summary":"Kaynaklar, bu dali soyun bulunmamasi, anilma veya hayir etkisinin kesilmesi ve olumlu iz birakmayan is ya da kisi nitelemesi etrafinda birlestirir.","sources":["SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الأبتر لمن لا عقب له، ومن انقطع ذكره أو أثر الخير عنه، وما قيل في الأبترين لقلة خيرهما","what_is_not_ar":"لا يدخل فيه القطع الحسي للشيء أو الذنب، ولا قطع الرحم اختيارا، ولا نقص افتتاح الخطبة أو الأمر"},"support_links":["sup_1ccd806eec605431df6e","sup_3d30bf2c82237f8654ee","sup_6be6f7c55a3adad4460a","sup_871c90aae6b44e686c5a"]},{"boundary":"Dal yalniz eksik baslangicli soz veya is kalibidir; genel hayir kesilmesi ya da fiziksel kesme degildir.","branch_kind":"collocation","branch_ref":"root_000080/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَبْتَر","morph_features":"STEM|POS:N|LEM:>abotar|ROOT:btr|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"108:3:4:2","qac_word_ref":"108:3:4","surface_ar":"أَبْتَرُ"}],"gloss":"eksik acilisli soz veya is","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Beklenen kutsal acilis anmasinin bulunmamasi, soz veya isin eksik baslamasina yol acar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Toplu hitapta ovgu ve dua ile acmamak bu nitelemenin belirgin ornegidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ayni degerlendirme, Tanri anmasiyla baslanmayan islere de kalipli olarak uygulanir."}}],"root_ar":"ب ت ر","root_id":"root_000080","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Beklenen dini acilis anmasi yapilmadan baslayan hitap veya is kaliplari icindir.","boundary_detail":"Dal yalniz eksik baslangicli soz veya is kalibidir; genel hayir kesilmesi ya da fiziksel kesme degildir.","branch_image_ar":"بتر افتتاح الكلام والعمل","concept_gloss":"eksik acilisli soz veya is","contextual_glosses":[{"applicability":"Toplu hitabin beklenen ovgu ve dua acilisindan yoksun kaldigi baglamlarda dogaldir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel is kalibini kapsamaz.","preserves":"Hitap acilisindaki eksikligi korur."},"facet_ids":["F002"],"text":"duasiz baslayan hitap","usage_role":"contextual"},{"applicability":"Bir isin beklenen anmayla baslamadigi genel kalipta kullanilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Toplu hitap ozelindeki ovgu ve dua ayrintisini disarida birakir.","preserves":"Baslangicta anmanin eksik olmasini korur."},"facet_ids":["F003"],"text":"Tanri anmasiz baslayan is","usage_role":"contextual"}],"definition":"Bir konusma, toplu hitap veya is, beklenen kutsal acilis anmasi yapilmadan basladiginda eksik acilisli sayilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Beklenen kutsal acilis anmasinin bulunmamasi, soz veya isin eksik baslamasina yol acar."},{"facet_id":"F002","role":"specialization","statement":"Toplu hitapta ovgu ve dua ile acmamak bu nitelemenin belirgin ornegidir."},{"facet_id":"F003","role":"extension","statement":"Ayni degerlendirme, Tanri anmasiyla baslanmayan islere de kalipli olarak uygulanir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kaynakta olmayan herhangi bir yarim kalmislik veya tamamlanmamislik alanini ekler.","collision":"Dal, isin bitmemesine degil baslangic unsurunun eksikligine baglidir.","fit":"broadening","loses":null,"preserves":"Eksiklik fikrini korur."},"text":"yarim kalmis is"}],"identity_rationale":"Kaynak ifadesi, belirli bir konusma acilisinin Tanriyi anma ve peygambere dua gibi unsurlari icermemesiyle eksik sayilmasini ve daha genel olarak ise Tanri anmasiyla baslanmamasini verir. Bu dal, eksik acilisli soz veya is kalibina bagli tutuldugunda kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ovgu ve dua ile acilmamis hitap"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"Tanri anmasiyla baslamayan is eksik sayilir"}],"lexicalization_note":"Anlam belirli acilis eksikligi kaliplarina baglidir; ciplak bir kesme veya genel eksiklik anlamina genisletilmez.","neighbor_coverage_note":"Komsular arasinda en belirgin sinir, hitap alanindaki genel soz ile bu dalin eksik acilis kosulu arasindadir.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal hitabin yapisindaki eksik acilis kosuluna baglidir; komsu dal konusma ve hitap eyleminin kendisini kapsar.","focus_only":"Hitabin beklenen acilis anmasi olmadan baslamasini niteler.","gloss":"eksik acilisli hitap ile hitap","neighbor_only":"Konusma, hitap ve hitap edilen soz alanini genel olarak adlandirir.","neighbor_ref":"root_000421/B001","relation_type":"same_field","shared_zone":"Ikisi de soz ve toplu hitap alanindadir."},{"boundary_match":"partial","distinction":"Bu dal baslangic kosuluna bagli kalipli bir nitelemedir; komsu dal soy ve hayir etkisinin devam etmemesini anlatir.","focus_only":"Baslangicta beklenen anma eksik oldugu icin soz veya is eksik sayilir.","gloss":"acilis eksigi ile iyi iz kesilmesi","neighbor_only":"Soy, ad veya hayir etkisi kesildigi icin kisi ya da is olumlu izsiz sayilir.","neighbor_ref":"root_000080/B002","relation_type":"near_neighbor","shared_zone":"Ikisi de eksiklik veya hayir etkisinin kaybi imgesini kullanabilir."},{"boundary_match":"partial","distinction":"Bu dal kalipli ve soyut bir acilis eksigidir; komsu dal maddi kesme cekirdegine aittir.","focus_only":"Soz veya is, beklenen acilis unsuru olmadigi icin eksik nitelenir.","gloss":"acilis eksigi ile fiziksel kesme","neighbor_only":"Nesne veya parca fiziksel olarak kesilip koparilir.","neighbor_ref":"root_000080/B001","relation_type":"near_neighbor","shared_zone":"Eksik veya kesilmis sayilma imgesi ortak olabilir."}],"source_phrase_ar":"خطب زياد خطبته البتراء لأنه لم يحمد الله فيها ولم يصل على النبي (sihah); خطبة بتراء لما لم يذكر فيها اسم الله (mufradat); كل أمر لا يبدأ فيه بذكر الله فهو أبتر (mufradat); خطبته البتراء لأنه لم يفتتحها بحمد الله تعالى والصلاة على النبي (maqayis)","source_summary":"Kaynaklar, bu dali sozun veya isin beklenen kutsal acilis anmasindan yoksun baslamasi olarak verir; toplu hitap ornegi ve genel is formulu ayni kalipli alanda toplanir.","sources":["SI","MU","MQ"],"what_is_ar":"يدخل فيه الخطبة البتراء التي لم تفتتح بحمد الله والصلاة على النبي أو لم يذكر فيها اسم الله، وما روي في كل أمر لا يبدأ بذكر الله","what_is_not_ar":"لا يدخل فيه مجرد انقطاع الخير العام إذا لم يكن الكلام عن افتتاح ناقص، ولا انقطاع العقب أو القطع الحسي"},"support_links":[]},{"boundary":"Dal, akrabalik bagini bilerek koparan kisiye iliskindir; soy yoklugu veya nesne kesme degildir.","branch_kind":"bare","branch_ref":"root_000080/B004","candidate_links":[{"candidate_id":"cand_dcbe3f95c34e5aef4607","lane":"macro"},{"candidate_id":"cand_41d09b87577f3cca2578","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَبْتَر","morph_features":"STEM|POS:N|LEM:>abotar|ROOT:btr|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"108:3:4:2","qac_word_ref":"108:3:4","surface_ar":"أَبْتَرُ"}],"gloss":"akrabalik bagini koparma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Akrabalik bagi kesilip koparilan iliski olarak gorulur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kisi, bu bagi koparan fail oldugu icin nitelendirilir."}}],"root_ar":"ب ت ر","root_id":"root_000080","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kisinin kendi akrabalik iliskisini kesmesi ve bu nedenle nitelenmesi icindir.","boundary_detail":"Dal, akrabalik bagini bilerek koparan kisiye iliskindir; soy yoklugu veya nesne kesme degildir.","branch_image_ar":"قطع الرحم","concept_gloss":"akrabalik bagini koparma","contextual_glosses":[{"applicability":"Kisi nitelemesi gereken baglamlarda dogal bir karsiliktir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Failin akrabalik bagini koparmasini korur."},"facet_ids":["F001","F002"],"text":"akrabasiyla bagini koparan","usage_role":"contextual"}],"definition":"Kisinin akrabalik bagini, ona dusen iliski ve ilgiyi keserek koparmasidir; odak, kesilen soy bagindan cok bagini koparan faildedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Akrabalik bagi kesilip koparilan iliski olarak gorulur."},{"facet_id":"F002","role":"specialization","statement":"Kisi, bu bagi koparan fail oldugu icin nitelendirilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Soyun bulunmamasi veya devam etmemesi anlamini ekler.","collision":"Bu anlam ayri dalda yer alir.","fit":"displacement","loses":"Failin kendi akrabalik bagini koparma eylemini kaybeder.","preserves":"Akrabalik ve kesilme alanina yakin durur."},"text":"soyu kesilmis"}],"identity_rationale":"Kaynak ifadesi, kisinin akrabalik bagini kesen fail olarak nitelenmesini verir. Saglanan dal cercevesi, bunu soyun kendiliginden kesilmesi veya fiziksel parca kesme ile karistirmadan akrabalik bagini koparma alaninda tutar.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"akrabalik bagini koparan kisi"}],"lexicalization_note":"Mekanik kapsam ciplak daldir; tanim akrabalik bagini koparma cekirdegini kalipli baska anlamlarla karistirmaz.","neighbor_coverage_note":"Akrabalik davranisi ve genel iliski kesme komsulari siniri yeterince aciklar; evlilik ve diger bag adaylari daha uzak alanda kalir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal akrabalik iliskisine ve onu koparan kisiye daralir; komsu dal genel bag, iliski ve ayrilik kesilmelerini daha genis verir.","focus_only":"Akrabalik bagini koparan kisiye ozgudur.","gloss":"akrabalik bagi kopusu","neighbor_only":"Hicran, genel iliski kesme, insanlarin birbirinden ayrilmasi ve savasta ayrilma gibi daha genis kopuslari kapsar.","neighbor_ref":"root_001240/B007","relation_type":"near_synonym","shared_zone":"Ikisi de iliski veya bag kesme alaninda bulusur."},{"boundary_match":"opposed","distinction":"Bu dal bagin kesilmesini anlatir; komsu dal ayni iliski ekseninde bagin korunmasi ve iyilikle surdurulmesini anlatir.","focus_only":"Akrabalik bagini kesme ve iliskiyi koparma vardir.","gloss":"akrabalik kopusu ile akrabalik iyiligi","neighbor_only":"Akrabaya iyilik, bag kurma ve iliskiyi gozetme vardir.","neighbor_ref":"root_000104/B003","relation_type":"antonym","shared_zone":"Her iki dal akrabalik iliskisine yonelik davranis alanindadir."},{"boundary_match":"field_only","distinction":"Bu dal bir failin akrabalik iliskisini kesmesine odaklanir; komsu dal ardil soyun veya iyi etkinin kalmamasina odaklanir.","focus_only":"Kisi akrabalik bagini kendisi koparir.","gloss":"bag koparma ile soy kesilmesi","neighbor_only":"Kiside soy, anilma veya hayir etkisi devam etmez.","neighbor_ref":"root_000080/B002","relation_type":"same_field","shared_zone":"Ikisi de aile veya devam baginin kesilmesi imgesine yakindir."}],"source_phrase_ar":"رجل أباتر للذي يقطع رحمه (sihah); رجل أباتر يقطع رحمه (mufradat); رجل أباتر يقطع رحمه يبترها (maqayis)","source_summary":"Kaynaklar, bu dali akrabalik bagini kesen kisi nitelemesi olarak verir; anlam, soyun yok olmasi degil, kisinin bagini koparma eylemidir.","sources":["SI","MU","MQ"],"what_is_ar":"يدخل فيه الرجل الأباتر الذي يقطع رحمه ويبترها","what_is_not_ar":"لا يدخل فيه انقطاع العقب الذي يقع للإنسان، ولا قطع الذنب والشيء، ولا نقص افتتاح الخطبة"},"support_links":["sup_32b608df079240a28d59","sup_98c51b5c1916eab123eb"]},{"boundary":"Dal, gunes ve kusluk vaktiyle sinirli ozel kullanimdir; genel kesme anlamina tasinmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000080/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَبْتَر","morph_features":"STEM|POS:N|LEM:>abotar|ROOT:btr|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"108:3:4:2","qac_word_ref":"108:3:4","surface_ar":"أَبْتَرُ"}],"gloss":"kusluk gunesi ve o vakitte namaz kilma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gunes, yeri bastiran belirgin parlakligi icinde ozel bir adla anilir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kusluk namazinin, gunes isinlari cubuk gibi belirginlestigi anda kilinmasi bu alana baglanir."}}],"root_ar":"ب ت ر","root_id":"root_000080","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gunesin belirli kusluk parlakligi ile o anda kilinan namaz anlatimini birlikte kapsar.","boundary_detail":"Dal, gunes ve kusluk vaktiyle sinirli ozel kullanimdir; genel kesme anlamina tasinmaz.","branch_image_ar":"البتيراء للشمس ووقت الضحى","concept_gloss":"kusluk gunesi ve o vakitte namaz kilma","contextual_glosses":[{"applicability":"Ozel gunes adlandirmasi gereken baglamlarda kullanilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"O vakitte namaz kilma eylemini kapsamaz.","preserves":"Gunesin kusluk gorunumunu korur."},"facet_ids":["F001"],"text":"kusluk gunesi","usage_role":"contextual"},{"applicability":"Vakit-eylem kullaniminin aciklanmasi gereken baglamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gunes adlandirmasini tek basina karsilamaz.","preserves":"Belirli kusluk aninda namaz kilmayi korur."},"facet_ids":["F002"],"text":"kusluk gunesi yukselince namaz kilmak","usage_role":"contextual"}],"definition":"Gunesin yeri parlak bicimde bastigi kusluk anina ve o anda kusluk namazi kilma eylemine bagli dar bir kullanimdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gunes, yeri bastiran belirgin parlakligi icinde ozel bir adla anilir."},{"facet_id":"F002","role":"associated_use","statement":"Kusluk namazinin, gunes isinlari cubuk gibi belirginlestigi anda kilinmasi bu alana baglanir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kaynakta bulunmayan fiziksel kesilme anlamini ekler.","collision":"Dal, genel kesme cekirdegine degil ozel gunes-vakit kullanimina baglidir.","fit":"displacement","loses":"Kusluk parlakligi ve vakit-eylem kullanimini kaybeder.","preserves":"Gunes unsurunu korur."},"text":"kesilmis gunes"}],"identity_rationale":"Kaynak ifadesi, belirli bir gunes adlandirmasini ve kusluk vakti gunes isinlari belirginlesirken kilinan ibadet eylemini tek kaynakta verir. Dal cercevesi bu dar ve ozel kullanimlari fiziksel kesme, soy kesilmesi veya acilis eksigi anlamlarindan ayirarak dogru sinirlar.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bu kullanimda gunes"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"isinlar belirginlestigi kusluk aninda namaz kilmak"}],"lexicalization_note":"Bir adlandirma ve bir vakit-eylem kullanimi birlikte bulunur; tanim bunlari dar ozel alanda ayirir.","neighbor_coverage_note":"Yararli komsular zaman ve gunes alanindadir; ayni kokun kesme dallari burada yalniz uzak bir arka plan olusturur.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal dar bir kusluk gunesi ve eylem kullanimina baglidir; komsu dal sabah ve gunun baslangic zamanini genel olarak verir.","focus_only":"Kuslukta parlak gunes ve o vakitte namaz kilma kullanimi vardir.","gloss":"kusluk gunesi ile sabah","neighbor_only":"Sabah, tan ve gunun ilk zamani genel olarak adlandirilir.","neighbor_ref":"root_000839/B001","relation_type":"same_field","shared_zone":"Ikisi de gunun erken zamanlari ve isik alanindadir."},{"boundary_match":"field_only","distinction":"Bu dal yukselen parlak kusluk anina baglidir; komsu dal batma yonundeki egilimi anlatir.","focus_only":"Gunesin yeri bastiran kusluk parlakligi soz konusudur.","gloss":"kusluk parlakligi ile batisa egilme","neighbor_only":"Gunesin veya yildizin batisa egilmesi, gun sonu yonelimi soz konusudur.","neighbor_ref":"root_000866/B004","relation_type":"same_field","shared_zone":"Ikisi de gunesin gorunen durumunu zamanla iliskilendirir."},{"boundary_match":"thematic_only","distinction":"Bu dalin anlamini genel kesme cekirdeginden cikarmak okuyucuyu yaniltir; kanit, dar gunes ve vakit kullanimini verir.","focus_only":"Gunes ve kusluk vaktiyle sinirli ozel sozluk kullanimidir.","gloss":"gunes-vakit kullanimi ile kesme","neighbor_only":"Nesne veya parcanin kesilmesi temel anlamdir.","neighbor_ref":"root_000080/B001","relation_type":"thematic","shared_zone":"Kok baglantisi disinda guclu bir anlam ortakligi yoktur."}],"source_phrase_ar":"أبتر إذا صلى الضحى حين تقضب الشمس؛ تقضب أي يخرج شعاعها كالقضبان؛ حين تبهر البتيراء الأرض؛ البتيراء الشمس (tahdhib)","source_summary":"Tek verilen kaynak, gunesin belirli parlak kusluk gorunumunu ve o vakitte kusluk namazi kilma anlatimini birlikte aktarir; bu, kokun genel kesme alanindan cok dar bir sozluk kullanimidir.","sources":["TA"],"what_is_ar":"يدخل فيه استعمال البتيراء للشمس، وقول ابن الأعرابي أبتر إذا صلى الضحى حين تقضب الشمس","what_is_not_ar":"لا يدخل فيه الخطبة البتراء، ولا الأبتر بمعنى منقطع العقب، ولا القطع الحسي"},"support_links":[]},{"boundary":"Dal, dogrudan kesme fiili degil, kisa-toplu beden nitelemesine iliskin bilesik soz aciklamasidir.","branch_kind":"non_bare","branch_ref":"root_000080/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَبْتَر","morph_features":"STEM|POS:N|LEM:>abotar|ROOT:btr|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"108:3:4:2","qac_word_ref":"108:3:4","surface_ar":"أَبْتَرُ"}],"gloss":"kisa ve toplu yapili olma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kisa ve toplu beden yapisi nitelemenin hedefidir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu nitelik, boydan mahrum kalmis gibi dusunulerek bilesik soz aciklamasinda koke baglanir."}}],"root_ar":"ب ت ر","root_id":"root_000080","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalniz bilesik sozun kisa, toplu beden nitelemesi ve kaynak aciklamasi icin uygundur.","boundary_detail":"Dal, dogrudan kesme fiili degil, kisa-toplu beden nitelemesine iliskin bilesik soz aciklamasidir.","branch_image_ar":"قصر الخلقة كأن الطول بتر","concept_gloss":"kisa ve toplu yapili olma","contextual_glosses":[{"applicability":"Bilesik sozun kisi nitelemesi olarak cevrilmesi gereken baglamlarda kullanilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kisa ve toplu yapili kisi anlamini korur."},"facet_ids":["F001","F002"],"text":"kisa, toplu yapili kisi","usage_role":"contextual"}],"definition":"Kisa ve toplu yapili kisi icin, boyu sanki kesilip eksiltilmis gibi aciklanan bilesik soze bagli nitelemedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kisa ve toplu beden yapisi nitelemenin hedefidir."},{"facet_id":"F002","role":"source_variant","statement":"Bu nitelik, boydan mahrum kalmis gibi dusunulerek bilesik soz aciklamasinda koke baglanir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Genel yaratilis kesilmesi gibi kaynakta sinirli olmayan bir anlam ekler.","collision":"Dal bilesik sozun beden nitelemesiyle sinirlidir.","fit":"displacement","loses":"Kisa ve toplu yapili kisi nitelemesini belirsizlestirir.","preserves":"Boyun eksilmis gibi dusunulmesi imgesini korur."},"text":"kesilmis yaratilis"}],"identity_rationale":"Kaynak ifadesi, kisa ve toplu yapili kisi anlamina gelen bilesik sozu, iki unsurdan turemis bir aciklama olarak verir ve boydan mahrum kalma imgesiyle bu koke baglar. Dal korunabilir, ancak anlam ciplak kokun dogrudan kullanimi degil, yalniz bu bilesik sozun etimolojik aciklamasina bagli dar bir kullanmdir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"kisa ve toplu yapili kisi"}],"lexicalization_note":"Anlam bilesik sozle sinirlidir; ciplak koke kisa olmak gibi genel bir anlam yuklenmez.","neighbor_coverage_note":"Beden boyu komsulari siniri aciklar; ayni kokun soy ve akrabalik dallari bu dar bilesik kullanim icin belirleyici degildir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kisa ve toplu beden icin bilesik sozle sinirlidir; komsu dal kisalik alanini daha dogrudan ve genel verir.","focus_only":"Kisa ve toplu yapili kisiye iliskin bilesik soz aciklamasidir.","gloss":"bilesik kisa-toplu niteleme","neighbor_only":"Kisaligi ve kisa kilmayi genel beden veya nesne nitelemesi olarak verir.","neighbor_ref":"root_001231/B001","relation_type":"near_synonym","shared_zone":"Ikisi de kisa olma alaninda bulusur."},{"boundary_match":"opposed","distinction":"Bu dal kisalik ve topluluga yonelir; komsu dal uzunluk ve guzel beden orantisini verir.","focus_only":"Boyu eksilmis gibi kisa ve toplu yapi vurgulanir.","gloss":"kisa-toplu ile uzun-orantili beden","neighbor_only":"Uzun, duzgun ve iyi orantili govde yapisi vurgulanir.","neighbor_ref":"root_001204/B003","relation_type":"polarity_pair","shared_zone":"Her iki dal beden yapisi ve boy orani alanindadir."},{"boundary_match":"thematic_only","distinction":"Bu dal ciplak kesme anlami degildir; komsu dalda kesme eylemi dogrudan ve fiziksel cekirdektir.","focus_only":"Bilesik sozde beden kisaligini aciklayan etimolojik bir yorum vardir.","gloss":"kisa beden yorumu ile kesme","neighbor_only":"Nesne veya parcanin gercekten kesilip koparilmasi vardir.","neighbor_ref":"root_000080/B001","relation_type":"thematic","shared_zone":"Boyun kesilmis gibi dusunulmesi, kesme cekirdegine tematik olarak baglanir."}],"source_phrase_ar":"بحتر وهو القصير المجتمع الخلق؛ منحوت من كلمتين من الباء والتاء والراء؛ كأنه حرم الطول فبتر خلقه؛ والكلمة الثانية الحاء والتاء والراء (maqayis)","source_summary":"Tek verilen kaynak, kisa ve toplu yapili kisi anlamindaki bilesik sozu bu kokle ve ikinci bir unsurla aciklar; baglanti, boyun kesilmis gibi eksik kalmasi yorumuna dayanir.","sources":["MQ"],"what_is_ar":"يدخل فيه بحتر بمعنى القصير المجتمع الخلق على تفسير Maqayis أنه منحوت من بتر وحتر، كأنه حرم الطول فبتر خلقه","what_is_not_ar":"لا يدخل فيه الاستعمال الثلاثي المباشر لبتر، ولا قطع الذنب أو انقطاع العقب"},"support_links":[]},{"boundary":"Bu dal tiksinmeyi, çirkinlik niteliğini veya bir hakkı kabul etmeyi değil, nefret ile ona bağlı uzak durmayı anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000820/B001","candidate_links":[{"candidate_id":"cand_992e44dc4e2f7c847564","lane":"macro"},{"candidate_id":"cand_fa682536bb92a87acd69","lane":"macro"},{"candidate_id":"cand_86938f2928d0cebcf722","lane":"macro"},{"candidate_id":"cand_41d09b87577f3cca2578","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"شَانِئ","morph_features":"STEM|POS:N|ACT|PCPL|LEM:$aAni}|ROOT:$nA|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"108:3:2:1","qac_word_ref":"108:3:2","surface_ar":"شَانِئَ"}],"gloss":"nefret edip uzak durma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya şeye karşı güçlü bir sevgisizlik ve nefret duyulur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Nefret, kişiyi yöneldiği kişiden ya da şeyden uzak durmaya götürür."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Karşılıklı biçimde kullanıldığında iki tarafın birbirinden nefret etmesini anlatır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Türetilmiş biçimler nefretin kendisini ya da nefret eden ve düşmanlık besleyen kimseyi adlandırabilir."}}],"root_ar":"ش ن ء","root_id":"root_000820","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın nefret çekirdeğini ve bu duygudan doğan uzak durma yönelimini birlikte karşılayan genel kavram anlatımıdır.","boundary_detail":"Bu dal tiksinmeyi, çirkinlik niteliğini veya bir hakkı kabul etmeyi değil, nefret ile ona bağlı uzak durmayı anlatır.","branch_image_ar":"البغضة والعداوة","concept_gloss":"nefret edip uzak durma","contextual_glosses":[{"applicability":"Bağlam yalnızca bir kişiye veya şeye yönelen olumsuz duyguyu öne çıkarıyorsa doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bu duygunun doğurduğu uzak durma yönelimini açıkça söylemez.","preserves":"Bir kişiye veya şeye yönelen nefret duygusunu korur."},"facet_ids":["F001"],"text":"nefret etmek","usage_role":"general"},{"applicability":"Eylemin karşılıklı olduğu ve tarafların birbirine aynı duyguyla yöneldiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı nefret ilişkisini ve iki taraflı katılımı eksiksiz korur."},"facet_ids":["F003"],"text":"birbirinden nefret etmek","usage_role":"contextual"},{"applicability":"Türetilmiş biçim bir duyguyu değil, bu duyguyu taşıyan kişiyi adlandırdığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nefret duyan kişi rolünü doğrudan ve doğal biçimde korur."},"facet_ids":["F004"],"text":"nefret eden kimse","usage_role":"explanatory"}],"definition":"Bir kişiye ya da şeye karşı nefret duymak ve bu nefret yüzünden ondan uzak durmaktır. Karşılıklı kullanım, tarafların birbirinden nefret etmesini bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya şeye karşı güçlü bir sevgisizlik ve nefret duyulur."},{"facet_id":"F002","role":"extension","statement":"Nefret, kişiyi yöneldiği kişiden ya da şeyden uzak durmaya götürür."},{"facet_id":"F003","role":"specialization","statement":"Karşılıklı biçimde kullanıldığında iki tarafın birbirinden nefret etmesini anlatır."},{"facet_id":"F004","role":"associated_use","statement":"Türetilmiş biçimler nefretin kendisini ya da nefret eden ve düşmanlık besleyen kimseyi adlandırabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Açık çatışma, karşı eylem veya yerleşik husumet anlamı ekleyebilir.","collision":"Nefret duygusunu etkin bir çatışma ilişkisiyle karıştırabilir.","fit":"broadening","loses":null,"preserves":"Kişiler arasındaki güçlü olumsuz yönelimi kısmen korur."},"text":"düşmanlık"}],"identity_rationale":"Kaynak ifadesi çekirdeği bir kişiye ya da şeye karşı nefret duyma ve bu duyguyla ondan uzak durma olarak kurar. Düşmanlık, nefret eden kimsenin düşman diye nitelenebildiği kullanımlarda belirir; bu nedenle çekirdeğin yerine geçirilmeden bağımlı bir sonuç olarak korunmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"birinden nefret etti ve ona düşmanlık besledi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"nefret ve düşmanlık"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"nefret anlamındaki hafifletilmiş söyleyiş"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"nefret"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"nefret eden veya düşmanlık besleyen kimse"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"senden nefret eden ve sana düşmanlık besleyen kimse"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"birbirlerinden nefret ettiler"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"senden nefret eden kimse hakkında söylenen kinayeli söz"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"nefret etme"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"bir topluluğa duyulan nefret"}],"lexicalization_note":"Tanım yalın nefret çekirdeğini, karşılıklı nefret biçimini, nefret eden kişiyi bildiren kullanımları ve toplulukla kurulan tamlamayı birbirine karıştırmadan ayırır.","neighbor_coverage_note":"Adayların tümü değerlendirildi; genel nefret, tiksinti, dışa vurulan husumet ve nefret edilen kişi niteliği sınırı açıklayan en yararlı karşılaştırmalar olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal nefret alanını daha geniş çekim ve ettirim biçimleriyle kapsar; bu dal ise nefretin yanı sıra ondan uzak durma yönelimini belirginleştirir.","focus_only":"Nefretin nesnesinden uzak durma yönelimi çekirdeğin açık bir parçasıdır.","gloss":"genel nefret alanı","neighbor_only":"Nefretin oluşması, karşılıklı kılınması ve bir şeyi sevilmez hale getirme gibi daha geniş oluş ve ettirme biçimlerini kapsar.","neighbor_ref":"root_000136/B001","relation_type":"near_synonym","shared_zone":"İki dal da sevginin karşıtı olan nefret duygusunu ve birini sevmemeyi anlatır."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeği nefrettir; komşu dalın çekirdeği ise özellikle pislik karşısındaki tiksinti ve uzaklaşmadır.","focus_only":"Bir kişi veya şeye karşı nefret ve buna bağlı düşmanlık yönelimi bulunur.","gloss":"tiksinip uzak durma","neighbor_only":"Pis ya da kirletici sayılan şeyden tiksinme ve fiziksel ya da ruhsal olarak uzaklaşma öne çıkar.","neighbor_ref":"root_000820/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da güçlü olumsuz duygu, kaçınma ve nesneden uzaklaşma görülebilir."},{"boundary_match":"partial","distinction":"Bu dal duygu ve kaçınmaya odaklanır; komşu dal ise kişiler arasında dışa vuran sürtüşme ve husumet ilişkisini anlatır.","focus_only":"İçsel nefret ve nefret edilen şeyden kaçınma, açık çatışma olmadan da bulunabilir.","gloss":"husumet ve çekişme","neighbor_only":"Karşılıklı sürtüşme, sövme, ayıplama ve çatışmaya varmayan husumet davranışları bulunur.","neighbor_ref":"root_000780/B004","relation_type":"near_neighbor","shared_zone":"İki dal da kişiler arasında sevgisizlik, düşmanlık ve birbirinden uzaklaşma alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dal nefret eden öznenin duygusunu ve tutumunu, komşu dal ise nefret edilen ya da çirkin bulunan kişinin niteliğini kodlar.","focus_only":"Bir öznenin birine ya da bir şeye karşı duyduğu nefret ve uzak durma yönelimi anlatılır.","gloss":"sevilmeyen veya çirkin olma","neighbor_only":"Bir kişinin sevilmeyen, kötü huylu veya görünüşçe çirkin oluşu nitelik olarak anlatılır.","neighbor_ref":"root_000820/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal nefretin yöneldiği kişiyle ve o kişinin olumsuz değerlendirilmesiyle ilişkilidir."}],"source_phrase_ar":"أصل يدل على البغضة والتجنب للشيء؛ شنئ فلان فلانا إذا أبغضه (maqayis#2749;maqayis#2750)؛ شنيء يشنأ شنأة وشنآنا أي أبغض (ayn)؛ الشنآن البغض وتشانؤوا أي تباغضوا (sihah)؛ الشانيء المبغض والشنء البغضة (tahdhib)؛ شنئته تقذرته بغضا له وشنآن قوم أي بغضهم (mufradat)","source_summary":"Kaynaklar nefret duygusunda birleşir; bu duygu uzak durmayla ilişkilendirilir, karşılıklı biçimde iki taraf arasındaki nefreti ve türemiş biçimlerde nefret eden kimseyi de ifade eder.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه شنأ بمعنى أبغض، والشنآن والشنان والشنء بمعنى البغضة، والشانيء والشانئك بمعنى المبغض والعدو، والتشانؤ بمعنى التباغض.","what_is_not_ar":"لا يدخل التقزز والتباعد من الأدناس إلا من جهة اتصاله بالبغض، ولا يدخل الإقرار بالحق أو إخراجه."},"support_links":["sup_1ccd806eec605431df6e","sup_1cd967015b08216ed1f4","sup_32b608df079240a28d59","sup_e7edf6676a6d0470ba4d"]},{"boundary":"Dal, genel nefret veya sırf fiziksel uzaklaşma değil, tiksintiyle birlikte pis ya da kirletici sayılan şeyden uzak durmadır.","branch_kind":"mixed_non_bare","branch_ref":"root_000820/B002","candidate_links":[{"candidate_id":"cand_dcbe3f95c34e5aef4607","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"شَانِئ","morph_features":"STEM|POS:N|ACT|PCPL|LEM:$aAni}|ROOT:$nA|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"108:3:2:1","qac_word_ref":"108:3:2","surface_ar":"شَانِئَ"}],"gloss":"tiksinip uzak durma","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Pis veya kirletici sayılan bir şey karşısında güçlü bir tiksinti duyulur."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tiksinti, kişiyi pislikten veya iğrenç bulduğu şeyden uzak durmaya yöneltir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Nefret edilen bir şeyi iğrenç bulma, tiksintinin özel bir nedeni olarak anlatılabilir."}}],"root_ar":"ش ن ء","root_id":"root_000820","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Pis veya kirletici sayılan bir şeye karşı duyulan tiksintiyi ve bundan doğan uzaklaşmayı birlikte karşılar.","boundary_detail":"Dal, genel nefret veya sırf fiziksel uzaklaşma değil, tiksintiyle birlikte pis ya da kirletici sayılan şeyden uzak durmadır.","branch_image_ar":"التقزز والتباعد","concept_gloss":"tiksinip uzak durma","contextual_glosses":[{"applicability":"Bağlamda kişinin iğrenme tepkisi öndeyse ve uzaklaşma ayrıca anlaşılabiliyorsa doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nesneden fiilen ya da tutum olarak uzak durmayı açıkça belirtmez.","preserves":"Pis veya iğrenç bulunan şeye karşı duyulan tiksintiyi korur."},"facet_ids":["F001"],"text":"tiksinmek","usage_role":"general"},{"applicability":"Bir şeyin nefret edildiği için iğrenç bulunduğu özel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nefreti neden, iğrenmeyi ise ortaya çıkan tepki olarak korur."},"facet_ids":["F003"],"text":"nefretinden iğrenmek","usage_role":"contextual"}],"definition":"Pis veya kirletici sayılan bir şeyden tiksinmek ve ondan uzak durmaktır. Bazı kullanımlarda nefret, nesneyi iğrenç bulmanın nedeni olarak belirtilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Pis veya kirletici sayılan bir şey karşısında güçlü bir tiksinti duyulur."},{"facet_id":"F002","role":"core","statement":"Tiksinti, kişiyi pislikten veya iğrenç bulduğu şeyden uzak durmaya yöneltir."},{"facet_id":"F003","role":"specialization","statement":"Nefret edilen bir şeyi iğrenç bulma, tiksintinin özel bir nedeni olarak anlatılabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Pislikten veya iğrenç bulunan nesneden uzak durma sonucunu söylemez.","preserves":"Güçlü olumsuz tepkiyi ve nesneyi pis bulmayı korur."},"text":"iğrenmek"}],"identity_rationale":"Kaynak ifadesi tiksinmeyi, pisliklerden uzak durmayı ve nefret edilen bir şeyi iğrenç bulmayı açıkça destekler. Geçici çerçevede bu dala eklenen topluluk adı türetimi ise dal iddiasında yer almadığından kavram tanımına alınmamış, yalnızca ayrı sözlüksel birimlerin açıklamasında korunmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"ondan nefret ettiği için tiksindi"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"pislikten tiksinip uzak durma"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir şeyden tiksinip uzak duran kimse"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bu nitelemeden türetildiği belirtilen bir Yemen topluluğunun adı"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"aynı topluluk adının farklı söylenişi"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"söz konusu topluluğa mensup"}],"lexicalization_note":"Tanım, tiksinme adını ve bir şeyden tiksinmeyi kapsar; topluluk adıyla ilgili birimler kavram çekirdeğine genellenmeden ayrı sözlüksel açıklamalar olarak kalır.","neighbor_coverage_note":"Adayların tümü değerlendirildi; sakınma, nefret, pislik niteliği ve iç bulanmasıyla kurulan dört karşılaştırma dalın tiksinti sınırını yeterince açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal pislik karşısındaki tiksintiyi neden olarak öne çıkarır; komşu dal ise hoşlanmama yüzünden kendini koruyarak kaçınmaya odaklanır.","focus_only":"Tiksintinin özellikle pis veya kirletici sayılan bir nesneye yönelmesi bulunur.","gloss":"hoşlanmayıp sakınma","neighbor_only":"Kişinin hoşlanmadığı şeyden kendini koruması ve ona yaklaşmaması öne çıkar.","neighbor_ref":"root_001059/B008","relation_type":"near_synonym","shared_zone":"İki dal da hoşlanılmayan bir şeyden kaçınmayı ve ona yaklaşmamayı anlatır."},{"boundary_match":"partial","distinction":"Bu dalın ayırıcı öğesi tiksinti ve pislik algısıdır; komşu dalda ise temel duygu nefret, olası ilişki de düşmanlıktır.","focus_only":"Pis veya kirletici sayılan şey karşısında tiksinme ve ondan uzaklaşma bulunur.","gloss":"nefret edip uzak durma","neighbor_only":"Bir kişi ya da şeye karşı nefret ve buna bağlı düşmanlık yönelimi bulunur.","neighbor_ref":"root_000820/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal güçlü olumsuz duygu ve bu duygunun nesnesinden uzak durma alanında kesişir."},{"boundary_match":"partial","distinction":"Bu dal algılayan kişinin tepkisini kodlar; komşu dal ise tepkiye yol açan şeyin pis veya sakıncalı niteliğini kodlar.","focus_only":"Pis sayılan şey karşısındaki kişinin tiksinti ve uzak durma tepkisini anlatır.","gloss":"pis ve sakıncalı şey","neighbor_only":"Bir nesnenin, eylemin veya durumun kirli, bulaştırıcı ya da sakıncalı niteliğini anlatır.","neighbor_ref":"root_000543/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal pislik, iğrençlik ve kaçınılması gereken şey düşüncesinde buluşur."},{"boundary_match":"partial","distinction":"Bu dal nesneye yönelen tiksinti ile kaçınmayı, komşu dal ise kişinin içinde beliren bulantı ve kötüleşme halini anlatır.","focus_only":"Tiksinti, pis sayılan nesneden bilinçli biçimde uzak durmaya yöneltir.","gloss":"iç bulanması","neighbor_only":"Mide bulantısına benzeyen iç sıkıntısı ve kötüleşme hali öne çıkar.","neighbor_ref":"root_000619/B004","relation_type":"near_neighbor","shared_zone":"İki dal da bir şey karşısında duyulan iğrenme ve bedensel rahatsızlık alanına yaklaşır."}],"source_phrase_ar":"الشنوءة وهي التقزز (maqayis#2749;maqayis#2750)؛ الشنوءة التقزز وهو التباعد من الأدناس (sihah)؛ الرجل الشنوءة الذي يتقزز من الشيء (tahdhib)؛ شنئته تقذرته بغضا له (mufradat)","source_summary":"Kaynaklar tiksinme ile pislikten uzaklaşmayı aynı çekirdekte birleştirir; ayrıca nefret edilen şeyi iğrenç bulmayı bu çekirdeğin özel bir gerçekleşmesi olarak verir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الشنوءة بمعنى التقزز والتباعد من الأدناس، وتقذر الشيء بغضا له، وما اشتق منه مثل أزد شنوءة حيث تذكره المصادر في هذا الباب.","what_is_not_ar":"لا يدخل مجرد العداوة أو اسم البغضة إذا لم يذكر فيه معنى التقزز أو التباعد، ولا يدخل الإقرار."},"support_links":["sup_98c51b5c1916eab123eb"]},{"boundary":"Bu dal yalnızca belirtilen yapılarda geçerlidir; yalın köke genel bir kabul etme veya çıkarma anlamı yüklemez.","branch_kind":"collocation","branch_ref":"root_000820/B003","candidate_links":[{"candidate_id":"cand_7dd89cf2b1d9006b91f3","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"شَانِئ","morph_features":"STEM|POS:N|ACT|PCPL|LEM:$aAni}|ROOT:$nA|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"108:3:2:1","qac_word_ref":"108:3:2","surface_ar":"شَانِئَ"}],"gloss":"belirli yapılarda kabul etme veya aradan çıkarma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Anlam, yalın eylemden değil, eylemin aldığı belirli tümleç ve nesneden doğar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir durumla veya ona gönderme yapan tümleçle kullanıldığında o durumu kabul edip doğrulamayı bildirir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hak nesnesiyle kullanıldığında hakkı tanımayı ve onu kişinin kendi elinden çıkarmasını birlikte bildirir."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Hükümdar nesnesiyle çoğul kullanım, onu topluluğun arasından çıkarmayı bildirir."}}],"root_ar":"ش ن ء","root_id":"root_000820","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu üst anlatım yalnızca kanıtlanan üç bağlı kullanımın haritası için geçerlidir; her bağlamda ilgili tümleç ayrımı korunmalıdır.","boundary_detail":"Bu dal yalnızca belirtilen yapılarda geçerlidir; yalın köke genel bir kabul etme veya çıkarma anlamı yüklemez.","branch_image_ar":"إقرار الحق وإخراجه","concept_gloss":"belirli yapılarda kabul etme veya aradan çıkarma","contextual_glosses":[{"applicability":"Eylem bir durumla veya ona gönderme yapan tümleçle kurulduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirtilen durumu kabul etme ve doğrulama işlemini birlikte korur."},"facet_ids":["F002"],"text":"onu kabul edip doğruladı","usage_role":"contextual"},{"applicability":"Nesne bir başkasına ait hak olduğunda, kabul ile kişinin elinden çıkarma aşamalarını birlikte verir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hakkı tanıma ve onu kendi elinden çıkarma aşamalarını birlikte korur."},"facet_ids":["F003"],"text":"hakkını tanıyıp elinden çıkardı","usage_role":"contextual"},{"applicability":"Çoğul özne ve hükümdar nesnesi bulunan özel kullanımda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hükümdarı topluluğun içinden çıkarma işlemini ve katılımcıları korur."},"facet_ids":["F004"],"text":"hükümdarı aralarından çıkardılar","usage_role":"contextual"}],"definition":"Belirli tümleçli yapılarda bir durumu kabul edip doğrulamayı bildirir. Hak nesnesiyle hakkı tanıyıp kendi elinden çıkarmayı, hükümdar nesnesiyle ise onu topluluğun arasından çıkarmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Anlam, yalın eylemden değil, eylemin aldığı belirli tümleç ve nesneden doğar."},{"facet_id":"F002","role":"specialization","statement":"Bir durumla veya ona gönderme yapan tümleçle kullanıldığında o durumu kabul edip doğrulamayı bildirir."},{"facet_id":"F003","role":"specialization","statement":"Hak nesnesiyle kullanıldığında hakkı tanımayı ve onu kişinin kendi elinden çıkarmasını birlikte bildirir."},{"facet_id":"F004","role":"specialization","statement":"Hükümdar nesnesiyle çoğul kullanım, onu topluluğun arasından çıkarmayı bildirir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Bütün dalın yalnızca kabul anlamına geldiği izlenimini oluşturur.","fit":"narrowing","loses":"Hakkı elden çıkarma ile hükümdarı topluluğun arasından çıkarma kullanımlarını siler.","preserves":"Durum tümleciyle kurulan kabul ve doğrulama kullanımını korur."},"text":"kabul etmek"}],"identity_rationale":"Kaynak ifadesi tek bir yalın anlam değil, tümlece göre ayrılan üç bağlı kullanım verir: bir durumu kabul etme, bir hakkı tanıyıp kendi elinden çıkarma ve bir hükümdarı topluluğun arasından çıkarma. Dal korunabilir, ancak bütün bu işlemleri genel bir kabul anlamına indirgememek gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"onu kabul edip doğruladı"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"hakkını tanıyıp kendi elinden çıkardı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"hükümdarı aralarından çıkardılar"}],"lexicalization_note":"Tanım bütünüyle belirtilen tümleçli yapılara bağlıdır ve kabul, hakkı elden çıkarma ile hükümdarı aradan çıkarma kullanımlarını ayrı tutar.","neighbor_coverage_note":"Adayların tümü değerlendirildi; kabulün bağlamsal sınırı ile hakkı elden çıkarma işlemini açıklayan dört komşu seçildi, ilgisiz kök içi dallar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal belirli bir aktarım bağlamındaki itirafa odaklanır; bu dalın kabul kullanımı farklı bir yapıya bağlıdır ve ayrıca iki çıkarma yapısı vardır.","focus_only":"Kabulün yanında hakkı elden çıkarma ve hükümdarı topluluktan çıkarma yapıları da bulunur.","gloss":"belirli bağlamda itiraf","neighbor_only":"Kabul ve itiraf anlamı belirli bir aktarılan söz bağlamıyla sınırlıdır.","neighbor_ref":"root_000055/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir olguyu veya yükümlülüğü kabul edip doğrulama alanında kesişir."},{"boundary_match":"partial","distinction":"Bu dalda kabul belirli tümlecin anlamıdır ve baskı şartı yoktur; komşu dal kabulü zorlanma ve boyun eğmeyle sınırlar.","focus_only":"Kabul kullanımı zorlanma şartı taşımaz ve dal ayrıca iki çıkarma yapısı içerir.","gloss":"baskı altında kabul","neighbor_only":"Hakkı kabul etmeye baskı, boyun eğme ve istemeyerek uyma eşlik eder.","neighbor_ref":"root_000088/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir hakkı veya durumu kabul edip ona uygun davranmayı anlatabilir."},{"boundary_match":"partial","distinction":"Bu dal hakkı tanıyan kişinin onu elinden çıkarmasını anlatır; komşu dal ise yükümlü kişiyi borç ya da haktan kurtarmayı anlatır.","focus_only":"Hak önce tanınır ve ardından kişinin kendi elinden çıkarılır.","gloss":"haktan ibra etme","neighbor_only":"Borç, güvence veya haktan yükümlüyü açıkça kurtarma ve tarafların ayrılması bulunur.","neighbor_ref":"root_000099/B004","relation_type":"near_neighbor","shared_zone":"İki dal hakla ilgili bir yükümlülüğün kişinin üzerinden veya elinden çıkması alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dal tanıma ve elden çıkarma işlemlerini bildirir; komşu dal hakkın sahibine geri ulaşmasını sonuç olarak açıkça kodlar.","focus_only":"Hakkı kabul edip kişinin kendi elinden çıkarma aşaması bulunur.","gloss":"hakkı sahibine geri verme","neighbor_only":"Hakkı doğrudan sahibine geri verme ve yerine ulaştırma sonucu bulunur.","neighbor_ref":"root_000609/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal bir hakkın onu elinde tutan kişiden çıkmasıyla ilgilidir."}],"source_phrase_ar":"شنئت للأمر وبه إذا أقررت (maqayis#2749;maqayis#2750)؛ شنئ به أي أقر (sihah)؛ شنئت حقك أي أقررت به وأخرجته من عندي؛ شنئوا الملك أي أخرجوه من عندهم (tahdhib)","source_summary":"Toplu iddia, tümlece göre değişen üç işlemi bir araya getirir: bir durumu kabul etmek, bir hakkı tanıyıp elden çıkarmak ve bir hükümdarı topluluğun arasından çıkarmak.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه شنئت للأمر أو به بمعنى أقررت، وشنئت حقك بمعنى أقررت به وأخرجته من عندي، واستعمال شنئوا الملك بمعنى أخرجوه من عندهم.","what_is_not_ar":"لا يدخل البغض والشنآن، ولا التقزز، ولا قبح المنظر."},"support_links":["sup_3e5f5601c4e099e3207c"]},{"boundary":"Dal nefret etme eylemini değil, bir kişinin sevilmeyen, kötü huylu veya görünüşçe çirkin diye nitelenmesini bildirir.","branch_kind":"bare","branch_ref":"root_000820/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَانِئ","morph_features":"STEM|POS:N|ACT|PCPL|LEM:$aAni}|ROOT:$nA|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"108:3:2:1","qac_word_ref":"108:3:2","surface_ar":"شَانِئَ"}],"gloss":"sevilmeyen, kötü huylu veya çirkin olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi, başkalarının sevmediği ve kendisine nefret yönelttiği kimse olarak nitelenir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Nitelemenin gerekçesi kişinin kötü huyu ve itici davranışları olabilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Niteleme kişinin veya şeyin görünüşçe çirkin bulunmasına da dayanabilir."}}],"root_ar":"ش ن ء","root_id":"root_000820","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kişiye veya şeye yüklenen üç seçenekli olumsuz niteliğini bir üst anlatımda eksiksiz birleştirir.","boundary_detail":"Dal nefret etme eylemini değil, bir kişinin sevilmeyen, kötü huylu veya görünüşçe çirkin diye nitelenmesini bildirir.","branch_image_ar":"وصف البغيض أو القبيح","concept_gloss":"sevilmeyen, kötü huylu veya çirkin olma","contextual_glosses":[{"applicability":"Bağlam kişinin başkalarında uyandırdığı nefreti veya sevgisizliği öne çıkardığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin başkalarınca sevilmemesi ve nefrete konu olması niteliğini korur."},"facet_ids":["F001"],"text":"sevilmeyen kimse","usage_role":"contextual"},{"applicability":"Niteleme kişinin karakterindeki kötülüğe ve iticiliğe dayandığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Olumsuz değerlendirmenin kötü huydan kaynaklanmasını açıkça korur."},"facet_ids":["F002"],"text":"kötü huylu kimse","usage_role":"contextual"},{"applicability":"Niteleme insanın dış görünüşüne ve biçimsel çirkinliğine yöneldiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsanın görünüşçe çirkin bulunmasını doğrudan ve eksiksiz korur."},"facet_ids":["F003"],"text":"görünüşü çirkin kimse","usage_role":"contextual"}],"definition":"Bir insanı veya şeyi insanların sevmediği, kötü huylu ya da görünüşü çirkin biri veya şey olarak nitelemektir. Bu özellikler kaynaklarda seçenekli görünümler olarak yer alır ve her kullanımda birlikte bulunmaları gerekmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi, başkalarının sevmediği ve kendisine nefret yönelttiği kimse olarak nitelenir."},{"facet_id":"F002","role":"source_variant","statement":"Nitelemenin gerekçesi kişinin kötü huyu ve itici davranışları olabilir."},{"facet_id":"F003","role":"source_variant","statement":"Niteleme kişinin veya şeyin görünüşçe çirkin bulunmasına da dayanabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başkalarınca sevilmeme ve kötü huylu olma seçeneklerini dışarıda bırakır.","preserves":"Görünüş bakımından olumsuz değerlendirme seçeneğini korur."},"text":"çirkin"}],"identity_rationale":"Kaynak ifadesi aynı niteleme alanında üç ayrı gerekçe verir: insanların kişiyi sevmemesi, kişinin kötü huylu olması ve görünüşünün çirkin bulunması. Dal çerçevesi bu seçenekleri birini diğerinin zorunlu nedeni yapmadan koruduğu sürece kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"insanların sevmediği veya görünüşü çirkin kimse"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"görünüşü çirkin kimse"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"güzel olsa bile sevilmeyen kimse"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"sevilmeyen, kötü huylu kimse"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"sevilmeyen kadın"}],"lexicalization_note":"Tanım yalnızca dalın yalın niteleme alanını kapsar; başka dallardaki nefret eylemi, tiksinme veya kabul yapıları buraya taşınmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; genel çirkinlik, biçimsel çirkinlik, kadınla sınırlı çirkinlik ve nefret duygusu sınırı açıklayan en yararlı dört karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal çirkin görünüşün yanında sevilmeme ve kötü huy niteliklerini de taşır; komşu dal ise çirkinliği daha geniş varlık ve durumlara yayar.","focus_only":"İnsanların sevmemesi ve kişinin kötü huylu olması, görünüş çirkinliğine alternatif olabilir.","gloss":"genel çirkinlik","neighbor_only":"Çirkinlik insan, nesne, eylem ve durumların genel olarak güzelliğe aykırılığını kapsar.","neighbor_ref":"root_001194/B001","relation_type":"near_neighbor","shared_zone":"İki dal kişi veya şeyin görünüşçe çirkin ve olumsuz bulunmasını anlatabilir."},{"boundary_match":"partial","distinction":"Komşu dal biçimsel bozukluk ve görünüş çirkinliğine daralır; bu dal ise görünüş dışında sevilmeme ve kötü huyu da seçenek olarak içerir.","focus_only":"Sevilmeme ve kötü huy, görünüşte biçim bozukluğu bulunmadan da nitelemeyi doğurabilir.","gloss":"biçimi bozuk ve çirkin olma","neighbor_only":"Yüz veya yaratılış biçimindeki bozukluk ve farklılık özellikle öne çıkar.","neighbor_ref":"root_000831/B004","relation_type":"near_synonym","shared_zone":"İki dal da insanın dış görünüşünü çirkin veya itici diye niteleyebilir."},{"boundary_match":"partial","distinction":"Komşu dal kadın ve görünüş çirkinliğiyle sınırlıdır; bu dal daha geniş katılımcıları ve sevilmeme ile kötü huy seçeneklerini kapsar.","focus_only":"Niteleme cinsiyetle sınırlı değildir ve sevilmeme ya da kötü huydan da doğabilir.","gloss":"çirkin ve biçimsiz kadın","neighbor_only":"Niteleme özellikle bir kadının çirkin ve biçimsiz oluşuyla sınırlıdır.","neighbor_ref":"root_000271/B006","relation_type":"near_synonym","shared_zone":"İki dal bir kadını görünüş bakımından çirkin diye niteleme bağlamında örtüşür."},{"boundary_match":"partial","distinction":"Bu dal nefretin hedefindeki kişinin niteliğini, komşu dal ise nefret eden kişinin duygusunu ve tutumunu kodlar.","focus_only":"Nefret edilen kişinin sevilmeyen, kötü huylu veya çirkin niteliği anlatılır.","gloss":"nefret edip uzak durma","neighbor_only":"Nefret eden öznenin duygusu ve nefret ettiği şeyden uzak durma yönelimi anlatılır.","neighbor_ref":"root_000820/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal nefret duygusunun yöneldiği kişi ve onun olumsuz değerlendirilmesiyle ilişkilidir."}],"source_phrase_ar":"رجل مشناء إذا كان يبغضه الناس (maqayis#2749;maqayis#2750)؛ رجل شناءة وشنائية مبغض سيء الخلق (ayn)؛ رجل مشنأ أي قبيح المنظر والمشناء مثله (sihah)؛ المشنيئة البغيضة ورجل مشناء إذا كان قبيح المنظر (tahdhib)","source_summary":"Toplu kaynak iddiası aynı niteleme biçimlerini sevilmeme, kötü huy ve görünüş çirkinliği arasında farklı biçimde açıklar; bunlar tek bir zorunlu özellik dizisi değil, kaynaklar arasında değişen seçeneklerdir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه أوصاف الإنسان أو الشيء بما يورث البغض أو يدل على سوء الخلق أو قبح المنظر، مثل مشناء ومشنأ وشناءة وشنائية ومشنيئة.","what_is_not_ar":"لا يدخل مصدر البغض المجرد، ولا فعل الإبغاض نفسه، ولا الإقرار بالحق."},"support_links":[]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000532/B002","candidate_links":[{"candidate_id":"cand_fa682536bb92a87acd69","lane":"macro"},{"candidate_id":"cand_7ddcda5da4144d111e47","lane":"macro"},{"candidate_id":"cand_86938f2928d0cebcf722","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_4b4804f63b6dd0d2009e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Nurture, repair, and completion supply the process by which a received good is brought to maturity.","root":"ر ب ب","source_ref":"108:2","source_word_indices":["2"]},{"hft_ref":"hft_53c17dd34ad82657fb04","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Completion supplies the telic frame within which the commanded cut can belong to a finished response.","root":"ر ب ب","source_ref":"108:2","source_word_indices":["2"]},{"hft_ref":"hft_0e17669895926a26a3b3","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Nurture and completion constrain the heat image toward formation rather than destruction.","root":"ر ب ب","source_ref":"108:2","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000532","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_1cd967015b08216ed1f4","sup_e7edf6676a6d0470ba4d","sup_fc287cfced1a3677c692"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000532/B007","candidate_links":[{"candidate_id":"cand_20d3e6a98f8ea91a473b","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a876a951b928f942ef3c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Abiding and duration stabilize the procession as repeated continuity rather than a single act.","root":"ر ب ب","source_ref":"108:2","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000532","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_871c90aae6b44e686c5a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000532/B008","candidate_links":[{"candidate_id":"cand_3b48b16627f3d533a3fb","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_0276948f10b32ca50ac6","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The cloud branch supplies gathered capacity held before release.","root":"ر ب ب","source_ref":"108:2","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000532","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_3d30bf2c82237f8654ee"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000537/B005","candidate_links":[{"candidate_id":"cand_fa682536bb92a87acd69","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_4b4804f63b6dd0d2009e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The non-dominant mapped root contributes feeding and growth, keeping a second live route from lordly nurture to developing continuity.","root":"ر ب ب","source_ref":"108:2","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000537","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_1cd967015b08216ed1f4"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000537/B007","candidate_links":[{"candidate_id":"cand_41d09b87577f3cca2578","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6109ed67a16d53598671","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The non-dominant mapped branch supplies an extended household of close kin as the social network.","root":"ر ب ب","source_ref":"108:2","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000537","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_32b608df079240a28d59"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000879/B003","candidate_links":[{"candidate_id":"cand_fa682536bb92a87acd69","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_4b4804f63b6dd0d2009e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Specific worship supplies the responsive practice that follows reception of the gift.","root":"ص ل و","source_ref":"108:2","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000879","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_1cd967015b08216ed1f4"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000879/B006","candidate_links":[{"candidate_id":"cand_20d3e6a98f8ea91a473b","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a876a951b928f942ef3c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Following the previous runner supplies a serial model in which continuity consists of taking one's place after another.","root":"ص ل و","source_ref":"108:2","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000879","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_871c90aae6b44e686c5a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000880/B004","candidate_links":[{"candidate_id":"cand_86938f2928d0cebcf722","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_0e17669895926a26a3b3","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The non-dominant split branch supplies heating that straightens or sets a thing, making pressure potentially formative.","root":"ص ل و","source_ref":"108:2","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000880","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_e7edf6676a6d0470ba4d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001028/B002","candidate_links":[{"candidate_id":"cand_7dd89cf2b1d9006b91f3","lane":"macro"},{"candidate_id":"cand_992e44dc4e2f7c847564","lane":"macro"},{"candidate_id":"cand_3b48b16627f3d533a3fb","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6916deda0e3d590ccd51","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Actual handing over establishes a completed transfer and therefore a possible contested entitlement.","root":"ع ط و","source_ref":"108:1","source_word_indices":["2"]},{"hft_ref":"hft_6d244feb0f860ec9b201","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Handover establishes the directional path by which good reaches the addressee.","root":"ع ط و","source_ref":"108:1","source_word_indices":["2"]},{"hft_ref":"hft_0276948f10b32ca50ac6","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Handover supplies transfer from a source toward a recipient.","root":"ع ط و","source_ref":"108:1","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001028","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_1ccd806eec605431df6e","sup_3d30bf2c82237f8654ee","sup_3e5f5601c4e099e3207c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001028/B003","candidate_links":[{"candidate_id":"cand_41d09b87577f3cca2578","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6109ed67a16d53598671","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Service and handing to family supply circulation of benefit through a household relation.","root":"ع ط و","source_ref":"108:1","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001028","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_32b608df079240a28d59"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001286/B001","candidate_links":[{"candidate_id":"cand_992e44dc4e2f7c847564","lane":"macro"},{"candidate_id":"cand_3b48b16627f3d533a3fb","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6d244feb0f860ec9b201","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Abundance and numerical growth extend the received good forward rather than leaving it a one-time possession.","root":"ك ث ر","source_ref":"108:1","source_word_indices":["3"]},{"hft_ref":"hft_0276948f10b32ca50ac6","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Growth in abundance supplies the expanding effect of what is transferred.","root":"ك ث ر","source_ref":"108:1","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001286","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_1ccd806eec605431df6e","sup_3d30bf2c82237f8654ee"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001286/B002","candidate_links":[{"candidate_id":"cand_63a150ab0ea61644e363","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_f917866131c96195525b","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Outnumbering supplies an explicit competitive measure rather than undifferentiated plenty.","root":"ك ث ر","source_ref":"108:1","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001286","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6be6f7c55a3adad4460a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001286/B003","candidate_links":[{"candidate_id":"cand_63a150ab0ea61644e363","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_f917866131c96195525b","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Multiplicity in companions, speech, or demands supplies the possible present social noise of the contest.","root":"ك ث ر","source_ref":"108:1","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001286","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6be6f7c55a3adad4460a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001479/B002","candidate_links":[{"candidate_id":"cand_7ddcda5da4144d111e47","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_53c17dd34ad82657fb04","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Piercing the camel at the chest supplies a concrete, agentive cut performed under command.","root":"ن ح ر","source_ref":"108:2","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001479","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_fc287cfced1a3677c692"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001479/B003","candidate_links":[{"candidate_id":"cand_dcbe3f95c34e5aef4607","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_4076795693b2bff53498","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Chest facing chest supplies frontal presence and embodied encounter.","root":"ن ح ر","source_ref":"108:2","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001479","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_98c51b5c1916eab123eb"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001479/B009","candidate_links":[{"candidate_id":"cand_3b48b16627f3d533a3fb","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_0276948f10b32ca50ac6","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A cloud pouring out water supplies release and distribution from the gathered source.","root":"ن ح ر","source_ref":"108:2","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001479","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_3d30bf2c82237f8654ee"]}],"candidate_inventory":[{"anchor_refs":["108:1","108:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"108:3","branch_refs":["root_000080/B001","root_000820/B003","root_001028/B002"],"candidate_id":"cand_7dd89cf2b1d9006b91f3","commentary_obligation":"review","hft_ref":"hft_6916deda0e3d590ccd51","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_grant_turns_hostility_into_conceded_claim","source_type":"hft","support_ids":["sup_3e5f5601c4e099e3207c"],"title":"d_grant_turns_hostility_into_conceded_claim","trust":"legacy_unbound"},{"anchor_refs":["108:1","108:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"108:3","branch_refs":["root_000080/B002","root_000820/B001","root_001028/B002","root_001286/B001"],"candidate_id":"cand_992e44dc4e2f7c847564","commentary_obligation":"review","hft_ref":"hft_6d244feb0f860ec9b201","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_received_abundance_opens_continuity_channel","source_type":"hft","support_ids":["sup_1ccd806eec605431df6e"],"title":"d_received_abundance_opens_continuity_channel","trust":"legacy_unbound"},{"anchor_refs":["108:1","108:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"108:3","branch_refs":["root_000080/B002","root_001286/B002","root_001286/B003"],"candidate_id":"cand_63a150ab0ea61644e363","commentary_obligation":"review","hft_ref":"hft_f917866131c96195525b","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_numerical_contest_becomes_temporal","source_type":"hft","support_ids":["sup_6be6f7c55a3adad4460a"],"title":"d_numerical_contest_becomes_temporal","trust":"legacy_unbound"},{"anchor_refs":["108:2","108:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"108:3","branch_refs":["root_000080/B001","root_000532/B002","root_000537/B005","root_000820/B001","root_000879/B003"],"candidate_id":"cand_fa682536bb92a87acd69","commentary_obligation":"review","hft_ref":"hft_4b4804f63b6dd0d2009e","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_worship_enters_completion_and_growth","source_type":"hft","support_ids":["sup_1cd967015b08216ed1f4"],"title":"d_worship_enters_completion_and_growth","trust":"legacy_unbound"},{"anchor_refs":["108:2","108:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"108:3","branch_refs":["root_000080/B002","root_000532/B007","root_000879/B006"],"candidate_id":"cand_20d3e6a98f8ea91a473b","commentary_obligation":"review","hft_ref":"hft_a876a951b928f942ef3c","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_following_procession_reframes_posterity","source_type":"hft","support_ids":["sup_871c90aae6b44e686c5a"],"title":"d_following_procession_reframes_posterity","trust":"legacy_unbound"},{"anchor_refs":["108:2","108:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"108:3","branch_refs":["root_000080/B001","root_000532/B002","root_001479/B002"],"candidate_id":"cand_7ddcda5da4144d111e47","commentary_obligation":"review","hft_ref":"hft_53c17dd34ad82657fb04","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_purposeful_cut_exposes_premature_cut","source_type":"hft","support_ids":["sup_fc287cfced1a3677c692"],"title":"d_purposeful_cut_exposes_premature_cut","trust":"legacy_unbound"},{"anchor_refs":["108:2","108:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"108:3","branch_refs":["root_000080/B004","root_000820/B002","root_001479/B003"],"candidate_id":"cand_dcbe3f95c34e5aef4607","commentary_obligation":"review","hft_ref":"hft_4076795693b2bff53498","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_facing_body_opposes_aversive_retreat","source_type":"hft","support_ids":["sup_98c51b5c1916eab123eb"],"title":"d_facing_body_opposes_aversive_retreat","trust":"legacy_unbound"},{"anchor_refs":["108:2","108:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"108:3","branch_refs":["root_000080/B001","root_000532/B002","root_000820/B001","root_000880/B004"],"candidate_id":"cand_86938f2928d0cebcf722","commentary_obligation":"review","hft_ref":"hft_0e17669895926a26a3b3","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:o_hostile_heat_becomes_formative_pressure","source_type":"hft","support_ids":["sup_e7edf6676a6d0470ba4d"],"title":"o_hostile_heat_becomes_formative_pressure","trust":"legacy_unbound"},{"anchor_refs":["108:1","108:2","108:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"108:3","branch_refs":["root_000080/B004","root_000537/B007","root_000820/B001","root_001028/B003"],"candidate_id":"cand_41d09b87577f3cca2578","commentary_obligation":"review","hft_ref":"hft_6109ed67a16d53598671","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:o_household_circulation_vs_kin_severance","source_type":"hft","support_ids":["sup_32b608df079240a28d59"],"title":"o_household_circulation_vs_kin_severance","trust":"legacy_unbound"},{"anchor_refs":["108:1","108:2","108:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"108:3","branch_refs":["root_000080/B002","root_000532/B008","root_001028/B002","root_001286/B001","root_001479/B009"],"candidate_id":"cand_3b48b16627f3d533a3fb","commentary_obligation":"review","hft_ref":"hft_0276948f10b32ca50ac6","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:o_cloud_release_models_distributed_abundance","source_type":"hft","support_ids":["sup_3d30bf2c82237f8654ee"],"title":"o_cloud_release_models_distributed_abundance","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_c00be38453e24a9e277f","connection_ref":"conn_fad70897c18626915b78","note":"The immediate preceding gift, الكوثر, is the primary counterweight to الأبتر.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"108:1","source_target_components":["108:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"108:1","target_evidence":{"arabic_uthmani":"إِنَّآ أَعْطَيْنَٰكَ ٱلْكَوْثَرَ","ayah_ref":"108:1"},"target_ref":"108:1"},{"connection_evidence_ref":"conn_ev_568b965a1a5595e50e49","connection_ref":"conn_c70931387c4abd3c323c","note":"The immediate sacrificial command directly frames the offering-versus-barrenness reading.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"108:2","source_target_components":["108:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"108:2","target_evidence":{"arabic_uthmani":"فَصَلِّ لِرَبِّكَ وَٱنْحَرْ","ayah_ref":"108:2"},"target_ref":"108:2"}],"focus":{"arabic_uthmani":"إِنَّ شَانِئَكَ هُوَ ٱلْأَبْتَرُ","qac_morphemes":[{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"108:3:1:1","qac_word_ref":"108:3:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"شَانِئ","morph_features":"STEM|POS:N|ACT|PCPL|LEM:$aAni}|ROOT:$nA|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"108:3:2:1","qac_word_ref":"108:3:2","root_ar":"ش ن ء","surface_ar":"شَانِئَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"108:3:2:2","qac_word_ref":"108:3:2","root_ar":"","surface_ar":"كَ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|3MS","morpheme_role":"STEM","pos":"PRON","qac_ref":"108:3:3:1","qac_word_ref":"108:3:3","root_ar":"","surface_ar":"هُوَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"108:3:4:1","qac_word_ref":"108:3:4","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"أَبْتَر","morph_features":"STEM|POS:N|LEM:>abotar|ROOT:btr|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"108:3:4:2","qac_word_ref":"108:3:4","root_ar":"ب ت ر","surface_ar":"أَبْتَرُ"}],"word_analysis_qac_refs":[["108:3:1:1"],["108:3:2:1","108:3:2:2"],["108:3:3:1"],["108:3:4:1","108:3:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["108:3:1","108:3:2","108:3:3","108:3:4"]},"focus_surface_evidence":{"arabic_uthmani":"إِنَّ شَانِئَكَ هُوَ ٱلْأَبْتَرُ","qac_morphemes":[{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"108:3:1:1","qac_word_ref":"108:3:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"شَانِئ","morph_features":"STEM|POS:N|ACT|PCPL|LEM:$aAni}|ROOT:$nA|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"108:3:2:1","qac_word_ref":"108:3:2","root_ar":"ش ن ء","surface_ar":"شَانِئَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"108:3:2:2","qac_word_ref":"108:3:2","root_ar":"","surface_ar":"كَ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|3MS","morpheme_role":"STEM","pos":"PRON","qac_ref":"108:3:3:1","qac_word_ref":"108:3:3","root_ar":"","surface_ar":"هُوَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"108:3:4:1","qac_word_ref":"108:3:4","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"أَبْتَر","morph_features":"STEM|POS:N|LEM:>abotar|ROOT:btr|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"108:3:4:2","qac_word_ref":"108:3:4","root_ar":"ب ت ر","surface_ar":"أَبْتَرُ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["108:3:1:1"],["108:3:2:1","108:3:2:2"],["108:3:3:1"],["108:3:4:1","108:3:4:2"]],"word_analysis_refs":["108:3:1","108:3:2","108:3:3","108:3:4"],"word_rows":[{"analysis_record_ref":"108:3:1","analytic_gloss_range_en":"emphatic clause-opening particle that governs the whole nominal verdict and frames it as confirmed assertion","analytic_root_gloss_range_en":null,"qac_refs":["108:3:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"إِنَّ","transliteration":"inna"}},{"analysis_record_ref":"108:3:2","analytic_gloss_range_en":"the addressee's hater as an active-participle persona: settled, directed hostility toward the second-person object, not abstract hatred or a single past act","analytic_root_gloss_range_en":"hatred, loathing, rancor, enmity, and disparaging hostility; the local active participle personalizes that field as an antagonist aimed at the addressee","qac_refs":["108:3:2:1","108:3:2:2"],"root":{"arabic":"ش ن أ","transliteration":"sh-n-ʾ"},"surface":{"arabic":"شَانِئَكَ","transliteration":"shāni'aka"}},{"analysis_record_ref":"108:3:3","analytic_gloss_range_en":"independent separating pronoun that fixes predication and adds restrictive identity-force without introducing a new participant","analytic_root_gloss_range_en":null,"qac_refs":["108:3:3:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"هُوَ","transliteration":"huwa"}},{"analysis_record_ref":"108:3:4","analytic_gloss_range_en":"definite predicate naming the hater as the cut-off one: severed from continuation, good effect, and remembered future, with the physical cutting image still felt","analytic_root_gloss_range_en":"cutting short or cutting off, taillessness, loss of posterity or good effect, truncated beginnings, severed kinship, and other curtailed-length extensions; locally the person-predicate selects severed continuity rather than all branches","qac_refs":["108:3:4:1","108:3:4:2"],"root":{"arabic":"ب ت ر","transliteration":"b-t-r"},"surface":{"arabic":"ٱلْأَبْتَرُ","transliteration":"al-abtaru"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":3,"missing_anchor_refs":[],"supplied_unique_anchor_count":3},"assigned_record_count":10,"assigned_records":[{"anchor_refs":["108:1","108:3"],"branch_refs":["root_000080/B001","root_000820/B003","root_001028/B002"],"candidate_id":"cand_7dd89cf2b1d9006b91f3","evidence_scope":"declared_pericope","hft_ref":"hft_6916deda0e3d590ccd51","item_id":"d_grant_turns_hostility_into_conceded_claim","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_grant_turns_hostility_into_conceded_claim","support_id":"sup_3e5f5601c4e099e3207c"},{"anchor_refs":["108:1","108:3"],"branch_refs":["root_000080/B002","root_000820/B001","root_001028/B002","root_001286/B001"],"candidate_id":"cand_992e44dc4e2f7c847564","evidence_scope":"declared_pericope","hft_ref":"hft_6d244feb0f860ec9b201","item_id":"d_received_abundance_opens_continuity_channel","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_received_abundance_opens_continuity_channel","support_id":"sup_1ccd806eec605431df6e"},{"anchor_refs":["108:1","108:3"],"branch_refs":["root_000080/B002","root_001286/B002","root_001286/B003"],"candidate_id":"cand_63a150ab0ea61644e363","evidence_scope":"declared_pericope","hft_ref":"hft_f917866131c96195525b","item_id":"d_numerical_contest_becomes_temporal","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_numerical_contest_becomes_temporal","support_id":"sup_6be6f7c55a3adad4460a"},{"anchor_refs":["108:2","108:3"],"branch_refs":["root_000080/B001","root_000532/B002","root_000537/B005","root_000820/B001","root_000879/B003"],"candidate_id":"cand_fa682536bb92a87acd69","evidence_scope":"declared_pericope","hft_ref":"hft_4b4804f63b6dd0d2009e","item_id":"d_worship_enters_completion_and_growth","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_worship_enters_completion_and_growth","support_id":"sup_1cd967015b08216ed1f4"},{"anchor_refs":["108:2","108:3"],"branch_refs":["root_000080/B002","root_000532/B007","root_000879/B006"],"candidate_id":"cand_20d3e6a98f8ea91a473b","evidence_scope":"declared_pericope","hft_ref":"hft_a876a951b928f942ef3c","item_id":"d_following_procession_reframes_posterity","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_following_procession_reframes_posterity","support_id":"sup_871c90aae6b44e686c5a"},{"anchor_refs":["108:2","108:3"],"branch_refs":["root_000080/B001","root_000532/B002","root_001479/B002"],"candidate_id":"cand_7ddcda5da4144d111e47","evidence_scope":"declared_pericope","hft_ref":"hft_53c17dd34ad82657fb04","item_id":"d_purposeful_cut_exposes_premature_cut","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_purposeful_cut_exposes_premature_cut","support_id":"sup_fc287cfced1a3677c692"},{"anchor_refs":["108:2","108:3"],"branch_refs":["root_000080/B004","root_000820/B002","root_001479/B003"],"candidate_id":"cand_dcbe3f95c34e5aef4607","evidence_scope":"declared_pericope","hft_ref":"hft_4076795693b2bff53498","item_id":"d_facing_body_opposes_aversive_retreat","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_facing_body_opposes_aversive_retreat","support_id":"sup_98c51b5c1916eab123eb"},{"anchor_refs":["108:2","108:3"],"branch_refs":["root_000080/B001","root_000532/B002","root_000820/B001","root_000880/B004"],"candidate_id":"cand_86938f2928d0cebcf722","evidence_scope":"declared_pericope","hft_ref":"hft_0e17669895926a26a3b3","item_id":"o_hostile_heat_becomes_formative_pressure","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:o_hostile_heat_becomes_formative_pressure","support_id":"sup_e7edf6676a6d0470ba4d"},{"anchor_refs":["108:1","108:2","108:3"],"branch_refs":["root_000080/B004","root_000537/B007","root_000820/B001","root_001028/B003"],"candidate_id":"cand_41d09b87577f3cca2578","evidence_scope":"declared_pericope","hft_ref":"hft_6109ed67a16d53598671","item_id":"o_household_circulation_vs_kin_severance","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:o_household_circulation_vs_kin_severance","support_id":"sup_32b608df079240a28d59"},{"anchor_refs":["108:1","108:2","108:3"],"branch_refs":["root_000080/B002","root_000532/B008","root_001028/B002","root_001286/B001","root_001479/B009"],"candidate_id":"cand_3b48b16627f3d533a3fb","evidence_scope":"declared_pericope","hft_ref":"hft_0276948f10b32ca50ac6","item_id":"o_cloud_release_models_distributed_abundance","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:o_cloud_release_models_distributed_abundance","support_id":"sup_3d30bf2c82237f8654ee"}],"diagnostics":[],"lane_counts":{"global":10,"macro":10,"micro":3},"packet_summary":{"ayah_count":3,"focus_ref":"108:3","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ص ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":false,"target_occurrences":7,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["108:1","108:2","108:3"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"108:3","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":13,"unstructured_record_count":0},"identity":{"ayah_ref":"108:3","lane":"macro","linguistic_source_ref":"108:3","surface_ref":"108:3","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"108:3","target_tokens":[["Kuşkusuz",["108:3:1"]],["sana",["108:3:2"]],["kin",["108:3:2"]],["duyanın",["108:3:2"]],["kendisi",["108:3:3"]],["soyu",["108:3:4"]],["kesik",["108:3:4"]],["olandır",["108:3:3","108:3:4"]]],"text":"Kuşkusuz sana kin duyanın kendisi soyu kesik olandır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":10,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":1,"ayah_to":3,"id":"s108-p01-001-003","label":"Whole surah","number":1,"refs":["108:1","108:2","108:3"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"108:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"108:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["108:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"108:0"},{"ayah_ref":"108:1","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"108:1","root_occurrences":[{"lemmas_ar":["أَعْطَىٰ"],"occurrence_count":1,"pos_tags":["V"],"root":"ع ط و","surfaces_ar":["أَعْطَيْ"],"word_indices":["2"]},{"lemmas_ar":["كَوْثَر"],"occurrence_count":1,"pos_tags":["N"],"root":"ك ث ر","surfaces_ar":["كَوْثَرَ"],"word_indices":["3"]}],"root_sequence":["ع ط و","ك ث ر"],"text_ar":"إِنَّآ أَعْطَيْنَٰكَ ٱلْكَوْثَرَ"}],"context_order":["108:1"],"context_root_cues":[{"root":"ع ط و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الأخذ والتناول باليد"},{"branch_id":"B002","branch_image_ar":"المناولة والإعطاء"},{"branch_id":"B003","branch_image_ar":"الخدمة والمناولة للأهل"},{"branch_id":"B004","branch_image_ar":"التعاطي والخوض فيما يبلغه"},{"branch_id":"B005","branch_image_ar":"استعطاء الناس"},{"branch_id":"B006","branch_image_ar":"اللين والانقياد والمطاوعة"},{"branch_id":"B007","branch_image_ar":"الغلبة في التعاطي"}],"mapped_root_id":"root_001028","mapped_root_norm":"ع ط و"}]},{"root":"ك ث ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الكثرة ونماء العدد"},{"branch_id":"B002","branch_image_ar":"المكاثرة والغلبة بالعدد"},{"branch_id":"B003","branch_image_ar":"كثرة في صاحب أو كلام أو مطالب"},{"branch_id":"B005","branch_image_ar":"كوثر الغبار وتكوثره"},{"branch_id":"B006","branch_image_ar":"الكثر جمار النخل"},{"branch_id":"B007","branch_image_ar":"الكمثرة اجتماع الشيء"}],"mapped_root_id":"root_001286","mapped_root_norm":"ك ث ر"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"108:1","surface_ref":"108:1"},{"ayah_ref":"108:2","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"108:2","root_occurrences":[{"lemmas_ar":["صَلَّىٰ"],"occurrence_count":1,"pos_tags":["V"],"root":"ص ل و","surfaces_ar":["صَلِّ"],"word_indices":["1"]},{"lemmas_ar":["رَبّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ر ب ب","surfaces_ar":["رَبِّ"],"word_indices":["2"]},{"lemmas_ar":["ٱنْحَرْ"],"occurrence_count":1,"pos_tags":["V"],"root":"ن ح ر","surfaces_ar":["ٱنْحَرْ"],"word_indices":["3"]}],"root_sequence":["ص ل و","ر ب ب","ن ح ر"],"text_ar":"فَصَلِّ لِرَبِّكَ وَٱنْحَرْ"}],"context_order":["108:2"],"context_root_cues":[{"root":"ص ل و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ملاقاة النار وحرها"},{"branch_id":"B002","branch_image_ar":"الدعاء والثناء والرحمة"},{"branch_id":"B003","branch_image_ar":"العبادة المخصوصة"},{"branch_id":"B004","branch_image_ar":"الشرك المنصوبة"},{"branch_id":"B005","branch_image_ar":"الصَّلا من الظهر والجنب"},{"branch_id":"B006","branch_image_ar":"تلو السابق في السباق"},{"branch_id":"B007","branch_image_ar":"مواضع الصلاة ودور العبادة"},{"branch_id":"B008","branch_image_ar":"الصَّلاية حجر الدق"},{"branch_id":"B009","branch_image_ar":"الصِّليان نبت ترعاه الإبل"}],"mapped_root_id":"root_000879","mapped_root_norm":"ص ل و"},{"branches":[{"branch_id":"B001","branch_image_ar":"الصلاة عبادة لازمة"},{"branch_id":"B002","branch_image_ar":"الدعاء والبركة والرحمة"},{"branch_id":"B003","branch_image_ar":"ملاقاة النار وحرها"},{"branch_id":"B004","branch_image_ar":"إيقاد الصلاء وتسوية الشيء بالنار"},{"branch_id":"B005","branch_image_ar":"المَصالي أشراك وفخوخ"},{"branch_id":"B006","branch_image_ar":"الصَّلا موضع الظهر والذنب"},{"branch_id":"B007","branch_image_ar":"المصلي يتلو السابق"},{"branch_id":"B008","branch_image_ar":"الصلوات مواضع عبادة"},{"branch_id":"B009","branch_image_ar":"الصلاية حجر يدق عليه"},{"branch_id":"B010","branch_image_ar":"الصِّليان نبت ترعاه الإبل"}],"mapped_root_id":"root_000880","mapped_root_norm":"ص ل ي"}]},{"root":"ر ب ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ربوبية وملك وسيادة"},{"branch_id":"B002","branch_image_ar":"إصلاح وتربية وإتمام"},{"branch_id":"B003","branch_image_ar":"علم رباني"},{"branch_id":"B004","branch_image_ar":"ربة وجماعات كثيرة"},{"branch_id":"B005","branch_image_ar":"ربيب وربيبة ورابة"},{"branch_id":"B006","branch_image_ar":"رُبّ خاثر وإصلاح به"},{"branch_id":"B007","branch_image_ar":"لزوم وإقامة ودوام"},{"branch_id":"B008","branch_image_ar":"رباب السحاب"},{"branch_id":"B009","branch_image_ar":"شاة رُبّى وحداثة"},{"branch_id":"B010","branch_image_ar":"ربابة تجمع القداح"},{"branch_id":"B011","branch_image_ar":"ربابة عهد وميثاق"},{"branch_id":"B012","branch_image_ar":"ربة نبات"},{"branch_id":"B013","branch_image_ar":"ماء رَبَب كثير"},{"branch_id":"B014","branch_image_ar":"رَبْرَب قطيع"},{"branch_id":"B015","branch_image_ar":"حرف رب وربما"},{"branch_id":"B016","branch_image_ar":"رُبَى حاجة وعقدة ونعمة"},{"branch_id":"B017","branch_image_ar":"رباني الملاحين"}],"mapped_root_id":"root_000532","mapped_root_norm":"ر ب ب"},{"branches":[{"branch_id":"B001","branch_image_ar":"زيادة وعلو"},{"branch_id":"B002","branch_image_ar":"أرض مرتفعة"},{"branch_id":"B003","branch_image_ar":"زيادة الربا في المعاملة"},{"branch_id":"B004","branch_image_ar":"تصعد النفس وانتفاخه"},{"branch_id":"B005","branch_image_ar":"تغذية ونشوء"},{"branch_id":"B006","branch_image_ar":"نتوء أصل الفخذ"},{"branch_id":"B007","branch_image_ar":"أهل البيت من بني الأعمام"}],"mapped_root_id":"root_000537","mapped_root_norm":"ر ب و"}]},{"root":"ن ح ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"النحر صدر ظاهر"},{"branch_id":"B002","branch_image_ar":"طعن البعير في نحره"},{"branch_id":"B003","branch_image_ar":"نحر يقابل نحر"},{"branch_id":"B004","branch_image_ar":"تناحر على الشيء"},{"branch_id":"B005","branch_image_ar":"نحر نفسه"},{"branch_id":"B006","branch_image_ar":"نحر الزمن حد يواجه حدا"},{"branch_id":"B008","branch_image_ar":"نحر العلم إتقانا"},{"branch_id":"B009","branch_image_ar":"انتحر السحاب بالماء"}],"mapped_root_id":"root_001479","mapped_root_norm":"ن ح ر"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"108:2","surface_ref":"108:2"},{"ayah_ref":"1:2","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:2","root_occurrences":[{"lemmas_ar":["حَمْد"],"occurrence_count":1,"pos_tags":["N"],"root":"ح م د","surfaces_ar":["حَمْدُ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["لَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَبّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ر ب ب","surfaces_ar":["رَبِّ"],"word_indices":["3"]},{"lemmas_ar":["عَٰلَمِين"],"occurrence_count":1,"pos_tags":["N"],"root":"ع ل م","surfaces_ar":["عَٰلَمِينَ"],"word_indices":["4"]}],"root_sequence":["ح م د","ء ل ه","ر ب ب","ع ل م"],"text_ar":"ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ"}],"context_order":["1:2"],"context_root_cues":[{"root":"ح م د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الحمد خلاف الذم"},{"branch_id":"B002","branch_image_ar":"وجود الشيء محمودا"},{"branch_id":"B003","branch_image_ar":"المحمود كثير الخصال"},{"branch_id":"B004","branch_image_ar":"حماداك الغاية المحمودة"},{"branch_id":"B005","branch_image_ar":"يتحمد بالمنة"}],"mapped_root_id":"root_000355","mapped_root_norm":"ح م د"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ب ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ربوبية وملك وسيادة"},{"branch_id":"B002","branch_image_ar":"إصلاح وتربية وإتمام"},{"branch_id":"B003","branch_image_ar":"علم رباني"},{"branch_id":"B004","branch_image_ar":"ربة وجماعات كثيرة"},{"branch_id":"B005","branch_image_ar":"ربيب وربيبة ورابة"},{"branch_id":"B006","branch_image_ar":"رُبّ خاثر وإصلاح به"},{"branch_id":"B007","branch_image_ar":"لزوم وإقامة ودوام"},{"branch_id":"B008","branch_image_ar":"رباب السحاب"},{"branch_id":"B009","branch_image_ar":"شاة رُبّى وحداثة"},{"branch_id":"B010","branch_image_ar":"ربابة تجمع القداح"},{"branch_id":"B011","branch_image_ar":"ربابة عهد وميثاق"},{"branch_id":"B012","branch_image_ar":"ربة نبات"},{"branch_id":"B013","branch_image_ar":"ماء رَبَب كثير"},{"branch_id":"B014","branch_image_ar":"رَبْرَب قطيع"},{"branch_id":"B015","branch_image_ar":"حرف رب وربما"},{"branch_id":"B016","branch_image_ar":"رُبَى حاجة وعقدة ونعمة"},{"branch_id":"B017","branch_image_ar":"رباني الملاحين"}],"mapped_root_id":"root_000532","mapped_root_norm":"ر ب ب"},{"branches":[{"branch_id":"B001","branch_image_ar":"زيادة وعلو"},{"branch_id":"B002","branch_image_ar":"أرض مرتفعة"},{"branch_id":"B003","branch_image_ar":"زيادة الربا في المعاملة"},{"branch_id":"B004","branch_image_ar":"تصعد النفس وانتفاخه"},{"branch_id":"B005","branch_image_ar":"تغذية ونشوء"},{"branch_id":"B006","branch_image_ar":"نتوء أصل الفخذ"},{"branch_id":"B007","branch_image_ar":"أهل البيت من بني الأعمام"}],"mapped_root_id":"root_000537","mapped_root_norm":"ر ب و"}]},{"root":"ع ل م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"انكشاف الشيء للعارف"},{"branch_id":"B002","branch_image_ar":"أثر يميز الشيء ويهدي إليه"},{"branch_id":"B004","branch_image_ar":"شق ظاهر في الشفة العليا"},{"branch_id":"B005","branch_image_ar":"ماء كثير مجتمع في عيلم"},{"branch_id":"B006","branch_image_ar":"طائر جارح يسمى العلام"},{"branch_id":"B007","branch_image_ar":"ذكر الضباع يسمى العيلام"}],"mapped_root_id":"root_001040","mapped_root_norm":"ع ل م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:2","membership_added_ayah":true,"membership_target_surah":108,"surface_ref":"1:2"},{"ayah_ref":"1:3","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:3","root_occurrences":[{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["1","2"]}],"root_sequence":["ر ح م","ر ح م"],"text_ar":"ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"}],"context_order":["1:3"],"context_root_cues":[{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:3","membership_added_ayah":true,"membership_target_surah":108,"surface_ref":"1:3"},{"ayah_ref":"1:4","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:4","root_occurrences":[{"lemmas_ar":["مَٰلِك"],"occurrence_count":1,"pos_tags":["N"],"root":"م ل ك","surfaces_ar":["مَٰلِكِ"],"word_indices":["1"]},{"lemmas_ar":["يَوْم"],"occurrence_count":1,"pos_tags":["N"],"root":"ي و م","surfaces_ar":["يَوْمِ"],"word_indices":["2"]},{"lemmas_ar":["دِين"],"occurrence_count":1,"pos_tags":["N"],"root":"د ي ن","surfaces_ar":["دِّينِ"],"word_indices":["3"]}],"root_sequence":["م ل ك","ي و م","د ي ن"],"text_ar":"مَٰلِكِ يَوْمِ ٱلدِّينِ"}],"context_order":["1:4"],"context_root_cues":[{"root":"م ل ك","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"قوة الشيء وتماسكه"},{"branch_id":"B002","branch_image_ar":"المِلْك والتصرف"},{"branch_id":"B003","branch_image_ar":"المُلك والسلطان"},{"branch_id":"B004","branch_image_ar":"الإملاك والتزويج"},{"branch_id":"B005","branch_image_ar":"مِلاك الأمر وعِماده"},{"branch_id":"B006","branch_image_ar":"مَلَك الطريق والوادي"},{"branch_id":"B007","branch_image_ar":"الماء مَلَك الأمر"},{"branch_id":"B008","branch_image_ar":"المتقدم القائد في الحيوان"}],"mapped_root_id":"root_001444","mapped_root_norm":"م ل ك"}]},{"root":"ي و م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"وقت النهار المحدود"},{"branch_id":"B002","branch_image_ar":"مدة من الزمان"},{"branch_id":"B003","branch_image_ar":"كائنة اليوم وشدته"}],"mapped_root_id":"root_001700","mapped_root_norm":"ي و م"}]},{"root":"د ي ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الطاعة والانقياد"},{"branch_id":"B002","branch_image_ar":"الحساب والجزاء"},{"branch_id":"B003","branch_image_ar":"الدين المالي"},{"branch_id":"B004","branch_image_ar":"الإذلال والملك"},{"branch_id":"B005","branch_image_ar":"العادة والشأن"},{"branch_id":"B006","branch_image_ar":"مدينة الطاعة"},{"branch_id":"B007","branch_image_ar":"التصديق والتفويض"}],"mapped_root_id":"root_000504","mapped_root_norm":"د ي ن"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:4","membership_added_ayah":true,"membership_target_surah":108,"surface_ref":"1:4"},{"ayah_ref":"1:5","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:5","root_occurrences":[{"lemmas_ar":["عَبَدَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ع ب د","surfaces_ar":["نَعْبُدُ"],"word_indices":["2"]},{"lemmas_ar":["ٱسْتَعِينُ"],"occurrence_count":1,"pos_tags":["V"],"root":"ع و ن","surfaces_ar":["نَسْتَعِينُ"],"word_indices":["4"]}],"root_sequence":["ع ب د","ع و ن"],"text_ar":"إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ"}],"context_order":["1:5"],"context_root_cues":[{"root":"ع ب د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرق والملك"},{"branch_id":"B003","branch_image_ar":"العبادة والطاعة الخاضعة"},{"branch_id":"B004","branch_image_ar":"التعبيد والاستعباد"},{"branch_id":"B005","branch_image_ar":"التذليل والتسوية"},{"branch_id":"B006","branch_image_ar":"التكريم والتعظيم"},{"branch_id":"B007","branch_image_ar":"القوة والصلابة"},{"branch_id":"B008","branch_image_ar":"الأنفة والغضب"},{"branch_id":"B009","branch_image_ar":"قلة اللبث وسرعة العدو"},{"branch_id":"B010","branch_image_ar":"التفرق في الوجوه"},{"branch_id":"B011","branch_image_ar":"العطب والانقطاع"},{"branch_id":"B012","branch_image_ar":"صَلاءة الطيب"}],"mapped_root_id":"root_000973","mapped_root_norm":"ع ب د"}]},{"root":"ع و ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الإعانة والمظاهرة"},{"branch_id":"B002","branch_image_ar":"العَوان بين السنين"},{"branch_id":"B003","branch_image_ar":"الحرب العَوان"},{"branch_id":"B004","branch_image_ar":"النخلة العَوانة القديمة"},{"branch_id":"B005","branch_image_ar":"استواء الخلقة وتلاحق القوة"},{"branch_id":"B006","branch_image_ar":"العانة قطيع الحمر"},{"branch_id":"B007","branch_image_ar":"عانة الرجل"},{"branch_id":"B008","branch_image_ar":"النسبة إلى عانة"}],"mapped_root_id":"root_001064","mapped_root_norm":"ع و ن"},{"branches":[{"branch_id":"B001","branch_image_ar":"العين الناظرة"},{"branch_id":"B002","branch_image_ar":"المشاهدة بالعين"},{"branch_id":"B003","branch_image_ar":"عين الحفظ والرعاية"},{"branch_id":"B004","branch_image_ar":"الإصابة بالعين"},{"branch_id":"B005","branch_image_ar":"العين الجاسوسة"},{"branch_id":"B006","branch_image_ar":"منبع الماء الجاري"},{"branch_id":"B007","branch_image_ar":"عين الجلد والسقاء"},{"branch_id":"B008","branch_image_ar":"عين الشمس"},{"branch_id":"B009","branch_image_ar":"النقرة أو الموضع العيني"},{"branch_id":"B010","branch_image_ar":"عين السحاب والمطر"},{"branch_id":"B011","branch_image_ar":"النقد الحاضر"},{"branch_id":"B012","branch_image_ar":"العينة والسلف"},{"branch_id":"B013","branch_image_ar":"عين الشيء نفسه"},{"branch_id":"B014","branch_image_ar":"العين خيار الشيء"},{"branch_id":"B015","branch_image_ar":"أعيان القوم والإخوة"},{"branch_id":"B016","branch_image_ar":"سعة العين وحسنها"},{"branch_id":"B017","branch_image_ar":"العين بمعنى الناس الحاضرون"}],"mapped_root_id":"root_001069","mapped_root_norm":"ع ي ن"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:5","membership_added_ayah":true,"membership_target_surah":108,"surface_ref":"1:5"},{"ayah_ref":"1:6","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:6","root_occurrences":[{"lemmas_ar":["هَدَى"],"occurrence_count":1,"pos_tags":["V"],"root":"ه د ي","surfaces_ar":["ٱهْدِ"],"word_indices":["1"]},{"lemmas_ar":["صِرَٰط"],"occurrence_count":1,"pos_tags":["N"],"root":"ص ر ط","surfaces_ar":["صِّرَٰطَ"],"word_indices":["2"]},{"lemmas_ar":["مُّسْتَقِيم"],"occurrence_count":1,"pos_tags":["ADJ"],"root":"ق و م","surfaces_ar":["مُسْتَقِيمَ"],"word_indices":["3"]}],"root_sequence":["ه د ي","ص ر ط","ق و م"],"text_ar":"ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ"}],"context_order":["1:6"],"context_root_cues":[{"root":"ه د ي","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"دلالة بلطف إلى الطريق والحق"},{"branch_id":"B002","branch_image_ar":"جهة الأمر وسيرته وقصده"},{"branch_id":"B003","branch_image_ar":"المتقدم الهادي وأوائل الشيء"},{"branch_id":"B004","branch_image_ar":"بعثة لطف وهدية إلى ذي مودة"},{"branch_id":"B005","branch_image_ar":"الهدي المهدى إلى الحرم"},{"branch_id":"B006","branch_image_ar":"العروس المهدية إلى زوجها"},{"branch_id":"B007","branch_image_ar":"هدي الحرمة والأسير"},{"branch_id":"B008","branch_image_ar":"مشي التهادي مع الاعتماد والتمايل"},{"branch_id":"B009","branch_image_ar":"الهداء البليد الضعيف"},{"branch_id":"B010","branch_image_ar":"هدي السكون وحسن الهيئة"},{"branch_id":"B011","branch_image_ar":"إهداء الشعر ومهاداته"}],"mapped_root_id":"root_001583","mapped_root_norm":"ه د ي"}]},{"root":"ص ر ط","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الطريق المستقيم"},{"branch_id":"B002","branch_image_ar":"الغيبة في المرور والبلع"},{"branch_id":"B003","branch_image_ar":"السيف القاطع الماضي في الضربة"}],"mapped_root_id":"root_000858","mapped_root_norm":"ص ر ط"}]},{"root":"ق و م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"جماعة الناس والرجال"},{"branch_id":"B002","branch_image_ar":"انتصاب وقيام بالبدن"},{"branch_id":"B003","branch_image_ar":"عزم ونهوض إلى الأمر"},{"branch_id":"B004","branch_image_ar":"رعاية وحفظ وولاية"},{"branch_id":"B006","branch_image_ar":"مقام وإقامة في موضع"},{"branch_id":"B007","branch_image_ar":"نيابة وقيام مقام غيره"},{"branch_id":"B008","branch_image_ar":"استقامة واعتدال واستواء"},{"branch_id":"B009","branch_image_ar":"قوام وعماد ومعاش"},{"branch_id":"B010","branch_image_ar":"قيمة وتقويم وتسعير"},{"branch_id":"B011","branch_image_ar":"قامة وقوام الجسم والطول"},{"branch_id":"B012","branch_image_ar":"آلة قائمة وجزء قائم"},{"branch_id":"B013","branch_image_ar":"قيامة وبعث وقيام الساعة"},{"branch_id":"B014","branch_image_ar":"مقاومة ومنازلة"},{"branch_id":"B015","branch_image_ar":"وزن سواء ومقدار معتدل"},{"branch_id":"B016","branch_image_ar":"جمود ووقوف وكلال"},{"branch_id":"B017","branch_image_ar":"انتصاف النهار وقائم الظهيرة"},{"branch_id":"B018","branch_image_ar":"نفاق السوق"},{"branch_id":"B019","branch_image_ar":"وجع قائم بالعضو"},{"branch_id":"B020","branch_image_ar":"قوام في قوائم الشاة"},{"branch_id":"B021","branch_image_ar":"عين قائمة ذاهبة البصر"}],"mapped_root_id":"root_001273","mapped_root_norm":"ق و م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:6","membership_added_ayah":true,"membership_target_surah":108,"surface_ref":"1:6"},{"ayah_ref":"1:7","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:7","root_occurrences":[{"lemmas_ar":["صِرَٰط"],"occurrence_count":1,"pos_tags":["N"],"root":"ص ر ط","surfaces_ar":["صِرَٰطَ"],"word_indices":["1"]},{"lemmas_ar":["أَنْعَمَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ن ع م","surfaces_ar":["أَنْعَمْ"],"word_indices":["3"]},{"lemmas_ar":["غَيْر"],"occurrence_count":1,"pos_tags":["N"],"root":"غ ي ر","surfaces_ar":["غَيْرِ"],"word_indices":["5"]},{"lemmas_ar":["مَغْضُوب"],"occurrence_count":1,"pos_tags":["N"],"root":"غ ض ب","surfaces_ar":["مَغْضُوبِ"],"word_indices":["6"]},{"lemmas_ar":["ضَآلّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ض ل ل","surfaces_ar":["ضَّآلِّينَ"],"word_indices":["9"]}],"root_sequence":["ص ر ط","ن ع م","غ ي ر","غ ض ب","ض ل ل"],"text_ar":"صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ"}],"context_order":["1:7"],"context_root_cues":[{"root":"ص ر ط","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الطريق المستقيم"},{"branch_id":"B002","branch_image_ar":"الغيبة في المرور والبلع"},{"branch_id":"B003","branch_image_ar":"السيف القاطع الماضي في الضربة"}],"mapped_root_id":"root_000858","mapped_root_norm":"ص ر ط"}]},{"root":"ن ع م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"حسن الحال والنعمة"},{"branch_id":"B002","branch_image_ar":"اللين والنعومة ورفاه العيش"},{"branch_id":"B003","branch_image_ar":"مدح الشيء بنعم"},{"branch_id":"B004","branch_image_ar":"الجواب بنعم والتصديق"},{"branch_id":"B005","branch_image_ar":"مال الأنعام والإبل"},{"branch_id":"B006","branch_image_ar":"النعام والنعامة الطائر"},{"branch_id":"B007","branch_image_ar":"ما سمي نعامة تشبيها بالهيئة"},{"branch_id":"B008","branch_image_ar":"طيران النعامة وتفرق القوم"},{"branch_id":"B009","branch_image_ar":"النعامى ريح لينة"},{"branch_id":"B010","branch_image_ar":"زاد وأنعم في الفعل"},{"branch_id":"B011","branch_image_ar":"موافقة المكان وطيب المقام"},{"branch_id":"B012","branch_image_ar":"المشي على القدم وابتذالها"},{"branch_id":"B013","branch_image_ar":"نعم الله بك عينا وقرة العين"}],"mapped_root_id":"root_001525","mapped_root_norm":"ن ع م"}]},{"root":"غ ي ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الصلاح والمنفعة بالميرة والسقي والإصلاح"},{"branch_id":"B002","branch_image_ar":"الغَيْر في الدية"},{"branch_id":"B003","branch_image_ar":"تغيير الصورة أو إبدال الشيء بغيره"},{"branch_id":"B004","branch_image_ar":"الغَيْرة على الأهل"},{"branch_id":"B005","branch_image_ar":"السوى والخلاف والاستثناء والنفي"}],"mapped_root_id":"root_001119","mapped_root_norm":"غ ي ر"}]},{"root":"غ ض ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"اشتداد السخط وثورانه للانتقام"},{"branch_id":"B002","branch_image_ar":"الغضب لشخص حي أو به بعد موته"},{"branch_id":"B003","branch_image_ar":"المراغمة والمخالفة"},{"branch_id":"B004","branch_image_ar":"صلابة الصخرة وتماسكها"},{"branch_id":"B005","branch_image_ar":"غلظ الجسم وشدة الحمرة"},{"branch_id":"B006","branch_image_ar":"تورم العين وما حولها"},{"branch_id":"B007","branch_image_ar":"العبوس والضجر والعظم في وصف الحيوان أو الشخص"},{"branch_id":"B008","branch_image_ar":"جلد صلب أو مطوي كدرقة"}],"mapped_root_id":"root_001092","mapped_root_norm":"غ ض ب"}]},{"root":"ض ل ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الضلال عن الهدى والقصد"},{"branch_id":"B002","branch_image_ar":"الغيبوبة والخفاء"},{"branch_id":"B003","branch_image_ar":"فقدان الشيء"},{"branch_id":"B004","branch_image_ar":"ضياع الحفظ"},{"branch_id":"B005","branch_image_ar":"الضالّة في المضيعة"}],"mapped_root_id":"root_000913","mapped_root_norm":"ض ل ل"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:7","membership_added_ayah":true,"membership_target_surah":108,"surface_ref":"1:7"}],"support_registry":[{"anchor_evidence":[{"arabic_uthmani":"إِنَّآ أَعْطَيْنَٰكَ ٱلْكَوْثَرَ","ayah_ref":"108:1"},{"arabic_uthmani":"إِنَّ شَانِئَكَ هُوَ ٱلْأَبْتَرُ","ayah_ref":"108:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000080/B001","root_000820/B003","root_001028/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001028","role":"Actual handing over establishes a completed transfer and therefore a possible contested entitlement.","root":"ع ط و","source_ref":"108:1","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000820","role":"Acknowledging and releasing a right supplies the surprising concession role for the hostile agent.","root":"ش ن ء","source_ref":"108:3","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000080","role":"Cutting before completion makes the opponent's counterclaim, rather than the grant, the aborted undertaking.","root":"ب ت ر","source_ref":"108:3","source_word_indices":["4"]}],"changed_reading":{"after":"The prior grant makes him legible as a counterclaimant whose opposition concedes the addressee's right and fails before completion.","before":"The hater simply loses future standing."},"confidence":"exploratory","mechanism":"Once a grant has been handed to the addressee, the rare acknowledgment-and-release branch of ش ن ء can activate a contest over entitlement. The hater becomes an unsuccessful counterclaimant who must yield the right he contests, while his challenge is the thing cut short.","model_id":"d_grant_turns_hostility_into_conceded_claim","reader_inference":"The packet supplies a completed handover, a remote focus-root branch of conceding a right, and premature cutting; I infer a contested claim whose resolution forces the hater to yield. A live alternative is that giving only contrasts with loss and does not create a juridical scene.","status":"new","structural_cues":["108:1 presents the grant as completed before the focus verdict.","The second-person recipient of the grant is also the person against whom the focus hostility is directed."],"trigger_roots":["ع ط و"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_grant_turns_hostility_into_conceded_claim","source_type":"hft","support_id":"sup_3e5f5601c4e099e3207c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّآ أَعْطَيْنَٰكَ ٱلْكَوْثَرَ","ayah_ref":"108:1"},{"arabic_uthmani":"إِنَّ شَانِئَكَ هُوَ ٱلْأَبْتَرُ","ayah_ref":"108:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000080/B002","root_000820/B001","root_001028/B002","root_001286/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001028","role":"Handover establishes the directional path by which good reaches the addressee.","root":"ع ط و","source_ref":"108:1","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001286","role":"Abundance and numerical growth extend the received good forward rather than leaving it a one-time possession.","root":"ك ث ر","source_ref":"108:1","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000820","role":"Enmity marks the relation that cannot enter or cancel the transmission circuit.","root":"ش ن ء","source_ref":"108:3","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000080","role":"Cut-off mention and good effect specify what exclusion from the expanding circuit costs the hater.","root":"ب ت ر","source_ref":"108:3","source_word_indices":["4"]}],"changed_reading":{"after":"It describes relational exclusion from a received good that continues to multiply beyond the hater's reach.","before":"The predicate describes the hater's private lack of descendants, renown, or good."},"confidence":"strong","mechanism":"Handover plus numerical growth forms a source-recipient-future circuit. Against that circuit, the focus predicate no longer means only that the hater possesses little; it means that hostility has no access to the multiplying transmission of good, mention, and effect.","model_id":"d_received_abundance_opens_continuity_channel","reader_inference":"The packet supplies handing over, growth, hostility, and loss of continuing effect; I infer a durable transmission circuit and treat the hater's cutoff as exclusion from it. A live alternative is a noncausal juxtaposition of abundance and privation.","status":"revised","structural_cues":["The context begins with a completed first-person-plural grant to the same second-person addressee.","The focus verdict follows after the gift and its commanded response, making continuity and cutoff sequentially contrastive."],"trigger_roots":["ع ط و","ك ث ر"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_received_abundance_opens_continuity_channel","source_type":"hft","support_id":"sup_1ccd806eec605431df6e","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّآ أَعْطَيْنَٰكَ ٱلْكَوْثَرَ","ayah_ref":"108:1"},{"arabic_uthmani":"إِنَّ شَانِئَكَ هُوَ ٱلْأَبْتَرُ","ayah_ref":"108:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000080/B002","root_001286/B002","root_001286/B003"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001286","role":"Outnumbering supplies an explicit competitive measure rather than undifferentiated plenty.","root":"ك ث ر","source_ref":"108:1","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_001286","role":"Multiplicity in companions, speech, or demands supplies the possible present social noise of the contest.","root":"ك ث ر","source_ref":"108:1","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000080","role":"Loss of mention and good effect moves the decisive count from present quantity to persistence through time.","root":"ب ت ر","source_ref":"108:3","source_word_indices":["4"]}],"changed_reading":{"after":"They are rival measures of success: current numerical pressure is defeated by the addressee's future continuity and the hater's vanishing effect.","before":"Abundance and cutoff are opposite quantities."},"confidence":"medium","mechanism":"The outnumbering branch turns the contrast into a contest over scale, but the focus predicate changes the axis from present headcount to future persistence. A hostile party may possess many voices or claims now, yet loses the contest if its mention and good effect do not continue.","model_id":"d_numerical_contest_becomes_temporal","reader_inference":"The packet supplies outnumbering, many companions or claims, and interrupted mention; I infer that the text changes the scoreboard from present quantity to temporal endurance. A live alternative is that numerical competition is only a branch-level analogy.","status":"strengthened","structural_cues":["The abundance term occurs before the singularly identified hater in the focus ayah.","The focus emphatic pronoun isolates the bearer of the cutoff despite any wider hostile plurality inferred from competitive abundance."],"trigger_roots":["ك ث ر"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_numerical_contest_becomes_temporal","source_type":"hft","support_id":"sup_6be6f7c55a3adad4460a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَصَلِّ لِرَبِّكَ وَٱنْحَرْ","ayah_ref":"108:2"},{"arabic_uthmani":"إِنَّ شَانِئَكَ هُوَ ٱلْأَبْتَرُ","ayah_ref":"108:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000080/B001","root_000532/B002","root_000537/B005","root_000820/B001","root_000879/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000879","role":"Specific worship supplies the responsive practice that follows reception of the gift.","root":"ص ل و","source_ref":"108:2","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000532","role":"Nurture, repair, and completion supply the process by which a received good is brought to maturity.","root":"ر ب ب","source_ref":"108:2","source_word_indices":["2"]},{"branch_id":"B005","mapped_root_id":"root_000537","role":"The non-dominant mapped root contributes feeding and growth, keeping a second live route from lordly nurture to developing continuity.","root":"ر ب ب","source_ref":"108:2","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000820","role":"Hostility supplies the counter-trajectory that tries to obstruct the formed response.","root":"ش ن ء","source_ref":"108:3","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000080","role":"Premature cutting names the failure of the hostile trajectory to reach completion.","root":"ب ت ر","source_ref":"108:3","source_word_indices":["4"]}],"changed_reading":{"after":"The hater occupies a failed trajectory: opposition cannot mature, while the addressee's responsive practice is nurtured into continuity.","before":"The hater is an already cut-off person."},"confidence":"strong","mechanism":"The commanded act is directed into a field of worship, nurture, completion, and growth. That field converts the focus predicate from a generic fate into a contrast of trajectories: responsive alignment is formed and carried onward, while the hostile project is interrupted before attaining its end.","model_id":"d_worship_enters_completion_and_growth","reader_inference":"The packet supplies worship, nurturing completion, a split-root image of feeding and growth, and premature cutting; I infer that responsive alignment enables maturation while the hostile project aborts. A live alternative is a static lexical opposition between completion and cutting with no causal participation.","status":"revised","structural_cues":["108:2 converts the completed gift of 108:1 into an imperative response directed to the addressee's Lord.","The focus verdict comes after the paired imperatives, so completion and interruption can be read as divergent outcomes of response and hostility."],"trigger_roots":["ص ل و","ر ب ب"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_worship_enters_completion_and_growth","source_type":"hft","support_id":"sup_1cd967015b08216ed1f4","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَصَلِّ لِرَبِّكَ وَٱنْحَرْ","ayah_ref":"108:2"},{"arabic_uthmani":"إِنَّ شَانِئَكَ هُوَ ٱلْأَبْتَرُ","ayah_ref":"108:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000080/B002","root_000532/B007","root_000879/B006"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_000879","role":"Following the previous runner supplies a serial model in which continuity consists of taking one's place after another.","root":"ص ل و","source_ref":"108:2","source_word_indices":["1"]},{"branch_id":"B007","mapped_root_id":"root_000532","role":"Abiding and duration stabilize the procession as repeated continuity rather than a single act.","root":"ر ب ب","source_ref":"108:2","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000080","role":"Interrupted posterity, mention, and good effect identify the hater as unable to continue in the sequence.","root":"ب ت ر","source_ref":"108:3","source_word_indices":["4"]}],"changed_reading":{"after":"Posterity also becomes succession: being followed in responsive practice and good effect, a chain from which the hater is absent.","before":"Posterity is primarily a genealogical possession."},"confidence":"medium","mechanism":"The image of a runner following the one ahead, joined to abiding duration, recasts continuity as a procession rather than only biological descent. The addressee's response can be followed, repeated, and carried onward; the hater is the one who cannot take or transmit a place in that sequence.","model_id":"d_following_procession_reframes_posterity","reader_inference":"The packet supplies a following-runner image, duration, and lost posterity or mention; I infer a transmissible procession of practice and memory. A live alternative is that the racing image remains a remote lexical branch and biological or reputational continuity stays primary.","status":"new","structural_cues":["The prefixed conjunction on the first imperative makes the commanded response follow the completed grant.","The two imperatives create repeatable acts before the focus verdict names the failed continuation."],"trigger_roots":["ص ل و","ر ب ب"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_following_procession_reframes_posterity","source_type":"hft","support_id":"sup_871c90aae6b44e686c5a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَصَلِّ لِرَبِّكَ وَٱنْحَرْ","ayah_ref":"108:2"},{"arabic_uthmani":"إِنَّ شَانِئَكَ هُوَ ٱلْأَبْتَرُ","ayah_ref":"108:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000080/B001","root_000532/B002","root_001479/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000532","role":"Completion supplies the telic frame within which the commanded cut can belong to a finished response.","root":"ر ب ب","source_ref":"108:2","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001479","role":"Piercing the camel at the chest supplies a concrete, agentive cut performed under command.","root":"ن ح ر","source_ref":"108:2","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000080","role":"Cutting something short before completion supplies the contrasting failed and untimely severance.","root":"ب ت ر","source_ref":"108:3","source_word_indices":["4"]}],"changed_reading":{"after":"It marks specifically an untimely and fruitless interruption, contrasted with a deliberate cut integrated into a completed act.","before":"The predicate treats all severance as undifferentiated loss."},"confidence":"medium","mechanism":"The context places a commanded, directed chest-cut beside nurture and completion. This distinguishes a purposeful act that consummates a response from the focus root's cutting-before-completion: the hater is not condemned for every kind of cutting but for an abortive, nonfruitful interruption.","model_id":"d_purposeful_cut_exposes_premature_cut","reader_inference":"The packet supplies a commanded chest-cut, nurture toward completion, and premature truncation; I infer a contrast in agency and telos between consummating sacrifice and abortive hostility. A live alternative is that the two cutting images are only material resonance.","status":"revised","structural_cues":["The cutting imperative is directed to the Lord and immediately precedes the focus verdict.","The command is coordinated with worship, embedding the physical act in a completed response rather than random violence."],"trigger_roots":["ر ب ب","ن ح ر"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_purposeful_cut_exposes_premature_cut","source_type":"hft","support_id":"sup_fc287cfced1a3677c692","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَصَلِّ لِرَبِّكَ وَٱنْحَرْ","ayah_ref":"108:2"},{"arabic_uthmani":"إِنَّ شَانِئَكَ هُوَ ٱلْأَبْتَرُ","ayah_ref":"108:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000080/B004","root_000820/B002","root_001479/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001479","role":"Chest facing chest supplies frontal presence and embodied encounter.","root":"ن ح ر","source_ref":"108:2","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000820","role":"Disgusted avoidance supplies the opposite motion of recoil and distance.","root":"ش ن ء","source_ref":"108:3","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_000080","role":"Severing kinship turns bodily retreat into a broken social bond.","root":"ب ت ر","source_ref":"108:3","source_word_indices":["4"]}],"changed_reading":{"after":"It is also spatially enacted: the one who recoils from encounter breaks the bond and leaves himself on the severed side.","before":"The hater's cutoff is an externally imposed social fate."},"confidence":"exploratory","mechanism":"The chest-facing-chest branch gives the context a bodily geometry of exposed encounter. Against it, the hater's disgusted recoil becomes a refusal to face relation, and severed kinship is the social result of that retreat.","model_id":"d_facing_body_opposes_aversive_retreat","reader_inference":"The packet supplies frontal encounter, aversive retreat, and severed kinship; I infer that refusal to face relation performs the cutoff. A live alternative is that the frontal branch stays a concrete idiom of ن ح ر with no interpersonal geometry.","status":"new","structural_cues":["The facing image is activated by the second imperative immediately before the focus ayah.","The context addresses the recipient directly, while the focus shifts to a third-person hostile agent and emphatically isolates him."],"trigger_roots":["ن ح ر"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_facing_body_opposes_aversive_retreat","source_type":"hft","support_id":"sup_98c51b5c1916eab123eb","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَصَلِّ لِرَبِّكَ وَٱنْحَرْ","ayah_ref":"108:2"},{"arabic_uthmani":"إِنَّ شَانِئَكَ هُوَ ٱلْأَبْتَرُ","ayah_ref":"108:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000080/B001","root_000532/B002","root_000820/B001","root_000880/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000880","role":"The non-dominant split branch supplies heating that straightens or sets a thing, making pressure potentially formative.","root":"ص ل و","source_ref":"108:2","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000532","role":"Nurture and completion constrain the heat image toward formation rather than destruction.","root":"ر ب ب","source_ref":"108:2","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000820","role":"Enmity supplies the adversarial pressure whose intended effect is being reversed.","root":"ش ن ء","source_ref":"108:3","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000080","role":"Premature cutting confines failure to the hostile undertaking rather than to the addressee's formation.","root":"ب ت ر","source_ref":"108:3","source_word_indices":["4"]}],"changed_reading":{"after":"As a contained material analogy, hostile pressure can be absorbed into the addressee's formation while the hostile undertaking itself fails to finish.","before":"Hostility is merely an external attempt to damage, and the hater is separately cut off."},"confidence":"exploratory","containment":"This is surprising because it activates the non-dominant ص ل ي heat-and-straightening branch beneath a surface act of worship. It remains anchored through focus hostility and premature cutting, with lordly completion supplying the opposite outcome. Render it only as a material analogy in which pressure may form the addressee while the hostile project fails, never as a replacement gloss for the imperative.","focus_anchor":"The focus joins hostile force from ش ن ء to a ب ت ر predicate of failure before completion.","outlier_id":"o_hostile_heat_becomes_formative_pressure"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:o_hostile_heat_becomes_formative_pressure","source_type":"hft","support_id":"sup_e7edf6676a6d0470ba4d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّآ أَعْطَيْنَٰكَ ٱلْكَوْثَرَ","ayah_ref":"108:1"},{"arabic_uthmani":"فَصَلِّ لِرَبِّكَ وَٱنْحَرْ","ayah_ref":"108:2"},{"arabic_uthmani":"إِنَّ شَانِئَكَ هُوَ ٱلْأَبْتَرُ","ayah_ref":"108:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000080/B004","root_000537/B007","root_000820/B001","root_001028/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001028","role":"Service and handing to family supply circulation of benefit through a household relation.","root":"ع ط و","source_ref":"108:1","source_word_indices":["2"]},{"branch_id":"B007","mapped_root_id":"root_000537","role":"The non-dominant mapped branch supplies an extended household of close kin as the social network.","root":"ر ب ب","source_ref":"108:2","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000820","role":"Enmity supplies the antagonistic relation that refuses household circulation.","root":"ش ن ء","source_ref":"108:3","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_000080","role":"Severing kinship makes the hater's exclusion a broken network tie rather than only lack of descendants.","root":"ب ت ر","source_ref":"108:3","source_word_indices":["4"]}],"changed_reading":{"after":"Cutoff may describe refusal of a circulating household bond: benefit moves through relation while hostility severs its bearer from the network.","before":"Cutoff concerns an individual's missing posterity."},"confidence":"exploratory","containment":"This social reading is branch-distant because it combines service to family with the non-dominant ر ب و household branch. It remains validly anchored in the focus branch of severed kinship and in the same recipient-hostile relation. Render it as a possible network mechanism, not as a historical claim about a particular family or genealogy.","focus_anchor":"The ب ت ر predicate has an explicit severed-kinship branch, while the ش ن ء agent supplies the hostile bond-breaker.","outlier_id":"o_household_circulation_vs_kin_severance"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:o_household_circulation_vs_kin_severance","source_type":"hft","support_id":"sup_32b608df079240a28d59","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّآ أَعْطَيْنَٰكَ ٱلْكَوْثَرَ","ayah_ref":"108:1"},{"arabic_uthmani":"فَصَلِّ لِرَبِّكَ وَٱنْحَرْ","ayah_ref":"108:2"},{"arabic_uthmani":"إِنَّ شَانِئَكَ هُوَ ٱلْأَبْتَرُ","ayah_ref":"108:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000080/B002","root_000532/B008","root_001028/B002","root_001286/B001","root_001479/B009"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001028","role":"Handover supplies transfer from a source toward a recipient.","root":"ع ط و","source_ref":"108:1","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001286","role":"Growth in abundance supplies the expanding effect of what is transferred.","root":"ك ث ر","source_ref":"108:1","source_word_indices":["3"]},{"branch_id":"B008","mapped_root_id":"root_000532","role":"The cloud branch supplies gathered capacity held before release.","root":"ر ب ب","source_ref":"108:2","source_word_indices":["2"]},{"branch_id":"B009","mapped_root_id":"root_001479","role":"A cloud pouring out water supplies release and distribution from the gathered source.","root":"ن ح ر","source_ref":"108:2","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000080","role":"Interrupted good effect identifies the hater as detached from the distributed consequences of abundance.","root":"ب ت ر","source_ref":"108:3","source_word_indices":["4"]}],"changed_reading":{"after":"In the contained ecological analogy, the hater is a severed route outside a gathered-and-released flow whose effects keep spreading.","before":"The hater lacks a private stock of posterity, mention, or good."},"confidence":"exploratory","containment":"This is a cross-domain ecological activation built from remote cloud branches under ر ب ب and ن ح ر. It remains anchored because handover and growth precede a focus predicate of interrupted good effect, and the two cloud branches independently align as storage and release. Render it only as an exploratory flow model, not as a lexical claim that the context nouns or imperatives denote weather.","focus_anchor":"The focus predicate from ب ت ر can mark interruption of a good effect, allowing a distributed-flow analogy to specify what is interrupted.","outlier_id":"o_cloud_release_models_distributed_abundance"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:o_cloud_release_models_distributed_abundance","source_type":"hft","support_id":"sup_3d30bf2c82237f8654ee","trust":"legacy_unbound"}]}
</lane_packet_json>
