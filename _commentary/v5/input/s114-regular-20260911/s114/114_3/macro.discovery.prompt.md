# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **114:3**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s114-regular-20260911/s114/114_3/macro.discovery.json` and modify nothing
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
  "ayah_ref": "114:3",
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
{"analysis_context":{"analysis_id":"s114-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"114:3","host_surah":114,"lane_context_refs":["114:0","114:1","114:2","114:4","114:5","114:6","1:2","1:3","1:4","1:5","1:6","1:7"],"ordered_context_refs":["114:0","114:1","114:2","114:4","114:5","114:6","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, tapınma eylemi ile bundan türeyen tapınılan veya tapınılır kılınan varlık anlamlarını kapsar; şaşkınlık, yoğun üzüntü ve salt özel ad kullanımları bu sınırın dışındadır.","branch_kind":"mixed_non_bare","branch_ref":"root_000047/B001","candidate_links":[{"candidate_id":"cand_a141ebc9607e343bf58b","lane":"macro"},{"candidate_id":"cand_fed3de197eb82ee15a4e","lane":"macro"},{"candidate_id":"cand_b7fa44c03435d65f2171","lane":"macro"},{"candidate_id":"cand_22c353ec36fe10a32fd9","lane":"macro"},{"candidate_id":"cand_89203cf9b82735660002","lane":"macro"},{"candidate_id":"cand_6e9f963d0aa0deae57fb","lane":"macro"},{"candidate_id":"cand_5bf4c39ff45a602d0073","lane":"macro"},{"candidate_id":"cand_4d3159f860f3a9da97c8","lane":"macro"},{"candidate_id":"cand_b373ab74fe22aebd264e","lane":"macro"},{"candidate_id":"cand_c7a119f0d4388d779979","lane":"macro"},{"candidate_id":"cand_a25c69ed47788b211120","lane":"macro"},{"candidate_id":"cand_da624628bd350ede26c4","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"إِلَٰه","morph_features":"STEM|POS:N|LEM:<ila`h|ROOT:Alh|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:3:1:1","qac_word_ref":"114:3:1","surface_ar":"إِلَٰهِ"}],"gloss":"tapınma ve tapınılan varlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel eylem, bir varlığa tapınmak ve kişinin kendini bu tapınmaya vermesidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylemden türeyen varlık anlamı, kendisine tapınılan varlığı veya tapınma konusu sayılan nesneyi gösterir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen kullanım, bir varlığı başkalarınca tapınılır duruma getirme veya öyle sunma işlemini bildirir."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Güneşe kimi topluluklarca tapınılması nedeniyle ona tapınılan varlık anlamındaki bir ad verilmesi, varlık anlamının tarihsel bir örneğidir."}}],"root_ar":"ء ل ه","root_id":"root_000047","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Eylem çekirdeğiyle ondan türeyen tapınılan varlık anlamının birlikte temsil edilmesi gereken genel açıklamalarda kullanılır.","boundary_detail":"Dal, tapınma eylemi ile bundan türeyen tapınılan veya tapınılır kılınan varlık anlamlarını kapsar; şaşkınlık, yoğun üzüntü ve salt özel ad kullanımları bu sınırın dışındadır.","branch_image_ar":"التعبد والمعبود","concept_gloss":"tapınma ve tapınılan varlık","contextual_glosses":[{"applicability":"Bir kişinin tapınma eylemini veya kendini tapınmaya vermesini bildiren eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylem olarak tapınma çekirdeğini eksiksiz korur."},"facet_ids":["F001"],"text":"tapınmak","usage_role":"general"},{"applicability":"Bir topluluğun kendisine tapındığı varlık veya nesneden söz edilen ad bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tapınmanın yöneldiği varlık veya nesne anlamını korur."},"facet_ids":["F002"],"text":"tapınılan varlık","usage_role":"contextual"},{"applicability":"Bir varlığın başkalarına tapınma konusu olarak benimsetilmesini anlatan ettirgen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir varlığı tapınma konusu durumuna getirme işlemini korur."},"facet_ids":["F003"],"text":"tapınılır kılmak","usage_role":"explanatory"}],"definition":"Bir varlığa tapınma eylemini ve kişinin kendini tapınmaya vermesini anlatır. Türemiş kullanımlarda bir varlığı tapınılır kılmayı, tapınılan varlığı ve tapınma konusu sayılan varlıkları da adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel eylem, bir varlığa tapınmak ve kişinin kendini bu tapınmaya vermesidir."},{"facet_id":"F002","role":"extension","statement":"Eylemden türeyen varlık anlamı, kendisine tapınılan varlığı veya tapınma konusu sayılan nesneyi gösterir."},{"facet_id":"F003","role":"specialization","statement":"Ettirgen kullanım, bir varlığı başkalarınca tapınılır duruma getirme veya öyle sunma işlemini bildirir."},{"facet_id":"F004","role":"example","statement":"Güneşe kimi topluluklarca tapınılması nedeniyle ona tapınılan varlık anlamındaki bir ad verilmesi, varlık anlamının tarihsel bir örneğidir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Yalnızca belirli bir varlık türünü adlandırdığı için bütün dalın karşılığı sanılabilir.","fit":"narrowing","loses":"Tapınma eylemini, kişinin tapınmaya yönelmesini ve tapınılır kılma işlemini karşılamaz.","preserves":"Tapınılan varlık anlamını kısa ve doğal biçimde korur."},"text":"tanrı"}],"identity_rationale":"Kaynak ifadesi tapınma eylemini, kişinin kendini tapınmaya vermesini, bir varlığı tapınılır kılmayı ve tapınılan varlığı aynı anlam örgüsü içinde açıkça birleştirir. Geçici dal çerçevesi bu çekirdeği ve ondan türeyen varlık adlarını doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tapınmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kendini tapınmaya vermek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"tapınılır kılmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"tapınılan varlık, tanrı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"tapınılan varlık"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"tanrılar, tapınılan nesneler"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"tapınma"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kimi toplulukların tapındığı için bu adla anılan güneş"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"senin tapınman"}],"lexicalization_note":"Tanım, yalın eylem çekirdeğini türemiş eylem ve varlık adlarından ayırır; türemiş biçimlerin kapsamı yalın eylemin tamamına aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Tapınma eylemi, korkuya bağlı özel tapınma yaşayışı ve aynı kökün özel ad dalı sınırı keskinleştirdi; peygamberlik, büyücülük, belirli tapınma nesneleri, sahiplik ve tarihsel hizmet grubu adayları ise yalnızca aynı dinsel alana veya tekil örneklere temas ettiği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal eylem ve yaklaşma yönünde yoğunlaşırken bu dal aynı çekirdekten tapınılan varlık ile ettirgen kılma anlamlarını da türetir; bu yüzden yalnızca eylem bağlamında yakınlaşırlar.","focus_only":"Tapınılan varlığı ve bir varlığı tapınılır kılma işlemini de adlandırır.","gloss":"tapınma ve yaklaşarak yönelme","neighbor_only":"Tapınmayla birlikte yaklaşma ve kendini bu işe verme yönünü öne çıkarır.","neighbor_ref":"root_001498/B001","relation_type":"near_synonym","shared_zone":"İki dal da tapınma eylemini ve kişinin bu eyleme yönelmesini kapsar."},{"boundary_match":"partial","distinction":"Bu dal genel tapınma çekirdeğini ve ondan türeyen varlık anlamlarını kapsar; komşu dal ise korku, inziva ve olağanın üstündeki uygulamalarla sınırlı özel bir yaşayışı anlatır.","focus_only":"Tapınmayı korku, inziva veya aşırı uygulama koşuluna bağlamaz ve tapınılan varlığı da adlandırabilir.","gloss":"korkuyla yoğunlaşan özel tapınma yaşayışı","neighbor_only":"Korkudan doğan, inziva veya ek yüklenme biçimindeki özel bir tapınma yaşayışını bildirir.","neighbor_ref":"root_000604/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da kişinin kendini tapınmaya vermesi bulunur."},{"boundary_match":"partial","distinction":"Bu dal genel anlam örgüsünü verir; komşu dal ise o örgüden türemiş özel adı ve adın belirli söz kalıplarındaki kullanımını ayrı bir biçim alanı olarak sınırlar.","focus_only":"Genel tapınma eylemini, tapınılan varlığı ve tapınılır kılmayı kapsar.","gloss":"Yaratıcıya özgü ad ve kullanım kalıpları","neighbor_only":"Yaratıcıya özgü adı ve bu adla kurulan seslenme, dilek ve ant kalıplarını kapsar.","neighbor_ref":"root_000047/B002","relation_type":"near_neighbor","shared_zone":"Özel ad, tapınılan yüce varlık düşüncesi üzerinden bu dalın varlık anlamıyla bağlantılıdır."}],"source_phrase_ar":"أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)","source_summary":"Kaynakların ortak çizgisi, tapınmayı anlamın temeli sayar; kişinin tapınmaya yönelmesini, tapınılan varlığı ve tapınılır kılma işlemini bu temelden türetir. Tapınma konusu sayılan yontular ve güneş örneği, varlık anlamının belirli uygulamalarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه أله وتأله بمعنى عبد وتنسك، والتأليه بمعنى التعبيد، والإله والآلهة والإلاهة لما جعل معبودا.","what_is_not_ar":"لا يدخل فيه أله بمعنى تحير، ولا ألهت على فلان بمعنى اشتد جزعي عليه، ولا أسماء المواضع أو الحية أو الهلال إلا من جهة التسمية لا معنى العبادة."},"support_links":["sup_02e169fe0d3adf6d330d","sup_15654188a4a968fdf517","sup_1bda9c12faa6759bb714","sup_2f91a8a3542485f8254c","sup_6097d2a052d527c059e7","sup_6f7fc1ca0bc4eae9000a","sup_b4ff40f5dbbb297b8e4c","sup_bdd37317ea70daa6c704","sup_bfc8c4e17918a87aaa4c","sup_c84d65e31f3be5dc8853","sup_d85d3cf24e0877bb451e","sup_e908d372714a107278e4"]},{"boundary":"Dal, özel ad ile bu ada bağlı seslenme, dilek, şaşma ve ant biçimleriyle sınırlıdır; herhangi bir tapınılan varlığı gösteren genel ad anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000047/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِلَٰه","morph_features":"STEM|POS:N|LEM:<ila`h|ROOT:Alh|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:3:1:1","qac_word_ref":"114:3:1","surface_ar":"إِلَٰهِ"}],"gloss":"Yaratıcıya özgü ad ile seslenme ve ant biçimleri","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dalın merkezinde, Yaratıcıyı başkalarından ayırarak gösteren ve yalnız ona özgü sayılan özel ad bulunur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Özel adın, tapınılan varlığı bildiren genel addan ses düşmesi ve belirleyici unsur eklenmesiyle oluştuğu açıklanır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özel ad, sözün başında ant değeri taşıyarak ardından gelen yapmama bildirimini güçlendirebilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Özel adın doğrudan ya da seslenme öğesi yerine geçen bir sonla kullanılması, yakarma ve dilek bildiren seslenme biçimleri kurar."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Ses veya parçaların düşürüldüğü kısalmış biçimler, şaşma ve ant anlatan kalıplarda kullanılır."}}],"root_ar":"ء ل ه","root_id":"root_000047","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Özel adın kendisiyle ona bağlı seslenme, dilek ve ant kullanımlarının birlikte açıklanması gereken dal düzeyinde kullanılır.","boundary_detail":"Dal, özel ad ile bu ada bağlı seslenme, dilek, şaşma ve ant biçimleriyle sınırlıdır; herhangi bir tapınılan varlığı gösteren genel ad anlamına genişletilmez.","branch_image_ar":"اسم الله في القسم والنداء","concept_gloss":"Yaratıcıya özgü ad ile seslenme ve ant biçimleri","contextual_glosses":[{"applicability":"Söz konusu adın yalnız Yaratıcıyı gösteren yalın ad olarak ele alındığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Adın Yaratıcıya özgü olmasını ve ayırt edici ad işlevini korur."},"facet_ids":["F001"],"text":"Yaratıcı'nın özel adı","usage_role":"general"},{"applicability":"Yakarış veya dilek sırasında Yaratıcıya doğrudan seslenilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaratıcıya yöneltilen doğrudan seslenme işlevini doğal biçimde korur."},"facet_ids":["F004"],"text":"ey Tanrı","usage_role":"contextual"},{"applicability":"Özel adın bir bildirimin doğruluğunu pekiştiren ant değeri taşıdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaratıcıya dayanarak ant verme işlevini açık biçimde korur."},"facet_ids":["F003"],"text":"Tanrı adına ant olsun","usage_role":"contextual"},{"applicability":"Özel adın ses veya parçaları düşürülmüş tarihsel kalıplarının işlevini açıklarken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kısaltılma biçimini ve şaşma ya da ant işlevini birlikte korur."},"facet_ids":["F005"],"text":"kısaltılmış şaşma veya ant sözü","usage_role":"explanatory"}],"definition":"Yaratıcıya özgü adın kendisini ve bu adla kurulan seslenme, dilek, şaşma ve ant biçimlerini kapsar. Bu biçimler doğrudan seslenme, adın ant değeriyle kullanılması veya ses ve parçaların düşürülmesiyle kısaltılma yollarını gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dalın merkezinde, Yaratıcıyı başkalarından ayırarak gösteren ve yalnız ona özgü sayılan özel ad bulunur."},{"facet_id":"F002","role":"source_variant","statement":"Özel adın, tapınılan varlığı bildiren genel addan ses düşmesi ve belirleyici unsur eklenmesiyle oluştuğu açıklanır."},{"facet_id":"F003","role":"associated_use","statement":"Özel ad, sözün başında ant değeri taşıyarak ardından gelen yapmama bildirimini güçlendirebilir."},{"facet_id":"F004","role":"associated_use","statement":"Özel adın doğrudan ya da seslenme öğesi yerine geçen bir sonla kullanılması, yakarma ve dilek bildiren seslenme biçimleri kurar."},{"facet_id":"F005","role":"source_variant","statement":"Ses veya parçaların düşürüldüğü kısalmış biçimler, şaşma ve ant anlatan kalıplarda kullanılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Genel tür adı olarak başka tapınılan varlıklar için de kullanılabildiğinden özel adla karışır.","fit":"narrowing","loses":"Adın tek bir varlığa özgü özel ad oluşunu ve seslenme ile ant biçimlerini karşılamaz.","preserves":"Yüce bir tapınılan varlığa gönderimde bulunma yönünü korur."},"text":"tanrı"}],"identity_rationale":"Kaynak ifadesi Yaratıcıya özgü adın kendisini, genel tapınılan-varlık adından türetiliş açıklamasını ve bu özel adla kurulan seslenme ile ant biçimlerini birlikte verir. Geçici çerçeve kullanılabilir, ancak dal yalnızca seslenme ve ant kalıpları değildir; özel adın yalın kullanımı da çekirdekte tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"Yaratıcıya özgü ad"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"Tanrı adına ant olsun, bunu yapmadım"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ey Tanrı; yakarma seslenişi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ey Tanrı; doğrudan seslenme"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"Tanrı adına sen veya baban; şaşma ya da ant kalıbı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları"}],"lexicalization_note":"Yalın özel ad, doğrudan seslenme biçimleri ve ant ya da şaşma kalıpları ayrı tutulur; kalıplara özgü işlevler özel adın her kullanımına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Genel tapınma dalı, yaşam üzerine ant, genel seslenme, kısaltılmış kişi seslenmesi ve yakarışa karşılık sözü gerçek sınır karşılaştırmaları sağladı; baba hitapları, genel dışlama yapıları, başka ant sözleri ve sesçe eşlik eden kalıplar daha zayıf ya da yalnızca biçimsel temas gösterdiği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli bir özel adın biçim ve kullanım alanıdır; komşu dal ise özel adla sınırlanmayan genel tapınma eylemini ve tapınılan varlık anlamını verir.","focus_only":"Yaratıcıya özgü adı ve bu adla kurulan seslenme, dilek, şaşma ve ant biçimlerini kapsar.","gloss":"tapınma ve tapınılan varlık","neighbor_only":"Genel tapınma eylemini, tapınılan varlığı ve bir varlığı tapınılır kılma işlemini kapsar.","neighbor_ref":"root_000047/B001","relation_type":"near_neighbor","shared_zone":"Özel ad, tapınılan yüce varlığı göstermesi bakımından genel varlık anlamına dayanır."},{"boundary_match":"partial","distinction":"Ortak işlev ant vermedir, fakat bu dalın dayanağı Yaratıcıya özgü addır; komşu dal yaşam süresini bildiren sözleri kullanır ve ayrıca ısrarlı istemeye uzanabilir.","focus_only":"Ant işlevini Yaratıcıya özgü adın yalın veya kısalmış biçimleriyle kurar.","gloss":"ömür üzerine ant ve ısrarlı isteme","neighbor_only":"Ant veya ısrarlı isteme işlevini yaşam süresini bildiren sözlerle kurar.","neighbor_ref":"root_001044/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir sözü güçlendiren ant işlevli kalıplar içerir."},{"boundary_match":"field_only","distinction":"Bu dal belirli bir muhatabın özel adı çevresinde oluşur; komşu dal ise muhatabın kimliğinden bağımsız genel seslenme araçlarını ve uzaklık ayrımını konu edinir.","focus_only":"Belirli bir özel adı ve o adın yakarma ile ant kullanımlarını içerir.","gloss":"genel seslenme öğeleri","neighbor_only":"Yakın veya uzaktaki muhataba yöneltilen genel seslenme öğelerini bildirir.","neighbor_ref":"root_000074/B008","relation_type":"same_field","shared_zone":"Her iki dal da doğrudan seslenme sırasında kullanılan biçimlerle ilgilidir."},{"boundary_match":"field_only","distinction":"Bu dalın kısalmaları belirli özel adın dinsel seslenme ve ant işlevlerine bağlıdır; komşu dalın kısalmaları ise belirsiz bir kişiye seslenmenin dilbilgisel biçimleridir.","focus_only":"Yaratıcıya özgü adı ve ona bağlı seslenme ile ant biçimlerini kapsar.","gloss":"kişiye yönelik kısaltılmış seslenme","neighbor_only":"Belirsiz bir kişiye yönelen kısaltılmış seslenme biçimlerini kapsar.","neighbor_ref":"root_001178/B003","relation_type":"same_field","shared_zone":"Her iki dalda da seslenme sırasında biçimsel kısalma görülebilir."},{"boundary_match":"thematic_only","distinction":"Bu dal bir muhataba seslenir; komşu dal ise söylenmiş yakarışa kabul dileği veya onayla karşılık verir. Aynı sahnede bulunsalar da anlam çekirdekleri örtüşmez.","focus_only":"Yakarışın yöneltildiği Yaratıcıyı özel adıyla çağırır.","gloss":"yakarışın kabulünü isteyen karşılık","neighbor_only":"Yakarışın kabul edilmesini isteyen veya söyleneni onaylayan karşılık sözünü bildirir.","neighbor_ref":"root_000054/B003","relation_type":"thematic","shared_zone":"İki dal da yakarış ortamında kullanılan kısa söz biçimlerine katılır."}],"source_phrase_ar":"فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)","source_summary":"Kaynaklar özel adı Yaratıcıya özgü bir ad olarak tanımlar ve onu tapınılan varlığı gösteren genel adla köken bakımından ilişkilendirir. Aynı adın doğrudan seslenmede, yakarmada, ant bildiriminde ve parçaları düşürülmüş kalıplarda kullanıldığı birlikte gösterilir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه اسم الله والقول في أصله من إله، وصيغ الاستعمال مثل الله ما فعلت بمعنى والله، واللهم، ويا الله، ولاه أبوك أو لاه أنت ونحوها.","what_is_not_ar":"ليس فرعا مستقلا عن معنى الإله المعبود من جهة الاشتقاق، ولا يدخل فيه إطلاق إله أو آلهة على كل معبود إذا لم يكن الكلام على صيغة الاسم أو النداء أو القسم."},"support_links":[]},{"boundary":"Dal, insan türünü ve onun tekil ya da toplu üyelerini kapsar; yakınlık duygusunu, duyusal algıyı ve insana dönük yanı kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B001","candidate_links":[{"candidate_id":"cand_b7fa44c03435d65f2171","lane":"macro"},{"candidate_id":"cand_b373ab74fe22aebd264e","lane":"macro"},{"candidate_id":"cand_a25c69ed47788b211120","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:3:2:2","qac_word_ref":"114:3:2","surface_ar":"نَّاسِ"}],"gloss":"insan türü ve bu türden bir kişi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan türünü, insanların oluşturduğu topluluğu veya bu türün tek bir üyesini görünmeyen varlıklar sınıfının karşısında adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlandırmanın insanların duyularla görünür oluşuna bağlanması, anlamın özü değil kökene ilişkin bir açıklamadır."}}],"root_ar":"ن و س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsanları bir tür veya topluluk olarak anlatırken de bu türün tek bir üyesini belirtirken de kullanılabilir.","boundary_detail":"Dal, insan türünü ve onun tekil ya da toplu üyelerini kapsar; yakınlık duygusunu, duyusal algıyı ve insana dönük yanı kapsamaz.","branch_image_ar":"ظهور الإنسان المخالف للتوحش والجن","concept_gloss":"insan türü ve bu türden bir kişi","contextual_glosses":[{"applicability":"Türün üyeleri topluca veya görünmeyen varlıklar sınıfının karşıtı olarak anıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan türünün toplu olarak adlandırılmasını açık ve doğal biçimde korur."},"facet_ids":["F001"],"text":"insanlar","usage_role":"general"},{"applicability":"Bağlam türün tek bir üyesini veya herhangi bir kimseyi gösterdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan topluluğundan tek bir üyenin belirtilmesini korur."},"facet_ids":["F001"],"text":"bir kişi","usage_role":"contextual"}],"definition":"Görünmeyen varlıklar sınıfının karşısında yer alan insan türünü, bu türün topluluğunu ya da tek bir üyesini belirtir. İnsanların görünür oluşu, bu adlandırma için aktarılan bir gerekçedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan türünü, insanların oluşturduğu topluluğu veya bu türün tek bir üyesini görünmeyen varlıklar sınıfının karşısında adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Adlandırmanın insanların duyularla görünür oluşuna bağlanması, anlamın özü değil kökene ilişkin bir açıklamadır."}],"identity_rationale":"Kaynak ifadesi, görünmeyen varlıklar sınıfının karşısındaki insan türünü, bu türün topluluğunu ve tek bir üyesini birlikte gösterir. Görünür olma açıklaması adlandırma gerekçesidir; insan olmanın kurucu tanımı değildir. Evde kimsenin bulunmadığını bildiren kalıp ise dal çekirdeğine genellenemez ve yalnızca kendi sözcüksel biriminde korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"insanlar; insan topluluğu"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"insan; insan türü"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"insan topluluğunun bir üyesi; insana veya insanlara ait"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"insanlar; insan toplulukları"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"insanlar; halk"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"evde hiç kimse yok"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"belirli bir ağızda insan ve onun çoğulu"}],"lexicalization_note":"Çıplak biçimlerdeki insan ve insan topluluğu anlamı dal çekirdeğidir; evde hiç kimse bulunmadığını anlatan kalıp ayrı tutulur ve çekirdeğe yeni bir genel anlam katmaz.","neighbor_coverage_note":"Bütün aday kartlar karşılaştırıldı. Yalnız insanı adlandırma sınırını yaratılmışlar kapsamından ve yakınlık duygusundan ayıran, okuyucu için en yararlı üç karşıtlık yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yer değiştirme yalnız insanı genel olarak adlandıran bağlamlarda mümkündür. Odak dalın görünmeyen varlıklarla sınıf karşıtlığı, komşunun ise görünür beden yönü kendi sınırında kalır.","focus_only":"Odak dal, insanları görünmeyen varlıklar sınıfının karşısında bir tür olarak kurar ve görünürlüğe dayalı bir adlandırma açıklaması taşır.","gloss":"insan türünü iki ayrı yönden adlandırma","neighbor_only":"Komşu dal, insanı görünür ten ve yaratılmış beden yönüyle adlandırır; tekil, çoğul, erkek ve kadın kapsamını özellikle öne çıkarır.","neighbor_ref":"root_000120/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da insanı hem tür hem bu türün üyesi olarak gösterebilir."},{"boundary_match":"partial","distinction":"Komşunun genel yaratılmışlar kapsamı odak dala taşınamaz; odak dal da yalnız insanları belirttiği için bütün yaratılmışların yerine kullanılamaz.","focus_only":"Odak dal yalnız insan türünü ve bu türün tekil ya da toplu üyelerini belirtir.","gloss":"insan türü ile bütün yaratılmışlar ayrımı","neighbor_only":"Komşu dal yeryüzündeki bütün yaratılmışları kapsayabilir ve bazı yorumlarda insanlarla görünmeyen varlıkları birlikte içerir.","neighbor_ref":"root_000061/B001","relation_type":"near_neighbor","shared_zone":"İnsanlar iki dalın gönderim alanında da bulunabilir."},{"boundary_match":"field_only","distinction":"Birinde insanın kim olduğu adlandırılır, diğerinde bir kişi ya da şey karşısındaki duygusal durum anlatılır; sıradan bağlamlarda birbirlerinin yerine geçmezler.","focus_only":"Odak dal insan türünü ve bu türün üyelerini adlandırır.","gloss":"insan adı ile yakınlık duygusu ayrımı","neighbor_only":"Komşu dal yabancılık ve ürkme duygusunun kalkmasını, yakınlık ve rahatlık oluşmasını anlatır.","neighbor_ref":"root_000059/B003","relation_type":"same_field","shared_zone":"Her iki dalda da insan, temel gönderim noktası veya deneyim sahibi olabilir."}],"source_phrase_ar":"الإنس خلاف الجن وسموا لظهورهم (maqayis;mufradat)؛ الإنس البشر والواحد إنسي والجمع أناسي (sihah)؛ الإنس جماعة الناس والأناسي جماع (tahdhib)","source_summary":"Aktarımlar, dalın insan türünü hem topluluk hem tek kişi olarak gösterebildiğinde ve görünmeyen varlıklar sınıfıyla karşıtlık kurduğunda birleşir. Görünürlük, ortak anlamdan çok adlandırmanın gerekçesi olarak sunulur.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الإنس والبشر والناس والأناسي والإنسان من حيث الجماعة أو الواحد، وما بالدار أنيس بمعنى أحد.","what_is_not_ar":"لا يدخل مجرد الاستئناس النفسي ولا الإيناس بمعنى الإبصار ولا الجانب الإنسي إلا بدليل."},"support_links":["sup_2f91a8a3542485f8254c","sup_bfc8c4e17918a87aaa4c","sup_d85d3cf24e0877bb451e"]},{"boundary":"Dal duyusal olarak fark etmeyi ve belirtilen bağlamlardaki işitme, sezme ve bakıp araştırma kullanımlarını kapsar; yakınlık ve rahatlık duygusunu kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B002","candidate_links":[{"candidate_id":"cand_89203cf9b82735660002","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:3:2:2","qac_word_ref":"114:3:2","surface_ar":"نَّاسِ"}],"gloss":"görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi gözle görerek fark etmeyi veya seçmeyi anlatır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli bir ses nesnesiyle kullanıldığında o sesi işitmeyi anlatır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kimsedeki olgunluk belirtisini bilip ayırt etmeyi veya kaygı veren bir durumu duyularla sezmeyi anlatabilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Çevreye bakıp dikkatle araştırarak birinin bulunup bulunmadığını anlamaya çalışma kullanımını taşır."}}],"root_ar":"ن و س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın görme çekirdeğiyle birlikte yalnız belirtilen bağlamlarda ortaya çıkan işitme, sezme ve çevreyi araştırma uzantılarını topluca verir.","boundary_detail":"Dal duyusal olarak fark etmeyi ve belirtilen bağlamlardaki işitme, sezme ve bakıp araştırma kullanımlarını kapsar; yakınlık ve rahatlık duygusunu kapsamaz.","branch_image_ar":"إيناس الشيء برؤية أو إحساس أو سماع","concept_gloss":"görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma","contextual_glosses":[{"applicability":"Nesnenin gözle seçildiği veya görüldüğü temel kullanımda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gözle görme ve görüleni fark etme işlemlerini birlikte korur."},"facet_ids":["F001"],"text":"görüp fark etmek","usage_role":"general"},{"applicability":"Nesne açıkça bir ses olduğunda kullanılan bağlama bağlı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sesin kulakla algılanması biçimindeki özel kullanımı korur."},"facet_ids":["F002"],"text":"sesi işitmek","usage_role":"contextual"},{"applicability":"Bir kimsedeki olgunluk veya kaygı uyandıran durum gibi bir belirtinin ayırt edildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Duyusal belirtiden bir durumun varlığını anlayıp ayırt etmeyi korur."},"facet_ids":["F003"],"text":"belirtiyi sezmek","usage_role":"contextual"},{"applicability":"Çevreyi gözleyip birinin bulunup bulunmadığını anlamaya çalışma kullanımında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dikkatle bakma ile birini bulmaya yönelik araştırmayı birlikte korur."},"facet_ids":["F004"],"text":"bakıp araştırmak","usage_role":"explanatory"}],"definition":"Bir şeyi görüp fark etmeyi anlatır. Belirli kullanımlarda bir sesi işitmeye, bir kimsedeki olgunluk belirtisini ya da kaygı veren bir durumu sezmeye ve çevreye bakarak birinin bulunup bulunmadığını araştırmaya uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi gözle görerek fark etmeyi veya seçmeyi anlatır."},{"facet_id":"F002","role":"extension","statement":"Belirli bir ses nesnesiyle kullanıldığında o sesi işitmeyi anlatır."},{"facet_id":"F003","role":"extension","statement":"Bir kimsedeki olgunluk belirtisini bilip ayırt etmeyi veya kaygı veren bir durumu duyularla sezmeyi anlatabilir."},{"facet_id":"F004","role":"associated_use","statement":"Çevreye bakıp dikkatle araştırarak birinin bulunup bulunmadığını anlamaya çalışma kullanımını taşır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Zamanla gelişen yakınlık ve yabancılığın kalkması anlamını ekler.","collision":"Yakınlık ve rahatlık bildiren ayrı dalla karışır.","fit":"displacement","loses":"Görme, işitme, belirtiyi sezme ve çevreye bakıp araştırma işlemlerini siler.","preserves":"Bir kişi veya şeye yönelen deneyim fikrini çok genel biçimde korur."},"text":"alışmak"}],"identity_rationale":"Kaynak ifadesi görmeyi temel alır, fakat belirli kullanımlarda işitmeyi, bir belirtiyi anlayıp ayırt etmeyi ve çevreye bakarak birini aramayı da aynı dalda aktarır. Bu yüzden dal genel ve sınırsız bir algı yetisi diye tanımlanamaz; her uzantı kendi bağlamına bağlı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir şeyi görmek ve fark etmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"sesi işitmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"onda olgunluk belirtisi görmek ve bunu anlamak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ürken yabani hayvanın birini sezip çevreye bakınması"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"çevreye bakıp birinin olup olmadığını araştırmak"}],"lexicalization_note":"Görüp fark etme çekirdeği ile ses işitme, olgunluk belirtisini ayırt etme ve çevreye bakıp araştırma kalıpları ayrı tutulur; kalıplardaki kapsam çıplak biçime genellenmez.","neighbor_coverage_note":"Bütün aday kartlar değerlendirildi. Görme, genel duyumsama ve yakınlık duygusuyla karışma olasılığı en yüksek üç sınır yayımlandı; diğer adaylar dalı açıklayan ek bir karşıtlık sağlamadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yalnız görsel algı bağlamında yakın karşılık olabilirler. Odak dalın işitme ve belirtiyi sezme uzantıları komşuya, komşunun göz organı anlamı da odak dala taşınamaz.","focus_only":"Odak dal, görmenin yanında belirli yapılarda işitme, belirti sezme ve çevreyi araştırma uzantılarını taşır.","gloss":"fark etme ile gözle görme ayrımı","neighbor_only":"Komşu dal göz organını, görme duyusunu ve göz açıp dikkatle bakma eylemini kendi başına kapsar.","neighbor_ref":"root_000121/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi göz yoluyla görüp seçme alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu daha genel bir duyu alanıdır; odak dalın uzantıları ise kanıtlanan nesne ve yapılara bağlıdır. Bu nedenle genel duyumsama her durumda odak ifadeyle karşılanamaz.","focus_only":"Odak dal görmeyi merkez alır ve yalnız belirli söz çevrelerinde işitme, sezme ve araştırmaya uzanır.","gloss":"belirli algı kullanımları ile genel duyumsama","neighbor_only":"Komşu dal herhangi bir duyu aracılığıyla algılama, bilme ve varlığını saptama alanını genel olarak kapsar.","neighbor_ref":"root_000321/B002","relation_type":"near_synonym","shared_zone":"Her ikisi de bir şeyin duyular aracılığıyla fark edilmesini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal algısal saptamayı, komşu dal ise karşılaşma sonrasındaki duygusal rahatlığı bildirir. Algı gerçekleşebilir ama yakınlık doğmayabilir.","focus_only":"Odak dal bir nesneyi görme, işitme veya belirtilerinden sezme eylemini anlatır.","gloss":"duyusal fark etme ile yakınlık hissetme","neighbor_only":"Komşu dal bir kişi ya da şey karşısında yabancılık ve ürkme duymayıp yakınlık hissetmeyi anlatır.","neighbor_ref":"root_000059/B003","relation_type":"near_neighbor","shared_zone":"Bir kişi veya şeyle karşılaşma iki anlam alanının ortak başlangıç durumu olabilir."}],"source_phrase_ar":"آنست الشيء إذا رأيته وآنسته إذا سمعته (maqayis)؛ آنسته أبصرته وآنست الصوت سمعته وآنست منه رشدا علمته (sihah)؛ آنس من جانب يعني أبصر نارا والاستئناس النظر وأحس بما رابه (tahdhib)؛ فإن آنستم منهم رشدا أي أبصرتم وآنست نارا (mufradat)","source_summary":"Aktarılan anlam alanının merkezi görüp fark etmektir. Aynı ifade ailesi belirli nesne ve yapılarda işitme, bir belirtiyi anlayıp ayırt etme, kaygı veren şeyi sezme ve bakıp araştırma yönlerinde kullanılır; bunlar sınırsız bir genel algı anlamı oluşturmaz.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه آنس الشيء إذا أبصره أو رآه، وآنس الصوت إذا سمعه، وأحس الفزع أو وجد الشيء في نفسه، والاستئناس بمعنى النظر والتبصر.","what_is_not_ar":"لا يدخل الأنس بمعنى الراحة والمؤالفة ولا الإنس بمعنى البشر إلا بقرينة."},"support_links":["sup_c84d65e31f3be5dc8853"]},{"boundary":"Dal duygusal yakınlık, rahatlık ve bunları sağlayan varlıkları kapsar; insan türünün adı, duyusal fark etme ve insana bakan yan anlamları dışarıda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B003","candidate_links":[{"candidate_id":"cand_22c353ec36fe10a32fd9","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:3:2:2","qac_word_ref":"114:3:2","surface_ar":"نَّاسِ"}],"gloss":"yabancılık duymadan yakınlık ve rahatlık hissetme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi ya da şey karşısında yabancılık ve ürkme duygusunun kalkıp yakınlık, rahatlık veya sevinç oluşmasını anlatır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişiye arkadaşlık ederek veya yanında bulunarak yabancılık duygusunu gideren kişi ya da şeyi adlandırır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsana alışık ve saldırgan olmayan hayvanı, özellikle bu nitelikteki köpeği anlatabilir."}}],"root_ar":"ن و س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi veya şeyin ürkütücü ve yabancı gelmemesi, tersine yakınlık ve iç rahatlığı vermesi anlatıldığında dalın çekirdeğini karşılar.","boundary_detail":"Dal duygusal yakınlık, rahatlık ve bunları sağlayan varlıkları kapsar; insan türünün adı, duyusal fark etme ve insana bakan yan anlamları dışarıda kalır.","branch_image_ar":"الأنس الذي يزيل الوحشة","concept_gloss":"yabancılık duymadan yakınlık ve rahatlık hissetme","contextual_glosses":[{"applicability":"Bir kişi veya şey karşısındaki yabancılık duygusunun kalktığı temel durumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Alışma sonucunda yabancılığın kalkmasını ve yakınlık oluşmasını korur."},"facet_ids":["F001"],"text":"alışıp yakınlık duymak","usage_role":"general"},{"applicability":"Yalnızlığı veya ürkmeyi gideren bir arkadaş, nesne ya da başka bir dayanak adlandırıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yakınlık ve güven veren kaynağın kişiyle sınırlı olmamasını korur."},"facet_ids":["F002"],"text":"yanında rahatlık veren kişi veya şey","usage_role":"explanatory"},{"applicability":"İnsandan kaçmayan ve ısırıp saldırmayan evcil ya da alışkın hayvan için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın insana alışıklığını ve saldırgan olmama sınırını birlikte korur."},"facet_ids":["F003"],"text":"insana alışık ve saldırgan olmayan","usage_role":"contextual"}],"definition":"Bir kişi ya da şey karşısında yabancılık, ürkme veya kaçınma duymayıp yakınlık, rahatlık ve sevinç hissetmeyi anlatır. Bu duyguyu veren kişi veya şeye ve insana alışık, saldırgan olmayan hayvana da aktarılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi ya da şey karşısında yabancılık ve ürkme duygusunun kalkıp yakınlık, rahatlık veya sevinç oluşmasını anlatır."},{"facet_id":"F002","role":"extension","statement":"Kişiye arkadaşlık ederek veya yanında bulunarak yabancılık duygusunu gideren kişi ya da şeyi adlandırır."},{"facet_id":"F003","role":"specialization","statement":"İnsana alışık ve saldırgan olmayan hayvanı, özellikle bu nitelikteki köpeği anlatabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Her türlü sevincin bu dala ait olduğu izlenimini verebilir.","fit":"narrowing","loses":"Yabancılığın ve ürkmenin kalkmasını, alışmayı ve rahatlık veren kişi ya da şey kapsamını kaybeder.","preserves":"Yakınlık durumunda ortaya çıkabilen olumlu duyguyu korur."},"text":"sevinç"}],"identity_rationale":"Kaynak ifadesi, bir kişi veya şey karşısında yabancılık ve ürkme duygusunun kalkmasını çekirdek anlam olarak verir. Yakınlık ve sevinç, rahatlık veren kişi ya da şey ve insana alışık saldırgan olmayan hayvan kullanımları bu çekirdekten bağımlı biçimde açıklanabilir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yakınlık ve rahatlık; yabancılık duymama"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"birine alışıp onun yanında sevinmek"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"biriyle yakınlık kurmak ve onsuz kendini yalnız hissetmek"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"yakın arkadaş; rahatlık veren kişi veya şey"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yakınlıktan ve söyleşiden hoşlanan genç kadın"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"insana alışık, saldırgan olmayan köpek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"gece yolcusuna veya konaklayana güven veren ateş"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"sahibine güven veren bütün silahlar; zırh, miğfer, koruyucu örtü ve kalkan gibi savunma donanımları"}],"lexicalization_note":"Yabancılık duymama çekirdeği ile rahatlık veren kişi veya şey ve insana alışık hayvan gibi özelleşmiş biçimler ayrı katmanlarda tutulur; özel biçimler bütün dalı tanımlamaz.","neighbor_coverage_note":"Bütün aday kartlar karşılaştırıldı. Alışıp bağlanma, özel dostluk ve insan türünü adlandırma alanları dal sınırını en açık gösterdiği için yalnız bu üç ayrım yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın belirleyici yönü yabancılık ve ürkmenin karşıtı olan iç rahatlığıdır; komşu dal süreklilik, bağlanma ve alışkanlık yönlerini odaktan daha geniş taşır.","focus_only":"Odak dal yabancılık ve ürkmenin kalkmasıyla oluşan yakınlık ve rahatlığı, ayrıca bunu sağlayan varlığı öne çıkarır.","gloss":"yakınlık rahatlığı ile alışıp bağlanma","neighbor_only":"Komşu dal bir kişi, yer veya şeye alışmayı, ona bağlanmayı, onunla sürekli bulunmayı ve hayvanın evcilleşmesini daha geniş biçimde kapsar.","neighbor_ref":"root_000045/B005","relation_type":"near_synonym","shared_zone":"İki dal da bir kişi, yer, şey veya hayvana karşı yabancılığın azalmasını anlatabilir."},{"boundary_match":"partial","distinction":"Her rahatlık veren yakınlık özel ve arı bir dostluk değildir. Komşunun karşılıklı dostluk sınırı odak dalın nesne ve hayvan uzantılarına uygulanamaz.","focus_only":"Odak dal kişi dışındaki şeylerin verdiği rahatlığı ve insana alışık hayvanı da kapsayabilir.","gloss":"rahatlık veren yakınlık ile özel dostluk","neighbor_only":"Komşu dal seçilmiş kişiler arasındaki arı, özel ve karşılıklı dostluk bağını anlatır.","neighbor_ref":"root_000430/B007","relation_type":"near_neighbor","shared_zone":"İki dal da kişiler arasında yakınlık ve içtenlik bulunan durumlarda buluşur."},{"boundary_match":"field_only","distinction":"Odak dal bir duygusal ilişkiyi, komşu dal ise bir varlık sınıfını adlandırır. İnsan olmak yakınlık hissetmeyi gerektirmez ve iki ifade birbirinin yerine geçmez.","focus_only":"Odak dal yabancılığın kalkmasıyla doğan duygusal yakınlığı ve rahatlığı anlatır.","gloss":"yakınlık durumu ile insan adı ayrımı","neighbor_only":"Komşu dal insan türünü, insan topluluğunu veya bu türden tek bir kişiyi adlandırır.","neighbor_ref":"root_000059/B001","relation_type":"same_field","shared_zone":"İnsan, iki dalda da temel katılımcı veya gönderim noktasıdır."}],"source_phrase_ar":"الأنس أنس الإنسان بالشيء إذا لم يستوحش منه (maqayis)؛ الإيناس خلاف الإيحاش والإنس خلاف الوحشة والأنيس المؤانس وكل ما يؤنس به (sihah)؛ أنست بفلان أي فرحت به والأنس والاستئناس هو التأنس وكلب أنوس نقيض العقور (tahdhib)؛ الأنس خلاف النفور ولكل ما يؤنس به (mufradat)","source_summary":"Ortak çekirdek, yabancılık ve kaçınmanın karşıtı olan yakınlık ve rahatlıktır. Bu durum birine alışıp onun yanında sevinmeyi, rahatlık veren kişi veya şeyi ve insana alışık saldırgan olmayan hayvanı kapsayacak biçimde genişler.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه أنس الإنسان بالشيء أو بفلان، المؤانسة والتأنيس، الأنيس وكل ما يؤنس به، الفرح بالقرب والحديث، والحيوان الأنوس غير العقور.","what_is_not_ar":"لا يدخل الإنس بمعنى البشر ولا الإيناس بمعنى الإبصار ولا الجانب الإنسي إلا بدليل."},"support_links":["sup_6f7fc1ca0bc4eae9000a"]},{"boundary":"Dal, bir nesnenin insana veya kullanıcıya bakan yanını belirtir; salt sol, salt sağ, genel ön taraf ya da insanın kendisi anlamına gelmez.","branch_kind":"bare","branch_ref":"root_000059/B004","candidate_links":[{"candidate_id":"cand_da624628bd350ede26c4","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:3:2:2","qac_word_ref":"114:3:2","surface_ar":"نَّاسِ"}],"gloss":"insana dönük yan","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin insana en yakın olan veya insana doğru bakan yanını belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvanda binicinin bulunduğu, binme ve sağma işlemlerinde insana yakın olan yanı anlatır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yayda okçuya doğru bakan ve kullanıcının karşısında bulunan yanı anlatır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İnsana yakın yan bazı aktarımda sol, başka bir aktarımda sağ diye belirlenir; yönün özü bu değişken tanımlardan bağımsızdır."}}],"root_ar":"ن و س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin yönü, ona yaklaşan veya onu kullanan insana göre belirlendiğinde dalın ortak çekirdeğini verir.","boundary_detail":"Dal, bir nesnenin insana veya kullanıcıya bakan yanını belirtir; salt sol, salt sağ, genel ön taraf ya da insanın kendisi anlamına gelmez.","branch_image_ar":"الجانب الإنسي المقبل على الإنسان","concept_gloss":"insana dönük yan","contextual_glosses":[{"applicability":"Hayvanın binme ve sağma sırasında insana yakın kalan yanı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın yanını biniciyle kurduğu işlevsel ilişkiye göre belirler."},"facet_ids":["F002"],"text":"biniciye yakın yan","usage_role":"contextual"},{"applicability":"Yayın kullanım sırasında okçuya doğru dönük olan yüzü belirtilirken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yay yüzünün yönünü okçunun konumuna göre belirleme özelliğini korur."},"facet_ids":["F003"],"text":"okçuya bakan yay yüzü","usage_role":"explanatory"}],"definition":"Bir nesnenin insana, kullanıcıya veya onun bulunduğu yöne bakan yanıdır. Hayvan ve yay üzerinde işlevsel ilişkiyle belirlenir; bu yanın sabit olarak sol ya da sağ sayılması konusunda aktarım uyuşmazlığı vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin insana en yakın olan veya insana doğru bakan yanını belirtir."},{"facet_id":"F002","role":"specialization","statement":"Hayvanda binicinin bulunduğu, binme ve sağma işlemlerinde insana yakın olan yanı anlatır."},{"facet_id":"F003","role":"specialization","statement":"Yayda okçuya doğru bakan ve kullanıcının karşısında bulunan yanı anlatır."},{"facet_id":"F004","role":"source_variant","statement":"İnsana yakın yan bazı aktarımda sol, başka bir aktarımda sağ diye belirlenir; yönün özü bu değişken tanımlardan bağımsızdır."}],"identity_rationale":"Kaynak ifadesinin güvenilir çekirdeği, bir şeyin insana veya onu kullanan kişiye dönük ve yakın olan yanıdır. Bu yanın solda mı sağda mı olduğu konusunda aktarımlar uyuşmaz; hayvan ve yay örnekleri yönü işlevsel ilişkiyle belirler. Bu nedenle sabit bir sağ-sol tanımı dalın özüne konamaz.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir şeyin insana bakan veya en yakın olan yanı"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yayın okçuya bakan yüzü"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"hayvanın biniciye yakın olan yanı"}],"lexicalization_note":"Tanım çıplak dalın insana dönük yan çekirdeğiyle sınırlıdır. Hayvan ve yay uygulamaları bu çekirdeğin örneklenmesidir; yalnız bu kullanımlardan yeni bir genel yön anlamı çıkarılmaz.","neighbor_coverage_note":"Adayların tamamı incelendi. Genel ön taraf, yönelme eylemi ve arka bölümle kurulan karşılaştırmalar insana göre belirlenen yanın sınırını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda yön, insanın nesneyle kurduğu konum veya kullanım ilişkisine bağlıdır. Komşu dalın genel ön ve yakın anlamları bu özel bağı gerektirmez.","focus_only":"Odak dal bir nesnenin insana veya onu kullanan kişiye dönük yanını ilişkiye göre belirler.","gloss":"insana dönük yan ile genel ön taraf","neighbor_only":"Komşu dal genel olarak ön, önde, yakın veya karşıda bulunma yönlerini kişiye bağlı bir kullanım ilişkisi gerektirmeden anlatır.","neighbor_ref":"root_000053/B011","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin bakana göre karşıda veya önde kalan bölümünü gösterebilir."},{"boundary_match":"partial","distinction":"Bir nesnenin insana dönük yanı bir bölüm adıdır; komşu ise dönme veya yönelme olayını anlatır. Sonuç konumu ile o konuma geçiş eylemi birbirinin yerine kullanılamaz.","focus_only":"Odak dal, yönelme tamamlandıktan sonra insana dönük olan sabit yanı adlandırır.","gloss":"dönük yan ile yönelme eylemi","neighbor_only":"Komşu dal yüz, baş, el, kap veya hayvanın bir hedefe doğru dönmesi ve yönelmesi eylemini anlatır.","neighbor_ref":"root_001263/B003","relation_type":"near_neighbor","shared_zone":"İki dal da bir kişi veya hedefe doğru bakma yönünü içerir."},{"boundary_match":"partial","distinction":"Bağlama göre karşıt görünebilseler de odak dal her zaman geometrik ön yüz değildir ve bu yüzden düzenli bir karşıt çift oluşturmaz; belirleyici ölçüt insana yakınlıktır.","focus_only":"Odak dal insana veya kullanıcıya yakın ve ona bakan yanı gösterir.","gloss":"insana bakan yan ile arka taraf","neighbor_only":"Komşu dal bir şeyin arkasında kalan, yüzünün karşıtı olan arka bölümünü gösterir.","neighbor_ref":"root_000458/B001","relation_type":"near_neighbor","shared_zone":"İki dal da bir nesnenin başka bir yöne göre belirlenen bölümünü adlandırır."}],"source_phrase_ar":"الإنسي الأيسر من كل شيء وقيل الأيمن وما أقبل منهما على الإنسان فهو إنسي وإنسي القوس ما أقبل عليك منها (sihah)؛ الإنسي من الدواب الجانب الأيسر الذي منه يركب ويحتلب ومن الإنسان الجانب الذي يلي الرجل الأخرى (tahdhib)؛ إنسي الدابة للجانب الذي يلي الراكب وإنسي القوس للجانب الذي يقبل على الرامي (mufradat)","source_summary":"Ortak anlam, nesnenin insana veya kullanıcıya dönük yanıdır; hayvanda biniciye, yayda okçuya göre belirlenir. İnsan bedenindeki tekil uygulamada öteki bacağa bakan yan kastedilir. Bu yanın solda mı sağda mı bulunduğuna ilişkin anlatımlar ayrıştığı için genel tanım sabit bir yön seçmez.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه إنسي الدابة والقوس وكل شيئين: ما يلي الإنسان أو يقبل على الراكب أو الرامي، في مقابلة الوحشي.","what_is_not_ar":"لا يدخل الإنسان نفسه ولا الأنس النفسي ولا الإبصار."},"support_links":["sup_6097d2a052d527c059e7"]},{"boundary":"Dal göz bebeğinde görülen küçük görüntüyü, ayrıca ayrı bir aktarım olarak parmak ucunu kapsar; gözün kendisini veya genel insan türünü belirtmez.","branch_kind":"bare","branch_ref":"root_000059/B005","candidate_links":[{"candidate_id":"cand_c7a119f0d4388d779979","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:3:2:2","qac_word_ref":"114:3:2","surface_ar":"نَّاسِ"}],"gloss":"göz bebeğinde görülen küçük yansıma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Göz bebeğinin kara bölümünde görülen küçük insan biçimli görüntüyü veya yansımayı adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı bir aktarımda parmak ucu veya eldeki parmak ucunu anlatan kullanım da aynı adla verilir."}}],"root_ar":"ن و س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir bakanın göz bebeğinde beliren küçük insan biçimli görüntü adlandırıldığında dalın ortak ve temel anlamını karşılar.","boundary_detail":"Dal göz bebeğinde görülen küçük görüntüyü, ayrıca ayrı bir aktarım olarak parmak ucunu kapsar; gözün kendisini veya genel insan türünü belirtmez.","branch_image_ar":"إنسان العين وصورة الإنسان في السواد","concept_gloss":"göz bebeğinde görülen küçük yansıma","contextual_glosses":[{"applicability":"Yansımanın insan biçiminde algılanması özellikle belirtilmek istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Görüntünün göz bebeğinde bulunmasını ve küçük insan biçiminde görünmesini korur."},"facet_ids":["F001"],"text":"göz bebeğindeki küçük insan görüntüsü","usage_role":"explanatory"},{"applicability":"Yalnız parmak ucunu aynı adla veren ayrı kaynak kullanımında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Göz anlamından bağımsız olan parmak ucu kullanımını doğrudan korur."},"facet_ids":["F002"],"text":"parmak ucu","usage_role":"contextual"}],"definition":"Gözün kara bölümünde görülen küçük insan biçimli görüntü veya yansımadır. Ayrı bir kaynak kullanımında aynı ad parmak ucuna da verilir, ancak bu kullanım göz görüntüsü çekirdeğini değiştirmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Göz bebeğinin kara bölümünde görülen küçük insan biçimli görüntüyü veya yansımayı adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Ayrı bir aktarımda parmak ucu veya eldeki parmak ucunu anlatan kullanım da aynı adla verilir."}],"identity_rationale":"Kaynak ifadesinin ortak çekirdeği, gözün kara bölümünde görülen küçük insan biçimli görüntü veya yansımadır. Parmak ucu anlamı tek aktarım içinde eklenir ve gözdeki görüntünün kurucu parçası değildir; bağımlı bir kaynak varyantı olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"göz bebeğinde görülen küçük görüntü veya yansıma"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"göz bebeklerinde görülen küçük görüntüler"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"parmak ucu; eldeki parmak ucunu anlatan kullanım"}],"lexicalization_note":"Çıplak dalın çekirdeği gözün kara bölümündeki küçük görüntüdür. Parmak ucu aktarımı bağımlı bir varyanttır; gözle ilgili belirli biçimlerden genel görüntü veya genel insan anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün aday kartlar değerlendirildi. Anatomik göz bebeği, genel tasvir ve göz organı karşılaştırmaları görüntünün yerini ve türünü en iyi sınırladığı için bu üçü yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Komşu anatomik bölümün kendisidir; odak dal ise o bölümde görülen görüntüdür. Taşıyıcı yapı ile üzerinde beliren yansıma birbirinin yerine kullanılamaz.","focus_only":"Odak dal göz bebeğinde görülen küçük insan biçimli görüntüyü veya yansımayı adlandırır.","gloss":"göz bebeği ile göz bebeğindeki yansıma","neighbor_only":"Komşu dal göz bebeğinin kendisini, onun kara bölümünü ve anatomik yapısını adlandırır.","neighbor_ref":"root_000300/B002","relation_type":"same_field","shared_zone":"İki dal aynı göz bölgesine gönderimde bulunur."},{"boundary_match":"partial","distinction":"Odak görüntü göz bebeğindeki belirli yansımadır; komşu ise konum ve oluşum biçimi bakımından çok daha genel tasvirleri kapsar. Her tasvir gözdeki yansıma değildir.","focus_only":"Odak dal yalnız göz bebeğinde beliren küçük insan biçimli görüntüyü ve ayrı bir parmak ucu varyantını kapsar.","gloss":"gözdeki yansıma ile genel tasvir","neighbor_only":"Komşu dal resim, model, heykel veya başka bir varlığa göre biçimlendirilmiş genel örnekleri kapsar.","neighbor_ref":"root_001397/B008","relation_type":"near_neighbor","shared_zone":"Her iki dal başka bir varlığın görünüşünü taşıyan bir görüntüyü anlatabilir."},{"boundary_match":"field_only","distinction":"Göz, görmeyi sağlayan organdır; odak dal ise gözde görülen yansımadır. Organın adı yansımanın, yansımanın adı da organın genel karşılığı değildir.","focus_only":"Odak dal gören gözün içinde beliren küçük görüntüyü adlandırır.","gloss":"göz organı ile içindeki küçük görüntü","neighbor_only":"Komşu dal görme organı olan gözün kendisini ve onun görme işlevini adlandırır.","neighbor_ref":"root_001069/B001","relation_type":"same_field","shared_zone":"Her iki dal göz ve görme alanına aittir."}],"source_phrase_ar":"إنسان العين صبيها الذي في السواد (maqayis)؛ إنسان العين المثال الذي يرى في السواد أي سواد العين (sihah)؛ الإنسان أيضا إنسان العين وجمعه أناسي والإنسان الأنملة (tahdhib)","source_summary":"Ortak aktarım, göz bebeğinin kara bölümünde görülen küçük görüntüyü bir insan biçimi olarak tanımlar. Buna ek olarak parmak ucu anlamı da bildirilir, fakat bu ek kullanım gözdeki yansıma çekirdeğinden ayrı tutulur.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه إنسان العين: المثال أو الصبي الذي يرى في سواد العين، وما ألحقه تهذيب اللغة من الأنملة أو إنسان الكف.","what_is_not_ar":"لا يدخل الإنسان بمعنى البشر عموما ولا الأنس بمعنى الراحة."},"support_links":["sup_b4ff40f5dbbb297b8e4c"]},{"boundary":"Dal yalnız belirtilen söz kuruluşlarında kişinin kendisini veya seçkin yakınını gösterir; genel insan, gerçek evlatlık ve her türlü arkadaşlık anlamına genişletilemez.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B006","candidate_links":[{"candidate_id":"cand_5bf4c39ff45a602d0073","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:3:2:2","qac_word_ref":"114:3:2","surface_ar":"نَّاسِ"}],"gloss":"belirli sözlerde kişinin kendisi veya seçilmiş yakını","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiye kendi durumunu soran belirli kuruluşta muhatabın kendisini gösterir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişiye bağlanarak söylendiğinde onun seçilmiş yakınını, özel arkadaşını veya sırdaşını belirtir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı anlam çevresindeki paralel adlar yakın dostu, içten arkadaşı ve oturup konuşulan kişiyi gösterebilir."}}],"root_ar":"ن و س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kaynakta gösterilen soru ve kişi bağlantısı kuruluşlarını topluca açıklarken kullanılabilir; genel bir kişi ya da akraba adı değildir.","boundary_detail":"Dal yalnız belirtilen söz kuruluşlarında kişinin kendisini veya seçkin yakınını gösterir; genel insan, gerçek evlatlık ve her türlü arkadaşlık anlamına genişletilemez.","branch_image_ar":"ابن الإنس للنفس والصفوة","concept_gloss":"belirli sözlerde kişinin kendisi veya seçilmiş yakını","contextual_glosses":[{"applicability":"Muhataba kendi durumunun nasıl olduğu sorulduğunda doğal Türkçe karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sorunun muhatabın kendi durumuna yönelmesini korur."},"facet_ids":["F001"],"text":"kendin; nasılsın","usage_role":"contextual"},{"applicability":"Bir kişinin seçip özel tuttuğu yakın arkadaş veya sırdaş anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yakın kişinin seçilmiş, özel ve güvenilen biri olmasını korur."},"facet_ids":["F002"],"text":"onun en yakını ve sırdaşı","usage_role":"contextual"},{"applicability":"Yakın dost, içten arkadaş ve birlikte oturup konuşulan kişi için sıralanan paralel adları açıklarken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yakınlık, dostluk ve sürekli görüşme ilişkilerini birlikte korur."},"facet_ids":["F003"],"text":"yakın dostum ve görüşme arkadaşım","usage_role":"explanatory"}],"definition":"Belirli bir soru kuruluşunda muhatabın kendisini ve durumunu, başka bir kişiyle kurulan adlandırmada ise onun seçilmiş yakınını, sırdaşını veya sürekli görüştüğü arkadaşını belirtir. İki kullanım aynı kuruluş ailesinde bulunsa da katılımcı ilişkileri ayrıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiye kendi durumunu soran belirli kuruluşta muhatabın kendisini gösterir."},{"facet_id":"F002","role":"core","statement":"Bir kişiye bağlanarak söylendiğinde onun seçilmiş yakınını, özel arkadaşını veya sırdaşını belirtir."},{"facet_id":"F003","role":"associated_use","statement":"Aynı anlam çevresindeki paralel adlar yakın dostu, içten arkadaşı ve oturup konuşulan kişiyi gösterebilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Gerçek bir baba ile erkek çocuk arasındaki soy ilişkisini ekler.","collision":"Sözün amaçlanan kişi ilişkisini gerçek akrabalıkla karıştırır.","fit":"displacement","loses":"Kişinin kendisini veya seçilmiş yakınını gösteren kalıplaşmış gönderimi kaybeder.","preserves":"Kuruluşun yüzeyindeki çocuk ve soy ilişkisi çağrışımını korur."},"text":"oğlu"}],"identity_rationale":"Kaynak ifadesi iki ayrı kalıplaşmış ilişkiyi açıkça ayırır: kişiye kendi durumunu soran sözde kişinin kendisi, bir başkasına bağlanan sözde ise seçilmiş yakın ve sırdaş kastedilir. Yakın arkadaş ve oturup konuşulan kişi için verilen paralel adlar ikinci alanı destekler.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"kendin; kendi durumun nasıl"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"onun seçkin yakını ve sırdaşı"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"yakınım, içten dostum ve görüşme arkadaşım"}],"lexicalization_note":"Kişinin kendisini soran kuruluş, seçilmiş yakını belirten kuruluş ve yakın arkadaş adları ayrı tutulur. Bunların hiçbiri çıplak biçime genel kişi veya akrabalık anlamı olarak taşınmaz.","neighbor_coverage_note":"Aday kartların tamamı incelendi. Kişinin kendisini gösteren başka kuruluş, iç çevre ve genel dostluk alanları iki ayrı gönderimi en iyi sınırlandırdığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ortak gönderim yalnız benlik anlamındadır; kuruluşlar değiştirilemez. Odak dalın seçilmiş yakın ve sırdaş anlamı komşuda bulunmaz.","focus_only":"Odak dal kişinin kendisini belirli bir soru kuruluşunda gösterir ve ayrıca seçilmiş yakın anlamını da taşır.","gloss":"kişinin kendisini gösteren iki ayrı söz","neighbor_only":"Komşu dal şiirsel bir söyleyişte yalnız kişinin kendi benliğini başka bir kalıpla belirtir.","neighbor_ref":"root_001271/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal belirli bir söz kuruluşunda kişinin kendisine gönderimde bulunur."},{"boundary_match":"partial","distinction":"Odak dal çoğunlukla tek bir yakın veya sırdaşı gösterir; komşu kişinin iç çevresini ve işlerine alınan özel kişileri daha geniş kapsar.","focus_only":"Odak dal seçilmiş yakını ve sırdaşı gösterebilir, fakat kişinin kendisini soran ayrı bir kullanım da içerir.","gloss":"seçilmiş yakın ile iç çevre","neighbor_only":"Komşu dal bir kişinin işine ve sırrına alınan bütün iç çevreyi ve özel kişileri topluluk olarak kapsayabilir.","neighbor_ref":"root_000128/B004","relation_type":"near_neighbor","shared_zone":"Güvenilen ve özel tutulan kişi iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Her dost odak daldaki özel adlandırmanın taşıdığı seçilmiş yakın değildir; odak dalın kişinin kendisine gönderimi de genel dostluk alanının dışındadır.","focus_only":"Odak dal özel kuruluşlarla kişinin kendisini ya da seçilmiş yakınını belirtir.","gloss":"seçilmiş sırdaş ile genel dostluk","neighbor_only":"Komşu dal arkadaşlık ve dostluk ilişkisini açık ya da gizli yönleriyle genel olarak anlatır.","neighbor_ref":"root_000397/B001","relation_type":"near_neighbor","shared_zone":"Seçilmiş yakın kişi aynı zamanda dost veya arkadaş olabilir."}],"source_phrase_ar":"كيف ابن إنسك إذا سأله عن نفسه (maqayis)؛ كيف ابن إنسك يعني نفسه وفلان ابن إنس فلان أي صفيه وخاصته وهذا خدني وإنسي وخلصي وجلسي (sihah)؛ كيف ترى ابن إنسك إذا خاطبت الرجل عن نفسه وفلان ابن أنس فلان أي صفيه وأنيسه (tahdhib)؛ قيل ابن إنسك للنفس (mufradat)","source_summary":"Aktarımlar, doğrudan hitapta kişinin kendi durumunu soran kullanım ile birinin seçkin yakını ve sırdaşını gösteren kullanımı birlikte verir. Yakın dost ve sürekli görüşülen arkadaş anlamındaki paralel adlar ikinci ilişki alanını genişletir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه كيف ابن إنسك للسؤال عن النفس، وفلان ابن أنس فلان لصفيه وخاصته، وما قاربه من الخدن والأنيس والخلص والجليس.","what_is_not_ar":"لا يدخل مطلق الإنسان ولا مطلق المؤانسة إلا إذا جاء بصيغة هذا الباب أو قرينته."},"support_links":["sup_bdd37317ea70daa6c704"]},{"boundary":"Dal eve girmeden önce izin ve kabul arama durumuyla sınırlıdır; genel görme, genel yakınlık, eve yerleşme veya barınma anlamına gelmez.","branch_kind":"unresolved","branch_ref":"root_000059/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:3:2:2","qac_word_ref":"114:3:2","surface_ar":"نَّاسِ"}],"gloss":"girişten önce izin ve kabul arama","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eve girmeden önce selam verip girmek için izin istemeyi ve kabul beklemeyi anlatır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı açıklama, girişten önce içeridekilerden yakınlık ve kabul işareti bulmayı öne çıkarır."}}],"root_ar":"ن و س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir eve girmeden önce selam, izin sorusu veya içeridekilerin kabulünü yoklama yoluyla girişe onay arandığında kullanılır.","boundary_detail":"Dal eve girmeden önce izin ve kabul arama durumuyla sınırlıdır; genel görme, genel yakınlık, eve yerleşme veya barınma anlamına gelmez.","branch_image_ar":"الاستئناس قبل دخول البيوت","concept_gloss":"girişten önce izin ve kabul arama","contextual_glosses":[{"applicability":"Giriş izninin selam ve açık bir izin sorusuyla istendiğini belirten açıklamada uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Selam verme, izin sorma ve girişten önce bekleme işlemlerini korur."},"facet_ids":["F001"],"text":"selam verip girebilir miyim diye sormak","usage_role":"explanatory"},{"applicability":"İçeridekilerin yakınlık ve kabul gösterdiğini anlayarak girişe elverişli ortam bulma yorumunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Girişten önce kabul ve yakınlık işareti bulma yönünü korur."},"facet_ids":["F002"],"text":"girişe açık bir karşılama bulmak","usage_role":"contextual"}],"definition":"Bir eve girmeden önce selam vererek izin istemeyi ve içeridekilerin girişe açık olduğunu anlamayı anlatır. Aktarımın bir yönü doğrudan izin sorusunu, diğer yönü girişe elverişli bir kabul ve yakınlık bulmayı öne çıkarır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eve girmeden önce selam verip girmek için izin istemeyi ve kabul beklemeyi anlatır."},{"facet_id":"F002","role":"source_variant","statement":"Ayrı açıklama, girişten önce içeridekilerden yakınlık ve kabul işareti bulmayı öne çıkarır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yalnız gözle inceleme ve bir şeyi görme anlamını ekler.","collision":"Duyusal fark etme ve çevreye bakıp araştırma dalıyla karışır.","fit":"displacement","loses":"Selam verme, izin isteme ve içeridekilerin kabulünü bekleme koşullarını kaybeder.","preserves":"Girişten önce çevreyi yoklama düşüncesine sınırlı ölçüde yaklaşır."},"text":"bakıp görmek"}],"identity_rationale":"Kaynak ifadesi yalnız eve giriş öncesindeki belirli söz çevresinde açıklanır. Bir aktarım bunu selam verip izin isteme ve girebilir miyim diye sorma olarak, diğeri ise girişe elverişli bir kabul ve yakınlık bulma olarak yorumlar. Dal bu iki açıklamayı korumalı, fakat çıplak biçime genel bakma veya genel rahatlık anlamı yüklememelidir.","lexicalization_note":"Mekanik kapsam çözümlenmemiştir ve eldeki kanıt yalnız giriş öncesi kuruluşu gösterir. Bu nedenle tanım bu söz çevresine bağlanır, çıplak bir genel anlam varsayılmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı. Genel yakınlık, çevreyi gözleme ve barınma senaryosu giriş öncesi izin sınırını en iyi açıkladığı için bu üç ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir giriş davranışı ve onay koşuludur; komşu dal yer ve zamanla sınırlı olmayan duygusal durumdur. Genel yakınlık, giriş izninin yerine geçmez.","focus_only":"Odak dal eve girişten önce selam, izin sorusu ve kabul bekleme yoluyla yürütülen sınırlı bir davranışı anlatır.","gloss":"giriş kabulü ile genel yakınlık duygusu","neighbor_only":"Komşu dal kişi veya şey karşısında genel olarak yabancılık ve ürkme duymayıp yakınlık ve rahatlık hissetmeyi anlatır.","neighbor_ref":"root_000059/B003","relation_type":"near_neighbor","shared_zone":"Kabul gören kişi giriş öncesinde kendini yabancı hissetmeyebilir ve yakınlık işareti bulabilir."},{"boundary_match":"partial","distinction":"Çevreyi gözlemek yalnız bilgi edinir; odak dal içeridekilerden onay almayı amaçlar. Birini görmek veya sesini duymak, tek başına giriş izni değildir.","focus_only":"Odak dal girişten önce selam verip izin ve kabul aramayı gerektirir.","gloss":"izin arama ile çevreyi gözleme","neighbor_only":"Komşu dal görme, işitme, belirti sezme veya çevreye bakarak birini araştırma eylemlerini anlatır.","neighbor_ref":"root_000059/B002","relation_type":"near_neighbor","shared_zone":"Girişten önce içeride birinin bulunup bulunmadığını anlamaya çalışma iki alanı aynı durumda buluşturabilir."},{"boundary_match":"thematic_only","distinction":"Odak dal girişten önceki toplumsal onayı, komşu dal ise bir yere yönelip orada barınmayı anlatır; aralarında sıradan sözcüksel yer değiştirme yoktur.","focus_only":"Odak dal bir eve girmeden önce kabul ve izin arama davranışıdır.","gloss":"eve giriş izni ile barınma","neighbor_only":"Komşu dal bir yere sığınma, yerleşme, barınma veya başkasını barındırma hareketini anlatır.","neighbor_ref":"root_000070/B001","relation_type":"thematic","shared_zone":"İki dal da bir yerle insan arasındaki giriş ve bulunma senaryosunda yer alabilir."}],"source_phrase_ar":"حتى تستأنسوا معناه حتى تستأذنوا وإنما هو حتى تسلموا وتستأنسوا السلام عليكم أأدخل (tahdhib)؛ حتى تستأنسوا أي تجدوا إيناسا (mufradat)","source_summary":"Giriş öncesi davranış iki yönden açıklanır: selam verip açıkça izin istemek ve girebilir miyim diye sormak ya da içeridekilerden girişe elverişli bir kabul ve yakınlık bulmak. Her iki açıklama da eve izinsiz girmeme sınırında birleşir.","sources":["TA","MU"],"what_is_ar":"يدخل فيه تفسير حتى تستأنسوا بالاستئذان أو السلام وطلب الدخول، أو بإيجاد إيناس قبل الدخول.","what_is_not_ar":"لا يدخل مطلق الإبصار أو مطلق الأنس إلا في صيغة الدخول المذكورة."},"support_links":[]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000266/B005","candidate_links":[{"candidate_id":"cand_b373ab74fe22aebd264e","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_2c9fe5dda172552add04","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Hidden beings supply one concealed origin of the invasive prompting.","root":"ج ن ن","source_ref":"114:6","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000266","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_2f91a8a3542485f8254c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000266/B013","candidate_links":[{"candidate_id":"cand_a25c69ed47788b211120","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_22c40f7000cc77e7f131","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The dark mass or crowd of people supplies collective density as a form of concealment.","root":"ج ن ن","source_ref":"114:6","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000266","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_d85d3cf24e0877bb451e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000443/B001","candidate_links":[{"candidate_id":"cand_22c353ec36fe10a32fd9","lane":"macro"},{"candidate_id":"cand_6e9f963d0aa0deae57fb","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_4252c90d91602b7fcae2","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Retreat into concealment makes the hostile presence intermittent rather than abiding.","root":"خ ن س","source_ref":"114:4","source_word_indices":["4"]},{"hft_ref":"hft_8985d1bb6766c23840a8","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Withdrawal into concealment lets the proposal evade inspection after it is planted.","root":"خ ن س","source_ref":"114:4","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000443","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6f7fc1ca0bc4eae9000a","sup_e908d372714a107278e4"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000443/B002","candidate_links":[{"candidate_id":"cand_89203cf9b82735660002","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_0ee69de0f686a6f12207","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Stars that disappear and return supply a recurring visibility cycle.","root":"خ ن س","source_ref":"114:4","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000443","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_c84d65e31f3be5dc8853"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000443/B005","candidate_links":[{"candidate_id":"cand_da624628bd350ede26c4","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_d26143759611c07fa903","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A horse veering during its run supplies lateral deflection without stopping forward motion.","root":"خ ن س","source_ref":"114:4","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000443","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6097d2a052d527c059e7"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000532/B002","candidate_links":[{"candidate_id":"cand_a141ebc9607e343bf58b","lane":"macro"},{"candidate_id":"cand_fed3de197eb82ee15a4e","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_caa02b0d9ed3ab776ba0","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Repair, nurture, and completion make refuge an active process of restoring the speaker.","root":"ر ب ب","source_ref":"114:1","source_word_indices":["3"]},{"hft_ref":"hft_e52bc292f99aef8a18ab","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Nurture, repair, and completion supply the formative first relation.","root":"ر ب ب","source_ref":"114:1","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000532","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_02e169fe0d3adf6d330d","sup_15654188a4a968fdf517"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000787/B003","candidate_links":[{"candidate_id":"cand_89203cf9b82735660002","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_0ee69de0f686a6f12207","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Scattered fire-sparks supply brief, attention-catching bursts.","root":"ش ر ر","source_ref":"114:4","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000787","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_c84d65e31f3be5dc8853"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000792/B001","candidate_links":[{"candidate_id":"cand_6e9f963d0aa0deae57fb","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_8985d1bb6766c23840a8","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Exchange between buying and selling supplies the transactional mechanism.","root":"ش ر ر","source_ref":"114:4","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000792","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_e908d372714a107278e4"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000792/B002","candidate_links":[{"candidate_id":"cand_6e9f963d0aa0deae57fb","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_8985d1bb6766c23840a8","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Equivalence and comparison supply the whispered claim that a substitute has matching value.","root":"ش ر ر","source_ref":"114:4","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000792","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_e908d372714a107278e4"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000849/B004","candidate_links":[{"candidate_id":"cand_5bf4c39ff45a602d0073","lane":"macro"},{"candidate_id":"cand_c7a119f0d4388d779979","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_8f9dd8257c4bad7f8403","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The origin from which actions issue supplies the causal location of the contest.","root":"ص د ر","source_ref":"114:5","source_word_indices":["4"]},{"hft_ref":"hft_dbe4955d533b7fa7d938","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The source from which actions issue connects altered self-perception to later conduct.","root":"ص د ر","source_ref":"114:5","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000849","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b4ff40f5dbbb297b8e4c","sup_bdd37317ea70daa6c704"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001059/B001","candidate_links":[{"candidate_id":"cand_a141ebc9607e343bf58b","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_caa02b0d9ed3ab776ba0","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Seeking shelter and holding fast supplies the protective action performed by the utterance.","root":"ع و ذ","source_ref":"114:1","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001059","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_02e169fe0d3adf6d330d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001059/B004","candidate_links":[{"candidate_id":"cand_22c353ec36fe10a32fd9","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_4252c90d91602b7fcae2","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Adhering and remaining within a shelter gives protective nearness temporal persistence.","root":"ع و ذ","source_ref":"114:1","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001059","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6f7fc1ca0bc4eae9000a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001272/B001","candidate_links":[{"candidate_id":"cand_a141ebc9607e343bf58b","lane":"macro"},{"candidate_id":"cand_4d3159f860f3a9da97c8","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_caa02b0d9ed3ab776ba0","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Bringing speech out in pronunciation makes the surrounding construction a performed utterance.","root":"ق و ل","source_ref":"114:1","source_word_indices":["1"]},{"hft_ref":"hft_196c33721bb1a686c585","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Pronounced saying supplies the overt and accountable speech channel.","root":"ق و ل","source_ref":"114:1","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001272","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_02e169fe0d3adf6d330d","sup_1bda9c12faa6759bb714"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001272/B012","candidate_links":[{"candidate_id":"cand_4d3159f860f3a9da97c8","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_196c33721bb1a686c585","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Unmanifested saying within the self shows that qawl can also occupy an inner channel.","root":"ق و ل","source_ref":"114:1","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001272","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_1bda9c12faa6759bb714"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001444/B001","candidate_links":[{"candidate_id":"cand_b7fa44c03435d65f2171","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_862692e882a8cbb59b34","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Strength and cohesion supply the social effect attributed to shared orientation.","root":"م ل ك","source_ref":"114:2","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001444","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_bfc8c4e17918a87aaa4c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001444/B002","candidate_links":[{"candidate_id":"cand_fed3de197eb82ee15a4e","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_e52bc292f99aef8a18ab","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Possession and power of disposition supply the governing middle relation.","root":"م ل ك","source_ref":"114:2","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001444","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_15654188a4a968fdf517"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001444/B005","candidate_links":[{"candidate_id":"cand_fed3de197eb82ee15a4e","lane":"macro"},{"candidate_id":"cand_b7fa44c03435d65f2171","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_e52bc292f99aef8a18ab","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The mainstay of an affair makes kingship the structural pivot between nurture and worship.","root":"م ل ك","source_ref":"114:2","source_word_indices":["1"]},{"hft_ref":"hft_862692e882a8cbb59b34","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A mainstay supplies the image of worship as the collective's organizing support.","root":"م ل ك","source_ref":"114:2","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001444","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_15654188a4a968fdf517","sup_bfc8c4e17918a87aaa4c"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001444/B006","candidate_links":[{"candidate_id":"cand_da624628bd350ede26c4","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_d26143759611c07fa903","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Owning a road or valley supplies the image of a course lying within ordered jurisdiction.","root":"م ل ك","source_ref":"114:2","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001444","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_6097d2a052d527c059e7"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001651/B001","candidate_links":[{"candidate_id":"cand_22c353ec36fe10a32fd9","lane":"macro"},{"candidate_id":"cand_6e9f963d0aa0deae57fb","lane":"macro"},{"candidate_id":"cand_5bf4c39ff45a602d0073","lane":"macro"},{"candidate_id":"cand_4d3159f860f3a9da97c8","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_4252c90d91602b7fcae2","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Hidden self-talk supplies the intimate but hostile voice against which companionship operates.","root":"و س و س","source_ref":"114:4","source_word_indices":["3"]},{"hft_ref":"hft_8985d1bb6766c23840a8","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Hidden self-talk locates the bargaining process inside apparently private thought.","root":"و س و س","source_ref":"114:4","source_word_indices":["3"]},{"hft_ref":"hft_8f9dd8257c4bad7f8403","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Hidden self-talk supplies the covert input introduced before action becomes visible.","root":"و س و س","source_ref":"114:5","source_word_indices":["2"]},{"hft_ref":"hft_196c33721bb1a686c585","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Hidden self-talk supplies the covert channel that can masquerade as one's own thought.","root":"و س و س","source_ref":"114:5","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001651","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_1bda9c12faa6759bb714","sup_6f7fc1ca0bc4eae9000a","sup_bdd37317ea70daa6c704","sup_e908d372714a107278e4"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001651/B002","candidate_links":[{"candidate_id":"cand_89203cf9b82735660002","lane":"macro"},{"candidate_id":"cand_c7a119f0d4388d779979","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_0ee69de0f686a6f12207","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A hidden low sound supplies a stimulus near the threshold of hearing.","root":"و س و س","source_ref":"114:4","source_word_indices":["3"]},{"hft_ref":"hft_dbe4955d533b7fa7d938","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A hidden sound adds a barely perceived signal that can alter the inward image.","root":"و س و س","source_ref":"114:4","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001651","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b4ff40f5dbbb297b8e4c","sup_c84d65e31f3be5dc8853"]}],"candidate_inventory":[{"anchor_refs":["114:1","114:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"114:3","branch_refs":["root_000047/B001","root_000532/B002","root_001059/B001","root_001272/B001"],"candidate_id":"cand_a141ebc9607e343bf58b","commentary_obligation":"review","hft_ref":"hft_caa02b0d9ed3ab776ba0","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_performed_refuge","source_type":"hft","support_ids":["sup_02e169fe0d3adf6d330d"],"title":"d_performed_refuge","trust":"legacy_unbound"},{"anchor_refs":["114:1","114:2","114:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"114:3","branch_refs":["root_000047/B001","root_000532/B002","root_001444/B002","root_001444/B005"],"candidate_id":"cand_fed3de197eb82ee15a4e","commentary_obligation":"review","hft_ref":"hft_e52bc292f99aef8a18ab","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_title_progression","source_type":"hft","support_ids":["sup_15654188a4a968fdf517"],"title":"d_title_progression","trust":"legacy_unbound"},{"anchor_refs":["114:2","114:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"114:3","branch_refs":["root_000047/B001","root_000059/B001","root_001444/B001","root_001444/B005"],"candidate_id":"cand_b7fa44c03435d65f2171","commentary_obligation":"review","hft_ref":"hft_862692e882a8cbb59b34","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_collective_cohesion","source_type":"hft","support_ids":["sup_bfc8c4e17918a87aaa4c"],"title":"d_collective_cohesion","trust":"legacy_unbound"},{"anchor_refs":["114:1","114:3","114:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"114:3","branch_refs":["root_000047/B001","root_000059/B003","root_000443/B001","root_001059/B004","root_001651/B001"],"candidate_id":"cand_22c353ec36fe10a32fd9","commentary_obligation":"review","hft_ref":"hft_4252c90d91602b7fcae2","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_abiding_companionship","source_type":"hft","support_ids":["sup_6f7fc1ca0bc4eae9000a"],"title":"d_abiding_companionship","trust":"legacy_unbound"},{"anchor_refs":["114:3","114:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"114:3","branch_refs":["root_000047/B001","root_000059/B002","root_000443/B002","root_000787/B003","root_001651/B002"],"candidate_id":"cand_89203cf9b82735660002","commentary_obligation":"review","hft_ref":"hft_0ee69de0f686a6f12207","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_intermitent_attention","source_type":"hft","support_ids":["sup_c84d65e31f3be5dc8853"],"title":"d_intermitent_attention","trust":"legacy_unbound"},{"anchor_refs":["114:3","114:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"114:3","branch_refs":["root_000047/B001","root_000443/B001","root_000792/B001","root_000792/B002","root_001651/B001"],"candidate_id":"cand_6e9f963d0aa0deae57fb","commentary_obligation":"review","hft_ref":"hft_8985d1bb6766c23840a8","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_covert_exchange","source_type":"hft","support_ids":["sup_e908d372714a107278e4"],"title":"d_covert_exchange","trust":"legacy_unbound"},{"anchor_refs":["114:3","114:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"114:3","branch_refs":["root_000047/B001","root_000059/B006","root_000849/B004","root_001651/B001"],"candidate_id":"cand_5bf4c39ff45a602d0073","commentary_obligation":"review","hft_ref":"hft_8f9dd8257c4bad7f8403","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_action_source","source_type":"hft","support_ids":["sup_bdd37317ea70daa6c704"],"title":"d_action_source","trust":"legacy_unbound"},{"anchor_refs":["114:1","114:3","114:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"114:3","branch_refs":["root_000047/B001","root_001272/B001","root_001272/B012","root_001651/B001"],"candidate_id":"cand_4d3159f860f3a9da97c8","commentary_obligation":"review","hft_ref":"hft_196c33721bb1a686c585","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_speech_channels","source_type":"hft","support_ids":["sup_1bda9c12faa6759bb714"],"title":"d_speech_channels","trust":"legacy_unbound"},{"anchor_refs":["114:3","114:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"114:3","branch_refs":["root_000047/B001","root_000059/B001","root_000266/B005"],"candidate_id":"cand_b373ab74fe22aebd264e","commentary_obligation":"review","hft_ref":"hft_2c9fe5dda172552add04","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:d_porous_human_network","source_type":"hft","support_ids":["sup_2f91a8a3542485f8254c"],"title":"d_porous_human_network","trust":"legacy_unbound"},{"anchor_refs":["114:3","114:4","114:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"114:3","branch_refs":["root_000047/B001","root_000059/B005","root_000849/B004","root_001651/B002"],"candidate_id":"cand_c7a119f0d4388d779979","commentary_obligation":"review","hft_ref":"hft_dbe4955d533b7fa7d938","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:o_pupil_interface","source_type":"hft","support_ids":["sup_b4ff40f5dbbb297b8e4c"],"title":"o_pupil_interface","trust":"legacy_unbound"},{"anchor_refs":["114:3","114:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"114:3","branch_refs":["root_000047/B001","root_000059/B001","root_000266/B013"],"candidate_id":"cand_a25c69ed47788b211120","commentary_obligation":"review","hft_ref":"hft_22c40f7000cc77e7f131","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:o_crowd_opacity","source_type":"hft","support_ids":["sup_d85d3cf24e0877bb451e"],"title":"o_crowd_opacity","trust":"legacy_unbound"},{"anchor_refs":["114:2","114:3","114:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"114:3","branch_refs":["root_000047/B001","root_000059/B004","root_000443/B005","root_001444/B006"],"candidate_id":"cand_da624628bd350ede26c4","commentary_obligation":"review","hft_ref":"hft_d26143759611c07fa903","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:o_route_deviation","source_type":"hft","support_ids":["sup_6097d2a052d527c059e7"],"title":"o_route_deviation","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_725c2b3d089047aad25d","connection_ref":"conn_c71530a38c76c01c57bd","note":"Immediate companion title: Malik of al-nas frames the preceding step before Ilah of al-nas.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_4f98406122e30420796a","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"114:2","source_note":"Same الناس triad; weak f02/f05 route adds a neighboring title only.","source_row_role":"ranked_review","source_target_component_ref":"114:3","source_target_components":["114:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"114:3"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"114:2","source_target_components":["114:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"114:2","target_evidence":{"arabic_uthmani":"مَلِكِ ٱلنَّاسِ","ayah_ref":"114:2"},"target_ref":"114:2"},{"connection_evidence_ref":"conn_ev_827dff451b35ecf6f33c","connection_ref":"conn_5d53bb834969ccd3318f","note":"Directly identifies human as a possible whisper-source, preserving f04.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_99cd936f1342796c54aa","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"114:6","source_note":"Immediate context fixes the addressed human community under divine authority.","source_row_role":"ranked_review","source_target_component_ref":"114:3","source_target_components":["114:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"114:3"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"114:6","source_target_components":["114:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"114:6","target_evidence":{"arabic_uthmani":"مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ","ayah_ref":"114:6"},"target_ref":"114:6"},{"connection_evidence_ref":"conn_ev_8e33cc39fcac5907d77d","connection_ref":"conn_a4c9d75d329a950f8dab","note":"Immediate opening title, Rabb of al-nas, establishes the first member of the focal sequence.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_8b37d83a8908f22ecc79","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"114:1","source_note":"Yakın bağlamdaki üçüncü unvan, insan kaynaklı baskı ihtimalini paralel tutar.","source_row_role":"ranked_review","source_target_component_ref":"114:3","source_target_components":["114:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"114:3"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"114:1","source_target_components":["114:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"114:1","target_evidence":{"arabic_uthmani":"قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ","ayah_ref":"114:1"},"target_ref":"114:1"},{"connection_evidence_ref":"conn_ev_1a74184f23bb5cf86573","connection_ref":"conn_132c5810aa8a8367f694","note":"Directly places whispering in sudur al-nas and supports human transmission in f04.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_76de52281323c7800e20","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"114:5","source_note":"Nearby al-nas title only; little mechanism.","source_row_role":"ranked_review","source_target_component_ref":"114:3","source_target_components":["114:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"114:3"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"114:5","source_target_components":["114:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"114:5","target_evidence":{"arabic_uthmani":"ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ","ayah_ref":"114:5"},"target_ref":"114:5"},{"connection_ref":"conn_d433fd222a28894eee49","note":null,"origin":"derived_reciprocal_seed","prior_label":null,"qualification":{"boundary":"At least one source-direction review meaningfully linked this target back to the focus ayah. Treat its note and label only as a discovery nomination. Reassess the relation from the focus ayah using the supplied exact target Arabic; do not invent missing target morphology or inherit the source label.","derived_reciprocal_counterevidence":false,"derived_reciprocal_seed":true,"has_missing_ayah_suggestion_source_row":true,"has_ranked_review_source_row":false,"has_reciprocal_counterevidence":false,"has_reciprocal_nomination":true,"receiving_direction_requires_fresh_assessment":true,"source_direction_labels_are_not_focus_decisions":true,"source_row_roles_are_provenance_not_decisions":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_c6042ac8bb7b122db8e8","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"114:4","source_note":"Immediate title of the protector completes the refuge frame before the focus.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"114:3","source_target_components":["114:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"114:3"}],"relation_scope":"declared_pericope_reciprocal_evidence","target_evidence":{"arabic_uthmani":"مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ","ayah_ref":"114:4"},"target_ref":"114:4"}],"focus":{"arabic_uthmani":"إِلَٰهِ ٱلنَّاسِ","qac_morphemes":[{"lemma_ar":"إِلَٰه","morph_features":"STEM|POS:N|LEM:<ila`h|ROOT:Alh|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:3:1:1","qac_word_ref":"114:3:1","root_ar":"ء ل ه","surface_ar":"إِلَٰهِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"114:3:2:1","qac_word_ref":"114:3:2","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:3:2:2","qac_word_ref":"114:3:2","root_ar":"ن و س","surface_ar":"نَّاسِ"}],"word_analysis_qac_refs":[["114:3:1:1"],["114:3:2:1","114:3:2:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["114:3:1","114:3:2"]},"focus_surface_evidence":{"arabic_uthmani":"إِلَٰهِ ٱلنَّاسِ","qac_morphemes":[{"lemma_ar":"إِلَٰه","morph_features":"STEM|POS:N|LEM:<ila`h|ROOT:Alh|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:3:1:1","qac_word_ref":"114:3:1","root_ar":"ء ل ه","surface_ar":"إِلَٰهِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"114:3:2:1","qac_word_ref":"114:3:2","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"نَّاس","morph_features":"STEM|POS:N|LEM:n~aAs|ROOT:nws|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"114:3:2:2","qac_word_ref":"114:3:2","root_ar":"ن و س","surface_ar":"نَّاسِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["114:3:1:1"],["114:3:2:1","114:3:2:2"]],"word_analysis_refs":["114:3:1","114:3:2"],"word_rows":[{"analysis_record_ref":"114:3:1","analytic_gloss_range_en":"deity or object of worship, here locally bound as the final construct title in the refuge sequence","analytic_root_gloss_range_en":"worship, deifying, bewildered turning, shelter-seeking, and attachment images; the local noun selects the deity-title while allowing refuge-pressure to remain audible","qac_refs":["114:3:1:1"],"root":{"arabic":"أ ل ه","transliteration":"ʾ-l-h"},"surface":{"arabic":"إِلَٰهِ","transliteration":"ilāhi"}},{"analysis_record_ref":"114:3:2","analytic_gloss_range_en":"the people, human beings, the human collective; here the definite genitive complement to the deity-title","analytic_root_gloss_range_en":"human sociality, familiarity, perceptibility, and collective peoplehood; forgetfulness remains a disputed etymological pressure rather than the selected local derivation","qac_refs":["114:3:2:1","114:3:2:2"],"root":{"arabic":"أ ن س","transliteration":"ʾ-n-s"},"surface":{"arabic":"ٱلنَّاسِ","transliteration":"al-nāsi"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":2,"words_total":2,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":6,"missing_anchor_refs":[],"supplied_unique_anchor_count":6},"assigned_record_count":12,"assigned_records":[{"anchor_refs":["114:1","114:3"],"branch_refs":["root_000047/B001","root_000532/B002","root_001059/B001","root_001272/B001"],"candidate_id":"cand_a141ebc9607e343bf58b","evidence_scope":"declared_pericope","hft_ref":"hft_caa02b0d9ed3ab776ba0","item_id":"d_performed_refuge","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_performed_refuge","support_id":"sup_02e169fe0d3adf6d330d"},{"anchor_refs":["114:1","114:2","114:3"],"branch_refs":["root_000047/B001","root_000532/B002","root_001444/B002","root_001444/B005"],"candidate_id":"cand_fed3de197eb82ee15a4e","evidence_scope":"declared_pericope","hft_ref":"hft_e52bc292f99aef8a18ab","item_id":"d_title_progression","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_title_progression","support_id":"sup_15654188a4a968fdf517"},{"anchor_refs":["114:2","114:3"],"branch_refs":["root_000047/B001","root_000059/B001","root_001444/B001","root_001444/B005"],"candidate_id":"cand_b7fa44c03435d65f2171","evidence_scope":"declared_pericope","hft_ref":"hft_862692e882a8cbb59b34","item_id":"d_collective_cohesion","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_collective_cohesion","support_id":"sup_bfc8c4e17918a87aaa4c"},{"anchor_refs":["114:1","114:3","114:4"],"branch_refs":["root_000047/B001","root_000059/B003","root_000443/B001","root_001059/B004","root_001651/B001"],"candidate_id":"cand_22c353ec36fe10a32fd9","evidence_scope":"declared_pericope","hft_ref":"hft_4252c90d91602b7fcae2","item_id":"d_abiding_companionship","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_abiding_companionship","support_id":"sup_6f7fc1ca0bc4eae9000a"},{"anchor_refs":["114:3","114:4"],"branch_refs":["root_000047/B001","root_000059/B002","root_000443/B002","root_000787/B003","root_001651/B002"],"candidate_id":"cand_89203cf9b82735660002","evidence_scope":"declared_pericope","hft_ref":"hft_0ee69de0f686a6f12207","item_id":"d_intermitent_attention","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_intermitent_attention","support_id":"sup_c84d65e31f3be5dc8853"},{"anchor_refs":["114:3","114:4"],"branch_refs":["root_000047/B001","root_000443/B001","root_000792/B001","root_000792/B002","root_001651/B001"],"candidate_id":"cand_6e9f963d0aa0deae57fb","evidence_scope":"declared_pericope","hft_ref":"hft_8985d1bb6766c23840a8","item_id":"d_covert_exchange","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_covert_exchange","support_id":"sup_e908d372714a107278e4"},{"anchor_refs":["114:3","114:5"],"branch_refs":["root_000047/B001","root_000059/B006","root_000849/B004","root_001651/B001"],"candidate_id":"cand_5bf4c39ff45a602d0073","evidence_scope":"declared_pericope","hft_ref":"hft_8f9dd8257c4bad7f8403","item_id":"d_action_source","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_action_source","support_id":"sup_bdd37317ea70daa6c704"},{"anchor_refs":["114:1","114:3","114:5"],"branch_refs":["root_000047/B001","root_001272/B001","root_001272/B012","root_001651/B001"],"candidate_id":"cand_4d3159f860f3a9da97c8","evidence_scope":"declared_pericope","hft_ref":"hft_196c33721bb1a686c585","item_id":"d_speech_channels","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_speech_channels","support_id":"sup_1bda9c12faa6759bb714"},{"anchor_refs":["114:3","114:6"],"branch_refs":["root_000047/B001","root_000059/B001","root_000266/B005"],"candidate_id":"cand_b373ab74fe22aebd264e","evidence_scope":"declared_pericope","hft_ref":"hft_2c9fe5dda172552add04","item_id":"d_porous_human_network","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:d_porous_human_network","support_id":"sup_2f91a8a3542485f8254c"},{"anchor_refs":["114:3","114:4","114:5"],"branch_refs":["root_000047/B001","root_000059/B005","root_000849/B004","root_001651/B002"],"candidate_id":"cand_c7a119f0d4388d779979","evidence_scope":"declared_pericope","hft_ref":"hft_dbe4955d533b7fa7d938","item_id":"o_pupil_interface","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:o_pupil_interface","support_id":"sup_b4ff40f5dbbb297b8e4c"},{"anchor_refs":["114:3","114:6"],"branch_refs":["root_000047/B001","root_000059/B001","root_000266/B013"],"candidate_id":"cand_a25c69ed47788b211120","evidence_scope":"declared_pericope","hft_ref":"hft_22c40f7000cc77e7f131","item_id":"o_crowd_opacity","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:o_crowd_opacity","support_id":"sup_d85d3cf24e0877bb451e"},{"anchor_refs":["114:2","114:3","114:4"],"branch_refs":["root_000047/B001","root_000059/B004","root_000443/B005","root_001444/B006"],"candidate_id":"cand_da624628bd350ede26c4","evidence_scope":"declared_pericope","hft_ref":"hft_d26143759611c07fa903","item_id":"o_route_deviation","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:o_route_deviation","support_id":"sup_6097d2a052d527c059e7"}],"diagnostics":[],"lane_counts":{"global":10,"macro":12,"micro":3},"packet_summary":{"ayah_count":6,"focus_ref":"114:3","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ش ر ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000787","furuq_root_norm":"ش ر ر","furuq_source_root_norm":"ش ر ر","is_dominant":true,"target_occurrences":19,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000792","furuq_root_norm":"ش ر ي","furuq_source_root_norm":"ش ر ي","is_dominant":false,"target_occurrences":11,"target_rank":2}]}],"window":["114:1","114:2","114:3","114:4","114:5","114:6"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"114:3","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"114:3","lane":"macro","linguistic_source_ref":"114:3","surface_ref":"114:3","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"114:3","target_tokens":[["İnsanların",["114:3:2"]],["ilahına",["114:3:1"]]],"text":"İnsanların ilahına."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":12,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":1,"ayah_to":6,"id":"s114-p01-001-006","label":"Whole surah","number":1,"refs":["114:1","114:2","114:3","114:4","114:5","114:6"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"114:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"114:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["114:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"114:0"},{"ayah_ref":"114:1","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"114:1","root_occurrences":[{"lemmas_ar":["قَالَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ق و ل","surfaces_ar":["قُلْ"],"word_indices":["1"]},{"lemmas_ar":["عُذْ"],"occurrence_count":1,"pos_tags":["V"],"root":"ع و ذ","surfaces_ar":["أَعُوذُ"],"word_indices":["2"]},{"lemmas_ar":["رَبّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ر ب ب","surfaces_ar":["رَبِّ"],"word_indices":["3"]},{"lemmas_ar":["نَّاس"],"occurrence_count":1,"pos_tags":["N"],"root":"ن و س","surfaces_ar":["نَّاسِ"],"word_indices":["4"]}],"root_sequence":["ق و ل","ع و ذ","ر ب ب","ن و س"],"text_ar":"قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ"}],"context_order":["114:1"],"context_root_cues":[{"root":"ق و ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"إخراج القول بالنطق"},{"branch_id":"B002","branch_image_ar":"اللسان آلة القول"},{"branch_id":"B003","branch_image_ar":"كثرة القول في صاحبه"},{"branch_id":"B004","branch_image_ar":"القيل صاحب القول النافذ"},{"branch_id":"B005","branch_image_ar":"قول ما لم يكن أو نسبته"},{"branch_id":"B006","branch_image_ar":"اجترار القول إلى النفس"},{"branch_id":"B007","branch_image_ar":"القول الفاشي بين الناس"},{"branch_id":"B008","branch_image_ar":"عود القال لضرب القلة"},{"branch_id":"B009","branch_image_ar":"المقاولة في الأمر"},{"branch_id":"B010","branch_image_ar":"اقتالة الحكم على غيره"},{"branch_id":"B011","branch_image_ar":"قول يجري مجرى الظن"},{"branch_id":"B012","branch_image_ar":"قول في النفس لم يظهر"},{"branch_id":"B013","branch_image_ar":"القول اعتقاد ومذهب"},{"branch_id":"B014","branch_image_ar":"قول الشيء دلالته"},{"branch_id":"B015","branch_image_ar":"العناية الصادقة بالشيء"},{"branch_id":"B016","branch_image_ar":"قول الشيء حده"}],"mapped_root_id":"root_001272","mapped_root_norm":"ق و ل"},{"branches":[{"branch_id":"B001","branch_image_ar":"القِلَّة والضآلة"},{"branch_id":"B002","branch_image_ar":"قُلَّة الشيء ورأسه"},{"branch_id":"B003","branch_image_ar":"القُلَّة الجرة الكبيرة"},{"branch_id":"B004","branch_image_ar":"الإقلال والاستقلال حملا ونهوضا"},{"branch_id":"B005","branch_image_ar":"القِلُّ رعدة واضطراب"},{"branch_id":"B006","branch_image_ar":"القلقلة اضطراب وتحرك"}],"mapped_root_id":"root_001251","mapped_root_norm":"ق ل ل"}]},{"root":"ع و ذ","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الالتجاء والاعتصام"},{"branch_id":"B002","branch_image_ar":"الوقاية بعوذة أو تعويذ"},{"branch_id":"B003","branch_image_ar":"الأنثى العائذ بعد الولادة"},{"branch_id":"B004","branch_image_ar":"اللصوق والملازمة في كنف شيء"},{"branch_id":"B005","branch_image_ar":"معوذ الفرس في موضع القلادة"},{"branch_id":"B006","branch_image_ar":"الإفلات عوذا بتخويف دون تمام الفعل"},{"branch_id":"B007","branch_image_ar":"تعاوذ القوم في الحرب وتواكلوا"},{"branch_id":"B008","branch_image_ar":"التحامي كراهة من الشيء"}],"mapped_root_id":"root_001059","mapped_root_norm":"ع و ذ"}]},{"root":"ر ب ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ربوبية وملك وسيادة"},{"branch_id":"B002","branch_image_ar":"إصلاح وتربية وإتمام"},{"branch_id":"B003","branch_image_ar":"علم رباني"},{"branch_id":"B004","branch_image_ar":"ربة وجماعات كثيرة"},{"branch_id":"B005","branch_image_ar":"ربيب وربيبة ورابة"},{"branch_id":"B006","branch_image_ar":"رُبّ خاثر وإصلاح به"},{"branch_id":"B007","branch_image_ar":"لزوم وإقامة ودوام"},{"branch_id":"B008","branch_image_ar":"رباب السحاب"},{"branch_id":"B009","branch_image_ar":"شاة رُبّى وحداثة"},{"branch_id":"B010","branch_image_ar":"ربابة تجمع القداح"},{"branch_id":"B011","branch_image_ar":"ربابة عهد وميثاق"},{"branch_id":"B012","branch_image_ar":"ربة نبات"},{"branch_id":"B013","branch_image_ar":"ماء رَبَب كثير"},{"branch_id":"B014","branch_image_ar":"رَبْرَب قطيع"},{"branch_id":"B015","branch_image_ar":"حرف رب وربما"},{"branch_id":"B016","branch_image_ar":"رُبَى حاجة وعقدة ونعمة"},{"branch_id":"B017","branch_image_ar":"رباني الملاحين"}],"mapped_root_id":"root_000532","mapped_root_norm":"ر ب ب"},{"branches":[{"branch_id":"B001","branch_image_ar":"زيادة وعلو"},{"branch_id":"B002","branch_image_ar":"أرض مرتفعة"},{"branch_id":"B003","branch_image_ar":"زيادة الربا في المعاملة"},{"branch_id":"B004","branch_image_ar":"تصعد النفس وانتفاخه"},{"branch_id":"B005","branch_image_ar":"تغذية ونشوء"},{"branch_id":"B006","branch_image_ar":"نتوء أصل الفخذ"},{"branch_id":"B007","branch_image_ar":"أهل البيت من بني الأعمام"}],"mapped_root_id":"root_000537","mapped_root_norm":"ر ب و"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"114:1","surface_ref":"114:1"},{"ayah_ref":"114:2","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"114:2","root_occurrences":[{"lemmas_ar":["مَلِك"],"occurrence_count":1,"pos_tags":["N"],"root":"م ل ك","surfaces_ar":["مَلِكِ"],"word_indices":["1"]},{"lemmas_ar":["نَّاس"],"occurrence_count":1,"pos_tags":["N"],"root":"ن و س","surfaces_ar":["نَّاسِ"],"word_indices":["2"]}],"root_sequence":["م ل ك","ن و س"],"text_ar":"مَلِكِ ٱلنَّاسِ"}],"context_order":["114:2"],"context_root_cues":[{"root":"م ل ك","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"قوة الشيء وتماسكه"},{"branch_id":"B002","branch_image_ar":"المِلْك والتصرف"},{"branch_id":"B003","branch_image_ar":"المُلك والسلطان"},{"branch_id":"B004","branch_image_ar":"الإملاك والتزويج"},{"branch_id":"B005","branch_image_ar":"مِلاك الأمر وعِماده"},{"branch_id":"B006","branch_image_ar":"مَلَك الطريق والوادي"},{"branch_id":"B007","branch_image_ar":"الماء مَلَك الأمر"},{"branch_id":"B008","branch_image_ar":"المتقدم القائد في الحيوان"}],"mapped_root_id":"root_001444","mapped_root_norm":"م ل ك"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"114:2","surface_ref":"114:2"},{"ayah_ref":"114:4","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"114:4","root_occurrences":[{"lemmas_ar":["شَرّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ش ر ر","surfaces_ar":["شَرِّ"],"word_indices":["2"]},{"lemmas_ar":["وَسْوَاس"],"occurrence_count":1,"pos_tags":["N"],"root":"و س و س","surfaces_ar":["وَسْوَاسِ"],"word_indices":["3"]},{"lemmas_ar":["خَنَّاس"],"occurrence_count":1,"pos_tags":["ADJ"],"root":"خ ن س","surfaces_ar":["خَنَّاسِ"],"word_indices":["4"]}],"root_sequence":["ش ر ر","و س و س","خ ن س"],"text_ar":"مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ"}],"context_order":["114:4"],"context_root_cues":[{"root":"ش ر ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الشَّرّ والسوء"},{"branch_id":"B002","branch_image_ar":"نشر الشيء في الشمس ليجف"},{"branch_id":"B003","branch_image_ar":"شَرَر النار المتطاير"},{"branch_id":"B004","branch_image_ar":"الشَّرْشَرَة تقطيع ونفض"},{"branch_id":"B005","branch_image_ar":"الشواء المتقاطر دسمه"},{"branch_id":"B006","branch_image_ar":"الشراشر ذباذب وأثقال"},{"branch_id":"B007","branch_image_ar":"إلقاء الشراشر إلقاء النفس كلها"},{"branch_id":"B009","branch_image_ar":"الشَّرّان أذى كالبعوض"},{"branch_id":"B010","branch_image_ar":"شِرّة الشباب نشاط وحرص"},{"branch_id":"B011","branch_image_ar":"المشارة مخاصمة"},{"branch_id":"B012","branch_image_ar":"الشِّرْشِر نبت"}],"mapped_root_id":"root_000787","mapped_root_norm":"ش ر ر"},{"branches":[{"branch_id":"B001","branch_image_ar":"المعاوضة بين بيع وشراء"},{"branch_id":"B002","branch_image_ar":"المماثلة والمقابلة"},{"branch_id":"B003","branch_image_ar":"الناحية والطرف"},{"branch_id":"B004","branch_image_ar":"نبات الشَّري والشرية"},{"branch_id":"B005","branch_image_ar":"الموضع ذو الغياض والأسد"},{"branch_id":"B006","branch_image_ar":"الشِّريان عود القسي والعروق"},{"branch_id":"B007","branch_image_ar":"انتشار البرق ولمعانه"},{"branch_id":"B008","branch_image_ar":"الهيجان واللجاج والاندفاع"},{"branch_id":"B009","branch_image_ar":"داء الشَّرى في الجلد"},{"branch_id":"B010","branch_image_ar":"إملاء الحوض والجفنة"},{"branch_id":"B011","branch_image_ar":"الشُّراة وبيع النفس"},{"branch_id":"B012","branch_image_ar":"الدعاء بالمساءة"}],"mapped_root_id":"root_000792","mapped_root_norm":"ش ر ي"}]},{"root":"و س و س","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"حديث النفس الخفي"},{"branch_id":"B002","branch_image_ar":"صوت خفي"},{"branch_id":"B003","branch_image_ar":"الوسواس الشيطان"}],"mapped_root_id":"root_001651","mapped_root_norm":"و س و س"}]},{"root":"خ ن س","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الانخناس إلى خفاء أو تأخر"},{"branch_id":"B002","branch_image_ar":"الكواكب التي تخفى وترجع"},{"branch_id":"B003","branch_image_ar":"الخَنَس في الأنف"},{"branch_id":"B004","branch_image_ar":"مأوى الظباء أو الظباء"},{"branch_id":"B005","branch_image_ar":"عدول الفرس في حضره"}],"mapped_root_id":"root_000443","mapped_root_norm":"خ ن س"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"114:4","surface_ref":"114:4"},{"ayah_ref":"114:5","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"114:5","root_occurrences":[{"lemmas_ar":["وَسْوَسَ"],"occurrence_count":1,"pos_tags":["V"],"root":"و س و س","surfaces_ar":["يُوَسْوِسُ"],"word_indices":["2"]},{"lemmas_ar":["صَدْر"],"occurrence_count":1,"pos_tags":["N"],"root":"ص د ر","surfaces_ar":["صُدُورِ"],"word_indices":["4"]},{"lemmas_ar":["نَّاس"],"occurrence_count":1,"pos_tags":["N"],"root":"ن و س","surfaces_ar":["نَّاسِ"],"word_indices":["5"]}],"root_sequence":["و س و س","ص د ر","ن و س"],"text_ar":"ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ"}],"context_order":["114:5"],"context_root_cues":[{"root":"و س و س","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"حديث النفس الخفي"},{"branch_id":"B002","branch_image_ar":"صوت خفي"},{"branch_id":"B003","branch_image_ar":"الوسواس الشيطان"}],"mapped_root_id":"root_001651","mapped_root_norm":"و س و س"}]},{"root":"ص د ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الصدر الجارحة وما يتصل بها"},{"branch_id":"B002","branch_image_ar":"المقدّم والأعلى والأول"},{"branch_id":"B003","branch_image_ar":"الصُّدور عن المورد"},{"branch_id":"B004","branch_image_ar":"الأصل الذي تصدر عنه الأفعال"},{"branch_id":"B005","branch_image_ar":"المصادرة على مال"},{"branch_id":"B006","branch_image_ar":"الطائفة من الشيء"}],"mapped_root_id":"root_000849","mapped_root_norm":"ص د ر"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"114:5","surface_ref":"114:5"},{"ayah_ref":"114:6","context_kind":"ordered_context_ayah","evidence":{"context_ayat":[{"ref":"114:6","root_occurrences":[{"lemmas_ar":["جِنَّة"],"occurrence_count":1,"pos_tags":["N"],"root":"ج ن ن","surfaces_ar":["جِنَّةِ"],"word_indices":["2"]},{"lemmas_ar":["نَّاس"],"occurrence_count":1,"pos_tags":["N"],"root":"ن و س","surfaces_ar":["نَّاسِ"],"word_indices":["3"]}],"root_sequence":["ج ن ن","ن و س"],"text_ar":"مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ"}],"context_order":["114:6"],"context_root_cues":[{"root":"ج ن ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الستر والاستتار"},{"branch_id":"B002","branch_image_ar":"غشيان الليل"},{"branch_id":"B003","branch_image_ar":"البستان المستور بالشجر"},{"branch_id":"B005","branch_image_ar":"الجن المستترون"},{"branch_id":"B006","branch_image_ar":"ستر العقل بالجنون"},{"branch_id":"B007","branch_image_ar":"الجنين المستور في البطن"},{"branch_id":"B008","branch_image_ar":"الجُنّة الواقية"},{"branch_id":"B009","branch_image_ar":"مواراة الميت"},{"branch_id":"B010","branch_image_ar":"الجنان المستور في الصدر"},{"branch_id":"B011","branch_image_ar":"التفاف النبات واندفاعه"},{"branch_id":"B012","branch_image_ar":"الجان حية"},{"branch_id":"B013","branch_image_ar":"سواد الناس وجماعتهم"},{"branch_id":"B014","branch_image_ar":"جن الشيء في بدايته"},{"branch_id":"B016","branch_image_ar":"الجناجن عظام الصدر"},{"branch_id":"B017","branch_image_ar":"المَجَنَّة موضع الاستتار"}],"mapped_root_id":"root_000266","mapped_root_norm":"ج ن ن"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"114:6","surface_ref":"114:6"},{"ayah_ref":"1:2","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:2","root_occurrences":[{"lemmas_ar":["حَمْد"],"occurrence_count":1,"pos_tags":["N"],"root":"ح م د","surfaces_ar":["حَمْدُ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["لَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَبّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ر ب ب","surfaces_ar":["رَبِّ"],"word_indices":["3"]},{"lemmas_ar":["عَٰلَمِين"],"occurrence_count":1,"pos_tags":["N"],"root":"ع ل م","surfaces_ar":["عَٰلَمِينَ"],"word_indices":["4"]}],"root_sequence":["ح م د","ء ل ه","ر ب ب","ع ل م"],"text_ar":"ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ"}],"context_order":["1:2"],"context_root_cues":[{"root":"ح م د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الحمد خلاف الذم"},{"branch_id":"B002","branch_image_ar":"وجود الشيء محمودا"},{"branch_id":"B003","branch_image_ar":"المحمود كثير الخصال"},{"branch_id":"B004","branch_image_ar":"حماداك الغاية المحمودة"},{"branch_id":"B005","branch_image_ar":"يتحمد بالمنة"}],"mapped_root_id":"root_000355","mapped_root_norm":"ح م د"}]},{"root":"ر ب ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"ربوبية وملك وسيادة"},{"branch_id":"B002","branch_image_ar":"إصلاح وتربية وإتمام"},{"branch_id":"B003","branch_image_ar":"علم رباني"},{"branch_id":"B004","branch_image_ar":"ربة وجماعات كثيرة"},{"branch_id":"B005","branch_image_ar":"ربيب وربيبة ورابة"},{"branch_id":"B006","branch_image_ar":"رُبّ خاثر وإصلاح به"},{"branch_id":"B007","branch_image_ar":"لزوم وإقامة ودوام"},{"branch_id":"B008","branch_image_ar":"رباب السحاب"},{"branch_id":"B009","branch_image_ar":"شاة رُبّى وحداثة"},{"branch_id":"B010","branch_image_ar":"ربابة تجمع القداح"},{"branch_id":"B011","branch_image_ar":"ربابة عهد وميثاق"},{"branch_id":"B012","branch_image_ar":"ربة نبات"},{"branch_id":"B013","branch_image_ar":"ماء رَبَب كثير"},{"branch_id":"B014","branch_image_ar":"رَبْرَب قطيع"},{"branch_id":"B015","branch_image_ar":"حرف رب وربما"},{"branch_id":"B016","branch_image_ar":"رُبَى حاجة وعقدة ونعمة"},{"branch_id":"B017","branch_image_ar":"رباني الملاحين"}],"mapped_root_id":"root_000532","mapped_root_norm":"ر ب ب"},{"branches":[{"branch_id":"B001","branch_image_ar":"زيادة وعلو"},{"branch_id":"B002","branch_image_ar":"أرض مرتفعة"},{"branch_id":"B003","branch_image_ar":"زيادة الربا في المعاملة"},{"branch_id":"B004","branch_image_ar":"تصعد النفس وانتفاخه"},{"branch_id":"B005","branch_image_ar":"تغذية ونشوء"},{"branch_id":"B006","branch_image_ar":"نتوء أصل الفخذ"},{"branch_id":"B007","branch_image_ar":"أهل البيت من بني الأعمام"}],"mapped_root_id":"root_000537","mapped_root_norm":"ر ب و"}]},{"root":"ع ل م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"انكشاف الشيء للعارف"},{"branch_id":"B002","branch_image_ar":"أثر يميز الشيء ويهدي إليه"},{"branch_id":"B004","branch_image_ar":"شق ظاهر في الشفة العليا"},{"branch_id":"B005","branch_image_ar":"ماء كثير مجتمع في عيلم"},{"branch_id":"B006","branch_image_ar":"طائر جارح يسمى العلام"},{"branch_id":"B007","branch_image_ar":"ذكر الضباع يسمى العيلام"}],"mapped_root_id":"root_001040","mapped_root_norm":"ع ل م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:2","membership_added_ayah":true,"membership_target_surah":114,"surface_ref":"1:2"},{"ayah_ref":"1:3","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:3","root_occurrences":[{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["1","2"]}],"root_sequence":["ر ح م","ر ح م"],"text_ar":"ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"}],"context_order":["1:3"],"context_root_cues":[{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:3","membership_added_ayah":true,"membership_target_surah":114,"surface_ref":"1:3"},{"ayah_ref":"1:4","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:4","root_occurrences":[{"lemmas_ar":["مَٰلِك"],"occurrence_count":1,"pos_tags":["N"],"root":"م ل ك","surfaces_ar":["مَٰلِكِ"],"word_indices":["1"]},{"lemmas_ar":["يَوْم"],"occurrence_count":1,"pos_tags":["N"],"root":"ي و م","surfaces_ar":["يَوْمِ"],"word_indices":["2"]},{"lemmas_ar":["دِين"],"occurrence_count":1,"pos_tags":["N"],"root":"د ي ن","surfaces_ar":["دِّينِ"],"word_indices":["3"]}],"root_sequence":["م ل ك","ي و م","د ي ن"],"text_ar":"مَٰلِكِ يَوْمِ ٱلدِّينِ"}],"context_order":["1:4"],"context_root_cues":[{"root":"م ل ك","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"قوة الشيء وتماسكه"},{"branch_id":"B002","branch_image_ar":"المِلْك والتصرف"},{"branch_id":"B003","branch_image_ar":"المُلك والسلطان"},{"branch_id":"B004","branch_image_ar":"الإملاك والتزويج"},{"branch_id":"B005","branch_image_ar":"مِلاك الأمر وعِماده"},{"branch_id":"B006","branch_image_ar":"مَلَك الطريق والوادي"},{"branch_id":"B007","branch_image_ar":"الماء مَلَك الأمر"},{"branch_id":"B008","branch_image_ar":"المتقدم القائد في الحيوان"}],"mapped_root_id":"root_001444","mapped_root_norm":"م ل ك"}]},{"root":"ي و م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"وقت النهار المحدود"},{"branch_id":"B002","branch_image_ar":"مدة من الزمان"},{"branch_id":"B003","branch_image_ar":"كائنة اليوم وشدته"}],"mapped_root_id":"root_001700","mapped_root_norm":"ي و م"}]},{"root":"د ي ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الطاعة والانقياد"},{"branch_id":"B002","branch_image_ar":"الحساب والجزاء"},{"branch_id":"B003","branch_image_ar":"الدين المالي"},{"branch_id":"B004","branch_image_ar":"الإذلال والملك"},{"branch_id":"B005","branch_image_ar":"العادة والشأن"},{"branch_id":"B006","branch_image_ar":"مدينة الطاعة"},{"branch_id":"B007","branch_image_ar":"التصديق والتفويض"}],"mapped_root_id":"root_000504","mapped_root_norm":"د ي ن"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:4","membership_added_ayah":true,"membership_target_surah":114,"surface_ref":"1:4"},{"ayah_ref":"1:5","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:5","root_occurrences":[{"lemmas_ar":["عَبَدَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ع ب د","surfaces_ar":["نَعْبُدُ"],"word_indices":["2"]},{"lemmas_ar":["ٱسْتَعِينُ"],"occurrence_count":1,"pos_tags":["V"],"root":"ع و ن","surfaces_ar":["نَسْتَعِينُ"],"word_indices":["4"]}],"root_sequence":["ع ب د","ع و ن"],"text_ar":"إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ"}],"context_order":["1:5"],"context_root_cues":[{"root":"ع ب د","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرق والملك"},{"branch_id":"B003","branch_image_ar":"العبادة والطاعة الخاضعة"},{"branch_id":"B004","branch_image_ar":"التعبيد والاستعباد"},{"branch_id":"B005","branch_image_ar":"التذليل والتسوية"},{"branch_id":"B006","branch_image_ar":"التكريم والتعظيم"},{"branch_id":"B007","branch_image_ar":"القوة والصلابة"},{"branch_id":"B008","branch_image_ar":"الأنفة والغضب"},{"branch_id":"B009","branch_image_ar":"قلة اللبث وسرعة العدو"},{"branch_id":"B010","branch_image_ar":"التفرق في الوجوه"},{"branch_id":"B011","branch_image_ar":"العطب والانقطاع"},{"branch_id":"B012","branch_image_ar":"صَلاءة الطيب"}],"mapped_root_id":"root_000973","mapped_root_norm":"ع ب د"}]},{"root":"ع و ن","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الإعانة والمظاهرة"},{"branch_id":"B002","branch_image_ar":"العَوان بين السنين"},{"branch_id":"B003","branch_image_ar":"الحرب العَوان"},{"branch_id":"B004","branch_image_ar":"النخلة العَوانة القديمة"},{"branch_id":"B005","branch_image_ar":"استواء الخلقة وتلاحق القوة"},{"branch_id":"B006","branch_image_ar":"العانة قطيع الحمر"},{"branch_id":"B007","branch_image_ar":"عانة الرجل"},{"branch_id":"B008","branch_image_ar":"النسبة إلى عانة"}],"mapped_root_id":"root_001064","mapped_root_norm":"ع و ن"},{"branches":[{"branch_id":"B001","branch_image_ar":"العين الناظرة"},{"branch_id":"B002","branch_image_ar":"المشاهدة بالعين"},{"branch_id":"B003","branch_image_ar":"عين الحفظ والرعاية"},{"branch_id":"B004","branch_image_ar":"الإصابة بالعين"},{"branch_id":"B005","branch_image_ar":"العين الجاسوسة"},{"branch_id":"B006","branch_image_ar":"منبع الماء الجاري"},{"branch_id":"B007","branch_image_ar":"عين الجلد والسقاء"},{"branch_id":"B008","branch_image_ar":"عين الشمس"},{"branch_id":"B009","branch_image_ar":"النقرة أو الموضع العيني"},{"branch_id":"B010","branch_image_ar":"عين السحاب والمطر"},{"branch_id":"B011","branch_image_ar":"النقد الحاضر"},{"branch_id":"B012","branch_image_ar":"العينة والسلف"},{"branch_id":"B013","branch_image_ar":"عين الشيء نفسه"},{"branch_id":"B014","branch_image_ar":"العين خيار الشيء"},{"branch_id":"B015","branch_image_ar":"أعيان القوم والإخوة"},{"branch_id":"B016","branch_image_ar":"سعة العين وحسنها"},{"branch_id":"B017","branch_image_ar":"العين بمعنى الناس الحاضرون"}],"mapped_root_id":"root_001069","mapped_root_norm":"ع ي ن"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:5","membership_added_ayah":true,"membership_target_surah":114,"surface_ref":"1:5"},{"ayah_ref":"1:6","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:6","root_occurrences":[{"lemmas_ar":["هَدَى"],"occurrence_count":1,"pos_tags":["V"],"root":"ه د ي","surfaces_ar":["ٱهْدِ"],"word_indices":["1"]},{"lemmas_ar":["صِرَٰط"],"occurrence_count":1,"pos_tags":["N"],"root":"ص ر ط","surfaces_ar":["صِّرَٰطَ"],"word_indices":["2"]},{"lemmas_ar":["مُّسْتَقِيم"],"occurrence_count":1,"pos_tags":["ADJ"],"root":"ق و م","surfaces_ar":["مُسْتَقِيمَ"],"word_indices":["3"]}],"root_sequence":["ه د ي","ص ر ط","ق و م"],"text_ar":"ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ"}],"context_order":["1:6"],"context_root_cues":[{"root":"ه د ي","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"دلالة بلطف إلى الطريق والحق"},{"branch_id":"B002","branch_image_ar":"جهة الأمر وسيرته وقصده"},{"branch_id":"B003","branch_image_ar":"المتقدم الهادي وأوائل الشيء"},{"branch_id":"B004","branch_image_ar":"بعثة لطف وهدية إلى ذي مودة"},{"branch_id":"B005","branch_image_ar":"الهدي المهدى إلى الحرم"},{"branch_id":"B006","branch_image_ar":"العروس المهدية إلى زوجها"},{"branch_id":"B007","branch_image_ar":"هدي الحرمة والأسير"},{"branch_id":"B008","branch_image_ar":"مشي التهادي مع الاعتماد والتمايل"},{"branch_id":"B009","branch_image_ar":"الهداء البليد الضعيف"},{"branch_id":"B010","branch_image_ar":"هدي السكون وحسن الهيئة"},{"branch_id":"B011","branch_image_ar":"إهداء الشعر ومهاداته"}],"mapped_root_id":"root_001583","mapped_root_norm":"ه د ي"}]},{"root":"ص ر ط","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الطريق المستقيم"},{"branch_id":"B002","branch_image_ar":"الغيبة في المرور والبلع"},{"branch_id":"B003","branch_image_ar":"السيف القاطع الماضي في الضربة"}],"mapped_root_id":"root_000858","mapped_root_norm":"ص ر ط"}]},{"root":"ق و م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"جماعة الناس والرجال"},{"branch_id":"B002","branch_image_ar":"انتصاب وقيام بالبدن"},{"branch_id":"B003","branch_image_ar":"عزم ونهوض إلى الأمر"},{"branch_id":"B004","branch_image_ar":"رعاية وحفظ وولاية"},{"branch_id":"B006","branch_image_ar":"مقام وإقامة في موضع"},{"branch_id":"B007","branch_image_ar":"نيابة وقيام مقام غيره"},{"branch_id":"B008","branch_image_ar":"استقامة واعتدال واستواء"},{"branch_id":"B009","branch_image_ar":"قوام وعماد ومعاش"},{"branch_id":"B010","branch_image_ar":"قيمة وتقويم وتسعير"},{"branch_id":"B011","branch_image_ar":"قامة وقوام الجسم والطول"},{"branch_id":"B012","branch_image_ar":"آلة قائمة وجزء قائم"},{"branch_id":"B013","branch_image_ar":"قيامة وبعث وقيام الساعة"},{"branch_id":"B014","branch_image_ar":"مقاومة ومنازلة"},{"branch_id":"B015","branch_image_ar":"وزن سواء ومقدار معتدل"},{"branch_id":"B016","branch_image_ar":"جمود ووقوف وكلال"},{"branch_id":"B017","branch_image_ar":"انتصاف النهار وقائم الظهيرة"},{"branch_id":"B018","branch_image_ar":"نفاق السوق"},{"branch_id":"B019","branch_image_ar":"وجع قائم بالعضو"},{"branch_id":"B020","branch_image_ar":"قوام في قوائم الشاة"},{"branch_id":"B021","branch_image_ar":"عين قائمة ذاهبة البصر"}],"mapped_root_id":"root_001273","mapped_root_norm":"ق و م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:6","membership_added_ayah":true,"membership_target_surah":114,"surface_ref":"1:6"},{"ayah_ref":"1:7","context_kind":"external_ayah_member","evidence":{"context_ayat":[{"ref":"1:7","root_occurrences":[{"lemmas_ar":["صِرَٰط"],"occurrence_count":1,"pos_tags":["N"],"root":"ص ر ط","surfaces_ar":["صِرَٰطَ"],"word_indices":["1"]},{"lemmas_ar":["أَنْعَمَ"],"occurrence_count":1,"pos_tags":["V"],"root":"ن ع م","surfaces_ar":["أَنْعَمْ"],"word_indices":["3"]},{"lemmas_ar":["غَيْر"],"occurrence_count":1,"pos_tags":["N"],"root":"غ ي ر","surfaces_ar":["غَيْرِ"],"word_indices":["5"]},{"lemmas_ar":["مَغْضُوب"],"occurrence_count":1,"pos_tags":["N"],"root":"غ ض ب","surfaces_ar":["مَغْضُوبِ"],"word_indices":["6"]},{"lemmas_ar":["ضَآلّ"],"occurrence_count":1,"pos_tags":["N"],"root":"ض ل ل","surfaces_ar":["ضَّآلِّينَ"],"word_indices":["9"]}],"root_sequence":["ص ر ط","ن ع م","غ ي ر","غ ض ب","ض ل ل"],"text_ar":"صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ"}],"context_order":["1:7"],"context_root_cues":[{"root":"ص ر ط","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الطريق المستقيم"},{"branch_id":"B002","branch_image_ar":"الغيبة في المرور والبلع"},{"branch_id":"B003","branch_image_ar":"السيف القاطع الماضي في الضربة"}],"mapped_root_id":"root_000858","mapped_root_norm":"ص ر ط"}]},{"root":"ن ع م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"حسن الحال والنعمة"},{"branch_id":"B002","branch_image_ar":"اللين والنعومة ورفاه العيش"},{"branch_id":"B003","branch_image_ar":"مدح الشيء بنعم"},{"branch_id":"B004","branch_image_ar":"الجواب بنعم والتصديق"},{"branch_id":"B005","branch_image_ar":"مال الأنعام والإبل"},{"branch_id":"B006","branch_image_ar":"النعام والنعامة الطائر"},{"branch_id":"B007","branch_image_ar":"ما سمي نعامة تشبيها بالهيئة"},{"branch_id":"B008","branch_image_ar":"طيران النعامة وتفرق القوم"},{"branch_id":"B009","branch_image_ar":"النعامى ريح لينة"},{"branch_id":"B010","branch_image_ar":"زاد وأنعم في الفعل"},{"branch_id":"B011","branch_image_ar":"موافقة المكان وطيب المقام"},{"branch_id":"B012","branch_image_ar":"المشي على القدم وابتذالها"},{"branch_id":"B013","branch_image_ar":"نعم الله بك عينا وقرة العين"}],"mapped_root_id":"root_001525","mapped_root_norm":"ن ع م"}]},{"root":"غ ي ر","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الصلاح والمنفعة بالميرة والسقي والإصلاح"},{"branch_id":"B002","branch_image_ar":"الغَيْر في الدية"},{"branch_id":"B003","branch_image_ar":"تغيير الصورة أو إبدال الشيء بغيره"},{"branch_id":"B004","branch_image_ar":"الغَيْرة على الأهل"},{"branch_id":"B005","branch_image_ar":"السوى والخلاف والاستثناء والنفي"}],"mapped_root_id":"root_001119","mapped_root_norm":"غ ي ر"}]},{"root":"غ ض ب","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"اشتداد السخط وثورانه للانتقام"},{"branch_id":"B002","branch_image_ar":"الغضب لشخص حي أو به بعد موته"},{"branch_id":"B003","branch_image_ar":"المراغمة والمخالفة"},{"branch_id":"B004","branch_image_ar":"صلابة الصخرة وتماسكها"},{"branch_id":"B005","branch_image_ar":"غلظ الجسم وشدة الحمرة"},{"branch_id":"B006","branch_image_ar":"تورم العين وما حولها"},{"branch_id":"B007","branch_image_ar":"العبوس والضجر والعظم في وصف الحيوان أو الشخص"},{"branch_id":"B008","branch_image_ar":"جلد صلب أو مطوي كدرقة"}],"mapped_root_id":"root_001092","mapped_root_norm":"غ ض ب"}]},{"root":"ض ل ل","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الضلال عن الهدى والقصد"},{"branch_id":"B002","branch_image_ar":"الغيبوبة والخفاء"},{"branch_id":"B003","branch_image_ar":"فقدان الشيء"},{"branch_id":"B004","branch_image_ar":"ضياع الحفظ"},{"branch_id":"B005","branch_image_ar":"الضالّة في المضيعة"}],"mapped_root_id":"root_000913","mapped_root_norm":"ض ل ل"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:7","membership_added_ayah":true,"membership_target_surah":114,"surface_ref":"1:7"}],"support_registry":[{"anchor_evidence":[{"arabic_uthmani":"قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ","ayah_ref":"114:1"},{"arabic_uthmani":"إِلَٰهِ ٱلنَّاسِ","ayah_ref":"114:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000047/B001","root_000532/B002","root_001059/B001","root_001272/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000047","role":"The worshipped-one image supplies the allegiance enacted within the refuge utterance.","root":"ء ل ه","source_ref":"114:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001272","role":"Bringing speech out in pronunciation makes the surrounding construction a performed utterance.","root":"ق و ل","source_ref":"114:1","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001059","role":"Seeking shelter and holding fast supplies the protective action performed by the utterance.","root":"ع و ذ","source_ref":"114:1","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000532","role":"Repair, nurture, and completion make refuge an active process of restoring the speaker.","root":"ر ب ب","source_ref":"114:1","source_word_indices":["3"]}],"changed_reading":{"after":"`إله الناس` is also an avowed allegiance inside a speech-act of entering restorative protection.","before":"`إله الناس` is a nominal statement about who God is."},"confidence":"strong","mechanism":"Audible saying initiates refuge, and refuge is directed through a lordly relation of repair and completion. Inside that frame, `إله الناس` changes from a static title into the avowed worship relation by which the speaker enters protective formation.","model_id":"d_performed_refuge","reader_inference":"The packet supplies pronounced saying, refuge, and reparative nurture; I supply the arrow that avowing the deity-title helps enact entry into that refuge. A live alternative is that the command merely reports the titles without making their pronunciation operative.","status":"revised","structural_cues":["The imperative `قُلْ` and first-person `أَعُوذُ` place the following titles inside one performed refuge utterance.","`الناس` remains the genitive while the governing title changes across 114:1-3."],"trigger_roots":["ق و ل","ع و ذ","ر ب ب"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_performed_refuge","source_type":"hft","support_id":"sup_02e169fe0d3adf6d330d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ","ayah_ref":"114:1"},{"arabic_uthmani":"مَلِكِ ٱلنَّاسِ","ayah_ref":"114:2"},{"arabic_uthmani":"إِلَٰهِ ٱلنَّاسِ","ayah_ref":"114:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000047/B001","root_000532/B002","root_001444/B002","root_001444/B005"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000047","role":"Worship supplies the terminal relation of allegiance in the three-title sequence.","root":"ء ل ه","source_ref":"114:3","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000532","role":"Nurture, repair, and completion supply the formative first relation.","root":"ر ب ب","source_ref":"114:1","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001444","role":"Possession and power of disposition supply the governing middle relation.","root":"م ل ك","source_ref":"114:2","source_word_indices":["1"]},{"branch_id":"B005","mapped_root_id":"root_001444","role":"The mainstay of an affair makes kingship the structural pivot between nurture and worship.","root":"م ل ك","source_ref":"114:2","source_word_indices":["1"]}],"changed_reading":{"after":"It names the distinct culmination where being nurtured and governed becomes an orientation of worship.","before":"`إله الناس` repeats the authority already expressed by lord and king."},"confidence":"strong","mechanism":"Repairing nurture, governing disposition, and worship form a possible progression while `الناس` remains constant: humans are formed, ordered, and finally oriented in allegiance. The focus title is the culmination of relation rather than a synonym mechanically added to the first two.","model_id":"d_title_progression","reader_inference":"The packet supplies sequence plus the branch functions of nurture, disposition, mainstay, and worship; I supply the directional movement from formation through governance to allegiance. The titles may instead be an unordered cumulative stack.","status":"revised","structural_cues":["The same genitive `الناس` follows three different heads in immediate sequence.","The focus ayah is the shortest and final member of the title series."],"trigger_roots":["ر ب ب","م ل ك"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_title_progression","source_type":"hft","support_id":"sup_15654188a4a968fdf517","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"مَلِكِ ٱلنَّاسِ","ayah_ref":"114:2"},{"arabic_uthmani":"إِلَٰهِ ٱلنَّاسِ","ayah_ref":"114:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000047/B001","root_000059/B001","root_001444/B001","root_001444/B005"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000047","role":"Common worship supplies the relation capable of binding separate persons.","root":"ء ل ه","source_ref":"114:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000059","role":"Visible human presence makes the social collective, rather than an abstract species, the focus.","root":"ن و س","source_ref":"114:3","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001444","role":"Strength and cohesion supply the social effect attributed to shared orientation.","root":"م ل ك","source_ref":"114:2","source_word_indices":["1"]},{"branch_id":"B005","mapped_root_id":"root_001444","role":"A mainstay supplies the image of worship as the collective's organizing support.","root":"م ل ك","source_ref":"114:2","source_word_indices":["1"]}],"changed_reading":{"after":"Shared orientation to the deity can itself be the mainstay that constitutes people as a coherent public.","before":"The deity stands over an already constituted set of individuals."},"confidence":"medium","mechanism":"The adjacent kingship inventory activates strength, cohesion, and a mainstay. Read back through the worship relation, `إله الناس` can describe the shared allegiance that holds a visible collective together, not only the private belief of each member.","model_id":"d_collective_cohesion","reader_inference":"The packet supplies cohesion and mainstay under the adjacent kingship root; I transfer those as effects of the focus ayah's shared worship relation. The alternative is to keep cohesion wholly inside political sovereignty.","status":"new","structural_cues":["`ملك الناس` and `إله الناس` are adjacent constructions with the same dependent collective."],"trigger_roots":["م ل ك"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_collective_cohesion","source_type":"hft","support_id":"sup_bfc8c4e17918a87aaa4c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ","ayah_ref":"114:1"},{"arabic_uthmani":"إِلَٰهِ ٱلنَّاسِ","ayah_ref":"114:3"},{"arabic_uthmani":"مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ","ayah_ref":"114:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000047/B001","root_000059/B003","root_000443/B001","root_001059/B004","root_001651/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000047","role":"Worship keeps the companionship model anchored in the focus title's devotional relation.","root":"ء ل ه","source_ref":"114:3","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000059","role":"Familiar comfort that removes estrangement supplies the affective quality of protection.","root":"ن و س","source_ref":"114:3","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_001059","role":"Adhering and remaining within a shelter gives protective nearness temporal persistence.","root":"ع و ذ","source_ref":"114:1","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001651","role":"Hidden self-talk supplies the intimate but hostile voice against which companionship operates.","root":"و س و س","source_ref":"114:4","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000443","role":"Retreat into concealment makes the hostile presence intermittent rather than abiding.","root":"خ ن س","source_ref":"114:4","source_word_indices":["4"]}],"changed_reading":{"after":"It also names an abiding, estrangement-removing nearness that outlasts the whisperer's arrivals and withdrawals.","before":"`إله الناس` is primarily a public relation of collective worship."},"confidence":"medium","mechanism":"Refuge as adhering within protection joins the focus inventory's familiar comfort, while the hostile voice is hidden and recurrently retreats. The deity-human relation becomes abiding companionship whose continuity counters an invasive voice defined by unstable appearance.","model_id":"d_abiding_companionship","reader_inference":"The packet supplies adhesion in shelter, familiar comfort, hidden self-talk, and retreat; I supply the contrast between stable companionship and intermittent intrusion. A live alternative is that refuge remains juridical protection with no affective companionship.","status":"strengthened","structural_cues":["The refuge frame precedes the divine titles, while the withdrawing whisperer follows them.","The focus relation stands between sought shelter and unstable hidden speech."],"trigger_roots":["ع و ذ","و س و س","خ ن س"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_abiding_companionship","source_type":"hft","support_id":"sup_6f7fc1ca0bc4eae9000a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِلَٰهِ ٱلنَّاسِ","ayah_ref":"114:3"},{"arabic_uthmani":"مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ","ayah_ref":"114:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000047/B001","root_000059/B002","root_000443/B002","root_000787/B003","root_001651/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000047","role":"Worship supplies a durable orientation against intermittent solicitations.","root":"ء ل ه","source_ref":"114:3","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000059","role":"Seeing, hearing, and sensing locate the contest inside human perceptual awareness.","root":"ن و س","source_ref":"114:3","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000787","role":"Scattered fire-sparks supply brief, attention-catching bursts.","root":"ش ر ر","source_ref":"114:4","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001651","role":"A hidden low sound supplies a stimulus near the threshold of hearing.","root":"و س و س","source_ref":"114:4","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000443","role":"Stars that disappear and return supply a recurring visibility cycle.","root":"خ ن س","source_ref":"114:4","source_word_indices":["4"]}],"changed_reading":{"after":"The deity is the stable orientation of perceivers whose attention is vulnerable to brief, low, repeatedly vanishing signals.","before":"The deity is related to humans as generally perceptive beings."},"confidence":"medium","mechanism":"Flying sparks, a low hidden sound, and star-like hiding and return converge on intermittent stimulation. The perceptive-human baseline is therefore revised: human awareness is a pulsed field, and the worship relation supplies a stable reference through sensory flicker.","model_id":"d_intermitent_attention","reader_inference":"The packet supplies sparks, hidden sound, recurrent disappearance, and perceptive humanity; I supply their shared temporal pattern and contrast it with stable worship. They may instead remain unrelated lexical images with no common attention model.","status":"revised","structural_cues":["The threat description immediately follows the completed three-title sequence.","`الخناس` modifies the whispering source, combining low signal with recurrent withdrawal."],"trigger_roots":["ش ر ر","و س و س","خ ن س"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_intermitent_attention","source_type":"hft","support_id":"sup_c84d65e31f3be5dc8853","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِلَٰهِ ٱلنَّاسِ","ayah_ref":"114:3"},{"arabic_uthmani":"مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ","ayah_ref":"114:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000047/B001","root_000443/B001","root_000792/B001","root_000792/B002","root_001651/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000047","role":"The worshipped object supplies what covert exchange attempts to replace or reprice.","root":"ء ل ه","source_ref":"114:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000792","role":"Exchange between buying and selling supplies the transactional mechanism.","root":"ش ر ر","source_ref":"114:4","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000792","role":"Equivalence and comparison supply the whispered claim that a substitute has matching value.","root":"ش ر ر","source_ref":"114:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001651","role":"Hidden self-talk locates the bargaining process inside apparently private thought.","root":"و س و س","source_ref":"114:4","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000443","role":"Withdrawal into concealment lets the proposal evade inspection after it is planted.","root":"خ ن س","source_ref":"114:4","source_word_indices":["4"]}],"changed_reading":{"after":"It fixes the non-substitutable object of worship against covert inner bargains that counterfeit equivalence and trade allegiance away.","before":"`إله الناس` identifies the proper object of worship before an unspecified evil."},"confidence":"exploratory","mechanism":"The non-dominant mapped branch of `ش ر ر` activates exchange and equivalence. Joined to concealed self-talk that then recedes, it models temptation as a covert transaction: whispered comparisons make some substitute seem worth trading for the focus ayah's true object of worship.","model_id":"d_covert_exchange","reader_inference":"The packet explicitly supplies a non-dominant exchange branch, equivalence, hidden self-talk, and retreat; I supply the arrow from exchange to substitution of allegiance. The ordinary harm branch remains a live and much nearer alternative.","status":"new","structural_cues":["`شَرِّ` governs the whole whisperer construction, allowing its split inventory to color the threat's mechanism.","The threat appears only after the focus ayah has identified the object of worship."],"trigger_roots":["ش ر ر","و س و س","خ ن س"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_covert_exchange","source_type":"hft","support_id":"sup_e908d372714a107278e4","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِلَٰهِ ٱلنَّاسِ","ayah_ref":"114:3"},{"arabic_uthmani":"ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ","ayah_ref":"114:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000047/B001","root_000059/B006","root_000849/B004","root_001651/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000047","role":"Worship supplies the governing allegiance whose practical effects emerge as action.","root":"ء ل ه","source_ref":"114:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001651","role":"Hidden self-talk supplies the covert input introduced before action becomes visible.","root":"و س و س","source_ref":"114:5","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_000849","role":"The origin from which actions issue supplies the causal location of the contest.","root":"ص د ر","source_ref":"114:5","source_word_indices":["4"]},{"branch_id":"B006","mapped_root_id":"root_000059","role":"The idiom of one's self or intimate companion makes the apparently private self the immediate target.","root":"ن و س","source_ref":"114:5","source_word_indices":["5"]}],"changed_reading":{"after":"It reaches the pre-action source of the self, where allegiance organizes which inner prompt is allowed to issue as conduct.","before":"The focus phrase governs the public fact of human worship."},"confidence":"strong","mechanism":"Hidden self-talk enters the breast understood as the source from which actions issue, while the repeated human root can narrow toward one's own self. The focus worship relation is thus upstream governance of action-generation, exactly where rival impulses seek to become deeds.","model_id":"d_action_source","reader_inference":"The packet supplies hidden self-talk, an action-origin, and the private self; I supply the arrow that competing inward inputs become outward deeds and that worship governs this upstream point. `صدور` may remain chiefly anatomical without the causal extension.","status":"strengthened","structural_cues":["The prepositional phrase `في صدور الناس` explicitly locates whispering inside the people named by the focus construct.","The same `الناس` is first related to the deity and later named as the interior site of intrusion."],"trigger_roots":["و س و س","ص د ر","ن و س"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_action_source","source_type":"hft","support_id":"sup_bdd37317ea70daa6c704","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ","ayah_ref":"114:1"},{"arabic_uthmani":"إِلَٰهِ ٱلنَّاسِ","ayah_ref":"114:3"},{"arabic_uthmani":"ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ","ayah_ref":"114:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000047/B001","root_001272/B001","root_001272/B012","root_001651/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000047","role":"The worship relation supplies the criterion by which competing speech channels are oriented.","root":"ء ل ه","source_ref":"114:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001272","role":"Pronounced saying supplies the overt and accountable speech channel.","root":"ق و ل","source_ref":"114:1","source_word_indices":["1"]},{"branch_id":"B012","mapped_root_id":"root_001272","role":"Unmanifested saying within the self shows that qawl can also occupy an inner channel.","root":"ق و ل","source_ref":"114:1","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001651","role":"Hidden self-talk supplies the covert channel that can masquerade as one's own thought.","root":"و س و س","source_ref":"114:5","source_word_indices":["2"]}],"changed_reading":{"after":"It becomes the allegiance by which a person tests whether inner or outer speech is avowed, answerable, and truly one's own.","before":"`إله الناس` is content named by the speaker."},"confidence":"medium","mechanism":"The command to say spans both articulated speech and a qawl branch for unmanifested inner saying; the later whisper is hidden self-talk. `إله الناس` can therefore function as the allegiance-marker that distinguishes avowed speech from speech that arrives covertly in the first-person register.","model_id":"d_speech_channels","reader_inference":"The packet supplies overt saying, inner saying, and hidden self-talk; I supply the competition between accountable avowal and covertly inserted speech. A live alternative is that these are merely different speech modes without a contest over authorship.","status":"new","structural_cues":["An imperative of saying opens the unit, while a finite verb of whispering later defines the threat.","The focus title lies between the overt command and the covert speech description."],"trigger_roots":["ق و ل","و س و س"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_speech_channels","source_type":"hft","support_id":"sup_1bda9c12faa6759bb714","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِلَٰهِ ٱلنَّاسِ","ayah_ref":"114:3"},{"arabic_uthmani":"مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ","ayah_ref":"114:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000047/B001","root_000059/B001","root_000266/B005"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000047","role":"Shared worship supplies the relation that can orient humans despite influence moving through the group.","root":"ء ل ه","source_ref":"114:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000059","role":"Visible human presence identifies the focus collective later reused as a possible source class.","root":"ن و س","source_ref":"114:3","source_word_indices":["2"]},{"branch_id":"B005","mapped_root_id":"root_000266","role":"Hidden beings supply one concealed origin of the invasive prompting.","root":"ج ن ن","source_ref":"114:6","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000059","role":"Visible humans supply the coordinated second origin and make social transmission possible.","root":"ن و س","source_ref":"114:6","source_word_indices":["3"]}],"changed_reading":{"after":"They are a porous collective whose members may receive or transmit hidden pressure, so shared worship also governs social mediation.","before":"The people in `إله الناس` are only protected beneficiaries."},"confidence":"strong","mechanism":"The ending coordinates hidden beings with visible humans as source classes. The very people attached to the deity in the focus ayah are therefore not only recipients of protection; they can become relays of concealed prompting to one another, making the worship relation a safeguard within a porous social network.","model_id":"d_porous_human_network","reader_inference":"The packet supplies the hidden-visible pairing and recurrence of the same human noun; I supply the network arrow by which humans relay covert influence to other humans. The alternative is a simple two-species classification with no emphasis on transmission.","status":"revised","structural_cues":["The closing coordination `من الجنة والناس` pairs hidden and visible source classes.","`الناس` moves from dependent of the deity in 114:3 to a coordinated source category in 114:6."],"trigger_roots":["ج ن ن","ن و س"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:d_porous_human_network","source_type":"hft","support_id":"sup_2f91a8a3542485f8254c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِلَٰهِ ٱلنَّاسِ","ayah_ref":"114:3"},{"arabic_uthmani":"مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ","ayah_ref":"114:4"},{"arabic_uthmani":"ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ","ayah_ref":"114:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000047/B001","root_000059/B005","root_000849/B004","root_001651/B002"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000059","role":"The little human image in the dark pupil supplies a model of the self appearing inside perception.","root":"ن و س","source_ref":"114:3","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000047","role":"Worship anchors the optical image in the question of what the perceived self is oriented toward.","root":"ء ل ه","source_ref":"114:3","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001651","role":"A hidden sound adds a barely perceived signal that can alter the inward image.","root":"و س و س","source_ref":"114:4","source_word_indices":["3"]},{"branch_id":"B004","mapped_root_id":"root_000849","role":"The source from which actions issue connects altered self-perception to later conduct.","root":"ص د ر","source_ref":"114:5","source_word_indices":["4"]}],"changed_reading":{"after":"Exploratorily, the deity is also the orientation of the inward human image at the perceptual interface where subtle signals can reshape action.","before":"The deity is related to people as externally visible bodies."},"confidence":"exploratory","containment":"This is surprising because it carries the eye's tiny human image into a cross-sensory model of inward representation. It remains anchored in the focus noun's attested branch and in context branches for hidden sound and action-source. Render it only as an optical analogy for vulnerable self-perception, never as a lexical translation of `الناس` as pupil.","focus_anchor":"The focus noun's inventory includes the human-like image seen in the pupil.","outlier_id":"o_pupil_interface"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:o_pupil_interface","source_type":"hft","support_id":"sup_b4ff40f5dbbb297b8e4c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِلَٰهِ ٱلنَّاسِ","ayah_ref":"114:3"},{"arabic_uthmani":"مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ","ayah_ref":"114:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000047/B001","root_000059/B001","root_000266/B013"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000047","role":"Worship keeps the model about the collective's orientation rather than crowd behavior in general.","root":"ء ل ه","source_ref":"114:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000059","role":"Visible human presence supplies the public collective that can nevertheless become opaque in aggregate.","root":"ن و س","source_ref":"114:3","source_word_indices":["2"]},{"branch_id":"B013","mapped_root_id":"root_000266","role":"The dark mass or crowd of people supplies collective density as a form of concealment.","root":"ج ن ن","source_ref":"114:6","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000059","role":"The coordinated visible-human category keeps the opacity model tied to actual social presence.","root":"ن و س","source_ref":"114:6","source_word_indices":["3"]}],"changed_reading":{"after":"Exploratorily, it concerns allegiance within a crowd whose very density can hide agency and circulate influence without a visible author.","before":"`إله الناس` concerns a transparent sum of visible individuals."},"confidence":"exploratory","containment":"This is surprising because a `ج ن ن` branch names the dark mass or crowd of people, partially folding visible humanity back into concealment. It remains relevant because 114:6 directly coordinates that root with the same `الناس` that anchors the focus. Use it as a social-opacity analogy, not as a replacement gloss for `الجنة` or proof that the two nouns are identical.","focus_anchor":"`الناس` names the manifest collective related to the deity, while the closing context places that collective beside a root with a crowd-mass branch.","outlier_id":"o_crowd_opacity"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:o_crowd_opacity","source_type":"hft","support_id":"sup_d85d3cf24e0877bb451e","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"مَلِكِ ٱلنَّاسِ","ayah_ref":"114:2"},{"arabic_uthmani":"إِلَٰهِ ٱلنَّاسِ","ayah_ref":"114:3"},{"arabic_uthmani":"مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ","ayah_ref":"114:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000047/B001","root_000059/B004","root_000443/B005","root_001444/B006"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000047","role":"Devotional orientation supplies the course from which deviation matters.","root":"ء ل ه","source_ref":"114:3","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_000059","role":"The person-facing side supplies a directional face for human orientation.","root":"ن و س","source_ref":"114:3","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_001444","role":"Owning a road or valley supplies the image of a course lying within ordered jurisdiction.","root":"م ل ك","source_ref":"114:2","source_word_indices":["1"]},{"branch_id":"B005","mapped_root_id":"root_000443","role":"A horse veering during its run supplies lateral deflection without stopping forward motion.","root":"خ ن س","source_ref":"114:4","source_word_indices":["4"]}],"changed_reading":{"after":"Exploratorily, it is the orienting course of human allegiance, while whispering works as a concealed lateral deviation that can occur even during apparent forward motion.","before":"`إله الناس` is a destination named independently of movement."},"confidence":"exploratory","containment":"This is surprising because it crosses a route owned under `م ل ك` with a horse's lateral veering under `خ ن س`. It remains anchored in `إله` as orientation of worship and in the immediate title-threat sequence. Render it as a spatial analogy for allegiance and deviation, not as the lexical meaning of any focus word.","focus_anchor":"Worship in `إله` supplies an orientation, while the neighboring context inventories supply a governed route and a sudden deviation from motion.","outlier_id":"o_route_deviation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:o_route_deviation","source_type":"hft","support_id":"sup_6097d2a052d527c059e7","trust":"legacy_unbound"}]}
</lane_packet_json>
