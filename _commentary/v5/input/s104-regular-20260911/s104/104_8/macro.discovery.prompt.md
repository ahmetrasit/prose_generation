# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **104:8**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s104-regular-20260911/s104/104_8/macro.discovery.json` and modify nothing
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
  "ayah_ref": "104:8",
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
{"analysis_context":{"analysis_id":"s104-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"104:8","host_surah":104,"lane_context_refs":["104:0","104:1","104:2","104:3","104:4","104:5","104:6","104:7","104:9","1:2","1:3","1:4","1:5","1:6","1:7"],"ordered_context_refs":["104:0","104:1","104:2","104:3","104:4","104:5","104:6","104:7","104:9","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dalın çekirdeği kapatma ve kuşatmadır; kapı, ateş ve kişi grubu yalnızca bu çekirdeğin belirli gerçekleşmeleridir.","branch_kind":"mixed_non_bare","branch_ref":"root_000036/B001","candidate_links":[{"candidate_id":"cand_143e589d5321bb026b33","lane":"macro"},{"candidate_id":"cand_110242bef49ccc802ec1","lane":"macro"},{"candidate_id":"cand_59ae345bde11641a0f28","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"مُّؤْصَدَة","morph_features":"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:8:3:1","qac_word_ref":"104:8:3","surface_ar":"مُّؤْصَدَةٌ"}],"gloss":"kuşatıp kapatma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey başka bir şeyi içine alır, üstüne kapanır ve onun dışarıya açılmasını engeller."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kapı söz konusu olduğunda eylem, kapıyı kapalı duruma getirmeyi anlatır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir topluluğun üzerine kapatma ve ateşin üzerlerine kapatılmış olması, çekirdeğin yapıya bağlı kullanımlarıdır."}}],"root_ar":"و ص د","root_id":"root_000036","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem kapsama hem de kapalı duruma getirme öğelerini birlikte taşıyan en kısa genel karşılığıdır.","boundary_detail":"Dalın çekirdeği kapatma ve kuşatmadır; kapı, ateş ve kişi grubu yalnızca bu çekirdeğin belirli gerçekleşmeleridir.","branch_image_ar":"الإطباق والإغلاق على الشيء","concept_gloss":"kuşatıp kapatma","contextual_glosses":[{"applicability":"Kapının açık durumdan kapalı duruma getirildiği eylem bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dalın kapı dışındaki kuşatma ve üzerini kapatma kapsamını taşımaz.","preserves":"Kapalı duruma getirme işlemini açık biçimde korur."},"facet_ids":["F002"],"text":"kapıyı kapatmak","usage_role":"contextual"},{"applicability":"Bir topluluğun ya da kapatılmış ateşin dışarıya açılmayacak biçimde çevrelendiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel ad anlamını ve kapı kapatma kullanımını dışarıda bırakır.","preserves":"Bir şeyin başkalarının üzerine kapanması ve onları içeride tutması korunur."},"facet_ids":["F003"],"text":"üzerlerine kapatılmış","usage_role":"contextual"}],"definition":"Bir şeyi başka bir şeyin üzerine kapatmak ya da onu bütünüyle kuşatıp dışarıya açılmasını engellemektir. Bu çekirdek, kapı kapatma gibi eylemlerde ve kapatılmış şeyleri niteleyen yapılarda gerçekleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey başka bir şeyi içine alır, üstüne kapanır ve onun dışarıya açılmasını engeller."},{"facet_id":"F002","role":"specialization","statement":"Kapı söz konusu olduğunda eylem, kapıyı kapalı duruma getirmeyi anlatır."},{"facet_id":"F003","role":"associated_use","statement":"Bir topluluğun üzerine kapatma ve ateşin üzerlerine kapatılmış olması, çekirdeğin yapıya bağlı kullanımlarıdır."}],"identity_rationale":"Kaynak ifadesi, bir şeyin başka bir şeyi içine alıp üstüne kapanması çekirdeğini; kapı kapatma, birilerinin üzerine kapatma ve kapatılmış ateş örnekleriyle birlikte açıkça verir. Hazırlanan dal bu ortak kapatma ve kuşatma anlamını doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kapatıp örten şey"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kuşatıp kapatma"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"üzerlerine kapattı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"kapıyı kapattı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"üzerlerine kapatılmış ateş"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kapatıp örten şey için kullanılan ad"}],"lexicalization_note":"Tanım genel kapatma çekirdeğini korur; kapıyı kapatma, insanların üzerine kapatma ve kapatılmış ateş kullanımlarını yalnızca bağlı yapılara özgü gerçekleşmeler olarak ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan üç karşılaştırma kapı kapatma, açıklığı tıkama ve erişimi engelleme ile karışabilecek sınırları gösterir, diğer adaylar ise daha uzak sonuçları ya da ayrı dal anlamlarını yineler.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal kapı üzerinde gerçekleşen özel bir eylemdir; odak dalın çekirdeği ise daha genel kuşatıp kapatma ilişkisidir ve kapı dışındaki nesne ya da katılımcılara da uygulanır.","focus_only":"Odak dal, bir şeyi kuşatıp üzerine kapanma ile kapatılmış nesne ve durumları da kapsar.","gloss":"kapıyı çekip kapatma","neighbor_only":"Komşu dal özellikle kapıyı geri itip kapatma eylemine bağlıdır.","neighbor_ref":"root_000279/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da kapının kapalı duruma getirilmesini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalın tanımlayıcı yönü kuşatıp üzerine kapanmadır; komşu dalda ise belirleyici işlem boşluğu tıkamak veya ağzı sıkıca bağlamaktır.","focus_only":"Odak dal, bir şeyin başka bir şeyin üzerine kapanması veya onu kuşatması işlemini öne çıkarır.","gloss":"açıklığı tıkayıp kapatma","neighbor_only":"Komşu dal, bir açıklığın tıkaçla ya da sıkıca bağlanarak ortadan kaldırılmasını öne çıkarır.","neighbor_ref":"root_000884/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da açıklığın kalmaması ve dışarıyla bağlantının kesilmesi sonucu bulunur."},{"boundary_match":"partial","distinction":"Erişimin engellenmesi odak dalda kapatmanın sonucu olabilir; komşu dalda ise sonuç doğrudan çekirdektir ve kuşatıp kapanma şart değildir.","focus_only":"Odak dal somut biçimde kuşatıp kapatma işlemini bildirir.","gloss":"erişimi engelleme","neighbor_only":"Komşu dalın çekirdeği, belirli bir kapatma biçimi aramadan erişimi engellemektir.","neighbor_ref":"root_000294/B001","relation_type":"near_neighbor","shared_zone":"Kapatma, içeridekine erişimi engelleyebilir ve böylece iki anlam aynı sonuçta buluşabilir."}],"source_phrase_ar":"شيء يشتمل على الشيء (maqayis); الإِصد والإِصاد والوصاد بمنزلة المطبق (ayn); أصدت عليهم وأوصدته (ayn); نار مُؤصدة أي مطبقة (ayn); آصدت الباب إذا أغلقته (sihah)","source_summary":"Kaynaklar, anlamı bir şeyin diğerini kuşatıp kapatması çevresinde birleştirir; ad biçimleri kapatan şeyi, eylem biçimleri ise kapatma işlemini belirtir.","sources":["MQ","AY","SI"],"what_is_ar":"يدخل فيه الإِصاد والإِصد بمعنى المطبق؛ وآصدت الباب؛ ونار مُؤصدة","what_is_not_ar":"الحظيرة والقميص والفناء والموضع"},"support_links":["sup_165680375e97542f7f38","sup_5d2776aaaf2cae3635f9","sup_a67359983706f42e9f71"]},{"boundary":"Bu dal bir kapatma eylemini değil, içindekileri çevreleyen ve tutan alan türünü anlatır.","branch_kind":"bare","branch_ref":"root_000036/B002","candidate_links":[{"candidate_id":"cand_a476a0d17ba22279c9f8","lane":"macro"},{"candidate_id":"cand_a9e991d63f66fb4186cb","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"مُّؤْصَدَة","morph_features":"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:8:3:1","qac_word_ref":"104:8:3","surface_ar":"مُّؤْصَدَةٌ"}],"gloss":"çevrili barınak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Alan, içinde bulunanları çevreler ve sınırları içinde bir arada tutar."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynak ifadesinde bu alan, ağıl ya da ona denk bir çevrili yer olarak açıklanır."}}],"root_ar":"و ص د","root_id":"root_000036","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İçindekileri çevreleyip bir arada tutan alanın yalın ve genel Türkçe karşılığıdır.","boundary_detail":"Bu dal bir kapatma eylemini değil, içindekileri çevreleyen ve tutan alan türünü anlatır.","branch_image_ar":"الحظيرة المشتملة على ما فيها","concept_gloss":"çevrili barınak","contextual_glosses":[{"applicability":"Çevrili alanın hayvan barındıran bir yer olarak kullanıldığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İçeride tutulanların mutlaka hayvan olmadığı daha genel alan kapsamını daraltır.","preserves":"Çevrili ve barındırıcı alan niteliğini korur."},"facet_ids":["F002"],"text":"ağıl","usage_role":"contextual"}],"definition":"İçinde bulunanları çevreleyerek bir arada tutan, barınak veya ağıl niteliğindeki çevrili alandır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Alan, içinde bulunanları çevreler ve sınırları içinde bir arada tutar."},{"facet_id":"F002","role":"source_variant","statement":"Kaynak ifadesinde bu alan, ağıl ya da ona denk bir çevrili yer olarak açıklanır."}],"identity_rationale":"Kaynak ifadesi, içindekileri çevreleyip barındırdığı için bu adla anılan bir çitli ya da çevrili alanı doğrudan tanımlar. Hazırlanan dalın çevreleme ve içeride tutma çerçevesi bu ifadeyle uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"içindekileri çevreleyen barınak veya ağıl"}],"lexicalization_note":"Tanım yalın alan adını esas alır ve başka dallardaki kapatma eylemi ya da özel söz öbeklerini bu anlama katmaz.","neighbor_coverage_note":"Tüm adaylar incelendi; hayvan ağılı, çitli alan ve somut çevreleme ile yapılan üç karşılaştırma dalın yer türü ve kapsam sınırını yeterince belirginleştirir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal hayvan barındırma bakımından özelleşmiştir; odak dalın kaynak ifadesi ise çevreleme ve içeride tutmayı temel alır, içeridekilerin türünü sınırlamaz.","focus_only":"Odak dal, içindekileri çevreleyen alanı barındırdığı şeyin türünü zorunlu kılmadan adlandırır.","gloss":"hayvan ağılı","neighbor_only":"Komşu dal özellikle sığır veya koyun gibi hayvanların barındığı ağılı anlatır.","neighbor_ref":"root_000897/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da çevrili bir barınak veya ağıl alanını gösterebilir."},{"boundary_match":"partial","distinction":"Odak dal kapsayıcı alan adı olarak daha yalındır; komşu dal yapı malzemesini, duvarı ve çevrili yerin farklı kullanım alanlarını ayrıca kapsar.","focus_only":"Odak dal, alanın içindekileri kapsayıp bir arada tutma işlevini öne çıkarır.","gloss":"çitli alan","neighbor_only":"Komşu dal, ahşap, kamış veya ağaçtan yapılabilen duvarı ve bu duvarla kurulan çevrili yeri de kapsar.","neighbor_ref":"root_000338/B001","relation_type":"near_synonym","shared_zone":"İki dal da içindekileri sınırlandıran çevrili alanı anlatır."},{"boundary_match":"partial","distinction":"Odak dal bir yer türüdür; komşu dalın çekirdeği ise o yeri meydana getirebilen çevreleme ilişkisidir.","focus_only":"Odak dal, çevreleme sonucunda oluşan barınak niteliğindeki alanı adlandırır.","gloss":"çevreleme","neighbor_only":"Komşu dal, bir şeyi duvarla veya başka unsurlarla çevreleme eylem ve durumunu anlatır.","neighbor_ref":"root_000372/B001","relation_type":"near_neighbor","shared_zone":"Çevrili bir alan, somut çevreleme işleminin sonucudur."}],"source_phrase_ar":"الحظيرة أُصيدة سميت بذلك لاشتمالها على ما فيها (maqayis); الأُصيدة كالحظيرة لغة في الوصيدة (sihah)","source_summary":"Kaynaklar, bu adı içindekileri çevreleyip tutan ağıl benzeri bir alan için verir ve adlandırmayı alanın kapsayıcı niteliğiyle ilişkilendirir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه الأُصيدة بمعنى الحظيرة أو الوصيدة لاشتمالها على ما فيها","what_is_not_ar":"الإغلاق والقميص والفناء والموضع"},"support_links":["sup_dc0dac4740d7cd2ef07c","sup_effc37c280bf1d1f85ae"]},{"boundary":"Giysi anlamı dalın çekirdeğidir; giysiye sahip olma ve onu giydirme eylemi çekirdekle eşitlenmemelidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000036/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُّؤْصَدَة","morph_features":"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:8:3:1","qac_word_ref":"104:8:3","surface_ar":"مُّؤْصَدَةٌ"}],"gloss":"kız çocuklarının giydiği küçük veya içe giyilen gömlek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kız çocuklarının giydiği küçük bir gömlek veya giysi altına giyilen gömlek türüdür."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kız çocuğunun bu giysiye sahip olduğu, giysi adıyla kurulan bağlı bir yapıda belirtilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Türemiş eylem, birine bu küçük gömleği giydirmeyi anlatır."}}],"root_ar":"و ص د","root_id":"root_000036","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynaklardaki küçük gömlek ve giysi altına giyilen gömlek çeşitlerini, kız çocuklarıyla ilişkisini koruyarak seçenekli biçimde yansıtır.","boundary_detail":"Giysi anlamı dalın çekirdeğidir; giysiye sahip olma ve onu giydirme eylemi çekirdekle eşitlenmemelidir.","branch_image_ar":"الأُصدة التي تلبسها الصبايا","concept_gloss":"kız çocuklarının giydiği küçük veya içe giyilen gömlek","contextual_glosses":[{"applicability":"Kullanıcının bağlamdan kız çocuğu olduğunun anlaşıldığı giysi anlatımlarında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kız çocuklarına özgü kullanım bilgisini açıkça söylemez.","preserves":"Giysinin küçük bir iç gömleği olmasını korur."},"facet_ids":["F001"],"text":"küçük iç gömleği","usage_role":"general"},{"applicability":"Kız çocuğunun söz konusu giysiye sahip olduğunu bildiren bağlı yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kız çocuğu ile sahip olduğu küçük iç gömleği arasındaki ilişkiyi eksiksiz korur."},"facet_ids":["F002"],"text":"küçük iç gömleği olan kız","usage_role":"contextual"},{"applicability":"Birine bu özel giysi türünün giydirildiği türemiş eylem bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Giysiyi başka birine giydirme işlemini ve giysi türünü korur."},"facet_ids":["F003"],"text":"küçük iç gömleğini giydirmek","usage_role":"contextual"}],"definition":"Kız çocuklarının giydiği küçük bir gömlek ya da başka bir giysinin altına giyilen gömlektir. Bu giysiye sahip olma ve birine onu giydirme, ayrı yapılarda kurulan bağlı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kız çocuklarının giydiği küçük bir gömlek veya giysi altına giyilen gömlek türüdür."},{"facet_id":"F002","role":"associated_use","statement":"Bir kız çocuğunun bu giysiye sahip olduğu, giysi adıyla kurulan bağlı bir yapıda belirtilir."},{"facet_id":"F003","role":"extension","statement":"Türemiş eylem, birine bu küçük gömleği giydirmeyi anlatır."}],"identity_rationale":"Kaynak ifadesi kız çocuklarının giydiği küçük gömleği veya giysi altına giyilen gömleği temel alır, fakat aynı iddia bu giysiye sahip olma ve birine bu giysiyi giydirme yapılarını da içerir. Dal korunabilir; giysinin kendisi çekirdek, sahiplik ve giydirme ise yapıya bağlı kullanımlar olarak ayrılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kız çocuklarının giydiği küçük veya içe giyilen gömlek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"küçük iç gömleği olan kız"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"ona küçük iç gömleğini giydirdi"}],"lexicalization_note":"Tanım küçük iç gömleğini merkezde tutar; giysiye sahip olma ve birine onu giydirme anlamlarını yalnızca ilgili söz öbekleri ve türemiş eylemle sınırlar.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; küçük kısa giysi, iç kat ve genel gömlek karşılaştırmaları bu özel çocuk giysisinin biçim, kullanım ve kullanıcı sınırlarını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal gömlek ve içe giyilme özellikleriyle sınırlıdır; komşu dal ise kesim ve gövdedeki duruş bakımından farklı kısa giysileri de içine alır.","focus_only":"Odak dal, kız çocuklarının giydiği veya başka giysinin altına giyilen küçük gömleği anlatır.","gloss":"kısa çocuk giysisi","neighbor_only":"Komşu dal küçük gömleğin yanında gövdeye asılı duran, bele kadar uzanan başka kısa giysi türlerini de kapsar.","neighbor_ref":"root_001039/B015","relation_type":"near_synonym","shared_zone":"Her iki dal da kız çocuklarıyla ilişkilendirilebilen küçük veya kısa bir üst giysisini gösterebilir."},{"boundary_match":"partial","distinction":"Odak dal çocuklara özgü küçük gömlek türüdür; komşu dalın kullanıcı, konum ve giysi biçimi kapsamı daha geniştir.","focus_only":"Odak dal giysiyi küçük kızların giydiği küçük bir gömlek olarak sınırlar.","gloss":"giysi altına giyilen ince kat","neighbor_only":"Komşu dal iki giysi arasında, zırh altında veya kadınların bedeninin başka bölümünde kullanılan daha geniş bir iç giysi sınıfıdır.","neighbor_ref":"root_001102/B007","relation_type":"near_synonym","shared_zone":"İki dal da başka bir giysinin altında giyilen bir giysiyi anlatabilir."},{"boundary_match":"partial","distinction":"Genel gömlek karşılığı odak dalın kullanıcı ve kullanım sınırlarını siler; odak dal da komşunun genel ve aktarmalı kapsamının tümünü taşımaz.","focus_only":"Odak dal küçük boyut, içe giyilme ve kız çocuklarıyla kullanım sınırlarını taşır.","gloss":"gömlek","neighbor_only":"Komşu dal genel gömlek ve giyme anlamlarının yanı sıra örtü ve görev gibi aktarmalı kullanımları da kapsar.","neighbor_ref":"root_001256/B001","relation_type":"near_synonym","shared_zone":"Odak giysi genel gömlek sınıfının küçük ve özel bir türüdür."}],"source_phrase_ar":"الأُصدة قميص صغير يلبسه الصبايا (maqayis); صبية ذات مُؤصد (maqayis); الأُصدة قميص يلبس تحت الثوب وتلبسه صغار الجواري (sihah); أصدته تأصيدا (sihah)","source_summary":"Kaynaklar küçük kızların giydiği, kimi açıklamada başka bir giysinin altında bulunan küçük gömleği bildirir; ayrıca bu giysiye sahip olma ve onu giydirme yapıları aynı iddiada yer alır.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه الأُصدة وهي قميص صغير أو قميص يلبس تحت الثوب وتلبسه صغار الجواري","what_is_not_ar":"الإغلاق والحظيرة والفناء والموضع"},"support_links":[]},{"boundary":"Dal yalnızca avlu anlamıdır; kapı, giriş veya kapatma anlamları bu dala taşınmaz.","branch_kind":"bare","branch_ref":"root_000036/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُّؤْصَدَة","morph_features":"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:8:3:1","qac_word_ref":"104:8:3","surface_ar":"مُّؤْصَدَةٌ"}],"gloss":"avlu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yapıyla bağlantılı açık alanı, başka bir deyişle avluyu belirtir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu anlam, aynı avlu adının dilsel bir biçim değişkesi olarak aktarılır."}}],"root_ar":"و ص د","root_id":"root_000036","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yapıyla bağlantılı açık alan anlamını tam ve doğal biçimde karşılar.","boundary_detail":"Dal yalnızca avlu anlamıdır; kapı, giriş veya kapatma anlamları bu dala taşınmaz.","branch_image_ar":"الفناء والوصيد","concept_gloss":"avlu","contextual_glosses":[{"applicability":"Açık alanın bir eve bağlı olduğunun bağlamda belirtilmesi gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ev dışındaki yapılara bağlı avlu olasılığını sınırlar.","preserves":"Avlunun bir yapıyla bağlantılı açık alan olmasını korur."},"facet_ids":["F001"],"text":"evin avlusu","usage_role":"contextual"}],"definition":"Bir evin ya da yapının çevresinde veya önünde bulunan açık alan, yani avludur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yapıyla bağlantılı açık alanı, başka bir deyişle avluyu belirtir."},{"facet_id":"F002","role":"source_variant","statement":"Bu anlam, aynı avlu adının dilsel bir biçim değişkesi olarak aktarılır."}],"identity_rationale":"Kaynak ifadesi sözcüğü doğrudan avlu anlamındaki başka bir biçimin dilsel çeşidi olarak tanımlar. Hazırlanan dalın avlu odağı bu tek kaynaklı ve açık tanımla tam olarak örtüşür.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"avlu"}],"lexicalization_note":"Tanım yalın biçimin avlu anlamıyla sınırlıdır ve komşu biçimin kapı gibi ek anlamlarını ya da başka söz öbeklerini içeri almaz.","neighbor_coverage_note":"Bütün komşular gözden geçirildi; ev avlusu, evin önü ve genel açık alanla ilgili üç yakın karşılaştırma avlu çekirdeğini ve kapı anlamının dışarıda kalışını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Avlu bağlamında anlamlar örtüşür, ancak komşu dalın kapı kapsamı odak dalda bulunmaz; bu nedenle tam eş anlamlılık yalnızca avlu kullanımında geçerlidir.","focus_only":null,"gloss":"ev avlusu veya kapısı","neighbor_only":"Komşu dal avlunun yanı sıra evin kapısını da gösterebilir ve alanı eve bitişik oluşuyla açıklar.","neighbor_ref":"root_001653/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da evle bağlantılı avlu anlamında kullanılabilir."},{"boundary_match":"partial","distinction":"Odak dal genel avlu adıdır; komşu dal alanın evin yanlarına uzanması ve önündeki genişlik gibi mekânsal ayrıntıları ayrıca taşır.","focus_only":"Odak dal yalın biçimde avlu alanını adlandırır.","gloss":"evin avlusu ve önü","neighbor_only":"Komşu dal evin çevresine uzanan alanı ve özellikle evin önündeki genişliği de vurgular.","neighbor_ref":"root_001181/B002","relation_type":"near_synonym","shared_zone":"İki dal evle bağlantılı avlu veya açık alan anlamında buluşur."},{"boundary_match":"partial","distinction":"Gösterilen yer büyük ölçüde örtüşse de odak dal belirli bir avlu adının biçim çeşididir; komşu dalın sözlüksel kapsamı evin sahası olarak bağımsızdır.","focus_only":"Odak dal kaynakta başka bir avlu adının söyleyiş çeşidi olarak belirlenmiştir.","gloss":"evin açık alanı","neighbor_only":"Komşu dal evin saha ve açık alanını daha genel bir yer adıyla ifade eder.","neighbor_ref":"root_000756/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bir evin avlusunu veya açık sahasını gösterebilir."}],"source_phrase_ar":"الأَصيد لغة في الوصيد وهو الفناء (sihah)","source_summary":"Tek kaynak, biçimi avlu anlamındaki eşdeğer bir söyleyiş çeşidi olarak verir.","sources":["SI"],"what_is_ar":"يدخل فيه الأَصيد لغة في الوصيد وهو الفناء","what_is_not_ar":"الإغلاق والحظيرة والقميص والموضع"},"support_links":[]},{"boundary":"Dağlar arasındaki çukur alan yer türüdür; belirli yeri gösteren uzun ifade ise bu çekirdeğe bağlı ayrı bir sözlüksel kullanımdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000036/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُّؤْصَدَة","morph_features":"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:8:3:1","qac_word_ref":"104:8:3","surface_ar":"مُّؤْصَدَةٌ"}],"gloss":"dağlar arasındaki çukur alan","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dağlar arasında yer alan çukur veya çanak biçimli doğal alanı belirtir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Daha uzun bir sözlüksel ifade, belirli bir yerin adı olarak kullanılır."}}],"root_ar":"و ص د","root_id":"root_000036","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın biçimin doğal yer türünü eksiksiz karşılar; belirli yer kullanımı ayrıca bağlamsal olarak gösterilir.","boundary_detail":"Dağlar arasındaki çukur alan yer türüdür; belirli yeri gösteren uzun ifade ise bu çekirdeğe bağlı ayrı bir sözlüksel kullanımdır.","branch_image_ar":"الموضع بين الجبال","concept_gloss":"dağlar arasındaki çukur alan","contextual_glosses":[{"applicability":"Dağlar arasında kalan çukur ve çanak biçimli doğal alanın kısa bağlamsal karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dağlarla çevrili çukur alan görünümünü doğal bir Türkçe ifadeyle korur."},"facet_ids":["F001"],"text":"dağ çanağı","usage_role":"contextual"},{"applicability":"Daha uzun sözlüksel ifadenin özel bir yeri gösterdiği kullanım açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yerin dağlar arasındaki çukur alanla sözlüksel bağlantısını açıkça taşımaz.","preserves":"İfadenin tek ve belirli bir yere gönderimde bulunmasını korur."},"facet_ids":["F002"],"text":"belirli bir yer","usage_role":"explanatory"}],"definition":"Dağlar arasında bulunan çukur veya çanak biçimli bir alandır. Daha uzun bir sözlüksel yapıda ise belirli bir yeri gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dağlar arasında yer alan çukur veya çanak biçimli doğal alanı belirtir."},{"facet_id":"F002","role":"associated_use","statement":"Daha uzun bir sözlüksel ifade, belirli bir yerin adı olarak kullanılır."}],"identity_rationale":"Kaynak ifadesi iki bağlı kullanımı birlikte verir: dağlar arasındaki çukur alanı belirten yalın biçim ve belirli bir yeri gösteren daha uzun ifade. Hazırlanan dal kullanılabilir, ancak yer türü ile özel bir yeri belirten sözlüksel kullanım tek ve belirsiz bir yer anlamıymış gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"belirli bir yer adı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"dağlar arasındaki çukur alan"}],"lexicalization_note":"Tanım yalın biçimin dağlar arasındaki çukur alan anlamıyla daha uzun ifadenin belirli yer kullanımını açıkça ayırır.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; alçak arazi, tepe arası çöküntü, dağ geçidi ve özel dağ adı karşılaştırmaları doğal yer türü ile belirli yer kullanımının sınırlarını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dağlık çevre ve çukur alanla sınırlıdır; komşu dal farklı yükselti türleri ve benzetmeli beden bölgeleri arasında da kullanılabilir.","focus_only":"Odak dal dağlarla çevrili çukur bir alanı belirtir.","gloss":"iki yükselti arasındaki alçak yer","neighbor_only":"Komşu dal iki yükselti, kum sırtı veya başka beden çıkıntıları arasındaki alçak boşluğa kadar uzanan daha geniş bir kapsama sahiptir.","neighbor_ref":"root_001176/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da dağlar veya yükseltiler arasında kalan alçak bir yeri gösterebilir."},{"boundary_match":"partial","distinction":"Odak dal çanak veya çukur alanı vurgular; komşu dalın ayırt edici yönü düşen şeyin yöneldiği alçak ve eğimli yer olmasıdır ve ayrıca araç parçasına uzanır.","focus_only":"Odak dal dağlar arasındaki çukur doğal alanı yer türü olarak adlandırır.","gloss":"iki tepe arasındaki alçak yer","neighbor_only":"Komşu dal iki tepe arasındaki eğimli alçak yerin yanı sıra tahılın düştüğü değirmen bölümünü de kapsar.","neighbor_ref":"root_000402/B003","relation_type":"near_neighbor","shared_zone":"İki dal, yükseltiler arasında bulunan alçak bir doğal alanı anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal kapalıca bir çukur alan görünümündedir; komşu dal ise aralık, geçiş yolu veya akış koridoru olmasıyla ayrılır.","focus_only":"Odak dal dağlar arasında kalan çukur veya çanak biçimli alanı anlatır.","gloss":"dağ geçidi","neighbor_only":"Komşu dal iki dağ arasındaki yarık, geçit, yol veya su yatağı niteliğini öne çıkarır.","neighbor_ref":"root_000797/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da iki dağ arasındaki bir arazi biçimini gösterebilir."},{"boundary_match":"thematic_only","distinction":"Odak dalın yalın biçiminde tanımlanabilir bir arazi türü vardır; komşu dal ise yalnızca belirli bir coğrafi varlığı adlandırır.","focus_only":"Odak dal bir doğal yer türünü ve buna bağlı belirli yer kullanımını içerir.","gloss":"belirli dağ veya yer adı","neighbor_only":"Komşu dal belirli bir dağın veya yerin özel adıdır.","neighbor_ref":"root_001243/B009","relation_type":"thematic","shared_zone":"İki dal da dağlık bir coğrafyada belirli bir yere gönderimde bulunabilir."}],"source_phrase_ar":"ذات الأَصاد موضع (sihah); الأَصاد ردهة بين أجبل (sihah)","source_summary":"Tek kaynak, yalın biçimi dağlar arasındaki çukur alan olarak açıklar ve aynı öğeyi içeren daha uzun ifadeyi belirli bir yer için kaydeder.","sources":["SI"],"what_is_ar":"يدخل فيه الأَصاد علما على موضع أو ردهة بين أجبل","what_is_not_ar":"الإغلاق والحظيرة والقميص والفناء"},"support_links":[]},{"boundary":"It covers al-jamʿ as inferior or seed-grown date-palms whose specific variety is not known.","branch_kind":null,"branch_ref":"root_000259/B011","candidate_links":[{"candidate_id":"cand_b2a1c4ffab694254b498","lane":"macro"}],"focus_root_occurrences":[],"gloss":"seed-grown date-palms of unnamed kind","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"نخل دقل اجتمع من النوى لا يعرف اسمه","image_en":"seed-grown date-palms of unnamed kind"}}],"root_ar":"ج م ع","root_id":"root_000259","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"نخل دقل اجتمع من النوى لا يعرف اسمه","image_en":"seed-grown date-palms of unnamed kind","scope_ar":"يدخل فيه الجمع بمعنى الدقل أو كل لون من النخل خرج من النوى ولا يعرف اسمه.","scope_en":"It covers al-jamʿ as inferior or seed-grown date-palms whose specific variety is not known."},"support_links":["sup_5f7a4f8320a8a28a7f86"]},{"boundary":"Includes the palm spadix or inflorescence, the palm putting it forth, and crops beginning to appear.","branch_kind":null,"branch_ref":"root_000945/B005","candidate_links":[{"candidate_id":"cand_b2a1c4ffab694254b498","lane":"macro"}],"focus_root_occurrences":[],"gloss":"emergence of palm spadix and plants","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"خروج الطلع والنبات","image_en":"emergence of palm spadix and plants"}}],"root_ar":"ط ل ع","root_id":"root_000945","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"خروج الطلع والنبات","image_en":"emergence of palm spadix and plants","scope_ar":"يدخل فيه طلع النخلة وطلعتها، وإطلاع النخل، وظهور الزرع إذا بدا","scope_en":"Includes the palm spadix or inflorescence, the palm putting it forth, and crops beginning to appear."},"support_links":["sup_5f7a4f8320a8a28a7f86"]},{"boundary":"This covers tree blossom, bloom, and a tree putting forth its blossoms.","branch_kind":null,"branch_ref":"root_001564/B004","candidate_links":[{"candidate_id":"cand_b2a1c4ffab694254b498","lane":"macro"}],"focus_root_occurrences":[],"gloss":"tree blossom and bloom","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"نور الشجر وزهره","image_en":"tree blossom and bloom"}}],"root_ar":"ن و ر","root_id":"root_001564","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"نور الشجر وزهره","image_en":"tree blossom and bloom","scope_ar":"يدخل فيه نور الشجر ونواره، وتنوير الشجرة أو إنارتها بمعنى إزهارها وإخراج نورها.","scope_en":"This covers tree blossom, bloom, and a tree putting forth its blossoms."},"support_links":["sup_5f7a4f8320a8a28a7f86"]},{"boundary":"Genel bitiştirme çekirdeği ile kapıyı örtüp sıkıca kapatma gerçekleşimi ayrı tutulmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001653/B001","candidate_links":[{"candidate_id":"cand_8ba5c25e88f9feecc3a3","lane":"macro"},{"candidate_id":"cand_f718b7c92959d2a7a4ff","lane":"macro"},{"candidate_id":"cand_f40721ca343636338e9c","lane":"macro"},{"candidate_id":"cand_96152092b327e933d309","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"مُّؤْصَدَة","morph_features":"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:8:3:1","qac_word_ref":"104:8:3","surface_ar":"مُّؤْصَدَةٌ"}],"gloss":"bitiştirerek sıkıca kapatma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel ilişki, bir şeyi başka bir şeye katıp iki şeyi birbirine bitiştirmektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kapıya bağlı gerçekleşimde kapı örtülür, iki yüzey birbirine getirilir ve kapanış sağlamlaştırılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Eylemin sonucu, kapının bütünüyle örtülmüş ve sıkıca kapalı durumda bulunmasıdır."}}],"root_ar":"و ص د","root_id":"root_001653","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel bitiştirme çekirdeğini ve kapı bağlamındaki örtme, sağlam kapatma ve kapalı sonuç bütününü birlikte anlatır.","boundary_detail":"Genel bitiştirme çekirdeği ile kapıyı örtüp sıkıca kapatma gerçekleşimi ayrı tutulmalıdır.","branch_image_ar":"إطباق الباب وإحكام إغلاقه","concept_gloss":"bitiştirerek sıkıca kapatma","contextual_glosses":[{"applicability":"Kapının örtülerek sağlam biçimde kapatıldığı eylem bağlamlarında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel bitiştirme çekirdeğini ve kapalı sonucu ayrıca adlandırmaz.","preserves":"Kapıya uygulanan örtme ve sağlam kapatma eylemini korur."},"facet_ids":["F002"],"text":"kapıyı sıkıca kapatmak","usage_role":"contextual"},{"applicability":"Eylemden çok kapının eriştiği örtülü ve sağlam kapalı durumu öne çıkaran bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bitiştirme çekirdeğini ve kapatma işlemini göstermez.","preserves":"Ortaya çıkan sağlam kapalı durumu korur."},"facet_ids":["F003"],"text":"sıkıca kapalı","usage_role":"contextual"}],"definition":"Bir şeyi başka bir şeye katıp bitiştirme düşüncesidir. Kapı bağlamında iki yüzeyi birbirine getirerek kapıyı örtmeyi, sıkıca kapatmayı ve böyle kapalı durumda bulunmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel ilişki, bir şeyi başka bir şeye katıp iki şeyi birbirine bitiştirmektir."},{"facet_id":"F002","role":"specialization","statement":"Kapıya bağlı gerçekleşimde kapı örtülür, iki yüzey birbirine getirilir ve kapanış sağlamlaştırılır."},{"facet_id":"F003","role":"extension","statement":"Eylemin sonucu, kapının bütünüyle örtülmüş ve sıkıca kapalı durumda bulunmasıdır."}],"identity_rationale":"Kaynak sözü, kapıyı kapatma kullanımının arkasında bir şeyi başka bir şeye katıp bitiştirme çekirdeğini de açıkça verir. Bu nedenle sağlanan kapı çerçevesi geçerlidir, ancak dalın bütününü yalnızca kapıyla sınırlandırmamak gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kapıyı örtüp sıkıca kapatmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kapıyı örtüp sıkıca kapatmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"örtülmüş ve kapalı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"örtülmüş ve sıkıca kapatılmış"}],"lexicalization_note":"Tanım, genel bitiştirme çekirdeğini kapıya bağlı eylem ve kapalı durum bildiren biçimlerle kaynaştırmadan ayırır.","neighbor_coverage_note":"En yakın kapanma eylemleri, kilitleme alanı ve aynı kökteki kapı adı yayımlandı; set çekme, çevreleme, mühürleme, taş barınak ve bitki dalları ise ya daha uzak ya da bu karşıtlıkları yineleyen adaylardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kapıdaki yüzeyleri bitiştirip kapanışı sağlamlaştırırken komşu dalın kapsamı bir şeyin üzerine kapanma yönünde daha geneldir.","focus_only":"Bitiştirme yönü ve kapının sağlam biçimde kapanması bu dalda birlikte öne çıkar.","gloss":"üzerine kapatma","neighbor_only":"Komşu dal, kapanmayı kapı dışındaki bir şeyin üzerine kapanma biçiminde de kurar.","neighbor_ref":"root_000036/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyi örtme, kapatma ve kapalı duruma getirme alanını paylaşır."},{"boundary_match":"partial","distinction":"Komşu dal kapıyı geri getiren hareketi öne çıkarır; bu dal ise yüzeylerin bitişmesiyle oluşan tam ve sağlam kapanışı vurgular.","focus_only":"Yüzeyleri bitiştirme, kapanışı sıkılaştırma ve kapalı sonucu birlikte içerir.","gloss":"kapıyı geri çekip kapatma","neighbor_only":"Kapıyı geri itme ya da çekme hareketi komşu dalın ayırt edici yönüdür.","neighbor_ref":"root_000279/B007","relation_type":"near_synonym","shared_zone":"İki dal da kapının açık durumdan kapalı duruma geçirilmesini anlatır."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeği örtüp kapatmaktır; komşu dalın çekirdeği kilitleme ya da bağlama yoluyla kapalı tutmadır ve daha geniş yan anlamları vardır.","focus_only":"Kapının örtülüp yüzeylerinin bitişmesi ve böylece kapalı duruma gelmesi anlatılır.","gloss":"kilitleyip bağlama","neighbor_only":"Kilitleme ve bağlama yanında sertleşme, kuruma ve başka genişlemeler de bulunur.","neighbor_ref":"root_001246/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal kapının açılmasını engelleyen sağlam bir kapanışla ilişkilendirilebilir."},{"boundary_match":"field_only","distinction":"Bu dal bir kapatma işlemi ve durumudur; komşu dal ise bir yerin ya da nesnenin adıdır, bu nedenle ortak bağlam anlam özdeşliği doğurmaz.","focus_only":"Kapıyı örtme ve sıkıca kapatma eylemi ile bunun sonucu anlatılır.","gloss":"eve bağlı avlu veya kapı","neighbor_only":"Eve bağlı açık alanı ya da bazı kullanımlarda kapının kendisini adlandırır.","neighbor_ref":"root_001653/B002","relation_type":"same_field","shared_zone":"Her iki dalın kullanımı ev ve kapı çevresinde görülebilir."}],"source_phrase_ar":"أصل يدل على ضم شيء إلى شيء (maqayis)؛ أوصدت الباب أغلقته والموصد المطبق (maqayis)؛ أوصدت الباب وآصدته إذا أغلقته فهو موصد ومطبقة (sihah)؛ أوصدت الباب وآصدته أي أطبقته وأحكمته ومؤصدة مطبقة (mufradat)","source_summary":"Kaynakların ortak anlatımı, bitiştirme temelini kapının örtülüp kapanmasıyla ilişkilendirir; kapatma eylemi, sıkılık ve ortaya çıkan kapalı durum aynı anlam çevresinde yer alır.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه أوصدت وآصدت الباب بمعنى أغلقته، والموصد أو المؤصد بمعنى المطبق المحكم.","what_is_not_ar":"لا يدخل فيه الوصيد بمعنى الفناء أو النبات أو الوصيدة الحجرية إلا من جهة اشتراكها في أصل الضم والاتصال."},"support_links":["sup_4daa7b66b5ecfc645bc8","sup_4f2ab0a9681fb98b573c","sup_92c77e8ebb3c8ac9b9eb","sup_a1caae65b879709ccb2c"]},{"boundary":"Eve bağlı açık alan temel anlamdır; kapı anlamı kaynaklarda yer alan ayrı bir kullanım olarak korunmalıdır.","branch_kind":"non_bare","branch_ref":"root_001653/B002","candidate_links":[{"candidate_id":"cand_8ba5c25e88f9feecc3a3","lane":"macro"},{"candidate_id":"cand_d436e7850e0fe0725385","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"مُّؤْصَدَة","morph_features":"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:8:3:1","qac_word_ref":"104:8:3","surface_ar":"مُّؤْصَدَةٌ"}],"gloss":"eve bağlı avlu veya kapı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderge, eve bağlı açık alan ya da evin önündeki avludur."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Açık alanın ayırt edici ilişkisi, evle bitişik ya da eve bağlı olmasıdır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı ad bazı kullanımlarda evin kapısını belirtir."}}],"root_ar":"و ص د","root_id":"root_001653","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Eve bağlı açık alanı temel gönderge, evin kapısını ise ayrı bir kaynak kullanımı olarak birlikte kapsar.","boundary_detail":"Eve bağlı açık alan temel anlamdır; kapı anlamı kaynaklarda yer alan ayrı bir kullanım olarak korunmalıdır.","branch_image_ar":"فناء البيت أو بابه المتصل بالربع","concept_gloss":"eve bağlı avlu veya kapı","contextual_glosses":[{"applicability":"Sözcük evin önündeki ya da eve bağlı açık alanı gösterdiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı adın kapıyı belirten kaynak kullanımını dışarıda bırakır.","preserves":"Eve bağlı açık alanın yer ve bağlantı niteliğini korur."},"facet_ids":["F001","F002"],"text":"evin avlusu","usage_role":"contextual"},{"applicability":"Sözcüğün açık alanı değil doğrudan evin kapısını gösterdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eve bağlı açık alan olan temel göndergeyi içermez.","preserves":"Kapıyı adlandıran kaynak kullanımını korur."},"facet_ids":["F003"],"text":"evin kapısı","usage_role":"contextual"}],"definition":"Eve bağlı olan ve evin önünde ya da çevresinde yer alan açık alandır. Bazı kullanımlarda evin kapısını da adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderge, eve bağlı açık alan ya da evin önündeki avludur."},{"facet_id":"F002","role":"core","statement":"Açık alanın ayırt edici ilişkisi, evle bitişik ya da eve bağlı olmasıdır."},{"facet_id":"F003","role":"source_variant","statement":"Aynı ad bazı kullanımlarda evin kapısını belirtir."}],"identity_rationale":"Kaynak sözü, eve bağlı açık alan anlamını bağlantı ilişkisiyle açıklar ve aynı biçim için kapı anlamını da bildirir. Sağlanan çerçeve bu iki tanıklığı sınırlarını bozmadan yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"evin avlusu veya kapısı"}],"lexicalization_note":"Tanım yalnızca belirtilen adın eve bağlı açık alan ve kapı anlamlarıyla sınırlıdır; kökün genel anlamı gibi sunulmaz.","neighbor_coverage_note":"Eve bağlı açık alan ve kapı anlamına en çok yaklaşan üç yer dalı ile aynı kökteki kapatma dalı yayımlandı; genel meydan, giriş, kısa duvar, gizlenme yeri ve diğer kök içi dallar daha uzak alan ilişkileridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Açık alan anlamında örtüşürler; bu dalın ayrıca kapı kullanımı bulunduğu için bütün kapsamları birbirinin yerine geçmez.","focus_only":"Eve bağlı açık alan yanında evin kapısını belirten ayrı bir kullanım da vardır.","gloss":"evin açık alanı","neighbor_only":"Komşu dal yalnızca açık alanı adlandıran sesçe farklı bir biçimdir.","neighbor_ref":"root_000036/B004","relation_type":"near_synonym","shared_zone":"İki dal da eve bağlı açık alanı aynı temel yer ilişkisiyle adlandırır."},{"boundary_match":"partial","distinction":"Bu dal eve bağlı avlu ile kapı arasında sınırlı kalır; komşu dal kapı önü yapıları ve başka kurumsal kullanımlara uzanır.","focus_only":"Eve bağlantıyla tanımlanan avlu ve ayrıca kapı kullanımı bulunur.","gloss":"kapı önü ve avlu","neighbor_only":"Kapı önü, eşik çevresi, gölgelik ya da yönetici kapıları gibi daha geniş kullanımları kapsar.","neighbor_ref":"root_000687/B004","relation_type":"near_synonym","shared_zone":"Her iki dal kapıyı ve kapının önündeki açık alanı adlandırabilir."},{"boundary_match":"partial","distinction":"Komşu dal açık alanın yayılım ve genişlik yönünü öne çıkarır; bu dal ise eve bağlantıyı temel alır ve kapıyı da adlandırabilir.","focus_only":"Açık alanın yanında kapıyı adlandıran kullanım da bulunur.","gloss":"evin önü ve çevresindeki avlu","neighbor_only":"Evin önüne ve yanlarına uzanan genişliği özellikle belirtir.","neighbor_ref":"root_001181/B002","relation_type":"near_synonym","shared_zone":"İki dal da eve bitişik ya da evin önündeki açık alanı anlatır."},{"boundary_match":"field_only","distinction":"Bu dal bir yer ya da nesne adıdır; komşu dal ise kapıya uygulanan eylem ve ortaya çıkan durumdur.","focus_only":"Eve bağlı açık alanı veya kapının kendisini adlandırır.","gloss":"kapıyı sıkıca kapatma","neighbor_only":"Kapıyı örtme, yüzeylerini bitiştirme ve sıkıca kapatma eylemini anlatır.","neighbor_ref":"root_001653/B001","relation_type":"same_field","shared_zone":"İki dal da ev ve kapı çevresinde kullanılan kavramlardır."}],"source_phrase_ar":"الوصيد الفناء لاتصاله بالربع (maqayis)؛ الوصيد فناء البيت والوصيد الباب (ayn)؛ الوصيد الفناء (sihah)","source_summary":"Toplu kaynak anlatımında eve bağlı açık alan ortak merkezdir; bağlantı, bu adlandırmanın gerekçesi olarak verilir. Bunun yanında aynı adın evin kapısını belirttiği bir kullanım da kaydedilir.","sources":["MQ","AY","SI"],"what_is_ar":"يدخل فيه الوصيد بمعنى فناء البيت، وبمعنى الباب، والفناء لاتصاله بالربع.","what_is_not_ar":"لا يدخل فيه إطباق الباب فعلا، ولا الوصيدة الحجرية، ولا النبات المتقارب الأصول."},"support_links":["sup_4f2ab0a9681fb98b573c","sup_841384807a53aa4e0c3d"]},{"boundary":"Taştan yapılma, dağda bulunma ve hayvanları barındırma özellikleri genel çevrili alan anlamına indirgenmemelidir.","branch_kind":"mixed_non_bare","branch_ref":"root_001653/B003","candidate_links":[{"candidate_id":"cand_d436e7850e0fe0725385","lane":"macro"},{"candidate_id":"cand_265439d0dadc84eade74","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"مُّؤْصَدَة","morph_features":"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:8:3:1","qac_word_ref":"104:8:3","surface_ar":"مُّؤْصَدَةٌ"}],"gloss":"dağdaki taş hayvan barınağı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderge, hayvanları içinde tutmak ya da barındırmak için yapılmış oda benzeri çevrili bir yapıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yapı dağda bulunur ve dallardan değil taşlardan yapılmasıyla sıradan hayvan çevirmeliğinden ayrılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu yapıdan türeyen kullanım, dağda böyle bir taş barınak kurma eylemini anlatır."}}],"root_ar":"و ص د","root_id":"root_001653","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yapının dağda bulunmasını, taş malzemesini, çevrili oda biçimini ve hayvan barındırma amacını birlikte taşır.","boundary_detail":"Taştan yapılma, dağda bulunma ve hayvanları barındırma özellikleri genel çevrili alan anlamına indirgenmemelidir.","branch_image_ar":"وصيدة حجرية للمال في الجبل","concept_gloss":"dağdaki taş hayvan barınağı","contextual_glosses":[{"applicability":"Oda görünümünden çok hayvanları çevreleyip içinde tutma işlevinin öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dağda bulunma koşulunu ve oda biçimi seçeneğini açıkça belirtmez.","preserves":"Taş malzemeyi ve hayvanları çevrili alanda tutma işlevini korur."},"facet_ids":["F001","F002"],"text":"taştan hayvan çevirmeliği","usage_role":"contextual"},{"applicability":"Adlandırılan yapının kendisini değil, dağda bu yapıyı kurma eylemini anlatan kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yapı adının hayvan barındırma amacını açıkça söylemez.","preserves":"Dağda taş barınak yapma eylemini korur."},"facet_ids":["F003"],"text":"dağda taş barınak kurmak","usage_role":"contextual"}],"definition":"Dağda hayvanları barındırmak için taşlardan yapılan oda ya da çevrili alandır. Buna bağlı eylem, dağda böyle bir taş barınak kurmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderge, hayvanları içinde tutmak ya da barındırmak için yapılmış oda benzeri çevrili bir yapıdır."},{"facet_id":"F002","role":"specialization","statement":"Yapı dağda bulunur ve dallardan değil taşlardan yapılmasıyla sıradan hayvan çevirmeliğinden ayrılır."},{"facet_id":"F003","role":"associated_use","statement":"Bu yapıdan türeyen kullanım, dağda böyle bir taş barınak kurma eylemini anlatır."}],"identity_rationale":"Kaynak sözü, dağda hayvanları barındırmak için taşlardan yapılan oda ya da çevrili alanı açıkça tanımlar ve böyle bir yapı kurma eylemini de bildirir. Sağlanan dal çerçevesi yapı, malzeme, yer ve amaç sınırlarını korur.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"dağda hayvanlar için yapılan taş oda veya çevirmelik"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"dağda böyle bir taş barınak kurmak"}],"lexicalization_note":"Tanım, özel yapı adını dağda bu yapıyı kurma eyleminden ayırır ve ikisini genel bir çevreleme anlamına genişletmez.","neighbor_coverage_note":"Taş çevirmeliğe en yakın genel ve bitkisel malzemeli çevirmelikler, çevrili yer ve dağ mağarası yayımlandı; çatı, üst örtü, kapatma eylemi, avlu ve bitki dalları yapının yalnızca ortamını ya da uzak bir özelliğini paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalı belirleyen malzeme taş ve yer dağdır; komşu dal bitkisel malzemeli çevirmelikleri ve daha geniş amaçları kapsar.","focus_only":"Dağda bulunan ve özellikle taşlardan yapılan oda ya da çevrili barınaktır.","gloss":"dal veya kamıştan hayvan çevirmeliği","neighbor_only":"Tahta, kamış, ağaç ya da dallardan yapılabilir ve ekini çevreleme amacı da taşıyabilir.","neighbor_ref":"root_000338/B001","relation_type":"near_synonym","shared_zone":"İki dal da hayvanları bir arada tutan çevrili bir yapı bildirebilir."},{"boundary_match":"partial","distinction":"Komşu dal kuşatma işlevine dayalı genel çevirmeliktir; bu dal ise dağda hayvanlar için taştan yapılmış özel yapıdır.","focus_only":"Taş malzeme, dağ ortamı ve hayvan barındırma amacı zorunlu sınırlar olarak öne çıkar.","gloss":"içindekileri kuşatan çevirmelik","neighbor_only":"İçindekileri kuşatan genel bir çevirmelik olarak daha geniş kapsamlıdır.","neighbor_ref":"root_000036/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da içindekileri çevreleyip bir arada tutan barınak türünü anlatır."},{"boundary_match":"partial","distinction":"Bu dalın malzeme, yer ve kullanım amacı belirgindir; komşu dal ise çevrili mekânların genel alanıdır.","focus_only":"Dağda hayvanlar için taştan yapılan belirli bir oda ya da çevirmeliktir.","gloss":"duvarla çevrili yer","neighbor_only":"Duvarla çevrilmiş yer, oda, bahçe ve yerleşim gibi pek çok farklı mekânı kapsar.","neighbor_ref":"root_000296/B004","relation_type":"near_neighbor","shared_zone":"İki dal da sınırları belirlenmiş ve çevrelenmiş bir mekânı gösterebilir."},{"boundary_match":"field_only","distinction":"Bu dal taşla kurulan hayvan yapısıdır; komşu dal dağın içinde bulunan mağaradır ve yapım malzemesi ile hayvan amacı taşımaz.","focus_only":"Taşların bir araya getirilmesiyle hayvanlar için insan eliyle kurulan yapıdır.","gloss":"dağ mağarası","neighbor_only":"Dağın içinde doğal ya da oyulmuş geniş bir boşluktur.","neighbor_ref":"root_001325/B001","relation_type":"same_field","shared_zone":"Her iki dal da dağda bulunan, içine girilebilen ve barınma sağlayabilen bir yeri anlatır."}],"source_phrase_ar":"الوصيدة كالحظيرة تتخذ للمال إلا أنها من الحجارة والحظيرة من الغصنة واستوصدت في الجبل (sihah)؛ الوصيدة حجرة تجعل للمال في الجبل (mufradat)","source_summary":"Kaynakların ortak çekirdeği, dağda hayvanlar için yapılan taş oda ya da taşla çevrili barınaktır. Toplu anlatım ayrıca yapıyı dallardan yapılan çevirmelikten ayırır ve dağda bu yapıyı kurma eylemini kaydeder.","sources":["SI","MU"],"what_is_ar":"يدخل فيه الوصيدة: حجرة أو شبه حظيرة من حجارة تتخذ للمال في الجبل، ومنه استوصد في الجبل إذا اتخذها.","what_is_not_ar":"لا يدخل فيه الحظيرة من الغصنة عند الصحاح، ولا مطلق الفناء أو إغلاق الباب."},"support_links":["sup_841384807a53aa4e0c3d","sup_d3a112cca9f1e8f2f49e"]},{"boundary":"Yakınlık bitkinin üst bölümünde değil kökler arasındadır; yalnızca sık ya da bol bitki yeterli değildir.","branch_kind":"non_bare","branch_ref":"root_001653/B004","candidate_links":[{"candidate_id":"cand_b2a1c4ffab694254b498","lane":"macro"},{"candidate_id":"cand_7f972b2f4b2ec3934d08","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"مُّؤْصَدَة","morph_features":"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:8:3:1","qac_word_ref":"104:8:3","surface_ar":"مُّؤْصَدَةٌ"}],"gloss":"kökleri birbirine yakın bitki","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ayırt edici özellik, bitki köklerinin birbirine yakın aralıklarla bulunmasıdır."}}],"root_ar":"و ص د","root_id":"root_001653","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bitkiyi kökler arasındaki yakınlık ölçütüyle tanımlar ve başka bir sıklık türü eklemez.","boundary_detail":"Yakınlık bitkinin üst bölümünde değil kökler arasındadır; yalnızca sık ya da bol bitki yeterli değildir.","branch_image_ar":"نبات متقارب الأصول","concept_gloss":"kökleri birbirine yakın bitki","contextual_glosses":[{"applicability":"Kök yakınlığının yüzeyde dipten sık bir görünüm oluşturduğu betimleyici bağlamlarda kullanılabilir.","error_profile":{"adds":"Kök yakınlığı dışında genel bir örtü yoğunluğu izlenimi ekleyebilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Bitkilerin dip bölümündeki sık ve yakın düzeni korur."},"facet_ids":["F001"],"text":"dipten sık bitki örtüsü","usage_role":"contextual"}],"definition":"Kökleri birbirine yakın duran, dipten sık ve bitişik görünüm veren bitki ya da bitki topluluğudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ayırt edici özellik, bitki köklerinin birbirine yakın aralıklarla bulunmasıdır."}],"identity_rationale":"Kaynak sözü, bitkiyi köklerinin birbirine yakın olmasıyla tanımlar. Sağlanan çerçeve bu ölçütü doğru biçimde korur ve onu genel bitki sıklığı ya da dal dolaşıklığıyla karıştırmaz.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kökleri birbirine yakın bitki"}],"lexicalization_note":"Tanım yalnızca kökleri birbirine yakın bitkiyi adlandıran belirtilmiş sözcükle sınırlıdır ve genel bir kök anlamı sayılmaz.","neighbor_coverage_note":"Genel bitki yoğunluğu, dal dolaşıklığı ve üst üste dizilme en açıklayıcı karşıtlardır; belirli bitki türleri, kumda büyüme, diken filizi ve belirli ağaçlık alan adayları yalnızca bitki alanını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal miktar ve genel yoğunluğu öne çıkarır; bu dalda belirleyici olan bitki sayısı değil köklerin birbirine yakınlığıdır.","focus_only":"Sıklık özellikle köklerin birbirine yakın aralıklarla bulunmasına dayanır.","gloss":"yoğun bitki örtüsü","neighbor_only":"Bir yerde çok sayıda bitki ya da ağaç bulunmasına ve genel yoğun görünüme dayanır.","neighbor_ref":"root_000798/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da bitkilerin sık ve yoğun görünmesini anlatabilir."},{"boundary_match":"partial","distinction":"Bu dal köklerin yakınlığını ölçüt alır; komşu dal ise dalların çoğalması ve birbirine geçmesiyle oluşan üst bölüm yoğunluğunu anlatır.","focus_only":"Yakınlık bitkinin toprak altındaki ya da dipteki kök düzenindedir.","gloss":"dalları çok ve birbirine geçmiş ağaç","neighbor_only":"Yoğunluk dalların çokluğu ve birbirine dolanıp sıkı biçimde örtüşmesindedir.","neighbor_ref":"root_001025/B007","relation_type":"near_neighbor","shared_zone":"İki dal da bitkinin parçalarının birbirine yakın ve sık bir düzen oluşturmasını anlatır."},{"boundary_match":"partial","distinction":"Bu dal köklerin yan yana yakınlığıdır; komşu dalın belirleyici ilişkisi cisimlerin üst üste binmesi ve katmanlaşmasıdır.","focus_only":"Bitki kökleri aynı düzlemde birbirine yakın konumlanır.","gloss":"üst üste yığılma","neighbor_only":"Doğal cisimler, bulutlar ya da ürünler üst üste dizilip katman oluşturur.","neighbor_ref":"root_001515/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal doğal varlıkların aralarında az boşluk kalacak biçimde düzenlenmesini anlatabilir."}],"source_phrase_ar":"الوصيد النبت المتقارب الأصول (maqayis)؛ الوصيد النبات المتقارب الاصول (sihah)؛ الوصيد المتقارب الأصول (mufradat)","source_summary":"Kaynaklar bitkiyi ortak biçimde köklerinin birbirine yakın oluşuyla tanımlar; belirleyici ölçüt bitkinin türü, boyu ya da dal sayısı değil kökler arasındaki yakınlıktır.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه الوصيد بمعنى النبت أو النبات المتقارب الأصول.","what_is_not_ar":"لا يدخل فيه الفناء أو الباب أو الوصيدة الحجرية أو إطباق الباب إلا من جهة أصل التقارب والضم."},"support_links":["sup_5f7a4f8320a8a28a7f86","sup_60aeafa1f6b805240d9d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000047/B001","candidate_links":[{"candidate_id":"cand_59ae345bde11641a0f28","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_7a126688b12f4ab99914","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The divine referent fixes agency and ownership outside the occupants, reinforcing that neither ignition nor closure is under their control.","root":"ء ل ه","source_ref":"104:6","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000047","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a67359983706f42e9f71"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000259/B001","candidate_links":[{"candidate_id":"cand_7f972b2f4b2ec3934d08","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_9e7358a4190aea26e844","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Joining dispersed things into one aggregate supplies the assembly of separate elements into a continuous enclosing mesh.","root":"ج م ع","source_ref":"104:2","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000259","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_60aeafa1f6b805240d9d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000259/B005","candidate_links":[{"candidate_id":"cand_a476a0d17ba22279c9f8","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_02ef96e01e546a529c4e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The fist closing its fingers provides a concrete clasp for gathering and lets accumulation prefigure the later fastening.","root":"ج م ع","source_ref":"104:2","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000259","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_effc37c280bf1d1f85ae"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000318/B002","candidate_links":[{"candidate_id":"cand_f718b7c92959d2a7a4ff","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b0e539b21413d100ee2f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Supposition marks the wealth-to-permanence link as the offender's constructed causal model, available for reversal.","root":"ح س ب","source_ref":"104:3","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000318","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a1caae65b879709ccb2c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000337/B001","candidate_links":[{"candidate_id":"cand_265439d0dadc84eade74","lane":"macro"},{"candidate_id":"cand_110242bef49ccc802ec1","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_04f243a0b578667a701a","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Breaking a dry thing into fragments supplies the destructive internal operation whose products the enclosure prevents from dispersing.","root":"ح ط م","source_ref":"104:4","source_word_indices":["4"]},{"hft_ref":"hft_c10b7e9d4384b938d545","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Fragmentation supplies the concealed operation inside the boundary and keeps the epistemic model anchored to the named crusher.","root":"ح ط م","source_ref":"104:5","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000337","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_5d2776aaaf2cae3635f9","sup_d3a112cca9f1e8f2f49e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000429/B001","candidate_links":[{"candidate_id":"cand_f718b7c92959d2a7a4ff","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b0e539b21413d100ee2f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Stable continuance resistant to passing away supplies the desired duration that the seal recodes as confinement.","root":"خ ل د","source_ref":"104:3","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000429","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a1caae65b879709ccb2c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000429/B002","candidate_links":[{"candidate_id":"cand_f718b7c92959d2a7a4ff","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b0e539b21413d100ee2f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Clinging and remaining attached make the revised permanence spatial: the occupant is fixed to the enclosed state.","root":"خ ل د","source_ref":"104:3","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000429","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a1caae65b879709ccb2c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000469/B008","candidate_links":[{"candidate_id":"cand_110242bef49ccc802ec1","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_c10b7e9d4384b938d545","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The disturbed water-vortex supplies a form-distant image of an internally circulating process that cannot be read from a calm exterior.","root":"د ر ي","source_ref":"104:5","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000469","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_5d2776aaaf2cae3635f9"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000473/B001","candidate_links":[{"candidate_id":"cand_110242bef49ccc802ec1","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_c10b7e9d4384b938d545","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Knowledge and discernment make access to what the crusher is an explicit problem, allowing the seal to acquire an epistemic edge.","root":"د ر ي","source_ref":"104:5","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000473","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_5d2776aaaf2cae3635f9"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000945/B003","candidate_links":[{"candidate_id":"cand_f40721ca343636338e9c","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_53ffa3ebf7f5418d973c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Overlooking and uncovering an affair supply penetrating inspection, making the fire's reach revelatory as well as spatial.","root":"ط ل ع","source_ref":"104:7","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000945","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_4daa7b66b5ecfc645bc8"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000945/B006","candidate_links":[{"candidate_id":"cand_f40721ca343636338e9c","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_53ffa3ebf7f5418d973c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"An ascending access or approach supplies a route inward and upward that contrasts with the occupants' blocked route out.","root":"ط ل ع","source_ref":"104:7","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000945","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_4daa7b66b5ecfc645bc8"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000989/B005","candidate_links":[{"candidate_id":"cand_a476a0d17ba22279c9f8","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_02ef96e01e546a529c4e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Counting that returns with time contributes iterative rechecking, making the hoard a repeatedly secured total rather than a single acquisition.","root":"ع د د","source_ref":"104:2","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000989","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_effc37c280bf1d1f85ae"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001043/B002","candidate_links":[{"candidate_id":"cand_96152092b327e933d309","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_fb609188930aebcb0588","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Propping a thing with a support supplies the fastening action that makes the closure structurally maintained.","root":"ع م د","source_ref":"104:9","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001043","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_92c77e8ebb3c8ac9b9eb"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001043/B013","candidate_links":[{"candidate_id":"cand_96152092b327e933d309","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_fb609188930aebcb0588","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Damming a flow contributes active blockage, casting the columns as impediments to passage rather than neutral scenery.","root":"ع م د","source_ref":"104:9","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001043","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_92c77e8ebb3c8ac9b9eb"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001122/B002","candidate_links":[{"candidate_id":"cand_f40721ca343636338e9c","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_53ffa3ebf7f5418d973c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The heart viewed as inner ignition makes the reached interior both the target of inspection and a site continuous with the surrounding fire.","root":"ف ء د","source_ref":"104:7","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001122","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_4daa7b66b5ecfc645bc8"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001315/B005","candidate_links":[{"candidate_id":"cand_143e589d5321bb026b33","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_c092b10b841d4e5597b0","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The encircling crown contributes an all-around topology, turning totality into circumferential pressure around the agents.","root":"ك ل ل","source_ref":"104:1","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001315","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_165680375e97542f7f38"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001376/B002","candidate_links":[{"candidate_id":"cand_143e589d5321bb026b33","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_c092b10b841d4e5597b0","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Pushing supplies the outward displacement that is reversed when the plural objects are shut in rather than able to push others aside.","root":"ل م ز","source_ref":"104:1","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001376","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_165680375e97542f7f38"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001407/B001","candidate_links":[{"candidate_id":"cand_96152092b327e933d309","lane":"macro"},{"candidate_id":"cand_7f972b2f4b2ec3934d08","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_fb609188930aebcb0588","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Drawing something lengthwise until it connects supplies extended bars or supports spanning the closure.","root":"م د د","source_ref":"104:9","source_word_indices":["3"]},{"hft_ref":"hft_9e7358a4190aea26e844","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Lengthwise drawing until connection supplies the spanning links that turn close-packed elements into an extended barrier.","root":"م د د","source_ref":"104:9","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001407","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_60aeafa1f6b805240d9d","sup_92c77e8ebb3c8ac9b9eb"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001407/B004","candidate_links":[{"candidate_id":"cand_96152092b327e933d309","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_fb609188930aebcb0588","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A term or time made long adds temporal extension, so the fastening persists rather than merely snapping shut once.","root":"م د د","source_ref":"104:9","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001407","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_92c77e8ebb3c8ac9b9eb"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001457/B001","candidate_links":[{"candidate_id":"cand_a476a0d17ba22279c9f8","lane":"macro"},{"candidate_id":"cand_f718b7c92959d2a7a4ff","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_02ef96e01e546a529c4e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The taking and multiplying of wealth supplies the contents whose controlled abundance defines the collector's prior agency.","root":"م و ل","source_ref":"104:2","source_word_indices":["3"]},{"hft_ref":"hft_b0e539b21413d100ee2f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Abundant owned wealth supplies the imagined instrument by which the offender expects to secure duration.","root":"م و ل","source_ref":"104:3","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001457","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a1caae65b879709ccb2c","sup_effc37c280bf1d1f85ae"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001466/B001","candidate_links":[{"candidate_id":"cand_265439d0dadc84eade74","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_04f243a0b578667a701a","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Throwing and casting supply the inbound motion, making closure the endpoint of a directed transfer rather than an initially static room.","root":"ن ب ذ","source_ref":"104:4","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001466","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_d3a112cca9f1e8f2f49e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001466/B006","candidate_links":[{"candidate_id":"cand_a9e991d63f66fb4186cb","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_3b9f3f1a56b61b83a0c7","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Material cast into a vessel supplies the unusual processing analogy: thrown contents are enclosed so an internal change can proceed.","root":"ن ب ذ","source_ref":"104:4","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001466","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_dc0dac4740d7cd2ef07c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001564/B002","candidate_links":[{"candidate_id":"cand_59ae345bde11641a0f28","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_7a126688b12f4ab99914","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Blazing fire supplies the enclosing medium rather than merely an object located somewhere inside the enclosure.","root":"ن و ر","source_ref":"104:6","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001564","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a67359983706f42e9f71"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001600/B001","candidate_links":[{"candidate_id":"cand_143e589d5321bb026b33","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_c092b10b841d4e5597b0","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Hand-pressure and squeezing materialize the aggressor's social action as compression that the later seal can return upon him.","root":"ه م ز","source_ref":"104:1","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001600","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_165680375e97542f7f38"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001672/B001","candidate_links":[{"candidate_id":"cand_59ae345bde11641a0f28","lane":"macro"},{"candidate_id":"cand_a9e991d63f66fb4186cb","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_7a126688b12f4ab99914","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The act of kindling makes the enclosure dynamically burning rather than a cold, completed container.","root":"و ق د","source_ref":"104:6","source_word_indices":["3"]},{"hft_ref":"hft_3b9f3f1a56b61b83a0c7","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Active kindling replaces passive storage with a heated process occurring inside the sealed volume.","root":"و ق د","source_ref":"104:6","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001672","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a67359983706f42e9f71","sup_dc0dac4740d7cd2ef07c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001672/B003","candidate_links":[{"candidate_id":"cand_59ae345bde11641a0f28","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_7a126688b12f4ab99914","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The hearth or fire-site supplies the furnace architecture in which ignition and closure operate as one system.","root":"و ق د","source_ref":"104:6","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001672","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a67359983706f42e9f71"]}],"candidate_inventory":[{"anchor_refs":["104:8"],"branch_refs":["root_001653/B001","root_001653/B002"],"candidate_id":"cand_8ba5c25e88f9feecc3a3","commentary_obligation":"review","focus_branch_refs":["root_001653/B001","root_001653/B002"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":[],"root_ids":[],"scope":"pericope","source_local_id":"A:Sealed Doorway","source_type":"channel","support_ids":["sup_4f2ab0a9681fb98b573c","sup_50870d6fa2c37fd646fe","sup_55665a5337b68352eaf5","sup_a7d8e8226f01e27b3640","sup_d59157dcac91c1ce3dce"],"title":"Sealed Doorway","trust":"trusted","unresolved_branch_citations":[{"citation":"ء ص د/B001","reason":"no registered branch match"}],"unresolved_branch_refs":[]},{"anchor_refs":["104:8"],"branch_refs":["root_001653/B002","root_001653/B003"],"candidate_id":"cand_d436e7850e0fe0725385","commentary_obligation":"review","focus_branch_refs":["root_001653/B002","root_001653/B003"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":[],"root_ids":[],"scope":"pericope","source_local_id":"B:Courtyard, Stone Pen, and Mountain Recess","source_type":"channel","support_ids":["sup_1fbcde8a665debbef781","sup_4badb174a5098596deb7","sup_63a5ca04e84df1f65c54","sup_841384807a53aa4e0c3d","sup_8750817c453187919d69"],"title":"Courtyard, Stone Pen, and Mountain Recess","trust":"trusted","unresolved_branch_citations":[{"citation":"ء ص د/B002","reason":"no registered branch match"},{"citation":"ء ص د/B004","reason":"no registered branch match"},{"citation":"ء ص د/B005","reason":"no registered branch match"}],"unresolved_branch_refs":[]},{"anchor_refs":["104:2","104:6","104:7","104:8"],"branch_refs":["root_000259/B011","root_000945/B005","root_001564/B004","root_001653/B004"],"candidate_id":"cand_b2a1c4ffab694254b498","commentary_obligation":"review","focus_branch_refs":["root_001653/B004"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000259/B011","root_000945/B005","root_001564/B004"],"root_ids":[],"scope":"pericope","source_local_id":"B:Sprouting, Flowering, and Close-Rooted Growth","source_type":"channel","support_ids":["sup_26ee11e89ce063f1a310","sup_3d6e15c7ecffec5a9491","sup_5f7a4f8320a8a28a7f86","sup_a5c18d72be88982377ec","sup_d3438c2095bfd00355d0"],"title":"Sprouting, Flowering, and Close-Rooted Growth","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["104:1","104:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:8","branch_refs":["root_000036/B001","root_001315/B005","root_001376/B002","root_001600/B001"],"candidate_id":"cand_143e589d5321bb026b33","commentary_obligation":"review","hft_ref":"hft_c092b10b841d4e5597b0","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_pressure_reversal","source_type":"hft","support_ids":["sup_165680375e97542f7f38"],"title":"delta_pressure_reversal","trust":"legacy_unbound"},{"anchor_refs":["104:2","104:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:8","branch_refs":["root_000036/B002","root_000259/B005","root_000989/B005","root_001457/B001"],"candidate_id":"cand_a476a0d17ba22279c9f8","commentary_obligation":"review","hft_ref":"hft_02ef96e01e546a529c4e","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_hoard_becomes_clasp","source_type":"hft","support_ids":["sup_effc37c280bf1d1f85ae"],"title":"delta_hoard_becomes_clasp","trust":"legacy_unbound"},{"anchor_refs":["104:3","104:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:8","branch_refs":["root_000318/B002","root_000429/B001","root_000429/B002","root_001457/B001","root_001653/B001"],"candidate_id":"cand_f718b7c92959d2a7a4ff","commentary_obligation":"review","hft_ref":"hft_b0e539b21413d100ee2f","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_counterfeit_permanence","source_type":"hft","support_ids":["sup_a1caae65b879709ccb2c"],"title":"delta_counterfeit_permanence","trust":"legacy_unbound"},{"anchor_refs":["104:4","104:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:8","branch_refs":["root_000337/B001","root_001466/B001","root_001653/B003"],"candidate_id":"cand_265439d0dadc84eade74","commentary_obligation":"review","hft_ref":"hft_04f243a0b578667a701a","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_cast_crush_capture","source_type":"hft","support_ids":["sup_d3a112cca9f1e8f2f49e"],"title":"delta_cast_crush_capture","trust":"legacy_unbound"},{"anchor_refs":["104:5","104:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:8","branch_refs":["root_000036/B001","root_000337/B001","root_000469/B008","root_000473/B001"],"candidate_id":"cand_110242bef49ccc802ec1","commentary_obligation":"review","hft_ref":"hft_c10b7e9d4384b938d545","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_epistemic_seal","source_type":"hft","support_ids":["sup_5d2776aaaf2cae3635f9"],"title":"delta_epistemic_seal","trust":"legacy_unbound"},{"anchor_refs":["104:6","104:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:8","branch_refs":["root_000036/B001","root_000047/B001","root_001564/B002","root_001672/B001","root_001672/B003"],"candidate_id":"cand_59ae345bde11641a0f28","commentary_obligation":"review","hft_ref":"hft_7a126688b12f4ab99914","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_sealed_furnace","source_type":"hft","support_ids":["sup_a67359983706f42e9f71"],"title":"delta_sealed_furnace","trust":"legacy_unbound"},{"anchor_refs":["104:7","104:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:8","branch_refs":["root_000945/B003","root_000945/B006","root_001122/B002","root_001653/B001"],"candidate_id":"cand_f40721ca343636338e9c","commentary_obligation":"review","hft_ref":"hft_53ffa3ebf7f5418d973c","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_one_way_inward_boundary","source_type":"hft","support_ids":["sup_4daa7b66b5ecfc645bc8"],"title":"delta_one_way_inward_boundary","trust":"legacy_unbound"},{"anchor_refs":["104:8","104:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:8","branch_refs":["root_001043/B002","root_001043/B013","root_001407/B001","root_001407/B004","root_001653/B001"],"candidate_id":"cand_96152092b327e933d309","commentary_obligation":"review","hft_ref":"hft_fb609188930aebcb0588","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_braced_duration_lock","source_type":"hft","support_ids":["sup_92c77e8ebb3c8ac9b9eb"],"title":"delta_braced_duration_lock","trust":"legacy_unbound"},{"anchor_refs":["104:4","104:6","104:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:8","branch_refs":["root_000036/B002","root_001466/B006","root_001672/B001"],"candidate_id":"cand_a9e991d63f66fb4186cb","commentary_obligation":"review","hft_ref":"hft_3b9f3f1a56b61b83a0c7","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_sealed_processing_vessel","source_type":"hft","support_ids":["sup_dc0dac4740d7cd2ef07c"],"title":"outlier_sealed_processing_vessel","trust":"legacy_unbound"},{"anchor_refs":["104:2","104:8","104:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:8","branch_refs":["root_000259/B001","root_001407/B001","root_001653/B004"],"candidate_id":"cand_7f972b2f4b2ec3934d08","commentary_obligation":"review","hft_ref":"hft_9e7358a4190aea26e844","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_interlocked_mesh","source_type":"hft","support_ids":["sup_60aeafa1f6b805240d9d"],"title":"outlier_interlocked_mesh","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_c47f63b449477273dbfb","connection_ref":"conn_b4e4aacc9e6ea079ec99","note":"The immediate continuation adds extended columns, making closure sustained rather than momentary.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_f137b223ca3b5d5634b4","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"104:9","source_note":"Immediate predecessor: مُؤْصَدَة supplies the closure that the extended columns complete.","source_row_role":"ranked_review","source_target_component_ref":"104:8","source_target_components":["104:8"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"104:8"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"104:9","source_target_components":["104:9"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"104:9","target_evidence":{"arabic_uthmani":"فِى عَمَدٍۢ مُّمَدَّدَةٍۭ","ayah_ref":"104:9"},"target_ref":"104:9"},{"connection_evidence_ref":"conn_ev_adbe62e3455d956b067e","connection_ref":"conn_234780f35308827c091f","note":"The preceding relative clause fixes the enclosing referent within the surah's fire sequence.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_a51febc3186302cb9738","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"104:7","source_note":"The immediate closure explicitly completes the f03 no-exit sequence.","source_row_role":"ranked_review","source_target_component_ref":"104:8","source_target_components":["104:8"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"104:8"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"104:7","source_target_components":["104:7"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"104:7","target_evidence":{"arabic_uthmani":"ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ","ayah_ref":"104:7"},"target_ref":"104:7"},{"connection_evidence_ref":"conn_ev_a00589e5346d08808656","connection_ref":"conn_15e16dc22cdb92cd9ad1","note":"It identifies the immediate antecedent of the feminine pronoun as the kindled fire.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_a78b5a00462a1d173c86","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"104:6","source_note":"Direct sequel: the fire is shut over them.","source_row_role":"ranked_review","source_target_component_ref":"104:8","source_target_components":["104:8"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"104:8"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"104:6","source_target_components":["104:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"104:6","target_evidence":{"arabic_uthmani":"نَارُ ٱللَّهِ ٱلْمُوقَدَةُ","ayah_ref":"104:6"},"target_ref":"104:6"},{"connection_evidence_ref":"conn_ev_6e4cbf1e6cc2ff47f433","connection_ref":"conn_0b53e05b64233a7acf29","note":"The earlier wealth-accumulation motif supplies the context for the reversal-of-possession reading.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_922f0be046b8c95f30ee","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"104:2","source_note":"Shows the punishment as closed over them, completing the reversal of retained wealth.","source_row_role":"ranked_review","source_target_component_ref":"104:8","source_target_components":["104:8"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"104:8"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"104:2","source_target_components":["104:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"104:2","target_evidence":{"arabic_uthmani":"ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ","ayah_ref":"104:2"},"target_ref":"104:2"},{"connection_evidence_ref":"conn_ev_08b0073ce556c91d5c37","connection_ref":"conn_8ad79d65f977c76ba548","note":"The claimed permanence of accumulated wealth directly frames the focus's reversal-of-permanence reading.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"104:3","source_target_components":["104:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"104:3","target_evidence":{"arabic_uthmani":"يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ","ayah_ref":"104:3"},"target_ref":"104:3"},{"connection_evidence_ref":"conn_ev_35dd5294b58c632b2af4","connection_ref":"conn_2ee996f6d4c6c13312d3","note":"The immediate movement into ٱلْحُطَمَةِ supplies the transition into the enclosing fire.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":true,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_18967ad27181b74fa4cb","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"104:4","source_note":"Immediate continuation adds the closing enclosure around the destination.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"104:8","source_target_components":["104:8"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"104:8"}],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"104:4","source_target_components":["104:4"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"104:4","target_evidence":{"arabic_uthmani":"كَلَّا ۖ لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ","ayah_ref":"104:4"},"target_ref":"104:4"},{"connection_evidence_ref":"conn_ev_9c3d87c7f7a4c3edbc75","connection_ref":"conn_c759acac8ce3b3021b4b","note":"The naming question sustains the immediate fire sequence without adding closure mechanics.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":true,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_f29b4a898a3a44d308fa","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"104:5","source_note":"Immediate continuation: innaha alayhim musadah completes the enclosing answer begun at 104:6-7 and 104:9.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"104:8","source_target_components":["104:8"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"104:8"}],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"104:5","source_target_components":["104:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"104:5","target_evidence":{"arabic_uthmani":"وَمَآ أَدْرَىٰكَ مَا ٱلْحُطَمَةُ","ayah_ref":"104:5"},"target_ref":"104:5"}],"focus":{"arabic_uthmani":"إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ","qac_morphemes":[{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"104:8:1:1","qac_word_ref":"104:8:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"104:8:1:2","qac_word_ref":"104:8:1","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"عَلَىٰ","morph_features":"STEM|POS:P|LEM:EalaY`","morpheme_role":"STEM","pos":"P","qac_ref":"104:8:2:1","qac_word_ref":"104:8:2","root_ar":"","surface_ar":"عَلَيْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"104:8:2:2","qac_word_ref":"104:8:2","root_ar":"","surface_ar":"هِم"},{"lemma_ar":"مُّؤْصَدَة","morph_features":"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:8:3:1","qac_word_ref":"104:8:3","root_ar":"و ص د","surface_ar":"مُّؤْصَدَةٌ"}],"word_analysis_qac_refs":[["104:8:1:1","104:8:1:2"],["104:8:2:1","104:8:2:2"],["104:8:3:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["104:8:1","104:8:2","104:8:3"]},"focus_surface_evidence":{"arabic_uthmani":"إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ","qac_morphemes":[{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"104:8:1:1","qac_word_ref":"104:8:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"104:8:1:2","qac_word_ref":"104:8:1","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"عَلَىٰ","morph_features":"STEM|POS:P|LEM:EalaY`","morpheme_role":"STEM","pos":"P","qac_ref":"104:8:2:1","qac_word_ref":"104:8:2","root_ar":"","surface_ar":"عَلَيْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"104:8:2:2","qac_word_ref":"104:8:2","root_ar":"","surface_ar":"هِم"},{"lemma_ar":"مُّؤْصَدَة","morph_features":"STEM|POS:N|LEM:m~u&oSadap|ROOT:wSd|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:8:3:1","qac_word_ref":"104:8:3","root_ar":"و ص د","surface_ar":"مُّؤْصَدَةٌ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["104:8:1:1","104:8:1:2"],["104:8:2:1","104:8:2:2"],["104:8:3:1"]],"word_analysis_refs":["104:8:1","104:8:2","104:8:3"],"word_rows":[{"analysis_record_ref":"104:8:1","analytic_gloss_range_en":"emphatic clause opening with a bound feminine subject pronoun","analytic_root_gloss_range_en":null,"qac_refs":["104:8:1:1","104:8:1:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"إِنَّهَا","transliteration":"innahā"}},{"analysis_record_ref":"104:8:2","analytic_gloss_range_en":"fronted upon-them phrase binding the plural target to the sealed state","analytic_root_gloss_range_en":null,"qac_refs":["104:8:2:1","104:8:2:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"عَلَيْهِمْ","transliteration":"ʿalayhim"}},{"analysis_record_ref":"104:8:3","analytic_gloss_range_en":"sealed, shut, or bolted as a completed passive state in this clause","analytic_root_gloss_range_en":"closure and door-fastening pressure is locally selected; supplied fire-kindling associations can remain undertone only, not the governing sense","qac_refs":["104:8:3:1"],"root":{"arabic":"أ ص د","transliteration":"ʾ-ṣ-d"},"surface":{"arabic":"مُّؤْصَدَةٌ","transliteration":"muʾṣadatun"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":9,"missing_anchor_refs":[],"supplied_unique_anchor_count":9},"assigned_record_count":10,"assigned_records":[{"anchor_refs":["104:1","104:8"],"branch_refs":["root_000036/B001","root_001315/B005","root_001376/B002","root_001600/B001"],"candidate_id":"cand_143e589d5321bb026b33","evidence_scope":"declared_pericope","hft_ref":"hft_c092b10b841d4e5597b0","item_id":"delta_pressure_reversal","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_pressure_reversal","support_id":"sup_165680375e97542f7f38"},{"anchor_refs":["104:2","104:8"],"branch_refs":["root_000036/B002","root_000259/B005","root_000989/B005","root_001457/B001"],"candidate_id":"cand_a476a0d17ba22279c9f8","evidence_scope":"declared_pericope","hft_ref":"hft_02ef96e01e546a529c4e","item_id":"delta_hoard_becomes_clasp","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_hoard_becomes_clasp","support_id":"sup_effc37c280bf1d1f85ae"},{"anchor_refs":["104:3","104:8"],"branch_refs":["root_000318/B002","root_000429/B001","root_000429/B002","root_001457/B001","root_001653/B001"],"candidate_id":"cand_f718b7c92959d2a7a4ff","evidence_scope":"declared_pericope","hft_ref":"hft_b0e539b21413d100ee2f","item_id":"delta_counterfeit_permanence","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_counterfeit_permanence","support_id":"sup_a1caae65b879709ccb2c"},{"anchor_refs":["104:4","104:8"],"branch_refs":["root_000337/B001","root_001466/B001","root_001653/B003"],"candidate_id":"cand_265439d0dadc84eade74","evidence_scope":"declared_pericope","hft_ref":"hft_04f243a0b578667a701a","item_id":"delta_cast_crush_capture","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_cast_crush_capture","support_id":"sup_d3a112cca9f1e8f2f49e"},{"anchor_refs":["104:5","104:8"],"branch_refs":["root_000036/B001","root_000337/B001","root_000469/B008","root_000473/B001"],"candidate_id":"cand_110242bef49ccc802ec1","evidence_scope":"declared_pericope","hft_ref":"hft_c10b7e9d4384b938d545","item_id":"delta_epistemic_seal","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_epistemic_seal","support_id":"sup_5d2776aaaf2cae3635f9"},{"anchor_refs":["104:6","104:8"],"branch_refs":["root_000036/B001","root_000047/B001","root_001564/B002","root_001672/B001","root_001672/B003"],"candidate_id":"cand_59ae345bde11641a0f28","evidence_scope":"declared_pericope","hft_ref":"hft_7a126688b12f4ab99914","item_id":"delta_sealed_furnace","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_sealed_furnace","support_id":"sup_a67359983706f42e9f71"},{"anchor_refs":["104:7","104:8"],"branch_refs":["root_000945/B003","root_000945/B006","root_001122/B002","root_001653/B001"],"candidate_id":"cand_f40721ca343636338e9c","evidence_scope":"declared_pericope","hft_ref":"hft_53ffa3ebf7f5418d973c","item_id":"delta_one_way_inward_boundary","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_one_way_inward_boundary","support_id":"sup_4daa7b66b5ecfc645bc8"},{"anchor_refs":["104:8","104:9"],"branch_refs":["root_001043/B002","root_001043/B013","root_001407/B001","root_001407/B004","root_001653/B001"],"candidate_id":"cand_96152092b327e933d309","evidence_scope":"declared_pericope","hft_ref":"hft_fb609188930aebcb0588","item_id":"delta_braced_duration_lock","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_braced_duration_lock","support_id":"sup_92c77e8ebb3c8ac9b9eb"},{"anchor_refs":["104:4","104:6","104:8"],"branch_refs":["root_000036/B002","root_001466/B006","root_001672/B001"],"candidate_id":"cand_a9e991d63f66fb4186cb","evidence_scope":"declared_pericope","hft_ref":"hft_3b9f3f1a56b61b83a0c7","item_id":"outlier_sealed_processing_vessel","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_sealed_processing_vessel","support_id":"sup_dc0dac4740d7cd2ef07c"},{"anchor_refs":["104:2","104:8","104:9"],"branch_refs":["root_000259/B001","root_001407/B001","root_001653/B004"],"candidate_id":"cand_7f972b2f4b2ec3934d08","evidence_scope":"declared_pericope","hft_ref":"hft_9e7358a4190aea26e844","item_id":"outlier_interlocked_mesh","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_interlocked_mesh","support_id":"sup_60aeafa1f6b805240d9d"}],"diagnostics":[],"lane_counts":{"global":9,"macro":10,"micro":4},"packet_summary":{"ayah_count":9,"focus_ref":"104:8","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"و ص د","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000036","furuq_root_norm":"ء ص د","furuq_source_root_norm":"أ ص د","is_dominant":true,"target_occurrences":2,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001653","furuq_root_norm":"و ص د","furuq_source_root_norm":"و ص د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]}],"window":["104:1","104:2","104:3","104:4","104:5","104:6","104:7","104:8","104:9"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"104:8","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":14,"unstructured_record_count":0},"identity":{"ayah_ref":"104:8","lane":"macro","linguistic_source_ref":"104:8","surface_ref":"104:8","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"104:8","target_tokens":[["Gerçekten",["104:8:1"]],["o",["104:8:1"]],["üzerlerine",["104:8:2"]],["kapatılmıştır",["104:8:3"]]],"text":"Gerçekten o, üzerlerine kapatılmıştır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":10,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":1,"ayah_to":9,"id":"s104-p01-001-009","label":"Whole surah","number":1,"refs":["104:1","104:2","104:3","104:4","104:5","104:6","104:7","104:8","104:9"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"104:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"104:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["104:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"104:0"},{"ayah_ref":"104:1","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"104:1","root_occurrences":[{"lemmas_ar":["كُلّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ك ل ل","surfaces_ar":["كُلِّ"],"word_indices":["2"]},{"lemmas_ar":["هُمَزَة"],"occurrence_count":1,"pos_tags":["N"],"root":"ه م ز","surfaces_ar":["هُمَزَةٍ"],"word_indices":["3"]},{"lemmas_ar":["لُّمَزَة"],"occurrence_count":1,"pos_tags":["N"],"root":"ل م ز","surfaces_ar":["لُّمَزَةٍ"],"word_indices":["4"]}],"root_sequence":["ك ل ل","ه م ز","ل م ز"],"text_ar":"وَيْلٌۭ لِّكُلِّ هُمَزَةٍۢ لُّمَزَةٍ"}],"context_order":["104:1"],"context_root_cues":[{"root":"ك ل ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الكَلال وخلاف الحدة"},{"branch_id":"B002","branch_image_ar":"الكُلّ عيالا وثقلا"},{"branch_id":"B003","branch_image_ar":"الكُلّ إحاطة وتماما"},{"branch_id":"B004","branch_image_ar":"الكَلالة قرابة عارضة"},{"branch_id":"B005","branch_image_ar":"الإكليل وما يحيط"},{"branch_id":"B006","branch_image_ar":"الكِلّة سترا وبيتا"},{"branch_id":"B007","branch_image_ar":"الكُلْكُل صدرا"},{"branch_id":"B008","branch_image_ar":"الكُلْكُل قصر وغلظ"},{"branch_id":"B009","branch_image_ar":"الكلاكل جماعات"},{"branch_id":"B011","branch_image_ar":"الانكلال تبسما ولمعا"}],"mapped_root_id":"root_001315","mapped_root_norm":"ك ل ل"}]},{"root":"ه م ز","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ضغط الشيء وعصره باليد"},{"branch_id":"B002","branch_image_ar":"ضغط الحرف في الكلام"},{"branch_id":"B003","branch_image_ar":"دفع ونخس يحرّك الشيء"},{"branch_id":"B004","branch_image_ar":"عيب الناس والوقيعة فيهم"}],"mapped_root_id":"root_001600","mapped_root_norm":"ه م ز"}]},{"root":"ل م ز","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العيب باللمز"},{"branch_id":"B002","branch_image_ar":"الدفع باللمز"}],"mapped_root_id":"root_001376","mapped_root_norm":"ل م ز"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"104:1","surface_ref":"104:1"},{"ayah_ref":"104:2","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"104:2","root_occurrences":[{"lemmas_ar":["جَمَعَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ج م ع","surfaces_ar":["جَمَعَ"],"word_indices":["2"]},{"lemmas_ar":["مَال"],"occurrence_count":1,"pos_tags":["N"],"root":"م و ل","surfaces_ar":["مَالًا"],"word_indices":["3"]},{"lemmas_ar":["عَدَّدَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ع د د","surfaces_ar":["عَدَّدَ"],"word_indices":["4"]}],"root_sequence":["ج م ع","م و ل","ع د د"],"text_ar":"ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ"}],"context_order":["104:2"],"context_root_cues":[{"root":"ج م ع","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ضم المتفرق حتى يصير شيئا مجموعا"},{"branch_id":"B002","branch_image_ar":"جماعة اجتمعت أو أخلاط ضمتها الجهة"},{"branch_id":"B003","branch_image_ar":"عزم محكم جمع الرأي بعد تفرقه"},{"branch_id":"B004","branch_image_ar":"موضع أو يوم أو نداء يجمع الناس"},{"branch_id":"B005","branch_image_ar":"قبضة الكف إذا ضمت الأصابع"},{"branch_id":"B006","branch_image_ar":"اتصال الجماع والمجامعة"},{"branch_id":"B007","branch_image_ar":"حال المرأة أو الأنثى التي بقي حملها أو عذرها معها"},{"branch_id":"B008","branch_image_ar":"القيد الذي يجمع اليدين إلى العنق"},{"branch_id":"B009","branch_image_ar":"اكتمال الشيء كله بلا تفرق أو نقص"},{"branch_id":"B010","branch_image_ar":"استجماع القوة أو السير حتى تتلاحق أجزاؤه"},{"branch_id":"B011","branch_image_ar":"نخل دقل اجتمع من النوى لا يعرف اسمه"},{"branch_id":"B012","branch_image_ar":"عظم الشيء كأنه جامع ممتلئ"},{"branch_id":"B013","branch_image_ar":"ممالأة واجتماع مع غيرك على أمر"}],"mapped_root_id":"root_000259","mapped_root_norm":"ج م ع"}]},{"root":"م و ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"اتخاذ المال وكثرته"}],"mapped_root_id":"root_001457","mapped_root_norm":"م و ل"}]},{"root":"ع د د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"إحصاء المعدود"},{"branch_id":"B002","branch_image_ar":"تهيئة العدة"},{"branch_id":"B003","branch_image_ar":"مدة العدة المعدودة"},{"branch_id":"B004","branch_image_ar":"الماء العد"},{"branch_id":"B005","branch_image_ar":"عداد الوقت ومعاودته"},{"branch_id":"B006","branch_image_ar":"نظير يعد مع غيره"}],"mapped_root_id":"root_000989","mapped_root_norm":"ع د د"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"104:2","surface_ref":"104:2"},{"ayah_ref":"104:3","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"104:3","root_occurrences":[{"lemmas_ar":["حَسِبَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ح س ب","surfaces_ar":["يَحْسَبُ"],"word_indices":["1"]},{"lemmas_ar":["مَال"],"occurrence_count":1,"pos_tags":["N"],"root":"م و ل","surfaces_ar":["مَالَ"],"word_indices":["3"]},{"lemmas_ar":["أَخْلَدَ"],"occurrence_count":1,"pos_tags":["V"],"root":"خ ل د","surfaces_ar":["أَخْلَدَ"],"word_indices":["4"]}],"root_sequence":["ح س ب","م و ل","خ ل د"],"text_ar":"يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ"}],"context_order":["104:3"],"context_root_cues":[{"root":"ح س ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العد والحساب"},{"branch_id":"B002","branch_image_ar":"الحسبان والظن"},{"branch_id":"B003","branch_image_ar":"الكفاية والإغناء"},{"branch_id":"B004","branch_image_ar":"الحسب والمآثر"},{"branch_id":"B006","branch_image_ar":"الحسبة والنظر في الأمر"},{"branch_id":"B008","branch_image_ar":"المحسبة والوسادة"},{"branch_id":"B009","branch_image_ar":"لون الأحسب والأحسبية"},{"branch_id":"B010","branch_image_ar":"التحسب والاستخبار"}],"mapped_root_id":"root_000318","mapped_root_norm":"ح س ب"}]},{"root":"م و ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"اتخاذ المال وكثرته"}],"mapped_root_id":"root_001457","mapped_root_norm":"م و ل"}]},{"root":"خ ل د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ثبات وبقاء لا يسرع إليه الفناء"},{"branch_id":"B002","branch_image_ar":"ركون ولصوق وملازمة"},{"branch_id":"B003","branch_image_ar":"زينة ملازمة للأذن أو اليد"},{"branch_id":"B004","branch_image_ar":"بال مستقر في القلب"},{"branch_id":"B005","branch_image_ar":"دويبة عمياء تشبه الجرذ"}],"mapped_root_id":"root_000429","mapped_root_norm":"خ ل د"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"104:3","surface_ref":"104:3"},{"ayah_ref":"104:4","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"104:4","root_occurrences":[{"lemmas_ar":["نَبَذَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ن ب ذ","surfaces_ar":["يُنۢبَذَ"],"word_indices":["2"]},{"lemmas_ar":["حُطَمَة"],"occurrence_count":1,"pos_tags":["N"],"root":"ح ط م","surfaces_ar":["حُطَمَةِ"],"word_indices":["4"]}],"root_sequence":["ن ب ذ","ح ط م"],"text_ar":"كَلَّا ۖ لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ"}],"context_order":["104:4"],"context_root_cues":[{"root":"ن ب ذ","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الطرح والإلقاء"},{"branch_id":"B002","branch_image_ar":"مناجزة الخصم بالنبذ"},{"branch_id":"B003","branch_image_ar":"إيجاب البيع بالنبذ"},{"branch_id":"B004","branch_image_ar":"الانتحاء إلى ناحية"},{"branch_id":"B005","branch_image_ar":"النَّبْذ اليسير"},{"branch_id":"B006","branch_image_ar":"النبيذ المطروح في الوعاء"},{"branch_id":"B007","branch_image_ar":"الولد المنبوذ"},{"branch_id":"B008","branch_image_ar":"الوسادة المنبوذة"},{"branch_id":"B009","branch_image_ar":"النبيذة المهملة أو المنبثة"}],"mapped_root_id":"root_001466","mapped_root_norm":"ن ب ذ"}]},{"root":"ح ط م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"كسر الشيء اليابس حتى يتفتت"},{"branch_id":"B003","branch_image_ar":"سنة شديدة تكسر الناس والمال"},{"branch_id":"B004","branch_image_ar":"سائق أو راع يعنف بالماشية"},{"branch_id":"B005","branch_image_ar":"سن أو طول صحبة يحطم البدن"},{"branch_id":"B006","branch_image_ar":"جماعة أو عيث يحطم ما يلقى"},{"branch_id":"B007","branch_image_ar":"موضع مكسور أو مزحوم عند الكعبة"},{"branch_id":"B008","branch_image_ar":"أكول يهضم كأنه نار أو جارسة"},{"branch_id":"B009","branch_image_ar":"حطام الدنيا الزائل"}],"mapped_root_id":"root_000337","mapped_root_norm":"ح ط م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"104:4","surface_ref":"104:4"},{"ayah_ref":"104:5","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"104:5","root_occurrences":[{"lemmas_ar":["أَدْرَىٰ"],"occurrence_count":1,"pos_tags":["V"],"root":"د ر ي","surfaces_ar":["أَدْرَىٰ"],"word_indices":["2"]},{"lemmas_ar":["حُطَمَة"],"occurrence_count":1,"pos_tags":["N"],"root":"ح ط م","surfaces_ar":["حُطَمَةُ"],"word_indices":["4"]}],"root_sequence":["د ر ي","ح ط م"],"text_ar":"وَمَآ أَدْرَىٰكَ مَا ٱلْحُطَمَةُ"}],"context_order":["104:5"],"context_root_cues":[{"root":"د ر ي","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"درور الشيء وخروجه غزيرا من مصدره"},{"branch_id":"B002","branch_image_ar":"عدو سريع متتابع"},{"branch_id":"B003","branch_image_ar":"تدردر واضطراب في اللحم والفم"},{"branch_id":"B004","branch_image_ar":"سمت الطريق ومهب الريح والمحاذاة"},{"branch_id":"B005","branch_image_ar":"بياض الدر وصفاؤه ولمعانه"},{"branch_id":"B006","branch_image_ar":"درة الضرب والسلطان"},{"branch_id":"B007","branch_image_ar":"إدارة المغزل واستحكام دورانه"},{"branch_id":"B008","branch_image_ar":"دردور الماء واضطراب الدوامة"}],"mapped_root_id":"root_000469","mapped_root_norm":"د ر ر"},{"branches":[{"branch_id":"B001","branch_image_ar":"الدراية والعلم"},{"branch_id":"B002","branch_image_ar":"قصد الشيء واعتماده"},{"branch_id":"B003","branch_image_ar":"الختل والاستتار للصيد"},{"branch_id":"B004","branch_image_ar":"المدرى والحد المحدد"}],"mapped_root_id":"root_000473","mapped_root_norm":"د ر ي"}]},{"root":"ح ط م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"كسر الشيء اليابس حتى يتفتت"},{"branch_id":"B003","branch_image_ar":"سنة شديدة تكسر الناس والمال"},{"branch_id":"B004","branch_image_ar":"سائق أو راع يعنف بالماشية"},{"branch_id":"B005","branch_image_ar":"سن أو طول صحبة يحطم البدن"},{"branch_id":"B006","branch_image_ar":"جماعة أو عيث يحطم ما يلقى"},{"branch_id":"B007","branch_image_ar":"موضع مكسور أو مزحوم عند الكعبة"},{"branch_id":"B008","branch_image_ar":"أكول يهضم كأنه نار أو جارسة"},{"branch_id":"B009","branch_image_ar":"حطام الدنيا الزائل"}],"mapped_root_id":"root_000337","mapped_root_norm":"ح ط م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"104:5","surface_ref":"104:5"},{"ayah_ref":"104:6","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"104:6","root_occurrences":[{"lemmas_ar":["نَار"],"occurrence_count":1,"pos_tags":["N"],"root":"ن و ر","surfaces_ar":["نَارُ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["مُوقَدَة"],"occurrence_count":1,"pos_tags":["ADJ"],"root":"و ق د","surfaces_ar":["مُوقَدَةُ"],"word_indices":["3"]}],"root_sequence":["ن و ر","ء ل ه","و ق د"],"text_ar":"نَارُ ٱللَّهِ ٱلْمُوقَدَةُ"}],"context_order":["104:6"],"context_root_cues":[{"root":"ن و ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الضياء والإضاءة"},{"branch_id":"B002","branch_image_ar":"النار المتقدة والسمة بها"},{"branch_id":"B004","branch_image_ar":"نور الشجر وزهره"},{"branch_id":"B005","branch_image_ar":"المنار والمنارة الظاهرة"},{"branch_id":"B006","branch_image_ar":"النِّفار وقلة الثبات"},{"branch_id":"B007","branch_image_ar":"النائرة بين القوم"},{"branch_id":"B008","branch_image_ar":"دخان الوشم والكحل"},{"branch_id":"B009","branch_image_ar":"النُّورَة المطلية"}],"mapped_root_id":"root_001564","mapped_root_norm":"ن و ر"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"و ق د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"اشتعال النار وإيقادها"},{"branch_id":"B002","branch_image_ar":"الحطب ومادة الوقود"},{"branch_id":"B003","branch_image_ar":"موضع النار والموقد"},{"branch_id":"B004","branch_image_ar":"وقدة الصيف وشدة الحر"},{"branch_id":"B005","branch_image_ar":"سرعة الاتقاد وفوران الشدة"},{"branch_id":"B006","branch_image_ar":"تلألؤ كاتقاد النار"}],"mapped_root_id":"root_001672","mapped_root_norm":"و ق د"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"104:6","surface_ref":"104:6"},{"ayah_ref":"104:7","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"104:7","root_occurrences":[{"lemmas_ar":["طَّلَعَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ط ل ع","surfaces_ar":["تَطَّلِعُ"],"word_indices":["2"]},{"lemmas_ar":["فُؤَاد"],"occurrence_count":1,"pos_tags":["N"],"root":"ف ء د","surfaces_ar":["أَفْـِٔدَةِ"],"word_indices":["4"]}],"root_sequence":["ط ل ع","ف ء د"],"text_ar":"ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ"}],"context_order":["104:7"],"context_root_cues":[{"root":"ط ل ع","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"طلوع النير وموضعه"},{"branch_id":"B002","branch_image_ar":"ظهور المقبل على القوم"},{"branch_id":"B003","branch_image_ar":"الإشراف والكشف على الأمر"},{"branch_id":"B004","branch_image_ar":"طليعة تستكشف العدو"},{"branch_id":"B005","branch_image_ar":"خروج الطلع والنبات"},{"branch_id":"B006","branch_image_ar":"مصعد ومأتى مشرف"},{"branch_id":"B007","branch_image_ar":"امتلاء مستوعب"},{"branch_id":"B008","branch_image_ar":"تطلع النفس وكثرة النظر"},{"branch_id":"B009","branch_image_ar":"طلعة مرئية"},{"branch_id":"B010","branch_image_ar":"سهم يطلع فوق الغرض"},{"branch_id":"B011","branch_image_ar":"قيء يطلع"},{"branch_id":"B012","branch_image_ar":"طول بارز"}],"mapped_root_id":"root_000945","mapped_root_norm":"ط ل ع"}]},{"root":"ف ء د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"حمى النار التي تشوي وتخبز وتوقد"},{"branch_id":"B002","branch_image_ar":"الفؤاد قلب منظور إليه كتوقد داخلي"},{"branch_id":"B003","branch_image_ar":"إصابة الفؤاد أو حلول دائه"},{"branch_id":"B004","branch_image_ar":"ضعف الفؤاد حتى كأنه لا فؤاد له"}],"mapped_root_id":"root_001122","mapped_root_norm":"ف ء د"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"104:7","surface_ref":"104:7"},{"ayah_ref":"104:9","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"104:9","root_occurrences":[{"lemmas_ar":["عَمَد"],"occurrence_count":1,"pos_tags":["N"],"root":"ع م د","surfaces_ar":["عَمَدٍ"],"word_indices":["2"]},{"lemmas_ar":["مُّمَدَّدَة"],"occurrence_count":1,"pos_tags":["ADJ"],"root":"م د د","surfaces_ar":["مُّمَدَّدَةٍۭ"],"word_indices":["3"]}],"root_sequence":["ع م د","م د د"],"text_ar":"فِى عَمَدٍۢ مُّمَدَّدَةٍۭ"}],"context_order":["104:9"],"context_root_cues":[{"root":"ع م د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"القصد المتعمد"},{"branch_id":"B002","branch_image_ar":"إسناد الشيء بعماد"},{"branch_id":"B003","branch_image_ar":"العمود والعماد"},{"branch_id":"B004","branch_image_ar":"أهل العمود والعماد"},{"branch_id":"B005","branch_image_ar":"الطول والرفعة في العماد"},{"branch_id":"B006","branch_image_ar":"المعتمد عليه في القوم"},{"branch_id":"B007","branch_image_ar":"قوام الشيء ووسطه"},{"branch_id":"B008","branch_image_ar":"وجع يهد ويفدح"},{"branch_id":"B009","branch_image_ar":"انشداح السنام والجرح"},{"branch_id":"B010","branch_image_ar":"ثرى عمد"},{"branch_id":"B011","branch_image_ar":"الشاب العمداني"},{"branch_id":"B013","branch_image_ar":"سد مجرى السيل"},{"branch_id":"B014","branch_image_ar":"لزوم الشيء"},{"branch_id":"B015","branch_image_ar":"الغضب والغلبة بالغضب"}],"mapped_root_id":"root_001043","mapped_root_norm":"ع م د"}]},{"root":"م د د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"جر الشيء في طول حتى يتصل ويمتد"},{"branch_id":"B002","branch_image_ar":"زيادة موصولة تمد غيرها بعون أو مادة"},{"branch_id":"B003","branch_image_ar":"ماء يجري ويمتلئ ويمده ماء آخر"},{"branch_id":"B004","branch_image_ar":"أجل أو زمن يطال ويمتد"},{"branch_id":"B005","branch_image_ar":"دواة تمد القلم بمداد"},{"branch_id":"B006","branch_image_ar":"مد يقدر به الكيل"},{"branch_id":"B007","branch_image_ar":"جرح تمتد فيه مدة من قيح"},{"branch_id":"B008","branch_image_ar":"ماء الإبل يمد بدقيق ونحوه"}],"mapped_root_id":"root_001407","mapped_root_norm":"م د د"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"104:9","surface_ref":"104:9"},{"ayah_ref":"1:2","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:2","root_occurrences":[{"lemmas_ar":["حَمْد"],"occurrence_count":1,"pos_tags":["N"],"root":"ح م د","surfaces_ar":["حَمْدُ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["لَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَبّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ر ب ب","surfaces_ar":["رَبِّ"],"word_indices":["3"]},{"lemmas_ar":["عَٰلَمِين"],"occurrence_count":1,"pos_tags":["N"],"root":"ع ل م","surfaces_ar":["عَٰلَمِينَ"],"word_indices":["4"]}],"root_sequence":["ح م د","ء ل ه","ر ب ب","ع ل م"],"text_ar":"ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ"}],"context_order":["1:2"],"context_root_cues":[{"root":"ح م د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الحمد خلاف الذم"},{"branch_id":"B002","branch_image_ar":"وجود الشيء محمودا"},{"branch_id":"B003","branch_image_ar":"المحمود كثير الخصال"},{"branch_id":"B004","branch_image_ar":"حماداك الغاية المحمودة"},{"branch_id":"B005","branch_image_ar":"يتحمد بالمنة"}],"mapped_root_id":"root_000355","mapped_root_norm":"ح م د"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ب ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ربوبية وملك وسيادة"},{"branch_id":"B002","branch_image_ar":"إصلاح وتربية وإتمام"},{"branch_id":"B003","branch_image_ar":"علم رباني"},{"branch_id":"B004","branch_image_ar":"ربة وجماعات كثيرة"},{"branch_id":"B005","branch_image_ar":"ربيب وربيبة ورابة"},{"branch_id":"B006","branch_image_ar":"رُبّ خاثر وإصلاح به"},{"branch_id":"B007","branch_image_ar":"لزوم وإقامة ودوام"},{"branch_id":"B008","branch_image_ar":"رباب السحاب"},{"branch_id":"B009","branch_image_ar":"شاة رُبّى وحداثة"},{"branch_id":"B010","branch_image_ar":"ربابة تجمع القداح"},{"branch_id":"B011","branch_image_ar":"ربابة عهد وميثاق"},{"branch_id":"B012","branch_image_ar":"ربة نبات"},{"branch_id":"B013","branch_image_ar":"ماء رَبَب كثير"},{"branch_id":"B014","branch_image_ar":"رَبْرَب قطيع"},{"branch_id":"B015","branch_image_ar":"حرف رب وربما"},{"branch_id":"B016","branch_image_ar":"رُبَى حاجة وعقدة ونعمة"},{"branch_id":"B017","branch_image_ar":"رباني الملاحين"}],"mapped_root_id":"root_000532","mapped_root_norm":"ر ب ب"},{"branches":[{"branch_id":"B001","branch_image_ar":"زيادة وعلو"},{"branch_id":"B002","branch_image_ar":"أرض مرتفعة"},{"branch_id":"B003","branch_image_ar":"زيادة الربا في المعاملة"},{"branch_id":"B004","branch_image_ar":"تصعد النفس وانتفاخه"},{"branch_id":"B005","branch_image_ar":"تغذية ونشوء"},{"branch_id":"B006","branch_image_ar":"نتوء أصل الفخذ"},{"branch_id":"B007","branch_image_ar":"أهل البيت من بني الأعمام"}],"mapped_root_id":"root_000537","mapped_root_norm":"ر ب و"}]},{"root":"ع ل م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"انكشاف الشيء للعارف"},{"branch_id":"B002","branch_image_ar":"أثر يميز الشيء ويهدي إليه"},{"branch_id":"B004","branch_image_ar":"شق ظاهر في الشفة العليا"},{"branch_id":"B005","branch_image_ar":"ماء كثير مجتمع في عيلم"},{"branch_id":"B006","branch_image_ar":"طائر جارح يسمى العلام"},{"branch_id":"B007","branch_image_ar":"ذكر الضباع يسمى العيلام"}],"mapped_root_id":"root_001040","mapped_root_norm":"ع ل م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:2","membership_added_ayah":true,"membership_target_surah":104,"surface_ref":"1:2"},{"ayah_ref":"1:3","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:3","root_occurrences":[{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["1","2"]}],"root_sequence":["ر ح م","ر ح م"],"text_ar":"ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"}],"context_order":["1:3"],"context_root_cues":[{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:3","membership_added_ayah":true,"membership_target_surah":104,"surface_ref":"1:3"},{"ayah_ref":"1:4","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:4","root_occurrences":[{"lemmas_ar":["مَٰلِك"],"occurrence_count":1,"pos_tags":["N"],"root":"م ل ك","surfaces_ar":["مَٰلِكِ"],"word_indices":["1"]},{"lemmas_ar":["يَوْم"],"occurrence_count":1,"pos_tags":["N"],"root":"ي و م","surfaces_ar":["يَوْمِ"],"word_indices":["2"]},{"lemmas_ar":["دِين"],"occurrence_count":1,"pos_tags":["N"],"root":"د ي ن","surfaces_ar":["دِّينِ"],"word_indices":["3"]}],"root_sequence":["م ل ك","ي و م","د ي ن"],"text_ar":"مَٰلِكِ يَوْمِ ٱلدِّينِ"}],"context_order":["1:4"],"context_root_cues":[{"root":"م ل ك","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"قوة الشيء وتماسكه"},{"branch_id":"B002","branch_image_ar":"المِلْك والتصرف"},{"branch_id":"B003","branch_image_ar":"المُلك والسلطان"},{"branch_id":"B004","branch_image_ar":"الإملاك والتزويج"},{"branch_id":"B005","branch_image_ar":"مِلاك الأمر وعِماده"},{"branch_id":"B006","branch_image_ar":"مَلَك الطريق والوادي"},{"branch_id":"B007","branch_image_ar":"الماء مَلَك الأمر"},{"branch_id":"B008","branch_image_ar":"المتقدم القائد في الحيوان"}],"mapped_root_id":"root_001444","mapped_root_norm":"م ل ك"}]},{"root":"ي و م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"وقت النهار المحدود"},{"branch_id":"B002","branch_image_ar":"مدة من الزمان"},{"branch_id":"B003","branch_image_ar":"كائنة اليوم وشدته"}],"mapped_root_id":"root_001700","mapped_root_norm":"ي و م"}]},{"root":"د ي ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الطاعة والانقياد"},{"branch_id":"B002","branch_image_ar":"الحساب والجزاء"},{"branch_id":"B003","branch_image_ar":"الدين المالي"},{"branch_id":"B004","branch_image_ar":"الإذلال والملك"},{"branch_id":"B005","branch_image_ar":"العادة والشأن"},{"branch_id":"B006","branch_image_ar":"مدينة الطاعة"},{"branch_id":"B007","branch_image_ar":"التصديق والتفويض"}],"mapped_root_id":"root_000504","mapped_root_norm":"د ي ن"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:4","membership_added_ayah":true,"membership_target_surah":104,"surface_ref":"1:4"},{"ayah_ref":"1:5","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:5","root_occurrences":[{"lemmas_ar":["عَبَدَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ع ب د","surfaces_ar":["نَعْبُدُ"],"word_indices":["2"]},{"lemmas_ar":["ٱسْتَعِينُ"],"occurrence_count":1,"pos_tags":["V"],"root":"ع و ن","surfaces_ar":["نَسْتَعِينُ"],"word_indices":["4"]}],"root_sequence":["ع ب د","ع و ن"],"text_ar":"إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ"}],"context_order":["1:5"],"context_root_cues":[{"root":"ع ب د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرق والملك"},{"branch_id":"B003","branch_image_ar":"العبادة والطاعة الخاضعة"},{"branch_id":"B004","branch_image_ar":"التعبيد والاستعباد"},{"branch_id":"B005","branch_image_ar":"التذليل والتسوية"},{"branch_id":"B006","branch_image_ar":"التكريم والتعظيم"},{"branch_id":"B007","branch_image_ar":"القوة والصلابة"},{"branch_id":"B008","branch_image_ar":"الأنفة والغضب"},{"branch_id":"B009","branch_image_ar":"قلة اللبث وسرعة العدو"},{"branch_id":"B010","branch_image_ar":"التفرق في الوجوه"},{"branch_id":"B011","branch_image_ar":"العطب والانقطاع"},{"branch_id":"B012","branch_image_ar":"صَلاءة الطيب"}],"mapped_root_id":"root_000973","mapped_root_norm":"ع ب د"}]},{"root":"ع و ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الإعانة والمظاهرة"},{"branch_id":"B002","branch_image_ar":"العَوان بين السنين"},{"branch_id":"B003","branch_image_ar":"الحرب العَوان"},{"branch_id":"B004","branch_image_ar":"النخلة العَوانة القديمة"},{"branch_id":"B005","branch_image_ar":"استواء الخلقة وتلاحق القوة"},{"branch_id":"B006","branch_image_ar":"العانة قطيع الحمر"},{"branch_id":"B007","branch_image_ar":"عانة الرجل"},{"branch_id":"B008","branch_image_ar":"النسبة إلى عانة"}],"mapped_root_id":"root_001064","mapped_root_norm":"ع و ن"},{"branches":[{"branch_id":"B001","branch_image_ar":"العين الناظرة"},{"branch_id":"B002","branch_image_ar":"المشاهدة بالعين"},{"branch_id":"B003","branch_image_ar":"عين الحفظ والرعاية"},{"branch_id":"B004","branch_image_ar":"الإصابة بالعين"},{"branch_id":"B005","branch_image_ar":"العين الجاسوسة"},{"branch_id":"B006","branch_image_ar":"منبع الماء الجاري"},{"branch_id":"B007","branch_image_ar":"عين الجلد والسقاء"},{"branch_id":"B008","branch_image_ar":"عين الشمس"},{"branch_id":"B009","branch_image_ar":"النقرة أو الموضع العيني"},{"branch_id":"B010","branch_image_ar":"عين السحاب والمطر"},{"branch_id":"B011","branch_image_ar":"النقد الحاضر"},{"branch_id":"B012","branch_image_ar":"العينة والسلف"},{"branch_id":"B013","branch_image_ar":"عين الشيء نفسه"},{"branch_id":"B014","branch_image_ar":"العين خيار الشيء"},{"branch_id":"B015","branch_image_ar":"أعيان القوم والإخوة"},{"branch_id":"B016","branch_image_ar":"سعة العين وحسنها"},{"branch_id":"B017","branch_image_ar":"العين بمعنى الناس الحاضرون"}],"mapped_root_id":"root_001069","mapped_root_norm":"ع ي ن"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:5","membership_added_ayah":true,"membership_target_surah":104,"surface_ref":"1:5"},{"ayah_ref":"1:6","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:6","root_occurrences":[{"lemmas_ar":["هَدَى"],"occurrence_count":1,"pos_tags":["V"],"root":"ه د ي","surfaces_ar":["ٱهْدِ"],"word_indices":["1"]},{"lemmas_ar":["صِرَٰط"],"occurrence_count":1,"pos_tags":["N"],"root":"ص ر ط","surfaces_ar":["صِّرَٰطَ"],"word_indices":["2"]},{"lemmas_ar":["مُّسْتَقِيم"],"occurrence_count":1,"pos_tags":["ADJ"],"root":"ق و م","surfaces_ar":["مُسْتَقِيمَ"],"word_indices":["3"]}],"root_sequence":["ه د ي","ص ر ط","ق و م"],"text_ar":"ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ"}],"context_order":["1:6"],"context_root_cues":[{"root":"ه د ي","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"دلالة بلطف إلى الطريق والحق"},{"branch_id":"B002","branch_image_ar":"جهة الأمر وسيرته وقصده"},{"branch_id":"B003","branch_image_ar":"المتقدم الهادي وأوائل الشيء"},{"branch_id":"B004","branch_image_ar":"بعثة لطف وهدية إلى ذي مودة"},{"branch_id":"B005","branch_image_ar":"الهدي المهدى إلى الحرم"},{"branch_id":"B006","branch_image_ar":"العروس المهدية إلى زوجها"},{"branch_id":"B007","branch_image_ar":"هدي الحرمة والأسير"},{"branch_id":"B008","branch_image_ar":"مشي التهادي مع الاعتماد والتمايل"},{"branch_id":"B009","branch_image_ar":"الهداء البليد الضعيف"},{"branch_id":"B010","branch_image_ar":"هدي السكون وحسن الهيئة"},{"branch_id":"B011","branch_image_ar":"إهداء الشعر ومهاداته"}],"mapped_root_id":"root_001583","mapped_root_norm":"ه د ي"}]},{"root":"ص ر ط","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الطريق المستقيم"},{"branch_id":"B002","branch_image_ar":"الغيبة في المرور والبلع"},{"branch_id":"B003","branch_image_ar":"السيف القاطع الماضي في الضربة"}],"mapped_root_id":"root_000858","mapped_root_norm":"ص ر ط"}]},{"root":"ق و م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"جماعة الناس والرجال"},{"branch_id":"B002","branch_image_ar":"انتصاب وقيام بالبدن"},{"branch_id":"B003","branch_image_ar":"عزم ونهوض إلى الأمر"},{"branch_id":"B004","branch_image_ar":"رعاية وحفظ وولاية"},{"branch_id":"B006","branch_image_ar":"مقام وإقامة في موضع"},{"branch_id":"B007","branch_image_ar":"نيابة وقيام مقام غيره"},{"branch_id":"B008","branch_image_ar":"استقامة واعتدال واستواء"},{"branch_id":"B009","branch_image_ar":"قوام وعماد ومعاش"},{"branch_id":"B010","branch_image_ar":"قيمة وتقويم وتسعير"},{"branch_id":"B011","branch_image_ar":"قامة وقوام الجسم والطول"},{"branch_id":"B012","branch_image_ar":"آلة قائمة وجزء قائم"},{"branch_id":"B013","branch_image_ar":"قيامة وبعث وقيام الساعة"},{"branch_id":"B014","branch_image_ar":"مقاومة ومنازلة"},{"branch_id":"B015","branch_image_ar":"وزن سواء ومقدار معتدل"},{"branch_id":"B016","branch_image_ar":"جمود ووقوف وكلال"},{"branch_id":"B017","branch_image_ar":"انتصاف النهار وقائم الظهيرة"},{"branch_id":"B018","branch_image_ar":"نفاق السوق"},{"branch_id":"B019","branch_image_ar":"وجع قائم بالعضو"},{"branch_id":"B020","branch_image_ar":"قوام في قوائم الشاة"},{"branch_id":"B021","branch_image_ar":"عين قائمة ذاهبة البصر"}],"mapped_root_id":"root_001273","mapped_root_norm":"ق و م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:6","membership_added_ayah":true,"membership_target_surah":104,"surface_ref":"1:6"},{"ayah_ref":"1:7","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:7","root_occurrences":[{"lemmas_ar":["صِرَٰط"],"occurrence_count":1,"pos_tags":["N"],"root":"ص ر ط","surfaces_ar":["صِرَٰطَ"],"word_indices":["1"]},{"lemmas_ar":["أَنْعَمَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ن ع م","surfaces_ar":["أَنْعَمْ"],"word_indices":["3"]},{"lemmas_ar":["غَيْر"],"occurrence_count":1,"pos_tags":["N"],"root":"غ ي ر","surfaces_ar":["غَيْرِ"],"word_indices":["5"]},{"lemmas_ar":["مَغْضُوب"],"occurrence_count":1,"pos_tags":["N"],"root":"غ ض ب","surfaces_ar":["مَغْضُوبِ"],"word_indices":["6"]},{"lemmas_ar":["ضَآلّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ض ل ل","surfaces_ar":["ضَّآلِّينَ"],"word_indices":["9"]}],"root_sequence":["ص ر ط","ن ع م","غ ي ر","غ ض ب","ض ل ل"],"text_ar":"صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ"}],"context_order":["1:7"],"context_root_cues":[{"root":"ص ر ط","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الطريق المستقيم"},{"branch_id":"B002","branch_image_ar":"الغيبة في المرور والبلع"},{"branch_id":"B003","branch_image_ar":"السيف القاطع الماضي في الضربة"}],"mapped_root_id":"root_000858","mapped_root_norm":"ص ر ط"}]},{"root":"ن ع م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"حسن الحال والنعمة"},{"branch_id":"B002","branch_image_ar":"اللين والنعومة ورفاه العيش"},{"branch_id":"B003","branch_image_ar":"مدح الشيء بنعم"},{"branch_id":"B004","branch_image_ar":"الجواب بنعم والتصديق"},{"branch_id":"B005","branch_image_ar":"مال الأنعام والإبل"},{"branch_id":"B006","branch_image_ar":"النعام والنعامة الطائر"},{"branch_id":"B007","branch_image_ar":"ما سمي نعامة تشبيها بالهيئة"},{"branch_id":"B008","branch_image_ar":"طيران النعامة وتفرق القوم"},{"branch_id":"B009","branch_image_ar":"النعامى ريح لينة"},{"branch_id":"B010","branch_image_ar":"زاد وأنعم في الفعل"},{"branch_id":"B011","branch_image_ar":"موافقة المكان وطيب المقام"},{"branch_id":"B012","branch_image_ar":"المشي على القدم وابتذالها"},{"branch_id":"B013","branch_image_ar":"نعم الله بك عينا وقرة العين"}],"mapped_root_id":"root_001525","mapped_root_norm":"ن ع م"}]},{"root":"غ ي ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الصلاح والمنفعة بالميرة والسقي والإصلاح"},{"branch_id":"B002","branch_image_ar":"الغَيْر في الدية"},{"branch_id":"B003","branch_image_ar":"تغيير الصورة أو إبدال الشيء بغيره"},{"branch_id":"B004","branch_image_ar":"الغَيْرة على الأهل"},{"branch_id":"B005","branch_image_ar":"السوى والخلاف والاستثناء والنفي"}],"mapped_root_id":"root_001119","mapped_root_norm":"غ ي ر"}]},{"root":"غ ض ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"اشتداد السخط وثورانه للانتقام"},{"branch_id":"B002","branch_image_ar":"الغضب لشخص حي أو به بعد موته"},{"branch_id":"B003","branch_image_ar":"المراغمة والمخالفة"},{"branch_id":"B004","branch_image_ar":"صلابة الصخرة وتماسكها"},{"branch_id":"B005","branch_image_ar":"غلظ الجسم وشدة الحمرة"},{"branch_id":"B006","branch_image_ar":"تورم العين وما حولها"},{"branch_id":"B007","branch_image_ar":"العبوس والضجر والعظم في وصف الحيوان أو الشخص"},{"branch_id":"B008","branch_image_ar":"جلد صلب أو مطوي كدرقة"}],"mapped_root_id":"root_001092","mapped_root_norm":"غ ض ب"}]},{"root":"ض ل ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الضلال عن الهدى والقصد"},{"branch_id":"B002","branch_image_ar":"الغيبوبة والخفاء"},{"branch_id":"B003","branch_image_ar":"فقدان الشيء"},{"branch_id":"B004","branch_image_ar":"ضياع الحفظ"},{"branch_id":"B005","branch_image_ar":"الضالّة في المضيعة"}],"mapped_root_id":"root_000913","mapped_root_norm":"ض ل ل"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:7","membership_added_ayah":true,"membership_target_surah":104,"surface_ref":"1:7"}],"support_registry":[{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Courtyard, Stone Pen, and Mountain Recess","source_type":"channel","support_id":"sup_1fbcde8a665debbef781","text":"104:8 مُّؤْصَدَةٌ (`و ص د`); no separate surface occurrence for `ء ص د`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Sprouting, Flowering, and Close-Rooted Growth","source_type":"channel","support_id":"sup_26ee11e89ce063f1a310","text":"Something hidden or low comes into view by rising, sprouting, approaching, peeking, flashing, or occupying a vantage point.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Sprouting, Flowering, and Close-Rooted Growth","source_type":"channel","support_id":"sup_3d6e15c7ecffec5a9491","text":"Emergence proceeds from first visible growth to flower and then to a dense stand whose roots draw near one another. The unnamed mixed palm adds generative variety to the same cultivated scene.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Courtyard, Stone Pen, and Mountain Recess","source_type":"channel","support_id":"sup_4badb174a5098596deb7","text":"Space is bounded by doors, yards, pens, covers, restraints, walls, and load-bearing members that determine what remains inside and what can stand.","trust":"trusted"},{"branch_refs":["root_001653/B001","root_001653/B002"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"A:Sealed Doorway","source_type":"channel","support_id":"sup_4f2ab0a9681fb98b573c","text":"firmly closed door (`و ص د:B001/m01`); doorway attached to a dwelling (`و ص د:B002/m02`); sealing and shutting (`ء ص د:B001/m01`)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Sealed Doorway","source_type":"channel","support_id":"sup_50870d6fa2c37fd646fe","text":"A doorway is brought shut and made fast so passage is no longer available.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Sealed Doorway","source_type":"channel","support_id":"sup_55665a5337b68352eaf5","text":"Object and action coincide: the doorway marks the access point, while closing pressure converts it into an impassable boundary. The alternate closure branch intensifies the sense of something clamped over its contents.","trust":"trusted"},{"branch_refs":["root_000259/B011","root_000945/B005","root_001564/B004","root_001653/B004"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"B:Sprouting, Flowering, and Close-Rooted Growth","source_type":"channel","support_id":"sup_5f7a4f8320a8a28a7f86","text":"emerging palm spathe or crop (`ط ل ع:B005/m01`); blossom (`ن و ر:B004/m01`); close-rooted vegetation (`و ص د:B004/m01`); mixed seed-grown date palm (`ج م ع:B011/m01`)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Courtyard, Stone Pen, and Mountain Recess","source_type":"channel","support_id":"sup_63a5ca04e84df1f65c54","text":"Closure acquires a spatial interior. The house forecourt, livestock pen, and mountain recess all use surrounding edges to hold what lies within, even when the bounded space remains open above.","trust":"trusted"},{"branch_refs":["root_001653/B002","root_001653/B003"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"B:Courtyard, Stone Pen, and Mountain Recess","source_type":"channel","support_id":"sup_841384807a53aa4e0c3d","text":"house forecourt (`و ص د:B002/m01`); mountain stone pen (`و ص د:B003/m01`); encompassing enclosure (`ء ص د:B002/m01`); courtyard or open fore-space (`ء ص د:B004/m01`); place between mountains (`ء ص د:B005/m01`)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Courtyard, Stone Pen, and Mountain Recess","source_type":"channel","support_id":"sup_8750817c453187919d69","text":"A bounded exterior space gathers occupants or livestock within a forecourt, stone enclosure, or recess between mountains.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"B:Sprouting, Flowering, and Close-Rooted Growth","source_type":"channel","support_id":"sup_a5c18d72be88982377ec","text":"Plants emerge from hidden growth, flower, and thicken into a closely rooted stand.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Sealed Doorway","source_type":"channel","support_id":"sup_a7d8e8226f01e27b3640","text":"Space is bounded by doors, yards, pens, covers, restraints, walls, and load-bearing members that determine what remains inside and what can stand.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"B:Sprouting, Flowering, and Close-Rooted Growth","source_type":"channel","support_id":"sup_d3438c2095bfd00355d0","text":"104:2 جَمَعَ (`ج م ع`); 104:6 نَارُ (`ن و ر`); 104:7 تَطَّلِعُ (`ط ل ع`); 104:8 مُّؤْصَدَةٌ (`و ص د`)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Sealed Doorway","source_type":"channel","support_id":"sup_d59157dcac91c1ce3dce","text":"104:8 مُّؤْصَدَةٌ (`و ص د`); no separate surface occurrence for `ء ص د`","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَيْلٌۭ لِّكُلِّ هُمَزَةٍۢ لُّمَزَةٍ","ayah_ref":"104:1"},{"arabic_uthmani":"إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ","ayah_ref":"104:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000036/B001","root_001315/B005","root_001376/B002","root_001600/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000036","role":"Closing over and shutting in supplies the terminal enclosure into which the earlier pressure can be reversed.","root":"و ص د","source_ref":"104:8","source_word_indices":["3"]},{"branch_id":"B005","mapped_root_id":"root_001315","role":"The encircling crown contributes an all-around topology, turning totality into circumferential pressure around the agents.","root":"ك ل ل","source_ref":"104:1","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001600","role":"Hand-pressure and squeezing materialize the aggressor's social action as compression that the later seal can return upon him.","root":"ه م ز","source_ref":"104:1","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001376","role":"Pushing supplies the outward displacement that is reversed when the plural objects are shut in rather than able to push others aside.","root":"ل م ز","source_ref":"104:1","source_word_indices":["4"]}],"changed_reading":{"after":"The seal is a spatial reversal of their own practice: those who pressed and pushed people are now compressed inside an all-around boundary.","before":"The seal is a generic punishment imposed on the named offenders."},"confidence":"medium","mechanism":"The opening social acts carry images of surrounding, pressing, and pushing. When the focus seal later closes عَلَيْهِم, those outward acts acquire a material recoil: agents who compressed and displaced others are themselves placed under an all-around, exit-denying pressure.","model_id":"delta_pressure_reversal","reader_inference":"The packet supplies encirclement, squeezing, pushing, and a seal; I supply the retaliatory arrow from their outward pressure to pressure returned upon them. A live alternative is that the social acts merely identify the occupants and the closure has no mimetic relation to those acts.","status":"new","structural_cues":["The opening agent nouns precede the later plural pronoun عَلَيْهِم, allowing the same people to move from sources of pressure to recipients of closure."],"trigger_roots":["ك ل ل","ه م ز","ل م ز"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_pressure_reversal","source_type":"hft","support_id":"sup_165680375e97542f7f38","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ","ayah_ref":"104:2"},{"arabic_uthmani":"إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ","ayah_ref":"104:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000036/B002","root_000259/B005","root_000989/B005","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000036","role":"The pen containing what lies inside supplies the focus geometry into which the collector's gathered total is reversed.","root":"و ص د","source_ref":"104:8","source_word_indices":["3"]},{"branch_id":"B005","mapped_root_id":"root_000259","role":"The fist closing its fingers provides a concrete clasp for gathering and lets accumulation prefigure the later fastening.","root":"ج م ع","source_ref":"104:2","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"The taking and multiplying of wealth supplies the contents whose controlled abundance defines the collector's prior agency.","root":"م و ل","source_ref":"104:2","source_word_indices":["3"]},{"branch_id":"B005","mapped_root_id":"root_000989","role":"Counting that returns with time contributes iterative rechecking, making the hoard a repeatedly secured total rather than a single acquisition.","root":"ع د د","source_ref":"104:2","source_word_indices":["4"]}],"changed_reading":{"after":"His own logic of gathering, grasping, and repeatedly securing a total returns as an enclosure that gathers and secures him.","before":"The hoarder is later placed in an unrelated closed punishment."},"confidence":"strong","mechanism":"Gathering draws dispersed units into one grasp, wealth supplies the accumulated contents, and repeated counting keeps re-closing the collection as a controlled total. The focus enclosure reverses possession: the collector's clasped aggregate becomes the form of a clasp around its collector.","model_id":"delta_hoard_becomes_clasp","reader_inference":"The packet supplies a closing fist, accumulated wealth, recurrent counting, and an enclosure; I infer an agency reversal in which the practiced clasp becomes a clasp around the practitioner. The live alternative is a simple moral sequence with no material echo between hoarding and sealing.","status":"new","structural_cues":["The chained verbs جَمَعَ and عَدَّدَهُ give the offender active control over bounded contents; عَلَيْهِم later makes him the bounded content."],"trigger_roots":["ج م ع","م و ل","ع د د"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_hoard_becomes_clasp","source_type":"hft","support_id":"sup_effc37c280bf1d1f85ae","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ","ayah_ref":"104:3"},{"arabic_uthmani":"إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ","ayah_ref":"104:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000318/B002","root_000429/B001","root_000429/B002","root_001457/B001","root_001653/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001653","role":"The securely fastened door converts permanence into enforced non-departure rather than protected life.","root":"و ص د","source_ref":"104:8","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000318","role":"Supposition marks the wealth-to-permanence link as the offender's constructed causal model, available for reversal.","root":"ح س ب","source_ref":"104:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"Abundant owned wealth supplies the imagined instrument by which the offender expects to secure duration.","root":"م و ل","source_ref":"104:3","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000429","role":"Stable continuance resistant to passing away supplies the desired duration that the seal recodes as confinement.","root":"خ ل د","source_ref":"104:3","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000429","role":"Clinging and remaining attached make the revised permanence spatial: the occupant is fixed to the enclosed state.","root":"خ ل د","source_ref":"104:3","source_word_indices":["4"]}],"changed_reading":{"after":"The seal counterfeits the desired immortality: he receives lastingness as forced attachment to a state he cannot leave.","before":"The seal merely disproves the belief that wealth grants immortality."},"confidence":"strong","mechanism":"The imagined causal chain runs from wealth to enduring life. The completed seal does not simply cancel that wish; it grotesquely changes its terms, replacing free persistence through possession with persistence in a condition from which departure is barred.","model_id":"delta_counterfeit_permanence","reader_inference":"The packet supplies supposition, wealth, resistant continuance, clinging, and a secured door; I infer ironic fulfillment, with desired permanence reversed into imposed non-exit. A live alternative is that closure only follows the failed belief and does not answer it in the same semantic currency.","status":"revised","structural_cues":["The clause أَنَّ مَالَهُ أَخْلَدَهُ explicitly gives wealth a supposed causative role, while the passive focus form removes the offender's control over the resulting duration."],"trigger_roots":["ح س ب","م و ل","خ ل د"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_counterfeit_permanence","source_type":"hft","support_id":"sup_a1caae65b879709ccb2c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّا ۖ لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ","ayah_ref":"104:4"},{"arabic_uthmani":"إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ","ayah_ref":"104:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000337/B001","root_001466/B001","root_001653/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001653","role":"The stone pen or mountain chamber supplies a hard containing volume that retains what has been cast into it.","root":"و ص د","source_ref":"104:8","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001466","role":"Throwing and casting supply the inbound motion, making closure the endpoint of a directed transfer rather than an initially static room.","root":"ن ب ذ","source_ref":"104:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000337","role":"Breaking a dry thing into fragments supplies the destructive internal operation whose products the enclosure prevents from dispersing.","root":"ح ط م","source_ref":"104:4","source_word_indices":["4"]}],"changed_reading":{"after":"The closure completes the crusher's mechanism by capturing what is cast in and retaining it through the destructive process.","before":"They are thrown into a crusher that happens also to be closed."},"confidence":"strong","mechanism":"Casting supplies entry velocity and crushing supplies destructive impact, but neither alone explains why the process cannot be escaped. The focus closure becomes the terminal capture phase: what is thrown into the crusher is held inside the operation after impact.","model_id":"delta_cast_crush_capture","reader_inference":"The packet supplies casting, fragmentation, and a stone enclosure; I supply the temporal arrow casting then impact then retention. A live alternative is that the casting and crushing name punishment while the later seal independently states only that escape is impossible.","status":"strengthened","structural_cues":["The movement from فِى in 104:4 to عَلَيْهِم in 104:8 sequences entry into the named process and closure over its occupants."],"trigger_roots":["ن ب ذ","ح ط م"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_cast_crush_capture","source_type":"hft","support_id":"sup_d3a112cca9f1e8f2f49e","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَمَآ أَدْرَىٰكَ مَا ٱلْحُطَمَةُ","ayah_ref":"104:5"},{"arabic_uthmani":"إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ","ayah_ref":"104:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000036/B001","root_000337/B001","root_000469/B008","root_000473/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000036","role":"Closing over supplies the opaque boundary that separates an exterior knower from the chamber's active interior.","root":"و ص د","source_ref":"104:8","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000473","role":"Knowledge and discernment make access to what the crusher is an explicit problem, allowing the seal to acquire an epistemic edge.","root":"د ر ي","source_ref":"104:5","source_word_indices":["2"]},{"branch_id":"B008","mapped_root_id":"root_000469","role":"The disturbed water-vortex supplies a form-distant image of an internally circulating process that cannot be read from a calm exterior.","root":"د ر ي","source_ref":"104:5","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000337","role":"Fragmentation supplies the concealed operation inside the boundary and keeps the epistemic model anchored to the named crusher.","root":"ح ط م","source_ref":"104:5","source_word_indices":["4"]}],"changed_reading":{"after":"Its seal also marks an epistemic asymmetry: the exterior can be told what it is while the turbulent interior remains resistant to ordinary inspection or mastery.","before":"The sealed chamber is fully described once its name and fire are supplied."},"confidence":"exploratory","mechanism":"The question of being made to know introduces an epistemic boundary around the crusher, while the split-root vortex image gives its hidden interior a turbulent material analogue. The focus seal can thus mark not only blocked bodies but blocked mastery from outside: revelation names the chamber without making its operation ordinary or surveyable.","model_id":"delta_epistemic_seal","reader_inference":"The packet supplies knowing, a split-root vortex, fragmentation, and closure; I infer that the closed material boundary also figures limited external mastery of the process within. A live alternative is that the question only magnifies the crusher rhetorically and the vortex branch contributes no mechanism.","status":"new","structural_cues":["The doubled interrogative frame وَمَا أَدْرَىٰكَ مَا interrupts the physical sequence to stage a problem of access before the fire is identified and finally sealed."],"trigger_roots":["د ر ي","ح ط م"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_epistemic_seal","source_type":"hft","support_id":"sup_5d2776aaaf2cae3635f9","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"نَارُ ٱللَّهِ ٱلْمُوقَدَةُ","ayah_ref":"104:6"},{"arabic_uthmani":"إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ","ayah_ref":"104:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000036/B001","root_000047/B001","root_001564/B002","root_001672/B001","root_001672/B003"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000036","role":"Closing over and shutting in supplies the furnace seal that prevents both the occupants and the active heat from freely dispersing.","root":"و ص د","source_ref":"104:8","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001564","role":"Blazing fire supplies the enclosing medium rather than merely an object located somewhere inside the enclosure.","root":"ن و ر","source_ref":"104:6","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000047","role":"The divine referent fixes agency and ownership outside the occupants, reinforcing that neither ignition nor closure is under their control.","root":"ء ل ه","source_ref":"104:6","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001672","role":"The act of kindling makes the enclosure dynamically burning rather than a cold, completed container.","root":"و ق د","source_ref":"104:6","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_001672","role":"The hearth or fire-site supplies the furnace architecture in which ignition and closure operate as one system.","root":"و ق د","source_ref":"104:6","source_word_indices":["3"]}],"changed_reading":{"after":"The kindled fire itself closes over them as a sealed furnace-medium, so burning and non-exit become one mechanism.","before":"A closed chamber contains a separately burning fire."},"confidence":"strong","mechanism":"Fire, active ignition, fuel, and fire-site images transform the focus enclosure into a furnace. Because the feminine pronoun can resume the preceding fire, the thing closed over them is not merely a room containing flame; the divinely attributed, kindled fire itself forms the enclosing medium, while the seal retains its intensity.","model_id":"delta_sealed_furnace","reader_inference":"The packet supplies blazing fire, divine attribution, ignition, a fire-site, and closure; I infer a furnace relation in which sealing retains intensity and makes the fire itself environmental. A live alternative is that the seal only denies bodily escape and adds no thermal or systemic function.","status":"revised","structural_cues":["The feminine singular إِنَّهَا can resume نَارُ ٱللَّهِ ٱلْمُوقَدَةُ, so grammar permits the fire itself to be what is closed over them."],"trigger_roots":["ن و ر","ء ل ه","و ق د"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_sealed_furnace","source_type":"hft","support_id":"sup_a67359983706f42e9f71","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ","ayah_ref":"104:7"},{"arabic_uthmani":"إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ","ayah_ref":"104:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000945/B003","root_000945/B006","root_001122/B002","root_001653/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001653","role":"The fastened door supplies outward non-passage, the restrictive half of the one-way boundary.","root":"و ص د","source_ref":"104:8","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_000945","role":"Overlooking and uncovering an affair supply penetrating inspection, making the fire's reach revelatory as well as spatial.","root":"ط ل ع","source_ref":"104:7","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_000945","role":"An ascending access or approach supplies a route inward and upward that contrasts with the occupants' blocked route out.","root":"ط ل ع","source_ref":"104:7","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001122","role":"The heart viewed as inner ignition makes the reached interior both the target of inspection and a site continuous with the surrounding fire.","root":"ف ء د","source_ref":"104:7","source_word_indices":["4"]}],"changed_reading":{"after":"The seal is selectively one-way: fire and exposure reach the innermost self, but the enclosed self has no reciprocal path outward.","before":"A seal blocks all crossing in either direction."},"confidence":"strong","mechanism":"The fire ascends to, overlooks, or exposes the inner hearts before it is said to be sealed over the people. This makes the boundary asymmetrical rather than simply impermeable: the destructive agency reaches and reveals the interior, while the sealed occupants cannot cross outward.","model_id":"delta_one_way_inward_boundary","reader_inference":"The packet supplies ascent, inspection, inward ignition, and a fastened door; I infer directional permeability, with destructive access inward but no occupant passage outward. A live alternative is a temporal sequence in which penetration occurs before a wholly impermeable closure, without any enduring one-way structure.","status":"new","structural_cues":["The relation عَلَى is repeated across تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ and عَلَيْهِم مُّؤْصَدَةٌ, linking inward reach to closure over the whole persons."],"trigger_roots":["ط ل ع","ف ء د"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_one_way_inward_boundary","source_type":"hft","support_id":"sup_4daa7b66b5ecfc645bc8","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ","ayah_ref":"104:8"},{"arabic_uthmani":"فِى عَمَدٍۢ مُّمَدَّدَةٍۭ","ayah_ref":"104:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_001043/B002","root_001043/B013","root_001407/B001","root_001407/B004","root_001653/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001653","role":"The sealed door supplies the aperture that the following supports can brace and keep shut.","root":"و ص د","source_ref":"104:8","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001043","role":"Propping a thing with a support supplies the fastening action that makes the closure structurally maintained.","root":"ع م د","source_ref":"104:9","source_word_indices":["2"]},{"branch_id":"B013","mapped_root_id":"root_001043","role":"Damming a flow contributes active blockage, casting the columns as impediments to passage rather than neutral scenery.","root":"ع م د","source_ref":"104:9","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001407","role":"Drawing something lengthwise until it connects supplies extended bars or supports spanning the closure.","root":"م د د","source_ref":"104:9","source_word_indices":["3"]},{"branch_id":"B004","mapped_root_id":"root_001407","role":"A term or time made long adds temporal extension, so the fastening persists rather than merely snapping shut once.","root":"م د د","source_ref":"104:9","source_word_indices":["3"]}],"changed_reading":{"after":"The closure is an engineered and durational lock: braced against release, extended across its boundary, and kept operative through time.","before":"The door is shut by an unspecified single act."},"confidence":"strong","mechanism":"Supports, columns, and a dam-like blockage give the seal an engineered fastening, while extension supplies both spatial reach and prolonged duration. The closure is therefore not a single moment of shutting but a braced apparatus extended across the boundary and sustained through time.","model_id":"delta_braced_duration_lock","reader_inference":"The packet supplies a sealed door, supports, a dam, lengthwise connection, and prolonged time; I infer that the columns function as extended closure hardware and that spatial extension activates duration. A live alternative is that the columns belong to the punishment scene without mechanically bracing the seal, and that extension is only spatial.","status":"strengthened","structural_cues":["The postposed phrase فِى عَمَدٍ مُّمَدَّدَةٍ follows immediately after the completed closure and can specify its architecture or condition."],"trigger_roots":["ع م د","م د د"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_braced_duration_lock","source_type":"hft","support_id":"sup_92c77e8ebb3c8ac9b9eb","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّا ۖ لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ","ayah_ref":"104:4"},{"arabic_uthmani":"نَارُ ٱللَّهِ ٱلْمُوقَدَةُ","ayah_ref":"104:6"},{"arabic_uthmani":"إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ","ayah_ref":"104:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000036/B002","root_001466/B006","root_001672/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000036","role":"The enclosing pen supplies the bounded vessel that contains what has been placed within.","root":"و ص د","source_ref":"104:8","source_word_indices":["3"]},{"branch_id":"B006","mapped_root_id":"root_001466","role":"Material cast into a vessel supplies the unusual processing analogy: thrown contents are enclosed so an internal change can proceed.","root":"ن ب ذ","source_ref":"104:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001672","role":"Active kindling replaces passive storage with a heated process occurring inside the sealed volume.","root":"و ق د","source_ref":"104:6","source_word_indices":["3"]}],"changed_reading":{"after":"As a contained material analogy, they are cast as contents into a sealed vessel whose closure enables an ongoing transformative process.","before":"The enclosure only stores prisoners after they are thrown in."},"confidence":"exploratory","containment":"The beverage-in-a-vessel branch of ن ب ذ is a branch-distant activation, not the direct sense of the contextual verb. It remains anchored through the explicit casting, the focus enclosure, and the kindled fire; downstream prose should present a sealed processing-vessel analogy, not claim fermentation as the ayah's lexical meaning.","focus_anchor":"The pen/chamber sense of the focus root can receive what is cast in and then close over it, supporting a container-process topology.","outlier_id":"outlier_sealed_processing_vessel"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_sealed_processing_vessel","source_type":"hft","support_id":"sup_dc0dac4740d7cd2ef07c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ","ayah_ref":"104:2"},{"arabic_uthmani":"إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ","ayah_ref":"104:8"},{"arabic_uthmani":"فِى عَمَدٍۢ مُّمَدَّدَةٍۭ","ayah_ref":"104:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000259/B001","root_001407/B001","root_001653/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001653","role":"Plants with closely packed roots supply the focus-anchored image of many interlocking elements leaving no easy path through.","root":"و ص د","source_ref":"104:8","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000259","role":"Joining dispersed things into one aggregate supplies the assembly of separate elements into a continuous enclosing mesh.","root":"ج م ع","source_ref":"104:2","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001407","role":"Lengthwise drawing until connection supplies the spanning links that turn close-packed elements into an extended barrier.","root":"م د د","source_ref":"104:9","source_word_indices":["3"]}],"changed_reading":{"after":"Exploratorily, the seal is a dense interlocked mesh: many gathered and extended elements close every route through their connected structure.","before":"The closure is one solid door laid across one opening."},"confidence":"exploratory","containment":"The close-rooted vegetation branch is unexpected and should not botanicalize the verse. It is nevertheless a legitimate non-dominant focus mapping, and gathering plus lengthwise connection make its topology coherent; downstream prose should qualify it as an interlocking-mesh analogy for how the seal holds, not as an alternative dictionary gloss.","focus_anchor":"The non-dominant mapping of the sole focus root supplies elements whose roots crowd together, allowing مُّؤْصَدَةٌ to activate closure by dense interlocking rather than by one planar door.","outlier_id":"outlier_interlocked_mesh"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_interlocked_mesh","source_type":"hft","support_id":"sup_60aeafa1f6b805240d9d","trust":"legacy_unbound"}]}
</lane_packet_json>
