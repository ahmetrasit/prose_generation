# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **101:10**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s101-regular-20260911/s101/101_10/micro.discovery.json` and modify nothing
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
  "ayah_ref": "101:10",
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
{"branch_registry":[{"boundary":"Çekirdek, bir kaynağın bol ürün vermesidir; kalıplaşmış övgü, yergi ve bolluk anlatımları ayrı uzantılardır.","branch_kind":"mixed_non_bare","branch_ref":"root_000469/B001","candidate_links":[{"candidate_id":"cand_5d9699d27c78bce7443f","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَدْرَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>adoraY`|ROOT:dry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"101:10:2:1","qac_word_ref":"101:10:2","surface_ar":"أَدْرَىٰ"}],"gloss":"bir kaynaktan bolca çıkma veya bol ürün verme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sıvı veya ürün, kendi doğal kaynağından bolca çıkar ya da akar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Süt verme ve bulutun bol yağmur bırakması, çekirdeğin başlıca somut gerçekleşmeleridir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Vergi gelirinin çoğalması ve pazarın canlanması, bol ürün verme düşüncesinin soyut uzantılarıdır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Övgü ve yergi sözleri ile dişi keçinin erkeği istemesi yalnız kendi kalıplarında geçerli bağlantılı kullanımlardır."}}],"root_ar":"د ر ي","root_id":"root_000469","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Somut akış çekirdeğini ve bu çekirdeğe dayanan üretkenlik düşüncesini birlikte anlatan genel karşılıktır.","boundary_detail":"Çekirdek, bir kaynağın bol ürün vermesidir; kalıplaşmış övgü, yergi ve bolluk anlatımları ayrı uzantılardır.","branch_image_ar":"درور الشيء وخروجه غزيرا من مصدره","concept_gloss":"bir kaynaktan bolca çıkma veya bol ürün verme","contextual_glosses":[{"applicability":"Meme veya süt veren hayvan bağlamında doğal ve doğrudan kullanılan karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yağmur, gözyaşı, gelir, pazar ve kalıplaşmış söz kullanımlarını dışarıda bırakır.","preserves":"Doğal bir kaynağın bol ürün vermesi özelliğini korur."},"facet_ids":["F001","F002"],"text":"bol süt vermek","usage_role":"contextual"},{"applicability":"Gökyüzü veya bulutun çok yağmur vermesini anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Süt ve öteki sıvılarla soyut bolluk uzantılarını karşılamaz.","preserves":"Kaynağından bolca çıkan yağmur ve süreklilik düşüncesini korur."},"facet_ids":["F001","F002"],"text":"bol bol yağmak","usage_role":"contextual"},{"applicability":"Vergi geliri ve pazarın canlanması gibi soyut bolluk bağlamlarını açıklamak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Somut sıvı çıkışını ve kalıplaşmış övgü-yergi kullanımlarını dışarıda bırakır.","preserves":"Bol ürün verme düşüncesinin ekonomik uzantısını korur."},"facet_ids":["F003"],"text":"geliri veya sürümü artmak","usage_role":"explanatory"}],"definition":"Bir kaynaktan süt, yağmur, gözyaşı ya da benzeri bir ürünün bolca çıkması veya kaynağın bunu bolca vermesidir. Bu çekirdek, gelir ve pazarın artması gibi bolluk anlatımlarına ve yalnız belirli söz kalıplarında görülen övgü, yergi ve çiftleşme isteği kullanımlarına uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sıvı veya ürün, kendi doğal kaynağından bolca çıkar ya da akar."},{"facet_id":"F002","role":"specialization","statement":"Süt verme ve bulutun bol yağmur bırakması, çekirdeğin başlıca somut gerçekleşmeleridir."},{"facet_id":"F003","role":"extension","statement":"Vergi gelirinin çoğalması ve pazarın canlanması, bol ürün verme düşüncesinin soyut uzantılarıdır."},{"facet_id":"F004","role":"associated_use","statement":"Övgü ve yergi sözleri ile dişi keçinin erkeği istemesi yalnız kendi kalıplarında geçerli bağlantılı kullanımlardır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Sıradan ve az miktarlı her türlü akışla kolayca karışır.","fit":"narrowing","loses":"Bolluk, ürün verme ve soyut üretkenlik uzantılarını belirtmez.","preserves":"Bir sıvının kaynağından dışarı çıkması yönünü korur."},"text":"akmak"},{"category":"confusable","error_profile":{"adds":"Genel uğur, refah ve manevi iyilik gibi kaynakta bulunmayan geniş anlamlar ekler.","collision":"Akışla ilgisi olmayan genel bolluk anlatımlarıyla karışır.","fit":"broadening","loses":"Bir kaynaktan dışarı çıkma işlemini ve somut sıvı akışını siler.","preserves":"Bolluk ve verimlilik çağrışımını kısmen korur."},"text":"bereket"}],"identity_rationale":"Kaynak ifadesi sütün memeden, yağmurun buluttan ve başka sıvıların kendi kaynağından bolca çıkmasını ortak çekirdek olarak destekler. Bunun yanında gelir ve pazar bolluğu, övgü-yergi kalıpları ve dişi keçinin erkeği istemesi gibi kullanımlar da vardır; bunlar doğrudan sıvı akışıymış gibi genellenmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"sütün memeden çıkıp akması"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"süt"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bol sütlü dişi deve"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bulutun yağmur boşaltması"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bol yağmur getiren"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"gözünden yaş akması"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"damarların kanla dolması"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"Ne güzel iş ve iyilik!"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"İyiliği artmasın!"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"vergi gelirinin artması"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"pazarın canlanması"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"dişi keçilerin teke istemesi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"sütün bolluğu veya akışı"}],"lexicalization_note":"Çıplak akış çekirdeği ile süt, yağmur ve gözyaşı kullanımları; övgü, yergi, pazar ve gelir kalıplarından ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sıvı çıkışı, süt verimi ve bollukla gerçek sınır paylaşan üçü seçildi. Aynı kökün öteki kolları eşsesli, kalan adaylar ise yalnız akış alanını paylaşan daha uzak örneklerdir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol kaynağın bol ve verimli biçimde ürün vermesine odaklanırken komşu, miktar sürekliliğinden bağımsız olarak sıvının güçlü ya da tek hamlelik çıkışını anlatır.","focus_only":"Üretici bir kaynaktan sürme ve süreklilik ya da bolluk odağı vardır.","gloss":"bir hamlede fışkırıp dökülme","neighbor_only":"Sıvının bir hamlede ileri atılması veya dökülmesi öne çıkar.","neighbor_ref":"root_000481/B001","relation_type":"near_synonym","shared_zone":"Her ikisi de sıvının belirgin biçimde dışarı çıkmasını anlatır."},{"boundary_match":"partial","distinction":"Komşu yalnız süt alanında yoğunlaşır; bu kol ise sütü daha genel bir kaynaktan bol çıkış çekirdeğinin somut örneklerinden biri olarak içerir.","focus_only":"Yağmur, gözyaşı, gelir ve pazar gibi süt dışındaki alanlara da uzanır.","gloss":"sütün sürekli gelmesi","neighbor_only":"Sütü ve sütün art arda gelmesini kendi başına adlandırır.","neighbor_ref":"root_000563/B006","relation_type":"near_synonym","shared_zone":"İki kol da sütün bol veya ardışık biçimde gelmesini kapsar."},{"boundary_match":"partial","distinction":"Bu kolun belirleyici öğesi kaynaktan çıkış ya da ürün vermedir; komşuda ise çokluk ve genişlik, böyle bir çıkış işlemi bulunmadan da yeterlidir.","focus_only":"Bolluğu, bir kaynağın dışarı ürün vermesi veya akıtması üzerinden kurar.","gloss":"su ve geçim bolluğu","neighbor_only":"Su miktarı, yağış ve geçim genişliğini çıkış işlemi olmadan da anlatır.","neighbor_ref":"root_001075/B001","relation_type":"near_neighbor","shared_zone":"Yağmur, su ve maddi bolluk alanlarında kesişirler."}],"source_phrase_ar":"الدر در اللبن (maqayis;jamhara;sihah;tahdhib;mufradat)؛ در السحاب بالمطر ودرت السماء وسحابة مدرار (maqayis;jamhara;sihah;tahdhib;mufradat)؛ لله دره ولا در دره أي خيره أو عمله (maqayis;jamhara;sihah;tahdhib;mufradat)؛ در الخراج وحلوبة المسلمين وللسوق درة (maqayis;jamhara;sihah;tahdhib;mufradat)؛ استدرت المعزى إذا أرادت الفحل (maqayis;sihah;tahdhib;mufradat)","source_summary":"Birleşik tanıklık, süt ve yağmur başta olmak üzere kaynaktan bol çıkışı; buradan gelişen gelir, pazar, övgü-yergi ve çiftleşme isteği kullanımlarıyla birlikte verir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه در اللبن من الضرع، والمطر من السماء والسحاب، والدمع والدم في العروق، وفيء المسلمين وخراجهم، ونفاق السوق، وصيغ المدح والذم في الخير والعمل، واستدرار المعزى للفحل لما يفضي إلى الدر","what_is_not_ar":"لا يدخل فيه العدو السريع، ولا اللؤلؤ والكوكب الدرّي، ولا الدردر ومغارز الأسنان، ولا الدرة أداة الضرب"},"support_links":["sup_37b84b512f92b308db68"]},{"boundary":"Anlam, özellikle at ve binek hayvanının hızlı koşusudur; her türlü hızlı hareketi kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000469/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَدْرَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>adoraY`|ROOT:dry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"101:10:2:1","qac_word_ref":"101:10:2","surface_ar":"أَدْرَىٰ"}],"gloss":"hızlı, güçlü ve akıcı koşma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Binek hayvanı güçlü, hızlı ve akıcı bir koşu gerçekleştirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Koşmayı sağlayan bacak gücü, belirli bir söz kalıbında ayrıca vurgulanır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Atın tırıs benzeri yürüyüşünde ön ayağını kaldırıp indirmesi, koşu alanına bağlı özel bir kullanımdır."}}],"root_ar":"د ر ي","root_id":"root_000469","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"At veya başka bir binek hayvanının koşusunu bütün temel nitelikleriyle karşılayan genel anlatımdır.","boundary_detail":"Anlam, özellikle at ve binek hayvanının hızlı koşusudur; her türlü hızlı hareketi kapsamaz.","branch_image_ar":"عدو سريع متتابع","concept_gloss":"hızlı, güçlü ve akıcı koşma","contextual_glosses":[{"applicability":"Atın şiddetli fakat akıcı koşusunun anlatıldığı cümlelerde doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başka binek hayvanlarını ve özel ayak hareketi kullanımını dışarıda bırakır.","preserves":"At koşusundaki hız ve rahatlık özelliklerini korur."},"facet_ids":["F001"],"text":"hızlı ve rahatça koşmak","usage_role":"contextual"},{"applicability":"Bacağın koşma gücünü öne çıkaran kalıplaşmış kullanımın açıklamasıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Akıcı koşu olayını ve atın özel ayak hareketini karşılamaz.","preserves":"Koşu gücü ve hız yeteneği yönünü korur."},"facet_ids":["F002"],"text":"koşuda güçlü olmak","usage_role":"explanatory"}],"definition":"Atın veya başka bir binek hayvanının güçlü, hızlı ve akıcı biçimde koşmasıdır. Bazı kullanımlar koşma gücünü, bazılarıysa atın belirli yürüyüşünde ön ayağını kaldırıp indirmesini özellikle belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Binek hayvanı güçlü, hızlı ve akıcı bir koşu gerçekleştirir."},{"facet_id":"F002","role":"specialization","statement":"Koşmayı sağlayan bacak gücü, belirli bir söz kalıbında ayrıca vurgulanır."},{"facet_id":"F003","role":"associated_use","statement":"Atın tırıs benzeri yürüyüşünde ön ayağını kaldırıp indirmesi, koşu alanına bağlı özel bir kullanımdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Koşu dışındaki bütün hareket ve süreçlerin hız kazanmasını kapsar.","collision":"Genel hız değişimiyle özel koşu biçimini birbirine karıştırır.","fit":"broadening","loses":"Hayvan koşusu, güç ve akıcılık bileşenlerini belirtmez.","preserves":"Hızın artması yönünü sınırlı ölçüde korur."},"text":"hızlanmak"},{"category":"alternative","error_profile":{"adds":null,"collision":"Sıradan insan koşusu ve düşük hızlı koşuyla kolayca karışır.","fit":"narrowing","loses":"Şiddet, üstün hız, akıcılık ve binek hayvanı sınırını siler.","preserves":"Ayaklarla hızlı ilerleme olayını temel düzeyde korur."},"text":"koşmak"}],"identity_rationale":"Kaynak ifadesi at veya başka bir binek hayvanının şiddetli, hızlı ve aynı zamanda rahat koşmasını açıkça destekler. Atın belirli yürüyüşünde ön ayağı kaldırıp indirmesi de tanıklanır; bu nedenle kol genel hız değil, hayvan koşusu ve ona bağlı yürüyüş biçimiyle sınırlandırılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"çok hızlı koşan binek hayvanı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"atın hızlı ve rahat koşması"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bacakta güçlü koşma yetisi"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"atın tırıs sırasında ön ayağını kaldırıp indirdiği yürüyüş biçimi"}],"lexicalization_note":"Hızlı ve akıcı hayvan koşusu çekirdeği korunur; bacak gücü ve atın özel ayak hareketi yalnız kendi bağlamlarında geçerlidir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hızlı binek koşusunun hız, yürüyüş biçimi, rahatlık ve toynak etkisi sınırlarını gösteren dört aday seçildi. Öteki adaylar ya yalnız genel hız alanındadır ya da aynı kökün ayrı anlamlarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol hayvanın koşusuna ve koşunun gücüne bağlıdır; komşu ise hafiflik ve geçiş hızını öne çıkararak hareket türü bakımından daha geniştir.","focus_only":"Özellikle at veya binek hayvanında güçlü ve akıcı koşuyu belirtir.","gloss":"hafif ve hızlı ilerleme","neighbor_only":"Hafif geçiş ve hızlı ilerleme, daha geniş hareket türleri için kullanılabilir.","neighbor_ref":"root_001443/B007","relation_type":"near_synonym","shared_zone":"Her ikisi de hızlı ve kolay görünen ilerlemeyi anlatır."},{"boundary_match":"partial","distinction":"Komşu belirli bir yürüyüş türünü ve ettirgen kullanımı içerir; bu kol ise daha çok hayvanın hızlı, güçlü ve rahat koşma niteliğini anlatır.","focus_only":"Hayvanın hızlı koşma niteliği ve akıcı koşusu başlı başına öne çıkar.","gloss":"bineğin hızlı yürüyüşü","neighbor_only":"Belirli bir binek yürüyüşünü ve binicinin hayvanı bu yürüyüşe sevk etmesini de kapsar.","neighbor_ref":"root_001628/B001","relation_type":"near_synonym","shared_zone":"At ve deve gibi bineklerin hızlı ilerleyişinde kesişirler."},{"boundary_match":"partial","distinction":"Bu kol hız ve güç bakımından belirgindir; komşuda belirleyici öğe atın bırakılmış, yumuşak ve geniş koşmasıdır, koşunun ne kadar hızlı olduğu ikincildir.","focus_only":"Yüksek hız ve koşu gücü kurucu özelliklerdir.","gloss":"salınmış geniş koşu","neighbor_only":"Dizginsiz bırakılmış, geniş ve yumuşak koşu biçimi öne çıkar; hız derecesi tartışmalıdır.","neighbor_ref":"root_000553/B005","relation_type":"near_synonym","shared_zone":"İki kol da atın rahat ve geniş adımlı koşusunda yaklaşır."},{"boundary_match":"partial","distinction":"Bu kol koşunun hız ve akıcılık niteliğine odaklanır; komşu ise koşu sırasında toynakların yerde oluşturduğu güçlü kazıma etkisini öne çıkarır.","focus_only":"Koşunun hızı, şiddeti ve rahat akışı anlatılır.","gloss":"toprağı kazan güçlü at koşusu","neighbor_only":"Atın toynağıyla toprağı güçlü biçimde eşelemesi veya kazması vurgulanır.","neighbor_ref":"root_001599/B005","relation_type":"near_neighbor","shared_zone":"Her ikisi de güçlü at koşusunu konu edinir."}],"source_phrase_ar":"الدرير من الدواب الشديد العدو السريعة (maqayis)؛ در الفرس دريرا إذا عدا عدوا شديدا سهلا (jamhara)؛ فرس درير أي سريع (sihah)؛ در الفرس درة فهو درير إذا أسرع في عدوه والإدرار في الخيل (tahdhib)","source_summary":"Birleşik tanıklık, hızlı ve rahat hayvan koşusunu; koşma gücü ve atın belirli ayak hareketiyle ilgili daha dar kullanımlarla birlikte verir.","sources":["MQ","JA","SI","TA"],"what_is_ar":"يدخل فيه الفرس أو الدابة الدريرة السريعة، ودرة الساق في الجري، وإدرار الخيل في هيئة رفع اليد في الخبب","what_is_not_ar":"لا يدخل فيه الدرور بمعنى اللبن والمطر، ولا دوران المغزل، ولا الدرة أداة الضرب"},"support_links":[]},{"boundary":"Sallanma ve tekrarlı hareket çekirdektir; diş yuvası gibi beden adları ile amaçsız gidip gelme ayrı uzantılardır.","branch_kind":"bare","branch_ref":"root_000469/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَدْرَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>adoraY`|ROOT:dry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"101:10:2:1","qac_word_ref":"101:10:2","surface_ar":"أَدْرَىٰ"}],"gloss":"gevşekçe sallanma veya tekrar tekrar gidip gelme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gevşek bir parça sallanır, oynar veya tekrar tekrar gidip gelir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Diş yuvaları ve kimi aktarımda dil ucu, hareket imgesiyle bağlantılı beden adlarıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çocuğun bir şeyi ağzında çevirip çiğnemesi, hareket çekirdeğinin ağız içindeki özel gerçekleşmesidir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Dişlerin dökülmesiyle yuvaların görünmesi, beden adı kullanımına bağlı bir durumdur."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Bir kimsenin gereksiz yere gidip gelmesi, tekrarlı hareketin davranış alanındaki uzantısıdır."}}],"root_ar":"د ر ي","root_id":"root_000469","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kolun hareket çekirdeğini karşılar; beden adı olan kullanımlar için ayrıca açıklama gerekir.","boundary_detail":"Sallanma ve tekrarlı hareket çekirdektir; diş yuvası gibi beden adları ile amaçsız gidip gelme ayrı uzantılardır.","branch_image_ar":"تدردر واضطراب في اللحم والفم","concept_gloss":"gevşekçe sallanma veya tekrar tekrar gidip gelme","contextual_glosses":[{"applicability":"Gevşek et veya başka bir parçanın hareketini anlatan bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ağız içi beden adlarını ve amaçsız dolaşma uzantısını dışarıda bırakır.","preserves":"Gevşek parçanın kararsız ve tekrarlı hareketini korur."},"facet_ids":["F001"],"text":"sallanıp oynamak","usage_role":"contextual"},{"applicability":"Çocuğun bir yiyeceği ağzında evirip çiğnediği bağlam için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Etin sallanmasını, beden adlarını ve amaçsız gidip gelmeyi karşılamaz.","preserves":"Ağız içindeki tekrarlı hareket ve çiğneme eylemini korur."},"facet_ids":["F003"],"text":"ağzında çevirip çiğnemek","usage_role":"contextual"},{"applicability":"Bir kimsenin amacı olmadan tekrar tekrar bir yerlere gidişini anlatır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ağız ve gevşek et çevresindeki somut kullanımları dışarıda bırakır.","preserves":"Tekrarlı hareket ve amaçsızlık uzantısını korur."},"facet_ids":["F005"],"text":"boş yere gidip gelmek","usage_role":"contextual"}],"definition":"Temel hareket imgesi, gevşek bir parçanın sallanıp oynaması veya bir şeyin tekrar tekrar gidip gelmesidir. Ağız alanında bu imge diş yuvalarının adı, çocuğun bir şeyi ağzında çevirip çiğnemesi ve dişler düşünce yuvaların görünmesi gibi özel kullanımlara uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gevşek bir parça sallanır, oynar veya tekrar tekrar gidip gelir."},{"facet_id":"F002","role":"source_variant","statement":"Diş yuvaları ve kimi aktarımda dil ucu, hareket imgesiyle bağlantılı beden adlarıdır."},{"facet_id":"F003","role":"specialization","statement":"Çocuğun bir şeyi ağzında çevirip çiğnemesi, hareket çekirdeğinin ağız içindeki özel gerçekleşmesidir."},{"facet_id":"F004","role":"associated_use","statement":"Dişlerin dökülmesiyle yuvaların görünmesi, beden adı kullanımına bağlı bir durumdur."},{"facet_id":"F005","role":"extension","statement":"Bir kimsenin gereksiz yere gidip gelmesi, tekrarlı hareketin davranış alanındaki uzantısıdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Soğuk, korku veya hastalık kaynaklı istemsiz hareket çağrışımı ekler.","collision":"Korku ve hastalıkla oluşan beden titremesiyle karışır.","fit":"narrowing","loses":"Gevşekçe sallanmayı, ağız kullanımlarını ve amaçsız gidip gelmeyi siler.","preserves":"Küçük ve tekrarlı hareket düşüncesini kısmen korur."},"text":"titremek"},{"category":"confusable","error_profile":{"adds":"Kaynakta adlandırılan yuvanın yerine komşu bir dokuyu koyar.","collision":"Diş yuvası ile dişi çevreleyen yumuşak doku birbirine karışır.","fit":"displacement","loses":"Diş yuvasını, hareket çekirdeğini ve öteki kullanımları karşılamaz.","preserves":"Diş çevresindeki bir beden bölgesine gönderme yapar."},"text":"diş eti"}],"identity_rationale":"Kaynak ifadesi gevşek etin sallanmasını ve çocuğun bir şeyi ağzında çevirip çiğnemesini hareket çekirdeğiyle birleştirir; diş yuvaları, dil ucu, dişsizlik ve gereksiz gidip gelme kullanımlarını da aynı kol içinde verir. Geçici çerçeve ağız ve et alanını iyi yakalar, ancak gereksiz gidip gelme uzantısını ve durağan beden adlarını ayrıca belirtmek gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"diş yuvaları; kimi kullanımda dil ucu"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"çocuğun bir şeyi ağzında çevirip çiğnemesi"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"sallanıp oynamak"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"dişleri dökülüp diş yuvaları görünmek"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"gereksiz yere gidip gelen kimse"}],"lexicalization_note":"Kol çıplak biçimde tanıklanır; tanım hem hareket çekirdeğini hem de kaynakta verilen beden adı ve amaçsız dolaşma uzantılarını sınırlarıyla korur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; gevşek et, ağız anatomisi ve tekrarlı sarsılma sınırlarını en açık gösteren üçü seçildi. Kalanlar yalnız beden alanını paylaşır veya aynı kökün bağımsız anlam kollarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu gevşek etin kendisine ve onun oynaklığına odaklanır; bu kol aynı hareket imgesini ağız içi adlara, çiğnemeye ve davranışsal gidip gelmeye de taşır.","focus_only":"Diş yuvaları, ağızda çiğneme ve amaçsız gidip gelme kullanımlarını da kapsar.","gloss":"gevşek ve oynak et","neighbor_only":"Özellikle karın çevresindeki gevşek veya genel olarak oynak et parçasını adlandırır.","neighbor_ref":"root_000940/B008","relation_type":"near_synonym","shared_zone":"Gevşek etin sallanıp oynaması iki kolun doğrudan kesişimidir."},{"boundary_match":"field_only","distinction":"Bu kolun beden adı dişin oturduğu yuvadır ve hareket kullanımlarıyla bağlantılıdır; komşu ise dişler arasını dolduran doku ya da kemiği adlandırır.","focus_only":"Diş yuvasını ve sallanma ya da tekrarlı ağız hareketini içerir.","gloss":"dişler arasındaki et veya kemik","neighbor_only":"Dişler arasını dolduran et veya kemik ile dil kökü altındaki yapıları adlandırır.","neighbor_ref":"root_001044/B009","relation_type":"same_field","shared_zone":"İki kol da dişler ve ağız içindeki anatomik yapılara ilişkindir."},{"boundary_match":"partial","distinction":"Bu kol sallanan parça ve tekrar eden hareket biçimini adlandırır; komşu hareketin korku, hastalık ya da güçsüzlük gibi nedenlerini belirginleştirir.","focus_only":"Gevşek parça hareketi, ağız kullanımları ve amaçsız gidip gelme birlikte bulunur.","gloss":"ürperme ve sarsılma","neighbor_only":"Korku, hastalık, gevşeklik veya güçsüzlükten doğan ürperme ve sarsılma öne çıkar.","neighbor_ref":"root_000573/B001","relation_type":"near_neighbor","shared_zone":"Her ikisi de kararsız ve tekrarlı hareket görünümünü paylaşır."}],"source_phrase_ar":"الدردر منابت أسنان الصبي ومن تدردرت اللحمة إذا اضطربت ودردر الصبي الشيء إذا لاكه (maqayis)؛ الدردر مغارز أسنان الصبي ودردر الصبي البسرة لاكها (sihah)؛ تدردر أي تمرمر وترجرج والدردر مغرز السن وطرف اللسان والدردرى الذي يذهب ويجيء في غير حاجة (tahdhib)","source_summary":"Birleşik tanıklık; sallanan et, diş yuvaları, ağızda çevirip çiğneme, dişsizlik ve gereksiz gidip gelme kullanımlarını hareket ve ağız alanları çevresinde toplar.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه الدردر مغارز الأسنان أو منابت أسنان الصبي، وتدردر اللحم أو البضعة إذا اضطربت وترجرجت، ودردرة الصبي الشيء إذا لاكه، والدردري الذي يذهب ويجيء في غير حاجة","what_is_not_ar":"لا يدخل فيه الدرة اللؤلؤة، ولا الدرة أداة الضرب، ولا درور اللبن والمطر"},"support_links":[]},{"boundary":"Kol, yön doğrultusu ile karşı karşıya hizalanmayı kapsar; yolun kendisi veya rüzgâr türü değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000469/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَدْرَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>adoraY`|ROOT:dry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"101:10:2:1","qac_word_ref":"101:10:2","surface_ar":"أَدْرَىٰ"}],"gloss":"doğrultu, yön veya karşı karşıya hizalanma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin uzandığı, izlendiği veya yöneldiği hat ve doğrultu belirtilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yolun güzergâhı ve rüzgârın esiş yönü, doğrultu çekirdeğinin iki somut uygulamasıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İki kişi veya yerin karşı karşıya ve aynı hizada oluşu, doğrultunun uzamsal uzantısıdır."}}],"root_ar":"د ر ي","root_id":"root_000469","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yol, rüzgâr ve uzamsal karşılıklılık kullanımlarını birlikte kapsayan genel karşılıktır.","boundary_detail":"Kol, yön doğrultusu ile karşı karşıya hizalanmayı kapsar; yolun kendisi veya rüzgâr türü değildir.","branch_image_ar":"سمت الطريق ومهب الريح والمحاذاة","concept_gloss":"doğrultu, yön veya karşı karşıya hizalanma","contextual_glosses":[{"applicability":"Bir yolun izlediği hat veya güzergâhın anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Rüzgâr yönünü ve karşı karşıya hizalanma kullanımını dışarıda bırakır.","preserves":"İzlenen hat ve yön doğrultusu bileşenini korur."},"facet_ids":["F001","F002"],"text":"yolun doğrultusu","usage_role":"contextual"},{"applicability":"Rüzgârın geldiği veya ilerlediği yönün belirtildiği bağlamlara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yol ve karşılıklı hizalanma kullanımlarını karşılamaz.","preserves":"Doğrultu çekirdeğinin rüzgâr alanındaki uygulamasını korur."},"facet_ids":["F001","F002"],"text":"rüzgârın esiş yönü","usage_role":"contextual"},{"applicability":"İki kişi, ev veya yerin birbirine bakacak biçimde hizalandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yolun hattı ile rüzgârın esiş yönünü dışarıda bırakır.","preserves":"Karşılıklılık ve aynı doğrultuda bulunma özelliğini korur."},"facet_ids":["F003"],"text":"tam karşısında olmak","usage_role":"contextual"}],"definition":"Bir yolun izlediği doğrultu, rüzgârın geldiği veya estiği yön ya da iki yerin veya kişinin birbirinin tam karşısında ve aynı hizada bulunmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin uzandığı, izlendiği veya yöneldiği hat ve doğrultu belirtilir."},{"facet_id":"F002","role":"specialization","statement":"Yolun güzergâhı ve rüzgârın esiş yönü, doğrultu çekirdeğinin iki somut uygulamasıdır."},{"facet_id":"F003","role":"extension","statement":"İki kişi veya yerin karşı karşıya ve aynı hizada oluşu, doğrultunun uzamsal uzantısıdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Fiziksel yolun kendisiyle yolun izlediği doğrultu birbirine karışır.","fit":"narrowing","loses":"Yolun doğrultusunu, rüzgâr yönünü ve karşılıklı hizalanmayı belirtmez.","preserves":"Güzergâh alanıyla olan bağlantıyı kısmen korur."},"text":"yol"},{"category":"confusable","error_profile":{"adds":"Muhalefet, savunma ve değiş tokuş gibi uzamsal olmayan anlamlar ekler.","collision":"Uzamsal hizalanma ile karşıtlık ilişkisi kolayca karışır.","fit":"broadening","loses":"Yol ve rüzgâr doğrultusu bileşenlerini karşılamaz.","preserves":"Bir şeyin öbürünün önünde bulunması yönünü korur."},"text":"karşı"}],"identity_rationale":"Kaynak ifadesi yolun doğrultusunu veya izlenen hattını, rüzgârın esiş yönünü ve iki şeyin karşı karşıya ya da aynı hizada bulunmasını birlikte verir. Hazırlanan çerçeve bu ortak yön ve hizalanma alanını doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"yolun doğrultusu veya güzergâhı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"rüzgârın esiş yönü"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"tam karşında veya hizanda"}],"lexicalization_note":"Yol ve rüzgâr yönü çıplak anlam alanını gösterir; bir kişinin tam karşıda oluşu yalnız tanıklanan kalıp içinde korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; karşılıklılık, yol hattı ve görünür hizalanma sınırlarını gösteren üç yakın aday seçildi. Ötekiler belirli bir yol veya rüzgâr türünü adlandırır ya da aynı kökün ayrı anlamlarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu karşılıklı konuma odaklanır; bu kol karşılıklılığı içerirken aynı zamanda yolun izlediği hattı ve rüzgâr yönünü de adlandırır.","focus_only":"Yolun doğrultusunu ve rüzgârın esiş yönünü de kapsar.","gloss":"karşıda ve aynı hizada olma","neighbor_only":"Evlerin karşılıklı oluşunu ve buna benzer yüz yüze konumları merkez alır.","neighbor_ref":"root_001450/B010","relation_type":"near_synonym","shared_zone":"İki şeyin birbirinin tam karşısında bulunmasında örtüşürler."},{"boundary_match":"partial","distinction":"Bu kol yön ve doğrultu ilişkisini kurar; komşu ise bu ilişkiye ek olarak yolun kendisini, kavşağı ve son noktayı adlandıran yer anlamlarına sahiptir.","focus_only":"Rüzgâr yönü ve soyut doğrultu ilişkisi açıkça bulunur.","gloss":"yol, kavşak ve hizalanma","neighbor_only":"İşlek yol, yol kavşağı ve varılan son nokta gibi yer adlarını da kapsar.","neighbor_ref":"root_000009/B010","relation_type":"near_synonym","shared_zone":"Yol hattı ve evlerin birbirine göre hizası alanlarında kesişirler."},{"boundary_match":"partial","distinction":"Bu kol için aynı doğrultuda karşıda bulunmak yeterlidir; komşuda karşılıklı görünürlük ve yüz yüze gelme daha belirgin bir koşuldur.","focus_only":"Karşılıklı görüş gerektirmeyen yol ve rüzgâr doğrultularını da kapsar.","gloss":"birbirini görecek biçimde karşılaşma","neighbor_only":"Karşı duran öğelerin birbirini görebilmesi veya yerleşimlerin karşılıklı görünmesi öne çıkar.","neighbor_ref":"root_001520/B003","relation_type":"near_synonym","shared_zone":"Yerlerin ve nesnelerin karşı karşıya hizalanmasında örtüşürler."}],"source_phrase_ar":"درر الريح مهبها ودرر الطريق قصده (maqayis)؛ هما على درر واحد ونحن على درر الطريق ودرر الريح مهبها (sihah)؛ فلان دررك أي قبالتك وعلى درر الطريق أي مدرجته وداري بدرر دارك أي بحذائها (tahdhib)","source_summary":"Birleşik tanıklık, yolun doğrultusu ile rüzgârın esiş yönünü ve kişi ya da evlerin karşı karşıya hizalanmasını tek bir yön ilişkisi altında toplar.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه درر الطريق بمعنى قصده أو مدرجته، ودرر الريح مهبها، والمحاذاة أو المقابلة كقولهم فلان دررك وداري بدرر دارك","what_is_not_ar":"لا يدخل فيه الجريان الغزير من اللبن أو المطر، ولا العدو السريع"},"support_links":[]},{"boundary":"Çekirdek inci veya iri incidir; beyaz ve güçlü ışıklı yıldız yalnız inci benzetmesine dayanan özel bir uzantıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000469/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَدْرَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>adoraY`|ROOT:dry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"101:10:2:1","qac_word_ref":"101:10:2","surface_ar":"أَدْرَىٰ"}],"gloss":"iri inci; inci gibi beyaz ve parlak yıldız","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne olarak inci veya inciler adlandırılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İncinin iri oluşu, kaynak tanıklığında öne çıkan özel bir niteliktir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Beyaz ve güçlü ışıklı yıldız, inciye benzetilerek kurulan özel bir adlandırmadır."}}],"root_ar":"د ر ي","root_id":"root_000469","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnci çekirdeğini ve yalnız yıldız anlatımında geçerli benzetmeli uzantıyı birlikte gösterir.","boundary_detail":"Çekirdek inci veya iri incidir; beyaz ve güçlü ışıklı yıldız yalnız inci benzetmesine dayanan özel bir uzantıdır.","branch_image_ar":"بياض الدر وصفاؤه ولمعانه","concept_gloss":"iri inci; inci gibi beyaz ve parlak yıldız","contextual_glosses":[{"applicability":"İncinin kendisinin veya iri incilerin adlandırıldığı nesne bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnciye benzetilen parlak yıldız kullanımını dışarıda bırakır.","preserves":"İnci nesnesini ve kaynakta öne çıkan irilik niteliğini korur."},"facet_ids":["F001","F002"],"text":"iri inci","usage_role":"general"},{"applicability":"Beyazlığı ve güçlü ışığı bakımından inciye benzetilen yıldız için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İncinin nesne olarak temel adlandırmasını karşılamaz.","preserves":"Yıldızın inciye dayanan beyazlık ve parlaklık benzetmesini korur."},"facet_ids":["F003"],"text":"inci gibi parlayan yıldız","usage_role":"contextual"}],"definition":"İnciyi, özellikle iri ve değerli inciyi adlandırır. Belirli bir yıldız anlatımında, beyazlığı ve güçlü ışığı nedeniyle inciye benzetilen parlak yıldızı niteler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne olarak inci veya inciler adlandırılır."},{"facet_id":"F002","role":"specialization","statement":"İncinin iri oluşu, kaynak tanıklığında öne çıkan özel bir niteliktir."},{"facet_id":"F003","role":"extension","statement":"Beyaz ve güçlü ışıklı yıldız, inciye benzetilerek kurulan özel bir adlandırmadır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Her türlü yüzey veya ışık kaynağının parlaklığını kapsayan genel bir nitelik ekler.","collision":"Nesne adı ile nesnenin yalnız bir görünüş özelliği birbirine karışır.","fit":"displacement","loses":"Temel inci nesnesini ve incinin iriliğini bütünüyle siler.","preserves":"Yıldız uzantısındaki ışık niteliğini kısmen korur."},"text":"parlaklık"},{"category":"confusable","error_profile":{"adds":"İnciyle ilgisi olmayan bütün beyaz nesne ve yüzeyleri kapsar.","collision":"İnci adlandırması genel renk niteliğine indirgenir.","fit":"displacement","loses":"İnciyi, iriliği ve yıldızın güçlü ışığını karşılamaz.","preserves":"İnci ve yıldız arasında kurulan renk benzerliğini korur."},"text":"beyazlık"}],"identity_rationale":"Kaynak ifadesinin temel adlandırması beyazlık veya parlaklık niteliği değil, büyük inciler ya da tek bir incidir. Parlak ve ışığı güçlü yıldız kullanımı, yıldızın beyazlığı ve ışığı bakımından inciye benzetilmesine dayanır; bu yüzden nitelik, nesne çekirdeğinin yerine geçirilmeden uzantı olarak kurulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"iri inciler veya inci topluluğu"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"iri inci; tek bir inci"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"inci gibi beyaz ve parlak yıldız"}],"lexicalization_note":"İnci adı çıplak çekirdektir; parlak yıldız anlamı yalnız tanıklanan yıldız tamlaması içinde, inci benzetmesine bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; nesne ile parlaklık niteliğini, genel beyazlığı ve ateş benzetmeli ışıldamayı ayıran üç aday seçildi. Kalanlar yalnız aydınlık görünüşü paylaşır veya aynı kökün bağımsız anlamlarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol öncelikle bir nesne adıdır ve yıldız uzantısını o nesneye benzeterek kurar; komşu ise mücevherin ışıldama olayını nesneden bağımsız bir nitelik olarak anlatır.","focus_only":"İnci nesnesini ve inciye benzetilen parlak yıldızı adlandırır.","gloss":"mücevherin ışıldaması","neighbor_only":"Bir mücevherin ışıldama ve parıltı çıkarma niteliğini anlatır.","neighbor_ref":"root_001686/B002","relation_type":"near_neighbor","shared_zone":"İnci ve başka değerli taşların parlak görünüşünde kesişirler."},{"boundary_match":"partial","distinction":"Bu kol nesne kimliğine bağlıdır; komşuysa çok farklı varlıklara uygulanabilen genel bir parlak beyazlık ve güzel renk niteliğidir.","focus_only":"İri inciyi ve inciye benzetilen yıldızı belirli nesneler olarak adlandırır.","gloss":"parlak beyaz ve güzel renk","neighbor_only":"İnsan, hayvan, bitki, bulut ve başka varlıklardaki parlak beyaz rengi genel olarak niteler.","neighbor_ref":"root_000650/B002","relation_type":"near_neighbor","shared_zone":"Beyazlık ve aydınlık görünüş, inci betimlemesinde ortak alandır."},{"boundary_match":"partial","distinction":"Bu kolun parlaklık yönü inciye özgü beyazlık ve yıldız benzetmesiyle sınırlıdır; komşu ateş imgesinden gelişen genel ışıldamayı anlatır.","focus_only":"Parlaklık inci nesnesinden ve yıldızın inciye benzetilmesinden doğar.","gloss":"ateş gibi ışıldama","neighbor_only":"Parlama, ateşin tutuşmasına benzetilen genel bir ışıldama olayıdır.","neighbor_ref":"root_001672/B006","relation_type":"near_neighbor","shared_zone":"Mücevher ve benzeri nesnelerin belirgin ışık saçmasında kesişirler."}],"source_phrase_ar":"الدر كبار اللؤلؤ والكوكب الدري الثاقب المضيء (maqayis)؛ الدرة ما عظم من اللؤلؤ (jamhara)؛ الدرة اللؤلؤة والكوكب الدري الثاقب المضيء نسب إلى الدر لبياضه (sihah)؛ الدر العظام من اللؤلؤ والكوكب الدري الثاقب المضيء (tahdhib)","source_summary":"Birleşik tanıklık iri inciyi ve tek inciyi temel adlandırma olarak verir; beyaz ve güçlü ışıklı yıldız kullanımını da inci benzetmesiyle açıklar.","sources":["MQ","JA","SI","TA"],"what_is_ar":"يدخل فيه الدر بمعنى كبار اللؤلؤ أو اللؤلؤة، والكوكب الدري المنسوب إلى الدر في صفائه وبياضه وثقوبه وإضاءته","what_is_not_ar":"لا يدخل فيه در اللبن والمطر، ولا الدرة أداة الضرب، ولا الدردور في الماء"},"support_links":[]},{"boundary":"Kol vurma aracını, özellikle yönetici değneğini adlandırır; vurma eyleminin veya zorbalığın genel adı değildir.","branch_kind":"bare","branch_ref":"root_000469/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَدْرَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>adoraY`|ROOT:dry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"101:10:2:1","qac_word_ref":"101:10:2","surface_ar":"أَدْرَىٰ"}],"gloss":"özellikle yöneticinin kullandığı vurma değneği","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne, birine vurmak için kullanılan değnek türü bir araçtır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aracın yöneticiye ait oluşu, kaynakta özellikle belirtilen kurumsal kullanımdır."}}],"root_ar":"د ر ي","root_id":"root_000469","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Aracın işlevini ve kaynakta öne çıkan yönetici kullanımını birlikte belirten karşılıktır.","boundary_detail":"Kol vurma aracını, özellikle yönetici değneğini adlandırır; vurma eyleminin veya zorbalığın genel adı değildir.","branch_image_ar":"درة الضرب والسلطان","concept_gloss":"özellikle yöneticinin kullandığı vurma değneği","contextual_glosses":[{"applicability":"Bir yöneticinin vurmak için kullandığı araç bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Vurmakta kullanılan değneği ve kaynakta özellikle belirtilen yönetici kullanımını korur."},"facet_ids":["F001","F002"],"text":"yöneticinin vurma değneği","usage_role":"contextual"},{"applicability":"Aracın sahibinden çok vurma işlevinin önemli olduğu genel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kaynakta özellikle belirtilen yönetici kullanımını görünmez kılar.","preserves":"Değnek biçimindeki vurma aracı kimliğini korur."},"facet_ids":["F001"],"text":"vurma değneği","usage_role":"general"}],"definition":"Vurmak için kullanılan, özellikle bir yöneticinin kullandığı değnek türü bir araçtır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne, birine vurmak için kullanılan değnek türü bir araçtır."},{"facet_id":"F002","role":"specialization","statement":"Aracın yöneticiye ait oluşu, kaynakta özellikle belirtilen kurumsal kullanımdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Esnek kayışlardan oluşan belirli bir araç yapısını ekler.","collision":"Sert değnek ile esnek kayışlı kırbaç birbirine karışır.","fit":"narrowing","loses":"Değnek biçimini ve yöneticiye özgü kullanımı zorunlu olarak karşılamaz.","preserves":"İnsan veya hayvana vurmak için kullanılan araç işlevini korur."},"text":"kırbaç"},{"category":"confusable","error_profile":{"adds":"Yönetme yetkisi, saygınlık ve güç gibi soyut anlamlar ekler.","collision":"Yöneticinin aracı ile yöneticinin yetkisi birbirine karışır.","fit":"broadening","loses":"Somut vurma aracını ve değnek biçimini bütünüyle siler.","preserves":"Yöneticiyle kurulan kurumsal bağlantıyı kısmen korur."},"text":"otorite"}],"identity_rationale":"Kaynak ifadesi vurmak için kullanılan bilinen bir aracı ve özellikle yöneticinin bu amaçla kullandığı değneği açıkça adlandırır. Hazırlanan çerçeve, inci veya süt bolluğu anlamlarıyla karıştırmadan bu araç kimliğini doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"özellikle yöneticinin kullandığı vurma değneği"}],"lexicalization_note":"Araç anlamı çıplak biçimde tanıklanır; tanım yalnız vurmakta kullanılan değneği kapsar ve eylem ya da yönetim gücü anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; araç yapısı ile vurma eylemini ayıran üç aday seçildi. Zorlama, zulüm ve yönetici gücü adayları aynı senaryoda yer alsa da bu somut aracın anlam sınırını doğrudan paylaşmaz.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol araç kimliğini değnek ve yönetici kullanımıyla sınırlar; komşu kırbacın özel yapısını ve araçla yapılan vurma eylemini de anlamın içine alır.","focus_only":"Değnek türü araç ve özellikle yöneticinin taşıdığı biçim öne çıkar.","gloss":"kırbaç ve kırbaçla vurma","neighbor_only":"Esnek kayışlı kırbacı, onun yapısını ve onunla vurma eylemini birlikte kapsar.","neighbor_ref":"root_000759/B002","relation_type":"near_synonym","shared_zone":"İki kol da vurmakta kullanılan bir aracı içerir."},{"boundary_match":"field_only","distinction":"Bu kol somut aracın adıdır; komşuysa kırbaç ya da kılıç gibi bir araç kullanılarak darbenin kişiye uygulanması olayını anlatır.","focus_only":"Vurmak için kullanılan belirli bir değnek türünü adlandırır.","gloss":"kırbaç veya kılıçla vurma","neighbor_only":"Bir kişiye kırbaç veya kılıç darbesi indirme eylemini anlatır.","neighbor_ref":"root_001088/B006","relation_type":"same_field","shared_zone":"Vurma aracı ve darbe alanında buluşurlar."},{"boundary_match":"field_only","distinction":"Bu kol bir araç adıdır; komşu ise darbenin deriye uygulanmasını, silahlı çatışmayı veya yere sermeyi eylem olarak kurar.","focus_only":"Vurma eyleminden bağımsız olarak taşınabilen aracı adlandırır.","gloss":"deriye vuran ceza ve silahlı çarpışma","neighbor_only":"Deriye vuran ceza, kılıçla çarpışma ve yere serme gibi eylemleri kapsar.","neighbor_ref":"root_000253/B004","relation_type":"same_field","shared_zone":"Vurma senaryosunda araç ve katılımcı alanını paylaşırlar."}],"source_phrase_ar":"الدرة التي يضرب بها عربية معروفة (jamhara)؛ الدرة التي يضرب بها (sihah)؛ الدرة درة السلطان التي يضرب بها (tahdhib)","source_summary":"Birleşik tanıklık, vurmakta kullanılan bilinen değneği ortak anlam olarak verir ve yöneticinin kullandığı biçimini özellikle öne çıkarır.","sources":["JA","SI","TA"],"what_is_ar":"يدخل فيه الدرة التي يضرب بها، ودرة السلطان","what_is_not_ar":"لا يدخل فيه الدرة بمعنى اللؤلؤة أو كثرة اللبن"},"support_links":[]},{"boundary":"Kol, ip eğirmede iği döndürüp bükümü sağlamlaştırma işlemidir; genel dönme veya her türlü dokuma değildir.","branch_kind":"bare","branch_ref":"root_000469/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَدْرَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>adoraY`|ROOT:dry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"101:10:2:1","qac_word_ref":"101:10:2","surface_ar":"أَدْرَىٰ"}],"gloss":"ipliği sıkı bükmek için iği döndürme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İğ veya onun dönen parçası sürekli çevrilerek döndürülür."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Döndürme işlemi ip eğirme sırasında yapılır ve ipliğin bükümünü sıkılaştırır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İşi yapan kişi ve dönen iğ, işlemi gerçekleştirme veya taşıma özellikleriyle ayrıca nitelenebilir."}}],"root_ar":"د ر ي","root_id":"root_000469","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Döndürme işlemini, eğirme bağlamını ve sağlam büküm amacını birlikte karşılar.","boundary_detail":"Kol, ip eğirmede iği döndürüp bükümü sağlamlaştırma işlemidir; genel dönme veya her türlü dokuma değildir.","branch_image_ar":"إدارة المغزل واستحكام دورانه","concept_gloss":"ipliği sıkı bükmek için iği döndürme","contextual_glosses":[{"applicability":"İplik eğirme işleminin açıkça anlatıldığı cümlelerde kullanılabilecek doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aracı, döndürme işlemini, ipliği ve sıkı büküm sonucunu korur."},"facet_ids":["F001","F002"],"text":"iği çevirip ipliği sıkı bükmek","usage_role":"general"},{"applicability":"Döndürmenin sonucunun ve amacının öne çıktığı açıklayıcı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İğin çevrilmesi işlemini ve eğiren kişinin hareketini açıkça belirtmez.","preserves":"İplik bükümünün sıkı ve sağlam duruma getirilmesini korur."},"facet_ids":["F002"],"text":"bükümü sağlamlaştırmak","usage_role":"explanatory"}],"definition":"İplik eğiren kişinin iği veya iğin dönen parçasını çevirerek ipliğin bükümünü sıkı ve sağlam hâle getirmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İğ veya onun dönen parçası sürekli çevrilerek döndürülür."},{"facet_id":"F002","role":"specialization","statement":"Döndürme işlemi ip eğirme sırasında yapılır ve ipliğin bükümünü sıkılaştırır."},{"facet_id":"F003","role":"associated_use","statement":"İşi yapan kişi ve dönen iğ, işlemi gerçekleştirme veya taşıma özellikleriyle ayrıca nitelenebilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Her türlü nesnenin veya kişinin amaçsız eksen hareketini kapsar.","collision":"Genel dönme ile ip eğirmeye özgü işlem birbirine karışır.","fit":"broadening","loses":"İp eğirme, iğ ve bükümü sıkılaştırma amacını siler.","preserves":"Eksen çevresindeki hareketi temel düzeyde korur."},"text":"dönmek"},{"category":"confusable","error_profile":{"adds":"İplikleri birbirine geçirerek kumaş oluşturma aşamasını ekler.","collision":"İplik eğirme ile kumaş dokuma üretimin farklı aşamalarıdır.","fit":"displacement","loses":"İği döndürme ve tek ipliğin bükümünü sıkılaştırma işlemini karşılamaz.","preserves":"İplik ve kumaş üretimi alanıyla bağlantıyı korur."},"text":"dokumak"}],"identity_rationale":"Kaynak ifadesi kadının iği veya iğin dönen parçasını çevirerek ipliğin bükümünü sıkılaştırmasını açıkça anlatır. Hazırlanan çerçeve hem döndürme işlemini hem de sağlam büküm sonucunu doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"ipliği sıkı bükmek için iği veya dönen parçasını çevirmek"}],"lexicalization_note":"İğ döndürme eylemi çıplak biçimde tanıklanır; tanım işlemi ip eğirme ve bükümü sıkılaştırma amacıyla sınırlar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sıkı ve gevşek büküm karşıtlığını, üretim kalitesini ve genel eksen dönüşünü gösteren üçü seçildi. Kalanlar yalnız araç veya dokuma alanını paylaşır ya da aynı kökün ayrı anlamlarıdır.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Bu kol sıkı ve sağlam büküm oluşturan işlemi anlatırken komşu, aynı eksenin öteki ucundaki gevşek ya da tek kat bükülmüş ipliği adlandırır.","focus_only":"İğin döndürülmesiyle iplik bükümünün sıkılaştırılması hedeflenir.","gloss":"gevşek veya tek kat bükülmüş iplik","neighbor_only":"İpliğin gevşek bükülmüş veya tek kat kalmış durumu adlandırılır.","neighbor_ref":"root_000684/B007","relation_type":"polarity_pair","shared_zone":"İki kol da ipliğin büküm derecesini aynı üretim ekseninde değerlendirir."},{"boundary_match":"partial","distinction":"Bu kol belirli bir döndürme işlemini adlandırır; komşu ise eğirme ve dokumanın sonucundaki kaliteyi, kullanılan hareketten bağımsız olarak daha geniş biçimde niteler.","focus_only":"İğin çevrilmesi biçimindeki belirli hareket ve araç ilişkisi kurucudur.","gloss":"iyi ve sağlam eğirme veya dokuma","neighbor_only":"İplik ve kumaş üretiminin iyi, sağlam ve nitelikli yapılmasını daha geniş biçimde anlatır.","neighbor_ref":"root_000217/B007","relation_type":"near_synonym","shared_zone":"İpliğin sıkı bükülmesi ve sağlam üretilmesi alanında örtüşürler."},{"boundary_match":"partial","distinction":"Bu kol dönüşü ip eğirme işlemi ve sıkı büküm sonucu ile sınırlar; komşu ise eksen çevresindeki mekanik dönüşü farklı araç ve nesnelere uygular.","focus_only":"Dönüş, iğ ve iplik bükümünü sıkılaştırma amacıyla yapılır.","gloss":"eksen çevresinde dönme","neighbor_only":"Bir makara veya benzeri parçanın eksen çevresinde dönmesi ve başka nesnelerin çevrilmesi anlatılır.","neighbor_ref":"root_000369/B007","relation_type":"near_neighbor","shared_zone":"Her ikisi de bir parçanın eksen çevresindeki dönüş hareketini içerir."}],"source_phrase_ar":"أدرت المرأة المغزل إذا فتلته فتلا شديدا فهي مدر والمغزل مدر (jamhara)؛ أدرت الغزالة درارتها إذا أدارتها لتستحكم قوة ما تغزله (tahdhib)","source_summary":"Birleşik tanıklık, iğin veya dönen parçasının çevrilmesini ve bu dönüşle eğrilen ipliğin bükümünün sıkılaştırılmasını birlikte verir.","sources":["JA","TA"],"what_is_ar":"يدخل فيه إدارة المرأة للمغزل أو الدرارة حتى يستحكم الفتل وتثبت الفلكة مع شدة الدوران","what_is_not_ar":"لا يدخل فيه العدو السريع، ولا درور اللبن، ولا الدردور البحري"},"support_links":[]},{"boundary":"Kol, dönen ve kabaran suyun oluşturduğu tehlikeli girdaptır; denizin veya dalganın genel adı değildir.","branch_kind":"bare","branch_ref":"root_000469/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَدْرَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>adoraY`|ROOT:dry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"101:10:2:1","qac_word_ref":"101:10:2","surface_ar":"أَدْرَىٰ"}],"gloss":"gemiyi tehlikeye atan çalkantılı deniz girdabı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Su kendi çevresinde dönerek kabarır ve güçlü biçimde çalkalanır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hareket, denizde belirli ve yerelleşmiş tehlikeli bir su bölgesi oluşturur."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu su hareketi yüzünden boğulma ve geminin kurtulamaması ciddi bir sonuçtur."}}],"root_ar":"د ر ي","root_id":"root_000469","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dönen su hareketini, denizdeki yerini ve boğulma tehlikesini birlikte karşılar.","boundary_detail":"Kol, dönen ve kabaran suyun oluşturduğu tehlikeli girdaptır; denizin veya dalganın genel adı değildir.","branch_image_ar":"دردور الماء واضطراب الدوامة","concept_gloss":"gemiyi tehlikeye atan çalkantılı deniz girdabı","contextual_glosses":[{"applicability":"Dönen suyun gemi ve insanlar için tehlike oluşturduğu deniz bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Girdap hareketini, deniz sınırını ve tehlike özelliğini korur."},"facet_ids":["F001","F002","F003"],"text":"tehlikeli deniz girdabı","usage_role":"general"},{"applicability":"Su hareketinin görünüşünün açıklandığı, yer ve sonucu ikincil kalan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Denizdeki yerleşik bölgeyi ve gemi için doğan ağır tehlikeyi açıkça belirtmez.","preserves":"Suyun dönmesi, kabarması ve çalkalanması özelliklerini korur."},"facet_ids":["F001"],"text":"dönüp kabaran su","usage_role":"explanatory"}],"definition":"Suyun dönüp kabararak güçlü biçimde çalkalandığı girdap veya denizde bu hareketin boğulma ve geminin kurtulamaması tehlikesi doğurduğu yerdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Su kendi çevresinde dönerek kabarır ve güçlü biçimde çalkalanır."},{"facet_id":"F002","role":"specialization","statement":"Hareket, denizde belirli ve yerelleşmiş tehlikeli bir su bölgesi oluşturur."},{"facet_id":"F003","role":"associated_use","statement":"Bu su hareketi yüzünden boğulma ve geminin kurtulamaması ciddi bir sonuçtur."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"İlerleyen veya rüzgârla yükselen sıradan su sırtlarını kapsar.","collision":"İlerleyen dalga ile yerinde dönen girdap birbirine karışır.","fit":"displacement","loses":"Kendi çevresinde dönüşü, yerelleşmiş girdabı ve batma tehlikesini siler.","preserves":"Suyun kabarıp hareket etmesi görünüşünü kısmen korur."},"text":"dalga"},{"category":"alternative","error_profile":{"adds":"Sakin ve tehlikesiz bölümler dahil bütün geniş tuzlu su alanını kapsar.","collision":"Tehlikeli yerel su oluşumu denizin bütünüyle karışır.","fit":"broadening","loses":"Dönme, kabarma ve gemiyi tehdit eden yerel hareketi belirtmez.","preserves":"Olayın gerçekleştiği genel su alanını korur."},"text":"deniz"}],"identity_rationale":"Kaynak ifadesi dönen suyu ve denizde suyun kabarıp çalkalandığı, gemilerin çoğu kez kurtulamadığı tehlikeli yeri birlikte tanımlar. Hazırlanan çerçeve hem dönme hareketini hem de boğulma ve gemi tehlikesini doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"girdap; gemiyi tehlikeye atan çalkantılı deniz yeri"}],"lexicalization_note":"Girdap ve tehlikeli deniz yeri anlamı çıplak biçimde tanıklanır; başka dönme türleri veya genel deniz anlamı tanıma alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dalga, açık deniz çalkantısı, durgunluk karşıtı ve sürükleyici taşkınla sınırı gösteren dört aday seçildi. Diğerleri yalnız deniz ortamını paylaşır veya aynı kökün ayrı anlamlarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kolun hareketi dönerek aynı bölgede tehlike yaratır; komşunun hareketi rüzgârla yükselen ya da ilerleyen dalga ve su tabakalarıdır.","focus_only":"Su kendi çevresinde döner ve yerelleşmiş bir batma tehlikesi oluşturur.","gloss":"rüzgârla yükselen deniz dalgası","neighbor_only":"Rüzgârın su yüzeyinde yükselttiği tabakalar veya ilerleyen dalga görünümü öne çıkar.","neighbor_ref":"root_000023/B003","relation_type":"near_neighbor","shared_zone":"İki kol da deniz yüzeyindeki güçlü ve görünür su hareketini anlatır."},{"boundary_match":"partial","distinction":"Bu kol belirli bir girdap noktasını adlandırır; komşu ise dönme koşulu aramadan denizin derin ve geniş, dalgaları hareketli bölümünü anlatır.","focus_only":"Yerel dönme hareketi ve geminin kurtulamama tehlikesi kurucudur.","gloss":"derin ve dalgalı açık deniz","neighbor_only":"Denizin derin, geniş ve dalgalı ana bölümü ile geminin orada ilerlemesi anlatılır.","neighbor_ref":"root_001344/B002","relation_type":"near_neighbor","shared_zone":"Çalkantılı deniz suyu ve geminin tehlikeli sularda bulunması alanında kesişirler."},{"boundary_match":"opposed","distinction":"Bu kol yoğun dönme ve çalkantıyla tanımlanırken komşu, hareketin kesilip suyun veya geminin durulmasıyla tanımlanır.","focus_only":"Su dönüp kabarır ve gemi için ciddi tehlike oluşturacak ölçüde hareketlidir.","gloss":"hareketten sonra durulma","neighbor_only":"Su, rüzgâr veya gemi hareketten sonra durulup yerinde kalır.","neighbor_ref":"root_000590/B001","relation_type":"polarity_pair","shared_zone":"İki kol aynı su ve gemi alanında hareket derecesinin karşıt uçlarını gösterir."},{"boundary_match":"partial","distinction":"Bu kol yerel dönme ve girdap hareketidir; komşuysa yükselen suyun taşması ve önündekileri alıp götüren genişleyici gücüyle belirlenir.","focus_only":"Tehlike, suyun yerel ve dairesel hareketinden doğar.","gloss":"yükselip önündekini sürükleyen su","neighbor_only":"Su yükselip taşarak önündekileri sürükleyen doğrusal ve yaygın bir güç gösterir.","neighbor_ref":"root_000937/B002","relation_type":"near_neighbor","shared_zone":"Güçlü su hareketinin insan veya gemi için oluşturduğu tehlikede kesişirler."}],"source_phrase_ar":"الدردور الماء الذي يدور ويخاف فيه الغرق (sihah)؛ الدردور موضع من البحر يجيش ماؤه وقلما تسلم السفينة منه (tahdhib)","source_summary":"Birleşik tanıklık, kendi çevresinde dönen ve kabaran suyu; boğulma korkusu yaratan, gemiler için çok tehlikeli bir deniz yeri olarak tanımlar.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الدردور، وهو ماء يدور أو موضع من البحر يجيش ماؤه ويخاف فيه الغرق","what_is_not_ar":"لا يدخل فيه درور المطر، ولا دوران المغزل، ولا الدردر مغارز الأسنان"},"support_links":[]},{"boundary":"Bu dal temel bilme, ustalıkla kavrama ve bildirme anlamlarıyla sınırlıdır; saldırı amacıyla yönelme, avda gizlenme ve sivri uç anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000473/B001","candidate_links":[{"candidate_id":"cand_a1af961842a53c169b45","lane":"micro"},{"candidate_id":"cand_5d9699d27c78bce7443f","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَدْرَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>adoraY`|ROOT:dry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"101:10:2:1","qac_word_ref":"101:10:2","surface_ar":"أَدْرَىٰ"}],"gloss":"bir şeyi bilme, ustalıkla kavrama ve başkasına bildirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Özne bir şeyi öğrenir, bilir veya onun hakkında kavrayış sahibi olur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ettirgen kullanımda özne, başka birinin söz konusu şeyi bilmesini sağlar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bazı kullanımlarda bilgi, düşünsel ustalık, incelik veya bir yol bulma sonucunda edinilen kavrayıştır."}}],"root_ar":"د ر ي","root_id":"root_000473","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yalın bilme çekirdeğini, özel kavrayış biçimini ve ettirgen bildirme yönünü birlikte anlatan genel karşılıktır.","boundary_detail":"Bu dal temel bilme, ustalıkla kavrama ve bildirme anlamlarıyla sınırlıdır; saldırı amacıyla yönelme, avda gizlenme ve sivri uç anlamlarını kapsamaz.","branch_image_ar":"الدراية والعلم","concept_gloss":"bir şeyi bilme, ustalıkla kavrama ve başkasına bildirme","contextual_glosses":[{"applicability":"Öznenin bir şey hakkında bilgi sahibi olduğu, ettirgenlik veya özel bir edinme yolu belirtilmeyen cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başkasını bilgilendirme ve bilgiyi düşünsel ustalıkla edinme yönlerini dışarıda bırakır.","preserves":"Bir şey hakkında bilgi sahibi olma çekirdeğini korur."},"facet_ids":["F001"],"text":"bilmek","usage_role":"general"},{"applicability":"Öznenin sahip olduğu bilgiyi başka birine aktararak onun da bilmesini sağladığı ettirgen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öznenin kendi bilme durumu ile düşünsel ustalıkla edinilen kavrayışı belirtmez.","preserves":"Başka birinin bir şeyi bilmesini sağlama yönünü korur."},"facet_ids":["F002"],"text":"haber vermek","usage_role":"contextual"},{"applicability":"Bilginin ince düşünme, beceri veya dolaylı bir yol bulma sonucunda elde edildiği özel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalın bilme kapsamını ve başkasını bilgilendiren ettirgen kullanımı dışarıda bırakır.","preserves":"Bilginin düşünsel ustalıkla edinilen kavrayış niteliğini korur."},"facet_ids":["F003"],"text":"ustalıkla kavramak","usage_role":"explanatory"}],"definition":"Bir şeyi bilmek ve ona dair kavrayış edinmek, ayrıca bir başkasının da o şeyi bilmesini sağlamaktır. Bilginin düşünsel ustalık veya ince bir yol bularak edinilmesi bu çekirdeğin özel bir görünümüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Özne bir şeyi öğrenir, bilir veya onun hakkında kavrayış sahibi olur."},{"facet_id":"F002","role":"extension","statement":"Ettirgen kullanımda özne, başka birinin söz konusu şeyi bilmesini sağlar."},{"facet_id":"F003","role":"specialization","statement":"Bazı kullanımlarda bilgi, düşünsel ustalık, incelik veya bir yol bulma sonucunda edinilen kavrayıştır."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":"Türkçedeki yerleşik kullanımında yeterlilik, dayanıklılık ve ileri görüşlülük çağrışımları ekler.","collision":"Yerleşik Türkçe anlamı, dalın geniş bilme ve bildirme yapısıyla karışır.","fit":"drifted_loanword","loses":"Yalın bilme ile başkasını bilgilendirme işlevlerini karşılamaz.","preserves":"Ustalık ve güçlü kavrayış çağrışımını kısmen korur."},"text":"dirayet"}],"identity_rationale":"Toplu kaynak ifadesi, bir şeyi bilme ile onu başkasına bildirme ettirgenliğini birlikte verir; ayrıca bazı kullanımlarda bilginin zihinsel ustalıkla edinildiğini belirtir. Hazırlanmış çerçeve bu bileşenleri aynı anlam alanında doğru biçimde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi bilmek veya ondan haberdar olmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"birine bildirmek, onun bilmesini sağlamak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bilgi ve kavrayış; özellikle düşünsel ustalıkla edinilen bilgi"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bilmiyorum"}],"lexicalization_note":"Çıplak bilme anlamı ile ettirgen bildirme, adlaşmış kavrayış ve kalıplaşmış söyleyişler ayrı tutulur; kalıba bağlı bir kullanım kökün bütün anlamına yayılmaz.","neighbor_coverage_note":"Sunulan bütün adaylar, aynı kökün diğer dalları dahil, bilme, bildirme, tanıma, haber aktarma ve öteki bağımsız anlamlar bakımından karşılaştırıldı. Okurun sınırı en kolay karıştırabileceği üç bilgi dalı seçildi; kalanlar ya daha uzak bir alanı paylaşır ya da ek bir ayrım sağlamadan bu karşıtlıkları tekrarlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bilmeden bildirmeye uzanan bir katılımcı değişimini barındırır; komşu ise bilginin akılla kavranması ve doğrulanması üzerinde yoğunlaşır. Bu nedenle yalnız bilme bağlamında yaklaşırlar, bütün sınırlarında birbirlerinin yerine geçmezler.","focus_only":"Bu dal başkasını bilgilendiren ettirgen kullanımı ve kimi bağlamlarda düşünsel ustalıkla edinilen bilgiyi de içerir.","gloss":"bilme ve akılla kavrama","neighbor_only":"Komşu dal, anlamları doğrulama, akılla kavrama ve çabuk anlama yönlerini öne çıkarır.","neighbor_ref":"root_001182/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şey hakkında bilgi ve kavrayış sahibi olmayı anlatır."},{"boundary_match":"partial","distinction":"Odak dalın bildirmesi genel bir ettirgen bilgi aktarımıdır; komşu dalda duyuru, çağrı ve bunlara bağlı roller kurucu kapsam kazanır. Araç ve olay yapısı bakımından sınırları ayrıdır.","focus_only":"Odak dal, çağrı veya ilan gerektirmeden bir şeyi bilme ve bir başkasına bildirme anlamını taşır.","gloss":"bilme ve çağrıyla duyurma","neighbor_only":"Komşu dal, seslenme, ilan etme ve çağrının ulaştığı yer gibi duyurma araçlarını ve sonuçlarını da kapsar.","neighbor_ref":"root_000022/B003","relation_type":"near_synonym","shared_zone":"İki dal da bilgi sahibi olma ve bilgiyi başkasına ulaştırma alanında kesişir."},{"boundary_match":"partial","distinction":"Odak dal genel bilgi ve kavrayış eksenindedir; komşunun çekirdeğinde bir izden tanıma ve ayırt etme işlemi vardır. Sonuçları benzeşse de bilgiye ulaşma koşulları aynı değildir.","focus_only":"Odak dal, önceden bir iz veya belirti bulunmasını gerektirmeden bilme ve bildirme anlamını taşır.","gloss":"belirtiden tanıyıp ayırt etme","neighbor_only":"Komşu dal, iz ya da belirti üzerinden tanıma, ayırt etme, karşılıklı tanışma ve araştırarak öğrenme süreçlerini içerir.","neighbor_ref":"root_001002/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da bilgi edinme ve bir şeyi bilinir kılma sonucuna ulaşabilir."}],"source_phrase_ar":"دريت الشيء والله أدرانيه (maqayis)؛ درى يدري درية ودريا ودريانا ودراية (ayn)؛ دريته ودريت به أي علمت به وأدريته أي أعلمته (sihah)؛ أتى فلان الأمر من غير درية أي من غير علم (tahdhib)؛ الدراية المعرفة المدركة بضرب من الحيل (mufradat)","source_summary":"Tanıklıkların ortak çekirdeği bir şeyi bilme ve başkasına bildirmedir. Toplu ifade, bilginin yalın öğrenmeden düşünsel ustalıkla edinilen kavrayışa kadar uzanabildiğini de gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"العلم بالشيء والدراية به وإعلام غيره به","what_is_not_ar":"ليس دفع الشيء ولا العوج ولا المدارأة المهموزة"},"support_links":["sup_37b84b512f92b308db68","sup_d613b8467aa18c1ab729"]},{"boundary":"Anlam yalnız sunulan saldırı veya baskın kalıbında geçerlidir; genel amaç edinme, fiziksel yönelme ya da her türlü saldırı anlamına genişletilemez.","branch_kind":"collocation","branch_ref":"root_000473/B002","candidate_links":[{"candidate_id":"cand_efcbcca786d919499e44","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَدْرَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>adoraY`|ROOT:dry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"101:10:2:1","qac_word_ref":"101:10:2","surface_ar":"أَدْرَىٰ"}],"gloss":"saldırı amacıyla bir yer ya da kişiyi seçmek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yer veya kişi bilinçli biçimde amaç edinilir ve eylemin yöneltileceği taraf olarak seçilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Amaç edinme, özellikle baskın veya saldırı düzenleme niyetine bağlıdır."}}],"root_ar":"د ر ي","root_id":"root_000473","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir yerin veya kişinin baskın ya da saldırı niyetiyle amaç edinildiği kalıbın tam karşılığıdır.","boundary_detail":"Anlam yalnız sunulan saldırı veya baskın kalıbında geçerlidir; genel amaç edinme, fiziksel yönelme ya da her türlü saldırı anlamına genişletilemez.","branch_image_ar":"قصد الشيء واعتماده","concept_gloss":"saldırı amacıyla bir yer ya da kişiyi seçmek","contextual_glosses":[{"applicability":"Amaç edinilen tarafın bir yer olduğu ve yapılacak eylemin baskın olarak belirtildiği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Amaç edinilen tarafın kişi veya topluluk olabilmesi ile daha genel saldırı seçeneğini dışarıda bırakır.","preserves":"Yer seçimini ve baskın amacını açık biçimde korur."},"facet_ids":["F001","F002"],"text":"bir yeri baskın için seçmek","usage_role":"contextual"},{"applicability":"Bir yere veya topluluğa karşı saldırı niyeti bulunduğunu akıcı biçimde açıklamak gereken bağlamlarda kullanılır.","error_profile":{"adds":"Fiili hareketin başlayacağı veya kara üzerinden ilerleme olacağı izlenimini ekleyebilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Belirli bir tarafa yönelik saldırı niyetini korur."},"facet_ids":["F001","F002"],"text":"üzerine yürümeyi tasarlamak","usage_role":"explanatory"}],"definition":"Belirli bir yer ya da kişiyi, üzerine baskın veya saldırı düzenlemek üzere bilinçli biçimde amaç edinip seçmektir. Anlam, genel yönelmeyi değil saldırı niyeti taşıyan bu özel yapıyı bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yer veya kişi bilinçli biçimde amaç edinilir ve eylemin yöneltileceği taraf olarak seçilir."},{"facet_id":"F002","role":"specialization","statement":"Amaç edinme, özellikle baskın veya saldırı düzenleme niyetine bağlıdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Saldırı niyeti bulunmayan hareket, ilgi veya amaç bağlamlarını da kapsar.","collision":"Genel hareket ve amaç fiilleriyle karışarak yapının savaş bağlamındaki sınırını siler.","fit":"broadening","loses":null,"preserves":"Belirli bir tarafa dönük olma yönünü korur."},"text":"yönelmek"}],"identity_rationale":"Kaynak ifadesi, bir şeyi isteyerek amaç edinme çekirdeğini belirli bir yer veya topluluğu baskın ya da saldırı için seçme kullanımıyla açıklar. Ancak mekanik collocation profili nedeniyle hazırlanan çerçeve, genel amaç edinmeyi dal anlamı saymayıp yalnız baskın veya saldırı için hedef seçme yapısını koruyacak biçimde daraltılmıştır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bir yeri baskın veya saldırı için seçmek"}],"lexicalization_note":"Bu dal yalnız belirli bir yer ya da kişiyi baskın veya saldırı amacıyla seçen yapıya bağlıdır; buradan çıplak kök için genel bir yönelme anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar genel amaç edinme, yönelme, arama, savaş hareketi ve aynı kökün bağımsız dalları bakımından değerlendirildi. Seçilen üç komşu, özel saldırı yapısını genel amaç, genel yöneliş ve gerçekleşen savaş hareketinden ayırır; ötekiler bu sınırları daha az doğrudan gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel ve araçtan bağımsız bir amaç edinme çekirdeğine sahiptir. Odak dal ise bu çekirdeği baskın veya saldırı niyeti taşıyan belirli bir yapıya daraltır.","focus_only":"Odak dal yalnız bir yer veya kişiyi baskın ya da saldırı için seçen yapıya bağlıdır.","gloss":"bilinçli biçimde amaç edinmek","neighbor_only":"Komşu dal genel amaç edinme, bilinçli yönelme ve ok ya da mızrağı belirli bir kişiye doğrultma kullanımlarını kapsar.","neighbor_ref":"root_001697/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da belirli bir tarafın isteyerek seçilmesi ve eylemin ona yöneltilmesi vardır."},{"boundary_match":"partial","distinction":"Odak dal hedef seçimi ile saldırı niyetini birlikte gerektirir. Komşu dalda yönelme nötr olabilir ve fiili hareketi de içerebilir; bu yüzden sıradan kullanımda birbirlerinin yerine geçmezler.","focus_only":"Odak dalın kurucu öğesi saldırı amacıyla seçim ve niyettir; gerçek bir hareketin başlaması gerekmez.","gloss":"bir şeye doğru yönelmek","neighbor_only":"Komşu dal bir şeye doğru yönelme, ona gitme ve onu zihinde tutma gibi daha genel süreçleri kapsar.","neighbor_ref":"root_001230/B001","relation_type":"near_neighbor","shared_zone":"İki dal da eylemin belirli bir tarafa yönelmesini anlatır."},{"boundary_match":"thematic_only","distinction":"Ortaklık yalnız savaş sahnesidir. Odak dal amaç ve hedef belirleme aşamasını, komşu ise çatışma içindeki takip ve manevra olayını adlandırır.","focus_only":"Odak dal saldırıdan önce yer veya kişi seçme ve ona yönelme niyetini bildirir.","gloss":"savaşta rakibi kovalamak","neighbor_only":"Komşu dal atlı rakiplerin birbirini kovalaması, karşılıklı saldırması ve savaşta yanıltıcı geri çekilme yapmasını anlatır.","neighbor_ref":"root_000930/B003","relation_type":"thematic","shared_zone":"Her iki dal savaş ve saldırı sahnesinde yer alabilir."}],"source_phrase_ar":"أصلان أحدهما قصد الشيء واعتماده طلبا (maqayis)؛ ادرى بنو فلان مكان كذا أي اعتمدوه بغزو أو غارة (maqayis)؛ ادرأوا فلانا كأنهم اعتمدوه بالغارة والغزو (ayn)؛ بني فلان ادروا مكانا كأنهم اعتمدوه بالغزو والغارة (sihah)","source_summary":"Tanıklıklar, amaçlı seçme çekirdeğini bir yerin veya topluluğun baskın ve saldırı için hedeflenmesiyle somutlaştırır. Bu savaş bağlamı, genel amaç edinme anlamını özel bir yapıda sınırlar.","sources":["MQ","AY","SI"],"what_is_ar":"قصد الموضع أو الشخص واعتماده طلبا ولا سيما بالغزو أو الغارة","what_is_not_ar":"ليس مطلق العلم ولا ختل الصيد ولا الدفع المهموز"},"support_links":["sup_55b7cb70fd5c82518e5f"]},{"boundary":"Dal, sıradan saklanma veya bütün avlanma biçimleriyle değil, avı aldatıp yaklaşmayı ve atış olanağı elde etmeyi sağlayan gizlenme düzeniyle sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000473/B003","candidate_links":[{"candidate_id":"cand_efcbcca786d919499e44","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَدْرَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>adoraY`|ROOT:dry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"101:10:2:1","qac_word_ref":"101:10:2","surface_ar":"أَدْرَىٰ"}],"gloss":"avın yerini gözetleyip gizlenerek onu aldatmak ve atış fırsatı bulmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Avcı, avın yerini henüz açıkça görmeden araştırır ve onu hileyle yaklaşılabilir duruma getirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Avcı bir hayvanın ardına saklanır; av bu hayvana alışıp ürkmediğinde atış olanağı doğar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gizlenme ve aldatma, avı vurmayı mümkün kılan hazırlık aşamalarıdır; vurmanın kendisi dalın tek başına çekirdeği değildir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Avcılıktaki hileli yaklaşma, bir kişiyi kandırma anlamına genişleyebilir."}}],"root_ar":"د ر ي","root_id":"root_000473","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Avın aranması, bir perde arkasında ürkütülmeden yaklaşılması ve aldatma yoluyla atış olanağı elde edilmesi aşamalarını birlikte anlatır.","boundary_detail":"Dal, sıradan saklanma veya bütün avlanma biçimleriyle değil, avı aldatıp yaklaşmayı ve atış olanağı elde etmeyi sağlayan gizlenme düzeniyle sınırlıdır.","branch_image_ar":"الختل والاستتار للصيد","concept_gloss":"avın yerini gözetleyip gizlenerek onu aldatmak ve atış fırsatı bulmak","contextual_glosses":[{"applicability":"Avcının bir perde veya hayvan arkasında saklanıp avı ürkütmeden yaklaştırdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Avın yerini önceden araştırma ile bu düzenin atış fırsatı doğuran sonucunu açıkça belirtmez.","preserves":"Avcılıktaki gizlenme ve aldatma bileşenlerini korur."},"facet_ids":["F001","F002"],"text":"avı gizlenerek kandırmak","usage_role":"contextual"},{"applicability":"Avcılık dışındaki türemiş kullanımda, bir kişinin hileli davranışla yanıltıldığı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Avı gözetleme, hayvan arkasında gizlenme ve atış olanağı elde etme yapısını dışarıda bırakır.","preserves":"Hileyle yanıltma çekirdeğinin kişiye yönelen uzantısını korur."},"facet_ids":["F004"],"text":"birini hileyle kandırmak","usage_role":"contextual"}],"definition":"Avın yerini gözetleyip onu ürkütmeden yaklaşmak, bir hayvanı perde edinerek gizlenmek ve avı aldatarak vurma fırsatı bulmaktır. Aynı hile çekirdeği, türemiş kullanımda bir kişiyi kandırmaya da uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Avcı, avın yerini henüz açıkça görmeden araştırır ve onu hileyle yaklaşılabilir duruma getirir."},{"facet_id":"F002","role":"specialization","statement":"Avcı bir hayvanın ardına saklanır; av bu hayvana alışıp ürkmediğinde atış olanağı doğar."},{"facet_id":"F003","role":"associated_use","statement":"Gizlenme ve aldatma, avı vurmayı mümkün kılan hazırlık aşamalarıdır; vurmanın kendisi dalın tek başına çekirdeği değildir."},{"facet_id":"F004","role":"extension","statement":"Avcılıktaki hileli yaklaşma, bir kişiyi kandırma anlamına genişleyebilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Avın yerini araştırma, onu aldatma, hayvanı perde edinme ve atış fırsatı oluşturma bileşenlerini kaybeder.","preserves":"Avcının görünmemek için perde arkasına geçmesini korur."},"text":"saklanmak"},{"category":"alternative","error_profile":{"adds":"Gizlenme ve aldatma içermeyen bütün avlanma yöntemlerini de kapsar.","collision":"Genel avlanma eylemiyle karışarak bu dalın özel yöntem ve aşamalarını görünmez kılar.","fit":"broadening","loses":null,"preserves":"Eylemin av elde etmeye yönelik olduğunu korur."},"text":"avlanmak"}],"identity_rationale":"Kaynak ifadesi, avın yerini henüz görmeden araştırma, avı aldatma ve bir hayvanın ardına saklanarak atış olanağı bulma aşamalarını birlikte verir; kişi kandırmaya uzanan kullanım da aynı hile çekirdeğine bağlıdır. Hazırlanmış çerçeve avcılık merkezini doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"avcının ardına saklandığı ve avı ürkütmeden yaklaştırdığı hayvan"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"avı gizlenip aldatarak atış menziline getirmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"hileyle kandırmak"}],"lexicalization_note":"Avı hileyle ele geçirme çekirdeği, avcının ardına saklandığı hayvan, avla kurulan özel yapı ve kişiyi kandıran türemiş kullanım olarak ayrı tutulur; özel av kalıbı çıplak anlama genellenmez.","neighbor_coverage_note":"Sunulan bütün adaylar gizlenme, avcı siperi, av arama, av aracı, kandırma ve aynı kökün öteki dalları bakımından değerlendirildi. Seçilen iki karşıtlık yöntemi avcı siperinden ve gece avından ayırır; kalan adaylar ya daha genel saklanmayı anlatır ya da aynı ayrımı tekrarlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yöntem ve süreçtir; komşu ise bu süreçte kullanılabilen örtü veya siperin adıdır. Biri eylemi, diğeri aracı belirttiğinden sıradan kullanımda yer değiştiremezler.","focus_only":"Odak dal avı araştırma, kandırma ve hayvanı perde edinerek atış fırsatı oluşturma sürecidir.","gloss":"avcı siperi","neighbor_only":"Komşu dal, avcının arkasına saklandığı perde veya siper nesnesini adlandırır.","neighbor_ref":"root_000584/B011","relation_type":"near_neighbor","shared_zone":"Her iki dalda da avcının görünmeden atış yapabilmek için bir örtünün ardına geçmesi vardır."},{"boundary_match":"field_only","distinction":"Odak dalda belirleyici unsur aldatıcı perde ve gizlenmedir; komşuda belirleyici unsur gece veya ışık koşuludur. Ortak alan avcılıktır, yöntemleri aynı değildir.","focus_only":"Odak dalın ayırt edici yöntemi, bir hayvanın ardında gizlenerek avı kandırmaktır.","gloss":"gece av aramak","neighbor_only":"Komşu dal gece veya ay ışığında av aramayı ve ışık koşullarından yararlanarak kuş ya da ceylan avlamayı anlatır.","neighbor_ref":"root_001255/B003","relation_type":"same_field","shared_zone":"Her iki dal avı bulup yaklaşmaya çalışan avcıyı ve avlanma hazırlığını konu edinir."}],"source_phrase_ar":"الدرية الدابة التي يستتر بها الذي يرمي الصيد (maqayis)؛ تدريت الصيد إذا نظرت أين هو ولم تره بعد ودريته ختلته (maqayis)؛ الدريئة ما تتستر به فترمي الصيد وتقول منه دريت الصيد (ayn)؛ الدرية غير مهموز دابة يستتر بها الصائد (sihah)؛ تدراه وادراه بمعنى أي ختله (sihah)؛ دريت فلانا أدريه دريا إذا ختلته (tahdhib)؛ الدرية البعير يستتر به من الوحش (tahdhib)؛ الدرية للناقة التي ينصبها الصائد ليأنس بها الصيد (mufradat)","source_summary":"Tanıklıklar, avı aldatma ile avcının bir hayvanı gizlenme perdesi olarak kullanmasını aynı avlanma düzeninde birleştirir. Toplu ifade ayrıca avın yerini araştıran ilk aşamayı ve kişi kandırmaya uzanan kullanımı korur.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"ختل الصيد والتستر له بدابة أو بعير أو ناقة حتى يمكن رميه","what_is_not_ar":"ليس العلم المجرد ولا قصد الغارة ولا الحلقة التي يتعلم عليها الطعن"},"support_links":["sup_55b7cb70fd5c82518e5f"]},{"boundary":"Dalın merkezi sivri veya belirgin uçtur; saçla ilgili araç ve eylem bu biçimsel temelden türemiştir, genel saç bakımı ya da her türlü keskinlik anlamına yayılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000473/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَدْرَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>adoraY`|ROOT:dry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"101:10:2:1","qac_word_ref":"101:10:2","surface_ar":"أَدْرَىٰ"}],"gloss":"sivri uç ve bundan ad alan saç düzeltme aracı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesnede sivri, keskin veya belirginleşmiş bir uç bulunur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sivri boynuz ve uçları dolulukla belirginleşen iki meme, bu biçim özelliğine göre adlandırılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sivri boynuza benzeyen şiş biçimli araç, saçı ayırıp düzeltmek için kullanılır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kadının saçını tarayıp düzeltmesi, araç adından türeyen eylem olarak anlatılır."}}],"root_ar":"د ر ي","root_id":"root_000473","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın sivrilik temelini ve bu biçimden türeyen özel araç anlamını birlikte göstermek gereken genel açıklamalarda kullanılır.","boundary_detail":"Dalın merkezi sivri veya belirgin uçtur; saçla ilgili araç ve eylem bu biçimsel temelden türemiştir, genel saç bakımı ya da her türlü keskinlik anlamına yayılmaz.","branch_image_ar":"المدرى والحد المحدد","concept_gloss":"sivri uç ve bundan ad alan saç düzeltme aracı","contextual_glosses":[{"applicability":"Hayvanın boynuzunun keskin ve sivri ucunun adlandırıldığı somut bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Saç düzeltme aracı, bu araçla yapılan eylem ve öteki belirgin uç adlarını dışarıda bırakır.","preserves":"Sivri uç çekirdeğini ve onun boynuzdaki özel gerçekleşmesini korur."},"facet_ids":["F001","F002"],"text":"sivri boynuz","usage_role":"contextual"},{"applicability":"Saçı ayırmak, taramak veya düzeltmek için kullanılan ince ve sivri araçtan söz edildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Boynuz ve başka sivri uç adlarını, ayrıca araçla yapılan eylemi dışarıda bırakır.","preserves":"Sivri biçimi ve saç düzeltmeye yarayan araç işlevini korur."},"facet_ids":["F001","F003"],"text":"saç ayırma şişi","usage_role":"contextual"},{"applicability":"Kadının saçını ilgili araçla tarayıp düzenlediği eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sivri uç çekirdeğini, boynuz adını ve kullanılan aracın biçimini açıkça belirtmez.","preserves":"Saç üzerinde yapılan tarama ve düzeltme eylemini korur."},"facet_ids":["F004"],"text":"saçını tarayıp düzeltmek","usage_role":"contextual"}],"definition":"Bir şeyde sivri, keskin veya belirgin bir ucun bulunmasıdır; bu özellik hayvanın boynuzunu, dolunca uçları belirginleşen iki memesini ve saçı ayırıp düzeltmede kullanılan şiş biçimli aracı adlandırır. Saçı bu araçla tarayıp düzeltme eylemi de aynı biçimsel temelden türemiştir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesnede sivri, keskin veya belirginleşmiş bir uç bulunur."},{"facet_id":"F002","role":"specialization","statement":"Sivri boynuz ve uçları dolulukla belirginleşen iki meme, bu biçim özelliğine göre adlandırılır."},{"facet_id":"F003","role":"extension","statement":"Sivri boynuza benzeyen şiş biçimli araç, saçı ayırıp düzeltmek için kullanılır."},{"facet_id":"F004","role":"associated_use","statement":"Kadının saçını tarayıp düzeltmesi, araç adından türeyen eylem olarak anlatılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Dişli ve geniş yüzeyli sıradan tarak biçimini düşündürür.","collision":"Genel saç tarağıyla karışarak aracın sivri uçtan türeyen özel biçimini siler.","fit":"displacement","loses":"Sivri boynuz temelini ve şiş biçimli tekil uç özelliğini kaybeder.","preserves":"Saçı düzenlemeye yarayan araç işlevini kısmen korur."},"text":"tarak"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Boynuz, saç aracı ve saç düzeltme eylemine uzanan somut adlandırmaları dışarıda bırakır.","preserves":"Dalın sivrilik ve keskin uç temelini korur."},"text":"keskinlik"}],"identity_rationale":"Kaynak ifadesi, nesnedeki sivrilik çekirdeğinden hayvanın sivri boynuzuna, saçı düzeltmeye yarayan şiş biçimli araca ve saçı bu araçla tarama eylemine uzanan düzenli bir gelişim kurar. Hazırlanmış çerçeve bu türetim zincirini doğru temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"sivri boynuz; saçı düzeltmeye yarayan sivri araç"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"saçı ayırıp düzeltmeye yarayan şiş biçimli araç"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"saçını tarayıp düzeltmek"}],"lexicalization_note":"Sivri uç çekirdeği, boynuz ve belirgin uç adlarıyla birlikte saç düzeltme aracına ve bu araçla yapılan eyleme uzanır; araç ve eylem anlamları çıplak kökün sınırsız anlamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar sivri uç, boynuz, çıkıntı, saç aracı ve saç düzenleme işlemi açısından karşılaştırıldı. Seçilen dört komşu dalın biçimsel çekirdeğini keskin kenardan, genel boynuz çıkıntısından, araç eşadından ve başka saç işlemlerinden ayırır; kalanlar daha uzak biçim benzerlikleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ayırt edici somutlaşmaları boynuz ve saç aracıdır. Komşu dal ise kesme, delme ve etkili olma gücünü merkez alır; bu nedenle ortak sivrilik alanına rağmen ikame edilemezler.","focus_only":"Odak dal sivri boynuzdan saç düzeltme aracına uzanan biçim ve adlandırma zincirini içerir.","gloss":"kesici ve delici keskin uç","neighbor_only":"Komşu dal kesici veya delici ağız, bıçak ve mızrak ucu ile dil, bakış ve anlayışın etkili keskinliğine kadar uzanır.","neighbor_ref":"root_000002/B005","relation_type":"near_neighbor","shared_zone":"Her iki dalda da sivrilik, keskin uç ve nüfuz etme olanağı bulunur."},{"boundary_match":"partial","distinction":"Odak dal boynuzdaki keskin ucu ve bundan türeyen aracı öne çıkarır; komşu dalda belirleyici özellik güçlü çıkıntı ve çift yan biçimidir. Türetim yönleri farklıdır.","focus_only":"Odak dal boynuzun sivriliğini temel alır ve oradan saç aracına ve eylemine uzanır.","gloss":"boynuz biçimli güçlü çıkıntı","neighbor_only":"Komşu dal boynuzu güçlü bir çıkıntı olarak ele alıp başın yanları, saç örgüsü, dağ ve başka çıkıntılara genişletir.","neighbor_ref":"root_001221/B006","relation_type":"near_neighbor","shared_zone":"İki dal hayvan boynuzunu ve onun sivri, dışa çıkan biçimini paylaşır."},{"boundary_match":"partial","distinction":"Komşu, odak dalın yalnız araç facetine karşılık gelen dar bir adlandırmadır. Odak dalın boynuz, genel sivrilik ve saç düzeltme eylemi kapsamı komşuda bulunmaz.","focus_only":"Odak dal sivrilik çekirdeğini, boynuz ile saç aracını ve bunlardan türeyen eylemi birlikte kapsar.","gloss":"aynı sivri aracın başka adı","neighbor_only":"Komşu dal yalnız aynı tür aracın başka bir adını bildirir.","neighbor_ref":"root_001103/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal saç düzeltmede kullanılabilen sivri araç referansında buluşur."},{"boundary_match":"field_only","distinction":"Odak dalın işlemi sivri araçla tarama ve ayırmadır; komşunun işlemi kesme veya bağlamadır. Ortak saç bakımı alanı, eylem çekirdeklerini eşitlemez.","focus_only":"Odak dal saçı sivri bir araçla ayırıp tarayarak düzeltmeyi anlatır.","gloss":"saçı kesip bağlayarak düzenlemek","neighbor_only":"Komşu dal saçı keserek kısaltma, düğümleme veya kesime hazırlama işlemlerini anlatır.","neighbor_ref":"root_000952/B004","relation_type":"same_field","shared_zone":"Her iki dal saçın biçimini düzenleyen işlemler alanındadır."}],"source_phrase_ar":"الأصل الآخر حدة تكون في الشيء (maqayis)؛ مدرى لأنه محدد (maqayis)؛ شاة مدراة حديدة القرنين (maqayis)؛ تدرت المرأة إذا سرحت شعرها (maqayis;sihah)؛ المدريين طبيا الشاة لأنهما إذا امتلئا تحدد طرفاهما (maqayis)؛ المدرى القرن والمدراة شيء كالمسلة (sihah)؛ المدرى لقرن الشاة واستعير المدرى لما يصلح به الشعر (mufradat)","source_summary":"Tanıklıklar sivrilik çekirdeğini boynuz, belirgin uç ve şiş biçimli saç aracı üzerinden kurar. Toplu ifade, araçla saç düzeltme eylemini de bu somut biçim benzerliğinin türevi olarak gösterir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"المدرى والمدراة للقرن المحدد وما يسرح به الشعر وما سمي مدريين لتحدد طرفيه","what_is_not_ar":"ليس العلم ولا الختل ولا الدريئة المهموزة التي يتعلم عليها الطعن"},"support_links":[]},{"boundary":"Bu dal silah kullanma alıştırması için karşıya konan hedef nesnesidir; avcının arkasına saklandığı hayvan veya siper ile gerçek avı vurma süreci değildir.","branch_kind":"bare","branch_ref":"root_000473/B005","candidate_links":[{"candidate_id":"cand_efcbcca786d919499e44","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَدْرَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>adoraY`|ROOT:dry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"101:10:2:1","qac_word_ref":"101:10:2","surface_ar":"أَدْرَىٰ"}],"gloss":"saplama ve atış alıştırma hedefi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Silah kullanma alıştırmasında vurulmak üzere karşıya bir nesne konur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hedef halka, deri veya başka bir maddeden olabilir ve saplama ya da atış öğreniminde kullanılır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Adlandırma tanıklıklarda farklı sesletim biçimleriyle aktarılır; bu çeşitlilik hedef nesnesinin kavram sınırını değiştirmez."}}],"root_ar":"د ر ي","root_id":"root_000473","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Silah kullanmayı öğrenen kişinin vurmak üzere karşısına koyduğu halka, deri veya benzeri nesneyi genel olarak adlandırır.","boundary_detail":"Bu dal silah kullanma alıştırması için karşıya konan hedef nesnesidir; avcının arkasına saklandığı hayvan veya siper ile gerçek avı vurma süreci değildir.","branch_image_ar":"الدريئة التي يتعلم عليها الطعن","concept_gloss":"saplama ve atış alıştırma hedefi","contextual_glosses":[{"applicability":"Mızrağı doğru yöneltme ve saplama becerisinin üzerinde çalışıldığı hedef nesnesinden söz edildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ok veya başka bir araçla yapılan atış alıştırması kapsamını dışarıda bırakır.","preserves":"Saplama öğrenimini ve karşıya konan hedef nesnesini korur."},"facet_ids":["F001","F002"],"text":"mızrak alıştırma hedefi","usage_role":"contextual"},{"applicability":"Uzaktan atılan bir silahla vurma becerisinin geliştirildiği hedef nesnesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yakından mızrak saplamayı öğrenme kullanımını dışarıda bırakır.","preserves":"Atış öğrenimini ve hedef nesnesinin alıştırma işlevini korur."},"facet_ids":["F001","F002"],"text":"atış alıştırma hedefi","usage_role":"contextual"}],"definition":"Mızrak saplamayı veya atış yapmayı öğrenmek için karşıya konan halka, deri ya da benzeri hedef nesnesidir. Adlandırmanın tanıklanan sesletim çeşitleri değişse de alıştırma işlevi ve hedef rolü aynıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Silah kullanma alıştırmasında vurulmak üzere karşıya bir nesne konur."},{"facet_id":"F002","role":"specialization","statement":"Hedef halka, deri veya başka bir maddeden olabilir ve saplama ya da atış öğreniminde kullanılır."},{"facet_id":"F003","role":"source_variant","statement":"Adlandırma tanıklıklarda farklı sesletim biçimleriyle aktarılır; bu çeşitlilik hedef nesnesinin kavram sınırını değiştirmez."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Taşınan ve kullanıcıyı saldırıdan koruyan savunma aracı işlevini ekler.","collision":"Deri malzeme ve darbe alma ortaklığı, alıştırma hedefini savunma aracıyla karıştırabilir.","fit":"displacement","loses":"Öğrenme amacıyla sabit hedef olarak karşıya konma işlevini kaybeder.","preserves":"Bir silah darbesini karşılayan nesne olma özelliğini kısmen korur."},"text":"kalkan"}],"identity_rationale":"Kaynak ifadesi, saplama öğrenmek için karşıya konan halka, deri veya başka bir nesneyi ortak çekirdek olarak verir; bir tanıklık bunu atış öğrenimine de açar. Hazırlanmış çerçeve alıştırma nesnesini avcının gizlenme perdesinden doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"üzerinde saplama alıştırması yapılan hedef"}],"lexicalization_note":"Tanıklanan çıplak ad, saplama veya atış alıştırmasının hedef nesnesini belirtir; avcılıkta gizlenmeye yarayan kalıba bağlı anlam bu dala taşınmaz.","neighbor_coverage_note":"Bütün adaylar hedef nesnesi, mızrağı doğrultma, alıştırma oku, avcı siperi ve güçlü saplama bakımından karşılaştırıldı. Seçilen beş komşu, hedefi isabet sonucundan, silah eyleminden, kullanılan oktan ve avcılık düzeninden ayırır; kalanlar daha uzak savaş veya beden konumlarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal daha genel bir alıştırma nesnesidir ve saplamayı da içerir. Komşu dal okçuluk hedefinde uzmanlaşır ve başarılı isabet olayına uzanır; bu ek sınırlar tam eşanlamlılığı engeller.","focus_only":"Odak dal atışın yanı sıra mızrakla saplama öğrenimini ve farklı malzemelerden hedefleri kapsar.","gloss":"okçuluk hedefi ve isabet","neighbor_only":"Komşu dal özellikle okçuluk yarışmasında dikilen deri hedefi ve atışın hedefe isabet etmesi sonucunu da kapsar.","neighbor_ref":"root_001218/B002","relation_type":"near_synonym","shared_zone":"Her iki dal atış öğrenimi veya yarışmasında vurulmak üzere dikilen hedef nesnesini anlatır."},{"boundary_match":"partial","distinction":"Odak dalın sınırı öğrenme hedefiyle belirlenir. Komşunun avcılıkta gizlenme aracını da kapsaması, onun kullanım alanını nesne benzerliği üzerinden genişletir.","focus_only":"Odak dal yalnız saplama veya atış öğrenmek için karşıya konan hedef nesnesidir.","gloss":"alıştırma hedefi veya avcı perdesi","neighbor_only":"Komşu dal alıştırma hedefinin yanında avcının arkasına saklandığı perde veya hayvanı da aynı kapsamda tutar.","neighbor_ref":"root_000466/B005","relation_type":"near_neighbor","shared_zone":"İki dal silahın yöneltildiği alıştırma nesnesinde kesişir."},{"boundary_match":"field_only","distinction":"Odak dal hedef rolündeki nesneyi, komşu dal ise silahı doğrultan kişinin eylemini adlandırır. Katılımcı rolleri karşıt olduğu için birbirlerinin yerine kullanılamazlar.","focus_only":"Odak dal mızrağın yöneltildiği ve üzerinde alıştırma yapılan nesnedir.","gloss":"mızrağı amaca doğrultmak","neighbor_only":"Komşu dal mızrağı istenen noktaya doğrultup saplamaya hazırlama eylemidir.","neighbor_ref":"root_000161/B007","relation_type":"same_field","shared_zone":"Her iki dal mızrak kullanma ve belirli bir noktaya saplama sahnesindedir."},{"boundary_match":"field_only","distinction":"Odak dal vurulan nesnedir, komşu ise ona atılan küçük silahlardır. Aynı eğitim sahnesindeki ayrı araçları gösterirler.","focus_only":"Odak dal atış veya saplama alıştırmasında vurulan hedef nesnesidir.","gloss":"alıştırma için küçük oklar","neighbor_only":"Komşu dal atış öğreniminde kullanılan küçük okları, yani hedefe gönderilen araçları adlandırır.","neighbor_ref":"root_000339/B002","relation_type":"same_field","shared_zone":"İki dal silah kullanmayı öğrenme ve atış alıştırması alanında buluşur."},{"boundary_match":"thematic_only","distinction":"Odak dal öğrenme ortamındaki nesneyi, komşu dal ise avcılık yöntemini anlatır. Hedef nesnesi ile gizlenme süreci aynı kavram değildir.","focus_only":"Odak dal cansız ve alıştırma amacıyla karşıya konmuş bir hedef nesnesidir.","gloss":"avı gizlenerek kandırmak","neighbor_only":"Komşu dal canlı avı bir hayvanın arkasında gizlenerek kandırma ve vurma fırsatı bulma sürecidir.","neighbor_ref":"root_000473/B003","relation_type":"thematic","shared_zone":"Her iki dalda da bir şeye silah yöneltme ve onu vurma düşüncesi bulunur."}],"source_phrase_ar":"الدريئة الحلقة التي يتعلم عليها الطعن (maqayis)؛ الدريئة من أدم وغيره يتعلم عليها الطعان (ayn)؛ الدريئة بالهمز الحلقة (ayn)؛ الدريئة مهموزة الحلقة التي يتعلم الرامي عليها (tahdhib)؛ الدرية لما يتعلم عليه الطعن (mufradat)","source_summary":"Tanıklıklar saplama veya atış öğreniminde kullanılan hedef nesnesinde birleşir; nesnenin halka, deri ya da başka bir malzemeden yapılabilmesi çekirdeği değiştirmez. Toplu ifade adlandırma biçimindeki çeşitliliği de anlam ayrılığına dönüştürmez.","sources":["MQ","AY","TA","MU"],"what_is_ar":"الدريئة أو الدرية لما يتعلم عليه الطعن أو الرمي","what_is_not_ar":"ليست الدرية التي يستتر بها الصائد ولا ختل الصيد ولا دفع الشيء"},"support_links":["sup_55b7cb70fd5c82518e5f"]},{"boundary":"Dal yalnız insanlarla yumuşak ve geçimli davranma yapısını tanımlar; yakın biçimlerde görülen sakınma, çekişme ve karşı çıkma anlamları kaynak varyantı olarak sınırda tutulur.","branch_kind":"collocation","branch_ref":"root_000473/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَدْرَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>adoraY`|ROOT:dry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"101:10:2:1","qac_word_ref":"101:10:2","surface_ar":"أَدْرَىٰ"}],"gloss":"insanlarla yumuşak ve incelikli geçinmek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, insanlara karşı yumuşak, geçimli ve incelikli davranarak iyi ilişkiyi sürdürür."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yumuşak davranış, doğrudan çatışmadan kaçınmaya ve kişinin kendisini karşı tarafın zararından korumasına yarayabilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yakın bir biçim çekişme ve karşı çıkma anlamı taşır; bu karşıt değer olumlu geçinme anlamının sınırını gösterir."}}],"root_ar":"د ر ي","root_id":"root_000473","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan ilişkilerinde çatışmayı önleyen, iyi geçinmeyi ve ölçülü yumuşaklığı birlikte anlatan yapının doğal genel karşılığıdır.","boundary_detail":"Dal yalnız insanlarla yumuşak ve geçimli davranma yapısını tanımlar; yakın biçimlerde görülen sakınma, çekişme ve karşı çıkma anlamları kaynak varyantı olarak sınırda tutulur.","branch_image_ar":"ملاينة الناس ومداراتهم","concept_gloss":"insanlarla yumuşak ve incelikli geçinmek","contextual_glosses":[{"applicability":"Bir kişiye sertçe karşı çıkmak yerine ölçülü ve incelikli davranış gösterilen cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İyi geçinmeyi sürdürme ve kendini çatışmadan koruma amaçlarını açıkça belirtmez.","preserves":"İlişkide sertlikten kaçınan yumuşak davranış biçimini korur."},"facet_ids":["F001"],"text":"yumuşak davranmak","usage_role":"general"},{"applicability":"İlişkiyi bozmamak için karşı tarafa incelikle davranılan ve gerilimden kaçınılan bağlamlarda kullanılır.","error_profile":{"adds":"Karşı tarafı özellikle memnun etme ve onayını kazanma amacı çağrışımını ekleyebilir.","collision":null,"fit":"broadening","loses":null,"preserves":"İyi geçinme, incelik ve çatışmadan kaçınma yönlerini korur."},"facet_ids":["F001","F002"],"text":"gönlünü hoş tutarak geçinmek","usage_role":"contextual"}],"definition":"İnsanlarla ilişkide çatışmaya girmeden yumuşak, incelikli ve geçimli davranmak, böylece ilişkiyi sürdürmek ve kendini sürtüşmeden korumaktır. Yakın biçimlerin birinden sakınma, çekişme veya karşı çıkma anlamları bu olumlu ilişki çekirdeğinin dışında kalır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, insanlara karşı yumuşak, geçimli ve incelikli davranarak iyi ilişkiyi sürdürür."},{"facet_id":"F002","role":"associated_use","statement":"Yumuşak davranış, doğrudan çatışmadan kaçınmaya ve kişinin kendisini karşı tarafın zararından korumasına yarayabilir."},{"facet_id":"F003","role":"source_variant","statement":"Yakın bir biçim çekişme ve karşı çıkma anlamı taşır; bu karşıt değer olumlu geçinme anlamının sınırını gösterir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Çıkar için samimiyetsiz övgü, boyun eğme ve değersizleşme yargısı ekler.","collision":"Uzlaştırıcı davranışı çıkarcı ve küçültücü bir tutumla karıştırır.","fit":"displacement","loses":"İyi ahlak, karşılıklı geçim ve ölçülü incelik yönlerini kaybeder.","preserves":"Karşı tarafı kızdırmamak için yumuşak davranma görünümünü kısmen korur."},"text":"yalakalık"},{"category":"confusable","error_profile":{"adds":"Uyuşmazlık, karşı çıkma ve açık çatışma anlamlarını ekler.","collision":"Yakın biçimdeki karşıt kaynak varyantıyla karışarak bu dalın olumlu ilişki anlamını tersine çevirir.","fit":"displacement","loses":"Yumuşaklık, incelik, iyi geçinme ve çatışmadan kaçınma bileşenlerini bütünüyle kaybeder.","preserves":"İki kişi arasındaki ilişki ve karşılıklı davranış alanını korur."},"text":"çekişmek"}],"identity_rationale":"Kaynak ifadesinin baskın yönü insanlarla iyi geçinmek için yumuşak, uzlaştırıcı ve incelikli davranmaktır. Bununla birlikte yakın bir biçim birinden sakınmayı, çekişmeyi veya karşı çıkmayı da bildirebilir; bu karşıt kullanım yok sayılamaz, fakat olumlu ilişki yapısının çekirdeğine de katılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"insanlara karşı yumuşak ve uzlaştırıcı davranmak"}],"lexicalization_note":"Anlam insanlarla ilişkide yumuşak ve uzlaştırıcı davranmayı bildiren yapıya bağlıdır; yakın biçimlerin karşıt anlamları bu yapıya eklenmez ve buradan çıplak kök anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar yumuşak davranma, çatışmadan korunma, hoşnut etme, iyi geçinme, sertlik ve ilişkiyi kesme eksenlerinde karşılaştırıldı. Seçilen beş komşu tam eşdeğeri, amaç bakımından daralan yakın anlamları, daha geniş yumuşaklık alanını ve açık karşıtlığı gösterir; kalanlar bu sınırları tekrarlar.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek eylem, katılımcılar ve ilişki sınırı bakımından anlamlı bir ayrım yoktur. Tek kişi veya insanlar topluluğu üzerinden örneklenmeleri tam ikameyi bozmaz.","focus_only":null,"gloss":"birine yumuşak ve incelikli davranmak","neighbor_only":null,"neighbor_ref":"root_000485/B006","relation_type":"synonym","shared_zone":"Her iki dal, kişiyle çatışmadan geçinmek için ona yumuşak, ölçülü ve incelikli davranmayı anlatır."},{"boundary_match":"partial","distinction":"Odak dalın kapsamı olumlu toplumsal ilişkiyi de içerir; komşu dalda kendini karşı taraftan koruma amacı daha belirleyicidir. Amaç ağırlıkları farklı olduğu için sınır yalnız kısmen örtüşür.","focus_only":"Odak dal iyi ahlak ve geçimli ilişkiyi sürdürme yönünü açıkça içerir.","gloss":"yumuşak davranarak kendini korumak","neighbor_only":"Komşu dal karşıdaki kişiden korunmayı ve doğrudan çatışma yerine yumuşaklığı bir savunma yolu olarak seçmeyi öne çıkarır.","neighbor_ref":"root_000466/B008","relation_type":"near_synonym","shared_zone":"Her iki dal bir kişiye sertçe karşı çıkmak yerine yumuşak ve incelikli davranmayı anlatır."},{"boundary_match":"partial","distinction":"Odak dal ilişki alanı bakımından geneldir. Komşu dalın talep ve hoşnut etme koşulu daha dardır; bu özel koşul her odak kullanımında bulunmaz.","focus_only":"Odak dal genel insan ilişkilerinde iyi geçinmeyi ve incelikli davranmayı kapsar.","gloss":"istekte bulunurken yumuşak davranmak","neighbor_only":"Komşu dal özellikle bir talep sırasında karşı tarafı hoşnut etmeye çalışma ve yumuşatma bağlamında uzmanlaşır.","neighbor_ref":"root_000751/B002","relation_type":"near_synonym","shared_zone":"İki dal da karşı tarafla iyi geçinmek için sertlikten kaçınıp yumuşak davranmayı anlatır."},{"boundary_match":"opposed","distinction":"Odak dal yakınlığı ve geçimi koruyan yumuşak kutuptadır; komşu dal sertlik ve kopuş kutbundadır. Ortak ilişki ekseninde sonuçları karşıt yöndedir.","focus_only":"Odak dal ilişkiyi yumuşaklık ve incelikle sürdürmeyi amaçlar.","gloss":"sert davranıp ilişkiyi kesmek","neighbor_only":"Komşu dal sertlik, kötü geçim ve bağları keserek ilişkiden uzaklaşmayı anlatır.","neighbor_ref":"root_000251/B002","relation_type":"antonym","shared_zone":"Her iki dal kişiler arasındaki ilişkinin nasıl sürdürüldüğünü veya bozulduğunu değerlendirir."},{"boundary_match":"partial","distinction":"Odak dalın kurucu ortamı insanlarla geçinme ve gerilimi önlemedir. Komşu dal yumuşaklığı şefkat, yardım ve iş yapma biçimine genişletir; sıradan kullanımda tam ikame yoktur.","focus_only":"Odak dal insanlarla çatışmadan geçinmek için gösterilen ölçülü ve incelikli davranışa bağlıdır.","gloss":"şefkatli ve yumuşak davranmak","neighbor_only":"Komşu dal işte kolaylık, şefkat, iyilik ulaştırma, koruma ve yakınlara iyi davranma gibi daha geniş bir yumuşaklık alanını kapsar.","neighbor_ref":"root_001356/B001","relation_type":"near_neighbor","shared_zone":"İki dal sertlikten uzak, yumuşak ve yarar gözeten davranışta kesişir."}],"source_phrase_ar":"مداراة الناس تهمز ولا تهمز وهي المداجاة والملاينة (sihah)؛ دارأت الرجل مدارأة إذا اتقيته (tahdhib)؛ المدارأة المشاغبة والمخالفة (tahdhib)؛ المداراة في حسن الخلق والمعاشرة مع الناس (tahdhib)","source_summary":"Toplu tanıklık, insanlarla iyi geçinmede yumuşaklık ve incelik çekirdeğini verir; bu tavrın kişiyi çatışmadan koruyan yönünü de gösterir. Aynı toplu ifade, yakın bir biçimde ortaya çıkan çekişme ve karşı çıkma değerini ortak anlama katmadan sınır karşıtlığı olarak korur.","sources":["AY","SI","TA"],"what_is_ar":"المداراة في حسن الخلق والمعاشرة والمداجاة والملاينة","what_is_not_ar":"ليست المدارأة المهموزة للمشاغبة والمخالفة والتدافع"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["101:10:1"],"branch_refs":[],"candidate_id":"cand_8bc15f8b526b4eb8127e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:10:1:boundary-handoff","source_type":"word_analysis","support_ids":["sup_41c5c9a6de2faaad1916","sup_dbe4464e28d3923ae2e6"],"title":"causal closure becomes open question","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:1","qac_refs":["101:10:1:1"],"status":"accepted"}},{"anchor_refs":["101:10:1"],"branch_refs":[],"candidate_id":"cand_717075878b63c9b0d4bb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:10:1:continuation-resumption","source_type":"word_analysis","support_ids":["sup_b4e522cdb38fb4a26acc","sup_dbe4464e28d3923ae2e6"],"title":"continuation and resumption stay live","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:1","qac_refs":["101:10:1:1"],"status":"accepted"}},{"anchor_refs":["101:10:1"],"branch_refs":[],"candidate_id":"cand_bba2bc4e648db38985c8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:10:1:same-surah-formula-return","source_type":"word_analysis","support_ids":["sup_38efc5d7c57e18143918","sup_dbe4464e28d3923ae2e6"],"title":"opening formula returns from 101:3","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:1","qac_refs":["101:10:1:1"],"status":"accepted"}},{"anchor_refs":["101:10:1"],"branch_refs":[],"candidate_id":"cand_f255a5231a93066697d3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:10:1:wa-ma-sound-launch","source_type":"word_analysis","support_ids":["sup_ce58258a41baf4cd3fa5","sup_dbe4464e28d3923ae2e6"],"title":"short connector opens into long question","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:1","qac_refs":["101:10:1:1"],"status":"accepted"}},{"anchor_refs":["101:10:2"],"branch_refs":[],"candidate_id":"cand_551ca6fbc3ba014ca4d3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:10:2:lengthened-onset","source_type":"word_analysis","support_ids":["sup_2320e3349c064e8ab53d","sup_d8dfaec9bd4aa720fde3"],"title":"lengthened opening makes the question stretch","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:2","qac_refs":["101:10:1:2"],"status":"accepted"}},{"anchor_refs":["101:10:2"],"branch_refs":[],"candidate_id":"cand_8a193bc27c6fbb3a0984","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:10:2:outer-interrogative-subject","source_type":"word_analysis","support_ids":["sup_2320e3349c064e8ab53d","sup_62fdcb90ecf7ab5f3a6f"],"title":"outer question asks for the knowledge-source","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:2","qac_refs":["101:10:1:2"],"status":"accepted"}},{"anchor_refs":["101:10:2"],"branch_refs":[],"candidate_id":"cand_c0187d45dad38d01d97f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:10:2:paired-ma-setup","source_type":"word_analysis","support_ids":["sup_2320e3349c064e8ab53d","sup_56ef4e8253200b144476"],"title":"first question-word sets up the second","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:2","qac_refs":["101:10:1:2"],"status":"accepted"}},{"anchor_refs":["101:10:2"],"branch_refs":[],"candidate_id":"cand_409682e6594d609635dc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:10:2:rhetorical-epistemic-challenge","source_type":"word_analysis","support_ids":["sup_2320e3349c064e8ab53d","sup_95d51eb7b39f894aeca6"],"title":"question form exposes no adequate answer","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:2","qac_refs":["101:10:1:2"],"status":"accepted"}},{"anchor_refs":["101:10:3"],"branch_refs":[],"candidate_id":"cand_da821c8c6a2332be12d1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000469","root_000473"],"scope":"focus_ayah","source_local_id":"101:10:3:addressee-shift","source_type":"word_analysis","support_ids":["sup_9c36c532c06979c4756c","sup_b21f1c00264057a9ecbe"],"title":"suffix turns verdict into direct address","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:3","qac_refs":["101:10:2:1","101:10:2:2"],"status":"accepted"}},{"anchor_refs":["101:10:3"],"branch_refs":[],"candidate_id":"cand_24a4b5cb827fdb0953cc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000469","root_000473"],"scope":"focus_ayah","source_local_id":"101:10:3:blocked-reach-encounter","source_type":"word_analysis","support_ids":["sup_b21f1c00264057a9ecbe","sup_d97d2b6e55be85ea676f"],"title":"knowledge as encounter cannot reach the abyss","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:3","qac_refs":["101:10:2:1","101:10:2:2"],"status":"accepted"}},{"anchor_refs":["101:10:3"],"branch_refs":[],"candidate_id":"cand_a75179a53426b2c6a8c8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000469","root_000473"],"scope":"focus_ayah","source_local_id":"101:10:3:double-ma-hinge","source_type":"word_analysis","support_ids":["sup_56f8e36edeaeabdf4b1b","sup_b21f1c00264057a9ecbe"],"title":"verb hinges between two questions","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:3","qac_refs":["101:10:2:1","101:10:2:2"],"status":"accepted"}},{"anchor_refs":["101:10:3"],"branch_refs":[],"candidate_id":"cand_a73b8e83d70ac8888e9e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000469","root_000473"],"scope":"focus_ayah","source_local_id":"101:10:3:form-iv-causative-frame","source_type":"word_analysis","support_ids":["sup_b21f1c00264057a9ecbe","sup_cedc9c2268a2bd63d06d"],"title":"causative verb asks what could make you know","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:3","qac_refs":["101:10:2:1","101:10:2:2"],"status":"accepted"}},{"anchor_refs":["101:10:3"],"branch_refs":[],"candidate_id":"cand_9599dc7a87d1fc51fe8d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000469","root_000473"],"scope":"focus_ayah","source_local_id":"101:10:3:forward-answer-gap","source_type":"word_analysis","support_ids":["sup_7517be3a2544695e7810","sup_b21f1c00264057a9ecbe"],"title":"knowledge gap points to 101:11","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:3","qac_refs":["101:10:2:1","101:10:2:2"],"status":"accepted"}},{"anchor_refs":["101:10:3"],"branch_refs":[],"candidate_id":"cand_3d387b7822ba7c7c14eb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000469","root_000473"],"scope":"focus_ayah","source_local_id":"101:10:3:knowledge-branch-narrowed","source_type":"word_analysis","support_ids":["sup_b21f1c00264057a9ecbe","sup_b930a013ed5fa6d8c881"],"title":"root range narrows to knowing and making known","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:3","qac_refs":["101:10:2:1","101:10:2:2"],"status":"accepted"}},{"anchor_refs":["101:10:3"],"branch_refs":[],"candidate_id":"cand_8cac139d65bff2723ee6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000469","root_000473"],"scope":"focus_ayah","source_local_id":"101:10:3:negative-epistemic-force","source_type":"word_analysis","support_ids":["sup_901e41fbd90bf28f40a8","sup_b21f1c00264057a9ecbe"],"title":"knowing verb argues impossibility","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:3","qac_refs":["101:10:2:1","101:10:2:2"],"status":"accepted"}},{"anchor_refs":["101:10:3"],"branch_refs":[],"candidate_id":"cand_c738e71b4ecff6da90f7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000469","root_000473"],"scope":"focus_ayah","source_local_id":"101:10:3:perfective-closure","source_type":"word_analysis","support_ids":["sup_b21f1c00264057a9ecbe","sup_fffcba04cfeceac91cd5"],"title":"perfective form makes knowing feel already closed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:3","qac_refs":["101:10:2:1","101:10:2:2"],"status":"accepted"}},{"anchor_refs":["101:10:3"],"branch_refs":[],"candidate_id":"cand_04d85f4d4d4e3b36b389","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000469","root_000473"],"scope":"focus_ayah","source_local_id":"101:10:3:same-surah-formula-echo","source_type":"word_analysis","support_ids":["sup_1de77d58d2a19f03c673","sup_b21f1c00264057a9ecbe"],"title":"formula echoes 101:3","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:3","qac_refs":["101:10:2:1","101:10:2:2"],"status":"accepted"}},{"anchor_refs":["101:10:3"],"branch_refs":[],"candidate_id":"cand_0f21e0d2f75348f5a47c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000469","root_000473"],"scope":"focus_ayah","source_local_id":"101:10:3:sound-closure","source_type":"word_analysis","support_ids":["sup_b21f1c00264057a9ecbe","sup_fbe65646e05f36791b3b"],"title":"length and final stop shape the sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:3","qac_refs":["101:10:2:1","101:10:2:2"],"status":"accepted"}},{"anchor_refs":["101:10:3"],"branch_refs":[],"candidate_id":"cand_69ceaaa9e0ef3615c78d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000469","root_000473"],"scope":"focus_ayah","source_local_id":"101:10:3:unidentified-subject-cause","source_type":"word_analysis","support_ids":["sup_09b1cf5304c68f40feda","sup_b21f1c00264057a9ecbe"],"title":"unknown subject leaves the cause unnamed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:3","qac_refs":["101:10:2:1","101:10:2:2"],"status":"accepted"}},{"anchor_refs":["101:10:3"],"branch_refs":[],"candidate_id":"cand_b1af461fbca5223b1d7b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000469","root_000473"],"scope":"focus_ayah","source_local_id":"101:10:3:verbal-interruption","source_type":"word_analysis","support_ids":["sup_b167528b661a34c406aa","sup_b21f1c00264057a9ecbe"],"title":"verbal question interrupts nominal verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:3","qac_refs":["101:10:2:1","101:10:2:2"],"status":"accepted"}},{"anchor_refs":["101:10:4"],"branch_refs":[],"candidate_id":"cand_c097408cee7a68309459","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:10:4:deferral-within-formula","source_type":"word_analysis","support_ids":["sup_3dd7a46480ef7edef0f7","sup_fa22d5d57f509c3d1a41"],"title":"definition request becomes deferral","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:4","qac_refs":["101:10:3:1"],"status":"accepted"}},{"anchor_refs":["101:10:4"],"branch_refs":[],"candidate_id":"cand_d09954f20a6480043f19","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:10:4:fronted-predicate","source_type":"word_analysis","support_ids":["sup_6037e2ced91576e663fc","sup_fa22d5d57f509c3d1a41"],"title":"predicate-question precedes the pronoun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:4","qac_refs":["101:10:3:1"],"status":"accepted"}},{"anchor_refs":["101:10:4"],"branch_refs":[],"candidate_id":"cand_5c08e87e2e75bdbd47b5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:10:4:inner-essence-question","source_type":"word_analysis","support_ids":["sup_c83dfe9e037c721e5556","sup_fa22d5d57f509c3d1a41"],"title":"inner question asks what it is","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:4","qac_refs":["101:10:3:1"],"status":"accepted"}},{"anchor_refs":["101:10:4"],"branch_refs":[],"candidate_id":"cand_443645f2a31814e63c5d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:10:4:tighter-second-ma-echo","source_type":"word_analysis","support_ids":["sup_fa22d5d57f509c3d1a41","sup_fdfa39a4d5f41009ccb9"],"title":"second question-word tightens the first","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:4","qac_refs":["101:10:3:1"],"status":"accepted"}},{"anchor_refs":["101:10:5"],"branch_refs":[],"candidate_id":"cand_74c9587818b2bbf4a9c2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:10:5:backward-forward-sound-echo","source_type":"word_analysis","support_ids":["sup_176b826744c00152ff38","sup_c268f48b5d9639880f94"],"title":"sound binds 101:9, 101:10, and 101:11","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:5","qac_refs":["101:10:4:1"],"status":"accepted"}},{"anchor_refs":["101:10:5"],"branch_refs":[],"candidate_id":"cand_5a68e2a194b54d848ff6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:10:5:boundary-to-question","source_type":"word_analysis","support_ids":["sup_c268f48b5d9639880f94","sup_cf4ec64397176d55ee11"],"title":"fall depiction becomes knowledge challenge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:5","qac_refs":["101:10:4:1"],"status":"accepted"}},{"anchor_refs":["101:10:5"],"branch_refs":[],"candidate_id":"cand_73e59fe1444c87530f02","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:10:5:definite-feminine-pointer","source_type":"word_analysis","support_ids":["sup_c268f48b5d9639880f94","sup_ca3af5a74f1c371dc0d2"],"title":"definite pronoun points back while withholding definition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:5","qac_refs":["101:10:4:1"],"status":"accepted"}},{"anchor_refs":["101:10:5"],"branch_refs":[],"candidate_id":"cand_db5bcd54bac1010eb9a6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:10:5:nominal-mini-clause","source_type":"word_analysis","support_ids":["sup_0c6a7f569ab145f4a5ec","sup_c268f48b5d9639880f94"],"title":"verbless clause makes identity central","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:5","qac_refs":["101:10:4:1"],"status":"accepted"}},{"anchor_refs":["101:10:5"],"branch_refs":[],"candidate_id":"cand_9c1d10037c597fdc618a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:10:5:pausal-and-variant-closure","source_type":"word_analysis","support_ids":["sup_898b7fa2d259ab5a86b8","sup_c268f48b5d9639880f94"],"title":"pause and variants alter the closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:5","qac_refs":["101:10:4:1"],"status":"accepted"}},{"anchor_refs":["101:10:5"],"branch_refs":[],"candidate_id":"cand_d3a5be0313a1f284b8ad","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"101:10:5:unresolved-ayah-closure","source_type":"word_analysis","support_ids":["sup_4b47d03047fb9715d6b6","sup_c268f48b5d9639880f94"],"title":"ayah ends on pointer, not answer","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:10:5","qac_refs":["101:10:4:1"],"status":"accepted"}},{"anchor_refs":["101:10:2"],"branch_refs":[],"candidate_id":"cand_15b04ce488bc3b2b6273","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000469","root_000473"],"scope":"focus_ayah","source_local_id":"101:10:2:1","source_type":"qac_morpheme","support_ids":["sup_3933ef5dad2a62d3acf1"],"title":"QAC root occurrence: د ر ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["101:10"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:10","branch_refs":["root_000473/B001"],"candidate_id":"cand_a1af961842a53c169b45","commentary_obligation":"review","hft_ref":"hft_49b996bb2659b4c3b745","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_epistemic_threshold","source_type":"hft","support_ids":["sup_d613b8467aa18c1ab729"],"title":"b_epistemic_threshold","trust":"legacy_unbound"},{"anchor_refs":["101:10"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:10","branch_refs":["root_000473/B002","root_000473/B003","root_000473/B005"],"candidate_id":"cand_efcbcca786d919499e44","commentary_obligation":"review","hft_ref":"hft_7c17a2564f58ca021aa3","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_directed_concealed_encounter","source_type":"hft","support_ids":["sup_55b7cb70fd5c82518e5f"],"title":"b_directed_concealed_encounter","trust":"legacy_unbound"},{"anchor_refs":["101:10"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:10","branch_refs":["root_000469/B001","root_000473/B001"],"candidate_id":"cand_5d9699d27c78bce7443f","commentary_obligation":"review","hft_ref":"hft_959561c6689ffba2e45c","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_yielding_disclosure","source_type":"hft","support_ids":["sup_37b84b512f92b308db68"],"title":"b_yielding_disclosure","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَمَآ أَدْرَىٰكَ مَا هِيَهْ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"101:10:1:1","qac_word_ref":"101:10:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:INTG|LEM:maA","morpheme_role":"STEM","pos":"INTG","qac_ref":"101:10:1:2","qac_word_ref":"101:10:1","root_ar":"","surface_ar":"مَآ"},{"lemma_ar":"أَدْرَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>adoraY`|ROOT:dry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"101:10:2:1","qac_word_ref":"101:10:2","root_ar":"د ر ي","surface_ar":"أَدْرَىٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"101:10:2:2","qac_word_ref":"101:10:2","root_ar":"","surface_ar":"كَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:INTG|LEM:maA","morpheme_role":"STEM","pos":"INTG","qac_ref":"101:10:3:1","qac_word_ref":"101:10:3","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|3FS","morpheme_role":"STEM","pos":"PRON","qac_ref":"101:10:4:1","qac_word_ref":"101:10:4","root_ar":"","surface_ar":"هِيَهْ"}],"word_analysis_qac_refs":[["101:10:1:1"],["101:10:1:2"],["101:10:2:1","101:10:2:2"],["101:10:3:1"],["101:10:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["101:10:1","101:10:2","101:10:3","101:10:4","101:10:5"]},"focus_surface_evidence":{"arabic_uthmani":"وَمَآ أَدْرَىٰكَ مَا هِيَهْ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"101:10:1:1","qac_word_ref":"101:10:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:INTG|LEM:maA","morpheme_role":"STEM","pos":"INTG","qac_ref":"101:10:1:2","qac_word_ref":"101:10:1","root_ar":"","surface_ar":"مَآ"},{"lemma_ar":"أَدْرَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>adoraY`|ROOT:dry|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"101:10:2:1","qac_word_ref":"101:10:2","root_ar":"د ر ي","surface_ar":"أَدْرَىٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"101:10:2:2","qac_word_ref":"101:10:2","root_ar":"","surface_ar":"كَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:INTG|LEM:maA","morpheme_role":"STEM","pos":"INTG","qac_ref":"101:10:3:1","qac_word_ref":"101:10:3","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|3FS","morpheme_role":"STEM","pos":"PRON","qac_ref":"101:10:4:1","qac_word_ref":"101:10:4","root_ar":"","surface_ar":"هِيَهْ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["101:10:1:1"],["101:10:1:2"],["101:10:2:1","101:10:2:2"],["101:10:3:1"],["101:10:4:1"]],"word_analysis_refs":["101:10:1","101:10:2","101:10:3","101:10:4","101:10:5"],"word_rows":[{"analysis_record_ref":"101:10:1","analytic_gloss_range_en":"opening conjunction that can coordinate with the prior verdict or resume into a fresh rhetorical question","analytic_root_gloss_range_en":null,"qac_refs":["101:10:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"101:10:2","analytic_gloss_range_en":"outer interrogative subject asking what could cause the addressee to know","analytic_root_gloss_range_en":null,"qac_refs":["101:10:1:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"مَآ","transliteration":"mā"}},{"analysis_record_ref":"101:10:3","analytic_gloss_range_en":"Form IV perfect verb meaning made you know or caused you to perceive, with the addressee encoded as object","analytic_root_gloss_range_en":"locally selected knowing, awareness, and causing-to-know branch; wider root branches such as raiding, hunting concealment, sharp implements, targets, or tactful handling are not locally active","qac_refs":["101:10:2:1","101:10:2:2"],"root":{"arabic":"د ر ي","transliteration":"d-r-y"},"surface":{"arabic":"أَدْرَىٰكَ","transliteration":"adrāka"}},{"analysis_record_ref":"101:10:4","analytic_gloss_range_en":"inner interrogative predicate asking what the pronoun's referent is","analytic_root_gloss_range_en":null,"qac_refs":["101:10:3:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"مَا","transliteration":"mā"}},{"analysis_record_ref":"101:10:5","analytic_gloss_range_en":"third-person feminine singular pronoun with pausal ending, pointing back to the preceding feminine referent while withholding its explanation","analytic_root_gloss_range_en":null,"qac_refs":["101:10:4:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"هِيَهْ","transliteration":"hiyah"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["101:10"],"branch_refs":["root_000473/B001"],"candidate_id":"cand_a1af961842a53c169b45","evidence_scope":"focus_ayah","hft_ref":"hft_49b996bb2659b4c3b745","item_id":"b_epistemic_threshold","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_epistemic_threshold","support_id":"sup_d613b8467aa18c1ab729"},{"anchor_refs":["101:10"],"branch_refs":["root_000473/B002","root_000473/B003","root_000473/B005"],"candidate_id":"cand_efcbcca786d919499e44","evidence_scope":"focus_ayah","hft_ref":"hft_7c17a2564f58ca021aa3","item_id":"b_directed_concealed_encounter","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_directed_concealed_encounter","support_id":"sup_55b7cb70fd5c82518e5f"},{"anchor_refs":["101:10"],"branch_refs":["root_000469/B001","root_000473/B001"],"candidate_id":"cand_5d9699d27c78bce7443f","evidence_scope":"focus_ayah","hft_ref":"hft_959561c6689ffba2e45c","item_id":"b_yielding_disclosure","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_yielding_disclosure","support_id":"sup_37b84b512f92b308db68"}],"diagnostics":[],"lane_counts":{"global":7,"macro":7,"micro":3},"packet_summary":{"ayah_count":11,"focus_ref":"101:10","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["101:1","101:2","101:3","101:4","101:5","101:6","101:7","101:8","101:9","101:10","101:11"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"101:10","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":7,"source_present":true,"structured_insight_count":10,"unstructured_record_count":0},"identity":{"ayah_ref":"101:10","lane":"micro","linguistic_source_ref":"101:10","surface_ref":"101:10","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"101:10","target_tokens":[["Ve",["101:10:1"]],["onun",["101:10:4"]],["ne",["101:10:3"]],["olduğunu",["101:10:3","101:10:4"]],["sana",["101:10:2"]],["ne",["101:10:1"]],["bildirdi",["101:10:2"]]],"text":"Ve onun ne olduğunu sana ne bildirdi?"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":11,"id":"s101-p01-001-011","label":"Whole surah","number":1,"refs":["101:1","101:2","101:3","101:4","101:5","101:6","101:7","101:8","101:9","101:10","101:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:3:unidentified-subject-cause","source_type":"word_analysis","support_id":"sup_09b1cf5304c68f40feda","text":"{\"blocking_evidence\":null,\"headline\":\"unknown subject leaves the cause unnamed\",\"reader_payoff\":\"The reader notices that the grammar supplies a subject for the verb while withholding any named cause of knowledge.\",\"reason\":\"Attachment evidence marks the preceding {{ar:مَآ}} ({{tr:mā}}) as the subject of the verb, so the syntactic slot is present but interrogative and unidentified.\",\"representative_source_ids\":[\"QG-c338ce5b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:5:nominal-mini-clause","source_type":"word_analysis","support_id":"sup_0c6a7f569ab145f4a5ec","text":"{\"blocking_evidence\":null,\"headline\":\"verbless clause makes identity central\",\"reader_payoff\":\"The reader notices that the embedded question is a compact nominal clause about identity, not an event or action.\",\"reason\":\"Attachment evidence marks {{ar:مَا هِيَهْ}} ({{tr:mā hiyah}}) as a nominal embedded question with predication between the interrogative and pronoun.\",\"representative_source_ids\":[\"QT-d5856fae\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:5:backward-forward-sound-echo","source_type":"word_analysis","support_id":"sup_176b826744c00152ff38","text":"{\"blocking_evidence\":null,\"headline\":\"sound binds 101:9, 101:10, and 101:11\",\"reader_payoff\":\"The reader notices that the pronoun's sound recalls the prior abyss-word in 101:9 and leans into the following answer in 101:11.\",\"reason\":\"The surface form of {{ar:هِيَهْ}} ({{tr:hiyah}}) supports the local sound observation, and translation support ties the pronoun across both neighboring ayahs.\",\"representative_source_ids\":[\"QE-6db90514\",\"QP-1af316d0\",\"QP-c04c551e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:3:same-surah-formula-echo","source_type":"word_analysis","support_id":"sup_1de77d58d2a19f03c673","text":"{\"blocking_evidence\":null,\"headline\":\"formula echoes 101:3\",\"reader_payoff\":\"The reader notices that the same formula from 101:3 frames both the opening event and the later consequence as exceeding ordinary knowing.\",\"reason\":\"Attachment cross-reference evidence marks the current formula as repeating the rhetorical knowledge formula first occurring in this chunk at 101:3.\",\"representative_source_ids\":[\"QE-7bc540e7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:2","source_type":"word_analysis","support_id":"sup_2320e3349c064e8ab53d","text":"{\"gloss_range\":\"outer interrogative subject asking what could cause the addressee to know\",\"prose\":\"{{ar:مَآ}} ({{tr:mā}}) is the outer question-word, functioning as the subject of {{ar:أَدْرَىٰكَ}} ({{tr:adrāka}}). It does not ask for the identity of the abyss yet; it first asks what source, cause, or informant could make the addressee know. Because the verb is causative, this fronted interrogative places the missing cause of knowledge before the act of knowing itself. The formulaic question is therefore not a request for information but an epistemic challenge: what adequate source could convey the reality named in 101:9? The elongated written and recited shape gives the opening question a stretched onset, and the later {{ar:مَا}} ({{tr:mā}}) reprises it as a second step, moving from the means of knowledge to the nature of the referent.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مَآ}} ({{tr:mā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:1:same-surah-formula-return","source_type":"word_analysis","support_id":"sup_38efc5d7c57e18143918","text":"{\"blocking_evidence\":null,\"headline\":\"opening formula returns from 101:3\",\"reader_payoff\":\"The reader notices that the same knowing-question frame from 101:3 returns, now redirected from the surah's named event to its consequence.\",\"reason\":\"Attachment cross-reference evidence explicitly marks {{ar:وَمَآ أَدْرَىٰكَ مَا}} ({{tr:wa-mā adrāka mā}}) as repeating the rhetorical knowledge formula first occurring in this chunk at 101:3.\",\"representative_source_ids\":[\"QE-a2526772\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"101:10:2:1","source_type":"qac_morpheme","support_id":"sup_3933ef5dad2a62d3acf1","text":"{\"lemma_ar\":\"أَدْرَىٰ\",\"morph_features\":\"STEM|POS:V|PERF|(IV)|LEM:>adoraY`|ROOT:dry|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"101:10:2:1\",\"qac_word_ref\":\"101:10:2\",\"root_ar\":\"د ر ي\",\"surface_ar\":\"أَدْرَىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:4:deferral-within-formula","source_type":"word_analysis","support_id":"sup_3dd7a46480ef7edef0f7","text":"{\"blocking_evidence\":null,\"headline\":\"definition request becomes deferral\",\"reader_payoff\":\"The reader notices that the apparent definition request is delayed by the formula and held open until 101:11.\",\"reason\":\"Translation support recommends reading the window through 101:11, where the answer follows, so the inner question should be preserved as deferral rather than immediately resolved.\",\"representative_source_ids\":[\"QI-c212f7c4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:1:boundary-handoff","source_type":"word_analysis","support_id":"sup_41c5c9a6de2faaad1916","text":"{\"blocking_evidence\":null,\"headline\":\"causal closure becomes open question\",\"reader_payoff\":\"The reader notices the boundary shift from a consequence stated in 101:9 to a looser conjunction that lets that consequence become a question.\",\"reason\":\"The prior boundary is carried by a causal particle in 101:9, while this ayah opens with {{ar:وَ}} ({{tr:wa}}), and translation support warns that the formula should not be flattened into explanation.\",\"representative_source_ids\":[\"QT-9731c16d\",\"QB-f2f4f899\",\"QT-87396e52\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:5:unresolved-ayah-closure","source_type":"word_analysis","support_id":"sup_4b47d03047fb9715d6b6","text":"{\"blocking_evidence\":null,\"headline\":\"ayah ends on pointer, not answer\",\"reader_payoff\":\"The reader notices that ayah 10 closes on a pronoun awaiting specification, forcing the answer-dependency toward 101:11.\",\"reason\":\"Attachment translation support explicitly relates {{ar:هِيَهْ}} ({{tr:hiyah}}) to the preceding referent in 101:9 and the following answer in 101:11.\",\"representative_source_ids\":[\"QT-60ac761f\",\"QE-c2b911e0\",\"QB-94d6f3d4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:2:paired-ma-setup","source_type":"word_analysis","support_id":"sup_56ef4e8253200b144476","text":"{\"blocking_evidence\":null,\"headline\":\"first question-word sets up the second\",\"reader_payoff\":\"The reader notices that the two question-words form a structural and acoustic pair, not decorative repetition.\",\"reason\":\"Attachment evidence separates the outer verbal question from the embedded nominal question, while the surface repetition binds the two interrogatives locally.\",\"representative_source_ids\":[\"QE-1d63d13c\",\"QP-8645d9a3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:3:double-ma-hinge","source_type":"word_analysis","support_id":"sup_56f8e36edeaeabdf4b1b","text":"{\"blocking_evidence\":null,\"headline\":\"verb hinges between two questions\",\"reader_payoff\":\"The reader notices that the verb sits between the outer source-question and inner essence-question, making the nested progression audible and grammatical.\",\"reason\":\"The local word order places {{ar:أَدْرَىٰكَ}} ({{tr:adrāka}}) between the two interrogatives, with attachment evidence distinguishing the outer verbal question from the embedded content question.\",\"representative_source_ids\":[\"QT-bb7282dc\",\"QE-caf1991e\",\"QP-7157b172\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:4:fronted-predicate","source_type":"word_analysis","support_id":"sup_6037e2ced91576e663fc","text":"{\"blocking_evidence\":null,\"headline\":\"predicate-question precedes the pronoun\",\"reader_payoff\":\"The reader notices that the demand for essence comes before the pronoun pointer, so definition is sought before reference settles.\",\"reason\":\"Attachment evidence marks the second {{ar:مَا}} ({{tr:mā}}) in predication with {{ar:هِيَهْ}} ({{tr:hiyah}}), and the surface order places the interrogative first.\",\"representative_source_ids\":[\"QT-aff914ce\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:2:outer-interrogative-subject","source_type":"word_analysis","support_id":"sup_62fdcb90ecf7ab5f3a6f","text":"{\"blocking_evidence\":null,\"headline\":\"outer question asks for the knowledge-source\",\"reader_payoff\":\"The reader notices that the ayah first questions the source that could make knowledge possible, before asking what the referent is.\",\"reason\":\"QAC and attachment evidence identify the first {{ar:مَآ}} ({{tr:mā}}) as the subject of {{ar:أَدْرَىٰكَ}} ({{tr:adrāka}}), which governs the embedded content question.\",\"representative_source_ids\":[\"QG-4da709c6\",\"QS-fe7c20fc\",\"QT-e9fc6cf6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:3:forward-answer-gap","source_type":"word_analysis","support_id":"sup_7517be3a2544695e7810","text":"{\"blocking_evidence\":null,\"headline\":\"knowledge gap points to 101:11\",\"reader_payoff\":\"The reader notices that the verb opens a knowledge gap that the next ayah must answer in 101:11.\",\"reason\":\"Translation support explicitly warns that the question should be read with 101:9 and 101:11, because the answer follows after this ayah.\",\"representative_source_ids\":[\"QB-5488724c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:5:pausal-and-variant-closure","source_type":"word_analysis","support_id":"sup_898b7fa2d259ab5a86b8","text":"{\"blocking_evidence\":null,\"headline\":\"pause and variants alter the closure\",\"reader_payoff\":\"The reader notices that the pronoun's referent stays the same while the recited ending can close as breath, openness, or clipped suspension.\",\"reason\":\"QAC marks {{ar:هِيَهْ}} ({{tr:hiyah}}) with pausal {{ar:هْ}} ({{tr:h}}), while translation support says the answer follows in 101:11, so the topic is limited to ayah closure and not treated as a surah-final ending.\",\"representative_source_ids\":[\"QF-b22ccc8d\",\"QF-fd7009e7\",\"QY-2e2a1c5d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:3:negative-epistemic-force","source_type":"word_analysis","support_id":"sup_901e41fbd90bf28f40a8","text":"{\"blocking_evidence\":null,\"headline\":\"knowing verb argues impossibility\",\"reader_payoff\":\"The reader notices that the formula uses the language of making known to dramatize the absence of any adequate knowing.\",\"reason\":\"The attachment evidence identifies the double-question construction, and translation support warns against reducing it to plain explanation.\",\"representative_source_ids\":[\"QS-f069ccfd\",\"QI-7c8e9578\",\"QI-1228859e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:2:rhetorical-epistemic-challenge","source_type":"word_analysis","support_id":"sup_95d51eb7b39f894aeca6","text":"{\"blocking_evidence\":null,\"headline\":\"question form exposes no adequate answer\",\"reader_payoff\":\"The reader notices that the interrogative keeps its question form while functioning as a challenge to ordinary access to knowledge.\",\"reason\":\"The local formula and translation support require preserving the compressed question rather than turning it into a flat explanatory statement.\",\"representative_source_ids\":[\"MG-9939fe47\",\"QI-4780d1a7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:3:addressee-shift","source_type":"word_analysis","support_id":"sup_9c36c532c06979c4756c","text":"{\"blocking_evidence\":null,\"headline\":\"suffix turns verdict into direct address\",\"reader_payoff\":\"The reader notices the shift from a third-person judgment scene to a direct second-person confrontation with the listener's knowledge limit.\",\"reason\":\"QAC identifies the object suffix as second-person masculine singular, and attachment cross-reference evidence treats it as the discourse addressee.\",\"representative_source_ids\":[\"QF-3400d92a\",\"QI-11f6bf70\",\"QB-5691b034\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:3:verbal-interruption","source_type":"word_analysis","support_id":"sup_b167528b661a34c406aa","text":"{\"blocking_evidence\":null,\"headline\":\"verbal question interrupts nominal verdict\",\"reader_payoff\":\"The reader notices the move from a static nominal verdict into a staged verbal event of knowing addressed to the listener.\",\"reason\":\"Attachment evidence marks the current clause as a verbal formula after the prior verdict, preserving the structural shift.\",\"representative_source_ids\":[\"QT-0f644e97\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:3","source_type":"word_analysis","support_id":"sup_b21f1c00264057a9ecbe","text":"{\"gloss_range\":\"Form IV perfect verb meaning made you know or caused you to perceive, with the addressee encoded as object\",\"prose\":\"{{ar:أَدْرَىٰكَ}} ({{tr:adrāka}}) is the hinge of the double question. Its Form IV shape asks what could cause the addressee to know, not whether the addressee already knows by private capacity. The attached {{ar:كَ}} ({{tr:ka}}) makes the listener the direct recipient of that attempted knowledge, while the following {{ar:مَا هِيَهْ}} ({{tr:mā hiyah}}) supplies the content that would have to be made known. The perfective form gives the knowledge-event a closed feel: the possibility sounds already tested and unavailable, as though even later encounter would not turn this reality into adequate knowledge. Within the local root range, the active branch is knowing, awareness, and making known; broader dictionary branches for attack, stalking, sharp implements, practice targets, or tactful social handling are only excluded background. The surviving pressure is sharper than a dictionary gloss, though: knowledge would have to be conveyed, perceived, or gained by contact, and the ayah makes that very cause vanish. Structurally, the verb turns the prior third-person verdict into a second-person knowledge challenge, sits between {{ar:مَآ}} ({{tr:mā}}) and {{ar:مَا}} ({{tr:mā}}), echoes the formula of 101:3, and opens the gap that 101:11 answers.\",\"root_display\":\"{{ar:د ر ي}} ({{tr:d-r-y}})\",\"root_gloss_range\":\"locally selected knowing, awareness, and causing-to-know branch; wider root branches such as raiding, hunting concealment, sharp implements, targets, or tactful handling are not locally active\",\"surface_display\":\"{{ar:أَدْرَىٰكَ}} ({{tr:adrāka}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:1:continuation-resumption","source_type":"word_analysis","support_id":"sup_b4e522cdb38fb4a26acc","text":"{\"blocking_evidence\":null,\"headline\":\"continuation and resumption stay live\",\"reader_payoff\":\"The reader notices that the ayah both continues the judgment of 101:9 and reopens it as a direct rhetorical challenge.\",\"reason\":\"QAC permits both coordination and resumptive reading for {{ar:وَ}} ({{tr:wa}}), while attachment evidence marks the ayah as the outer question of the formula and cross-reference evidence ties it to the prior discourse.\",\"representative_source_ids\":[\"QG-1e53ae09\",\"QG-26ea2649\",\"QS-c029eb7a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:3:knowledge-branch-narrowed","source_type":"word_analysis","support_id":"sup_b930a013ed5fa6d8c881","text":"{\"blocking_evidence\":null,\"headline\":\"root range narrows to knowing and making known\",\"reader_payoff\":\"The reader notices that the verb carries mediated and experiential knowing as the live pressure, while unrelated root branches do not enter the local sense.\",\"reason\":\"V4 supports the accepted knowing and causing-to-know branch for the local lexical unit, but its other branches for setting upon, hunting concealment, implements, targets, and tactful handling are not activated by the local Form IV formula.\",\"representative_source_ids\":[\"QS-04ea2a1d\",\"QS-eafaa2a6\",\"MF-206ed391\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:5","source_type":"word_analysis","support_id":"sup_c268f48b5d9639880f94","text":"{\"gloss_range\":\"third-person feminine singular pronoun with pausal ending, pointing back to the preceding feminine referent while withholding its explanation\",\"prose\":\"{{ar:هِيَهْ}} ({{tr:hiyah}}) closes the ayah on a definite feminine pronoun, not on the answer. The grammar points back strongly to the preceding feminine {{ar:هَاوِيَةٌۭ}} ({{tr:hāwiyah}}) in 101:9, but the word does not rename or define it; it says \\\"it/she\\\" with enough precision to bind the boundary and enough withholding to make 101:11 necessary. That is controlled uncertainty rather than failed reference. The compact clause {{ar:مَا هِيَهْ}} ({{tr:mā hiyah}}) has no overt verb, so the issue is identity itself. The pausal {{ar:هْ}} ({{tr:h}}) makes stopping visible in the recited form, and accepted ending variants preserve the pronoun while changing the closure into breath, open vowel, or clipped suspension. The sound also binds backward and forward: {{ar:هِيَهْ}} ({{tr:hiyah}}) echoes the breathy shape of {{ar:هَاوِيَةٌۭ}} ({{tr:hāwiyah}}) in 101:9 and anticipates {{ar:نَارٌ حَامِيَةٌۢ}} ({{tr:nārun ḥāmiyah}}) in 101:11.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:هِيَهْ}} ({{tr:hiyah}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:4:inner-essence-question","source_type":"word_analysis","support_id":"sup_c83dfe9e037c721e5556","text":"{\"blocking_evidence\":null,\"headline\":\"inner question asks what it is\",\"reader_payoff\":\"The reader notices the move from asking what could make knowledge possible to asking what the referent itself is.\",\"reason\":\"QAC identifies the second {{ar:مَا}} ({{tr:mā}}) as the inner interrogative, and attachment evidence marks {{ar:مَا هِيَهْ}} ({{tr:mā hiyah}}) as the embedded question governed by the verb.\",\"representative_source_ids\":[\"QG-255c7ed0\",\"QS-fdeea8bd\",\"MG-3471cac0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:5:definite-feminine-pointer","source_type":"word_analysis","support_id":"sup_ca3af5a74f1c371dc0d2","text":"{\"blocking_evidence\":null,\"headline\":\"definite pronoun points back while withholding definition\",\"reader_payoff\":\"The reader notices that the pronoun is grammatically precise enough to point back to 101:9, while still withholding the reality it points to.\",\"reason\":\"Attachment evidence strongly licenses {{ar:هِيَهْ}} ({{tr:hiyah}}) as resuming {{ar:هَاوِيَةٌۭ}} ({{tr:hāwiyah}}) from 101:9, so broader ambiguity claims are narrowed to controlled withholding rather than an unsettled antecedent.\",\"representative_source_ids\":[\"QG-1c8309e6\",\"QG-c65b4797\",\"QS-e589a81e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:1:wa-ma-sound-launch","source_type":"word_analysis","support_id":"sup_ce58258a41baf4cd3fa5","text":"{\"blocking_evidence\":null,\"headline\":\"short connector opens into long question\",\"reader_payoff\":\"The reader notices the audible expansion from a brief connector into the lengthened opening question-word.\",\"reason\":\"The surface sequence places short {{ar:وَ}} ({{tr:wa}}) immediately before elongated {{ar:مَآ}} ({{tr:mā}}), supporting the local sound observation without making it govern grammar.\",\"representative_source_ids\":[\"QP-392b0df9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:3:form-iv-causative-frame","source_type":"word_analysis","support_id":"sup_cedc9c2268a2bd63d06d","text":"{\"blocking_evidence\":null,\"headline\":\"causative verb asks what could make you know\",\"reader_payoff\":\"The reader notices that the issue is an absent cause that could deliver knowledge to the addressee, not the addressee's unaided awareness.\",\"reason\":\"QAC and attachment evidence identify {{ar:أَدْرَىٰكَ}} ({{tr:adrāka}}) as Form IV with a second-person object suffix and a clausal complement, while V4 includes the accepted sense of making someone know.\",\"representative_source_ids\":[\"QG-ba4c19c4\",\"QF-792ed088\",\"QY-f9073c6b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:5:boundary-to-question","source_type":"word_analysis","support_id":"sup_cf4ec64397176d55ee11","text":"{\"blocking_evidence\":null,\"headline\":\"fall depiction becomes knowledge challenge\",\"reader_payoff\":\"The reader notices that the prior consequence becomes a precise pronoun inside a question, shifting from depicted fall to the listener's inability to define it.\",\"reason\":\"The boundary pressure survives, but attachment evidence narrows it: the pronoun chain strongly resumes {{ar:هَاوِيَةٌۭ}} ({{tr:hāwiyah}}) from 101:9 rather than leaving the antecedent equally split.\",\"representative_source_ids\":[\"QB-3788fc3f\",\"QB-c80ad14a\",\"QY-e1fa51f0\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:2:lengthened-onset","source_type":"word_analysis","support_id":"sup_d8dfaec9bd4aa720fde3","text":"{\"blocking_evidence\":null,\"headline\":\"lengthened opening makes the question stretch\",\"reader_payoff\":\"The reader notices that the first question-word opens with a lengthened sound before the knowledge verb arrives.\",\"reason\":\"The surface form supplied by QAC is {{ar:مَآ}} ({{tr:mā}}), allowing the sound-shape observation as local phonetic payoff.\",\"representative_source_ids\":[\"QF-0afc84c0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:3:blocked-reach-encounter","source_type":"word_analysis","support_id":"sup_d97d2b6e55be85ea676f","text":"{\"blocking_evidence\":null,\"headline\":\"knowledge as encounter cannot reach the abyss\",\"reader_payoff\":\"The reader notices the image of knowledge needing to arrive by contact or encounter, only to fail before the abyss named in 101:9.\",\"reason\":\"The local sense remains knowing and making known, so reach or encounter language is retained as a constrained payoff of the CRITICAL rows rather than as a separate activated dictionary branch.\",\"representative_source_ids\":[\"QS-02ef6fe6\",\"QS-97f95d4e\",\"QB-e414d39b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:1","source_type":"word_analysis","support_id":"sup_dbe4464e28d3923ae2e6","text":"{\"gloss_range\":\"opening conjunction that can coordinate with the prior verdict or resume into a fresh rhetorical question\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) makes the ayah begin as both continuation and renewed address. As coordination, it keeps the question tied to the preceding verdict in 101:9, where the consequence has just been named; as resumption, it lets the discourse step out of declarative judgment into a fresh rhetorical challenge. That double availability is the payoff of the small connector: the abyss is not left as a settled label, but immediately reopened as something the listener cannot grasp. The particle also helps relaunch the same {{ar:وَ مَآ أَدْرَىٰكَ}} ({{tr:wa mā adrāka}}) formula heard earlier in 101:3, so the surah's opening unknowability returns at the boundary of its consequence. Sound-wise, the short connector releases into the long first question-word, moving from a brief link into a widened inquiry.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:4","source_type":"word_analysis","support_id":"sup_fa22d5d57f509c3d1a41","text":"{\"gloss_range\":\"inner interrogative predicate asking what the pronoun's referent is\",\"prose\":\"{{ar:مَا}} ({{tr:mā}}) is the inner interrogative, the predicate of the compact nominal question {{ar:مَا هِيَهْ}} ({{tr:mā hiyah}}). After the first {{ar:مَآ}} ({{tr:mā}}) asks what could make knowledge possible, this second one asks what the referent actually is. That shift is not flat repetition: the ayah moves from epistemic access to essence and identity. Because the inner question is embedded under {{ar:أَدْرَىٰكَ}} ({{tr:adrāka}}), it is already framed by the absence of an adequate cause of knowledge. Its fronted position before the pronoun makes the search for essence arrive before the pointer can settle, and its open vowel renews the cadence that carries the question toward the pause.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مَا}} ({{tr:mā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:3:sound-closure","source_type":"word_analysis","support_id":"sup_fbe65646e05f36791b3b","text":"{\"blocking_evidence\":null,\"headline\":\"length and final stop shape the sound\",\"reader_payoff\":\"The reader notices the verb's long sound closing sharply on the addressed suffix before the ayah returns to open vowels.\",\"reason\":\"The surface form places a long verbal core before the final {{ar:كَ}} ({{tr:ka}}) suffix, supporting a local sound-shape observation without changing grammar.\",\"representative_source_ids\":[\"QF-c19830e8\",\"QP-7b38322b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:4:tighter-second-ma-echo","source_type":"word_analysis","support_id":"sup_fdfa39a4d5f41009ccb9","text":"{\"blocking_evidence\":null,\"headline\":\"second question-word tightens the first\",\"reader_payoff\":\"The reader notices that the repeated question-word narrows the inquiry from access to identity while keeping the open-vowel cadence alive.\",\"reason\":\"The two interrogatives occupy different clauses in attachment evidence but share the same local sound and surface pattern.\",\"representative_source_ids\":[\"QE-ec830398\",\"QP-875ef77b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:10:3:perfective-closure","source_type":"word_analysis","support_id":"sup_fffcba04cfeceac91cd5","text":"{\"blocking_evidence\":null,\"headline\":\"perfective form makes knowing feel already closed\",\"reader_payoff\":\"The reader notices that the perfective formula makes the possibility of knowing feel already tested and unavailable.\",\"reason\":\"QAC marks the verb as perfect, and contextual profiles show this exact root-form belongs to repeated formulaic uses with clausal complements.\",\"representative_source_ids\":[\"QG-a76a9734\",\"QI-9102defe\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَمَآ أَدْرَىٰكَ مَا هِيَهْ","ayah_ref":"101:10"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000473/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000473","role":"Knowing and causing another to know supply the literal epistemic act, while the causative address makes disclosure the mechanism.","root":"د ر ي","source_ref":"101:10","source_word_indices":["2"]}],"changed_reading":{"after":"A staged threshold asking what can cause the addressee to know an intentionally unresolved referent.","before":"A direct request to identify an unknown thing."},"confidence":"strong","focus_anchor":"The causative أَدْرَىٰكَ inside وَمَا أَدْرَىٰكَ مَا هِيَهْ, with the referent held in the feminine pronoun هِيَهْ.","mechanism":"The knowing branch and doubled interrogative stage a threshold: the address does not merely request a label but asks what agency could bring the hearer into knowledge while identity remains withheld.","model_id":"b_epistemic_threshold"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_epistemic_threshold","source_type":"hft","support_id":"sup_d613b8467aa18c1ab729","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَمَآ أَدْرَىٰكَ مَا هِيَهْ","ayah_ref":"101:10"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000473/B002","root_000473/B003","root_000473/B005"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000473","role":"Aiming at and setting upon something supplies directed attention as the question's functional motion.","root":"د ر ي","source_ref":"101:10","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000473","role":"Concealment while stalking supplies the screened visibility of the referent held behind هِيَهْ.","root":"د ر ي","source_ref":"101:10","source_word_indices":["2"]},{"branch_id":"B005","mapped_root_id":"root_000473","role":"A target used for learning a thrust supplies the exploratory sense that the address trains perception by fixing an endpoint.","root":"د ر ي","source_ref":"101:10","source_word_indices":["2"]}],"changed_reading":{"after":"The utterance sights and trains the hearer upon a deliberately concealed target whose identity must be encountered.","before":"Knowledge is passively received as information."},"confidence":"exploratory","focus_anchor":"أَدْرَىٰكَ directs the addressee through the second مَا toward an object still concealed behind هِيَهْ.","mechanism":"The aiming, stalking, and practice-target branches let cognition coexist with directed encounter: attention is aimed and trained upon a screened object rather than handed a detached definition.","model_id":"b_directed_concealed_encounter"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_directed_concealed_encounter","source_type":"hft","support_id":"sup_55b7cb70fd5c82518e5f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَمَآ أَدْرَىٰكَ مَا هِيَهْ","ayah_ref":"101:10"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000469/B001","root_000473/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000473","role":"Knowing supplies the semantic event that the model treats as disclosure.","root":"د ر ي","source_ref":"101:10","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000469","role":"Abundant yielding from a source supplies the form-distant image of knowledge issuing after deliberate withholding.","root":"د ر ي","source_ref":"101:10","source_word_indices":["2"]}],"changed_reading":{"after":"The question opens a withheld source from which knowledge is about to issue in a concentrated release.","before":"The speaker asks for a fact."},"confidence":"exploratory","focus_anchor":"The supplied split mapping of the focus root remains attached to أَدْرَىٰكَ at word 2.","mechanism":"Alongside ordinary knowing, the mapped image of abundant issue from a source makes disclosure feel like released pressure: the question withholds a source so that knowledge can arrive as outflow rather than static definition.","model_id":"b_yielding_disclosure"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_yielding_disclosure","source_type":"hft","support_id":"sup_37b84b512f92b308db68","trust":"legacy_unbound"}]}
</lane_packet_json>
