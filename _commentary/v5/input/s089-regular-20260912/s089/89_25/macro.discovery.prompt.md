# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **89:25**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s089-regular-20260912/s089/89_25/macro.discovery.json` and modify nothing
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

- Macro has no explicitly added external ayat. Assess the declared pericope or host-surah context, including any automatic host basmala, as ordinary non-focus context.

## Response Schema

Return exactly these top-level fields:

```json
{
  "schema_version": "commentary-v5-scope-discovery-v1",
  "ayah_ref": "89:25",
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
{"branch_registry":[{"boundary":"Bu dal tekliği ve eşsizliği anlatır; olumsuzlukta kişi kapsamını, onlu sayı kuruluşlarını, gün adını ve dağ adını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000017/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:5:1","qac_word_ref":"89:25:5","surface_ar":"أَحَدٌ"}],"gloss":"tek ve eşi olmayan olma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığı bir tane, tek veya eşi bulunmayan olarak gösterir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Mutlak niteleme olarak kullanıldığında Tanrı'nın ortağı ve benzeri bulunmadığını bildirir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı sözün art arda yinelenmesi tek olma bildirimini pekiştirir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kaynak ifadesi sözcüğü saymanın başlangıcındaki bir sayısıyla da ilişkilendirir; düzenli sayı kuruluşları ayrı dalda ele alınır."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tek olma çekirdeğini, mutlak eşsizliği ve yinelemeli pekiştirmeyi birlikte temsil eden dal düzeyi karşılıktır.","boundary_detail":"Bu dal tekliği ve eşsizliği anlatır; olumsuzlukta kişi kapsamını, onlu sayı kuruluşlarını, gün adını ve dağ adını kapsamaz.","branch_image_ar":"الأَحَدِيَّة والوَحْدَة","concept_gloss":"tek ve eşi olmayan olma","contextual_glosses":[{"applicability":"Sayılabilir bir varlığın tek örnek olduğunu bildiren genel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Mutlak eşsizlik ile yinelemeli pekiştirme yüzlerini taşımaz.","preserves":"Bir tane olma çekirdeğini korur."},"facet_ids":["F001","F004"],"text":"bir tane","usage_role":"contextual"},{"applicability":"Tanrı'nın ortağı ve benzeri olmadığını bildiren mutlak niteleme bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel sayısal birliği ve yinelemeli söyleyiş biçimini kapsamaz.","preserves":"Mutlak tekliği ve eşsizliği korur."},"facet_ids":["F002"],"text":"tek ve eşsiz","usage_role":"contextual"},{"applicability":"Teklik bildiren sözün yinelenerek güçlü biçimde vurgulandığı söyleyiş için açıklayıcı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yinelenmeyen genel kullanımın bütün kapsamını taşımaz.","preserves":"Yineleme yoluyla yapılan tek olma vurgusunu korur."},"facet_ids":["F003"],"text":"yalnız bir, yalnız bir","usage_role":"explanatory"}],"definition":"Bir varlığın bir tane, tek ya da eşi olmayan olmasıdır; mutlak kullanımda Tanrı'nın ortağı ve benzeri bulunmadığını bildirir. Sözcüğün yinelenmesi bu tekliği güçlü biçimde vurgular.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığı bir tane, tek veya eşi bulunmayan olarak gösterir."},{"facet_id":"F002","role":"specialization","statement":"Mutlak niteleme olarak kullanıldığında Tanrı'nın ortağı ve benzeri bulunmadığını bildirir."},{"facet_id":"F003","role":"associated_use","statement":"Aynı sözün art arda yinelenmesi tek olma bildirimini pekiştirir."},{"facet_id":"F004","role":"source_variant","statement":"Kaynak ifadesi sözcüğü saymanın başlangıcındaki bir sayısıyla da ilişkilendirir; düzenli sayı kuruluşları ayrı dalda ele alınır."}],"identity_rationale":"Kaynak ifadesi tek olma, mutlak biçimde eşsiz sayılma ve yinelemeyle bu niteliği pekiştirme çekirdeğini destekler. Aynı ifade saymanın ilk basamağına da değindiği için dal korunabilir, ancak düzenli sayı kurma kullanımları ayrı sayı dalına bırakılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir tane; tek ve eşsiz"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yalnız bir, yalnız bir"}],"lexicalization_note":"Tanım yalın biçimdeki tek olma anlamını ve yinelemeli pekiştirmeyi ayrı yüzler olarak tutar; yinelemeyi yalın biçimin zorunlu anlamı yapmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en güçlü sınırlar mutlak birlik, alana bağlı eşsizlik, sayısal bir ve tek başına kalma dallarıyla kuruldu, kalanlar yalnız uzak konu ortaklığı taşıdığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal yalnız Tanrı'nın birliği çevresinde kuruludur; odak dal ise genel tek olmayı ve yinelemeli vurguyu da taşıdığı için bütünüyle onun yerine geçmez.","focus_only":"Odak dal genel tekliği, sayı başlangıcına değen kullanımı ve yinelemeli pekiştirmeyi de içerir.","gloss":"Tanrı'nın ortak ve benzerden uzak tekliği","neighbor_only":"Komşu dal Tanrı'nın birliği inancını, ortak bulunmamasını ve bölünmezliği daha geniş bir inanç alanı olarak işler.","neighbor_ref":"root_001631/B004","relation_type":"near_synonym","shared_zone":"İki dal da Tanrı için mutlak tekliği ve ortak bulunmamasını bildirir."},{"boundary_match":"partial","distinction":"Odak dalın tekliği varlığın bir tane veya mutlak eşsiz olmasıdır; komşu dalın eşsizliği ise belirli bir nitelik alanındaki karşılaştırmaya bağlıdır.","focus_only":"Odak dal sayısal birlik ve mutlak tek olma bildirebilir.","gloss":"belirli bir alanda benzeri bulunmayan","neighbor_only":"Komşu dal belirli bir üstünlük ya da kötülük alanında benzeri bulunmayan kişiyi anlatır.","neighbor_ref":"root_001240/B018","relation_type":"near_synonym","shared_zone":"İki dal da eş ya da benzer bulunmaması düşüncesinde buluşur."},{"boundary_match":"partial","distinction":"Odak dal nitelik olarak tekliği merkez alır; komşu dal ise birin sayı dizisindeki ve birleşik sayılardaki görevini merkez alır.","focus_only":"Odak dal varlığın tek ve eşi olmayan oluşunu, ayrıca bu niteliğin vurgulanmasını anlatır.","gloss":"bir sayısı ve onlu sayı kuruluşları","neighbor_only":"Komşu dal sayma dizisini, onlu sayı kuruluşlarını ve bir kümeyi on bire çıkarma işlemini kapsar.","neighbor_ref":"root_000017/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir tane olma düşüncesi ve sayının ilk basamağıyla bağ vardır."},{"boundary_match":"partial","distinction":"Odak dal bir nitelik bildirirken komşu dal tek başına kalma ya da ayrı ayrı hareket etme sürecini ve sonucunu bildirir.","focus_only":"Odak dal bir varlığın tek ya da eşsiz olma niteliğini bildirir.","gloss":"tek başına kalma ve birer birer dağılma","neighbor_only":"Komşu dal kişinin tek başına kalması veya bir topluluğun birer birer gelmesi gibi değişme ve dağılım olaylarını bildirir.","neighbor_ref":"root_000017/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da birlikten veya topluluktan ayrı tek olma görünümüne dokunur."}],"source_phrase_ar":"أحد فرع والأصل الواو وحد (maqayis); أحد بمعنى الواحد وهو أول العدد (sihah); قل هو الله أحد (sihah;mufradat); يستعمل مطلقا وصفا في وصف الله تعالى وأصله وحد (mufradat); أحد أحد (sihah)","source_summary":"Kaynakların ortak çizgisi tek olma düşüncesidir. Bu çizgi genel olarak bir tane olmayı, Tanrı için mutlak eşsizliği ve yineleme yoluyla yapılan güçlü vurguyu bir araya getirir; sayı başlangıcına ilişkin kayıt ise komşu sayı dalıyla sınır oluşturur.","sources":["MQ","SI","MU"],"what_is_ar":"أحد بمعنى الواحد، والوصف المطلق بأحد، وتكرار أحد أحد للتأكيد","what_is_not_ar":"ليس نفي الجنس ولا أحد عشر ولا يوم الأحد ولا جبل أُحُد"},"support_links":[]},{"boundary":"Bu dal yalnız olumsuz bağlamdaki kişi kapsamıdır; olumlu tekliği, sayı kuruluşlarını, gün adını ve dağ adını içermez.","branch_kind":"bare","branch_ref":"root_000017/B002","candidate_links":[{"candidate_id":"cand_adc65b573ffb57784cc7","lane":"macro"},{"candidate_id":"cand_a95f0954dad41bb50636","lane":"macro"},{"candidate_id":"cand_237d34934dd595db7ef7","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:5:1","qac_word_ref":"89:25:5","surface_ar":"أَحَدٌ"}],"gloss":"hiç kimse","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Olumsuzluk altında konuşmaya konu olabilecek kişiler türünün tamamını kapsar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin yanı sıra iki veya daha çok kişinin varlığını ya da katılımını da dışlar."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir yerde hiç kimsenin bulunmadığını veya bir eylemi hiç kimsenin yapmadığını söyleyen cümlelerde gerçekleşir."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Olumsuzluk altında kişi türünün tamamını, sayı ayrımı yapmadan dışlayan doğal dal karşılığıdır.","boundary_detail":"Bu dal yalnız olumsuz bağlamdaki kişi kapsamıdır; olumlu tekliği, sayı kuruluşlarını, gün adını ve dağ adını içermez.","branch_image_ar":"استغراق النفي","concept_gloss":"hiç kimse","contextual_glosses":[{"applicability":"Bir yerde kişi bulunmadığını bildiren varlık cümlelerinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir eyleme katılmama gibi yer bildirmeyen olumsuz bağlamları kapsamaz.","preserves":"Kişilerin tümünü olumsuzluk altında dışlama kapsamını korur."},"facet_ids":["F001","F002","F003"],"text":"hiç kimse yok","usage_role":"contextual"},{"applicability":"Belirli bir insan topluluğunun hiçbir üyesinin eyleme katılmadığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Belirsiz bir yerde insan bulunmaması gibi topluluğu belirtilmeyen bağlamları kapsamaz.","preserves":"Belirli bir topluluğun bütün üyelerini olumsuzluk kapsamına alır."},"facet_ids":["F001","F002"],"text":"aranızdan hiç kimse","usage_role":"contextual"}],"definition":"Olumsuz bir cümlede, söz konusu olabilecek kişilerden bir tekinin bile bulunmadığını ya da eyleme katılmadığını bildirir. Kapsam yalnız bir kişiyi değil, iki ve daha çok kişiyi de dışarıda bırakır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Olumsuzluk altında konuşmaya konu olabilecek kişiler türünün tamamını kapsar."},{"facet_id":"F002","role":"specialization","statement":"Bir kişinin yanı sıra iki veya daha çok kişinin varlığını ya da katılımını da dışlar."},{"facet_id":"F003","role":"example","statement":"Bir yerde hiç kimsenin bulunmadığını veya bir eylemi hiç kimsenin yapmadığını söyleyen cümlelerde gerçekleşir."}],"identity_rationale":"Kaynak ifadesi, sözcüğün olumsuzluk içinde konuşmaya konu olabilecek kişilerin bütün türünü kapsadığını ve yalnız tek kişiyi değil iki ya da daha çok kişiyi de dışladığını açıkça belirtir. Hazırlanan dal çerçevesi bu kapsamı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"olumsuzlukta hiç kimse"}],"lexicalization_note":"Tanım yalın birimin olumsuz cümledeki kapsamına bağlıdır ve başka bir söz öbeğine özgü anlamı bu dala taşımaz.","neighbor_coverage_note":"Adayların tümü gözden geçirildi; yer boşluğunu bildiren kalıplar, daha geniş yokluk kalıbı ve olumlu teklik dalı okur açısından en yararlı karşıtlıkları verdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişi türünü olumsuzlukla kapsayan genel birimdir; komşu dal ise belirli kalıplaşmış sözlerle yerin boşluğunu, bazen de iz yokluğunu anlatır.","focus_only":"Odak dal olumsuzluk altında kişi türünün tamamını düzenli bir dil bilgisel kapsamla dışlar.","gloss":"bir yerde kimse ya da iz bulunmaması","neighbor_only":"Komşu dal, bir yerde insanın ya da kimi kullanımlarda herhangi bir izin bulunmadığını bildiren kalıplaşmış sözleri kapsar.","neighbor_ref":"root_000075/B008","relation_type":"near_neighbor","shared_zone":"İki dal da bir yerde kişinin bulunmadığını söyleyebilir."},{"boundary_match":"partial","distinction":"Odak dalın alanı kişilerdir; komşu dalın kalıplaşmış kullanımı kişi dışındaki şeylere ve suya kadar genişleyebilir.","focus_only":"Odak dal yalnız konuşmaya konu olabilecek kişilerin tümünü dışlar.","gloss":"en küçük kişi ya da şeyin bile yokluğu","neighbor_only":"Komşu dal kalıplaşmış bir sözle kişi, herhangi bir şey veya su gibi farklı varlıkların en küçüğünü bile dışlayabilir.","neighbor_ref":"root_000187/B005","relation_type":"near_neighbor","shared_zone":"İki dal da olumsuzlukta en küçük bir örneğin bile bulunmadığını bildirebilir."},{"boundary_match":"partial","distinction":"Odak dalın anlamı olumsuzluk ve bütün kişileri kapsama koşuluna bağlıdır; komşu dal olumlu tekliği veya eşsizliği anlatır.","focus_only":"Odak dal olumsuzluk altında herhangi bir kişinin varlığını ya da katılımını dışlar.","gloss":"bir tane, tek ve eşsiz","neighbor_only":"Komşu dal olumlu biçimde bir tane, tek veya eşi olmayan olmayı bildirir.","neighbor_ref":"root_000017/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalın biçiminde bir kişiye ya da varlığa ilişkin birlik düşüncesi bulunur."}],"source_phrase_ar":"لا أحد في الدار؛ ما في الدار أحد (sihah); أحد في النفي لاستغراق جنس الناطقين ولا واحد ولا اثنان فصاعدا (mufradat); فما منكم من أحد عنه حاجزين (sihah;mufradat)","source_summary":"Kaynaklar olumsuzluk içindeki kullanımın kişi türünü bütünüyle kapsadığı konusunda birleşir. Böylece söz yalnız tek bir kişinin yokluğunu değil, o türe giren herhangi bir sayıda kişinin bulunmamasını da bildirir.","sources":["SI","MU"],"what_is_ar":"أحد في سياق النفي لاستغراق جنس من يصلح أن يخاطب، فيشمل الواحد وما فوقه","what_is_not_ar":"ليس إثبات الواحد ولا العدد المركب ولا علم الجبل"},"support_links":["sup_00fd087243ab7be0533d","sup_1c3bce9a96bb443ddb39","sup_c1b36ff6a9825dc288e6"]},{"boundary":"Bu dal sayı ve sayı kurma alanındadır; olumsuz kişi kapsamını, mutlak eşsizliği, gün adını ve özel dağ adını içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_000017/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:5:1","qac_word_ref":"89:25:5","surface_ar":"أَحَدٌ"}],"gloss":"bir sayısı, onlu kuruluşları ve on bire çıkarma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sayma dizisinin başlangıcındaki bir sayısını bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir sayısı on veya yirmi gibi onluklarla birleşerek on bir ve yirmi bir türü sayıları kurar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Eylem biçimi, bir topluluğun sayısını on bire çıkarma işlemini bildirir."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın sayıyı, onluklarla kurulan sayı biçimlerini ve on bire çıkarma eylemini birlikte temsil eder.","boundary_detail":"Bu dal sayı ve sayı kurma alanındadır; olumsuz kişi kapsamını, mutlak eşsizliği, gün adını ve özel dağ adını içermez.","branch_image_ar":"الواحد في العد والتركيب","concept_gloss":"bir sayısı, onlu kuruluşları ve on bire çıkarma","contextual_glosses":[{"applicability":"Sayma dizisinin ilk sayısını yalın olarak bildiren bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Onluklarla kurulan sayıları ve on bire çıkarma eylemini kapsamaz.","preserves":"Bir sayısının sayma başlangıcındaki değerini korur."},"facet_ids":["F001"],"text":"bir","usage_role":"contextual"},{"applicability":"Bir sayısının on veya yirmiyle kurduğu birleşik ya da bağlı sayı örneklerinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalın bir sayısını ve bir topluluğu on bire çıkarma eylemini kapsamaz.","preserves":"Bir sayısının onluklarla birleşerek sayı kurmasını korur."},"facet_ids":["F002"],"text":"on bir ya da yirmi bir","usage_role":"contextual"},{"applicability":"Bir topluluğun sayısını on bire ulaştıran eylem biçiminin doğal karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalın sayıyı ve onluklarla kurulan sayı adlarını kapsamaz.","preserves":"Bir topluluğu on bire ulaştırma işlemini ve sonucunu korur."},"facet_ids":["F003"],"text":"on bire çıkarmak","usage_role":"contextual"}],"definition":"Saymanın başlangıcındaki bir sayısını, bu sayının on ve yirmi gibi onluklarla birleşerek kurduğu sayıları ve bir topluluğu on bire çıkarma işlemini kapsar. Yalın sayı, birleşik sayı ve yapma eylemi birbirinden ayrı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sayma dizisinin başlangıcındaki bir sayısını bildirir."},{"facet_id":"F002","role":"extension","statement":"Bir sayısı on veya yirmi gibi onluklarla birleşerek on bir ve yirmi bir türü sayıları kurar."},{"facet_id":"F003","role":"associated_use","statement":"Eylem biçimi, bir topluluğun sayısını on bire çıkarma işlemini bildirir."}],"identity_rationale":"Kaynak ifadesi bir sayısını saymanın başlangıcı olarak, on ve yirmi gibi onluklarla kurulan sayılarda bir bileşen olarak ve bir kümeyi on bire çıkaran eylem biçiminde açıkça sunar. Dal çerçevesi bu üç kullanımı doğru biçimde ayırarak bir arada tutar.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"saymanın başlangıcındaki bir"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"on bir, on bir dişil biçimi ve yirmi bir"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"onları on bire çıkarmak"}],"lexicalization_note":"Tanım yalın bir sayısını, onluklarla kurulan söz öbeklerini ve on bire çıkarma biçimini ayrı yüzler olarak gösterir; söz öbeği anlamını yalın biçime yaymaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; onluklar, üç sayısı, teklik dalı ve üçe tamamlama dalı sayı alanının en açıklayıcı sınırlarını verdi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal kuruluş içindeki bir bileşenini ve on bire çıkarma eylemini izler; komşu dal ise onluk sayıların kendisini ve çevresindeki biçimleri izler.","focus_only":"Odak dal bir sayısını, onluklara eklenmesini ve on bire çıkarma işlemini merkez alır.","gloss":"on ve onluk sayılar","neighbor_only":"Komşu dal on, yirmi ve bunlara komşu onluk sayı sözlerini merkez alır.","neighbor_ref":"root_001016/B001","relation_type":"same_field","shared_zone":"İki dal on bir ve yirmi bir gibi sayı kuruluşlarında birlikte görünür."},{"boundary_match":"field_only","distinction":"Ortak alan sayı sistemidir, ancak merkez sayılar ve bunlardan kurulan biçimler farklıdır; birbirlerinin yerine kullanılamazlar.","focus_only":"Odak dal bir sayısını ve onun onluklarla kurduğu biçimleri kapsar.","gloss":"üç sayısı ve bağlı biçimleri","neighbor_only":"Komşu dal üç sayısını, onun sıra, dağıtma, yüzlük ve binlik gibi geniş türevlerini kapsar.","neighbor_ref":"root_000203/B001","relation_type":"same_field","shared_zone":"İki dal sayı adlarını ve bu adların düzenli kuruluşlarını işler."},{"boundary_match":"partial","distinction":"Odak dal sayı dizisi ve sayı kuruluşuyla sınırlıdır; komşu dal nitelik olarak tekliği ve eşsizliği merkez alır.","focus_only":"Odak dal sayma, onluklarla sayı kurma ve bir kümeyi on bire çıkarma görevlerini kapsar.","gloss":"tek ve eşi olmayan olma","neighbor_only":"Komşu dal tek ve eşi olmayan olmayı, mutlak nitelemeyi ve yinelemeli pekiştirmeyi kapsar.","neighbor_ref":"root_000017/B001","relation_type":"near_neighbor","shared_zone":"İki dal bir tane olma ve saymanın ilk basamağı çevresinde temas eder."},{"boundary_match":"partial","distinction":"Odak dalın merkez sayısı bir ve onlu kuruluşlarıdır; komşu dalın merkez sayısı beş, sıra değeri beşinci ve tamamlama sonucu beştir.","focus_only":"Odak dal bir sayısını, onun onluklarla kurduğu sayıları ve bir topluluğu on bire çıkarma işlemini bildirir.","gloss":"beş, beşinci ve beşe tamamlama","neighbor_only":"Komşu dal beş sayısını, beşinci olmayı, beş kişiden birini ve bir topluluğu beşe tamamlamayı bildirir.","neighbor_ref":"root_000439/B001","relation_type":"near_neighbor","shared_zone":"İki dal sayı adı, sıra içindeki yer ve bir topluluğu belirli sayıya ulaştırma alanlarında temas eder."}],"source_phrase_ar":"أحد واثنان وأحد عشر وإحدى عشرة (sihah); الواحد المضموم إلى العشرات نحو أحد عشر وأحد وعشرين (mufradat); فأحدهن أي صيرهن أحد عشر (sihah)","source_summary":"Kaynakların ortak kaydı bir sayısının hem sayma dizisindeki yalın yerini hem de onluklarla kurduğu sayıları gösterir. Aynı kanıt, ayrı bir eylem biçiminde bir kümeyi on bire çıkarma sonucunu da korur.","sources":["SI","MU"],"what_is_ar":"أحد في العد، وتركيبه مع العشرات، وتصْيير المعدود أحد عشر","what_is_not_ar":"ليس نفي الجنس ولا الأحدية المطلقة ولا يوم الأحد"},"support_links":[]},{"boundary":"Ad öbeğindeki seçme veya ilk olma kullanımı ile haftanın gün adı ayrı yüzlerdir; sayı kuruluşları ve dağ adı bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000017/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:5:1","qac_word_ref":"89:25:5","surface_ar":"أَحَدٌ"}],"gloss":"iki kişiden biri, ilk olan ve haftanın ilk günü","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir ad öbeği içinde iki kişiden birini ayırır veya bağlama göre ilk olanı gösterir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gün sözüyle kurulan söz öbeği haftanın ilk gününü ve o günün özel adını bildirir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kaynak ifadesi haftanın bu gününe verilen adın çoğul biçimini de kaydeder."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ad öbeğindeki seçme ya da ilk olma işlevini ve gün adıyla sınırlı takvim kullanımını birlikte temsil eder.","boundary_detail":"Ad öbeğindeki seçme veya ilk olma kullanımı ile haftanın gün adı ayrı yüzlerdir; sayı kuruluşları ve dağ adı bu dala girmez.","branch_image_ar":"الأول والإضافة","concept_gloss":"iki kişiden biri, ilk olan ve haftanın ilk günü","contextual_glosses":[{"applicability":"İki kişilik bir topluluktan herhangi bir üyeyi ad öbeği içinde ayıran bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sıra bakımından ilk olmayı, gün adını ve gün adının çoğulunu kapsamaz.","preserves":"İki kişiden birini seçme işlevini korur."},"facet_ids":["F001"],"text":"ikinizden biri","usage_role":"contextual"},{"applicability":"Haftanın ilk gününün Türkçedeki yerleşik adını gerektiren takvim bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İki kişiden birini ayırma işlevini ve çoğul gün adı biçimini kapsamaz.","preserves":"Haftanın ilk gününün özel gün adı olma işlevini korur."},"facet_ids":["F002"],"text":"Pazar günü","usage_role":"contextual"},{"applicability":"Gün adının çoğul ya da yinelenen günler anlamındaki kullanımını karşılar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek bir günü ve iki kişiden birini ayırma işlevini kapsamaz.","preserves":"Gün adının çoğul kullanımını korur."},"facet_ids":["F003"],"text":"Pazar günleri","usage_role":"contextual"}],"definition":"Bir ad öbeğinin parçası olduğunda iki kişiden birini seçer veya bağlama göre ilk olanı bildirir. Gün adıyla kurulan kullanımda haftanın ilk gününü ve bu günün özel adını, ayrıca gün adının çoğul biçimini kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir ad öbeği içinde iki kişiden birini ayırır veya bağlama göre ilk olanı gösterir."},{"facet_id":"F002","role":"specialization","statement":"Gün sözüyle kurulan söz öbeği haftanın ilk gününü ve o günün özel adını bildirir."},{"facet_id":"F003","role":"source_variant","statement":"Kaynak ifadesi haftanın bu gününe verilen adın çoğul biçimini de kaydeder."}],"identity_rationale":"Kaynak ifadesi bir ad öbeği içinde bir kişiyi ayıran ya da ilk olanı bildiren kullanımla haftanın ilk gününün adını birlikte verir ve gün adının çoğulunu da kaydeder. Hazırlanan çerçeve kullanılabilir, ancak iki kişiden birini seçme anlamı her bağlamda sıra bakımından ilk olmayı zorunlu kılmaz.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ikinizden biri"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"Pazar günü"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"Pazar günleri"}],"lexicalization_note":"Tanım ad öbeğine bağlı seçme kullanımını, gün adı söz öbeğini ve gün adının çoğul biçimini ayırır; bunları yalın kökün tek bir genel anlamına dönüştürmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ilk olma alanındaki komşu ile üç farklı gün adı ve sayı dalı, dalın hem sıra hem takvim sınırlarını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ilk olma yüzü belirli ad öbeklerine ve gün adına bağlıdır; komşu dal ise nesnelerin ön, üst ve başlangıç bölümlerine uzanan daha geniş bir öncelik alanıdır.","focus_only":"Odak dal ad öbeğinde iki kişiden birini ayırmayı ve haftanın ilk gününün adını da kapsar.","gloss":"ön, üst ve ilk bölüm","neighbor_only":"Komşu dal bir nesnenin önü, üstü ya da başlangıcı gibi uzamsal ve sıralı öncelikleri geniş biçimde kapsar.","neighbor_ref":"root_000849/B002","relation_type":"near_neighbor","shared_zone":"İki dal sıra bakımından ilk veya önde olanı gösterebilir."},{"boundary_match":"field_only","distinction":"Ortak alan haftanın günleridir, ancak gösterdikleri günler farklıdır ve gün adları birbirinin yerine geçmez.","focus_only":"Odak dal haftanın ilk gününün adını ve bu adın çoğulunu kapsar.","gloss":"Salı günü","neighbor_only":"Komşu dal Salı gününün adını ve onun tekil ile çoğul biçimlerini kapsar.","neighbor_ref":"root_000203/B006","relation_type":"same_field","shared_zone":"İki dal haftanın belirli bir gününe verilen adı ve adın sayı biçimlerini işler."},{"boundary_match":"field_only","distinction":"Odak dal ilk güne, komşu dal beşinci güne işaret eder; ortak takvim alanına karşın gösterdikleri gün ayrıdır.","focus_only":"Odak dal haftanın ilk gününü ve adını bildirir.","gloss":"Perşembe günü","neighbor_only":"Komşu dal haftanın beşinci gününün yerleşik adını bildirir.","neighbor_ref":"root_000439/B004","relation_type":"same_field","shared_zone":"İki dal haftanın gün adları dizgesine aittir."},{"boundary_match":"field_only","distinction":"Aynı takvim alanındadırlar, fakat haftanın farklı günlerini gösterirler ve odak dal ayrıca ad öbeğinde birini ayırma işlevi taşır.","focus_only":"Odak dal haftanın ilk gününü, adını ve çoğul biçimini kapsar.","gloss":"Çarşamba günü","neighbor_only":"Komşu dal Çarşamba gününün adını, söyleniş ayrıntısını ve çoğulunu kapsar.","neighbor_ref":"root_000536/B010","relation_type":"same_field","shared_zone":"İki dal bir hafta gününün adı ve çoğul kullanımı çevresinde buluşur."},{"boundary_match":"partial","distinction":"Odak dal seçme, sıra ve gün adı yapılarıyla sınırlıdır; komşu dal sayma ve sayı oluşturma işlemleriyle sınırlıdır.","focus_only":"Odak dal ad öbeğinde bir kişiyi ayırma ve haftanın ilk gününü adlandırma işlevlerini taşır.","gloss":"bir sayısı ve onlu sayı kuruluşları","neighbor_only":"Komşu dal bir sayısını, onluklarla sayı kurmayı ve bir topluluğu on bire çıkarmayı taşır.","neighbor_ref":"root_000017/B003","relation_type":"near_neighbor","shared_zone":"İki dal bir ve ilk düşüncelerinde temas eder."}],"source_phrase_ar":"أن يستعمل مضافا أو مضافا إليه بمعنى الأول (mufradat); أما أحدكما (mufradat); يوم الأحد أي يوم الأول (mufradat); يوم الأحد يجمع على آحاد (sihah)","source_summary":"Kaynakların birleşik kaydı, ad öbeği içindeki birini ayırma veya ilk sayma işlevini haftanın ilk gününün adıyla ilişkilendirir. Gün adının çoğul biçimi de aynı kanıt içinde korunur.","sources":["SI","MU"],"what_is_ar":"أحد مضافا أو مضافا إليه بمعنى الأول، واسم يوم الأحد","what_is_not_ar":"ليس أحد عشر ولا لا أحد ولا جبل أُحُد"},"support_links":[]},{"boundary":"Bu dal tek başına kalma ve ayrı ayrı hareket etme olaylarıdır; sayısal biri, olumsuz kişi kapsamını ve özel adları içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_000017/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:5:1","qac_word_ref":"89:25:5","surface_ar":"أَحَدٌ"}],"gloss":"tek başına kalma ve birer birer gelme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin bir işi başkalarından ayrı olarak üstlenmesini veya tek başına kalmasını bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir topluluğun üyelerinin toplu halde değil, ayrı ayrı ve birer birer gelmesini bildirir."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bireyin yalnızlaşmasını veya işi yalnız üstlenmesini ve topluluğun ayrı ayrı gelişini birlikte temsil eder.","boundary_detail":"Bu dal tek başına kalma ve ayrı ayrı hareket etme olaylarıdır; sayısal biri, olumsuz kişi kapsamını ve özel adları içermez.","branch_image_ar":"الانفراد والتفرق آحادا","concept_gloss":"tek başına kalma ve birer birer gelme","contextual_glosses":[{"applicability":"Bir kişinin başkalarından ayrılarak yalnız kalmasını bildiren bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir işi yalnız üstlenme ayrıntısını ve topluluğun birer birer gelişini kapsamaz.","preserves":"Bireyin başkalarından ayrı ve yalnız duruma gelmesini korur."},"facet_ids":["F001"],"text":"tek başına kalmak","usage_role":"contextual"},{"applicability":"Bir kişinin belirli bir işi başkalarının katılımı olmadan üstlendiği bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel tek başına kalmayı ve topluluğun ayrı ayrı gelişini kapsamaz.","preserves":"Bir işi başkalarından ayrı olarak üstlenme ilişkisini korur."},"facet_ids":["F001"],"text":"işi yalnız üstlenmek","usage_role":"contextual"},{"applicability":"Bir topluluğun üyelerinin toplu halde değil, ayrı ayrı geldiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bireyin bir işi yalnız üstlenmesini veya tek başına kalmasını kapsamaz.","preserves":"Ayrı ayrı ve birer birer geliş biçimini korur."},"facet_ids":["F002"],"text":"birer birer gelmek","usage_role":"contextual"}],"definition":"Bir kişinin bir işi başkalarından ayrı olarak yalnız üstlenmesi ya da tek başına kalmasıdır. Topluluk için kullanıldığında kişilerin toplu değil, ayrı ayrı ve birer birer gelmesini bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin bir işi başkalarından ayrı olarak üstlenmesini veya tek başına kalmasını bildirir."},{"facet_id":"F002","role":"extension","statement":"Bir topluluğun üyelerinin toplu halde değil, ayrı ayrı ve birer birer gelmesini bildirir."}],"identity_rationale":"Kaynak ifadesi kişinin bir işi yalnız üstlenmesi ya da tek başına kalması ile insanların ayrı ayrı, birer birer gelmesini açıkça birbirine bağlı iki kullanım olarak verir. Hazırlanan dal bu eylem ve dağılım ayrımını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"tek başına kalmak; işi yalnız üstlenmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"birer birer, ayrı ayrı"}],"lexicalization_note":"Tanım türemiş eylem biçimindeki yalnızlaşmayı ve yinelemeli dağılım sözündeki birer birer gelişi ayrı yüzler olarak tutar; ikisini yalın kök anlamı saymaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; yana çekilme, dağınık bulunma, yönlere dağılma ve benzeri az tek örnek dalları süreç ile nitelik sınırlarını en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnız üstlenme ile birer birer gelişe uzanır; komşu dal ise yana çekilme ve konumsal ayrılmayı daha belirgin biçimde taşır.","focus_only":"Odak dal bir işi yalnız üstlenmeyi ve topluluğun birer birer gelişini de kapsar.","gloss":"yana çekilme ve topluluktan ayrılma","neighbor_only":"Komşu dal topluluktan yana çekilmeyi, yer değiştirmeyi ve ayrı bir konumda bulunmayı kapsar.","neighbor_ref":"root_000305/B004","relation_type":"near_synonym","shared_zone":"İki dal bir kişinin topluluktan ayrılıp tek başına bulunmasını anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal birer birer geliş biçimini ve bireysel yalnızlaşmayı belirtir; komşu dal yalnız topluluğun dağılmış durumunu kalıplaşmış biçimde bildirir.","focus_only":"Odak dal bireyin yalnızlaşmasını ve kişilerin birer birer gelişini kapsar.","gloss":"insanların dağılıp darmadağın olması","neighbor_only":"Komşu dal insanların genel olarak dağılmış ve darmadağın durumda bulunmasını anlatan kalıplaşmış bir sözdür.","neighbor_ref":"root_000154/B008","relation_type":"near_synonym","shared_zone":"İki dal bir topluluğun üyelerinin birlikte değil, dağınık durumda bulunmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal gelişin birer birer oluşunu ve bireysel yalnızlaşmayı da içerir; komşu dal yönlere dağılıp gitme olayına bağlıdır.","focus_only":"Odak dal tek başına kalmayı ve ayrı ayrı gelmeyi bildirir.","gloss":"farklı yönlere dağılıp gitmek","neighbor_only":"Komşu dal topluluğun farklı yönlere giderek dağılmasını bildiren kalıplaşmış bir anlatımdır.","neighbor_ref":"root_001331/B008","relation_type":"near_synonym","shared_zone":"İki dal bir topluluğun üyelerinin birbirinden ayrılarak dağılmasını kapsar."},{"boundary_match":"partial","distinction":"Odak dal insanların yalnızlaşma ya da ayrı ayrı hareket etme sürecini bildirir; komşu dal ise belirli bir hayvanın tek başına oluşunu adlandıran türle sınırlı bir kullanımdır.","focus_only":"Odak dal yalnızlaşma sürecini veya kişilerin ayrı ayrı hareket etmesini anlatır.","gloss":"topluluktan ayrı duran tek hayvan","neighbor_only":"Komşu dal belirli yaban hayvanlarının topluluktan ayrı duran tek üyesini adlandırır.","neighbor_ref":"root_000877/B009","relation_type":"near_neighbor","shared_zone":"İki dal bir canlının başkalarından ayrı ve tek başına bulunması düşüncesinde buluşur."}],"source_phrase_ar":"ما استأحدت بهذا الأمر أي ما انفردت به (maqayis); استأحد الرجل انفرد (sihah); جاءوا آحاد أحاد (sihah)","source_summary":"Kaynaklar tek başına kalma veya bir işi yalnız üstlenme anlamını birlikte destekler. Aynı kayıt, topluluğun üyelerinin ayrı ayrı ve birer birer gelişiyle bu çekirdeğin dağılımsal uzantısını da gösterir.","sources":["MQ","SI"],"what_is_ar":"الانفراد بالفعل، والمجيء آحادا أفرادا","what_is_not_ar":"ليس الواحد في العدد ولا نفي الجنس ولا علم الجبل"},"support_links":[]},{"boundary":"Bu dal yalnız belirli bir dağın özel adıdır; tek olma, olumsuz kişi kapsamı, sayı, gün adı ve yalnızlaşma anlamlarını taşımaz.","branch_kind":"non_bare","branch_ref":"root_000017/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:5:1","qac_word_ref":"89:25:5","surface_ar":"أَحَدٌ"}],"gloss":"Medine'deki belirli bir dağın özel adı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir dağın özel adı olarak tek bir coğrafi varlığı gösterir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dağın yeri kaynakta Medine ile ilişkilendirilmiştir."}}],"root_ar":"ء ح د","root_id":"root_000017","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel dağ anlamı yüklemeden, kaynakta Medine'de bulunduğu belirtilen tek coğrafi varlığın özel ad işlevini açıklar.","boundary_detail":"Bu dal yalnız belirli bir dağın özel adıdır; tek olma, olumsuz kişi kapsamı, sayı, gün adı ve yalnızlaşma anlamlarını taşımaz.","branch_image_ar":"جبل أُحُد","concept_gloss":"Medine'deki belirli bir dağın özel adı","contextual_glosses":[{"applicability":"Dağın kimliği bağlamdan zaten biliniyorsa, adı yeniden üretmeden özel ad işlevini açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kaynakta belirtilen kentle kurulan yer bağını açıkça taşımaz.","preserves":"Belirli bir dağın özel adı olma işlevini korur."},"facet_ids":["F001"],"text":"o dağın özel adı","usage_role":"explanatory"}],"definition":"Medine'de bulunan belirli bir dağa verilen özel addır. Genel olarak dağ türünü ya da dağın bir niteliğini değil, tek bir coğrafi varlığın kimliğini gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir dağın özel adı olarak tek bir coğrafi varlığı gösterir."},{"facet_id":"F002","role":"specialization","statement":"Dağın yeri kaynakta Medine ile ilişkilendirilmiştir."}],"identity_rationale":"Kaynak ifadesi bu birimi genel bir dağ türü olarak değil, belirli bir kentteki tek bir dağın özel adı olarak tanımlar. Hazırlanan dalın özel yer adı çerçevesi bu kanıtla doğrudan uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"Medine'deki dağın özel adı"}],"lexicalization_note":"Tanım yalnız kaynakta belirlenen özel dağ adına bağlıdır ve bu yer adı kullanımından genel bir dağ ya da yalın kök anlamı çıkarmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; başka dağ ve yer adları yalnız alan ortaklığı düzeyinde karşılaştırıldı, anlamdaşlık kurulmadı ve en açıklayıcı üç özel ad adayı yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Özel ad işlevleri aynı olsa da gösterdikleri coğrafi varlıklar ayrıdır; adlar birbirinin yerine kullanılamaz.","focus_only":"Odak dal kaynakta belirtilen kentteki belirli bir dağı adlandırır.","gloss":"başka bir dağın özel adı","neighbor_only":"Komşu dal başka bir belirli dağa verilen ayrı özel adı kapsar.","neighbor_ref":"root_000706/B006","relation_type":"same_field","shared_zone":"İki dal da genel dağ türünü değil, belirli bir dağın özel adını bildirir."},{"boundary_match":"field_only","distinction":"Aynı özel ad türüne girseler de farklı kentlerdeki farklı dağları gösterirler; kimlikleri ortak değildir.","focus_only":"Odak dal kaynakta belirtilen kentteki belirli dağı gösterir.","gloss":"başka bir kentteki tanınmış dağın adı","neighbor_only":"Komşu dal başka bir kentteki tanınmış dağı gösteren ayrı bir özel addır.","neighbor_ref":"root_000314/B006","relation_type":"same_field","shared_zone":"İki dal da bir kentle ilişkilendirilen tanınmış dağın özel adıdır."},{"boundary_match":"field_only","distinction":"Odak dal tek bir dağa bağlıdır; komşu dalın adı birden çok yer biçimine ve birden çok coğrafi varlığa uygulanabilir.","focus_only":"Odak dal yalnız tek bir belirli dağın özel adıdır.","gloss":"dağ ve tepeler için kullanılan başka bir yer adı","neighbor_only":"Komşu dal aynı adla anılan birden çok yer, dağ veya tepeyi kapsayabilir.","neighbor_ref":"root_000602/B002","relation_type":"same_field","shared_zone":"İki dal coğrafi varlıkları gösteren özel yer adları alanındadır."}],"source_phrase_ar":"أحد جبل بالمدينة (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak tanıklığı, birimi Medine'deki belirli dağın özel adı olarak kaydeder."}],"source_summary":"Bu dal genel bir sözlük anlamından çok, tek bir coğrafi varlığı gösteren özel ad kullanımını kapsar. Kaynak kaydı, gösterilen varlığın Medine'de bulunan dağ olduğunu bildirir.","sources":["SI"],"what_is_ar":"اسم جبل بالمدينة","what_is_not_ar":"ليس معنى الواحد ولا النفي ولا الاستئحاد"},"support_links":[]},{"boundary":"Çekirdek tat ve tüketim hoşluğudur; cezalandırma, yeme içmeden kesilme ve sudaki yabancı madde bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000994/B001","candidate_links":[{"candidate_id":"cand_abf48fd018bde284a94b","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:25:3:1","qac_word_ref":"89:25:3","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:4:1","qac_word_ref":"89:25:4","surface_ar":"عَذَابَ"}],"gloss":"tatlı ve kolay tüketilen yiyecek ya da içecek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yiyecek veya içeceğin damakta hoş, tatlı ve kolay tüketilir olmasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Su söz konusu olduğunda hoş içimin yanında tuzlu olmama niteliği belirgindir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli yapılarda tatlı su edinme veya arama ve bir şeyi tatlı sayma anlatılır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir ikili adlandırma tükürük ile şarabı birlikte bu hoşluk niteliği altında anar."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yiyecek ve içeceklerdeki ortak tat ve tüketim hoşluğu çekirdeğini, suyun tuzlu olmaması dahil, birlikte karşılar.","boundary_detail":"Çekirdek tat ve tüketim hoşluğudur; cezalandırma, yeme içmeden kesilme ve sudaki yabancı madde bu dala girmez.","branch_image_ar":"العذوبة والطيب في الماء والمطعوم","concept_gloss":"tatlı ve kolay tüketilen yiyecek ya da içecek","contextual_glosses":[{"applicability":"Suyun tuzlu olmayıp hoş ve kolay içilmesini anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başka yiyecek ve içeceklere uzanan genel kapsamı dışarıda bırakır.","preserves":"Suyun tatlılığını ve hoş içimini eksiksiz korur."},"facet_ids":["F002"],"text":"tatlı ve içimi hoş su","usage_role":"contextual"},{"applicability":"Tatlı içme suyu bulma veya bir yerden böyle su sağlama yapılarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tatlı suyu amaç edinme ve onu sağlama işlemini korur."},"facet_ids":["F003"],"text":"tatlı su aramak","usage_role":"contextual"}],"definition":"Su başta olmak üzere bir yiyecek veya içeceğin tatlı, hoş ve kolay tüketilir olması; su için ayrıca tuzlu olmama niteliğini taşır. Bu niteliğe bağlı yapılar tatlı su edinmeyi, aramayı ya da bir şeyi tatlı saymayı anlatabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yiyecek veya içeceğin damakta hoş, tatlı ve kolay tüketilir olmasıdır."},{"facet_id":"F002","role":"specialization","statement":"Su söz konusu olduğunda hoş içimin yanında tuzlu olmama niteliği belirgindir."},{"facet_id":"F003","role":"associated_use","statement":"Belirli yapılarda tatlı su edinme veya arama ve bir şeyi tatlı sayma anlatılır."},{"facet_id":"F004","role":"source_variant","statement":"Bir ikili adlandırma tükürük ile şarabı birlikte bu hoşluk niteliği altında anar."}],"identity_rationale":"Yetkili ifade, suyun tatlı, hoş ve tuzlu olmayan niteliğini merkeze alırken kolay tüketilen başka yiyecek ve içecekleri de kapsar. Tatlı su arama, suyu tatlı bulma ve iki belirli sıvıyı birlikte adlandırma kullanımları bu niteliğe bağlı yan kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tatlı, hoş ve kolay tüketilir"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"tatlılık ve içim hoşluğu"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"suları tatlılaştı veya tatlı suya kavuştular"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"tatlı içme suyu aradılar veya sağladılar"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"onu tatlı saydı"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"onun için şu kuyudan su çekilir"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birlikte anılan tükürük ve şarap"}],"lexicalization_note":"Tanım hem yalın nitelik bildiren biçimleri hem de tatlı su edinme, arama veya öyle sayma yapılarıyla sınırlı kullanımları ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tatlı su ve berrak içme suyu adayları sınırı en iyi gösterdiği için yayımlandı, ötekiler örnek, uzak alan veya aynı kökün ayrı dalıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal yalnız tatlı su alanında odak dalıyla örtüşür; odak dalının yiyecek-içecek genellemesi ve niteliğe bağlı işlemleri komşunun sınırını aşar.","focus_only":"Odak dalı su dışındaki kolay tüketilen yiyecek ve içecekleri, ayrıca tatlı su edinme ve değerlendirme yapılarını da kapsar.","gloss":"tatlı su","neighbor_only":null,"neighbor_ref":"root_001137/B001","relation_type":"near_synonym","shared_zone":"Her ikisi de tatlı, tuzlu olmayan ve hoş içilen suyu adlandırır."},{"boundary_match":"partial","distinction":"Odak dalında belirleyici eksen tatlılık ve tuzlu olmamadır; komşuda ise berraklıktan doğan içim kolaylığı öne çıkar.","focus_only":"Odak dalı berraklık şartı koymaz ve hoş tüketilen başka yiyecek ve içecekleri de kapsar.","gloss":"berrak ve kolay içilen su","neighbor_only":"Komşu dal içim kolaylığını özellikle suyun berraklığına bağlar.","neighbor_ref":"root_000638/B003","relation_type":"near_synonym","shared_zone":"Her ikisi de suyun zorlanmadan içilmesini ve damakta hoş olmasını kapsar."}],"source_phrase_ar":"عذب الماء عذوبة فهو عذب طيب (maqayis;ayn;tahdhib)؛ العذب ضد الملح وكل مستسيغ من طعام أو شراب (jamhara)؛ ماء عذب طيب بارد (mufradat)؛ استعذب القوم ماءهم إذا استقوه عذبا (sihah)","source_summary":"Kaynakların ortak çekirdeği tatlı, hoş ve kolay tüketilen su, yiyecek veya içecektir; su edinme, arama ve tatlı sayma kullanımları bu çekirdeğe bağlanır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الماء العذب الطيب والمستساغ من طعام أو شراب، والاستعذاب بمعنى طلب الماء العذب أو عده عذبا، وما ألحقته المصادر بالريق والخمر.","what_is_not_ar":"ليس العذاب والعقوبة، ولا الامتناع عن الأكل والشرب."},"support_links":["sup_96fc8008d6dc5ae0a6d0"]},{"boundary":"Bu dal başkasını engellemekten değil, kişinin veya hayvanın fiilen yemeyip içmemesinden söz eder.","branch_kind":"mixed_non_bare","branch_ref":"root_000994/B002","candidate_links":[{"candidate_id":"cand_4942998db392139bc3e2","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:25:3:1","qac_word_ref":"89:25:3","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:4:1","qac_word_ref":"89:25:4","surface_ar":"عَذَابَ"}],"gloss":"yemeden içmeden durma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan veya hayvan fiilen yiyecek ve içecek tüketmeden durur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvanda yememenin nedeni özellikle şiddetli susuzluk olabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hal, geceyi hiçbir şey yemeden ve içmeden geçirmek biçiminde anlatılabilir."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan veya hayvanın tüketmeme halini, nedeni ve süresi ayrıca belirtilebilen genel bir karşılıkla verir.","boundary_detail":"Bu dal başkasını engellemekten değil, kişinin veya hayvanın fiilen yemeyip içmemesinden söz eder.","branch_image_ar":"العذوب امتناع الجسد عن الأكل والشرب","concept_gloss":"yemeden içmeden durma","contextual_glosses":[{"applicability":"Şiddetli susuzluk yüzünden yemeyen hayvanın anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İçmeme bileşenini ve neden belirtilmeyen kullanımları açıkça söylemez.","preserves":"Susuzluğun yol açtığı yememe durumunu korur."},"facet_ids":["F002"],"text":"susuzluktan yemiyor","usage_role":"contextual"},{"applicability":"Tüketmeme halinin gece boyunca sürdüğünü anlatan yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yememeyi, içmemeyi ve gece boyunca sürmeyi birlikte korur."},"facet_ids":["F001","F003"],"text":"geceyi yemeden içmeden geçirdi","usage_role":"contextual"}],"definition":"Bir insanın veya hayvanın, çoğu kez şiddetli susuzluk yüzünden, hiçbir şey yemeden ve içmeden durmasıdır. Bu hal bir gece boyunca sürme veya yemek karşısında belirsiz bir ara durumda kalma biçiminde de anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan veya hayvan fiilen yiyecek ve içecek tüketmeden durur."},{"facet_id":"F002","role":"specialization","statement":"Hayvanda yememenin nedeni özellikle şiddetli susuzluk olabilir."},{"facet_id":"F003","role":"associated_use","statement":"Hal, geceyi hiçbir şey yemeden ve içmeden geçirmek biçiminde anlatılabilir."}],"identity_rationale":"Yetkili ifade hayvan ya da insanın yemeden ve içmeden durduğu bir hali açıkça bildirir. Şiddetli susuzluk sık bir neden olsa da tüm tanıklarda zorunlu değildir; bu yüzden hal, açlık duygusuna veya dinî oruca indirgenmez.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"susuzluktan yemedi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yiyip içmeden duran"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yiyip içmeden duran"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yemekten kaçınır"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"geceyi yemeden içmeden geçirdi"}],"lexicalization_note":"Tanım, hal bildiren biçimleri ve hayvanın, insanın ya da gecenin özne olduğu belirli yapıları ayırarak birlikte kapsar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; oruç, açlık ve aynı kökün alıkoyma dalı en olası karışmaları gösterir, öteki adaylar neden, sonuç veya daha uzak bedensel alanlardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak bir canlıda gözlenen yememe-içmeme halidir; komşu ise iradeli veya kurallı bir kaçınma uygulamasını ve daha geniş yasak alanını anlatır.","focus_only":"Odak, hayvanda susuzluktan doğabilen ve amaç ya da kural gerektirmeyen bir tüketmeme halini de kapsar.","gloss":"oruç tutma","neighbor_only":"Komşu, amaçlı veya kurallı perhizde yiyecek ve içecek dışındaki yasaklardan da kaçınmayı kapsar.","neighbor_ref":"root_000894/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da belirli bir süre yiyecek ve içecekten uzak durma vardır."},{"boundary_match":"partial","distinction":"Açlık mide boşluğu ve duyumdur; odak ise açlık duyulsun ya da duyulmasın, yememe ve içmeme davranışının sürmesidir.","focus_only":"Odak, içmemeyi ve özellikle susuzluğun yemeyi durdurduğu hayvan davranışını da içerir.","gloss":"açlık","neighbor_only":"Komşu, boş midenin yarattığı açlık duyusunu ve aç kişi halini merkez alır.","neighbor_ref":"root_000278/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal yiyecek tüketilmemesiyle bağlantılı bedensel bir durumu anlatır."},{"boundary_match":"partial","distinction":"Odak sonucu oluşan yeme-içmeme halini adlandırır; komşu ise yönelinen şeyden çekilme veya birini çekme işlemini anlatır.","focus_only":"Odak, belirli bir nesneye yönelik iradeli vazgeçiş olmadan da görülen bedensel tüketmeme halidir.","gloss":"vazgeçme veya alıkoyma","neighbor_only":"Komşu, herhangi bir işten vazgeçmeyi veya başkasını o işten alıkoymayı kapsar.","neighbor_ref":"root_000994/B003","relation_type":"near_neighbor","shared_zone":"Yemekten uzak durma bağlamında iki dal yüzeyde birbirine yaklaşabilir."}],"source_phrase_ar":"عذب الحمار يعذب عذبا وعذوبا فهو عاذب وعذوب لا يأكل من شدة العطش (maqayis;ayn)؛ العذوب من الدواب وغيرها القائم الذي لا يأكل ولا يشرب (sihah)؛ بات عذوبا إذا لم يأكل شيئا ولم يشرب (tahdhib)","source_summary":"Tanıklıklar, insan veya hayvanın yemeyip içmediği hali ortaklaştırır; şiddetli susuzluk bunun belirgin fakat her kullanım için zorunlu olmayan nedenidir.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه عذوب الحمار أو الفرس أو الرجل إذا لم يأكل ولم يشرب، خاصة من شدة العطش أو بوصف قائم لا يذوق شيئا.","what_is_not_ar":"ليس منع الغير عن الشيء ولا العذاب بمعنى العقوبة."},"support_links":["sup_5a7efe651f736329089e"]},{"boundary":"Dal, tüketmeme halini değil bir hedefe yönelişin kesilmesini veya kestirilmesini anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000994/B003","candidate_links":[{"candidate_id":"cand_4942998db392139bc3e2","lane":"macro"},{"candidate_id":"cand_9a1d17b5c90cd62cc8b6","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:25:3:1","qac_word_ref":"89:25:3","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:4:1","qac_word_ref":"89:25:4","surface_ar":"عَذَابَ"}],"gloss":"vazgeçme veya alıkoyma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Özne yöneldiği bir şeyden vazgeçer veya geri durur."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişi başkasını bir işten uzak tutar veya o işi ona bıraktırır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Alıkoyma, birini bir işten sütten keser gibi kesme biçiminde anlatılabilir."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın dönüşlü ve ettirgen iki katılımcı düzenini kısa ve doğal biçimde birlikte karşılar.","boundary_detail":"Dal, tüketmeme halini değil bir hedefe yönelişin kesilmesini veya kestirilmesini anlatır.","branch_image_ar":"الكف والمنع والفطام عن الشيء","concept_gloss":"vazgeçme veya alıkoyma","contextual_glosses":[{"applicability":"Öznenin bir konuyu veya davranışı kendi isteğiyle bıraktığı yapılarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öznenin yöneldiği şeyden geri durmasını korur."},"facet_ids":["F001"],"text":"ondan vazgeçti","usage_role":"contextual"},{"applicability":"Bir kişinin başka bir kişiyi belirli bir işten uzak tuttuğu yapılarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ettirgen katılımcı düzenini ve engellenen işi korur."},"facet_ids":["F002"],"text":"onu bu işten alıkoydu","usage_role":"contextual"}],"definition":"Bir şeyden vazgeçip ona yönelmeyi bırakmak veya bir başkasını o şeyden uzak tutup alıkoymaktır. Sütten kesmeye benzer biçimde bir alışkanlığı ya da işi kestirmek bu ikinci yönün özel bir anlatımıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Özne yöneldiği bir şeyden vazgeçer veya geri durur."},{"facet_id":"F002","role":"core","statement":"Bir kişi başkasını bir işten uzak tutar veya o işi ona bıraktırır."},{"facet_id":"F003","role":"specialization","statement":"Alıkoyma, birini bir işten sütten keser gibi kesme biçiminde anlatılabilir."}],"identity_rationale":"Yetkili ifade hem öznenin bir şeyden vazgeçmesini hem de bir başkasını ondan alıkoymasını açıkça bir araya getirir. Bir işten kesme ve sütten kesmeye benzetilen uzaklaştırma bu yön değişiminin özel gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"o şeyden vazgeçti"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kadınlardan söz etmekten kaçının"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"onu o işten alıkoydu"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"onu o işten kesti"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"senden vazgeçtim"}],"lexicalization_note":"Anlam belirli edatlı ve ettirgen yapılara bağlıdır; öznenin vazgeçmesi ile başkasını alıkoyması tanımda ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel geri durma ile geniş engelleme alanları yayımlandı, daha dar tutma ve ayırma adayları bunlara göre yinelenen ya da uzak kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak, belirli yapılarda kendi vazgeçişiyle başkasını alıkoymayı eşler; komşu daha genel geri çekilme ve yüz çevirme alanına yayılır.","focus_only":"Odak, başkasını bir işten kesme ve sütten kesmeye benzer ettirgen alıkoyma kullanımını açıkça içerir.","gloss":"geri durma ve bırakma","neighbor_only":"Komşu, geri çekilmenin yanında bir işi bir yana bırakma ve evde kalma gibi daha geniş uzak durma görünümlerine uzanır.","neighbor_ref":"root_000906/B004","relation_type":"near_synonym","shared_zone":"İki dal da bir şeye yönelişi kesme, ondan geri durma veya onu bırakma alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak yönelişin kesilmesine odaklanır; komşu ise fiziksel, hukuki veya kurumsal engel ve yasağı daha geniş bir çekirdek olarak taşır.","focus_only":"Odak, kişinin kendi isteğiyle vazgeçmesini ve kişisel bir ettirgen alıkoymayı kapsar.","gloss":"engelleme ve yasaklama","neighbor_only":"Komşu, giriş, çıkış veya eylem üzerinde engel, yasak, görevli ve yaptırım gibi kurumsal sınırlar da kurar.","neighbor_ref":"root_000002/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal bir kişinin belirli bir eylemi yapmasını önleme alanında buluşur."}],"source_phrase_ar":"أعذب عن الشيء إذا لها عنه وتركه (maqayis)؛ أعذب عن الشيء إذا امتنع عنه (jamhara;tahdhib)؛ أعذبته عن الأمر إذا منعته عنه (sihah)؛ عذبته تعذيبا كقولك فطمته عن هذا الأمر (ayn;tahdhib)","source_summary":"Ortak anlam, bir şeye yönelişi kesmektir; bu kesilme öznenin kendi vazgeçişi veya başka bir kişinin onu engellemesi biçiminde gerçekleşir.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه أعذب عن الشيء إذا تركه أو امتنع عنه، وأعذب غيره أو عذبه إذا منعه، والفطام عن أمر، وصيغة أعذبوا عن النساء في الذكر.","what_is_not_ar":"ليس العذوبة في الماء، ولا العقوبة والإيجاع."},"support_links":["sup_5a7efe651f736329089e","sup_da134ef25e532f8166a2"]},{"boundary":"Genel çıplaklıktan daha dardır: belirleyici koşul, varlıkla gökyüzü arasındaki üst örtünün yokluğudur.","branch_kind":"mixed_non_bare","branch_ref":"root_000994/B004","candidate_links":[{"candidate_id":"cand_9a1d17b5c90cd62cc8b6","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:25:3:1","qac_word_ref":"89:25:3","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:4:1","qac_word_ref":"89:25:4","surface_ar":"عَذَابَ"}],"gloss":"gökyüzüne karşı örtüsüz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Varlık ile gökyüzü arasında onu örten hiçbir engel bulunmaz."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu durum geceyi gökyüzüne açık ve örtüsüz geçirme örneğiyle anlatılır."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Üstünde hiçbir örtü olmadan doğrudan gökyüzüne açık kalan kişi veya nesne için kullanılır.","boundary_detail":"Genel çıplaklıktan daha dardır: belirleyici koşul, varlıkla gökyüzü arasındaki üst örtünün yokluğudur.","branch_image_ar":"العذوب المكشوف للسماء","concept_gloss":"gökyüzüne karşı örtüsüz","contextual_glosses":[{"applicability":"Birinin geceyi üstünde dam veya örtü bulunmadan geçirdiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geceleme olayını ve gökyüzüne açık kalmayı korur."},"facet_ids":["F001","F002"],"text":"geceyi açıkta geçirdi","usage_role":"contextual"}],"definition":"Bir varlığın kendisiyle gökyüzü arasında hiçbir dam, örtü veya siper bulunmadan açıkta kalmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Varlık ile gökyüzü arasında onu örten hiçbir engel bulunmaz."},{"facet_id":"F002","role":"example","statement":"Bu durum geceyi gökyüzüne açık ve örtüsüz geçirme örneğiyle anlatılır."}],"identity_rationale":"Yetkili ifade, bir varlık ile gökyüzü arasında hiçbir örtü bulunmamasını doğrudan bildirir. Aynı biçimlerin yememe-içmeme dalında da bulunması bu mekânsal anlamı değiştirmez.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"gökyüzüne karşı örtüsüz olan"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"gökyüzüne karşı örtüsüz olan"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"geceyi gökyüzüne açık geçirdi"}],"lexicalization_note":"Yalın durum bildiren biçimler ile geceyi gökyüzüne açık geçirme yapısı aynı mekânsal çekirdek altında, yapı sınırları korunarak verilir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel örtüsüzlük ile açık alan adayları sınırı en iyi gösterdi, öteki adaylar belirli yüzeyler, görünürlük veya uzak mekân ilişkileridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dikey olarak gökyüzüne açık kalma durumudur; komşu beden, yer ve hayvan üzerinde çok daha genel bir örtüsüzlük alanı kurar.","focus_only":"Odak özellikle üst örtünün yokluğunu ve gökyüzüne doğrudan açık olmayı şart koşar.","gloss":"çıplaklık ve örtüsüzlük","neighbor_only":"Komşu giysisizliği, genel örtüsüzlüğü, açık araziyi ve eyersiz hayvanı da kapsar.","neighbor_ref":"root_001004/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir varlığı örten veya gizleyen bir katmanın bulunmaması vardır."},{"boundary_match":"partial","distinction":"Odak kişinin veya nesnenin örtüsüz durumudur; komşu ise bulunulan yerin geniş ve açık oluşunu merkez alır.","focus_only":"Odak, yerdeki genişlikten bağımsız olarak bir varlığın üstünde örtü bulunmamasını anlatır.","gloss":"açık alan","neighbor_only":"Komşu, geniş ve açık bir alanı ve kişinin o alana çıkmasını adlandırır.","neighbor_ref":"root_000105/B002","relation_type":"near_neighbor","shared_zone":"Açık gökyüzü altında bulunma sahnesinde iki dal birlikte gerçekleşebilir."}],"source_phrase_ar":"العذوب الذي ليس بينه وبين السماء ستر وكذلك العاذب (maqayis;tahdhib)؛ فبات عذوبا للسماء كأنه سهيل (maqayis;tahdhib)","source_summary":"Tanıklıklar, gökyüzüyle kişi veya nesne arasında örtü bulunmayan açıkta kalma durumunda birleşir ve bunu geceleme örneğiyle gösterir.","sources":["MQ","TA"],"what_is_ar":"يدخل فيه العذوب أو العاذب الذي لا ستر بينه وبين السماء.","what_is_not_ar":"ليس مجرد الامتناع عن الطعام والشراب إلا حيث احتملته الشواهد."},"support_links":["sup_da134ef25e532f8166a2"]},{"boundary":"Çekirdek ağır acı çektirme veya cezadır; her güçlük kendiliğinden bu dala girmez ve bildirilen dayak kökeni tanımın şartı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000994/B005","candidate_links":[{"candidate_id":"cand_adc65b573ffb57784cc7","lane":"macro"},{"candidate_id":"cand_a95f0954dad41bb50636","lane":"macro"},{"candidate_id":"cand_237d34934dd595db7ef7","lane":"macro"},{"candidate_id":"cand_abf48fd018bde284a94b","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:25:3:1","qac_word_ref":"89:25:3","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:4:1","qac_word_ref":"89:25:4","surface_ar":"عَذَابَ"}],"gloss":"ağır acı çektirme ve cezalandırma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiye ağır acı verilir veya ağır bir ceza uygulanır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli bir yapı, bütünüyle yok etmeye yönelik cezayı anlatır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bildirilen bir görüş anlamı dayaktan başlatır ve sonra her ağır sıkıntıya genişletir."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem uygulanan ağır cezayı hem de birine şiddetli acı verme eylemini karşılayan çekirdek ifadedir.","boundary_detail":"Çekirdek ağır acı çektirme veya cezadır; her güçlük kendiliğinden bu dala girmez ve bildirilen dayak kökeni tanımın şartı değildir.","branch_image_ar":"العذاب إيلام وعقوبة","concept_gloss":"ağır acı çektirme ve cezalandırma","contextual_glosses":[{"applicability":"Eyleyenin başka bir kişiye şiddetli acı verdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eyleyeni, etkileneni ve ağır acının verilmesini korur."},"facet_ids":["F001"],"text":"ona ağır acı çektirdi","usage_role":"contextual"},{"applicability":"Cezanın hedefi bütünüyle ortadan kaldırmak olduğunda kullanılan özel karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Cezalandırmayı ve yok etmeye yönelik özel sonucu korur."},"facet_ids":["F002"],"text":"yok edici ceza","usage_role":"contextual"}],"definition":"Birine ağır acı çektirme veya onu ağır biçimde cezalandırmadır. Dayak kökeni ve anlamın her türlü ağır sıkıntıya yayılması, çekirdeğin parçası değil aktarılan bir açıklamadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiye ağır acı verilir veya ağır bir ceza uygulanır."},{"facet_id":"F002","role":"specialization","statement":"Belirli bir yapı, bütünüyle yok etmeye yönelik cezayı anlatır."},{"facet_id":"F003","role":"source_variant","statement":"Bildirilen bir görüş anlamı dayaktan başlatır ve sonra her ağır sıkıntıya genişletir."}],"identity_rationale":"Yetkili ifade ağır acı verme ve cezalandırma çekirdeğini doğrular. Bunun dayaktan türediği ve sonra her ağır sıkıntıya aktarıldığı açıklaması ortak zorunlu anlam değil, bildirilen bir köken ve genişleme görüşüdür; dal ancak bu kayıtla kabul edilebilir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"ağır acı ve ceza"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"ona ağır acı çektirdi veya ceza verdi"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"yok edici ceza"}],"lexicalization_note":"Tanım ad, eylem ve yok etmeye yönelik ceza yapısını ayırır; yapıya bağlı özel ceza bütün dala genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; acı verme, acı duyma ve sınanma adayları temel sınırları gösterdi, diğerleri belirli ceza türleri veya daha uzak şiddet sahneleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak ağır acı ve ceza eksenindedir; komşu ise şiddet veya ceza şartı olmadan acı verme eylemini ve acı verici niteliği kapsar.","focus_only":"Odak, acı vermenin yanında ağır ceza uygulamayı ve cezayı ad olarak da kapsar.","gloss":"acı verme veya acı verici olma","neighbor_only":"Komşu, bir şeyin veya kişinin acı verici olduğunu nitelemeyi de kapsar.","neighbor_ref":"root_000046/B002","relation_type":"near_synonym","shared_zone":"İki dal da başka bir kişide acı meydana getirme alanında doğrudan örtüşür."},{"boundary_match":"partial","distinction":"Odak acının uygulanması ve cezalandırma yönündedir; komşu ise etkilenen kişinin acıyı hissetmesi durumudur.","focus_only":"Odak, acının bir başkasına uygulanmasını ve bunun ceza niteliği taşımasını içerir.","gloss":"acı duyma","neighbor_only":"Komşu, acıyı yaşayan kişinin bedensel veya ruhsal duyumunu merkez alır.","neighbor_ref":"root_000046/B001","relation_type":"near_neighbor","shared_zone":"Uygulanan ağır acı, etkilenen kişide acı duyumuna yol açar."},{"boundary_match":"partial","distinction":"Odakta acı verme ve ceza vardır; komşuda belirleyici unsur iyi veya kötü bir durumun sınama işlevi görmesidir.","focus_only":"Odak, birine ağır acı veya ceza uygulanmasını çekirdek edinir.","gloss":"sınanma ve sıkıntı","neighbor_only":"Komşu, sınanma niteliğindeki sıkıntıların yanında rahatlığı ve mal ya da çocuklarla sınanmayı da kapsar.","neighbor_ref":"root_001128/B004","relation_type":"near_neighbor","shared_zone":"Ağır sıkıntı veya ceza, iki dalın kesiştiği deneyim alanıdır."}],"source_phrase_ar":"العذاب يقال منه عذب تعذيبا وناس يقولون أصل العذاب الضرب ثم استعير ذلك في كل شدة (maqayis)؛ عذبت الرجل وغيره تعذيبا والاسم العذاب (jamhara)؛ العذاب العقوبة وقد عذبته تعذيبا (sihah)؛ العذاب هو الإيجاع الشديد (mufradat)","source_summary":"Ortak çekirdek ağır acı verme ve cezalandırmadır; dayak kökeni ile her ağır sıkıntıya yayılma ise zorunlu anlamdan ayrı, aktarılan bir açıklamadır.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه العذاب والعقوبة والإيجاع الشديد، والتعذيب، وما يذكره المصدر من أصل الضرب ثم استعارة كل شدة.","what_is_not_ar":"ليس الماء العذب ولا طرف السوط المسمى عذبة."},"support_links":["sup_00fd087243ab7be0533d","sup_1c3bce9a96bb443ddb39","sup_96fc8008d6dc5ae0a6d0","sup_c1b36ff6a9825dc288e6"]},{"boundary":"Dal, bir şeyin ince ucu veya ona bağlı sarkan parçadır; su kirliliği, ceza ve hayvanın ayakları bu kapsama girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000994/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:25:3:1","qac_word_ref":"89:25:3","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:4:1","qac_word_ref":"89:25:4","surface_ar":"عَذَابَ"}],"gloss":"ince uç veya sarkan bağlı parça","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kamçı veya dil gibi bir şeyin ince, dışa uzanan son bölümüdür."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir nesneye bağlanan veya ondan sarkan ip, kayış, bez ya da deri parçasıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ağaçta aynı biçimsel alan dışa uzanan dalı karşılar."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem doğal uçlarını hem de bir araca bağlanan ip, kayış, bez veya deri parçalarını kapsar.","boundary_detail":"Dal, bir şeyin ince ucu veya ona bağlı sarkan parçadır; su kirliliği, ceza ve hayvanın ayakları bu kapsama girmez.","branch_image_ar":"العذبة طرف أو علاقة متدلية","concept_gloss":"ince uç veya sarkan bağlı parça","contextual_glosses":[{"applicability":"Kamçının son bölümü ya da ona takılmış sarkan bağ anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kamçıya ait uç ve sarkan bağ seçeneklerini korur."},"facet_ids":["F001","F002"],"text":"kamçının ucu veya askısı","usage_role":"contextual"},{"applicability":"Ayakkabı bağı, eyer veya başka bir kayışın serbestçe sarkan ucunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kayışa bağlı olmayı, uç konumunu ve sarkmayı korur."},"facet_ids":["F002"],"text":"sarkan kayış ucu","usage_role":"contextual"}],"definition":"Bir nesnenin ince veya dışa uzanan ucu ya da ona bağlanıp sarkan ip, kayış, bez, deri veya dal parçasıdır. Belirli araç ve beden bölümlerinde parçanın yeri ve işlevi ayrıca belirlenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kamçı veya dil gibi bir şeyin ince, dışa uzanan son bölümüdür."},{"facet_id":"F002","role":"core","statement":"Bir nesneye bağlanan veya ondan sarkan ip, kayış, bez ya da deri parçasıdır."},{"facet_id":"F003","role":"extension","statement":"Ağaçta aynı biçimsel alan dışa uzanan dalı karşılar."}],"identity_rationale":"Yetkili ifade kamçı ve dil ucu gibi uçları; mızrağa bağlanan bez, teraziyi kaldıran ip, ayakkabı bağı ucu ve dal gibi uzanan ya da sarkan parçaları birlikte verir. Geçici çerçeve bu ortak biçimsel alanı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"kamçının ucu veya askısı"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"mızrak başına bağlanan bez"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"dilin ince ucu"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"teraziyi kaldıran ip"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"ağaç dalı"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"deve kamışının öndeki sivri ucu"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"ayakkabı bağının serbest ucu"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"kayışların uçları"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"eyerin arkasından sarkan deri parçası"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"ağıtçı kadının bezi"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"kamçıya askı yaptı"}],"lexicalization_note":"Anlam çoğunlukla belirtilen nesneyle kurulan yapılara bağlıdır; uç, bağ, bez, ip ve dal gerçekleşmeleri tek bir yalın ada indirgenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kamçı ve dil ucunu paylaşan aday ile sarkan bağ adayının ayrımı yayımlandı, diğerleri yalnız biçimsel benzerlik veya uzak parça ilişkisi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu uç ve çıkıntı çevresinde kalır; odak bu alanı aşarak çeşitli nesnelere bağlı veya onlardan sarkan ince parçaları da adlandırır.","focus_only":"Odak, uçların yanında mızrağa bağlanan bez, terazi ipi, dal ve sarkan kayış gibi bağlı parçaları da kapsar.","gloss":"uç veya uçtaki çıkıntı","neighbor_only":"Komşu, uçtaki belirgin düğüm veya çıkıntıyı özellikle öne çıkarır.","neighbor_ref":"root_000205/B005","relation_type":"near_synonym","shared_zone":"Kamçı ucu ve ona benzetilen dil ucu iki dalın doğrudan ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak uç ve bağlı ince parça düzenine dayanır; komşu saç örgüsü, en üst bölüm ve sarkan eklenti arasında daha geniş bir biçim alanı kurar.","focus_only":"Odak, araçların işlevli uçlarını ve terazi ipi ya da mızrak bezi gibi özel bağlı parçaları içerir.","gloss":"örgü, üst bölüm veya sarkan bağ","neighbor_only":"Komşu, saç örgüsünü ve bir şeyin en üst bölümünü de kapsar.","neighbor_ref":"root_000505/B009","relation_type":"near_neighbor","shared_zone":"Ayakkabı, kılıç veya eyerden sarkan bağ ve uzantılar iki dalda kesişir."}],"source_phrase_ar":"عذبة السوط طرفه (maqayis;tahdhib)؛ عذبة الرمح الخرقة التي تشد على رأسه (jamhara)؛ عذبة اللسان طرفه (jamhara;sihah;tahdhib)؛ عذبة الميزان الخيط الذي يرفع به (sihah;tahdhib)؛ عذبة الشجر غصنه (sihah;tahdhib)؛ عذبة شراك النعل المرسلة من الشراك (tahdhib)","source_summary":"Tanıklıklar uçta bulunan veya bir şeye bağlanıp sarkan ince parçaları ortaklaştırır; kamçı, dil, mızrak, terazi, ağaç ve ayakkabı bağı bunun belirli gerçekleşmeleridir.","sources":["MQ","JA","SI","TA"],"what_is_ar":"يدخل فيه طرف السوط واللسان، والخرقة أو السير المشدود، والخيط، والغصن، وأطراف السيور والشراك، وما كان من علاقة أو ذوابة متدلية.","what_is_not_ar":"ليس العذاب ولا العذوبة في الماء، ولا القوائم المسماة عذوبات الناقة."},"support_links":[]},{"boundary":"Bu dalın öğeleri genel kök anlamı gibi genişletilmemeli, birbirinin yerine geçebilen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtta verilen biçim veya bağlam sınırı içinde tutulmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000994/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:25:3:1","qac_word_ref":"89:25:3","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:4:1","qac_word_ref":"89:25:4","surface_ar":"عَذَابَ"}],"gloss":"yalıtık adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Suyun içinde çer çöp bulunur veya havuzun yüzeyini yosunsu bir tabaka kaplar."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Havuzdaki çer çöpü çıkarmak ya da yüzey tabakasını kırıp suyu görünür kılmak anlatılır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ayrı bir yapı, su başının çevresinde otlak veya ot bulunmamasını bildirir."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki dağınık veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu dalın öğeleri genel kök anlamı gibi genişletilmemeli, birbirinin yerine geçebilen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtta verilen biçim veya bağlam sınırı içinde tutulmalıdır.","branch_image_ar":"العذبة شوائب الماء أو سطحه","concept_gloss":"yalıtık adlandırmalar","contextual_glosses":[{"applicability":"Suda bulunan küçük yabancı maddeler veya bunların çokluğu anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Suyun içindeki küçük yabancı maddeyi ve çokluk olasılığını korur."},"facet_ids":["F001"],"text":"sudaki çer çöp","usage_role":"contextual"},{"applicability":"Suyun kendisini değil, çevresinde hayvanların otlayacağı bitki bulunmamasını anlatan ayrı yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Su başını ve çevresindeki otlak yokluğunu birlikte korur."},"facet_ids":["F003"],"text":"çevresinde otlak bulunmayan su başı","usage_role":"explanatory"}],"definition":"Bir kullanım kümesi sudaki çer çöpü veya havuz yüzeyindeki yosunsu tabakayı ve bunların temizlenmesini anlatır. Ayrı bir kullanım ise bir su başının çevresinde otlak ve ot bulunmadığını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Suyun içinde çer çöp bulunur veya havuzun yüzeyini yosunsu bir tabaka kaplar."},{"facet_id":"F002","role":"associated_use","statement":"Havuzdaki çer çöpü çıkarmak ya da yüzey tabakasını kırıp suyu görünür kılmak anlatılır."},{"facet_id":"F003","role":"source_variant","statement":"Ayrı bir yapı, su başının çevresinde otlak veya ot bulunmamasını bildirir."}],"identity_rationale":"Bu dal packet düzeyinde inceleme statüsünde tutulmuş sınır-riskli malzemeyi taşır. Kanıt, tek bir yalın kök imgesinden çok biçime veya özel kullanıma bağlı dağınık adlandırmaları gösterdiği için dal yapısal bölme şartı koşmadan sınırlı bir adlandırma kümesi olarak okunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"sudaki çer çöp veya yüzey tabakası"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"çer çöpü bol su"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"havuzundaki çer çöpü çıkar"},{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"havuzun yüzey tabakasını kır"},{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"çevresinde otlak bulunmayan su başı"}],"lexicalization_note":"Kapsam verilen biçim veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"العذبة القذاة وماء ذو عذب أي كثير القذى (sihah)؛ أعذب حوضك أي انزع ما فيه من القذى (sihah)؛ اضرب عذبة الحوض حتى يظهر الماء أي اضرب عرمضه (tahdhib)؛ ماء ما به عذبة أي لا رعي فيه ولا كلأ (tahdhib)","source_summary":"İnceleme statüsündeki kanıt, tek bir birleşik anlamdan çok biçime veya özel bağlama bağlı sınırlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["SI","TA"],"what_is_ar":"يدخل فيه العذبة بمعنى القذاة في الماء، وكثرة القذى، وإزالة ما في الحوض من القذى أو عرمضه، مع شاهد تهذيب عن ماء لا رعي فيه ولا كلأ.","what_is_not_ar":"ليس الماء العذب الطيب؛ بل مادة غير مرغوبة أو محيطة بالماء."},"support_links":[]},{"boundary":"Dal tat, su veya içim hoşluğu değil, kişinin iyi ve cömert karakterini bildirir.","branch_kind":"bare","branch_ref":"root_000994/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:25:3:1","qac_word_ref":"89:25:3","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:4:1","qac_word_ref":"89:25:4","surface_ar":"عَذَابَ"}],"gloss":"iyi ve cömert huylu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi iyi, cömert ve değerli bir karakter taşır."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin ahlaki karakterinin iyi, cömert ve değerli olduğunu bildiren genel karşılıktır.","boundary_detail":"Dal tat, su veya içim hoşluğu değil, kişinin iyi ve cömert karakterini bildirir.","branch_image_ar":"العذبي كريم الأخلاق","concept_gloss":"iyi ve cömert huylu","contextual_glosses":[{"applicability":"Kişinin karakterini doğal bir ad öbeği içinde anlatmak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İyi huyu, cömertliği ve kişi niteliğini korur."},"facet_ids":["F001"],"text":"iyi huylu ve cömert biri","usage_role":"general"}],"definition":"İyi, cömert ve değerli huylara sahip kişi niteliğidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi iyi, cömert ve değerli bir karakter taşır."}],"identity_rationale":"Yetkili ifade tek ve açık biçimde iyi, cömert ve değerli huylara sahip kişiyi niteler. Geçici çerçeve bu ahlaki kişilik niteliğini eksiksiz yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"iyi ve cömert huylu"}],"lexicalization_note":"Tanım yalnız yalın kişi niteliğini verir; komşu erdem adları veya belirli davranış kalıpları bu dala taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eşleşen iyi karakter dalı ile daha geniş erdemli olgunluk alanı yayımlandı, diğerleri cömertliğin özel görünümleri veya uzak kişi tipleridir.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kanıt sınırlarında iki dal arasında kapsam, katılımcı veya koşul farkı görünmez.","focus_only":null,"gloss":"iyi ve cömert huylu kişi","neighbor_only":null,"neighbor_ref":"root_001075/B003","relation_type":"synonym","shared_zone":"Her iki dal da kişiyi iyi ve cömert karakterli olması bakımından niteler."},{"boundary_match":"partial","distinction":"Odak yalın bir iyi ve cömert huy sıfatıdır; komşu daha geniş bir kişilik ve toplumsal olgunluk idealini adlandırır.","focus_only":"Odak doğrudan kişinin iyi ve cömert huylu oluşunu bildiren bir niteliktir.","gloss":"erdemli olgunluk","neighbor_only":"Komşu, toplumsal olarak kabul edilen insanlık ve olgunluk idealini ve bu niteliği edinme çabasını da kapsar.","neighbor_ref":"root_001409/B002","relation_type":"near_neighbor","shared_zone":"İyi karakter ve toplumca değer verilen davranış niteliği iki dalda kesişir."}],"source_phrase_ar":"العذبي الكريم الأخلاق (sihah)","source_summary":"Tek tanıklık kişiyi iyi ve cömert karakterli olarak niteleyen yalın bir sıfat anlamı verir.","sources":["SI"],"what_is_ar":"يدخل فيه وصف العذبي بمعنى الكريم الأخلاق.","what_is_not_ar":"ليس العذب بمعنى الطيب من الماء إلا من جهة اللفظ المشترك في المادة."},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"bare","branch_ref":"root_000994/B009","candidate_links":[{"candidate_id":"cand_f00fd46613cdfb4e1c0d","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:25:3:1","qac_word_ref":"89:25:3","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:4:1","qac_word_ref":"89:25:4","surface_ar":"عَذَابَ"}],"gloss":"biçime bağlı adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Doğumdan sonra çocuğun ardından döl yatağından bir madde çıkar."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı bir biçim kadının döl yatağını, yani doğacak çocuğun geliştiği organı adlandırır."}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"العذابة والرحم والخرج بعد الولد","concept_gloss":"biçime bağlı adlandırmalar","contextual_glosses":[{"applicability":"Çocuğun doğumunu izleyerek döl yatağından çıkan madde anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Maddenin doğumdan sonra ve döl yatağından çıkmasını korur."},"facet_ids":["F001"],"text":"doğumdan sonra çıkan madde","usage_role":"explanatory"},{"applicability":"Doğacak çocuğun geliştiği kadın organının doğrudan adlandırıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadına ait anatomik organ referentini korur."},"facet_ids":["F002"],"text":"kadının döl yatağı","usage_role":"contextual"}],"definition":"Bir anlam doğumdan sonra çocuğun ardından döl yatağından çıkan maddeyi bildirir. Ayrı bir anlam ise kadının döl yatağının kendisini adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Doğumdan sonra çocuğun ardından döl yatağından bir madde çıkar."},{"facet_id":"F002","role":"core","statement":"Ayrı bir biçim kadının döl yatağını, yani doğacak çocuğun geliştiği organı adlandırır."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_041","rendering_kind":"ordinary","target_gloss":"doğumdan sonra döl yatağından çıkan madde"},{"lexical_unit_id":"lu_042","rendering_kind":"ordinary","target_gloss":"kadının döl yatağı"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"العذب ما يخرج على أثر الولد من الرحم (tahdhib)؛ العذابة رحم المرأة (tahdhib)","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["TA"],"what_is_ar":"يدخل فيه العذب الخارج على أثر الولد من الرحم، والعذابة بمعنى الرحم.","what_is_not_ar":"ليس العذاب ولا العذوبة ولا العذبة الطرفية."},"support_links":["sup_cd126a40aea1e9b928c4"]},{"boundary":"This branch covers binding or tying something, and the bond, rope, or restraint used for that binding.","branch_kind":null,"branch_ref":"root_001623/B003","candidate_links":[{"candidate_id":"cand_adc65b573ffb57784cc7","lane":"macro"},{"candidate_id":"cand_237d34934dd595db7ef7","lane":"macro"}],"focus_root_occurrences":[],"gloss":"binding with a restraint","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الإيثاق والوثاق الذي يشد به","image_en":"binding with a restraint"}}],"root_ar":"و ث ق","root_id":"root_001623","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الإيثاق والوثاق الذي يشد به","image_en":"binding with a restraint","scope_ar":"يدخل فيه أوثقته وإيثاقا ووثاقا، وشد الشيء أو الأسير، والوثاق بوصفه حبلا أو كل ما يوثق به الشيء.","scope_en":"This branch covers binding or tying something, and the bond, rope, or restraint used for that binding."},"support_links":["sup_1c3bce9a96bb443ddb39","sup_c1b36ff6a9825dc288e6"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000043/B004","candidate_links":[{"candidate_id":"cand_4942998db392139bc3e2","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_3ba67664ae61ff8a5efc","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Consuming and taking property turns appetite into appropriation.","root":"ء ك ل","source_ref":"89:19","source_word_indices":["1","3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000043","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_5a7efe651f736329089e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000261/B001","candidate_links":[{"candidate_id":"cand_4942998db392139bc3e2","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_3ba67664ae61ff8a5efc","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Accumulation to fullness intensifies the asymmetry between private intake and refused provision.","root":"ج م م","source_ref":"89:20","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000261","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_5a7efe651f736329089e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000266/B003","candidate_links":[{"candidate_id":"cand_9a1d17b5c90cd62cc8b6","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a5e672b9bd80445d53c7","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The tree-screened garden provides the protected interior from which punitive exposure is excluded.","root":"ج ن ن","source_ref":"89:30","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000266","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_da134ef25e532f8166a2"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000281/B001","candidate_links":[{"candidate_id":"cand_a95f0954dad41bb50636","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6df9bb611383b6249f1f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Arrival turns sovereignty from a remote attribution into the immediate center of the scene.","root":"ج ي ء","source_ref":"89:22","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000281","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_00fd087243ab7be0533d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000281/B004","candidate_links":[{"candidate_id":"cand_a95f0954dad41bb50636","lane":"macro"},{"candidate_id":"cand_f00fd46613cdfb4e1c0d","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6df9bb611383b6249f1f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Bringing and making present the punitive destination supplies an executable scene with instrumental movement.","root":"ج ي ء","source_ref":"89:23","source_word_indices":["1"]},{"hft_ref":"hft_fe84c2e4b8b45a6885d9","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Bringing something forth and making it present supplies emergence into the transformed scene.","root":"ج ي ء","source_ref":"89:23","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000281","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_00fd087243ab7be0533d","sup_cd126a40aea1e9b928c4"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000334/B001","candidate_links":[{"candidate_id":"cand_4942998db392139bc3e2","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_3ba67664ae61ff8a5efc","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Urging toward an act marks the missing social impulse that should have moved provision outward.","root":"ح ض ض","source_ref":"89:18","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000334","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_5a7efe651f736329089e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000464/B001","candidate_links":[{"candidate_id":"cand_9a1d17b5c90cd62cc8b6","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a5e672b9bd80445d53c7","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Passage into an interior supplies admission among a receiving community.","root":"د خ ل","source_ref":"89:29","source_word_indices":["1"]},{"hft_ref":"hft_a5e672b9bd80445d53c7","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The repeated inward passage extends admission from community into destination.","root":"د خ ل","source_ref":"89:30","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000464","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_da134ef25e532f8166a2"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000482/B001","candidate_links":[{"candidate_id":"cand_f00fd46613cdfb4e1c0d","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_fe84c2e4b8b45a6885d9","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Repeated demolition of the earth supplies the violent transformation analogous to labor.","root":"د ك ك","source_ref":"89:21","source_word_indices":["3","5","6"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000482","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_cd126a40aea1e9b928c4"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000532/B001","candidate_links":[{"candidate_id":"cand_a95f0954dad41bb50636","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6df9bb611383b6249f1f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Lordship and dominion identify the unmatched source of command and measure.","root":"ر ب ب","source_ref":"89:22","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000532","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_00fd087243ab7be0533d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000544/B001","candidate_links":[{"candidate_id":"cand_9a1d17b5c90cd62cc8b6","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a5e672b9bd80445d53c7","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Return to a prior belonging supplies restored relation as the opposite of punitive severance.","root":"ر ج ع","source_ref":"89:28","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000544","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_da134ef25e532f8166a2"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000560/B002","candidate_links":[{"candidate_id":"cand_abf48fd018bde284a94b","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b32fbfa688bf6603bed3","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Sustaining nourishment gives the sensory polarity an economic and bodily stake.","root":"ر ز ق","source_ref":"89:16","source_word_indices":["7"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000560","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_96fc8008d6dc5ae0a6d0"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000569/B003","candidate_links":[{"candidate_id":"cand_9a1d17b5c90cd62cc8b6","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a5e672b9bd80445d53c7","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Mutual acceptance supplies a two-sided relation unavailable in the isolated punitive model.","root":"ر ض و","source_ref":"89:28","source_word_indices":["4","5"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000569","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_da134ef25e532f8166a2"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000871/B001","candidate_links":[{"candidate_id":"cand_a95f0954dad41bb50636","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6df9bb611383b6249f1f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Ordered straight ranks cast the present agents as arranged under command.","root":"ص ف ف","source_ref":"89:22","source_word_indices":["4","5"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000871","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_00fd087243ab7be0533d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000934/B001","candidate_links":[{"candidate_id":"cand_abf48fd018bde284a94b","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b32fbfa688bf6603bed3","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Tasting and taking food reconnect the focus root's palatability pole to the surrounding appetite sequence.","root":"ط ع م","source_ref":"89:18","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000934","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_96fc8008d6dc5ae0a6d0"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000934/B002","candidate_links":[{"candidate_id":"cand_4942998db392139bc3e2","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_3ba67664ae61ff8a5efc","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Feeding another supplies the withheld good rather than food as a merely private object.","root":"ط ع م","source_ref":"89:18","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000934","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_5a7efe651f736329089e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001378/B001","candidate_links":[{"candidate_id":"cand_4942998db392139bc3e2","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_3ba67664ae61ff8a5efc","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Gathering scattered shares into one holding supplies the totalizing direction of consumption.","root":"ل م م","source_ref":"89:19","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001378","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_5a7efe651f736329089e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001444/B009","candidate_links":[{"candidate_id":"cand_a95f0954dad41bb50636","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_6df9bb611383b6249f1f","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The angel branch supplies other agents who are present without becoming sovereign peers.","root":"م ل ك","source_ref":"89:22","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001444","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_00fd087243ab7be0533d"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001533/B005","candidate_links":[{"candidate_id":"cand_f00fd46613cdfb4e1c0d","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_fe84c2e4b8b45a6885d9","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Childbirth and postpartum emergence echo the focus's remote generative branch from the far side of punishment.","root":"ن ف س","source_ref":"89:27","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001533","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_cd126a40aea1e9b928c4"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001692/B001","candidate_links":[{"candidate_id":"cand_4942998db392139bc3e2","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_3ba67664ae61ff8a5efc","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A child severed from a sustaining guardian supplies the vulnerable endpoint of failed provision.","root":"ي ت م","source_ref":"89:17","source_word_indices":["5"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001692","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_5a7efe651f736329089e"]}],"candidate_inventory":[{"anchor_refs":["89:25"],"branch_refs":["root_000017/B002","root_000994/B005","root_001623/B003"],"candidate_id":"cand_adc65b573ffb57784cc7","commentary_obligation":"review","focus_branch_refs":["root_000017/B002","root_000994/B005"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_001623/B003"],"root_ids":[],"scope":"pericope","source_local_id":"G:Unmatched Binding and Punishment","source_type":"channel","support_ids":["sup_1bd8b35a6c4b10a61110","sup_66598efb5cbecdb292ae","sup_828ee17df7742d894b68","sup_a98b161412a5a26d0b07","sup_c1b36ff6a9825dc288e6"],"title":"Unmatched Binding and Punishment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:17","89:18","89:19","89:20","89:25"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:25","branch_refs":["root_000043/B004","root_000261/B001","root_000334/B001","root_000934/B002","root_000994/B002","root_000994/B003","root_001378/B001","root_001692/B001"],"candidate_id":"cand_4942998db392139bc3e2","commentary_obligation":"review","hft_ref":"hft_3ba67664ae61ff8a5efc","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_reciprocal_deprivation","source_type":"hft","support_ids":["sup_5a7efe651f736329089e"],"title":"delta_reciprocal_deprivation","trust":"legacy_unbound"},{"anchor_refs":["89:22","89:23","89:25"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:25","branch_refs":["root_000017/B002","root_000281/B001","root_000281/B004","root_000532/B001","root_000871/B001","root_000994/B005","root_001444/B009"],"candidate_id":"cand_a95f0954dad41bb50636","commentary_obligation":"review","hft_ref":"hft_6df9bb611383b6249f1f","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_sovereign_source_not_empty_scene","source_type":"hft","support_ids":["sup_00fd087243ab7be0533d"],"title":"delta_sovereign_source_not_empty_scene","trust":"legacy_unbound"},{"anchor_refs":["89:25","89:26"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:25","branch_refs":["root_000017/B002","root_000994/B005","root_001623/B003"],"candidate_id":"cand_237d34934dd595db7ef7","commentary_obligation":"review","hft_ref":"hft_0a867e6a5ca9402239ef","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_punishment_binding_pair","source_type":"hft","support_ids":["sup_1c3bce9a96bb443ddb39"],"title":"delta_punishment_binding_pair","trust":"legacy_unbound"},{"anchor_refs":["89:25","89:28","89:29","89:30"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:25","branch_refs":["root_000266/B003","root_000464/B001","root_000544/B001","root_000569/B003","root_000994/B003","root_000994/B004"],"candidate_id":"cand_9a1d17b5c90cd62cc8b6","commentary_obligation":"review","hft_ref":"hft_a5e672b9bd80445d53c7","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_exclusion_against_return_and_entry","source_type":"hft","support_ids":["sup_da134ef25e532f8166a2"],"title":"delta_exclusion_against_return_and_entry","trust":"legacy_unbound"},{"anchor_refs":["89:16","89:18","89:25"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:25","branch_refs":["root_000560/B002","root_000934/B001","root_000994/B001","root_000994/B005"],"candidate_id":"cand_abf48fd018bde284a94b","commentary_obligation":"review","hft_ref":"hft_b32fbfa688bf6603bed3","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_sweetness_reversal","source_type":"hft","support_ids":["sup_96fc8008d6dc5ae0a6d0"],"title":"outlier_sweetness_reversal","trust":"legacy_unbound"},{"anchor_refs":["89:21","89:23","89:25","89:27"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:25","branch_refs":["root_000281/B004","root_000482/B001","root_000994/B009","root_001533/B005"],"candidate_id":"cand_f00fd46613cdfb4e1c0d","commentary_obligation":"review","hft_ref":"hft_fe84c2e4b8b45a6885d9","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_cosmic_afterbirth","source_type":"hft","support_ids":["sup_cd126a40aea1e9b928c4"],"title":"outlier_cosmic_afterbirth","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_6b6e1c483af95acd25e5","connection_ref":"conn_f904571a324e9dce6701","note":"Supplies the favorable destination that frames the chapter's final contrast.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_7063d50f624ac136c43a","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"89:29","source_note":"Earlier surah judgment contrast, remote from entry among servants.","source_row_role":"ranked_review","source_target_component_ref":"89:25","source_target_components":["89:25"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:25"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:29","source_target_components":["89:29"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:29","target_evidence":{"arabic_uthmani":"فَٱدْخُلِى فِى عِبَٰدِى","ayah_ref":"89:29"},"target_ref":"89:29"},{"connection_evidence_ref":"conn_ev_fecedf208cdc162db51d","connection_ref":"conn_9577a80ac71155e5ef36","note":"Adjacent parallel: unmatched binding reinforces unmatched punishment.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_59b45a3331335ed409af","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"89:26","source_note":"Immediate parallel: unmatched punishment supplies the paired punitive frame.","source_row_role":"ranked_review","source_target_component_ref":"89:25","source_target_components":["89:25"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:25"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:26","source_target_components":["89:26"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:26","target_evidence":{"arabic_uthmani":"وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ","ayah_ref":"89:26"},"target_ref":"89:26"},{"connection_evidence_ref":"conn_ev_e9efd5dc2369efd1cad5","connection_ref":"conn_850eba23db5564b8bc5c","note":"Completes the chapter's favorable destination opposite the punitive scene.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_c1b7465b2129e2c75c0d","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"89:30","source_note":"Intensifies the immediate Jahannam contrast before the garden destination.","source_row_role":"ranked_review","source_target_component_ref":"89:25","source_target_components":["89:25"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:25"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:30","source_target_components":["89:30"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:30","target_evidence":{"arabic_uthmani":"وَٱدْخُلِى جَنَّتِى","ayah_ref":"89:30"},"target_ref":"89:30"},{"connection_evidence_ref":"conn_ev_797d77b05314126bf451","connection_ref":"conn_1254d0c95def5e1f2487","note":"Immediate scene-setting: Jahannam and belated remembrance precede the focus.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_774bdc50b523c950103b","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"89:23","source_note":"Immediate continuation: intensifies the punitive consequence once Jahannam is present.","source_row_role":"ranked_review","source_target_component_ref":"89:25","source_target_components":["89:25"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:25"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:23","source_target_components":["89:23"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:23","target_evidence":{"arabic_uthmani":"وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ","ayah_ref":"89:23"},"target_ref":"89:23"},{"connection_evidence_ref":"conn_ev_43c59c29f8dedd2288bc","connection_ref":"conn_464e1d1e559e9867a0e3","note":"Begins the nearby favorable address that contrasts with the punitive outcome.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_4c98ab1ea82f035fbdea","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"89:27","source_note":"Immediate judgment backdrop helps locate the address after accountability.","source_row_role":"ranked_review","source_target_component_ref":"89:25","source_target_components":["89:25"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:25"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:27","source_target_components":["89:27"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:27","target_evidence":{"arabic_uthmani":"يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ","ayah_ref":"89:27"},"target_ref":"89:27"},{"connection_evidence_ref":"conn_ev_280b95c57f59d900f263","connection_ref":"conn_a8abae3e6e0f041d72cc","note":"Links the chapter's neglect of the needy to the punitive setting.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_455259384da1a8c2e430","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"same_surah","source_direction_label":"no value","source_focus_ref":"89:18","source_note":"No discernible contribution to the focal care or provision question.","source_row_role":"ranked_review","source_target_component_ref":"89:25","source_target_components":["89:25"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:25"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:18","source_target_components":["89:18"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:18","target_evidence":{"arabic_uthmani":"وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ","ayah_ref":"89:18"},"target_ref":"89:18"},{"connection_evidence_ref":"conn_ev_af8fd83bab65f824759a","connection_ref":"conn_803b379112b9799b1bc4","note":"Completes the favorable return that contrasts with the focus.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_29dc65efce14b48bed30","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"89:28","source_note":"No direct addition; it continues the punishment contrast before the address.","source_row_role":"ranked_review","source_target_component_ref":"89:25","source_target_components":["89:25"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:25"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:28","source_target_components":["89:28"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:28","target_evidence":{"arabic_uthmani":"ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ","ayah_ref":"89:28"},"target_ref":"89:28"},{"connection_evidence_ref":"conn_ev_7a6ea6049ac7a8c3dbcb","connection_ref":"conn_a5f6e0c86e9984e404a6","note":"Sets up the chapter's correction of human judgments about favor.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_8e0cb4a351e10ed24aaf","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"89:15","source_note":"Places the passage's claims under eventual consequence without clarifying the present inference.","source_row_role":"ranked_review","source_target_component_ref":"89:25","source_target_components":["89:25"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:25"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:15","source_target_components":["89:15"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:15","target_evidence":{"arabic_uthmani":"فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ","ayah_ref":"89:15"},"target_ref":"89:15"},{"connection_evidence_ref":"conn_ev_d753dd98b615b75f1142","connection_ref":"conn_d8bf9509b6d0b38400ef","note":"Supplies the chapter's neglected-orphan charge before the focus.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_f9d3254584cafb704945","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"89:17","source_note":"Later punishment supplies only a distant consequence within the surah.","source_row_role":"ranked_review","source_target_component_ref":"89:25","source_target_components":["89:25"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:25"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"89:17","source_target_components":["89:17"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:17","target_evidence":{"arabic_uthmani":"كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ","ayah_ref":"89:17"},"target_ref":"89:17"},{"connection_evidence_ref":"conn_ev_3100c1d2d907b1e00880","connection_ref":"conn_14b0c61e5befe7d2fe66","note":"Immediate local correction of the human inference from constricted provision.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"89:16","source_target_components":["89:16"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:16","target_evidence":{"arabic_uthmani":"وَأَمَّآ إِذَا مَا ٱبْتَلَىٰهُ فَقَدَرَ عَلَيْهِ رِزْقَهُۥ فَيَقُولُ رَبِّىٓ أَهَٰنَنِ","ayah_ref":"89:16"},"target_ref":"89:16"},{"connection_evidence_ref":"conn_ev_7d502646272b0c1fa43d","connection_ref":"conn_544020702e125ecec995","note":"Immediate local charge of consuming inheritance without restraint.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":true,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_71a6afd209209d8a85bc","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"89:19","source_note":"The unmatched punishment follows the focus's judgment sequence, indirectly.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"89:25","source_target_components":["89:25"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:25"}],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"89:19","source_target_components":["89:19"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:19","target_evidence":{"arabic_uthmani":"وَتَأْكُلُونَ ٱلتُّرَاثَ أَكْلًۭا لَّمًّۭا","ayah_ref":"89:19"},"target_ref":"89:19"},{"connection_evidence_ref":"conn_ev_cf064f2c5447c672c8c0","connection_ref":"conn_fa49252e376a8bd2c1e3","note":"Immediate local charge of excessive attachment to wealth.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"89:20","source_target_components":["89:20"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:20","target_evidence":{"arabic_uthmani":"وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا","ayah_ref":"89:20"},"target_ref":"89:20"},{"connection_evidence_ref":"conn_ev_30f134bf02da406621a3","connection_ref":"conn_5d48ba1aa523b1e96c9c","note":"Introduces the Day's earth-shattering threshold before the focus.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"89:21","source_target_components":["89:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:21","target_evidence":{"arabic_uthmani":"كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا","ayah_ref":"89:21"},"target_ref":"89:21"},{"connection_evidence_ref":"conn_ev_2c39f7c7e74a99b65c14","connection_ref":"conn_4d58c44e37fc58dc1fcd","note":"Introduces the divine-and-angelic arrival before the focus.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"89:22","source_target_components":["89:22"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:22","target_evidence":{"arabic_uthmani":"وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا","ayah_ref":"89:22"},"target_ref":"89:22"},{"connection_evidence_ref":"conn_ev_ff65b29ef5f2e29f985c","connection_ref":"conn_71448e80a53ce314d425","note":"Immediate remorse supplies the human response on that Day.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"89:24","source_target_components":["89:24"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"89:24","target_evidence":{"arabic_uthmani":"يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى","ayah_ref":"89:24"},"target_ref":"89:24"}],"focus":{"arabic_uthmani":"فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"89:25:1:1","qac_word_ref":"89:25:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"يَوْمَئِذ","morph_features":"STEM|POS:T|LEM:yawoma}i*","morpheme_role":"STEM","pos":"T","qac_ref":"89:25:1:2","qac_word_ref":"89:25:1","root_ar":"","surface_ar":"يَوْمَئِذٍ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"89:25:2:1","qac_word_ref":"89:25:2","root_ar":"","surface_ar":"لَّا"},{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:25:3:1","qac_word_ref":"89:25:3","root_ar":"ع ذ ب","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:4:1","qac_word_ref":"89:25:4","root_ar":"ع ذ ب","surface_ar":"عَذَابَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:25:4:2","qac_word_ref":"89:25:4","root_ar":"","surface_ar":"هُۥٓ"},{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:5:1","qac_word_ref":"89:25:5","root_ar":"ء ح د","surface_ar":"أَحَدٌ"}],"word_analysis_qac_refs":[["89:25:1:1"],["89:25:1:2"],["89:25:2:1"],["89:25:3:1"],["89:25:4:1","89:25:4:2"],["89:25:5:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["89:25:1","89:25:2","89:25:3","89:25:4","89:25:5","89:25:6"]},"focus_surface_evidence":{"arabic_uthmani":"فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"89:25:1:1","qac_word_ref":"89:25:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"يَوْمَئِذ","morph_features":"STEM|POS:T|LEM:yawoma}i*","morpheme_role":"STEM","pos":"T","qac_ref":"89:25:1:2","qac_word_ref":"89:25:1","root_ar":"","surface_ar":"يَوْمَئِذٍ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"89:25:2:1","qac_word_ref":"89:25:2","root_ar":"","surface_ar":"لَّا"},{"lemma_ar":"عَذَّبَ","morph_features":"STEM|POS:V|IMPF|(II)|LEM:Ea*~aba|ROOT:E*b|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"89:25:3:1","qac_word_ref":"89:25:3","root_ar":"ع ذ ب","surface_ar":"يُعَذِّبُ"},{"lemma_ar":"عَذَاب","morph_features":"STEM|POS:N|LEM:Ea*aAb|ROOT:E*b|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:4:1","qac_word_ref":"89:25:4","root_ar":"ع ذ ب","surface_ar":"عَذَابَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:25:4:2","qac_word_ref":"89:25:4","root_ar":"","surface_ar":"هُۥٓ"},{"lemma_ar":"أَحَد","morph_features":"STEM|POS:N|LEM:>aHad|ROOT:AHd|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:25:5:1","qac_word_ref":"89:25:5","root_ar":"ء ح د","surface_ar":"أَحَدٌ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["89:25:1:1"],["89:25:1:2"],["89:25:2:1"],["89:25:3:1"],["89:25:4:1","89:25:4:2"],["89:25:5:1"]],"word_analysis_refs":["89:25:1","89:25:2","89:25:3","89:25:4","89:25:5","89:25:6"],"word_rows":[{"analysis_record_ref":"89:25:1","analytic_gloss_range_en":"resultive boundary particle joining the prior regret and judgment scene to the punishment clause","analytic_root_gloss_range_en":null,"qac_refs":["89:25:1:1"],"root":{},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"89:25:2","analytic_gloss_range_en":"deictic event-time, functioning as an accusative temporal frame for the punishment clause","analytic_root_gloss_range_en":"day can range from ordinary daylight to a marked event-time or the day-then construction; here the deictic judgment-event branch is selected","qac_refs":["89:25:1:2"],"root":{"arabic":"ي و م","transliteration":"y-w-m"},"surface":{"arabic":"يَوْمَئِذٍۢ","transliteration":"yawmaʾidhin"}},{"analysis_record_ref":"89:25:3","analytic_gloss_range_en":"declarative negator scoping over the imperfect punishment relation and the final indefinite","analytic_root_gloss_range_en":null,"qac_refs":["89:25:2:1"],"root":{},"surface":{"arabic":"لَّا","transliteration":"lā"}},{"analysis_record_ref":"89:25:4","analytic_gloss_range_en":"Form II imperfect punishment act under negation, with active agency in the standard reading and a passive qirāʾah contrast","analytic_root_gloss_range_en":"the root includes sweet freshness, abstention, withholding, exposedness, punishment, appendage, and other branches; the local Form II predicate selects the punishment and torment branch","qac_refs":["89:25:3:1"],"root":{"arabic":"ع ذ ب","transliteration":"ʿ-dh-b"},"surface":{"arabic":"يُعَذِّبُ","transliteration":"yuʿadhdhibu"}},{"analysis_record_ref":"89:25:5","analytic_gloss_range_en":"possessed verbal noun functioning as cognate measure or punishment standard, not an ordinary victim object","analytic_root_gloss_range_en":"the broad root includes sweet freshness and other branches, but this possessed verbal noun selects the punishment and penal consequence branch","qac_refs":["89:25:4:1","89:25:4:2"],"root":{"arabic":"ع ذ ب","transliteration":"ʿ-dh-b"},"surface":{"arabic":"عَذَابَهُۥٓ","transliteration":"ʿadhābahū"}},{"analysis_record_ref":"89:25:6","analytic_gloss_range_en":"indefinite singular under negation, functioning as final universal closure over possible participants","analytic_root_gloss_range_en":"oneness and single-individual range; under negation here it becomes distributive universal exclusion","qac_refs":["89:25:5:1"],"root":{"arabic":"أ ح د","transliteration":"ʾ-ḥ-d"},"surface":{"arabic":"أَحَدٌۭ","transliteration":"aḥadun"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":6,"words_total":6,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":14,"missing_anchor_refs":[],"supplied_unique_anchor_count":14},"assigned_record_count":6,"assigned_records":[{"anchor_refs":["89:17","89:18","89:19","89:20","89:25"],"branch_refs":["root_000043/B004","root_000261/B001","root_000334/B001","root_000934/B002","root_000994/B002","root_000994/B003","root_001378/B001","root_001692/B001"],"candidate_id":"cand_4942998db392139bc3e2","evidence_scope":"declared_pericope","hft_ref":"hft_3ba67664ae61ff8a5efc","item_id":"delta_reciprocal_deprivation","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_reciprocal_deprivation","support_id":"sup_5a7efe651f736329089e"},{"anchor_refs":["89:22","89:23","89:25"],"branch_refs":["root_000017/B002","root_000281/B001","root_000281/B004","root_000532/B001","root_000871/B001","root_000994/B005","root_001444/B009"],"candidate_id":"cand_a95f0954dad41bb50636","evidence_scope":"declared_pericope","hft_ref":"hft_6df9bb611383b6249f1f","item_id":"delta_sovereign_source_not_empty_scene","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_sovereign_source_not_empty_scene","support_id":"sup_00fd087243ab7be0533d"},{"anchor_refs":["89:25","89:26"],"branch_refs":["root_000017/B002","root_000994/B005","root_001623/B003"],"candidate_id":"cand_237d34934dd595db7ef7","evidence_scope":"declared_pericope","hft_ref":"hft_0a867e6a5ca9402239ef","item_id":"delta_punishment_binding_pair","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_punishment_binding_pair","support_id":"sup_1c3bce9a96bb443ddb39"},{"anchor_refs":["89:25","89:28","89:29","89:30"],"branch_refs":["root_000266/B003","root_000464/B001","root_000544/B001","root_000569/B003","root_000994/B003","root_000994/B004"],"candidate_id":"cand_9a1d17b5c90cd62cc8b6","evidence_scope":"declared_pericope","hft_ref":"hft_a5e672b9bd80445d53c7","item_id":"delta_exclusion_against_return_and_entry","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_exclusion_against_return_and_entry","support_id":"sup_da134ef25e532f8166a2"},{"anchor_refs":["89:16","89:18","89:25"],"branch_refs":["root_000560/B002","root_000934/B001","root_000994/B001","root_000994/B005"],"candidate_id":"cand_abf48fd018bde284a94b","evidence_scope":"declared_pericope","hft_ref":"hft_b32fbfa688bf6603bed3","item_id":"outlier_sweetness_reversal","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_sweetness_reversal","support_id":"sup_96fc8008d6dc5ae0a6d0"},{"anchor_refs":["89:21","89:23","89:25","89:27"],"branch_refs":["root_000281/B004","root_000482/B001","root_000994/B009","root_001533/B005"],"candidate_id":"cand_f00fd46613cdfb4e1c0d","evidence_scope":"declared_pericope","hft_ref":"hft_fe84c2e4b8b45a6885d9","item_id":"outlier_cosmic_afterbirth","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_cosmic_afterbirth","support_id":"sup_cd126a40aea1e9b928c4"}],"diagnostics":[],"lane_counts":{"global":13,"macro":6,"micro":4},"packet_summary":{"ayah_count":30,"focus_ref":"89:25","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000702","furuq_root_norm":"س ر ي","furuq_source_root_norm":"س ر ي","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000697","furuq_root_norm":"س ر ر","furuq_source_root_norm":"س ر ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ف ع ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001167","furuq_root_norm":"ف ع ل","furuq_source_root_norm":"ف ع ل","is_dominant":true,"target_occurrences":108,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000007","furuq_root_norm":"ء ب و","furuq_source_root_norm":"أ ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ع و د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":true,"target_occurrences":35,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ج و ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000273","furuq_root_norm":"ج و ب","furuq_source_root_norm":"ج و ب","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000283","furuq_root_norm":"ج ي ب","furuq_source_root_norm":"ج ي ب","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000220","furuq_root_norm":"ج ب ي","furuq_source_root_norm":"ج ب ي","is_dominant":false,"target_occurrences":2,"target_rank":3},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000214","furuq_root_norm":"ج ب ب","furuq_source_root_norm":"ج ب ب","is_dominant":false,"target_occurrences":1,"target_rank":4}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ب ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000153","furuq_root_norm":"ب ل و","furuq_source_root_norm":"ب ل و","is_dominant":true,"target_occurrences":28,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000154","furuq_root_norm":"ب ل ي","furuq_source_root_norm":"ب ل ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ه و ن","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001453","furuq_root_norm":"م ه ن","furuq_source_root_norm":"م ه ن","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001608","furuq_root_norm":"ه و ن","furuq_source_root_norm":"ه و ن","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001687","furuq_root_norm":"و ه ن","furuq_source_root_norm":"و ه ن","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ء ك ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000043","furuq_root_norm":"ء ك ل","furuq_source_root_norm":"أ ك ل","is_dominant":true,"target_occurrences":79,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001315","furuq_root_norm":"ك ل ل","furuq_source_root_norm":"ك ل ل","is_dominant":false,"target_occurrences":30,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14","89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"89:25","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":14,"unstructured_record_count":0},"identity":{"ayah_ref":"89:25","lane":"macro","linguistic_source_ref":"89:25","surface_ref":"89:25","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"89:25","target_tokens":[["O",["89:25:1"]],["gün",["89:25:1"]],["hiç",["89:25:5"]],["kimse",["89:25:5"]],["onun",["89:25:4"]],["azabı",["89:25:4"]],["gibi",["89:25:4"]],["azap",["89:25:3"]],["edemez",["89:25:2","89:25:3"]]],"text":"O gün hiç kimse onun azabı gibi azap edemez."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":6,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":15,"ayah_to":30,"id":"s089-p02-015-030","label":"The wealth test, judgment, and tranquil soul","number":2,"refs":["89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"89:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"89:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["89:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"89:0"}],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"G:Unmatched Binding and Punishment","source_type":"channel","support_id":"sup_1bd8b35a6c4b10a61110","text":"On the decisive day, no other agent matches the punishment or binding imposed.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"G:Unmatched Binding and Punishment","source_type":"channel","support_id":"sup_66598efb5cbecdb292ae","text":"Power establishes order, exceeds its bounds, watches for response, and imposes sanction.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"G:Unmatched Binding and Punishment","source_type":"channel","support_id":"sup_828ee17df7742d894b68","text":"89:25-26 (لا يعذب عذابه أحد، لا يوثق وثاقه أحد)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"G:Unmatched Binding and Punishment","source_type":"channel","support_id":"sup_a98b161412a5a26d0b07","text":"Repeated negation isolates one unmatched agent and pairs two sanctions: pain imposed and movement secured.","trust":"trusted"},{"branch_refs":["root_000017/B002","root_000994/B005","root_001623/B003"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"G:Unmatched Binding and Punishment","source_type":"channel","support_id":"sup_c1b36ff6a9825dc288e6","text":"exhaustive “no one” `ء ح د:B002/m01`; punishment `ع ذ ب:B005/m01`; binding `و ث ق:B003/m01`","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ","ayah_ref":"89:17"},{"arabic_uthmani":"وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ","ayah_ref":"89:18"},{"arabic_uthmani":"وَتَأْكُلُونَ ٱلتُّرَاثَ أَكْلًۭا لَّمًّۭا","ayah_ref":"89:19"},{"arabic_uthmani":"وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا","ayah_ref":"89:20"},{"arabic_uthmani":"فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ","ayah_ref":"89:25"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":5,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":5,"target_morphology_supplied":false},"branch_refs":["root_000043/B004","root_000261/B001","root_000334/B001","root_000934/B002","root_000994/B002","root_000994/B003","root_001378/B001","root_001692/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000994","role":"Going without food or drink gives the resulting punishment a bodily deprivation mode.","root":"ع ذ ب","source_ref":"89:25","source_word_indices":["3","4"]},{"branch_id":"B003","mapped_root_id":"root_000994","role":"Forcible withholding supplies the reciprocal operation applied by the changed reading.","root":"ع ذ ب","source_ref":"89:25","source_word_indices":["3","4"]},{"branch_id":"B001","mapped_root_id":"root_001692","role":"A child severed from a sustaining guardian supplies the vulnerable endpoint of failed provision.","root":"ي ت م","source_ref":"89:17","source_word_indices":["5"]},{"branch_id":"B001","mapped_root_id":"root_000334","role":"Urging toward an act marks the missing social impulse that should have moved provision outward.","root":"ح ض ض","source_ref":"89:18","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000934","role":"Feeding another supplies the withheld good rather than food as a merely private object.","root":"ط ع م","source_ref":"89:18","source_word_indices":["4"]},{"branch_id":"B004","mapped_root_id":"root_000043","role":"Consuming and taking property turns appetite into appropriation.","root":"ء ك ل","source_ref":"89:19","source_word_indices":["1","3"]},{"branch_id":"B001","mapped_root_id":"root_001378","role":"Gathering scattered shares into one holding supplies the totalizing direction of consumption.","root":"ل م م","source_ref":"89:19","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000261","role":"Accumulation to fullness intensifies the asymmetry between private intake and refused provision.","root":"ج م م","source_ref":"89:20","source_word_indices":["4"]}],"changed_reading":{"after":"Punishment can mirror the wrongdoing as enforced lack: hoarded access becomes inaccessible, and withheld sustenance returns as deprivation.","before":"Punishment is severe pain imposed for wrongdoing."},"confidence":"medium","mechanism":"The social sequence contrasts a dependent cut off from care and food not urged for another with aggressive consumption and total accumulation. This activates the focus's abstention and withholding branches as a reciprocal economy: punishment removes access from those who withheld and engulfed access.","model_id":"delta_reciprocal_deprivation","reader_inference":"The packet supplies failed care, refused encouragement to feed, appropriation, gathering, and fullness; I infer a measure-for-measure arrow from social withholding to punitive deprivation. A live alternative is that these are grounds for generic punishment without specifying its mode.","status":"revised","structural_cues":["Verses 17-20 move in one direction from refused care and feeding to consuming, gathering, and loving abundance.","The focus follows this appetite sequence after the cosmic interruption of 89:21-24."],"trigger_roots":["ي ت م","ح ض ض","ط ع م","ء ك ل","ل م م","ج م م"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_reciprocal_deprivation","source_type":"hft","support_id":"sup_5a7efe651f736329089e","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا","ayah_ref":"89:22"},{"arabic_uthmani":"وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ","ayah_ref":"89:23"},{"arabic_uthmani":"فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ","ayah_ref":"89:25"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000017/B002","root_000281/B001","root_000281/B004","root_000532/B001","root_000871/B001","root_000994/B005","root_001444/B009"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000994","role":"The penal action is the operation whose ultimate source is being distinguished.","root":"ع ذ ب","source_ref":"89:25","source_word_indices":["3","4"]},{"branch_id":"B002","mapped_root_id":"root_000017","role":"Exhaustive negation excludes any peer without requiring every present subordinate to vanish.","root":"ء ح د","source_ref":"89:25","source_word_indices":["5"]},{"branch_id":"B001","mapped_root_id":"root_000281","role":"Arrival turns sovereignty from a remote attribution into the immediate center of the scene.","root":"ج ي ء","source_ref":"89:22","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000532","role":"Lordship and dominion identify the unmatched source of command and measure.","root":"ر ب ب","source_ref":"89:22","source_word_indices":["2"]},{"branch_id":"B009","mapped_root_id":"root_001444","role":"The angel branch supplies other agents who are present without becoming sovereign peers.","root":"م ل ك","source_ref":"89:22","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000871","role":"Ordered straight ranks cast the present agents as arranged under command.","root":"ص ف ف","source_ref":"89:22","source_word_indices":["4","5"]},{"branch_id":"B004","mapped_root_id":"root_000281","role":"Bringing and making present the punitive destination supplies an executable scene with instrumental movement.","root":"ج ي ء","source_ref":"89:23","source_word_indices":["1"]}],"changed_reading":{"after":"Other agents may be present and ordered, but none is a peer source or measure of the punishment.","before":"No other actor is present or involved in punishment."},"confidence":"medium","mechanism":"The scene contains arrival, sovereign presence, ranked angels, and the bringing-forth of the punitive destination. Since many agents are visibly present, the focus's 'no one' can distinguish incomparable authorship and measure from subordinate participation rather than asserting an empty field of actors.","model_id":"delta_sovereign_source_not_empty_scene","reader_inference":"The packet supplies a sovereign, angels in ranks, and something punitive brought forward; I infer a hierarchy between originating authority and instrumental execution. A live alternative is that the host only witnesses, so أَحَد straightforwardly excludes every other punishing agent.","status":"revised","structural_cues":["The subject of sovereign arrival and the ranked host precede the focus by only three verses.","The passive bringing of the punitive destination leaves its immediate carrier unexpressed while keeping the sovereign scene explicit."],"trigger_roots":["ر ب ب","ج ي ء","م ل ك","ص ف ف"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_sovereign_source_not_empty_scene","source_type":"hft","support_id":"sup_00fd087243ab7be0533d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ","ayah_ref":"89:25"},{"arabic_uthmani":"وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ","ayah_ref":"89:26"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000017/B002","root_000994/B005","root_001623/B003"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000994","role":"Penal pain supplies the first member of the syntactic pair.","root":"ع ذ ب","source_ref":"89:25","source_word_indices":["3","4"]},{"branch_id":"B002","mapped_root_id":"root_000017","role":"Exhaustive negation closes the first member and establishes the repeated scope.","root":"ء ح د","source_ref":"89:25","source_word_indices":["5"]},{"branch_id":"B003","mapped_root_id":"root_001623","role":"Tight binding and the bond used to secure supply immobilization as punishment's paired operation.","root":"و ث ق","source_ref":"89:26","source_word_indices":["2","3"]},{"branch_id":"B002","mapped_root_id":"root_000017","role":"The repeated exhaustive noun seals the formal equivalence between punishing and binding clauses.","root":"ء ح د","source_ref":"89:26","source_word_indices":["4"]}],"changed_reading":{"after":"Punishment is paired with unmatched securing: pain becomes a fixed, inescapable condition.","before":"Punishment is unmatched intensity of pain."},"confidence":"strong","mechanism":"The next verse repeats the focus's negation, imperfect verb, cognate noun with possessive suffix, and final أَحَد, but substitutes securing bonds for punishment. The parallel couples pain with immobilization: punishment is an enforced condition that cannot be escaped or loosened.","model_id":"delta_punishment_binding_pair","reader_inference":"The packet supplies a near-identical construction and a branch of physical securing; I infer that the parallel makes confinement part of the punitive mechanism. The alternative is simple coordination of two distinct unmatched acts, pain and binding, without semantic fusion.","status":"new","structural_cues":["Verses 25 and 26 form an exact two-line syntactic echo: negation, verb, cognate object with -hu, and أَحَد."],"trigger_roots":["و ث ق","ء ح د"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_punishment_binding_pair","source_type":"hft","support_id":"sup_1c3bce9a96bb443ddb39","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ","ayah_ref":"89:25"},{"arabic_uthmani":"ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ","ayah_ref":"89:28"},{"arabic_uthmani":"فَٱدْخُلِى فِى عِبَٰدِى","ayah_ref":"89:29"},{"arabic_uthmani":"وَٱدْخُلِى جَنَّتِى","ayah_ref":"89:30"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":4,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":4,"target_morphology_supplied":false},"branch_refs":["root_000266/B003","root_000464/B001","root_000544/B001","root_000569/B003","root_000994/B003","root_000994/B004"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000994","role":"Withholding and weaning anchor exclusion as a punitive operation in the focus.","root":"ع ذ ب","source_ref":"89:25","source_word_indices":["3","4"]},{"branch_id":"B004","mapped_root_id":"root_000994","role":"Lack of cover anchors the spatial consequence of denied entry.","root":"ع ذ ب","source_ref":"89:25","source_word_indices":["3","4"]},{"branch_id":"B001","mapped_root_id":"root_000544","role":"Return to a prior belonging supplies restored relation as the opposite of punitive severance.","root":"ر ج ع","source_ref":"89:28","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000569","role":"Mutual acceptance supplies a two-sided relation unavailable in the isolated punitive model.","root":"ر ض و","source_ref":"89:28","source_word_indices":["4","5"]},{"branch_id":"B001","mapped_root_id":"root_000464","role":"Passage into an interior supplies admission among a receiving community.","root":"د خ ل","source_ref":"89:29","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000464","role":"The repeated inward passage extends admission from community into destination.","root":"د خ ل","source_ref":"89:30","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000266","role":"The tree-screened garden provides the protected interior from which punitive exposure is excluded.","root":"ج ن ن","source_ref":"89:30","source_word_indices":["2"]}],"changed_reading":{"after":"Punishment also consists in what cannot be entered or recovered: relation, acceptance, community, and shelter.","before":"Punishment is what is actively done to the condemned."},"confidence":"medium","mechanism":"The alternative trajectory is return, reciprocal acceptance, repeated entry, and protected enclosure. This sharpens the focus's withholding and exposure branches by contrast: punishment can be exclusion from restored relation and denied passage into shelter.","model_id":"delta_exclusion_against_return_and_entry","reader_inference":"The packet supplies return, mutual acceptance, inward passage, and protected garden; I infer their denial as a subtractive dimension of punishment. They may instead describe only the saved destination without specifying what punishment withholds.","status":"strengthened","structural_cues":["The post-focus address reverses the focus's singular third-person scene into direct invitation and two repeated imperatives of entry.","Return, acceptance, communal inclusion, and enclosure accumulate as one positive route."],"trigger_roots":["ر ج ع","ر ض و","د خ ل","ج ن ن"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_exclusion_against_return_and_entry","source_type":"hft","support_id":"sup_da134ef25e532f8166a2","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَأَمَّآ إِذَا مَا ٱبْتَلَىٰهُ فَقَدَرَ عَلَيْهِ رِزْقَهُۥ فَيَقُولُ رَبِّىٓ أَهَٰنَنِ","ayah_ref":"89:16"},{"arabic_uthmani":"وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ","ayah_ref":"89:18"},{"arabic_uthmani":"فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ","ayah_ref":"89:25"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000560/B002","root_000934/B001","root_000994/B001","root_000994/B005"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000994","role":"Fresh palatability supplies the positive sensory pole that punishment reverses or removes.","root":"ع ذ ب","source_ref":"89:25","source_word_indices":["3","4"]},{"branch_id":"B005","mapped_root_id":"root_000994","role":"Severe torment supplies the negative pole actually selected by the focus form.","root":"ع ذ ب","source_ref":"89:25","source_word_indices":["3","4"]},{"branch_id":"B002","mapped_root_id":"root_000560","role":"Sustaining nourishment gives the sensory polarity an economic and bodily stake.","root":"ر ز ق","source_ref":"89:16","source_word_indices":["7"]},{"branch_id":"B001","mapped_root_id":"root_000934","role":"Tasting and taking food reconnect the focus root's palatability pole to the surrounding appetite sequence.","root":"ط ع م","source_ref":"89:18","source_word_indices":["4"]}],"changed_reading":{"after":"Torment can be rendered cautiously as sweetness made unavailable or experience made radically unpalatable.","before":"Torment is simply the presence of painful sensation."},"confidence":"exploratory","containment":"The reversal is surprising because sweetness and torment are opposed branches of the same focus root, not interchangeable senses. It remains valid as a latent polarity because the context repeatedly stages nourishment, feeding, and refusal. Downstream prose should call it a semantic inversion or withdrawal of palatability, never claim that punishment lexically means sweetness.","focus_anchor":"The repeated focus root contains both severe punishment and fresh palatable water or food in its supplied inventory.","outlier_id":"outlier_sweetness_reversal"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_sweetness_reversal","source_type":"hft","support_id":"sup_96fc8008d6dc5ae0a6d0","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا","ayah_ref":"89:21"},{"arabic_uthmani":"وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ","ayah_ref":"89:23"},{"arabic_uthmani":"فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ","ayah_ref":"89:25"},{"arabic_uthmani":"يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ","ayah_ref":"89:27"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":4,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":4,"target_morphology_supplied":false},"branch_refs":["root_000281/B004","root_000482/B001","root_000994/B009","root_001533/B005"],"payload":{"activation_trace":[{"branch_id":"B009","mapped_root_id":"root_000994","role":"The womb-and-afterbirth branch supplies an expelled remainder following a transformative emergence.","root":"ع ذ ب","source_ref":"89:25","source_word_indices":["3","4"]},{"branch_id":"B001","mapped_root_id":"root_000482","role":"Repeated demolition of the earth supplies the violent transformation analogous to labor.","root":"د ك ك","source_ref":"89:21","source_word_indices":["3","5","6"]},{"branch_id":"B004","mapped_root_id":"root_000281","role":"Bringing something forth and making it present supplies emergence into the transformed scene.","root":"ج ي ء","source_ref":"89:23","source_word_indices":["1"]},{"branch_id":"B005","mapped_root_id":"root_001533","role":"Childbirth and postpartum emergence echo the focus's remote generative branch from the far side of punishment.","root":"ن ف س","source_ref":"89:27","source_word_indices":["2"]}],"changed_reading":{"after":"In a contained imagistic reading, punishment is the grim remainder brought forth by the world's violent transformation.","before":"Punishment follows the cosmic scene as a separate judicial event."},"confidence":"exploratory","containment":"This is the most branch-distant activation: it reads the final upheaval through the focus root's womb/afterbirth branch and the later النفس branch of childbirth. It remains packet-anchored because both branch images are explicit and the context breaks the earth and brings the punitive destination forth. Downstream prose must label it an imagistic eschatological analogy, not morphology, doctrine, or a lexical gloss.","focus_anchor":"A supplied branch of the repeated focus root names womb and what emerges after birth.","outlier_id":"outlier_cosmic_afterbirth"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_cosmic_afterbirth","source_type":"hft","support_id":"sup_cd126a40aea1e9b928c4","trust":"legacy_unbound"}]}
</lane_packet_json>
