# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **112:2**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s112-regular-20260911/s112/112_2/macro.discovery.json` and modify nothing
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
  "ayah_ref": "112:2",
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
{"analysis_context":{"analysis_id":"s112-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"112:2","host_surah":112,"lane_context_refs":["112:0","112:1","112:3","112:4","1:2","1:3","1:4","1:5","1:6","1:7"],"ordered_context_refs":["112:0","112:1","112:3","112:4","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Proper name of the mountain at Medina.","branch_kind":null,"branch_ref":"root_000017/B006","candidate_links":[{"candidate_id":"cand_efcc4fe9a68292fba3cb","lane":"macro"},{"candidate_id":"cand_baf623a2485e8f58d8e4","lane":"macro"}],"focus_root_occurrences":[],"gloss":"Mount Uhud","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"جبل أُحُد","image_en":"Mount Uhud"}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"جبل أُحُد","image_en":"Mount Uhud","scope_ar":"اسم جبل بالمدينة","scope_en":"Proper name of the mountain at Medina."},"support_links":["sup_1a0856210be9e803e446","sup_a615894cd3931903f048"]},{"boundary":"Dal, tapınma eylemi ile bundan türeyen tapınılan veya tapınılır kılınan varlık anlamlarını kapsar; şaşkınlık, yoğun üzüntü ve salt özel ad kullanımları bu sınırın dışındadır.","branch_kind":"mixed_non_bare","branch_ref":"root_000047/B001","candidate_links":[{"candidate_id":"cand_f3696bfca36ea91b97c8","lane":"macro"},{"candidate_id":"cand_69cf89bfc9c4f34ab395","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|NOM","morpheme_role":"STEM","pos":"PN","qac_ref":"112:2:1:1","qac_word_ref":"112:2:1","surface_ar":"ٱللَّهُ"}],"gloss":"tapınma ve tapınılan varlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel eylem, bir varlığa tapınmak ve kişinin kendini bu tapınmaya vermesidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylemden türeyen varlık anlamı, kendisine tapınılan varlığı veya tapınma konusu sayılan nesneyi gösterir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen kullanım, bir varlığı başkalarınca tapınılır duruma getirme veya öyle sunma işlemini bildirir."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Güneşe kimi topluluklarca tapınılması nedeniyle ona tapınılan varlık anlamındaki bir ad verilmesi, varlık anlamının tarihsel bir örneğidir."}}],"root_ar":"ء ل ه","root_id":"root_000047","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Eylem çekirdeğiyle ondan türeyen tapınılan varlık anlamının birlikte temsil edilmesi gereken genel açıklamalarda kullanılır.","boundary_detail":"Dal, tapınma eylemi ile bundan türeyen tapınılan veya tapınılır kılınan varlık anlamlarını kapsar; şaşkınlık, yoğun üzüntü ve salt özel ad kullanımları bu sınırın dışındadır.","branch_image_ar":"التعبد والمعبود","concept_gloss":"tapınma ve tapınılan varlık","contextual_glosses":[{"applicability":"Bir kişinin tapınma eylemini veya kendini tapınmaya vermesini bildiren eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylem olarak tapınma çekirdeğini eksiksiz korur."},"facet_ids":["F001"],"text":"tapınmak","usage_role":"general"},{"applicability":"Bir topluluğun kendisine tapındığı varlık veya nesneden söz edilen ad bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tapınmanın yöneldiği varlık veya nesne anlamını korur."},"facet_ids":["F002"],"text":"tapınılan varlık","usage_role":"contextual"},{"applicability":"Bir varlığın başkalarına tapınma konusu olarak benimsetilmesini anlatan ettirgen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir varlığı tapınma konusu durumuna getirme işlemini korur."},"facet_ids":["F003"],"text":"tapınılır kılmak","usage_role":"explanatory"}],"definition":"Bir varlığa tapınma eylemini ve kişinin kendini tapınmaya vermesini anlatır. Türemiş kullanımlarda bir varlığı tapınılır kılmayı, tapınılan varlığı ve tapınma konusu sayılan varlıkları da adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel eylem, bir varlığa tapınmak ve kişinin kendini bu tapınmaya vermesidir."},{"facet_id":"F002","role":"extension","statement":"Eylemden türeyen varlık anlamı, kendisine tapınılan varlığı veya tapınma konusu sayılan nesneyi gösterir."},{"facet_id":"F003","role":"specialization","statement":"Ettirgen kullanım, bir varlığı başkalarınca tapınılır duruma getirme veya öyle sunma işlemini bildirir."},{"facet_id":"F004","role":"example","statement":"Güneşe kimi topluluklarca tapınılması nedeniyle ona tapınılan varlık anlamındaki bir ad verilmesi, varlık anlamının tarihsel bir örneğidir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Yalnızca belirli bir varlık türünü adlandırdığı için bütün dalın karşılığı sanılabilir.","fit":"narrowing","loses":"Tapınma eylemini, kişinin tapınmaya yönelmesini ve tapınılır kılma işlemini karşılamaz.","preserves":"Tapınılan varlık anlamını kısa ve doğal biçimde korur."},"text":"tanrı"}],"identity_rationale":"Kaynak ifadesi tapınma eylemini, kişinin kendini tapınmaya vermesini, bir varlığı tapınılır kılmayı ve tapınılan varlığı aynı anlam örgüsü içinde açıkça birleştirir. Geçici dal çerçevesi bu çekirdeği ve ondan türeyen varlık adlarını doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tapınmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kendini tapınmaya vermek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"tapınılır kılmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"tapınılan varlık, tanrı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"tapınılan varlık"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"tanrılar, tapınılan nesneler"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"tapınma"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kimi toplulukların tapındığı için bu adla anılan güneş"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"senin tapınman"}],"lexicalization_note":"Tanım, yalın eylem çekirdeğini türemiş eylem ve varlık adlarından ayırır; türemiş biçimlerin kapsamı yalın eylemin tamamına aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Tapınma eylemi, korkuya bağlı özel tapınma yaşayışı ve aynı kökün özel ad dalı sınırı keskinleştirdi; peygamberlik, büyücülük, belirli tapınma nesneleri, sahiplik ve tarihsel hizmet grubu adayları ise yalnızca aynı dinsel alana veya tekil örneklere temas ettiği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal eylem ve yaklaşma yönünde yoğunlaşırken bu dal aynı çekirdekten tapınılan varlık ile ettirgen kılma anlamlarını da türetir; bu yüzden yalnızca eylem bağlamında yakınlaşırlar.","focus_only":"Tapınılan varlığı ve bir varlığı tapınılır kılma işlemini de adlandırır.","gloss":"tapınma ve yaklaşarak yönelme","neighbor_only":"Tapınmayla birlikte yaklaşma ve kendini bu işe verme yönünü öne çıkarır.","neighbor_ref":"root_001498/B001","relation_type":"near_synonym","shared_zone":"İki dal da tapınma eylemini ve kişinin bu eyleme yönelmesini kapsar."},{"boundary_match":"partial","distinction":"Bu dal genel tapınma çekirdeğini ve ondan türeyen varlık anlamlarını kapsar; komşu dal ise korku, inziva ve olağanın üstündeki uygulamalarla sınırlı özel bir yaşayışı anlatır.","focus_only":"Tapınmayı korku, inziva veya aşırı uygulama koşuluna bağlamaz ve tapınılan varlığı da adlandırabilir.","gloss":"korkuyla yoğunlaşan özel tapınma yaşayışı","neighbor_only":"Korkudan doğan, inziva veya ek yüklenme biçimindeki özel bir tapınma yaşayışını bildirir.","neighbor_ref":"root_000604/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da kişinin kendini tapınmaya vermesi bulunur."},{"boundary_match":"partial","distinction":"Bu dal genel anlam örgüsünü verir; komşu dal ise o örgüden türemiş özel adı ve adın belirli söz kalıplarındaki kullanımını ayrı bir biçim alanı olarak sınırlar.","focus_only":"Genel tapınma eylemini, tapınılan varlığı ve tapınılır kılmayı kapsar.","gloss":"Yaratıcıya özgü ad ve kullanım kalıpları","neighbor_only":"Yaratıcıya özgü adı ve bu adla kurulan seslenme, dilek ve ant kalıplarını kapsar.","neighbor_ref":"root_000047/B002","relation_type":"near_neighbor","shared_zone":"Özel ad, tapınılan yüce varlık düşüncesi üzerinden bu dalın varlık anlamıyla bağlantılıdır."}],"source_phrase_ar":"أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)","source_summary":"Kaynakların ortak çizgisi, tapınmayı anlamın temeli sayar; kişinin tapınmaya yönelmesini, tapınılan varlığı ve tapınılır kılma işlemini bu temelden türetir. Tapınma konusu sayılan yontular ve güneş örneği, varlık anlamının belirli uygulamalarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه أله وتأله بمعنى عبد وتنسك، والتأليه بمعنى التعبيد، والإله والآلهة والإلاهة لما جعل معبودا.","what_is_not_ar":"لا يدخل فيه أله بمعنى تحير، ولا ألهت على فلان بمعنى اشتد جزعي عليه، ولا أسماء المواضع أو الحية أو الهلال إلا من جهة التسمية لا معنى العبادة."},"support_links":["sup_1bef9dae4403b8349275","sup_ff2a388e186f88f5eb67"]},{"boundary":"Dal, özel ad ile bu ada bağlı seslenme, dilek, şaşma ve ant biçimleriyle sınırlıdır; herhangi bir tapınılan varlığı gösteren genel ad anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000047/B002","candidate_links":[{"candidate_id":"cand_f3696bfca36ea91b97c8","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|NOM","morpheme_role":"STEM","pos":"PN","qac_ref":"112:2:1:1","qac_word_ref":"112:2:1","surface_ar":"ٱللَّهُ"}],"gloss":"Yaratıcıya özgü ad ile seslenme ve ant biçimleri","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dalın merkezinde, Yaratıcıyı başkalarından ayırarak gösteren ve yalnız ona özgü sayılan özel ad bulunur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Özel adın, tapınılan varlığı bildiren genel addan ses düşmesi ve belirleyici unsur eklenmesiyle oluştuğu açıklanır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özel ad, sözün başında ant değeri taşıyarak ardından gelen yapmama bildirimini güçlendirebilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Özel adın doğrudan ya da seslenme öğesi yerine geçen bir sonla kullanılması, yakarma ve dilek bildiren seslenme biçimleri kurar."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Ses veya parçaların düşürüldüğü kısalmış biçimler, şaşma ve ant anlatan kalıplarda kullanılır."}}],"root_ar":"ء ل ه","root_id":"root_000047","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Özel adın kendisiyle ona bağlı seslenme, dilek ve ant kullanımlarının birlikte açıklanması gereken dal düzeyinde kullanılır.","boundary_detail":"Dal, özel ad ile bu ada bağlı seslenme, dilek, şaşma ve ant biçimleriyle sınırlıdır; herhangi bir tapınılan varlığı gösteren genel ad anlamına genişletilmez.","branch_image_ar":"اسم الله في القسم والنداء","concept_gloss":"Yaratıcıya özgü ad ile seslenme ve ant biçimleri","contextual_glosses":[{"applicability":"Söz konusu adın yalnız Yaratıcıyı gösteren yalın ad olarak ele alındığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Adın Yaratıcıya özgü olmasını ve ayırt edici ad işlevini korur."},"facet_ids":["F001"],"text":"Yaratıcı'nın özel adı","usage_role":"general"},{"applicability":"Yakarış veya dilek sırasında Yaratıcıya doğrudan seslenilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaratıcıya yöneltilen doğrudan seslenme işlevini doğal biçimde korur."},"facet_ids":["F004"],"text":"ey Tanrı","usage_role":"contextual"},{"applicability":"Özel adın bir bildirimin doğruluğunu pekiştiren ant değeri taşıdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaratıcıya dayanarak ant verme işlevini açık biçimde korur."},"facet_ids":["F003"],"text":"Tanrı adına ant olsun","usage_role":"contextual"},{"applicability":"Özel adın ses veya parçaları düşürülmüş tarihsel kalıplarının işlevini açıklarken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kısaltılma biçimini ve şaşma ya da ant işlevini birlikte korur."},"facet_ids":["F005"],"text":"kısaltılmış şaşma veya ant sözü","usage_role":"explanatory"}],"definition":"Yaratıcıya özgü adın kendisini ve bu adla kurulan seslenme, dilek, şaşma ve ant biçimlerini kapsar. Bu biçimler doğrudan seslenme, adın ant değeriyle kullanılması veya ses ve parçaların düşürülmesiyle kısaltılma yollarını gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dalın merkezinde, Yaratıcıyı başkalarından ayırarak gösteren ve yalnız ona özgü sayılan özel ad bulunur."},{"facet_id":"F002","role":"source_variant","statement":"Özel adın, tapınılan varlığı bildiren genel addan ses düşmesi ve belirleyici unsur eklenmesiyle oluştuğu açıklanır."},{"facet_id":"F003","role":"associated_use","statement":"Özel ad, sözün başında ant değeri taşıyarak ardından gelen yapmama bildirimini güçlendirebilir."},{"facet_id":"F004","role":"associated_use","statement":"Özel adın doğrudan ya da seslenme öğesi yerine geçen bir sonla kullanılması, yakarma ve dilek bildiren seslenme biçimleri kurar."},{"facet_id":"F005","role":"source_variant","statement":"Ses veya parçaların düşürüldüğü kısalmış biçimler, şaşma ve ant anlatan kalıplarda kullanılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Genel tür adı olarak başka tapınılan varlıklar için de kullanılabildiğinden özel adla karışır.","fit":"narrowing","loses":"Adın tek bir varlığa özgü özel ad oluşunu ve seslenme ile ant biçimlerini karşılamaz.","preserves":"Yüce bir tapınılan varlığa gönderimde bulunma yönünü korur."},"text":"tanrı"}],"identity_rationale":"Kaynak ifadesi Yaratıcıya özgü adın kendisini, genel tapınılan-varlık adından türetiliş açıklamasını ve bu özel adla kurulan seslenme ile ant biçimlerini birlikte verir. Geçici çerçeve kullanılabilir, ancak dal yalnızca seslenme ve ant kalıpları değildir; özel adın yalın kullanımı da çekirdekte tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"Yaratıcıya özgü ad"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"Tanrı adına ant olsun, bunu yapmadım"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ey Tanrı; yakarma seslenişi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ey Tanrı; doğrudan seslenme"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"Tanrı adına sen veya baban; şaşma ya da ant kalıbı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları"}],"lexicalization_note":"Yalın özel ad, doğrudan seslenme biçimleri ve ant ya da şaşma kalıpları ayrı tutulur; kalıplara özgü işlevler özel adın her kullanımına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Genel tapınma dalı, yaşam üzerine ant, genel seslenme, kısaltılmış kişi seslenmesi ve yakarışa karşılık sözü gerçek sınır karşılaştırmaları sağladı; baba hitapları, genel dışlama yapıları, başka ant sözleri ve sesçe eşlik eden kalıplar daha zayıf ya da yalnızca biçimsel temas gösterdiği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli bir özel adın biçim ve kullanım alanıdır; komşu dal ise özel adla sınırlanmayan genel tapınma eylemini ve tapınılan varlık anlamını verir.","focus_only":"Yaratıcıya özgü adı ve bu adla kurulan seslenme, dilek, şaşma ve ant biçimlerini kapsar.","gloss":"tapınma ve tapınılan varlık","neighbor_only":"Genel tapınma eylemini, tapınılan varlığı ve bir varlığı tapınılır kılma işlemini kapsar.","neighbor_ref":"root_000047/B001","relation_type":"near_neighbor","shared_zone":"Özel ad, tapınılan yüce varlığı göstermesi bakımından genel varlık anlamına dayanır."},{"boundary_match":"partial","distinction":"Ortak işlev ant vermedir, fakat bu dalın dayanağı Yaratıcıya özgü addır; komşu dal yaşam süresini bildiren sözleri kullanır ve ayrıca ısrarlı istemeye uzanabilir.","focus_only":"Ant işlevini Yaratıcıya özgü adın yalın veya kısalmış biçimleriyle kurar.","gloss":"ömür üzerine ant ve ısrarlı isteme","neighbor_only":"Ant veya ısrarlı isteme işlevini yaşam süresini bildiren sözlerle kurar.","neighbor_ref":"root_001044/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir sözü güçlendiren ant işlevli kalıplar içerir."},{"boundary_match":"field_only","distinction":"Bu dal belirli bir muhatabın özel adı çevresinde oluşur; komşu dal ise muhatabın kimliğinden bağımsız genel seslenme araçlarını ve uzaklık ayrımını konu edinir.","focus_only":"Belirli bir özel adı ve o adın yakarma ile ant kullanımlarını içerir.","gloss":"genel seslenme öğeleri","neighbor_only":"Yakın veya uzaktaki muhataba yöneltilen genel seslenme öğelerini bildirir.","neighbor_ref":"root_000074/B008","relation_type":"same_field","shared_zone":"Her iki dal da doğrudan seslenme sırasında kullanılan biçimlerle ilgilidir."},{"boundary_match":"field_only","distinction":"Bu dalın kısalmaları belirli özel adın dinsel seslenme ve ant işlevlerine bağlıdır; komşu dalın kısalmaları ise belirsiz bir kişiye seslenmenin dilbilgisel biçimleridir.","focus_only":"Yaratıcıya özgü adı ve ona bağlı seslenme ile ant biçimlerini kapsar.","gloss":"kişiye yönelik kısaltılmış seslenme","neighbor_only":"Belirsiz bir kişiye yönelen kısaltılmış seslenme biçimlerini kapsar.","neighbor_ref":"root_001178/B003","relation_type":"same_field","shared_zone":"Her iki dalda da seslenme sırasında biçimsel kısalma görülebilir."},{"boundary_match":"thematic_only","distinction":"Bu dal bir muhataba seslenir; komşu dal ise söylenmiş yakarışa kabul dileği veya onayla karşılık verir. Aynı sahnede bulunsalar da anlam çekirdekleri örtüşmez.","focus_only":"Yakarışın yöneltildiği Yaratıcıyı özel adıyla çağırır.","gloss":"yakarışın kabulünü isteyen karşılık","neighbor_only":"Yakarışın kabul edilmesini isteyen veya söyleneni onaylayan karşılık sözünü bildirir.","neighbor_ref":"root_000054/B003","relation_type":"thematic","shared_zone":"İki dal da yakarış ortamında kullanılan kısa söz biçimlerine katılır."}],"source_phrase_ar":"فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)","source_summary":"Kaynaklar özel adı Yaratıcıya özgü bir ad olarak tanımlar ve onu tapınılan varlığı gösteren genel adla köken bakımından ilişkilendirir. Aynı adın doğrudan seslenmede, yakarmada, ant bildiriminde ve parçaları düşürülmüş kalıplarda kullanıldığı birlikte gösterilir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه اسم الله والقول في أصله من إله، وصيغ الاستعمال مثل الله ما فعلت بمعنى والله، واللهم، ويا الله، ولاه أبوك أو لاه أنت ونحوها.","what_is_not_ar":"ليس فرعا مستقلا عن معنى الإله المعبود من جهة الاشتقاق، ولا يدخل فيه إطلاق إله أو آلهة على كل معبود إذا لم يكن الكلام على صيغة الاسم أو النداء أو القسم."},"support_links":["sup_1bef9dae4403b8349275"]},{"boundary":"Dal, yalnızca istemeyi değil, belirli bir hedefe dayanarak yönelmeyi anlatır; katılık, tıkaç, baş sargısı, vurma ve sırf kalıcılık anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000882/B001","candidate_links":[{"candidate_id":"cand_088f8ff19aca87ab1ae2","lane":"macro"},{"candidate_id":"cand_d6ebc2e6cef62b184ba8","lane":"macro"},{"candidate_id":"cand_69cf89bfc9c4f34ab395","lane":"macro"},{"candidate_id":"cand_d4656a4de53e00edf334","lane":"macro"},{"candidate_id":"cand_63634fbcaf8f23a622bc","lane":"macro"},{"candidate_id":"cand_58a7d601560660ef48a5","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"صَّمَد","morph_features":"STEM|POS:N|LEM:S~amad|ROOT:Smd|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:2:2:2","qac_word_ref":"112:2:2","surface_ar":"صَّمَدُ"}],"gloss":"dayanak alarak bir hedefe yönelme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir hedefe bilerek yönelme ve o hedefi dayanak edinme eylemidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İşlerde ve ihtiyaçlarda kendisine yönelinen, topluluğunda üstün konumdaki kişiyi belirtir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsanların dua ve istekle yöneldiği yüce varlığa ilişkin özel bir adlandırmada kullanılır."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İnsanların gitmeyi amaçladığı bir ev, yönelinen ev olarak nitelenebilir."}}],"root_ar":"ص م د","root_id":"root_000882","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın eylemsel çekirdeğini verir; kişi ve özel adlandırma kullanımları bağlama göre ayrıca açıklanır.","boundary_detail":"Dal, yalnızca istemeyi değil, belirli bir hedefe dayanarak yönelmeyi anlatır; katılık, tıkaç, baş sargısı, vurma ve sırf kalıcılık anlamlarını kapsamaz.","branch_image_ar":"القصد إلى المعتمد المقصود","concept_gloss":"dayanak alarak bir hedefe yönelme","contextual_glosses":[{"applicability":"Topluluğunda üstün olan ve meselelerde başvuru mercii sayılan kişi için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Üstün kişi olmayı ve işlerde kendisine yönelinmesini birlikte korur."},"facet_ids":["F002"],"text":"işlerde kendisine başvurulan önder","usage_role":"contextual"},{"applicability":"İnsanların gitmeyi hedeflediği bir evin nitelemesi olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Evin belirli bir yönelişin hedefi oluşunu açıkça korur."},"facet_ids":["F004"],"text":"amaçlanan ev","usage_role":"contextual"}],"definition":"Bir şeyi belirli bir hedef edinerek ona yönelmek ve onu dayanak almaktır. Bundan hareketle, işlerde ve ihtiyaçlarda kendisine başvurulan üstün kişi de yönelinen merci olarak adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir hedefe bilerek yönelme ve o hedefi dayanak edinme eylemidir."},{"facet_id":"F002","role":"extension","statement":"İşlerde ve ihtiyaçlarda kendisine yönelinen, topluluğunda üstün konumdaki kişiyi belirtir."},{"facet_id":"F003","role":"specialization","statement":"İnsanların dua ve istekle yöneldiği yüce varlığa ilişkin özel bir adlandırmada kullanılır."},{"facet_id":"F004","role":"example","statement":"İnsanların gitmeyi amaçladığı bir ev, yönelinen ev olarak nitelenebilir."}],"identity_rationale":"Kaynak ifadesi, bir hedefe bilerek yönelme ve onu dayanak edinme çekirdeğini; ayrıca iş ve ihtiyaçlarda kendisine yönelinen üstün kişiyi açıkça bir arada verir. Verilen dal çerçevesi bu çekirdeği ve ondan gelişen kişi kullanımını doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"amaç edinme ve dayanarak yönelme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"onu amaçlayıp ona dayanarak yöneldi"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"işlerde kendisine başvurulan en üstün kişi"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"işlerde kendisine yönelinen kişi veya amaçlanan şey"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"amaçlanıp gidilen ev"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kulların dua ve istekle yöneldiği yüce varlığın adı"}],"lexicalization_note":"Tanım, hedefe yönelme çekirdeğini temel alır; kendisine başvurulan üstün kişi, amaçlanan ev ve özel adlandırma gibi biçime ya da belirli kullanıma bağlı yönleri ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan iki karşılaştırma, yönelişin sığınmadan ve önderlikte salt öncelikten ayrıldığı sınırları en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal amaçlama ve dayanma ilişkisini genel olarak kurar; komşu dal ise tehlike veya korku karşısında korunma ve yardım arayışını anlatır.","focus_only":"Yöneliş herhangi bir hedefe ya da işlerde başvurulan üstün kişiye olabilir ve acil korku şartı taşımaz.","gloss":"hedefe yönelme ile sığınma","neighbor_only":"Komşu dal, korkutucu bir durumda yardım için sığınılan kişi veya yere özgüdür.","neighbor_ref":"root_001152/B003","relation_type":"near_neighbor","shared_zone":"Her ikisinde de bir kişi ya da yer, kendisine yönelinen odak olabilir."},{"boundary_match":"field_only","distinction":"Buradaki ayırt edici ilişki başvuru ve yöneliştir; komşuda ise anılma sırasındaki öncelik belirleyicidir.","focus_only":"Üstün kişi, başkalarının iş ve ihtiyaçlarda kendisine yönelmesi bakımından adlandırılır.","gloss":"başvurulan önder ile önce anılan önder","neighbor_only":"Komşu dalda üstün kişi, önceliği nedeniyle adı ilk anılan kişidir.","neighbor_ref":"root_000091/B003","relation_type":"same_field","shared_zone":"İki dal da topluluk içinde üstün ve önde gelen bir kişiyi konu eder."}],"source_phrase_ar":"الصمد القصد وصمدته صمدا (maqayis); وصمدت قصدت وصمدت صمد كذا أي قصدت قصده واعتمدته (ayn); صمده يصمده صمدا أي قصده والصمد السيد لأنه يصمد إليه في الحوائج وبيت مصمد أي مقصود (sihah); الصمد السيد الذي قد انتهى سؤدده والذي يصمد إليه الأمر وصمدت صمد هذا الأمر أي قصدت قصده واعتمدته (tahdhib); الصمد السيد الذي يصمد إليه في الأمر وصمده قصد معتمدا عليه قصده (mufradat)","source_summary":"Kaynakların ortak çizgisi, hedefe yönelmeyi dayanak ve amaç ilişkisiyle kurar. Kişi kullanımında üstünlük, başkalarının iş ve ihtiyaçlarında o kişiye yönelmesiyle anlam kazanır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"قصد الشيء واعتماده؛ السيد الذي يقصد إليه في الأمور والحوائج؛ الصمد من جهة الصمود إليه","what_is_not_ar":"الصلابة وانعدام الجوف؛ المكان الصلب؛ الصماد عفاص القارورة؛ خرقة الرأس؛ الضرب بالعصا؛ الدوام المجرد"},"support_links":["sup_030f748f86f810cfd95d","sup_1bf4543365054975cbdc","sup_4b7092422c0c3c34ae0a","sup_63de50bd450f8d4f43f7","sup_bf4bb823003955e2c4d4","sup_ff2a388e186f88f5eb67"]},{"boundary":"Dal genel bir katılık sözünden daha dardır: yoğun, oyuksuz ya da yarıksız bütünlük belirleyicidir; yönelme, kapatma, sarma, vurma ve kalıcılık bu sınıra girmez.","branch_kind":"bare","branch_ref":"root_000882/B002","candidate_links":[{"candidate_id":"cand_efcc4fe9a68292fba3cb","lane":"macro"},{"candidate_id":"cand_8881b175ace608d50653","lane":"macro"},{"candidate_id":"cand_98c30129ed8b24028224","lane":"macro"},{"candidate_id":"cand_d3b5015d11ff0d408a4f","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"صَّمَد","morph_features":"STEM|POS:N|LEM:S~amad|ROOT:Smd|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:2:2:2","qac_word_ref":"112:2:2","surface_ar":"صَّمَدُ"}],"gloss":"içi boş olmayan katı bütünlük","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Katı, yoğun, içi boş olmayan ve yarık taşımayan bütünlük niteliğidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sert ya da yüksek ve kalın bir yerin fiziksel niteliğini belirtir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yere sağlam oturmuş kaya ile çetin ve sert zemin bu niteliğin örnekleridir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Dağın kalın bölümünden alçalıp düzleşen ve üzerinde ağaç yetişen arazi parçası özel bir yer kullanımıdır."}}],"root_ar":"ص م د","root_id":"root_000882","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın nesne ve yer kullanımlarını birleştiren fiziksel çekirdeği karşılar.","boundary_detail":"Dal genel bir katılık sözünden daha dardır: yoğun, oyuksuz ya da yarıksız bütünlük belirleyicidir; yönelme, kapatma, sarma, vurma ve kalıcılık bu sınıra girmez.","branch_image_ar":"الصلابة المكتنزة بلا جوف","concept_gloss":"içi boş olmayan katı bütünlük","contextual_glosses":[{"applicability":"Sert ya da yüksek ve kalın bir yerin anlatıldığı arazi bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dalın başka nesnelerdeki boşluksuz ve yoğun bütünlük kapsamını dışarıda bırakır.","preserves":"Yer kullanımındaki sertlik ve yükselti ya da kalınlık özelliklerini korur."},"facet_ids":["F002"],"text":"sert ve yüksekçe arazi","usage_role":"contextual"},{"applicability":"Toprakla aynı düzeyde sağlam duran kaya örneği için uygun bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel nitelik ile diğer sert yer ve nesne kullanımlarını dışarıda bırakır.","preserves":"Kayanın yere sağlam oturmuş ve sert oluşunu korur."},"facet_ids":["F003"],"text":"yere oturmuş kaya","usage_role":"contextual"}],"definition":"Bir şeyin katı, yoğun ve iç boşluğu ya da yarığı bulunmayan bir bütün oluşturmasıdır. Sert, yüksek ve kalın yerler ile yere sağlam oturmuş kaya ve çetin zemin bu niteliğin yer örnekleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Katı, yoğun, içi boş olmayan ve yarık taşımayan bütünlük niteliğidir."},{"facet_id":"F002","role":"specialization","statement":"Sert ya da yüksek ve kalın bir yerin fiziksel niteliğini belirtir."},{"facet_id":"F003","role":"example","statement":"Yere sağlam oturmuş kaya ile çetin ve sert zemin bu niteliğin örnekleridir."},{"facet_id":"F004","role":"source_variant","statement":"Dağın kalın bölümünden alçalıp düzleşen ve üzerinde ağaç yetişen arazi parçası özel bir yer kullanımıdır."}],"identity_rationale":"Kaynak ifadesi katılık, yoğun bütünlük ve iç boşluğunun bulunmamasını doğrudan bildirir; sert veya yüksek ve kalın yer, yere oturmuş kaya ve yarıktan yoksun sert yüzey örnekleri de bu çekirdeğe bağlıdır. Verilen dal çerçevesi kaynak kapsamını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"sert veya yüksek ve kalın yer"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"içi boş ve yüzeyi yarık olmayan katı şey"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"içi boş olmayan"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yere sağlam oturmuş düz kaya"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"dağın kalın bölümünden alçalıp düzleşen ağaçlı arazi"}],"lexicalization_note":"Tanım çıplak dalın katı, yoğun ve içi boş olmayan bütünlük çekirdeğiyle sınırlıdır; belirli nesne ve yer örnekleri bu çekirdeğin gerçekleşmeleridir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen karşılaştırmalar boşluksuz katılığı yoğunluk, kalınlık ve kazıyı durduran sert zemin kavramlarından ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal boşluksuz bütünlüğü ve sert yerleri merkez alır; komşu dal yoğunlaşmayı daha çeşitli gövde ve topluluk örneklerine yayar.","focus_only":"İç boşluğunun bulunmaması ile sert, yüksek veya kalın yer ve zemin kullanımları bu dalda açıkça yer alır.","gloss":"boşluksuz katılık ile sıkı yoğunluk","neighbor_only":"Komşu dal, boru içinin doluluğundan sıkışık topluluğa kadar gövde yoğunluğu ve aralık azlığına uzanır.","neighbor_ref":"root_000884/B003","relation_type":"near_synonym","shared_zone":"İki dal da katı, sıkı ve boşluğu az bir fiziksel yapıyı anlatabilir."},{"boundary_match":"partial","distinction":"Burada yapıdaki boşluksuz katılık öndedir; komşuda cismin kalınlığı ve bunun akış ya da uzama üzerindeki etkisi öndedir.","focus_only":"Bu dalda iç boşluğu ve yarık bulunmaması belirleyici olabilir.","gloss":"katı bütünlük ile kalınlık","neighbor_only":"Komşu dal kalınlık ve iriliği, ayrıca akmayı veya uzamayı önleme sonuçlarını kapsar.","neighbor_ref":"root_000196/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal sertlik, yoğunluk ve kalınlık alanında kesişebilir."},{"boundary_match":"field_only","distinction":"Bu dal zeminin niteliğini adlandırır; komşu dal ise kazma eyleminin bu nitelik yüzünden durduğu olayı anlatır.","focus_only":"Sert zemin, bu dalda genel fiziksel niteliğin doğrudan bir yer gerçekleşmesidir.","gloss":"sert zemin ile kazı engeli","neighbor_only":"Komşu dal, kazının sert zemin veya dağa ulaşıp artık ilerleyememesi olayını gerektirir.","neighbor_ref":"root_000217/B005","relation_type":"same_field","shared_zone":"İki dal da sert toprak ya da dağ zeminiyle ilgilidir."}],"source_phrase_ar":"الصلابة في الشيء والصمد كل مكان صلب (maqayis); المصمت الذي ليس بأجوف والصمدة صخرة راسية (ayn); الصمد المكان المرتفع الغليظ والمصمد لغة في المصمت وهو الذي لا جوف له (sihah); المصمت الذي لا جوف له والمكان المرتفع الغليظ والمصمد الصلب الذي ليس فيه خدد والشديد من الأرض (tahdhib); الصمد الذي ليس بأجوف (mufradat)","source_summary":"Ortak anlatım katılığı, yoğunluğu ve boşluksuz bütünlüğü birleştirir. Yer kullanımları sert veya yüksek ve kalın araziyi; somut örnekler ise yere oturmuş kaya, yarıksız sert yüzey ve çetin zemini gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الصلابة والاكتناز وانعدام الجوف؛ المكان الصلب أو المرتفع الغليظ؛ الصخرة الراسية والأرض الشديدة","what_is_not_ar":"القصد إلى الشيء والسؤدد المقصود؛ الصماد بمعنى عفاص القارورة أو خرقة الرأس؛ الضرب بالعصا؛ الدوام"},"support_links":["sup_1a0856210be9e803e446","sup_3ee39c2204f5b7bb7ff3","sup_9f8ca522212e6058a1f3","sup_ba0eac616e1904fe1c14"]},{"boundary":"Dal yalnızca şişenin ağzındaki kapatma parçasına ve bu parçayla kapatma işlemine bağlıdır; genel kapatma, katılık veya başı bezle sarma anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000882/B003","candidate_links":[{"candidate_id":"cand_70cdcd5e0e44461106c0","lane":"macro"},{"candidate_id":"cand_a636d876580a77e74354","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"صَّمَد","morph_features":"STEM|POS:N|LEM:S~amad|ROOT:Smd|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:2:2:2","qac_word_ref":"112:2:2","surface_ar":"صَّمَدُ"}],"gloss":"şişe ağzı tıkacı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Şişenin ağzını sıkıca kapatan tıkaç ya da kapatma parçasıdır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Şişeye bu kapatma parçasını takarak ağzını kapatma eylemidir."}}],"root_ar":"ص م د","root_id":"root_000882","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın nesne çekirdeğini kısa ve doğal biçimde karşılar; kapatma eylemi ayrıca verilir.","boundary_detail":"Dal yalnızca şişenin ağzındaki kapatma parçasına ve bu parçayla kapatma işlemine bağlıdır; genel kapatma, katılık veya başı bezle sarma anlamına genişletilmez.","branch_image_ar":"سدادة القارورة المحكمة","concept_gloss":"şişe ağzı tıkacı","contextual_glosses":[{"applicability":"Şişeye kapatma parçası takma eyleminin anlatıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Şişeye tıkaç takma işlemini ve bunun kapatma sonucunu korur."},"facet_ids":["F002"],"text":"şişeyi tıkaçla kapatmak","usage_role":"contextual"}],"definition":"Şişenin ağzına geçirilen ve içeriği dış etkilerden koruyarak ağzı kapatan tıkaçtır. Buna bağlı eylem, şişeye böyle bir tıkaç takıp ağzını kapatmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Şişenin ağzını sıkıca kapatan tıkaç ya da kapatma parçasıdır."},{"facet_id":"F002","role":"associated_use","statement":"Şişeye bu kapatma parçasını takarak ağzını kapatma eylemidir."}],"identity_rationale":"Kaynak ifadesi hem şişenin ağzını kapatan tıkacı hem de şişeye bu parçayı takarak ağzını kapatma eylemini verir. Verilen çerçeve nesne ile ona bağlı işlemi doğru biçimde bir arada, ancak ayırt edilebilir olarak tutar.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"şişe ağzı tıkacı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"şişeye tıkaç takıp ağzını kapatmak"}],"lexicalization_note":"Tanım şişe tıkacı adını, şişeyi bu tıkaçla kapatma kullanımından ayırır; işlem anlamı bağımsız bir genel kapatma fiili sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen iki komşu, şişeye özgü tıkaç ve takma işlemini daha geniş kapatıcı araç alanından ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal şişeye ve ona tıkaç takma işlemine bağlıdır; komşu dalın kap ve kuyu kapsamı daha geniştir.","focus_only":"Bu dal hem şişe tıkacını hem de şişeyi o parçayla kapatma eylemini içerir.","gloss":"şişe tıkacı","neighbor_only":"Komşu dal tıkaç parçasını başka bir kap türüyle ve kuyu bağlamıyla da ilişkilendirir.","neighbor_ref":"root_000840/B018","relation_type":"near_synonym","shared_zone":"İki dal da dar ağızlı bir kabın ağzını kapatan parçayı adlandırır."},{"boundary_match":"partial","distinction":"Burada kapatılan açıklık şişenin ağzıdır; komşuda fiziksel veya mecazlı çok çeşitli eksiklik ve açıklıklar söz konusudur.","focus_only":"Belirli nesne şişe tıkacıdır ve buna bağlı takma eylemi de dalın parçasıdır.","gloss":"şişe tıkacı ile boşluk kapatıcı","neighbor_only":"Komşu dal delik, gedik, geçit ve ihtiyaç gibi çok çeşitli boşlukları gideren araçları kapsar.","neighbor_ref":"root_000687/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir açıklığı kapatan araç düşüncesi bulunur."}],"source_phrase_ar":"الصماد عفاص القارورة وصمدتها صمدا (ayn); الصماد عفاص القارورة (sihah); الصماد سداد القارورة والصماد عفاص القارورة وقد صمدتها أصمدها (tahdhib)","source_summary":"Kaynaklar şişe ağzındaki tıkaç konusunda birleşir; aktarılan fiil kullanımı da şişeye bu parçayı takıp ağzını kapatmayı anlatır.","sources":["AY","SI","TA"],"what_is_ar":"الصماد بمعنى عفاص القارورة أو سدادها؛ فعل صمد القارورة أي جعل لها صمادا","what_is_not_ar":"القصد والسؤدد؛ الصلابة العامة؛ خرقة الرأس؛ الضرب بالعصا؛ الدوام"},"support_links":["sup_b6032205f2fd34f3aa82","sup_c3cb483585e5972e0b41"]},{"boundary":"Sarma işlemi başa ve sarık dışındaki bir bez, mendil ya da kumaşa özgüdür; şişe tıkacı, genel örtme ve sarık sarma bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000882/B004","candidate_links":[{"candidate_id":"cand_ebf3ac787bc5050437f9","lane":"macro"},{"candidate_id":"cand_4a2eac32468cb9b8bb2c","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"صَّمَد","morph_features":"STEM|POS:N|LEM:S~amad|ROOT:Smd|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:2:2:2","qac_word_ref":"112:2:2","surface_ar":"صَّمَدُ"}],"gloss":"başı sarık dışındaki bezle sarma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başı bez, mendil veya kumaşla çevreleyip sarma eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kullanılan baş sargısı sarık değildir; başka tür bir bez, mendil veya kumaştır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başı sarmakta kullanılan bez, mendil veya kumaş parçasının adıdır."}}],"root_ar":"ص م د","root_id":"root_000882","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın işlem çekirdeğini ve sarığı dışlayan araç sınırını birlikte karşılar.","boundary_detail":"Sarma işlemi başa ve sarık dışındaki bir bez, mendil ya da kumaşa özgüdür; şişe tıkacı, genel örtme ve sarık sarma bu dala girmez.","branch_image_ar":"شد الرأس بصماد","concept_gloss":"başı sarık dışındaki bezle sarma","contextual_glosses":[{"applicability":"Başı sarmakta kullanılan bez, mendil veya kumaş parçası için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Parçanın başı sarmak için kullanılan bir kumaş olmasını korur."},"facet_ids":["F003"],"text":"baş sargısı","usage_role":"contextual"}],"definition":"Başı, sarık sayılmayan bir bez, mendil ya da kumaş parçasıyla çevreleyip sarmaktır. Bu işte kullanılan kumaş parçası da baş sargısı olarak adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başı bez, mendil veya kumaşla çevreleyip sarma eylemidir."},{"facet_id":"F002","role":"specialization","statement":"Kullanılan baş sargısı sarık değildir; başka tür bir bez, mendil veya kumaştır."},{"facet_id":"F003","role":"associated_use","statement":"Başı sarmakta kullanılan bez, mendil veya kumaş parçasının adıdır."}],"identity_rationale":"Kaynak ifadesi başın bez, mendil veya kumaşla sarılmasını ve kullanılan sargı parçasını açıkça belirtir; sarığı ise özellikle dışarıda bırakır. Verilen dal çerçevesi bu işlem, araç ve dışlama sınırını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"başını sarık dışındaki bir bezle sardı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"sarık olmayan bez baş sargısı"}],"lexicalization_note":"Tanım, başı belirli bir kumaş parçasıyla sarma kullanımını ve bu işte kullanılan sargıyı ayırır; anlam genel sarma ya da örtmeye genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan karşılaştırmalar bu baş sargısını genel bağlama ve çene altından geçirilen sarık kullanımından ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın konusu yalnızca baş ve sarık dışındaki sargıdır; komşu dalın işlemi, nesnesi ve başlık türleri çok daha geniştir.","focus_only":"Bu dal başı bezle sarmaya özgüdür ve sarığı açıkça dışarıda bırakır.","gloss":"baş sargısı ile genel bağlama","neighbor_only":"Komşu dal baş dışında da bağlama, burma ve sıkıca katlamaya uzanır; sarık ve benzeri başlıkları da kapsar.","neighbor_ref":"root_001018/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir kumaş ya da bağla çevreleyip sıkı tutma düşüncesi bulunur."},{"boundary_match":"field_only","distinction":"Burada sarık özellikle dışlanır; komşu dal ise sarığın çene altından geçirilmesini kurucu koşul olarak taşır.","focus_only":"Baş, sarık sayılmayan bir bez veya kumaşla sarılır.","gloss":"bez baş sargısı ile çene altı sarığı","neighbor_only":"Komşu dalda sarık çene altından geçirilerek belirli bir sarma düzeni kurulur.","neighbor_ref":"root_001350/B003","relation_type":"same_field","shared_zone":"İki dal da baş çevresinde kumaşla yapılan bir sarma biçimini anlatır."}],"source_phrase_ar":"صمد رأسه تصميدا وذلك إذا لف رأسه بخرقة أو منديل أو ثوب ما خلا العمامة وهي الصماد (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, başın bez, mendil veya kumaşla sarıldığını ve bu parçanın sarık olmadığını özellikle belirtir."}],"source_summary":"Aktarılan kullanım başı kumaşla sarma işlemini, kullanılan baş sargısını ve sarığın kapsam dışında tutulmasını birlikte bildirir.","sources":["TA"],"what_is_ar":"تصميد الرأس بخرقة أو منديل أو ثوب دون العمامة","what_is_not_ar":"عفاص القارورة؛ القصد؛ الصلابة؛ الضرب بالعصا؛ الدوام"},"support_links":["sup_3af6d4338a0b1243cda7","sup_cc3f7f04cdb9092703fb"]},{"boundary":"Dal belirli bir söz kalıbına bağlı olarak bir işin başında bulunma ve ona özen gösterme birlikteliğini anlatır; genel yönetim veya salt önemseme değildir.","branch_kind":"non_bare","branch_ref":"root_000882/B005","candidate_links":[{"candidate_id":"cand_4c54829f192041193fa8","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"صَّمَد","morph_features":"STEM|POS:N|LEM:S~amad|ROOT:Smd|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:2:2:2","qac_word_ref":"112:2:2","surface_ar":"صَّمَدُ"}],"gloss":"bir işin başında durup ona özen gösterme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir işin üzerinde bulunup gidişini gözetmektir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gözetilen işe önem vermek ve onunla özenle ilgilenmek kurucu bir koşuldur."}}],"root_ar":"ص م د","root_id":"root_000882","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Verilen özel kullanımın gözetim ve özen bileşenlerini birlikte karşılar.","boundary_detail":"Dal belirli bir söz kalıbına bağlı olarak bir işin başında bulunma ve ona özen gösterme birlikteliğini anlatır; genel yönetim veya salt önemseme değildir.","branch_image_ar":"الإشراف على الأمر مع الحفل به","concept_gloss":"bir işin başında durup ona özen gösterme","contextual_glosses":[{"applicability":"Bir kişinin sorumlu biçimde bir işin gidişiyle ilgilendiği bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gözetim ile önem ve özen göstermeyi birlikte korur."},"facet_ids":["F001","F002"],"text":"işi gözetip önemsemek","usage_role":"contextual"}],"definition":"Bir işin başında bulunarak onu gözetmek ve aynı zamanda o işe önem verip özen göstermektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir işin üzerinde bulunup gidişini gözetmektir."},{"facet_id":"F002","role":"core","statement":"Gözetilen işe önem vermek ve onunla özenle ilgilenmek kurucu bir koşuldur."}],"identity_rationale":"Kaynak ifadesi bir işin üzerinde bulunup onu gözetmeyi, aynı zamanda o işe önem ve özen vermeyi birlikte şart koşar. Verilen dal çerçevesi, yalnızca yönelme ya da ilgilenme değil, gözetim ile özenin birleştiği bu özel kullanımı doğru aktarır.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bir işin başında durup ona özen gösteren"}],"lexicalization_note":"Tanım yalnızca verilen söz kalıbındaki işin başında bulunma ve ona özen gösterme anlamına bağlıdır; çıplak köke bağımsız bir gözetim anlamı yüklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen ilişkiler özenli iş gözetimini genel idareden ve resmî göreve getirilmeden ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda işe önem verme ve özen gösterme zorunludur; komşu dal daha geniş koruma, bakım ve yönetim görevlerini içerir.","focus_only":"Bu dal belirli bir iş üzerinde bulunmayı ve o işe gönülden önem vermeyi birlikte gerektirir.","gloss":"özenli iş gözetimi ile genel idare","neighbor_only":"Komşu dal koruma, sürekli bakım, siyasal yönetim ve yetki gibi daha geniş görev ilişkilerini kapsar.","neighbor_ref":"root_001273/B004","relation_type":"near_synonym","shared_zone":"İki dal da bir işin ya da şeyin başında bulunup onunla ilgilenmeyi anlatır."},{"boundary_match":"partial","distinction":"Burada ilişkinin özü fiilî gözetim ve özendir; komşuda görevin verilmesi ve resmî yetki belirleyicidir.","focus_only":"Gözetim, işe önem ve özen göstermeyle tanımlanır; resmî atama şart değildir.","gloss":"özenli gözetim ile göreve atanma","neighbor_only":"Komşu dal resmî bir göreve getirilme ve özellikle kamu işini üstlenme ilişkisini taşır.","neighbor_ref":"root_001046/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal bir işin sorumluluğunu üstlenip onun başında bulunma alanında buluşur."}],"source_phrase_ar":"إني على صمادة من أمر إذا أشرف عليه وحفلت به (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, işin başında bulunma ile o işi önemseyip özenle yürütmeyi aynı kullanım içinde birleştirir."}],"source_summary":"Aktarılan özel kullanım, bir iş üzerinde gözetici konumda bulunmayı o işe içten önem ve özen göstermeyle birleştirir.","sources":["TA"],"what_is_ar":"قولهم على صمادة من أمر لمن أشرف عليه وحفل به","what_is_not_ar":"القصد المجرد؛ الصلابة؛ عفاص القارورة؛ خرقة الرأس؛ الضرب بالعصا"},"support_links":["sup_aeba3cb4dab32b86de2e"]},{"boundary":"Dal değnekle vurma söz öbeğine bağlıdır; genel vurma, kılıçla vurma veya çıplak kökün bağımsız anlamı olarak yorumlanmaz.","branch_kind":"collocation","branch_ref":"root_000882/B006","candidate_links":[{"candidate_id":"cand_baf623a2485e8f58d8e4","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"صَّمَد","morph_features":"STEM|POS:N|LEM:S~amad|ROOT:Smd|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:2:2:2","qac_word_ref":"112:2:2","surface_ar":"صَّمَدُ"}],"gloss":"değnekle vurma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir hedefe vurma eylemi değnek aracılığıyla gerçekleştirilir."}}],"root_ar":"ص م د","root_id":"root_000882","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca değnek aracını içeren söz öbeğinin tam eylem anlamını karşılar.","boundary_detail":"Dal değnekle vurma söz öbeğine bağlıdır; genel vurma, kılıçla vurma veya çıplak kökün bağımsız anlamı olarak yorumlanmaz.","branch_image_ar":"إيقاع الضرب بالعصا","concept_gloss":"değnekle vurma","contextual_glosses":[{"applicability":"Geçmiş zamanda bir hedefe değnekle vurulduğunu anlatan cümlelerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemin hedefini, vurmayı ve değnek aracını doğal cümle biçiminde korur."},"facet_ids":["F001"],"text":"ona değnekle vurdu","usage_role":"contextual"}],"definition":"Bir kişiye ya da nesneye değnek kullanarak vurma eylemidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir hedefe vurma eylemi değnek aracılığıyla gerçekleştirilir."}],"identity_rationale":"Kaynak ifadesi bir kişiye ya da nesneye değnekle vurmayı açıkça ve yalnızca bu araçla kurulan kullanım içinde bildirir. Verilen dal çerçevesi eylemi, aracı ve kullanım sınırını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ona değnekle vurdu"}],"lexicalization_note":"Tanım yalnızca değnek aracını açıkça içeren yapıya bağlıdır; buradan genel bir vurma anlamı ya da başka araçlara uzanan çıplak dal çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen iki yakın ilişki, değnek koşulunu genel vurma ve daha özel çubukla vurma kapsamlarından ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Değnekli bağlamda karşılıklar yakındır; komşu dalın araçsız genel vurma kapsamı bu dalda bulunmaz.","focus_only":"Bu dal yalnızca değnek aracını içeren belirli yapıyla sınırlıdır.","gloss":"değnekle vurma","neighbor_only":"Komşu dal değnekle vurmanın yanında araç belirtilmeyen genel vurma kullanımını da kapsar.","neighbor_ref":"root_001443/B006","relation_type":"near_synonym","shared_zone":"İki dal da bir hedefe değnek kullanarak vurma bağlamında örtüşür."},{"boundary_match":"partial","distinction":"Ortak eylem vurmadır, ancak araç sınırı aynı değildir: bu dal değneği, komşu ise özel olarak ince çubuğu öne çıkarır.","focus_only":"Bu dalda araç genel olarak değnektir ve belirli söz öbeği sınırı korunur.","gloss":"değnekle vurma ile çubukla vurma","neighbor_only":"Komşu dal, daha ince ve belirli bir çubuk türüyle vurmayı gerektirir.","neighbor_ref":"root_001236/B006","relation_type":"near_synonym","shared_zone":"İki dal da sopa türü bir araçla vurma eylemini anlatır."}],"source_phrase_ar":"صمده بالعصا صمدا إذا ضربه بها (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, eylemin değnekle gerçekleştirilen bir vurma olduğunu açıkça sınırlar."}],"source_summary":"Aktarılan kullanım vurma eylemini, kullanılan aracın değnek olması koşuluyla verir.","sources":["TA"],"what_is_ar":"صمده بالعصا بمعنى ضربه بها","what_is_not_ar":"قصد الشيء واعتماده؛ الصلابة؛ السداد؛ الدوام"},"support_links":["sup_a615894cd3931903f048"]},{"boundary":"Genel anlam kalıcılık ve sürekliliktir; soğuk, kıtlık ve sürekli süt verme koşulları yalnızca dişi deveye ilişkin özel kullanıma aittir.","branch_kind":"mixed_non_bare","branch_ref":"root_000882/B007","candidate_links":[{"candidate_id":"cand_86598f2af415568f75df","lane":"macro"},{"candidate_id":"cand_98c30129ed8b24028224","lane":"macro"},{"candidate_id":"cand_6ebb95fdbf1216e10090","lane":"macro"},{"candidate_id":"cand_d3b5015d11ff0d408a4f","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"صَّمَد","morph_features":"STEM|POS:N|LEM:S~amad|ROOT:Smd|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:2:2:2","qac_word_ref":"112:2:2","surface_ar":"صَّمَدُ"}],"gloss":"kalıcı ve sürekli olma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sürekli olma, kalma ve yok oluşa rağmen varlığını koruma niteliğidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişi devenin soğuk ve kıtlık koşullarında varlığını ve dayanıklılığını korumasıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu dişi devenin zorlu koşullarda süt vermeyi kesintisiz sürdürmesi de özel kullanımın parçasıdır."}}],"root_ar":"ص م د","root_id":"root_000882","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın genel çekirdeğini karşılar; dişi deveye özgü dayanma ve süt verme ayrıntıları ayrıca belirtilir.","boundary_detail":"Genel anlam kalıcılık ve sürekliliktir; soğuk, kıtlık ve sürekli süt verme koşulları yalnızca dişi deveye ilişkin özel kullanıma aittir.","branch_image_ar":"الدوام والبقاء على الشدة","concept_gloss":"kalıcı ve sürekli olma","contextual_glosses":[{"applicability":"Başka varlıklar yok olduktan sonra da varlığını sürdüren için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başkalarının yok oluşundan sonra da kalma sınırını açıkça korur."},"facet_ids":["F001"],"text":"yok oluştan sonra da kalan","usage_role":"contextual"},{"applicability":"Soğuk ve kıtlığa dayanırken süt vermeyi sürdüren dişi deve için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanı, zorlu koşullara dayanmayı ve kesintisiz süt vermeyi birlikte korur."},"facet_ids":["F002","F003"],"text":"zorlu koşullarda sütü kesilmeyen dişi deve","usage_role":"explanatory"}],"definition":"Bir varlığın sürekli olması ve başkaları yok olduktan sonra da varlığını korumasıdır. Dişi deveye ilişkin özel kullanım, soğuk ve kıtlıkta ayakta kalırken süt vermeyi kesintisiz sürdürmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sürekli olma, kalma ve yok oluşa rağmen varlığını koruma niteliğidir."},{"facet_id":"F002","role":"specialization","statement":"Dişi devenin soğuk ve kıtlık koşullarında varlığını ve dayanıklılığını korumasıdır."},{"facet_id":"F003","role":"specialization","statement":"Bu dişi devenin zorlu koşullarda süt vermeyi kesintisiz sürdürmesi de özel kullanımın parçasıdır."}],"identity_rationale":"Kaynak ifadesinin genel çekirdeği sürekli olma ve yok oluştan sonra da kalmadır. Soğuk ve kıtlık altında dayanma ile sütün kesintisiz gelmesi ise yalnızca dişi deve kullanımının kurucu ayrıntılarıdır; bu nedenle dal başlığındaki zorluk altında kalma unsuru genel kalıcılığa yayılmadan sınırlandırılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"sürekli ve yok oluştan sonra da kalan"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"soğuk ve kıtlıkta dayanıp sütü kesilmeyen dişi deve"}],"lexicalization_note":"Tanım genel kalıcı ve sürekli olma biçimini, zorlu koşullara dayanıp sütü sürme anlamındaki dişi deve kullanımından ayırır; özel koşullar genel çekirdeğe katılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen yakın anlamlar genel kalıcılık çekirdeğini uzun ömür, etki, mekânda kalma ve direnme uzantılarından ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Genel kalıcılıkta yakın olsalar da bu dalın yok oluştan sonra kalma ve hayvana özgü dayanma ayrıntıları, komşunun uzun ömür ve etki kapsamından ayrılır.","focus_only":"Bu dal, başkalarının yok oluşundan sonra kalmayı ve dişi devenin zorlu koşullarda sütü sürdürmesini içerir.","gloss":"kalıcı olma ile varlığını sürdürme","neighbor_only":"Komşu dal uzun yaşama, izin veya etkinin kalması ve ödülün sürmesi gibi daha geniş sonuçlara uzanır.","neighbor_ref":"root_000142/B001","relation_type":"near_synonym","shared_zone":"İki dal da yok olmama, kalma ve süreklilik çekirdeğinde büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Bu dal süreklilik ve sonradan da kalma eksenindedir; komşu dal mekânda kalma ve eylem sırasında sağlam durma alanlarına da yayılır.","focus_only":"Bu dalda başkalarının yok oluşundan sonra kalma ve özel hayvan kullanımı bulunur.","gloss":"kalıcılık ile süreğen sağlam duruş","neighbor_only":"Komşu dal bir yerde kalma, savaşta direnme ve ayakların sağlam durması gibi durumları kapsar.","neighbor_ref":"root_000192/B001","relation_type":"near_synonym","shared_zone":"İki dal da devam etme, yok olmama ve varlığını koruma düşüncesini taşır."}],"source_phrase_ar":"الصمد الدائم والدائم الباقي بعد فناء خلقه وناقة مصماد وهي الباقية على القر والجدب الدائمة الرسل (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, genel kalıcılık anlamının yanında soğuk ve kıtlıkta ayakta kalıp sürekli süt veren dişi deve kullanımını aktarır."}],"source_summary":"Aktarılan anlam genel düzeyde süreklilik ve başkalarının yok oluşundan sonra da kalmayı bildirir. Hayvan kullanımında bu çekirdek, soğuk ve kıtlığa dayanma ile süt vermeyi sürdürme ayrıntılarıyla özelleşir.","sources":["TA"],"what_is_ar":"الدوام والبقاء؛ الناقة المصماد الباقية على القر والجدب الدائمة الرسل","what_is_not_ar":"القصد إلى المقصود؛ الصلابة بلا جوف؛ عفاص القارورة؛ خرقة الرأس؛ الضرب بالعصا"},"support_links":["sup_3dbc4de463a160d68f7a","sup_7ae07167a8a81a3707fd","sup_9f8ca522212e6058a1f3","sup_ba0eac616e1904fe1c14"]},{"boundary":"Includes qīl/al-maqul as a Yemeni or Himyarite title, with plurals such as maqawila, aqyal, and aqwal.","branch_kind":null,"branch_ref":"root_001272/B004","candidate_links":[{"candidate_id":"cand_4c54829f192041193fa8","lane":"macro"}],"focus_root_occurrences":[],"gloss":"Yemeni qīl, a titled chief whose word has force","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"القيل صاحب القول النافذ","image_en":"Yemeni qīl, a titled chief whose word has force"}}],"root_ar":"ق و ل","root_id":"root_001272","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"القيل صاحب القول النافذ","image_en":"Yemeni qīl, a titled chief whose word has force","scope_ar":"يدخل فيه المقول أو القيل بلغة أهل اليمن، والواحد القيل، والجمع المقاولة والأقيال والأقوال، وملك حمير دون الملك الأعظم، والمرأة قيلة.","scope_en":"Includes qīl/al-maqul as a Yemeni or Himyarite title, with plurals such as maqawila, aqyal, and aqwal."},"support_links":["sup_aeba3cb4dab32b86de2e"]},{"boundary":"Includes al-qal as the stick used to strike the qilla.","branch_kind":null,"branch_ref":"root_001272/B008","candidate_links":[{"candidate_id":"cand_baf623a2485e8f58d8e4","lane":"macro"}],"focus_root_occurrences":[],"gloss":"the qal stick used in the game of qilla","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"عود القال لضرب القلة","image_en":"the qal stick used in the game of qilla"}}],"root_ar":"ق و ل","root_id":"root_001272","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"عود القال لضرب القلة","image_en":"the qal stick used in the game of qilla","scope_ar":"يدخل فيه القال، الخشبة التي تضرب بها القلة.","scope_en":"Includes al-qal as the stick used to strike the qilla."},"support_links":["sup_a615894cd3931903f048"]},{"boundary":"Includes qawaltuhu and taqawalna when they mean mutual discussion or negotiation about a matter.","branch_kind":null,"branch_ref":"root_001272/B009","candidate_links":[{"candidate_id":"cand_4c54829f192041193fa8","lane":"macro"}],"focus_root_occurrences":[],"gloss":"mutual verbal negotiation","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"المقاولة في الأمر","image_en":"mutual verbal negotiation"}}],"root_ar":"ق و ل","root_id":"root_001272","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"المقاولة في الأمر","image_en":"mutual verbal negotiation","scope_ar":"يدخل فيه قاولته في أمره وتقاولنا إذا تفاوضنا.","scope_en":"Includes qawaltuhu and taqawalna when they mean mutual discussion or negotiation about a matter."},"support_links":["sup_aeba3cb4dab32b86de2e"]},{"boundary":"Includes tilting, overturning, pouring out by turning over, tilting a bow or bowl, diverting people from their direction, swaying motion, and the downcast or changed face/color image.","branch_kind":null,"branch_ref":"root_001305/B002","candidate_links":[{"candidate_id":"cand_baf623a2485e8f58d8e4","lane":"macro"},{"candidate_id":"cand_86598f2af415568f75df","lane":"macro"},{"candidate_id":"cand_58a7d601560660ef48a5","lane":"macro"}],"focus_root_occurrences":[],"gloss":"tilting, overturning, and diverting","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الإمالة والقلب والصرف","image_en":"tilting, overturning, and diverting"}}],"root_ar":"ك ف ء","root_id":"root_001305","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الإمالة والقلب والصرف","image_en":"tilting, overturning, and diverting","scope_ar":"يدخل فيه إمالة الشيء وقلبه وكبه؛ إمالة القوس والصحفة؛ صرف القوم عن وجهتهم؛ التمايل في المشي أو كالسفينة؛ انكسار الوجه وتغير اللون","scope_en":"Includes tilting, overturning, pouring out by turning over, tilting a bow or bowl, diverting people from their direction, swaying motion, and the downcast or changed face/color image."},"support_links":["sup_030f748f86f810cfd95d","sup_7ae07167a8a81a3707fd","sup_a615894cd3931903f048"]},{"boundary":"Includes the kifa cloth, one or two sewn pieces used to cover or form the rear of a tent or dwelling.","branch_kind":null,"branch_ref":"root_001305/B004","candidate_links":[{"candidate_id":"cand_ebf3ac787bc5050437f9","lane":"macro"}],"focus_root_occurrences":[],"gloss":"tent-back covering","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"كِفاء الخباء","image_en":"tent-back covering"}}],"root_ar":"ك ف ء","root_id":"root_001305","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"كِفاء الخباء","image_en":"tent-back covering","scope_ar":"يدخل فيه الكِفاء بمعنى شقة أو شقتين تخاطان ويجعل بهما مؤخر الخباء أو البيت","scope_en":"Includes the kifa cloth, one or two sewn pieces used to cover or form the rear of a tent or dwelling."},"support_links":["sup_3af6d4338a0b1243cda7"]},{"boundary":"Includes place, position, rank, and tamakkun where the sources derive them from kana/yakun.","branch_kind":null,"branch_ref":"root_001332/B002","candidate_links":[{"candidate_id":"cand_efcc4fe9a68292fba3cb","lane":"macro"},{"candidate_id":"cand_4c54829f192041193fa8","lane":"macro"}],"focus_root_occurrences":[],"gloss":"place, position, or rank from being","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"المكان والمكانة من الكون","image_en":"place, position, or rank from being"}}],"root_ar":"ك و ن","root_id":"root_001332","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"المكان والمكانة من الكون","image_en":"place, position, or rank from being","scope_ar":"يدخل فيه المكان والموضع والمكانة والمنزلة والتمكن إذا جعلت من كان يكون.","scope_en":"Includes place, position, rank, and tamakkun where the sources derive them from kana/yakun."},"support_links":["sup_1a0856210be9e803e446","sup_aeba3cb4dab32b86de2e"]},{"boundary":"Includes suretyship, guaranteeing a person, and the form iktana in the same sense.","branch_kind":null,"branch_ref":"root_001332/B003","candidate_links":[{"candidate_id":"cand_4c54829f192041193fa8","lane":"macro"}],"focus_root_occurrences":[],"gloss":"suretyship or undertaking responsibility","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الكفالة والقيام على فلان","image_en":"suretyship or undertaking responsibility"}}],"root_ar":"ك و ن","root_id":"root_001332","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الكفالة والقيام على فلان","image_en":"suretyship or undertaking responsibility","scope_ar":"يدخل فيه الكيانة والكفالة والتكفل بفلان واكتنت به.","scope_en":"Includes suretyship, guaranteeing a person, and the form iktana in the same sense."},"support_links":["sup_aeba3cb4dab32b86de2e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000017/B001","candidate_links":[{"candidate_id":"cand_d4656a4de53e00edf334","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_9f2ae92f8c595ef4a571","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Oneness and unity supply a single pole toward which the focus predicate's directed resort can converge.","root":"ء ح د","source_ref":"112:1","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000017","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_bf4bb823003955e2c4d4"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000017/B002","candidate_links":[{"candidate_id":"cand_d4656a4de53e00edf334","lane":"macro"},{"candidate_id":"cand_8881b175ace608d50653","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_9f2ae92f8c595ef4a571","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Exhaustive negation removes any leftover instance that could serve as a coordinate endpoint.","root":"ء ح د","source_ref":"112:4","source_word_indices":["5"]},{"hft_ref":"hft_8bb732226fb7ee9f050c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Exhaustive negation prevents an unmentioned constituent or peer from casually remaining outside the unity claim.","root":"ء ح د","source_ref":"112:4","source_word_indices":["5"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000017","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_3ee39c2204f5b7bb7ff3","sup_bf4bb823003955e2c4d4"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000017/B003","candidate_links":[{"candidate_id":"cand_8881b175ace608d50653","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_8bb732226fb7ee9f050c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The one as a unit in counting and composition introduces the live question of whether unity is aggregate or integral.","root":"ء ح د","source_ref":"112:1","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000017","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_3ee39c2204f5b7bb7ff3"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001251/B004","candidate_links":[{"candidate_id":"cand_d3b5015d11ff0d408a4f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_c5649d16ef9ab26c6751","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Independently carrying and rising under a load supplies a dynamic load-bearing image from the packet's secondary root mapping.","root":"ق و ل","source_ref":"112:1","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001251","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_ba0eac616e1904fe1c14"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001272/B012","candidate_links":[{"candidate_id":"cand_4a2eac32468cb9b8bb2c","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6f6432efc43c364a1b0a","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Unvoiced saying within oneself supplies an interior recitation-space behind the overt command.","root":"ق و ل","source_ref":"112:1","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001272","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_cc3f7f04cdb9092703fb"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001272/B014","candidate_links":[{"candidate_id":"cand_d6ebc2e6cef62b184ba8","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_1cecc9426ec5c10e0b01","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A thing's 'saying' as its indication makes the commanded utterance point beyond sound to the relation asserted in the focus.","root":"ق و ل","source_ref":"112:1","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001272","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_63de50bd450f8d4f43f7"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001272/B016","candidate_links":[{"candidate_id":"cand_d6ebc2e6cef62b184ba8","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_1cecc9426ec5c10e0b01","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Saying a thing as defining its limit makes the utterance set a conceptual boundary around the focus predicate.","root":"ق و ل","source_ref":"112:1","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001272","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_63de50bd450f8d4f43f7"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001305/B001","candidate_links":[{"candidate_id":"cand_63634fbcaf8f23a622bc","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a810c1636699e87c4109","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Equality and matching opposition supply the possible coordinate pole that the context explicitly negates.","root":"ك ف ء","source_ref":"112:4","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001305","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_1bf4543365054975cbdc"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001332/B001","candidate_links":[{"candidate_id":"cand_6ebb95fdbf1216e10090","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_7addfa2f5379473c46d3","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Occurrence or presence in time supplies the temporal field across which the negated counterpart fails to appear.","root":"ك و ن","source_ref":"112:4","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001332","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_3dbc4de463a160d68f7a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001683/B003","candidate_links":[{"candidate_id":"cand_98c30129ed8b24028224","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6f60ecdd37081c800b9d","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The event of birth supplies the concrete incoming and outgoing transitions canceled by the paired verbal forms.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001683","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_9f8ca522212e6058a1f3"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001683/B005","candidate_links":[{"candidate_id":"cand_98c30129ed8b24028224","lane":"macro"},{"candidate_id":"cand_a636d876580a77e74354","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6f60ecdd37081c800b9d","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Something obtained or newly produced from something else generalizes lineage into derivation and lets the two negations test causal dependence.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]},{"hft_ref":"hft_217c5a55b8ebf66c65b8","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Something derived or newly produced from another supplies the causal throughput canceled in both directions by the context.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001683","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_9f8ca522212e6058a1f3","sup_b6032205f2fd34f3aa82"]}],"candidate_inventory":[{"anchor_refs":["112:1","112:2","112:4"],"branch_refs":["root_000017/B006","root_000882/B002","root_001332/B002"],"candidate_id":"cand_efcc4fe9a68292fba3cb","commentary_obligation":"review","focus_branch_refs":["root_000882/B002"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000017/B006","root_001332/B002"],"root_ids":[],"scope":"pericope","source_local_id":"A:Cavityless Solidity and Anchored Terrain","source_type":"channel","support_ids":["sup_18bd56aae82af75aed78","sup_1a0856210be9e803e446","sup_1dccd4b489e0526a9d0a","sup_ef9c0f0d3c4b0d250494","sup_f10881522267002dad0f"],"title":"Cavityless Solidity and Anchored Terrain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["112:1","112:2","112:4"],"branch_refs":["root_000017/B006","root_000882/B006","root_001272/B008","root_001305/B002"],"candidate_id":"cand_baf623a2485e8f58d8e4","commentary_obligation":"review","focus_branch_refs":["root_000882/B006"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000017/B006","root_001272/B008","root_001305/B002"],"root_ids":[],"scope":"pericope","source_local_id":"A:Striking and Redirection","source_type":"channel","support_ids":["sup_1597e1f26b9a7af2b72a","sup_66bf252d3f03a98fddf8","sup_8cdd408f6919a5461749","sup_a615894cd3931903f048","sup_f8c965c775c0f4ee340a"],"title":"Striking and Redirection","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["112:1","112:2"],"branch_refs":["root_000047/B001","root_000047/B002"],"candidate_id":"cand_f3696bfca36ea91b97c8","commentary_obligation":"review","focus_branch_refs":["root_000047/B001","root_000047/B002"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":[],"root_ids":[],"scope":"pericope","source_local_id":"A:Worship and the Invoked Divine Name","source_type":"channel","support_ids":["sup_1bef9dae4403b8349275","sup_395720d0afec54652862","sup_3e913ef8198ac10a8683","sup_b8f4b63ff762260c906f","sup_e9768bff321cf768b5aa"],"title":"Worship and the Invoked Divine Name","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["112:2","112:4"],"branch_refs":["root_000882/B007","root_001305/B002"],"candidate_id":"cand_86598f2af415568f75df","commentary_obligation":"review","focus_branch_refs":["root_000882/B007"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_001305/B002"],"root_ids":[],"scope":"pericope","source_local_id":"B:Bodily Yielding and Endurance","source_type":"channel","support_ids":["sup_36492e638922ecafa6fc","sup_52504d9cb4c61655d993","sup_6b2b9078380eb59f55f6","sup_7ae07167a8a81a3707fd","sup_e4f236e8afd4d585ddc0"],"title":"Bodily Yielding and Endurance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["112:2"],"branch_refs":["root_000882/B001"],"candidate_id":"cand_088f8ff19aca87ab1ae2","commentary_obligation":"review","focus_branch_refs":["root_000882/B001"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":[],"root_ids":[],"scope":"pericope","source_local_id":"B:Sought Patron and Directed Reliance","source_type":"channel","support_ids":["sup_4b7092422c0c3c34ae0a","sup_5a96ce3c24011ceef289","sup_aebf3f6e54edff5b03e5","sup_b3b232819d8563a575d7","sup_b45129aced4f8292ad75"],"title":"Sought Patron and Directed Reliance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["112:2"],"branch_refs":["root_000882/B003"],"candidate_id":"cand_70cdcd5e0e44461106c0","commentary_obligation":"review","focus_branch_refs":["root_000882/B003"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":[],"root_ids":[],"scope":"pericope","source_local_id":"B:Stoppered Vessel","source_type":"channel","support_ids":["sup_1e7e408efcf3b2fa22f0","sup_549623946fa68875127c","sup_86b7a6c6266dd5afa0c6","sup_c3cb483585e5972e0b41","sup_eeb3338460af018ddc54"],"title":"Stoppered Vessel","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["112:2","112:4"],"branch_refs":["root_000882/B004","root_001305/B004"],"candidate_id":"cand_ebf3ac787bc5050437f9","commentary_obligation":"review","focus_branch_refs":["root_000882/B004"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_001305/B004"],"root_ids":[],"scope":"pericope","source_local_id":"C:Fabric Closures for Body and Dwelling","source_type":"channel","support_ids":["sup_1fade16ab31fa07a8c28","sup_3af6d4338a0b1243cda7","sup_543d0fa7387918136e8e","sup_86b68be59ed3789534ce","sup_d4b7c06d83225815f2f9"],"title":"Fabric Closures for Body and Dwelling","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["112:1","112:2","112:4"],"branch_refs":["root_000882/B005","root_001272/B004","root_001272/B009","root_001332/B002","root_001332/B003"],"candidate_id":"cand_4c54829f192041193fa8","commentary_obligation":"review","focus_branch_refs":["root_000882/B005"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_001272/B004","root_001272/B009","root_001332/B002","root_001332/B003"],"root_ids":[],"scope":"pericope","source_local_id":"C:Responsible Authority and Negotiation","source_type":"channel","support_ids":["sup_159df745f54ffadbf270","sup_2ef0e1e43d7abcf72685","sup_4fdbacddd0a0074bc122","sup_aeba3cb4dab32b86de2e","sup_b55a9b9d44d597bf89d8"],"title":"Responsible Authority and Negotiation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["112:1","112:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:2","branch_refs":["root_000882/B001","root_001272/B014","root_001272/B016"],"candidate_id":"cand_d6ebc2e6cef62b184ba8","commentary_obligation":"review","hft_ref":"hft_1cecc9426ec5c10e0b01","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta-speech-as-definition","source_type":"hft","support_ids":["sup_63de50bd450f8d4f43f7"],"title":"delta-speech-as-definition","trust":"legacy_unbound"},{"anchor_refs":["112:1","112:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:2","branch_refs":["root_000047/B001","root_000882/B001"],"candidate_id":"cand_69cf89bfc9c4f34ab395","commentary_obligation":"review","hft_ref":"hft_6f5f7f7982d103d8f748","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta-repeated-referent","source_type":"hft","support_ids":["sup_ff2a388e186f88f5eb67"],"title":"delta-repeated-referent","trust":"legacy_unbound"},{"anchor_refs":["112:1","112:2","112:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:2","branch_refs":["root_000017/B001","root_000017/B002","root_000882/B001"],"candidate_id":"cand_d4656a4de53e00edf334","commentary_obligation":"review","hft_ref":"hft_9f2ae92f8c595ef4a571","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta-single-convergence","source_type":"hft","support_ids":["sup_bf4bb823003955e2c4d4"],"title":"delta-single-convergence","trust":"legacy_unbound"},{"anchor_refs":["112:1","112:2","112:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:2","branch_refs":["root_000017/B002","root_000017/B003","root_000882/B002"],"candidate_id":"cand_8881b175ace608d50653","commentary_obligation":"review","hft_ref":"hft_8bb732226fb7ee9f050c","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta-uncomposed-integrity","source_type":"hft","support_ids":["sup_3ee39c2204f5b7bb7ff3"],"title":"delta-uncomposed-integrity","trust":"legacy_unbound"},{"anchor_refs":["112:2","112:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:2","branch_refs":["root_000882/B002","root_000882/B007","root_001683/B003","root_001683/B005"],"candidate_id":"cand_98c30129ed8b24028224","commentary_obligation":"review","hft_ref":"hft_6f60ecdd37081c800b9d","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta-nonderived-nonemanating","source_type":"hft","support_ids":["sup_9f8ca522212e6058a1f3"],"title":"delta-nonderived-nonemanating","trust":"legacy_unbound"},{"anchor_refs":["112:2","112:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:2","branch_refs":["root_000882/B007","root_001332/B001"],"candidate_id":"cand_6ebb95fdbf1216e10090","commentary_obligation":"review","hft_ref":"hft_7addfa2f5379473c46d3","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta-temporal-invariance","source_type":"hft","support_ids":["sup_3dbc4de463a160d68f7a"],"title":"delta-temporal-invariance","trust":"legacy_unbound"},{"anchor_refs":["112:2","112:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:2","branch_refs":["root_000882/B001","root_001305/B001"],"candidate_id":"cand_63634fbcaf8f23a622bc","commentary_obligation":"review","hft_ref":"hft_a810c1636699e87c4109","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta-asymmetric-dependence","source_type":"hft","support_ids":["sup_1bf4543365054975cbdc"],"title":"delta-asymmetric-dependence","trust":"legacy_unbound"},{"anchor_refs":["112:1","112:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:2","branch_refs":["root_000882/B002","root_000882/B007","root_001251/B004"],"candidate_id":"cand_d3b5015d11ff0d408a4f","commentary_obligation":"review","hft_ref":"hft_c5649d16ef9ab26c6751","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier-split-root-load-bearing","source_type":"hft","support_ids":["sup_ba0eac616e1904fe1c14"],"title":"outlier-split-root-load-bearing","trust":"legacy_unbound"},{"anchor_refs":["112:1","112:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:2","branch_refs":["root_000882/B004","root_001272/B012"],"candidate_id":"cand_4a2eac32468cb9b8bb2c","commentary_obligation":"review","hft_ref":"hft_6f6432efc43c364a1b0a","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier-bound-attention","source_type":"hft","support_ids":["sup_cc3f7f04cdb9092703fb"],"title":"outlier-bound-attention","trust":"legacy_unbound"},{"anchor_refs":["112:2","112:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:2","branch_refs":["root_000882/B003","root_001683/B005"],"candidate_id":"cand_a636d876580a77e74354","commentary_obligation":"review","hft_ref":"hft_217c5a55b8ebf66c65b8","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier-sealed-derivation","source_type":"hft","support_ids":["sup_b6032205f2fd34f3aa82"],"title":"outlier-sealed-derivation","trust":"legacy_unbound"},{"anchor_refs":["112:2","112:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"112:2","branch_refs":["root_000882/B001","root_001305/B002"],"candidate_id":"cand_58a7d601560660ef48a5","commentary_obligation":"review","hft_ref":"hft_b2d88f5a1a6664669921","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier-unturnable-orientation","source_type":"hft","support_ids":["sup_030f748f86f810cfd95d"],"title":"outlier-unturnable-orientation","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_c06e55c1626da8de4191","connection_ref":"conn_45a1bb434b156db2d75b","note":"Immediate sibling context: divine oneness frames 112:2 without selecting among its parallel readings.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_fb4352d7b5f28e2834eb","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"112:1","source_note":"Direct sequel: divine self-sufficiency specifies the identity named in 112:1.","source_row_role":"ranked_review","source_target_component_ref":"112:2","source_target_components":["112:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"112:2"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"112:1","source_target_components":["112:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"112:1","target_evidence":{"arabic_uthmani":"قُلْ هُوَ ٱللَّهُ أَحَدٌ","ayah_ref":"112:1"},"target_ref":"112:1"},{"connection_evidence_ref":"conn_ev_ca74e98b36e7cb401993","connection_ref":"conn_870beef0bfb6df938e5f","note":"Immediate sibling boundary against equivalence reinforces non-composite and non-rival aspects of 112:2.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_015589d485f51ffaa722","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"112:4","source_note":"Self-sufficiency supplies a nearby basis for excluding any equal counterpart.","source_row_role":"ranked_review","source_target_component_ref":"112:2","source_target_components":["112:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"112:2"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"112:4","source_target_components":["112:4"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"112:4","target_evidence":{"arabic_uthmani":"وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ","ayah_ref":"112:4"},"target_ref":"112:4"},{"connection_evidence_ref":"conn_ev_bf3baa4f280a9e4608a7","connection_ref":"conn_28570e2dfdec477baa37","note":"Immediate sibling boundary on begetting and birth; indispensable for f02 and the f03 boundary reading.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_0e54bf681ab470d41d97","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"112:3","source_note":"Immediate self-sufficiency context for the denial in 112:3.","source_row_role":"ranked_review","source_target_component_ref":"112:2","source_target_components":["112:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"112:2"}],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"112:3","source_target_components":["112:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"112:3","target_evidence":{"arabic_uthmani":"لَمْ يَلِدْ وَلَمْ يُولَدْ","ayah_ref":"112:3"},"target_ref":"112:3"}],"focus":{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","qac_morphemes":[{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|NOM","morpheme_role":"STEM","pos":"PN","qac_ref":"112:2:1:1","qac_word_ref":"112:2:1","root_ar":"ء ل ه","surface_ar":"ٱللَّهُ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"112:2:2:1","qac_word_ref":"112:2:2","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"صَّمَد","morph_features":"STEM|POS:N|LEM:S~amad|ROOT:Smd|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:2:2:2","qac_word_ref":"112:2:2","root_ar":"ص م د","surface_ar":"صَّمَدُ"}],"word_analysis_qac_refs":[["112:2:1:1"],["112:2:2:1","112:2:2:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["112:2:1","112:2:2"]},"focus_surface_evidence":{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","qac_morphemes":[{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|NOM","morpheme_role":"STEM","pos":"PN","qac_ref":"112:2:1:1","qac_word_ref":"112:2:1","root_ar":"ء ل ه","surface_ar":"ٱللَّهُ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"112:2:2:1","qac_word_ref":"112:2:2","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"صَّمَد","morph_features":"STEM|POS:N|LEM:S~amad|ROOT:Smd|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"112:2:2:2","qac_word_ref":"112:2:2","root_ar":"ص م د","surface_ar":"صَّمَدُ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["112:2:1:1"],["112:2:2:1","112:2:2:2"]],"word_analysis_refs":["112:2:1","112:2:2"],"word_rows":[{"analysis_record_ref":"112:2:1","analytic_gloss_range_en":"the proper divine name as nominative subject of a two-word nominal equation; not the common countable deity noun","analytic_root_gloss_range_en":"proper-name field with debated derivational pressure around worship, bewilderment, and refuge; local grammar selects the fixed divine name while allowing directional resonance with the predicate","qac_refs":["112:2:1:1"],"root":{"arabic":"أ ل ه","transliteration":"ʾ-l-h"},"surface":{"arabic":"ٱللَّهُ","transliteration":"allāhu"}},{"analysis_record_ref":"112:2:2","analytic_gloss_range_en":"the definite predicate-title, locally gathering resort-in-need, self-sufficiency, solidity without hollowness, and acknowledged mastery while excluding process senses as the main local reading","analytic_root_gloss_range_en":"accepted root range includes intending and resorting to a relied-on one, compact solidity without hollowness, stopping, wrapping, attention to an affair, striking with a stick, and enduring; the local title activates the resort, solidity, endurance, and mastery field, not the unrelated stopper, wrapping, verge, or striking branches","qac_refs":["112:2:2:1","112:2:2:2"],"root":{"arabic":"ص م د","transliteration":"ṣ-m-d"},"surface":{"arabic":"ٱلصَّمَدُ","transliteration":"aṣ-ṣamad"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":2,"words_total":2,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":4,"missing_anchor_refs":[],"supplied_unique_anchor_count":4},"assigned_record_count":11,"assigned_records":[{"anchor_refs":["112:1","112:2"],"branch_refs":["root_000882/B001","root_001272/B014","root_001272/B016"],"candidate_id":"cand_d6ebc2e6cef62b184ba8","evidence_scope":"declared_pericope","hft_ref":"hft_1cecc9426ec5c10e0b01","item_id":"delta-speech-as-definition","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta-speech-as-definition","support_id":"sup_63de50bd450f8d4f43f7"},{"anchor_refs":["112:1","112:2"],"branch_refs":["root_000047/B001","root_000882/B001"],"candidate_id":"cand_69cf89bfc9c4f34ab395","evidence_scope":"declared_pericope","hft_ref":"hft_6f5f7f7982d103d8f748","item_id":"delta-repeated-referent","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta-repeated-referent","support_id":"sup_ff2a388e186f88f5eb67"},{"anchor_refs":["112:1","112:2","112:4"],"branch_refs":["root_000017/B001","root_000017/B002","root_000882/B001"],"candidate_id":"cand_d4656a4de53e00edf334","evidence_scope":"declared_pericope","hft_ref":"hft_9f2ae92f8c595ef4a571","item_id":"delta-single-convergence","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta-single-convergence","support_id":"sup_bf4bb823003955e2c4d4"},{"anchor_refs":["112:1","112:2","112:4"],"branch_refs":["root_000017/B002","root_000017/B003","root_000882/B002"],"candidate_id":"cand_8881b175ace608d50653","evidence_scope":"declared_pericope","hft_ref":"hft_8bb732226fb7ee9f050c","item_id":"delta-uncomposed-integrity","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta-uncomposed-integrity","support_id":"sup_3ee39c2204f5b7bb7ff3"},{"anchor_refs":["112:2","112:3"],"branch_refs":["root_000882/B002","root_000882/B007","root_001683/B003","root_001683/B005"],"candidate_id":"cand_98c30129ed8b24028224","evidence_scope":"declared_pericope","hft_ref":"hft_6f60ecdd37081c800b9d","item_id":"delta-nonderived-nonemanating","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta-nonderived-nonemanating","support_id":"sup_9f8ca522212e6058a1f3"},{"anchor_refs":["112:2","112:4"],"branch_refs":["root_000882/B007","root_001332/B001"],"candidate_id":"cand_6ebb95fdbf1216e10090","evidence_scope":"declared_pericope","hft_ref":"hft_7addfa2f5379473c46d3","item_id":"delta-temporal-invariance","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta-temporal-invariance","support_id":"sup_3dbc4de463a160d68f7a"},{"anchor_refs":["112:2","112:4"],"branch_refs":["root_000882/B001","root_001305/B001"],"candidate_id":"cand_63634fbcaf8f23a622bc","evidence_scope":"declared_pericope","hft_ref":"hft_a810c1636699e87c4109","item_id":"delta-asymmetric-dependence","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta-asymmetric-dependence","support_id":"sup_1bf4543365054975cbdc"},{"anchor_refs":["112:1","112:2"],"branch_refs":["root_000882/B002","root_000882/B007","root_001251/B004"],"candidate_id":"cand_d3b5015d11ff0d408a4f","evidence_scope":"declared_pericope","hft_ref":"hft_c5649d16ef9ab26c6751","item_id":"outlier-split-root-load-bearing","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier-split-root-load-bearing","support_id":"sup_ba0eac616e1904fe1c14"},{"anchor_refs":["112:1","112:2"],"branch_refs":["root_000882/B004","root_001272/B012"],"candidate_id":"cand_4a2eac32468cb9b8bb2c","evidence_scope":"declared_pericope","hft_ref":"hft_6f6432efc43c364a1b0a","item_id":"outlier-bound-attention","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier-bound-attention","support_id":"sup_cc3f7f04cdb9092703fb"},{"anchor_refs":["112:2","112:3"],"branch_refs":["root_000882/B003","root_001683/B005"],"candidate_id":"cand_a636d876580a77e74354","evidence_scope":"declared_pericope","hft_ref":"hft_217c5a55b8ebf66c65b8","item_id":"outlier-sealed-derivation","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier-sealed-derivation","support_id":"sup_b6032205f2fd34f3aa82"},{"anchor_refs":["112:2","112:4"],"branch_refs":["root_000882/B001","root_001305/B002"],"candidate_id":"cand_58a7d601560660ef48a5","evidence_scope":"declared_pericope","hft_ref":"hft_b2d88f5a1a6664669921","item_id":"outlier-unturnable-orientation","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier-unturnable-orientation","support_id":"sup_030f748f86f810cfd95d"}],"diagnostics":[],"lane_counts":{"global":9,"macro":11,"micro":5},"packet_summary":{"ayah_count":4,"focus_ref":"112:2","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]}],"window":["112:1","112:2","112:3","112:4"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"112:2","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":16,"unstructured_record_count":0},"identity":{"ayah_ref":"112:2","lane":"macro","linguistic_source_ref":"112:2","surface_ref":"112:2","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"112:2","target_tokens":[["Allah",["112:2:1"]],["herkesin",["112:2:2"]],["dayanağıdır",["112:2:2"]]],"text":"Allah, herkesin dayanağıdır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":11,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":1,"ayah_to":4,"id":"s112-p01-001-004","label":"Whole surah","number":1,"refs":["112:1","112:2","112:3","112:4"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"112:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"112:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["112:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"112:0"},{"ayah_ref":"112:1","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"112:1","root_occurrences":[{"lemmas_ar":["قَالَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ق و ل","surfaces_ar":["قُلْ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهُ"],"word_indices":["3"]},{"lemmas_ar":["أَحَد"],"occurrence_count":1,"pos_tags":["N"],"root":"ء ح د","surfaces_ar":["أَحَدٌ"],"word_indices":["4"]}],"root_sequence":["ق و ل","ء ل ه","ء ح د"],"text_ar":"قُلْ هُوَ ٱللَّهُ أَحَدٌ"}],"context_order":["112:1"],"context_root_cues":[{"root":"ق و ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"إخراج القول بالنطق"},{"branch_id":"B002","branch_image_ar":"اللسان آلة القول"},{"branch_id":"B003","branch_image_ar":"كثرة القول في صاحبه"},{"branch_id":"B004","branch_image_ar":"القيل صاحب القول النافذ"},{"branch_id":"B005","branch_image_ar":"قول ما لم يكن أو نسبته"},{"branch_id":"B006","branch_image_ar":"اجترار القول إلى النفس"},{"branch_id":"B007","branch_image_ar":"القول الفاشي بين الناس"},{"branch_id":"B008","branch_image_ar":"عود القال لضرب القلة"},{"branch_id":"B009","branch_image_ar":"المقاولة في الأمر"},{"branch_id":"B010","branch_image_ar":"اقتالة الحكم على غيره"},{"branch_id":"B011","branch_image_ar":"قول يجري مجرى الظن"},{"branch_id":"B012","branch_image_ar":"قول في النفس لم يظهر"},{"branch_id":"B013","branch_image_ar":"القول اعتقاد ومذهب"},{"branch_id":"B014","branch_image_ar":"قول الشيء دلالته"},{"branch_id":"B015","branch_image_ar":"العناية الصادقة بالشيء"},{"branch_id":"B016","branch_image_ar":"قول الشيء حده"}],"mapped_root_id":"root_001272","mapped_root_norm":"ق و ل"},{"branches":[{"branch_id":"B001","branch_image_ar":"القِلَّة والضآلة"},{"branch_id":"B002","branch_image_ar":"قُلَّة الشيء ورأسه"},{"branch_id":"B003","branch_image_ar":"القُلَّة الجرة الكبيرة"},{"branch_id":"B004","branch_image_ar":"الإقلال والاستقلال حملا ونهوضا"},{"branch_id":"B005","branch_image_ar":"القِلُّ رعدة واضطراب"},{"branch_id":"B006","branch_image_ar":"القلقلة اضطراب وتحرك"}],"mapped_root_id":"root_001251","mapped_root_norm":"ق ل ل"}]},{"root":"ء ح د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الأَحَدِيَّة والوَحْدَة"},{"branch_id":"B002","branch_image_ar":"استغراق النفي"},{"branch_id":"B003","branch_image_ar":"الواحد في العد والتركيب"},{"branch_id":"B004","branch_image_ar":"الأول والإضافة"},{"branch_id":"B005","branch_image_ar":"الانفراد والتفرق آحادا"},{"branch_id":"B006","branch_image_ar":"جبل أُحُد"}],"mapped_root_id":"root_000017","mapped_root_norm":"ء ح د"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"112:1","surface_ref":"112:1"},{"ayah_ref":"112:3","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"112:3","root_occurrences":[{"lemmas_ar":["وَلَدَ","وَلَدَ"],"occurrence_count":2,"pos_tags":["V","V"],"root":"و ل د","surfaces_ar":["يَلِدْ","يُولَدْ"],"word_indices":["2","4"]}],"root_sequence":["و ل د","و ل د"],"text_ar":"لَمْ يَلِدْ وَلَمْ يُولَدْ"}],"context_order":["112:3"],"context_root_cues":[{"root":"و ل د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"مولود من نسل"},{"branch_id":"B002","branch_image_ar":"أبوان من جهة الولادة"},{"branch_id":"B003","branch_image_ar":"حدوث الولادة ووضع الحمل"},{"branch_id":"B004","branch_image_ar":"صغير قريب العهد بالولادة أو مملوك"},{"branch_id":"B005","branch_image_ar":"شيء حاصل عن شيء أو مستحدث منه"},{"branch_id":"B006","branch_image_ar":"قرين في سن الولادة"}],"mapped_root_id":"root_001683","mapped_root_norm":"و ل د"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"112:3","surface_ref":"112:3"},{"ayah_ref":"112:4","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"112:4","root_occurrences":[{"lemmas_ar":["كَانَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ك و ن","surfaces_ar":["يَكُن"],"word_indices":["2"]},{"lemmas_ar":["كُفُو"],"occurrence_count":1,"pos_tags":["N"],"root":"ك ف ء","surfaces_ar":["كُفُوًا"],"word_indices":["4"]},{"lemmas_ar":["أَحَد"],"occurrence_count":1,"pos_tags":["N"],"root":"ء ح د","surfaces_ar":["أَحَدٌۢ"],"word_indices":["5"]}],"root_sequence":["ك و ن","ك ف ء","ء ح د"],"text_ar":"وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ"}],"context_order":["112:4"],"context_root_cues":[{"root":"ك و ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"وقوع الشيء وحضوره في زمان"},{"branch_id":"B002","branch_image_ar":"المكان والمكانة من الكون"},{"branch_id":"B003","branch_image_ar":"الكفالة والقيام على فلان"},{"branch_id":"B004","branch_image_ar":"الخضوع بالاستكانة"},{"branch_id":"B005","branch_image_ar":"الشيخ المنسوب إلى كُنْتُ"},{"branch_id":"B006","branch_image_ar":"حالة السوء بكينة"}],"mapped_root_id":"root_001332","mapped_root_norm":"ك و ن"}]},{"root":"ك ف ء","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"المماثلة والمقابلة بالمثل"},{"branch_id":"B002","branch_image_ar":"الإمالة والقلب والصرف"},{"branch_id":"B003","branch_image_ar":"اختلاف القوافي"},{"branch_id":"B004","branch_image_ar":"كِفاء الخباء"},{"branch_id":"B005","branch_image_ar":"كفأة السنة والنتاج"}],"mapped_root_id":"root_001305","mapped_root_norm":"ك ف ء"}]},{"root":"ء ح د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الأَحَدِيَّة والوَحْدَة"},{"branch_id":"B002","branch_image_ar":"استغراق النفي"},{"branch_id":"B003","branch_image_ar":"الواحد في العد والتركيب"},{"branch_id":"B004","branch_image_ar":"الأول والإضافة"},{"branch_id":"B005","branch_image_ar":"الانفراد والتفرق آحادا"},{"branch_id":"B006","branch_image_ar":"جبل أُحُد"}],"mapped_root_id":"root_000017","mapped_root_norm":"ء ح د"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"112:4","surface_ref":"112:4"},{"ayah_ref":"1:2","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:2","root_occurrences":[{"lemmas_ar":["حَمْد"],"occurrence_count":1,"pos_tags":["N"],"root":"ح م د","surfaces_ar":["حَمْدُ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["لَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَبّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ر ب ب","surfaces_ar":["رَبِّ"],"word_indices":["3"]},{"lemmas_ar":["عَٰلَمِين"],"occurrence_count":1,"pos_tags":["N"],"root":"ع ل م","surfaces_ar":["عَٰلَمِينَ"],"word_indices":["4"]}],"root_sequence":["ح م د","ء ل ه","ر ب ب","ع ل م"],"text_ar":"ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ"}],"context_order":["1:2"],"context_root_cues":[{"root":"ح م د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الحمد خلاف الذم"},{"branch_id":"B002","branch_image_ar":"وجود الشيء محمودا"},{"branch_id":"B003","branch_image_ar":"المحمود كثير الخصال"},{"branch_id":"B004","branch_image_ar":"حماداك الغاية المحمودة"},{"branch_id":"B005","branch_image_ar":"يتحمد بالمنة"}],"mapped_root_id":"root_000355","mapped_root_norm":"ح م د"}]},{"root":"ر ب ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ربوبية وملك وسيادة"},{"branch_id":"B002","branch_image_ar":"إصلاح وتربية وإتمام"},{"branch_id":"B003","branch_image_ar":"علم رباني"},{"branch_id":"B004","branch_image_ar":"ربة وجماعات كثيرة"},{"branch_id":"B005","branch_image_ar":"ربيب وربيبة ورابة"},{"branch_id":"B006","branch_image_ar":"رُبّ خاثر وإصلاح به"},{"branch_id":"B007","branch_image_ar":"لزوم وإقامة ودوام"},{"branch_id":"B008","branch_image_ar":"رباب السحاب"},{"branch_id":"B009","branch_image_ar":"شاة رُبّى وحداثة"},{"branch_id":"B010","branch_image_ar":"ربابة تجمع القداح"},{"branch_id":"B011","branch_image_ar":"ربابة عهد وميثاق"},{"branch_id":"B012","branch_image_ar":"ربة نبات"},{"branch_id":"B013","branch_image_ar":"ماء رَبَب كثير"},{"branch_id":"B014","branch_image_ar":"رَبْرَب قطيع"},{"branch_id":"B015","branch_image_ar":"حرف رب وربما"},{"branch_id":"B016","branch_image_ar":"رُبَى حاجة وعقدة ونعمة"},{"branch_id":"B017","branch_image_ar":"رباني الملاحين"}],"mapped_root_id":"root_000532","mapped_root_norm":"ر ب ب"},{"branches":[{"branch_id":"B001","branch_image_ar":"زيادة وعلو"},{"branch_id":"B002","branch_image_ar":"أرض مرتفعة"},{"branch_id":"B003","branch_image_ar":"زيادة الربا في المعاملة"},{"branch_id":"B004","branch_image_ar":"تصعد النفس وانتفاخه"},{"branch_id":"B005","branch_image_ar":"تغذية ونشوء"},{"branch_id":"B006","branch_image_ar":"نتوء أصل الفخذ"},{"branch_id":"B007","branch_image_ar":"أهل البيت من بني الأعمام"}],"mapped_root_id":"root_000537","mapped_root_norm":"ر ب و"}]},{"root":"ع ل م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"انكشاف الشيء للعارف"},{"branch_id":"B002","branch_image_ar":"أثر يميز الشيء ويهدي إليه"},{"branch_id":"B004","branch_image_ar":"شق ظاهر في الشفة العليا"},{"branch_id":"B005","branch_image_ar":"ماء كثير مجتمع في عيلم"},{"branch_id":"B006","branch_image_ar":"طائر جارح يسمى العلام"},{"branch_id":"B007","branch_image_ar":"ذكر الضباع يسمى العيلام"}],"mapped_root_id":"root_001040","mapped_root_norm":"ع ل م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:2","membership_added_ayah":true,"membership_target_surah":112,"surface_ref":"1:2"},{"ayah_ref":"1:3","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:3","root_occurrences":[{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["1","2"]}],"root_sequence":["ر ح م","ر ح م"],"text_ar":"ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"}],"context_order":["1:3"],"context_root_cues":[{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:3","membership_added_ayah":true,"membership_target_surah":112,"surface_ref":"1:3"},{"ayah_ref":"1:4","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:4","root_occurrences":[{"lemmas_ar":["مَٰلِك"],"occurrence_count":1,"pos_tags":["N"],"root":"م ل ك","surfaces_ar":["مَٰلِكِ"],"word_indices":["1"]},{"lemmas_ar":["يَوْم"],"occurrence_count":1,"pos_tags":["N"],"root":"ي و م","surfaces_ar":["يَوْمِ"],"word_indices":["2"]},{"lemmas_ar":["دِين"],"occurrence_count":1,"pos_tags":["N"],"root":"د ي ن","surfaces_ar":["دِّينِ"],"word_indices":["3"]}],"root_sequence":["م ل ك","ي و م","د ي ن"],"text_ar":"مَٰلِكِ يَوْمِ ٱلدِّينِ"}],"context_order":["1:4"],"context_root_cues":[{"root":"م ل ك","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"قوة الشيء وتماسكه"},{"branch_id":"B002","branch_image_ar":"المِلْك والتصرف"},{"branch_id":"B003","branch_image_ar":"المُلك والسلطان"},{"branch_id":"B004","branch_image_ar":"الإملاك والتزويج"},{"branch_id":"B005","branch_image_ar":"مِلاك الأمر وعِماده"},{"branch_id":"B006","branch_image_ar":"مَلَك الطريق والوادي"},{"branch_id":"B007","branch_image_ar":"الماء مَلَك الأمر"},{"branch_id":"B008","branch_image_ar":"المتقدم القائد في الحيوان"}],"mapped_root_id":"root_001444","mapped_root_norm":"م ل ك"}]},{"root":"ي و م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"وقت النهار المحدود"},{"branch_id":"B002","branch_image_ar":"مدة من الزمان"},{"branch_id":"B003","branch_image_ar":"كائنة اليوم وشدته"}],"mapped_root_id":"root_001700","mapped_root_norm":"ي و م"}]},{"root":"د ي ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الطاعة والانقياد"},{"branch_id":"B002","branch_image_ar":"الحساب والجزاء"},{"branch_id":"B003","branch_image_ar":"الدين المالي"},{"branch_id":"B004","branch_image_ar":"الإذلال والملك"},{"branch_id":"B005","branch_image_ar":"العادة والشأن"},{"branch_id":"B006","branch_image_ar":"مدينة الطاعة"},{"branch_id":"B007","branch_image_ar":"التصديق والتفويض"}],"mapped_root_id":"root_000504","mapped_root_norm":"د ي ن"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:4","membership_added_ayah":true,"membership_target_surah":112,"surface_ref":"1:4"},{"ayah_ref":"1:5","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:5","root_occurrences":[{"lemmas_ar":["عَبَدَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ع ب د","surfaces_ar":["نَعْبُدُ"],"word_indices":["2"]},{"lemmas_ar":["ٱسْتَعِينُ"],"occurrence_count":1,"pos_tags":["V"],"root":"ع و ن","surfaces_ar":["نَسْتَعِينُ"],"word_indices":["4"]}],"root_sequence":["ع ب د","ع و ن"],"text_ar":"إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ"}],"context_order":["1:5"],"context_root_cues":[{"root":"ع ب د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرق والملك"},{"branch_id":"B003","branch_image_ar":"العبادة والطاعة الخاضعة"},{"branch_id":"B004","branch_image_ar":"التعبيد والاستعباد"},{"branch_id":"B005","branch_image_ar":"التذليل والتسوية"},{"branch_id":"B006","branch_image_ar":"التكريم والتعظيم"},{"branch_id":"B007","branch_image_ar":"القوة والصلابة"},{"branch_id":"B008","branch_image_ar":"الأنفة والغضب"},{"branch_id":"B009","branch_image_ar":"قلة اللبث وسرعة العدو"},{"branch_id":"B010","branch_image_ar":"التفرق في الوجوه"},{"branch_id":"B011","branch_image_ar":"العطب والانقطاع"},{"branch_id":"B012","branch_image_ar":"صَلاءة الطيب"}],"mapped_root_id":"root_000973","mapped_root_norm":"ع ب د"}]},{"root":"ع و ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الإعانة والمظاهرة"},{"branch_id":"B002","branch_image_ar":"العَوان بين السنين"},{"branch_id":"B003","branch_image_ar":"الحرب العَوان"},{"branch_id":"B004","branch_image_ar":"النخلة العَوانة القديمة"},{"branch_id":"B005","branch_image_ar":"استواء الخلقة وتلاحق القوة"},{"branch_id":"B006","branch_image_ar":"العانة قطيع الحمر"},{"branch_id":"B007","branch_image_ar":"عانة الرجل"},{"branch_id":"B008","branch_image_ar":"النسبة إلى عانة"}],"mapped_root_id":"root_001064","mapped_root_norm":"ع و ن"},{"branches":[{"branch_id":"B001","branch_image_ar":"العين الناظرة"},{"branch_id":"B002","branch_image_ar":"المشاهدة بالعين"},{"branch_id":"B003","branch_image_ar":"عين الحفظ والرعاية"},{"branch_id":"B004","branch_image_ar":"الإصابة بالعين"},{"branch_id":"B005","branch_image_ar":"العين الجاسوسة"},{"branch_id":"B006","branch_image_ar":"منبع الماء الجاري"},{"branch_id":"B007","branch_image_ar":"عين الجلد والسقاء"},{"branch_id":"B008","branch_image_ar":"عين الشمس"},{"branch_id":"B009","branch_image_ar":"النقرة أو الموضع العيني"},{"branch_id":"B010","branch_image_ar":"عين السحاب والمطر"},{"branch_id":"B011","branch_image_ar":"النقد الحاضر"},{"branch_id":"B012","branch_image_ar":"العينة والسلف"},{"branch_id":"B013","branch_image_ar":"عين الشيء نفسه"},{"branch_id":"B014","branch_image_ar":"العين خيار الشيء"},{"branch_id":"B015","branch_image_ar":"أعيان القوم والإخوة"},{"branch_id":"B016","branch_image_ar":"سعة العين وحسنها"},{"branch_id":"B017","branch_image_ar":"العين بمعنى الناس الحاضرون"}],"mapped_root_id":"root_001069","mapped_root_norm":"ع ي ن"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:5","membership_added_ayah":true,"membership_target_surah":112,"surface_ref":"1:5"},{"ayah_ref":"1:6","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:6","root_occurrences":[{"lemmas_ar":["هَدَى"],"occurrence_count":1,"pos_tags":["V"],"root":"ه د ي","surfaces_ar":["ٱهْدِ"],"word_indices":["1"]},{"lemmas_ar":["صِرَٰط"],"occurrence_count":1,"pos_tags":["N"],"root":"ص ر ط","surfaces_ar":["صِّرَٰطَ"],"word_indices":["2"]},{"lemmas_ar":["مُّسْتَقِيم"],"occurrence_count":1,"pos_tags":["ADJ"],"root":"ق و م","surfaces_ar":["مُسْتَقِيمَ"],"word_indices":["3"]}],"root_sequence":["ه د ي","ص ر ط","ق و م"],"text_ar":"ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ"}],"context_order":["1:6"],"context_root_cues":[{"root":"ه د ي","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"دلالة بلطف إلى الطريق والحق"},{"branch_id":"B002","branch_image_ar":"جهة الأمر وسيرته وقصده"},{"branch_id":"B003","branch_image_ar":"المتقدم الهادي وأوائل الشيء"},{"branch_id":"B004","branch_image_ar":"بعثة لطف وهدية إلى ذي مودة"},{"branch_id":"B005","branch_image_ar":"الهدي المهدى إلى الحرم"},{"branch_id":"B006","branch_image_ar":"العروس المهدية إلى زوجها"},{"branch_id":"B007","branch_image_ar":"هدي الحرمة والأسير"},{"branch_id":"B008","branch_image_ar":"مشي التهادي مع الاعتماد والتمايل"},{"branch_id":"B009","branch_image_ar":"الهداء البليد الضعيف"},{"branch_id":"B010","branch_image_ar":"هدي السكون وحسن الهيئة"},{"branch_id":"B011","branch_image_ar":"إهداء الشعر ومهاداته"}],"mapped_root_id":"root_001583","mapped_root_norm":"ه د ي"}]},{"root":"ص ر ط","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الطريق المستقيم"},{"branch_id":"B002","branch_image_ar":"الغيبة في المرور والبلع"},{"branch_id":"B003","branch_image_ar":"السيف القاطع الماضي في الضربة"}],"mapped_root_id":"root_000858","mapped_root_norm":"ص ر ط"}]},{"root":"ق و م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"جماعة الناس والرجال"},{"branch_id":"B002","branch_image_ar":"انتصاب وقيام بالبدن"},{"branch_id":"B003","branch_image_ar":"عزم ونهوض إلى الأمر"},{"branch_id":"B004","branch_image_ar":"رعاية وحفظ وولاية"},{"branch_id":"B006","branch_image_ar":"مقام وإقامة في موضع"},{"branch_id":"B007","branch_image_ar":"نيابة وقيام مقام غيره"},{"branch_id":"B008","branch_image_ar":"استقامة واعتدال واستواء"},{"branch_id":"B009","branch_image_ar":"قوام وعماد ومعاش"},{"branch_id":"B010","branch_image_ar":"قيمة وتقويم وتسعير"},{"branch_id":"B011","branch_image_ar":"قامة وقوام الجسم والطول"},{"branch_id":"B012","branch_image_ar":"آلة قائمة وجزء قائم"},{"branch_id":"B013","branch_image_ar":"قيامة وبعث وقيام الساعة"},{"branch_id":"B014","branch_image_ar":"مقاومة ومنازلة"},{"branch_id":"B015","branch_image_ar":"وزن سواء ومقدار معتدل"},{"branch_id":"B016","branch_image_ar":"جمود ووقوف وكلال"},{"branch_id":"B017","branch_image_ar":"انتصاف النهار وقائم الظهيرة"},{"branch_id":"B018","branch_image_ar":"نفاق السوق"},{"branch_id":"B019","branch_image_ar":"وجع قائم بالعضو"},{"branch_id":"B020","branch_image_ar":"قوام في قوائم الشاة"},{"branch_id":"B021","branch_image_ar":"عين قائمة ذاهبة البصر"}],"mapped_root_id":"root_001273","mapped_root_norm":"ق و م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:6","membership_added_ayah":true,"membership_target_surah":112,"surface_ref":"1:6"},{"ayah_ref":"1:7","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:7","root_occurrences":[{"lemmas_ar":["صِرَٰط"],"occurrence_count":1,"pos_tags":["N"],"root":"ص ر ط","surfaces_ar":["صِرَٰطَ"],"word_indices":["1"]},{"lemmas_ar":["أَنْعَمَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ن ع م","surfaces_ar":["أَنْعَمْ"],"word_indices":["3"]},{"lemmas_ar":["غَيْر"],"occurrence_count":1,"pos_tags":["N"],"root":"غ ي ر","surfaces_ar":["غَيْرِ"],"word_indices":["5"]},{"lemmas_ar":["مَغْضُوب"],"occurrence_count":1,"pos_tags":["N"],"root":"غ ض ب","surfaces_ar":["مَغْضُوبِ"],"word_indices":["6"]},{"lemmas_ar":["ضَآلّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ض ل ل","surfaces_ar":["ضَّآلِّينَ"],"word_indices":["9"]}],"root_sequence":["ص ر ط","ن ع م","غ ي ر","غ ض ب","ض ل ل"],"text_ar":"صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ"}],"context_order":["1:7"],"context_root_cues":[{"root":"ص ر ط","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الطريق المستقيم"},{"branch_id":"B002","branch_image_ar":"الغيبة في المرور والبلع"},{"branch_id":"B003","branch_image_ar":"السيف القاطع الماضي في الضربة"}],"mapped_root_id":"root_000858","mapped_root_norm":"ص ر ط"}]},{"root":"ن ع م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"حسن الحال والنعمة"},{"branch_id":"B002","branch_image_ar":"اللين والنعومة ورفاه العيش"},{"branch_id":"B003","branch_image_ar":"مدح الشيء بنعم"},{"branch_id":"B004","branch_image_ar":"الجواب بنعم والتصديق"},{"branch_id":"B005","branch_image_ar":"مال الأنعام والإبل"},{"branch_id":"B006","branch_image_ar":"النعام والنعامة الطائر"},{"branch_id":"B007","branch_image_ar":"ما سمي نعامة تشبيها بالهيئة"},{"branch_id":"B008","branch_image_ar":"طيران النعامة وتفرق القوم"},{"branch_id":"B009","branch_image_ar":"النعامى ريح لينة"},{"branch_id":"B010","branch_image_ar":"زاد وأنعم في الفعل"},{"branch_id":"B011","branch_image_ar":"موافقة المكان وطيب المقام"},{"branch_id":"B012","branch_image_ar":"المشي على القدم وابتذالها"},{"branch_id":"B013","branch_image_ar":"نعم الله بك عينا وقرة العين"}],"mapped_root_id":"root_001525","mapped_root_norm":"ن ع م"}]},{"root":"غ ي ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الصلاح والمنفعة بالميرة والسقي والإصلاح"},{"branch_id":"B002","branch_image_ar":"الغَيْر في الدية"},{"branch_id":"B003","branch_image_ar":"تغيير الصورة أو إبدال الشيء بغيره"},{"branch_id":"B004","branch_image_ar":"الغَيْرة على الأهل"},{"branch_id":"B005","branch_image_ar":"السوى والخلاف والاستثناء والنفي"}],"mapped_root_id":"root_001119","mapped_root_norm":"غ ي ر"}]},{"root":"غ ض ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"اشتداد السخط وثورانه للانتقام"},{"branch_id":"B002","branch_image_ar":"الغضب لشخص حي أو به بعد موته"},{"branch_id":"B003","branch_image_ar":"المراغمة والمخالفة"},{"branch_id":"B004","branch_image_ar":"صلابة الصخرة وتماسكها"},{"branch_id":"B005","branch_image_ar":"غلظ الجسم وشدة الحمرة"},{"branch_id":"B006","branch_image_ar":"تورم العين وما حولها"},{"branch_id":"B007","branch_image_ar":"العبوس والضجر والعظم في وصف الحيوان أو الشخص"},{"branch_id":"B008","branch_image_ar":"جلد صلب أو مطوي كدرقة"}],"mapped_root_id":"root_001092","mapped_root_norm":"غ ض ب"}]},{"root":"ض ل ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الضلال عن الهدى والقصد"},{"branch_id":"B002","branch_image_ar":"الغيبوبة والخفاء"},{"branch_id":"B003","branch_image_ar":"فقدان الشيء"},{"branch_id":"B004","branch_image_ar":"ضياع الحفظ"},{"branch_id":"B005","branch_image_ar":"الضالّة في المضيعة"}],"mapped_root_id":"root_000913","mapped_root_norm":"ض ل ل"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:7","membership_added_ayah":true,"membership_target_surah":112,"surface_ref":"1:7"}],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Striking and Redirection","source_type":"channel","support_id":"sup_1597e1f26b9a7af2b72a","text":"Two wooden implements supply the tool-and-impact pattern, while the motion field supplies its possible effects: tilting, overturning, diversion, and sway. Mount Uhud gives the construction a concrete geographic setting for the staff-strike scene.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"C:Responsible Authority and Negotiation","source_type":"channel","support_id":"sup_159df745f54ffadbf270","text":"Rank is converted into responsibility. The authoritative speaker can negotiate an affair, stand over it attentively, and guarantee another person, joining verbal force to institutional care.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Cavityless Solidity and Anchored Terrain","source_type":"channel","support_id":"sup_18bd56aae82af75aed78","text":"A space, container, body, or dwelling is stabilized by dense matter or a fitted closure.","trust":"trusted"},{"branch_refs":["root_000017/B006","root_000882/B002","root_001332/B002"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"A:Cavityless Solidity and Anchored Terrain","source_type":"channel","support_id":"sup_1a0856210be9e803e446","text":"compact solidity without a cavity `ص م د:B002/m01`; hard or elevated place `ص م د:B002/m02`; anchored rock and severe ground `ص م د:B002/m03`; place or location `ك و ن:B002/m01`; Mount Uhud `ء ح د:B006/m01`","trust":"trusted"},{"branch_refs":["root_000047/B001","root_000047/B002"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"A:Worship and the Invoked Divine Name","source_type":"channel","support_id":"sup_1bef9dae4403b8349275","text":"devotional worship `ء ل ه:B001/m01`; worshipped entity `ء ل ه:B001/m02`; making an object worshipped `ء ل ه:B001/m03`; divine name `ء ل ه:B002/m01`; oath formula `ء ل ه:B002/m02`; vocative invocation `ء ل ه:B002/m03`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Cavityless Solidity and Anchored Terrain","source_type":"channel","support_id":"sup_1dccd4b489e0526a9d0a","text":"112:1 `أحد`; 112:2 `الصمد`; 112:4 `يكن`, `أحد`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Stoppered Vessel","source_type":"channel","support_id":"sup_1e7e408efcf3b2fa22f0","text":"112:2 `الصمد`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"C:Fabric Closures for Body and Dwelling","source_type":"channel","support_id":"sup_1fade16ab31fa07a8c28","text":"Cloth is fitted and fastened to stabilize the head or close the rear of a shelter.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"C:Responsible Authority and Negotiation","source_type":"channel","support_id":"sup_2ef0e1e43d7abcf72685","text":"A ranked authority gives operative speech, sponsors a dependent, oversees an affair, and negotiates its disposition.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Bodily Yielding and Endurance","source_type":"channel","support_id":"sup_36492e638922ecafa6fc","text":"The two outcomes contrast yielding with resistance. One body registers disturbance in face and color; the enduring camel remains productive through cold and drought, turning persistence into sustained life under pressure.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Worship and the Invoked Divine Name","source_type":"channel","support_id":"sup_395720d0afec54652862","text":"A worshipper directs devotion toward one made the object of worship and addresses the divine name in oath or invocation.","trust":"trusted"},{"branch_refs":["root_000882/B004","root_001305/B004"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"C:Fabric Closures for Body and Dwelling","source_type":"channel","support_id":"sup_3af6d4338a0b1243cda7","text":"binding the head with cloth `ص م د:B004/m01`; sewn rear tent panels `ك ف ء:B004/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Worship and the Invoked Divine Name","source_type":"channel","support_id":"sup_3e913ef8198ac10a8683","text":"The divine name occupies both relational poles: it identifies the worshipped object and provides the form by which a speaker swears or calls. The lexical field also exposes the social act that constitutes something as an object of worship.","trust":"trusted"},{"branch_refs":["root_000882/B001"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"B:Sought Patron and Directed Reliance","source_type":"channel","support_id":"sup_4b7092422c0c3c34ae0a","text":"aiming toward and relying upon `ص م د:B001/m01`; lord or patron sought for needs `ص م د:B001/m02`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"C:Responsible Authority and Negotiation","source_type":"channel","support_id":"sup_4fdbacddd0a0074bc122","text":"112:1 `قل`; 112:2 `الصمد`; 112:4 `يكن`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Bodily Yielding and Endurance","source_type":"channel","support_id":"sup_52504d9cb4c61655d993","text":"112:2 `الصمد`; 112:4 `كفوا`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"C:Fabric Closures for Body and Dwelling","source_type":"channel","support_id":"sup_543d0fa7387918136e8e","text":"The same functional pattern operates at two scales. A cloth secures the body, while one or two sewn panels close and shape the back of a tent or dwelling.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Stoppered Vessel","source_type":"channel","support_id":"sup_549623946fa68875127c","text":"A space, container, body, or dwelling is stabilized by dense matter or a fitted closure.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Sought Patron and Directed Reliance","source_type":"channel","support_id":"sup_5a96ce3c24011ceef289","text":"Participants direct worship, need, allegiance, responsibility, or concern toward an asymmetrically positioned figure.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Striking and Redirection","source_type":"channel","support_id":"sup_66bf252d3f03a98fddf8","text":"112:1 `قل`, `أحد`; 112:2 `الصمد`; 112:4 `كفوا`, `أحد`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Bodily Yielding and Endurance","source_type":"channel","support_id":"sup_6b2b9078380eb59f55f6","text":"Pressure produces either visible bodily disturbance or continued functioning through severe conditions.","trust":"trusted"},{"branch_refs":["root_000882/B007","root_001305/B002"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"B:Bodily Yielding and Endurance","source_type":"channel","support_id":"sup_7ae07167a8a81a3707fd","text":"downcast face or changed color `ك ف ء:B002/m05`; persistence and survival `ص م د:B007/m01`; camel enduring cold and drought while maintaining milk `ص م د:B007/m02`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"C:Fabric Closures for Body and Dwelling","source_type":"channel","support_id":"sup_86b68be59ed3789534ce","text":"112:2 `الصمد`; 112:4 `كفوا`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Stoppered Vessel","source_type":"channel","support_id":"sup_86b7a6c6266dd5afa0c6","text":"A fitted plug closes and secures the mouth of a bottle.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Striking and Redirection","source_type":"channel","support_id":"sup_8cdd408f6919a5461749","text":"External pressure produces impact, redirection, visible yielding, or sustained resistance.","trust":"trusted"},{"branch_refs":["root_000017/B006","root_000882/B006","root_001272/B008","root_001305/B002"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"A:Striking and Redirection","source_type":"channel","support_id":"sup_a615894cd3931903f048","text":"staff blow `ص م د:B006/m01`; game stick used to strike `ق و ل:B008/m01`; tilting, inversion, or upending `ك ف ء:B002/m01`; tilting a bow or dish `ك ف ء:B002/m02`; diverting a group `ك ف ء:B002/m03`; swaying motion `ك ف ء:B002/m04`; Mount Uhud as setting `ء ح د:B006/m01`","trust":"trusted"},{"branch_refs":["root_000882/B005","root_001272/B004","root_001272/B009","root_001332/B002","root_001332/B003"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"C:Responsible Authority and Negotiation","source_type":"channel","support_id":"sup_aeba3cb4dab32b86de2e","text":"chieftain whose word carries force `ق و ل:B004/m01`; rank or standing `ك و ن:B002/m02`; establishment in position `ك و ن:B002/m03`; sponsorship and guarantee `ك و ن:B003/m01`; oversight of an affair `ص م د:B005/m01`; attentive concern for it `ص م د:B005/m02`; negotiation `ق و ل:B009/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Sought Patron and Directed Reliance","source_type":"channel","support_id":"sup_aebf3f6e54edff5b03e5","text":"A person deliberately turns toward a dependable patron for affairs and needs.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Sought Patron and Directed Reliance","source_type":"channel","support_id":"sup_b3b232819d8563a575d7","text":"Direction and dependence form one action: the seeker chooses a destination because the figure approached is the one on whom affairs and needs can rest.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Sought Patron and Directed Reliance","source_type":"channel","support_id":"sup_b45129aced4f8292ad75","text":"112:2 `الصمد`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"C:Responsible Authority and Negotiation","source_type":"channel","support_id":"sup_b55a9b9d44d597bf89d8","text":"Participants direct worship, need, allegiance, responsibility, or concern toward an asymmetrically positioned figure.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Worship and the Invoked Divine Name","source_type":"channel","support_id":"sup_b8f4b63ff762260c906f","text":"Participants direct worship, need, allegiance, responsibility, or concern toward an asymmetrically positioned figure.","trust":"trusted"},{"branch_refs":["root_000882/B003"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"B:Stoppered Vessel","source_type":"channel","support_id":"sup_c3cb483585e5972e0b41","text":"bottle stopper `ص م د:B003/m01`; act of stoppering `ص م د:B003/m02`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"C:Fabric Closures for Body and Dwelling","source_type":"channel","support_id":"sup_d4b7c06d83225815f2f9","text":"A space, container, body, or dwelling is stabilized by dense matter or a fitted closure.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Bodily Yielding and Endurance","source_type":"channel","support_id":"sup_e4f236e8afd4d585ddc0","text":"External pressure produces impact, redirection, visible yielding, or sustained resistance.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Worship and the Invoked Divine Name","source_type":"channel","support_id":"sup_e9768bff321cf768b5aa","text":"112:1 `الله`; 112:2 `الله`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Stoppered Vessel","source_type":"channel","support_id":"sup_eeb3338460af018ddc54","text":"The object and operation form a compact containment mechanism: a closure is made for the vessel and then set in place to seal it.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Cavityless Solidity and Anchored Terrain","source_type":"channel","support_id":"sup_ef9c0f0d3c4b0d250494","text":"Solidity scales from material texture to landscape. Dense matter becomes hard ground and fixed rock, location gives it spatial placement, and Mount Uhud supplies the fully named elevated setting.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Cavityless Solidity and Anchored Terrain","source_type":"channel","support_id":"sup_f10881522267002dad0f","text":"Dense, cavityless matter forms hard ground, fixed rock, and elevated terrain located in a definite place.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Striking and Redirection","source_type":"channel","support_id":"sup_f8c965c775c0f4ee340a","text":"Applied force strikes a target or changes the orientation and course of an object or group.","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"قُلْ هُوَ ٱللَّهُ أَحَدٌ","ayah_ref":"112:1"},{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","ayah_ref":"112:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000882/B001","root_001272/B014","root_001272/B016"],"payload":{"activation_trace":[{"branch_id":"B014","mapped_root_id":"root_001272","role":"A thing's 'saying' as its indication makes the commanded utterance point beyond sound to the relation asserted in the focus.","root":"ق و ل","source_ref":"112:1","source_word_indices":["1"]},{"branch_id":"B016","mapped_root_id":"root_001272","role":"Saying a thing as defining its limit makes the utterance set a conceptual boundary around the focus predicate.","root":"ق و ل","source_ref":"112:1","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000882","role":"Resort to the relied-on destination supplies the relation that the spoken definition publicly fixes.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]}],"changed_reading":{"after":"Allah al-Samad is also a commanded public definition that fixes the endpoint of recourse in speech.","before":"Allah al-Samad is a private descriptive proposition about divine status."},"confidence":"medium","mechanism":"The command to speak activates saying as both indication and delimiting definition. The compact nominal equation in 112:2 therefore functions not only as information but as a publicly uttered boundary for where reliance is to terminate.","model_id":"delta-speech-as-definition","reader_inference":"The packet supplies commanded speech, indication, definition, and directed resort. I infer that utterance performs boundary-setting for reliance. A live alternative is that the command merely reports a proposition and adds no performative force.","status":"new","structural_cues":["112:1 opens with an imperative of speech immediately before the verbless two-term predication in 112:2.","The focus ayah's brevity lets the commanded utterance operate like a formula rather than a narrative description."],"trigger_roots":["ق و ل"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta-speech-as-definition","source_type":"hft","support_id":"sup_63de50bd450f8d4f43f7","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"قُلْ هُوَ ٱللَّهُ أَحَدٌ","ayah_ref":"112:1"},{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","ayah_ref":"112:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000047/B001","root_000882/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000047","role":"The worshipped referent is introduced in the preceding equation and supplies the repeated identity carried into the focus.","root":"ء ل ه","source_ref":"112:1","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000882","role":"The destination relied upon supplies the new relation predicated of that repeated referent.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]}],"changed_reading":{"after":"The predicate is locked to the same named worshipped referent identified immediately before it.","before":"Al-Samad could denote a high but generic type of dependable lord."},"confidence":"strong","mechanism":"Repetition of the same divine name across 112:1 and 112:2 creates a tight referential bridge: the worshipped one just identified is precisely the one now predicated as the destination of resort, preventing الصمد from drifting into a generic class of chiefs.","model_id":"delta-repeated-referent","reader_inference":"The packet supplies a repeated named worshipped referent and a resorted-to predicate. I infer deliberate coreference that excludes a merely generic 'reliable chief.' A live alternative is simple rhetorical repetition without this narrowing effect.","status":"strengthened","structural_cues":["The exact proper name recurs in adjacent ayat, each time in a short nominal predication.","The second occurrence replaces the preceding predicate أحد with الصمد while retaining the subject."],"trigger_roots":["ء ل ه"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta-repeated-referent","source_type":"hft","support_id":"sup_ff2a388e186f88f5eb67","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"قُلْ هُوَ ٱللَّهُ أَحَدٌ","ayah_ref":"112:1"},{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","ayah_ref":"112:2"},{"arabic_uthmani":"وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ","ayah_ref":"112:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000017/B001","root_000017/B002","root_000882/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000017","role":"Oneness and unity supply a single pole toward which the focus predicate's directed resort can converge.","root":"ء ح د","source_ref":"112:1","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000017","role":"Exhaustive negation removes any leftover instance that could serve as a coordinate endpoint.","root":"ء ح د","source_ref":"112:4","source_word_indices":["5"]},{"branch_id":"B001","mapped_root_id":"root_000882","role":"Intentional resort supplies the many directed paths whose convergence is reorganized by the two context occurrences.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]}],"changed_reading":{"after":"Al-Samad configures recourse as convergence on one endpoint with no coordinate remainder.","before":"Al-Samad is one dependable option distinguished by supreme rank."},"confidence":"strong","mechanism":"Unity before the focus and exhaustive negation at the close reshape resort into a topology of convergence: many affairs can be directed, but they do not terminate at several coordinate destinations. The one endpoint is also left without any residual competing instance.","model_id":"delta-single-convergence","reader_inference":"The packet supplies unity, exhaustive negation, and directed resort. I infer a many-paths-to-one-endpoint structure. A live alternative is that unity and resort remain independent predicates with no spatial or network relation.","status":"revised","structural_cues":["The focus is preceded by أحد as a positive predicate and the sequence closes with أحد inside a negated counterpart construction.","The two occurrences bracket the focus with positive singularity and exhaustive exclusion."],"trigger_roots":["ء ح د"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta-single-convergence","source_type":"hft","support_id":"sup_bf4bb823003955e2c4d4","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"قُلْ هُوَ ٱللَّهُ أَحَدٌ","ayah_ref":"112:1"},{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","ayah_ref":"112:2"},{"arabic_uthmani":"وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ","ayah_ref":"112:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000017/B002","root_000017/B003","root_000882/B002"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000017","role":"The one as a unit in counting and composition introduces the live question of whether unity is aggregate or integral.","root":"ء ح د","source_ref":"112:1","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000017","role":"Exhaustive negation prevents an unmentioned constituent or peer from casually remaining outside the unity claim.","root":"ء ح د","source_ref":"112:4","source_word_indices":["5"]},{"branch_id":"B002","mapped_root_id":"root_000882","role":"Compact solidity without a hollow supplies the material analogy for integrity without an interior dependency.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]}],"changed_reading":{"after":"It becomes an exploratory image of integral unity whose reliability is not produced by cooperating internal parts.","before":"Non-hollowness is only a vivid image of physical firmness."},"confidence":"exploratory","mechanism":"The counting-and-composition branch of أحد presses the compact, non-hollow image of الصمد into a mereological question. Read against asserted unity and final exhaustive negation, compactness can suggest integrity not assembled from independently sustaining pieces.","model_id":"delta-uncomposed-integrity","reader_inference":"The packet supplies one-as-unit/composition, exhaustive negation, and compact non-hollowness. I infer a contrast between assembled unity and integral unity. A live alternative is that the counting branch marks only numerical one and cannot support non-composition.","status":"revised","structural_cues":["أحد directly precedes the focus predicate and recurs in the closing negation.","The focus itself is a bare nominal equation, so the concrete property is asserted without an intervening comparison marker."],"trigger_roots":["ء ح د"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta-uncomposed-integrity","source_type":"hft","support_id":"sup_3ee39c2204f5b7bb7ff3","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","ayah_ref":"112:2"},{"arabic_uthmani":"لَمْ يَلِدْ وَلَمْ يُولَدْ","ayah_ref":"112:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000882/B002","root_000882/B007","root_001683/B003","root_001683/B005"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001683","role":"The event of birth supplies the concrete incoming and outgoing transitions canceled by the paired verbal forms.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]},{"branch_id":"B005","mapped_root_id":"root_001683","role":"Something obtained or newly produced from something else generalizes lineage into derivation and lets the two negations test causal dependence.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]},{"branch_id":"B002","mapped_root_id":"root_000882","role":"Compact integrity supplies the focus anchor that is recast as having neither an originating deficit nor a generated continuation.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]},{"branch_id":"B007","mapped_root_id":"root_000882","role":"Lasting continuance supplies the persistence that no predecessor or offspring is needed to maintain.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]}],"changed_reading":{"after":"The Samad's endurance is non-genealogical and non-derivative: it neither arrives from a producer nor continues by producing a successor.","before":"The Samad is enduring because the referent lasts exceptionally long."},"confidence":"strong","mechanism":"The paired active and passive birth negations turn compact endurance into causal independence in both directions. The Samad is neither a product derived from an upstream source nor a source that secures continuity by issuing a downstream successor.","model_id":"delta-nonderived-nonemanating","reader_inference":"The packet supplies birth, derivation, active/passive reversal, and enduring compactness. I infer that the reversal blocks both incoming origin and outgoing successor as supports for persistence. A live alternative confines the negation to biological parentage and leaves broader causal derivation unstated.","status":"revised","structural_cues":["The same root occurs twice in reversed active and passive verbal orientation.","The paired negations immediately follow the nominal focus, supplying two directional tests of its claim."],"trigger_roots":["و ل د"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta-nonderived-nonemanating","source_type":"hft","support_id":"sup_9f8ca522212e6058a1f3","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","ayah_ref":"112:2"},{"arabic_uthmani":"وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ","ayah_ref":"112:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000882/B007","root_001332/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001332","role":"Occurrence or presence in time supplies the temporal field across which the negated counterpart fails to appear.","root":"ك و ن","source_ref":"112:4","source_word_indices":["2"]},{"branch_id":"B007","mapped_root_id":"root_000882","role":"Lasting endurance supplies the focus claim that is strengthened from persistence under hardship to persistence without a temporal peer-phase.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]}],"changed_reading":{"after":"The Samad's unmatched reliability is read across temporal occurrence, not as a temporary configuration.","before":"The Samad happens to stand without an equal in the asserted present."},"confidence":"medium","mechanism":"The context branch of coming to presence in time tests the focus's enduring support against temporal occurrence. The closing negation allows no time at which a counterpart comes to be, so the Samad's singular reliability is not a temporary unmatched phase.","model_id":"delta-temporal-invariance","reader_inference":"The packet supplies enduring continuance and occurrence in time under negation. I infer that no temporal state introduces a counterpart and that this stabilizes the focus relation across time. A live alternative treats يكن as only copular support with no independent temporal activation.","status":"strengthened","structural_cues":["The timeless-looking nominal focus is followed by a negated form of being in the final ayah.","The final construction places the absence of a counterpart under temporalized existence rather than stating only a static inequality."],"trigger_roots":["ك و ن"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta-temporal-invariance","source_type":"hft","support_id":"sup_3dbc4de463a160d68f7a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","ayah_ref":"112:2"},{"arabic_uthmani":"وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ","ayah_ref":"112:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000882/B001","root_001305/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001305","role":"Equality and matching opposition supply the possible coordinate pole that the context explicitly negates.","root":"ك ف ء","source_ref":"112:4","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000882","role":"Directed resort and reliance supply the dependency arrows whose symmetry would require such a matching pole.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]}],"changed_reading":{"after":"The Samad is the terminal pole of a non-reciprocal dependency field for which no matching pole exists.","before":"The Samad is the highest member within a field of comparable powers."},"confidence":"strong","mechanism":"Resort establishes directed dependence toward the Samad; the negated equal counterpart removes any peer that could mirror or reciprocate that relation. The result is not merely maximal rank but an asymmetric dependency network with one terminal pole.","model_id":"delta-asymmetric-dependence","reader_inference":"The packet supplies directed resort and negated matching equivalence. I infer that a peer would make the dependency structure reciprocal or multipolar, so its negation yields asymmetry. A live alternative is that the context denies likeness without saying anything about dependency arrows.","status":"revised","structural_cues":["The focus positively names the endpoint of recourse, while the final ayah negates a matching counterpart.","The counterpart is placed in relation to له, making equality relational rather than merely descriptive."],"trigger_roots":["ك ف ء"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta-asymmetric-dependence","source_type":"hft","support_id":"sup_1bf4543365054975cbdc","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"قُلْ هُوَ ٱللَّهُ أَحَدٌ","ayah_ref":"112:1"},{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","ayah_ref":"112:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000882/B002","root_000882/B007","root_001251/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001251","role":"Independently carrying and rising under a load supplies a dynamic load-bearing image from the packet's secondary root mapping.","root":"ق و ل","source_ref":"112:1","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000882","role":"Compact solidity supplies the stable structure capable of receiving the load-bearing activation.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]},{"branch_id":"B007","mapped_root_id":"root_000882","role":"Endurance under severity turns carrying from a static pose into sustained support under adverse conditions.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]}],"changed_reading":{"after":"At the split-root fringe, the command activates the Samad as independently rising under and sustaining the loads that recourse directs there.","before":"The opening command only introduces a statement about a firm, enduring referent."},"confidence":"exploratory","containment":"This activation is surprising because it uses the packet's non-dominant ق ل ل mapping for قُلْ rather than the ordinary speech root. It remains anchored through that explicit split mapping and its convergence with الصمد's solidity and endurance, but downstream prose should label it a mapping-induced load-bearing analogy, not a lexical gloss of the imperative.","focus_anchor":"The compact and enduring branches of الصمد can receive the context image of independently taking up and rising under a load.","outlier_id":"outlier-split-root-load-bearing"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier-split-root-load-bearing","source_type":"hft","support_id":"sup_ba0eac616e1904fe1c14","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"قُلْ هُوَ ٱللَّهُ أَحَدٌ","ayah_ref":"112:1"},{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","ayah_ref":"112:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000882/B004","root_001272/B012"],"payload":{"activation_trace":[{"branch_id":"B012","mapped_root_id":"root_001272","role":"Unvoiced saying within oneself supplies an interior recitation-space behind the overt command.","root":"ق و ل","source_ref":"112:1","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_000882","role":"Wrapping the head with a cloth supplies a bodily image of binding and gathering attention around the predicate.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]}],"changed_reading":{"after":"As an exploratory recitational image, the phrase also binds inward attention around a single dependable focus.","before":"The phrase is only an outward declaration naming the destination of need."},"confidence":"exploratory","containment":"This is odd because it joins a head-wrapping branch of ص م د to an inward, unvoiced branch of saying even though قُلْ is overtly imperative. Both branches are packet-backed and the result stays anchored in the focus predicate, but it should be rendered only as a somatic-cognitive analogy for gathered attention, never as the lexical meaning of الصمد.","focus_anchor":"The concrete head-binding branch of الصمد can picture concentration around the focus formula.","outlier_id":"outlier-bound-attention"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier-bound-attention","source_type":"hft","support_id":"sup_cc3f7f04cdb9092703fb","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","ayah_ref":"112:2"},{"arabic_uthmani":"لَمْ يَلِدْ وَلَمْ يُولَدْ","ayah_ref":"112:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000882/B003","root_001683/B005"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000882","role":"The tightly fitted stopper supplies a concrete image of a boundary that closes passage and referral.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]},{"branch_id":"B005","mapped_root_id":"root_001683","role":"Something derived or newly produced from another supplies the causal throughput canceled in both directions by the context.","root":"و ل د","source_ref":"112:3","source_word_indices":["2","4"]}],"changed_reading":{"after":"Through the sealing image, the Samad is the boundary at which origin-and-offshoot referral closes rather than passing through.","before":"The birth negations merely exclude two kinship relations."},"confidence":"exploratory","containment":"The model is surprising because a bottle stopper and generation belong to distant material and biological domains. It remains valid as an analogy anchored in الصمد and the paired derivation cue, but downstream prose must say that causal referral closes here, not imply a literal container, bodily closure, or a denial of all divine action.","focus_anchor":"The tight-stopper branch of الصمد can be reactivated by the context's negation of being produced and producing.","outlier_id":"outlier-sealed-derivation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier-sealed-derivation","source_type":"hft","support_id":"sup_b6032205f2fd34f3aa82","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱللَّهُ ٱلصَّمَدُ","ayah_ref":"112:2"},{"arabic_uthmani":"وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ","ayah_ref":"112:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000882/B001","root_001305/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000882","role":"Intending and resorting to the relied-on one supplies a directed trajectory toward the focus referent.","root":"ص م د","source_ref":"112:2","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001305","role":"Tilting, overturning, and diverting supply the possible counterforce that would bend or reverse that trajectory.","root":"ك ف ء","source_ref":"112:4","source_word_indices":["4"]}],"changed_reading":{"after":"At the kinetic fringe, no counterforce can tilt, reverse, or redirect the trajectory of recourse away from the Samad.","before":"No being resembles the one to whom recourse is directed."},"confidence":"exploratory","containment":"This is branch-distant because the surface كُفُوًا most directly activates equivalence, while turning, tilting, and reversal come from another inventory branch. It remains anchored by the directional 'resorting toward' structure of الصمد, but downstream prose should present it as a secondary kinetic resonance, not as a replacement translation.","focus_anchor":"The directional resort encoded by الصمد supplies a trajectory that the turning branch of ك ف ء can test.","outlier_id":"outlier-unturnable-orientation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier-unturnable-orientation","source_type":"hft","support_id":"sup_030f748f86f810cfd95d","trust":"legacy_unbound"}]}
</lane_packet_json>
