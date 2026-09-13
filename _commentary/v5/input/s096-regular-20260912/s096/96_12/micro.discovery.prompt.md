# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **96:12**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s096-regular-20260912/s096/96_12/micro.discovery.json` and modify nothing
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
  "ayah_ref": "96:12",
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
{"branch_registry":[{"boundary":"Çıplak ad olarak durum ve konu alanıdır; buyruk, yöneticilik, bolluk ve belirti anlamları dışarıda kalır.","branch_kind":"bare","branch_ref":"root_000051/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَمَرَ","morph_features":"STEM|POS:V|PERF|LEM:>amara|ROOT:Amr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:12:2:1","qac_word_ref":"96:12:2","surface_ar":"أَمَرَ"}],"gloss":"konu ve hal","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Anlamın çekirdeği, insan işleri arasında tek tek sayılabilen konu, hal veya durumdur."}}],"root_ar":"ء م ر","root_id":"root_000051","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çıplak biçim bir olayın, kişinin veya topluluğun ele alınan durumu ya da işi olduğunda kullanılır.","boundary_detail":"Çıplak ad olarak durum ve konu alanıdır; buyruk, yöneticilik, bolluk ve belirti anlamları dışarıda kalır.","branch_image_ar":"الشأن والحال","concept_gloss":"konu ve hal","contextual_glosses":[{"applicability":"Bir kişinin veya şeyin içinde bulunduğu hali anlatan bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tekil konu veya iş olma yönünü her bağlamda açık taşımaz.","preserves":"Hal ve vaziyet yönünü korur."},"facet_ids":["F001"],"text":"durum","usage_role":"contextual"},{"applicability":"Bir kimsenin ele alınan meselesi veya yürüyen konusu kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hal ve genel durum genişliğini daraltır.","preserves":"Ele alınan tekil konu yönünü korur."},"facet_ids":["F001"],"text":"iş","usage_role":"contextual"}],"definition":"Bir kişinin, topluluğun veya durumun konusu, hali ya da ele alınan tekil işi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Anlamın çekirdeği, insan işleri arasında tek tek sayılabilen konu, hal veya durumdur."}],"identity_rationale":"Kaynak ifadesi bu dalda kelimeyi bir durum, konu, hal veya insanlar arasindaki tekil is olarak verir. Geçici çerçeve bu çıplak anlamı doğru yakalar ve buyruk, yöneticilik, bolluk ya da belirti anlamlarını bu dala karıştırmaz.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"konu, hal veya tekil iş"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"konular, haller ve işler"}],"lexicalization_note":"Mekanik tür bare olduğu için tanım yalnız çıplak biçimin durum, hal ve konu anlamını verir.","neighbor_coverage_note":"Adayların tamamı sınır için gözden geçirildi; yalnız aynı kökten okuyucu karışıklığı doğuran yakın alanlar yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal ele alınan şeyin ne olduğunu söyler; komşu dal ise birinin başka birine yönelttiği yapma yükümlülüğünü anlatır.","focus_only":"Bir durumun veya konunun kendisini adlandırır.","gloss":"konu ile buyruk","neighbor_only":"Birine bir eylemi yapmasını bildiren bağlayıcı isteği anlatır.","neighbor_ref":"root_000051/B002","relation_type":"same_field","shared_zone":"İkisi de insan işleri ve yapılacak şeyler alanında karışabilir."},{"boundary_match":"field_only","distinction":"Bu dal yetki sahibi kişiyi değil, söz konusu edilen hali veya işi adlandırır; komşu dalda ise makam ve yönetme yetkisi çekirdektir.","focus_only":"Konu veya hal olarak kalan tekil işi anlatır.","gloss":"konu ile yönetim","neighbor_only":"Yönetme yetkisini, yöneticiyi veya birini yönetici yapmayı anlatır.","neighbor_ref":"root_000051/B003","relation_type":"same_field","shared_zone":"İkisi de bir iş üzerinde yetki veya düzen fikriyle birlikte geçebilir."},{"boundary_match":"field_only","distinction":"Bu dal işaret edilen konunun kendisine gider; komşu dal ise tanıtmaya veya zamanı göstermeye yarayan belirtiyi anlatır.","focus_only":"Ele alınan durum veya konudur.","gloss":"konu ile belirti","neighbor_only":"Bir şeyi tanıtan belirti, yol işareti ya da belirlenmiş zamandır.","neighbor_ref":"root_000051/B005","relation_type":"same_field","shared_zone":"Bir konuya ait tanıtıcı işaretler aynı söylemde bulunabilir."}],"source_phrase_ar":"الأمر من الأمور، الواحد من الأمور (maqayis)؛ الأمر واحد من أمور الناس (ayn)؛ الأمر واحد الأمور (sihah;tahdhib)؛ الأمر الشأن وجمعه أمور (mufradat)","source_summary":"Kaynaklar bu dalı ortak biçimde bir konu, hal ya da tekil iş anlamı olarak verir; çoğul kullanım da aynı alanın çoklu hallerini anlatır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الأمر بمعنى الشأن والحال والقضية العامة، وواحد الأمور، وما يرجع إلى جهة ما من شأن.","what_is_not_ar":"ليس طلب الفعل، ولا الولاية، ولا الكثرة والبركة، ولا العلامة."},"support_links":[]},{"boundary":"Çekirdek bir eylemi yaptırma isteğidir; genel konu, makam ve danışma bu dala dahil değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000051/B002","candidate_links":[{"candidate_id":"cand_83310c9496c9a84accae","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَمَرَ","morph_features":"STEM|POS:V|PERF|LEM:>amara|ROOT:Amr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:12:2:1","qac_word_ref":"96:12:2","surface_ar":"أَمَرَ"}],"gloss":"buyrukla yükümlü kılma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek anlam, yasaklamanın karşıtı olan yapma isteği ve yükümlü kılmadır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bazı biçimler bu isteğin söz dizisindeki kullanımını veya bir kez uyulacak özel yükümlülüğü gösterir."}}],"root_ar":"ء م ر","root_id":"root_000051","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiye belirli bir eylemi yapması yönünde bağlayıcı söz yöneltildiğinde uygundur.","boundary_detail":"Çekirdek bir eylemi yaptırma isteğidir; genel konu, makam ve danışma bu dala dahil değildir.","branch_image_ar":"الطلب والإلزام","concept_gloss":"buyrukla yükümlü kılma","contextual_glosses":[{"applicability":"Söz veya karar olarak eylem yapma yükümlülüğü bildirildiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yapma isteği ve bağlayıcı söz yönünü korur."},"facet_ids":["F001"],"text":"buyruk","usage_role":"general"},{"applicability":"Fiil olarak bir muhataptan belirli bir işi yapması isteniyorsa uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yükümlülüğün resmi veya bağlayıcı gücünü zayıflatabilir.","preserves":"Muhataba yönelen yapma isteğini korur."},"facet_ids":["F001"],"text":"yapmasını istemek","usage_role":"contextual"}],"definition":"Birine belirli bir eylemi yapmasını bildiren ve onu o eylemle yükümlü kılan söz ya da isteme eylemi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek anlam, yasaklamanın karşıtı olan yapma isteği ve yükümlü kılmadır."},{"facet_id":"F002","role":"associated_use","statement":"Bazı biçimler bu isteğin söz dizisindeki kullanımını veya bir kez uyulacak özel yükümlülüğü gösterir."}],"identity_rationale":"Kaynak ifadesi bu dalı yasaklamanın karşıtı olan yapma isteği, yükümlü kılma ve bu isteğin söz kalıbı olarak tanımlar. Geçici çerçeve çıplak ve yapı içi kullanımları birlikte tutar, fakat anlamı genel konuya veya yöneticiliğe genişletmez.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yapma buyruğu ve yükümlü kılma"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"ona bir şeyi yapmasını buyurdum"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"buyurma fiilinin söz içindeki biçimi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"uyulacak tek bir buyruk hakkı"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"iyiliği çokça buyuran"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"onlara uymaları buyruldu, onlar da karşı geldi"}],"lexicalization_note":"Mekanik tür mixed_non_bare olduğu için çıplak buyruk anlamı ile özel kalıp kullanımları ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlananlar buyruk anlamını konu, makam ve yükleme alanlarından ayıran en gerekli sınırlar oldu.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal bir muhataba yöneltilen yapma yükümlülüğünü anlatır; komşu dalda ise böyle bir isteme ilişkisi bulunmadan konunun kendisi anlatılır.","focus_only":"Bir eylemi yaptıran söz ve yükümlülük vardır.","gloss":"buyruk ile konu","neighbor_only":"Yaptırma sözü olmadan konu, hal veya iş adlandırılır.","neighbor_ref":"root_000051/B001","relation_type":"same_field","shared_zone":"Her ikisi de bir iş veya mesele çevresinde kullanılabilir."},{"boundary_match":"field_only","distinction":"Bu dal söylenen yapma yükümlülüğünü tanımlar; komşu dal bu yükümlülüğü verme yetkisine sahip makam veya kişiye odaklanır.","focus_only":"Sözle eylem yükümlülüğü getirme çekirdektir.","gloss":"buyruk ile yönetim","neighbor_only":"Makam, yönetici ve yönetme yetkisi çekirdektir.","neighbor_ref":"root_000051/B003","relation_type":"same_field","shared_zone":"Yönetici buyruk verebilir, fakat iki dal aynı anlam değildir."},{"boundary_match":"field_only","distinction":"Bu dal muhataba bağlayıcı yapma isteği yöneltir; komşu dal ise görüş alma, tartma ve karar oluşturma sürecidir.","focus_only":"Bir muhataba eylem yapma yükümlülüğü bildirilir.","gloss":"buyruk ile danışma","neighbor_only":"Bir iş hakkında görüş alışverişi yapıp görüşe varma süreci anlatılır.","neighbor_ref":"root_000051/B007","relation_type":"same_field","shared_zone":"İkisi de bir iş hakkında söz söyleme ve yön verme alanında buluşur."}],"source_phrase_ar":"الأمر الذي هو نقيض النهي قولك افعل كذا (maqayis)؛ الأمر نقيض النهي وإذا أمرت من الأمر قلت اؤمر (ayn)؛ أمرته بكذا أمرا والجمع الأوامر (sihah)؛ الأمر معروف نقيض النهي (tahdhib)؛ مصدر أمرته إذا كلفته أن يفعل شيئا، والتقدم بالشيء (mufradat)","source_summary":"Kaynaklar ortak olarak bu anlamı yasaklamanın karşıtı olan eylem buyurma ve birini bir şeyi yapmakla yükümlü kılma alanında toplar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الأمر المضاد للنهي، والتكليف بالفعل، وصيغ الطلب مثل مر وأمر، وامتثال الأمر.","what_is_not_ar":"ليس مطلق الشأن، ولا منصب الإمارة، ولا التشاور إلا من جهة اشتقاقه من قبول الأمر."},"support_links":["sup_933237a2713c380338f8"]},{"boundary":"Yönetme yetkisi, yönetici kişi ve yönetime getirme bu daldadır; sırf buyruk sözü değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000051/B003","candidate_links":[{"candidate_id":"cand_b7506fac0ab2231cc020","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَمَرَ","morph_features":"STEM|POS:V|PERF|LEM:>amara|ROOT:Amr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:12:2:1","qac_word_ref":"96:12:2","surface_ar":"أَمَرَ"}],"gloss":"yönetme yetkisi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek anlam, yönetme yetkisi ve bu yetkiye bağlı makamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yetkiyi taşıyan kişi ve birini o konuma getirme kullanımları aynı alanın özel gerçekleşmeleridir."}}],"root_ar":"ء م ر","root_id":"root_000051","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Makam, yönetici kişi veya göreve getirme anlamları yetki çekirdeğiyle birlikte söz konusu olduğunda uygundur.","boundary_detail":"Yönetme yetkisi, yönetici kişi ve yönetime getirme bu daldadır; sırf buyruk sözü değildir.","branch_image_ar":"الولاية وصاحب السلطان","concept_gloss":"yönetme yetkisi","contextual_glosses":[{"applicability":"Makam veya görev alanı kastedildiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Makam sahibinin adı ve göreve getirme fiili açık kalmayabilir.","preserves":"Yönetme makamını korur."},"facet_ids":["F001"],"text":"yöneticilik","usage_role":"contextual"},{"applicability":"Yetkiyi taşıyan kişi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Makam ve göreve getirme anlamlarını dışarıda bırakır.","preserves":"Yetki sahibi kişi yönünü korur."},"facet_ids":["F002"],"text":"yönetici","usage_role":"contextual"}],"definition":"Bir topluluk veya iş üzerinde yönetme yetkisi, bu yetkiyi taşıyan kişi ya da birini böyle bir konuma getirme eylemi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek anlam, yönetme yetkisi ve bu yetkiye bağlı makamdır."},{"facet_id":"F002","role":"specialization","statement":"Yetkiyi taşıyan kişi ve birini o konuma getirme kullanımları aynı alanın özel gerçekleşmeleridir."}],"identity_rationale":"Kaynak ifadesi yönetme makamını, bu makama sahip kişiyi ve birini o makama getirmeyi birlikte verir. Geçici çerçeve bu yetki alanını doğru korur ve sırf buyruk sözü ya da genel konu anlamıyla karıştırmaz.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yönetme makamı ve yetkisi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yetkili yönetici"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yönetici kılınmış kimse"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"onu yönetici yaptım"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"topluluğunun yöneticisi oldu"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yetki sahipleri"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"onları yönetici kıldık"}],"lexicalization_note":"Mekanik tür mixed_non_bare olduğu için makam, kişi ve göreve getirme kullanımları tek yetki alanı içinde ayrıştırılır.","neighbor_coverage_note":"Adaylar içinde yönetim yetkisini en çok karıştırabilecek makam, egemenlik ve buyruk alanları seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal özellikle yöneticilik ve o makama getirme etrafında durur; komşu dal daha geniş biçimde bir işi üstlenip gözetme veya yanında olma yetkisini de kapsar.","focus_only":"Bu kökte makam adı, makam sahibi ve göreve getirme aynı söz ailesi içinde belirtilir.","gloss":"yönetme yetkisi","neighbor_only":"Komşu dal yetimi veya kadını gözetme gibi bakım ve yakınlıkla yürüyen yetkileri de kapsar.","neighbor_ref":"root_001684/B003","relation_type":"near_synonym","shared_zone":"İkisi de bir iş veya topluluk üzerinde yetki kullanma alanını paylaşır."},{"boundary_match":"partial","distinction":"Bu dal görev ve yönetici yetkisini anlatır; komşu dal egemenlik ve krallık derecesindeki sahiplik ve güç alanına çıkar.","focus_only":"Yönetim makamına sahip olma veya o makama getirilme öndedir.","gloss":"yönetim ile egemenlik","neighbor_only":"Krallık, egemenlik ve üstün mülk alanı daha yüksek siyasal güç bildirir.","neighbor_ref":"root_001444/B003","relation_type":"near_neighbor","shared_zone":"İkisi de yönetme gücü ve toplumsal üstünlük alanında buluşur."},{"boundary_match":"field_only","distinction":"Bu dal buyruk verme yetkisini taşıyan makam veya kişiyi tanımlar; komşu dal o yetkinin ürettiği bağlayıcı sözü tanımlar.","focus_only":"Yetkiyi taşıyan makam veya kişi çekirdektir.","gloss":"yönetim ile buyruk","neighbor_only":"Bir eylemi yapma buyruğu çekirdektir.","neighbor_ref":"root_000051/B002","relation_type":"same_field","shared_zone":"Yönetici buyruk verebilir, bu yüzden alanlar temas eder."}],"source_phrase_ar":"الإمرة والإمارة وصاحبها أمير ومؤمر (maqayis)؛ الإمرة الإمارة وهو أمير مؤمر (ayn)؛ الأمير ذو الأمر والتأمير تولية الامارة (sihah)؛ أمر الرجل إمارة إذا صار عليهم أميرا (tahdhib)؛ أولي الأمر عنى الأمراء، وقرئ أمرنا أي جعلناهم أمراء (mufradat)","source_summary":"Kaynaklar bu dalda yönetim makamı, makam sahibi ve bir kimseyi yönetici yapma anlamlarını aynı yetki çekirdeğine bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الإمرة والإمارة والولاية، والأمير والمؤمر، وتولية شخص أميرا أو تسلطه.","what_is_not_ar":"ليس مجرد طلب الفعل في خطاب، ولا الشأن العام، ولا الكثرة."},"support_links":["sup_9be606ce16bec1a0a739"]},{"boundary":"Çekirdek bolluk ve verimli çoğalmadır; makam, buyruk ve işaret anlamları dışarıda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000051/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَمَرَ","morph_features":"STEM|POS:V|PERF|LEM:>amara|ROOT:Amr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:12:2:1","qac_word_ref":"96:12:2","surface_ar":"أَمَرَ"}],"gloss":"bereketli çoğalma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek anlam, sayıca veya varlıkça artma ve çoğalmadır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Artış, mal, soy, doğurganlık ve uğurluluk bağlamlarında verimli bereket olarak genişler."}}],"root_ar":"ء م ر","root_id":"root_000051","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Artış, çoğalış, mal veya nesilde verimlilik ve uğurluluk birlikte düşünüldüğünde uygundur.","boundary_detail":"Çekirdek bolluk ve verimli çoğalmadır; makam, buyruk ve işaret anlamları dışarıda kalır.","branch_image_ar":"النماء والبركة","concept_gloss":"bereketli çoğalma","contextual_glosses":[{"applicability":"Kişi, topluluk, mal veya neslin sayıca arttığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uğur ve bereket değerini açık taşımaz.","preserves":"Artış ve çoğalma yönünü korur."},"facet_ids":["F001"],"text":"çoğalmak","usage_role":"contextual"},{"applicability":"Kişi veya hayvanın mal, nesil ya da kazanç getirmesi anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Düz sayısal çoğalmayı her bağlamda açık belirtmez.","preserves":"Verimli uğurluluk yönünü korur."},"facet_ids":["F002"],"text":"uğurlu ve verimli","usage_role":"contextual"}],"definition":"Bir şeyin, malın, topluluğun veya neslin artması; artışın uğur ve verimlilik olarak görülmesi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek anlam, sayıca veya varlıkça artma ve çoğalmadır."},{"facet_id":"F002","role":"extension","statement":"Artış, mal, soy, doğurganlık ve uğurluluk bağlamlarında verimli bereket olarak genişler."}],"identity_rationale":"Kaynak ifadesi artma, çoğalma, bereket ve uğurlu çoğalış alanını birlikte verir. Geçici çerçeve bu büyüme çekirdeğini doğru taşır ve yönetim, buyruk veya belirti anlamlarına geçmez.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"artış, verim ve bereket"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"çoğaldı ve büyüdü"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"topluluk çoğaldı, malları veya nimetleri arttı"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"uğurlu, bereket getiren kişi"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"çok yavrulayan ve bereketli kısrak"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"Tanrı onun malını çoğalttı"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"onları veya varlıklılarını çoğalttık"}],"lexicalization_note":"Mekanik tür mixed_non_bare olduğu için genel çoğalma ile belirli kişi, mal ve hayvan kalıpları ayrı gösterilir.","neighbor_coverage_note":"Adaylar artış, bereket ve nesil alanına göre değerlendirildi; yalnız anlam sınırını gerçekten keskinleştirenler yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal çoğalma ve verimli artıştan hareket eder; komşu dal bereketi daha çok kalıcı hayır ve iyilik olarak düzenler.","focus_only":"Artma ve çoğalma çekirdeği mal, topluluk ve nesil için öne çıkar.","gloss":"bereketli çoğalma","neighbor_only":"Sabit hayır ve ilahi iyilik değeri daha belirgin bir eksendir.","neighbor_ref":"root_000109/B004","relation_type":"near_synonym","shared_zone":"İkisi de artış, bereket ve iyi sonuç alanını paylaşır."},{"boundary_match":"partial","distinction":"Bu dal genel artış ve bereketi kapsar; komşu dal daha belirgin biçimde sürü, hayvan varlığı ve yavru çoğalışı alanına bağlıdır.","focus_only":"Uğur ve bereket değeri artışla birlikte bulunur.","gloss":"artış ve nesil çoğalması","neighbor_only":"Hayvan varlığı, sürü ve yavru çoğalması daha açık bir alan oluşturur.","neighbor_ref":"root_001427/B003","relation_type":"near_synonym","shared_zone":"İkisi de çoğalma, mal ve yavru artışı alanında kesişir."},{"boundary_match":"thematic_only","distinction":"Bu dal çoğalma olgusunu tanımlar; komşu dal çoğalmanın ürünü olan belirli küçük hayvan adıdır.","focus_only":"Artış ve verimlilik sürecini anlatır.","gloss":"çoğalma ile yavru","neighbor_only":"Koyun yavrusunun kendisini adlandırır.","neighbor_ref":"root_000051/B009","relation_type":"thematic","shared_zone":"Nesil ve doğurganlık bağlamı ikisini aynı sahnede buluşturabilir."}],"source_phrase_ar":"الأمر النماء والبركة، وقد أمر الشيء أي كثر (maqayis)؛ الأمرة البركة وامرأة أمرة، وأمر الشيء أي كثر (ayn)؛ أمر هو أي كثر، وأمر القوم أي كثروا (sihah)؛ الأمرة الزيادة والنماء والبركة (tahdhib)؛ أمر القوم كثروا، وآمرنا بمعنى أكثرنا (mufradat)","source_summary":"Kaynaklar bu dalda artma, çoğalma, verimlilik ve uğur fikrini ortak biçimde verir; kişi, mal, topluluk ve hayvan doğurganlığı bunun bağlamlarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الكثرة والنماء والبركة واليمن، وكثرة المال أو القوم أو النسل.","what_is_not_ar":"ليس الأمر بمعنى طلب الفعل، ولا الإمارة إلا في قراءة أو تفسير منفصل، ولا العلامة."},"support_links":[]},{"boundary":"Belirti, yol işareti ve belirlenmiş zaman alanıdır; buyruk ve yönetim anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000051/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَمَرَ","morph_features":"STEM|POS:V|PERF|LEM:>amara|ROOT:Amr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:12:2:1","qac_word_ref":"96:12:2","surface_ar":"أَمَرَ"}],"gloss":"belirti veya belirlenmiş vakit","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek anlam, bir şeyi tanıtan veya gösteren belirti ve işarettir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yol veya çöl içindeki küçük taş işaretleri bu belirti anlamının özel bağlamıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirlenmiş zaman veya randevu da bu dalda verilen ayrı bir kapsamdır."}}],"root_ar":"ء م ر","root_id":"root_000051","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesneyi, yolu ya da zamanı tanıtan işaret ve belirleme anlamları birlikte söz konusu olduğunda uygundur.","boundary_detail":"Belirti, yol işareti ve belirlenmiş zaman alanıdır; buyruk ve yönetim anlamı değildir.","branch_image_ar":"العلامة والموعد","concept_gloss":"belirti veya belirlenmiş vakit","contextual_glosses":[{"applicability":"Bir şeyi tanıtan belirti veya yol üzerindeki alamet kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Belirlenmiş zaman anlamını dışarıda bırakır.","preserves":"Gösterme ve tanıtma yönünü korur."},"facet_ids":["F001","F002"],"text":"işaret","usage_role":"contextual"},{"applicability":"Önceden belirlenen zaman veya buluşma vaktinin anlatıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yol veya nesne belirtisi anlamını dışarıda bırakır.","preserves":"Belirlenmiş zaman yönünü korur."},"facet_ids":["F003"],"text":"randevu vakti","usage_role":"contextual"}],"definition":"Bir şeyi tanımaya veya yolu bulmaya yarayan belirti; ayrıca önceden belirlenmiş zaman ya da buluşma vaktidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek anlam, bir şeyi tanıtan veya gösteren belirti ve işarettir."},{"facet_id":"F002","role":"specialization","statement":"Yol veya çöl içindeki küçük taş işaretleri bu belirti anlamının özel bağlamıdır."},{"facet_id":"F003","role":"extension","statement":"Belirlenmiş zaman veya randevu da bu dalda verilen ayrı bir kapsamdır."}],"identity_rationale":"Kaynak ifadesi belirti, yol izi, küçük yol taşı ve belirlenmiş zaman ya da randevu anlamlarını aynı dalda verir. Geçici çerçeve hem gösterge hem belirlenmiş vakit yönünü korur ve buyruk ya da yönetim anlamını dışarıda bırakır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"belirti, belirlenmiş zaman veya buluşma vakti"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yolun işaretleri"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"çöl veya yol üzerindeki küçük işaret taşı"}],"lexicalization_note":"Mekanik tür mixed_non_bare olduğu için genel belirti anlamı ile yol işareti kalıpları ayrı belirtilir.","neighbor_coverage_note":"Gösterge alanındaki adaylar incelendi; belirti, delil ve şart sınırını açan üç karşılaştırma yeterli görüldü.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal işaret yanında randevu vakti ve yol işareti kullanımlarını korur; komşu dal daha genel gösterge alanındadır.","focus_only":"Belirti anlamına belirlenmiş zaman ve yol taşı kullanımı da eşlik eder.","gloss":"belirti","neighbor_only":"Komşu dal belirgin göstergeyi daha geniş biçimde, metin birimi gibi kullanımlarla da verir.","neighbor_ref":"root_000074/B003","relation_type":"near_synonym","shared_zone":"İkisi de bir şeyi tanıtan işaret alanında kesişir."},{"boundary_match":"partial","distinction":"Bu dal nesneleşmiş belirtiyi veya vakti anlatır; komşu dal o belirtiyle ulaştırma ve delil olma işlevini öne çıkarır.","focus_only":"İşaretin kendisi veya belirlenmiş vakit adlandırılır.","gloss":"belirti ile gösterme","neighbor_only":"Bir şeyle bilgiye veya yola ulaştırma eylemi ve delil olma ilişkisi öndedir.","neighbor_ref":"root_000484/B001","relation_type":"near_neighbor","shared_zone":"İkisi de tanımaya ve yol bulmaya yarayan gösterge alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dal tanıtan işaret ve vakit üzerine kurulur; komşu dalda şart koşma ve şart işaretleri gibi sözleşmesel alanlar da bulunur.","focus_only":"Yol işareti ve belirlenmiş zaman kapsamı vardır.","gloss":"belirti ile şart","neighbor_only":"Şart, sözleşme kaydı ve alametleri tanıma alanı daha geniştir.","neighbor_ref":"root_000788/B001","relation_type":"near_neighbor","shared_zone":"İkisi de tanıtıcı alamet alanına dokunur."}],"source_phrase_ar":"الأمارة الموعد، والأمارة العلامة، والأمار أمار الطريق معالمه (maqayis)؛ الأمار الموعد (ayn)؛ الأمار والأمارة الوقت والعلامة، والأمر بالتحريك جمع أمرة وهي العلم الصغير من أعلام المفاوز من الحجارة (sihah)؛ الأمار الوقت والعلامة، والأمرات الأعلام واحدتها أمرة (tahdhib)","source_summary":"Kaynaklar belirti ve yol işareti anlamını ortak biçimde verir; aynı dal içinde belirlenmiş zaman veya buluşma vaktine uzanan kullanım da bulunur.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الأمارة والأمار بمعنى العلامة، وأعلام الطريق أو المفازة، والموعد أو الوقت المضروب.","what_is_not_ar":"ليس المقصود الأمر التكليفي، ولا الإمارة السياسية، ولا العجب."},"support_links":[]},{"boundary":"Büyük ve yadırganan iş anlamıdır; genel konu, bolluk ve yöneticilik değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000051/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَمَرَ","morph_features":"STEM|POS:V|PERF|LEM:>amara|ROOT:Amr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:12:2:1","qac_word_ref":"96:12:2","surface_ar":"أَمَرَ"}],"gloss":"ağır ve yadırganan şey","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek anlam, büyük ve şiddetli oluşuyla yadırganan olaydır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynak açıklamalarında şaşırtıcılık, ağır kötülük ve aykırılık tonları aynı çekirdeğe bağlanır."}}],"root_ar":"ء م ر","root_id":"root_000051","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir olay büyüklüğü veya aykırılığı sebebiyle şaşırtıcı ve kınanır nitelikte olduğunda uygundur.","boundary_detail":"Büyük ve yadırganan iş anlamıdır; genel konu, bolluk ve yöneticilik değildir.","branch_image_ar":"الأمر العظيم المنكر","concept_gloss":"ağır ve yadırganan şey","contextual_glosses":[{"applicability":"Olayın büyüklüğü ve ağırlığı vurgulandığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yadırganma veya kötülük tonunu her zaman açık taşımaz.","preserves":"Büyüklük ve ağırlığı korur."},"facet_ids":["F001"],"text":"çok ağır iş","usage_role":"contextual"},{"applicability":"Aykırılık ve kınanma tonu önde olduğunda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Büyüklük ve şiddet boyutu zayıflayabilir.","preserves":"Yadırganma ve aykırılık yönünü korur."},"facet_ids":["F002"],"text":"yadırganacak şey","usage_role":"contextual"}],"definition":"Büyüklüğü, şiddeti veya aykırılığı yüzünden şaşırtıcı ve yadırganan ağır iş ya da olay.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek anlam, büyük ve şiddetli oluşuyla yadırganan olaydır."},{"facet_id":"F002","role":"source_variant","statement":"Kaynak açıklamalarında şaşırtıcılık, ağır kötülük ve aykırılık tonları aynı çekirdeğe bağlanır."}],"identity_rationale":"Kaynak ifadesi şaşırtıcı, ağır, büyük ve yadırganan işi anlatır; bazı açıklamalar bunu büyük kötülük veya tuhaflık olarak açar. Geçici çerçeve bu şiddetli yadırganma çekirdeğini doğru verir.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"büyük, ağır, yadırganan veya şaşırtıcı iş"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"büyük ve yadırganan bir şey"}],"lexicalization_note":"Mekanik tür mixed_non_bare olduğu için ad biçimi ile özel niteleme kalıbı aynı çekirdeğe bağlı tutulur.","neighbor_coverage_note":"Adayların tümü ağır olay, bela ve kötülük alanlarına göre elendi; en açıklayıcı üç sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal ağır ve kınanır oluşu öne çıkarır; komşu dal şaşırtıcı veya yapılmış şey niteliğine daha çok açılabilir.","focus_only":"Şiddetli yadırganma ve büyük kötülük tonu birlikte bulunabilir.","gloss":"şaşırtıcı ağır iş","neighbor_only":"Komşu dalda yapılmış, uydurulmuş veya şaşırtıcı şey tonu daha belirgindir.","neighbor_ref":"root_001150/B004","relation_type":"near_synonym","shared_zone":"İkisi de büyük ve şaşırtıcı olay alanında örtüşür."},{"boundary_match":"partial","distinction":"Bu dal olayın yadırganan büyüklüğünü adlandırır; komşu dal felaket veya çıkmaz niteliğini daha güçlü taşır.","focus_only":"Ağır ve yadırganan tek olay ya da iş anlatılır.","gloss":"ağır iş ile bela","neighbor_only":"Daha çok bela, çözülmesi güç ağır sıkıntı veya dehşetli durum alanıdır.","neighbor_ref":"root_001025/B003","relation_type":"near_neighbor","shared_zone":"İkisi de büyük, kötü ve sarsıcı olay alanında kesişir."},{"boundary_match":"field_only","distinction":"Bu dal her kötülüğü değil, büyüklüğü ve aykırılığıyla sarsıcı olan şeyi anlatır; komşu dal genel kötü ve zararlı olan alandır.","focus_only":"Büyük ve şaşırtıcı aykırılık çekirdektir.","gloss":"yadırganan iş ile kötülük","neighbor_only":"Genel kötülük ve iyi olanın karşıtı çekirdektir.","neighbor_ref":"root_000787/B001","relation_type":"same_field","shared_zone":"Kınanan veya kötü görülen olaylarda birlikte düşünülebilirler."}],"source_phrase_ar":"العجب، لقد جئت شيئا إمرا (maqayis)؛ أمر أمره أي اشتد والاسم الإمر، ويقال عجبا (sihah)؛ لقد جئت شيئا إمرا أي جئت شيئا عظيما من المنكر (tahdhib)؛ إمرا أي منكرا، من قولهم أمر الأمر أي كبر وكثر (mufradat)","source_summary":"Kaynaklar bu dalı büyük, şiddetli ve yadırganan bir şey olarak birleştirir; açıklamalar şaşırtıcılık ile ağır kötülük tonları arasında değişir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الإمر بمعنى العجب أو الأمر الشديد الكبير والمنكر العظيم.","what_is_not_ar":"ليس واحد الأمور مطلقا، ولا النماء، ولا الإمارة."},"support_links":[]},{"boundary":"Danışma, görüş alışverişi ve karar bağlama alanıdır; sırf buyruk ya da yöneticilik değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000051/B007","candidate_links":[{"candidate_id":"cand_e01563ebfa01aeb74ee1","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَمَرَ","morph_features":"STEM|POS:V|PERF|LEM:>amara|ROOT:Amr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:12:2:1","qac_word_ref":"96:12:2","surface_ar":"أَمَرَ"}],"gloss":"danışıp görüş oluşturma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek anlam, bir işte görüş almak veya karşılıklı danışmaktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin kendi içinde farklı eğilimleri tartıp bir görüşe bağlaması özel bir kullanımdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Görüşü kabul etme veya karar haline getirme anlamı danışma sürecinin sonucuna uzanır."}}],"root_ar":"ء م ر","root_id":"root_000051","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir konuda başkasıyla veya kendi içinde tartışma yoluyla görüşe varıldığında uygundur.","boundary_detail":"Danışma, görüş alışverişi ve karar bağlama alanıdır; sırf buyruk ya da yöneticilik değildir.","branch_image_ar":"المشاورة وتدبير الرأي","concept_gloss":"danışıp görüş oluşturma","contextual_glosses":[{"applicability":"Bir işte başkasının görüşüne başvurulduğunda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kendi içinde tartma ve görüşü kabul etme sonucunu açık taşımaz.","preserves":"Görüş alışverişi yönünü korur."},"facet_ids":["F001"],"text":"danışmak","usage_role":"general"},{"applicability":"Danışma veya iç tartışmanın sonunda görüşün kesinleşmesi anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Karara götüren danışma sürecini her zaman açık belirtmez.","preserves":"Görüş oluşturma sonucunu korur."},"facet_ids":["F002","F003"],"text":"karara bağlamak","usage_role":"contextual"}],"definition":"Bir iş hakkında başkasıyla veya kendi içinde görüş alışverişi yapıp bir görüşe varma ya da o görüşü kabul etme süreci.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek anlam, bir işte görüş almak veya karşılıklı danışmaktır."},{"facet_id":"F002","role":"specialization","statement":"Kişinin kendi içinde farklı eğilimleri tartıp bir görüşe bağlaması özel bir kullanımdır."},{"facet_id":"F003","role":"extension","statement":"Görüşü kabul etme veya karar haline getirme anlamı danışma sürecinin sonucuna uzanır."}],"identity_rationale":"Kaynak ifadesi başkasıyla danışmayı, topluluğun kendi arasında görüş alışverişini, kişinin kendi içinde tartıp karar bağlamasını ve görüş kabulünü birlikte verir. Geçici çerçeve bu danışma ve karar oluşturma alanını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"işimde ona danıştım"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"karşılıklı danışma veya birbirinin görüşünü kabul etme"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"kendi içinde düşünüp görüşünü karara bağladı"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"senin hakkında birbirleriyle danışıyorlar"}],"lexicalization_note":"Mekanik tür mixed_non_bare olduğu için karşılıklı danışma, kendi içinde tartma ve görüş kabulü ayrı tutulur.","neighbor_coverage_note":"Danışma, düşünme ve karar adayları tarandı; süreci ve sonucu ayıran üç karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal danışmayı karar oluşturma ve görüş kabulüyle birlikte verir; komşu dal görüş alışverişi eyleminin kendisinde daha dar kalır.","focus_only":"Görüşü kabul etme ve kişinin kendi içinde karar bağlaması da kapsama girer.","gloss":"danışma","neighbor_only":"Komşu dal özellikle görüş isteme ve görüş bildirme eylemini öne çıkarır.","neighbor_ref":"root_000827/B003","relation_type":"near_synonym","shared_zone":"İkisi de bir işte görüş alışverişi yapma alanında örtüşür."},{"boundary_match":"partial","distinction":"Bu dal görüşün danışma içinde oluşmasını anlatır; komşu dal danışma şartı olmadan düşünme, kanaat ve zihinsel değerlendirme alanına gider.","focus_only":"Başka biriyle danışma ve karşılıklı görüş alışverişi vardır.","gloss":"danışma ile düşünme","neighbor_only":"Kalbin görüşü, düşünme ve değerlendirme daha içsel bir alan oluşturur.","neighbor_ref":"root_000531/B002","relation_type":"near_neighbor","shared_zone":"İkisi de görüş üretme ve düşünme alanını paylaşır."},{"boundary_match":"partial","distinction":"Bu dal kararın danışma veya iç tartışma sürecinden çıkmasını anlatır; komşu dal kararın sıkı biçimde toplanıp kesinleştirilmesine odaklanır.","focus_only":"Görüş alışverişi ve kabul süreci öndedir.","gloss":"danışma ile azim","neighbor_only":"Dağınık görüşü toplayıp kesin azme dönüştürme ve hazırlama çekirdektir.","neighbor_ref":"root_000259/B003","relation_type":"near_neighbor","shared_zone":"İkisi de bir iş hakkında görüşün karar haline gelmesiyle ilgilidir."}],"source_phrase_ar":"فلان يؤامر نفسيه أي نفس تأمره بشيء ونفس تأمره بآخر (maqayis)؛ آمرته في أمري إذا شاورته، والائتمار والاستئمار المشاورة وكذلك التآمر (sihah)؛ ائتمر القوم إذا تشاوروا، أي كيف يرتئي رأيا ويشاور نفسه ويعقد عليه (tahdhib)؛ الائتمار قبول الأمر، ويقال للتشاور ائتمار (mufradat)","source_summary":"Kaynaklar bu dalı danışma, karşılıklı görüş alışverişi, kişinin kendi içinde düşünmesi ve sonunda görüşü kabul edip karara bağlaması alanında toplar.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه المؤامرة والائتمار والاستئمار والتآمر، أي مشاورة النفس أو الغير، وقبول الرأي أو العزم عليه.","what_is_not_ar":"ليس مجرد الأمر والنهي، ولا ولاية الأمير، ولا الضعيف الذي يتبع كل رأي."},"support_links":["sup_6738684846d79770b1f5"]},{"boundary":"Görüşsüz ve her söze uyan kişi anlamıdır; şaşırtıcı olay veya hayvan yavrusu değildir.","branch_kind":"bare","branch_ref":"root_000051/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَمَرَ","morph_features":"STEM|POS:V|PERF|LEM:>amara|ROOT:Amr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:12:2:1","qac_word_ref":"96:12:2","surface_ar":"أَمَرَ"}],"gloss":"zayıf görüşlü kişi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek anlam, görüş zayıflığı ve akılsızlıktır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu kişi her sözle yön değiştirir veya herkese danışıp onların dediğine uyar."}}],"root_ar":"ء م ر","root_id":"root_000051","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kendi sağlam kanaati olmayıp başkalarının her sözüne uyan kişi anlatıldığında uygundur.","boundary_detail":"Görüşsüz ve her söze uyan kişi anlamıdır; şaşırtıcı olay veya hayvan yavrusu değildir.","branch_image_ar":"ضعيف الرأي التابع","concept_gloss":"zayıf görüşlü kişi","contextual_glosses":[{"applicability":"Kişinin düşünce eksikliği ve sağlıksız yargısı öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Herkesin sözüne uyma ayrıntısını açık taşımaz.","preserves":"Akıl ve görüş zayıflığını korur."},"facet_ids":["F001"],"text":"akılsız","usage_role":"contextual"},{"applicability":"Kişinin başkalarının görüşleriyle kolayca yön değiştirmesi anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Akılsızlık ve görüş zayıflığı değerini tek başına tam taşımaz.","preserves":"Başkasına uyma yönünü korur."},"facet_ids":["F002"],"text":"her söze uyan","usage_role":"contextual"}],"definition":"Kendi görüşü zayıf olduğu için herkesin sözünü dinleyen, başkasının görüşüne kolayca uyan akılsız kişi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek anlam, görüş zayıflığı ve akılsızlıktır."},{"facet_id":"F002","role":"associated_use","statement":"Bu kişi her sözle yön değiştirir veya herkese danışıp onların dediğine uyar."}],"identity_rationale":"Kaynak ifadesi görüşü zayıf, akılsız veya her sözle yön değiştiren kişiyi anlatır. Geçici çerçeve bu insan niteliğini doğru korur ve yadırganan büyük iş ya da hayvan yavrusu anlamlarından ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"görüşü zayıf, her sözü dinleyip uyan akılsız kişi"}],"lexicalization_note":"Mekanik tür bare olduğu için tanım çıplak kişi niteliğini verir ve danışma dalına genişletilmez.","neighbor_coverage_note":"Adaylar görüş zayıflığı, akılsızlık ve bağımlı uyma ekseninde incelendi; kişi niteliğini netleştirenler seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal özellikle zayıf görüş ve akılsızlık niteliğine dayanır; komşu dal toplumsal uyma ve herkesle birlikte olma tavrını daha öne çıkarır.","focus_only":"Görüş zayıflığı ve akılsızlık açık çekirdektir.","gloss":"herkese uyan kişi","neighbor_only":"Komşu dal herkesle birlikte olduğunu söyleyen bağımlı ve iradesiz kişiyi daha geniş anlatır.","neighbor_ref":"root_001435/B004","relation_type":"near_synonym","shared_zone":"İkisi de kendi sağlam görüşü olmadan başkalarına uyan kişiyi anlatır."},{"boundary_match":"field_only","distinction":"Bu dal başkalarının sözüyle yön değiştiren kişiye odaklanır; komşu dal düşüncenin bozulması ve çarenin eksilmesi gibi daha geniş zihinsel bozukluk alanıdır.","focus_only":"Her söze uyan zayıf görüşlü kişi tanımlanır.","gloss":"zayıf görüş ile bozuk akıl","neighbor_only":"Aklın ters dönmesi, hilenin bozulması ve sağlam düşüncenin kaybı alanı daha geneldir.","neighbor_ref":"root_000041/B006","relation_type":"same_field","shared_zone":"İkisi de akıl ve sağlam görüş eksikliği alanında buluşur."},{"boundary_match":"thematic_only","distinction":"Bu dal olumsuz kişi niteliğidir; komşu dal bir konuda danışma ve görüş oluşturma eylemidir.","focus_only":"Danışmayı sağlıklı karar için değil, zayıf görüşle herkese bağımlı oluşu anlatır.","gloss":"bağımlı uyma ile danışma","neighbor_only":"Görüş alışverişi yapıp karar oluşturma sürecidir.","neighbor_ref":"root_000051/B007","relation_type":"thematic","shared_zone":"İkisi de görüş alma ve başkasının sözüyle ilişkilidir."}],"source_phrase_ar":"الإمر الرجل الضعيف الرأي الأحمق الذي يسمع كلام هذا وكلام هذا (maqayis)؛ الإمر الضعيف من الرجال (ayn)؛ رجل إمر وإمرة أي ضعيف الرأي يأتمر لكل أحد (sihah)؛ رجل إمر وإمرة أي يستأمر كل أحد في أمره، والإمر الأحمق (tahdhib)","source_summary":"Kaynaklar bu dalda zayıf görüşlü veya akılsız kişiyi, herkesin sözünü dinleyen ve her görüşe uyan biri olarak tanımlar.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الإمر أو الإمرة للرجل الضعيف الرأي أو الأحمق الذي يستأمر كل أحد ويأتمر لكل أمر.","what_is_not_ar":"ليس إمرا بمعنى العجب والمنكر، ولا الإمر ولد الضأن."},"support_links":[]},{"boundary":"Koyun yavrusu adıdır; insan niteliği, şaşırtıcı olay ve yöneticilik dışarıdadır.","branch_kind":"bare","branch_ref":"root_000051/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَمَرَ","morph_features":"STEM|POS:V|PERF|LEM:>amara|ROOT:Amr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:12:2:1","qac_word_ref":"96:12:2","surface_ar":"أَمَرَ"}],"gloss":"küçük koyun yavrusu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek anlam, koyun türünden küçük yavrudur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişi biçim, dişi yavru veya genç dişi koyun olarak verilir."}}],"root_ar":"ء م ر","root_id":"root_000051","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Koyun türünden küçük yavru veya onun dişi biçimi anlatıldığında uygundur.","boundary_detail":"Koyun yavrusu adıdır; insan niteliği, şaşırtıcı olay ve yöneticilik dışarıdadır.","branch_image_ar":"ولد الضأن الصغير","concept_gloss":"küçük koyun yavrusu","contextual_glosses":[{"applicability":"Koyun yavrusu genel olarak anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dişi yavru veya genç dişi koyun ayrımını açık taşımaz.","preserves":"Koyun yavrusu anlamını korur."},"facet_ids":["F001"],"text":"kuzu","usage_role":"general"},{"applicability":"Dişi biçim veya genç dişi koyun kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Erkek veya genel yavru kapsamını dışarıda bırakır.","preserves":"Dişi yavru yönünü korur."},"facet_ids":["F002"],"text":"dişi kuzu","usage_role":"contextual"}],"definition":"Koyunun küçük yavrusu; dişi biçiminde dişi kuzu veya genç dişi koyun.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek anlam, koyun türünden küçük yavrudur."},{"facet_id":"F002","role":"specialization","statement":"Dişi biçim, dişi yavru veya genç dişi koyun olarak verilir."}],"identity_rationale":"Kaynak ifadesi küçük koyun yavrusunu ve dişi biçimini açıkça verir. Geçici çerçeve bu hayvan adını doğru yakalar ve aynı yazılı biçimle gelen zayıf görüşlü kişi ya da ağır iş anlamlarına taşmaz.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"küçük koyun yavrusu; dişisi dişi kuzu veya genç dişi koyun"}],"lexicalization_note":"Mekanik tür bare olduğu için tanım çıplak hayvan adında kalır ve mecazi alan eklemez.","neighbor_coverage_note":"Hayvan yavrusu adayları değerlendirildi; tür, yaş ve kapsam sınırını gösteren üç ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal küçük koyun yavrusunu ve dişi biçimini birlikte verir; komşu dal genel kuzu yaş adında daha doğrudan durur.","focus_only":"Dişi biçim ve genç dişi koyun ayrımı da verilir.","gloss":"kuzu","neighbor_only":"Komşu dal koyun yavrusunu yaş evresiyle daha genel adlandırır.","neighbor_ref":"root_000357/B009","relation_type":"near_synonym","shared_zone":"İkisi de koyun yavrusu alanında örtüşür."},{"boundary_match":"partial","distinction":"Bu dal türü koyunla sınırlar; komşu dal birden çok küçük hayvan yavrusu için daha geniş bir sınıf adıdır.","focus_only":"Koyun yavrusuna ve dişi biçimine odaklanır.","gloss":"küçük koyun yavrusu","neighbor_only":"Koyun, keçi, yabani sığır ve benzeri küçük hayvan yavrularını daha geniş kapsar.","neighbor_ref":"root_000160/B004","relation_type":"near_synonym","shared_zone":"İkisi de küçük davar veya hayvan yavrusu alanında buluşur."},{"boundary_match":"field_only","distinction":"Bu dal türün küçük yavrusunu adlandırır; komşu dal türün genel adını ve topluluğunu anlatır.","focus_only":"Yavru ve yaş küçüklüğü çekirdektir.","gloss":"kuzu ile koyun","neighbor_only":"Koyun cinsi veya sürü bütünü çekirdektir.","neighbor_ref":"root_001109/B001","relation_type":"same_field","shared_zone":"İkisi de koyun türü ve küçükbaş hayvan alanındadır."}],"source_phrase_ar":"الإمرة الأنثى من الحملان (ayn)؛ الإمر الصغير من ولد الضأن والأنثى إمرة (sihah)؛ الإمر الخروف والإمرة الرخل (tahdhib)","source_summary":"Kaynaklar bu dalı koyun yavrusu ve onun dişi karşılığı olarak verir; anlam kişi niteliği ya da yadırganan olay alanına bağlı değildir.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه الإمر لولد الضأن أو الخروف، والإمرة للأنثى أو الرخل.","what_is_not_ar":"ليس الضعيف الرأي، ولا العجب، ولا الإمارة."},"support_links":[]},{"boundary":"Yalnız Tanrı'ya özgü var etme anlamıdır; insan buyruğu, makam veya genel konu anlamı değildir.","branch_kind":"bare","branch_ref":"root_000051/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَمَرَ","morph_features":"STEM|POS:V|PERF|LEM:>amara|ROOT:Amr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:12:2:1","qac_word_ref":"96:12:2","surface_ar":"أَمَرَ"}],"gloss":"Tanrı'ya özgü yaratma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek anlam, var etme ve yaratmadır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu yaratma insanlara değil, Tanrı'ya özgü olarak sınırlandırılır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yaratıcı sözle varlığın hemen gerçekleşmesi bu anlamın örnek anlatımıdır."}}],"root_ar":"ء م ر","root_id":"root_000051","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaratma veya varlığa çıkarma insan eylemi değil ilahi fiil olarak anlatıldığında uygundur.","boundary_detail":"Yalnız Tanrı'ya özgü var etme anlamıdır; insan buyruğu, makam veya genel konu anlamı değildir.","branch_image_ar":"الإبداع الإلهي","concept_gloss":"Tanrı'ya özgü yaratma","contextual_glosses":[{"applicability":"İlahi var etme bağlamı zaten açık olduğunda kısa karşılık olarak uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tanrı'ya özgü oluşu tek başına belirtmez.","preserves":"Var etme yönünü korur."},"facet_ids":["F001"],"text":"yaratma","usage_role":"contextual"},{"applicability":"Yaratıcı sözle oluşun hemen gerçekleştiği örnek anlatımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel yaratma çekirdeğini örnek anlatıma daraltır.","preserves":"Sözle oluşa çıkarma örneğini korur."},"facet_ids":["F003"],"text":"var edici söz","usage_role":"explanatory"}],"definition":"Tanrı'ya özgü olarak bir şeyi yoktan var etme veya yaratıcı sözle oluşa çıkarma eylemi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek anlam, var etme ve yaratmadır."},{"facet_id":"F002","role":"specialization","statement":"Bu yaratma insanlara değil, Tanrı'ya özgü olarak sınırlandırılır."},{"facet_id":"F003","role":"example","statement":"Yaratıcı sözle varlığın hemen gerçekleşmesi bu anlamın örnek anlatımıdır."}],"identity_rationale":"Kaynak ifadesi bu dalı yaratma ve var etme anlamına bağlar ve bunu Tanrı'ya özgü tutar; ayrıca var edici sözle hızla gerçekleşme örneği verir. Geçici çerçeve doğrudur, fakat tanımın insanın başkasına buyruğuna genellenmemesi gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"Tanrı'ya özgü yaratma ve var etme"}],"lexicalization_note":"Mekanik tür bare olsa da kaynak sınırlaması gereği tanım çıplak biçimi yalnız ilahi yaratma alanında tutar.","neighbor_coverage_note":"Adaylar buyruk, yükümlülük ve yürürlüğe koyma alanlarına göre değerlendirildi; ilahi yaratma sınırını açanlar yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal sözle varlığa çıkarma gibi ilahi yaratma alanıdır; komşu dal mevcut bir muhataba yöneltilen yapma buyruğudur.","focus_only":"Söz, yaratıcı oluşu gerçekleştiren ilahi var etme bağlamındadır.","gloss":"yaratma ile buyruk","neighbor_only":"İnsan veya yetkili bir muhataba yapma yükümlülüğü bildirir.","neighbor_ref":"root_000051/B002","relation_type":"near_neighbor","shared_zone":"İkisi de söz ve isteme görüntüsüyle anlatılabilir."},{"boundary_match":"partial","distinction":"Bu dal varlık kazandırır; komşu dal zaten konu olan bir işin geçerli ve işler hale gelmesini anlatır.","focus_only":"Varlığın yaratılması ve oluşa çıkarılması çekirdektir.","gloss":"yaratma ile yürürlüğe koyma","neighbor_only":"Bir işin yürürlüğe konması, geçirilmesi veya onaylanması çekirdektir.","neighbor_ref":"root_001430/B002","relation_type":"near_neighbor","shared_zone":"İkisi de bir söz veya kararın sonuç doğurması alanında temas eder."},{"boundary_match":"partial","distinction":"Bu dal yoktan var etme anlamındadır; komşu dal bir işin nüfuz edip uygulanmasına odaklanır.","focus_only":"Yaratıcı var etme Tanrı'ya özgü tutulur.","gloss":"var etme ile geçerlilik","neighbor_only":"Bir kişinin işinin geçip etkili olması veya bir kararın uygulanması anlatılır.","neighbor_ref":"root_001531/B002","relation_type":"near_neighbor","shared_zone":"İkisi de sonucun gerçekleşmesi ve etkili olma alanında buluşur."}],"source_phrase_ar":"ويقال للإبداع أمر، ويختص ذلك بالله تعالى دون الخلائق؛ قل الروح من أمر ربي أي من إبداعه؛ إنما قولنا لشيء إذا أردناه أن نقول له كن فيكون","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık anlamı Tanrı'ya özgü yaratma olarak sınırlar ve yaratıcı söz örneğiyle açıklar."}],"source_summary":"Bu dal için ortak çoklu kaynak özeti yoktur; tanıklık tek kaynak ayrıntısında ilahi yaratma ve var edici söz örneğiyle verilir.","sources":["MU"],"what_is_ar":"يدخل فيه الأمر بمعنى الإبداع والإنشاء المختص بالله، والتعبير عن سرعة الإيجاد بالقول.","what_is_not_ar":"ليس هذا أمر المخلوق لغيره، ولا الإمارة، ولا الشأن العام إلا من جهة اللفظ."},"support_links":[]},{"boundary":"Mızrağa uç takma ve sivri uç alanıdır; buyruk, yönetim ve belirti değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000051/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَمَرَ","morph_features":"STEM|POS:V|PERF|LEM:>amara|ROOT:Amr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:12:2:1","qac_word_ref":"96:12:2","surface_ar":"أَمَرَ"}],"gloss":"mızrağa uç takma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek anlam, mızrak sapına keskin uç yerleştirme işlemidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sivriltilmiş veya uç takılmış parça bu işlemin nesneleşmiş sonucudur."}}],"root_ar":"ء م ر","root_id":"root_000051","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir mızrak veya saplı silaha keskin uç takılması ya da bu sivri uç anlatıldığında uygundur.","boundary_detail":"Mızrağa uç takma ve sivri uç alanıdır; buyruk, yönetim ve belirti değildir.","branch_image_ar":"تسليح القناة بسنان","concept_gloss":"mızrağa uç takma","contextual_glosses":[{"applicability":"Uç takılmış veya keskinleştirilmiş parça nitelendiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ucu takma işlem sürecini açık taşımaz.","preserves":"Sivriltilmiş uç sonucunu korur."},"facet_ids":["F002"],"text":"sivri uçlu","usage_role":"contextual"},{"applicability":"Bir mızrağa uç takma buyruğu veya talimatı bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mızrak ve uç takma eylemini korur."},"facet_ids":["F001"],"text":"mızrağa demir uç geçir","usage_role":"contextual"}],"definition":"Bir mızrak ya da benzeri sapa keskin uç takma; ayrıca takılmış veya sivriltilmiş uç.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek anlam, mızrak sapına keskin uç yerleştirme işlemidir."},{"facet_id":"F002","role":"associated_use","statement":"Sivriltilmiş veya uç takılmış parça bu işlemin nesneleşmiş sonucudur."}],"identity_rationale":"Kaynak ifadesi sivriltilmiş uç ve bir mızrağa uç takma eylemini verir. Geçici çerçeve bu silah parçası ve donatma işlemini doğru yansıtır; buyruk, yönetici veya belirti anlamlarına geçmez.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"sivriltilmiş veya uç takılmış mızrak ucu"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"mızrağına keskin uç tak"}],"lexicalization_note":"Mekanik tür mixed_non_bare olduğu için belirli silah kalıbı ve mızrağa uç takma ifadesiyle sınırlı tanım yapılır.","neighbor_coverage_note":"Silah ve uç adayları değerlendirildi; işlem, parça ve bütün araç ayrımını gösteren üç ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal mızrağı uçla donatma işlemine dayanır; komşu dal daha doğrudan uçlu silah veya mızrak ucu adıdır.","focus_only":"Uç takma işlemi ve uç takılmış olma sonucu birlikte bulunur.","gloss":"uç takma ile mızrak ucu","neighbor_only":"Mızrak ucu veya kısa saplı silahın kendisi adlandırılır.","neighbor_ref":"root_000302/B004","relation_type":"near_neighbor","shared_zone":"İkisi de keskin mızrak ucu ve saplı silah alanındadır."},{"boundary_match":"partial","distinction":"Bu dal donatma işlemine ve takılmış uca odaklanır; komşu dal çeşitli ince çubuklar, mızrak parçaları ve sivri nesneleri kapsar.","focus_only":"Mızrağa keskin uç takma işlemi öndedir.","gloss":"uç takma ile ince mızrak","neighbor_only":"İnce dal, çubuk, mızrak ve sivri parça alanı daha geniştir.","neighbor_ref":"root_000403/B007","relation_type":"near_neighbor","shared_zone":"İkisi de saplı, sivri veya mızrakla ilgili nesneler alanında temas eder."},{"boundary_match":"field_only","distinction":"Bu dal mızrağın uçla donatılmasına gider; komşu dal bütün mızrak aracını ve onun kullanımını adlandırır.","focus_only":"Silahın ucunu takma veya sivriltme anlatılır.","gloss":"uç takma ile mızrak","neighbor_only":"Mızrak aracının kendisi ve onu taşıma veya onunla vurma alanı anlatılır.","neighbor_ref":"root_000597/B001","relation_type":"same_field","shared_zone":"İkisi de mızrak ve saplı silah alanında bulunur."}],"source_phrase_ar":"سنان مؤمر أي محدد؛ أمر قناتك أي اجعل فيها سنانا","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık sivriltilmiş uç ile bir mızrağa uç takma buyruğunu aynı silah bağlamında verir."}],"source_summary":"Bu dal için ortak çoklu kaynak özeti yoktur; tanıklık tek kaynak ayrıntısında sivriltilmiş uç ve mızrağa uç takma kullanımıyla verilir.","sources":["TA"],"what_is_ar":"يدخل فيه السنان المؤمر أي المحدد، وأمر القناة بمعنى جعل سنان فيها.","what_is_not_ar":"ليس الأمر بمعنى طلب الفعل، ولا الأمير، ولا العلامة."},"support_links":[]},{"boundary":"Dal genel koruma işlemini ve koruyucu aracı kapsar; kişinin kendini sakınması, ağırlık ölçüsü, hayvanın aksaması ve kuş adı bu sınıra girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001677/B001","candidate_links":[{"candidate_id":"cand_b7506fac0ab2231cc020","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَقْوَى","morph_features":"STEM|POS:N|LEM:taqowaY|ROOT:wqy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:12:3:3","qac_word_ref":"96:12:3","surface_ar":"تَّقْوَىٰٓ"}],"gloss":"araya engel koyarak zarardan koruma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Korunan şeyden zarar verici etkiyi uzak tutma ve onu incinmekten ya da bozulmaktan saklama işlemidir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Koruma, zarar ile korunacak şey arasına başka bir araç, katman veya engel koyularak gerçekleştirilir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kadının saçı ile dış örtüsü arasına koyduğu bez, bu koruyucu ara katmanın özel bir örneğidir."}}],"root_ar":"و ق ي","root_id":"root_001677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel eylem ile koruyucu aracın ortak çekirdeğini, herhangi bir özel kullanım alanına bağlamadan karşılar.","boundary_detail":"Dal genel koruma işlemini ve koruyucu aracı kapsar; kişinin kendini sakınması, ağırlık ölçüsü, hayvanın aksaması ve kuş adı bu sınıra girmez.","branch_image_ar":"دفع الضرر بوقاية","concept_gloss":"araya engel koyarak zarardan koruma","contextual_glosses":[{"applicability":"Eylemden çok, zarar ile korunacak şey arasına koyulan araç veya katman kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Araya koyulan unsurun koruyucu işlevini ve zararı kesen konumunu korur."},"facet_ids":["F002"],"text":"koruyucu engel","usage_role":"contextual"},{"applicability":"Kadına ait özel bez kullanımını açıkça anlatan bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bezin yerini, maddi niteliğini ve koruyucu ara katman işlevini korur."},"facet_ids":["F003"],"text":"saç ile dış örtü arasındaki koruyucu bez","usage_role":"explanatory"}],"definition":"Bir şeyi ona zarar verecek başka bir şeyden korumak için araya bir araç ya da engel koyma ve böylece zararı ondan uzak tutma. Bu işlevi gören araç veya engel de aynı kavram alanında adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Korunan şeyden zarar verici etkiyi uzak tutma ve onu incinmekten ya da bozulmaktan saklama işlemidir."},{"facet_id":"F002","role":"core","statement":"Koruma, zarar ile korunacak şey arasına başka bir araç, katman veya engel koyularak gerçekleştirilir."},{"facet_id":"F003","role":"example","statement":"Kadının saçı ile dış örtüsü arasına koyduğu bez, bu koruyucu ara katmanın özel bir örneğidir."}],"identity_rationale":"Kaynak ifadesi, bir şeyi ona zarar verecek başka bir şeyden korumayı ve bunun için araya koruyucu bir unsur koymayı ortak çekirdek olarak verir. Koruyucu bez örneği bu genel işlemin özel bir gerçekleşmesidir ve dalın kimliğini değiştirmez.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi koruyucu bir engelle zarardan saklamak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"koruma; zararı önleyen araç veya engel"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir şeyi korumaya yarayan araç ya da engel"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"zarardan koruyan şey"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"zararı savan koruyucu"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kadının saçı ile dış örtüsü arasına koyduğu koruyucu bez"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"koruyucu şeyler"}],"lexicalization_note":"Tanım, genel koruma çekirdeğini özel ad ve kalıplardan ayırır; kadına ait koruyucu bez yalnızca yapıya bağlı bir örnek olarak tutulur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yayımlanan beş ilişki koruma çekirdeğine en yakın sınırları gösterir. Kale, bekçilik, tutunarak korunma, üstü açıklık ve öteki kök içi dallar ya daha uzak alan ortaklığı kurar ya da ayrı adlandırmalardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda ayırt edici unsur, başka bir şeyi koruyucu engel olarak araya koymaktır; komşu dalın çekirdeği ise etkiyi bulunduğu yerden itmek veya doğrudan savmaktır.","focus_only":"Koruma, zarar ile hedef arasına başka bir unsur koyma mekanizmasıyla tanımlanır.","gloss":"koruma ile itip uzaklaştırma","neighbor_only":"Öteki dal yer değiştirtmeyi, karşılıklı itişmeyi ve kötülüğü doğrudan savmayı da kapsar.","neighbor_ref":"root_000480/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da zararlı veya istenmeyen bir etkinin hedefe ulaşmasını engeller."},{"boundary_match":"partial","distinction":"Bu dal koruyucu engel üzerinden zararı savmaya odaklanır; komşu dal ise engel gerektirmeyen bakım, gözetim ve süreklilik taşıyan kollamayı da içerir.","focus_only":"Zararı kesen bir araç ya da engelin araya girmesi açıkça kurucu unsurdur.","gloss":"koruma ile gözetip kollama","neighbor_only":"Sürekli gözetme, bakım, kollama ve bir şeyi iyi durumda tutma süreçlerini de kapsar.","neighbor_ref":"root_000372/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi zarar ve bozulmadan uzak tutma alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dal genel koruma işlemi ile onun aracını birlikte kapsar; komşu dal belirli bir koruyucu engel veya dayanak kavramında yoğunlaşır.","focus_only":"Koruma eylemi her tür araç veya katmanla gerçekleştirilebilir ve araç da adlandırılabilir.","gloss":"koruyucu araç ile koruyan engel","neighbor_only":"Koruyan ve çevreleyen belirli bir engel ya da dayanak adı merkezde yer alır.","neighbor_ref":"root_000071/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda bir engel, dış etkiden koruma ve çevreleyerek güvence sağlama işlevi görür."},{"boundary_match":"partial","distinction":"Komşu dal giysilerin birbirini koruduğu özel uygulamayı adlandırır; bu dal ise aynı araya koyma mekanizmasını her tür korunacak şeye açar.","focus_only":"Korunacak varlık ve zarar türü bakımından genel bir koruma şeması sunar.","gloss":"genel koruma ile giysiyi örtüyle koruma","neighbor_only":"Bir giysiyi başka bir giysiyle örtüp yıpranmaktan koruyan özel uygulamaya bağlıdır.","neighbor_ref":"root_001635/B006","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir katman, başka bir şeyi yıpranma veya zarardan korur."},{"boundary_match":"partial","distinction":"Bu dal genel ve çoğu kez maddi koruma ilişkisini anlatır; komşu dal aynı şemayı kişinin kendi davranışını ve güvenliğini gözetmesine özgüler.","focus_only":"Korunan katılımcı herhangi bir nesne veya canlı olabilir ve maddi bir engel kullanılabilir.","gloss":"bir şeyi koruma ile kendini sakınma","neighbor_only":"Korunan katılımcı kişinin kendisidir; korkulan şeyden ve yanlış davranıştan sakınma öne çıkar.","neighbor_ref":"root_001677/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da zarar ile korunacak taraf arasına koruyucu bir mesafe veya önlem koyar."}],"source_phrase_ar":"دفع شيء عن شيء بغيره (maqayis)؛ كل ما وقى شيئا فهو وقاء له ووقاية (ayn;jamhara;tahdhib)؛ حفظ الشيء مما يؤذيه ويضره (mufradat)؛ وقاية المرأة وهي الخرقة التي بين جلبابها وشعرها (jamhara)","source_summary":"Kaynakların ortak anlatımı, korumayı zararlı etkiyi başka bir şey aracılığıyla savma olarak kurar; hem koruma eylemini hem de bu işte kullanılan engeli kapsar. Kadının saçını dış örtüden ayıran bez, bu mekanizmanın özel bir örneğidir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه وقى الشيء وحفظه مما يؤذيه، والوقاء والوقاية والواقية وما يجعل حاجزا بين الشيء والضرر، ووقاية المرأة","what_is_not_ar":"لا يدخل فيه اسم الوزن أوقية ولا اسم الصرد ولا الظلع اليسير إلا من جهة الصورة العامة للاتقاء"},"support_links":["sup_9be606ce16bec1a0a739"]},{"boundary":"Dal kişinin kendisini koruması ve sakınmasıyla sınırlıdır; herhangi bir nesneyi koruma, yalnız başına iyi iş yapma veya işlenmiş yanlıştan dönme anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001677/B002","candidate_links":[{"candidate_id":"cand_83310c9496c9a84accae","lane":"micro"},{"candidate_id":"cand_e01563ebfa01aeb74ee1","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَقْوَى","morph_features":"STEM|POS:N|LEM:taqowaY|ROOT:wqy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:12:3:3","qac_word_ref":"96:12:3","surface_ar":"تَّقْوَىٰٓ"}],"gloss":"korkulan şeyden ya da yanlış davranıştan kendini koruma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, korkulan ya da zarar verecek şey ile kendi arasına koruyucu bir önlem koyar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Öz-koruma, kişiyi suç doğuran ve yanlış sayılan davranışlardan uzak tutma biçimini alabilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tanrı'ya karşı gelmekten sakınma, kişi ile sakınılan sonuç arasına koruyucu bir tutum koymak olarak düşünülür."}}],"root_ar":"و ق ي","root_id":"root_001677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem genel öz-koruma çekirdeğini hem de kişiyi yanlış davranıştan uzak tutan yönünü birlikte verir.","boundary_detail":"Dal kişinin kendisini koruması ve sakınmasıyla sınırlıdır; herhangi bir nesneyi koruma, yalnız başına iyi iş yapma veya işlenmiş yanlıştan dönme anlamına genişletilmez.","branch_image_ar":"جعل النفس في وقاية","concept_gloss":"korkulan şeyden ya da yanlış davranıştan kendini koruma","contextual_glosses":[{"applicability":"Korunulan tehlike veya yanlış davranış bağlamdan açıkça anlaşıldığında doğal ve kısa bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Korkulan şeyin veya yanlış davranışın türünü ve araya önlem koyma şemasını açıkça söylemez.","preserves":"Kişinin kendi güvenliğini ve davranışını gözeten öz-koruma yönünü korur."},"facet_ids":["F001","F002"],"text":"kendini sakınma","usage_role":"general"},{"applicability":"İnanç ve sorumluluk bağlamında, kişinin davranışını yasak olandan uzak tutması kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnanç bağlamındaki muhatabı, sakınma tutumunu ve yanlış davranıştan uzak durmayı korur."},"facet_ids":["F003"],"text":"Tanrı'ya karşı gelmekten sakınma","usage_role":"contextual"}],"definition":"Kişinin kendisini korktuğu veya zarar beklediği şeyden koruyacak bir önlem altına alması ve yanlış davranıştan uzak tutması. Tanrı'ya karşı gelmekten sakınma, bu öz-koruma tutumunun inanç alanındaki özel biçimidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, korkulan ya da zarar verecek şey ile kendi arasına koruyucu bir önlem koyar."},{"facet_id":"F002","role":"specialization","statement":"Öz-koruma, kişiyi suç doğuran ve yanlış sayılan davranışlardan uzak tutma biçimini alabilir."},{"facet_id":"F003","role":"specialization","statement":"Tanrı'ya karşı gelmekten sakınma, kişi ile sakınılan sonuç arasına koruyucu bir tutum koymak olarak düşünülür."}],"identity_rationale":"Kaynak ifadesi, kişinin kendisini korktuğu şeyden koruma altına almasını ve yanlış davranıştan uzak tutmasını aynı öz-koruma şemasında birleştirir. Tanrı'ya karşı gelmekten sakınma bu çekirdeğin inanç alanındaki belirgin gerçekleşmesidir.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kendini korkulan ya da zarar verecek şeyden korumak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir şeyi kendine koruyucu yapmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"Tanrı'ya karşı gelmekten sakınmak"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kişinin kendini korktuğu şeyden ve yanlış davranıştan koruması"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"sakınma ve kendini koruma"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"sakınan ve kendini yanlış davranıştan koruyan kimse"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"sakınma; kendini kötülükten koruma"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"sakınıp kendini koruma"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kendini yanlış davranışlardan koruyan kimse"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"sakınan ve kendini yanlış davranıştan koruyan kimse"}],"lexicalization_note":"Genel öz-koruma anlamı ile bir aracı kendine koruyucu yapma ve Tanrı'ya karşı gelmekten sakınma kalıpları ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler genel koruma, yanlıştan uzak durma, iyi davranış, suç korkusu ve tapınma sınırlarını en açık biçimde gösterir. Bağışlanma, tövbeye çağırma, benlik ve örtü adayları daha dolaylıdır; öteki kök içi dallar ayrı anlamlardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal genel koruma şemasını kişinin kendi güvenliğine ve davranışına taşır; komşu dal katılımcıyı ve zarar türünü sınırlandırmayan genel korumadır.","focus_only":"Korunan taraf zorunlu olarak kişinin kendisidir ve davranışsal sakınma da kapsama girer.","gloss":"kendini sakınma ile genel koruma","neighbor_only":"Herhangi bir nesne veya canlı, maddi bir araç ya da engel kullanılarak korunabilir.","neighbor_ref":"root_001677/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da zarar ile korunacak taraf arasına koruyucu bir önlem koyma şeması vardır."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeği önleyici öz-korumadır; komşu dal ise yanlış karşısında çekinmenin yanında işlenmiş bir yanlıştan çıkma sonucunu da kapsar.","focus_only":"Henüz gerçekleşmemiş tehlikeden ve yanlış davranıştan önleyici biçimde korunmayı da kapsar.","gloss":"yanlıştan sakınma ile yanlışın yükünden çıkma","neighbor_only":"İşlenmiş bir yanlışın yükünden çıkma ve ondan dönmüş olma anlamına kadar uzanabilir.","neighbor_ref":"root_000013/B002","relation_type":"near_synonym","shared_zone":"Her iki dal kişinin yanlış davranıştan uzak durmasını ve suç doğuran eylemi işlememesini anlatabilir."},{"boundary_match":"partial","distinction":"Bu dal koruyucu ve kaçınmacı tutumu tanımlar; komşu dal ise sakınmanın ötesinde olumlu iyilik ve itaat eylemlerini geniş biçimde kapsar.","focus_only":"Korkulan sonuç ile kişi arasına koruyucu bir sakınma tutumu koymak merkezde yer alır.","gloss":"sakınma ile iyilik ve itaat","neighbor_only":"İyi olma, itaat ve çok çeşitli yararlı işleri yapma yönünde olumlu bir eylem alanı sunar.","neighbor_ref":"root_000104/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal doğru davranışa yönelmeyi ve yanlış olandan uzak kalmayı destekler."},{"boundary_match":"partial","distinction":"Bu dal koruyucu davranış ve uzak durma eylemidir; komşu dal ise suç durumunu ve ona düşme korkusunu merkeze alır.","focus_only":"Kişinin korkulan veya suç doğuran durumdan kendini etkin biçimde korumasını anlatır.","gloss":"suçtan korunma ile suç korkusu","neighbor_only":"Suçun kendisini, suç kazanmayı ve kötü davranışa düşme korkusunu adlandırır.","neighbor_ref":"root_001051/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da yanlış davranış, onun doğuracağı yük ve bundan duyulan korku bulunur."},{"boundary_match":"field_only","distinction":"Ortak alan inanç ve sorumluluktur; bu dal sakınma yoluyla öz-korumayı, komşu dal ise tapınma ve yakınlık arama eylemini tanımlar.","focus_only":"Yanlış davranıştan uzak durarak kişinin kendisini koruması öne çıkar.","gloss":"sakınma ile tapınma","neighbor_only":"Tapınma, yakınlık arama ve kulluk eylemlerini olumlu uygulamalar olarak adlandırır.","neighbor_ref":"root_001498/B001","relation_type":"same_field","shared_zone":"İki dal inanç alanında kişinin Tanrı karşısındaki davranışını konu edinir."}],"source_phrase_ar":"اتق الله توقه أي اجعل بينك وبينه كالوقاية (maqayis)؛ التقوى في الأصل وقوى فعلى من وقيت (ayn;tahdhib)؛ التقوى جعل النفس في وقاية مما يخاف (mufradat)؛ حفظ النفس عما يؤثم (mufradat)؛ اتقى تقية وتقاة (sihah)","source_summary":"Kaynaklar bu dalı, kişinin kendisini korkulan şey karşısında koruma altına alması ve yanlış davranıştan uzak tutması olarak açıklar. İnanç bağlamındaki kullanım, Tanrı'ya karşı gelmekten sakınmayı kişi ile kötü sonuç arasındaki koruyucu tutum şeklinde somutlaştırır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه اتقى واتقاء وتقوى وتقى وتقاة وتقية وتقي، أي توقي الله أو النار أو المعاصي أو ما يخاف","what_is_not_ar":"لا يدخل فيه مطلق الوقاية المادية إلا إذا صار اتقاء للنفس"},"support_links":["sup_6738684846d79770b1f5","sup_933237a2713c380338f8"]},{"boundary":"Çekirdek hafif topallama ve ağrılı ya da hassas toynak yüzünden sakınarak yürümedir; eyer, emir ve sert zemin kullanımları bağımlı yan kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001677/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَقْوَى","morph_features":"STEM|POS:N|LEM:taqowaY|ROOT:wqy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:12:3:3","qac_word_ref":"96:12:3","surface_ar":"تَّقْوَىٰٓ"}],"gloss":"hafif topallama ve toynak ağrısıyla yürümekten çekinme","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tek sözcüklü temel anlam, hayvanın yürüyüşündeki hafif topallamadır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"At, topalladığı veya toynağındaki ağrı yüzünden yürümekten çekindiği ve sert zeminde ayağını sakındığı için bu nitelemeyi alır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hayvana yönelik emir kalıbı, onun aksayışını gözeterek yürümeyi sürdürme ve kendini zorlamama anlamı taşır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Eyer için kullanıldığında hayvanın sırtını yaralamayan veya berelenmesine yol açmayan eyer anlatılır."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Sert ve engebeli zeminle kurulan olumsuz emir, arazinin güçlüğünden yakınmama anlamına gelir."}}],"root_ar":"و ق ي","root_id":"root_001677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın tek sözcüklü çekirdeğini ve atın ağrılı ya da hassas toynak nedeniyle gösterdiği sakınan yürüyüşü birlikte karşılar.","boundary_detail":"Çekirdek hafif topallama ve ağrılı ya da hassas toynak yüzünden sakınarak yürümedir; eyer, emir ve sert zemin kullanımları bağımlı yan kullanımlardır.","branch_image_ar":"توقي الدابة من وجع الحافر","concept_gloss":"hafif topallama ve toynak ağrısıyla yürümekten çekinme","contextual_glosses":[{"applicability":"Tek sözcüklü durum adı, neden veya hayvanın türü ayrıca belirtilmeden kullanıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aksamanın hafif derecesini ve yürüyüş bozukluğu olmasını doğrudan korur."},"facet_ids":["F001"],"text":"hafif topallama","usage_role":"general"},{"applicability":"Atın topallaması veya toynak acısı yüzünden adım atmaktan çekinmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvan türünü, toynaktaki ağrıyı ve bunun yol açtığı çekingen yürüyüşü korur."},"facet_ids":["F002"],"text":"toynak ağrısıyla yürümekten çekinen at","usage_role":"explanatory"},{"applicability":"Topallayan hayvana ya da biniciye, mevcut aksamayı gözeterek yürümeyi sürdürmesi söylendiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aksamayı sürdürme, onu hesaba katma ve hareketi zorlamama yönündeki emri korur."},"facet_ids":["F003"],"text":"aksayışını gözet ve ağırdan al","usage_role":"contextual"},{"applicability":"Eyerin hayvanın sırtında yara veya bere oluşturmadığı belirtilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eyerin türünü ve hayvanın sırtını yaralamama sonucunu açıkça korur."},"facet_ids":["F004"],"text":"yara açmayan eyer","usage_role":"contextual"}],"definition":"Hafif topallama ile, özellikle toynak ağrısı veya hassasiyeti yüzünden yürümekten çekinen ya da sert zeminde ayağını sakınan atın durumu. Aynı kullanım kümesi, hayvanın aksamasına göre davranmayı, sert zeminden yakınmamayı ve hayvanda yara açmayan eyeri de anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tek sözcüklü temel anlam, hayvanın yürüyüşündeki hafif topallamadır."},{"facet_id":"F002","role":"specialization","statement":"At, topalladığı veya toynağındaki ağrı yüzünden yürümekten çekindiği ve sert zeminde ayağını sakındığı için bu nitelemeyi alır."},{"facet_id":"F003","role":"associated_use","statement":"Hayvana yönelik emir kalıbı, onun aksayışını gözeterek yürümeyi sürdürme ve kendini zorlamama anlamı taşır."},{"facet_id":"F004","role":"associated_use","statement":"Eyer için kullanıldığında hayvanın sırtını yaralamayan veya berelenmesine yol açmayan eyer anlatılır."},{"facet_id":"F005","role":"associated_use","statement":"Sert ve engebeli zeminle kurulan olumsuz emir, arazinin güçlüğünden yakınmama anlamına gelir."}],"identity_rationale":"Kaynak ifadesi yalnızca toynak ağrısından kaçınmayı değil, hafif topallamayı, topallayan atın davranışını, hayvanda yara açmayan eyeri ve aksayışa göre davranma sözünü birlikte verir. Bu nedenle dal korunabilir, fakat geçici hayvanın kendini koruması çerçevesi bütün malzemeyi taşıyacak biçimde aksama ve ona bağlı kullanımlar olarak yeniden kurulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"hafif topallama"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"topallayan, toynak ağrısıyla yürümekten çekinen veya ayağını sert zeminden sakınan at"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"hayvanın sırtında yara açmayan eyer"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"aksayışını gözet ve ağırdan al"}],"lexicalization_note":"Tek sözcüklü hafif topallama anlamı, atın yürüyüşü ile eyer ve emir kalıplarına bağlı anlamlardan açıkça ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan ilişkiler genel aksama, uzuv hastalığı, toynak anatomisi ve koruma bağlantısını ayırır. Keçi hastalıkları, düzensiz yürüyüş, binme ve öteki kök içi dallar daha uzak alan ortaklıklarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal hafif dereceyi ve toynak ağrısına bağlı çekingen yürüyüşü belirginleştirir; komşu dal daha genel aksama durumunda kalır.","focus_only":"Toynak ağrısıyla yürümekten çekinme ile yara açmayan eyer ve emir gibi bağımlı kullanımları da kapsar.","gloss":"hafif topallama ile hayvandaki genel aksama","neighbor_only":"Hayvandaki aksama veya eziklik daha genel bir durum adı olarak verilir ve koruyucu yan kullanımlar taşımaz.","neighbor_ref":"root_000448/B009","relation_type":"near_synonym","shared_zone":"Her iki dal hayvanın, özellikle atın, aksayan veya topallayan yürüyüşünü anlatır."},{"boundary_match":"partial","distinction":"Bu dal ağrının yürüyüşteki belirtisini ve sakınma davranışını anlatır; komşu dal ise ağrıyı doğuran hastalık veya yaralanmanın kendisini adlandırır.","focus_only":"Ağrıya verilen topallama ve yürümekten çekinme tepkisi ile ona bağlı kullanımlar merkezde yer alır.","gloss":"ağrılı yürüyüş ile uzuvdaki hastalık","neighbor_only":"Omuz veya toynağı etkileyen hastalığı ve taşın tırnak ya da toynağı çizmesini doğrudan adlandırır.","neighbor_ref":"root_001546/B006","relation_type":"near_neighbor","shared_zone":"İki dal toynak veya başka bir uzuvdaki ağrı ve bunun hayvan üzerindeki etkisiyle ilgilidir."},{"boundary_match":"field_only","distinction":"Ortak alan toynaktır; bu dal toynağa bağlı ağrı ve yürüyüş davranışını, komşu dal ise anatomik uzvun kendisini tanımlar.","focus_only":"Toynak ağrısının yol açtığı topallama ve sakınan yürüyüşü anlatır.","gloss":"toynak ağrısıyla yürüme ile toynak","neighbor_only":"Toynağın kendisini, biçimini ve zeminde iz açan uzuv olmasını adlandırır.","neighbor_ref":"root_000341/B002","relation_type":"same_field","shared_zone":"Her iki dal atın veya başka bir hayvanın toynağını ortak katılımcı olarak içerir."},{"boundary_match":"field_only","distinction":"Bu dal bir yürüyüş durumu ve ağrı tepkisidir; komşu dal ise toynağın sağ ve sol yanlarını gösteren anatomik addır.","focus_only":"Hayvanın ağrı nedeniyle aksaması ve sert zeminde ayağını sakınması bulunur.","gloss":"toynak ağrısı ile toynağın yanları","neighbor_only":"Toynağın iki yanındaki belirli anatomik bölümleri adlandırır.","neighbor_ref":"root_000358/B010","relation_type":"same_field","shared_zone":"Her iki dal toynak yapısı ve hayvanın ayağı çevresindeki aynı somut alana bağlıdır."},{"boundary_match":"thematic_only","distinction":"Koruma bu dalda yalnızca bazı at ve eyer kullanımlarının bağımlı yönüdür; komşu dalda ise bütün kavramın genel çekirdeğidir.","focus_only":"Hafif topallama ve ağrı yüzünden sakınarak yürüme, dalın temel kimliğini oluşturur.","gloss":"aksayarak sakınma ile genel koruma","neighbor_only":"Her tür varlığı zarardan korumak için araya araç veya engel koyan genel işlemi tanımlar.","neighbor_ref":"root_001677/B001","relation_type":"thematic","shared_zone":"Atın ayağını sert zeminden sakınması ve eyerin yara açmaması koruma düşüncesiyle ilişki kurar."}],"source_phrase_ar":"الوقى هو الظلع اليسير (maqayis)؛ فرس واق إذا كان ظالعا (ayn)؛ ق على ظلعك أي الزمه (sihah)؛ فرس واق إذا كان يهاب المشي من وجع يجده في حافره (sihah)؛ سرج واق إذا لم يكن معقرا (sihah;tahdhib)؛ لا تقي بالجدجد أي لا تشتكي حزونة الأرض (tahdhib)","source_summary":"Toplu kaynak ifadesi hafif topallamayı çekirdek yapar ve bunu topallayan, toynak ağrısı yüzünden yürümekten çekinen ya da sert zeminde ayağını sakınan atla açımlar. Aksamaya göre davranma, sert zeminden yakınmama ve yara açmayan eyer kullanımları aynı kümede yer alan fakat çekirdeğe bağımlı yan kullanımlardır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الوَقَى بمعنى الظلع اليسير، والفرس الواقي إذا يهاب المشي أو يقي حافره الموضع الغليظ، والسرج الواقي غير المعقر","what_is_not_ar":"لا يدخل فيه الوقاية العامة ولا التقوى ولا اسم الصرد"},"support_links":[]},{"boundary":"Dal yalnızca bu adlandırılmış ağırlık ölçüsü ve onun biçimleriyle sınırlıdır; genel tartma eylemine, her türlü miktara veya modern bir ölçü adına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001677/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَقْوَى","morph_features":"STEM|POS:N|LEM:taqowaY|ROOT:wqy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:12:3:3","qac_word_ref":"96:12:3","surface_ar":"تَّقْوَىٰٓ"}],"gloss":"kırk gümüş para ağırlığındaki, yağda yedi birimlik biçimi bulunan ölçü","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel biçim, belirli bir ağırlık ölçüsüdür ve para hesabında kırk gümüş paranın ağırlığına eşitlenir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başındaki ses düşmüş biçim, yağ ölçümünde kullanılan ve yedi temel ağırlık birimine eşit sayılan ayrı bir değeri bildirir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başlangıç sesini koruyan biçim daha düzgün kabul edilir ve ölçü adının iki çoğul söylenişi kaydedilir."}}],"root_ar":"و ق ي","root_id":"root_001677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ölçü ailesinin iki bağlama göre değişen değerini tek açıklayıcı karşılıkta birlikte göstermenin gerektiği yerlerde kullanılır.","boundary_detail":"Dal yalnızca bu adlandırılmış ağırlık ölçüsü ve onun biçimleriyle sınırlıdır; genel tartma eylemine, her türlü miktara veya modern bir ölçü adına genişletilmez.","branch_image_ar":"الأوقية وزن معلوم","concept_gloss":"kırk gümüş para ağırlığındaki, yağda yedi birimlik biçimi bulunan ölçü","contextual_glosses":[{"applicability":"Para ağırlığının esas alındığı ilk biçim ve kullanım kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölçünün ağırlık niteliğini ve kırk gümüş para ağırlığına eşit değerini korur."},"facet_ids":["F001"],"text":"kırk gümüş para ağırlığına denk ölçü","usage_role":"contextual"},{"applicability":"Başındaki ses düşmüş biçimin yağ ölçümündeki özel değeri açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yağ bağlamını, ağırlık ölçüsü olmasını ve yedi temel birime eşit değeri korur."},"facet_ids":["F002"],"text":"yağ için yedi temel birimlik ağırlık ölçüsü","usage_role":"explanatory"},{"applicability":"Ölçü adının birden fazla çoğul söylenişi bulunduğu açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Söz konusu biçimlerin aynı ağırlık ölçüsü adının çoğulları olmasını korur."},"facet_ids":["F003"],"text":"bu ağırlık ölçüsünün çoğul biçimleri","usage_role":"explanatory"}],"definition":"Bir kullanımda kırk gümüş paranın ağırlığına, başındaki ses düşmüş başka bir biçim ve kullanımda ise yağ için yedi temel ağırlık birimine eşit kabul edilen ölçü. İlk biçim daha düzgün sayılır ve birden çok çoğul biçimi vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel biçim, belirli bir ağırlık ölçüsüdür ve para hesabında kırk gümüş paranın ağırlığına eşitlenir."},{"facet_id":"F002","role":"source_variant","statement":"Başındaki ses düşmüş biçim, yağ ölçümünde kullanılan ve yedi temel ağırlık birimine eşit sayılan ayrı bir değeri bildirir."},{"facet_id":"F003","role":"source_variant","statement":"Başlangıç sesini koruyan biçim daha düzgün kabul edilir ve ölçü adının iki çoğul söylenişi kaydedilir."}],"identity_rationale":"Kaynak ifadesi dalı bilinen bir ağırlık ölçüsü olarak doğrular, ancak tek ve değişmez bir nicelik vermez. Bir kullanım kırk gümüş para ağırlığını, başındaki ses düşmüş başka bir biçim ise yağ için yedi temel ağırlık birimini gösterir; tanım bu bağlam farkını açıkça korumalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kırk gümüş para ağırlığına eşit bilinen ölçü"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"yağ için yedi temel ağırlık birimine eşit ölçü"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bu ağırlık ölçüsü adının çoğul biçimleri"}],"lexicalization_note":"Tanım, iki sözcük biçimine bağlı farklı ölçü değerlerini ve çoğul biçimleri ayırır; bunlardan genel bir kök anlamı çıkarmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yayımlananlar genel ağırlık, küçük para ölçüsü, başka geleneksel birim, hacim-miktar ölçüsü ve ayar standardı sınırlarını gösterir. Artış ve çok büyük tahıl ölçüsü daha uzaktır; öteki kök içi dallar anlamsal olarak ayrıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal değerleri ve sözcük biçimleri belirlenmiş tek bir geleneksel ölçüyü adlandırır; komşu dal ağırlık ve tartma alanının genel kavramıdır.","focus_only":"Bağlama göre kırk gümüş para veya yedi temel birim değerini taşıyan belirli bir ölçü adıdır.","gloss":"özel ağırlık ölçüsü ile genel tartma","neighbor_only":"Ağırlık, tartı aracı ve bir şeye ağırlığını verme gibi genel ölçme alanını kapsar.","neighbor_ref":"root_000202/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal belirlenmiş ağırlık ve ölçme düşüncesinde buluşur."},{"boundary_match":"partial","distinction":"Ölçülerin adları ve değerleri ayrıdır: bu dal kırk paralık değeri ve yağdaki değişkeyi taşırken komşu dal çoğunlukla beş paralık küçük miktarı bildirir.","focus_only":"Para hesabında kırk gümüş para ağırlığına veya yağda yedi birime bağlanan ölçüdür.","gloss":"kırk paralık ölçü ile beş paralık ölçü","neighbor_only":"Altın veya gümüş için kullanılan, çoğunlukla beş gümüş para ağırlığıyla açıklanan daha küçük ölçüdür.","neighbor_ref":"root_001570/B004","relation_type":"near_neighbor","shared_zone":"İki dal da değerli maden veya para üzerinden açıklanan geleneksel ağırlık ölçüleridir."},{"boundary_match":"partial","distinction":"Bu dalın ölçü adı ve verilen değerleri kendine özgüdür; komşu dal başka birim adını ve ağırlığın yanında hacim kullanımını kapsar.","focus_only":"İki sözcük biçimi ve iki bağlamsal değeri bulunan belirli bir ağırlık ölçüsüdür.","gloss":"iki ayrı geleneksel ölçü adı","neighbor_only":"Başka bir adla anılan, hem ağırlık hem hacim ölçüsü olabilen ayrı bir geleneksel birimdir.","neighbor_ref":"root_001449/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal belirli adları, tekil ve çoğul biçimleri bulunan geleneksel ölçü birimleridir."},{"boundary_match":"partial","distinction":"Bu dal ağırlığa ve belirli değerlere bağlıdır; komşu dal hacim ile para miktarı arasında daha geniş bir ölçüm alanına yayılır.","focus_only":"Öncelikle ağırlık ölçüsüdür ve iki özel sayısal değere bağlanır.","gloss":"ağırlık ölçüsü ile hacim ve miktar ölçüsü","neighbor_only":"Hacim ölçüsünü, yarım başka bir hacim ölçüsünü ve para miktarını birlikte kapsayabilir.","neighbor_ref":"root_001224/B007","relation_type":"near_neighbor","shared_zone":"İki dal da sayılabilir veya ölçülebilir bir miktarı geleneksel birimle belirtir."},{"boundary_match":"field_only","distinction":"Bu dal ölçülen miktarı bildiren birimdir; komşu dal ise ölçü araçlarının ve paraların doğruluğunu belirleyen ayar standardıdır.","focus_only":"Kendi adı, biçimleri ve geleneksel değerleri bulunan ölçü birimini tanımlar.","gloss":"ölçü birimi ile ölçü ayarı","neighbor_only":"Ölçekleri ve paraları denetlemeye yarayan ayarı veya ölçünleme işlemini tanımlar.","neighbor_ref":"root_001066/B013","relation_type":"same_field","shared_zone":"Her iki dal doğru ağırlık ve ölçü değerinin belirlenmesi alanındadır."}],"source_phrase_ar":"الأوقية في الحديث أربعون درهما (sihah;tahdhib)؛ الوقية وزن من أوزان الدهن وهي سبعة مثاقيل (tahdhib)؛ اللغة الجيدة أوقية وجمعها أواقي وأواق (tahdhib)","source_summary":"Toplu kaynak anlatımı, aynı ölçü ailesinde bağlama ve sözcük biçimine göre iki değer aktarır: para hesabında kırk gümüş para ağırlığı ve yağ hesabında yedi temel ağırlık birimi. Başlangıç sesini taşıyan biçim daha düzgün kabul edilir; ölçü adının iki çoğul biçimi de verilir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الأوقية والأواقي بوصفها وزنا معلوما للدراهم أو الدهن","what_is_not_ar":"لا يدخل فيه الوقاية ولا التقوى ولا الواقي بمعنى الصرد"},"support_links":[]},{"boundary":"Dal yalnızca örümcek kuşunun bu iki adına ve adlandırma açıklamasına aittir; koruyan kişi, topallayan at veya yara açmayan eyer anlamlarına geçmez.","branch_kind":"non_bare","branch_ref":"root_001677/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَقْوَى","morph_features":"STEM|POS:N|LEM:taqowaY|ROOT:wqy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:12:3:3","qac_word_ref":"96:12:3","surface_ar":"تَّقْوَىٰٓ"}],"gloss":"örümcek kuşu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözcük, örümcek kuşunu adlandıran özel bir kuş adıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuş adı, son sesi bulunan daha uzun ve bu sesin düştüğü daha kısa iki biçimde kullanılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Adın kuşa verilmesi, yürürken adımlarını fazla açmayan kısa adımlı yürüyüşüyle açıklanır."}}],"root_ar":"و ق ي","root_id":"root_001677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kuş türünün Türkçedeki doğal adı olarak dalın adlandırma çekirdeğini doğrudan karşılar.","boundary_detail":"Dal yalnızca örümcek kuşunun bu iki adına ve adlandırma açıklamasına aittir; koruyan kişi, topallayan at veya yara açmayan eyer anlamlarına geçmez.","branch_image_ar":"الواقي اسم للصرد","concept_gloss":"örümcek kuşu","contextual_glosses":[{"applicability":"Kuş adının yürüyüş biçimiyle ilişkilendirilen açıklaması da bağlamda görünür kılınmak istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kuş türünü ve adlandırmaya gerekçe gösterilen kısa adımlı yürüyüş özelliğini birlikte korur."},"facet_ids":["F001","F003"],"text":"kısa adımlarla yürüyen örümcek kuşu","usage_role":"explanatory"}],"definition":"Örümcek kuşunun, biri son sesi koruyan diğeri bu sesi düşüren iki biçimde söylenen adı. Adlandırma, kuşun yürürken adımlarını fazla açmamasıyla açıklanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözcük, örümcek kuşunu adlandıran özel bir kuş adıdır."},{"facet_id":"F002","role":"source_variant","statement":"Kuş adı, son sesi bulunan daha uzun ve bu sesin düştüğü daha kısa iki biçimde kullanılır."},{"facet_id":"F003","role":"associated_use","statement":"Adın kuşa verilmesi, yürürken adımlarını fazla açmayan kısa adımlı yürüyüşüyle açıklanır."}],"identity_rationale":"Kaynak ifadesi dalı doğrudan örümcek kuşunun adı olarak verir, adın son sesi bulunan ve düşmüş iki biçimini kaydeder ve adlandırmayı kuşun yürürken adımlarını fazla açmamasına bağlar. Geçici çerçeve bu sınırı doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"örümcek kuşu; aynı kuş adının uzun ve kısalmış biçimleri"}],"lexicalization_note":"Tanım, kuşa verilmiş iki özel ad biçimiyle sınırlı tutulur ve bunlardan genel bir koruma ya da yürüme anlamı türetilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan dört karşılaştırma kuş adları arasındaki tür ayrımını yeterince gösterir. Öteki kuş adayları da yalnızca aynı alanı paylaşır; kurt adı ile koruma, ağırlık ve hayvan yürüyüşü dalları farklı kimliklerdir.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Ortaklık yalnızca kuş adı olmalarıdır; bu dal örümcek kuşunu, komşu dal ise ibibiği adlandırır ve türler birbirinin yerine geçmez.","focus_only":"Örümcek kuşunu ve onun kısa adımlı yürüyüşüne bağlanan adını belirtir.","gloss":"örümcek kuşu ile ibibik","neighbor_only":"İbibik kuşunu ve o kuşa ait ad biçimlerini belirtir.","neighbor_ref":"root_001580/B005","relation_type":"same_field","shared_zone":"Her iki dal belirli bir kuş türünü doğrudan adlandıran sözleri içerir."},{"boundary_match":"field_only","distinction":"Bu dal örümcek kuşunun adıdır; komşu dal tarla kuşunun adıdır. Aynı üst alanda bulunsalar da tür kimlikleri ayrıdır.","focus_only":"Kısa adımlı yürüyüşüyle açıklanan örümcek kuşu adı merkezde yer alır.","gloss":"örümcek kuşu ile tarla kuşu","neighbor_only":"Tarla kuşunu ve ona ait farklı ad biçimlerini belirtir.","neighbor_ref":"root_001195/B003","relation_type":"same_field","shared_zone":"İki dal da küçük kuş türlerine verilmiş adları ve bu adların biçimlerini ele alır."},{"boundary_match":"field_only","distinction":"Anlamsal ortaklık kuş kategorisiyle sınırlıdır; dallar büyüklük, yapı ve tür bakımından bütünüyle farklı kuşları adlandırır.","focus_only":"Örümcek kuşunun özel adını bildirir.","gloss":"örümcek kuşu ile deve kuşu","neighbor_only":"Çok daha büyük ve uçamayan deve kuşunun tür adını bildirir.","neighbor_ref":"root_001525/B006","relation_type":"same_field","shared_zone":"Her iki dal bir kuş türünün doğrudan adı olarak kullanılır."},{"boundary_match":"field_only","distinction":"Bu dalın göndergesi örümcek kuşudur; komşu dal başka bir küçük kuş türünü adlandırır ve ortak kuş alanı tür özdeşliği oluşturmaz.","focus_only":"Örümcek kuşunu adlandırır ve adını kuşun yürüyüşüyle ilişkilendirir.","gloss":"örümcek kuşu ile bir serçe türü","neighbor_only":"Serçelere benzeyen başka bir küçük kuş türünün adını bildirir.","neighbor_ref":"root_000465/B008","relation_type":"same_field","shared_zone":"İki dal da küçük kuşlardan birine verilmiş sözlü adları taşır."}],"source_phrase_ar":"الواقي الصرد (sihah;tahdhib)؛ الواق بكسر القاف بلا ياء (sihah)؛ قيل للصرد واق لأنه لا ينبسط في مشيه (tahdhib)","source_summary":"Kaynakların ortak anlatımı bu sözcüğü örümcek kuşunun adı olarak tanımlar ve son sesi bulunan biçimin yanında o sesin düştüğü kısa biçimi de kaydeder. Adın nedeni, kuşun yürürken adımlarını fazla açmaması olarak açıklanır.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الواقي والواق اسما للصرد","what_is_not_ar":"لا يدخل فيه الواقي بمعنى الدافع ولا الفرس الواقي ولا السرج الواقي"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["96:12:1"],"branch_refs":[],"candidate_id":"cand_aa430d4f03ca582ca408","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:12:1:alternative-widening","source_type":"word_analysis","support_ids":["sup_1b7bba50a42acdd44e1b","sup_4e8300394c4621210421"],"title":"disjunction widens into a second positive option","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:1","qac_refs":["96:12:1:1"],"status":"accepted"}},{"anchor_refs":["96:12:1"],"branch_refs":[],"candidate_id":"cand_5bfb51e19d402d6f7a88","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:12:1:branch-distinction","source_type":"word_analysis","support_ids":["sup_4e8300394c4621210421","sup_fc4737a8012200c27699"],"title":"commanding is distinct from being guided","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:1","qac_refs":["96:12:1:1"],"status":"accepted"}},{"anchor_refs":["96:12:1"],"branch_refs":[],"candidate_id":"cand_7d0cd44a7a836574f8b6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:12:1:conditional-coordination","source_type":"word_analysis","support_ids":["sup_0fa31a8104152f95db2b","sup_4e8300394c4621210421"],"title":"second branch remains under the prior question","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:1","qac_refs":["96:12:1:1"],"status":"accepted"}},{"anchor_refs":["96:12:1"],"branch_refs":[],"candidate_id":"cand_6aca1d1f55045e918841","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:12:1:visible-boundary-dependency","source_type":"word_analysis","support_ids":["sup_4e8300394c4621210421","sup_a3c9a528969751459ba7"],"title":"ayah boundary stays grammatically open","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:1","qac_refs":["96:12:1:1"],"status":"accepted"}},{"anchor_refs":["96:12:2"],"branch_refs":[],"candidate_id":"cand_8c1a54f65bfd8ba8046d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:12:2:carried-active-subject","source_type":"word_analysis","support_ids":["sup_9b014bbfaca447b46945","sup_a95ca88e51e03a4efad7"],"title":"same implied subject becomes an agent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:2","qac_refs":["96:12:2:1"],"status":"accepted"}},{"anchor_refs":["96:12:2"],"branch_refs":[],"candidate_id":"cand_d68c5ec8558df112f115","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:12:2:command-protection-pairing","source_type":"word_analysis","support_ids":["sup_9b014bbfaca447b46945","sup_ff374018295384cddddd"],"title":"command and guarding are compressed together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:2","qac_refs":["96:12:2:1"],"status":"accepted"}},{"anchor_refs":["96:12:2"],"branch_refs":[],"candidate_id":"cand_808f2438cb207dba8418","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:12:2:directive-not-consultative","source_type":"word_analysis","support_ids":["sup_5a3df80eaf344120b291","sup_9b014bbfaca447b46945"],"title":"Form I selects directive authority","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:2","qac_refs":["96:12:2:1"],"status":"accepted"}},{"anchor_refs":["96:12:2"],"branch_refs":[],"candidate_id":"cand_1735d730dee29f35151b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:12:2:guidance-to-command-boundary","source_type":"word_analysis","support_ids":["sup_6d3f162bff8f8f66ceaf","sup_9b014bbfaca447b46945"],"title":"boundary shifts from state to volitional act","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:2","qac_refs":["96:12:2:1"],"status":"accepted"}},{"anchor_refs":["96:12:2"],"branch_refs":[],"candidate_id":"cand_f0b7b48d1fc354e233e1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:12:2:moral-command-formula","source_type":"word_analysis","support_ids":["sup_5d1138db682907e21efc","sup_9b014bbfaca447b46945"],"title":"same construction enters public moral command","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:2","qac_refs":["96:12:2:1"],"status":"accepted"}},{"anchor_refs":["96:12:2"],"branch_refs":[],"candidate_id":"cand_4d05500629e59cf61ce7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:12:2:objectless-content-frame","source_type":"word_analysis","support_ids":["sup_9b014bbfaca447b46945","sup_dc16276e997b46cfe553"],"title":"missing recipient centers the commanded content","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:2","qac_refs":["96:12:2:1"],"status":"accepted"}},{"anchor_refs":["96:12:2"],"branch_refs":[],"candidate_id":"cand_9699a72e147cacfe313a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:12:2:perfect-hypothetical-act","source_type":"word_analysis","support_ids":["sup_805a94f5c1366b518d0f","sup_9b014bbfaca447b46945"],"title":"perfect form weighs a completed counter-scenario","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:2","qac_refs":["96:12:2:1"],"status":"accepted"}},{"anchor_refs":["96:12:2"],"branch_refs":[],"candidate_id":"cand_95b91350ea02658fbdb2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:12:2:positive-public-pivot","source_type":"word_analysis","support_ids":["sup_9b014bbfaca447b46945","sup_defca6c918b3309e66ce"],"title":"private orientation becomes public command","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:2","qac_refs":["96:12:2:1"],"status":"accepted"}},{"anchor_refs":["96:12:2"],"branch_refs":[],"candidate_id":"cand_f75f8b504d90a2b675e1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:12:2:taqwa-endpoint-contrast","source_type":"word_analysis","support_ids":["sup_9b014bbfaca447b46945","sup_fd5bb0cc96129f2977fe"],"title":"taqwā becomes the named command content","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:2","qac_refs":["96:12:2:1"],"status":"accepted"}},{"anchor_refs":["96:12:3"],"branch_refs":[],"candidate_id":"cand_abd391a8e76f17d52eca","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"96:12:3:boundary-transition","source_type":"word_analysis","support_ids":["sup_6af2efb6637fdd2a5e68","sup_d5495a1cb0bbe6826bfd"],"title":"orientation becomes transmitted guardedness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:3","qac_refs":["96:12:3:1","96:12:3:2","96:12:3:3"],"status":"accepted"}},{"anchor_refs":["96:12:3"],"branch_refs":[],"candidate_id":"cand_acd2ecb0dc7ed8d6cf23","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"96:12:3:command-protection-field","source_type":"word_analysis","support_ids":["sup_02abd7dcbf688778d5ae","sup_d5495a1cb0bbe6826bfd"],"title":"command language meets protective response","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:3","qac_refs":["96:12:3:1","96:12:3:2","96:12:3:3"],"status":"accepted"}},{"anchor_refs":["96:12:3"],"branch_refs":[],"candidate_id":"cand_db06bf850822aecf6ba9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"96:12:3:content-complement","source_type":"word_analysis","support_ids":["sup_d5495a1cb0bbe6826bfd","sup_f86904989cc523745931"],"title":"prefixed phrase supplies the command content","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:3","qac_refs":["96:12:3:1","96:12:3:2","96:12:3:3"],"status":"accepted"}},{"anchor_refs":["96:12:3"],"branch_refs":[],"candidate_id":"cand_c245f69b0045104d629c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"96:12:3:definite-established-principle","source_type":"word_analysis","support_ids":["sup_622a2ef9f52bde632ca7","sup_d5495a1cb0bbe6826bfd"],"title":"definiteness names a known principle","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:3","qac_refs":["96:12:3:1","96:12:3:2","96:12:3:3"],"status":"accepted"}},{"anchor_refs":["96:12:3"],"branch_refs":[],"candidate_id":"cand_b6ef97c08f0e22144387","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"96:12:3:forward-contrast","source_type":"word_analysis","support_ids":["sup_bb24974eb0418be071f0","sup_d5495a1cb0bbe6826bfd"],"title":"positive guardedness anticipates refusal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:3","qac_refs":["96:12:3:1","96:12:3:2","96:12:3:3"],"status":"accepted"}},{"anchor_refs":["96:12:3"],"branch_refs":[],"candidate_id":"cand_0640252503d1c1b7bf47","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"96:12:3:local-branch-selection","source_type":"word_analysis","support_ids":["sup_0ba4fd5898aab6d1122c","sup_d5495a1cb0bbe6826bfd"],"title":"large protection family is concentrated into this noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:3","qac_refs":["96:12:3:1","96:12:3:2","96:12:3:3"],"status":"accepted"}},{"anchor_refs":["96:12:3"],"branch_refs":[],"candidate_id":"cand_83476cbf2c703e14233c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"96:12:3:long-a-pairing","source_type":"word_analysis","support_ids":["sup_2110bf4ff5a1a7ff21e5","sup_d5495a1cb0bbe6826bfd"],"title":"long final sound pairs guidance and protective awareness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:3","qac_refs":["96:12:3:1","96:12:3:2","96:12:3:3"],"status":"accepted"}},{"anchor_refs":["96:12:3"],"branch_refs":[],"candidate_id":"cand_5ac19ff0a036b2aa0f90","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"96:12:3:moral-action-echoes","source_type":"word_analysis","support_ids":["sup_4bb2d4220ef8c881bd4b","sup_d5495a1cb0bbe6826bfd"],"title":"taqwā functions as practical resource","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:3","qac_refs":["96:12:3:1","96:12:3:2","96:12:3:3"],"status":"accepted"}},{"anchor_refs":["96:12:3"],"branch_refs":[],"candidate_id":"cand_dcf89792cfbbe4a859f4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"96:12:3:positive-branch-closure","source_type":"word_analysis","support_ids":["sup_29d9a5999d2825447ba1","sup_d5495a1cb0bbe6826bfd"],"title":"final noun closes the positive hypothetical branch","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:3","qac_refs":["96:12:3:1","96:12:3:2","96:12:3:3"],"status":"accepted"}},{"anchor_refs":["96:12:3"],"branch_refs":[],"candidate_id":"cand_fa7b85cff8b9a81548a6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"96:12:3:protective-shield-image","source_type":"word_analysis","support_ids":["sup_00d6dc528e209b930b44","sup_d5495a1cb0bbe6826bfd"],"title":"shield image becomes moral guardedness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:3","qac_refs":["96:12:3:1","96:12:3:2","96:12:3:3"],"status":"accepted"}},{"anchor_refs":["96:12:3"],"branch_refs":[],"candidate_id":"cand_ba4a6a42d0425ffbd352","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"96:12:3:reflexive-self-guarding","source_type":"word_analysis","support_ids":["sup_ab94f6804bcce1221785","sup_d5495a1cb0bbe6826bfd"],"title":"the commanded content requires self-directed guarding","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:3","qac_refs":["96:12:3:1","96:12:3:2","96:12:3:3"],"status":"accepted"}},{"anchor_refs":["96:12:3"],"branch_refs":[],"candidate_id":"cand_90fd60acd076553a7d73","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"96:12:3:visible-fusion","source_type":"word_analysis","support_ids":["sup_c7e6d9862ff14c364edd","sup_d5495a1cb0bbe6826bfd"],"title":"written fusion visibly binds content to command","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:12:3","qac_refs":["96:12:3:1","96:12:3:2","96:12:3:3"],"status":"accepted"}},{"anchor_refs":["96:12:2"],"branch_refs":[],"candidate_id":"cand_4016d031b5a55037209c","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000051"],"scope":"focus_ayah","source_local_id":"96:12:2:1","source_type":"qac_morpheme","support_ids":["sup_413b4074cf15a71978fb"],"title":"QAC root occurrence: ء م ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["96:12:3"],"branch_refs":[],"candidate_id":"cand_4aa21c3a9b8615e18013","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"96:12:3:3","source_type":"qac_morpheme","support_ids":["sup_191d3923d3a2a2b21501"],"title":"QAC root occurrence: و ق ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["96:12"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"96:12","branch_refs":["root_000051/B002","root_001677/B002"],"candidate_id":"cand_83310c9496c9a84accae","commentary_obligation":"review","hft_ref":"hft_57132792e88cdda07e47","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_directive_as_self_protection","source_type":"hft","support_ids":["sup_933237a2713c380338f8"],"title":"baseline_directive_as_self_protection","trust":"legacy_unbound"},{"anchor_refs":["96:12"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"96:12","branch_refs":["root_000051/B003","root_001677/B001"],"candidate_id":"cand_b7506fac0ab2231cc020","commentary_obligation":"review","hft_ref":"hft_3571fdd27730d9e7cdf9","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_authority_measured_by_shelter","source_type":"hft","support_ids":["sup_9be606ce16bec1a0a739"],"title":"baseline_authority_measured_by_shelter","trust":"legacy_unbound"},{"anchor_refs":["96:12"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"96:12","branch_refs":["root_000051/B007","root_001677/B002"],"candidate_id":"cand_e01563ebfa01aeb74ee1","commentary_obligation":"review","hft_ref":"hft_cec3a4f67a7baa56e126","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_deliberated_guarding","source_type":"hft","support_ids":["sup_6738684846d79770b1f5"],"title":"baseline_deliberated_guarding","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"أَوْ أَمَرَ بِٱلتَّقْوَىٰٓ","qac_morphemes":[{"lemma_ar":"أَو","morph_features":"STEM|POS:CONJ|LEM:>aw","morpheme_role":"STEM","pos":"CONJ","qac_ref":"96:12:1:1","qac_word_ref":"96:12:1","root_ar":"","surface_ar":"أَوْ"},{"lemma_ar":"أَمَرَ","morph_features":"STEM|POS:V|PERF|LEM:>amara|ROOT:Amr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:12:2:1","qac_word_ref":"96:12:2","root_ar":"ء م ر","surface_ar":"أَمَرَ"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"96:12:3:1","qac_word_ref":"96:12:3","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"96:12:3:2","qac_word_ref":"96:12:3","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"تَقْوَى","morph_features":"STEM|POS:N|LEM:taqowaY|ROOT:wqy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:12:3:3","qac_word_ref":"96:12:3","root_ar":"و ق ي","surface_ar":"تَّقْوَىٰٓ"}],"word_analysis_qac_refs":[["96:12:1:1"],["96:12:2:1"],["96:12:3:1","96:12:3:2","96:12:3:3"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["96:12:1","96:12:2","96:12:3"]},"focus_surface_evidence":{"arabic_uthmani":"أَوْ أَمَرَ بِٱلتَّقْوَىٰٓ","qac_morphemes":[{"lemma_ar":"أَو","morph_features":"STEM|POS:CONJ|LEM:>aw","morpheme_role":"STEM","pos":"CONJ","qac_ref":"96:12:1:1","qac_word_ref":"96:12:1","root_ar":"","surface_ar":"أَوْ"},{"lemma_ar":"أَمَرَ","morph_features":"STEM|POS:V|PERF|LEM:>amara|ROOT:Amr|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:12:2:1","qac_word_ref":"96:12:2","root_ar":"ء م ر","surface_ar":"أَمَرَ"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"96:12:3:1","qac_word_ref":"96:12:3","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"96:12:3:2","qac_word_ref":"96:12:3","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"تَقْوَى","morph_features":"STEM|POS:N|LEM:taqowaY|ROOT:wqy|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:12:3:3","qac_word_ref":"96:12:3","root_ar":"و ق ي","surface_ar":"تَّقْوَىٰٓ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["96:12:1:1"],["96:12:2:1"],["96:12:3:1","96:12:3:2","96:12:3:3"]],"word_analysis_refs":["96:12:1","96:12:2","96:12:3"],"word_rows":[{"analysis_record_ref":"96:12:1","analytic_gloss_range_en":"disjunctive coordinating particle that opens a second positive hypothetical branch under the earlier suspended question","analytic_root_gloss_range_en":null,"qac_refs":["96:12:1:1"],"root":{},"surface":{"arabic":"أَوْ","transliteration":"aw"}},{"analysis_record_ref":"96:12:2","analytic_gloss_range_en":"perfect active command verb in a hypothetical frame, with the recipient unexpressed and the commanded content supplied by the following prepositional phrase","analytic_root_gloss_range_en":"commanding, ordering, and affair or matter language; the local Form I verb selects directive command while broader affair pressure remains secondary","qac_refs":["96:12:2:1"],"root":{"arabic":"أ م ر","transliteration":"ʾ-m-r"},"surface":{"arabic":"أَمَرَ","transliteration":"amara"}},{"analysis_record_ref":"96:12:3","analytic_gloss_range_en":"preposition-bound definite abstract noun naming the commanded content as established, actionable protective awareness","analytic_root_gloss_range_en":"guarding, shielding, preserving, and reflexive moral self-protection; local grammar selects the taqwā self-guarding branch, not measure, bird-name, or gait branches","qac_refs":["96:12:3:1","96:12:3:2","96:12:3:3"],"root":{"arabic":"و ق ي","transliteration":"w-q-y"},"surface":{"arabic":"بِٱلتَّقْوَىٰٓ","transliteration":"bi-t-taqwā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["96:12"],"branch_refs":["root_000051/B002","root_001677/B002"],"candidate_id":"cand_83310c9496c9a84accae","evidence_scope":"focus_ayah","hft_ref":"hft_57132792e88cdda07e47","item_id":"baseline_directive_as_self_protection","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_directive_as_self_protection","support_id":"sup_933237a2713c380338f8"},{"anchor_refs":["96:12"],"branch_refs":["root_000051/B003","root_001677/B001"],"candidate_id":"cand_b7506fac0ab2231cc020","evidence_scope":"focus_ayah","hft_ref":"hft_3571fdd27730d9e7cdf9","item_id":"baseline_authority_measured_by_shelter","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_authority_measured_by_shelter","support_id":"sup_9be606ce16bec1a0a739"},{"anchor_refs":["96:12"],"branch_refs":["root_000051/B007","root_001677/B002"],"candidate_id":"cand_e01563ebfa01aeb74ee1","evidence_scope":"focus_ayah","hft_ref":"hft_cec3a4f67a7baa56e126","item_id":"baseline_deliberated_guarding","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_deliberated_guarding","support_id":"sup_6738684846d79770b1f5"}],"diagnostics":[],"lane_counts":{"global":8,"macro":12,"micro":3},"packet_summary":{"ayah_count":19,"focus_ref":"96:12","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ص ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":false,"target_occurrences":7,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"د ع و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000478","furuq_root_norm":"د ع و","furuq_source_root_norm":"د ع و","is_dominant":true,"target_occurrences":77,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000477","furuq_root_norm":"د ع ع","furuq_source_root_norm":"د ع ع","is_dominant":false,"target_occurrences":22,"target_rank":2}]},{"qac_root":"ن د و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001487","furuq_root_norm":"ن د ي","furuq_source_root_norm":"ن د ي","is_dominant":true,"target_occurrences":33,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001486","furuq_root_norm":"ن د و","furuq_source_root_norm":"ن د و","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001563","furuq_root_norm":"ن و د","furuq_source_root_norm":"ن و د","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ط و ع","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000956","furuq_root_norm":"ط و ع","furuq_source_root_norm":"ط و ع","is_dominant":true,"target_occurrences":96,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000706","furuq_root_norm":"س ط ع","furuq_source_root_norm":"س ط ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["96:1","96:2","96:3","96:4","96:5","96:6","96:7","96:8","96:9","96:10","96:11","96:12","96:13","96:14","96:15","96:16","96:17","96:18","96:19"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"96:12","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"96:12","lane":"micro","linguistic_source_ref":"96:12","surface_ref":"96:12","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"96:12","target_tokens":[["Ya",["96:12:1"]],["da",["96:12:1"]],["sakınmayı",["96:12:3"]],["emrediyorsa",["96:12:2"]]],"text":"Ya da sakınmayı emrediyorsa?"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":19,"id":"s096-p01-001-019","label":"Whole surah","number":1,"refs":["96:1","96:2","96:3","96:4","96:5","96:6","96:7","96:8","96:9","96:10","96:11","96:12","96:13","96:14","96:15","96:16","96:17","96:18","96:19"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:3:protective-shield-image","source_type":"word_analysis","support_id":"sup_00d6dc528e209b930b44","text":"{\"blocking_evidence\":null,\"headline\":\"shield image becomes moral guardedness\",\"reader_payoff\":\"The reader feels protective awareness as active guardedness with a shield-like image, while the local religious register prevents it from becoming merely physical protection.\",\"reason\":\"V4 accepts guarding and self-protective caution branches for {{ar:و ق ي}} ({{tr:w-q-y}}), while the local definite abstract noun selects moral protective awareness rather than a literal covering.\",\"representative_source_ids\":[\"QS-b0fb540e\",\"QS-be8414ef\",\"MS-78a1a152\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:3:command-protection-field","source_type":"word_analysis","support_id":"sup_02abd7dcbf688778d5ae","text":"{\"blocking_evidence\":null,\"headline\":\"command language meets protective response\",\"reader_payoff\":\"The reader sees authority and self-guarding compressed into the same clause, with 20:132 providing a concrete command-to-taqwā counterpart.\",\"reason\":\"The local syntax joins the command verb to the protection noun as content, while the 20:132 comparison remains a parallel rather than a controller of local grammar.\",\"representative_source_ids\":[\"QI-22d9a9b4\",\"QI-48acbc49\",\"ME-8436a710\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:3:local-branch-selection","source_type":"word_analysis","support_id":"sup_0ba4fd5898aab6d1122c","text":"{\"blocking_evidence\":null,\"headline\":\"large protection family is concentrated into this noun\",\"reader_payoff\":\"The reader sees a large root family concentrated into one final noun: a known principle, a reflexive practice, and a protection image at once.\",\"reason\":\"The local word belongs to the abstract noun profile and the self-protection branch; V4's measure, bird-name, and gait branches are real root branches but are not locally activated by this form and syntax.\",\"representative_source_ids\":[\"QI-3bd76899\",\"QY-531b84da\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:1:conditional-coordination","source_type":"word_analysis","support_id":"sup_0fa31a8104152f95db2b","text":"{\"blocking_evidence\":null,\"headline\":\"second branch remains under the prior question\",\"reader_payoff\":\"The reader notices that 96:12 is still inside the suspended question from 96:11, not beginning an independent assertion.\",\"reason\":\"QAC identifies {{ar:أَوْ}} ({{tr:aw}}) as coordinating another hypothetical condition under the earlier question, and attachment evidence confirms that it marks coordination beyond the local ayah.\",\"representative_source_ids\":[\"QG-6fa342e1\",\"MG-878ab8e1\",\"QT-84e71517\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"96:12:3:3","source_type":"qac_morpheme","support_id":"sup_191d3923d3a2a2b21501","text":"{\"lemma_ar\":\"تَقْوَى\",\"morph_features\":\"STEM|POS:N|LEM:taqowaY|ROOT:wqy|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"96:12:3:3\",\"qac_word_ref\":\"96:12:3\",\"root_ar\":\"و ق ي\",\"surface_ar\":\"تَّقْوَىٰٓ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:1:alternative-widening","source_type":"word_analysis","support_id":"sup_1b7bba50a42acdd44e1b","text":"{\"blocking_evidence\":null,\"headline\":\"disjunction widens into a second positive option\",\"reader_payoff\":\"The reader weighs the second branch as an additional positive possibility that can intensify the first without canceling it.\",\"reason\":\"The particle is genuinely disjunctive, so the escalation reading is retained only as widening from guidance to public command, not as replacement of ordinary coordination.\",\"representative_source_ids\":[\"QG-ee5d9405\",\"QS-6fb529bc\",\"MT-c3a89bdb\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:3:long-a-pairing","source_type":"word_analysis","support_id":"sup_2110bf4ff5a1a7ff21e5","text":"{\"blocking_evidence\":null,\"headline\":\"long final sound pairs guidance and protective awareness\",\"reader_payoff\":\"The reader hears guidance in 96:11 and protective awareness in 96:12 as paired positive endpoints before the next reversal.\",\"reason\":\"The CRITICAL rows tie the final long sound of the local noun to the guidance ending in 96:11, and the local position supports the paired endpoint reading.\",\"representative_source_ids\":[\"QF-3bbbeaed\",\"QP-ba95a454\",\"QE-b3a4e5f9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:3:positive-branch-closure","source_type":"word_analysis","support_id":"sup_29d9a5999d2825447ba1","text":"{\"blocking_evidence\":null,\"headline\":\"final noun closes the positive hypothetical branch\",\"reader_payoff\":\"The reader notices the ayah land on protective awareness before 96:13 reverses the movement with denial and turning away.\",\"reason\":\"The phrase is the last word of the ayah and the syntactic complement that resolves the open command frame before the contrastive next ayah.\",\"representative_source_ids\":[\"QT-6c9cea9c\",\"QT-ada06455\",\"MT-3d740d33\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"96:12:2:1","source_type":"qac_morpheme","support_id":"sup_413b4074cf15a71978fb","text":"{\"lemma_ar\":\"أَمَرَ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:>amara|ROOT:Amr|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"96:12:2:1\",\"qac_word_ref\":\"96:12:2\",\"root_ar\":\"ء م ر\",\"surface_ar\":\"أَمَرَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:3:moral-action-echoes","source_type":"word_analysis","support_id":"sup_4bb2d4220ef8c881bd4b","text":"{\"blocking_evidence\":null,\"headline\":\"taqwā functions as practical resource\",\"reader_payoff\":\"The reader sees protective awareness as a practical moral resource, with action-oriented parallels in 5:2 and 5:8 and the provision formula in 2:197.\",\"reason\":\"The cited references present the same abstract noun in practical directive or resource frames, which coheres with its local role as commanded content.\",\"representative_source_ids\":[\"QE-772aaced\",\"QE-80b50153\",\"MI-471ecb06\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:1","source_type":"word_analysis","support_id":"sup_4e8300394c4621210421","text":"{\"gloss_range\":\"disjunctive coordinating particle that opens a second positive hypothetical branch under the earlier suspended question\",\"prose\":\"{{ar:أَوْ}} ({{tr:aw}}) makes 96:12 begin as a dependent continuation rather than a fresh standalone claim. It carries the reader back to the suspended question and first positive branch in 96:11, then opens {{ar:أَمَرَ بِٱلتَّقْوَىٰ}} ({{tr:amara bi-t-taqwā}}) as a second weighed possibility. The particle therefore does more than add another item: it keeps guidance and commanding protective awareness inside one conditional frame, while letting the second branch widen the scene from personal orientation to public directive action. Its independent word shape, rather than a light bound connector, helps the ayah boundary remain visibly porous.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:أَوْ}} ({{tr:aw}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:2:directive-not-consultative","source_type":"word_analysis","support_id":"sup_5a3df80eaf344120b291","text":"{\"blocking_evidence\":null,\"headline\":\"Form I selects directive authority\",\"reader_payoff\":\"The reader senses the command as authoritative speech, while the local form keeps consultative and broad affair senses from taking over.\",\"reason\":\"The local Form I verb plus content complement licenses directive command; the broader root-family and affair language survive only as pressure around consequential speech because V4 has no available guardrail rows for this root.\",\"representative_source_ids\":[\"QS-d7f66843\",\"QS-fd7274d4\",\"QF-46493617\",\"MS-779242e9\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:2:moral-command-formula","source_type":"word_analysis","support_id":"sup_5d1138db682907e21efc","text":"{\"blocking_evidence\":null,\"headline\":\"same construction enters public moral command\",\"reader_payoff\":\"The reader sees the command-plus-preposition construction in 96:12 as kin to public moral injunction, including the equity-command formula in 3:21.\",\"reason\":\"The local construction has the same command-plus-preposition shape, while attachment evidence keeps the local content specifically as {{ar:بِٱلتَّقْوَىٰ}} ({{tr:bi-t-taqwā}}).\",\"representative_source_ids\":[\"QE-9125c6f4\",\"ME-2163be84\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:3:definite-established-principle","source_type":"word_analysis","support_id":"sup_622a2ef9f52bde632ca7","text":"{\"blocking_evidence\":null,\"headline\":\"definiteness names a known principle\",\"reader_payoff\":\"The reader sees the command aimed at the recognized principle of protective awareness, not an indefinite suggestion of caution.\",\"reason\":\"QAC and the noun instance identify the phrase as a definite abstract verbal noun, making the commanded content identifiable and conceptually compact.\",\"representative_source_ids\":[\"QG-e07a86d9\",\"MG-6d265271\",\"QF-559361d2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:3:boundary-transition","source_type":"word_analysis","support_id":"sup_6af2efb6637fdd2a5e68","text":"{\"blocking_evidence\":null,\"headline\":\"orientation becomes transmitted guardedness\",\"reader_payoff\":\"The reader sees the positive pair complete as guidance gives orientation and protective awareness gives guarded vigilance.\",\"reason\":\"The previous branch uses being upon guidance, while this phrase supplies transmitted command content; the final noun also closes syntax and prepares the 96:13 contrast.\",\"representative_source_ids\":[\"QB-538dfa40\",\"QB-b8f40af7\",\"QY-d691c024\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:2:guidance-to-command-boundary","source_type":"word_analysis","support_id":"sup_6d3f162bff8f8f66ceaf","text":"{\"blocking_evidence\":null,\"headline\":\"boundary shifts from state to volitional act\",\"reader_payoff\":\"The reader notices the full hinge: one carried subject, a completed command, and an open audience converge at the ayah boundary.\",\"reason\":\"The CRITICAL convergence is supported by the perfect verb, the absent explicit recipient, and the attachment note that the subject remains grammatically open across 96:11-12.\",\"representative_source_ids\":[\"QB-46c7d0e1\",\"QB-5bc151c3\",\"QY-5245b0b5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:2:perfect-hypothetical-act","source_type":"word_analysis","support_id":"sup_805a94f5c1366b518d0f","text":"{\"blocking_evidence\":null,\"headline\":\"perfect form weighs a completed counter-scenario\",\"reader_payoff\":\"The reader hears the command as a completed hypothetical action being weighed within the larger question.\",\"reason\":\"QAC identifies the local form as a perfect active Form I verb coordinated under the suspended conditional scenario.\",\"representative_source_ids\":[\"QG-b981dbc8\",\"MT-32ec5c63\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:2","source_type":"word_analysis","support_id":"sup_9b014bbfaca447b46945","text":"{\"gloss_range\":\"perfect active command verb in a hypothetical frame, with the recipient unexpressed and the commanded content supplied by the following prepositional phrase\",\"prose\":\"{{ar:أَمَرَ}} ({{tr:amara}}) is the hinge where the positive scenario changes from being upon guidance to issuing directive speech. The verb is perfect and active, so the suspended question weighs a completed hypothetical act by the same carried 3ms subject, while the recipient remains unexpressed. That gap makes {{ar:بِٱلتَّقْوَىٰ}} ({{tr:bi-t-taqwā}}) dominate the frame as the content commanded. The root field includes affair or matter language, but this Form I verb with a governed content complement selects unilateral command rather than reciprocal counsel: the broader pressure makes the speech feel consequential, not merely descriptive. Its pairing with protective awareness fits command-to-guarding patterns such as 20:132 and 66:6, while the same command-plus-preposition construction also recalls public moral injunction in 3:21.\",\"root_display\":\"{{ar:أ م ر}} ({{tr:ʾ-m-r}})\",\"root_gloss_range\":\"commanding, ordering, and affair or matter language; the local Form I verb selects directive command while broader affair pressure remains secondary\",\"surface_display\":\"{{ar:أَمَرَ}} ({{tr:amara}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:1:visible-boundary-dependency","source_type":"word_analysis","support_id":"sup_a3c9a528969751459ba7","text":"{\"blocking_evidence\":null,\"headline\":\"ayah boundary stays grammatically open\",\"reader_payoff\":\"The reader sees the verse boundary itself carry dependency, because the first word asks to be read backward before moving forward.\",\"reason\":\"The standalone particle opens the ayah while depending on the earlier conditional frame; nothing in the local grammar makes it a self-contained opener.\",\"representative_source_ids\":[\"QF-c422f931\",\"QT-4f4eeeee\",\"QB-aa354aa6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:2:carried-active-subject","source_type":"word_analysis","support_id":"sup_a95ca88e51e03a4efad7","text":"{\"blocking_evidence\":null,\"headline\":\"same implied subject becomes an agent\",\"reader_payoff\":\"The reader sees one implied person held across two frames: first imagined upon guidance, then imagined issuing command.\",\"reason\":\"Attachment evidence marks the subject as implicit and ambiguous but carried by 3ms agreement from the coordinated scenario, so naming the subject too tightly would overresolve it.\",\"representative_source_ids\":[\"QS-28aecb39\",\"QF-447d46a0\",\"QB-c64d1478\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:3:reflexive-self-guarding","source_type":"word_analysis","support_id":"sup_ab94f6804bcce1221785","text":"{\"blocking_evidence\":null,\"headline\":\"the commanded content requires self-directed guarding\",\"reader_payoff\":\"The reader notices the crossed roles: command comes from outside, but the content requires each recipient to practice self-guarding.\",\"reason\":\"The noun instance connects the word with the Form VIII self-guarding field, and V4 accepts the branch of placing oneself in protective caution.\",\"representative_source_ids\":[\"QS-1e08c308\",\"QS-5079f5ef\",\"QF-ca75b1c2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:3:forward-contrast","source_type":"word_analysis","support_id":"sup_bb24974eb0418be071f0","text":"{\"blocking_evidence\":null,\"headline\":\"positive guardedness anticipates refusal\",\"reader_payoff\":\"The reader sees protective awareness become the positive pole that 96:13 immediately answers with denial and turning away.\",\"reason\":\"The final content word stands at the close of the positive hypothetical branch, and the CRITICAL row supplies the concrete next-ayah contrast at 96:13.\",\"representative_source_ids\":[\"QB-1b7616a5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:3:visible-fusion","source_type":"word_analysis","support_id":"sup_c7e6d9862ff14c364edd","text":"{\"blocking_evidence\":null,\"headline\":\"written fusion visibly binds content to command\",\"reader_payoff\":\"The reader sees and hears the command content as tightly bound to its prefixed preposition.\",\"reason\":\"The surface form carries the prefixed {{ar:بـ}} ({{tr:bi-}}) and the assimilated article sound into a single written phrase governed by the verb.\",\"representative_source_ids\":[\"QF-85dd2a2c\",\"QP-3596c023\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:3","source_type":"word_analysis","support_id":"sup_d5495a1cb0bbe6826bfd","text":"{\"gloss_range\":\"preposition-bound definite abstract noun naming the commanded content as established, actionable protective awareness\",\"prose\":\"{{ar:بِٱلتَّقْوَىٰٓ}} ({{tr:bi-t-taqwā}}) resolves the open command frame. The prefixed {{ar:بـ}} ({{tr:bi-}}) makes the phrase the governed content of {{ar:أَمَرَ}} ({{tr:amara}}), so the local sense is not a free instrument phrase; the written fusion and doubled t sound make that attachment visible and audible. The noun is definite and abstract, naming not some caution but the recognized practice of protective awareness. Its Form VIII background and {{ar:و ق ي}} ({{tr:w-q-y}}) root image make that practice active and reflexive: someone may command it outwardly, but each hearer must take up guardedness inwardly. The broader root includes guarding, shielding, and preservation, yet the local noun selects moral self-protection rather than remote branches such as measure, bird name, or guarded gait. As the final word, its long-a close pairs protective awareness with guidance from 96:11 and prepares the reversal in 96:13, while echoes such as 20:132, 5:2, 5:8, and 2:197 show protective awareness as practical command-content rather than an ornamental virtue.\",\"root_display\":\"{{ar:و ق ي}} ({{tr:w-q-y}})\",\"root_gloss_range\":\"guarding, shielding, preserving, and reflexive moral self-protection; local grammar selects the taqwā self-guarding branch, not measure, bird-name, or gait branches\",\"surface_display\":\"{{ar:بِٱلتَّقْوَىٰٓ}} ({{tr:bi-t-taqwā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:2:objectless-content-frame","source_type":"word_analysis","support_id":"sup_dc16276e997b46cfe553","text":"{\"blocking_evidence\":null,\"headline\":\"missing recipient centers the commanded content\",\"reader_payoff\":\"The reader notices that the clause does not foreground who receives the command; it foregrounds what the command contains.\",\"reason\":\"The verb instance marks no explicit object and a following prepositional complement, so the commanded content is carried by {{ar:بِٱلتَّقْوَىٰ}} ({{tr:bi-t-taqwā}}).\",\"representative_source_ids\":[\"QG-07073f1f\",\"QG-cf5d6477\",\"QH-9723cfd2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:2:positive-public-pivot","source_type":"word_analysis","support_id":"sup_defca6c918b3309e66ce","text":"{\"blocking_evidence\":null,\"headline\":\"private orientation becomes public command\",\"reader_payoff\":\"The reader feels the second positive branch expand from inward or positional guidance to outward speech addressed to others.\",\"reason\":\"The local clause is verbal, and the verb of commanding creates a public speech situation distinct from the prior stative branch.\",\"representative_source_ids\":[\"QT-03919b1f\",\"QT-780e831e\",\"QB-35df427e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:3:content-complement","source_type":"word_analysis","support_id":"sup_f86904989cc523745931","text":"{\"blocking_evidence\":null,\"headline\":\"prefixed phrase supplies the command content\",\"reader_payoff\":\"The reader notices that the final phrase completes what is commanded, rather than floating as an instrument, place, or independent object.\",\"reason\":\"Attachment evidence syntactically forces the {{ar:بـ}} ({{tr:bi-}}) phrase as the governed content complement of {{ar:أَمَرَ}} ({{tr:amara}}), so any instrumental possibility is kept only as a rejected local alternative inside the narrowed topic.\",\"representative_source_ids\":[\"QG-7e18b607\",\"QG-b6fafd58\",\"MG-89b8cc78\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:1:branch-distinction","source_type":"word_analysis","support_id":"sup_fc4737a8012200c27699","text":"{\"blocking_evidence\":null,\"headline\":\"commanding is distinct from being guided\",\"reader_payoff\":\"The reader notices that commanding protective awareness is a distinct second act, not merely a restatement of being upon guidance.\",\"reason\":\"The conjunction before the verb marks a new coordinated branch, while the local verbal clause supplies a separate predicate.\",\"representative_source_ids\":[\"QT-baf44493\",\"QB-71ed3eef\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:2:taqwa-endpoint-contrast","source_type":"word_analysis","support_id":"sup_fd5bb0cc96129f2977fe","text":"{\"blocking_evidence\":null,\"headline\":\"taqwā becomes the named command content\",\"reader_payoff\":\"The reader notices the contrast with 20:132, where command leads toward taqwā, while here the command directly names protective awareness as its content.\",\"reason\":\"The governed phrase in 96:12 supplies the command content directly, so the 20:132 comparison is useful as contrast rather than a replacement for local syntax.\",\"representative_source_ids\":[\"QI-4106a179\",\"QE-e1e5f6a8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:12:2:command-protection-pairing","source_type":"word_analysis","support_id":"sup_ff374018295384cddddd","text":"{\"blocking_evidence\":null,\"headline\":\"command and guarding are compressed together\",\"reader_payoff\":\"The reader sees directive speech and protective response compressed into the short phrase, with close command-and-guarding parallels at 20:132 and 66:6.\",\"reason\":\"The local words join the command root and the protection root, while the CRITICAL rows give concrete command-to-guarding references such as 20:132 and 66:6 without forcing them to control the local parse.\",\"representative_source_ids\":[\"QI-c69b617e\",\"QI-ef2bb7a8\",\"MI-058934ca\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"أَوْ أَمَرَ بِٱلتَّقْوَىٰٓ","ayah_ref":"96:12"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000051/B002","root_001677/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000051","role":"The command-or-directive image supplies an obligating speech act and functions as the initiating force of the mechanism.","root":"ء م ر","source_ref":"96:12","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001677","role":"The image of placing oneself in protective caution supplies the commanded content and locates its work inside the hearer's conduct.","root":"و ق ي","source_ref":"96:12","source_word_indices":["3"]}],"changed_reading":{"after":"Or issued a directive by which the hearer actively places the self under protective caution.","before":"Or enjoined piety."},"confidence":"strong","focus_anchor":"The verb أَمَرَ and the governed noun تَّقْوَىٰ.","mechanism":"A directive transfers an obligation to the hearer, while taqwa names the hearer's active placement of the self behind a guard. The construction therefore joins outward speech to inward risk regulation.","model_id":"baseline_directive_as_self_protection"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_directive_as_self_protection","source_type":"hft","support_id":"sup_933237a2713c380338f8","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَوْ أَمَرَ بِٱلتَّقْوَىٰٓ","ayah_ref":"96:12"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000051/B003","root_001677/B001"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000051","role":"The authority-and-command-holder image supplies a vertical social relation whose legitimacy is being tested.","root":"ء م ر","source_ref":"96:12","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001677","role":"The protective-barrier image supplies shelter from damage and functions as the criterion imposed on authority.","root":"و ق ي","source_ref":"96:12","source_word_indices":["3"]}],"changed_reading":{"after":"Or exercised command in a way whose defining result was protection rather than domination.","before":"Or exercised the power to command."},"confidence":"medium","focus_anchor":"The authority potential of أَمَرَ is constrained by the protective object تَّقْوَىٰ.","mechanism":"The command root can activate office and command-holding, but the object prevents authority from being self-validating: its legitimate tendency here is to ward harm away. Authority is read functionally, by what it shelters.","model_id":"baseline_authority_measured_by_shelter"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_authority_measured_by_shelter","source_type":"hft","support_id":"sup_9be606ce16bec1a0a739","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَوْ أَمَرَ بِٱلتَّقْوَىٰٓ","ayah_ref":"96:12"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000051/B007","root_001677/B002"],"payload":{"activation_trace":[{"branch_id":"B007","mapped_root_id":"root_000051","role":"The consultation-and-deliberation image supplies considered intent and functions as an inward echo of the outward command.","root":"ء م ر","source_ref":"96:12","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001677","role":"The self-guarding image gives the deliberation a concrete behavioral end: voluntarily taking protective caution.","root":"و ق ي","source_ref":"96:12","source_word_indices":["3"]}],"changed_reading":{"after":"Or formed and transmitted a considered resolve toward self-guarding.","before":"Or told another person to be wary."},"confidence":"exploratory","focus_anchor":"The deliberative branch of أَمَرَ and the reflexive guarding carried by تَّقْوَىٰ.","mechanism":"The utterance can faintly activate counsel, inward consultation, and formed intent alongside ordinary command. On that branch, taqwa is not merely imposed from outside; it is a protective resolve considered and accepted.","model_id":"baseline_deliberated_guarding"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_deliberated_guarding","source_type":"hft","support_id":"sup_6738684846d79770b1f5","trust":"legacy_unbound"}]}
</lane_packet_json>
