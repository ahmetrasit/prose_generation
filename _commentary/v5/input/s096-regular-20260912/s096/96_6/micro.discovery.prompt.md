# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **96:6**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s096-regular-20260912/s096/96_6/micro.discovery.json` and modify nothing
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
  "ayah_ref": "96:6",
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
{"branch_registry":[{"boundary":"Dal, insan türünü ve onun tekil ya da toplu üyelerini kapsar; yakınlık duygusunu, duyusal algıyı ve insana dönük yanı kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B001","candidate_links":[{"candidate_id":"cand_12218dcac34d2427ea99","lane":"micro"},{"candidate_id":"cand_10bd6da7b159be6c96e3","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"96:6:3:2","qac_word_ref":"96:6:3","surface_ar":"إِنسَٰنَ"}],"gloss":"insan türü ve bu türden bir kişi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan türünü, insanların oluşturduğu topluluğu veya bu türün tek bir üyesini görünmeyen varlıklar sınıfının karşısında adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlandırmanın insanların duyularla görünür oluşuna bağlanması, anlamın özü değil kökene ilişkin bir açıklamadır."}}],"root_ar":"ء ن س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsanları bir tür veya topluluk olarak anlatırken de bu türün tek bir üyesini belirtirken de kullanılabilir.","boundary_detail":"Dal, insan türünü ve onun tekil ya da toplu üyelerini kapsar; yakınlık duygusunu, duyusal algıyı ve insana dönük yanı kapsamaz.","branch_image_ar":"ظهور الإنسان المخالف للتوحش والجن","concept_gloss":"insan türü ve bu türden bir kişi","contextual_glosses":[{"applicability":"Türün üyeleri topluca veya görünmeyen varlıklar sınıfının karşıtı olarak anıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan türünün toplu olarak adlandırılmasını açık ve doğal biçimde korur."},"facet_ids":["F001"],"text":"insanlar","usage_role":"general"},{"applicability":"Bağlam türün tek bir üyesini veya herhangi bir kimseyi gösterdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan topluluğundan tek bir üyenin belirtilmesini korur."},"facet_ids":["F001"],"text":"bir kişi","usage_role":"contextual"}],"definition":"Görünmeyen varlıklar sınıfının karşısında yer alan insan türünü, bu türün topluluğunu ya da tek bir üyesini belirtir. İnsanların görünür oluşu, bu adlandırma için aktarılan bir gerekçedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan türünü, insanların oluşturduğu topluluğu veya bu türün tek bir üyesini görünmeyen varlıklar sınıfının karşısında adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Adlandırmanın insanların duyularla görünür oluşuna bağlanması, anlamın özü değil kökene ilişkin bir açıklamadır."}],"identity_rationale":"Kaynak ifadesi, görünmeyen varlıklar sınıfının karşısındaki insan türünü, bu türün topluluğunu ve tek bir üyesini birlikte gösterir. Görünür olma açıklaması adlandırma gerekçesidir; insan olmanın kurucu tanımı değildir. Evde kimsenin bulunmadığını bildiren kalıp ise dal çekirdeğine genellenemez ve yalnızca kendi sözcüksel biriminde korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"insanlar; insan topluluğu"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"insan; insan türü"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"insan topluluğunun bir üyesi; insana veya insanlara ait"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"insanlar; insan toplulukları"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"insanlar; halk"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"evde hiç kimse yok"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"belirli bir ağızda insan ve onun çoğulu"}],"lexicalization_note":"Çıplak biçimlerdeki insan ve insan topluluğu anlamı dal çekirdeğidir; evde hiç kimse bulunmadığını anlatan kalıp ayrı tutulur ve çekirdeğe yeni bir genel anlam katmaz.","neighbor_coverage_note":"Bütün aday kartlar karşılaştırıldı. Yalnız insanı adlandırma sınırını yaratılmışlar kapsamından ve yakınlık duygusundan ayıran, okuyucu için en yararlı üç karşıtlık yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yer değiştirme yalnız insanı genel olarak adlandıran bağlamlarda mümkündür. Odak dalın görünmeyen varlıklarla sınıf karşıtlığı, komşunun ise görünür beden yönü kendi sınırında kalır.","focus_only":"Odak dal, insanları görünmeyen varlıklar sınıfının karşısında bir tür olarak kurar ve görünürlüğe dayalı bir adlandırma açıklaması taşır.","gloss":"insan türünü iki ayrı yönden adlandırma","neighbor_only":"Komşu dal, insanı görünür ten ve yaratılmış beden yönüyle adlandırır; tekil, çoğul, erkek ve kadın kapsamını özellikle öne çıkarır.","neighbor_ref":"root_000120/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da insanı hem tür hem bu türün üyesi olarak gösterebilir."},{"boundary_match":"partial","distinction":"Komşunun genel yaratılmışlar kapsamı odak dala taşınamaz; odak dal da yalnız insanları belirttiği için bütün yaratılmışların yerine kullanılamaz.","focus_only":"Odak dal yalnız insan türünü ve bu türün tekil ya da toplu üyelerini belirtir.","gloss":"insan türü ile bütün yaratılmışlar ayrımı","neighbor_only":"Komşu dal yeryüzündeki bütün yaratılmışları kapsayabilir ve bazı yorumlarda insanlarla görünmeyen varlıkları birlikte içerir.","neighbor_ref":"root_000061/B001","relation_type":"near_neighbor","shared_zone":"İnsanlar iki dalın gönderim alanında da bulunabilir."},{"boundary_match":"field_only","distinction":"Birinde insanın kim olduğu adlandırılır, diğerinde bir kişi ya da şey karşısındaki duygusal durum anlatılır; sıradan bağlamlarda birbirlerinin yerine geçmezler.","focus_only":"Odak dal insan türünü ve bu türün üyelerini adlandırır.","gloss":"insan adı ile yakınlık duygusu ayrımı","neighbor_only":"Komşu dal yabancılık ve ürkme duygusunun kalkmasını, yakınlık ve rahatlık oluşmasını anlatır.","neighbor_ref":"root_000059/B003","relation_type":"same_field","shared_zone":"Her iki dalda da insan, temel gönderim noktası veya deneyim sahibi olabilir."}],"source_phrase_ar":"الإنس خلاف الجن وسموا لظهورهم (maqayis;mufradat)؛ الإنس البشر والواحد إنسي والجمع أناسي (sihah)؛ الإنس جماعة الناس والأناسي جماع (tahdhib)","source_summary":"Aktarımlar, dalın insan türünü hem topluluk hem tek kişi olarak gösterebildiğinde ve görünmeyen varlıklar sınıfıyla karşıtlık kurduğunda birleşir. Görünürlük, ortak anlamdan çok adlandırmanın gerekçesi olarak sunulur.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الإنس والبشر والناس والأناسي والإنسان من حيث الجماعة أو الواحد، وما بالدار أنيس بمعنى أحد.","what_is_not_ar":"لا يدخل مجرد الاستئناس النفسي ولا الإيناس بمعنى الإبصار ولا الجانب الإنسي إلا بدليل."},"support_links":["sup_4edd506a257f99282c67","sup_bf02d9b8e9643d6719e4"]},{"boundary":"Dal duyusal olarak fark etmeyi ve belirtilen bağlamlardaki işitme, sezme ve bakıp araştırma kullanımlarını kapsar; yakınlık ve rahatlık duygusunu kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"96:6:3:2","qac_word_ref":"96:6:3","surface_ar":"إِنسَٰنَ"}],"gloss":"görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi gözle görerek fark etmeyi veya seçmeyi anlatır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli bir ses nesnesiyle kullanıldığında o sesi işitmeyi anlatır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kimsedeki olgunluk belirtisini bilip ayırt etmeyi veya kaygı veren bir durumu duyularla sezmeyi anlatabilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Çevreye bakıp dikkatle araştırarak birinin bulunup bulunmadığını anlamaya çalışma kullanımını taşır."}}],"root_ar":"ء ن س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın görme çekirdeğiyle birlikte yalnız belirtilen bağlamlarda ortaya çıkan işitme, sezme ve çevreyi araştırma uzantılarını topluca verir.","boundary_detail":"Dal duyusal olarak fark etmeyi ve belirtilen bağlamlardaki işitme, sezme ve bakıp araştırma kullanımlarını kapsar; yakınlık ve rahatlık duygusunu kapsamaz.","branch_image_ar":"إيناس الشيء برؤية أو إحساس أو سماع","concept_gloss":"görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma","contextual_glosses":[{"applicability":"Nesnenin gözle seçildiği veya görüldüğü temel kullanımda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gözle görme ve görüleni fark etme işlemlerini birlikte korur."},"facet_ids":["F001"],"text":"görüp fark etmek","usage_role":"general"},{"applicability":"Nesne açıkça bir ses olduğunda kullanılan bağlama bağlı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sesin kulakla algılanması biçimindeki özel kullanımı korur."},"facet_ids":["F002"],"text":"sesi işitmek","usage_role":"contextual"},{"applicability":"Bir kimsedeki olgunluk veya kaygı uyandıran durum gibi bir belirtinin ayırt edildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Duyusal belirtiden bir durumun varlığını anlayıp ayırt etmeyi korur."},"facet_ids":["F003"],"text":"belirtiyi sezmek","usage_role":"contextual"},{"applicability":"Çevreyi gözleyip birinin bulunup bulunmadığını anlamaya çalışma kullanımında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dikkatle bakma ile birini bulmaya yönelik araştırmayı birlikte korur."},"facet_ids":["F004"],"text":"bakıp araştırmak","usage_role":"explanatory"}],"definition":"Bir şeyi görüp fark etmeyi anlatır. Belirli kullanımlarda bir sesi işitmeye, bir kimsedeki olgunluk belirtisini ya da kaygı veren bir durumu sezmeye ve çevreye bakarak birinin bulunup bulunmadığını araştırmaya uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi gözle görerek fark etmeyi veya seçmeyi anlatır."},{"facet_id":"F002","role":"extension","statement":"Belirli bir ses nesnesiyle kullanıldığında o sesi işitmeyi anlatır."},{"facet_id":"F003","role":"extension","statement":"Bir kimsedeki olgunluk belirtisini bilip ayırt etmeyi veya kaygı veren bir durumu duyularla sezmeyi anlatabilir."},{"facet_id":"F004","role":"associated_use","statement":"Çevreye bakıp dikkatle araştırarak birinin bulunup bulunmadığını anlamaya çalışma kullanımını taşır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Zamanla gelişen yakınlık ve yabancılığın kalkması anlamını ekler.","collision":"Yakınlık ve rahatlık bildiren ayrı dalla karışır.","fit":"displacement","loses":"Görme, işitme, belirtiyi sezme ve çevreye bakıp araştırma işlemlerini siler.","preserves":"Bir kişi veya şeye yönelen deneyim fikrini çok genel biçimde korur."},"text":"alışmak"}],"identity_rationale":"Kaynak ifadesi görmeyi temel alır, fakat belirli kullanımlarda işitmeyi, bir belirtiyi anlayıp ayırt etmeyi ve çevreye bakarak birini aramayı da aynı dalda aktarır. Bu yüzden dal genel ve sınırsız bir algı yetisi diye tanımlanamaz; her uzantı kendi bağlamına bağlı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir şeyi görmek ve fark etmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"sesi işitmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"onda olgunluk belirtisi görmek ve bunu anlamak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ürken yabani hayvanın birini sezip çevreye bakınması"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"çevreye bakıp birinin olup olmadığını araştırmak"}],"lexicalization_note":"Görüp fark etme çekirdeği ile ses işitme, olgunluk belirtisini ayırt etme ve çevreye bakıp araştırma kalıpları ayrı tutulur; kalıplardaki kapsam çıplak biçime genellenmez.","neighbor_coverage_note":"Bütün aday kartlar değerlendirildi. Görme, genel duyumsama ve yakınlık duygusuyla karışma olasılığı en yüksek üç sınır yayımlandı; diğer adaylar dalı açıklayan ek bir karşıtlık sağlamadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yalnız görsel algı bağlamında yakın karşılık olabilirler. Odak dalın işitme ve belirtiyi sezme uzantıları komşuya, komşunun göz organı anlamı da odak dala taşınamaz.","focus_only":"Odak dal, görmenin yanında belirli yapılarda işitme, belirti sezme ve çevreyi araştırma uzantılarını taşır.","gloss":"fark etme ile gözle görme ayrımı","neighbor_only":"Komşu dal göz organını, görme duyusunu ve göz açıp dikkatle bakma eylemini kendi başına kapsar.","neighbor_ref":"root_000121/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi göz yoluyla görüp seçme alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu daha genel bir duyu alanıdır; odak dalın uzantıları ise kanıtlanan nesne ve yapılara bağlıdır. Bu nedenle genel duyumsama her durumda odak ifadeyle karşılanamaz.","focus_only":"Odak dal görmeyi merkez alır ve yalnız belirli söz çevrelerinde işitme, sezme ve araştırmaya uzanır.","gloss":"belirli algı kullanımları ile genel duyumsama","neighbor_only":"Komşu dal herhangi bir duyu aracılığıyla algılama, bilme ve varlığını saptama alanını genel olarak kapsar.","neighbor_ref":"root_000321/B002","relation_type":"near_synonym","shared_zone":"Her ikisi de bir şeyin duyular aracılığıyla fark edilmesini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal algısal saptamayı, komşu dal ise karşılaşma sonrasındaki duygusal rahatlığı bildirir. Algı gerçekleşebilir ama yakınlık doğmayabilir.","focus_only":"Odak dal bir nesneyi görme, işitme veya belirtilerinden sezme eylemini anlatır.","gloss":"duyusal fark etme ile yakınlık hissetme","neighbor_only":"Komşu dal bir kişi ya da şey karşısında yabancılık ve ürkme duymayıp yakınlık hissetmeyi anlatır.","neighbor_ref":"root_000059/B003","relation_type":"near_neighbor","shared_zone":"Bir kişi veya şeyle karşılaşma iki anlam alanının ortak başlangıç durumu olabilir."}],"source_phrase_ar":"آنست الشيء إذا رأيته وآنسته إذا سمعته (maqayis)؛ آنسته أبصرته وآنست الصوت سمعته وآنست منه رشدا علمته (sihah)؛ آنس من جانب يعني أبصر نارا والاستئناس النظر وأحس بما رابه (tahdhib)؛ فإن آنستم منهم رشدا أي أبصرتم وآنست نارا (mufradat)","source_summary":"Aktarılan anlam alanının merkezi görüp fark etmektir. Aynı ifade ailesi belirli nesne ve yapılarda işitme, bir belirtiyi anlayıp ayırt etme, kaygı veren şeyi sezme ve bakıp araştırma yönlerinde kullanılır; bunlar sınırsız bir genel algı anlamı oluşturmaz.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه آنس الشيء إذا أبصره أو رآه، وآنس الصوت إذا سمعه، وأحس الفزع أو وجد الشيء في نفسه، والاستئناس بمعنى النظر والتبصر.","what_is_not_ar":"لا يدخل الأنس بمعنى الراحة والمؤالفة ولا الإنس بمعنى البشر إلا بقرينة."},"support_links":[]},{"boundary":"Dal duygusal yakınlık, rahatlık ve bunları sağlayan varlıkları kapsar; insan türünün adı, duyusal fark etme ve insana bakan yan anlamları dışarıda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B003","candidate_links":[{"candidate_id":"cand_5f5146d03da9767b76e8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"96:6:3:2","qac_word_ref":"96:6:3","surface_ar":"إِنسَٰنَ"}],"gloss":"yabancılık duymadan yakınlık ve rahatlık hissetme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi ya da şey karşısında yabancılık ve ürkme duygusunun kalkıp yakınlık, rahatlık veya sevinç oluşmasını anlatır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişiye arkadaşlık ederek veya yanında bulunarak yabancılık duygusunu gideren kişi ya da şeyi adlandırır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsana alışık ve saldırgan olmayan hayvanı, özellikle bu nitelikteki köpeği anlatabilir."}}],"root_ar":"ء ن س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi veya şeyin ürkütücü ve yabancı gelmemesi, tersine yakınlık ve iç rahatlığı vermesi anlatıldığında dalın çekirdeğini karşılar.","boundary_detail":"Dal duygusal yakınlık, rahatlık ve bunları sağlayan varlıkları kapsar; insan türünün adı, duyusal fark etme ve insana bakan yan anlamları dışarıda kalır.","branch_image_ar":"الأنس الذي يزيل الوحشة","concept_gloss":"yabancılık duymadan yakınlık ve rahatlık hissetme","contextual_glosses":[{"applicability":"Bir kişi veya şey karşısındaki yabancılık duygusunun kalktığı temel durumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Alışma sonucunda yabancılığın kalkmasını ve yakınlık oluşmasını korur."},"facet_ids":["F001"],"text":"alışıp yakınlık duymak","usage_role":"general"},{"applicability":"Yalnızlığı veya ürkmeyi gideren bir arkadaş, nesne ya da başka bir dayanak adlandırıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yakınlık ve güven veren kaynağın kişiyle sınırlı olmamasını korur."},"facet_ids":["F002"],"text":"yanında rahatlık veren kişi veya şey","usage_role":"explanatory"},{"applicability":"İnsandan kaçmayan ve ısırıp saldırmayan evcil ya da alışkın hayvan için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın insana alışıklığını ve saldırgan olmama sınırını birlikte korur."},"facet_ids":["F003"],"text":"insana alışık ve saldırgan olmayan","usage_role":"contextual"}],"definition":"Bir kişi ya da şey karşısında yabancılık, ürkme veya kaçınma duymayıp yakınlık, rahatlık ve sevinç hissetmeyi anlatır. Bu duyguyu veren kişi veya şeye ve insana alışık, saldırgan olmayan hayvana da aktarılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi ya da şey karşısında yabancılık ve ürkme duygusunun kalkıp yakınlık, rahatlık veya sevinç oluşmasını anlatır."},{"facet_id":"F002","role":"extension","statement":"Kişiye arkadaşlık ederek veya yanında bulunarak yabancılık duygusunu gideren kişi ya da şeyi adlandırır."},{"facet_id":"F003","role":"specialization","statement":"İnsana alışık ve saldırgan olmayan hayvanı, özellikle bu nitelikteki köpeği anlatabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Her türlü sevincin bu dala ait olduğu izlenimini verebilir.","fit":"narrowing","loses":"Yabancılığın ve ürkmenin kalkmasını, alışmayı ve rahatlık veren kişi ya da şey kapsamını kaybeder.","preserves":"Yakınlık durumunda ortaya çıkabilen olumlu duyguyu korur."},"text":"sevinç"}],"identity_rationale":"Kaynak ifadesi, bir kişi veya şey karşısında yabancılık ve ürkme duygusunun kalkmasını çekirdek anlam olarak verir. Yakınlık ve sevinç, rahatlık veren kişi ya da şey ve insana alışık saldırgan olmayan hayvan kullanımları bu çekirdekten bağımlı biçimde açıklanabilir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yakınlık ve rahatlık; yabancılık duymama"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"birine alışıp onun yanında sevinmek"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"biriyle yakınlık kurmak ve onsuz kendini yalnız hissetmek"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"yakın arkadaş; rahatlık veren kişi veya şey"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yakınlıktan ve söyleşiden hoşlanan genç kadın"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"insana alışık, saldırgan olmayan köpek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"gece yolcusuna veya konaklayana güven veren ateş"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"sahibine güven veren bütün silahlar; zırh, miğfer, koruyucu örtü ve kalkan gibi savunma donanımları"}],"lexicalization_note":"Yabancılık duymama çekirdeği ile rahatlık veren kişi veya şey ve insana alışık hayvan gibi özelleşmiş biçimler ayrı katmanlarda tutulur; özel biçimler bütün dalı tanımlamaz.","neighbor_coverage_note":"Bütün aday kartlar karşılaştırıldı. Alışıp bağlanma, özel dostluk ve insan türünü adlandırma alanları dal sınırını en açık gösterdiği için yalnız bu üç ayrım yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın belirleyici yönü yabancılık ve ürkmenin karşıtı olan iç rahatlığıdır; komşu dal süreklilik, bağlanma ve alışkanlık yönlerini odaktan daha geniş taşır.","focus_only":"Odak dal yabancılık ve ürkmenin kalkmasıyla oluşan yakınlık ve rahatlığı, ayrıca bunu sağlayan varlığı öne çıkarır.","gloss":"yakınlık rahatlığı ile alışıp bağlanma","neighbor_only":"Komşu dal bir kişi, yer veya şeye alışmayı, ona bağlanmayı, onunla sürekli bulunmayı ve hayvanın evcilleşmesini daha geniş biçimde kapsar.","neighbor_ref":"root_000045/B005","relation_type":"near_synonym","shared_zone":"İki dal da bir kişi, yer, şey veya hayvana karşı yabancılığın azalmasını anlatabilir."},{"boundary_match":"partial","distinction":"Her rahatlık veren yakınlık özel ve arı bir dostluk değildir. Komşunun karşılıklı dostluk sınırı odak dalın nesne ve hayvan uzantılarına uygulanamaz.","focus_only":"Odak dal kişi dışındaki şeylerin verdiği rahatlığı ve insana alışık hayvanı da kapsayabilir.","gloss":"rahatlık veren yakınlık ile özel dostluk","neighbor_only":"Komşu dal seçilmiş kişiler arasındaki arı, özel ve karşılıklı dostluk bağını anlatır.","neighbor_ref":"root_000430/B007","relation_type":"near_neighbor","shared_zone":"İki dal da kişiler arasında yakınlık ve içtenlik bulunan durumlarda buluşur."},{"boundary_match":"field_only","distinction":"Odak dal bir duygusal ilişkiyi, komşu dal ise bir varlık sınıfını adlandırır. İnsan olmak yakınlık hissetmeyi gerektirmez ve iki ifade birbirinin yerine geçmez.","focus_only":"Odak dal yabancılığın kalkmasıyla doğan duygusal yakınlığı ve rahatlığı anlatır.","gloss":"yakınlık durumu ile insan adı ayrımı","neighbor_only":"Komşu dal insan türünü, insan topluluğunu veya bu türden tek bir kişiyi adlandırır.","neighbor_ref":"root_000059/B001","relation_type":"same_field","shared_zone":"İnsan, iki dalda da temel katılımcı veya gönderim noktasıdır."}],"source_phrase_ar":"الأنس أنس الإنسان بالشيء إذا لم يستوحش منه (maqayis)؛ الإيناس خلاف الإيحاش والإنس خلاف الوحشة والأنيس المؤانس وكل ما يؤنس به (sihah)؛ أنست بفلان أي فرحت به والأنس والاستئناس هو التأنس وكلب أنوس نقيض العقور (tahdhib)؛ الأنس خلاف النفور ولكل ما يؤنس به (mufradat)","source_summary":"Ortak çekirdek, yabancılık ve kaçınmanın karşıtı olan yakınlık ve rahatlıktır. Bu durum birine alışıp onun yanında sevinmeyi, rahatlık veren kişi veya şeyi ve insana alışık saldırgan olmayan hayvanı kapsayacak biçimde genişler.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه أنس الإنسان بالشيء أو بفلان، المؤانسة والتأنيس، الأنيس وكل ما يؤنس به، الفرح بالقرب والحديث، والحيوان الأنوس غير العقور.","what_is_not_ar":"لا يدخل الإنس بمعنى البشر ولا الإيناس بمعنى الإبصار ولا الجانب الإنسي إلا بدليل."},"support_links":["sup_5588a2cd2cacf5478919"]},{"boundary":"Dal, bir nesnenin insana veya kullanıcıya bakan yanını belirtir; salt sol, salt sağ, genel ön taraf ya da insanın kendisi anlamına gelmez.","branch_kind":"bare","branch_ref":"root_000059/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"96:6:3:2","qac_word_ref":"96:6:3","surface_ar":"إِنسَٰنَ"}],"gloss":"insana dönük yan","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin insana en yakın olan veya insana doğru bakan yanını belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvanda binicinin bulunduğu, binme ve sağma işlemlerinde insana yakın olan yanı anlatır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yayda okçuya doğru bakan ve kullanıcının karşısında bulunan yanı anlatır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İnsana yakın yan bazı aktarımda sol, başka bir aktarımda sağ diye belirlenir; yönün özü bu değişken tanımlardan bağımsızdır."}}],"root_ar":"ء ن س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin yönü, ona yaklaşan veya onu kullanan insana göre belirlendiğinde dalın ortak çekirdeğini verir.","boundary_detail":"Dal, bir nesnenin insana veya kullanıcıya bakan yanını belirtir; salt sol, salt sağ, genel ön taraf ya da insanın kendisi anlamına gelmez.","branch_image_ar":"الجانب الإنسي المقبل على الإنسان","concept_gloss":"insana dönük yan","contextual_glosses":[{"applicability":"Hayvanın binme ve sağma sırasında insana yakın kalan yanı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın yanını biniciyle kurduğu işlevsel ilişkiye göre belirler."},"facet_ids":["F002"],"text":"biniciye yakın yan","usage_role":"contextual"},{"applicability":"Yayın kullanım sırasında okçuya doğru dönük olan yüzü belirtilirken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yay yüzünün yönünü okçunun konumuna göre belirleme özelliğini korur."},"facet_ids":["F003"],"text":"okçuya bakan yay yüzü","usage_role":"explanatory"}],"definition":"Bir nesnenin insana, kullanıcıya veya onun bulunduğu yöne bakan yanıdır. Hayvan ve yay üzerinde işlevsel ilişkiyle belirlenir; bu yanın sabit olarak sol ya da sağ sayılması konusunda aktarım uyuşmazlığı vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin insana en yakın olan veya insana doğru bakan yanını belirtir."},{"facet_id":"F002","role":"specialization","statement":"Hayvanda binicinin bulunduğu, binme ve sağma işlemlerinde insana yakın olan yanı anlatır."},{"facet_id":"F003","role":"specialization","statement":"Yayda okçuya doğru bakan ve kullanıcının karşısında bulunan yanı anlatır."},{"facet_id":"F004","role":"source_variant","statement":"İnsana yakın yan bazı aktarımda sol, başka bir aktarımda sağ diye belirlenir; yönün özü bu değişken tanımlardan bağımsızdır."}],"identity_rationale":"Kaynak ifadesinin güvenilir çekirdeği, bir şeyin insana veya onu kullanan kişiye dönük ve yakın olan yanıdır. Bu yanın solda mı sağda mı olduğu konusunda aktarımlar uyuşmaz; hayvan ve yay örnekleri yönü işlevsel ilişkiyle belirler. Bu nedenle sabit bir sağ-sol tanımı dalın özüne konamaz.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir şeyin insana bakan veya en yakın olan yanı"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yayın okçuya bakan yüzü"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"hayvanın biniciye yakın olan yanı"}],"lexicalization_note":"Tanım çıplak dalın insana dönük yan çekirdeğiyle sınırlıdır. Hayvan ve yay uygulamaları bu çekirdeğin örneklenmesidir; yalnız bu kullanımlardan yeni bir genel yön anlamı çıkarılmaz.","neighbor_coverage_note":"Adayların tamamı incelendi. Genel ön taraf, yönelme eylemi ve arka bölümle kurulan karşılaştırmalar insana göre belirlenen yanın sınırını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda yön, insanın nesneyle kurduğu konum veya kullanım ilişkisine bağlıdır. Komşu dalın genel ön ve yakın anlamları bu özel bağı gerektirmez.","focus_only":"Odak dal bir nesnenin insana veya onu kullanan kişiye dönük yanını ilişkiye göre belirler.","gloss":"insana dönük yan ile genel ön taraf","neighbor_only":"Komşu dal genel olarak ön, önde, yakın veya karşıda bulunma yönlerini kişiye bağlı bir kullanım ilişkisi gerektirmeden anlatır.","neighbor_ref":"root_000053/B011","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin bakana göre karşıda veya önde kalan bölümünü gösterebilir."},{"boundary_match":"partial","distinction":"Bir nesnenin insana dönük yanı bir bölüm adıdır; komşu ise dönme veya yönelme olayını anlatır. Sonuç konumu ile o konuma geçiş eylemi birbirinin yerine kullanılamaz.","focus_only":"Odak dal, yönelme tamamlandıktan sonra insana dönük olan sabit yanı adlandırır.","gloss":"dönük yan ile yönelme eylemi","neighbor_only":"Komşu dal yüz, baş, el, kap veya hayvanın bir hedefe doğru dönmesi ve yönelmesi eylemini anlatır.","neighbor_ref":"root_001263/B003","relation_type":"near_neighbor","shared_zone":"İki dal da bir kişi veya hedefe doğru bakma yönünü içerir."},{"boundary_match":"partial","distinction":"Bağlama göre karşıt görünebilseler de odak dal her zaman geometrik ön yüz değildir ve bu yüzden düzenli bir karşıt çift oluşturmaz; belirleyici ölçüt insana yakınlıktır.","focus_only":"Odak dal insana veya kullanıcıya yakın ve ona bakan yanı gösterir.","gloss":"insana bakan yan ile arka taraf","neighbor_only":"Komşu dal bir şeyin arkasında kalan, yüzünün karşıtı olan arka bölümünü gösterir.","neighbor_ref":"root_000458/B001","relation_type":"near_neighbor","shared_zone":"İki dal da bir nesnenin başka bir yöne göre belirlenen bölümünü adlandırır."}],"source_phrase_ar":"الإنسي الأيسر من كل شيء وقيل الأيمن وما أقبل منهما على الإنسان فهو إنسي وإنسي القوس ما أقبل عليك منها (sihah)؛ الإنسي من الدواب الجانب الأيسر الذي منه يركب ويحتلب ومن الإنسان الجانب الذي يلي الرجل الأخرى (tahdhib)؛ إنسي الدابة للجانب الذي يلي الراكب وإنسي القوس للجانب الذي يقبل على الرامي (mufradat)","source_summary":"Ortak anlam, nesnenin insana veya kullanıcıya dönük yanıdır; hayvanda biniciye, yayda okçuya göre belirlenir. İnsan bedenindeki tekil uygulamada öteki bacağa bakan yan kastedilir. Bu yanın solda mı sağda mı bulunduğuna ilişkin anlatımlar ayrıştığı için genel tanım sabit bir yön seçmez.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه إنسي الدابة والقوس وكل شيئين: ما يلي الإنسان أو يقبل على الراكب أو الرامي، في مقابلة الوحشي.","what_is_not_ar":"لا يدخل الإنسان نفسه ولا الأنس النفسي ولا الإبصار."},"support_links":[]},{"boundary":"Dal göz bebeğinde görülen küçük görüntüyü, ayrıca ayrı bir aktarım olarak parmak ucunu kapsar; gözün kendisini veya genel insan türünü belirtmez.","branch_kind":"bare","branch_ref":"root_000059/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"96:6:3:2","qac_word_ref":"96:6:3","surface_ar":"إِنسَٰنَ"}],"gloss":"göz bebeğinde görülen küçük yansıma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Göz bebeğinin kara bölümünde görülen küçük insan biçimli görüntüyü veya yansımayı adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı bir aktarımda parmak ucu veya eldeki parmak ucunu anlatan kullanım da aynı adla verilir."}}],"root_ar":"ء ن س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir bakanın göz bebeğinde beliren küçük insan biçimli görüntü adlandırıldığında dalın ortak ve temel anlamını karşılar.","boundary_detail":"Dal göz bebeğinde görülen küçük görüntüyü, ayrıca ayrı bir aktarım olarak parmak ucunu kapsar; gözün kendisini veya genel insan türünü belirtmez.","branch_image_ar":"إنسان العين وصورة الإنسان في السواد","concept_gloss":"göz bebeğinde görülen küçük yansıma","contextual_glosses":[{"applicability":"Yansımanın insan biçiminde algılanması özellikle belirtilmek istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Görüntünün göz bebeğinde bulunmasını ve küçük insan biçiminde görünmesini korur."},"facet_ids":["F001"],"text":"göz bebeğindeki küçük insan görüntüsü","usage_role":"explanatory"},{"applicability":"Yalnız parmak ucunu aynı adla veren ayrı kaynak kullanımında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Göz anlamından bağımsız olan parmak ucu kullanımını doğrudan korur."},"facet_ids":["F002"],"text":"parmak ucu","usage_role":"contextual"}],"definition":"Gözün kara bölümünde görülen küçük insan biçimli görüntü veya yansımadır. Ayrı bir kaynak kullanımında aynı ad parmak ucuna da verilir, ancak bu kullanım göz görüntüsü çekirdeğini değiştirmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Göz bebeğinin kara bölümünde görülen küçük insan biçimli görüntüyü veya yansımayı adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Ayrı bir aktarımda parmak ucu veya eldeki parmak ucunu anlatan kullanım da aynı adla verilir."}],"identity_rationale":"Kaynak ifadesinin ortak çekirdeği, gözün kara bölümünde görülen küçük insan biçimli görüntü veya yansımadır. Parmak ucu anlamı tek aktarım içinde eklenir ve gözdeki görüntünün kurucu parçası değildir; bağımlı bir kaynak varyantı olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"göz bebeğinde görülen küçük görüntü veya yansıma"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"göz bebeklerinde görülen küçük görüntüler"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"parmak ucu; eldeki parmak ucunu anlatan kullanım"}],"lexicalization_note":"Çıplak dalın çekirdeği gözün kara bölümündeki küçük görüntüdür. Parmak ucu aktarımı bağımlı bir varyanttır; gözle ilgili belirli biçimlerden genel görüntü veya genel insan anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün aday kartlar değerlendirildi. Anatomik göz bebeği, genel tasvir ve göz organı karşılaştırmaları görüntünün yerini ve türünü en iyi sınırladığı için bu üçü yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Komşu anatomik bölümün kendisidir; odak dal ise o bölümde görülen görüntüdür. Taşıyıcı yapı ile üzerinde beliren yansıma birbirinin yerine kullanılamaz.","focus_only":"Odak dal göz bebeğinde görülen küçük insan biçimli görüntüyü veya yansımayı adlandırır.","gloss":"göz bebeği ile göz bebeğindeki yansıma","neighbor_only":"Komşu dal göz bebeğinin kendisini, onun kara bölümünü ve anatomik yapısını adlandırır.","neighbor_ref":"root_000300/B002","relation_type":"same_field","shared_zone":"İki dal aynı göz bölgesine gönderimde bulunur."},{"boundary_match":"partial","distinction":"Odak görüntü göz bebeğindeki belirli yansımadır; komşu ise konum ve oluşum biçimi bakımından çok daha genel tasvirleri kapsar. Her tasvir gözdeki yansıma değildir.","focus_only":"Odak dal yalnız göz bebeğinde beliren küçük insan biçimli görüntüyü ve ayrı bir parmak ucu varyantını kapsar.","gloss":"gözdeki yansıma ile genel tasvir","neighbor_only":"Komşu dal resim, model, heykel veya başka bir varlığa göre biçimlendirilmiş genel örnekleri kapsar.","neighbor_ref":"root_001397/B008","relation_type":"near_neighbor","shared_zone":"Her iki dal başka bir varlığın görünüşünü taşıyan bir görüntüyü anlatabilir."},{"boundary_match":"field_only","distinction":"Göz, görmeyi sağlayan organdır; odak dal ise gözde görülen yansımadır. Organın adı yansımanın, yansımanın adı da organın genel karşılığı değildir.","focus_only":"Odak dal gören gözün içinde beliren küçük görüntüyü adlandırır.","gloss":"göz organı ile içindeki küçük görüntü","neighbor_only":"Komşu dal görme organı olan gözün kendisini ve onun görme işlevini adlandırır.","neighbor_ref":"root_001069/B001","relation_type":"same_field","shared_zone":"Her iki dal göz ve görme alanına aittir."}],"source_phrase_ar":"إنسان العين صبيها الذي في السواد (maqayis)؛ إنسان العين المثال الذي يرى في السواد أي سواد العين (sihah)؛ الإنسان أيضا إنسان العين وجمعه أناسي والإنسان الأنملة (tahdhib)","source_summary":"Ortak aktarım, göz bebeğinin kara bölümünde görülen küçük görüntüyü bir insan biçimi olarak tanımlar. Buna ek olarak parmak ucu anlamı da bildirilir, fakat bu ek kullanım gözdeki yansıma çekirdeğinden ayrı tutulur.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه إنسان العين: المثال أو الصبي الذي يرى في سواد العين، وما ألحقه تهذيب اللغة من الأنملة أو إنسان الكف.","what_is_not_ar":"لا يدخل الإنسان بمعنى البشر عموما ولا الأنس بمعنى الراحة."},"support_links":[]},{"boundary":"Dal yalnız belirtilen söz kuruluşlarında kişinin kendisini veya seçkin yakınını gösterir; genel insan, gerçek evlatlık ve her türlü arkadaşlık anlamına genişletilemez.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"96:6:3:2","qac_word_ref":"96:6:3","surface_ar":"إِنسَٰنَ"}],"gloss":"belirli sözlerde kişinin kendisi veya seçilmiş yakını","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiye kendi durumunu soran belirli kuruluşta muhatabın kendisini gösterir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişiye bağlanarak söylendiğinde onun seçilmiş yakınını, özel arkadaşını veya sırdaşını belirtir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı anlam çevresindeki paralel adlar yakın dostu, içten arkadaşı ve oturup konuşulan kişiyi gösterebilir."}}],"root_ar":"ء ن س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kaynakta gösterilen soru ve kişi bağlantısı kuruluşlarını topluca açıklarken kullanılabilir; genel bir kişi ya da akraba adı değildir.","boundary_detail":"Dal yalnız belirtilen söz kuruluşlarında kişinin kendisini veya seçkin yakınını gösterir; genel insan, gerçek evlatlık ve her türlü arkadaşlık anlamına genişletilemez.","branch_image_ar":"ابن الإنس للنفس والصفوة","concept_gloss":"belirli sözlerde kişinin kendisi veya seçilmiş yakını","contextual_glosses":[{"applicability":"Muhataba kendi durumunun nasıl olduğu sorulduğunda doğal Türkçe karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sorunun muhatabın kendi durumuna yönelmesini korur."},"facet_ids":["F001"],"text":"kendin; nasılsın","usage_role":"contextual"},{"applicability":"Bir kişinin seçip özel tuttuğu yakın arkadaş veya sırdaş anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yakın kişinin seçilmiş, özel ve güvenilen biri olmasını korur."},"facet_ids":["F002"],"text":"onun en yakını ve sırdaşı","usage_role":"contextual"},{"applicability":"Yakın dost, içten arkadaş ve birlikte oturup konuşulan kişi için sıralanan paralel adları açıklarken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yakınlık, dostluk ve sürekli görüşme ilişkilerini birlikte korur."},"facet_ids":["F003"],"text":"yakın dostum ve görüşme arkadaşım","usage_role":"explanatory"}],"definition":"Belirli bir soru kuruluşunda muhatabın kendisini ve durumunu, başka bir kişiyle kurulan adlandırmada ise onun seçilmiş yakınını, sırdaşını veya sürekli görüştüğü arkadaşını belirtir. İki kullanım aynı kuruluş ailesinde bulunsa da katılımcı ilişkileri ayrıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiye kendi durumunu soran belirli kuruluşta muhatabın kendisini gösterir."},{"facet_id":"F002","role":"core","statement":"Bir kişiye bağlanarak söylendiğinde onun seçilmiş yakınını, özel arkadaşını veya sırdaşını belirtir."},{"facet_id":"F003","role":"associated_use","statement":"Aynı anlam çevresindeki paralel adlar yakın dostu, içten arkadaşı ve oturup konuşulan kişiyi gösterebilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Gerçek bir baba ile erkek çocuk arasındaki soy ilişkisini ekler.","collision":"Sözün amaçlanan kişi ilişkisini gerçek akrabalıkla karıştırır.","fit":"displacement","loses":"Kişinin kendisini veya seçilmiş yakınını gösteren kalıplaşmış gönderimi kaybeder.","preserves":"Kuruluşun yüzeyindeki çocuk ve soy ilişkisi çağrışımını korur."},"text":"oğlu"}],"identity_rationale":"Kaynak ifadesi iki ayrı kalıplaşmış ilişkiyi açıkça ayırır: kişiye kendi durumunu soran sözde kişinin kendisi, bir başkasına bağlanan sözde ise seçilmiş yakın ve sırdaş kastedilir. Yakın arkadaş ve oturup konuşulan kişi için verilen paralel adlar ikinci alanı destekler.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"kendin; kendi durumun nasıl"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"onun seçkin yakını ve sırdaşı"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"yakınım, içten dostum ve görüşme arkadaşım"}],"lexicalization_note":"Kişinin kendisini soran kuruluş, seçilmiş yakını belirten kuruluş ve yakın arkadaş adları ayrı tutulur. Bunların hiçbiri çıplak biçime genel kişi veya akrabalık anlamı olarak taşınmaz.","neighbor_coverage_note":"Aday kartların tamamı incelendi. Kişinin kendisini gösteren başka kuruluş, iç çevre ve genel dostluk alanları iki ayrı gönderimi en iyi sınırlandırdığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ortak gönderim yalnız benlik anlamındadır; kuruluşlar değiştirilemez. Odak dalın seçilmiş yakın ve sırdaş anlamı komşuda bulunmaz.","focus_only":"Odak dal kişinin kendisini belirli bir soru kuruluşunda gösterir ve ayrıca seçilmiş yakın anlamını da taşır.","gloss":"kişinin kendisini gösteren iki ayrı söz","neighbor_only":"Komşu dal şiirsel bir söyleyişte yalnız kişinin kendi benliğini başka bir kalıpla belirtir.","neighbor_ref":"root_001271/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal belirli bir söz kuruluşunda kişinin kendisine gönderimde bulunur."},{"boundary_match":"partial","distinction":"Odak dal çoğunlukla tek bir yakın veya sırdaşı gösterir; komşu kişinin iç çevresini ve işlerine alınan özel kişileri daha geniş kapsar.","focus_only":"Odak dal seçilmiş yakını ve sırdaşı gösterebilir, fakat kişinin kendisini soran ayrı bir kullanım da içerir.","gloss":"seçilmiş yakın ile iç çevre","neighbor_only":"Komşu dal bir kişinin işine ve sırrına alınan bütün iç çevreyi ve özel kişileri topluluk olarak kapsayabilir.","neighbor_ref":"root_000128/B004","relation_type":"near_neighbor","shared_zone":"Güvenilen ve özel tutulan kişi iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Her dost odak daldaki özel adlandırmanın taşıdığı seçilmiş yakın değildir; odak dalın kişinin kendisine gönderimi de genel dostluk alanının dışındadır.","focus_only":"Odak dal özel kuruluşlarla kişinin kendisini ya da seçilmiş yakınını belirtir.","gloss":"seçilmiş sırdaş ile genel dostluk","neighbor_only":"Komşu dal arkadaşlık ve dostluk ilişkisini açık ya da gizli yönleriyle genel olarak anlatır.","neighbor_ref":"root_000397/B001","relation_type":"near_neighbor","shared_zone":"Seçilmiş yakın kişi aynı zamanda dost veya arkadaş olabilir."}],"source_phrase_ar":"كيف ابن إنسك إذا سأله عن نفسه (maqayis)؛ كيف ابن إنسك يعني نفسه وفلان ابن إنس فلان أي صفيه وخاصته وهذا خدني وإنسي وخلصي وجلسي (sihah)؛ كيف ترى ابن إنسك إذا خاطبت الرجل عن نفسه وفلان ابن أنس فلان أي صفيه وأنيسه (tahdhib)؛ قيل ابن إنسك للنفس (mufradat)","source_summary":"Aktarımlar, doğrudan hitapta kişinin kendi durumunu soran kullanım ile birinin seçkin yakını ve sırdaşını gösteren kullanımı birlikte verir. Yakın dost ve sürekli görüşülen arkadaş anlamındaki paralel adlar ikinci ilişki alanını genişletir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه كيف ابن إنسك للسؤال عن النفس، وفلان ابن أنس فلان لصفيه وخاصته، وما قاربه من الخدن والأنيس والخلص والجليس.","what_is_not_ar":"لا يدخل مطلق الإنسان ولا مطلق المؤانسة إلا إذا جاء بصيغة هذا الباب أو قرينته."},"support_links":[]},{"boundary":"Dal eve girmeden önce izin ve kabul arama durumuyla sınırlıdır; genel görme, genel yakınlık, eve yerleşme veya barınma anlamına gelmez.","branch_kind":"unresolved","branch_ref":"root_000059/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"96:6:3:2","qac_word_ref":"96:6:3","surface_ar":"إِنسَٰنَ"}],"gloss":"girişten önce izin ve kabul arama","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eve girmeden önce selam verip girmek için izin istemeyi ve kabul beklemeyi anlatır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı açıklama, girişten önce içeridekilerden yakınlık ve kabul işareti bulmayı öne çıkarır."}}],"root_ar":"ء ن س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir eve girmeden önce selam, izin sorusu veya içeridekilerin kabulünü yoklama yoluyla girişe onay arandığında kullanılır.","boundary_detail":"Dal eve girmeden önce izin ve kabul arama durumuyla sınırlıdır; genel görme, genel yakınlık, eve yerleşme veya barınma anlamına gelmez.","branch_image_ar":"الاستئناس قبل دخول البيوت","concept_gloss":"girişten önce izin ve kabul arama","contextual_glosses":[{"applicability":"Giriş izninin selam ve açık bir izin sorusuyla istendiğini belirten açıklamada uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Selam verme, izin sorma ve girişten önce bekleme işlemlerini korur."},"facet_ids":["F001"],"text":"selam verip girebilir miyim diye sormak","usage_role":"explanatory"},{"applicability":"İçeridekilerin yakınlık ve kabul gösterdiğini anlayarak girişe elverişli ortam bulma yorumunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Girişten önce kabul ve yakınlık işareti bulma yönünü korur."},"facet_ids":["F002"],"text":"girişe açık bir karşılama bulmak","usage_role":"contextual"}],"definition":"Bir eve girmeden önce selam vererek izin istemeyi ve içeridekilerin girişe açık olduğunu anlamayı anlatır. Aktarımın bir yönü doğrudan izin sorusunu, diğer yönü girişe elverişli bir kabul ve yakınlık bulmayı öne çıkarır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eve girmeden önce selam verip girmek için izin istemeyi ve kabul beklemeyi anlatır."},{"facet_id":"F002","role":"source_variant","statement":"Ayrı açıklama, girişten önce içeridekilerden yakınlık ve kabul işareti bulmayı öne çıkarır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yalnız gözle inceleme ve bir şeyi görme anlamını ekler.","collision":"Duyusal fark etme ve çevreye bakıp araştırma dalıyla karışır.","fit":"displacement","loses":"Selam verme, izin isteme ve içeridekilerin kabulünü bekleme koşullarını kaybeder.","preserves":"Girişten önce çevreyi yoklama düşüncesine sınırlı ölçüde yaklaşır."},"text":"bakıp görmek"}],"identity_rationale":"Kaynak ifadesi yalnız eve giriş öncesindeki belirli söz çevresinde açıklanır. Bir aktarım bunu selam verip izin isteme ve girebilir miyim diye sorma olarak, diğeri ise girişe elverişli bir kabul ve yakınlık bulma olarak yorumlar. Dal bu iki açıklamayı korumalı, fakat çıplak biçime genel bakma veya genel rahatlık anlamı yüklememelidir.","lexicalization_note":"Mekanik kapsam çözümlenmemiştir ve eldeki kanıt yalnız giriş öncesi kuruluşu gösterir. Bu nedenle tanım bu söz çevresine bağlanır, çıplak bir genel anlam varsayılmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı. Genel yakınlık, çevreyi gözleme ve barınma senaryosu giriş öncesi izin sınırını en iyi açıkladığı için bu üç ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir giriş davranışı ve onay koşuludur; komşu dal yer ve zamanla sınırlı olmayan duygusal durumdur. Genel yakınlık, giriş izninin yerine geçmez.","focus_only":"Odak dal eve girişten önce selam, izin sorusu ve kabul bekleme yoluyla yürütülen sınırlı bir davranışı anlatır.","gloss":"giriş kabulü ile genel yakınlık duygusu","neighbor_only":"Komşu dal kişi veya şey karşısında genel olarak yabancılık ve ürkme duymayıp yakınlık ve rahatlık hissetmeyi anlatır.","neighbor_ref":"root_000059/B003","relation_type":"near_neighbor","shared_zone":"Kabul gören kişi giriş öncesinde kendini yabancı hissetmeyebilir ve yakınlık işareti bulabilir."},{"boundary_match":"partial","distinction":"Çevreyi gözlemek yalnız bilgi edinir; odak dal içeridekilerden onay almayı amaçlar. Birini görmek veya sesini duymak, tek başına giriş izni değildir.","focus_only":"Odak dal girişten önce selam verip izin ve kabul aramayı gerektirir.","gloss":"izin arama ile çevreyi gözleme","neighbor_only":"Komşu dal görme, işitme, belirti sezme veya çevreye bakarak birini araştırma eylemlerini anlatır.","neighbor_ref":"root_000059/B002","relation_type":"near_neighbor","shared_zone":"Girişten önce içeride birinin bulunup bulunmadığını anlamaya çalışma iki alanı aynı durumda buluşturabilir."},{"boundary_match":"thematic_only","distinction":"Odak dal girişten önceki toplumsal onayı, komşu dal ise bir yere yönelip orada barınmayı anlatır; aralarında sıradan sözcüksel yer değiştirme yoktur.","focus_only":"Odak dal bir eve girmeden önce kabul ve izin arama davranışıdır.","gloss":"eve giriş izni ile barınma","neighbor_only":"Komşu dal bir yere sığınma, yerleşme, barınma veya başkasını barındırma hareketini anlatır.","neighbor_ref":"root_000070/B001","relation_type":"thematic","shared_zone":"İki dal da bir yerle insan arasındaki giriş ve bulunma senaryosunda yer alabilir."}],"source_phrase_ar":"حتى تستأنسوا معناه حتى تستأذنوا وإنما هو حتى تسلموا وتستأنسوا السلام عليكم أأدخل (tahdhib)؛ حتى تستأنسوا أي تجدوا إيناسا (mufradat)","source_summary":"Giriş öncesi davranış iki yönden açıklanır: selam verip açıkça izin istemek ve girebilir miyim diye sormak ya da içeridekilerden girişe elverişli bir kabul ve yakınlık bulmak. Her iki açıklama da eve izinsiz girmeme sınırında birleşir.","sources":["TA","MU"],"what_is_ar":"يدخل فيه تفسير حتى تستأنسوا بالاستئذان أو السلام وطلب الدخول، أو بإيجاد إيناس قبل الدخول.","what_is_not_ar":"لا يدخل مطلق الإبصار أو مطلق الأنس إلا في صيغة الدخول المذكورة."},"support_links":[]},{"boundary":"Bu dal, fiziksel taşmayı, belirli bir saptırıcı varlığın adını ve aynı kökün bağımsız sözlükleşmiş anlamlarını kapsamaz.","branch_kind":"bare","branch_ref":"root_000936/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:TagaY`|ROOT:Tgy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:6:4:2","qac_word_ref":"96:6:4","surface_ar":"يَطْغَىٰٓ"}],"gloss":"başkaldırıda sınırı aşma ve buna sürükleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başlıca anlam, başkaldırı ve karşı gelmede ölçüyü ya da sınırı aşmaktır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ettirgen biçimde bir etken, başka birini sınırı aşan başkaldırıya sürükler veya öyle biri haline getirir."}}],"root_ar":"ط غ ي","root_id":"root_000936","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu ifade hem sınırı aşan öznenin temel eylemini hem de başka bir özneyi aynı duruma götüren ettirgen katmanı birlikte anlatır.","boundary_detail":"Bu dal, fiziksel taşmayı, belirli bir saptırıcı varlığın adını ve aynı kökün bağımsız sözlükleşmiş anlamlarını kapsamaz.","branch_image_ar":"مجاوزة الحد في العصيان","concept_gloss":"başkaldırıda sınırı aşma ve buna sürükleme","contextual_glosses":[{"applicability":"Bir kişinin başkaldırıda ölçüyü aşmış durumunu adlandıran bağlamlarda doğal ve kısa bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir başkasını bu duruma sürükleyen ettirgen katılımcı değişimini tek başına göstermez.","preserves":"Ölçüyü aşan başkaldırı ve taşkın davranış çekirdeğini korur."},"facet_ids":["F001"],"text":"azgınlık","usage_role":"contextual"},{"applicability":"Bir etkenin başka birini başkaldırıda sınırı aşar hale getirdiği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öznenin kendiliğinden sınırı aşmasını anlatan yalın kullanım kapsam dışında kalır.","preserves":"Başka birini aşırılığa sürükleyen ettirgen ilişkiyi korur."},"facet_ids":["F002"],"text":"azdırmak","usage_role":"contextual"}],"definition":"Bir kişi ya da şeyin başkaldırı ve karşı gelmede olağan veya meşru sınırı aşmasıdır; ettirgen kullanımda ise bir etken başkasını bu aşırılığa sürükler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başlıca anlam, başkaldırı ve karşı gelmede ölçüyü ya da sınırı aşmaktır."},{"facet_id":"F002","role":"extension","statement":"Ettirgen biçimde bir etken, başka birini sınırı aşan başkaldırıya sürükler veya öyle biri haline getirir."}],"identity_rationale":"Kaynak ifadesi, başkaldırı ve karşı gelmede sınırı ya da ölçüyü aşmayı çekirdek anlam olarak verir; ayrıca bir etkenin başkasını bu aşırılığa sürüklediği ettirgen kullanımı açıkça ayırır. Geçici çerçeve bu iki katmanı doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"başkaldırıda sınırı aşmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"başkaldırıda sınırı aşan"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"başkaldırıda sınırı aşma"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"azdırmak; sınırı aşmaya sürüklemek"}],"lexicalization_note":"Tanım yalın dalın sınır aşan başkaldırı çekirdeğini ve onun ettirgen katılımcı değişimini kapsar; başka dallardaki kalıba bağlı anlamları içeri almaz.","neighbor_coverage_note":"Listelenen bütün komşu adayları değerlendirildi; yalnızca çekirdekle güçlü biçimde örtüşüp sınırı açıklayan iki karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdekler büyük ölçüde örtüşür; ancak komşunun zorba kişiyi de kapsayan daha geniş sınırı, odak dalın eylem ve ettirgenlik merkezli sınırıyla tam örtüşmez.","focus_only":"Odak dal, bir etkenin başkasını sınır aşan başkaldırıya sürüklemesini açıkça ayrı bir katman olarak düzenler.","gloss":"sınırı aşan başkaldırı","neighbor_only":"Komşu dal, zorba kişiyi de aynı dalın içinde sayarak kişi adlandırmasını eylem alanına katar.","neighbor_ref":"root_000937/B001","relation_type":"near_synonym","shared_zone":"İki dal da başkaldırıda ölçüyü aşma çekirdeğini ve bu duruma götüren ettirgen kullanımı paylaşır."},{"boundary_match":"partial","distinction":"Komşu genel ve eylem alanları bakımından geniş bir ölçüsüzlük kavramıdır; odak ise bunun başkaldırıya özgü türüdür.","focus_only":"Odak dal, sınır aşmayı özellikle başkaldırı ve karşı gelme alanıyla sınırlar.","gloss":"ölçüyü aşma","neighbor_only":"Komşu dal, para harcama, öldürme, yeme ve su kullanma gibi birçok alandaki ölçüsüzlüğü de kapsar.","neighbor_ref":"root_000699/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da belirlenmiş bir sınırı ya da uygun ölçüyü aşma düşüncesi vardır."}],"source_phrase_ar":"مجاوزة الحد في العصيان (maqayis;sihah;mufradat)؛ كل شيء جاوز القدر فقد طغا (tahdhib)؛ أطغاه المال أي جعله طاغيا وأطغاه كذا حمله على الطغيان (sihah;mufradat)","source_summary":"Kaynaklar, başkaldırıda ölçüyü aşma anlamında birleşir ve ettirgen biçimin para ya da başka bir etken yoluyla birini bu duruma getirdiğini belirtir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الطغيان والطغوان والطغوى، وطغا بمعنى جاوز الحد أو القدر في العصيان، وأطغاه غيره إذا جعله أو حمله على الطغيان.","what_is_not_ar":"لا يدخل فيه فيض الماء والبحر، ولا اسم الطاغوت الخاص، ولا شواذ الطغية والطغيا."},"support_links":[]},{"boundary":"Anlam yalnızca belirtilen su, kan, ses ve rüzgar kalıplarında geçerlidir; insanın başkaldırısını anlatan yalın dala genellenmez.","branch_kind":"collocation","branch_ref":"root_000936/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:TagaY`|ROOT:Tgy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:6:4:2","qac_word_ref":"96:6:4","surface_ar":"يَطْغَىٰٓ"}],"gloss":"su, kan, ses ya da rüzgarın sınırını aşıp baskınlaşması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Suya ilişkin kullanımlarda sel bol su getirir, deniz kabarır veya su olağan düzeyini aşıp sürükleyici olur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kan için kullanım, kanın şiddetle coşup olağan durumunu aşmasını anlatır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ses ve rüzgar için kullanım, bunların güçlenip baskın hale gelmesine uzanır."}}],"root_ar":"ط غ ي","root_id":"root_000936","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu açıklama yalnızca kanıtlanan adlarla kurulan kalıplarda, olağan düzeyin aşılması ve gücün baskın hale gelmesi anlamını verir.","boundary_detail":"Anlam yalnızca belirtilen su, kan, ses ve rüzgar kalıplarında geçerlidir; insanın başkaldırısını anlatan yalın dala genellenmez.","branch_image_ar":"طغيان الماء وما يجري مجراه","concept_gloss":"su, kan, ses ya da rüzgarın sınırını aşıp baskınlaşması","contextual_glosses":[{"applicability":"Su ya da selin olağan sınırını aşıp çevreye yayılması anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Denizin kabarmasını, kanın coşmasını ve ses ile rüzgarın baskınlaşmasını tek başına kapsamaz.","preserves":"Suyun olağan düzeyi aşarak yayılması çekirdeğini korur."},"facet_ids":["F001"],"text":"taşmak","usage_role":"contextual"},{"applicability":"Deniz dalgalarının ya da kanın şiddetle kabarıp olağan durumunu aşması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Suyun sürükleyiciliğini ve ses ile rüzgarın üstün gelmesini açıkça göstermez.","preserves":"Denizin veya kanın şiddetlenip olağan durumunu aşmasını korur."},"facet_ids":["F001","F002"],"text":"coşmak","usage_role":"contextual"},{"applicability":"Sesin ya da rüzgarın gücünün ötekileri bastırdığı bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Su ve kanın fiziksel olarak kabarıp sınırı aşması kapsam dışında kalır.","preserves":"Ses veya rüzgarın güçlenerek üstün duruma gelmesini korur."},"facet_ids":["F003"],"text":"baskın gelmek","usage_role":"contextual"}],"definition":"Sel, deniz ya da suyun olağan düzeyini aşıp kabarması ve kimi zaman önüne geleni sürüklemesi; kanın coşması veya ses ile rüzgarın baskınlaşmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Suya ilişkin kullanımlarda sel bol su getirir, deniz kabarır veya su olağan düzeyini aşıp sürükleyici olur."},{"facet_id":"F002","role":"extension","statement":"Kan için kullanım, kanın şiddetle coşup olağan durumunu aşmasını anlatır."},{"facet_id":"F003","role":"extension","statement":"Ses ve rüzgar için kullanım, bunların güçlenip baskın hale gelmesine uzanır."}],"identity_rationale":"Kaynak ifadesi selin bol su getirmesini, denizin kabarıp dalgalanmasını, suyun yükselip sürüklemesini ve kanın taşkınlaşmasını aynı fiziksel sınır aşımı altında toplar; ses ile rüzgarın üstün gelmesi de buna bağlı bir genişlemedir. Geçici çerçeve bu yapıyı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"sel bol suyla taşmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"deniz kabarıp sürükleyici olmak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"su olağan düzeyini aşmak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kan coşmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ses ya da rüzgar baskın gelmek"}],"lexicalization_note":"Tanım, yalnızca sel, deniz, su, kan, ses ve rüzgarla kurulan belirtilmiş kalıplara bağlıdır; bunlardan bağımsız bir yalın kök anlamı olarak sunulmaz.","neighbor_coverage_note":"Bütün adaylar kapsam ve çekirdek bakımından karşılaştırıldı; eş anlamlı dal ile taşma, kuşatma ve doluluk sınırını açıklayan iki yakın alan yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Kanıtlanan çekirdek, örnek alanları ve kapsam sınırı bakımından anlamlı bir ayrım yoktur.","focus_only":null,"gloss":"taşkın fiziksel güç","neighbor_only":null,"neighbor_ref":"root_000937/B002","relation_type":"synonym","shared_zone":"İki dal da su, sel, deniz ve kanın yükselmesini; ses ile rüzgarın da baskınlaşmasını aynı sınırla kapsar."},{"boundary_match":"partial","distinction":"Odak için belirleyici olan olağan ölçünün aşılmasıdır; komşuda ise çevreyi bütünüyle kaplama ve kuşatma öne çıkar.","focus_only":"Odak dal, suyun yanı sıra kan, ses ve rüzgarın ölçüyü aşıp baskınlaşmasını da içerir.","gloss":"çevreyi kaplayan büyük sel","neighbor_only":"Komşu dal, kuşatıp her yanı kaplayan yağmur, karanlık ve genel olayları da kapsar.","neighbor_ref":"root_000957/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da çok miktardaki suyun çevreye üstün gelmesi ve yıkıcı hale gelebilmesi vardır."},{"boundary_match":"field_only","distinction":"Doluluk bir ortamın içeriğinin tamamlanmasını anlatır; odak ise sınır aşan ve baskınlaşan hareketli gücü anlatır.","focus_only":"Odak dalda su veya benzeri güç olağan sınırını aşıp kabarır ve bazen sürükler.","gloss":"suyla dolma","neighbor_only":"Komşu dalda temel işlem bir kabın, yatağın ya da başka bir ortamın suyla dolmasıdır.","neighbor_ref":"root_000676/B001","relation_type":"same_field","shared_zone":"Her iki dal su miktarının artması ve bulunduğu alanda belirgin hale gelmesiyle ilgilidir."}],"source_phrase_ar":"طغى السيل إذا جاء بماء كثير (maqayis;sihah)؛ طغى البحر هاجت أمواجه (maqayis;sihah)؛ طغا البحر والماء إذا علا كل شيء فاجترفه (tahdhib)؛ استعير الطغيان فيه لتجاوز الماء الحد (mufradat)","source_summary":"Kaynaklar suyun olağan ölçüyü aşarak çoğalması, kabarması veya sürükleyici biçimde yükselmesi üzerinde birleşir; aynı fiziksel taşkınlık kan, ses ve rüzgar için de aktarılır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه طغيان السيل والبحر والماء والدم إذا كثر أو هاج أو علا القدر، واستعارة الطغيان لما يجاوز حده من القوى المادية.","what_is_not_ar":"لا يدخل فيه عصيان الإنسان نفسه، ولا الطاغوت، ولا الطغية بمعنى الصفاة أو أعلى الجبل."},"support_links":[]},{"boundary":"Bu dal yalnızca sıradan bir sınır aşma niteliğini veya zalim kişi sıfatını değil, saptırıcı önder ya da yanlış tapınma odağı olan varlığı adlandırır.","branch_kind":"bare","branch_ref":"root_000936/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:TagaY`|ROOT:Tgy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:6:4:2","qac_word_ref":"96:6:4","surface_ar":"يَطْغَىٰٓ"}],"gloss":"hak sınırını aşan saptırıcı veya Tanrı dışında tapınılan varlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hak sınırını aşarak sapmayı yöneten veya insanları doğru yoldan uzaklaştıran önder ya da varlıktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Falcı, büyücü ve başkaldıran görünmez varlık, saptırıcı baş olma yönüyle bu kapsama girer."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tanrı dışında kendisine tapınılan her varlık da bu adla anılır."}}],"root_ar":"ط غ ي","root_id":"root_000936","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, hem sapmayı yöneten varlığı hem de yanlış tapınmanın yöneldiği varlığı kapsayan sözlükleşmiş ad için kullanılır.","boundary_detail":"Bu dal yalnızca sıradan bir sınır aşma niteliğini veya zalim kişi sıfatını değil, saptırıcı önder ya da yanlış tapınma odağı olan varlığı adlandırır.","branch_image_ar":"الطاغوت رأس الضلالة والطغيان","concept_gloss":"hak sınırını aşan saptırıcı veya Tanrı dışında tapınılan varlık","contextual_glosses":[{"applicability":"İnsanları doğru yoldan uzaklaştıran önder ya da güçlü varlık vurgulandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tanrı dışında tapınılan her varlığı kapsayan tapınma ölçütünü tek başına göstermez.","preserves":"Sapmayı yöneten ve başkalarını doğru yoldan uzaklaştıran önderlik yönünü korur."},"facet_ids":["F001","F002"],"text":"sapmanın başı","usage_role":"contextual"},{"applicability":"Tanrı dışında kendisine tapınılan bir varlığın işlevi öne çıkarıldığında açıklayıcı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Saptırıcı önder, falcı veya büyücü gibi tapınma dışındaki örnekleri kapsamaz.","preserves":"Yanlış tapınmanın yöneldiği varlık olma ölçütünü korur."},"facet_ids":["F003"],"text":"sahte tapınma odağı","usage_role":"contextual"}],"definition":"Hak sınırını aşan, insanları doğru yoldan saptıran bir önder ya da varlık; ayrıca Tanrı dışında kendisine tapınılan her türlü varlıktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hak sınırını aşarak sapmayı yöneten veya insanları doğru yoldan uzaklaştıran önder ya da varlıktır."},{"facet_id":"F002","role":"specialization","statement":"Falcı, büyücü ve başkaldıran görünmez varlık, saptırıcı baş olma yönüyle bu kapsama girer."},{"facet_id":"F003","role":"extension","statement":"Tanrı dışında kendisine tapınılan her varlık da bu adla anılır."}],"identity_rationale":"Kaynak ifadesi hak sınırını aşan ve insanları saptıran önderleri, büyücüyü, falcıyı ve başkaldıran görünmez varlığı; ayrıca Tanrı dışında tapınılan her varlığı aynı ad altında toplar. Geçici çerçeve bu kapsayıcı kişi ve tapınma nesnesi anlamını doğru verir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"hak sınırını aşan saptırıcı veya Tanrı dışında tapınılan varlık"}],"lexicalization_note":"Tanım, bu sözlükleşmiş adın saptırıcı ve kendisine tapılan varlık kapsamını korur; başka dallardaki sıfat ve olay anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar incelendi; tam örtüşen dal, genel sınıf ile özel ad ayrımı ve doğru yoldan sapma alanındaki tematik karşıtlık yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek, kapsam ve örnek türleri bakımından yayımlanacak bir anlam ayrımı yoktur.","focus_only":null,"gloss":"sapmanın başı","neighbor_only":null,"neighbor_ref":"root_000937/B003","relation_type":"synonym","shared_zone":"İki dal da sınırı aşan saptırıcı önderleri ve Tanrı dışında tapınılan varlıkları kapsar."},{"boundary_match":"partial","distinction":"Odak genel ve işlevsel bir sınıf adıdır; komşu ise bu sınıfa girebilecek tek bir varlığın özel adıdır.","focus_only":"Odak dal, saptırıcı önderleri ve Tanrı dışında tapınılan bütün varlık türlerini kapsayan genel bir sınıftır.","gloss":"belirli bir put adı","neighbor_only":"Komşu dal, belirli bir puta verilmiş özel addan ibarettir.","neighbor_ref":"root_000760/B003","relation_type":"near_neighbor","shared_zone":"İki dal da Tanrı dışında tapınılan bir varlıkla ilgili olabilir."},{"boundary_match":"thematic_only","distinction":"Karşıt yönleri çağrıştırsalar da biri varlık sınıfı, öteki yön gösterme sürecidir; bu nedenle doğrudan karşıt anlamlı değildirler.","focus_only":"Odak dal doğru yoldan saptıran, sınırı aşan varlığı veya yanlış tapınma odağını adlandırır.","gloss":"doğru yolu gösterme","neighbor_only":"Komşu dal doğru yolu gösterme, açıklama, ona yönelme ve bu yönelişi kabul etme sürecini anlatır.","neighbor_ref":"root_001583/B001","relation_type":"thematic","shared_zone":"İki dal da kişinin doğru yol ile ilişkisini ve yönelişini konu edinir."}],"source_phrase_ar":"الطاغوت الكاهن والشيطان وكل رأس في الضلالة (sihah)؛ كل معبود من دون الله جبت وطاغوت (tahdhib)؛ عبارة عن كل متعد وكل معبود من دون الله والساحر والكاهن والمارد من الجن (mufradat)","source_summary":"Kaynaklar, hak sınırını aşan ve sapmayı yöneten önderleri çeşitli örneklerle açıklar; kapsamı Tanrı dışında tapınılan her türlü varlığa kadar genişletir.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه الطاغوت للكاهن والشيطان وكل رأس في الضلالة وكل معبود من دون الله، ويستعمل للواحد والجمع.","what_is_not_ar":"لا يدخل فيه مجرد صفة الطاغي، ولا الطاغية بمعنى الصاعقة أو صيحة العذاب."},"support_links":[]},{"boundary":"Bu kişi adı, aynı biçimin yıldırım, yıkıcı çığlık ya da başka bir felaket anlamından ve saptırıcı varlık sınıfından ayrıdır.","branch_kind":"bare","branch_ref":"root_000936/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:TagaY`|ROOT:Tgy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:6:4:2","qac_word_ref":"96:6:4","surface_ar":"يَطْغَىٰٓ"}],"gloss":"pervasız ve ezici zorba","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnatçı, kendini büyük gören ve insanları baskıyla ezen zalim kişi ya da hükümdardır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yaptığı kötülüğü önemsemeyen ve insanları yiyip bitirircesine ezen pervasız zorba tipini belirtir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir aktarımda belirli bir ülkenin hükümdarı için kullanılan bir unvan olarak verilir."}}],"root_ar":"ط غ ي","root_id":"root_000936","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsanları baskı altında tutan, yaptığı kötülüğü umursamayan ve kendini büyük gören kişi ya da hükümdar için kullanılır.","boundary_detail":"Bu kişi adı, aynı biçimin yıldırım, yıkıcı çığlık ya da başka bir felaket anlamından ve saptırıcı varlık sınıfından ayrıdır.","branch_image_ar":"الطاغية المتجبر","concept_gloss":"pervasız ve ezici zorba","contextual_glosses":[{"applicability":"Siyasi güç sahibi zalim ve baskıcı kişi özellikle vurgulandığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hükümdar olmayan zorba kişileri ve pervasızlık ayrıntısını tek başına kapsamaz.","preserves":"İnsanları ezen zalim yönetici olma yönünü korur."},"facet_ids":["F001","F003"],"text":"zorba hükümdar","usage_role":"contextual"}],"definition":"İnsanları ezen, yaptığı kötülüğü umursamayan, inatçı, kendini büyük gören zalim hükümdar ya da zorbaya verilen addır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnatçı, kendini büyük gören ve insanları baskıyla ezen zalim kişi ya da hükümdardır."},{"facet_id":"F002","role":"specialization","statement":"Yaptığı kötülüğü önemsemeyen ve insanları yiyip bitirircesine ezen pervasız zorba tipini belirtir."},{"facet_id":"F003","role":"source_variant","statement":"Bir aktarımda belirli bir ülkenin hükümdarı için kullanılan bir unvan olarak verilir."}],"identity_rationale":"Kaynak ifadesi bu adı, inatçı ve kendini büyük gören; yaptıklarını umursamadan insanları yiyip bitirircesine ezen hükümdar veya zorba için verir. Geçici çerçeve kişi türünü ve baskıcı davranışı doğru biçimde sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"pervasız, kendini büyük gören ve insanları ezen zorba"}],"lexicalization_note":"Tanım, sözlükleşmiş kişi adını yalın dal olarak korur ve aynı biçimin felaket anlamını bu dala taşımaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; zorbanın kişi niteliğini, büyüklük taslama tutumundan ve zorla boyun eğdirme eyleminden ayıran iki karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu bir tutum ve davranış alanıdır; odak ise bu tutumu baskı ve pervasızlıkla birleştiren zorba kişiyi adlandırır.","focus_only":"Odak dal, kendini büyük görmesini insanları ezen belirli bir zalim kişi tipinde somutlaştırır.","gloss":"büyüklük taslama","neighbor_only":"Komşu dal, kişi adı olmaktan çok yeryüzünde büyüklük taslama ve başkalarına üstünlük arama tutumunu anlatır.","neighbor_ref":"root_001042/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da kendini başkalarından üstün görme ve kınanan taşkınlık vardır."},{"boundary_match":"field_only","distinction":"Odak baskıcı failin kalıcı niteliğini ve kişi türünü, komşu ise baskı kurma eylemi ile sonucunu merkez alır.","focus_only":"Odak dal, baskıyı uygulayan inatçı ve pervasız zorba kişi tipini adlandırır.","gloss":"zorla boyun eğdirme","neighbor_only":"Komşu dal, üstün gelme, zorla alma, boyun eğdirme ve başka birini baskı altına sokma işlemini anlatır.","neighbor_ref":"root_001266/B001","relation_type":"same_field","shared_zone":"İki dal da güç kullanarak başkalarını ezme ve iradelerini kırma alanındadır."}],"source_phrase_ar":"الطاغية ملك الروم (sihah)؛ الطاغية الجبار العنيد (tahdhib)؛ الذي لا يبالي ما أتى يأكل الناس ويقهرهم (tahdhib)؛ الأحمق المستكبر الظالم (tahdhib)","source_summary":"Kaynakların toplu anlatımı, sözcüğü zalim, inatçı, kendini büyük gören ve insanları pervasızca ezen bir hükümdar ya da zorba adı olarak açıklar; bir aktarım onu belirli bir hükümdarlık unvanına bağlar.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الطاغية للملك أو الجبار العنيد أو المستكبر الظالم الذي يقهر الناس ولا يتحرج.","what_is_not_ar":"لا يدخل فيه الطاغية بمعنى الصاعقة أو صيحة العذاب، ولا الطاغوت بوصفه اسما جامعا للمعبود أو رأس الضلالة."},"support_links":[]},{"boundary":"Tanım, yıldırım veya yıkıcı çığlık, insanların kendi sınır aşımı ve büyük sel yorumlarını seçenekler olarak ayırır; zorba kişi anlamını dışarıda tutar.","branch_kind":"bare","branch_ref":"root_000936/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:TagaY`|ROOT:Tgy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:6:4:2","qac_word_ref":"96:6:4","surface_ar":"يَطْغَىٰٓ"}],"gloss":"yıkıcı yıldırım ya da çığlık, sınır aşımı veya büyük sel","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yorumda yıkıcı yıldırım ya da öldürücü ceza çığlığıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir başka yorumda, yok edilen insanların kendi sınır aşımını adlaştırır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başka bir açıklama sözcüğü suyun ölçüyü aşmasıyla oluşan büyük sele bağlar."}}],"root_ar":"ط غ ي","root_id":"root_000936","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu çok parçalı karşılık, kaynakların aynı sözlükleşmiş ad için verdiği birbirinden ayrılan yorumları seçenekler halinde korur.","boundary_detail":"Tanım, yıldırım veya yıkıcı çığlık, insanların kendi sınır aşımı ve büyük sel yorumlarını seçenekler olarak ayırır; zorba kişi anlamını dışarıda tutar.","branch_image_ar":"الطاغية عقوبة غالبة","concept_gloss":"yıkıcı yıldırım ya da çığlık, sınır aşımı veya büyük sel","contextual_glosses":[{"applicability":"Sözcüğün gökten gelen yıkıcı olay olarak yorumlandığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öldürücü çığlık, insanların kendi sınır aşımı ve büyük sel yorumlarını dışarıda bırakır.","preserves":"Yıkıma yol açan göksel olay yorumunu korur."},"facet_ids":["F001"],"text":"yıkıcı yıldırım","usage_role":"contextual"},{"applicability":"Yıkımın güçlü ve öldürücü bir sesle gerçekleştiği yorumda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yıldırım, insanların kendi sınır aşımı ve büyük sel yorumlarını kapsamaz.","preserves":"Yıkıcı ve öldürücü ses yorumunu açık biçimde korur."},"facet_ids":["F001"],"text":"öldürücü çığlık","usage_role":"contextual"},{"applicability":"Sözcüğün suyun ölçüyü aşmasına bağlandığı yorumda kullanılabilecek doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yıldırım, öldürücü çığlık ve insanların kendi sınır aşımı yorumlarını dışarıda bırakır.","preserves":"Suyun sınırı aşmasıyla oluşan büyük sel yorumunu korur."},"facet_ids":["F003"],"text":"büyük sel","usage_role":"contextual"}],"definition":"Yıkıma yol açan yıldırım ya da öldürücü çığlık için kullanılan bir ad olarak açıklanır; başka yorumlarda insanların kendi sınır aşımını veya büyük seli belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yorumda yıkıcı yıldırım ya da öldürücü ceza çığlığıdır."},{"facet_id":"F002","role":"source_variant","statement":"Bir başka yorumda, yok edilen insanların kendi sınır aşımını adlaştırır."},{"facet_id":"F003","role":"source_variant","statement":"Başka bir açıklama sözcüğü suyun ölçüyü aşmasıyla oluşan büyük sele bağlar."}],"identity_rationale":"Geçici çerçevedeki baskın ceza fikri, yıldırım ve yıkıcı çığlık yorumlarını karşılar; ancak kaynak ifadesi aynı biçimi insanların kendi sınır aşımı olarak adlaştıran ve büyük sele bağlayan ayrı yorumlar da verir. Dal korunabilir, fakat tek ve birleşik bir ceza türü gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yıkıcı yıldırım ya da çığlık; sınır aşımı veya büyük sel"}],"lexicalization_note":"Tanım, sözlükleşmiş yalın adın birbirinden ayrılan yorumlarını korur; bunları genel bir ceza ya da genel başkaldırı anlamına yaymaz.","neighbor_coverage_note":"Bütün adaylar kaynak yorumları ayrı tutularak değerlendirildi; yıldırım, çığlık ve genel ceza ile kurulan üç yararlı sınır karşılaştırması yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yıldırım yalnızca odak dalın yorumlarından biridir; komşu ise göksel çarpma olayının kendi daha geniş doğa olayı sınırına sahiptir.","focus_only":"Odak dal, yıldırımın yanı sıra öldürücü çığlık, insanların kendi sınır aşımı ve büyük sel yorumlarını da içerir.","gloss":"göksel çarpma ve yıldırım","neighbor_only":"Komşu dal, gökteki şiddetli ses veya çarpma olayını, ateş, ölüm ve ceza olasılıklarıyla genel olarak anlatır.","neighbor_ref":"root_000864/B002","relation_type":"near_synonym","shared_zone":"İki dal, gökten gelen şiddetli ve yıkıcı bir olayın yıldırım olarak anlaşılabildiği alanda örtüşür."},{"boundary_match":"partial","distinction":"Odaktaki ses belirli bir yıkım yorumudur; komşu ise yıkım gerektirmeyen çeşitli ürkütücü çığlıkları da kapsar.","focus_only":"Odak dalda öldürücü çığlık yalnızca bir yorumdur; yıldırım, sınır aşımı ve büyük sel seçenekleri de vardır.","gloss":"ürkütücü çığlık","neighbor_only":"Komşu dal saldırı, ağıt, ani kötülük ve korku gibi bağlamlardaki ürkütücü çığlıkları da kapsar.","neighbor_ref":"root_000895/B002","relation_type":"near_synonym","shared_zone":"İki dal, güçlü bir çığlığın korku veya yıkımla ilişkilendirildiği kullanımda örtüşür."},{"boundary_match":"partial","distinction":"Komşu genel ceza kavramıdır; odak ise yalnızca bazı yorumlarda ceza sayılan, başka yorumlarda eylem veya sel olan özel bir addır.","focus_only":"Odak dal, belirli bir sözlükleşmiş adın yıldırım, çığlık, sınır aşımı ve büyük sel biçimindeki yorumlarını taşır.","gloss":"acı veren ceza","neighbor_only":"Komşu dal, acı verme ve karşılık olarak uygulanan her türlü cezayı genel bir kavram halinde kapsar.","neighbor_ref":"root_000994/B005","relation_type":"near_neighbor","shared_zone":"Yıldırım veya öldürücü çığlık yorumu, yıkıcı bir ceza olarak anlaşılabildiğinde iki alan kesişir."}],"source_phrase_ar":"الطاغية الصاعقة ويعني صيحة العذاب (sihah)؛ طغت الصيحة على ثمود (tahdhib)؛ أهلكوا بالطاغية أي بطغيانهم مصدر على فاعلة (tahdhib)؛ إشارة إلى الطوفان المعبر عنه بإنا لما طغى الماء (mufradat)","source_summary":"Toplu kaynak kaydı tek bir açıklamada birleşmez: sözcük yıkıcı yıldırım veya öldürücü çığlık, yok edilenlerin kendi sınır aşımı ya da suyun ölçüyü aşmasıyla oluşan büyük sel olarak yorumlanır.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه إطلاق الطاغية على الصاعقة أو صيحة العذاب أو العقوبة الغالبة المتصلة بطغيان أو بطوفان.","what_is_not_ar":"لا يدخل فيه الطاغية بمعنى الجبار العنيد، ولا الطاغوت، ولا مطلق الطغيان المعنوي."},"support_links":[]},{"boundary":"Bu dal, aynı biçimin küçük parça anlamını ve kökün sınır aşma anlamlarını kapsamaz.","branch_kind":"bare","branch_ref":"root_000936/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:TagaY`|ROOT:Tgy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:6:4:2","qac_word_ref":"96:6:4","surface_ar":"يَطْغَىٰٓ"}],"gloss":"düz ve pürüzsüz kaya, dağ doruğu ya da yüksek yer","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Düz ve pürüzsüz kaya anlamına gelir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı biçim bir aktarımda dağın en yüksek yeri anlamındadır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İlgili başka biçim, genel olarak yüksek bir yeri adlandırır."}}],"root_ar":"ط غ ي","root_id":"root_000936","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Karşılık, iki sözlük biçiminin kaya niteliğini ve yükseltiye dayalı yer anlamlarını seçenekler halinde birlikte gösterir.","boundary_detail":"Bu dal, aynı biçimin küçük parça anlamını ve kökün sınır aşma anlamlarını kapsamaz.","branch_image_ar":"الطغية الصفاة أو الموضع المرتفع","concept_gloss":"düz ve pürüzsüz kaya, dağ doruğu ya da yüksek yer","contextual_glosses":[{"applicability":"Taşın düz ve pürüzsüz yüzeyi öne çıktığında kullanılabilecek açıklayıcı karşılıktır.","error_profile":{"adds":"Yalçın sözü, kaynakta zorunlu olmayan diklik ve aşılması güçlük çağrışımı ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Düz ve pürüzsüz kaya olma niteliğini korur."},"facet_ids":["F001"],"text":"yalçın düz kaya","usage_role":"contextual"},{"applicability":"Dağın en yüksek bölümünü gösteren aktarım söz konusu olduğunda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Pürüzsüz kaya ve dağla sınırlı olmayan yüksek yer anlamlarını kapsamaz.","preserves":"Dağın en yüksek yeri olma yorumunu korur."},"facet_ids":["F002"],"text":"dağ doruğu","usage_role":"contextual"}],"definition":"Düz ve pürüzsüz bir kaya ya da dağın en yüksek yeri; ilgili başka bir biçimde ise herhangi bir yüksek yerdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Düz ve pürüzsüz kaya anlamına gelir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı biçim bir aktarımda dağın en yüksek yeri anlamındadır."},{"facet_id":"F003","role":"extension","statement":"İlgili başka biçim, genel olarak yüksek bir yeri adlandırır."}],"identity_rationale":"Kaynak ifadesi bir biçim için düz ve pürüzsüz kaya ile dağ doruğunu, ikinci biçim için de her yüksek yeri verir. Geçici çerçeve taşın niteliğini ve yükselti kapsamını birbirinden ayırarak doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"düz ve pürüzsüz kaya ya da dağ doruğu"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yüksek yer"}],"lexicalization_note":"Tanım, iki yalın sözlük biçiminin düz kaya, dağ doruğu ve yüksek yer anlamlarını korur; eylem dallarına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eş dal ile pürüzsüz kaya anlamında örtüşen fakat maddi nitelikleri farklı komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek ve kapsam sınırları tam örtüştüğü için yayımlanacak bir anlam ayrımı yoktur.","focus_only":null,"gloss":"pürüzsüz kaya ve yüksek yer","neighbor_only":null,"neighbor_ref":"root_000937/B005","relation_type":"synonym","shared_zone":"İki dal da düz ve pürüzsüz kaya, dağın en yüksek yeri ve genel yüksek yer anlamlarını kapsar."},{"boundary_match":"partial","distinction":"Odak yükselti anlamlarına da açılır; komşu ise kayanın maddi yüzey ve temizlik özelliklerini daha sıkı tanımlar.","focus_only":"Odak dal, pürüzsüz kayanın yanı sıra dağ doruğu ve genel yüksek yer anlamlarını da taşır.","gloss":"düz ve temiz kaya","neighbor_only":"Komşu dal, kayanın geniş, sert ve toprak ile çamurdan arınmış olmasını daha ayrıntılı biçimde belirtir.","neighbor_ref":"root_000873/B006","relation_type":"near_synonym","shared_zone":"İki dal düz, sert ve pürüzsüz bir kaya parçasını adlandırma alanında örtüşür."}],"source_phrase_ar":"الطغية الصفاة الملساء (maqayis;tahdhib)؛ الطغية أعلى الجبل وكل مكان مرتفع طغوة (sihah)","source_summary":"Kaynak kaydı düz ve pürüzsüz kaya anlamını paylaşır; ayrıca dağın en yüksek yeri yorumunu ve ilgili biçimin herhangi bir yüksek yere verilen ad olduğunu korur.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه الطغية للصفاة الملساء أو أعلى الجبل، والطغوة للمكان المرتفع.","what_is_not_ar":"لا يدخل فيه الطغيان بمعنى مجاوزة الحد، ولا الطغية بمعنى النبذة، ولا الطغيا للبقرة."},"support_links":[]},{"boundary":"Bu dal belirli bir kesri, büyük bir bölümü, kaya veya yüksek yer anlamını ya da sınır aşma eylemini kapsamaz.","branch_kind":"bare","branch_ref":"root_000936/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:TagaY`|ROOT:Tgy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:6:4:2","qac_word_ref":"96:6:4","surface_ar":"يَطْغَىٰٓ"}],"gloss":"bir şeyden küçük parça","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bütünün türü belirtilmeksizin, ondan küçük bir parça veya az bir miktar anlatılır."}}],"root_ar":"ط غ ي","root_id":"root_000936","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bütünün türü belirtilmeden ondan ayrılan veya geriye kalan küçük parçayı anlatan genel karşılıktır.","boundary_detail":"Bu dal belirli bir kesri, büyük bir bölümü, kaya veya yüksek yer anlamını ya da sınır aşma eylemini kapsamaz.","branch_image_ar":"الطغية نبذة من الشيء","concept_gloss":"bir şeyden küçük parça","contextual_glosses":[{"applicability":"Maddenin veya bütünün türünün önemli olmadığı gündelik bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bütünden küçük ve belirsiz miktarda bir parça olma anlamını korur."},"facet_ids":["F001"],"text":"ufak bir parça","usage_role":"general"}],"definition":"Herhangi bir şeyden ayrılmış, alınmış ya da kalmış küçük bir parçadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bütünün türü belirtilmeksizin, ondan küçük bir parça veya az bir miktar anlatılır."}],"identity_rationale":"Kaynak ifadesi, herhangi bir şeyden alınan ya da kalan küçük bir parçayı tek ve açık anlam olarak verir. Geçici çerçeve bu nicelik ve parça sınırını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"herhangi bir şeyden küçük parça"}],"lexicalization_note":"Tanım, yalın sözlük biçiminin herhangi bir şeyden küçük parça anlamıyla sınırlıdır ve başka biçimlerin anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel küçük parça anlamını belirli maddelerdeki az miktardan ve kesilmiş parçadan ayıran iki karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak bütünü tümüyle açık bırakır; komşu ise azlığı belirli madde ve parça türleri üzerinden sözlükleştirir.","focus_only":"Odak dal, herhangi bir şeyden alınan küçük parçayı hiçbir madde türüyle sınırlamaz.","gloss":"az miktar","neighbor_only":"Komşu dal, mal, ot, yağmur ve yaş ürün gibi belirli maddelerin az miktarlarını ve bazı özel parçaları sayar.","neighbor_ref":"root_001466/B005","relation_type":"near_synonym","shared_zone":"İki dal da bir bütüne göre küçük kalan parça veya miktarı anlatır."},{"boundary_match":"partial","distinction":"Odakta küçüklük ve belirsiz bütün esastır; komşuda kesilip ayrılma ilişkisi öne çıkar.","focus_only":"Odak dal, parçanın küçük olmasını ve herhangi bir bütünden gelebilmesini öne çıkarır.","gloss":"kesilmiş parça","neighbor_only":"Komşu dal, meyve gibi bir nesneden kesilip ayrılmış parçayı anlatır; küçüklük zorunlu değildir.","neighbor_ref":"root_000786/B002","relation_type":"near_synonym","shared_zone":"Her iki dal bir bütünden ayrılmış parçayı adlandırabilir."}],"source_phrase_ar":"الطغية من كل شيء نبذة منه (sihah)","source_summary":"Tek kaynaklı kayıt, sözcüğü herhangi bir şeyden küçük bir parça ya da az miktar olarak açıklar ve ek bir kapsam koşulu vermez.","sources":["SI"],"what_is_ar":"يدخل فيه الطغية من كل شيء بمعنى نبذة منه.","what_is_not_ar":"لا يدخل فيه الصفاة الملساء أو المكان المرتفع، ولا الطغيان، ولا الطغيا للبقرة."},"support_links":[]},{"boundary":"Bu dal genel ses kavramı değildir; yalnızca belirtilen kişi veya topluluk kalıbındaki ağız kullanımını kapsar.","branch_kind":"collocation","branch_ref":"root_000936/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:TagaY`|ROOT:Tgy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:6:4:2","qac_word_ref":"96:6:4","surface_ar":"يَطْغَىٰٓ"}],"gloss":"bir kimsenin ya da topluluğun sesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kalıp, adı geçen kişinin veya topluluğun işitilen sesini belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kullanım genel dil değil, kaynakta özellikle belirtilen bir ağızla sınırlıdır."}}],"root_ar":"ط غ ي","root_id":"root_000936","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık yalnızca kaynakta belirtilen ağızda kişi veya toplulukla kurulan özel kalıp için geçerlidir.","boundary_detail":"Bu dal genel ses kavramı değildir; yalnızca belirtilen kişi veya topluluk kalıbındaki ağız kullanımını kapsar.","branch_image_ar":"طغي القوم صوتهم","concept_gloss":"bir kimsenin ya da topluluğun sesi","contextual_glosses":[{"applicability":"Kalıpta tek kişi yerine bir topluluğun çıkardığı veya ondan işitilen ses söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek bir kişinin sesini anlatan kullanım ile ağız kaydını tek başına göstermez.","preserves":"Sesin adı geçen topluluğa ait olması ilişkisini korur."},"facet_ids":["F001"],"text":"topluluğun sesi","usage_role":"contextual"}],"definition":"Belirli bir ağızda, bir kişi ya da toplulukla kurulan kalıp içinde o kişi veya topluluktan işitilen ses demektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kalıp, adı geçen kişinin veya topluluğun işitilen sesini belirtir."},{"facet_id":"F002","role":"specialization","statement":"Kullanım genel dil değil, kaynakta özellikle belirtilen bir ağızla sınırlıdır."}],"identity_rationale":"Kaynak ifadesi belirli bir ağız kullanımında, bir kişi ya da toplulukla kurulan kalıbın o kişi veya topluluğun sesi anlamına geldiğini açıkça bildirir. Geçici çerçeve hem anlamı hem de ağız kaydını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bir kimsenin ya da topluluğun sesi"}],"lexicalization_note":"Tanım, bir kişi ya da topluluğun sesi anlamındaki belirtilmiş ağız kalıbına bağlıdır ve yalın köke genel ses anlamı yüklemez.","neighbor_coverage_note":"Bütün adaylar kalıp ve ağız sınırı gözetilerek değerlendirildi; doğrudan ses adı, genel ses kavramı ve karışık topluluk gürültüsüyle üç ayrım yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Anlamsal çekirdek yakın olsa da odak dalın kişi veya toplulukla kurulan kalıp ve ağız sınırı komşuda yoktur.","focus_only":"Odak dal, sesi kişi ya da toplulukla kurulan belirli bir ağız kalıbı içinde anlatır.","gloss":"ses","neighbor_only":"Komşu dal, başka bir sözlük biçimini doğrudan ses adı olarak verir ve kişi ya da topluluk kalıbı şartı koymaz.","neighbor_ref":"root_000450/B007","relation_type":"near_synonym","shared_zone":"İki dalın çekirdeği de işitilen sesi adlandırmaktır."},{"boundary_match":"partial","distinction":"Komşu genel ses alanıdır; odak ise sahibi belirtilmiş ses için kalıba ve ağız kullanımına bağlı dar bir adlandırmadır.","focus_only":"Odak dal, belirli bir kişi ya da topluluğa ait sesi özel bir ağız kalıbında adlandırır.","gloss":"işitilen ses","neighbor_only":"Komşu dal, kulağa ulaşan her türlü sesi; bağırma, ezgi, gürültü ve yardım çağrısı gibi türleriyle kapsar.","neighbor_ref":"root_000890/B001","relation_type":"near_synonym","shared_zone":"Her iki dal insan veya topluluktan işitilebilen sesi kapsayabilir."},{"boundary_match":"partial","distinction":"Odakta sesin topluluğa ait olması yeterlidir; komşuda çoklu seslerin yükselmesi ve birbirine karışması belirleyicidir.","focus_only":"Odak dal, kişi veya topluluğun sesini yüksek, karışık ya da gürültülü olma şartı olmadan belirtir.","gloss":"karışık topluluk gürültüsü","neighbor_only":"Komşu dal, topluluk seslerinin yükselip karışmasını, gürültüyü ve uğultuyu özellikle içerir.","neighbor_ref":"root_001344/B005","relation_type":"near_neighbor","shared_zone":"İki dal da bir topluluktan çıkan ses için kullanılabilir."}],"source_phrase_ar":"سمعت طغي فلان أي صوته هذلية؛ سمعت طغي القوم وطهيهم ووغيهم أي صوتهم (tahdhib)","source_summary":"Tek kaynaklı kayıt, belirtilen ağızda kişi veya toplulukla kurulan kalıbı onların işitilen sesi olarak açıklar ve benzer ses adlarıyla birlikte aktarır.","sources":["TA"],"what_is_ar":"يدخل فيه طغي فلان أو طغي القوم بمعنى الصوت في النقل الهذلي.","what_is_not_ar":"لا يدخل فيه الطغيان، ولا طغيان الماء، ولا أسماء الطاغوت والطاغية."},"support_links":[]},{"boundary":"Ana anlam yabani sığır yavrusudur; böğüren inek aktarımı ayrı tutulur ve dal evcil sığır yavrusuna ya da genel sığır adına genişletilmez.","branch_kind":"bare","branch_ref":"root_000936/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:TagaY`|ROOT:Tgy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:6:4:2","qac_word_ref":"96:6:4","surface_ar":"يَطْغَىٰٓ"}],"gloss":"yabani sığır yavrusu; bir aktarımda böğüren inek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yabani sığırın küçük yavrusunu adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başka bir aktarım, sözcüğü böğüren bir inek için de verir."}}],"root_ar":"ط غ ي","root_id":"root_000936","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık ana hayvan adı anlamını öne alır ve kaynaklardaki farklı böğüren inek aktarımını ayrı bir seçenek olarak saklar.","boundary_detail":"Ana anlam yabani sığır yavrusudur; böğüren inek aktarımı ayrı tutulur ve dal evcil sığır yavrusuna ya da genel sığır adına genişletilmez.","branch_image_ar":"الطغيا الصغير من بقر الوحش","concept_gloss":"yabani sığır yavrusu; bir aktarımda böğüren inek","contextual_glosses":[{"applicability":"Hayvanın türü ve küçük yaşı açıkça kastedildiğinde ana ve en doğrudan karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Böğüren inek biçimindeki ayrı ve daha az belirli aktarımı kapsamaz.","preserves":"Yabani sığırın küçük yavrusu olma ana anlamını eksiksiz korur."},"facet_ids":["F001"],"text":"yabani sığır yavrusu","usage_role":"general"},{"applicability":"Kaynağın yaş ve yabanilik belirtmeden böğürme özelliğiyle verdiği ayrı aktarımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yabani sığırın küçük yavrusu olma ana anlamını kapsamaz.","preserves":"İneğin böğürmesiyle tanımlanan ayrı kaynak aktarımını korur."},"facet_ids":["F002"],"text":"böğüren inek","usage_role":"contextual"}],"definition":"Başlıca aktarımda yabani sığır yavrusuna verilen addır; başka bir aktarımda böğüren bir inek için de kullanıldığı bildirilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yabani sığırın küçük yavrusunu adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Başka bir aktarım, sözcüğü böğüren bir inek için de verir."}],"identity_rationale":"Bir kaynak ifadesi sözcüğü açıkça yabani sığır yavrusu olarak verir; diğer aktarım ise böğüren bir inekle birlikte anarak yaş ve yabanilik sınırını belirsizleştirir. Geçici çerçeve ana aktarımı korur, ancak ikinci aktarım ayrı bir kaynak değişkesi olarak belirtilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yabani sığır yavrusu; bir aktarımda böğüren inek"}],"lexicalization_note":"Tanım, yalın hayvan adının yabani sığır yavrusu anlamını ve ayrı böğüren inek aktarımını korur; başka hayvan adlarına genellenmez.","neighbor_coverage_note":"Bütün adaylar tür, yaş ve evcillik sınırları bakımından değerlendirildi; yabani sığır yavrusuyla örtüşen çok anlamlı ad ve evcil sığır yavrusu karşılaştırıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak bu hayvanı ana anlam yapar; komşu ise onu çeşitli hafif ya da genç hayvanlardan biri olarak daha geniş bir ad altında kapsar.","focus_only":"Odak dalın ana anlamı özellikle yabani sığır yavrusudur ve ayrıca böğüren inek aktarımı vardır.","gloss":"yabani sığır yavrusu ve benzer hayvanlar","neighbor_only":"Komşu dal yavru geyik, yaban keçisi ve hafif eşek gibi başka hayvanlara da uzanan çok anlamlı bir hayvan adıdır.","neighbor_ref":"root_001030/B004","relation_type":"near_synonym","shared_zone":"İki dal da yabani sığır yavrusunu adlandırabilir."},{"boundary_match":"partial","distinction":"Odakta yabanilik belirleyicidir; komşu evcil sığır yavrusuyla sınırlıdır ve böğüren yetişkin inek aktarımını taşımaz.","focus_only":"Odak dal yabani sığır yavrusunu ve ayrı bir böğüren inek aktarımını içerir.","gloss":"evcil sığır yavrusu","neighbor_only":"Komşu dal evcil sığırın yavrusunu ve onun dişi biçimini adlandırır.","neighbor_ref":"root_000987/B002","relation_type":"near_synonym","shared_zone":"Her iki dal sığır türünden bir hayvanın yavrusunu adlandırır."}],"source_phrase_ar":"طغيا وهو الصغير من بقر الوحش (sihah)؛ يقال للبقرة الخائرة والطغيا (tahdhib)","source_summary":"Toplu kaynak kaydı, ana anlamı yabani sığırın küçük yavrusu olarak verir; ayrıca yaş ve yabanilik sınırını aynı açıklıkla taşımayan böğüren inek aktarımını korur.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الطغيا اسما للصغير من بقر الوحش.","what_is_not_ar":"لا يدخل فيه الطغية للصفاة أو النبذة، ولا الطغيان، ولا الطاغوت."},"support_links":[]},{"boundary":"Dalın çekirdeği sınır veya ölçü aşımıdır; suyun taşması, sapmanın önderi ve pürüzsüz kaya anlamları bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000937/B001","candidate_links":[{"candidate_id":"cand_12218dcac34d2427ea99","lane":"micro"},{"candidate_id":"cand_5f5146d03da9767b76e8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طَغَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:TagaY`|ROOT:Tgy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:6:4:2","qac_word_ref":"96:6:4","surface_ar":"يَطْغَىٰٓ"}],"gloss":"itaatsizlikte veya ölçüde sınırı aşma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığın kendisi için geçerli sınırı veya uygun ölçüyü aşması çekirdek anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsan davranışında bu aşım, özellikle itaatsizlik ve başkaldırı içinde sınır tanımama biçiminde gerçekleşir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen kullanım, bir kimseyi sınır aşan ve taşkın davranışa sürükleme sonucunu bildirir."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kişi adı olarak türemiş kullanım, yaptığını umursamayan, insanları ezen, inatçı ve kibirli zorbayı niteler."}}],"root_ar":"ط غ ي","root_id":"root_000937","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çekirdek eylemi hem insanın itaatsizliği hem de herhangi bir şeyin kendi ölçüsünü aşması için karşılar.","boundary_detail":"Dalın çekirdeği sınır veya ölçü aşımıdır; suyun taşması, sapmanın önderi ve pürüzsüz kaya anlamları bu dala girmez.","branch_image_ar":"مجاوزة الحد في العصيان","concept_gloss":"itaatsizlikte veya ölçüde sınırı aşma","contextual_glosses":[{"applicability":"Bir kişinin itaatsizlik ve başkaldırı içinde kabul edilen sınırı aşmasını anlatan cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsan dışındaki şeylerin kendi ölçüsünü aşabilmesi kapsamını dışarıda bırakır.","preserves":"İnsan davranışındaki itaatsiz sınır aşımını doğal biçimde korur."},"facet_ids":["F001","F002"],"text":"azıp sınırı aştı","usage_role":"contextual"},{"applicability":"Bir etkenin başka bir kişiyi sınır tanımaz davranışa yönelttiği ettirgen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalın biçimde öznenin kendi sınırını aşması ve zorba kişi kullanımı bu karşılıkta yer almaz.","preserves":"Başka bir katılımcıyı aşırılığa sürükleyen ettirgen ilişkiyi korur."},"facet_ids":["F003"],"text":"onu azdırıp sınır aşmaya sürükledi","usage_role":"contextual"},{"applicability":"İnsanları ezen, yaptığı kötülüğü umursamayan inatçı ve kibirli kişiyi niteleyen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eylem olarak sınırı aşma ve başkasını bu eyleme sürükleme anlamlarını dışarıda bırakır.","preserves":"Kişiye yüklenen zorbalık, inat ve sınır tanımazlık özelliklerini korur."},"facet_ids":["F004"],"text":"sınır tanımaz zorba","usage_role":"contextual"}],"definition":"Bir kimsenin itaatsizlikte ya da herhangi bir şeyin kendi ölçüsünde belirlenmiş sınırı aşmasıdır. Türemiş kullanımlar, birini böyle bir aşırılığa sürüklemeyi ve sınır tanımayan inatçı zorba kişiyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığın kendisi için geçerli sınırı veya uygun ölçüyü aşması çekirdek anlamdır."},{"facet_id":"F002","role":"specialization","statement":"İnsan davranışında bu aşım, özellikle itaatsizlik ve başkaldırı içinde sınır tanımama biçiminde gerçekleşir."},{"facet_id":"F003","role":"extension","statement":"Ettirgen kullanım, bir kimseyi sınır aşan ve taşkın davranışa sürükleme sonucunu bildirir."},{"facet_id":"F004","role":"specialization","statement":"Kişi adı olarak türemiş kullanım, yaptığını umursamayan, insanları ezen, inatçı ve kibirli zorbayı niteler."}],"identity_rationale":"Kaynak ifadesi, çekirdeği itaatsizlikte sınırı aşma olarak verirken ölçüsünü aşan her şeyi de kapsar; ayrıca başkasını bu duruma sürükleyen ettirgen kullanımı ve sınır tanımaz zorba kişiyi bildiren türemiş kullanımı belirtir. Bu nedenle dal korunabilir, ancak yalnızca insanın itaatsizliğiyle sınırlandırılmamalı ve türemiş kullanımlar çekirdek eylemle özdeşleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"sınırı veya ölçüyü aşmak, azmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"itaatsizlikte sınırı aşan, azgın"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"itaatsizlikte sınır tanımazlık ve azgınlık"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sınırı aşma ve azgınlık"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"sınırı aşma durumu, azgınlık"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"onu azdırdı veya sınır aşmaya sürükledi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"inatçı, kibirli ve sınır tanımaz zorba"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"Roma hükümdarına verilen unvan"}],"lexicalization_note":"Tanım yalın sınır aşma çekirdeğini, birini sınır aşmaya sürükleyen ettirgen kullanımdan ve zorba kişiyi bildiren türemiş kullanımdan ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı kapsamlı dal ile sınır aşımı, nimet karşısında şımarma ve maddi taşkınlık arasındaki en yararlı dört karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kartlarda çekirdek, kapsam ve türemiş kullanımlar bakımından anlamlı bir sınır farkı görünmez.","focus_only":null,"gloss":"sınırı aşma ve azgınlık","neighbor_only":null,"neighbor_ref":"root_000936/B001","relation_type":"synonym","shared_zone":"Her iki dal da sınırın veya ölçünün aşılmasını, itaatsizliği ve birini bu duruma sürükleyen kullanımı kapsar."},{"boundary_match":"partial","distinction":"Odak dal itaatsizlik ve azgınlık ekseninde kişisel ve ettirgen türevler kurar; komşu dal ise amaçsız veya haksız kullanım ve savurganlık alanlarına uzanır.","focus_only":"İtaatsizlikte azgınlaşmayı, birini azdırmayı ve sınır tanımaz zorba kişiyi de kapsar.","gloss":"ölçüsüzce sınırı aşma","neighbor_only":"Harcama, öldürme, yeme ve su kullanımı gibi alanlarda bir şeyi hak veya yarar dışında kullanmayı özellikle kapsar.","neighbor_ref":"root_000699/B001","relation_type":"near_synonym","shared_zone":"İki dalın ortak alanı, geçerli sınırı veya uygun ölçüyü aşan davranıştır."},{"boundary_match":"partial","distinction":"Komşu dalın ayırt edici koşulu nimet karşısındaki şımarma ve coşkudur; odak dal için böyle bir neden veya duygu gerekli değildir.","focus_only":"Nimet veya sevinç koşulu olmadan genel sınır aşımını ve itaatsizliği kapsar.","gloss":"şımararak ölçüyü aşma","neighbor_only":"Özellikle nimet karşısındaki aşırı sevinç, şımarıklık ve nimeti küçümseme durumunu kapsar.","neighbor_ref":"root_000125/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişinin davranışta ölçüyü aşarak taşkınlaşmasını içerebilir."},{"boundary_match":"partial","distinction":"Odak dal davranışsal ve ahlaki sınır aşımıdır; komşu dal yalnızca belirli maddi güçlerle kurulan söz öbeklerinde kabarma ve bastırma olayını anlatır.","focus_only":"İtaatsizlikte davranış sınırını aşmayı ve bundan türeyen zorba kişi anlamını taşır.","gloss":"sınırı aşan taşkınlık","neighbor_only":"Su, sel, deniz, kan, ses veya rüzgarın miktar ya da güç bakımından kabarıp bastırmasını bildirir.","neighbor_ref":"root_000937/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da olağan sınırın veya ölçünün aşılması ortak bir kavramsal zemin oluşturur."}],"source_phrase_ar":"مجاوزة الحد في العصيان (maqayis;mufradat); جاوز الحد وكل مجاوز حده في العصيان (sihah); كل شيء جاوز القدر فقد طغا (tahdhib); أطغاه المال أي جعله طاغيا (sihah); الطاغية الجبار العنيد (tahdhib)","source_summary":"Kaynakların birleşen anlatımı, temel anlamı sınırın veya belirlenmiş ölçünün aşılması olarak kurar ve insan davranışında itaatsizliği öne çıkarır. Aynı kanıt, başkasını bu duruma sürükleme ile sınır tanımaz zorba kişiyi bildiren türemiş kullanımları da içerir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه طغى وطاغ والطغيان والطغوان والطغوى وأطغاه إذا حمله على الطغيان والطاغية بمعنى الجبار","what_is_not_ar":"ليس فيضان الماء ولا الطاغوت ولا الصخرة الملساء"},"support_links":["sup_4edd506a257f99282c67","sup_5588a2cd2cacf5478919"]},{"boundary":"Bu dal yalın bir kök anlamı değil, su, sel, deniz, kan, ses veya rüzgar öznesiyle kurulan taşma ve bastırma kullanımlarıdır.","branch_kind":"collocation","branch_ref":"root_000937/B002","candidate_links":[{"candidate_id":"cand_10bd6da7b159be6c96e3","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طَغَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:TagaY`|ROOT:Tgy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:6:4:2","qac_word_ref":"96:6:4","surface_ar":"يَطْغَىٰٓ"}],"gloss":"ölçüyü aşarak kabarıp bastırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Su veya sel, olağan miktarı ve düzeyi aşacak ölçüde çoğalır ve yükselir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Deniz kullanımında dalgaların şiddetle kabarıp yükselmesi ve önündekileri sürüklemesi öne çıkar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kan kullanımında sıvının coşması ve basınçla kabarması anlatılır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Ses veya rüzgar kullanımında olağan ölçüyü aşan kuvvetin üstün gelip bastırması anlatılır."}}],"root_ar":"ط غ ي","root_id":"root_000937","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kanıtlanan su, sel, deniz, kan, ses ve rüzgar söz öbeklerinin ortak taşma ve baskın gelme yapısını karşılar.","boundary_detail":"Bu dal yalın bir kök anlamı değil, su, sel, deniz, kan, ses veya rüzgar öznesiyle kurulan taşma ve bastırma kullanımlarıdır.","branch_image_ar":"علو الماء والقوة الجارفة","concept_gloss":"ölçüyü aşarak kabarıp bastırma","contextual_glosses":[{"applicability":"Selin olağan miktardan çok su taşıyarak yükseldiği bağlamlarda doğal bir cümle karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Deniz, kan, ses ve rüzgarla kurulan diğer söz öbeği kullanımlarını kapsamaz.","preserves":"Sel suyunun çokluğunu, yükselmesini ve taşmasını korur."},"facet_ids":["F001"],"text":"sel bol suyla kabarıp taştı","usage_role":"contextual"},{"applicability":"Deniz dalgalarının yükseldiği ve kuvvetle sürüklediği olay bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sel, su, kan, ses ve rüzgarla kurulan diğer kullanımlar bu karşılıkta yer almaz.","preserves":"Denizin dalga kabarmasını, yükselmesini ve sürükleyici gücünü korur."},"facet_ids":["F002"],"text":"deniz coşup önündekileri sürükledi","usage_role":"contextual"},{"applicability":"Kanın basınçla kabardığını ve şiddetle hareketlendiğini anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Su, sel, deniz, ses ve rüzgarla kurulan kullanımları dışarıda bırakır.","preserves":"Kanla sınırlı coşma ve kabarma görünümünü korur."},"facet_ids":["F003"],"text":"kan kabarıp coştu","usage_role":"contextual"},{"applicability":"Sesin veya rüzgarın olağan ölçüyü aşan bir güçle her şeye üstün geldiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sıvıların çoğalma, kabarma ve sürükleme görünümlerini kapsamaz.","preserves":"Ses ve rüzgarın ölçüyü aşan baskın kuvvetini korur."},"facet_ids":["F004"],"text":"çığlık ya da rüzgar baskın geldi","usage_role":"contextual"}],"definition":"Su, sel, deniz veya kanın olağan miktarını ya da düzeyini aşarak kabarması, coşması ve kimi bağlamlarda önündekileri sürüklemesidir. Ses ve rüzgarla kurulan kullanımlarda, ölçüyü aşan gücün baskın gelmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Su veya sel, olağan miktarı ve düzeyi aşacak ölçüde çoğalır ve yükselir."},{"facet_id":"F002","role":"specialization","statement":"Deniz kullanımında dalgaların şiddetle kabarıp yükselmesi ve önündekileri sürüklemesi öne çıkar."},{"facet_id":"F003","role":"specialization","statement":"Kan kullanımında sıvının coşması ve basınçla kabarması anlatılır."},{"facet_id":"F004","role":"extension","statement":"Ses veya rüzgar kullanımında olağan ölçüyü aşan kuvvetin üstün gelip bastırması anlatılır."}],"identity_rationale":"Kaynak ifadesi, selin bol suyla gelmesini, suyun belirlenmiş miktarı aşmasını, deniz dalgalarının kabarmasını, kanın coşmasını ve su ya da denizin yükselip önündekileri sürüklemesini açıkça bir arada verir. Ses ve rüzgarın ölçüyü aşan güçle bastırması da aynı maddi kuvvet uzantısı içinde desteklenir.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"sel bol suyla geldi ve kabardı"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"su olağan düzeyi aşıp yükseldi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"denizin dalgaları kabarıp yükseldi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kan kabarıp coştu"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"çığlık ya da rüzgar ölçüyü aşan güçle baskın geldi"}],"lexicalization_note":"Tanım yalnızca kanıtlanan söz öbeklerine bağlıdır; kabarma ve bastırma anlamı yalın biçime genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eşleşen dal ile itici sel gücü, deniz dalgası ve doğa olaylarının şiddetlenmesi arasındaki dört sınır karşılaştırması yeterli bulundu.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kartlarda çekirdek, katılımcılar ve maddi kuvvet uzantısı bakımından anlamlı bir sınır farkı görünmez.","focus_only":null,"gloss":"maddi gücün ölçüyü aşması","neighbor_only":null,"neighbor_ref":"root_000936/B002","relation_type":"synonym","shared_zone":"Her iki dal su, sel, deniz ve kanın olağan miktarı aşarak kabarmasını ve benzer maddi güç uzantılarını kapsar."},{"boundary_match":"partial","distinction":"Odak dalda temel sınır olağan miktar veya gücün aşılmasıdır; komşu dalda ise ögelerin birbirini iterek ilerlemesi ve kalabalık hareketi belirleyicidir.","focus_only":"Suyun düzeyi aşmasını, deniz dalgalarının kabarmasını, kanın coşmasını ve ses ya da rüzgarın bastırmasını kapsar.","gloss":"itici taşkın güç","neighbor_only":"Büyük sel ve dalga yanında insanların, yürüyüşün veya koşan atın birbirini iten yoğun hareketini de kapsar.","neighbor_ref":"root_000480/B005","relation_type":"near_synonym","shared_zone":"Büyük selin veya dalganın yoğun ve itici hareketi iki dalın ortak alanıdır."},{"boundary_match":"field_only","distinction":"Komşu dal su biçiminin adı ve betimidir; odak dal ise yalnız belirli söz öbeklerinde dalganın olağan ölçüyü aşarak coşmasını bildirir.","focus_only":"Denizin dışında sel, su, kan, ses ve rüzgarı da kapsar; olağan ölçüyü aşan güç belirleyicidir.","gloss":"deniz dalgası","neighbor_only":"Deniz dalgasını veya rüzgarın su yüzeyinde kaldırdığı tabakaları, ölçü aşımı şartı olmadan adlandırır.","neighbor_ref":"root_000023/B003","relation_type":"same_field","shared_zone":"İki dal da deniz yüzeyinde yükselen ve hareketlenen suyu anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal sınırı aşan kabarma ve baskın gelmeye bağlı söz öbekleridir; komşu dal daha genel biçimde hava olaylarının ve sıcaklık koşullarının şiddetlenmesini anlatır.","focus_only":"Sıvının miktar ve düzey aşımını, ayrıca sesin baskın gelmesini içerir.","gloss":"şiddetlenip coşma","neighbor_only":"Yağmurun düşüşü ile sıcak, soğuk ve rüzgarın şiddetlenmesini ölçü aşımı veya sürükleme şartı olmadan anlatır.","neighbor_ref":"root_000810/B005","relation_type":"near_neighbor","shared_zone":"Rüzgarın kuvvetlenmesi ve doğa olaylarının olağanın üstünde şiddet kazanması ortak alandır."}],"source_phrase_ar":"طغى السيل إذا جاء بماء كثير (maqayis;sihah); طغى الماء خروجه عن المقدار (maqayis); طغى البحر هاجت أمواجه (maqayis;sihah); طغى الدم تبيغ (maqayis;sihah); طغا البحر والماء إذا علا كل شيء فاجترفه (tahdhib); استعير الطغيان فيه لتجاوز الماء الحد (mufradat)","source_summary":"Toplu kanıt, söz öbeği içindeki öznenin olağan miktarı veya gücü aşmasını ortaklaştırır. Suda ve selde çokluk ile yükselme, denizde dalga kabarması ve sürükleme, kanda coşma, ses ve rüzgarda ise baskın güç bu çekirdeğin ayrı gerçekleşmeleridir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه طغيان الماء والسيل والبحر والدم وما علا فاجترف من صيحة أو ريح","what_is_not_ar":"ليس العصيان المجرد ولا الطاغوت ولا الصخرة الملساء"},"support_links":["sup_bf02d9b8e9643d6719e4"]},{"boundary":"Bu kategori sınır aşan kişiyi bağımsız olarak kapsar; ancak her zorbayı veya yalnızca azgın niteliği taşıyan kişiyi otomatik olarak kapsamaz. Yanlış yola önderlik eden, tapınılan veya iyilikten saptıran kişi ya da güç de bu kapsamdadır.","branch_kind":"bare","branch_ref":"root_000937/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:TagaY`|ROOT:Tgy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:6:4:2","qac_word_ref":"96:6:4","surface_ar":"يَطْغَىٰٓ"}],"gloss":"yanlış yolun önderi, tapınılan sahte varlık veya saptırıcı zorba güç","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yanlış yola önderlik eden ve başkalarını iyilik yolundan çeviren kişi, varlık veya güç temel kategoriyi oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tanrı dışında kendisine tapınılan herhangi bir varlık bu kategoriye girer."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Falcı, büyücü ve kötücül ya da başkaldıran doğaüstü varlıklar, saptırıcı işlevleriyle bu kategorinin örnekleridir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Sınırı aşan kişi ile başkalarını iyi yoldan uzaklaştıran kişi ya da güç, birbirine bağlanmadan aynı kategori adıyla anılabilir."}}],"root_ar":"ط غ ي","root_id":"root_000937","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kategorinin önderlik, Tanrı dışında tapınılma ve iyilikten saptırma biçimindeki üç temel gerçekleşmesini birlikte karşılar.","boundary_detail":"Bu kategori sınır aşan kişiyi bağımsız olarak kapsar; ancak her zorbayı veya yalnızca azgın niteliği taşıyan kişiyi otomatik olarak kapsamaz. Yanlış yola önderlik eden, tapınılan veya iyilikten saptıran kişi ya da güç de bu kapsamdadır.","branch_image_ar":"الطاغوت رأس الضلالة","concept_gloss":"yanlış yolun önderi, tapınılan sahte varlık veya saptırıcı zorba güç","contextual_glosses":[{"applicability":"Bir kişinin veya varlığın sapmayı yönetip başkalarını iyilikten uzaklaştırdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Önderlik etmeyen tapınma nesneleri ile falcı, büyücü ve doğaüstü varlık örneklerini bütünüyle kapsamaz.","preserves":"Saptırıcı önderlik ve iyilik yolundan çevirme işlevini korur."},"facet_ids":["F001","F004"],"text":"yanlış yolun önderi","usage_role":"contextual"},{"applicability":"Sözcüğün Tanrı yerine bağlılık ve tapınma yöneltilen herhangi bir varlığı anlattığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tapınılmadan da insanları iyilikten saptıran önder, falcı, büyücü veya zorba kişi kullanımlarını dışarıda bırakır.","preserves":"Tanrı dışında tapınılma ölçütünü açık ve doğal biçimde korur."},"facet_ids":["F002"],"text":"Tanrı dışında tapınılan varlık","usage_role":"explanatory"},{"applicability":"Kötücül doğaüstü bir varlığın veya zorlayıcı gücün insanı iyi yoldan uzaklaştırdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tapınılan varlık ve insan olan falcı, büyücü ya da yanlış yol önderinin bütün kullanımlarını kapsamaz.","preserves":"Kötücül güç ve iyilik yolundan saptırma işlevini korur."},"facet_ids":["F001","F003","F004"],"text":"iyilikten saptıran kötücül güç","usage_role":"contextual"}],"definition":"Yanlış yolun başı sayılan, sınır aşan, insanları iyilikten çeviren veya Tanrı dışında kendisine tapınılan kişi, varlık ya da güçtür. Falcı, büyücü ve kötücül doğaüstü varlıklar bu işlevleri taşıdıklarında kategoriye girer.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yanlış yola önderlik eden ve başkalarını iyilik yolundan çeviren kişi, varlık veya güç temel kategoriyi oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Tanrı dışında kendisine tapınılan herhangi bir varlık bu kategoriye girer."},{"facet_id":"F003","role":"example","statement":"Falcı, büyücü ve kötücül ya da başkaldıran doğaüstü varlıklar, saptırıcı işlevleriyle bu kategorinin örnekleridir."},{"facet_id":"F004","role":"extension","statement":"Sınırı aşan kişi ile başkalarını iyi yoldan uzaklaştıran kişi ya da güç, birbirine bağlanmadan aynı kategori adıyla anılabilir."}],"identity_rationale":"Kaynak ifadesi yanlış yolun önderini merkezde tutmakla birlikte kapsamı tek bir önder türüne indirmez; falcıyı, büyücüyü, kötücül doğaüstü varlığı, Tanrı dışında tapınılan varlığı, sınır aşan kişiyi ve iyilik yolundan çevireni de aynı ad altında toplar. Dal bu geniş ve işlevsel sınır açıkça korunursa geçerlidir.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yanlış yolun önderi, Tanrı dışında tapınılan varlık veya iyilikten saptıran zorba güç"}],"lexicalization_note":"Tanım, sözlük biriminin yalın kategori anlamını verir ve başka dallardaki su taşkınlığı ya da yıkıcı olay anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eşleşen dal ile sınır aşan zorba, belirli tapınma nesnesi ve kibir alanı arasındaki dört karşılaştırma kategori sınırını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ortak alan geniştir; ancak odak dalın sınır aşan kişiyi ve iyilikten çevireni bağımsız olarak kapsaması tam ikameyi engeller.","focus_only":"Odak dal, her sınır aşan kişiyi ve iyilik yolundan çevireni ayrıca kapsar.","gloss":"sapmanın önderi ve tapınılan varlık","neighbor_only":null,"neighbor_ref":"root_000936/B003","relation_type":"near_synonym","shared_zone":"Her iki dal yanlış yolun önderini, Tanrı dışında tapınılan varlığı ve falcı ya da kötücül güç gibi örnekleri kapsar."},{"boundary_match":"partial","distinction":"Odak dal saptırıcı veya tapınılan bir varlık kategorisidir; komşu dal ise böyle bir dini ya da yönlendirici işlev gerektirmeyen sınır aşımıdır.","focus_only":"Tapınılan varlığı, yanlış yolun önderini ve iyilikten saptıran doğaüstü ya da beşeri gücü kapsar.","gloss":"sınır tanımaz saptırıcı güç","neighbor_only":"Genel sınır veya ölçü aşımını, itaatsizliği ve bundan türeyen zorba kişi niteliğini kapsar.","neighbor_ref":"root_000937/B001","relation_type":"near_neighbor","shared_zone":"Sınır tanımayan zorba bir kişi aynı zamanda başkalarını yanlış yola sürüklediğinde iki kategori kesişebilir."},{"boundary_match":"field_only","distinction":"Komşu dal belirli bir nesnenin özel adıdır; odak dal ise ad, tür ve tekillik ayrımı yapmadan işlevsel bir genel kategori kurar.","focus_only":"Herhangi bir yanlış yol önderini, saptırıcı gücü veya Tanrı dışında tapınılan varlığı kapsayan genel kategoridir.","gloss":"tapınılan belirli nesne","neighbor_only":"Belirli bir topluluğa ait tek bir tapınma nesnesinin özel adını ve ona ilişkin anlatıyı kapsar.","neighbor_ref":"root_000032/B005","relation_type":"same_field","shared_zone":"İki dal da Tanrı dışında kendisine tapınılan bir varlığa uygulanabilir."},{"boundary_match":"partial","distinction":"Komşu dal bir büyüklük veya kibir niteliğidir; odak dal ise yanlış yola yönelten ya da tapınılan kişi, varlık veya güç kategorisidir.","focus_only":"Yanlış yola önderlik, tapınılma ve başkalarını iyilikten çevirme işlevlerini gerektirir.","gloss":"kibirli saptırıcı","neighbor_only":"Büyüklük, yücelik ve kişinin gerçeği kabul etmeyen kibri üzerinde durur; saptırma veya tapınılma gerektirmez.","neighbor_ref":"root_001281/B006","relation_type":"near_neighbor","shared_zone":"Kibirli ve gerçeğe direnen bir zorba, aynı zamanda başkalarını saptırdığında iki alan kesişebilir."}],"source_phrase_ar":"الطاغوت الكاهن والشيطان وكل رأس في الضلالة (sihah); كل معبود من دون الله جبت وطاغوت (tahdhib); الطاغوت الشيطان (tahdhib); الطاغوت عبارة عن كل متعد وكل معبود من دون الله (mufradat); الساحر والكاهن والمارد من الجن والصارف عن طريق الخير طاغوتا (mufradat)","source_summary":"Toplu kaynak anlatımı tek bir kişi türünden daha geniş bir işlevsel kategori kurar: yanlış yolun önderi, Tanrı dışında tapınılan varlık, kötücül doğaüstü güç, falcı, büyücü, sınır aşan kişi ve iyilikten saptıran kişi bu kapsamda birleşir.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه الطاغوت للكاهن والشيطان وكل رأس في الضلالة وكل معبود من دون الله والمتعدي الصارف عن طريق الخير","what_is_not_ar":"ليس كل طاغ ولا طغيان الماء ولا الصاعقة المسماة بالطاغية"},"support_links":[]},{"boundary":"Dal yalnızca zorba kişiyi anlatmaz; yıkıcı olayı veya kimi yorumda yıkıma neden olan sınır aşımını bildirir.","branch_kind":"bare","branch_ref":"root_000937/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:TagaY`|ROOT:Tgy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:6:4:2","qac_word_ref":"96:6:4","surface_ar":"يَطْغَىٰٓ"}],"gloss":"yıkıma götüren ezici olay veya sınır aşımı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ortak eksen, bir topluluğun yok oluşuna bağlanan ezici olay veya nedendir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir yorum, yıkım aracını şiddetli yıldırım ya da ceza bildiren öldürücü çığlık olarak belirler."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başka bir yorum, sözcüğü insanları yok eden büyük su baskınına gönderme sayar."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir diğer yorum, sözcüğü yıkım aracı değil, insanların yıkıma yol açan kendi sınır aşımının adlaşmış biçimi sayar."}}],"root_ar":"ط غ ي","root_id":"root_000937","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yıkıcı yıldırım, ceza çığlığı, büyük su baskını ve yıkıma neden olan davranış yorumu birlikte söz konusu olduğunda kullanılır.","boundary_detail":"Dal yalnızca zorba kişiyi anlatmaz; yıkıcı olayı veya kimi yorumda yıkıma neden olan sınır aşımını bildirir.","branch_image_ar":"الطاغية عذاب غالب","concept_gloss":"yıkıma götüren ezici olay veya sınır aşımı","contextual_glosses":[{"applicability":"Yok edici olayın gökten gelen şiddetli bir vuruş veya öldürücü bir ses olarak yorumlandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Büyük su baskını ve insanların kendi sınır aşımı biçimindeki diğer yorumları dışarıda bırakır.","preserves":"Yıldırım ve öldürücü ses yoluyla gerçekleşen ezici yıkım yorumunu korur."},"facet_ids":["F001","F002"],"text":"yıkıcı yıldırım ya da ceza çığlığı","usage_role":"explanatory"},{"applicability":"Yıkım aracının geniş çaplı ve ezici bir su baskını olarak yorumlandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yıldırım, öldürücü ses ve davranışsal sınır aşımı yorumlarını kapsamaz.","preserves":"Topluluğu yok eden büyük su baskını yorumunu açıkça korur."},"facet_ids":["F001","F003"],"text":"yok eden büyük su baskını","usage_role":"explanatory"},{"applicability":"Sözcüğün yıkım aracını değil, toplumun kendi taşkın davranışını adlandırdığı yorumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yıldırım, ceza çığlığı ve büyük su baskını biçimindeki yıkıcı olay yorumlarını dışarıda bırakır.","preserves":"İnsanların kendi sınır aşımının yıkıma neden olması ilişkisini korur."},"facet_ids":["F001","F004"],"text":"yıkıma yol açan sınır aşımı","usage_role":"explanatory"}],"definition":"Bir topluluğu yok eden ezici olay veya yıkıma götüren sınır aşımıdır. Kaynak yorumlarında olay, yıkıcı yıldırım ya da ceza çığlığı veya büyük su baskını olarak; neden ise insanların kendi taşkın davranışı olarak açıklanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ortak eksen, bir topluluğun yok oluşuna bağlanan ezici olay veya nedendir."},{"facet_id":"F002","role":"source_variant","statement":"Bir yorum, yıkım aracını şiddetli yıldırım ya da ceza bildiren öldürücü çığlık olarak belirler."},{"facet_id":"F003","role":"source_variant","statement":"Başka bir yorum, sözcüğü insanları yok eden büyük su baskınına gönderme sayar."},{"facet_id":"F004","role":"source_variant","statement":"Bir diğer yorum, sözcüğü yıkım aracı değil, insanların yıkıma yol açan kendi sınır aşımının adlaşmış biçimi sayar."}],"identity_rationale":"Kaynak ifadesi tek ve bütünüyle birleşmiş bir ceza türü vermez; aynı biçimi yıkıcı yıldırım veya ceza çığlığı, büyük su baskını ve insanların yıkıma yol açan kendi sınır aşımı olarak ayrı biçimlerde açıklar. Dal, bu yorum farklarını ezici bir yıkım ekseni altında koruduğu sürece kullanılabilir.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yıkıcı yıldırım veya ceza çığlığı, büyük su baskını ya da yıkıma yol açan sınır aşımı"}],"lexicalization_note":"Tanım, yalın sözlük biriminin kaynaklarda verilen olay ve neden yorumlarını korur; zorba kişi anlamını bu dala taşımaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yakın eşleşen ceza dalı ile yıldırım, yok oluş ve kapsayıcı bela alanları arasındaki dört karşılaştırma yorum farklarını yeterince gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal, yıkıcı olay yorumlarının yanında dilbilgisel olarak insanların kendi sınır aşımını bildiren neden yorumunu açıkça ayrı tutar.","focus_only":"Sözcüğü kimi yorumda insanların yıkıma yol açan kendi sınır aşımının adı sayar.","gloss":"ezici yıkım veya nedeni","neighbor_only":"Bütün kapsamı baskın ceza başlığı altında toplar ve olay ile neden arasındaki yorum farkını daha az belirgin bırakır.","neighbor_ref":"root_000936/B005","relation_type":"near_synonym","shared_zone":"İki dal da yıkıcı yıldırım, ceza çığlığı ve büyük su baskınıyla bağlantılı ezici yok oluşu kapsar."},{"boundary_match":"partial","distinction":"Komşu dal yıldırım olayının genel alanıdır; odak dal belirli bir yıkım anlatısındaki sözcüğün yıldırım yanında su baskını ve davranışsal neden yorumlarını da taşır.","focus_only":"Büyük su baskınını ve yıkıma neden olan davranışsal sınır aşımını da kapsar.","gloss":"yıkıcı göksel vuruş","neighbor_only":"Göksel gürültü, şiddetli vuruş, ateş, ölüm veya ceza içerebilen yıldırım olayının kendisini daha genel biçimde anlatır.","neighbor_ref":"root_000864/B002","relation_type":"near_neighbor","shared_zone":"Yok edici yıldırım veya şiddetli göksel ses iki dalın kesiştiği olaydır."},{"boundary_match":"partial","distinction":"Odak dal yıkımın ezici aracını veya nedenini öne çıkarır; komşu dal ise yok oluş ve bozulma sonucunun kendisini daha geniş biçimde adlandırır.","focus_only":"Yok oluşa yol açan yıldırım, ses, su baskını veya sınır aşımı biçimindeki araç ya da nedeni bildirir.","gloss":"yok oluş ve bozulma","neighbor_only":"Bir şeyin veya kişinin yok olmuş, bozulmuş ya da geçersiz hale gelmiş durumunu ve bu duruma ilişkin yargıyı kapsar.","neighbor_ref":"root_000164/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal yıkım, yok olma ve ağır ceza sonucuyla ilişkilidir."},{"boundary_match":"field_only","distinction":"Komşu dalın çekirdeği kapsayıp örtmedir; odak dalın çekirdeği ise yıkıma bağlanan ezici olay veya davranışsal nedendir.","focus_only":"Yıldırım, öldürücü ses, büyük su baskını veya davranışsal neden gibi belirli yıkım yorumlarını taşır.","gloss":"her yanı kaplayan bela","neighbor_only":"İnsanları bütünüyle kaplayan kıyamet, bela, yaygın sıkıntı veya kişiyi tutan hastalık alanlarını kapsar.","neighbor_ref":"root_001088/B002","relation_type":"same_field","shared_zone":"İki dal da topluluğu kuşatan ağır bir ceza veya yıkıcı olay bağlamında kullanılabilir."}],"source_phrase_ar":"الطاغية الصاعقة ويعني صيحة العذاب (sihah); أهلكوا بالطاغية أي بطغيانهم مصدر على فاعلة (tahdhib); فأهلكوا بالطاغية فإشارة إلى الطوفان (mufradat)","source_summary":"Kanıt aynı kullanım için üç açıklama sunar: öldürücü yıldırım veya ceza çığlığı, yıkıcı büyük su baskını ve insanların kendi sınır aşımı. Bunlar yıkım bağlantısında birleşir, fakat olayın aracı ile yıkımın davranışsal nedeni aynılaştırılmamalıdır.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه الطاغية إذا أريد بها الصاعقة أو صيحة العذاب أو الطوفان أو مصدر الطغيان في الهلاك","what_is_not_ar":"ليس الطاغية بمعنى الجبار ولا مطلق الطاغوت"},"support_links":[]},{"boundary":"Dal kaya yüzeyi, dağ doruğu ve yüksek yer adlarıyla sınırlıdır; sınır aşımı, su taşkınlığı ve saptırıcı güç anlamlarını içermez.","branch_kind":"bare","branch_ref":"root_000937/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَغَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:TagaY`|ROOT:Tgy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:6:4:2","qac_word_ref":"96:6:4","surface_ar":"يَطْغَىٰٓ"}],"gloss":"pürüzsüz kaya yüzeyi, dağ doruğu veya yüksek yer","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Adın bir kullanımı, yüzeyi düz ve kaygan olan kaya parçasını bildirir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kayanın pürüzsüzlüğü, üzerine konmaya çalışan yırtıcı kuşun pençesini geri sektirecek kadar belirgindir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı adın başka bir kullanımı dağın en yüksek bölümünü, yani doruğunu bildirir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Aynı kökten farklı bir ad biçimi, türü belirtilmeyen herhangi bir yüksek yeri bildirir."}}],"root_ar":"ط غ ي","root_id":"root_000937","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dal içindeki iki ad biçiminin pürüzsüz kaya, dağın en yüksek bölümü ve genel yüksek yer anlamlarını birlikte gösterir.","boundary_detail":"Dal kaya yüzeyi, dağ doruğu ve yüksek yer adlarıyla sınırlıdır; sınır aşımı, su taşkınlığı ve saptırıcı güç anlamlarını içermez.","branch_image_ar":"الطغية الصفاة الملساء","concept_gloss":"pürüzsüz kaya yüzeyi, dağ doruğu veya yüksek yer","contextual_glosses":[{"applicability":"Yüzeyinin düzgünlüğü ve kayganlığı nedeniyle pençenin tutunamadığı kaya anlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dağın doruğu ve genel yüksek yer anlamlarını dışarıda bırakır.","preserves":"Kayanın pürüzsüz ve kaygan yüzey niteliğini korur."},"facet_ids":["F001","F002"],"text":"pürüzsüz kaya yüzeyi","usage_role":"contextual"},{"applicability":"Aynı ad biçiminin dağın en yüksek bölümünü anlattığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Pürüzsüz kaya yüzeyi ve türü belirtilmeyen yüksek yer anlamlarını kapsamaz.","preserves":"Dağın en yüksek bölümü olma niteliğini açıkça korur."},"facet_ids":["F003"],"text":"dağın doruğu","usage_role":"contextual"},{"applicability":"Aynı kökten farklı ad biçiminin genel olarak çevresinden yüksek bir yeri anlattığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Pürüzsüz kaya yüzeyi ve özel olarak dağın doruğu olan diğer ad kullanımlarını dışarıda bırakır.","preserves":"Türü belirtilmeyen bir yerin çevresine göre yüksek olmasını korur."},"facet_ids":["F004"],"text":"yüksek yer","usage_role":"contextual"}],"definition":"Pürüzsüz bir kaya yüzeyi ya da dağın en yüksek bölümüdür; aynı kökten başka bir ad biçimi ise herhangi bir yüksek yeri bildirir. Kaya anlamında yüzey öylesine kaygandır ki yırtıcı kuşun pençesi geri seker.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Adın bir kullanımı, yüzeyi düz ve kaygan olan kaya parçasını bildirir."},{"facet_id":"F002","role":"example","statement":"Kayanın pürüzsüzlüğü, üzerine konmaya çalışan yırtıcı kuşun pençesini geri sektirecek kadar belirgindir."},{"facet_id":"F003","role":"source_variant","statement":"Aynı adın başka bir kullanımı dağın en yüksek bölümünü, yani doruğunu bildirir."},{"facet_id":"F004","role":"source_variant","statement":"Aynı kökten farklı bir ad biçimi, türü belirtilmeyen herhangi bir yüksek yeri bildirir."}],"identity_rationale":"Kaynak ifadesi pürüzsüz kaya yüzeyini, dağın en yüksek bölümünü ve aynı kökten başka bir biçimle herhangi bir yüksek yeri açıkça sıralar; kayanın kayganlığına yırtıcı kuş pençesinin tutunamaması da pürüzsüzlük niteliğini doğrular. Sağlanan dal çerçevesi bu üç kullanımı ayrıştırmaya elverişlidir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"pürüzsüz ve kaygan kaya yüzeyi"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"dağın doruğu"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yüksek yer"}],"lexicalization_note":"Tanım yalın ad biçimlerinin üç yer ve yüzey anlamını korur; bunları sınır aşma çekirdeğinden türetmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eşleşen dal ile pürüzsüz kaya, dağ bölümü, yerden yükselti ve sert yüksek arazi arasındaki beş karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kartlarda çekirdek, ad biçimleri ve yer kapsamı bakımından anlamlı bir sınır farkı görünmez.","focus_only":null,"gloss":"pürüzsüz kaya veya yüksek yer","neighbor_only":null,"neighbor_ref":"root_000936/B006","relation_type":"synonym","shared_zone":"Her iki dal pürüzsüz kaya yüzeyini, dağın en yüksek bölümünü ve aynı kökten adla yüksek yeri kapsar."},{"boundary_match":"partial","distinction":"Odak dal kaya yüzeyi yanında dağ doruğu ve yüksek yer anlamlarını taşır; komşu dal ise kayanın sertliği, genişliği ve yüzey temizliği üzerinde daha ayrıntılıdır.","focus_only":"Dağın doruğu ve genel yüksek yer anlamlarını da kapsar.","gloss":"pürüzsüz sert kaya","neighbor_only":"Geniş, sert ve pürüzsüz kayanın kumdan, çamurdan ve topraktan arınmış olmasını ve adı verilen belirli bir yeri de kapsar.","neighbor_ref":"root_000873/B006","relation_type":"near_synonym","shared_zone":"İki dalın ortak alanı yüzeyi pürüzsüz olan sert kaya parçasıdır."},{"boundary_match":"partial","distinction":"Odak dalda dağa ilişkin bölüm doruktur; komşu dal ise dağın bütününü veya özellikle orta kısmını bildirir.","focus_only":"Dağın yalnız en yüksek bölümünü, ayrıca pürüzsüz kaya ve genel yüksek yeri kapsar.","gloss":"dağ ve orta bölümü","neighbor_only":"Dağın bütünü ile dağların orta bölümünü adlandırır.","neighbor_ref":"root_000840/B017","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir dağın bölümü veya dağlık yükseltiyle ilişkilidir."},{"boundary_match":"partial","distinction":"Komşu dalın çekirdeği zeminden yükselmiş biçimdir; odak dal ise belirli ad biçimleriyle pürüzsüz kaya, dağ doruğu veya yüksek yer kategorilerini taşır.","focus_only":"Pürüzsüz kaya yüzeyini ve özellikle dağın doruğunu adlandırabilir.","gloss":"yerden yükselen tümsek","neighbor_only":"Toprağın tümsek, tepecik, kum sırtı veya rüzgarla oluşmuş kabarıklık gibi yükselen biçimlerini kapsar.","neighbor_ref":"root_000298/B001","relation_type":"near_neighbor","shared_zone":"Çevresindeki zeminden yüksek olan bir yer iki dalın ortak alanına girebilir."},{"boundary_match":"partial","distinction":"Odak dalın ayırt edici özellikleri pürüzsüz kaya yüzeyi ile doruk konumudur; komşu dal sert ve yüksek arazi türlerini daha genel biçimde toplar.","focus_only":"Kayada pürüzsüz yüzeyi ve dağda en yüksek bölümü özellikle ayırt eder.","gloss":"sert yüksek arazi","neighbor_only":"Sert veya kaba yüksek araziyi, küçük tepeyi, taşları ve belirgin arazi işaretlerini daha geniş biçimde kapsar.","neighbor_ref":"root_000258/B004","relation_type":"near_neighbor","shared_zone":"Sert, taşlık ve çevresine göre yüksek bir yer iki dalın kapsamında kesişebilir."}],"source_phrase_ar":"الطغية الصفاة الملساء (maqayis;tahdhib); الطغية أعلى الجبل (sihah); كل مكان مرتفع طغوة (sihah); تنبي العقاب لملاستها (sihah)","source_summary":"Toplu kanıt, pürüzsüz kaya ile dağın doruğunu aynı ad biçiminin iki kullanımı olarak, herhangi bir yüksek yeri ise aynı kökten başka bir ad biçiminin anlamı olarak verir. Yırtıcı kuşun pençesinin geri sekmesi, kaya yüzeyinin kayganlığına ilişkin açıklayıcı örnektir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه الطغية للصفاة الملساء وأعلى الجبل والطغوة للمكان المرتفع","what_is_not_ar":"ليس مجاوزة الحد ولا الطغيان ولا الطاغوت"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["96:6:1"],"branch_refs":[],"candidate_id":"cand_ad34891364bc2f3d5951","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:1:audible-halt","source_type":"word_analysis","support_ids":["sup_b392af20cb678bda1aa1","sup_d63d1618bce55e719494"],"title":"sound shape makes the stop audible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:1","qac_refs":["96:6:1:1"],"status":"accepted"}},{"anchor_refs":["96:6:1"],"branch_refs":[],"candidate_id":"cand_b2b83f1da22a8aa1410a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:1:boundary-pivot","source_type":"word_analysis","support_ids":["sup_737f48e9c55ee7c36f6f","sup_d63d1618bce55e719494"],"title":"teaching scene turns into indictment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:1","qac_refs":["96:6:1:1"],"status":"accepted"}},{"anchor_refs":["96:6:1"],"branch_refs":[],"candidate_id":"cand_34bac51c089d99084c0f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:1:confrontational-rebuke","source_type":"word_analysis","support_ids":["sup_2e43304fd0654ae8bb76","sup_d63d1618bce55e719494"],"title":"report becomes confrontational speech","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:1","qac_refs":["96:6:1:1"],"status":"accepted"}},{"anchor_refs":["96:6:1"],"branch_refs":[],"candidate_id":"cand_fbbf0fed89de07fa0fdb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:1:deterrent-alert","source_type":"word_analysis","support_ids":["sup_c4de3511d22612335cd5","sup_d63d1618bce55e719494"],"title":"deterrence and alerting work together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:1","qac_refs":["96:6:1:1"],"status":"accepted"}},{"anchor_refs":["96:6:1"],"branch_refs":[],"candidate_id":"cand_ec1b8179fc7c25083ec8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:1:emphasis-launch","source_type":"word_analysis","support_ids":["sup_c3c048422ba61c412524","sup_d63d1618bce55e719494"],"title":"opening resistance prepares stacked assertion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:1","qac_refs":["96:6:1:1"],"status":"accepted"}},{"anchor_refs":["96:6:1"],"branch_refs":[],"candidate_id":"cand_a2bedbb6c3e769cf0dff","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:1:surah-punctuation","source_type":"word_analysis","support_ids":["sup_b675d64c929702c79958","sup_d63d1618bce55e719494"],"title":"repeated stop marks surah escalation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:1","qac_refs":["96:6:1:1"],"status":"accepted"}},{"anchor_refs":["96:6:2"],"branch_refs":[],"candidate_id":"cand_6ee1c2fd32d41766b6fa","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:2:governed-diagnostic-clause","source_type":"word_analysis","support_ids":["sup_987353aa41bb252de651","sup_ef849c36075d9e575def"],"title":"emphatic particle governs the diagnosis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:2","qac_refs":["96:6:2:1"],"status":"accepted"}},{"anchor_refs":["96:6:2"],"branch_refs":[],"candidate_id":"cand_03c7b806c82ced0f1d24","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:2:maximal-emphasis-frame","source_type":"word_analysis","support_ids":["sup_66ca52ac7c9c5885cb54","sup_987353aa41bb252de651"],"title":"confirmation is doubled around the predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:2","qac_refs":["96:6:2:1"],"status":"accepted"}},{"anchor_refs":["96:6:2"],"branch_refs":[],"candidate_id":"cand_b74615acd148c10e4489","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:2:nasal-assertion","source_type":"word_analysis","support_ids":["sup_01c3b7f3b6db6b06344d","sup_987353aa41bb252de651"],"title":"nasal sound binds particle and noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:2","qac_refs":["96:6:2:1"],"status":"accepted"}},{"anchor_refs":["96:6:2"],"branch_refs":[],"candidate_id":"cand_52217dee2e83efef0229","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:2:particle-sequence","source_type":"word_analysis","support_ids":["sup_06295f6cd9d11f34660b","sup_987353aa41bb252de651"],"title":"halt then assertion creates a two-beat turn","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:2","qac_refs":["96:6:2:1"],"status":"accepted"}},{"anchor_refs":["96:6:3"],"branch_refs":[],"candidate_id":"cand_79bbd97571a4f47b7bb7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:3:etymology-irony","source_type":"word_analysis","support_ids":["sup_e1ee47f5957a3a0bf935","sup_e5c6c00f3debb2aae2d9"],"title":"sociability and forgetfulness sharpen the irony","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:3","qac_refs":["96:6:3:1","96:6:3:2"],"status":"accepted"}},{"anchor_refs":["96:6:3"],"branch_refs":[],"candidate_id":"cand_7ff6f9d68ea132ca40d4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:3:generic-singular-species","source_type":"word_analysis","support_ids":["sup_e1ee47f5957a3a0bf935","sup_eb9917a78993eeb0bb51"],"title":"singular definite carries species force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:3","qac_refs":["96:6:3:1","96:6:3:2"],"status":"accepted"}},{"anchor_refs":["96:6:3"],"branch_refs":[],"candidate_id":"cand_d23bf1653730f029fd9c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:3:governed-human-center","source_type":"word_analysis","support_ids":["sup_67066f4a58fb60ce0d11","sup_e1ee47f5957a3a0bf935"],"title":"human noun is seized by the emphatic frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:3","qac_refs":["96:6:3:1","96:6:3:2"],"status":"accepted"}},{"anchor_refs":["96:6:3"],"branch_refs":[],"candidate_id":"cand_0395d0f650dc9312af6b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:3:human-transgression-pairing","source_type":"word_analysis","support_ids":["sup_943c87b70200fc53a39b","sup_e1ee47f5957a3a0bf935"],"title":"human noun is paired with the excess root","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:3","qac_refs":["96:6:3:1","96:6:3:2"],"status":"accepted"}},{"anchor_refs":["96:6:3"],"branch_refs":[],"candidate_id":"cand_921c14ee0b41820deac3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:3:nasal-binding","source_type":"word_analysis","support_ids":["sup_63ec25d3dece750436ea","sup_e1ee47f5957a3a0bf935"],"title":"sound carries the governed relation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:3","qac_refs":["96:6:3:1","96:6:3:2"],"status":"accepted"}},{"anchor_refs":["96:6:3"],"branch_refs":[],"candidate_id":"cand_a137cba5dcdb89f672fa","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:3:negative-diagnosis-formula","source_type":"word_analysis","support_ids":["sup_cc9d607ceb3843ebd7b5","sup_e1ee47f5957a3a0bf935"],"title":"formula joins adverse human diagnoses","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:3","qac_refs":["96:6:3:1","96:6:3:2"],"status":"accepted"}},{"anchor_refs":["96:6:3"],"branch_refs":[],"candidate_id":"cand_13553e40fc7f452191d1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:3:recipient-to-agent","source_type":"word_analysis","support_ids":["sup_cfc3f7e660ea1ecfe535","sup_e1ee47f5957a3a0bf935"],"title":"created and taught human becomes transgressing agent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:3","qac_refs":["96:6:3:1","96:6:3:2"],"status":"accepted"}},{"anchor_refs":["96:6:3"],"branch_refs":[],"candidate_id":"cand_5cdd393421f3524f8aad","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:3:same-surah-load-bearing","source_type":"word_analysis","support_ids":["sup_96a410e3ff5eb50b1a05","sup_e1ee47f5957a3a0bf935"],"title":"same noun carries the section's anthropology","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:3","qac_refs":["96:6:3:1","96:6:3:2"],"status":"accepted"}},{"anchor_refs":["96:6:3"],"branch_refs":[],"candidate_id":"cand_87529bd1864d2adfe7e1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:3:singular-not-plural","source_type":"word_analysis","support_ids":["sup_579f51d24b2358429d9c","sup_e1ee47f5957a3a0bf935"],"title":"humanity is treated distributively as one subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:3","qac_refs":["96:6:3:1","96:6:3:2"],"status":"accepted"}},{"anchor_refs":["96:6:4"],"branch_refs":[],"candidate_id":"cand_dcc8565024f8aaa725c0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:4:compact-cadence","source_type":"word_analysis","support_ids":["sup_b53f0749ff4368a5e4b6","sup_cc367ea5f8ccbb97c3f6"],"title":"short onset pushes into the closing verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:4","qac_refs":["96:6:4:1"],"status":"accepted"}},{"anchor_refs":["96:6:4"],"branch_refs":[],"candidate_id":"cand_bebc3b38d46ccc1071aa","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:4:fused-prefix","source_type":"word_analysis","support_ids":["sup_b53f0749ff4368a5e4b6","sup_cfbbff72719d50861672"],"title":"certainty is fused to the action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:4","qac_refs":["96:6:4:1"],"status":"accepted"}},{"anchor_refs":["96:6:4"],"branch_refs":[],"candidate_id":"cand_d93d3fb1dce1624865ba","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:4:inna-la-frame","source_type":"word_analysis","support_ids":["sup_4e7b7672baf987187622","sup_b53f0749ff4368a5e4b6"],"title":"second confirmer completes the frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:4","qac_refs":["96:6:4:1"],"status":"accepted"}},{"anchor_refs":["96:6:4"],"branch_refs":[],"candidate_id":"cand_0866b09f08903c6a77a4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:6:4:predicate-emphasis-scope","source_type":"word_analysis","support_ids":["sup_b53f0749ff4368a5e4b6","sup_db1b0bac0b19f2209443"],"title":"predicate-side lām confirms the verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:4","qac_refs":["96:6:4:1"],"status":"accepted"}},{"anchor_refs":["96:6:5"],"branch_refs":[],"candidate_id":"cand_9ea2b2c17ee714a5a5b7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000936","root_000937"],"scope":"focus_ayah","source_local_id":"96:6:5:closure-landing","source_type":"word_analysis","support_ids":["sup_1721c6321ce780ccad68","sup_ead8b6a1109fb266e131"],"title":"final verb is the ayah's accusation point","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:5","qac_refs":["96:6:4:2"],"status":"accepted"}},{"anchor_refs":["96:6:5"],"branch_refs":[],"candidate_id":"cand_9c9fa2b6fedcbfc6d013","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000936","root_000937"],"scope":"focus_ayah","source_local_id":"96:6:5:converged-pressure-point","source_type":"word_analysis","support_ids":["sup_afe3c5abd17eb284d0d9","sup_ead8b6a1109fb266e131"],"title":"root image, aspect, and emphasis converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:5","qac_refs":["96:6:4:2"],"status":"accepted"}},{"anchor_refs":["96:6:5"],"branch_refs":[],"candidate_id":"cand_db298332f6237af0c8fd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000936","root_000937"],"scope":"focus_ayah","source_local_id":"96:6:5:derivational-overreach-field","source_type":"word_analysis","support_ids":["sup_92f3d2d6e4bdf3479c01","sup_ead8b6a1109fb266e131"],"title":"false-authority field deepens the overreach","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:5","qac_refs":["96:6:4:2"],"status":"accepted"}},{"anchor_refs":["96:6:5"],"branch_refs":[],"candidate_id":"cand_5f7dd9d2b9ce73a44b6b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000936","root_000937"],"scope":"focus_ayah","source_local_id":"96:6:5:emphatic-verbal-predicate","source_type":"word_analysis","support_ids":["sup_6b229b3d70125ae5afd0","sup_ead8b6a1109fb266e131"],"title":"assertion lands on the final verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:5","qac_refs":["96:6:4:2"],"status":"accepted"}},{"anchor_refs":["96:6:5"],"branch_refs":[],"candidate_id":"cand_19643a54ff5c61f55e6d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000936","root_000937"],"scope":"focus_ayah","source_local_id":"96:6:5:evaluative-blame","source_type":"word_analysis","support_ids":["sup_8803ab2fe6a604f79c1a","sup_ead8b6a1109fb266e131"],"title":"the verb names blameworthy overreach","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:5","qac_refs":["96:6:4:2"],"status":"accepted"}},{"anchor_refs":["96:6:5"],"branch_refs":[],"candidate_id":"cand_cd7faea6bff0c4e1bab1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000936","root_000937"],"scope":"focus_ayah","source_local_id":"96:6:5:extended-final-sound","source_type":"word_analysis","support_ids":["sup_b88d0a7f47e817cd31ee","sup_ead8b6a1109fb266e131"],"title":"long final sound stretches the verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:5","qac_refs":["96:6:4:2"],"status":"accepted"}},{"anchor_refs":["96:6:5"],"branch_refs":[],"candidate_id":"cand_52092827ff40fe7fe64b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000936","root_000937"],"scope":"focus_ayah","source_local_id":"96:6:5:generic-singular-actor","source_type":"word_analysis","support_ids":["sup_ead8b6a1109fb266e131","sup_f9d27c76f4f8ea56d70a"],"title":"generic humanity acts as one subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:5","qac_refs":["96:6:4:2"],"status":"accepted"}},{"anchor_refs":["96:6:5"],"branch_refs":[],"candidate_id":"cand_3374c5a840bd95124f37","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000936","root_000937"],"scope":"focus_ayah","source_local_id":"96:6:5:insan-pairing","source_type":"word_analysis","support_ids":["sup_6e99fdbbeeb000083728","sup_ead8b6a1109fb266e131"],"title":"human noun activates the excess pairing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:5","qac_refs":["96:6:4:2"],"status":"accepted"}},{"anchor_refs":["96:6:5"],"branch_refs":[],"candidate_id":"cand_985ceb114b9d146a5f22","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000936","root_000937"],"scope":"focus_ayah","source_local_id":"96:6:5:marked-imperfect-selection","source_type":"word_analysis","support_ids":["sup_e4714253fd414d8eab9d","sup_ead8b6a1109fb266e131"],"title":"rare imperfect form is deliberately selected","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:5","qac_refs":["96:6:4:2"],"status":"accepted"}},{"anchor_refs":["96:6:5"],"branch_refs":[],"candidate_id":"cand_fe445376901348fa738d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000936","root_000937"],"scope":"focus_ayah","source_local_id":"96:6:5:moral-overflow-root","source_type":"word_analysis","support_ids":["sup_c146d44c468baa918eb6","sup_ead8b6a1109fb266e131"],"title":"overflow image becomes moral overstepping","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:5","qac_refs":["96:6:4:2"],"status":"accepted"}},{"anchor_refs":["96:6:5"],"branch_refs":[],"candidate_id":"cand_9a4f75a707ffa208abab","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000936","root_000937"],"scope":"focus_ayah","source_local_id":"96:6:5:next-ayah-cause","source_type":"word_analysis","support_ids":["sup_7879eaf1262a95308067","sup_ead8b6a1109fb266e131"],"title":"complete accusation receives cause next","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:5","qac_refs":["96:6:4:2"],"status":"accepted"}},{"anchor_refs":["96:6:5"],"branch_refs":[],"candidate_id":"cand_ae63b1584831c264bb4b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000936","root_000937"],"scope":"focus_ayah","source_local_id":"96:6:5:objectless-transgression","source_type":"word_analysis","support_ids":["sup_d187495fe26fe41f5a02","sup_ead8b6a1109fb266e131"],"title":"no object leaves the crossing unlocalized","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:5","qac_refs":["96:6:4:2"],"status":"accepted"}},{"anchor_refs":["96:6:5"],"branch_refs":[],"candidate_id":"cand_d8fbd5b7a33e69e33cde","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000936","root_000937"],"scope":"focus_ayah","source_local_id":"96:6:5:ongoing-aspect","source_type":"word_analysis","support_ids":["sup_0cdfbf1a09029efbd74e","sup_ead8b6a1109fb266e131"],"title":"imperfect aspect makes transgression characteristic","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:5","qac_refs":["96:6:4:2"],"status":"accepted"}},{"anchor_refs":["96:6:5"],"branch_refs":[],"candidate_id":"cand_91fb8f4c524280511a97","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000936","root_000937"],"scope":"focus_ayah","source_local_id":"96:6:5:pharaonic-overreach","source_type":"word_analysis","support_ids":["sup_4f346bc1b45d8277c15e","sup_ead8b6a1109fb266e131"],"title":"Pharaoh-associated overreach becomes generic potential","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:5","qac_refs":["96:6:4:2"],"status":"accepted"}},{"anchor_refs":["96:6:5"],"branch_refs":[],"candidate_id":"cand_c849c74e607b951d9dc0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000936","root_000937"],"scope":"focus_ayah","source_local_id":"96:6:5:prior-teaching-reversal","source_type":"word_analysis","support_ids":["sup_5197bd7d942a6dee31b0","sup_ead8b6a1109fb266e131"],"title":"completed teaching meets ongoing excess","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:5","qac_refs":["96:6:4:2"],"status":"accepted"}},{"anchor_refs":["96:6:5"],"branch_refs":[],"candidate_id":"cand_03bf01a5ad2791df6aab","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000936","root_000937"],"scope":"focus_ayah","source_local_id":"96:6:5:visual-opposite-pole","source_type":"word_analysis","support_ids":["sup_10f4f3191fde3236e958","sup_ead8b6a1109fb266e131"],"title":"guided sight gives an opposite-pole contrast","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:6:5","qac_refs":["96:6:4:2"],"status":"accepted"}},{"anchor_refs":["96:6:3"],"branch_refs":[],"candidate_id":"cand_3fb3afd808b0336d2a16","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000059"],"scope":"focus_ayah","source_local_id":"96:6:3:2","source_type":"qac_morpheme","support_ids":["sup_11f60245dc602dc951ac"],"title":"QAC root occurrence: ء ن س","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["96:6:4"],"branch_refs":[],"candidate_id":"cand_4a188077e4d6710838fb","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000936","root_000937"],"scope":"focus_ayah","source_local_id":"96:6:4:2","source_type":"qac_morpheme","support_ids":["sup_1a32e08a8c6798837f5c"],"title":"QAC root occurrence: ط غ ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["96:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"96:6","branch_refs":["root_000059/B001","root_000937/B001"],"candidate_id":"cand_12218dcac34d2427ea99","commentary_obligation":"review","hft_ref":"hft_add38f071b4d377ba883","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b01_human_bound_crosser","source_type":"hft","support_ids":["sup_4edd506a257f99282c67"],"title":"b01_human_bound_crosser","trust":"legacy_unbound"},{"anchor_refs":["96:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"96:6","branch_refs":["root_000059/B001","root_000937/B002"],"candidate_id":"cand_10bd6da7b159be6c96e3","commentary_obligation":"review","hft_ref":"hft_ee646a6a7109a2593490","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b02_human_overflow","source_type":"hft","support_ids":["sup_bf02d9b8e9643d6719e4"],"title":"b02_human_overflow","trust":"legacy_unbound"},{"anchor_refs":["96:6"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"96:6","branch_refs":["root_000059/B003","root_000937/B001"],"candidate_id":"cand_5f5146d03da9767b76e8","commentary_obligation":"review","hft_ref":"hft_8096ca7f0a20d40dff54","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b03_familiarity_disarms_limits","source_type":"hft","support_ids":["sup_5588a2cd2cacf5478919"],"title":"b03_familiarity_disarms_limits","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ","qac_morphemes":[{"lemma_ar":"كَلَّا","morph_features":"STEM|POS:AVR|LEM:kal~aA","morpheme_role":"STEM","pos":"AVR","qac_ref":"96:6:1:1","qac_word_ref":"96:6:1","root_ar":"","surface_ar":"كَلَّآ"},{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"96:6:2:1","qac_word_ref":"96:6:2","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"96:6:3:1","qac_word_ref":"96:6:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"96:6:3:2","qac_word_ref":"96:6:3","root_ar":"ء ن س","surface_ar":"إِنسَٰنَ"},{"lemma_ar":"","morph_features":"PREFIX|l:EMPH+","morpheme_role":"PREFIX","pos":"EMPH","qac_ref":"96:6:4:1","qac_word_ref":"96:6:4","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"طَغَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:TagaY`|ROOT:Tgy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:6:4:2","qac_word_ref":"96:6:4","root_ar":"ط غ ي","surface_ar":"يَطْغَىٰٓ"}],"word_analysis_qac_refs":[["96:6:1:1"],["96:6:2:1"],["96:6:3:1","96:6:3:2"],["96:6:4:1"],["96:6:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["96:6:1","96:6:2","96:6:3","96:6:4","96:6:5"]},"focus_surface_evidence":{"arabic_uthmani":"كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ","qac_morphemes":[{"lemma_ar":"كَلَّا","morph_features":"STEM|POS:AVR|LEM:kal~aA","morpheme_role":"STEM","pos":"AVR","qac_ref":"96:6:1:1","qac_word_ref":"96:6:1","root_ar":"","surface_ar":"كَلَّآ"},{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"96:6:2:1","qac_word_ref":"96:6:2","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"96:6:3:1","qac_word_ref":"96:6:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"96:6:3:2","qac_word_ref":"96:6:3","root_ar":"ء ن س","surface_ar":"إِنسَٰنَ"},{"lemma_ar":"","morph_features":"PREFIX|l:EMPH+","morpheme_role":"PREFIX","pos":"EMPH","qac_ref":"96:6:4:1","qac_word_ref":"96:6:4","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"طَغَىٰ","morph_features":"STEM|POS:V|IMPF|LEM:TagaY`|ROOT:Tgy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:6:4:2","qac_word_ref":"96:6:4","root_ar":"ط غ ي","surface_ar":"يَطْغَىٰٓ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["96:6:1:1"],["96:6:2:1"],["96:6:3:1","96:6:3:2"],["96:6:4:1"],["96:6:4:2"]],"word_analysis_refs":["96:6:1","96:6:2","96:6:3","96:6:4","96:6:5"],"word_rows":[{"analysis_record_ref":"96:6:1","analytic_gloss_range_en":"deterrent and alerting response particle that halts the prior movement and opens an emphatic diagnosis","analytic_root_gloss_range_en":null,"qac_refs":["96:6:1:1"],"root":{},"surface":{"arabic":"كَلَّا","transliteration":"kallā"}},{"analysis_record_ref":"96:6:2","analytic_gloss_range_en":"emphatic annulling particle that governs the human noun and opens a confirmed diagnostic clause","analytic_root_gloss_range_en":null,"qac_refs":["96:6:2:1"],"root":{},"surface":{"arabic":"إِنَّ","transliteration":"inna"}},{"analysis_record_ref":"96:6:3","analytic_gloss_range_en":"the human being as a generic species noun, grammatically governed inside the emphatic clause","analytic_root_gloss_range_en":"human social and perceptive being; disputed links with forgetfulness remain interpretive pressure, while the local noun selects the generic human category","qac_refs":["96:6:3:1","96:6:3:2"],"root":{"arabic":"أ ن س","transliteration":"ʾ-n-s"},"surface":{"arabic":"ٱلْإِنسَٰنَ","transliteration":"al-insāna"}},{"analysis_record_ref":"96:6:4","analytic_gloss_range_en":"emphatic predicate prefix that completes the {{ar:إِنَّ ... لَـ}} ({{tr:inna ... la-}}) confirmation frame","analytic_root_gloss_range_en":null,"qac_refs":["96:6:4:1"],"root":{},"surface":{"arabic":"لَ","transliteration":"la-"}},{"analysis_record_ref":"96:6:5","analytic_gloss_range_en":"ongoing or characteristic overstepping of bounds in rebellion; the local human subject selects moral transgression while overflow imagery remains active as pressure","analytic_root_gloss_range_en":"overstepping bounds, rebellion, excess, overflow, false authority, and overwhelming force; local grammar selects the intransitive human overstepping branch and narrows physical overflow to source-image pressure","qac_refs":["96:6:4:2"],"root":{"arabic":"ط غ ي","transliteration":"ṭ-gh-y"},"surface":{"arabic":"يَطْغَىٰٓ","transliteration":"yaṭghā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["96:6"],"branch_refs":["root_000059/B001","root_000937/B001"],"candidate_id":"cand_12218dcac34d2427ea99","evidence_scope":"focus_ayah","hft_ref":"hft_add38f071b4d377ba883","item_id":"b01_human_bound_crosser","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b01_human_bound_crosser","support_id":"sup_4edd506a257f99282c67"},{"anchor_refs":["96:6"],"branch_refs":["root_000059/B001","root_000937/B002"],"candidate_id":"cand_10bd6da7b159be6c96e3","evidence_scope":"focus_ayah","hft_ref":"hft_ee646a6a7109a2593490","item_id":"b02_human_overflow","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b02_human_overflow","support_id":"sup_bf02d9b8e9643d6719e4"},{"anchor_refs":["96:6"],"branch_refs":["root_000059/B003","root_000937/B001"],"candidate_id":"cand_5f5146d03da9767b76e8","evidence_scope":"focus_ayah","hft_ref":"hft_8096ca7f0a20d40dff54","item_id":"b03_familiarity_disarms_limits","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b03_familiarity_disarms_limits","support_id":"sup_5588a2cd2cacf5478919"}],"diagnostics":[],"lane_counts":{"global":11,"macro":12,"micro":3},"packet_summary":{"ayah_count":19,"focus_ref":"96:6","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ص ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":false,"target_occurrences":7,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"د ع و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000478","furuq_root_norm":"د ع و","furuq_source_root_norm":"د ع و","is_dominant":true,"target_occurrences":77,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000477","furuq_root_norm":"د ع ع","furuq_source_root_norm":"د ع ع","is_dominant":false,"target_occurrences":22,"target_rank":2}]},{"qac_root":"ن د و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001487","furuq_root_norm":"ن د ي","furuq_source_root_norm":"ن د ي","is_dominant":true,"target_occurrences":33,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001486","furuq_root_norm":"ن د و","furuq_source_root_norm":"ن د و","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001563","furuq_root_norm":"ن و د","furuq_source_root_norm":"ن و د","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ط و ع","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000956","furuq_root_norm":"ط و ع","furuq_source_root_norm":"ط و ع","is_dominant":true,"target_occurrences":96,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000706","furuq_root_norm":"س ط ع","furuq_source_root_norm":"س ط ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["96:1","96:2","96:3","96:4","96:5","96:6","96:7","96:8","96:9","96:10","96:11","96:12","96:13","96:14","96:15","96:16","96:17","96:18","96:19"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"96:6","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":11,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"96:6","lane":"micro","linguistic_source_ref":"96:6","surface_ref":"96:6","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"96:6","target_tokens":[["Hayır",["96:6:1"]],["İnsan",["96:6:3"]],["gerçekten",["96:6:2","96:6:4"]],["sınırı",["96:6:4"]],["aşar",["96:6:4"]]],"text":"Hayır! İnsan gerçekten sınırı aşar."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":19,"id":"s096-p01-001-019","label":"Whole surah","number":1,"refs":["96:1","96:2","96:3","96:4","96:5","96:6","96:7","96:8","96:9","96:10","96:11","96:12","96:13","96:14","96:15","96:16","96:17","96:18","96:19"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:2:nasal-assertion","source_type":"word_analysis","support_id":"sup_01c3b7f3b6db6b06344d","text":"{\"blocking_evidence\":null,\"headline\":\"nasal sound binds particle and noun\",\"reader_payoff\":\"The reader hears the emphatic particle lean into the human noun it governs.\",\"reason\":\"The phonetic rows are surface-bound and reinforce the already licensed syntactic bond.\",\"representative_source_ids\":[\"QP-9ca5e0cb\",\"QP-b5f4bfae\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:2:particle-sequence","source_type":"word_analysis","support_id":"sup_06295f6cd9d11f34660b","text":"{\"blocking_evidence\":null,\"headline\":\"halt then assertion creates a two-beat turn\",\"reader_payoff\":\"The reader feels the move from {{ar:كَلَّا}} ({{tr:kallā}}) as halt to {{ar:إِنَّ}} ({{tr:inna}}) as formal judgment.\",\"reason\":\"The local sequence places the emphatic particle immediately after the deterrent particle and before the governed human noun.\",\"representative_source_ids\":[\"MT-5cba59c9\",\"QB-801a113a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:5:ongoing-aspect","source_type":"word_analysis","support_id":"sup_0cdfbf1a09029efbd74e","text":"{\"blocking_evidence\":null,\"headline\":\"imperfect aspect makes transgression characteristic\",\"reader_payoff\":\"The reader notices that the accusation is ongoing and characteristic rather than a single completed event.\",\"reason\":\"QAC and the verb instance identify the local form as imperfect active Form I.\",\"representative_source_ids\":[\"QG-ee73cd11\",\"MG-34639572\",\"QF-1da14546\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:5:visual-opposite-pole","source_type":"word_analysis","support_id":"sup_10f4f3191fde3236e958","text":"{\"blocking_evidence\":null,\"headline\":\"guided sight gives an opposite-pole contrast\",\"reader_payoff\":\"The reader sees the human overflow contrasted with a scene where sight does not cross bounds (53:17).\",\"reason\":\"The row gives a concrete contrast reference and does not claim that the local verb has a visual subject.\",\"representative_source_ids\":[\"QE-c2de88b5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"96:6:3:2","source_type":"qac_morpheme","support_id":"sup_11f60245dc602dc951ac","text":"{\"lemma_ar\":\"إِنسَٰن\",\"morph_features\":\"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"96:6:3:2\",\"qac_word_ref\":\"96:6:3\",\"root_ar\":\"ء ن س\",\"surface_ar\":\"إِنسَٰنَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:5:closure-landing","source_type":"word_analysis","support_id":"sup_1721c6321ce780ccad68","text":"{\"blocking_evidence\":null,\"headline\":\"final verb is the ayah's accusation point\",\"reader_payoff\":\"The reader notices that the whole clause funnels into the final accusation.\",\"reason\":\"The verb is the final word of the ayah and the predicate of the emphatic clause.\",\"representative_source_ids\":[\"QT-191c1588\",\"QB-26a24e8b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"96:6:4:2","source_type":"qac_morpheme","support_id":"sup_1a32e08a8c6798837f5c","text":"{\"lemma_ar\":\"طَغَىٰ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:TagaY`|ROOT:Tgy|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"96:6:4:2\",\"qac_word_ref\":\"96:6:4\",\"root_ar\":\"ط غ ي\",\"surface_ar\":\"يَطْغَىٰٓ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:1:confrontational-rebuke","source_type":"word_analysis","support_id":"sup_2e43304fd0654ae8bb76","text":"{\"blocking_evidence\":null,\"headline\":\"report becomes confrontational speech\",\"reader_payoff\":\"The reader feels the discourse register change from report to rebuke before the human is named.\",\"reason\":\"The particle's deterrent force and clause-initial position license the reported register shift.\",\"representative_source_ids\":[\"QB-f33c1107\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:4:inna-la-frame","source_type":"word_analysis","support_id":"sup_4e7b7672baf987187622","text":"{\"blocking_evidence\":null,\"headline\":\"second confirmer completes the frame\",\"reader_payoff\":\"The reader sees the middle particle lock the noun and verb into one delayed emphatic assertion.\",\"reason\":\"The local clause is syntactically forced as an {{ar:إِنَّ}} ({{tr:inna}}) construction whose predicate carries {{ar:لَـ}} ({{tr:la-}}).\",\"representative_source_ids\":[\"QI-eaf4fb29\",\"QT-f02760c9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:5:pharaonic-overreach","source_type":"word_analysis","support_id":"sup_4f346bc1b45d8277c15e","text":"{\"blocking_evidence\":null,\"headline\":\"Pharaoh-associated overreach becomes generic potential\",\"reader_payoff\":\"The reader hears the generic human diagnosis against the Pharaoh-associated overreach field (20:24; 79:17) and the imperfect warning parallel at 20:45.\",\"reason\":\"The cross-references are concrete and compatible with the local generic subject; they illuminate the root field without replacing the local human diagnosis.\",\"representative_source_ids\":[\"QI-dcc9a600\",\"QE-24095632\",\"ME-3bae0caf\",\"QH-006c8157\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:5:prior-teaching-reversal","source_type":"word_analysis","support_id":"sup_5197bd7d942a6dee31b0","text":"{\"blocking_evidence\":null,\"headline\":\"completed teaching meets ongoing excess\",\"reader_payoff\":\"The reader sees the prior gift of teaching in 96:5 reverse into ongoing boundary violation in 96:6.\",\"reason\":\"The local imperfect predicate follows the completed teaching scene identified in the CRITICAL boundary rows.\",\"representative_source_ids\":[\"QB-3dba2b24\",\"QB-8a9f075b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:3:singular-not-plural","source_type":"word_analysis","support_id":"sup_579f51d24b2358429d9c","text":"{\"blocking_evidence\":null,\"headline\":\"humanity is treated distributively as one subject\",\"reader_payoff\":\"The reader notices that the ayah does not scatter the diagnosis across plural cases but gathers humanity into one representative form.\",\"reason\":\"The local noun is singular and definite, while the contextual profile supports humans generic as the dominant referent class.\",\"representative_source_ids\":[\"QF-bda02dc7\",\"QF-ddc602da\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:3:nasal-binding","source_type":"word_analysis","support_id":"sup_63ec25d3dece750436ea","text":"{\"blocking_evidence\":null,\"headline\":\"sound carries the governed relation\",\"reader_payoff\":\"The reader hears the emphatic particle and human noun as a tightly joined unit.\",\"reason\":\"The sound observation is tied to adjacent surfaces that are also syntactically linked.\",\"representative_source_ids\":[\"QP-cdacda5f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:2:maximal-emphasis-frame","source_type":"word_analysis","support_id":"sup_66ca52ac7c9c5885cb54","text":"{\"blocking_evidence\":null,\"headline\":\"confirmation is doubled around the predicate\",\"reader_payoff\":\"The reader sees the claim strengthened by the full {{ar:إِنَّ ... لَـ}} ({{tr:inna ... la-}}) frame rather than by a single intensifier.\",\"reason\":\"Attachment translation support explicitly treats {{ar:إِنَّ}} ({{tr:inna}}) plus predicate {{ar:لَـ}} ({{tr:la-}}) as a combined emphatic construction.\",\"representative_source_ids\":[\"MG-23de040d\",\"QI-fb90a627\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:3:governed-human-center","source_type":"word_analysis","support_id":"sup_67066f4a58fb60ce0d11","text":"{\"blocking_evidence\":null,\"headline\":\"human noun is seized by the emphatic frame\",\"reader_payoff\":\"The reader notices that the human stands as the governed center between assertion particle and final verdict.\",\"reason\":\"QAC and attachment evidence mark the noun as accusative and governed by {{ar:إِنَّ}} ({{tr:inna}}).\",\"representative_source_ids\":[\"QG-1af8e26e\",\"QT-95237a4b\",\"MT-1c8dc9d5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:5:emphatic-verbal-predicate","source_type":"word_analysis","support_id":"sup_6b229b3d70125ae5afd0","text":"{\"blocking_evidence\":null,\"headline\":\"assertion lands on the final verb\",\"reader_payoff\":\"The reader sees the stacked emphatic frame resolve in the verb of transgression.\",\"reason\":\"The predicate is syntactically licensed as {{ar:لَيَطْغَىٰ}} ({{tr:la-yaṭghā}}), with {{ar:لَـ}} ({{tr:la-}}) confirming the verb under {{ar:إِنَّ}} ({{tr:inna}}).\",\"representative_source_ids\":[\"QG-f171f766\",\"QF-e1cc6715\",\"MF-a050780b\",\"QT-0f7d2d89\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:5:insan-pairing","source_type":"word_analysis","support_id":"sup_6e99fdbbeeb000083728","text":"{\"blocking_evidence\":null,\"headline\":\"human noun activates the excess pairing\",\"reader_payoff\":\"The reader sees {{ar:ط غ ي}} ({{tr:ṭ-gh-y}}) and the human noun paired locally against wider supplied co-occurrences (17:60; 10:11).\",\"reason\":\"The local syntax makes {{ar:ٱلْإِنسَٰنَ}} ({{tr:al-insāna}}) the subject of the verb, while the CRITICAL row supplies concrete co-occurrence references.\",\"representative_source_ids\":[\"QI-11371339\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:1:boundary-pivot","source_type":"word_analysis","support_id":"sup_737f48e9c55ee7c36f6f","text":"{\"blocking_evidence\":null,\"headline\":\"teaching scene turns into indictment\",\"reader_payoff\":\"The reader notices the ayah boundary pivot from divine teaching in 96:5 to public accusation in 96:6.\",\"reason\":\"The word opens a new clause after 96:5, and the following syntax supplies the accusatory diagnosis.\",\"representative_source_ids\":[\"QT-c4463178\",\"QB-00c47929\",\"QB-4a1741dc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:5:next-ayah-cause","source_type":"word_analysis","support_id":"sup_7879eaf1262a95308067","text":"{\"blocking_evidence\":null,\"headline\":\"complete accusation receives cause next\",\"reader_payoff\":\"The reader sees 96:6 stand as a complete accusation while 96:7 explains it through perceived self-sufficiency.\",\"reason\":\"The current clause is syntactically complete, and the CRITICAL rows supply the concrete next-ayah causal continuation at 96:7.\",\"representative_source_ids\":[\"QB-2a3c36c6\",\"QB-ce424844\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:5:evaluative-blame","source_type":"word_analysis","support_id":"sup_8803ab2fe6a604f79c1a","text":"{\"blocking_evidence\":null,\"headline\":\"the verb names blameworthy overreach\",\"reader_payoff\":\"The reader sees the action as morally charged overreach, not neutral expansion or energy.\",\"reason\":\"The accepted V4 branch includes overstepping in rebellion, matching the local human predicate.\",\"representative_source_ids\":[\"QS-cd5f2f72\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:5:derivational-overreach-field","source_type":"word_analysis","support_id":"sup_92f3d2d6e4bdf3479c01","text":"{\"blocking_evidence\":null,\"headline\":\"false-authority field deepens the overreach\",\"reader_payoff\":\"The reader senses the verb within a wider family of excess and false authority, while the local word remains the imperfect verb.\",\"reason\":\"V4 accepts the related false-authority branch for {{ar:ط غ ي}} ({{tr:ṭ-gh-y}}), but the local surface is not the noun of false authority.\",\"representative_source_ids\":[\"QS-f58b280e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:3:human-transgression-pairing","source_type":"word_analysis","support_id":"sup_943c87b70200fc53a39b","text":"{\"blocking_evidence\":null,\"headline\":\"human noun is paired with the excess root\",\"reader_payoff\":\"The reader notices the local pairing of the human noun with the transgression root against wider co-occurrence evidence (17:60; 10:11).\",\"reason\":\"The row supplies concrete references, and local syntax makes {{ar:ٱلْإِنسَٰنَ}} ({{tr:al-insāna}}) the subject of {{ar:لَيَطْغَىٰ}} ({{tr:la-yaṭghā}}).\",\"representative_source_ids\":[\"QI-6c509ff6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:3:same-surah-load-bearing","source_type":"word_analysis","support_id":"sup_96a410e3ff5eb50b1a05","text":"{\"blocking_evidence\":null,\"headline\":\"same noun carries the section's anthropology\",\"reader_payoff\":\"The reader sees the repeated noun carry the section from origin and teaching into crisis.\",\"reason\":\"The same-surah recurrence rows are concrete, and the local syntax makes the third occurrence the subject of the ayah's crisis predicate.\",\"representative_source_ids\":[\"QI-ee6fedc5\",\"ME-90c875cb\",\"QB-24d9f4cb\",\"QY-3d73aafb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:2","source_type":"word_analysis","support_id":"sup_987353aa41bb252de651","text":"{\"gloss_range\":\"emphatic annulling particle that governs the human noun and opens a confirmed diagnostic clause\",\"prose\":\"{{ar:إِنَّ}} ({{tr:inna}}) turns the halt into a governed assertion. It takes {{ar:ٱلْإِنسَٰنَ}} ({{tr:al-insāna}}) as its noun and scopes through the predicate {{ar:لَيَطْغَىٰ}} ({{tr:la-yaṭghā}}), so the ayah does not merely report human transgression but delivers it as confirmed diagnosis. Together with the later {{ar:لَ}} ({{tr:la-}}), it makes the claim press against resistance. Its doubled nasal onset also binds audibly into the following human noun, matching the tight grammar of the emphatic frame.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِنَّ}} ({{tr:inna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:5:converged-pressure-point","source_type":"word_analysis","support_id":"sup_afe3c5abd17eb284d0d9","text":"{\"blocking_evidence\":null,\"headline\":\"root image, aspect, and emphasis converge\",\"reader_payoff\":\"The reader sees the final word as the place where overflow imagery, ongoing aspect, and emphatic assertion meet.\",\"reason\":\"The convergence row is supported by local imperfect grammar, the {{ar:إِنَّ ... لَـ}} ({{tr:inna ... la-}}) frame, and accepted V4 root branches for overstepping and overflow.\",\"representative_source_ids\":[\"QY-15634db4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:1:audible-halt","source_type":"word_analysis","support_id":"sup_b392af20cb678bda1aa1","text":"{\"blocking_evidence\":null,\"headline\":\"sound shape makes the stop audible\",\"reader_payoff\":\"The reader hears the deterrent particle occupy space before the emphatic clause resumes.\",\"reason\":\"The sound observations are tied to the actual surface position and reinforce the word's stopping function.\",\"representative_source_ids\":[\"QF-7ecfab82\",\"QP-6189d382\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:4","source_type":"word_analysis","support_id":"sup_b53f0749ff4368a5e4b6","text":"{\"gloss_range\":\"emphatic predicate prefix that completes the {{ar:إِنَّ ... لَـ}} ({{tr:inna ... la-}}) confirmation frame\",\"prose\":\"{{ar:لَ}} ({{tr:la-}}) is the predicate-side confirmer. It carries no independent root meaning, but it hardens the final verb by completing the {{ar:إِنَّ ... لَـ}} ({{tr:inna ... la-}}) frame and making {{ar:لَيَطْغَىٰ}} ({{tr:la-yaṭghā}}) the clause's emphatic landing point. Because it is a bound prefix, the certainty is not floating beside the action; it is fused to the act of transgressing. Its short onset also pushes the recitation into the longer closing verb.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَ}} ({{tr:la-}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:1:surah-punctuation","source_type":"word_analysis","support_id":"sup_b675d64c929702c79958","text":"{\"blocking_evidence\":null,\"headline\":\"repeated stop marks surah escalation\",\"reader_payoff\":\"The reader notices that this stop belongs to a larger warning register, including later same-surah stops at 96:15 and 96:19.\",\"reason\":\"The recurrence claim is concrete for Surah 96, and the Meccan-register observation has no contrary local evidence.\",\"representative_source_ids\":[\"MT-daa41d28\",\"MS-ca6e3b49\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:5:extended-final-sound","source_type":"word_analysis","support_id":"sup_b88d0a7f47e817cd31ee","text":"{\"blocking_evidence\":null,\"headline\":\"long final sound stretches the verdict\",\"reader_payoff\":\"The reader hears the act of overstepping close on an extended, heavy sound rather than a clipped ending.\",\"reason\":\"The phonetic rows are tied to the final surface form and reinforce the semantic pressure of the closing predicate.\",\"representative_source_ids\":[\"QF-12f8b100\",\"QP-4fffa895\",\"QP-83beebba\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:5:moral-overflow-root","source_type":"word_analysis","support_id":"sup_c146d44c468baa918eb6","text":"{\"blocking_evidence\":null,\"headline\":\"overflow image becomes moral overstepping\",\"reader_payoff\":\"The reader feels transgression as a force spilling beyond containment, while the local frame keeps the sense moral rather than literal floodwater.\",\"reason\":\"V4 accepts both rebellion and overflow branches for {{ar:ط غ ي}} ({{tr:ṭ-gh-y}}), but the human intransitive predicate selects overstepping in conduct while retaining overflow as source-image pressure.\",\"representative_source_ids\":[\"QS-06b45118\",\"QS-28646d93\",\"QS-5ed3a181\",\"MS-7f938279\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:1:emphasis-launch","source_type":"word_analysis","support_id":"sup_c3c048422ba61c412524","text":"{\"blocking_evidence\":null,\"headline\":\"opening resistance prepares stacked assertion\",\"reader_payoff\":\"The reader sees the first word prepare the later {{ar:إِنَّ}} ({{tr:inna}}) and {{ar:لَـ}} ({{tr:la-}}) as a contested, forceful assertion.\",\"reason\":\"The attachment evidence reads words 2-5 as an emphatic clause, and the CRITICAL rows correctly place the opening particle before that assertion frame.\",\"representative_source_ids\":[\"QI-a940fe42\",\"QT-63cccf5e\",\"QY-f6152da0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:1:deterrent-alert","source_type":"word_analysis","support_id":"sup_c4de3511d22612335cd5","text":"{\"blocking_evidence\":null,\"headline\":\"deterrence and alerting work together\",\"reader_payoff\":\"The reader notices that the ayah begins with a rebuking halt and an alert to the diagnosis, not with a neutral transition.\",\"reason\":\"QAC identifies {{ar:كَلَّا}} ({{tr:kallā}}) as a deterrent or response particle with retrospective and prospective functions, so the older debate is retained as a live range rather than reduced to only one option.\",\"representative_source_ids\":[\"QG-f2a945eb\",\"MG-399e64a1\",\"QS-a31d5feb\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:4:compact-cadence","source_type":"word_analysis","support_id":"sup_cc367ea5f8ccbb97c3f6","text":"{\"blocking_evidence\":null,\"headline\":\"short onset pushes into the closing verb\",\"reader_payoff\":\"The reader hears a clipped confirmation before the long final predicate arrives.\",\"reason\":\"The cadence row is tied to the actual short particle before the longer final verb.\",\"representative_source_ids\":[\"QP-a61f3ec0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:3:negative-diagnosis-formula","source_type":"word_analysis","support_id":"sup_cc9d607ceb3843ebd7b5","text":"{\"blocking_evidence\":null,\"headline\":\"formula joins adverse human diagnoses\",\"reader_payoff\":\"The reader hears 96:6 as part of a recognized {{ar:إِنَّ ٱلْإِنسَٰنَ}} ({{tr:inna al-insāna}}) diagnosis pattern rather than an isolated accusation.\",\"reason\":\"The cited parallels are concrete and compatible with the local emphatic generic-human construction (70:19; 100:6; 103:2).\",\"representative_source_ids\":[\"MS-49c3f23d\",\"QI-6c6caa02\",\"QE-05c58efc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:4:fused-prefix","source_type":"word_analysis","support_id":"sup_cfbbff72719d50861672","text":"{\"blocking_evidence\":null,\"headline\":\"certainty is fused to the action\",\"reader_payoff\":\"The reader sees the emphatic force attached directly to the verb of transgression.\",\"reason\":\"The surface is a bound proclitic before the verb, and the verb instance is the predicate.\",\"representative_source_ids\":[\"QF-dab6f3ac\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:3:recipient-to-agent","source_type":"word_analysis","support_id":"sup_cfc3f7e660ea1ecfe535","text":"{\"blocking_evidence\":null,\"headline\":\"created and taught human becomes transgressing agent\",\"reader_payoff\":\"The reader tracks the same noun from creation at 96:2 through teaching at 96:5 into transgression at 96:6.\",\"reason\":\"The same surface noun recurs in the opening section, and the local clause changes its role into the subject of the transgression predicate.\",\"representative_source_ids\":[\"QS-e887a0b2\",\"QT-55481724\",\"QE-4b7535c1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:5:objectless-transgression","source_type":"word_analysis","support_id":"sup_d187495fe26fe41f5a02","text":"{\"blocking_evidence\":null,\"headline\":\"no object leaves the crossing unlocalized\",\"reader_payoff\":\"The reader notices that the Arabic states transgression without naming a specific object or victim.\",\"reason\":\"The verb instance marks the frame as intransitive with no explicit object, so the row's absolute language is retained as unlocalized scope rather than expanded into every possible target.\",\"representative_source_ids\":[\"MT-268fc41f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:1","source_type":"word_analysis","support_id":"sup_d63d1618bce55e719494","text":"{\"gloss_range\":\"deterrent and alerting response particle that halts the prior movement and opens an emphatic diagnosis\",\"prose\":\"{{ar:كَلَّا}} ({{tr:kallā}}) opens the ayah as a stop before it becomes a statement. Its force is not merely to decorate the sentence: it restrains or rebukes the prior flow, can already face the self-sufficiency named in 96:7, and alerts the reader to the emphatic diagnosis that follows in {{ar:إِنَّ ... لَيَطْغَىٰ}} ({{tr:inna ... la-yaṭghā}}). That makes 96:6 a staged interruption after the creation and teaching movement of 96:1-5, where the human who has received instruction is now brought under accusation. The long final sound and tightened doubled consonant make the halt audible, while the same particle's recurrence at 96:15 and 96:19 marks later escalations in the surah and its wider Meccan confrontational register.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:كَلَّا}} ({{tr:kallā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:4:predicate-emphasis-scope","source_type":"word_analysis","support_id":"sup_db1b0bac0b19f2209443","text":"{\"blocking_evidence\":null,\"headline\":\"predicate-side lām confirms the verdict\",\"reader_payoff\":\"The reader notices that the certainty lands on the predicate, not merely on the earlier human noun.\",\"reason\":\"QAC identifies the prefix as emphatic {{ar:لَـ}} ({{tr:la-}}), and attachment evidence treats it as confirming the predicate of {{ar:إِنَّ}} ({{tr:inna}}).\",\"representative_source_ids\":[\"QG-09cd63bd\",\"QS-10bbe51e\",\"QT-7bc6e91f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:3","source_type":"word_analysis","support_id":"sup_e1ee47f5957a3a0bf935","text":"{\"gloss_range\":\"the human being as a generic species noun, grammatically governed inside the emphatic clause\",\"prose\":\"{{ar:ٱلْإِنسَٰنَ}} ({{tr:al-insāna}}) is the governed noun of {{ar:إِنَّ}} ({{tr:inna}}), so the human is grammatically held inside the emphatic assertion before being accused by the final verb. Its definite singular form is generic: the ayah speaks of the human being as a category, compressed into one representative subject whose verb also appears singular. This same noun has already carried the opening movement at 96:2 and 96:5, so 96:6 turns the created and taught being into the agent of ongoing excess. The root field can suggest sociability, awareness, and a disputed shadow of forgetfulness, which sharpens the irony, but the local grammar selects the species noun rather than an etymological definition. The phrase also joins a wider negative-diagnosis pattern with {{ar:إِنَّ ٱلْإِنسَٰنَ}} ({{tr:inna al-insāna}}) in 70:19, 100:6, and 103:2, while the local pairing with {{ar:لَيَطْغَىٰ}} ({{tr:la-yaṭghā}}) makes that diagnosis transgression.\",\"root_display\":\"{{ar:أ ن س}} ({{tr:ʾ-n-s}})\",\"root_gloss_range\":\"human social and perceptive being; disputed links with forgetfulness remain interpretive pressure, while the local noun selects the generic human category\",\"surface_display\":\"{{ar:ٱلْإِنسَٰنَ}} ({{tr:al-insāna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:5:marked-imperfect-selection","source_type":"word_analysis","support_id":"sup_e4714253fd414d8eab9d","text":"{\"blocking_evidence\":null,\"headline\":\"rare imperfect form is deliberately selected\",\"reader_payoff\":\"The reader notices that the ayah chooses the sparse ongoing verb form rather than the broader noun-heavy or perfect distribution.\",\"reason\":\"The contextual profile marks the exact root-form as low occurrence, and the local verb instance confirms the imperfect form.\",\"representative_source_ids\":[\"QI-37ed4a5c\",\"QI-cfd6687d\",\"QH-a8450f9b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:3:etymology-irony","source_type":"word_analysis","support_id":"sup_e5c6c00f3debb2aae2d9","text":"{\"blocking_evidence\":null,\"headline\":\"sociability and forgetfulness sharpen the irony\",\"reader_payoff\":\"The reader senses irony in the socially aware human being becoming the transgressor, while the grammar still selects the ordinary human noun.\",\"reason\":\"No V4 guardrail rows are available for {{ar:أ ن س}} ({{tr:ʾ-n-s}}), so the valid etymological pressure may survive, but it must not replace the local generic noun sense.\",\"representative_source_ids\":[\"QS-4abcb075\",\"QS-8c049568\",\"MI-267a51b5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:5","source_type":"word_analysis","support_id":"sup_ead8b6a1109fb266e131","text":"{\"gloss_range\":\"ongoing or characteristic overstepping of bounds in rebellion; the local human subject selects moral transgression while overflow imagery remains active as pressure\",\"prose\":\"{{ar:يَطْغَىٰٓ}} ({{tr:yaṭghā}}) is the ayah's closing verdict. As an imperfect Form I verb, it presents transgression as ongoing or characteristic, not as one completed lapse, and the supplied distribution makes this sparse ongoing form stand out against broader perfect and noun forms. The subject is the singular generic {{ar:ٱلْإِنسَٰنَ}} ({{tr:al-insāna}}), so humanity is diagnosed through one representative actor, and the attached {{ar:لَ}} ({{tr:la-}}) makes the emphatic force land directly on the verb. Lexically, {{ar:ط غ ي}} ({{tr:ṭ-gh-y}}) selects overstepping bounds in rebellion here: the intransitive human frame names no explicit object and rules out a literal flood event, but the accepted overflow image still makes moral excess feel like force spilling past containment, with the flood reference at 69:11 as a concrete source-domain echo. The wider family of excess and false authority deepens the overreach without replacing the local imperfect verb. The verb also stands against the Pharaoh-associated field of overreach (20:24; 79:17), while 20:45 is the other supplied imperfect parallel and 53:17 gives the opposite picture of sight not crossing bounds. After the completed teaching of 96:5, the word closes 96:6 on an extended and heavy-sounding accusation, yet 96:7 immediately supplies the causal perception of self-sufficiency.\",\"root_display\":\"{{ar:ط غ ي}} ({{tr:ṭ-gh-y}})\",\"root_gloss_range\":\"overstepping bounds, rebellion, excess, overflow, false authority, and overwhelming force; local grammar selects the intransitive human overstepping branch and narrows physical overflow to source-image pressure\",\"surface_display\":\"{{ar:يَطْغَىٰٓ}} ({{tr:yaṭghā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:3:generic-singular-species","source_type":"word_analysis","support_id":"sup_eb9917a78993eeb0bb51","text":"{\"blocking_evidence\":null,\"headline\":\"singular definite carries species force\",\"reader_payoff\":\"The reader sees a species-wide diagnosis compressed into one singular grammatical subject.\",\"reason\":\"QAC explicitly describes the definite article as generic and the verb agreement as third masculine singular controlled by the noun.\",\"representative_source_ids\":[\"QG-95f36e18\",\"QG-fde8aa77\",\"QS-f1841f00\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:2:governed-diagnostic-clause","source_type":"word_analysis","support_id":"sup_ef849c36075d9e575def","text":"{\"blocking_evidence\":null,\"headline\":\"emphatic particle governs the diagnosis\",\"reader_payoff\":\"The reader notices that human transgression is placed inside a governed emphatic clause, not stated as a loose verbal report.\",\"reason\":\"QAC and attachment evidence identify {{ar:إِنَّ}} ({{tr:inna}}) as governing the noun and opening the clause whose predicate is {{ar:لَيَطْغَىٰ}} ({{tr:la-yaṭghā}}).\",\"representative_source_ids\":[\"QG-9012ded2\",\"QS-e9f51ed2\",\"QT-666773fa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:6:5:generic-singular-actor","source_type":"word_analysis","support_id":"sup_f9d27c76f4f8ea56d70a","text":"{\"blocking_evidence\":null,\"headline\":\"generic humanity acts as one subject\",\"reader_payoff\":\"The reader notices that a species-wide claim is grammatically concentrated into one singular actor.\",\"reason\":\"The verb is third masculine singular and its implicit subject is syntactically controlled by the generic noun.\",\"representative_source_ids\":[\"QG-f8d58042\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ","ayah_ref":"96:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000059/B001","root_000937/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000059","role":"Visible human presence supplies a public, socially consequential subject rather than an abstract impulse.","root":"ء ن س","source_ref":"96:6","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000937","role":"Overstepping a bound in rebellion supplies the sentence's core motion and makes the human an active boundary-crosser.","root":"ط غ ي","source_ref":"96:6","source_word_indices":["4"]}],"changed_reading":{"after":"The publicly present human becomes a boundary-crossing agent: transgression is movement past an operative limit, not merely a bad inner state.","before":"The human rebels or behaves excessively."},"confidence":"strong","focus_anchor":"The human at word 3 is the emphatically marked subject of the bound-crossing verb at word 4.","mechanism":"Visible human agency encounters an operative limit and moves beyond it; the sentence compresses subject, boundary, and breach into a recurring human tendency.","model_id":"b01_human_bound_crosser"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b01_human_bound_crosser","source_type":"hft","support_id":"sup_4edd506a257f99282c67","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ","ayah_ref":"96:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000059/B001","root_000937/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000059","role":"Visible human presence gives the overflow a concrete social carrier and field of effects.","root":"ء ن س","source_ref":"96:6","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000937","role":"Rising, engulfing force supplies a hydraulic mechanism in which human capacity becomes pressure beyond measure.","root":"ط غ ي","source_ref":"96:6","source_word_indices":["4"]}],"changed_reading":{"after":"Human force rises past its containing measure and begins to engulf its surroundings.","before":"The human commits too much wrongdoing."},"confidence":"medium","focus_anchor":"The same subject-predicate link between words 3 and 4 permits the material overflow branch of the verb to organize the clause.","mechanism":"Human presence behaves like a rising force that exceeds its container and then overwhelms what surrounds it. Moral excess is rendered as a change in pressure and capacity.","model_id":"b02_human_overflow"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b02_human_overflow","source_type":"hft","support_id":"sup_bf02d9b8e9643d6719e4","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ","ayah_ref":"96:6"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000059/B003","root_000937/B001"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000059","role":"Comfort that removes estrangement supplies the low-friction interior in which vigilance toward limits can lapse.","root":"ء ن س","source_ref":"96:6","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000937","role":"Rebellious boundary-crossing supplies the consequential movement that familiarity alone cannot explain.","root":"ط غ ي","source_ref":"96:6","source_word_indices":["4"]}],"changed_reading":{"after":"Overstepping may arise precisely when familiarity and comfort make the human feel that no boundary remains dangerous.","before":"Estrangement from what is right produces rebellion."},"confidence":"exploratory","focus_anchor":"The noun at word 3 can activate familiar comfort while the verb at word 4 still anchors the result as actual overstepping.","mechanism":"Familiarity removes estrangement and can also remove caution. The human oversteps from inside a sphere made safe and ordinary, so transgression incubates in comfort rather than only in hostility.","model_id":"b03_familiarity_disarms_limits"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b03_familiarity_disarms_limits","source_type":"hft","support_id":"sup_5588a2cd2cacf5478919","trust":"legacy_unbound"}]}
</lane_packet_json>
