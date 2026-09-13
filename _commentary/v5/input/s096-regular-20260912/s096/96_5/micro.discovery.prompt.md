# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **96:5**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s096-regular-20260912/s096/96_5/micro.discovery.json` and modify nothing
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
  "ayah_ref": "96:5",
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
{"branch_registry":[{"boundary":"Dal, insan türünü ve onun tekil ya da toplu üyelerini kapsar; yakınlık duygusunu, duyusal algıyı ve insana dönük yanı kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"96:5:2:2","qac_word_ref":"96:5:2","surface_ar":"إِنسَٰنَ"}],"gloss":"insan türü ve bu türden bir kişi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan türünü, insanların oluşturduğu topluluğu veya bu türün tek bir üyesini görünmeyen varlıklar sınıfının karşısında adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlandırmanın insanların duyularla görünür oluşuna bağlanması, anlamın özü değil kökene ilişkin bir açıklamadır."}}],"root_ar":"ء ن س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsanları bir tür veya topluluk olarak anlatırken de bu türün tek bir üyesini belirtirken de kullanılabilir.","boundary_detail":"Dal, insan türünü ve onun tekil ya da toplu üyelerini kapsar; yakınlık duygusunu, duyusal algıyı ve insana dönük yanı kapsamaz.","branch_image_ar":"ظهور الإنسان المخالف للتوحش والجن","concept_gloss":"insan türü ve bu türden bir kişi","contextual_glosses":[{"applicability":"Türün üyeleri topluca veya görünmeyen varlıklar sınıfının karşıtı olarak anıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan türünün toplu olarak adlandırılmasını açık ve doğal biçimde korur."},"facet_ids":["F001"],"text":"insanlar","usage_role":"general"},{"applicability":"Bağlam türün tek bir üyesini veya herhangi bir kimseyi gösterdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan topluluğundan tek bir üyenin belirtilmesini korur."},"facet_ids":["F001"],"text":"bir kişi","usage_role":"contextual"}],"definition":"Görünmeyen varlıklar sınıfının karşısında yer alan insan türünü, bu türün topluluğunu ya da tek bir üyesini belirtir. İnsanların görünür oluşu, bu adlandırma için aktarılan bir gerekçedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan türünü, insanların oluşturduğu topluluğu veya bu türün tek bir üyesini görünmeyen varlıklar sınıfının karşısında adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Adlandırmanın insanların duyularla görünür oluşuna bağlanması, anlamın özü değil kökene ilişkin bir açıklamadır."}],"identity_rationale":"Kaynak ifadesi, görünmeyen varlıklar sınıfının karşısındaki insan türünü, bu türün topluluğunu ve tek bir üyesini birlikte gösterir. Görünür olma açıklaması adlandırma gerekçesidir; insan olmanın kurucu tanımı değildir. Evde kimsenin bulunmadığını bildiren kalıp ise dal çekirdeğine genellenemez ve yalnızca kendi sözcüksel biriminde korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"insanlar; insan topluluğu"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"insan; insan türü"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"insan topluluğunun bir üyesi; insana veya insanlara ait"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"insanlar; insan toplulukları"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"insanlar; halk"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"evde hiç kimse yok"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"belirli bir ağızda insan ve onun çoğulu"}],"lexicalization_note":"Çıplak biçimlerdeki insan ve insan topluluğu anlamı dal çekirdeğidir; evde hiç kimse bulunmadığını anlatan kalıp ayrı tutulur ve çekirdeğe yeni bir genel anlam katmaz.","neighbor_coverage_note":"Bütün aday kartlar karşılaştırıldı. Yalnız insanı adlandırma sınırını yaratılmışlar kapsamından ve yakınlık duygusundan ayıran, okuyucu için en yararlı üç karşıtlık yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yer değiştirme yalnız insanı genel olarak adlandıran bağlamlarda mümkündür. Odak dalın görünmeyen varlıklarla sınıf karşıtlığı, komşunun ise görünür beden yönü kendi sınırında kalır.","focus_only":"Odak dal, insanları görünmeyen varlıklar sınıfının karşısında bir tür olarak kurar ve görünürlüğe dayalı bir adlandırma açıklaması taşır.","gloss":"insan türünü iki ayrı yönden adlandırma","neighbor_only":"Komşu dal, insanı görünür ten ve yaratılmış beden yönüyle adlandırır; tekil, çoğul, erkek ve kadın kapsamını özellikle öne çıkarır.","neighbor_ref":"root_000120/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da insanı hem tür hem bu türün üyesi olarak gösterebilir."},{"boundary_match":"partial","distinction":"Komşunun genel yaratılmışlar kapsamı odak dala taşınamaz; odak dal da yalnız insanları belirttiği için bütün yaratılmışların yerine kullanılamaz.","focus_only":"Odak dal yalnız insan türünü ve bu türün tekil ya da toplu üyelerini belirtir.","gloss":"insan türü ile bütün yaratılmışlar ayrımı","neighbor_only":"Komşu dal yeryüzündeki bütün yaratılmışları kapsayabilir ve bazı yorumlarda insanlarla görünmeyen varlıkları birlikte içerir.","neighbor_ref":"root_000061/B001","relation_type":"near_neighbor","shared_zone":"İnsanlar iki dalın gönderim alanında da bulunabilir."},{"boundary_match":"field_only","distinction":"Birinde insanın kim olduğu adlandırılır, diğerinde bir kişi ya da şey karşısındaki duygusal durum anlatılır; sıradan bağlamlarda birbirlerinin yerine geçmezler.","focus_only":"Odak dal insan türünü ve bu türün üyelerini adlandırır.","gloss":"insan adı ile yakınlık duygusu ayrımı","neighbor_only":"Komşu dal yabancılık ve ürkme duygusunun kalkmasını, yakınlık ve rahatlık oluşmasını anlatır.","neighbor_ref":"root_000059/B003","relation_type":"same_field","shared_zone":"Her iki dalda da insan, temel gönderim noktası veya deneyim sahibi olabilir."}],"source_phrase_ar":"الإنس خلاف الجن وسموا لظهورهم (maqayis;mufradat)؛ الإنس البشر والواحد إنسي والجمع أناسي (sihah)؛ الإنس جماعة الناس والأناسي جماع (tahdhib)","source_summary":"Aktarımlar, dalın insan türünü hem topluluk hem tek kişi olarak gösterebildiğinde ve görünmeyen varlıklar sınıfıyla karşıtlık kurduğunda birleşir. Görünürlük, ortak anlamdan çok adlandırmanın gerekçesi olarak sunulur.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الإنس والبشر والناس والأناسي والإنسان من حيث الجماعة أو الواحد، وما بالدار أنيس بمعنى أحد.","what_is_not_ar":"لا يدخل مجرد الاستئناس النفسي ولا الإيناس بمعنى الإبصار ولا الجانب الإنسي إلا بدليل."},"support_links":[]},{"boundary":"Dal duyusal olarak fark etmeyi ve belirtilen bağlamlardaki işitme, sezme ve bakıp araştırma kullanımlarını kapsar; yakınlık ve rahatlık duygusunu kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B002","candidate_links":[{"candidate_id":"cand_441a1b413958f88f8b7e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"96:5:2:2","qac_word_ref":"96:5:2","surface_ar":"إِنسَٰنَ"}],"gloss":"görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi gözle görerek fark etmeyi veya seçmeyi anlatır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli bir ses nesnesiyle kullanıldığında o sesi işitmeyi anlatır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kimsedeki olgunluk belirtisini bilip ayırt etmeyi veya kaygı veren bir durumu duyularla sezmeyi anlatabilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Çevreye bakıp dikkatle araştırarak birinin bulunup bulunmadığını anlamaya çalışma kullanımını taşır."}}],"root_ar":"ء ن س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın görme çekirdeğiyle birlikte yalnız belirtilen bağlamlarda ortaya çıkan işitme, sezme ve çevreyi araştırma uzantılarını topluca verir.","boundary_detail":"Dal duyusal olarak fark etmeyi ve belirtilen bağlamlardaki işitme, sezme ve bakıp araştırma kullanımlarını kapsar; yakınlık ve rahatlık duygusunu kapsamaz.","branch_image_ar":"إيناس الشيء برؤية أو إحساس أو سماع","concept_gloss":"görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma","contextual_glosses":[{"applicability":"Nesnenin gözle seçildiği veya görüldüğü temel kullanımda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gözle görme ve görüleni fark etme işlemlerini birlikte korur."},"facet_ids":["F001"],"text":"görüp fark etmek","usage_role":"general"},{"applicability":"Nesne açıkça bir ses olduğunda kullanılan bağlama bağlı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sesin kulakla algılanması biçimindeki özel kullanımı korur."},"facet_ids":["F002"],"text":"sesi işitmek","usage_role":"contextual"},{"applicability":"Bir kimsedeki olgunluk veya kaygı uyandıran durum gibi bir belirtinin ayırt edildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Duyusal belirtiden bir durumun varlığını anlayıp ayırt etmeyi korur."},"facet_ids":["F003"],"text":"belirtiyi sezmek","usage_role":"contextual"},{"applicability":"Çevreyi gözleyip birinin bulunup bulunmadığını anlamaya çalışma kullanımında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dikkatle bakma ile birini bulmaya yönelik araştırmayı birlikte korur."},"facet_ids":["F004"],"text":"bakıp araştırmak","usage_role":"explanatory"}],"definition":"Bir şeyi görüp fark etmeyi anlatır. Belirli kullanımlarda bir sesi işitmeye, bir kimsedeki olgunluk belirtisini ya da kaygı veren bir durumu sezmeye ve çevreye bakarak birinin bulunup bulunmadığını araştırmaya uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi gözle görerek fark etmeyi veya seçmeyi anlatır."},{"facet_id":"F002","role":"extension","statement":"Belirli bir ses nesnesiyle kullanıldığında o sesi işitmeyi anlatır."},{"facet_id":"F003","role":"extension","statement":"Bir kimsedeki olgunluk belirtisini bilip ayırt etmeyi veya kaygı veren bir durumu duyularla sezmeyi anlatabilir."},{"facet_id":"F004","role":"associated_use","statement":"Çevreye bakıp dikkatle araştırarak birinin bulunup bulunmadığını anlamaya çalışma kullanımını taşır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Zamanla gelişen yakınlık ve yabancılığın kalkması anlamını ekler.","collision":"Yakınlık ve rahatlık bildiren ayrı dalla karışır.","fit":"displacement","loses":"Görme, işitme, belirtiyi sezme ve çevreye bakıp araştırma işlemlerini siler.","preserves":"Bir kişi veya şeye yönelen deneyim fikrini çok genel biçimde korur."},"text":"alışmak"}],"identity_rationale":"Kaynak ifadesi görmeyi temel alır, fakat belirli kullanımlarda işitmeyi, bir belirtiyi anlayıp ayırt etmeyi ve çevreye bakarak birini aramayı da aynı dalda aktarır. Bu yüzden dal genel ve sınırsız bir algı yetisi diye tanımlanamaz; her uzantı kendi bağlamına bağlı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir şeyi görmek ve fark etmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"sesi işitmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"onda olgunluk belirtisi görmek ve bunu anlamak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ürken yabani hayvanın birini sezip çevreye bakınması"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"çevreye bakıp birinin olup olmadığını araştırmak"}],"lexicalization_note":"Görüp fark etme çekirdeği ile ses işitme, olgunluk belirtisini ayırt etme ve çevreye bakıp araştırma kalıpları ayrı tutulur; kalıplardaki kapsam çıplak biçime genellenmez.","neighbor_coverage_note":"Bütün aday kartlar değerlendirildi. Görme, genel duyumsama ve yakınlık duygusuyla karışma olasılığı en yüksek üç sınır yayımlandı; diğer adaylar dalı açıklayan ek bir karşıtlık sağlamadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yalnız görsel algı bağlamında yakın karşılık olabilirler. Odak dalın işitme ve belirtiyi sezme uzantıları komşuya, komşunun göz organı anlamı da odak dala taşınamaz.","focus_only":"Odak dal, görmenin yanında belirli yapılarda işitme, belirti sezme ve çevreyi araştırma uzantılarını taşır.","gloss":"fark etme ile gözle görme ayrımı","neighbor_only":"Komşu dal göz organını, görme duyusunu ve göz açıp dikkatle bakma eylemini kendi başına kapsar.","neighbor_ref":"root_000121/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi göz yoluyla görüp seçme alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu daha genel bir duyu alanıdır; odak dalın uzantıları ise kanıtlanan nesne ve yapılara bağlıdır. Bu nedenle genel duyumsama her durumda odak ifadeyle karşılanamaz.","focus_only":"Odak dal görmeyi merkez alır ve yalnız belirli söz çevrelerinde işitme, sezme ve araştırmaya uzanır.","gloss":"belirli algı kullanımları ile genel duyumsama","neighbor_only":"Komşu dal herhangi bir duyu aracılığıyla algılama, bilme ve varlığını saptama alanını genel olarak kapsar.","neighbor_ref":"root_000321/B002","relation_type":"near_synonym","shared_zone":"Her ikisi de bir şeyin duyular aracılığıyla fark edilmesini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal algısal saptamayı, komşu dal ise karşılaşma sonrasındaki duygusal rahatlığı bildirir. Algı gerçekleşebilir ama yakınlık doğmayabilir.","focus_only":"Odak dal bir nesneyi görme, işitme veya belirtilerinden sezme eylemini anlatır.","gloss":"duyusal fark etme ile yakınlık hissetme","neighbor_only":"Komşu dal bir kişi ya da şey karşısında yabancılık ve ürkme duymayıp yakınlık hissetmeyi anlatır.","neighbor_ref":"root_000059/B003","relation_type":"near_neighbor","shared_zone":"Bir kişi veya şeyle karşılaşma iki anlam alanının ortak başlangıç durumu olabilir."}],"source_phrase_ar":"آنست الشيء إذا رأيته وآنسته إذا سمعته (maqayis)؛ آنسته أبصرته وآنست الصوت سمعته وآنست منه رشدا علمته (sihah)؛ آنس من جانب يعني أبصر نارا والاستئناس النظر وأحس بما رابه (tahdhib)؛ فإن آنستم منهم رشدا أي أبصرتم وآنست نارا (mufradat)","source_summary":"Aktarılan anlam alanının merkezi görüp fark etmektir. Aynı ifade ailesi belirli nesne ve yapılarda işitme, bir belirtiyi anlayıp ayırt etme, kaygı veren şeyi sezme ve bakıp araştırma yönlerinde kullanılır; bunlar sınırsız bir genel algı anlamı oluşturmaz.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه آنس الشيء إذا أبصره أو رآه، وآنس الصوت إذا سمعه، وأحس الفزع أو وجد الشيء في نفسه، والاستئناس بمعنى النظر والتبصر.","what_is_not_ar":"لا يدخل الأنس بمعنى الراحة والمؤالفة ولا الإنس بمعنى البشر إلا بقرينة."},"support_links":["sup_9205e7b0ebdb213fb659"]},{"boundary":"Dal duygusal yakınlık, rahatlık ve bunları sağlayan varlıkları kapsar; insan türünün adı, duyusal fark etme ve insana bakan yan anlamları dışarıda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B003","candidate_links":[{"candidate_id":"cand_d583ab28ad614543cc0d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"96:5:2:2","qac_word_ref":"96:5:2","surface_ar":"إِنسَٰنَ"}],"gloss":"yabancılık duymadan yakınlık ve rahatlık hissetme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi ya da şey karşısında yabancılık ve ürkme duygusunun kalkıp yakınlık, rahatlık veya sevinç oluşmasını anlatır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişiye arkadaşlık ederek veya yanında bulunarak yabancılık duygusunu gideren kişi ya da şeyi adlandırır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsana alışık ve saldırgan olmayan hayvanı, özellikle bu nitelikteki köpeği anlatabilir."}}],"root_ar":"ء ن س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi veya şeyin ürkütücü ve yabancı gelmemesi, tersine yakınlık ve iç rahatlığı vermesi anlatıldığında dalın çekirdeğini karşılar.","boundary_detail":"Dal duygusal yakınlık, rahatlık ve bunları sağlayan varlıkları kapsar; insan türünün adı, duyusal fark etme ve insana bakan yan anlamları dışarıda kalır.","branch_image_ar":"الأنس الذي يزيل الوحشة","concept_gloss":"yabancılık duymadan yakınlık ve rahatlık hissetme","contextual_glosses":[{"applicability":"Bir kişi veya şey karşısındaki yabancılık duygusunun kalktığı temel durumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Alışma sonucunda yabancılığın kalkmasını ve yakınlık oluşmasını korur."},"facet_ids":["F001"],"text":"alışıp yakınlık duymak","usage_role":"general"},{"applicability":"Yalnızlığı veya ürkmeyi gideren bir arkadaş, nesne ya da başka bir dayanak adlandırıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yakınlık ve güven veren kaynağın kişiyle sınırlı olmamasını korur."},"facet_ids":["F002"],"text":"yanında rahatlık veren kişi veya şey","usage_role":"explanatory"},{"applicability":"İnsandan kaçmayan ve ısırıp saldırmayan evcil ya da alışkın hayvan için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın insana alışıklığını ve saldırgan olmama sınırını birlikte korur."},"facet_ids":["F003"],"text":"insana alışık ve saldırgan olmayan","usage_role":"contextual"}],"definition":"Bir kişi ya da şey karşısında yabancılık, ürkme veya kaçınma duymayıp yakınlık, rahatlık ve sevinç hissetmeyi anlatır. Bu duyguyu veren kişi veya şeye ve insana alışık, saldırgan olmayan hayvana da aktarılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi ya da şey karşısında yabancılık ve ürkme duygusunun kalkıp yakınlık, rahatlık veya sevinç oluşmasını anlatır."},{"facet_id":"F002","role":"extension","statement":"Kişiye arkadaşlık ederek veya yanında bulunarak yabancılık duygusunu gideren kişi ya da şeyi adlandırır."},{"facet_id":"F003","role":"specialization","statement":"İnsana alışık ve saldırgan olmayan hayvanı, özellikle bu nitelikteki köpeği anlatabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Her türlü sevincin bu dala ait olduğu izlenimini verebilir.","fit":"narrowing","loses":"Yabancılığın ve ürkmenin kalkmasını, alışmayı ve rahatlık veren kişi ya da şey kapsamını kaybeder.","preserves":"Yakınlık durumunda ortaya çıkabilen olumlu duyguyu korur."},"text":"sevinç"}],"identity_rationale":"Kaynak ifadesi, bir kişi veya şey karşısında yabancılık ve ürkme duygusunun kalkmasını çekirdek anlam olarak verir. Yakınlık ve sevinç, rahatlık veren kişi ya da şey ve insana alışık saldırgan olmayan hayvan kullanımları bu çekirdekten bağımlı biçimde açıklanabilir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yakınlık ve rahatlık; yabancılık duymama"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"birine alışıp onun yanında sevinmek"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"biriyle yakınlık kurmak ve onsuz kendini yalnız hissetmek"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"yakın arkadaş; rahatlık veren kişi veya şey"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yakınlıktan ve söyleşiden hoşlanan genç kadın"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"insana alışık, saldırgan olmayan köpek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"gece yolcusuna veya konaklayana güven veren ateş"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"sahibine güven veren bütün silahlar; zırh, miğfer, koruyucu örtü ve kalkan gibi savunma donanımları"}],"lexicalization_note":"Yabancılık duymama çekirdeği ile rahatlık veren kişi veya şey ve insana alışık hayvan gibi özelleşmiş biçimler ayrı katmanlarda tutulur; özel biçimler bütün dalı tanımlamaz.","neighbor_coverage_note":"Bütün aday kartlar karşılaştırıldı. Alışıp bağlanma, özel dostluk ve insan türünü adlandırma alanları dal sınırını en açık gösterdiği için yalnız bu üç ayrım yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın belirleyici yönü yabancılık ve ürkmenin karşıtı olan iç rahatlığıdır; komşu dal süreklilik, bağlanma ve alışkanlık yönlerini odaktan daha geniş taşır.","focus_only":"Odak dal yabancılık ve ürkmenin kalkmasıyla oluşan yakınlık ve rahatlığı, ayrıca bunu sağlayan varlığı öne çıkarır.","gloss":"yakınlık rahatlığı ile alışıp bağlanma","neighbor_only":"Komşu dal bir kişi, yer veya şeye alışmayı, ona bağlanmayı, onunla sürekli bulunmayı ve hayvanın evcilleşmesini daha geniş biçimde kapsar.","neighbor_ref":"root_000045/B005","relation_type":"near_synonym","shared_zone":"İki dal da bir kişi, yer, şey veya hayvana karşı yabancılığın azalmasını anlatabilir."},{"boundary_match":"partial","distinction":"Her rahatlık veren yakınlık özel ve arı bir dostluk değildir. Komşunun karşılıklı dostluk sınırı odak dalın nesne ve hayvan uzantılarına uygulanamaz.","focus_only":"Odak dal kişi dışındaki şeylerin verdiği rahatlığı ve insana alışık hayvanı da kapsayabilir.","gloss":"rahatlık veren yakınlık ile özel dostluk","neighbor_only":"Komşu dal seçilmiş kişiler arasındaki arı, özel ve karşılıklı dostluk bağını anlatır.","neighbor_ref":"root_000430/B007","relation_type":"near_neighbor","shared_zone":"İki dal da kişiler arasında yakınlık ve içtenlik bulunan durumlarda buluşur."},{"boundary_match":"field_only","distinction":"Odak dal bir duygusal ilişkiyi, komşu dal ise bir varlık sınıfını adlandırır. İnsan olmak yakınlık hissetmeyi gerektirmez ve iki ifade birbirinin yerine geçmez.","focus_only":"Odak dal yabancılığın kalkmasıyla doğan duygusal yakınlığı ve rahatlığı anlatır.","gloss":"yakınlık durumu ile insan adı ayrımı","neighbor_only":"Komşu dal insan türünü, insan topluluğunu veya bu türden tek bir kişiyi adlandırır.","neighbor_ref":"root_000059/B001","relation_type":"same_field","shared_zone":"İnsan, iki dalda da temel katılımcı veya gönderim noktasıdır."}],"source_phrase_ar":"الأنس أنس الإنسان بالشيء إذا لم يستوحش منه (maqayis)؛ الإيناس خلاف الإيحاش والإنس خلاف الوحشة والأنيس المؤانس وكل ما يؤنس به (sihah)؛ أنست بفلان أي فرحت به والأنس والاستئناس هو التأنس وكلب أنوس نقيض العقور (tahdhib)؛ الأنس خلاف النفور ولكل ما يؤنس به (mufradat)","source_summary":"Ortak çekirdek, yabancılık ve kaçınmanın karşıtı olan yakınlık ve rahatlıktır. Bu durum birine alışıp onun yanında sevinmeyi, rahatlık veren kişi veya şeyi ve insana alışık saldırgan olmayan hayvanı kapsayacak biçimde genişler.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه أنس الإنسان بالشيء أو بفلان، المؤانسة والتأنيس، الأنيس وكل ما يؤنس به، الفرح بالقرب والحديث، والحيوان الأنوس غير العقور.","what_is_not_ar":"لا يدخل الإنس بمعنى البشر ولا الإيناس بمعنى الإبصار ولا الجانب الإنسي إلا بدليل."},"support_links":["sup_52563ea186b9584513c1"]},{"boundary":"Dal, bir nesnenin insana veya kullanıcıya bakan yanını belirtir; salt sol, salt sağ, genel ön taraf ya da insanın kendisi anlamına gelmez.","branch_kind":"bare","branch_ref":"root_000059/B004","candidate_links":[{"candidate_id":"cand_9d6ead9ebd3579a2fb9d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"96:5:2:2","qac_word_ref":"96:5:2","surface_ar":"إِنسَٰنَ"}],"gloss":"insana dönük yan","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin insana en yakın olan veya insana doğru bakan yanını belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvanda binicinin bulunduğu, binme ve sağma işlemlerinde insana yakın olan yanı anlatır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yayda okçuya doğru bakan ve kullanıcının karşısında bulunan yanı anlatır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İnsana yakın yan bazı aktarımda sol, başka bir aktarımda sağ diye belirlenir; yönün özü bu değişken tanımlardan bağımsızdır."}}],"root_ar":"ء ن س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin yönü, ona yaklaşan veya onu kullanan insana göre belirlendiğinde dalın ortak çekirdeğini verir.","boundary_detail":"Dal, bir nesnenin insana veya kullanıcıya bakan yanını belirtir; salt sol, salt sağ, genel ön taraf ya da insanın kendisi anlamına gelmez.","branch_image_ar":"الجانب الإنسي المقبل على الإنسان","concept_gloss":"insana dönük yan","contextual_glosses":[{"applicability":"Hayvanın binme ve sağma sırasında insana yakın kalan yanı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın yanını biniciyle kurduğu işlevsel ilişkiye göre belirler."},"facet_ids":["F002"],"text":"biniciye yakın yan","usage_role":"contextual"},{"applicability":"Yayın kullanım sırasında okçuya doğru dönük olan yüzü belirtilirken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yay yüzünün yönünü okçunun konumuna göre belirleme özelliğini korur."},"facet_ids":["F003"],"text":"okçuya bakan yay yüzü","usage_role":"explanatory"}],"definition":"Bir nesnenin insana, kullanıcıya veya onun bulunduğu yöne bakan yanıdır. Hayvan ve yay üzerinde işlevsel ilişkiyle belirlenir; bu yanın sabit olarak sol ya da sağ sayılması konusunda aktarım uyuşmazlığı vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin insana en yakın olan veya insana doğru bakan yanını belirtir."},{"facet_id":"F002","role":"specialization","statement":"Hayvanda binicinin bulunduğu, binme ve sağma işlemlerinde insana yakın olan yanı anlatır."},{"facet_id":"F003","role":"specialization","statement":"Yayda okçuya doğru bakan ve kullanıcının karşısında bulunan yanı anlatır."},{"facet_id":"F004","role":"source_variant","statement":"İnsana yakın yan bazı aktarımda sol, başka bir aktarımda sağ diye belirlenir; yönün özü bu değişken tanımlardan bağımsızdır."}],"identity_rationale":"Kaynak ifadesinin güvenilir çekirdeği, bir şeyin insana veya onu kullanan kişiye dönük ve yakın olan yanıdır. Bu yanın solda mı sağda mı olduğu konusunda aktarımlar uyuşmaz; hayvan ve yay örnekleri yönü işlevsel ilişkiyle belirler. Bu nedenle sabit bir sağ-sol tanımı dalın özüne konamaz.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir şeyin insana bakan veya en yakın olan yanı"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yayın okçuya bakan yüzü"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"hayvanın biniciye yakın olan yanı"}],"lexicalization_note":"Tanım çıplak dalın insana dönük yan çekirdeğiyle sınırlıdır. Hayvan ve yay uygulamaları bu çekirdeğin örneklenmesidir; yalnız bu kullanımlardan yeni bir genel yön anlamı çıkarılmaz.","neighbor_coverage_note":"Adayların tamamı incelendi. Genel ön taraf, yönelme eylemi ve arka bölümle kurulan karşılaştırmalar insana göre belirlenen yanın sınırını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda yön, insanın nesneyle kurduğu konum veya kullanım ilişkisine bağlıdır. Komşu dalın genel ön ve yakın anlamları bu özel bağı gerektirmez.","focus_only":"Odak dal bir nesnenin insana veya onu kullanan kişiye dönük yanını ilişkiye göre belirler.","gloss":"insana dönük yan ile genel ön taraf","neighbor_only":"Komşu dal genel olarak ön, önde, yakın veya karşıda bulunma yönlerini kişiye bağlı bir kullanım ilişkisi gerektirmeden anlatır.","neighbor_ref":"root_000053/B011","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin bakana göre karşıda veya önde kalan bölümünü gösterebilir."},{"boundary_match":"partial","distinction":"Bir nesnenin insana dönük yanı bir bölüm adıdır; komşu ise dönme veya yönelme olayını anlatır. Sonuç konumu ile o konuma geçiş eylemi birbirinin yerine kullanılamaz.","focus_only":"Odak dal, yönelme tamamlandıktan sonra insana dönük olan sabit yanı adlandırır.","gloss":"dönük yan ile yönelme eylemi","neighbor_only":"Komşu dal yüz, baş, el, kap veya hayvanın bir hedefe doğru dönmesi ve yönelmesi eylemini anlatır.","neighbor_ref":"root_001263/B003","relation_type":"near_neighbor","shared_zone":"İki dal da bir kişi veya hedefe doğru bakma yönünü içerir."},{"boundary_match":"partial","distinction":"Bağlama göre karşıt görünebilseler de odak dal her zaman geometrik ön yüz değildir ve bu yüzden düzenli bir karşıt çift oluşturmaz; belirleyici ölçüt insana yakınlıktır.","focus_only":"Odak dal insana veya kullanıcıya yakın ve ona bakan yanı gösterir.","gloss":"insana bakan yan ile arka taraf","neighbor_only":"Komşu dal bir şeyin arkasında kalan, yüzünün karşıtı olan arka bölümünü gösterir.","neighbor_ref":"root_000458/B001","relation_type":"near_neighbor","shared_zone":"İki dal da bir nesnenin başka bir yöne göre belirlenen bölümünü adlandırır."}],"source_phrase_ar":"الإنسي الأيسر من كل شيء وقيل الأيمن وما أقبل منهما على الإنسان فهو إنسي وإنسي القوس ما أقبل عليك منها (sihah)؛ الإنسي من الدواب الجانب الأيسر الذي منه يركب ويحتلب ومن الإنسان الجانب الذي يلي الرجل الأخرى (tahdhib)؛ إنسي الدابة للجانب الذي يلي الراكب وإنسي القوس للجانب الذي يقبل على الرامي (mufradat)","source_summary":"Ortak anlam, nesnenin insana veya kullanıcıya dönük yanıdır; hayvanda biniciye, yayda okçuya göre belirlenir. İnsan bedenindeki tekil uygulamada öteki bacağa bakan yan kastedilir. Bu yanın solda mı sağda mı bulunduğuna ilişkin anlatımlar ayrıştığı için genel tanım sabit bir yön seçmez.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه إنسي الدابة والقوس وكل شيئين: ما يلي الإنسان أو يقبل على الراكب أو الرامي، في مقابلة الوحشي.","what_is_not_ar":"لا يدخل الإنسان نفسه ولا الأنس النفسي ولا الإبصار."},"support_links":["sup_9b1e21f2092002400d97"]},{"boundary":"Dal göz bebeğinde görülen küçük görüntüyü, ayrıca ayrı bir aktarım olarak parmak ucunu kapsar; gözün kendisini veya genel insan türünü belirtmez.","branch_kind":"bare","branch_ref":"root_000059/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"96:5:2:2","qac_word_ref":"96:5:2","surface_ar":"إِنسَٰنَ"}],"gloss":"göz bebeğinde görülen küçük yansıma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Göz bebeğinin kara bölümünde görülen küçük insan biçimli görüntüyü veya yansımayı adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı bir aktarımda parmak ucu veya eldeki parmak ucunu anlatan kullanım da aynı adla verilir."}}],"root_ar":"ء ن س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir bakanın göz bebeğinde beliren küçük insan biçimli görüntü adlandırıldığında dalın ortak ve temel anlamını karşılar.","boundary_detail":"Dal göz bebeğinde görülen küçük görüntüyü, ayrıca ayrı bir aktarım olarak parmak ucunu kapsar; gözün kendisini veya genel insan türünü belirtmez.","branch_image_ar":"إنسان العين وصورة الإنسان في السواد","concept_gloss":"göz bebeğinde görülen küçük yansıma","contextual_glosses":[{"applicability":"Yansımanın insan biçiminde algılanması özellikle belirtilmek istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Görüntünün göz bebeğinde bulunmasını ve küçük insan biçiminde görünmesini korur."},"facet_ids":["F001"],"text":"göz bebeğindeki küçük insan görüntüsü","usage_role":"explanatory"},{"applicability":"Yalnız parmak ucunu aynı adla veren ayrı kaynak kullanımında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Göz anlamından bağımsız olan parmak ucu kullanımını doğrudan korur."},"facet_ids":["F002"],"text":"parmak ucu","usage_role":"contextual"}],"definition":"Gözün kara bölümünde görülen küçük insan biçimli görüntü veya yansımadır. Ayrı bir kaynak kullanımında aynı ad parmak ucuna da verilir, ancak bu kullanım göz görüntüsü çekirdeğini değiştirmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Göz bebeğinin kara bölümünde görülen küçük insan biçimli görüntüyü veya yansımayı adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Ayrı bir aktarımda parmak ucu veya eldeki parmak ucunu anlatan kullanım da aynı adla verilir."}],"identity_rationale":"Kaynak ifadesinin ortak çekirdeği, gözün kara bölümünde görülen küçük insan biçimli görüntü veya yansımadır. Parmak ucu anlamı tek aktarım içinde eklenir ve gözdeki görüntünün kurucu parçası değildir; bağımlı bir kaynak varyantı olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"göz bebeğinde görülen küçük görüntü veya yansıma"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"göz bebeklerinde görülen küçük görüntüler"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"parmak ucu; eldeki parmak ucunu anlatan kullanım"}],"lexicalization_note":"Çıplak dalın çekirdeği gözün kara bölümündeki küçük görüntüdür. Parmak ucu aktarımı bağımlı bir varyanttır; gözle ilgili belirli biçimlerden genel görüntü veya genel insan anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün aday kartlar değerlendirildi. Anatomik göz bebeği, genel tasvir ve göz organı karşılaştırmaları görüntünün yerini ve türünü en iyi sınırladığı için bu üçü yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Komşu anatomik bölümün kendisidir; odak dal ise o bölümde görülen görüntüdür. Taşıyıcı yapı ile üzerinde beliren yansıma birbirinin yerine kullanılamaz.","focus_only":"Odak dal göz bebeğinde görülen küçük insan biçimli görüntüyü veya yansımayı adlandırır.","gloss":"göz bebeği ile göz bebeğindeki yansıma","neighbor_only":"Komşu dal göz bebeğinin kendisini, onun kara bölümünü ve anatomik yapısını adlandırır.","neighbor_ref":"root_000300/B002","relation_type":"same_field","shared_zone":"İki dal aynı göz bölgesine gönderimde bulunur."},{"boundary_match":"partial","distinction":"Odak görüntü göz bebeğindeki belirli yansımadır; komşu ise konum ve oluşum biçimi bakımından çok daha genel tasvirleri kapsar. Her tasvir gözdeki yansıma değildir.","focus_only":"Odak dal yalnız göz bebeğinde beliren küçük insan biçimli görüntüyü ve ayrı bir parmak ucu varyantını kapsar.","gloss":"gözdeki yansıma ile genel tasvir","neighbor_only":"Komşu dal resim, model, heykel veya başka bir varlığa göre biçimlendirilmiş genel örnekleri kapsar.","neighbor_ref":"root_001397/B008","relation_type":"near_neighbor","shared_zone":"Her iki dal başka bir varlığın görünüşünü taşıyan bir görüntüyü anlatabilir."},{"boundary_match":"field_only","distinction":"Göz, görmeyi sağlayan organdır; odak dal ise gözde görülen yansımadır. Organın adı yansımanın, yansımanın adı da organın genel karşılığı değildir.","focus_only":"Odak dal gören gözün içinde beliren küçük görüntüyü adlandırır.","gloss":"göz organı ile içindeki küçük görüntü","neighbor_only":"Komşu dal görme organı olan gözün kendisini ve onun görme işlevini adlandırır.","neighbor_ref":"root_001069/B001","relation_type":"same_field","shared_zone":"Her iki dal göz ve görme alanına aittir."}],"source_phrase_ar":"إنسان العين صبيها الذي في السواد (maqayis)؛ إنسان العين المثال الذي يرى في السواد أي سواد العين (sihah)؛ الإنسان أيضا إنسان العين وجمعه أناسي والإنسان الأنملة (tahdhib)","source_summary":"Ortak aktarım, göz bebeğinin kara bölümünde görülen küçük görüntüyü bir insan biçimi olarak tanımlar. Buna ek olarak parmak ucu anlamı da bildirilir, fakat bu ek kullanım gözdeki yansıma çekirdeğinden ayrı tutulur.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه إنسان العين: المثال أو الصبي الذي يرى في سواد العين، وما ألحقه تهذيب اللغة من الأنملة أو إنسان الكف.","what_is_not_ar":"لا يدخل الإنسان بمعنى البشر عموما ولا الأنس بمعنى الراحة."},"support_links":[]},{"boundary":"Dal yalnız belirtilen söz kuruluşlarında kişinin kendisini veya seçkin yakınını gösterir; genel insan, gerçek evlatlık ve her türlü arkadaşlık anlamına genişletilemez.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"96:5:2:2","qac_word_ref":"96:5:2","surface_ar":"إِنسَٰنَ"}],"gloss":"belirli sözlerde kişinin kendisi veya seçilmiş yakını","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiye kendi durumunu soran belirli kuruluşta muhatabın kendisini gösterir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişiye bağlanarak söylendiğinde onun seçilmiş yakınını, özel arkadaşını veya sırdaşını belirtir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı anlam çevresindeki paralel adlar yakın dostu, içten arkadaşı ve oturup konuşulan kişiyi gösterebilir."}}],"root_ar":"ء ن س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kaynakta gösterilen soru ve kişi bağlantısı kuruluşlarını topluca açıklarken kullanılabilir; genel bir kişi ya da akraba adı değildir.","boundary_detail":"Dal yalnız belirtilen söz kuruluşlarında kişinin kendisini veya seçkin yakınını gösterir; genel insan, gerçek evlatlık ve her türlü arkadaşlık anlamına genişletilemez.","branch_image_ar":"ابن الإنس للنفس والصفوة","concept_gloss":"belirli sözlerde kişinin kendisi veya seçilmiş yakını","contextual_glosses":[{"applicability":"Muhataba kendi durumunun nasıl olduğu sorulduğunda doğal Türkçe karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sorunun muhatabın kendi durumuna yönelmesini korur."},"facet_ids":["F001"],"text":"kendin; nasılsın","usage_role":"contextual"},{"applicability":"Bir kişinin seçip özel tuttuğu yakın arkadaş veya sırdaş anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yakın kişinin seçilmiş, özel ve güvenilen biri olmasını korur."},"facet_ids":["F002"],"text":"onun en yakını ve sırdaşı","usage_role":"contextual"},{"applicability":"Yakın dost, içten arkadaş ve birlikte oturup konuşulan kişi için sıralanan paralel adları açıklarken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yakınlık, dostluk ve sürekli görüşme ilişkilerini birlikte korur."},"facet_ids":["F003"],"text":"yakın dostum ve görüşme arkadaşım","usage_role":"explanatory"}],"definition":"Belirli bir soru kuruluşunda muhatabın kendisini ve durumunu, başka bir kişiyle kurulan adlandırmada ise onun seçilmiş yakınını, sırdaşını veya sürekli görüştüğü arkadaşını belirtir. İki kullanım aynı kuruluş ailesinde bulunsa da katılımcı ilişkileri ayrıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiye kendi durumunu soran belirli kuruluşta muhatabın kendisini gösterir."},{"facet_id":"F002","role":"core","statement":"Bir kişiye bağlanarak söylendiğinde onun seçilmiş yakınını, özel arkadaşını veya sırdaşını belirtir."},{"facet_id":"F003","role":"associated_use","statement":"Aynı anlam çevresindeki paralel adlar yakın dostu, içten arkadaşı ve oturup konuşulan kişiyi gösterebilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Gerçek bir baba ile erkek çocuk arasındaki soy ilişkisini ekler.","collision":"Sözün amaçlanan kişi ilişkisini gerçek akrabalıkla karıştırır.","fit":"displacement","loses":"Kişinin kendisini veya seçilmiş yakınını gösteren kalıplaşmış gönderimi kaybeder.","preserves":"Kuruluşun yüzeyindeki çocuk ve soy ilişkisi çağrışımını korur."},"text":"oğlu"}],"identity_rationale":"Kaynak ifadesi iki ayrı kalıplaşmış ilişkiyi açıkça ayırır: kişiye kendi durumunu soran sözde kişinin kendisi, bir başkasına bağlanan sözde ise seçilmiş yakın ve sırdaş kastedilir. Yakın arkadaş ve oturup konuşulan kişi için verilen paralel adlar ikinci alanı destekler.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"kendin; kendi durumun nasıl"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"onun seçkin yakını ve sırdaşı"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"yakınım, içten dostum ve görüşme arkadaşım"}],"lexicalization_note":"Kişinin kendisini soran kuruluş, seçilmiş yakını belirten kuruluş ve yakın arkadaş adları ayrı tutulur. Bunların hiçbiri çıplak biçime genel kişi veya akrabalık anlamı olarak taşınmaz.","neighbor_coverage_note":"Aday kartların tamamı incelendi. Kişinin kendisini gösteren başka kuruluş, iç çevre ve genel dostluk alanları iki ayrı gönderimi en iyi sınırlandırdığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ortak gönderim yalnız benlik anlamındadır; kuruluşlar değiştirilemez. Odak dalın seçilmiş yakın ve sırdaş anlamı komşuda bulunmaz.","focus_only":"Odak dal kişinin kendisini belirli bir soru kuruluşunda gösterir ve ayrıca seçilmiş yakın anlamını da taşır.","gloss":"kişinin kendisini gösteren iki ayrı söz","neighbor_only":"Komşu dal şiirsel bir söyleyişte yalnız kişinin kendi benliğini başka bir kalıpla belirtir.","neighbor_ref":"root_001271/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal belirli bir söz kuruluşunda kişinin kendisine gönderimde bulunur."},{"boundary_match":"partial","distinction":"Odak dal çoğunlukla tek bir yakın veya sırdaşı gösterir; komşu kişinin iç çevresini ve işlerine alınan özel kişileri daha geniş kapsar.","focus_only":"Odak dal seçilmiş yakını ve sırdaşı gösterebilir, fakat kişinin kendisini soran ayrı bir kullanım da içerir.","gloss":"seçilmiş yakın ile iç çevre","neighbor_only":"Komşu dal bir kişinin işine ve sırrına alınan bütün iç çevreyi ve özel kişileri topluluk olarak kapsayabilir.","neighbor_ref":"root_000128/B004","relation_type":"near_neighbor","shared_zone":"Güvenilen ve özel tutulan kişi iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Her dost odak daldaki özel adlandırmanın taşıdığı seçilmiş yakın değildir; odak dalın kişinin kendisine gönderimi de genel dostluk alanının dışındadır.","focus_only":"Odak dal özel kuruluşlarla kişinin kendisini ya da seçilmiş yakınını belirtir.","gloss":"seçilmiş sırdaş ile genel dostluk","neighbor_only":"Komşu dal arkadaşlık ve dostluk ilişkisini açık ya da gizli yönleriyle genel olarak anlatır.","neighbor_ref":"root_000397/B001","relation_type":"near_neighbor","shared_zone":"Seçilmiş yakın kişi aynı zamanda dost veya arkadaş olabilir."}],"source_phrase_ar":"كيف ابن إنسك إذا سأله عن نفسه (maqayis)؛ كيف ابن إنسك يعني نفسه وفلان ابن إنس فلان أي صفيه وخاصته وهذا خدني وإنسي وخلصي وجلسي (sihah)؛ كيف ترى ابن إنسك إذا خاطبت الرجل عن نفسه وفلان ابن أنس فلان أي صفيه وأنيسه (tahdhib)؛ قيل ابن إنسك للنفس (mufradat)","source_summary":"Aktarımlar, doğrudan hitapta kişinin kendi durumunu soran kullanım ile birinin seçkin yakını ve sırdaşını gösteren kullanımı birlikte verir. Yakın dost ve sürekli görüşülen arkadaş anlamındaki paralel adlar ikinci ilişki alanını genişletir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه كيف ابن إنسك للسؤال عن النفس، وفلان ابن أنس فلان لصفيه وخاصته، وما قاربه من الخدن والأنيس والخلص والجليس.","what_is_not_ar":"لا يدخل مطلق الإنسان ولا مطلق المؤانسة إلا إذا جاء بصيغة هذا الباب أو قرينته."},"support_links":[]},{"boundary":"Dal eve girmeden önce izin ve kabul arama durumuyla sınırlıdır; genel görme, genel yakınlık, eve yerleşme veya barınma anlamına gelmez.","branch_kind":"unresolved","branch_ref":"root_000059/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"96:5:2:2","qac_word_ref":"96:5:2","surface_ar":"إِنسَٰنَ"}],"gloss":"girişten önce izin ve kabul arama","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eve girmeden önce selam verip girmek için izin istemeyi ve kabul beklemeyi anlatır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı açıklama, girişten önce içeridekilerden yakınlık ve kabul işareti bulmayı öne çıkarır."}}],"root_ar":"ء ن س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir eve girmeden önce selam, izin sorusu veya içeridekilerin kabulünü yoklama yoluyla girişe onay arandığında kullanılır.","boundary_detail":"Dal eve girmeden önce izin ve kabul arama durumuyla sınırlıdır; genel görme, genel yakınlık, eve yerleşme veya barınma anlamına gelmez.","branch_image_ar":"الاستئناس قبل دخول البيوت","concept_gloss":"girişten önce izin ve kabul arama","contextual_glosses":[{"applicability":"Giriş izninin selam ve açık bir izin sorusuyla istendiğini belirten açıklamada uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Selam verme, izin sorma ve girişten önce bekleme işlemlerini korur."},"facet_ids":["F001"],"text":"selam verip girebilir miyim diye sormak","usage_role":"explanatory"},{"applicability":"İçeridekilerin yakınlık ve kabul gösterdiğini anlayarak girişe elverişli ortam bulma yorumunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Girişten önce kabul ve yakınlık işareti bulma yönünü korur."},"facet_ids":["F002"],"text":"girişe açık bir karşılama bulmak","usage_role":"contextual"}],"definition":"Bir eve girmeden önce selam vererek izin istemeyi ve içeridekilerin girişe açık olduğunu anlamayı anlatır. Aktarımın bir yönü doğrudan izin sorusunu, diğer yönü girişe elverişli bir kabul ve yakınlık bulmayı öne çıkarır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eve girmeden önce selam verip girmek için izin istemeyi ve kabul beklemeyi anlatır."},{"facet_id":"F002","role":"source_variant","statement":"Ayrı açıklama, girişten önce içeridekilerden yakınlık ve kabul işareti bulmayı öne çıkarır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yalnız gözle inceleme ve bir şeyi görme anlamını ekler.","collision":"Duyusal fark etme ve çevreye bakıp araştırma dalıyla karışır.","fit":"displacement","loses":"Selam verme, izin isteme ve içeridekilerin kabulünü bekleme koşullarını kaybeder.","preserves":"Girişten önce çevreyi yoklama düşüncesine sınırlı ölçüde yaklaşır."},"text":"bakıp görmek"}],"identity_rationale":"Kaynak ifadesi yalnız eve giriş öncesindeki belirli söz çevresinde açıklanır. Bir aktarım bunu selam verip izin isteme ve girebilir miyim diye sorma olarak, diğeri ise girişe elverişli bir kabul ve yakınlık bulma olarak yorumlar. Dal bu iki açıklamayı korumalı, fakat çıplak biçime genel bakma veya genel rahatlık anlamı yüklememelidir.","lexicalization_note":"Mekanik kapsam çözümlenmemiştir ve eldeki kanıt yalnız giriş öncesi kuruluşu gösterir. Bu nedenle tanım bu söz çevresine bağlanır, çıplak bir genel anlam varsayılmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı. Genel yakınlık, çevreyi gözleme ve barınma senaryosu giriş öncesi izin sınırını en iyi açıkladığı için bu üç ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir giriş davranışı ve onay koşuludur; komşu dal yer ve zamanla sınırlı olmayan duygusal durumdur. Genel yakınlık, giriş izninin yerine geçmez.","focus_only":"Odak dal eve girişten önce selam, izin sorusu ve kabul bekleme yoluyla yürütülen sınırlı bir davranışı anlatır.","gloss":"giriş kabulü ile genel yakınlık duygusu","neighbor_only":"Komşu dal kişi veya şey karşısında genel olarak yabancılık ve ürkme duymayıp yakınlık ve rahatlık hissetmeyi anlatır.","neighbor_ref":"root_000059/B003","relation_type":"near_neighbor","shared_zone":"Kabul gören kişi giriş öncesinde kendini yabancı hissetmeyebilir ve yakınlık işareti bulabilir."},{"boundary_match":"partial","distinction":"Çevreyi gözlemek yalnız bilgi edinir; odak dal içeridekilerden onay almayı amaçlar. Birini görmek veya sesini duymak, tek başına giriş izni değildir.","focus_only":"Odak dal girişten önce selam verip izin ve kabul aramayı gerektirir.","gloss":"izin arama ile çevreyi gözleme","neighbor_only":"Komşu dal görme, işitme, belirti sezme veya çevreye bakarak birini araştırma eylemlerini anlatır.","neighbor_ref":"root_000059/B002","relation_type":"near_neighbor","shared_zone":"Girişten önce içeride birinin bulunup bulunmadığını anlamaya çalışma iki alanı aynı durumda buluşturabilir."},{"boundary_match":"thematic_only","distinction":"Odak dal girişten önceki toplumsal onayı, komşu dal ise bir yere yönelip orada barınmayı anlatır; aralarında sıradan sözcüksel yer değiştirme yoktur.","focus_only":"Odak dal bir eve girmeden önce kabul ve izin arama davranışıdır.","gloss":"eve giriş izni ile barınma","neighbor_only":"Komşu dal bir yere sığınma, yerleşme, barınma veya başkasını barındırma hareketini anlatır.","neighbor_ref":"root_000070/B001","relation_type":"thematic","shared_zone":"İki dal da bir yerle insan arasındaki giriş ve bulunma senaryosunda yer alabilir."}],"source_phrase_ar":"حتى تستأنسوا معناه حتى تستأذنوا وإنما هو حتى تسلموا وتستأنسوا السلام عليكم أأدخل (tahdhib)؛ حتى تستأنسوا أي تجدوا إيناسا (mufradat)","source_summary":"Giriş öncesi davranış iki yönden açıklanır: selam verip açıkça izin istemek ve girebilir miyim diye sormak ya da içeridekilerden girişe elverişli bir kabul ve yakınlık bulmak. Her iki açıklama da eve izinsiz girmeme sınırında birleşir.","sources":["TA","MU"],"what_is_ar":"يدخل فيه تفسير حتى تستأنسوا بالاستئذان أو السلام وطلب الدخول، أو بإيجاد إيناس قبل الدخول.","what_is_not_ar":"لا يدخل مطلق الإبصار أو مطلق الأنس إلا في صيغة الدخول المذكورة."},"support_links":[]},{"boundary":"Çekirdek, bir şeyi bilme ve gerçeğiyle kavramadır; bildirme, öğretme, öğrenme ve bilgi yarışında yenme ayrı biçimlere bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001040/B001","candidate_links":[{"candidate_id":"cand_441a1b413958f88f8b7e","lane":"micro"},{"candidate_id":"cand_d583ab28ad614543cc0d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَلَّمَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Eal~ama|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:5:1:1","qac_word_ref":"96:5:1","surface_ar":"عَلَّمَ"},{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"96:5:5:1","qac_word_ref":"96:5:5","surface_ar":"يَعْلَمْ"}],"gloss":"bilme ve gerçeğini kavrama","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi bilme, tanıma ve gerçeğine uygun biçimde kavrama durumu bilgisizliğin karşıtıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir haberin farkına varmak veya ondan haberdar olmak, bilme çekirdeğinin belirli bir konuya uygulanmasıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bildirme, öğretme ve öğrenme biçimleri bilginin bir başkasına ulaştırılması ya da kişinin onu edinmesi süreçlerini anlatır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Karşılıklı bilgi sınamasında birini yenmek, belirli bir kuruluşta ortaya çıkan rekabetçi kullanımdır."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bilgisizliğin karşıtı olan temel zihinsel edinimi, tanımayı ve gerçeğe uygun kavrayışı birlikte karşılar.","boundary_detail":"Çekirdek, bir şeyi bilme ve gerçeğiyle kavramadır; bildirme, öğretme, öğrenme ve bilgi yarışında yenme ayrı biçimlere bağlıdır.","branch_image_ar":"انكشاف الشيء للعارف","concept_gloss":"bilme ve gerçeğini kavrama","contextual_glosses":[{"applicability":"Bir olay veya gelişme hakkındaki haberin kişinin bilgisine ulaşması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Haberin farkına varma ve ondan bilgi edinme yönünü korur."},"facet_ids":["F002"],"text":"haberinden haberdar olmak","usage_role":"contextual"},{"applicability":"Bilginin tekrar ve yönlendirmeyle bir öğrenende yerleşmesini sağlayan öğretim bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilginin aktarılması ve öğrenende kalıcı bir sonuç oluşturması sürecini korur."},"facet_ids":["F003"],"text":"öğretmek ve öğrenmesini sağlamak","usage_role":"explanatory"},{"applicability":"İki kişi arasındaki bilgi sınamasında bir tarafın ötekini yenmesi bağlamına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilgi alanındaki karşılaştırmayı ve üstün gelme sonucunu korur."},"facet_ids":["F004"],"text":"bilgide üstün gelmek","usage_role":"contextual"}],"definition":"Bir şeyi bilmek, tanımak ve onu gerçeğine uygun biçimde kavramak; böylece bilgisizlikten çıkmaktır. Haber verilmesi, öğretme, öğrenme ve bilgi bakımından üstün gelme bu çekirdekten hareket eden, belirli biçimlere bağlı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi bilme, tanıma ve gerçeğine uygun biçimde kavrama durumu bilgisizliğin karşıtıdır."},{"facet_id":"F002","role":"extension","statement":"Bir haberin farkına varmak veya ondan haberdar olmak, bilme çekirdeğinin belirli bir konuya uygulanmasıdır."},{"facet_id":"F003","role":"associated_use","statement":"Bildirme, öğretme ve öğrenme biçimleri bilginin bir başkasına ulaştırılması ya da kişinin onu edinmesi süreçlerini anlatır."},{"facet_id":"F004","role":"associated_use","statement":"Karşılıklı bilgi sınamasında birini yenmek, belirli bir kuruluşta ortaya çıkan rekabetçi kullanımdır."}],"identity_rationale":"Dalın bilme ve bilgisizliğin karşıtı olma yönündeki çekirdeği kaynak ifadesiyle uyumludur. Ancak haberden haberdar olma, öğretme, öğrenme ve bilgi bakımından üstün gelme kullanımları bu çekirdekle aynı düzeyde değil, belirli biçimlere bağlı uzantılar olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bilgi; bir şeyi gerçeğiyle kavrama"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şeyi bilmek ve tanımak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"haberinden haberdar olmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bildirmek, haberdar etmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"öğretmek, öğrenmesini sağlamak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"öğrenmek, kavramaya yönelmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bilmek; buyrukta bil ki"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bilgi yarışında yenmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bilen ve bildiğine göre davranan kişi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bilgili, bilgi sahibi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"çok bilgili, çok bilen"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"son derece bilgili kişi"}],"lexicalization_note":"Tanım çıplak bilme çekirdeğini öne alır; haber, öğretim, öğrenim ve karşılıklı bilgi sınamasıyla ilgili anlamları yalnızca ilgili biçim ve kuruluşlara bağlar.","neighbor_coverage_note":"Bilme çekirdeğini en çok açıklayan yakın kavrayış dalı, açık karşıtı olan bilgisizlik dalı ve doğru kullanım boyutu taşıyan bilgelik dalı seçildi; öteki adaylar yalnızca uzak çağrışım veya ayrı kök içi anlam alanı sunar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdekleri yakın olsa da odak dalın biçime bağlı aktarım ve edinim süreçleri ile komşunun akletme ve hızlı anlama vurgusu karşılıklı değiştirilebilirliği sınırlar.","focus_only":"Odak dal, haberden haberdar etme, öğretme, öğrenme ve bilgi yarışında üstün gelme gibi biçime bağlı uzantıları da kapsar.","gloss":"bilmek ve anlamını kavramak","neighbor_only":"Komşu dal, anlamları doğrulama, akletme ve çabuk kavrama yönlerini ayrıca öne çıkarır.","neighbor_ref":"root_001182/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyi bilme, tanıma ve zihnen kavrama alanında büyük ölçüde örtüşür."},{"boundary_match":"opposed","distinction":"Odak dal bilgiye erişmeyi ve kavramayı bildirirken komşu dal bu erişimin bulunmamasını ya da gerçeğin yanlış bilinmesini bildirir.","focus_only":"Bir şeyi tanıma, gerçeğine uygun kavrama ve bilgi sahibi olma bulunur.","gloss":"bilgi ile bilgisizlik karşıtlığı","neighbor_only":"Bilginin yokluğu, durumu tanımama veya gerçeğe aykırı bir kanaat bulunur.","neighbor_ref":"root_000271/B001","relation_type":"antonym","shared_zone":"İki dal aynı zihinsel erişim ekseninin olumlu ve olumsuz uçlarını gösterir."},{"boundary_match":"partial","distinction":"Bilmek tek başına odak dal için yeterli olabilir; komşu dal ise bilginin doğru yargı ve isabetli davranışla birleşmesini öne çıkarır.","focus_only":"Odak dalda yalın bilme ve tanıma, bilginin doğru kullanımından bağımsız olarak çekirdekte yer alabilir.","gloss":"bilgi ile bilgelik","neighbor_only":"Komşu dal doğruyu bulma, yerinde yargı ve bilgiyi isabetli kullanma niteliğini gerektirir.","neighbor_ref":"root_000348/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal bilgi sahibi olmayı ve zihinsel kavrayışı paylaşır."}],"source_phrase_ar":"العلم نقيض الجهل (maqayis;ayn;tahdhib)؛ علمت الشيء عرفته (sihah;tahdhib)؛ إدراك الشيء بحقيقته (mufradat)؛ ما علمت بخبرك أي ما شعرت به (ayn;tahdhib)؛ أعلمته بكذا وعلمته تعليما (ayn)؛ التعليم تنبيه النفس لتصور المعاني (mufradat)؛ تعلم بمعنى اعلم (maqayis;sihah;tahdhib)؛ عالمت الرجل فعلمته (sihah;tahdhib)","source_summary":"Kaynakların ortak çekirdeği, bilgiyi bilgisizliğin karşıtı sayar ve bir şeyi tanıyıp gerçeğiyle kavramayı öne çıkarır. Toplu tanıklık ayrıca haberden haberdar olmayı, bilgiyi aktarmayı, öğrenmeyi ve bilgiyle üstün gelmeyi biçime bağlı uzantılar olarak gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العلم نقيض الجهل وإدراك الشيء ومعرفته والشعور بالخبر والتعلم والتعليم والإعلام والمغالبة بالعلم","what_is_not_ar":"ليس هو العلامة الحسية ولا الجبل ولا الراية ولا الشق في الشفة ولا اسم العالمين"},"support_links":["sup_52563ea186b9584513c1","sup_9205e7b0ebdb213fb659"]},{"boundary":"Dal bütün işaret türlerini sınırsızca kapsamaz; kaynakta anılan ayırt etme ve yol gösterme işlevli izlerle bunlara bağlı kullanımlarla sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001040/B002","candidate_links":[{"candidate_id":"cand_9d6ead9ebd3579a2fb9d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَلَّمَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Eal~ama|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:5:1:1","qac_word_ref":"96:5:1","surface_ar":"عَلَّمَ"},{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"96:5:5:1","qac_word_ref":"96:5:5","surface_ar":"يَعْلَمْ"}],"gloss":"ayırt edici ve yol gösterici işaret","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesneyi veya kişiyi başkalarından ayırıp tanınır kılan belirgin iz ya da işaret çekirdeği oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bayrak, belirgin dağ, yol belirtisi ve kumaşın kenar deseni yön bulduran veya tanıtan somut gerçekleşmelerdir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Savaşçının, kumaşın veya sarığın ayırt edici bir işaretle donatılması belirli kuruluşlara bağlı eylemsel kullanımdır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Tanınmış bir kişinin belirgin bir bayrağa benzetilmesi ve yaklaşan son zamanı gösteren belirti, işaret çekirdeğinin uzantılarıdır."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyi tanınır kılan veya ona ulaşmayı sağlayan belirgin iz ve işaretlerin ortak çekirdeğini karşılar.","boundary_detail":"Dal bütün işaret türlerini sınırsızca kapsamaz; kaynakta anılan ayırt etme ve yol gösterme işlevli izlerle bunlara bağlı kullanımlarla sınırlıdır.","branch_image_ar":"أثر يميز الشيء ويهدي إليه","concept_gloss":"ayırt edici ve yol gösterici işaret","contextual_glosses":[{"applicability":"Askerlerin çevresinde toplandığı bayrak ya da yol bulmayı sağlayan belirgin dağ ve iz bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Görünürlük ile yöneltme ve tanıtma işlevini korur."},"facet_ids":["F002"],"text":"bayrak veya uzaktan seçilen kılavuz","usage_role":"contextual"},{"applicability":"Bir savaşçıya, kumaşa veya sarığa başkalarından ayıran görünür bir belirti ekleme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşaretin sonradan konmasını ve ayırt etme amacını korur."},"facet_ids":["F003"],"text":"tanıtıcı işaret koymak","usage_role":"contextual"},{"applicability":"Belirli bir son zamanın yaklaştığını haber veren gösterge bağlamına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir olayın yakınlığını gösterme işlevini korur."},"facet_ids":["F004"],"text":"yaklaşmayı gösteren belirti","usage_role":"explanatory"}],"definition":"Bir şeyi başkalarından ayıran, tanınmasını sağlayan veya ona götüren belirgin iz ya da işarettir. Bayrak, uzaktan seçilen dağ, yol belirtisi, kumaş kenarı ve sonradan konan tanıtıcı izler bu işlevin farklı gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesneyi veya kişiyi başkalarından ayırıp tanınır kılan belirgin iz ya da işaret çekirdeği oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Bayrak, belirgin dağ, yol belirtisi ve kumaşın kenar deseni yön bulduran veya tanıtan somut gerçekleşmelerdir."},{"facet_id":"F003","role":"associated_use","statement":"Savaşçının, kumaşın veya sarığın ayırt edici bir işaretle donatılması belirli kuruluşlara bağlı eylemsel kullanımdır."},{"facet_id":"F004","role":"extension","statement":"Tanınmış bir kişinin belirgin bir bayrağa benzetilmesi ve yaklaşan son zamanı gösteren belirti, işaret çekirdeğinin uzantılarıdır."}],"identity_rationale":"Kaynak ifadesi, bir şeyi başkasından ayıran belirgin izi dalın ortak çekirdeği olarak açıkça destekler. Bayrak, belirgin dağ, yol belirtisi, kumaş deseni ve savaş işareti gibi örnekler bu çekirdeğin farklı gerçekleşmeleridir; tanınmış kişi ve son zaman belirtisi ise benzetme veya gösterme ilişkisine bağlı uzantılardır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ayırt edici işaret"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bayrak, sancak"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yol gösteren belirgin dağ"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"kumaşın kenar işareti veya deseni"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yol gösteren iz veya belirti"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"savaşta kendine ayırt edici işaret takmak"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"kumaşı işaretlemek"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"işaret olarak kullanılan kına"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"sarığı tanıtıcı bir biçimde sarmak"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"tanınmış ve öne çıkan kişi"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"son saatin yaklaştığını gösteren belirti"}],"lexicalization_note":"Ayırt edici iz çıplak çekirdektir; savaşçı, kumaş, sarık ve belirli zaman göstergesiyle kurulan anlamlar kendi kuruluşlarına bağlı tutulur.","neighbor_coverage_note":"En yararlı karşılaştırmalar geçmişten kalan iz, bilerek konan tanıtıcı işaret ve fiziksel damga ile yapıldı; bayrak adayı yalnızca tek bir alt gerçekleşmeyi, öteki adaylar ise daha uzak renk veya biçim belirtilerini karşılar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda işaret önceden konabilir veya doğal bir kılavuz olabilir; komşu dalda iz, daha önceki bir varlık ya da olayın geride kalan sonucudur.","focus_only":"Odak dal, bilerek konan bayrak ve işaretlerin yanı sıra yön bulduran belirgin dağ gibi göstergeleri de kapsar.","gloss":"işaret ile kalıntı iz","neighbor_only":"Komşu dal, geçmişte var olmuş veya gerçekleşmiş bir şeyden geriye kalan izi özellikle gerektirir.","neighbor_ref":"root_000011/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da görünür bir izin başka bir şeyi tanıtması veya ona kanıt olması bakımından örtüşür."},{"boundary_match":"partial","distinction":"Komşu dalın çekirdeği işaretleme eylemine daha sıkı bağlıdır; odak dal ise konmuş işaretlerin yanında doğal kılavuzları ve bayrağı da adlandırır.","focus_only":"Odak dal doğal dağ işaretini, bayrağı, yol belirtisini ve kumaş kenarını da içine alan daha geniş bir gösterge alanına sahiptir.","gloss":"ayırt edici işaret koyma","neighbor_only":"Komşu dal özellikle atlara, varlıklara veya nesnelere tanıtma amacıyla işaret koyma eylemini öne çıkarır.","neighbor_ref":"root_000764/B004","relation_type":"near_synonym","shared_zone":"İki dal da bir varlığı başkalarından ayıracak görünür bir işaretle tanıtmayı kapsar."},{"boundary_match":"partial","distinction":"Damga bir yüzeye bilerek bırakılan fiziksel izdir; odak dalın işareti ise doğal veya yapılmış olabilir ve yön gösterme işlevi de taşıyabilir.","focus_only":"Odak dal işaret koyma dışında bayrak, dağ, yol kılavuzu ve kumaş deseni gibi bağımsız adları da kapsar.","gloss":"işaret ile damga","neighbor_only":"Komşu dal, hayvana veya nesneye yakma, kesme ya da benzeri yolla bırakılan bedensel ve maddi damgayı gerektirir.","neighbor_ref":"root_001650/B001","relation_type":"near_synonym","shared_zone":"Her iki dal görünür bir belirti aracılığıyla tanıtma ve ayırt etme işlevini paylaşır."}],"source_phrase_ar":"أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره (maqayis)؛ العلامة وهي معروفة (maqayis)؛ العلم الراية والجمع أعلام (maqayis;sihah;tahdhib)؛ العلم الجبل الطويل والجميع الأعلام (ayn)؛ العلم الجبل (sihah;mufradat)؛ المعلم الأثر يستدل به على الطريق (sihah;tahdhib)؛ علم الثوب ورقمه في أطرافه (sihah;tahdhib;mufradat)؛ أعلم الفارس إذا كانت له علامة في الحرب (maqayis;sihah;tahdhib)؛ العلام الحناء (maqayis;sihah;tahdhib;mufradat)؛ علمت عمتي أعلمها علما (tahdhib)","source_summary":"Kaynaklar ayırt edici izi ortak temel sayar ve bayrak, yüksek ya da belirgin dağ, yol göstergesi, kumaş kenarı, kına ve sonradan yerleştirilen tanıtıcı işaretleri bu temelde toplar. Tanınmış kişi ile yaklaşan son zamanın belirtisi de görünürlük ve gösterme işlevinden doğan uzantılardır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العلامة والعلم والراية والجبل والمعلم ومعالم الطريق والحدود وعلم الثوب ورقمه وتعليم الفارس والثوب والقدح والعمامة والحناء إذا جعلت علامة","what_is_not_ar":"ليس هو إدراك العلم ولا اسم الخلق ولا شق الشفة العليا"},"support_links":["sup_9b1e21f2092002400d97"]},{"boundary":"Dal yaratılmış varlıkların bütünü veya sınıflarıyla sınırlıdır; bilme durumu ve bağımsız bir fiziksel işaret anlamına gelmez.","branch_kind":"bare","branch_ref":"root_001040/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَلَّمَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Eal~ama|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:5:1:1","qac_word_ref":"96:5:1","surface_ar":"عَلَّمَ"},{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"96:5:5:1","qac_word_ref":"96:5:5","surface_ar":"يَعْلَمْ"}],"gloss":"evren ve bütün yaratılmışlar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Evren ve içindeki yaratılmış varlıkların tamamı tek bir bütün olarak adlandırılır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ad, yaratılmışların tamamı yanında onların her bir cinsini veya sınıfını ayrı bir bütün olarak da gösterebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yaratılmış bütünün kendi yaratıcısına gösterge olması, adlandırmanın açıklayıcı dayanağı olarak sunulur."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaratılmış varlıkların tümünü tek bir düzen veya bütün olarak anlatan temel kullanım için uygundur.","boundary_detail":"Dal yaratılmış varlıkların bütünü veya sınıflarıyla sınırlıdır; bilme durumu ve bağımsız bir fiziksel işaret anlamına gelmez.","branch_image_ar":"الخلق عالم يدل على صانعه","concept_gloss":"evren ve bütün yaratılmışlar","contextual_glosses":[{"applicability":"Sözün bütün evren yerine insan, görünmeyen varlıklar veya başka bir yaratık cinsi gibi ayrı sınıflara dağıtıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Her yaratık cinsinin ayrı bir bütün sayılması yönünü korur."},"facet_ids":["F002"],"text":"varlıkların her bir sınıfı","usage_role":"explanatory"}],"definition":"Yaratılmış olanların bütünü; bağlama göre evren ile içindekilerin tamamı veya yaratıkların ayrı ayrı sınıflarıdır. Bu bütünün yaratıcıyı gösteren bir belirti sayılması, adın açıklanan dayanağıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Evren ve içindeki yaratılmış varlıkların tamamı tek bir bütün olarak adlandırılır."},{"facet_id":"F002","role":"source_variant","statement":"Ad, yaratılmışların tamamı yanında onların her bir cinsini veya sınıfını ayrı bir bütün olarak da gösterebilir."},{"facet_id":"F003","role":"associated_use","statement":"Yaratılmış bütünün kendi yaratıcısına gösterge olması, adlandırmanın açıklayıcı dayanağı olarak sunulur."}],"identity_rationale":"Kaynak ifadesi, dalı yaratılmışların bütünü, gök düzeni ve içindekiler ya da yaratıkların ayrı sınıfları olarak açıklar. Her sınıfın ve bütünün yaratıcıyı gösteren bir belirti sayılması adlandırmanın gerekçesidir; bilme eylemi veya somut işaret dalıyla özdeş değildir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"evren veya yaratılmışlar bütünü"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bütün yaratıklar veya varlık sınıfları"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"evrenler, varlık dünyaları"}],"lexicalization_note":"Tanım, çıplak dalın evren, yaratılmışların bütünü ve varlık sınıfları anlamlarını verir; başka kuruluşlardan anlam aktarmaz.","neighbor_coverage_note":"Adayların çoğu hayvan bedenindeki renk ve işaretleri ya da ilgisiz özel adları anlatır; aynı kökün bilme ve işaret dalları adlandırma gerekçesini açıklasa da bu dalın yaratılmışlar bütünü sınırını keskinleştirecek bir karşıtlık oluşturmaz.","source_phrase_ar":"العالمون كل جنس من الخلق فهو في نفسه معلم وعلم (maqayis)؛ العالم الخلق والجمع العوالم (sihah)؛ العالمين رب الجن والإنس ورب الخلق كلهم (tahdhib)؛ العالم اسم للفلك وما يحويه وهو في الأصل اسم لما يعلم به (mufradat)؛ أصناف الخلائق (mufradat)","source_summary":"Kaynaklar bu adı yaratılmışların bütünü için kullanır; kapsam bazen evren ve içindekilerin tamamı, bazen de yaratıkların her bir cinsi veya sınıfıdır. Bütünün kendi yaratıcısına işaret etmesi adlandırmayı açıklayan ortak bir düşüncedir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه العالم والعالمون بمعنى الخلق أو أصناف الخلائق أو كل جنس من الخلق لأنه معلم في نفسه ودال","what_is_not_ar":"ليس هو العلم بمعنى المعرفة ولا العلم بمعنى الراية أو الجبل"},"support_links":[]},{"boundary":"Belirti özellikle üst dudakta bulunur; genel çatlaklar, alt dudak ve ağız çevresindeki başka eğrilikler kapsam dışıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001040/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَلَّمَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Eal~ama|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:5:1:1","qac_word_ref":"96:5:1","surface_ar":"عَلَّمَ"},{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"96:5:5:1","qac_word_ref":"96:5:5","surface_ar":"يَعْلَمْ"}],"gloss":"üst dudak yarığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Üst dudakta bulunan yarık, dalın anatomik çekirdeğini oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Üst dudağı yarık insan veya üst dudak bölgesinde bu belirti bulunan deve, özelliği taşıyan varlık olarak nitelenir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birinin üst dudağını yarmak, anatomik sonucun oluşturulmasını bildiren eylemsel kullanımdır."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan veya devenin üst dudak bölgesindeki belirgin yarığı adlandıran temel kullanım için uygundur.","boundary_detail":"Belirti özellikle üst dudakta bulunur; genel çatlaklar, alt dudak ve ağız çevresindeki başka eğrilikler kapsam dışıdır.","branch_image_ar":"شق ظاهر في الشفة العليا","concept_gloss":"üst dudak yarığı","contextual_glosses":[{"applicability":"Bir insanı veya deveyi üst dudak bölgesindeki yarıkla niteleyen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Özelliğin taşıyıcıda bulunmasını ve anatomik yerini korur."},"facet_ids":["F002"],"text":"üst dudağı yarık","usage_role":"contextual"},{"applicability":"Bir kişinin üst dudağında yarık oluşturma eylemini anlatan kuruluşta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemi, etkilenen kişiyi ve üst dudak sınırını korur."},"facet_ids":["F003"],"text":"üst dudağını yarmak","usage_role":"contextual"}],"definition":"İnsanın üst dudağında veya devenin üst dudak bölgesinde bulunan belirgin yarıktır. Aynı dal, bu özelliği taşıyanı niteleyen biçimi ve üst dudağı yarma eylemini de kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Üst dudakta bulunan yarık, dalın anatomik çekirdeğini oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Üst dudağı yarık insan veya üst dudak bölgesinde bu belirti bulunan deve, özelliği taşıyan varlık olarak nitelenir."},{"facet_id":"F003","role":"associated_use","statement":"Birinin üst dudağını yarmak, anatomik sonucun oluşturulmasını bildiren eylemsel kullanımdır."}],"identity_rationale":"Kaynak ifadesi dalı açıkça üst dudaktaki yarıkla sınırlar; insanın üst dudağının yarılmış olması, devenin üst dudak bölgesindeki aynı belirti ve üst dudağı yarma eylemi bu kimliği doğrular. Genel yarılma anlamı veya alt dudaktaki bir biçim bozukluğu bu dala dahil değildir.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"üst dudaktaki yarık"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"üst dudağı yarık kişi veya deve"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"üst dudağını yarmak"}],"lexicalization_note":"Üst dudak yarığı dalın temelidir; yarıklı kişi veya deve nitelemesi ile üst dudağı yarma eylemi ilgili biçimlere bağlı tutulur.","neighbor_coverage_note":"Genel yarılma dalı süreç ve kapsam farkını, ağız eğriliği dalı ise yakın anatomik karışmayı açıklar; öteki adaylar kırık iyileşmesi, hayvan yapısı veya daha uzak ayrılma türleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yer ve sonuç bakımından üst dudağa özelleşmiş anatomik bir addır; komşu dal ise nesne ve yüzey türü bakımından geniş bir yarılma eylemidir.","focus_only":"Odak dal belirli bir anatomik yerde, üst dudakta bulunan yarığı ve bu yarıkla niteleneni bildirir.","gloss":"üst dudak yarığı ile genel yarılma","neighbor_only":"Komşu dal nesne, deri, toprak, dağ ve başka yüzeylerdeki genel yarılma ve açılma sürecini kapsar.","neighbor_ref":"root_000807/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir yüzeyin ayrılmasıyla oluşan yarık düşüncesi bulunur."},{"boundary_match":"field_only","distinction":"Yarık, dokuda açılma veya ayrılmadır; eğrilik ise bir bölümün yana yönelmiş biçimidir ve üst dudakta bir açıklık gerektirmez.","focus_only":"Odak dalda üst dudak dokusunun yarılmış olması gerekir.","gloss":"dudak yarığı ile ağız eğriliği","neighbor_only":"Komşu dalda ağız, dudak veya gözün bir yana eğri oluşu vardır; doku yarığı gerekmez.","neighbor_ref":"root_000866/B003","relation_type":"same_field","shared_zone":"İki dal yüz ve ağız çevresindeki belirgin bir yapısal özelliği adlandırır."}],"source_phrase_ar":"العلم الشق في الشفة العليا والرجل أعلم (maqayis)؛ الأعلم الذي انشقت شفته العليا (ayn)؛ علم الرجل يعلم علما إذا صار أعلم وهو المشقوق الشفة العليا (sihah)؛ علمت الرجل أعلمه علما إذا شققت شفته العليا (tahdhib)؛ البعير يقال له أعلم لعلم في مشفره الأعلى (tahdhib)؛ الشق في الشفة العليا علم (mufradat)","source_summary":"Kaynaklar yarığın yerini üst dudak olarak ortak biçimde sınırlar ve yarıklı insanı bu özellikle niteler. Toplu tanıklık, devenin üst dudak bölgesindeki karşılığını ve üst dudağı yarma eylemini de aynı dalda gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العلم والشق في الشفة العليا ووصف الرجل أو البعير بالأعلم إذا كان الشق أو العلم في الموضع الأعلى","what_is_not_ar":"ليس هو العلم بمعنى المعرفة ولا العلامة الموضوعة اختيارا ولا الشق في الشفة السفلى"},"support_links":[]},{"boundary":"Deniz ile suyu bol kuyu tek bir ara nesnede birleştirilmez; bunlar aynı biçimin kaynaklarda verilen iki ayrı sözlük karşılığıdır.","branch_kind":"bare","branch_ref":"root_001040/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَلَّمَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Eal~ama|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:5:1:1","qac_word_ref":"96:5:1","surface_ar":"عَلَّمَ"},{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"96:5:5:1","qac_word_ref":"96:5:5","surface_ar":"يَعْلَمْ"}],"gloss":"deniz ya da suyu bol kuyu","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dal, aynı adın iki ayrı su varlığına verilen sözlük karşılıklarını birlikte kaydeder."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kaynak karşılığında ad, geniş tuzlu su kütlesi olan denizi gösterir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Diğer ve daha yaygın kaynak karşılığında ad, suyu çok olan kuyuyu gösterir."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözlük biçiminin kaynaklarda verilen iki ayrı karşılığını eksiltmeden birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Deniz ile suyu bol kuyu tek bir ara nesnede birleştirilmez; bunlar aynı biçimin kaynaklarda verilen iki ayrı sözlük karşılığıdır.","branch_image_ar":"ماء كثير مجتمع في عيلم","concept_gloss":"deniz ya da suyu bol kuyu","contextual_glosses":[{"applicability":"Sözlük biçiminin geniş su kütlesi karşılığıyla kullanıldığı tanıklığa özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı biçim için tanıklanan suyu bol kuyu karşılığını dışarıda bırakır.","preserves":"Deniz karşılığını doğal ve doğrudan biçimde korur."},"facet_ids":["F002"],"text":"deniz","usage_role":"contextual"},{"applicability":"Sözlük biçiminin bol su içeren kuyu karşılığıyla kullanıldığı tanıklıklara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı biçim için tanıklanan deniz karşılığını dışarıda bırakır.","preserves":"Kuyu türünü ve suyunun çokluğu koşulunu korur."},"facet_ids":["F003"],"text":"suyu bol kuyu","usage_role":"contextual"}],"definition":"Aynı sözlük biçiminin bir kullanımda denizi, başka bir kullanımda ise suyu bol kuyuyu adlandırmasıdır. İki karşılık, genel bir su birikintisi anlamında kaynaştırılmaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dal, aynı adın iki ayrı su varlığına verilen sözlük karşılıklarını birlikte kaydeder."},{"facet_id":"F002","role":"source_variant","statement":"Bir kaynak karşılığında ad, geniş tuzlu su kütlesi olan denizi gösterir."},{"facet_id":"F003","role":"source_variant","statement":"Diğer ve daha yaygın kaynak karşılığında ad, suyu çok olan kuyuyu gösterir."}],"identity_rationale":"Kaynak ifadesi tek bir su birikimi türü tanımlamaz; aynı sözlük biçimi için deniz ve suyu bol kuyu olmak üzere iki ayrı karşılık verir. Dal korunabilir, ancak geçici çerçevedeki ortak su kütlesi görüntüsü yerine bu açık seçeneklilik tanıma yazılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"deniz"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"suyu bol kuyu"}],"lexicalization_note":"Tanım çıplak sözlük biçiminin deniz ve suyu bol kuyu karşılıklarını ayrı ayrı korur; bunlardan genel bir su birikintisi anlamı türetmez.","neighbor_coverage_note":"Deniz karşılığını açıklayan geniş su dalı ile kuyu çevresindeki bol su dalı seçildi; diğer adaylar gölet, artık su, taşkın veya su tutan arazi gibi farklı taşıyıcı ve süreçlere bağlıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Örtüşme yalnızca deniz karşılığındadır; odak dalın kuyu seçeneği komşuda bulunmaz, komşunun büyük ırmak ve genel su genişliği ise odak dalın tanımına girmez.","focus_only":"Odak dal aynı sözlük biçiminin suyu bol kuyu karşılığını da bağımsız bir seçenek olarak taşır.","gloss":"deniz ve geniş su","neighbor_only":"Komşu dal deniz yanında büyük ırmak ve farklı büyüklükte su alanlarına uzanan genel bir geniş su kapsamına sahiptir.","neighbor_ref":"root_000086/B001","relation_type":"near_synonym","shared_zone":"Odak dalın deniz karşılığı, komşu dalın geniş ve çok su çekirdeğiyle örtüşür."},{"boundary_match":"partial","distinction":"Odak dal suyu taşıyan kuyuyu niteler; komşu dal ise kuyudan dökülen suyu ve taşma sürecini merkez alır.","focus_only":"Odak dal kuyunun kendisini suyunun bol olması koşuluyla adlandırır.","gloss":"suyu bol kuyu ile kuyu suyu","neighbor_only":"Komşu dal kuyudaki kovadan dökülen veya havuza taşan suyu, kokusunu ve taşma olayını anlatır.","neighbor_ref":"root_001077/B003","relation_type":"near_neighbor","shared_zone":"İki dal kuyu çevresinde suyun çokluğu ve görünür birikimiyle ilişkilidir."}],"source_phrase_ar":"العيلم يقال إنه البحر ويقال إنه البئر الكثيرة الماء (maqayis)؛ العيلم الركية الكثيرة الماء (sihah)؛ العيلم البئر الكثيرة الماء (tahdhib)","source_summary":"Toplu tanıklık iki karşılığı yan yana verir: bir aktarım sözcüğü deniz olarak açıklar, öteki tanıklıklar ise suyu bol kuyu anlamını destekler. Kaynaklara özgü ayrı claim kimlikleri bulunmadığı için bu karşıtlık ortak özet içinde, atıf uydurulmadan korunur.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه العيلم بمعنى البحر أو البئر الكثيرة الماء","what_is_not_ar":"ليس هو العالمين ولا العلم ولا العلامة ولا العيلم بمعنى آخر غير مائي"},"support_links":[]},{"boundary":"Çekirdek yırtıcı kuş adıdır; çevik ve zeki erkek nitelemesi yalnızca bu addan türeyen biçime bağlıdır.","branch_kind":"bare","branch_ref":"root_001040/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَلَّمَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Eal~ama|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:5:1:1","qac_word_ref":"96:5:1","surface_ar":"عَلَّمَ"},{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"96:5:5:1","qac_word_ref":"96:5:5","surface_ar":"يَعْلَمْ"}],"gloss":"doğan veya atmaca türü yırtıcı kuş","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ad, doğan veya atmaca türünden avcı bir kuşu gösterir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuş adından türeyen insan nitelemesi, çevik ve zeki bir erkeği belirtir."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın temel kuş adını iki kaynak karşılığı arasındaki seçenekliliği koruyarak açıklamak için uygundur.","boundary_detail":"Çekirdek yırtıcı kuş adıdır; çevik ve zeki erkek nitelemesi yalnızca bu addan türeyen biçime bağlıdır.","branch_image_ar":"طائر جارح يسمى العلام","concept_gloss":"doğan veya atmaca türü yırtıcı kuş","contextual_glosses":[{"applicability":"Kuş adından türemiş insan nitelemesinin kullanıldığı bağlama özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan oluşu ile çeviklik ve zekâ niteliklerini birlikte korur."},"facet_ids":["F002"],"text":"çevik ve zeki adam","usage_role":"contextual"}],"definition":"Doğan veya atmaca türünden bir yırtıcı kuş adıdır. Bu kuş adından türetilen bir niteleme, çevik ve zeki bir erkeği anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ad, doğan veya atmaca türünden avcı bir kuşu gösterir."},{"facet_id":"F002","role":"associated_use","statement":"Kuş adından türeyen insan nitelemesi, çevik ve zeki bir erkeği belirtir."}],"identity_rationale":"Kaynak ifadesi temel adı doğan veya atmaca türünden yırtıcı kuş için verir ve geçici dal görüntüsünü doğrular. Çevik ve zeki erkek nitelemesi ise kuş adından türetilmiş ayrı bir biçimdir; kuşun tanımına doğrudan katılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"doğan veya atmaca"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"çevik ve zeki adam"}],"lexicalization_note":"Çıplak dal doğan veya atmaca türünden kuş adını tanımlar; insan nitelemesi türemiş bir sözcüksel uzantı olarak bağımlı tutulur.","neighbor_coverage_note":"Yırtıcı kuş sınıfında en yakın iki aday seçildi; diğer adaylar kanat çırpma, beslenme, farklı hayvan adları veya yalnızca uzak bir doğan ilişkisi taşır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Aynı kuş alanını paylaşsalar da komşu dal renk ve ara tür özellikleriyle daha dar bir kuşu adlandırır; odak dalın türemiş insan nitelemesi de komşuda yoktur.","focus_only":"Odak dal doğan veya atmaca karşılığı taşıyan kuş adını ve ondan türeyen insan nitelemesini içerir.","gloss":"yırtıcı kuş adları","neighbor_only":"Komşu dal mavi renkli, doğan ile atmaca arasında tanımlanan veya beyaz doğan sayılan daha özel bir kuş adıdır.","neighbor_ref":"root_000631/B002","relation_type":"same_field","shared_zone":"Her iki dal doğan ve atmaca çevresindeki avcı kuş adlandırmaları alanındadır."},{"boundary_match":"partial","distinction":"Odak dalda zekâ kuştan türetilen insan niteliğinde belirginleşir; komşuda ise doğrudan belirli doğanların özelliğidir.","focus_only":"Odak dal doğan veya atmaca türünü genel bir adla karşılar ve bu addan insan nitelemesi türetir.","gloss":"doğan adı ile zeki doğan nitelemesi","neighbor_only":"Komşu dal özellikle zeki ve keskin bakışlı doğanlara verilen bir adı belirtir.","neighbor_ref":"root_001375/B006","relation_type":"near_neighbor","shared_zone":"İki dal doğan türünden yırtıcı kuşları adlandırır ve zekâ çağrışımını paylaşır."}],"source_phrase_ar":"العلام الصقر؛ العلامي الرجل الخفيف الذكي مأخوذ من العلام؛ العلام الباشق (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık temel adı doğan veya atmaca türünden kuş için verir ve türemiş biçimi çevik, zeki erkek olarak açıklar."}],"source_summary":"Dal tek bir sözlük tanıklığında yırtıcı kuş adı ile bu addan türetilmiş çevik ve zeki erkek nitelemesini birlikte sunar.","sources":["TA"],"what_is_ar":"يدخل فيه العلام بمعنى الصقر أو الباشق وما نسب إليه من العلامي","what_is_not_ar":"ليس هو العلام بمعنى الحناء ولا العلامة ولا العالم"},"support_links":[]},{"boundary":"Dal yalnızca erkek sırtlanı adlandırır; başka erkek hayvan adları ve benzer sesli su veya kuş adları kapsam dışıdır.","branch_kind":"bare","branch_ref":"root_001040/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَلَّمَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Eal~ama|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:5:1:1","qac_word_ref":"96:5:1","surface_ar":"عَلَّمَ"},{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"96:5:5:1","qac_word_ref":"96:5:5","surface_ar":"يَعْلَمْ"}],"gloss":"erkek sırtlan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Adlandırılan canlı, cinsiyeti erkek olan sırtlandır."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvanın türünü ve erkek oluşunu birlikte veren bütün bağlamlarda tam karşılıktır.","boundary_detail":"Dal yalnızca erkek sırtlanı adlandırır; başka erkek hayvan adları ve benzer sesli su veya kuş adları kapsam dışıdır.","branch_image_ar":"ذكر الضباع يسمى العيلام","concept_gloss":"erkek sırtlan","definition":"Erkek sırtlanı adlandıran yalın bir hayvan adıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Adlandırılan canlı, cinsiyeti erkek olan sırtlandır."}],"identity_rationale":"Kaynak ifadesinin iki tanıklığı da sözcüğü doğrudan erkek sırtlan olarak açıklar. Geçici dal görüntüsü bu yalın hayvan adıyla tam uyumludur ve başka bir tür, özellik veya mecaz eklemeyi gerektirmez.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"erkek sırtlan"}],"lexicalization_note":"Tanım çıplak hayvan adını erkek sırtlanla sınırlar ve başka türlere ya da bağlı kuruluşlara genişletmez.","neighbor_coverage_note":"Erkek sırtlanı aynı sınırlarla adlandıran aday tam eş anlamlı olarak seçildi; diğer adaylar kurt, erkek domuz, aslan, kuş veya daha geniş hayvan sınıflarıdır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Anlam çekirdeği, hayvan türü ve cinsiyet sınırı aynıdır; ayrım yalnızca kullanılan sözlük biçimindedir.","focus_only":null,"gloss":"erkek sırtlan","neighbor_only":null,"neighbor_ref":"root_001068/B007","relation_type":"synonym","shared_zone":"Her iki dal da hiçbir ek koşul getirmeden erkek sırtlanı adlandırır."}],"source_phrase_ar":"العيلام الذكر من الضباع (sihah)؛ العيلام الضبعان وهو ذكر الضباع (tahdhib)","source_summary":"Kaynaklar sözcüğün erkek sırtlanı adlandırdığı konusunda birleşir ve ek bir anlam ayrımı bildirmez.","sources":["SI","TA"],"what_is_ar":"يدخل فيه العيلام بمعنى ذكر الضباع","what_is_not_ar":"ليس هو العيلم البئر الكثيرة الماء ولا العلامة ولا العلم"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["96:5:1"],"branch_refs":[],"candidate_id":"cand_d86454b52fac3b599fac","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:5:1:boundary-argument-completion","source_type":"word_analysis","support_ids":["sup_744f1e7e605a856e4514","sup_93a859ca626f78eb4297"],"title":"instrument-only teaching receives whom and what","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:1","qac_refs":["96:5:1:1"],"status":"accepted"}},{"anchor_refs":["96:5:1"],"branch_refs":[],"candidate_id":"cand_cfdb51081ac63d330f3a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:5:1:completed-divine-predication","source_type":"word_analysis","support_ids":["sup_5da606ce320ba51d3d52","sup_93a859ca626f78eb4297"],"title":"completed act continues the divine subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:1","qac_refs":["96:5:1:1"],"status":"accepted"}},{"anchor_refs":["96:5:1"],"branch_refs":[],"candidate_id":"cand_270b17e44c0fad1cdcb3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:5:1:double-object-teaching","source_type":"word_analysis","support_ids":["sup_5c5b6e1753f51538fc7a","sup_93a859ca626f78eb4297"],"title":"teaching frame has recipient and content","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:1","qac_refs":["96:5:1:1"],"status":"accepted"}},{"anchor_refs":["96:5:1"],"branch_refs":[],"candidate_id":"cand_79fc4b82b36c02e32d62","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:5:1:epistemic-agency","source_type":"word_analysis","support_ids":["sup_6757ee2a4930c18fb066","sup_93a859ca626f78eb4297"],"title":"divine agency precedes human knowing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:1","qac_refs":["96:5:1:1"],"status":"accepted"}},{"anchor_refs":["96:5:1"],"branch_refs":[],"candidate_id":"cand_0b36cb890c807b67c00c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:5:1:form-ii-caused-knowing","source_type":"word_analysis","support_ids":["sup_63ced5471f7c6c19258b","sup_93a859ca626f78eb4297"],"title":"caused knowing rather than mere informing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:1","qac_refs":["96:5:1:1"],"status":"accepted"}},{"anchor_refs":["96:5:1"],"branch_refs":[],"candidate_id":"cand_8a3b6344937eb84e1cd5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:5:1:geminated-causative-sound","source_type":"word_analysis","support_ids":["sup_93a859ca626f78eb4297","sup_df1aa9952f41a01c1850"],"title":"gemination makes causation audible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:1","qac_refs":["96:5:1:1"],"status":"accepted"}},{"anchor_refs":["96:5:1"],"branch_refs":[],"candidate_id":"cand_56fc3edfeeb36581a830","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:5:1:generic-teaching-formula","source_type":"word_analysis","support_ids":["sup_08a66e616a90bc688321","sup_93a859ca626f78eb4297"],"title":"Adam-teaching pattern becomes human-wide","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:1","qac_refs":["96:5:1:1"],"status":"accepted"}},{"anchor_refs":["96:5:1"],"branch_refs":[],"candidate_id":"cand_9b5115cb785b5a86ba22","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:5:1:knowledge-human-pairing","source_type":"word_analysis","support_ids":["sup_2620737ae4f6fb5eed85","sup_93a859ca626f78eb4297"],"title":"human-knowledge pairing becomes syntactic","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:1","qac_refs":["96:5:1:1"],"status":"accepted"}},{"anchor_refs":["96:5:1"],"branch_refs":[],"candidate_id":"cand_4c6da0ddc6f2ffc24623","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:5:1:root-echo-and-boundary-completion","source_type":"word_analysis","support_ids":["sup_256c361504576a462055","sup_93a859ca626f78eb4297"],"title":"pen-teaching expands into specified teaching","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:1","qac_refs":["96:5:1:1"],"status":"accepted"}},{"anchor_refs":["96:5:2"],"branch_refs":[],"candidate_id":"cand_14ab6b2d6f5aede4153e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:5:2:antecedent-of-knowing","source_type":"word_analysis","support_ids":["sup_3fcde15b14071c2ab4ce","sup_fb0ca3df2726a2037024"],"title":"recipient becomes hidden subject of knowing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:2","qac_refs":["96:5:2:1","96:5:2:2"],"status":"accepted"}},{"anchor_refs":["96:5:2"],"branch_refs":[],"candidate_id":"cand_4628264a38da66ba1a7c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:5:2:audible-recipient-boundary","source_type":"word_analysis","support_ids":["sup_3fcde15b14071c2ab4ce","sup_f4b71071e74d265edce4"],"title":"hamza entry makes the recipient stand out","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:2","qac_refs":["96:5:2:1","96:5:2:2"],"status":"accepted"}},{"anchor_refs":["96:5:2"],"branch_refs":[],"candidate_id":"cand_6a25c0bf696a8e25fc6d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:5:2:creation-teaching-recurrence","source_type":"word_analysis","support_ids":["sup_3fcde15b14071c2ab4ce","sup_521be931b1d6ad74cbdc"],"title":"creation-teaching formula lands on the human noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:2","qac_refs":["96:5:2:1","96:5:2:2"],"status":"accepted"}},{"anchor_refs":["96:5:2"],"branch_refs":[],"candidate_id":"cand_93eac45ce7f8ff388680","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:5:2:etymology-pressure","source_type":"word_analysis","support_ids":["sup_3fcde15b14071c2ab4ce","sup_a88cb5bc241ef0f27deb"],"title":"receptivity and forgetfulness remain lexical pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:2","qac_refs":["96:5:2:1","96:5:2:2"],"status":"accepted"}},{"anchor_refs":["96:5:2"],"branch_refs":[],"candidate_id":"cand_6e72e20b05e06da35471","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:5:2:generic-singular-human","source_type":"word_analysis","support_ids":["sup_3fcde15b14071c2ab4ce","sup_fd935491f351ca9a1e3b"],"title":"definite singular carries a species claim","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:2","qac_refs":["96:5:2:1","96:5:2:2"],"status":"accepted"}},{"anchor_refs":["96:5:2"],"branch_refs":[],"candidate_id":"cand_af44f13b9290f026d596","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:5:2:human-knowledge-sandwich","source_type":"word_analysis","support_ids":["sup_3fcde15b14071c2ab4ce","sup_e2bb2caf851b695917ae"],"title":"human noun sits between teaching and knowing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:2","qac_refs":["96:5:2:1","96:5:2:2"],"status":"accepted"}},{"anchor_refs":["96:5:2"],"branch_refs":[],"candidate_id":"cand_a7a35beb7a8c4cb1668d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:5:2:same-surah-human-arc","source_type":"word_analysis","support_ids":["sup_2631dcac0ec7b9efadaf","sup_3fcde15b14071c2ab4ce"],"title":"created, taught, then oversteps","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:2","qac_refs":["96:5:2:1","96:5:2:2"],"status":"accepted"}},{"anchor_refs":["96:5:2"],"branch_refs":[],"candidate_id":"cand_843d553b066e93388460","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:5:2:taught-recipient","source_type":"word_analysis","support_ids":["sup_3fcde15b14071c2ab4ce","sup_67e3bf60f21567732d03"],"title":"accusative human is the taught object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:2","qac_refs":["96:5:2:1","96:5:2:2"],"status":"accepted"}},{"anchor_refs":["96:5:3"],"branch_refs":[],"candidate_id":"cand_fb7970f8622c4144fc0b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:5:3:negation-internal-to-relative","source_type":"word_analysis","support_ids":["sup_0cc06b801f91ca3fdd78","sup_d4421c252c8943a55b9a"],"title":"internal negation defines the relative content","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:3","qac_refs":["96:5:3:1"],"status":"accepted"}},{"anchor_refs":["96:5:3"],"branch_refs":[],"candidate_id":"cand_277edae5a83be1931cb9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:5:3:open-ended-content","source_type":"word_analysis","support_ids":["sup_5945ca433ef212a952ac","sup_d4421c252c8943a55b9a"],"title":"content is defined by prior absence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:3","qac_refs":["96:5:3:1"],"status":"accepted"}},{"anchor_refs":["96:5:3"],"branch_refs":[],"candidate_id":"cand_564ea1c5c5a6a16986c9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:5:3:relative-over-masdariyya","source_type":"word_analysis","support_ids":["sup_c649ba14d4194923570a","sup_d4421c252c8943a55b9a"],"title":"relative reading is primary over source reading","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:3","qac_refs":["96:5:3:1"],"status":"accepted"}},{"anchor_refs":["96:5:3"],"branch_refs":[],"candidate_id":"cand_8789f2110a67a845d929","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:5:3:second-object-relative","source_type":"word_analysis","support_ids":["sup_2d5789d81dffd0b8a4a7","sup_d4421c252c8943a55b9a"],"title":"relative word fills the second object slot","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:3","qac_refs":["96:5:3:1"],"status":"accepted"}},{"anchor_refs":["96:5:3"],"branch_refs":[],"candidate_id":"cand_aacb40795ac323ea440d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:5:3:two-object-routes","source_type":"word_analysis","support_ids":["sup_d4421c252c8943a55b9a","sup_fd4835d8748b8ec3e744"],"title":"pivot position keeps two routes visible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:3","qac_refs":["96:5:3:1"],"status":"accepted"}},{"anchor_refs":["96:5:4"],"branch_refs":[],"candidate_id":"cand_02b3c5dc5dd00bf77787","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:5:4:boundary-from-method-to-condition","source_type":"word_analysis","support_ids":["sup_361b53217fa285ad6dd1","sup_ca7dac67930421a5816a"],"title":"instrument gives way to prior absence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:4","qac_refs":["96:5:4:1"],"status":"accepted"}},{"anchor_refs":["96:5:4"],"branch_refs":[],"candidate_id":"cand_1d3647a9e4a987727ed4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:5:4:cadence-arrest","source_type":"word_analysis","support_ids":["sup_361b53217fa285ad6dd1","sup_f11cdbda4eda4a9b1cd2"],"title":"clipped particle arrests the phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:4","qac_refs":["96:5:4:1"],"status":"accepted"}},{"anchor_refs":["96:5:4"],"branch_refs":[],"candidate_id":"cand_e89e57efd743c447f048","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:5:4:jussive-governance","source_type":"word_analysis","support_ids":["sup_361b53217fa285ad6dd1","sup_382cff852ae2ea94aa66"],"title":"particle governs the final verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:4","qac_refs":["96:5:4:1"],"status":"accepted"}},{"anchor_refs":["96:5:4"],"branch_refs":[],"candidate_id":"cand_80b24d5efa47d0621ded","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:5:4:prior-ignorance-baseline","source_type":"word_analysis","support_ids":["sup_361b53217fa285ad6dd1","sup_fdfc5dd39cadd006f83e"],"title":"negative baseline answers positive teaching","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:4","qac_refs":["96:5:4:1"],"status":"accepted"}},{"anchor_refs":["96:5:4"],"branch_refs":[],"candidate_id":"cand_3c8c649bb90fda801fd9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:5:4:tight-negation-scope","source_type":"word_analysis","support_ids":["sup_361b53217fa285ad6dd1","sup_fde7033c49a243d27724"],"title":"negation stays inside the relative clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:4","qac_refs":["96:5:4:1"],"status":"accepted"}},{"anchor_refs":["96:5:5"],"branch_refs":[],"candidate_id":"cand_831b3b05f2f4c1bdf409","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:5:5:ayah-closure","source_type":"word_analysis","support_ids":["sup_e19ca26ffb9049da2ba9","sup_fd9eab52b2ac2e815466"],"title":"final word lands on knowledge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:5","qac_refs":["96:5:5:1"],"status":"accepted"}},{"anchor_refs":["96:5:5"],"branch_refs":[],"candidate_id":"cand_5eefed7e5ffeb1b94e9d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:5:5:form-i-form-ii-echo","source_type":"word_analysis","support_ids":["sup_afb7c055a2d9847b7e1a","sup_e19ca26ffb9049da2ba9"],"title":"Form I knowing answers Form II teaching","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:5","qac_refs":["96:5:5:1"],"status":"accepted"}},{"anchor_refs":["96:5:5"],"branch_refs":[],"candidate_id":"cand_3260612a2a0221ed027d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:5:5:hidden-human-subject","source_type":"word_analysis","support_ids":["sup_6a29c6cd2ce1cf81b29c","sup_e19ca26ffb9049da2ba9"],"title":"hidden subject returns to the human","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:5","qac_refs":["96:5:5:1"],"status":"accepted"}},{"anchor_refs":["96:5:5"],"branch_refs":[],"candidate_id":"cand_e70e7ba27dff47df70bc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:5:5:jussive-negated-knowing","source_type":"word_analysis","support_ids":["sup_39ca55a7527a792c9254","sup_e19ca26ffb9049da2ba9"],"title":"verb bears the particle's jussive effect","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:5","qac_refs":["96:5:5:1"],"status":"accepted"}},{"anchor_refs":["96:5:5"],"branch_refs":[],"candidate_id":"cand_8f02ba485cc188e5d77c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:5:5:knowledge-not-opinion","source_type":"word_analysis","support_ids":["sup_e19ca26ffb9049da2ba9","sup_f7779de5ecf1935ded86"],"title":"negation denies real knowing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:5","qac_refs":["96:5:5:1"],"status":"accepted"}},{"anchor_refs":["96:5:5"],"branch_refs":[],"candidate_id":"cand_2a42b9d30a8a8220f9eb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:5:5:pen-and-sound-thread","source_type":"word_analysis","support_ids":["sup_51ac969cb62562db4889","sup_e19ca26ffb9049da2ba9"],"title":"pen line resolves into knowing endpoint","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:5","qac_refs":["96:5:5:1"],"status":"accepted"}},{"anchor_refs":["96:5:5"],"branch_refs":[],"candidate_id":"cand_52503207435734008bed","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:5:5:recoverable-object-through-ma","source_type":"word_analysis","support_ids":["sup_9f463bd07aef5ae51fd3","sup_e19ca26ffb9049da2ba9"],"title":"object is recovered from the relative word","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:5","qac_refs":["96:5:5:1"],"status":"accepted"}},{"anchor_refs":["96:5:5"],"branch_refs":[],"candidate_id":"cand_1953e77f740b19883596","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:5:5:same-surah-reminder","source_type":"word_analysis","support_ids":["sup_e19ca26ffb9049da2ba9","sup_eadb0d4bf08e30f495fd"],"title":"later question reopens the knowing formula","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:5:5","qac_refs":["96:5:5:1"],"status":"accepted"}},{"anchor_refs":["96:5:1"],"branch_refs":[],"candidate_id":"cand_9d0ea253b9aba0dcc653","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:5:1:1","source_type":"qac_morpheme","support_ids":["sup_820223d8d5040bdfb6c0"],"title":"QAC root occurrence: ع ل م","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["96:5:2"],"branch_refs":[],"candidate_id":"cand_4e9a330497c276967e0a","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000059"],"scope":"focus_ayah","source_local_id":"96:5:2:2","source_type":"qac_morpheme","support_ids":["sup_878b0d8a38dced305211"],"title":"QAC root occurrence: ء ن س","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["96:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"96:5","branch_refs":["root_000059/B002","root_001040/B001"],"candidate_id":"cand_441a1b413958f88f8b7e","commentary_obligation":"review","hft_ref":"hft_4ee82f658a07efc1fc3f","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_disclosure_transition","source_type":"hft","support_ids":["sup_9205e7b0ebdb213fb659"],"title":"baseline_disclosure_transition","trust":"legacy_unbound"},{"anchor_refs":["96:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"96:5","branch_refs":["root_000059/B004","root_001040/B002"],"candidate_id":"cand_9d6ead9ebd3579a2fb9d","commentary_obligation":"review","hft_ref":"hft_3a13a5d6534ae03272c3","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_marker_navigation","source_type":"hft","support_ids":["sup_9b1e21f2092002400d97"],"title":"baseline_marker_navigation","trust":"legacy_unbound"},{"anchor_refs":["96:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"96:5","branch_refs":["root_000059/B003","root_001040/B001"],"candidate_id":"cand_d583ab28ad614543cc0d","commentary_obligation":"review","hft_ref":"hft_17c4bfdc35c3e69a12eb","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_unknown_familiarized","source_type":"hft","support_ids":["sup_52563ea186b9584513c1"],"title":"baseline_unknown_familiarized","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"عَلَّمَ ٱلْإِنسَٰنَ مَا لَمْ يَعْلَمْ","qac_morphemes":[{"lemma_ar":"عَلَّمَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Eal~ama|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:5:1:1","qac_word_ref":"96:5:1","root_ar":"ع ل م","surface_ar":"عَلَّمَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"96:5:2:1","qac_word_ref":"96:5:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"96:5:2:2","qac_word_ref":"96:5:2","root_ar":"ء ن س","surface_ar":"إِنسَٰنَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:REL|LEM:maA","morpheme_role":"STEM","pos":"REL","qac_ref":"96:5:3:1","qac_word_ref":"96:5:3","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"لَم","morph_features":"STEM|POS:NEG|LEM:lam","morpheme_role":"STEM","pos":"NEG","qac_ref":"96:5:4:1","qac_word_ref":"96:5:4","root_ar":"","surface_ar":"لَمْ"},{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"96:5:5:1","qac_word_ref":"96:5:5","root_ar":"ع ل م","surface_ar":"يَعْلَمْ"}],"word_analysis_qac_refs":[["96:5:1:1"],["96:5:2:1","96:5:2:2"],["96:5:3:1"],["96:5:4:1"],["96:5:5:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["96:5:1","96:5:2","96:5:3","96:5:4","96:5:5"]},"focus_surface_evidence":{"arabic_uthmani":"عَلَّمَ ٱلْإِنسَٰنَ مَا لَمْ يَعْلَمْ","qac_morphemes":[{"lemma_ar":"عَلَّمَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Eal~ama|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:5:1:1","qac_word_ref":"96:5:1","root_ar":"ع ل م","surface_ar":"عَلَّمَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"96:5:2:1","qac_word_ref":"96:5:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"96:5:2:2","qac_word_ref":"96:5:2","root_ar":"ء ن س","surface_ar":"إِنسَٰنَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:REL|LEM:maA","morpheme_role":"STEM","pos":"REL","qac_ref":"96:5:3:1","qac_word_ref":"96:5:3","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"لَم","morph_features":"STEM|POS:NEG|LEM:lam","morpheme_role":"STEM","pos":"NEG","qac_ref":"96:5:4:1","qac_word_ref":"96:5:4","root_ar":"","surface_ar":"لَمْ"},{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|3MS|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"96:5:5:1","qac_word_ref":"96:5:5","root_ar":"ع ل م","surface_ar":"يَعْلَمْ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["96:5:1:1"],["96:5:2:1","96:5:2:2"],["96:5:3:1"],["96:5:4:1"],["96:5:5:1"]],"word_analysis_refs":["96:5:1","96:5:2","96:5:3","96:5:4","96:5:5"],"word_rows":[{"analysis_record_ref":"96:5:1","analytic_gloss_range_en":"completed Form II teaching that causes knowledge in a recipient and governs both the taught human and the taught content","analytic_root_gloss_range_en":"the root range centers on knowing, teaching, learning, and informing, with separate branches for marks, created realms, and rarer nominal images; this local Form II verb selects caused knowing","qac_refs":["96:5:1:1"],"root":{"arabic":"ع ل م","transliteration":"ʿ-l-m"},"surface":{"arabic":"عَلَّمَ","transliteration":"ʿallama"}},{"analysis_record_ref":"96:5:2","analytic_gloss_range_en":"definite singular generic human as the first taught object and later antecedent of the hidden knowing subject","analytic_root_gloss_range_en":"the aligned root field supports human familiarity, sociability, and receptivity; the classical forgetfulness derivation remains lexical pressure but does not replace the aligned local root","qac_refs":["96:5:2:1","96:5:2:2"],"root":{"arabic":"أ ن س","transliteration":"ʾ-n-s"},"surface":{"arabic":"ٱلْإِنسَٰنَ","transliteration":"al-insāna"}},{"analysis_record_ref":"96:5:3","analytic_gloss_range_en":"open relative content functioning as the second object of teaching and as the recoverable object inside the knowing clause","analytic_root_gloss_range_en":null,"qac_refs":["96:5:3:1"],"root":{},"surface":{"arabic":"مَا","transliteration":"mā"}},{"analysis_record_ref":"96:5:4","analytic_gloss_range_en":"jussive negation particle with tight scope over the following imperfect, marking prior non-knowing inside the relative clause","analytic_root_gloss_range_en":null,"qac_refs":["96:5:4:1"],"root":{},"surface":{"arabic":"لَمْ","transliteration":"lam"}},{"analysis_record_ref":"96:5:5","analytic_gloss_range_en":"Form I imperfect knowing, made jussive and negated by the preceding particle, with its object recovered through the relative word","analytic_root_gloss_range_en":"the root range centers on knowing and teaching while also containing separate sign, mark, created-realm, and rare nominal branches; this local Form I verb selects human knowing as the negated baseline","qac_refs":["96:5:5:1"],"root":{"arabic":"ع ل م","transliteration":"ʿ-l-m"},"surface":{"arabic":"يَعْلَمْ","transliteration":"yaʿlam"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["96:5"],"branch_refs":["root_000059/B002","root_001040/B001"],"candidate_id":"cand_441a1b413958f88f8b7e","evidence_scope":"focus_ayah","hft_ref":"hft_4ee82f658a07efc1fc3f","item_id":"baseline_disclosure_transition","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_disclosure_transition","support_id":"sup_9205e7b0ebdb213fb659"},{"anchor_refs":["96:5"],"branch_refs":["root_000059/B004","root_001040/B002"],"candidate_id":"cand_9d6ead9ebd3579a2fb9d","evidence_scope":"focus_ayah","hft_ref":"hft_3a13a5d6534ae03272c3","item_id":"baseline_marker_navigation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_marker_navigation","support_id":"sup_9b1e21f2092002400d97"},{"anchor_refs":["96:5"],"branch_refs":["root_000059/B003","root_001040/B001"],"candidate_id":"cand_d583ab28ad614543cc0d","evidence_scope":"focus_ayah","hft_ref":"hft_17c4bfdc35c3e69a12eb","item_id":"baseline_unknown_familiarized","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_unknown_familiarized","support_id":"sup_52563ea186b9584513c1"}],"diagnostics":[],"lane_counts":{"global":10,"macro":13,"micro":3},"packet_summary":{"ayah_count":19,"focus_ref":"96:5","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ص ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":false,"target_occurrences":7,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"د ع و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000478","furuq_root_norm":"د ع و","furuq_source_root_norm":"د ع و","is_dominant":true,"target_occurrences":77,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000477","furuq_root_norm":"د ع ع","furuq_source_root_norm":"د ع ع","is_dominant":false,"target_occurrences":22,"target_rank":2}]},{"qac_root":"ن د و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001487","furuq_root_norm":"ن د ي","furuq_source_root_norm":"ن د ي","is_dominant":true,"target_occurrences":33,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001486","furuq_root_norm":"ن د و","furuq_source_root_norm":"ن د و","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001563","furuq_root_norm":"ن و د","furuq_source_root_norm":"ن و د","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ط و ع","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000956","furuq_root_norm":"ط و ع","furuq_source_root_norm":"ط و ع","is_dominant":true,"target_occurrences":96,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000706","furuq_root_norm":"س ط ع","furuq_source_root_norm":"س ط ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["96:1","96:2","96:3","96:4","96:5","96:6","96:7","96:8","96:9","96:10","96:11","96:12","96:13","96:14","96:15","96:16","96:17","96:18","96:19"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"96:5","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":16,"unstructured_record_count":0},"identity":{"ayah_ref":"96:5","lane":"micro","linguistic_source_ref":"96:5","surface_ref":"96:5","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"96:5","target_tokens":[["İnsana",["96:5:2"]],["bilmediğini",["96:5:3","96:5:4","96:5:5"]],["öğretti",["96:5:1"]]],"text":"İnsana bilmediğini öğretti."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":19,"id":"s096-p01-001-019","label":"Whole surah","number":1,"refs":["96:1","96:2","96:3","96:4","96:5","96:6","96:7","96:8","96:9","96:10","96:11","96:12","96:13","96:14","96:15","96:16","96:17","96:18","96:19"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:1:generic-teaching-formula","source_type":"word_analysis","support_id":"sup_08a66e616a90bc688321","text":"{\"blocking_evidence\":null,\"headline\":\"Adam-teaching pattern becomes human-wide\",\"reader_payoff\":\"The reader sees the teaching formula that is specific to Adam in 2:31 widen here into a generic human claim, with creation-teaching resonance also visible in 55:3-4.\",\"reason\":\"The CRITICAL rows cite 2:31 and 55:3-4, while the local grammar has the same Form II teaching verb governing the generic human object.\",\"representative_source_ids\":[\"QI-2d2e1eb7\",\"QI-879b7f99\",\"MI-dc2c9427\",\"QE-1df2e207\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:3:negation-internal-to-relative","source_type":"word_analysis","support_id":"sup_0cc06b801f91ca3fdd78","text":"{\"blocking_evidence\":null,\"headline\":\"internal negation defines the relative content\",\"reader_payoff\":\"The reader notices that negation belongs inside the content clause rather than reaching back to deny the teaching act.\",\"reason\":\"The attachment evidence confines the negation to the following verb inside the relative clause while this word remains the object of teaching.\",\"representative_source_ids\":[\"QG-2e6ba915\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:1:root-echo-and-boundary-completion","source_type":"word_analysis","support_id":"sup_256c361504576a462055","text":"{\"blocking_evidence\":null,\"headline\":\"pen-teaching expands into specified teaching\",\"reader_payoff\":\"The reader notices that the teaching root returns from 96:4 and is completed here by recipient, content, and final knowing echo.\",\"reason\":\"The same root appears in the previous ayah's teaching-by-pen statement, the opening verb of this ayah, and the final negated knowing verb.\",\"representative_source_ids\":[\"QE-0d900627\",\"QE-aa34383f\",\"ME-15b13792\",\"QY-18a8a58c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:1:knowledge-human-pairing","source_type":"word_analysis","support_id":"sup_2620737ae4f6fb5eed85","text":"{\"blocking_evidence\":null,\"headline\":\"human-knowledge pairing becomes syntactic\",\"reader_payoff\":\"The reader sees a broader knowledge-human association become local syntax when the teaching verb directly governs the human noun.\",\"reason\":\"The contextual association is not treated as an independent meaning, but in this ayah it is made concrete by direct-object syntax.\",\"representative_source_ids\":[\"QI-2b42a44f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:2:same-surah-human-arc","source_type":"word_analysis","support_id":"sup_2631dcac0ec7b9efadaf","text":"{\"blocking_evidence\":null,\"headline\":\"created, taught, then oversteps\",\"reader_payoff\":\"The reader sees 96:5 as the middle term between the human created in 96:2 and the human who oversteps in 96:6.\",\"reason\":\"Same-surah recurrence supports an arc around the human noun, with this ayah making the repeated human the taught object.\",\"representative_source_ids\":[\"QI-72535609\",\"QE-bd2d5c4c\",\"ME-711e8805\",\"QB-45eb5ed0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:3:second-object-relative","source_type":"word_analysis","support_id":"sup_2d5789d81dffd0b8a4a7","text":"{\"blocking_evidence\":null,\"headline\":\"relative word fills the second object slot\",\"reader_payoff\":\"The reader sees the word as taught content, not as a disposable particle between verbs.\",\"reason\":\"Attachment evidence marks this word as the second direct object of the teaching verb and as the relative content completed by the following negated clause.\",\"representative_source_ids\":[\"QG-9a00da12\",\"QT-2ff60417\",\"QT-41ca2d36\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:4","source_type":"word_analysis","support_id":"sup_361b53217fa285ad6dd1","text":"{\"gloss_range\":\"jussive negation particle with tight scope over the following imperfect, marking prior non-knowing inside the relative clause\",\"prose\":\"{{ar:لَمْ}} ({{tr:lam}}) governs {{ar:يَعْلَمْ}} ({{tr:yaʿlam}}), making the following imperfect jussive by removing the indicative ending, so the negation is local and grammatical, not a broad denial of the teaching act. Its scope stays inside the relative clause and names the human's prior non-knowing. That makes it the negative counterpart to {{ar:عَلَّمَ}} ({{tr:ʿallama}}): the teaching act answers a clearly denied baseline of knowledge. After {{ar:مَا}} ({{tr:mā}}), the clipped particle turns open content into lack-defined content, moving the boundary from the instrument of 96:4 to the human condition in 96:5.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَمْ}} ({{tr:lam}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:4:jussive-governance","source_type":"word_analysis","support_id":"sup_382cff852ae2ea94aa66","text":"{\"blocking_evidence\":null,\"headline\":\"particle governs the final verb\",\"reader_payoff\":\"The reader sees the negation registered grammatically in the following verb, not only as a free-standing negative word.\",\"reason\":\"The bundle identifies this as a jussive particle governing the following imperfect and producing the apocopated final form.\",\"representative_source_ids\":[\"QG-75515062\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:5:jussive-negated-knowing","source_type":"word_analysis","support_id":"sup_39ca55a7527a792c9254","text":"{\"blocking_evidence\":null,\"headline\":\"verb bears the particle's jussive effect\",\"reader_payoff\":\"The reader sees the prior lack of knowledge marked in the verb form itself, not only in the preceding particle.\",\"reason\":\"The preceding particle governs this imperfect, making the negation visible in the apocopated verb form as well as in the particle.\",\"representative_source_ids\":[\"QG-df663a50\",\"MG-326d18a8\",\"QS-dd1e32eb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:2","source_type":"word_analysis","support_id":"sup_3fcde15b14071c2ab4ce","text":"{\"gloss_range\":\"definite singular generic human as the first taught object and later antecedent of the hidden knowing subject\",\"prose\":\"{{ar:ٱلْإِنسَٰنَ}} ({{tr:al-insāna}}) stands as the first object of {{ar:عَلَّمَ}} ({{tr:ʿallama}}), so the human appears first as the one taught, not as the originator of knowledge. Its definite singular form works generically: one grammatical human carries the species-level claim without scattering it into many individuals. The hamza-bearing entry makes that recipient stand audibly between the teaching act and the open content. The same noun then supplies the hidden subject of {{ar:يَعْلَمْ}} ({{tr:yaʿlam}}), making the human move from taught recipient to the one whose former knowing was absent. Classical sociability and forgetfulness pressure makes this recipient both receptive to teaching and vulnerable in knowledge, while the local word remains the generic human noun. The word also sits between the created human of 96:2 and the overstepping human of 96:6, so this taught recipient becomes the middle point of a local human arc. It also lets the Adam-teaching pattern in 2:31 and the creation-then-teaching sequence in 55:3-4 land on the human species here.\",\"root_display\":\"{{ar:أ ن س}} ({{tr:ʾ-n-s}})\",\"root_gloss_range\":\"the aligned root field supports human familiarity, sociability, and receptivity; the classical forgetfulness derivation remains lexical pressure but does not replace the aligned local root\",\"surface_display\":\"{{ar:ٱلْإِنسَٰنَ}} ({{tr:al-insāna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:5:pen-and-sound-thread","source_type":"word_analysis","support_id":"sup_51ac969cb62562db4889","text":"{\"blocking_evidence\":null,\"headline\":\"pen line resolves into knowing endpoint\",\"reader_payoff\":\"The reader hears and sees the movement from the pen as teaching instrument in 96:4 to knowing as the endpoint in 96:5.\",\"reason\":\"The boundary and phonetic rows tie the previous instrument line to the final knowing verb without changing the local parse of this word.\",\"representative_source_ids\":[\"QP-08e0063b\",\"QP-aa21a463\",\"QB-ebba32c8\",\"QB-ece36bf9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:2:creation-teaching-recurrence","source_type":"word_analysis","support_id":"sup_521be931b1d6ad74cbdc","text":"{\"blocking_evidence\":null,\"headline\":\"creation-teaching formula lands on the human noun\",\"reader_payoff\":\"The reader sees local human teaching join the Adam-teaching pattern in 2:31 and the creation-then-teaching sequence in 55:3-4.\",\"reason\":\"The cited cross-surah rows name 2:31 and 55:3-4, while the local noun is directly governed by the teaching verb.\",\"representative_source_ids\":[\"QI-28ef5ba5\",\"MI-12b41c4c\",\"QE-2a2128f5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:3:open-ended-content","source_type":"word_analysis","support_id":"sup_5945ca433ef212a952ac","text":"{\"blocking_evidence\":null,\"headline\":\"content is defined by prior absence\",\"reader_payoff\":\"The reader notices that the taught content stays expandable because it is named by former absence rather than by a closed list.\",\"reason\":\"The relative word leaves the taught object open, while the final verb recovers that same object as what the human did not know.\",\"representative_source_ids\":[\"QS-b3b4222f\",\"MS-5155c412\",\"MT-aa5975a8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:1:double-object-teaching","source_type":"word_analysis","support_id":"sup_5c5b6e1753f51538fc7a","text":"{\"blocking_evidence\":null,\"headline\":\"teaching frame has recipient and content\",\"reader_payoff\":\"The reader sees teaching as a complete event with both learner and taught content supplied, not as an abstract attribute.\",\"reason\":\"The attachment rows identify the human as first direct object and the relative content as second direct object, matching the bundle grammar for a doubly transitive teaching verb.\",\"representative_source_ids\":[\"QG-34890749\",\"QT-57772271\",\"MT-9581379d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:1:completed-divine-predication","source_type":"word_analysis","support_id":"sup_5da606ce320ba51d3d52","text":"{\"blocking_evidence\":null,\"headline\":\"completed act continues the divine subject\",\"reader_payoff\":\"The reader notices that the ayah does not introduce a new agent; it turns the previous divine description into a direct completed act.\",\"reason\":\"The perfect active verb has no overt subject, and the clause opens a direct predication after the previous divine description rather than introducing a new agent.\",\"representative_source_ids\":[\"QG-95d67f3e\",\"QG-cbad0ef9\",\"QT-14a1aef1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:1:form-ii-caused-knowing","source_type":"word_analysis","support_id":"sup_63ced5471f7c6c19258b","text":"{\"blocking_evidence\":null,\"headline\":\"caused knowing rather than mere informing\",\"reader_payoff\":\"The reader feels knowledge as produced in the human by the teacher, not as a simple notice delivered from outside.\",\"reason\":\"V4 places teaching within the knowing branch and separates other root branches, so the prose preserves internalizing causation without making every derivative or branch locally active.\",\"representative_source_ids\":[\"QF-867767ab\",\"QF-20cb094d\",\"MS-2d55c550\",\"MF-f171cf1e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:1:epistemic-agency","source_type":"word_analysis","support_id":"sup_6757ee2a4930c18fb066","text":"{\"blocking_evidence\":null,\"headline\":\"divine agency precedes human knowing\",\"reader_payoff\":\"The reader notices that knowledge is not presented as self-originating human possession but as an epistemic act sourced by God.\",\"reason\":\"The local verb is active Form II teaching, the human is its object, and the wider derivative family supports the teaching-knowing cycle while local grammar keeps initiating agency outside the human.\",\"representative_source_ids\":[\"QS-2686d009\",\"QS-5bcf5a81\",\"QS-72e522bf\",\"QS-bbbb41d1\",\"QF-b3669c62\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:2:taught-recipient","source_type":"word_analysis","support_id":"sup_67e3bf60f21567732d03","text":"{\"blocking_evidence\":null,\"headline\":\"accusative human is the taught object\",\"reader_payoff\":\"The reader notices that the human first appears as recipient of teaching, before any human knowing is named.\",\"reason\":\"The word is accusative and syntactically forced as the first direct object of the teaching verb, before the content object arrives.\",\"representative_source_ids\":[\"QG-0e359712\",\"QS-5acb110e\",\"QT-46f5faf1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:5:hidden-human-subject","source_type":"word_analysis","support_id":"sup_6a29c6cd2ce1cf81b29c","text":"{\"blocking_evidence\":null,\"headline\":\"hidden subject returns to the human\",\"reader_payoff\":\"The reader tracks the same human from object of teaching to subject of former non-knowing.\",\"reason\":\"The implicit-argument row strongly licenses the generic human as the subject of this 3ms verb.\",\"representative_source_ids\":[\"QG-61af824f\",\"QI-4699a857\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:1:boundary-argument-completion","source_type":"word_analysis","support_id":"sup_744f1e7e605a856e4514","text":"{\"blocking_evidence\":null,\"headline\":\"instrument-only teaching receives whom and what\",\"reader_payoff\":\"The reader notices that 96:5 answers the unresolved recipient and content after the instrument named in 96:4.\",\"reason\":\"The boundary rows treat 96:4 as instrument-focused and 96:5 as the direct predication that supplies the human recipient and unknown content.\",\"representative_source_ids\":[\"QB-1195a270\",\"QB-34f58366\",\"QB-500e402e\",\"QB-a2cee9b1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"96:5:1:1","source_type":"qac_morpheme","support_id":"sup_820223d8d5040bdfb6c0","text":"{\"lemma_ar\":\"عَلَّمَ\",\"morph_features\":\"STEM|POS:V|PERF|(II)|LEM:Eal~ama|ROOT:Elm|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"96:5:1:1\",\"qac_word_ref\":\"96:5:1\",\"root_ar\":\"ع ل م\",\"surface_ar\":\"عَلَّمَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"96:5:2:2","source_type":"qac_morpheme","support_id":"sup_878b0d8a38dced305211","text":"{\"lemma_ar\":\"إِنسَٰن\",\"morph_features\":\"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"96:5:2:2\",\"qac_word_ref\":\"96:5:2\",\"root_ar\":\"ء ن س\",\"surface_ar\":\"إِنسَٰنَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:1","source_type":"word_analysis","support_id":"sup_93a859ca626f78eb4297","text":"{\"gloss_range\":\"completed Form II teaching that causes knowledge in a recipient and governs both the taught human and the taught content\",\"prose\":\"{{ar:عَلَّمَ}} ({{tr:ʿallama}}) opens the ayah as a completed act of teaching, with the unstated divine subject continuing from the prior description. Its Form II shape makes the knowing root causative, and the doubled middle consonant lets that causation be heard: knowledge is made to occur in another, not merely announced. The local grammar fills both teaching slots, first {{ar:ٱلْإِنسَٰنَ}} ({{tr:al-insāna}}) as recipient and then {{ar:مَا}} ({{tr:mā}}) as the content completed by {{ar:يَعْلَمْ}} ({{tr:yaʿlam}}), so the word stages a full transfer from source to former lack. The same verb also returns from the teaching-by-pen line (96:4), now specifying whom and what, while its root echo with the final verb closes the teaching-knowing circuit. That teaching frame also recalls Adam being taught in 2:31 and the creation-then-teaching sequence in 55:3-4, but here the verb directly governs the generic human noun, turning the wider human-knowledge pairing into local syntax.\",\"root_display\":\"{{ar:ع ل م}} ({{tr:ʿ-l-m}})\",\"root_gloss_range\":\"the root range centers on knowing, teaching, learning, and informing, with separate branches for marks, created realms, and rarer nominal images; this local Form II verb selects caused knowing\",\"surface_display\":\"{{ar:عَلَّمَ}} ({{tr:ʿallama}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:5:recoverable-object-through-ma","source_type":"word_analysis","support_id":"sup_9f463bd07aef5ae51fd3","text":"{\"blocking_evidence\":null,\"headline\":\"object is recovered from the relative word\",\"reader_payoff\":\"The reader notices that what God taught and what the human did not know are the same object, compressed rather than repeated.\",\"reason\":\"The verb has no repeated object after it because the relative word is already the understood object within the knowing clause.\",\"representative_source_ids\":[\"QG-f2bdaf4d\",\"MS-c588665d\",\"QT-dae48be9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:2:etymology-pressure","source_type":"word_analysis","support_id":"sup_a88cb5bc241ef0f27deb","text":"{\"blocking_evidence\":null,\"headline\":\"receptivity and forgetfulness remain lexical pressure\",\"reader_payoff\":\"The reader feels the human as both suited to receive teaching and vulnerable in knowledge, while the local aligned word remains the generic human noun.\",\"reason\":\"The aligned root is the sociability and familiarity root, while the forgetfulness derivation is a classical lexical discussion; the prose keeps both as pressure without replacing the local parse.\",\"representative_source_ids\":[\"QS-1e777173\",\"QS-2da8d13c\",\"QS-63cc028e\",\"MS-e27201f6\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:5:form-i-form-ii-echo","source_type":"word_analysis","support_id":"sup_afb7c055a2d9847b7e1a","text":"{\"blocking_evidence\":null,\"headline\":\"Form I knowing answers Form II teaching\",\"reader_payoff\":\"The reader hears the same root move from divine caused knowing to the human knowing that was formerly absent.\",\"reason\":\"The surface forms contrast Form II teaching at the opening with Form I knowing at the close, both within the same root field.\",\"representative_source_ids\":[\"QF-0c12115c\",\"QE-0c819ef0\",\"ME-b4ee21af\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:3:relative-over-masdariyya","source_type":"word_analysis","support_id":"sup_c649ba14d4194923570a","text":"{\"blocking_evidence\":null,\"headline\":\"relative reading is primary over source reading\",\"reader_payoff\":\"The reader can see the grammatical reparse point, while local object syntax keeps the main reading on what was taught rather than the fact of not knowing.\",\"reason\":\"The grammar acknowledges both parse routes, but the direct-object role favors taught content rather than merely the fact or condition of not knowing.\",\"representative_source_ids\":[\"MG-3fcc8846\",\"QS-19f8425f\",\"QF-8b9bbc3e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:4:boundary-from-method-to-condition","source_type":"word_analysis","support_id":"sup_ca7dac67930421a5816a","text":"{\"blocking_evidence\":null,\"headline\":\"instrument gives way to prior absence\",\"reader_payoff\":\"The reader sees the movement from teaching by instrument in 96:4 to the human lack that teaching addresses in 96:5.\",\"reason\":\"The boundary rows compare the instrument-focused teaching of 96:4 with the negated cognitive condition inside 96:5.\",\"representative_source_ids\":[\"QB-74260cf7\",\"QB-b5767a89\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:3","source_type":"word_analysis","support_id":"sup_d4421c252c8943a55b9a","text":"{\"gloss_range\":\"open relative content functioning as the second object of teaching and as the recoverable object inside the knowing clause\",\"prose\":\"{{ar:مَا}} ({{tr:mā}}) is the second object of {{ar:عَلَّمَ}} ({{tr:ʿallama}}), but it also opens the relative clause that ends with {{ar:يَعْلَمْ}} ({{tr:yaʿlam}}). That double position makes the taught content open-ended: the ayah does not name a closed domain, but defines the content by what had not been known. The possible source-like reading is grammatically visible, yet the object-role evidence makes the relative-content reading primary here. As a pivot, the word connects the divine teaching act to the human knowing clause without repeating the object twice.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مَا}} ({{tr:mā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:1:geminated-causative-sound","source_type":"word_analysis","support_id":"sup_df1aa9952f41a01c1850","text":"{\"blocking_evidence\":null,\"headline\":\"gemination makes causation audible\",\"reader_payoff\":\"The reader hears the doubled middle consonant as sound pressure matching the Form II causative force.\",\"reason\":\"The CRITICAL row ties the audible doubling to the same surface feature that marks Form II causation.\",\"representative_source_ids\":[\"QP-3583cec2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:5","source_type":"word_analysis","support_id":"sup_e19ca26ffb9049da2ba9","text":"{\"gloss_range\":\"Form I imperfect knowing, made jussive and negated by the preceding particle, with its object recovered through the relative word\",\"prose\":\"{{ar:يَعْلَمْ}} ({{tr:yaʿlam}}) closes the ayah as the human-side verb of knowing. {{ar:لَمْ}} ({{tr:lam}}) has made it jussive and negated, with the clipped verb form carrying the particle's effect, while {{ar:مَا}} ({{tr:mā}}) supplies the object already taught by {{ar:عَلَّمَ}} ({{tr:ʿallama}}). The hidden subject routes back to {{ar:ٱلْإِنسَٰنَ}} ({{tr:al-insāna}}), so the final word seals the full circuit: caused knowing at the opening answers genuine prior non-knowledge at the close, not weak opinion. The same lam-shaped knowing formula returns as a question in 96:14, and the sound thread from the pen line in 96:4 to this ending makes knowing the audible endpoint.\",\"root_display\":\"{{ar:ع ل م}} ({{tr:ʿ-l-m}})\",\"root_gloss_range\":\"the root range centers on knowing and teaching while also containing separate sign, mark, created-realm, and rare nominal branches; this local Form I verb selects human knowing as the negated baseline\",\"surface_display\":\"{{ar:يَعْلَمْ}} ({{tr:yaʿlam}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:2:human-knowledge-sandwich","source_type":"word_analysis","support_id":"sup_e2bb2caf851b695917ae","text":"{\"blocking_evidence\":null,\"headline\":\"human noun sits between teaching and knowing\",\"reader_payoff\":\"The reader notices the human noun held between the divine teaching verb and the later human knowing verb.\",\"reason\":\"The contextual human-knowledge pairing is realized locally by the noun's position after the teaching verb and by its control of the final verb's hidden subject.\",\"representative_source_ids\":[\"QI-51436e32\",\"QT-f78df981\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:5:same-surah-reminder","source_type":"word_analysis","support_id":"sup_eadb0d4bf08e30f495fd","text":"{\"blocking_evidence\":null,\"headline\":\"later question reopens the knowing formula\",\"reader_payoff\":\"The reader sees the statement of prior ignorance in 96:5 become a later pointed knowledge question in 96:14.\",\"reason\":\"The CRITICAL rows explicitly connect this negated knowing form with the same-surah question in 96:14.\",\"representative_source_ids\":[\"QI-0f750fbc\",\"MI-38e6694b\",\"QE-704fe068\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:4:cadence-arrest","source_type":"word_analysis","support_id":"sup_f11cdbda4eda4a9b1cd2","text":"{\"blocking_evidence\":null,\"headline\":\"clipped particle arrests the phrase\",\"reader_payoff\":\"The reader hears a brief closed beat before the final knowing verb, matching the particle's arresting semantic work.\",\"reason\":\"The prosodic row is tied to the local short particle immediately before the governed final verb.\",\"representative_source_ids\":[\"QP-4f4405b1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:2:audible-recipient-boundary","source_type":"word_analysis","support_id":"sup_f4b71071e74d265edce4","text":"{\"blocking_evidence\":null,\"headline\":\"hamza entry makes the recipient stand out\",\"reader_payoff\":\"The reader hears a sharper entry into the human noun between the teaching act and the open content.\",\"reason\":\"The CRITICAL row treats the written and audible boundary of the noun as a local cue that helps the recipient stand between verb and content.\",\"representative_source_ids\":[\"QP-0747f2e4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:5:knowledge-not-opinion","source_type":"word_analysis","support_id":"sup_f7779de5ecf1935ded86","text":"{\"blocking_evidence\":null,\"headline\":\"negation denies real knowing\",\"reader_payoff\":\"The reader understands the negated state as genuine non-knowledge, while the broad dictionary root range is narrowed to the knowing branch here.\",\"reason\":\"V4 supports the knowing branch as opposite of ignorance, while unrelated mark, realm, and rare nominal branches do not become local senses of this verb.\",\"representative_source_ids\":[\"QS-4df72267\",\"QS-8efdd7f7\",\"QI-5075f4d6\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:2:antecedent-of-knowing","source_type":"word_analysis","support_id":"sup_fb0ca3df2726a2037024","text":"{\"blocking_evidence\":null,\"headline\":\"recipient becomes hidden subject of knowing\",\"reader_payoff\":\"The reader tracks one human referent through a role change from taught object to former non-knower.\",\"reason\":\"The implicit-argument evidence routes the final verb's 3ms subject back to the generic human taught in the same ayah.\",\"representative_source_ids\":[\"QG-1933370b\",\"QT-f78df981\",\"QB-2b20e0aa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:3:two-object-routes","source_type":"word_analysis","support_id":"sup_fd4835d8748b8ec3e744","text":"{\"blocking_evidence\":null,\"headline\":\"pivot position keeps two routes visible\",\"reader_payoff\":\"The reader sees one small word serve as both the teaching verb's second object and the relative clause's recoverable object.\",\"reason\":\"The same surface position supports the pivot observation, while the local direct-object evidence selects the relative route as primary.\",\"representative_source_ids\":[\"QY-07ba7008\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:2:generic-singular-human","source_type":"word_analysis","support_id":"sup_fd935491f351ca9a1e3b","text":"{\"blocking_evidence\":null,\"headline\":\"definite singular carries a species claim\",\"reader_payoff\":\"The reader sees a species-wide claim compressed into one singular grammatical recipient.\",\"reason\":\"The QAC grammar explicitly treats the definite article and singular noun as generic, and contextual profiles show the human noun field commonly referring to generic humans.\",\"representative_source_ids\":[\"QG-9745cae3\",\"QF-08d5ab1c\",\"QF-8dab4852\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:5:ayah-closure","source_type":"word_analysis","support_id":"sup_fd9eab52b2ac2e815466","text":"{\"blocking_evidence\":null,\"headline\":\"final word lands on knowledge\",\"reader_payoff\":\"The reader hears the ayah end on the knowledge root, where negation, jussive governance, and closure converge.\",\"reason\":\"The final verb completes the relative clause and closes the ayah while bearing the governed jussive form.\",\"representative_source_ids\":[\"QT-46864ba1\",\"QY-e70b51f8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:4:tight-negation-scope","source_type":"word_analysis","support_id":"sup_fde7033c49a243d27724","text":"{\"blocking_evidence\":null,\"headline\":\"negation stays inside the relative clause\",\"reader_payoff\":\"The reader notices that the particle negates the human's prior knowing, not the divine teaching.\",\"reason\":\"Attachment evidence makes the particle complement the following verb only, while the teaching verb remains outside the negated relative clause.\",\"representative_source_ids\":[\"QG-cbebdc71\",\"QT-bfa49267\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:5:4:prior-ignorance-baseline","source_type":"word_analysis","support_id":"sup_fdfc5dd39cadd006f83e","text":"{\"blocking_evidence\":null,\"headline\":\"negative baseline answers positive teaching\",\"reader_payoff\":\"The reader feels the teaching act measured against a clearly denied state of prior knowledge.\",\"reason\":\"The particle creates the negative side of the teaching-knowing contrast without moving its scope back onto the opening verb.\",\"representative_source_ids\":[\"QS-0fa2e872\",\"QS-96b4f4fa\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"عَلَّمَ ٱلْإِنسَٰنَ مَا لَمْ يَعْلَمْ","ayah_ref":"96:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000059/B002","root_001040/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001040","role":"Emergence into clarity supplies the state change, while the doubled root assigns its cause to teaching and its result to human knowing.","root":"ع ل م","source_ref":"96:5","source_word_indices":["1","5"]},{"branch_id":"B002","mapped_root_id":"root_000059","role":"Perceptual detection makes the human a locus in which an absent object can enter sensed awareness.","root":"ء ن س","source_ref":"96:5","source_word_indices":["2"]}],"changed_reading":{"after":"The verse stages a caused transition from non-apprehension to disclosed awareness, with the human as the changed locus.","before":"A teacher transfers unspecified information to a human."},"confidence":"strong","focus_anchor":"The same ع ل م root occurs in the causative opening verb and the negated final verb, enclosing the human recipient and the unknown object.","mechanism":"Teaching causes a passage across an epistemic boundary: what had not entered the human's awareness becomes disclosed to that human.","model_id":"baseline_disclosure_transition"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_disclosure_transition","source_type":"hft","support_id":"sup_9205e7b0ebdb213fb659","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"عَلَّمَ ٱلْإِنسَٰنَ مَا لَمْ يَعْلَمْ","ayah_ref":"96:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000059/B004","root_001040/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001040","role":"A differentiating trace that guides toward its referent turns teaching into the production of epistemic bearings.","root":"ع ل م","source_ref":"96:5","source_word_indices":["1","5"]},{"branch_id":"B004","mapped_root_id":"root_000059","role":"The person-facing side gives the marks an orientation toward a situated human recipient rather than leaving them as inert signs.","root":"ء ن س","source_ref":"96:5","source_word_indices":["2"]}],"changed_reading":{"after":"Knowledge is an orienting system of distinctions by which the human can find what was formerly inaccessible.","before":"Knowledge is an abstract possession placed in the learner."},"confidence":"medium","focus_anchor":"عَلَّمَ and يَعْلَمْ frame the human and the open relative مَا, allowing the mark-image of ع ل م to organize the construction.","mechanism":"Teaching places distinctions that point beyond themselves; knowing is the ability to follow those marks into territory that previously had no usable bearings.","model_id":"baseline_marker_navigation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_marker_navigation","source_type":"hft","support_id":"sup_9b1e21f2092002400d97","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"عَلَّمَ ٱلْإِنسَٰنَ مَا لَمْ يَعْلَمْ","ayah_ref":"96:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000059/B003","root_001040/B001"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000059","role":"Familiar comfort replacing estrangement supplies the relational change undergone by the human before the unknown.","root":"ء ن س","source_ref":"96:5","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001040","role":"Disclosure provides the cognitive mechanism through which estranged material becomes available for familiarity.","root":"ع ل م","source_ref":"96:5","source_word_indices":["1","5"]}],"changed_reading":{"after":"Teaching brings the human into familiarity with a reality that had remained cognitively estranged.","before":"Teaching corrects a deficit of information."},"confidence":"medium","focus_anchor":"The human stands between teaching and the clause of prior non-knowing, so the change can be read affectively as well as cognitively.","mechanism":"Instruction removes the estrangement of the unknown: disclosure does not merely add content but makes an alien field perceptible and inhabitable.","model_id":"baseline_unknown_familiarized"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_unknown_familiarized","source_type":"hft","support_id":"sup_52563ea186b9584513c1","trust":"legacy_unbound"}]}
</lane_packet_json>
