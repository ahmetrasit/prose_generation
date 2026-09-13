# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **91:10**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s091-regular-20260912/s091/91_10/macro.discovery.json` and modify nothing
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
  "ayah_ref": "91:10",
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
{"branch_registry":[{"boundary":"Dalın odağı yalnızca üzüntü duygusu değil, aranan sonucun elde edilememesi ve girişimin yararsız kalmasıdır; kalıplaşmış sözler çıplak anlamın kapsamını genişletmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000451/B001","candidate_links":[{"candidate_id":"cand_897cc19078c266ccd756","lane":"macro"},{"candidate_id":"cand_aba275d909f1d7a713d3","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"خَابَ","morph_features":"STEM|POS:V|PERF|LEM:xaAba|ROOT:xyb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:10:2:1","qac_word_ref":"91:10:2","surface_ar":"خَابَ"}],"gloss":"istediğini elde edemeyip yarar görememe","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İstekte bulunan kişi aradığı sonuca ulaşamaz ve girişiminden yarar göremez."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sonuç, kişinin beklediği paydan yoksun kalması veya kaybetmesi olarak görünür."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen biçim, başka bir kişinin istediğini elde edememesine yol açmayı bildirir."}}],"root_ar":"خ ي ب","root_id":"root_000451","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir isteğin veya girişimin sonuçsuz kaldığı genel durumlar için uygundur.","boundary_detail":"Dalın odağı yalnızca üzüntü duygusu değil, aranan sonucun elde edilememesi ve girişimin yararsız kalmasıdır; kalıplaşmış sözler çıplak anlamın kapsamını genişletmez.","branch_image_ar":"فوت الطلب وحرمان الجد","concept_gloss":"istediğini elde edemeyip yarar görememe","contextual_glosses":[{"applicability":"Bir girişimin beklenen sonuca ulaşmadığını kısa biçimde söylemek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İstenen şeyden yoksun kalma ve hiçbir yarar görememe ayrıntılarını açıkça vermez.","preserves":"Girişimin olumlu sonuç vermemesi yönünü korur."},"facet_ids":["F001"],"text":"başarısız olmak","usage_role":"general"},{"applicability":"Sonucun açıkça bir kayıp olarak sunulduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Her sonuç alamama durumunun somut bir kayıp sayılmadığı ayrımını siler.","preserves":"Olumsuz sonuca uğrama ve elde edememe yönünü korur."},"facet_ids":["F002"],"text":"kaybetmek","usage_role":"contextual"},{"applicability":"Bir kişinin başka bir kişiyi istediğini elde edemez duruma getirdiği ettirgen kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başka bir kişiyi sonuç alamaz duruma düşürme ilişkisini korur."},"facet_ids":["F003"],"text":"birini başarısızlığa uğratmak","usage_role":"contextual"}],"definition":"Bir kimsenin bir isteğin peşinden gidip onu elde edememesi ve girişiminden iyi bir sonuç ya da yarar görememesidir; bağlama göre yoksun kalma veya kaybetme sonucunu da içerir. Ettirgen kullanım, bir başkasının istediğine ulaşmasını engelleyerek onu bu sonuca düşürmeyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İstekte bulunan kişi aradığı sonuca ulaşamaz ve girişiminden yarar göremez."},{"facet_id":"F002","role":"extension","statement":"Sonuç, kişinin beklediği paydan yoksun kalması veya kaybetmesi olarak görünür."},{"facet_id":"F003","role":"extension","statement":"Ettirgen biçim, başka bir kişinin istediğini elde edememesine yol açmayı bildirir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kişinin üzüntü veya düş kırıklığı yaşadığı varsayımını ekler.","collision":"Sonuç alamayan kişinin duygusal tepkisini, sonuç alamama durumunun kendisiyle karıştırır.","fit":"displacement","loses":"İstenen şeyi elde edememe ve girişimden yarar görememe olayını duygusal sonucuyla değiştirir.","preserves":"Beklentinin gerçekleşmemesinden doğan olumsuzluğu korur."},"text":"hayal kırıklığı"},{"category":"common_loanword","error_profile":{"adds":"Ağır duygusal yıkım ve büyük zarar çağrışımı ekleyebilir.","collision":"Güncel kullanımda güçlü duygusal çöküşle karışabilir.","fit":"drifted_loanword","loses":"İstek, çaba, elde edememe ve yararsız kalma ilişkisini açıkça kurmaz.","preserves":"Olumsuz ve beklenmedik sonuç çağrışımını korur."},"text":"hüsran"}],"identity_rationale":"Yetkili dal savı, bir isteğin peşinden giden kişinin istediğine ulaşamamasını ve girişiminden yarar görememesini ortak çekirdek olarak verir. Yoksun kalma, kaybetme ve bir başkasını bu sonuca düşürme anlatımları da bu çekirdeğin sonuç ya da ettirgen görünümleridir; hazırlanmış dal çerçevesi bu yapıyı doğru biçimde karşılar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"istediğini elde edememek ve girişiminden yarar görememek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"isteğini elde edememe ve umduğunu bulamama"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"birini başarısızlığa uğratmak; istediğini elde etmesini engellemek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"birine umduğunu bulamama dilemek veya bunu onun için bildirmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"çekingenlik umduğunu boşa çıkarır"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"kaybetmek"}],"lexicalization_note":"Çıplak biçimler sonuç alamama, yarar görememe, kaybetme ve bu sonuca düşürme anlamlarını taşır. İki kalıplaşmış kullanım ise yalnızca kendi söz dizileri içinde geçerlidir ve dalın çıplak anlamına eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. En güçlü beş karşılaştırma sonuç alamama, yoksun bırakılma, eli boş kalma, başarısızlığa uğratma ve umudun kesilmesi sınırlarını gösterir; oyun, açlık, ateş aracı ve aynı kökün öteki dalları yalnızca uzak bir durum ortaklığı taşıdığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal, bir isteğin veya çabanın boşa çıkmasını ve yarar vermemesini olay örgüsünün merkezine koyar. Komşu dal ise girişim bulunmasa da bir payın, iyiliğin veya beklenen şeyin verilmemesini kapsayabilir.","focus_only":"İstekte bulunanın girişiminin sonuçsuz ve yararsız kalması odağa alınır.","gloss":"sonuç alamama ile yoksun bırakılma","neighbor_only":"Bir şeyin verilmemesi ve kişinin beklediği iyilikten veya paydan yoksun bırakılması daha geniş biçimde anlatılır.","neighbor_ref":"root_000313/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da beklenen bir şeyin elde edilememesini ve kişinin ondan yoksun kalmasını kapsar."},{"boundary_match":"partial","distinction":"Odak dal genel bir sonuçsuzluk ve yararsızlık durumudur. Komşu dal, belirli arama ve kazanma durumlarında kişinin av, kazanç ya da gereksinim elde edememesine daha sıkı bağlıdır.","focus_only":"Her tür istek ve girişimde sonuç alamama ile yararsız kalmayı kapsar.","gloss":"umduğunu bulamama ile eli boş kalma","neighbor_only":"Avcı, tuzak kuran, savaşçı veya gereksinim peşindeki kişi gibi belirli arayıcıların eli boş kalmasını öne çıkarır.","neighbor_ref":"root_001641/B004","relation_type":"near_synonym","shared_zone":"İki dalda da bir amaç peşindeki kişi beklediği kazanımı elde edemez."},{"boundary_match":"partial","distinction":"Odak dal başarısızlığı istek, elde etme ve yarar görme ilişkisiyle sınırlar. Komşu dalın kartı ise bu sonucu başka bir sözün açıklaması olarak verir ve aynı ayrıntılı sınırları kurmaz.","focus_only":"İstenen şeyi elde edememe, yarar görememe, yoksun kalma ve kaybetme sınırlarını açıkça taşır.","gloss":"başarısız olma ve başarısızlığa uğratma","neighbor_only":"Başka bir sözcüğün başarısız olma ve başarısızlığa uğratma anlamıyla açıklanmasına bağlıdır.","neighbor_ref":"root_001361/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin başarısız olması ile başka biri tarafından başarısızlığa uğratılması alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal, girişimin başarısız sonucunu genel olarak anlatır. Komşu dal ise bu sonucu özellikle bir yerden veya girişimden eli boş geri dönme sahnesi içinde anlatır.","focus_only":"Kişinin geri dönmesi gerekmeksizin isteğinde sonuç alamamasını kapsar.","gloss":"sonuç alamama ile eli boş dönme","neighbor_only":"Bir amaçtan kazanç elde etmeden geri dönme ve bu dönüşün dışarıdan görülmesi durumuna bağlıdır.","neighbor_ref":"root_000816/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda da kişi amaçladığı şeyi kazanamadan kalır."},{"boundary_match":"partial","distinction":"Odak dal gerçekleşmiş sonuçsuzluğu bildirir; komşu dal kişinin artık olumlu sonuç beklememesini bildirir. Biri olayın sonucu, diğeri beklentinin sona ermesidir.","focus_only":"Gerçek bir isteğin veya girişimin istenen sonucu vermemesi söz konusudur.","gloss":"sonuç alamama ile umudu kesme","neighbor_only":"Beklentinin ve umudun kesilmesi, henüz bir girişimin sonucu belli olmadan da gerçekleşebilir.","neighbor_ref":"root_001690/B001","relation_type":"near_neighbor","shared_zone":"İki dal da kişinin beklediği olumlu sonuca ulaşamaması çevresinde yer alır."}],"source_phrase_ar":"أصل واحد يدل على عدم فائدة وحرمان (maqayis)؛ سعى في أمر فخاب إذا حرم فلم يفد خيرا (maqayis)؛ خاب الرجل خيبة إذا لم ينل ما يطلب وخيبته أنا تخييبا وخيبة لزيد (sihah)؛ الخيبة حرمان الجد وخاب إذا خسر (tahdhib)؛ الخيبة فوت الطلب (mufradat)","source_summary":"Aktarımlar, ortak olarak istenen şeyin elde edilememesini, çabanın yararsız kalmasını ve kişinin iyi sonuçtan yoksun kalmasını anlatır. Kaybetme ve bir başkasını aynı sonuca uğratma kullanımları bu temel durumun uzantılarıdır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"الخيبة وخاب وخيبه وسعي خائب إذا لم ينل الطالب ما طلب أو حرم الجد ولم يفد خيرا أو خسر أو قيل خيبة لفلان","what_is_not_ar":"ليس الخياب القدح الذي لا يوري؛ وليس وادي تخيب بمعنى الباطل؛ وليس الخوبة للفقر والجوع والأرض التي لم تمطر"},"support_links":["sup_c049d5b530df51c81252","sup_fbf5dfdbe7be688e19d3"]},{"boundary":"Bu dal sonuç alamayan kişiyi değil, çakıldığı halde ateş vermeyen ateş yakma aracını adlandırır.","branch_kind":"bare","branch_ref":"root_000451/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَابَ","morph_features":"STEM|POS:V|PERF|LEM:xaAba|ROOT:xyb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:10:2:1","qac_word_ref":"91:10:2","surface_ar":"خَابَ"}],"gloss":"ateş çıkarmayan tutuşturma aracı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ateş üretmesi beklenen çakma aracı kullanıldığı halde ateş çıkarmaz."}}],"root_ar":"خ ي ب","root_id":"root_000451","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ateş üretmesi beklenirken çakıldığında ateş vermeyen aracın adı olarak uygundur.","boundary_detail":"Bu dal sonuç alamayan kişiyi değil, çakıldığı halde ateş vermeyen ateş yakma aracını adlandırır.","branch_image_ar":"الخِياب القدح الذي لا يوري","concept_gloss":"ateş çıkarmayan tutuşturma aracı","contextual_glosses":[{"applicability":"Ateş yakma aracının bir çubuk olduğu açık bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çubuk dışında bir çakma aracının kastedilebildiği daha geniş nesne kapsamını dışarıda bırakır.","preserves":"Ateş yakmak için kullanılan aracın kıvılcım vermemesi özelliğini korur."},"facet_ids":["F001"],"text":"kıvılcım çıkarmayan ateş çubuğu","usage_role":"contextual"}],"definition":"Ateş yakmak için çakılan veya sürtülen, fakat kıvılcım ya da ateş çıkarmayan araçtır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ateş üretmesi beklenen çakma aracı kullanıldığı halde ateş çıkarmaz."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Aracın mutlaka taş olduğu ve ateş çıkarıp çıkarmadığına bakılmadığı daha geniş bir nesne sınıfını ekler.","collision":"İşlevini yerine getiren sıradan çakmak taşıyla karışır.","fit":"broadening","loses":null,"preserves":"Ateş çıkarmak için çakılan bir aracı belirtir."},"text":"çakmak taşı"},{"category":"confusable","error_profile":{"adds":"Daha önce yanmış bir ateşin sonradan söndüğü olayını ekler.","collision":"Aracın niteliğini ateşin sonraki durumuyla karıştırır.","fit":"displacement","loses":"Ateş üretmesi beklenen aracın bu işi başaramaması özelliğini bütünüyle siler.","preserves":"Ateşin bulunmaması sonucunu yüzeysel olarak korur."},"text":"sönmüş ateş"}],"identity_rationale":"Yetkili dal savı, ateş elde etmek için çakılan aracın ateş çıkarmaması özelliğini doğrudan bildirir. Hazırlanmış çerçeve nesneyi ve onu ayıran olumsuz işlevi eksiksiz koruduğundan dal kimliği değiştirilmeden kabul edilebilir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"çakıldığında ateş çıkarmayan tutuşturma aracı"}],"lexicalization_note":"Anlam tek bir çıplak nesne adıdır: ateş yakmak için kullanılan, fakat çakıldığında ateş çıkarmayan araç. Başka dallardaki sonuçsuzluk veya kalıplaşmış anlatım buraya taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Yayımlanan karşılaştırmalar tam eşdeğeri, ateş veren karşıt kutbu, gecikmeli ateş verme durumunu ve daha özel sert araç türünü gösterir; ateş yakma malzemeleri ile aynı kökün kişi ve asılsızlık dalları doğrudan sınır karşılaştırması sağlamadığı için dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kartlarda nesne türü, beklenen işlev ve işlevin gerçekleşmemesi bakımından bir sınır farkı görünmez; bu nedenle kavramsal olarak birbirinin yerine geçebilirler.","focus_only":null,"gloss":"ateş çıkarmayan ateş çubuğu","neighbor_only":null,"neighbor_ref":"root_000778/B003","relation_type":"synonym","shared_zone":"İki dal da ateş elde etmek için kullanılan fakat ateş çıkarmayan çubuğu adlandırır."},{"boundary_match":"opposed","distinction":"Odak dal aynı işlevin gerçekleşmemesini, komşu dal ise ateşin ortaya çıkmasını anlatır. Ortak eksen ateş üretimidir ve sonuçlar karşıt kutuplardadır.","focus_only":"Çakma aracı kullanıldığı halde kıvılcım ya da ateş çıkmaz.","gloss":"ateş vermeme ile ateş verme","neighbor_only":"Ateş çubuğunda saklı ateş ortaya çıkar ve ateş yakılır.","neighbor_ref":"root_001642/B002","relation_type":"polarity_pair","shared_zone":"Her iki dal da ateş çubuğunun çakılması ve ateş üretme işlevi üzerinde bulunur."},{"boundary_match":"partial","distinction":"Odak dalda işlev başarısız olur; komşu dalda işlev yalnızca gecikir. Gecikerek ateş veren araç, ateş vermeyen araçla aynı değildir.","focus_only":"Araç hiç ateş çıkarmaz.","gloss":"ateş vermeme ile geç ateş verme","neighbor_only":"Araç ateşi gecikmeli ve güçlükle çıkarır.","neighbor_ref":"root_001334/B006","relation_type":"near_neighbor","shared_zone":"İki dal da ateş çubuğunun beklenen zamanda ateş üretmemesi çevresindedir."},{"boundary_match":"partial","distinction":"Odak dal yalnızca başarısız ateş üretme işleviyle tanımlanır. Komşu dal, sertlik, taş olma veya ses çıkarma gibi daha özel nesne nitelikleri de içerir.","focus_only":"Ateş çıkarmama dışında sertlik, ses çıkarma veya belirli bir malzeme koşulu taşımaz.","gloss":"ateş vermeyen araç ile sert ateş aracı","neighbor_only":"Sert ateş çubuğu ya da taşın vurulduğunda ses çıkarıp ateş vermemesi gibi ek özellikler taşır.","neighbor_ref":"root_000877/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da vurulduğu halde ateş çıkarmayan bir ateş yakma aracını anlatır."}],"source_phrase_ar":"الأصل قولهم للقدح الذي لا يوري هو خياب (maqayis)؛ الخياب القدح الذي لا يوري (tahdhib)","source_summary":"Aktarımlar aynı nesne sınırında birleşir: ateş yakmak için kullanılan çakma aracı ateş çıkarmaz ve adını bu işlev bozukluğundan alır.","sources":["MQ","TA"],"what_is_ar":"الخِياب وهو القدح الذي لا يوري","what_is_not_ar":"ليس خيبة الطلب والحرمان؛ وليس وادي تخيب؛ وليس الخوبة"},"support_links":[]},{"boundary":"Anlam bağımsız bir çıplak sözcüğe değil, belirli bir vadiye düşme anlatımının bütününe bağlıdır; gerçek bir coğrafi yere gönderme yapılmaz.","branch_kind":"non_bare","branch_ref":"root_000451/B003","candidate_links":[{"candidate_id":"cand_21d2c78e6eded8256e81","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"خَابَ","morph_features":"STEM|POS:V|PERF|LEM:xaAba|ROOT:xyb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:10:2:1","qac_word_ref":"91:10:2","surface_ar":"خَابَ"}],"gloss":"asılsızlığa düşme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli vadiye düşme anlatımı, kişilerin asılsız ve gerçek dışı olana yönelmesini bildirir."}}],"root_ar":"خ ي ب","root_id":"root_000451","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kanıtta verilen özel vadi anlatımının kavramsal karşılığı olarak kullanılır.","boundary_detail":"Anlam bağımsız bir çıplak sözcüğe değil, belirli bir vadiye düşme anlatımının bütününe bağlıdır; gerçek bir coğrafi yere gönderme yapılmaz.","branch_image_ar":"وادي تُخَيِّب الباطل","concept_gloss":"asılsızlığa düşme","contextual_glosses":[{"applicability":"Vadi görüntüsünü Türkçede doğal bir yol benzetmesiyle açıklamak gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin gerçeğe dayanmayan bir yöne girmesi ve oraya sapması anlamını korur."},"facet_ids":["F001"],"text":"asılsız bir yola sapmak","usage_role":"explanatory"},{"applicability":"Asılsızlığın özellikle sonuç vermeyecek bir uğraş olarak gerçekleştiği bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Asılsız söz, düşünce veya sav gibi iş dışındaki gerçekleşmeleri dışarıda bırakır.","preserves":"Gerçek temeli olmayan bir şeye yönelip onda kalma anlamını korur."},"facet_ids":["F001"],"text":"boş bir işe saplanmak","usage_role":"contextual"}],"definition":"Belirli bir vadiye düşme kalıbı içinde, kişilerin gerçek bir yere girmesini değil, asılsız ve gerçek dışı olana saplanmasını anlatan özel kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli vadiye düşme anlatımı, kişilerin asılsız ve gerçek dışı olana yönelmesini bildirir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Gerçek bir vadinin yanlış seçildiği coğrafi durumu ekler.","collision":"Sözün mecazlı anlamını gerçek yer adıyla karıştırır.","fit":"displacement","loses":"Kalıbın asılsızlık ve gerçek dışılık anlamını siler.","preserves":"Vadi görüntüsünü yüzeyde korur."},"text":"yanlış vadi"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Anlamı yalnızca söze indirger; asılsız bir iş, sav veya yönelişi kapsamaz.","preserves":"Asılsızlık ve gerçek dışılık yönünü korur."},"text":"boş söz"}],"identity_rationale":"Yetkili dal savı, belirli bir vadiye düşme sözünün gerçek bir yer bildirmeyip asılsız olanı anlattığını açıkça belirtir. Hazırlanmış çerçeve hem kalıba bağlılığı hem de asılsızlık anlamını koruduğundan dal kimliği kabul edilebilir.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"asılsız bir yola düşmek; gerçek dışı olana saplanmak"}],"lexicalization_note":"Dal yalnızca belirli vadiye düşme sözünde asılsızlığa saplanmayı anlatır. Bu anlam kökün çıplak biçimlerine veya başka vadi sözlerine kendiliğinden aktarılamaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Tam eşdeğer vadi anlatımı ile genel asılsızlık, boş söz ve yalan söyleme alanları yayımlandı; uydurma dilek, aldatıcı görünüş ve öteki uzak asılsızlık adayları bu sınırları yinelediği için, aynı kökün öteki dallarıysa anlam ortaklığı taşımadığı için seçilmedi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kartlar, kalıp türü ve asılsızlık anlamı bakımından aynı kavramsal sınırı gösterir. Sözlerin içindeki özel adlar farklı olsa da yayımlanacak anlam düzeyinde bir ayrım bulunmaz.","focus_only":null,"gloss":"vadi anlatımıyla asılsızlığa düşme","neighbor_only":null,"neighbor_ref":"root_001596/B011","relation_type":"synonym","shared_zone":"İki dal da belirli bir vadiye düşme sözünü asılsızlığa saplanma anlamında kullanır."},{"boundary_match":"partial","distinction":"Odak dal kalıplaşmış bir anlatımın verdiği özel anlamdır. Komşu dal ise asılsızlığın kendisini, doğruluğun ve kalıcılığın karşıtı olarak daha geniş biçimde tanımlar.","focus_only":"Asılsızlık anlamı yalnızca belirli vadiye düşme kalıbıyla verilir.","gloss":"özel asılsızlık anlatımı ile genel asılsızlık","neighbor_only":"Gerçeklikten ve doğruluktan uzak olan her şeyi, belirli bir söz kalıbına bağlı olmadan kapsar.","neighbor_ref":"root_000127/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da gerçekliği ve dayanağı bulunmayan şeyi anlatır."},{"boundary_match":"partial","distinction":"Odak dalın sınırı anlatım kalıbından gelir ve yalnızca konuşmaya bağlı değildir. Komşu dalın sınırı ise asılsız veya yararsız söz alanıdır.","focus_only":"Asılsızlık söz, düşünce veya iş ayrımı olmadan özel vadi anlatımı içinde sunulur.","gloss":"asılsızlığa saplanma ile boş söz","neighbor_only":"Asılsızlık ve boşluk özellikle söylenen sözlere ve yararsız konuşmaya bağlanır.","neighbor_ref":"root_001609/B010","relation_type":"near_synonym","shared_zone":"İki dal da gerçek temeli bulunmayan ve boş sayılan içeriği kapsar."},{"boundary_match":"partial","distinction":"Odak dal asılsız bir alana yönelmeyi anlatır ve aldatma eylemini zorunlu kılmaz. Komşu dal ise çoğu kullanımında gerçeğe aykırı söz üretme veya sunma eylemini öne çıkarır.","focus_only":"Kişinin asılsız olana düşmesi özel bir yer anlatımıyla bildirilir.","gloss":"asılsızlığa düşme ile yalan söyleme","neighbor_only":"Yalan söyleme, gerçeğe aykırı tanıklık ve gerçek dışı bir şeyi doğruymuş gibi sunma eylemlerini içerir.","neighbor_ref":"root_000654/B002","relation_type":"near_neighbor","shared_zone":"İki dal gerçekliğe aykırı içerik alanında buluşur."}],"source_phrase_ar":"وقعوا في وادي تُخَيِّب معناه الباطل","source_qualifications":[{"kind":"sole_attestation","summary":"Tek aktarım, belirli vadiye düşme sözünü asılsız olana saplanma anlamıyla açıklar."}],"source_summary":"Bu özel kullanım için kaynaklar arası ortaklık gösterilemez; dalın anlamı tek aktarımda belirli vadi anlatımının asılsızlığı bildirmesiyle sınırlandırılır.","sources":["SI"],"what_is_ar":"وادي تُخَيِّب إذا أريد به الباطل","what_is_not_ar":"ليس الخيبة في الطلب؛ وليس الخياب القدح؛ وليس الخوبة"},"support_links":["sup_4bb7a79c106038a0c933"]},{"boundary":"Yoksullaşma ile tüm varlığın tükenmesi çekirdeğe en yakın anlamlardır; açlık ve yağmur almamış toprak ayrı uzantılar olarak tutulmalı, biçim kuşkusu da kesinlik iddiasıyla örtülmemelidir.","branch_kind":"bare","branch_ref":"root_000451/B004","candidate_links":[{"candidate_id":"cand_d639702f530fc65c300d","lane":"macro"},{"candidate_id":"cand_178907ea4e2d8b981b3b","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"خَابَ","morph_features":"STEM|POS:V|PERF|LEM:xaAba|ROOT:xyb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:10:2:1","qac_word_ref":"91:10:2","surface_ar":"خَابَ"}],"gloss":"yoksullaşma ve geçim kaynaklarının tükenmesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin geçim olanaklarını yitirerek yoksullaşması anlatılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir topluluğun elinde bulunanların hiçbir şey kalmayacak biçimde bütünüyle tükenmesi anlatılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kaynak yokluğunun bedensel sonucu olan açlık aynı adla belirtilir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Yağmur almamış toprak, su ve ürün yoksunluğu üzerinden aynı adla belirtilir."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Bir kullanımın sözcük biçimi konusunda aktarım kuşkusu bulunur; bunun yanında bu dalda esas alınan biçimin doğru olduğu ayrıca belirtilir."}}],"root_ar":"خ ي ب","root_id":"root_000451","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kişi ve topluluk düzeyindeki temel kaynak kaybını birlikte anlatmak için uygundur.","boundary_detail":"Yoksullaşma ile tüm varlığın tükenmesi çekirdeğe en yakın anlamlardır; açlık ve yağmur almamış toprak ayrı uzantılar olarak tutulmalı, biçim kuşkusu da kesinlik iddiasıyla örtülmemelidir.","branch_image_ar":"الخَوْبة فقر وذهاب وجوع","concept_gloss":"yoksullaşma ve geçim kaynaklarının tükenmesi","contextual_glosses":[{"applicability":"Bir kişinin geçim olanaklarını yitirip yoksul duruma geldiği kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin yoksul duruma geçmesi anlamını korur."},"facet_ids":["F001"],"text":"yoksullaşmak","usage_role":"contextual"},{"applicability":"Bir topluluğun elindeki varlıkların bütünüyle yok olduğu kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eldeki şeylerin hiçbir şey kalmayacak biçimde tükenmesini korur."},"facet_ids":["F002"],"text":"elde avuçta ne varsa tükenmek","usage_role":"contextual"},{"applicability":"Sözcüğün doğrudan yiyecek yoksunluğunu adlandırdığı kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bedensel yiyecek gereksiniminin karşılanmaması anlamını korur."},"facet_ids":["F003"],"text":"açlık","usage_role":"contextual"},{"applicability":"Sözcüğün yağış görmemiş bir toprağı adlandırdığı kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Toprağın yağmur almamış olması özelliğini doğrudan korur."},"facet_ids":["F004"],"text":"yağmur almamış toprak","usage_role":"contextual"}],"definition":"Bu dal, geçim kaynaklarının tükenmesi çevresinde yoksullaşmayı ve bir topluluğun elindekilerin bütünüyle yok olmasını anlatır. Aynı ad açlık ve yağmur almamış toprak için de kullanılır; bu yan anlamlar tek bir çıplak anlama karıştırılmamalıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin geçim olanaklarını yitirerek yoksullaşması anlatılır."},{"facet_id":"F002","role":"specialization","statement":"Bir topluluğun elinde bulunanların hiçbir şey kalmayacak biçimde bütünüyle tükenmesi anlatılır."},{"facet_id":"F003","role":"extension","statement":"Kaynak yokluğunun bedensel sonucu olan açlık aynı adla belirtilir."},{"facet_id":"F004","role":"extension","statement":"Yağmur almamış toprak, su ve ürün yoksunluğu üzerinden aynı adla belirtilir."},{"facet_id":"F005","role":"source_variant","statement":"Bir kullanımın sözcük biçimi konusunda aktarım kuşkusu bulunur; bunun yanında bu dalda esas alınan biçimin doğru olduğu ayrıca belirtilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Topluluğun elindekilerin bütünüyle tükenmesi, açlık ve yağmur almamış toprak anlamlarını dışarıda bırakır.","preserves":"Kişinin geçim olanaklarından yoksun olması yönünü korur."},"text":"yoksulluk"},{"category":"confusable","error_profile":{"adds":"Geniş bir bölgede uzun süren genel ürün ve yiyecek azlığı anlamını ekler.","collision":"Bireysel yoksullaşmayı toplumsal ürün kıtlığıyla karıştırabilir.","fit":"broadening","loses":"Kişinin yoksullaşması ile belirli bir topluluğun elindekilerin bütünüyle tükenmesi ayrımını vermez.","preserves":"Kaynak azlığı, açlık ve geçim sıkıntısı alanını kısmen korur."},"text":"kıtlık"},{"category":"confusable","error_profile":{"adds":"Tek bir yağmur almamış toprak yerine geniş ve süreğen bir iklim olayını düşündürebilir.","collision":"Toprağın niteliğini bölgesel iklim olayıyla karıştırabilir.","fit":"narrowing","loses":"Yoksullaşma, eldekinin tükenmesi ve açlık anlamlarını dışarıda bırakır.","preserves":"Yağmur yoksunluğu ve toprağın yağış almaması yönünü korur."},"text":"kuraklık"}],"identity_rationale":"Yetkili dal savı yoksullaşmayı, bir topluluğun elindekilerin bütünüyle tükenmesini, açlığı ve yağmur almamış toprağı aynı dalda kaydeder. Bu anlamlar geçim ve kaynak yokluğu çevresinde ilişkilendirilebilir, ancak tek bir eşdeğer gibi birleştirilemez; ayrıca sav, bir kullanımın sözcük biçimi konusunda açık bir aktarım kuşkusu taşır. Dal korunabilir, fakat bu çoklu yapı ve kuşku görünür tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yoksullaşmak"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"eldeki her şeyin hiçbir şey kalmayacak biçimde tükenmesi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"açlık"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yağmur almamış toprak"}],"lexicalization_note":"Dört anlam da çıplak biçimlere bağlıdır: yoksullaşmak, eldeki her şeyin tükenmesi, açlık ve yağmur almamış toprak. Bunlar yapı bağı olmadan kaydedilir, ancak birbirlerinin yerine geçen tek bir genel anlam sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. En yararlı karşılaştırmalar genel darlık, geçim sıkıntısı, gereksinim ve susuz arazi sınırlarını gösterir; sürekli tam yoksulluk, kıtlık mevsimi, az sulu kuyu ve malın zayıflaması adayları bu ayrımları yinelediği için, aynı kökün öteki dallarıysa anlam ortaklığı taşımadığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bazı kullanımlarda tam tükenmeyi ve ayrı adlandırmalar olarak açlık ile yağmur almamış toprağı verir. Komşu dal ise tam yok oluş gerektirmeyen genel azlık, darlık ve eli sıkılık durumlarını da kapsar.","focus_only":"Eldeki her şeyin bütünüyle tükenmesi, açlık ve yağmur almamış toprağın aynı adla anılması öne çıkar.","gloss":"tükenme ile genel darlık","neighbor_only":"İyiliğin azlığı, eli sıkılık, geçim darlığı, yağmur ve bitkinin azlığı gibi eksiklik derecelerini daha geniş kapsar.","neighbor_ref":"root_000224/B002","relation_type":"near_synonym","shared_zone":"İki dal yoksulluk, geçim sıkıntısı ve yağış azlığı çevresinde büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal kaynak yokluğu, tam tükenme ve yağışsız toprak çevresinde örgütlenir. Komşu dal ise genel sıkıntı, zarar ve kötü durumları da içerdiği için daha geniş bir acı ve darlık alanına yayılır.","focus_only":"Kaynakların tükenmesi yanında yağmur almamış toprağı ayrı bir anlam olarak içerir.","gloss":"yoksullaşma ile geçim sıkıntısı","neighbor_only":"Sıkıntı, zarar, başa gelen kötü durum ve yoksulluk yakarışı gibi daha geniş yaşantı ve söyleyiş alanlarını içerir.","neighbor_ref":"root_000079/B002","relation_type":"near_synonym","shared_zone":"Her iki dal yoksulluk ve açlık durumlarını kapsar."},{"boundary_match":"partial","distinction":"Odak dal yoksullaşmanın yanı sıra tam kaynak tükenmesini ve iki ayrı doğa ya da beden uzantısını kaydeder. Komşu dal genel gereksinim ve kötü geçim durumu üzerinde kalır.","focus_only":"Bir topluluğun elindekilerin tamamen tükenmesi, açlık ve yağmursuz toprak uzantılarını içerir.","gloss":"yoksullaşma ile gereksinim içinde olma","neighbor_only":"Gereksinim, kötü durum ve geçimdeki gedik anlamlarını tam tükenme koşulu olmadan kapsar.","neighbor_ref":"root_000414/B003","relation_type":"near_synonym","shared_zone":"İki dal kişinin geçim olanaklarının yetersizleşmesi ve yoksul duruma gelmesi alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal toprağın yağış görmemesine bağlıdır. Komşu dal ise yağış nedenini zorunlu kılmadan arazide suyun bulunmamasını ve ayrıca canlıdaki süt kaybını anlatır.","focus_only":"Toprağın özellikle yağmur almamış olması belirtilir.","gloss":"yağmur almamış toprak ile susuz arazi","neighbor_only":"Arazide su bulunmaması ile dişi hayvanda sütün azalması veya kesilmesi birlikte kapsanır.","neighbor_ref":"root_000227/B011","relation_type":"near_neighbor","shared_zone":"İki dal toprağın su kaynağından yoksun olması alanında buluşur."}],"source_phrase_ar":"خاب يخوب خوبا إذا افتقر؛ أصابتهم خوبة إذا ذهب ما عندهم؛ يقال للجوع الخوبة؛ الخوبة والقواية والخطيطة الأرض التي لم تمطر؛ لا أدري ما أصابتهم خوبة وأظنه حوبة؛ والخوبة بالخاء صحيح","source_qualifications":[{"kind":"sole_attestation","summary":"Tek aktarım yoksullaşma, eldekinin bütünüyle tükenmesi, açlık ve yağmur almamış toprak anlamlarını birlikte kaydeder; ayrıca bir kullanımın biçiminden kuşku duyarken bu dalda esas alınan biçimi doğrular."}],"source_summary":"Dalın bütün anlam alanı tek aktarımın tanıklığına dayanır; bu nedenle kaynaklar arası ortak bir anlam özeti kurulamaz. Aktarımın kendi içindeki biçim kuşkusu, anlamların kesinlik düzeyini değerlendirirken korunmalıdır.","sources":["TA"],"what_is_ar":"خاب يخوب خوبا إذا افتقر؛ والخوبة إذا ذهب ما عند القوم؛ والجوع؛ والأرض التي لم تمطر","what_is_not_ar":"ليس خيبة الطلب؛ وليس الخياب القدح؛ وليس وادي تخيب"},"support_links":["sup_0dfc8c3ded68753a86b6","sup_9be7379ef7e7f26e64c1"]},{"boundary":"Dal, nesnenin saklanması ile kişinin kendisini görünürlükten çekmesini kapsar; benliği kötülüğe sürükleme ve değerce düşürme ayrı dalda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000476/B001","candidate_links":[{"candidate_id":"cand_897cc19078c266ccd756","lane":"macro"},{"candidate_id":"cand_fb41e6a616d99d17db5c","lane":"macro"},{"candidate_id":"cand_e6c4b10b0547c380cfce","lane":"macro"},{"candidate_id":"cand_41845910da30d8ed3c60","lane":"macro"},{"candidate_id":"cand_1387f0b5d53e9de7f7ca","lane":"macro"},{"candidate_id":"cand_93e9781fb5767daa6a18","lane":"macro"},{"candidate_id":"cand_21d2c78e6eded8256e81","lane":"macro"},{"candidate_id":"cand_5e39ac9975aea9cead75","lane":"macro"},{"candidate_id":"cand_aba275d909f1d7a713d3","lane":"macro"},{"candidate_id":"cand_4e9ba063a74c9b2bada4","lane":"macro"},{"candidate_id":"cand_4d24e4ae9fd2afc74f7f","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"دَسَّىٰ","morph_features":"STEM|POS:V|PERF|LEM:das~aY`|ROOT:dsw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:10:4:1","qac_word_ref":"91:10:4","surface_ar":"دَسَّىٰ"}],"gloss":"gizleme ve gözden çekilme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığı görünürlükten uzaklaştırarak saklama veya öznenin kendisini görünmez kılma eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin kendisini geri plana çekip tanınmaz ve önemsiz kalmasını sağlaması, kendine yönelen kullanımda belirginleşir."}}],"root_ar":"د س و","root_id":"root_000476","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin saklanmasıyla öznenin kendisini görünürlükten çekmesini birlikte karşılayan üst düzey anlatımdır.","boundary_detail":"Dal, nesnenin saklanması ile kişinin kendisini görünürlükten çekmesini kapsar; benliği kötülüğe sürükleme ve değerce düşürme ayrı dalda kalır.","branch_image_ar":"الاندساس في الخفاء","concept_gloss":"gizleme ve gözden çekilme","contextual_glosses":[{"applicability":"Öznenin kendisini görünürlükten çektiği ve saklandığı geçişsiz bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir nesnenin saklanmasını ve kişinin kendisini özellikle geri plana itmesini tek başına karşılamaz.","preserves":"Öznenin görünürlükten çekilip saklanmasını doğal biçimde karşılar."},"facet_ids":["F001"],"text":"gizlenmek","usage_role":"contextual"},{"applicability":"Bir nesnenin ya da kişinin görünürlükten uzaklaştırıldığı geçişli bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öznenin kendiliğinden gizlenmesini ve kendisini geri plana çekmesini dışarıda bırakır.","preserves":"Bir katılımcıyı görünürlükten uzaklaştırıp saklama işlemini korur."},"facet_ids":["F001"],"text":"onu gizlemek","usage_role":"contextual"},{"applicability":"Kişinin tanınmamak ve önemsiz kalmak üzere kendisini silikleştirdiği bağlamlara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kendine yönelen saklama işlemini ve geri planda kalma sonucunu birlikte korur."},"facet_ids":["F002"],"text":"kendini geri plana çekmek","usage_role":"explanatory"}],"definition":"Bir şeyi görünürlükten uzaklaştırıp saklama ya da öznenin kendisini gizleyerek gözden çekilmesidir. Kişinin kendisini geri plana itip silikleştirmesi, yalnızca kendine yönelen yapının özel boyutudur ve tek başına ahlaki bozulma bildirmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığı görünürlükten uzaklaştırarak saklama veya öznenin kendisini görünmez kılma eylemidir."},{"facet_id":"F002","role":"specialization","statement":"Kişinin kendisini geri plana çekip tanınmaz ve önemsiz kalmasını sağlaması, kendine yönelen kullanımda belirginleşir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Fiziksel bir yüzeyi kaplama çağrışımını gereksiz biçimde öne çıkarır.","collision":"Genel kaplama alanıyla karışarak bu dalın saklanma ve gözden çekilme sınırını belirsizleştirir.","fit":"displacement","loses":"Öznenin gizlenmesini ve kişinin kendisini geri plana çekmesini karşılamaz.","preserves":"Bir şeyi görünür olmaktan çıkarma yönünü kısmen korur."},"text":"örtmek"}],"identity_rationale":"Yetkili ifade bir nesneyi saklamayı, öznenin gizlenmesini ve kişinin kendisini gizleyip geri planda bırakmasını birlikte bildirir. Hazırlanan çerçeve bu ortak gizlilik yönünü doğru yakalar; ancak kişinin kendisini silikleştirmesi burada görünürlükten ve tanınmışlıktan çekilmenin özel bir biçimidir, benliğin ahlaken bozulması değildir.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"gizlenmek"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"onu gizlemek"}],"lexicalization_note":"Yalın kullanım öznenin gizlenmesini bildirir; nesneli ve kendine yönelen yapılar ise bir şeyi ya da kişinin kendisini saklamasıyla sınırlıdır. Bu yapılara özgü kapsam yalın kullanıma genellenmez.","neighbor_coverage_note":"Dokuz adayın tamamı değerlendirildi. Genel örtme ve saklama adayları seçilen genel gizlilik karşılaştırmalarını yineledi; kaçak gibi saklanma, başkasından bir işi gizleme ve iç yüz alanındaki adaylar daha dar senaryolarda kaldı. Aynı kökün sapma ve bozma dalıyla ise yayınlanabilir bir anlam örtüşmesi bulunmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın çekirdeği genel saklama ve gizlenme işlemidir; komşu dal ise kişinin toplumsal görünürlüğünü bilinçli olarak azaltmasına daha dar biçimde odaklanır.","focus_only":"Bir nesneyi saklamayı ve öznenin bütünüyle gözden çekilmesini de kapsar.","gloss":"kendini görünmez kılma","neighbor_only":"Özellikle kişinin insanlar arasında ün kazanmamasına ve tanınmamasına odaklanır.","neighbor_ref":"root_001097/B008","relation_type":"near_synonym","shared_zone":"Her iki dalda da kişi kendisini başkalarının dikkatinden ve tanınmışlıktan uzak tutar."},{"boundary_match":"partial","distinction":"Komşu dal saklama ve gizlilik alanını genel olarak adlandırır; bu dal ise bir şeyi saklama eylemiyle öznenin kendi görünürlüğünden çekilmesini birlikte sınırlar.","focus_only":"Öznenin gizlenmeye girmesini ve kişinin kendisini silikleştirmesini özel olarak içerir.","gloss":"saklama ve gizlenme","neighbor_only":"Sır tutma, gizlilik ve açıklığın karşıtı olma gibi daha geniş durumları kapsar.","neighbor_ref":"root_000428/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi görünür ve açık olmaktan çıkarma çekirdeğini paylaşır."},{"boundary_match":"partial","distinction":"Bu dalın odağı görünürlükten saklanmadır; komşu dalda belirleyici işlem, bilinen bir içeriği açıklamamak ve dışarıya vermemektir.","focus_only":"Bir nesnenin veya kişinin kendisinin görünürlükten uzaklaştırılmasına dayanır.","gloss":"saklama ve açıklamama","neighbor_only":"Söz, sır, tanıklık, hak veya değerin açıklanmayıp tutulmasına dayanır.","neighbor_ref":"root_001284/B001","relation_type":"near_neighbor","shared_zone":"Her ikisi de bir içeriği başkalarının erişiminden ya da bilgisinden uzak tutabilir."},{"boundary_match":"field_only","distinction":"Bu dal görünmezliğe götüren eylemi anlatır; komşu dal ise ortaya çıkan kişilik durumunu veya kişiye yüklenen niteliği anlatır.","focus_only":"Saklama, gizlenme veya kişinin kendisini geri plana çekmesi biçiminde bir işlem bildirir.","gloss":"gözden çekilme ve siliklik","neighbor_only":"Gizli, silik ya da çok uyuyan bir kişinin niteliğini ve durumunu betimler.","neighbor_ref":"root_000459/B006","relation_type":"same_field","shared_zone":"İki dal da kişinin görünmez, silik ve geri planda kalması alanına temas eder."}],"source_phrase_ar":"دساها أي أخفاها (sihah)؛ دسا إذا استخفى (tahdhib)؛ دس فلان نفسه إذا أخفاها وأخملها (tahdhib)","source_summary":"Kanıt, bir şeyi saklama, öznenin gizlenmesi ve kişinin kendisini gözden uzak tutup silikleştirmesini aynı gizlilik ekseninde birleştirir. Kendine yönelen kullanım, genel saklama çekirdeğine toplumsal görünmezlik ve geri planda kalma boyutu ekler.","sources":["SI","TA"],"what_is_ar":"يدخل فيه دساها بمعنى أخفاها واستخفى ودس نفسه طلبا للخمول.","what_is_not_ar":"لا يدخل فيه معنى زكا أو الظهور والتنمية؛ ولا تجعل مادة دس المضاعفة أصلا مستقلا هنا بلا تنبيه."},"support_links":["sup_1e561cfbfe36088d0209","sup_4bb7a79c106038a0c933","sup_7cdad3ea51c2b6c5520f","sup_88c394817a7712d6ca4c","sup_97485b7f619a0983be42","sup_a0e64d5abd1db23059d0","sup_b182d80b27cf57712aa2","sup_bd44a05b1e9ba9cdf25f","sup_bfdcdef8035e313e8d2d","sup_c049d5b530df51c81252","sup_fbf5dfdbe7be688e19d3"]},{"boundary":"Dal, benliğe yönelen değer düşürme ve kötülüğe sürükleme ile sınırlıdır; ahlaki sonuç taşımayan sıradan saklama bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000476/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"دَسَّىٰ","morph_features":"STEM|POS:V|PERF|LEM:das~aY`|ROOT:dsw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:10:4:1","qac_word_ref":"91:10:4","surface_ar":"دَسَّىٰ"}],"gloss":"benliği arınmanın karşıtına düşürüp değersizleştirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin benliğini arındırıp geliştirmek yerine değerce düşürmesi ve köreltmesidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kendine yönelen kullanımda kişi kendi benliğini silikleştirir, değerini ve elde edeceği payı azaltır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Benliğin kötü davranışların içine sürüklenmesi, değer düşürme çekirdeğinin ahlaki alandaki belirgin sonucudur."}}],"root_ar":"د س و","root_id":"root_000476","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Benliğin arınma ve gelişme yönünün tersine çevrilmesini ve değer kaybını anlatır.","boundary_detail":"Dal, benliğe yönelen değer düşürme ve kötülüğe sürükleme ile sınırlıdır; ahlaki sonuç taşımayan sıradan saklama bu dala girmez.","branch_image_ar":"إخمال النفس وتخسيسها","concept_gloss":"benliği arınmanın karşıtına düşürüp değersizleştirme","contextual_glosses":[{"applicability":"Kişinin kendi benliğinin değerini ve payını düşürdüğü bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Arınmanın bütün karşıtlık alanını ve kötü davranışların içine sürüklenme boyutunu tam vermez.","preserves":"Kişinin kendi benliğine yönelttiği değer düşürme işlemini korur."},"facet_ids":["F001","F002"],"text":"kendini alçaltmak","usage_role":"contextual"},{"applicability":"Benliğin kötü davranışlara yoğun biçimde sokulduğu ahlaki bağlamlara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Benliğin kötü davranışların içine sürüklenmesini ve bunun yoğunluğunu korur."},"facet_ids":["F003"],"text":"kendini kötülüğe gömmek","usage_role":"contextual"},{"applicability":"Arınma ve gelişme yetisinin tersine çevrildiğini açıklamak gereken genel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kötü davranışların içine sürüklenme biçimindeki özel gerçekleşmeyi dışarıda bırakır.","preserves":"Arınma ve gelişme yerine benliğin güçten ve değerden düşmesini korur."},"facet_ids":["F001"],"text":"benliğini köreltmek","usage_role":"explanatory"}],"definition":"Kişinin benliğini arındırıp geliştirmek yerine onu değerce düşürmesi ve köreltmesidir. Yalın kullanım bu olumsuz niteliği, kendine yönelen yapılar ise işlemin kişinin kendi benliğine uygulanmasını bildirir. Özel nesneli kullanımda bu çekirdek, benliğin kötü davranışların içine sürüklenmesi biçiminde gerçekleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin benliğini arındırıp geliştirmek yerine değerce düşürmesi ve köreltmesidir."},{"facet_id":"F002","role":"specialization","statement":"Kendine yönelen kullanımda kişi kendi benliğini silikleştirir, değerini ve elde edeceği payı azaltır."},{"facet_id":"F003","role":"extension","statement":"Benliğin kötü davranışların içine sürüklenmesi, değer düşürme çekirdeğinin ahlaki alandaki belirgin sonucudur."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Ahlaki sonuç taşımayan sıradan saklama anlamını öne çıkarır.","collision":"Aynı kökün görünürlükten saklanma dalıyla karışır.","fit":"displacement","loses":"Arınmanın karşıtı olma, değeri düşürme ve kötü davranışlara sürükleme çekirdeğini kaybeder.","preserves":"Benliği görünürlükten uzaklaştırma çağrışımını sınırlı ölçüde korur."},"text":"gizlemek"}],"identity_rationale":"Yetkili ifade, kişinin benliğini arındırmanın karşıtı bir duruma düşürmesini, onun değerini ve payını azaltmasını ve onu kötü davranışların içine sürüklemesini birlikte bildirir. Hazırlanan çerçeve bu öz-yönelimli değersizleştirme ve bozma çekirdeğini doğru temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"arınmanın karşıtı durumda olmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kendi benliğini arınmanın karşıtına sürüklemek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bu alanda arınmanın karşıtı durumda olmak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"onu kötü davranışlara gömmek"}],"lexicalization_note":"Yalın kullanım benliğin arınmış ve gelişmiş olmasının karşıtı niteliği bildirir; kendine yönelen yapılar bu niteliğin benliğe uygulanmasını, özel nesneli kullanım ise kötü davranışlara sürüklemeyi anlatır. Yapılara özgü ayrıntılar birbirine genellenmez.","neighbor_coverage_note":"On adayın tamamı değerlendirildi. Arınma ve kötülükten sakınma karşıtları ile aynı kökün iki yakın dalı ve genel kötülük niteliği en açıklayıcı sınırları verdi. Saflık, günah, haktan çevirme, yıkım ve adaletten sapma adayları ya seçilen karşıtlıkları yineledi ya da yalnızca daha geniş bir ahlaki alanı paylaştı.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Bu dal benliği arınmanın tersine götürürken komşu dal onu arıtıp düzeltir; ortak bir gelişme ekseninde karşıt yönleri temsil ederler.","focus_only":"Benliğin değerini düşürüp onu kötü davranışlara sürükler.","gloss":"benliği bozma ve arıtma","neighbor_only":"Sınama sonrasında arıtma, düzeltme ve geliştirme işlemini bildirir.","neighbor_ref":"root_001403/B002","relation_type":"polarity_pair","shared_zone":"İki dal da benliğin veya iç dünyanın değer yönünden değiştirilmesini konu edinir."},{"boundary_match":"opposed","distinction":"Bu dal kötü davranışa gömülme yönünü, komşu dal ise ondan çekinip uzaklaşma yönünü gösterir; karşıtlık yalnızca bu ortak ahlaki eksende geçerlidir.","focus_only":"Benliği kötü davranışların içine sürükleyerek değerini düşürür.","gloss":"kötülüğe girme ve kötülükten kaçınma","neighbor_only":"Kötü davranıştan sakınmayı, ondan uzak durmayı veya onun yükünden çıkmayı bildirir.","neighbor_ref":"root_000013/B002","relation_type":"polarity_pair","shared_zone":"İki dal da kişinin kötü davranış karşısındaki yönelişini ve benliğine etkisini konu edinir."},{"boundary_match":"partial","distinction":"Bu dalda silikleşme değer ve davranış yönünden bir bozulmadır; komşu dalda ise belirleyici unsur görünür olmamak ve saklanmaktır.","focus_only":"Benliğin değerini düşürür ve onu kötü davranışlara sürükler.","gloss":"benliği değersizleştirme ve kendini gizleme","neighbor_only":"Bir şeyi veya kişinin kendisini görünürlükten uzaklaştırıp saklar.","neighbor_ref":"root_000476/B001","relation_type":"near_neighbor","shared_zone":"Kişinin kendisini silikleştirmesi iki dalda da yüzeysel bir yakınlık oluşturabilir."},{"boundary_match":"partial","distinction":"Bu dal öz-yönelimli değer düşürmeye dayanır; komşu dal ise yönelimden sapma veya başka birini saptırma ilişkisine dayanır.","focus_only":"Bozucu işlemi kişinin kendi benliğine yöneltir ve arınmanın karşıtıyla tanımlar.","gloss":"kendini bozma ve saptırma","neighbor_only":"Öznenin sapmasını veya başka bir kişiyi saptırıp bozmasını bildirir.","neighbor_ref":"root_000476/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da doğru ve iyi yönden uzaklaşmayla sonuçlanan bir bozulma içerir."},{"boundary_match":"partial","distinction":"Bu dal benliğe yönelen bozucu bir işlemdir; komşu dal ise işlem gerektirmeden kötü veya değersiz olma niteliğini adlandırır.","focus_only":"Kişinin benliğine uyguladığı değersizleştirme ve kötülüğe sürükleme sürecini bildirir.","gloss":"değersizleştirme ve kötülük","neighbor_only":"Bir şeyin, kişinin, sözün veya davranışın kötü ve değersiz niteliğini geniş biçimde betimler.","neighbor_ref":"root_000386/B001","relation_type":"near_neighbor","shared_zone":"İki dal da değer düşüklüğü ve ahlaki kötülük alanında buluşur."}],"source_phrase_ar":"وهو نقيض زكا يزكو زكاء وزكاة وهو داس لا زاك (ayn)؛ خاب من دس نفسه أي أخملها وخسس حظها (tahdhib)؛ دسسها في المعاصي (mufradat)","source_summary":"Kanıtlar, benliği arındırmanın karşıtı olan değersizleştirme ile kötü davranışlara sürüklemeyi aynı öz-yıpratma çerçevesinde birleştirir. Yalın kullanım karşıt niteliği, kendine yönelen kullanımlar ise bu bozucu işlemin kişinin benliğine uygulanmasını belirtir.","sources":["AY","TA","MU"],"what_is_ar":"يدخل فيه نقيض زكا في النفس: دس نفسه، أخملها، خسس حظها، ودسسها في المعاصي.","what_is_not_ar":"لا يدخل فيه مجرد الإخفاء الحسي إذا لم يحمل معنى الخمول أو الفساد."},"support_links":[]},{"boundary":"Dal, öznenin sapması ile başka birini saptırıp bozmayı kapsar; sıradan gizleme ve yalnızca kişinin kendi benliğini değersizleştirmesi bu sınırın dışındadır.","branch_kind":"mixed_non_bare","branch_ref":"root_000476/B003","candidate_links":[{"candidate_id":"cand_a072ff8f7ec7eb77c242","lane":"macro"},{"candidate_id":"cand_897cc19078c266ccd756","lane":"macro"},{"candidate_id":"cand_d639702f530fc65c300d","lane":"macro"},{"candidate_id":"cand_93e9781fb5767daa6a18","lane":"macro"},{"candidate_id":"cand_92526f81d621406e9abe","lane":"macro"},{"candidate_id":"cand_178907ea4e2d8b981b3b","lane":"macro"},{"candidate_id":"cand_4e9ba063a74c9b2bada4","lane":"macro"},{"candidate_id":"cand_4d24e4ae9fd2afc74f7f","lane":"macro"},{"candidate_id":"cand_effac49b63ff6469fec7","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"دَسَّىٰ","morph_features":"STEM|POS:V|PERF|LEM:das~aY`|ROOT:dsw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:10:4:1","qac_word_ref":"91:10:4","surface_ar":"دَسَّىٰ"}],"gloss":"sapma ve başkasını saptırıp bozma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Öznenin doğru yönelimden ayrılarak yanlış bir yöne sapmasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Geçişli yapıda özne başka bir kişiyi doğru yönden uzaklaştırır, saptırır ve bozar."}}],"root_ar":"د س و","root_id":"root_000476","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem öznenin yanlış yöne sapmasını hem de geçişli yapıda başka bir kişinin saptırılıp bozulmasını birlikte karşılar.","boundary_detail":"Dal, öznenin sapması ile başka birini saptırıp bozmayı kapsar; sıradan gizleme ve yalnızca kişinin kendi benliğini değersizleştirmesi bu sınırın dışındadır.","branch_image_ar":"الغواية والإفساد","concept_gloss":"sapma ve başkasını saptırıp bozma","contextual_glosses":[{"applicability":"Öznenin kendi yöneliminden ayrıldığı geçişsiz bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öznenin doğru kabul edilen yönelimden ayrılıp sapmasını korur."},"facet_ids":["F001"],"text":"yoldan sapmak","usage_role":"contextual"},{"applicability":"Bir etkenin başka bir kişiyi yanlış yöne sürükleyip bozduğu geçişli bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başka bir kişiyi saptırma işlemini, katılımcı farkını ve bozucu sonucu korur."},"facet_ids":["F002"],"text":"birini yoldan çıkarıp bozmak","usage_role":"contextual"}],"definition":"Öznenin doğru yönelimden ayrılıp sapmasıdır; kişi nesnesi alan yapıda ise öznenin başka birini doğru yönden uzaklaştırarak saptırıp bozmasıdır. İkinci kullanım, ilkinden farklı olarak bozucu bir etken ile etkilenen kişiyi gerektirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Öznenin doğru yönelimden ayrılarak yanlış bir yöne sapmasıdır."},{"facet_id":"F002","role":"specialization","statement":"Geçişli yapıda özne başka bir kişiyi doğru yönden uzaklaştırır, saptırır ve bozar."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Her tür zarar verme ve işlevsizleştirme anlamıyla karışabilecek kadar geneldir.","fit":"narrowing","loses":"Doğru yönelimden saptırma işlemini ve öznenin kendisinin sapabildiği geçişsiz kullanımı kaybeder.","preserves":"Geçişli kullanımın olumsuz sonuç doğuran bozma yönünü korur."},"text":"bozmak"}],"identity_rationale":"Yetkili ifade iki katılımcı düzenini açıkça ayırır: bir kullanımda özne doğru yönelimden sapar, diğerinde ise bir kişi başka birini saptırıp bozar. Hazırlanan dalın sapma ve bozma çerçevesi bu geçişsizlik ile geçişlilik ayrımını koruduğu sürece kanıtı doğru temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yoldan sapmak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"birini yoldan çıkarıp bozmak"}],"lexicalization_note":"Yalın kullanım öznenin kendisinin sapmasını, kişi nesnesi alan yapı ise öznenin başkasını saptırıp bozmasını bildirir. Geçişli yapının ettirici katılımcı ilişkisi yalın kullanıma taşınmaz.","neighbor_coverage_note":"Dokuz adayın tamamı değerlendirildi. En yakın saptırma dalı ile sapmaya yol açan çekici gösterme, eğrilik, genel bozulma ve yanlışlığa gömülme alanları yayınlandı. İzleri izleme ve başkaldıran kötü varlık adayları yalnızca aynı senaryoya katıldı; yıkım genel bozma adayını yineledi, gizleme dalında ise anlam örtüşmesi yoktu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal geçişsiz sapmayı da içerir ve geçişli kullanımda saptırma ile bozma sonucunu birlikte taşır; komşu dal ise doğru yönden çevirmenin çeşitli araçlarını daha geniş biçimde kapsar.","focus_only":"Öznenin kendisinin sapmasını ve saptırılan kişinin bozulması sonucunu da içerir.","gloss":"saptırıp bozma","neighbor_only":"Doğru yönden çevirmenin yanında istek uyandırma, aldatma ve kötülüğü çekici gösterme yollarını kapsar.","neighbor_ref":"root_001128/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir kişiyi doğru kabul edilen yönden uzaklaştırma işlemini bildirir."},{"boundary_match":"partial","distinction":"Bu dal sapma eylemi ve sonucunu adlandırır; komşu dal ise sapmaya götürebilen çekici gösterme ve kandırma sürecini adlandırır.","focus_only":"Kişinin gerçekten sapmasını veya bir başkasının saptırılıp bozulmasını bildirir.","gloss":"saptırma ve kötülüğü çekici gösterme","neighbor_only":"Yanlış olanı çekici ve doğruymuş gibi göstererek kişiyi kandırma yöntemine odaklanır.","neighbor_ref":"root_000763/B002","relation_type":"near_neighbor","shared_zone":"Kötü bir yönelimin oluşmasına dışarıdan ya da kişinin içinden gelen bir etki katkıda bulunabilir."},{"boundary_match":"partial","distinction":"Bu dal yön değiştirme eylemini ve ettirici kullanımını anlatır; komşu dal ise ortaya çıkan eğri veya bozuk niteliği anlatır.","focus_only":"Bir sapma olayı veya başka birini saptıran etken-katılımcı ilişkisi bildirir.","gloss":"sapma ve eğrilik","neighbor_only":"Düşünce, yaşam veya davranışta düz olmama niteliğini ve eğriliği betimler.","neighbor_ref":"root_001057/B002","relation_type":"near_neighbor","shared_zone":"İki dal da doğru ve düzgün kabul edilen yönden ayrılma alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dalda bozma, kişiyi doğru yönelimden saptırmanın sonucudur; komşu dalda yönelim ilişkisi olmadan genel bozulma ve ziyan öne çıkar.","focus_only":"Doğru yönden sapma ve başka birini bu yöne sürükleme işlemini içerir.","gloss":"saptırma ve bozulma","neighbor_only":"Malın veya başka bir şeyin bozulmasını, ziyan olmasını ve kimi kullanımda ölümü bildirir.","neighbor_ref":"root_000139/B009","relation_type":"near_neighbor","shared_zone":"İki dalın geçişli kullanımlarında olumsuz bir bozma sonucu bulunabilir."},{"boundary_match":"field_only","distinction":"Bu dal yönelim değişikliğini ve bunu doğuran kişiyi ifade edebilir; komşu dal ise gerçeği örten ve kişiyi yanlışlık içinde tutan durumu anlatır.","focus_only":"Sapma hareketini veya başka birini saptıran etkin işlemi bildirir.","gloss":"saptırma ve yanlışlığa gömülme","neighbor_only":"Kişiyi gerçeği görmekten alıkoyan yanlışlık, bilgisizlik, oyalanma ve dalgınlık durumunu betimler.","neighbor_ref":"root_001105/B003","relation_type":"same_field","shared_zone":"İki dal da kişinin gerçek ve doğru olandan uzak kalmasıyla ilişkilidir."}],"source_phrase_ar":"ودسا كقولك غوى (ayn)؛ دسيت أغويت وأفسدت (tahdhib)","source_summary":"Kanıt, öznenin sapmasıyla başka birini saptırıp bozması arasında açık bir katılımcı farkı kurar. İki kullanım doğru yönelimden uzaklaşma sonucunda birleşir; geçişli kullanım bu sonuca dışarıdan etkileyen bir kişi ekler.","sources":["AY","TA"],"what_is_ar":"يدخل فيه دسا بمعنى غوى، ودسيت فلانا أي أغويته وأفسدته.","what_is_not_ar":"لا يدخل فيه الإخفاء المجرد ولا التزكية."},"support_links":["sup_0dfc8c3ded68753a86b6","sup_3d90a7b40391172c5a62","sup_5c62b8c4fd63eb1143df","sup_97485b7f619a0983be42","sup_9be7379ef7e7f26e64c1","sup_b182d80b27cf57712aa2","sup_bd44a05b1e9ba9cdf25f","sup_d239945e97188c332b64","sup_fbf5dfdbe7be688e19d3"]},{"boundary":"Includes overstepping the proper limit in rebellion, the transgressor, the verbal nouns, the causative, and tyrannical personhood.","branch_kind":null,"branch_ref":"root_000937/B001","candidate_links":[{"candidate_id":"cand_a072ff8f7ec7eb77c242","lane":"macro"}],"focus_root_occurrences":[],"gloss":"overstepping the bound in rebellion","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"مجاوزة الحد في العصيان","image_en":"overstepping the bound in rebellion"}}],"root_ar":"ط غ ي","root_id":"root_000937","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"مجاوزة الحد في العصيان","image_en":"overstepping the bound in rebellion","scope_ar":"يدخل فيه طغى وطاغ والطغيان والطغوان والطغوى وأطغاه إذا حمله على الطغيان والطاغية بمعنى الجبار","scope_en":"Includes overstepping the proper limit in rebellion, the transgressor, the verbal nouns, the causative, and tyrannical personhood."},"support_links":["sup_3d90a7b40391172c5a62"]},{"boundary":"A covering or veil over something, including eye or heart covering, covering oneself with a garment, and named covers such as saddle or pack covers.","branch_kind":null,"branch_ref":"root_001088/B001","candidate_links":[{"candidate_id":"cand_e6c4b10b0547c380cfce","lane":"macro"},{"candidate_id":"cand_41845910da30d8ed3c60","lane":"macro"}],"focus_root_occurrences":[],"gloss":"covering veil","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"غطاء يعلو الشيء ويستره","image_en":"covering veil"}}],"root_ar":"غ ش و","root_id":"root_001088","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"غطاء يعلو الشيء ويستره","image_en":"covering veil","scope_ar":"يدخل فيه الغشاء والغطاء والغشاوة على القلب أو البصر، واستغشاء الثوب، وما يسمى غاشية لأنه يغطي كغاشية السرج والرحل.","scope_en":"A covering or veil over something, including eye or heart covering, covering oneself with a garment, and named covers such as saddle or pack covers."},"support_links":["sup_7cdad3ea51c2b6c5520f","sup_bfdcdef8035e313e8d2d"]},{"boundary":"An overwhelming event, punishment, day, or disease called ghashiyah because it covers, envelops, or overtakes.","branch_kind":null,"branch_ref":"root_001088/B002","candidate_links":[{"candidate_id":"cand_e6c4b10b0547c380cfce","lane":"macro"}],"focus_root_occurrences":[],"gloss":"overwhelming affliction","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"غاشية تعم وتجلل","image_en":"overwhelming affliction"}}],"root_ar":"غ ش و","root_id":"root_001088","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"غاشية تعم وتجلل","image_en":"overwhelming affliction","scope_ar":"يدخل فيه الغاشية للقيامة أو العذاب أو النائبة التي تغشى الناس وتعمهم، والداء المسمى غاشية لأنه يأخذ صاحبه.","scope_en":"An overwhelming event, punishment, day, or disease called ghashiyah because it covers, envelops, or overtakes."},"support_links":["sup_bfdcdef8035e313e8d2d"]},{"boundary":"Being overcome, fainting, or having consciousness and understanding covered over, including death-like faintness.","branch_kind":null,"branch_ref":"root_001088/B005","candidate_links":[{"candidate_id":"cand_e6c4b10b0547c380cfce","lane":"macro"}],"focus_root_occurrences":[],"gloss":"being overcome or fainting","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"غشية تغطي الوعي","image_en":"being overcome or fainting"}}],"root_ar":"غ ش و","root_id":"root_001088","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"غشية تغطي الوعي","image_en":"being overcome or fainting","scope_ar":"يدخل فيه غشي عليه وغشيان الموت، أي حالة تنوب الإنسان فتغشى فهمه أو وعيه فيصير مغشيا عليه.","scope_en":"Being overcome, fainting, or having consciousness and understanding covered over, including death-like faintness."},"support_links":["sup_bfdcdef8035e313e8d2d"]},{"boundary":"Includes wickedness, immorality, sins, suspicion, lying, unbelief, disobedience, departure from right, and related physical slant where the sources use the same image of deviation.","branch_kind":null,"branch_ref":"root_001132/B004","candidate_links":[{"candidate_id":"cand_a072ff8f7ec7eb77c242","lane":"macro"},{"candidate_id":"cand_897cc19078c266ccd756","lane":"macro"},{"candidate_id":"cand_93e9781fb5767daa6a18","lane":"macro"}],"focus_root_occurrences":[],"gloss":"departure from right and breach of restraint","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"انحراف عن الحق وخرق الستر","image_en":"departure from right and breach of restraint"}}],"root_ar":"ف ج ر","root_id":"root_001132","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"انحراف عن الحق وخرق الستر","image_en":"departure from right and breach of restraint","scope_ar":"يدخل فيه الفجور والفسق والمعاصي والريبة والكذب والكفر والعصيان والميل عن الحق وما لحق به من ميل حسي","scope_en":"Includes wickedness, immorality, sins, suspicion, lying, unbelief, disobedience, departure from right, and related physical slant where the sources use the same image of deviation."},"support_links":["sup_3d90a7b40391172c5a62","sup_97485b7f619a0983be42","sup_fbf5dfdbe7be688e19d3"]},{"boundary":"Includes the named battle-days of al-Fijar among the Arabs and their naming from violated sanctities.","branch_kind":null,"branch_ref":"root_001132/B006","candidate_links":[{"candidate_id":"cand_a072ff8f7ec7eb77c242","lane":"macro"}],"focus_root_occurrences":[],"gloss":"the Fijar battle-days named for violated sanctity","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"وقائع الفجار لانتهاك الحرمة","image_en":"the Fijar battle-days named for violated sanctity"}}],"root_ar":"ف ج ر","root_id":"root_001132","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"وقائع الفجار لانتهاك الحرمة","image_en":"the Fijar battle-days named for violated sanctity","scope_ar":"يدخل فيه اسم أيام الفجار ووقائعها بين العرب وتسميتها بما وقع فيها من استحلال الحرمات","scope_en":"Includes the named battle-days of al-Fijar among the Arabs and their naming from violated sanctities."},"support_links":["sup_3d90a7b40391172c5a62"]},{"boundary":"Includes iqtala qawlan when it means to draw or pull a statement to oneself, whether good or evil.","branch_kind":null,"branch_ref":"root_001272/B006","candidate_links":[{"candidate_id":"cand_fb41e6a616d99d17db5c","lane":"macro"}],"focus_root_occurrences":[],"gloss":"drawing a saying to oneself","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"اجترار القول إلى النفس","image_en":"drawing a saying to oneself"}}],"root_ar":"ق و ل","root_id":"root_001272","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"اجترار القول إلى النفس","image_en":"drawing a saying to oneself","scope_ar":"يدخل فيه اقتال قولا إذا اجتر إلى نفسه قولا من خير أو شر.","scope_en":"Includes iqtala qawlan when it means to draw or pull a statement to oneself, whether good or evil."},"support_links":["sup_88c394817a7712d6ca4c"]},{"boundary":"Calling the soul الكذوب","branch_kind":null,"branch_ref":"root_001290/B008","candidate_links":[{"candidate_id":"cand_fb41e6a616d99d17db5c","lane":"macro"}],"focus_root_occurrences":[],"gloss":"the soul called al-kadhub","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"النفس الكذوب","image_en":"the soul called al-kadhub"}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"النفس الكذوب","image_en":"the soul called al-kadhub","scope_ar":"يدخل فيه إطلاق الكذوب على النفس","scope_en":"Calling the soul الكذوب"},"support_links":["sup_88c394817a7712d6ca4c"]},{"boundary":"It includes preciousness, desirability, rivalry for a valued thing, and withholding or envy over it because the self values it.","branch_kind":null,"branch_ref":"root_001533/B010","candidate_links":[{"candidate_id":"cand_fb41e6a616d99d17db5c","lane":"macro"}],"focus_root_occurrences":[],"gloss":"precious value desired by selves","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"شيء نفيس تتنافس فيه النفوس","image_en":"precious value desired by selves"}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"شيء نفيس تتنافس فيه النفوس","image_en":"precious value desired by selves","scope_ar":"يدخل فيه النفيس والنفاسة والمنفس، والرغبة والمنافسة في الشيء، والضن أو الحسد به إذا كان لقيمته ورغبة النفس فيه.","scope_en":"It includes preciousness, desirability, rivalry for a valued thing, and withholding or envy over it because the self values it."},"support_links":["sup_88c394817a7712d6ca4c"]},{"boundary":"It includes what is inward in a person: thought, intent, discernment, and hidden inner knowledge.","branch_kind":null,"branch_ref":"root_001533/B013","candidate_links":[{"candidate_id":"cand_fb41e6a616d99d17db5c","lane":"macro"}],"focus_root_occurrences":[],"gloss":"inner mind, thought, or hidden intent","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"ما في النفس من عقل وروع","image_en":"inner mind, thought, or hidden intent"}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"ما في النفس من عقل وروع","image_en":"inner mind, thought, or hidden intent","scope_ar":"يدخل فيه ما في نفس المرء من روع وقصد، ونفس العقل والتمييز، وما يعبر عنه بالغيب أو العندية في سياق ما في النفس.","scope_en":"It includes what is inward in a person: thought, intent, discernment, and hidden inner knowledge."},"support_links":["sup_88c394817a7712d6ca4c"]},{"boundary":"Religious or moral guarding of oneself: اتقاء, تقوى, تقاة, تقية, and تقي, including guarding oneself from God, fire, sin, or feared harm.","branch_kind":null,"branch_ref":"root_001677/B002","candidate_links":[{"candidate_id":"cand_fb41e6a616d99d17db5c","lane":"macro"},{"candidate_id":"cand_4d24e4ae9fd2afc74f7f","lane":"macro"}],"focus_root_occurrences":[],"gloss":"placing the self in protective caution","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"جعل النفس في وقاية","image_en":"placing the self in protective caution"}}],"root_ar":"و ق ي","root_id":"root_001677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"جعل النفس في وقاية","image_en":"placing the self in protective caution","scope_ar":"يدخل فيه اتقى واتقاء وتقوى وتقى وتقاة وتقية وتقي، أي توقي الله أو النار أو المعاصي أو ما يخاف","scope_en":"Religious or moral guarding of oneself: اتقاء, تقوى, تقاة, تقية, and تقي, including guarding oneself from God, fire, sin, or feared harm."},"support_links":["sup_88c394817a7712d6ca4c","sup_b182d80b27cf57712aa2"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000025/B002","candidate_links":[{"candidate_id":"cand_d639702f530fc65c300d","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_c7e52fe07b49160f8b20","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal soft fertile earth supplies a medium in which hiddenness can normally become growth.","root":"ء ر ض","source_ref":"91:6","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000025","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_0dfc8c3ded68753a86b6"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000129/B001","candidate_links":[{"candidate_id":"cand_92526f81d621406e9abe","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_7f3fa272b98cf39c95df","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal stirring of something stationary supplies the transition from latent condition to activated conduct.","root":"ب ع ث","source_ref":"91:12","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000129","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_5c62b8c4fd63eb1143df"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000185/B012","candidate_links":[{"candidate_id":"cand_effac49b63ff6469fec7","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a247670a83178fb34329","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The non-dominant branch's literal following in error supplies transmission by imitation along a sequence.","root":"ت ل و","source_ref":"91:2","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000185","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_d239945e97188c332b64"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000256/B001","candidate_links":[{"candidate_id":"cand_41845910da30d8ed3c60","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_c81bdbc5b1cb2744ee54","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal unveiling and becoming manifest makes disclosure an active operation rather than mere ambient light.","root":"ج ل و","source_ref":"91:3","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000256","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_7cdad3ea51c2b6c5520f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000447/B001","candidate_links":[{"candidate_id":"cand_aba275d909f1d7a713d3","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b2afa8b76c5927994fea","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal dread that anticipates harm supplies the subjective alarm whose absence need not cancel objective failure.","root":"خ و ف","source_ref":"91:15","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000447","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_c049d5b530df51c81252"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000486/B001","candidate_links":[{"candidate_id":"cand_178907ea4e2d8b981b3b","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_f5342c4cdf3948967a9c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal extirpation image supplies the collective terminal scale of the process.","root":"د م د م","source_ref":"91:14","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000486","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_9be7379ef7e7f26e64c1"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000521/B002","candidate_links":[{"candidate_id":"cand_aba275d909f1d7a713d3","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b2afa8b76c5927994fea","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal tail or end of a thing supplies a consequence that remains attached behind the concealed act.","root":"ذ ن ب","source_ref":"91:14","source_word_indices":["6"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000521","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_c049d5b530df51c81252"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000521/B003","candidate_links":[{"candidate_id":"cand_effac49b63ff6469fec7","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a247670a83178fb34329","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal followers or tails image supplies the social remainder that trails and reproduces an initiating corruption.","root":"ذ ن ب","source_ref":"91:14","source_word_indices":["6"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000521","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_d239945e97188c332b64"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000537/B005","candidate_links":[{"candidate_id":"cand_178907ea4e2d8b981b3b","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_f5342c4cdf3948967a9c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The non-dominant mapped branch's literal nourishment and growth image supplies the live counter-mechanism to barrenness and extirpation.","root":"ر ب ب","source_ref":"91:14","source_word_indices":["5"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000537","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_9be7379ef7e7f26e64c1"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000563/B002","candidate_links":[{"candidate_id":"cand_5e39ac9975aea9cead75","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_80f4f35bb41d5e285d09","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal messenger and message externalize the claim, removing lack of communication as the only explanation.","root":"ر س ل","source_ref":"91:13","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000563","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a0e64d5abd1db23059d0"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000637/B001","candidate_links":[{"candidate_id":"cand_d639702f530fc65c300d","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_c7e52fe07b49160f8b20","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal increase and growth image supplies the observable output that differentiates cultivation from burial.","root":"ز ك و","source_ref":"91:9","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000637","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_0dfc8c3ded68753a86b6"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000722/B003","candidate_links":[{"candidate_id":"cand_5e39ac9975aea9cead75","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_80f4f35bb41d5e285d09","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal share of watering and its channel gives the communicated limit a concrete resource-allocation function.","root":"س ق ي","source_ref":"91:13","source_word_indices":["7"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000722","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a0e64d5abd1db23059d0"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000743/B001","candidate_links":[{"candidate_id":"cand_4e9ba063a74c9b2bada4","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_9f2332966a386bfcada6","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The non-dominant branch's literal narrow aperture supplies the small, easily missed route of ingress.","root":"س م و","source_ref":"91:5","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000743","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_bd44a05b1e9ba9cdf25f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000743/B002","candidate_links":[{"candidate_id":"cand_4e9ba063a74c9b2bada4","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_9f2332966a386bfcada6","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The non-dominant branch's literal poison entering a body supplies the cross-domain model of inward corruption.","root":"س م و","source_ref":"91:5","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000743","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_bd44a05b1e9ba9cdf25f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000766/B002","candidate_links":[{"candidate_id":"cand_1387f0b5d53e9de7f7ca","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a3423d04e07cada05829","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal straightness and completion in the entity supplies the formed integrity that concealment deforms.","root":"س و ي","source_ref":"91:7","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000766","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_1e561cfbfe36088d0209"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000766/B011","candidate_links":[{"candidate_id":"cand_1387f0b5d53e9de7f7ca","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a3423d04e07cada05829","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal dropping or omission image activates a terminal flattening pole against the earlier completed form.","root":"س و ي","source_ref":"91:14","source_word_indices":["7"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000766","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_1e561cfbfe36088d0209"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000809/B001","candidate_links":[{"candidate_id":"cand_92526f81d621406e9abe","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_7f3fa272b98cf39c95df","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal wretchedness branch supplies the human proxy in whom the group's buried condition becomes concentrated and visible.","root":"ش ق و","source_ref":"91:12","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000809","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_5c62b8c4fd63eb1143df"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000904/B002","candidate_links":[{"candidate_id":"cand_41845910da30d8ed3c60","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_c81bdbc5b1cb2744ee54","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal emergence into the sun and appearance supplies the expected outward phase that terminal concealment blocks.","root":"ض ح و","source_ref":"91:1","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000904","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_7cdad3ea51c2b6c5520f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000928/B001","candidate_links":[{"candidate_id":"cand_d639702f530fc65c300d","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_c7e52fe07b49160f8b20","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal spreading and extension supplies open room for development, the spatial opposite of suppressive compaction.","root":"ط ح و","source_ref":"91:6","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000928","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_0dfc8c3ded68753a86b6"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000937/B002","candidate_links":[{"candidate_id":"cand_92526f81d621406e9abe","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_7f3fa272b98cf39c95df","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal water rising beyond its limit supplies outward overflow as the release phase of suppressed corruption.","root":"ط غ ي","source_ref":"91:11","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000937","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_5c62b8c4fd63eb1143df"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001033/B006","candidate_links":[{"candidate_id":"cand_aba275d909f1d7a713d3","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b2afa8b76c5927994fea","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal end and aftermath of a thing supplies the later horizon on which failure becomes legible.","root":"ع ق ب","source_ref":"91:15","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001033","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_c049d5b530df51c81252"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001033/B011","candidate_links":[{"candidate_id":"cand_aba275d909f1d7a713d3","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b2afa8b76c5927994fea","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal remainder and trace supplies evidence that burial never fully removes what was done.","root":"ع ق ب","source_ref":"91:15","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001033","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_c049d5b530df51c81252"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001035/B013","candidate_links":[{"candidate_id":"cand_178907ea4e2d8b981b3b","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_f5342c4cdf3948967a9c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal root or base of a thing turns the violent act into removal of generative support.","root":"ع ق ر","source_ref":"91:14","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001035","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_9be7379ef7e7f26e64c1"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001035/B017","candidate_links":[{"candidate_id":"cand_178907ea4e2d8b981b3b","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_f5342c4cdf3948967a9c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal barren sand that does not grow supplies the ecological output of root-cutting.","root":"ع ق ر","source_ref":"91:14","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001035","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_9be7379ef7e7f26e64c1"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001175/B003","candidate_links":[{"candidate_id":"cand_d639702f530fc65c300d","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_c7e52fe07b49160f8b20","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal plougher who cuts earth makes success an active technique of opening a growth channel.","root":"ف ل ح","source_ref":"91:9","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001175","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_0dfc8c3ded68753a86b6"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001272/B012","candidate_links":[{"candidate_id":"cand_5e39ac9975aea9cead75","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_80f4f35bb41d5e285d09","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal saying held within and not manifested supplies an internal acknowledgment that can be buried rather than enacted.","root":"ق و ل","source_ref":"91:13","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001272","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a0e64d5abd1db23059d0"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001290/B009","candidate_links":[{"candidate_id":"cand_21d2c78e6eded8256e81","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_21ab430f853ffc6884c8","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal garment that misreports its wearer's condition gives the concealed self a deceptive social surface.","root":"ك ذ ب","source_ref":"91:11","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001290","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_4bb7a79c106038a0c933"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001381/B001","candidate_links":[{"candidate_id":"cand_4d24e4ae9fd2afc74f7f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_0ae5ea7324c69c39b20c","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal swallowing and taking in completely supplies an ingestion model for inward reception.","root":"ل ه م","source_ref":"91:8","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001381","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b182d80b27cf57712aa2"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001392/B001","candidate_links":[{"candidate_id":"cand_41845910da30d8ed3c60","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_c81bdbc5b1cb2744ee54","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal darkness of night supplies a legitimate bounded interval of hiddenness.","root":"ل ي ل","source_ref":"91:4","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001392","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_7cdad3ea51c2b6c5520f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001533/B012","candidate_links":[{"candidate_id":"cand_1387f0b5d53e9de7f7ca","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_a3423d04e07cada05829","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal identity or very self of a thing makes the buried object a whole rather than one detachable appetite.","root":"ن ف س","source_ref":"91:7","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001533","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_1e561cfbfe36088d0209"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001677/B001","candidate_links":[{"candidate_id":"cand_93e9781fb5767daa6a18","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_1149dc9ef7bcc9dddbee","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The literal warding of harm supplies the protective function whose failure permits covert ingress.","root":"و ق ي","source_ref":"91:8","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001677","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_97485b7f619a0983be42"]}],"candidate_inventory":[{"anchor_refs":["91:10","91:11","91:8"],"branch_refs":["root_000476/B003","root_000937/B001","root_001132/B004","root_001132/B006"],"candidate_id":"cand_a072ff8f7ec7eb77c242","commentary_obligation":"review","focus_branch_refs":["root_000476/B003"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000937/B001","root_001132/B004","root_001132/B006"],"root_ids":[],"scope":"pericope","source_local_id":"A:Rebellion and Boundary Crossing","source_type":"channel","support_ids":["sup_3d90a7b40391172c5a62","sup_6bfbfa7ec596c44e71f7","sup_99c62958c58da96af2f6","sup_c175d1a153b2f4bd857b","sup_fc137caa1ce638fd21db"],"title":"Rebellion and Boundary Crossing","trust":"trusted","unresolved_branch_citations":[{"citation":"ط غ و/B001","reason":"no registered branch match"},{"citation":"ط غ و/B003","reason":"no registered branch match"},{"citation":"ط غ و/B004","reason":"no registered branch match"}],"unresolved_branch_refs":[]},{"anchor_refs":["91:10","91:8"],"branch_refs":["root_000451/B001","root_000476/B001","root_000476/B003","root_001132/B004"],"candidate_id":"cand_897cc19078c266ccd756","commentary_obligation":"review","focus_branch_refs":["root_000451/B001","root_000476/B001","root_000476/B003"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_001132/B004"],"root_ids":[],"scope":"pericope","source_local_id":"C:Concealment, Corruption, and Failure","source_type":"channel","support_ids":["sup_3284e00c9e6ae5c78331","sup_5e81cac8e7beb87e303b","sup_b211f60b95dd1046e7fb","sup_ee32bdcc03bebd7f7cfd","sup_fbf5dfdbe7be688e19d3"],"title":"Concealment, Corruption, and Failure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["91:10","91:11","91:13","91:14","91:7","91:8"],"branch_refs":["root_000476/B001","root_001272/B006","root_001290/B008","root_001533/B010","root_001533/B013","root_001677/B002"],"candidate_id":"cand_fb41e6a616d99d17db5c","commentary_obligation":"review","focus_branch_refs":["root_000476/B001"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_001272/B006","root_001290/B008","root_001533/B010","root_001533/B013","root_001677/B002"],"root_ids":[],"scope":"pericope","source_local_id":"D:Deceptive Impulse and Divided Interior","source_type":"channel","support_ids":["sup_18265744a4403597bbfb","sup_6d033e5e86550a68528a","sup_88c394817a7712d6ca4c","sup_9d8ac03997b266ea0577","sup_a20edda17205780aa0d2"],"title":"Deceptive Impulse and Divided Interior","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["91:10","91:4"],"branch_refs":["root_000476/B001","root_001088/B001","root_001088/B002","root_001088/B005"],"candidate_id":"cand_e6c4b10b0547c380cfce","commentary_obligation":"review","focus_branch_refs":["root_000476/B001"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_001088/B001","root_001088/B002","root_001088/B005"],"root_ids":[],"scope":"pericope","source_local_id":"D:Veiling and Loss of Awareness","source_type":"channel","support_ids":["sup_47d303ad71b41e69a8fe","sup_57aa31b21fb8ac1ac953","sup_6945605fbf9bf82e41c3","sup_6b43f7e8e28870567b68","sup_bfdcdef8035e313e8d2d"],"title":"Veiling and Loss of Awareness","trust":"trusted","unresolved_branch_citations":[{"citation":"غ ش ي/B007","reason":"no registered branch match"}],"unresolved_branch_refs":[]},{"anchor_refs":["91:1","91:10","91:3","91:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:10","branch_refs":["root_000256/B001","root_000476/B001","root_000904/B002","root_001088/B001","root_001392/B001"],"candidate_id":"cand_41845910da30d8ed3c60","commentary_obligation":"review","hft_ref":"hft_c81bdbc5b1cb2744ee54","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta-terminal-cover-versus-rhythm","source_type":"hft","support_ids":["sup_7cdad3ea51c2b6c5520f"],"title":"delta-terminal-cover-versus-rhythm","trust":"legacy_unbound"},{"anchor_refs":["91:10","91:6","91:9"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:10","branch_refs":["root_000025/B002","root_000451/B004","root_000476/B003","root_000637/B001","root_000928/B001","root_001175/B003"],"candidate_id":"cand_d639702f530fc65c300d","commentary_obligation":"review","hft_ref":"hft_c7e52fe07b49160f8b20","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta-anti-cultivation","source_type":"hft","support_ids":["sup_0dfc8c3ded68753a86b6"],"title":"delta-anti-cultivation","trust":"legacy_unbound"},{"anchor_refs":["91:10","91:14","91:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:10","branch_refs":["root_000476/B001","root_000766/B002","root_000766/B011","root_001533/B012"],"candidate_id":"cand_1387f0b5d53e9de7f7ca","commentary_obligation":"review","hft_ref":"hft_a3423d04e07cada05829","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta-whole-self-flattening","source_type":"hft","support_ids":["sup_1e561cfbfe36088d0209"],"title":"delta-whole-self-flattening","trust":"legacy_unbound"},{"anchor_refs":["91:10","91:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:10","branch_refs":["root_000476/B001","root_000476/B003","root_001132/B004","root_001677/B001"],"candidate_id":"cand_93e9781fb5767daa6a18","commentary_obligation":"review","hft_ref":"hft_1149dc9ef7bcc9dddbee","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta-covert-ingress","source_type":"hft","support_ids":["sup_97485b7f619a0983be42"],"title":"delta-covert-ingress","trust":"legacy_unbound"},{"anchor_refs":["91:10","91:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:10","branch_refs":["root_000451/B003","root_000476/B001","root_001290/B009"],"candidate_id":"cand_21d2c78e6eded8256e81","commentary_obligation":"review","hft_ref":"hft_21ab430f853ffc6884c8","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta-deceptive-garment","source_type":"hft","support_ids":["sup_4bb7a79c106038a0c933"],"title":"delta-deceptive-garment","trust":"legacy_unbound"},{"anchor_refs":["91:10","91:11","91:12"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:10","branch_refs":["root_000129/B001","root_000476/B003","root_000809/B001","root_000937/B002"],"candidate_id":"cand_92526f81d621406e9abe","commentary_obligation":"review","hft_ref":"hft_7f3fa272b98cf39c95df","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta-latent-pressure-proxy","source_type":"hft","support_ids":["sup_5c62b8c4fd63eb1143df"],"title":"delta-latent-pressure-proxy","trust":"legacy_unbound"},{"anchor_refs":["91:10","91:13"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:10","branch_refs":["root_000476/B001","root_000563/B002","root_000722/B003","root_001272/B012"],"candidate_id":"cand_5e39ac9975aea9cead75","commentary_obligation":"review","hft_ref":"hft_80f4f35bb41d5e285d09","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta-suppressed-message-and-share","source_type":"hft","support_ids":["sup_a0e64d5abd1db23059d0"],"title":"delta-suppressed-message-and-share","trust":"legacy_unbound"},{"anchor_refs":["91:10","91:14"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:10","branch_refs":["root_000451/B004","root_000476/B003","root_000486/B001","root_000537/B005","root_001035/B013","root_001035/B017"],"candidate_id":"cand_178907ea4e2d8b981b3b","commentary_obligation":"review","hft_ref":"hft_f5342c4cdf3948967a9c","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta-root-cutting-scale","source_type":"hft","support_ids":["sup_9be7379ef7e7f26e64c1"],"title":"delta-root-cutting-scale","trust":"legacy_unbound"},{"anchor_refs":["91:10","91:14","91:15"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:10","branch_refs":["root_000447/B001","root_000451/B001","root_000476/B001","root_000521/B002","root_001033/B006","root_001033/B011"],"candidate_id":"cand_aba275d909f1d7a713d3","commentary_obligation":"review","hft_ref":"hft_b2afa8b76c5927994fea","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta-delayed-aftermath","source_type":"hft","support_ids":["sup_c049d5b530df51c81252"],"title":"delta-delayed-aftermath","trust":"legacy_unbound"},{"anchor_refs":["91:10","91:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:10","branch_refs":["root_000476/B001","root_000476/B003","root_000743/B001","root_000743/B002"],"candidate_id":"cand_4e9ba063a74c9b2bada4","commentary_obligation":"review","hft_ref":"hft_9f2332966a386bfcada6","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier-aperture-and-poison","source_type":"hft","support_ids":["sup_bd44a05b1e9ba9cdf25f"],"title":"outlier-aperture-and-poison","trust":"legacy_unbound"},{"anchor_refs":["91:10","91:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:10","branch_refs":["root_000476/B001","root_000476/B003","root_001381/B001","root_001677/B002"],"candidate_id":"cand_4d24e4ae9fd2afc74f7f","commentary_obligation":"review","hft_ref":"hft_0ae5ea7324c69c39b20c","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier-undigested-inspiration","source_type":"hft","support_ids":["sup_b182d80b27cf57712aa2"],"title":"outlier-undigested-inspiration","trust":"legacy_unbound"},{"anchor_refs":["91:10","91:14","91:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:10","branch_refs":["root_000185/B012","root_000476/B003","root_000521/B003"],"candidate_id":"cand_effac49b63ff6469fec7","commentary_obligation":"review","hft_ref":"hft_a247670a83178fb34329","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier-propagated-burial","source_type":"hft","support_ids":["sup_d239945e97188c332b64"],"title":"outlier-propagated-burial","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_08180bd1ce3760139f2a","connection_ref":"conn_8dc5a7f65402684c16b5","note":"The immediate positive counterpart makes cleansing versus burying the passage's central polarity.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_2cbbe000036d3248318a","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"91:9","source_note":"Immediate contrary sequel: corrupting the self marks the failed alternative.","source_row_role":"ranked_review","source_target_component_ref":"91:10","source_target_components":["91:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:10"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"91:9","source_target_components":["91:9"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:9","target_evidence":{"arabic_uthmani":"قَدْ أَفْلَحَ مَن زَكَّىٰهَا","ayah_ref":"91:9"},"target_ref":"91:9"},{"connection_evidence_ref":"conn_ev_6a76dc073b27e7d6e5c3","connection_ref":"conn_4e607710bec60aa2ac1f","note":"Its covering image supplies a non-agentive parallel to concealment, delimiting the focus's active verb.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_6d7c0d1a8a4454db5317","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"91:4","source_note":"The adjacent self-context makes the f01 reading about self-concealment salient.","source_row_role":"ranked_review","source_target_component_ref":"91:10","source_target_components":["91:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:10"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"91:4","source_target_components":["91:4"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:4","target_evidence":{"arabic_uthmani":"وَٱلَّيْلِ إِذَا يَغْشَىٰهَا","ayah_ref":"91:4"},"target_ref":"91:4"},{"connection_evidence_ref":"conn_ev_f723c033abe3da48214a","connection_ref":"conn_fd0c1095166785663e3e","note":"Directly establishes the self whose suppression and failure the focus predicates.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_26bc28cfbb31ff0bff6c","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"91:7","source_note":"Immediate sequel defines the contrary outcome of corrupting the self.","source_row_role":"ranked_review","source_target_component_ref":"91:10","source_target_components":["91:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:10"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"91:7","source_target_components":["91:7"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:7","target_evidence":{"arabic_uthmani":"وَنَفْسٍۢ وَمَا سَوَّىٰهَا","ayah_ref":"91:7"},"target_ref":"91:7"},{"connection_evidence_ref":"conn_ev_ec119177dbd0db37cde0","connection_ref":"conn_d7d72f87ae6ee310e743","note":"The self's two moral directions supplies the immediate alternative within which burial operates.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_8aebb0127f833629e300","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"91:8","source_note":"Immediate ch033 counterpart: the same nafs receives f02's negative moral outcome.","source_row_role":"ranked_review","source_target_component_ref":"91:10","source_target_components":["91:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:10"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"91:8","source_target_components":["91:8"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:8","target_evidence":{"arabic_uthmani":"فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا","ayah_ref":"91:8"},"target_ref":"91:8"},{"connection_evidence_ref":"conn_ev_8b2788836281a05b3383","connection_ref":"conn_afad2d2a51a5bcc6a164","note":"The next verse begins the Thamud case with transgression, opening the focus's social sequel.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_4c463bed25fd7de236c6","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"91:11","source_note":"Immediate moral contrast before the Thamud example.","source_row_role":"ranked_review","source_target_component_ref":"91:10","source_target_components":["91:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:10"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"91:11","source_target_components":["91:11"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:11","target_evidence":{"arabic_uthmani":"كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ","ayah_ref":"91:11"},"target_ref":"91:11"},{"connection_evidence_ref":"conn_ev_419684792e66250cba90","connection_ref":"conn_89f5564fb1822017b4f7","note":"Daylight's revealing forms a useful contrary image to the focus's burying and concealment.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_957b48b16f761569c42c","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"91:3","source_note":"Immediate moral culmination gives the oath sequence a consequential horizon.","source_row_role":"ranked_review","source_target_component_ref":"91:10","source_target_components":["91:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:10"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"91:3","source_target_components":["91:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:3","target_evidence":{"arabic_uthmani":"وَٱلنَّهَارِ إِذَا جَلَّىٰهَا","ayah_ref":"91:3"},"target_ref":"91:3"},{"connection_evidence_ref":"conn_ev_f06e014e3d106d26768c","connection_ref":"conn_f3e584509d29db643366","note":"The oath's earth-forming image does not materially clarify the moral predicate.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_a99328447dd4cd3a1d21","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"91:6","source_note":"Immediate f03 contrary: the self can be buried rather than cultivated.","source_row_role":"ranked_review","source_target_component_ref":"91:10","source_target_components":["91:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:10"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"91:6","source_target_components":["91:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:6","target_evidence":{"arabic_uthmani":"وَٱلْأَرْضِ وَمَا طَحَىٰهَا","ayah_ref":"91:6"},"target_ref":"91:6"},{"connection_evidence_ref":"conn_ev_9a5121295ac6a9123495","connection_ref":"conn_cd411ddb4f83e1009ea4","note":"The solar oath gives a distant illumination contrast but no specific account of failure.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_eb0684a49ba7ada7157b","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"91:1","source_note":"Local moral outcome relates the oath opening to concealment, not solar detail.","source_row_role":"ranked_review","source_target_component_ref":"91:10","source_target_components":["91:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:10"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"91:1","source_target_components":["91:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:1","target_evidence":{"arabic_uthmani":"وَٱلشَّمْسِ وَضُحَىٰهَا","ayah_ref":"91:1"},"target_ref":"91:1"},{"connection_evidence_ref":"conn_ev_1d361327886c4eb651a7","connection_ref":"conn_67d56cd7793145814d00","note":"This oath element supplies no distinct route after the surrounding 91 material.","origin":"authored_focus_row","prior_label":"no value","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_cb1c42168ac388d16cd4","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"91:2","source_note":"Başarısızlığın karşı sonuç oluşu, f05'in surenin sonunda açılan yönünü destekler.","source_row_role":"ranked_review","source_target_component_ref":"91:10","source_target_components":["91:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:10"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"91:2","source_target_components":["91:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:2","target_evidence":{"arabic_uthmani":"وَٱلْقَمَرِ إِذَا تَلَىٰهَا","ayah_ref":"91:2"},"target_ref":"91:2"},{"connection_evidence_ref":"conn_ev_ddedb84d5db034341425","connection_ref":"conn_561d0679093f9abe2d30","note":"The oath's construction image does not add to the self's moral failure.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_179603fc8f75607a6fbf","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"91:5","source_note":"Failure through corrupting the self supplies the direct contrary inner outcome.","source_row_role":"ranked_review","source_target_component_ref":"91:10","source_target_components":["91:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:10"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"91:5","source_target_components":["91:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:5","target_evidence":{"arabic_uthmani":"وَٱلسَّمَآءِ وَمَا بَنَىٰهَا","ayah_ref":"91:5"},"target_ref":"91:5"},{"connection_evidence_ref":"conn_ev_b524a0be71f426eb2aa1","connection_ref":"conn_32ff84cc7e9a812dc9dc","note":"The messenger's restraint within the Thamud account advances the social test that follows.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_62a3882b87e6623b64de","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"91:13","source_note":"Nearby moral framing, but no direct directive or protected resource.","source_row_role":"ranked_review","source_target_component_ref":"91:10","source_target_components":["91:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:10"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"91:13","source_target_components":["91:13"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:13","target_evidence":{"arabic_uthmani":"فَقَالَ لَهُمْ رَسُولُ ٱللَّهِ نَاقَةَ ٱللَّهِ وَسُقْيَٰهَا","ayah_ref":"91:13"},"target_ref":"91:13"},{"connection_evidence_ref":"conn_ev_25a8f8a675524fe371c7","connection_ref":"conn_ebd01f80f806630c2457","note":"Thamud's rejection and destructive aftermath concretize a possible social consequence of transgression.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_ba8c903b52dd727825be","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"91:14","source_note":"Immediate failure counterpart to 91:9 before the Thamud account.","source_row_role":"ranked_review","source_target_component_ref":"91:10","source_target_components":["91:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:10"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"91:14","source_target_components":["91:14"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:14","target_evidence":{"arabic_uthmani":"فَكَذَّبُوهُ فَعَقَرُوهَا فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا","ayah_ref":"91:14"},"target_ref":"91:14"},{"connection_evidence_ref":"conn_ev_beeedb0014bceb6bd43e","connection_ref":"conn_0691f263cecc0e3c2f43","note":"The immediate sequel identifies the wretched initiator, advancing the focus's social trajectory.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":false,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"91:12","source_target_components":["91:12"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:12","target_evidence":{"arabic_uthmani":"إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا","ayah_ref":"91:12"},"target_ref":"91:12"},{"connection_evidence_ref":"conn_ev_ce8013ed180272e172c8","connection_ref":"conn_7bc7fd6b110395a3932c","note":"The close of the Thamud sequence sharpens the question of consequence and finality.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":true,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_4a8343238bdf4311c676","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"91:15","source_note":"Completes the immediate moral polarity by naming failure through corruption.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"91:10","source_target_components":["91:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:10"}],"relation_scope":"declared_pericope","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"91:15","source_target_components":["91:15"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"91:15","target_evidence":{"arabic_uthmani":"وَلَا يَخَافُ عُقْبَٰهَا","ayah_ref":"91:15"},"target_ref":"91:15"}],"focus":{"arabic_uthmani":"وَقَدْ خَابَ مَن دَسَّىٰهَا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"91:10:1:1","qac_word_ref":"91:10:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"قَد","morph_features":"STEM|POS:CERT|LEM:qad","morpheme_role":"STEM","pos":"CERT","qac_ref":"91:10:1:2","qac_word_ref":"91:10:1","root_ar":"","surface_ar":"قَدْ"},{"lemma_ar":"خَابَ","morph_features":"STEM|POS:V|PERF|LEM:xaAba|ROOT:xyb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:10:2:1","qac_word_ref":"91:10:2","root_ar":"خ ي ب","surface_ar":"خَابَ"},{"lemma_ar":"مَن","morph_features":"STEM|POS:REL|LEM:man","morpheme_role":"STEM","pos":"REL","qac_ref":"91:10:3:1","qac_word_ref":"91:10:3","root_ar":"","surface_ar":"مَن"},{"lemma_ar":"دَسَّىٰ","morph_features":"STEM|POS:V|PERF|LEM:das~aY`|ROOT:dsw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:10:4:1","qac_word_ref":"91:10:4","root_ar":"د س و","surface_ar":"دَسَّىٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:10:4:2","qac_word_ref":"91:10:4","root_ar":"","surface_ar":"هَا"}],"word_analysis_qac_refs":[["91:10:1:1"],["91:10:1:2"],["91:10:2:1"],["91:10:3:1"],["91:10:4:1","91:10:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["91:10:1","91:10:2","91:10:3","91:10:4","91:10:5"]},"focus_surface_evidence":{"arabic_uthmani":"وَقَدْ خَابَ مَن دَسَّىٰهَا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"91:10:1:1","qac_word_ref":"91:10:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"قَد","morph_features":"STEM|POS:CERT|LEM:qad","morpheme_role":"STEM","pos":"CERT","qac_ref":"91:10:1:2","qac_word_ref":"91:10:1","root_ar":"","surface_ar":"قَدْ"},{"lemma_ar":"خَابَ","morph_features":"STEM|POS:V|PERF|LEM:xaAba|ROOT:xyb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:10:2:1","qac_word_ref":"91:10:2","root_ar":"خ ي ب","surface_ar":"خَابَ"},{"lemma_ar":"مَن","morph_features":"STEM|POS:REL|LEM:man","morpheme_role":"STEM","pos":"REL","qac_ref":"91:10:3:1","qac_word_ref":"91:10:3","root_ar":"","surface_ar":"مَن"},{"lemma_ar":"دَسَّىٰ","morph_features":"STEM|POS:V|PERF|LEM:das~aY`|ROOT:dsw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"91:10:4:1","qac_word_ref":"91:10:4","root_ar":"د س و","surface_ar":"دَسَّىٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:10:4:2","qac_word_ref":"91:10:4","root_ar":"","surface_ar":"هَا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["91:10:1:1"],["91:10:1:2"],["91:10:2:1"],["91:10:3:1"],["91:10:4:1","91:10:4:2"]],"word_analysis_refs":["91:10:1","91:10:2","91:10:3","91:10:4","91:10:5"],"word_rows":[{"analysis_record_ref":"91:10:1","analytic_gloss_range_en":"opening conjunction that joins the clause to 91:9 while the paired verdicts make the joining contrastive","analytic_root_gloss_range_en":null,"qac_refs":["91:10:1:1"],"root":{"note":"(no root)"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"91:10:2","analytic_gloss_range_en":"certainty particle before a perfect verb, giving the failure verdict certified and accomplished force rather than probability","analytic_root_gloss_range_en":null,"qac_refs":["91:10:1:2"],"root":{"note":"(no root)"},"surface":{"arabic":"قَدْ","transliteration":"qad"}},{"analysis_record_ref":"91:10:3","analytic_gloss_range_en":"certified, completed failure borne by the agent himself; locally the sense is total moral non-attainment rather than failing at a specified object","analytic_root_gloss_range_en":"root range centered on failing to obtain what was sought, deprivation, disappointment, and loss; other lexical images such as a sparkless fire-stick or named falsehood expressions are not locally selected","qac_refs":["91:10:2:1"],"root":{"arabic":"خ ي ب","transliteration":"kh-y-b"},"surface":{"arabic":"خَابَ","transliteration":"khāba"}},{"analysis_record_ref":"91:10:4","analytic_gloss_range_en":"generic relative subject with live conditional force, identifying the failed class by the act that follows rather than by a named identity","analytic_root_gloss_range_en":null,"qac_refs":["91:10:3:1"],"root":{"note":"(no root)"},"surface":{"arabic":"مَن","transliteration":"man"}},{"analysis_record_ref":"91:10:5","analytic_gloss_range_en":"completed transitive soul-burying or corrupting act, with concealment, suppression, covert insertion, and self-debasement converging on the prior soul object","analytic_root_gloss_range_en":"root range around hidden insertion, concealment, self-lowering away from purity, burying in sins, straying, and spoiling; the local object and paired purification clause select soul-corruption rather than a literal burial scene","qac_refs":["91:10:4:1","91:10:4:2"],"root":{"arabic":"د س و","transliteration":"d-s-w"},"surface":{"arabic":"دَسَّىٰهَا","transliteration":"dassāhā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":15,"missing_anchor_refs":[],"supplied_unique_anchor_count":15},"assigned_record_count":12,"assigned_records":[{"anchor_refs":["91:1","91:10","91:3","91:4"],"branch_refs":["root_000256/B001","root_000476/B001","root_000904/B002","root_001088/B001","root_001392/B001"],"candidate_id":"cand_41845910da30d8ed3c60","evidence_scope":"declared_pericope","hft_ref":"hft_c81bdbc5b1cb2744ee54","item_id":"delta-terminal-cover-versus-rhythm","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta-terminal-cover-versus-rhythm","support_id":"sup_7cdad3ea51c2b6c5520f"},{"anchor_refs":["91:10","91:6","91:9"],"branch_refs":["root_000025/B002","root_000451/B004","root_000476/B003","root_000637/B001","root_000928/B001","root_001175/B003"],"candidate_id":"cand_d639702f530fc65c300d","evidence_scope":"declared_pericope","hft_ref":"hft_c7e52fe07b49160f8b20","item_id":"delta-anti-cultivation","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta-anti-cultivation","support_id":"sup_0dfc8c3ded68753a86b6"},{"anchor_refs":["91:10","91:14","91:7"],"branch_refs":["root_000476/B001","root_000766/B002","root_000766/B011","root_001533/B012"],"candidate_id":"cand_1387f0b5d53e9de7f7ca","evidence_scope":"declared_pericope","hft_ref":"hft_a3423d04e07cada05829","item_id":"delta-whole-self-flattening","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta-whole-self-flattening","support_id":"sup_1e561cfbfe36088d0209"},{"anchor_refs":["91:10","91:8"],"branch_refs":["root_000476/B001","root_000476/B003","root_001132/B004","root_001677/B001"],"candidate_id":"cand_93e9781fb5767daa6a18","evidence_scope":"declared_pericope","hft_ref":"hft_1149dc9ef7bcc9dddbee","item_id":"delta-covert-ingress","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta-covert-ingress","support_id":"sup_97485b7f619a0983be42"},{"anchor_refs":["91:10","91:11"],"branch_refs":["root_000451/B003","root_000476/B001","root_001290/B009"],"candidate_id":"cand_21d2c78e6eded8256e81","evidence_scope":"declared_pericope","hft_ref":"hft_21ab430f853ffc6884c8","item_id":"delta-deceptive-garment","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta-deceptive-garment","support_id":"sup_4bb7a79c106038a0c933"},{"anchor_refs":["91:10","91:11","91:12"],"branch_refs":["root_000129/B001","root_000476/B003","root_000809/B001","root_000937/B002"],"candidate_id":"cand_92526f81d621406e9abe","evidence_scope":"declared_pericope","hft_ref":"hft_7f3fa272b98cf39c95df","item_id":"delta-latent-pressure-proxy","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta-latent-pressure-proxy","support_id":"sup_5c62b8c4fd63eb1143df"},{"anchor_refs":["91:10","91:13"],"branch_refs":["root_000476/B001","root_000563/B002","root_000722/B003","root_001272/B012"],"candidate_id":"cand_5e39ac9975aea9cead75","evidence_scope":"declared_pericope","hft_ref":"hft_80f4f35bb41d5e285d09","item_id":"delta-suppressed-message-and-share","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta-suppressed-message-and-share","support_id":"sup_a0e64d5abd1db23059d0"},{"anchor_refs":["91:10","91:14"],"branch_refs":["root_000451/B004","root_000476/B003","root_000486/B001","root_000537/B005","root_001035/B013","root_001035/B017"],"candidate_id":"cand_178907ea4e2d8b981b3b","evidence_scope":"declared_pericope","hft_ref":"hft_f5342c4cdf3948967a9c","item_id":"delta-root-cutting-scale","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta-root-cutting-scale","support_id":"sup_9be7379ef7e7f26e64c1"},{"anchor_refs":["91:10","91:14","91:15"],"branch_refs":["root_000447/B001","root_000451/B001","root_000476/B001","root_000521/B002","root_001033/B006","root_001033/B011"],"candidate_id":"cand_aba275d909f1d7a713d3","evidence_scope":"declared_pericope","hft_ref":"hft_b2afa8b76c5927994fea","item_id":"delta-delayed-aftermath","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta-delayed-aftermath","support_id":"sup_c049d5b530df51c81252"},{"anchor_refs":["91:10","91:5"],"branch_refs":["root_000476/B001","root_000476/B003","root_000743/B001","root_000743/B002"],"candidate_id":"cand_4e9ba063a74c9b2bada4","evidence_scope":"declared_pericope","hft_ref":"hft_9f2332966a386bfcada6","item_id":"outlier-aperture-and-poison","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier-aperture-and-poison","support_id":"sup_bd44a05b1e9ba9cdf25f"},{"anchor_refs":["91:10","91:8"],"branch_refs":["root_000476/B001","root_000476/B003","root_001381/B001","root_001677/B002"],"candidate_id":"cand_4d24e4ae9fd2afc74f7f","evidence_scope":"declared_pericope","hft_ref":"hft_0ae5ea7324c69c39b20c","item_id":"outlier-undigested-inspiration","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier-undigested-inspiration","support_id":"sup_b182d80b27cf57712aa2"},{"anchor_refs":["91:10","91:14","91:2"],"branch_refs":["root_000185/B012","root_000476/B003","root_000521/B003"],"candidate_id":"cand_effac49b63ff6469fec7","evidence_scope":"declared_pericope","hft_ref":"hft_a247670a83178fb34329","item_id":"outlier-propagated-burial","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier-propagated-burial","support_id":"sup_d239945e97188c332b64"}],"diagnostics":[],"lane_counts":{"global":10,"macro":12,"micro":4},"packet_summary":{"ayah_count":15,"focus_ref":"91:10","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ت ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000186","furuq_root_norm":"ت ل و","furuq_source_root_norm":"ت ل و","is_dominant":true,"target_occurrences":39,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000185","furuq_root_norm":"ت ل ل","furuq_source_root_norm":"ت ل ل","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["91:1","91:2","91:3","91:4","91:5","91:6","91:7","91:8","91:9","91:10","91:11","91:12","91:13","91:14","91:15"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"91:10","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":16,"unstructured_record_count":0},"identity":{"ayah_ref":"91:10","lane":"macro","linguistic_source_ref":"91:10","surface_ref":"91:10","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"91:10","target_tokens":[["Onu",["91:10:4"]],["yozlaştıran",["91:10:3","91:10:4"]],["ise",["91:10:1"]],["gerçekten",["91:10:1"]],["kaybetmiştir",["91:10:2"]]],"text":"Onu yozlaştıran ise gerçekten kaybetmiştir."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":12,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":1,"ayah_to":15,"id":"s091-p01-001-015","label":"Whole surah","number":1,"refs":["91:1","91:2","91:3","91:4","91:5","91:6","91:7","91:8","91:9","91:10","91:11","91:12","91:13","91:14","91:15"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"91:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"91:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["91:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"91:0"}],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"D:Deceptive Impulse and Divided Interior","source_type":"channel","support_id":"sup_18265744a4403597bbfb","text":"An inner impulse conceals itself, fabricates a claim, and competes with reflective intention.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"C:Concealment, Corruption, and Failure","source_type":"channel","support_id":"sup_3284e00c9e6ae5c78331","text":"91:8 `فجورها`; 91:10 `خاب` and `دساها`","trust":"trusted"},{"branch_refs":["root_000476/B003","root_000937/B001","root_001132/B004","root_001132/B006"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"A:Rebellion and Boundary Crossing","source_type":"channel","support_id":"sup_3d90a7b40391172c5a62","text":"transgression beyond bounds `ط غ ي:B001/m01`; rebellious excess `ط غ و:B001/m01`; heads of misguidance `ط غ و:B003/m01` and `ط غ ي:B003/m01`; coercive tyrant `ط غ و:B004/m01`; moral breach `ف ج ر:B004/m01`; sacrilegious conflict `ف ج ر:B006/m01`; induced corruption `د س و:B003/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"D:Veiling and Loss of Awareness","source_type":"channel","support_id":"sup_47d303ad71b41e69a8fe","text":"91:4 `يغشاها`; 91:10 `دساها`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"D:Veiling and Loss of Awareness","source_type":"channel","support_id":"sup_57aa31b21fb8ac1ac953","text":"A covering descends over an object, a population, or consciousness itself.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"C:Concealment, Corruption, and Failure","source_type":"channel","support_id":"sup_5e81cac8e7beb87e303b","text":"Burial provides the governing image: what should be formed and purified is instead pushed down and obscured. Corruption redirects it, moral breach opens a path away from right order, and failure names the resulting deprivation.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"D:Veiling and Loss of Awareness","source_type":"channel","support_id":"sup_6945605fbf9bf82e41c3","text":"The night’s covering expands into a general mechanism of occlusion. Cloth, disaster, fainting, and deliberate hiding each place a layer between a subject and visibility, awareness, or social notice.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"D:Veiling and Loss of Awareness","source_type":"channel","support_id":"sup_6b43f7e8e28870567b68","text":"A field becomes visible, bright, veiled, or perceptually inaccessible through recurring changes of light and covering.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Rebellion and Boundary Crossing","source_type":"channel","support_id":"sup_6bfbfa7ec596c44e71f7","text":"91:8 `فجورها`; 91:10 `دساها`; 91:11 `طغواها`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"D:Deceptive Impulse and Divided Interior","source_type":"channel","support_id":"sup_6d033e5e86550a68528a","text":"The interior is a contested space rather than a single voice. Desire and a concealed impulse generate a private account, while intention and restraint determine whether that account remains deceptive or is brought under moral protection.","trust":"trusted"},{"branch_refs":["root_000476/B001","root_001272/B006","root_001290/B008","root_001533/B010","root_001533/B013","root_001677/B002"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"D:Deceptive Impulse and Divided Interior","source_type":"channel","support_id":"sup_88c394817a7712d6ca4c","text":"deceitful self `ك ذ ب:B008/m01`; concealed inward impulse `د س و:B001/m01`; inwardly drawn saying `ق و ل:B006/m01`; inward intention `ن ف س:B013/m02`; desire for the precious `ن ف س:B010/m01`; protective restraint `و ق ي:B002/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Rebellion and Boundary Crossing","source_type":"channel","support_id":"sup_99c62958c58da96af2f6","text":"A participant exceeds a rightful measure, rejects restraint, and becomes a source of misguidance.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"D:Deceptive Impulse and Divided Interior","source_type":"channel","support_id":"sup_9d8ac03997b266ea0577","text":"91:7 `نفس`; 91:8 `تقواها`; 91:10 `دساها`; 91:11 and 91:14 forms of `كذب`; 91:13 `قال`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"D:Deceptive Impulse and Divided Interior","source_type":"channel","support_id":"sup_a20edda17205780aa0d2","text":"The inner person is formed through cognition, protection, purification, concealment, or corruption, and those operations issue in flourishing or failure.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"C:Concealment, Corruption, and Failure","source_type":"channel","support_id":"sup_b211f60b95dd1046e7fb","text":"The inner person is formed through cognition, protection, purification, concealment, or corruption, and those operations issue in flourishing or failure.","trust":"trusted"},{"branch_refs":["root_000476/B001","root_001088/B001","root_001088/B002","root_001088/B005"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"D:Veiling and Loss of Awareness","source_type":"channel","support_id":"sup_bfdcdef8035e313e8d2d","text":"material or perceptual covering `غ ش و:B001/m01` and `غ ش ي:B001/m01`; all-enveloping affliction `غ ش و:B002/m01`; swoon or deathly obscuration `غ ش و:B005/m01`; loss of understanding `غ ش ي:B007/m01`; stealthy self-concealment `د س و:B001/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Rebellion and Boundary Crossing","source_type":"channel","support_id":"sup_c175d1a153b2f4bd857b","text":"Force crosses a limit, confronts an opponent, competes for dominance, gathers collectively, and may culminate in destructive overpowering.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"C:Concealment, Corruption, and Failure","source_type":"channel","support_id":"sup_ee32bdcc03bebd7f7cfd","text":"The self is buried from view, turned away from right order, and deprived of its sought outcome.","trust":"trusted"},{"branch_refs":["root_000451/B001","root_000476/B001","root_000476/B003","root_001132/B004"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"C:Concealment, Corruption, and Failure","source_type":"channel","support_id":"sup_fbf5dfdbe7be688e19d3","text":"stealthy burial `د س و:B001/m01`; misguidance and corruption `د س و:B003/m01`; breach of moral bounds `ف ج ر:B004/m01`; failure and deprivation `خ ي ب:B001/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Rebellion and Boundary Crossing","source_type":"channel","support_id":"sup_fc137caa1ce638fd21db","text":"Transgression is a failure of measure that becomes socially active. The rebel crosses a boundary, the head of misguidance redirects others, and the tyrant converts excess into coercive rule.","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلشَّمْسِ وَضُحَىٰهَا","ayah_ref":"91:1"},{"arabic_uthmani":"وَقَدْ خَابَ مَن دَسَّىٰهَا","ayah_ref":"91:10"},{"arabic_uthmani":"وَٱلنَّهَارِ إِذَا جَلَّىٰهَا","ayah_ref":"91:3"},{"arabic_uthmani":"وَٱلَّيْلِ إِذَا يَغْشَىٰهَا","ayah_ref":"91:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":4,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":4,"target_morphology_supplied":false},"branch_refs":["root_000256/B001","root_000476/B001","root_000904/B002","root_001088/B001","root_001392/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000476","role":"The literal hiding operation remains the focus anchor whose duration and function are revised by the surrounding cycle.","root":"د س و","source_ref":"91:10","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000904","role":"The literal emergence into the sun and appearance supplies the expected outward phase that terminal concealment blocks.","root":"ض ح و","source_ref":"91:1","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000256","role":"The literal unveiling and becoming manifest makes disclosure an active operation rather than mere ambient light.","root":"ج ل و","source_ref":"91:3","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001392","role":"The literal darkness of night supplies a legitimate bounded interval of hiddenness.","root":"ل ي ل","source_ref":"91:4","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001088","role":"The literal cover laid over a thing shows that covering can serve a rhythm, sharpening the focus act as cover made one-way.","root":"غ ش و","source_ref":"91:4","source_word_indices":["3"]}],"changed_reading":{"after":"Cover can be legitimate and temporary; failure lies in turning it into a closed state that prevents renewed disclosure.","before":"Concealment itself is intrinsically the failure."},"confidence":"strong","mechanism":"The context gives both emergence into light and legitimate nocturnal covering. This prevents a flat equation of all hiddenness with corruption: دَسَّىٰهَا becomes terminal or mistimed concealment, a cover that refuses the return to disclosure and therefore arrests the cycle by which hidden potential becomes visible.","model_id":"delta-terminal-cover-versus-rhythm","reader_inference":"The packet supplies appearance, unveiling, night, and covering; I infer that their alternation sets a functional norm and that the focus act fails by making concealment terminal. A live alternative is that دَسَّىٰهَا names direct corruption without any temporal claim.","status":"revised","structural_cues":["The repeated feminine -hā object moves through exposure, unveiling, and covering before returning in دَسَّىٰهَا.","Day and night alternate; the focus verb supplies no corresponding re-emergence."],"trigger_roots":["ض ح و","ج ل و","ل ي ل","غ ش و"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta-terminal-cover-versus-rhythm","source_type":"hft","support_id":"sup_7cdad3ea51c2b6c5520f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَقَدْ خَابَ مَن دَسَّىٰهَا","ayah_ref":"91:10"},{"arabic_uthmani":"وَٱلْأَرْضِ وَمَا طَحَىٰهَا","ayah_ref":"91:6"},{"arabic_uthmani":"قَدْ أَفْلَحَ مَن زَكَّىٰهَا","ayah_ref":"91:9"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000025/B002","root_000451/B004","root_000476/B003","root_000637/B001","root_000928/B001","root_001175/B003"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000451","role":"The literal rainless land and deprivation image supplies the sterile endpoint of failed cultivation.","root":"خ ي ب","source_ref":"91:10","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000476","role":"The literal spoiling operation distinguishes corrupt burial from generative placement in soil.","root":"د س و","source_ref":"91:10","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000025","role":"The literal soft fertile earth supplies a medium in which hiddenness can normally become growth.","root":"ء ر ض","source_ref":"91:6","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000928","role":"The literal spreading and extension supplies open room for development, the spatial opposite of suppressive compaction.","root":"ط ح و","source_ref":"91:6","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_001175","role":"The literal plougher who cuts earth makes success an active technique of opening a growth channel.","root":"ف ل ح","source_ref":"91:9","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000637","role":"The literal increase and growth image supplies the observable output that differentiates cultivation from burial.","root":"ز ك و","source_ref":"91:9","source_word_indices":["4"]}],"changed_reading":{"after":"The decisive question is whether hidden potential can emerge and increase: failure is a corrupt burial that makes the inner ground sterile.","before":"Putting the referent under cover is itself the condemned act."},"confidence":"strong","mechanism":"The earth, its spreading, the furrow-maker, and growth transform burial into an agronomic test. Hiding is not automatically sterile—a seed also enters the ground—but دَسَّىٰهَا is the handling that corrupts, compacts, or withholds conditions of emergence, while the adjacent alternative opens a furrow and tends increase.","model_id":"delta-anti-cultivation","reader_inference":"The packet supplies fertile earth, spatial spreading, a plougher, growth, corrupting concealment, and rainless deprivation; I map the self to soil or seed and construe دَسَّىٰهَا as anti-cultivation. The live alternative is a non-material contrast of purification and corruption.","status":"strengthened","structural_cues":["91:9 and 91:10 mirror قَدْ plus an outcome verb plus مَن plus a causative verb with -hā.","The success verb immediately before the focus ayah also carries an earth-cutting branch."],"trigger_roots":["ء ر ض","ط ح و","ف ل ح","ز ك و"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta-anti-cultivation","source_type":"hft","support_id":"sup_0dfc8c3ded68753a86b6","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَقَدْ خَابَ مَن دَسَّىٰهَا","ayah_ref":"91:10"},{"arabic_uthmani":"فَكَذَّبُوهُ فَعَقَرُوهَا فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا","ayah_ref":"91:14"},{"arabic_uthmani":"وَنَفْسٍۢ وَمَا سَوَّىٰهَا","ayah_ref":"91:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000476/B001","root_000766/B002","root_000766/B011","root_001533/B012"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000476","role":"The literal concealment image supplies the inward act by which the formed self is made absent.","root":"د س و","source_ref":"91:10","source_word_indices":["4"]},{"branch_id":"B012","mapped_root_id":"root_001533","role":"The literal identity or very self of a thing makes the buried object a whole rather than one detachable appetite.","root":"ن ف س","source_ref":"91:7","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000766","role":"The literal straightness and completion in the entity supplies the formed integrity that concealment deforms.","root":"س و ي","source_ref":"91:7","source_word_indices":["3"]},{"branch_id":"B011","mapped_root_id":"root_000766","role":"The literal dropping or omission image activates a terminal flattening pole against the earlier completed form.","root":"س و ي","source_ref":"91:14","source_word_indices":["7"]}],"changed_reading":{"after":"The person makes the whole formed self unavailable and flattened, rehearsing inwardly a loss of distinction that can later appear at collective scale.","before":"A person hides one morally bad feature of an otherwise intact self."},"confidence":"medium","mechanism":"The context identifies the recurring feminine referent with the self as a whole and brackets it between formation and later leveling or omission. دَسَّىٰهَا can therefore be read as self-erasure: hiding or corrupting the whole formed self until its distinctions are flattened, an inward small-scale analogue of the terminal leveling later applied collectively.","model_id":"delta-whole-self-flattening","reader_inference":"The packet supplies selfhood, completed form, and a later omission branch; I infer semantic bracketing and an inward-to-collective scale relation. A live alternative is that the two س و ي occurrences carry separate constructive and destructive senses without making the focus act their bridge.","status":"revised","structural_cues":["The same root س و ي and feminine object occur before and after the focus pair, at 91:7 and 91:14.","The -hā chain allows the inward focus act and the later collective endpoint to echo without forcing identical referents."],"trigger_roots":["ن ف س","س و ي"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta-whole-self-flattening","source_type":"hft","support_id":"sup_1e561cfbfe36088d0209","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَقَدْ خَابَ مَن دَسَّىٰهَا","ayah_ref":"91:10"},{"arabic_uthmani":"فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا","ayah_ref":"91:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000476/B001","root_000476/B003","root_001132/B004","root_001677/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000476","role":"The literal hidden insertion image supplies covert inward entry as an alternative direction for the focus operation.","root":"د س و","source_ref":"91:10","source_word_indices":["4"]},{"branch_id":"B003","mapped_root_id":"root_000476","role":"The literal spoiling image identifies the functional effect of what is covertly inserted.","root":"د س و","source_ref":"91:10","source_word_indices":["4"]},{"branch_id":"B004","mapped_root_id":"root_001132","role":"The literal deviation and breach of a covering supplies the compromised boundary through which hidden corruption can enter.","root":"ف ج ر","source_ref":"91:8","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001677","role":"The literal warding of harm supplies the protective function whose failure permits covert ingress.","root":"و ق ي","source_ref":"91:8","source_word_indices":["3"]}],"changed_reading":{"after":"The agent may also corrupt the self by admitting or planting something covertly inside it through a breached protective boundary.","before":"The agent covers or buries the self from the outside."},"confidence":"medium","mechanism":"The insertion side of د س و becomes active beside a breached covering and a protective barrier. The focus can describe not only pushing the self out of sight but also placing corruptive material secretly into it through a failed boundary.","model_id":"delta-covert-ingress","reader_inference":"The packet supplies hidden insertion, spoiling, a breached cover, and protection; I supply the arrow in which a breached boundary permits corruptive ingress. The materially live alternative is the more direct outward reading: the agent hides the self rather than inserts anything into it.","status":"new","structural_cues":["91:8 places rupture and protection as paired possibilities before the two opposed outcomes in 91:9-10.","The object suffix on دَسَّىٰهَا favors hiding the self, but the root inventory independently preserves insertion as a live directional possibility."],"trigger_roots":["ف ج ر","و ق ي"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta-covert-ingress","source_type":"hft","support_id":"sup_97485b7f619a0983be42","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَقَدْ خَابَ مَن دَسَّىٰهَا","ayah_ref":"91:10"},{"arabic_uthmani":"كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ","ayah_ref":"91:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000451/B003","root_000476/B001","root_001290/B009"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000451","role":"The literal vanity or falsehood image supplies the empty claim whose promised result fails.","root":"خ ي ب","source_ref":"91:10","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000476","role":"The literal concealment image places the actual inner condition beneath an exterior.","root":"د س و","source_ref":"91:10","source_word_indices":["4"]},{"branch_id":"B009","mapped_root_id":"root_001290","role":"The literal garment that misreports its wearer's condition gives the concealed self a deceptive social surface.","root":"ك ذ ب","source_ref":"91:11","source_word_indices":["1"]}],"changed_reading":{"after":"Burial generates a false public surface, so the failure includes maintaining an appearance that conceals and misstates the self beneath it.","before":"The buried condition is private and socially invisible."},"confidence":"medium","mechanism":"The later denial activates a garment-like false exterior. Concealment does not leave a neutral blank; it enables a presentation that lies about the condition beneath it, turning inward suppression into public misrepresentation.","model_id":"delta-deceptive-garment","reader_inference":"The packet supplies vanity, concealment, and a garment whose appearance is false; I infer that the false exterior forms over the hidden self. A live alternative is that denial merely follows corruption without functioning as its covering surface.","status":"strengthened","structural_cues":["The narrative resumes immediately after the focus verdict with collective denial.","A singular inward operation is followed by a plural public act, permitting a scale shift from self-concealment to shared appearance."],"trigger_roots":["ك ذ ب"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta-deceptive-garment","source_type":"hft","support_id":"sup_4bb7a79c106038a0c933","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَقَدْ خَابَ مَن دَسَّىٰهَا","ayah_ref":"91:10"},{"arabic_uthmani":"كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ","ayah_ref":"91:11"},{"arabic_uthmani":"إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا","ayah_ref":"91:12"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000129/B001","root_000476/B003","root_000809/B001","root_000937/B002"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000476","role":"The literal corruption image supplies the latent disposition stored within the person or group.","root":"د س و","source_ref":"91:10","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000937","role":"The literal water rising beyond its limit supplies outward overflow as the release phase of suppressed corruption.","root":"ط غ ي","source_ref":"91:11","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000129","role":"The literal stirring of something stationary supplies the transition from latent condition to activated conduct.","root":"ب ع ث","source_ref":"91:12","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000809","role":"The literal wretchedness branch supplies the human proxy in whom the group's buried condition becomes concentrated and visible.","root":"ش ق و","source_ref":"91:12","source_word_indices":["3"]}],"changed_reading":{"after":"A group may bury a shared disposition until it overflows through an activated representative, while personal agency remains live within the collective mechanism.","before":"One isolated person privately corrupts one isolated self."},"confidence":"medium","mechanism":"Inward suppression and outward excess become opposite phases of one latent system. What a group keeps hidden can accumulate like overpassing water, be stirred from rest, and emerge through a single maximally wretched agent; the focus subject can thus be carried at both personal and collective scales.","model_id":"delta-latent-pressure-proxy","reader_inference":"The packet supplies concealment or corruption, floodlike excess, arousal from rest, and a wretched agent; I infer a compression-to-release chain and collective externalization through a proxy. A live alternative is that these are parallel moral facts and the later actor is independently responsible rather than an outlet for the group.","status":"new","structural_cues":["The sequence after the focus moves from collective transgression to the arousal of one superlative individual.","The focus uses indefinite مَن, which can remain personal while also serving as a pattern instantiated within a group."],"trigger_roots":["ط غ ي","ب ع ث","ش ق و"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta-latent-pressure-proxy","source_type":"hft","support_id":"sup_5c62b8c4fd63eb1143df","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَقَدْ خَابَ مَن دَسَّىٰهَا","ayah_ref":"91:10"},{"arabic_uthmani":"فَقَالَ لَهُمْ رَسُولُ ٱللَّهِ نَاقَةَ ٱللَّهِ وَسُقْيَٰهَا","ayah_ref":"91:13"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000476/B001","root_000563/B002","root_000722/B003","root_001272/B012"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000476","role":"The literal concealment image supplies the suppression of a claim that has reached awareness.","root":"د س و","source_ref":"91:10","source_word_indices":["4"]},{"branch_id":"B012","mapped_root_id":"root_001272","role":"The literal saying held within and not manifested supplies an internal acknowledgment that can be buried rather than enacted.","root":"ق و ل","source_ref":"91:13","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000563","role":"The literal messenger and message externalize the claim, removing lack of communication as the only explanation.","root":"ر س ل","source_ref":"91:13","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_000722","role":"The literal share of watering and its channel gives the communicated limit a concrete resource-allocation function.","root":"س ق ي","source_ref":"91:13","source_word_indices":["7"]}],"changed_reading":{"after":"The failure can consist in burying a limit already known inwardly and stated publicly, especially when that limit governs another's share.","before":"The failure comes from a vague inner corruption or lack of moral awareness."},"confidence":"exploratory","mechanism":"Speech, message, and an allotted channel of water make the buried content more specific: it can be an already recognized claim that is kept from governing conduct. Failure is then not simple ignorance but suppression of an inwardly apprehended and publicly articulated limit.","model_id":"delta-suppressed-message-and-share","reader_inference":"The packet supplies inward unspoken saying, an external message, and a watering allotment; I infer that دَسَّىٰهَا can suppress recognition of another's concrete claim. A live alternative is that these details only narrate a later episode and do not specify what was buried in the focus ayah.","status":"new","structural_cues":["91:13 combines an act of saying with a named living claimant and its watering claim.","The message follows the activation of an agent, so knowledge and action are narratively separated."],"trigger_roots":["ق و ل","ر س ل","س ق ي"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta-suppressed-message-and-share","source_type":"hft","support_id":"sup_a0e64d5abd1db23059d0","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَقَدْ خَابَ مَن دَسَّىٰهَا","ayah_ref":"91:10"},{"arabic_uthmani":"فَكَذَّبُوهُ فَعَقَرُوهَا فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا","ayah_ref":"91:14"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000451/B004","root_000476/B003","root_000486/B001","root_000537/B005","root_001035/B013","root_001035/B017"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000451","role":"The literal rainless deprivation image supplies sterility as the focus-level result.","root":"خ ي ب","source_ref":"91:10","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000476","role":"The literal spoiling image supplies the inward first stage of the destructive progression.","root":"د س و","source_ref":"91:10","source_word_indices":["4"]},{"branch_id":"B013","mapped_root_id":"root_001035","role":"The literal root or base of a thing turns the violent act into removal of generative support.","root":"ع ق ر","source_ref":"91:14","source_word_indices":["2"]},{"branch_id":"B017","mapped_root_id":"root_001035","role":"The literal barren sand that does not grow supplies the ecological output of root-cutting.","root":"ع ق ر","source_ref":"91:14","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000486","role":"The literal extirpation image supplies the collective terminal scale of the process.","root":"د م د م","source_ref":"91:14","source_word_indices":["3"]},{"branch_id":"B005","mapped_root_id":"root_000537","role":"The non-dominant mapped branch's literal nourishment and growth image supplies the live counter-mechanism to barrenness and extirpation.","root":"ر ب ب","source_ref":"91:14","source_word_indices":["5"]}],"changed_reading":{"after":"Inner spoiling tends toward cutting the roots of shared life, replacing nourishment and growth with barrenness and eventual extirpation.","before":"Inner corruption can remain concealed and bounded within its possessor."},"confidence":"medium","mechanism":"The later sequence scales inner spoiling into destruction of generative infrastructure: the root is cut, the medium becomes barren, and extirpation follows, opposite a branch of nourishment and growth. دَسَّىٰهَا is therefore a small-scale beginning of root-destruction, not a condition that remains safely hidden.","model_id":"delta-root-cutting-scale","reader_inference":"The packet supplies spoiling, root or base, barrenness, extirpation, and a split-root nourishment image; I align them as a scale progression from inward damage to destroyed generativity. A live alternative is that the later actions are consequences in narrative sequence but do not unpack the inner mechanics of دَسَّىٰهَا.","status":"strengthened","structural_cues":["Repeated fa- in 91:14 accelerates denial, hamstringing, and extirpation into a causal-looking sequence.","The earlier growth contrast of 91:9-10 returns at a larger ecological and communal scale."],"trigger_roots":["ع ق ر","د م د م","ر ب ب"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta-root-cutting-scale","source_type":"hft","support_id":"sup_9be7379ef7e7f26e64c1","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَقَدْ خَابَ مَن دَسَّىٰهَا","ayah_ref":"91:10"},{"arabic_uthmani":"فَكَذَّبُوهُ فَعَقَرُوهَا فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا","ayah_ref":"91:14"},{"arabic_uthmani":"وَلَا يَخَافُ عُقْبَٰهَا","ayah_ref":"91:15"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000447/B001","root_000451/B001","root_000476/B001","root_000521/B002","root_001033/B006","root_001033/B011"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000451","role":"The literal missing of the sought result supplies failure as an outcome measured beyond the immediate act.","root":"خ ي ب","source_ref":"91:10","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000476","role":"The literal concealment image supplies the apparent disappearance of the cause before its effects return.","root":"د س و","source_ref":"91:10","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000521","role":"The literal tail or end of a thing supplies a consequence that remains attached behind the concealed act.","root":"ذ ن ب","source_ref":"91:14","source_word_indices":["6"]},{"branch_id":"B001","mapped_root_id":"root_000447","role":"The literal dread that anticipates harm supplies the subjective alarm whose absence need not cancel objective failure.","root":"خ و ف","source_ref":"91:15","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_001033","role":"The literal end and aftermath of a thing supplies the later horizon on which failure becomes legible.","root":"ع ق ب","source_ref":"91:15","source_word_indices":["3"]},{"branch_id":"B011","mapped_root_id":"root_001033","role":"The literal remainder and trace supplies evidence that burial never fully removes what was done.","root":"ع ق ب","source_ref":"91:15","source_word_indices":["3"]}],"changed_reading":{"after":"The agent may seem successful and feel no alarm in the short term; failure is disclosed by the tail, remainder, and aftermath that concealment cannot erase.","before":"Failure is an immediate disappointment that the agent should feel at once."},"confidence":"strong","mechanism":"Tail, end, expected harm, aftermath, and remainder make failure longitudinal. Concealment can appear to erase a cause and may produce no immediate alarm, but what is hidden leaves a trailing effect by which the verdict خَابَ is eventually disclosed.","model_id":"delta-delayed-aftermath","reader_inference":"The packet supplies a tail or end, anticipatory fear, aftermath, and residual trace; I infer that hidden causes return through delayed effects and that felt fear is not the measure of failure. A live alternative is that the aftermath language belongs only to the later destructive act, not to the focus subject's concealment.","status":"revised","structural_cues":["ذَنۢبِهِمْ in 91:14 and عُقْبَٰهَا in 91:15 close the sequence with tail, end, and consequence vocabulary.","The perfect خَابَ can state a verdict whose evidence unfolds after the concealing act."],"trigger_roots":["ذ ن ب","خ و ف","ع ق ب"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta-delayed-aftermath","source_type":"hft","support_id":"sup_c049d5b530df51c81252","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَقَدْ خَابَ مَن دَسَّىٰهَا","ayah_ref":"91:10"},{"arabic_uthmani":"وَٱلسَّمَآءِ وَمَا بَنَىٰهَا","ayah_ref":"91:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000476/B001","root_000476/B003","root_000743/B001","root_000743/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000476","role":"The literal hidden insertion image anchors the direction of covert entry.","root":"د س و","source_ref":"91:10","source_word_indices":["4"]},{"branch_id":"B003","mapped_root_id":"root_000476","role":"The literal spoiling image anchors the harmful transformation caused after entry.","root":"د س و","source_ref":"91:10","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000743","role":"The non-dominant branch's literal narrow aperture supplies the small, easily missed route of ingress.","root":"س م و","source_ref":"91:5","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000743","role":"The non-dominant branch's literal poison entering a body supplies the cross-domain model of inward corruption.","root":"س م و","source_ref":"91:5","source_word_indices":["1"]}],"changed_reading":{"after":"Corruption may begin as minute covert ingress through an unguarded aperture and spoil the self from within before concealment is noticed.","before":"Self-corruption is a large, visible choice to bury the whole self."},"confidence":"exploratory","containment":"This is surprising because it is activated by a non-dominant split mapping of the sky root into narrow-aperture and poison imagery, not by the ordinary sky sense. It remains valid as a material analogy because the focus root itself supplies hidden insertion and corruption. Downstream prose should label it an exploratory ingress model, never a lexical claim that the sky wording means poison.","focus_anchor":"The insertion and spoiling possibilities inside دَسَّىٰهَا anchor a model of corruption entering covertly through a minute opening.","outlier_id":"outlier-aperture-and-poison"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier-aperture-and-poison","source_type":"hft","support_id":"sup_bd44a05b1e9ba9cdf25f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَقَدْ خَابَ مَن دَسَّىٰهَا","ayah_ref":"91:10"},{"arabic_uthmani":"فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا","ayah_ref":"91:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000476/B001","root_000476/B003","root_001381/B001","root_001677/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000476","role":"The literal hidden insertion image anchors inward reception that remains unexposed and unworked.","root":"د س و","source_ref":"91:10","source_word_indices":["4"]},{"branch_id":"B003","mapped_root_id":"root_000476","role":"The literal spoiling image supplies the risk when received material is not differentiated or transformed.","root":"د س و","source_ref":"91:10","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_001381","role":"The literal swallowing and taking in completely supplies an ingestion model for inward reception.","root":"ل ه م","source_ref":"91:8","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001677","role":"The literal placing of oneself within protection supplies the selective boundary needed for safe inward reception.","root":"و ق ي","source_ref":"91:8","source_word_indices":["3"]}],"changed_reading":{"after":"What enters inwardly must be discriminated and integrated; swallowing it whole and leaving it hidden can turn reception into an undigested source of corruption.","before":"Receiving an inner distinction is sufficient so long as it is present somewhere within."},"confidence":"exploratory","containment":"This is surprising because the packet's ل ه م inventory activates swallowing rather than an ordinary cognitive gloss. It remains anchored through the focus root's covert insertion and corruption, producing a testable ingestion analogy: inward reception without transformation. Downstream prose should present this only as a branch-triggered model and must not imply that inspiration itself is corrupt.","focus_anchor":"دَسَّىٰهَا can picture content placed secretly within and then spoiled, allowing the inward reception of 91:8 to be tested as digestion rather than mere possession.","outlier_id":"outlier-undigested-inspiration"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier-undigested-inspiration","source_type":"hft","support_id":"sup_b182d80b27cf57712aa2","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَقَدْ خَابَ مَن دَسَّىٰهَا","ayah_ref":"91:10"},{"arabic_uthmani":"فَكَذَّبُوهُ فَعَقَرُوهَا فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا","ayah_ref":"91:14"},{"arabic_uthmani":"وَٱلْقَمَرِ إِذَا تَلَىٰهَا","ayah_ref":"91:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000185/B012","root_000476/B003","root_000521/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000476","role":"The literal leading-astray and spoiling image anchors an operation that can be done to another and therefore copied socially.","root":"د س و","source_ref":"91:10","source_word_indices":["4"]},{"branch_id":"B012","mapped_root_id":"root_000185","role":"The non-dominant branch's literal following in error supplies transmission by imitation along a sequence.","root":"ت ل و","source_ref":"91:2","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_000521","role":"The literal followers or tails image supplies the social remainder that trails and reproduces an initiating corruption.","root":"ذ ن ب","source_ref":"91:14","source_word_indices":["6"]}],"changed_reading":{"after":"The corrupted pattern can acquire followers, propagate by imitation, and leave a social tail beyond the initiating self.","before":"The buried corruption ends within the individual who performs it."},"confidence":"exploratory","containment":"This is surprising because it joins a non-dominant split branch of ت ل و with the follower or tail branch of ذ ن ب across a wide span. It remains anchored in the focus root's explicit spoiling of a person and explains how an inward pattern could become transmissible. Downstream prose should qualify it as a social propagation model, not a direct sense of any one focus word.","focus_anchor":"The corrupting sense of دَسَّىٰ permits the focus operation to become a pattern learned and repeated rather than an isolated hidden state.","outlier_id":"outlier-propagated-burial"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier-propagated-burial","source_type":"hft","support_id":"sup_d239945e97188c332b64","trust":"legacy_unbound"}]}
</lane_packet_json>
