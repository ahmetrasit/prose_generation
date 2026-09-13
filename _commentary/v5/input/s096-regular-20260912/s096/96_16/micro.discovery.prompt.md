# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **96:16**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s096-regular-20260912/s096/96_16/micro.discovery.json` and modify nothing
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
  "ayah_ref": "96:16",
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
{"branch_registry":[{"boundary":"Bu dal, bilerek işlenen ve kişiyi sorumlu kılan günahtan ayrılır; yağmurun bir araziyi atlaması da bağımsız bir arazi anlamı olarak ele alınır.","branch_kind":"mixed_non_bare","branch_ref":"root_000420/B001","candidate_links":[{"candidate_id":"cand_6927a041038dedb94467","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خَاطِئَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:xaATi}ap|ROOT:xTA|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"96:16:3:1","qac_word_ref":"96:16:3","surface_ar":"خَاطِئَةٍ"}],"gloss":"istemeden doğruyu tutturamama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi doğruyu veya belirli bir sonucu amaçlar, fakat istemeden başka bir yöne ya da sonuca varır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Türemiş bir kullanım, birine yanlış yaptığını söylemeyi veya onu yanlış bulmayı ifade eder."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir dilek kalıbında kötülüğün hedef kişiye uğramadan geçip gitmesi istenir."}}],"root_ar":"خ ط ء","root_id":"root_000420","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kasıtsız sapma ve amaçlanan sonuç yerine başka bir sonuca varma çekirdeğini birlikte karşılar.","boundary_detail":"Bu dal, bilerek işlenen ve kişiyi sorumlu kılan günahtan ayrılır; yağmurun bir araziyi atlaması da bağımsız bir arazi anlamı olarak ele alınır.","branch_image_ar":"مجاوزة الصواب وعدم إصابته","concept_gloss":"istemeden doğruyu tutturamama","contextual_glosses":[{"applicability":"Kişinin doğruyu amaçladığı hâlde yanlış bir yargıya veya sonuca vardığı genel bağlamlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yön, sınır veya fiziksel hedefi tutturamama kapsamını açıkça belirtmez.","preserves":"Doğruyu amaçlayıp başka bir sonuca varma düşüncesini korur."},"facet_ids":["F001"],"text":"yanılmak","usage_role":"general"},{"applicability":"Bir hedefe değmeme veya amaçlanan fiziksel sonucu elde edememe bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Düşünsel doğruyu bulamama ve bir işi yanlış yapma kapsamını dışarıda bırakır.","preserves":"Hedeflenen sonucun gerçekleşmemesi bileşenini korur."},"facet_ids":["F001"],"text":"ıskalamak","usage_role":"contextual"},{"applicability":"Birine yaptığı şeyin yanlış olduğunu söyleyen türemiş kullanım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başkasına yanlış yaptığını bildirme işlevini açık biçimde korur."},"facet_ids":["F002"],"text":"yanlış bulmak","usage_role":"contextual"}],"definition":"Doğruyu hedeflediği hâlde ona ulaşamama, doğru yön veya sınırdan istemeden sapma ya da yapılan işin amaçlanandan başka türlü sonuçlanmasıdır. Buna bağlı özel yapılarda birini yanlış sayma ve kötülüğün kişiye uğramamasını dileme anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi doğruyu veya belirli bir sonucu amaçlar, fakat istemeden başka bir yöne ya da sonuca varır."},{"facet_id":"F002","role":"associated_use","statement":"Türemiş bir kullanım, birine yanlış yaptığını söylemeyi veya onu yanlış bulmayı ifade eder."},{"facet_id":"F003","role":"associated_use","statement":"Bir dilek kalıbında kötülüğün hedef kişiye uğramadan geçip gitmesi istenir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Ahlaki suç, kasıt ve sorumluluk anlamlarını gereksiz yere ekler.","collision":"Kökün bilerek işlenen suç oluşturan ayrı dalıyla karışır.","fit":"displacement","loses":"Doğruyu amaçlama, kasıtsızlık ve hedeflenen sonucu tutturamama bileşenlerini kaybeder.","preserves":"Doğrudan ayrılma düşüncesinin yalnızca çok genel bir izini korur."},"text":"günah"}],"identity_rationale":"Dal çerçevesi, kaynak ifadesindeki doğruyu veya hedefi tutturamama, doğru yön ya da sınırdan sapma ve amaçlanandan başka bir sonuca varma çekirdeğini doğru biçimde yansıtır. Kasıtsızlık temel ayrımdır; birini yanlış sayma ve kötülüğün kişiye uğramamasını dileme ise bu çekirdeğe bağlı özel kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"istemeden yapılan yanlış; doğruyu tutturamama"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yanılmak; doğruyu tutturamamak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yanılmak; amaçlanan sonucu elde edememek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yanılmak; yanlış yapmak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"doğruyu amaçlayıp yanılan kimse"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yanlış yaptığını söylemek; yanlış bulmak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ıskalamak; değmemek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kötülük senden uzak olsun"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"çok yanılan da bazen doğruyu bulur"}],"lexicalization_note":"Yalın anlam, istemeden doğruyu ya da hedefi tutturamamadır; birini yanlış bulma ve kötülüğün uzak kalmasını dileme yalnızca kendi türemiş veya kalıplaşmış yapılarında geçerlidir.","neighbor_coverage_note":"Verilen bütün komşular değerlendirildi. Yalnızca kasıt, dil alanı, sonuca ulaşma kutbu ve araziye özgü hedef kaçırma bakımından dal sınırını belirginleştiren beş karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında doğru amaç ile gerçekleşen sonuç arasında istem dışı bir uyuşmazlık vardır. Komşu dalda ise yanlış eyleme yönelme kasıtlıdır ve ahlaki sorumluluk doğurur.","focus_only":"Doğru amaçlandığı hâlde sonuç istemeden tutturulamaz.","gloss":"kasıtsız yanılma / bilerek işlenen günah","neighbor_only":"Kişi sakıncalı eyleme bilerek yönelir ve bundan sorumlu tutulur.","neighbor_ref":"root_000420/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da doğru veya uygun olandan ayrılmayı konu eder."},{"boundary_match":"partial","distinction":"Odak dalı doğruyu veya hedefi tutturamamanın genel alanıdır. Komşu dal ise bu sapmayı özellikle dil bilgisi, okuma, söyleyiş ve sözün düzeltilmesi alanına bağlar.","focus_only":"Hata, düşünceyi, yönü, eylemi ve hedeflenen sonucu kapsayabilir.","gloss":"genel yanılma / dil yanlışı","neighbor_only":"Yanlışlık dil bilgisi, okuma ve söz söyleme doğruluğuyla sınırlıdır.","neighbor_ref":"root_001349/B002","relation_type":"near_neighbor","shared_zone":"İki dal da yerleşik bir doğrudan ayrılmayı ifade eder."},{"boundary_match":"partial","distinction":"Komşu kart yanılma eylemini doğrudan karşılar, ancak odak dalındaki niyet-sonuç ayrımını ve yön ya da sınırdan sapma kapsamını belirtmez. Bu nedenle çekirdekler yakın olsa da sınırlar tam olarak kanıtlanmış değildir.","focus_only":"Doğruyu amaçlama, istem dışı sapma ve sonucun niyete uymaması açıkça belirlenir.","gloss":"yanılmak","neighbor_only":"Komşu dal yanılma eylemini ayrı ve dar bir söz varlığıyla adlandırır.","neighbor_ref":"root_000704/B006","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak alanı yanlış yapma veya doğruyu tutturamamadır."},{"boundary_match":"opposed","distinction":"Odak dalı istenen sonucun gerçekleşmemesini anlatır. Komşu dal ise kişinin düşüncesizliğine rağmen istediği sonuca ulaşmasını öne çıkararak aynı eksende karşıt kutbu oluşturur.","focus_only":"Kişi amaçladığı doğru sonuca ulaşamaz.","gloss":"amacı tutturamama / amaca ulaşma","neighbor_only":"Kişi düşüncesizliğine rağmen amaçladığı sonuca ulaşır.","neighbor_ref":"root_000151/B006","relation_type":"polarity_pair","shared_zone":"İki dal da kişinin amaçladığı sonuca ulaşıp ulaşmaması ekseninde karşılaştırılabilir."},{"boundary_match":"partial","distinction":"Odak dalı genel bir yanılma ve hedefi tutturamama kavramıdır. Komşu dal bu şemayı yağmur ile arazi arasındaki ilişkiye bağlayıp yağış almayan araziyi adlandıran bağımsız bir anlam kurar.","focus_only":"Genel olarak bir kişinin veya eylemin doğruyu ya da hedefi tutturamaması anlatılır.","gloss":"hedefi tutturamama / yağmurun araziyi atlaması","neighbor_only":"Yağmurun çevreyi ıslatırken belirli bir arazi parçasına düşmemesi anlatılır.","neighbor_ref":"root_000420/B003","relation_type":"near_neighbor","shared_zone":"İki dalda da hareket eden şey beklenen hedefe ulaşmaz."}],"source_phrase_ar":"أخطأ إذا لم يصب الصواب؛ الخطأ ما لم يتعمد؛ خطأته تخطئة (ayn)؛ الخطأ نقيض الصواب؛ المخطئ من أراد الصواب فصار إلى غيره؛ خطأته تخطئة وتخطيئا (sihah)؛ أخطأ إذا لم يصب الصواب؛ أخطأت لما صنعه خطأ غير عمد؛ خطىء عنك السوء إذا دعوا له أن يدفع عنه السوء (tahdhib)؛ الخطأ العدول عن الجهة؛ يقع منه خلاف ما يريد؛ أصاب الخطأ وأخطأ الصواب (mufradat)؛ الخطاء مجاوزة حد الصواب؛ أخطأ إذا تعدى الصواب (maqayis)","source_summary":"Kaynakların ortak çerçevesinde kişi doğruyu veya istenen sonucu amaçladığı hâlde onu tutturamaz, doğru yönden ya da sınırdan sapar ve eylemi niyet ettiğinden farklı sonuçlanır. Bu temel anlam kasıtsızdır; ayrıca birini yanlış sayan ettirgen kullanım ile kötülüğün kişiden uzak kalmasını isteyen bir dilek kullanımı da kaydedilir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الخطأ بمعنى العدول عن الجهة أو عدم إصابة الصواب، والفعل غير المتعمد، ووقوع الفعل بخلاف المراد، والتخطئة بقولك أخطأت، والدعاء بأن يخطئ السوء الإنسان","what_is_not_ar":"ليس الذنب المتعمد من حيث هو إثم مقصود؛ وليس الأرض التي يخطئها المطر إلا من جهة صورة عدم الإصابة"},"support_links":["sup_65aa5d5b161877ad020f"]},{"boundary":"Bu dal, doğruyu amaçladığı hâlde istemeden yanılan kişiyi değil, yanlış eyleme kasıtla yönelen ve bundan sorumlu olan kişiyi ya da eylemini kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000420/B002","candidate_links":[{"candidate_id":"cand_f4fffa0771c9ea0583d1","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خَاطِئَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:xaATi}ap|ROOT:xTA|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"96:16:3:1","qac_word_ref":"96:16:3","surface_ar":"خَاطِئَةٍ"}],"gloss":"bilerek işlenen günah","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi yapılmaması gereken bir eyleme bilerek yönelir ve günah işler."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylem tamamlanmış bir yanlış sayılır ve kişi bundan dolayı sorumlu tutulur."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Türemiş bir ad, günaha kasıtla yönelen veya yapılmaması gerekeni bilerek yapan kişiyi gösterir."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bazı kullanımlarda adlandırılan eylem özellikle büyük ve ağır bir günahtır."}}],"root_ar":"خ ط ء","root_id":"root_000420","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kasıt, ahlaki yanlışlık ve sorumluluk bileşenlerini birlikte taşıdığı için dalın temel kavramını karşılar.","boundary_detail":"Bu dal, doğruyu amaçladığı hâlde istemeden yanılan kişiyi değil, yanlış eyleme kasıtla yönelen ve bundan sorumlu olan kişiyi ya da eylemini kapsar.","branch_image_ar":"الخطيئة ذنب وإثم","concept_gloss":"bilerek işlenen günah","contextual_glosses":[{"applicability":"Yapılmaması gereken bir eylemi bilerek gerçekleştirme anlatıldığında doğal eylem karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilerek kötü eyleme yönelme ve bundan ahlaki sorumluluk doğması bileşenlerini korur."},"facet_ids":["F001","F002"],"text":"günah işlemek","usage_role":"general"},{"applicability":"Yapılmaması gerekeni bilerek yapan kişiyi niteleyen türemiş kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kasıtla günah işleyen kişiyi gösterme işlevini korur."},"facet_ids":["F003"],"text":"günahkâr","usage_role":"contextual"},{"applicability":"Eylemin özellikle ağır bir günah olarak adlandırıldığı bağlamlarla sınırlıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Günahın ağır ve büyük sayılan özel türünü korur."},"facet_ids":["F004"],"text":"büyük günah","usage_role":"contextual"}],"definition":"Kişinin yanlış ve sakıncalı olduğunu bilerek yöneldiği, bu yüzden kınanıp sorumlu tutulduğu günah veya kötü eylemdir. Türemiş kullanımlar eylemi yapan kişiyi, günahların çoğulluğunu ve özellikle ağır günahı belirtebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi yapılmaması gereken bir eyleme bilerek yönelir ve günah işler."},{"facet_id":"F002","role":"core","statement":"Eylem tamamlanmış bir yanlış sayılır ve kişi bundan dolayı sorumlu tutulur."},{"facet_id":"F003","role":"extension","statement":"Türemiş bir ad, günaha kasıtla yönelen veya yapılmaması gerekeni bilerek yapan kişiyi gösterir."},{"facet_id":"F004","role":"specialization","statement":"Bazı kullanımlarda adlandırılan eylem özellikle büyük ve ağır bir günahtır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"İstem dışı, ahlaki sorumluluk taşımayan yanılmaları da kapsama katar.","collision":"Kökün kasıtsız yanılmayı anlatan ayrı dalıyla kolayca karışır.","fit":"broadening","loses":null,"preserves":"Doğru veya uygun olmayışın genel anlamını korur."},"text":"hata"}],"identity_rationale":"Dal çerçevesi, kaynak ifadesindeki bilerek sakıncalı olana yönelme, günah işleme ve bu eylemden dolayı sorumlu tutulma bileşenlerini doğru biçimde birleştirir. Büyük günah ve günahı işleyen kişi anlamları bu ahlaki çekirdeğin özel görünümleridir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"sorumluluk doğuran günah"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"günah; suç"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"günah işlemek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"hesabı sorulan günah veya kötü eylem"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"günahı bilerek işleyen kimse; günahkâr"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"büyük günah"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"günahlar"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ne büyük günah işledi!"}],"lexicalization_note":"Temel alan kasıtlı ve sorumluluk doğuran kötü eylemdir; eyleyen kişi, büyük günah, çoğul ve ünlem değeri taşıyan türemiş biçimler kendi dil bilgisel sınırlarında tutulur.","neighbor_coverage_note":"Verilen bütün komşular değerlendirildi. Kasıtsız yanılma, genel günah alanı, günahtan sakınma ve hesap sorma eylemiyle sınırı en açık gösteren beş karşılaştırma yayıma değer bulundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında kişi yapılmaması gerekeni kasıtla yapar ve ahlaki sorumluluk taşır. Komşu dalda kişi doğruyu amaçlar; yanlış sonuç niyetinden değil, istem dışı başarısızlıktan doğar.","focus_only":"Yanlış eyleme bilerek yönelme ve bundan sorumlu tutulma vardır.","gloss":"bilerek işlenen günah / kasıtsız yanılma","neighbor_only":"Doğru amaçlandığı hâlde sonuç istemeden tutturulamaz.","neighbor_ref":"root_000420/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da doğru veya uygun olandan ayrılmayı konu eder."},{"boundary_match":"partial","distinction":"Odak dalı kasıt ve hesabı sorulma sınırını öne çıkarır. Komşu dal günahı suç, karşı gelme ve kötü sonuç doğuran eylem alanıyla daha geniş biçimde adlandırır.","focus_only":"Günahın kasıtla işlenmesi ve kişiye sorumluluk yüklemesi açıkça belirtilir.","gloss":"kasıtlı günah / genel günah ve suç","neighbor_only":"Kötü sonuçlu eylem, suç ve karşı gelme alanları daha genel biçimde kapsanır.","neighbor_ref":"root_000521/B001","relation_type":"near_synonym","shared_zone":"İki dalın ortak çekirdeği ahlaken kötü ve suç oluşturan eylemdir."},{"boundary_match":"partial","distinction":"Odak dalının sınırı kasıtlı kötü eylem ve bundan sorumlu olmadır. Komşu dal aynı ahlaki alanda günahı, günaha düşmüş olmayı ve kişinin ondan sakınma tutumunu birlikte kapsar.","focus_only":"Bilerek yapılmaması gerekene yönelme ve ağır günah özelleşmesi bulunur.","gloss":"kasıtlı günah / günah ve sakınma","neighbor_only":"Günahın yanı sıra kişinin ondan sakınması ve arınma kaygısı da adlandırılır.","neighbor_ref":"root_000365/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da günahı ve günah işlemiş olma durumunu kapsar."},{"boundary_match":"partial","distinction":"Odak dalı kasıtlı günah eylemini ve sorumlu kişiyi adlandırır. Komşu dal ise günah anlamının yanında kişinin günaha düşmekten çekinmesini veya günahtan uzak durmasını da kapsar.","focus_only":"Kişinin bilerek işlediği kötü eylemin kendisi ve eyleyeni öne çıkar.","gloss":"günah işleme / günahtan çekinme","neighbor_only":"Günaha düşme yanında günahtan çekinme veya onu bırakma tutumu da öne çıkar.","neighbor_ref":"root_000304/B003","relation_type":"near_neighbor","shared_zone":"İki dal ahlaki suç ve günah alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dalı kişinin bilerek işlediği ve sorumluluk doğuran eylemdir. Komşu dal eylemin kendisini değil, o eylem yüzünden kişiyi sorumlu tutma ve ondan hesap sorma işlemini anlatır.","focus_only":"Sorumluluğu doğuran kasıtlı günah veya kötü eylem adlandırılır.","gloss":"günah / günahın hesabını sorma","neighbor_only":"İşlenen eylem nedeniyle kişiden hesap sorma işlemi adlandırılır.","neighbor_ref":"root_000018/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal suç oluşturan eylem ile sorumluluk arasındaki ilişkiye dayanır."}],"source_phrase_ar":"الخطء الذنب؛ خطئ يخطأ خطأ وخطأة؛ الخطيئة (sihah)؛ خطئت إذا أثمت؛ خاطئين أي آثمين؛ خطئت لما صنعه عمدا وهو الذنب؛ الخطيئة الذنب على عمد (tahdhib)؛ الخطأ التام المأخوذ به الإنسان؛ الخطيئة والسيئة يتقاربان؛ الخاطئ هو القاصد للذنب؛ الذنب العظيم (mufradat)؛ خطئ يخطأ إذا أذنب (maqayis)","source_summary":"Kaynakların ortak çerçevesi günah, suç ve ahlaki bakımdan kötü eylem anlamında birleşir. Bazı açıklama ve kullanımlarda eyleme bilerek yönelme, bundan sorumlu tutulma, eyleyeni gösteren ad ve büyük günah özelleşmesi ayrıca belirtilir.","sources":["SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الخطء والخطيئة بمعنى الذنب والإثم، والخاطئ القاصد للذنب أو المتعمد لما لا ينبغي، وما يسمى خطيئة وسيئة في باب المؤاخذة","what_is_not_ar":"ليس الخطأ غير المتعمد الذي أراد صاحبه الصواب؛ وليس مجرد عدم إصابة الهدف بلا إثم"},"support_links":["sup_ed56121597e410ee2d7b"]},{"boundary":"Bu dal bir yağış olayını veya genel kuraklığı değil, yağmurun çevreyi ıslatırken atladığı arazi parçasını adlandırır; günah anlamındaki dal ile karıştırılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000420/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَاطِئَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:xaATi}ap|ROOT:xTA|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"96:16:3:1","qac_word_ref":"96:16:3","surface_ar":"خَاطِئَةٍ"}],"gloss":"yağmurun atladığı arazi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yağmur başka bir araziye düşer, fakat adlandırılan arazi parçasını atlar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Arazi, yağış almış iki yerin arasında yağmursuz kalan bir parça olabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir dilek yapısında mevsim yağmurunun belirli araziye düşmeden geçmesi istenir."}}],"root_ar":"خ ط ء","root_id":"root_000420","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yağmurun başka yerlere düşerken belirli araziye düşmemesiyle oluşan temel karşıtlığı doğal ve kısa biçimde karşılar.","boundary_detail":"Bu dal bir yağış olayını veya genel kuraklığı değil, yağmurun çevreyi ıslatırken atladığı arazi parçasını adlandırır; günah anlamındaki dal ile karıştırılmaz.","branch_image_ar":"أرض أخطأها المطر","concept_gloss":"yağmurun atladığı arazi","contextual_glosses":[{"applicability":"Bağlam çevredeki veya başka yerdeki yağışı zaten gösteriyorsa, arazi durumunu akıcı biçimde anlatır.","error_profile":{"adds":"Çevrede yağmur bulunmayan genel kurak arazileri de kapsayabilir.","collision":"Genel yağışsızlık veya kuraklık bildiren arazi adlarıyla karışabilir.","fit":"broadening","loses":null,"preserves":"Adlandırılan arazinin yağmursuz kalması sonucunu korur."},"facet_ids":["F001"],"text":"yağış almayan arazi","usage_role":"general"},{"applicability":"Yağmur alan iki arazi parçası arasında yağışsız kalan özel arazi görünümü için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki yağışlı yer arasındaki kuru arazi özelleşmesini eksiksiz korur."},"facet_ids":["F002"],"text":"iki yağışlı alan arasında kuru kalan yer","usage_role":"explanatory"},{"applicability":"Yağmurun belirli bir yeri atlamasını isteyen özel dilek yapısının doğal Türkçe karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yağmurun hedef araziye düşmemesini isteme işlevini korur."},"facet_ids":["F003"],"text":"oraya yağmur yağmasın","usage_role":"contextual"}],"definition":"Yağmurun çevresindeki ya da başka yerlerdeki toprağa düştüğü hâlde kendisine düşmediği arazi parçasıdır; özellikle yağış alan iki arazi arasında kuru kalan yer böyle adlandırılır. Özel bir dilek yapısında yağmurun o yeri atlaması istenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yağmur başka bir araziye düşer, fakat adlandırılan arazi parçasını atlar."},{"facet_id":"F002","role":"specialization","statement":"Arazi, yağış almış iki yerin arasında yağmursuz kalan bir parça olabilir."},{"facet_id":"F003","role":"associated_use","statement":"Bir dilek yapısında mevsim yağmurunun belirli araziye düşmeden geçmesi istenir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Uzun süreli iklim kuraklığını ve toprağın genel verimsizliğini de kapsama katar.","collision":"Yağmurun seçici biçimde atladığı yer ile genel kurak araziyi birbirine karıştırır.","fit":"broadening","loses":null,"preserves":"Arazinin yağışsız ve kuru kalmış olması sonucunu korur."},"text":"kurak arazi"},{"category":"confusable","error_profile":{"adds":"Ahlaki suç, kasıt ve sorumluluk anlamlarını ilgisiz biçimde ekler.","collision":"Kökün kasıtlı günahı anlatan ayrı dalıyla doğrudan karışır.","fit":"displacement","loses":"Yağmur, arazi ve çevredeki yerlere göre yağışsız kalma ilişkisinin tamamını kaybeder.","preserves":"Bu dalın sesçe örtüşen bir adla ifade edilmesini yalnızca biçim düzeyinde çağrıştırır."},"text":"günah"}],"identity_rationale":"Dal çerçevesi, kaynak ifadesindeki yağmurun başka yerlere düştüğü hâlde belirli bir araziye düşmemesi ve özellikle yağış alan iki yer arasında kuru bir parça bırakması anlamını doğru biçimde yansıtır. Yağışın o yeri atlamasını isteyen dilek, aynı hedefi tutturamama şemasına bağlı özel bir yapıdır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yağmurun atladığı arazi"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"iki yağışlı arazi arasında yağışsız kalan yer"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"oraya yağmur yağmasın"}],"lexicalization_note":"Arazi adı, yağmurun başka yerlere düşerken belirli yeri atlamasıyla sınırlıdır; iki yağışlı alan arasındaki kuru yer ve yağmurun oraya düşmemesini isteyen dilek ayrıca korunur.","neighbor_coverage_note":"Verilen bütün komşular değerlendirildi. Yağışsız arazi, kuraklık sonucu, seçici sağanak, genel hedefi tutturamama ve yağmurun kendisiyle sınırı açıklayan beş karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında yağmurun başka yere düşüp bu araziyi seçici biçimde atlaması kurucu ilişkidir. Komşu dal yağışın veya sulamanın araziye ulaşmaması sonucunu verir, fakat çevrede yağış bulunması şartını belirtmez.","focus_only":"Yağmurun başka yerlere düşerken belirli araziyi atlaması karşılaştırması bulunur.","gloss":"yağmurun atladığı arazi / yağışsız kalmış arazi","neighbor_only":"Arazi yalnızca beklenen sulamadan veya yağmurdan yoksun kalmış olarak adlandırılır.","neighbor_ref":"root_001179/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da üzerine yağmur düşmemiş araziyi adlandırır."},{"boundary_match":"partial","distinction":"Odak dalı çevredeki yağışa karşı belirli yerin atlanmasına dayanır ve bitki örtüsü sonucu şart koşmaz. Komşu dal yağmurdan yoksun kalmayı bitkisizlik ve kuraklık sonucu ile genişletir.","focus_only":"Arazi, çevresi yağış alırken yağmurun seçici biçimde atladığı yer olarak belirlenir.","gloss":"yağmurun atladığı arazi / yağmursuz ve kıraç arazi","neighbor_only":"Yağışsızlığın yanında bitkisizlik ve kuraklıktan yanmış olma sonuçları da kapsanır.","neighbor_ref":"root_000041/B005","relation_type":"near_synonym","shared_zone":"İki dalın ortak alanı yağmur düşmeyen arazidir."},{"boundary_match":"partial","distinction":"Odak dalının odağı yağmurun ulaşmadığı arazi ve onun kuru kalmasıdır. Komşu dal ise aynı dağılım olayında araziyi değil, bazı parçaları ıslatıp bazılarını atlayan sağanağı adlandırır.","focus_only":"Seçici yağışın atladığı arazi parçası adlandırılır.","gloss":"yağışsız kalan yer / seçici sağanak","neighbor_only":"Bir parçaya düşüp başka parçayı atlayan yağmur sağanağının kendisi adlandırılır.","neighbor_ref":"root_001535/B013","relation_type":"near_neighbor","shared_zone":"İki dal da yağmurun bir alanı ıslatıp başka bir alanı atlaması durumuna dayanır."},{"boundary_match":"partial","distinction":"Odak dalı hedefi tutturamama şemasını yağmur ile arazi arasındaki ilişkiye bağlar ve ortaya çıkan araziyi adlandırır. Komşu dal ise bu şemayı genel yanılma ve amaçlanan sonucun gerçekleşmemesi olarak korur.","focus_only":"Yağmurun ulaşmadığı arazi bağımsız bir yer adı olarak belirlenir.","gloss":"yağmurun araziyi atlaması / genel hedefi tutturamama","neighbor_only":"Bir kişinin veya eylemin doğruyu, yönü ya da amaçlanan sonucu tutturamaması anlatılır.","neighbor_ref":"root_000420/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da hareket eden şey beklenen hedefe ulaşmaz."},{"boundary_match":"field_only","distinction":"Odak dalının çekirdeği yağmurun ulaşmadığı yer ve yerler arası dağılım karşıtlığıdır. Komşu dal ise yağmur olayını adlandırır; herhangi bir araziyi atlama koşulu taşımaz.","focus_only":"Yağmurun düşmediği ve bu nedenle kuru kalan arazi parçası adlandırılır.","gloss":"yağışsız arazi / yağmur","neighbor_only":"Niteliği güçlü ya da zayıf olabilen yağmur veya yağışın kendisi adlandırılır.","neighbor_ref":"root_000522/B005","relation_type":"same_field","shared_zone":"Her iki dal yağmur ve arazinin sulanmasıyla ilgili aynı doğa alanındadır."}],"source_phrase_ar":"الخطيئة أرض يخطئها المطر ويصيب غيرها (ayn)؛ الأرض الخطيطة هي التي لم تمطر بين أرضين ممطورتين؛ من أخطأ كأن المطر أخطأها؛ خطأ الله نوءها (maqayis)","source_summary":"Kaynakların ortak çerçevesinde yağmur başka bir yere düşerken belirli araziyi atlar ve o yer yağışsız kalır. Bu arazi, yağış almış iki yer arasında kalan kuru parça olarak özelleşebilir; ayrıca yağmurun belirli yere düşmemesini isteyen bir dilek yapısı kaydedilir.","sources":["AY","MQ"],"what_is_ar":"يدخل فيه الأرض التي يخطئها المطر ويصيب غيرها، والخطيئة أو الخطيطة بهذا المعنى، ونسبة خطأ الله نوءها إلى أن المطر لم يصبها","what_is_not_ar":"ليس الخط والكتابة والأثر الممتد من جذر خط؛ وليس الخطيئة بمعنى الذنب"},"support_links":[]},{"boundary":"Dal, gerçeğe aykırı söz ve davranışı kapsar; başkasını yalancılıkla niteleme eylemini ya da özel kalıpların bağımsız anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001290/B001","candidate_links":[{"candidate_id":"cand_f4fffa0771c9ea0583d1","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كَٰذِب","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:ka`*ib|ROOT:k*b|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"96:16:2:1","qac_word_ref":"96:16:2","surface_ar":"كَٰذِبَةٍ"}],"gloss":"sözde veya davranışta doğruluğa aykırılık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Doğruluğa aykırılık hem söylenen bir sözde hem de yapılan bir davranışta gerçekleşebilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu niteliği taşıyan veya onu sıkça gösteren kişi, yalan söyleyen kişi olarak adlandırılır."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem söz hem davranış alanındaki bütün yalın anlam çekirdeğini karşılayan açıklayıcı üst karşılıktır.","boundary_detail":"Dal, gerçeğe aykırı söz ve davranışı kapsar; başkasını yalancılıkla niteleme eylemini ya da özel kalıpların bağımsız anlamlarını kapsamaz.","branch_image_ar":"خلاف الصدق","concept_gloss":"sözde veya davranışta doğruluğa aykırılık","contextual_glosses":[{"applicability":"Bağlamın söz veya davranıştaki doğruluğa aykırılığı zaten belirginleştirdiği doğal kullanımlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doğruluğa aykırılık çekirdeğini ve kişiye yüklenebilen niteliği doğal Türkçeyle korur."},"facet_ids":["F001","F002"],"text":"yalan","usage_role":"general"}],"definition":"Bir sözün veya davranışın doğruluğa aykırı olmasıdır. Bu niteliği taşıyan kişi, yalan söyleyen ya da yalanı çokça tekrarlayan biri olarak betimlenebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Doğruluğa aykırılık hem söylenen bir sözde hem de yapılan bir davranışta gerçekleşebilir."},{"facet_id":"F002","role":"specialization","statement":"Bu niteliği taşıyan veya onu sıkça gösteren kişi, yalan söyleyen kişi olarak adlandırılır."}],"identity_rationale":"Kaynak ifadesi anlamı doğruluğun karşıtı olarak kurar ve bu karşıtlığın hem sözde hem davranışta gerçekleşebildiğini açıkça belirtir. Kişiyi bu nitelikle betimleyen biçimler aynı çekirdeğe bağlıdır; birini yalancı sayma eylemi ise ayrı dalın konusudur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"sözde veya davranışta doğruluğa aykırılık; yalan"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yalancı; çok yalan söyleyen kişi"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"uydurma söz; yalanlar"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"özürlere kaçınılmaz olarak yalan karışır"}],"lexicalization_note":"Tanım yalın anlam çekirdeğini verir; kişi betimleyen türevler ile özürlere ilişkin kalıp yalnız kendi sözcüksel karşılıklarında gösterilir ve yalın anlama eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yalanla en kolay karışan beş anlam yayımlandı, yalnızca aynı senaryoda bulunan özel kalıplar ve uzak tematik adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal gerçeğe aykırı içeriğin ya da davranışın niteliğidir; komşu dal ise bir kişi veya söz hakkında bu yönde hüküm verme işlemidir.","focus_only":"Doğruluğa aykırı sözün veya davranışın kendisini bildirir.","gloss":"yalan ile yalan sayma ayrımı","neighbor_only":"Bir sözü yalan sayma, birini yalancı bulma veya ona yalancılık yükleme işlemini bildirir.","neighbor_ref":"root_001290/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da doğruluk ile gerçeğe aykırılık arasındaki değerlendirme alanındadır."},{"boundary_match":"partial","distinction":"Odak dal genel doğruluğa aykırılıktır; komşu dal bunun daha ağır, saptırılmış veya başkalarını yanlış yöne sevk eden türünü belirginleştirir.","focus_only":"Sıradan ölçekteki söz ve davranış yalanlarını da kapsar.","gloss":"yalan ile saptırıcı büyük yalan","neighbor_only":"Doğrudan sapmış, büyük veya başkalarını yanlış yöne çeken ağır bir yalan alanını da öne çıkarır.","neighbor_ref":"root_000041/B002","relation_type":"near_synonym","shared_zone":"İki dal da doğruluğa aykırı söz ve aldatıcı içerik alanında büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal söz ve davranıştaki genel doğruluğa aykırılıktır; komşu dal özellikle bilgi yerine tahmine dayanarak asılsız söz üretmeyi de içerir.","focus_only":"Söz dışındaki davranışlarda görülen doğruluğa aykırılığı da kapsar.","gloss":"yalan ile bilgisizce söyleme","neighbor_only":"Bilgiye dayanmadan tahmin yürütme ve doğrulanmamış söz söyleme alanını da kapsar.","neighbor_ref":"root_000403/B002","relation_type":"near_synonym","shared_zone":"Gerçek dışı veya dayanaksız söz söyleme bağlamlarında iki anlam birbirine yaklaşır."},{"boundary_match":"partial","distinction":"Odak dal genel yalan niteliğidir; komşu dal yalanı özellikle haktan sapma, yalancı tanıklık ve batıllık çevresinde örgütler.","focus_only":"Her türlü sözsel veya davranışsal doğruluğa aykırılığı kapsar.","gloss":"genel yalan ile haktan sapmış söz","neighbor_only":"Yalancı tanıklık, haktan sapma ve batıl sayılan nesneler gibi özel alanlara uzanır.","neighbor_ref":"root_000654/B002","relation_type":"near_neighbor","shared_zone":"İki dal da gerçek ve hakikate aykırı söz alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal doğruluğa aykırılığı temel alır; komşu dal ise sözün kesinlik ve güven düzeyine odaklanır, bu nedenle her kuşkulu aktarım yalan değildir.","focus_only":"Sözün ya da davranışın doğruluğa aykırı olmasını doğrudan bildirir.","gloss":"yalan ile kuşkulu aktarım","neighbor_only":"Kesinlik bulunmadan aktarılan, kuşkulu veya doğruluğu güven vermeyen sözü de kapsar.","neighbor_ref":"root_000633/B001","relation_type":"near_neighbor","shared_zone":"Kuşkulu bir iddianın gerçek dışı çıkması durumunda iki alan kesişebilir."}],"source_phrase_ar":"الكذب خلاف الصدق (maqayis;jamhara); الكذاب لغة في الكذب (ayn); كذب كذبا فهو كاذب وكذاب وكذوب (sihah); يقال في المقال والفعال (mufradat)","source_summary":"Kaynaklar, doğruluğa aykırılığı ortak çekirdek sayar; kullanım alanını söz ve davranış olarak verir ve bu niteliği taşıyan kişiye yönelik adlandırmaları aynı anlam çevresinde toplar.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الكذب في القول والفعل، ووصف صاحبه بالكاذب والكذاب والكذوب، وجمع الأكاذيب والمكاذب","what_is_not_ar":"لا يدخل فيه فعل التكذيب والنسبة إلى الكذب، ولا إغراء كذب عليك، ولا الألفاظ الاصطلاحية الخاصة بالحملة واللبن والثوب"},"support_links":["sup_ed56121597e410ee2d7b"]},{"boundary":"Dal yalan üretmeyi değil, kişi veya söz hakkında yalan hükmü vermeyi ve belirli türevlerde bu hükmü bulguya dayandırmayı kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001290/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَٰذِب","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:ka`*ib|ROOT:k*b|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"96:16:2:1","qac_word_ref":"96:16:2","surface_ar":"كَٰذِبَةٍ"}],"gloss":"yalan sayma veya yalancı bulma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya söz, yalan olduğu söylenerek doğruluk bakımından olumsuz değerlendirilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli türemiş biçimler, kişiyi yalancı bulmayı veya onun yalanını ortaya çıkarmayı bildirir."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hüküm verme çekirdeği ile belirli türevlerdeki bulma ve açığa çıkarma ayrımını birlikte karşılar.","boundary_detail":"Dal yalan üretmeyi değil, kişi veya söz hakkında yalan hükmü vermeyi ve belirli türevlerde bu hükmü bulguya dayandırmayı kapsar.","branch_image_ar":"نسبة الشيء أو صاحبه إلى الكذب","concept_gloss":"yalan sayma veya yalancı bulma","contextual_glosses":[{"applicability":"Bir sözün veya kişinin söylediğinin yalan olduğunu bildiren bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişiyi yalancı bulma ve yalanını ortaya çıkarma sonucunu tek başına göstermez.","preserves":"Kişi veya söz hakkında yalan hükmü verme işlemini korur."},"facet_ids":["F001"],"text":"yalanlamak","usage_role":"contextual"},{"applicability":"Değerlendirme sonucunda bir kişinin yalan söylediğinin anlaşıldığı türemiş biçimler için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir sözü doğrudan yalan sayma ve muhataba yalan söylediğini bildirme işlemini kapsamaz.","preserves":"Kişiyi yalancı bulma veya yalanını açığa çıkarma sonucunu korur."},"facet_ids":["F002"],"text":"yalancı bulmak","usage_role":"contextual"}],"definition":"Bir kişiyi veya sözü yalanla ilişkilendirerek yalan olduğunu söylemektir. Bazı türemiş biçimlerde işlem, kişiyi yalancı bulma ya da yalanını ortaya çıkarma sonucunu bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya söz, yalan olduğu söylenerek doğruluk bakımından olumsuz değerlendirilir."},{"facet_id":"F002","role":"source_variant","statement":"Belirli türemiş biçimler, kişiyi yalancı bulmayı veya onun yalanını ortaya çıkarmayı bildirir."}],"identity_rationale":"Kaynak ifadesi tek bir işlemi değil, birbirine bağlı iki işlemi içerir: bir kişiyi veya sözü yalanla nitelemek ve bazı türemiş biçimlerde kişiyi yalancı bulmak ya da yalanını açığa çıkarmak. Dal korunabilir, ancak bu ayrım tek bir genel 'yalan yükleme' anlatımı içinde eritilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yalanlama; yalan sayma"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"birini yalancı saymak veya ona yalan söylediğini bildirmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birini yalancı bulmak veya yalanını ortaya çıkarmak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"seni yalancı saymıyorum"}],"lexicalization_note":"Tanım, türemiş ve nesne alan biçimlerinin farklı işlemlerini ayırır; bunlardan hiçbiri yalın biçimin genel yalan anlamı olarak sunulmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalanın kendisi, genel suçlama ve benzer isnat işlemleriyle sınırı gösteren dört aday seçildi, daha uzak söz ve özel kalıp alanları yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalan olduğuna hükmetme işlemidir; komşu dal ise bu hükmün konusu olan gerçeğe aykırı söz veya davranıştır.","focus_only":"Bir kişi veya söz hakkında yalan hükmü verme işlemini bildirir.","gloss":"yalan sayma ile yalan ayrımı","neighbor_only":"Doğruluğa aykırı sözün veya davranışın kendisini bildirir.","neighbor_ref":"root_001290/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da doğruluk değerlendirmesi ve yalan alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal yalnız doğruluk ve yalan eksenindeki hükme bağlıdır; komşu dalın suçlama ve kuşku alanı daha geniştir.","focus_only":"Yüklenen nitelik özellikle yalan söyleme veya sözün yalan olmasıdır.","gloss":"yalancılıkla niteleme ile suçlama","neighbor_only":"Kişiye herhangi bir suçlama ya da kuşku iliştirmeyi, hatta onda bulunmayan olumlu bir niteliği yakıştırmayı kapsayabilir.","neighbor_ref":"root_001607/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir kişi hakkında olumsuz bir niteleme veya iddia yöneltme işlemini içerebilir."},{"boundary_match":"field_only","distinction":"İşlemin yapısı benzerdir, ancak odak dalın hükmü yalanla, komşu dalın hükmü hırsızlıkla sınırlıdır; anlam çekirdekleri birbirinin yerine geçmez.","focus_only":"Kişiyi yalancılıkla veya sözünü yalan olmakla niteler.","gloss":"farklı fiillerle suçlayıcı niteleme","neighbor_only":"Kişiyi hırsızlık yapmakla niteler.","neighbor_ref":"root_000700/B005","relation_type":"same_field","shared_zone":"İki dal da bir kişiye belirli bir olumsuz eylemi yükleyen dilsel işlemlerdir."},{"boundary_match":"partial","distinction":"Odak dal doğruluk hakkında verilen hükümdür; komşu dal ise gerçekleşmemiş belirli bir eylemin kişiye isnat edilmesidir.","focus_only":"Bir kişiyi genel olarak yalancı sayabilir veya belirli bir sözü yalanlayabilir.","gloss":"yalan sayma ile yapılmamışı yükleme","neighbor_only":"Kişinin yapmadığı belirli bir içme eylemini ona yükleme iddiasıyla sınırlıdır.","neighbor_ref":"root_000783/B010","relation_type":"near_neighbor","shared_zone":"Bir kişiye gerçekleşmemiş bir eylem yüklenince bu iddiayı yalanlama bağlamında iki alan kesişir."}],"source_phrase_ar":"كذبت فلانا نسبته إلى الكذب وأكذبته وجدته كاذبا (maqayis); كذبته جعلته كاذبا (ayn); كذبت بالحديث كذابا وتكذيبا (jamhara); أكذبت الرجل ألفيته كاذبا وكذبته إذا قلت له كذبت (sihah); كذبته نسبته إلى الكذب (mufradat)","source_summary":"Kaynaklar, birini ya da bir sözü yalanla niteleme konusunda birleşir; aynı toplu kanıt, ayrı bir türemiş biçimde kişiyi yalancı bulma veya yalanı açığa çıkarma yorumunu da taşır.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه كذبت فلانا، وأكذبته، والتكذيب، والمكاذبة، ولا مكذبة بمعنى لا أكذبك، وقراءة لا يكذبونك في معنى لا يجدونك كاذبا أو لا ينسبونك إلى الكذب","what_is_not_ar":"لا يدخل فيه إنشاء الكذب نفسه، ولا الإغراء بقول كذب عليك، ولا كذب الحملة أو اللبن"},"support_links":[]},{"boundary":"Dal, belirli kalıbın 'sana düşer, onu yap' anlamıyla sınırlıdır; yalın köke genel bir zorunluluk veya özendirme anlamı vermez.","branch_kind":"collocation","branch_ref":"root_001290/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَٰذِب","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:ka`*ib|ROOT:k*b|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"96:16:2:1","qac_word_ref":"96:16:2","surface_ar":"كَٰذِبَةٍ"}],"gloss":"onu üstlen; sana düşer","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kalıp, söz konusu işin muhataba düşen bir yükümlülük olduğunu bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı kalıp, muhatabı o işi üstlenmeye yönelten güçlü bir özendirme olarak kullanılabilir."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalıbın hem yükümlülük bildiren hem de eyleme yönelten iki işlevini birlikte veren karşılıktır.","boundary_detail":"Dal, belirli kalıbın 'sana düşer, onu yap' anlamıyla sınırlıdır; yalın köke genel bir zorunluluk veya özendirme anlamı vermez.","branch_image_ar":"كذب عليك بمعنى الزم وعليك به","concept_gloss":"onu üstlen; sana düşer","contextual_glosses":[{"applicability":"Kalıbın yükümlülük bildiren yönünün öne çıktığı cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Buyruk ve güçlü özendirme tonunu tek başına tam olarak göstermez.","preserves":"İşin muhataba düşen bir yükümlülük oluşunu açıkça korur."},"facet_ids":["F001"],"text":"onu yapmalısın","usage_role":"contextual"},{"applicability":"Kalıbın muhatabı işe yönelten özendirme işlevinin baskın olduğu bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İşin önceden var olan bir yükümlülük olarak muhataba düştüğünü zorunlu biçimde bildirmez.","preserves":"Muhatabı söz konusu işi yapmaya yönelten güçlü çağrıyı korur."},"facet_ids":["F002"],"text":"haydi, onu üstlen","usage_role":"contextual"}],"definition":"Belirli bir kalıp içinde, bir şeyin kişiye düşen bir yükümlülük olduğunu bildirmek veya kişiyi onu yapmaya yöneltmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kalıp, söz konusu işin muhataba düşen bir yükümlülük olduğunu bildirir."},{"facet_id":"F002","role":"extension","statement":"Aynı kalıp, muhatabı o işi üstlenmeye yönelten güçlü bir özendirme olarak kullanılabilir."}],"identity_rationale":"Kaynak ifadesi belirli bir kalıbı zorunluluk bildirme ve bir işi yapmaya yöneltme anlamlarıyla açıklar. Bu anlamın yalan söylemeyle doğrudan bir bileşeni yoktur ve yalnız söz konusu kalıp içinde geçerlidir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"şunu üstlen; sana düşer veya onu yapmalısın"}],"lexicalization_note":"Tanım yalnızca verilen kalıplaşmış söyleyişi açıklar; zorunluluk ve yöneltme anlamları yalın biçime taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yükümlülük, özendirme ve bağlayıcılıkla doğrudan sınır kuran üç aday seçildi, yalnızca çalışma azmi veya uzak kök dallarıyla ilişkili adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli kalıbın 'sana düşer, onu yap' değeridir; komşu dal genel emir ve buyurma sistemidir.","focus_only":"Zorunluluk ile güçlü yöneltmeyi yalnız belirli bir kalıplaşmış söyleyişte birleştirir.","gloss":"kalıplaşmış yükümlülük ile genel buyruk","neighbor_only":"Genel buyruk, yasak karşıtı emir ve buyruğa uyma alanlarını kapsar.","neighbor_ref":"root_000051/B002","relation_type":"near_synonym","shared_zone":"İki dal da muhataptan bir eylemi gerçekleştirmesini isteme veya bunu gerekli kılma alanındadır."},{"boundary_match":"partial","distinction":"Odak dal yükümlülük bildirimini de taşır ve belirli bir kalıba bağlıdır; komşu dalın çekirdeği genel teşvik ve kışkırtmadır.","focus_only":"Bir işin muhataba düşen yükümlülük olduğunu da bildirebilir.","gloss":"üstlenmeye yöneltme ile kışkırtma","neighbor_only":"Özellikle çatışmaya yönelik kışkırtma, teşvik ve harekete geçirme anlamlarını kapsar.","neighbor_ref":"root_000309/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da muhatabı bir eyleme kuvvetle yöneltme işlevinde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal kalıplaşmış bir çağrı ve yükümlülük bildirimidir; komşu dal dışsal bir hüküm veya güçle bağlayıcılık kurma işlemidir.","focus_only":"Söyleyiş yoluyla muhatabı işi üstlenmeye çağırır.","gloss":"sözel yöneltme ile bağlayıcı kılma","neighbor_only":"Bir şeyi hüküm, kanıt, yönetim veya zor kullanmayla kişiye bağlayıp kaçınılmaz kılar.","neighbor_ref":"root_001354/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir işin kişi için gerekli veya bağlayıcı hale gelmesi alanında kesişir."}],"source_phrase_ar":"كذب عليك كذا بمعنى الإغراء أي عليك به أو قد وجب عليك (maqayis); كذب عليكم الحج أي وجب عليكم ودونكم الحج (ayn); كذب عليك كذا وكذا في معنى الإغراء (jamhara); كذب عليكم الحج أي وجب (sihah); كذب عليك الحج قيل معناه وجب فعليك به (mufradat)","source_summary":"Kaynaklar bu kalıplaşmış söyleyişi, bir işin muhataba düşmesi ve muhatabın o işi yapmaya yöneltilmesi anlamlarında ortaklaşa açıklar.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه كذب عليك الحج والجهاد والعسل ونحوها إذا أريد الوجوب أو الإغراء أو دونك الشيء","what_is_not_ar":"لا يدخل فيه الإخبار بالكذب، ولا تكذيب المخاطب، ولا كذب الحملة أو اللبن"},"support_links":[]},{"boundary":"Anlam yalnız saldırı hamlesi bağlamında ve olumlu-olumsuz biçimlerin karşıtlığıyla geçerlidir; genel yalan veya genel cesaret anlamı değildir.","branch_kind":"collocation","branch_ref":"root_001290/B004","candidate_links":[{"candidate_id":"cand_6927a041038dedb94467","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كَٰذِب","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:ka`*ib|ROOT:k*b|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"96:16:2:1","qac_word_ref":"96:16:2","surface_ar":"كَٰذِبَةٍ"}],"gloss":"hamlede duraksamak; olumsuzda sonuna kadar ilerlemek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Olumlu kalıp, saldırıya geçtikten sonra durmayı, geri kalmayı veya korkaklık göstermeyi bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Olumsuz kalıp, saldırganın durmadan ilerleyerek vuruşa kadar hamleyi sürdürdüğünü bildirir."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Savaş hamlesine bağlı olumlu duraksama ile olumsuz kalıptaki kesintisiz ilerlemeyi birlikte karşılar.","boundary_detail":"Anlam yalnız saldırı hamlesi bağlamında ve olumlu-olumsuz biçimlerin karşıtlığıyla geçerlidir; genel yalan veya genel cesaret anlamı değildir.","branch_image_ar":"صدق الحملة أو كذبها","concept_gloss":"hamlede duraksamak; olumsuzda sonuna kadar ilerlemek","contextual_glosses":[{"applicability":"Saldırıya başladıktan sonra geri duran veya korkaklık gösteren kişi için olumlu kalıpta uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Olumsuz kalıbın durmaksızın ilerleyip vuruşa ulaşma anlamını kapsamaz.","preserves":"Hamleyi tamamlamadan geri durma ve cesaret yitirme yönünü korur."},"facet_ids":["F001"],"text":"hamleden caymak","usage_role":"contextual"},{"applicability":"Olumsuz kalıpta saldırganın vuruşa kadar ilerlemeyi sürdürdüğü bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Olumlu kalıptaki duraksama ve korkaklık anlamını kapsamaz.","preserves":"Hamlede durmama, korkmama ve saldırıyı vuruşa kadar sürdürme yönünü korur."},"facet_ids":["F002"],"text":"geri durmadan saldırmak","usage_role":"contextual"}],"definition":"Bir saldırı hamlesinde geri durup hamleyi tamamlamamak veya korkaklık göstermektir; olumsuz kalıpta ise durmadan ilerleyip vuruncaya kadar hamleyi sürdürmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Olumlu kalıp, saldırıya geçtikten sonra durmayı, geri kalmayı veya korkaklık göstermeyi bildirir."},{"facet_id":"F002","role":"specialization","statement":"Olumsuz kalıp, saldırganın durmadan ilerleyerek vuruşa kadar hamleyi sürdürdüğünü bildirir."}],"identity_rationale":"Kaynak ifadesi savaş hamlesindeki iki karşıt kalıbı birlikte verir: olumlu biçim hamlede durma, geri çekilme veya korkaklık; olumsuz biçim ise durmadan ilerleyip vuruşa ulaşmadır. Dalın kimliği bu kutuplu kalıp düzenine uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"saldırıya geçti ama duraksadı veya korktu"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"saldırıya geçti ve vuruncaya kadar durmadı; korkmadı"}],"lexicalization_note":"Tanım savaş hamlesine bağlı iki kalıbı korur; duraksama ve kararlılıkla ilerleme anlamları yalın biçime genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hamlede durma, saldırının kendisi, cesaret ve kesintisiz hamlenin sonucu ile doğrudan sınır kuran dört aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir hamlenin seyri ve onun olumsuz karşıt kalıbıdır; komşu dal kişinin daha genel korkaklık niteliğidir.","focus_only":"Başlatılmış bir saldırı hamlesinin sürdürülüp sürdürülmediğini kalıp içinde değerlendirir.","gloss":"hamlede geri durma ile korkaklık","neighbor_only":"Kişinin genel olarak atılganlıktan kesilmiş ve korkak oluşunu betimler.","neighbor_ref":"root_001150/B008","relation_type":"near_neighbor","shared_zone":"Saldırıya devam etmeme, geri kalma ve korkaklık bağlamlarında iki alan kesişir."},{"boundary_match":"field_only","distinction":"Odak dal saldırının sürdürülme niteliğini bildirir; komşu dal saldırı ve koşu hareketinin kendisidir.","focus_only":"Hamlenin duraksama veya sonuna kadar sürme bakımından sonucunu değerlendirir.","gloss":"hamlenin seyri ile hücum eylemi","neighbor_only":"Düşmana saldırma, hücum etme ve koşma eyleminin kendisini bildirir.","neighbor_ref":"root_000782/B003","relation_type":"same_field","shared_zone":"İki dal da savaşta düşmana yönelen saldırı hamlesi alanındadır."},{"boundary_match":"partial","distinction":"Odak dal belirli saldırı kalıbında gerçekleşen davranışı değerlendirir; komşu dal daha genel bir cesaret ve atılganlık niteliğidir.","focus_only":"Olumlu ve olumsuz kalıplarla tek bir hamlede durma ya da sürdürme karşıtlığını kurar.","gloss":"hamleyi sürdürme ile cesaret","neighbor_only":"Genel cesaret, atılganlık ve düşmana doğru öne çıkma niteliğini bildirir.","neighbor_ref":"root_001207/B006","relation_type":"near_neighbor","shared_zone":"Hamleyi korkmadan sürdürme bağlamında iki anlam birbirine yaklaşır."},{"boundary_match":"partial","distinction":"Odak dal hamlenin kesintisiz sürmesini yeterli görür; komşu dal buna düşmanı yenme sonucunu da ekler.","focus_only":"Hamlede durma ile durmadan sürdürme karşıtlığını, zafer şartı aramadan bildirir.","gloss":"kesintisiz hamle ile yenilgiye uğratma","neighbor_only":"Kesintisiz bir saldırıyla karşı tarafı yenme sonucunu özellikle içerir.","neighbor_ref":"root_000003/B007","relation_type":"near_neighbor","shared_zone":"Duraksamadan yapılan saldırı hamlesi iki dalın ortak sahnesidir."}],"source_phrase_ar":"حمل فلان ثم كذب أي لم يصدق في الحملة (maqayis); حمل فلان على فلان فما كذب حتى طعن أو ضرب أي ما وقف (jamhara); حمل فلان فما كذب أي ما جبن (sihah); حمل فلان على قرنه فكذب (mufradat)","source_summary":"Kaynaklar saldırı hamlesini sürdürmeme ile korkaklık arasında bağ kurar; olumsuz kalıp ise durmayıp vuruşa kadar ilerleme anlamını verir.","sources":["MQ","JA","SI","MU"],"what_is_ar":"يدخل فيه كذب في الحملة إذا لم يصدقها أو جبن، ونفي الكذب عن الحملة إذا مضى فيها ولم يقف حتى يطعن أو يضرب","what_is_not_ar":"لا يدخل فيه الكذب في الخبر، ولا الإغراء، ولا وقوف الوحشي بعد شوط"},"support_links":["sup_65aa5d5b161877ad020f"]},{"boundary":"Dal, 'yapmakta gecikmedi' değerindeki kalıpla sınırlıdır; genel hız, acele veya yalan anlamı değildir.","branch_kind":"collocation","branch_ref":"root_001290/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَٰذِب","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:ka`*ib|ROOT:k*b|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"96:16:2:1","qac_word_ref":"96:16:2","surface_ar":"كَٰذِبَةٍ"}],"gloss":"gecikmeden yapmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, belirtilen işi yapmadan önce beklemez veya oyalanmaz."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Beklememenin sonucu, işin gecikmeden gerçekleştirilmesidir."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalıbın hem oyalanmama aşamasını hem de işi gecikmeden gerçekleştirme sonucunu özlü biçimde karşılar.","boundary_detail":"Dal, 'yapmakta gecikmedi' değerindeki kalıpla sınırlıdır; genel hız, acele veya yalan anlamı değildir.","branch_image_ar":"ما كذب أن فعل أي ما لبث","concept_gloss":"gecikmeden yapmak","contextual_glosses":[{"applicability":"Söz konusu işin beklenmeden gerçekleştiği geçmiş zaman anlatımlarında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Oyalanmama aşamasını ve işin gecikmeden gerçekleşmesini doğal kullanımda korur."},"facet_ids":["F001","F002"],"text":"hemen yaptı","usage_role":"contextual"}],"definition":"Belirli bir olumsuz kalıp içinde, bir kişinin söz konusu işi yapmakta oyalanmadığını ve gecikmeden yaptığını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, belirtilen işi yapmadan önce beklemez veya oyalanmaz."},{"facet_id":"F002","role":"extension","statement":"Beklememenin sonucu, işin gecikmeden gerçekleştirilmesidir."}],"identity_rationale":"Kaynak ifadesi yalnız belirli bir olumsuz kalıp içinde kişinin bir işi yapmakta oyalanmadığını ve gecikmediğini bildirir. Geçici dal çerçevesi bu yapıyı ve anlamı doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yapmakta gecikmedi; hemen yaptı"}],"lexicalization_note":"Tanım yalnız verilen olumsuz kalıbın gecikmeme anlamını açıklar; hız ve çabukluk yalın kökün anlamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; gecikmeme, ilk anda yapma ve genel acele arasındaki sınırı en iyi gösteren üç aday seçildi, yalnız zaman veya tekrar alanını paylaşan adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnız kalıplaşmış gecikmeme anlamıdır; komşu dal benzer kalıbın yanında koşma hızına ilişkin ayrı bir alan da taşır.","focus_only":"Gecikmemeyi yalnız belirli bir 'yapmakta oyalanmadı' kalıbında bildirir.","gloss":"gecikmeme ile az bekleme","neighbor_only":"Ayrı bir kullanımda koşmanın görece hızlı oluşunu da kapsar.","neighbor_ref":"root_000973/B009","relation_type":"near_synonym","shared_zone":"Bir işi yapmakta az bekleme veya hiç oyalanmama anlamında iki dal büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal bekleme süresinin yokluğuna odaklanır; komşu dal eylemin durumun ilk anındaki oluşunu ayrıca şart koşar.","focus_only":"Bir işi yapmak öncesindeki gecikmenin bulunmadığını kalıplaşmış biçimde bildirir.","gloss":"gecikmeden yapma ile ilk anda yapma","neighbor_only":"Eylemin ilk anda, durum henüz yatışmadan veya olayın başlangıç itkisiyle yapılmasını vurgular.","neighbor_ref":"root_001185/B002","relation_type":"near_synonym","shared_zone":"Bir eylemin beklenmeden ve hemen gerçekleşmesi iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal yalnız gecikmenin yokluğunu bildirir; komşu dal hızlandırma, öne alma ve vaktinden önce isteme gibi ek yönler taşır.","focus_only":"Belirli bir işin yapılmasında gecikme olmadığını bildirir.","gloss":"gecikmeme ile acele etme","neighbor_only":"Bir şeyi vaktinden önce isteme, öne alma ve genel acele ettirme alanlarını kapsar.","neighbor_ref":"root_000987/B001","relation_type":"near_neighbor","shared_zone":"İşin kısa sürede veya beklenmeden yapılması bağlamında iki anlam kesişebilir."}],"source_phrase_ar":"ما كذب فلان أن فعل كذا أي ما لبث (maqayis;sihah)","source_summary":"Kaynakların ortak açıklaması, belirli kalıbın kişinin bir işi yapmakta beklemediğini ve gecikmediğini bildirmesidir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه قولهم ما كذب فلان أن فعل كذا إذا لم يلبث ولم يتأخر","what_is_not_ar":"لا يدخل فيه الكذب في الخبر، ولا وجوب كذب عليك، ولا كذب اللبن"},"support_links":[]},{"boundary":"Anlam yalnız dişi devenin sütüne ilişkin kalıpta, sütün kaybolması veya beklenen süre boyunca devam etmemesiyle sınırlıdır.","branch_kind":"collocation","branch_ref":"root_001290/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَٰذِب","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:ka`*ib|ROOT:k*b|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"96:16:2:1","qac_word_ref":"96:16:2","surface_ar":"كَٰذِبَةٍ"}],"gloss":"sütün kesilmesi veya beklenenden önce tükenmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişi devenin sütü gider veya kesilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir açıklamada süt bir süre sürecek sanılır, fakat bu beklentinin tersine devam etmez."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dişi devenin sütüne bağlı kaybolma çekirdeğini ve devam beklentisinin boşa çıkmasını birlikte karşılar.","boundary_detail":"Anlam yalnız dişi devenin sütüne ilişkin kalıpta, sütün kaybolması veya beklenen süre boyunca devam etmemesiyle sınırlıdır.","branch_image_ar":"كذب لبن الناقة إذا ذهب ولم يدم","concept_gloss":"sütün kesilmesi veya beklenenden önce tükenmesi","contextual_glosses":[{"applicability":"Sütün artık gelmediği ve önceki üretimin sona erdiği bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sütün süreceği beklentisinin özellikle boşa çıkmış olduğunu tek başına bildirmez.","preserves":"Dişi devenin sütünün gitmesi veya sona ermesi çekirdeğini korur."},"facet_ids":["F001"],"text":"sütü kesildi","usage_role":"contextual"},{"applicability":"Sütün belirli bir süre devam edeceği beklentisinin gerçekleşmediği açıklayıcı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sütün devamına ilişkin beklentiyi ve beklenenden önce kesilmesini birlikte korur."},"facet_ids":["F001","F002"],"text":"sütü umulduğu kadar sürmedi","usage_role":"explanatory"}],"definition":"Dişi devenin sütünün kaybolması veya bir süre devam edeceği sanıldığı halde beklenenden önce kesilmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dişi devenin sütü gider veya kesilir."},{"facet_id":"F002","role":"source_variant","statement":"Bir açıklamada süt bir süre sürecek sanılır, fakat bu beklentinin tersine devam etmez."}],"identity_rationale":"Kaynak ifadesi dişi devenin sütünün gitmesini ortak çekirdek olarak verir; toplu kanıttaki ek açıklama, bir süre devam edeceği sanılan sütün beklenenden önce kesilmesini belirtir. Geçici çerçeve iki yönü de doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"dişi devenin sütü kesildi veya umulduğu kadar sürmedi"}],"lexicalization_note":"Tanım yalnız dişi devenin sütünü konu alan kalıba bağlıdır; genel tükenme veya genel beklenti boşa çıkması anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; süt kesilmesi, geri dönüş beklentisi ve süt bolluğu eksenini açıklayan üç aday seçildi, yalnız başka sıvıları veya hayvan özelliklerini paylaşan adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dişi devenin sütüne ve kimi kullanımda boşa çıkan süreklilik beklentisine bağlıdır; komşu dal süt veriminin azalmasını ve yağmuru da kapsar.","focus_only":"Dişi devenin sütünün gitmesini ve beklenen süre boyunca devam etmemesini bildirir.","gloss":"sütün beklenmedik kesilmesi ile verimin azalması","neighbor_only":"Sütün azalmasını veya kesilmesini yağmurun azalması ve kesilmesiyle aynı anlam alanında kapsar.","neighbor_ref":"root_000305/B005","relation_type":"near_synonym","shared_zone":"Sütün azalması veya bütünüyle kesilmesi iki dalın doğrudan ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal gerçekleşen kaybı ve boşa çıkan devam beklentisini anlatır; komşu dal kayıptan sonraki geri dönüş umuduna odaklanır.","focus_only":"Sütün fiilen gittiğini veya beklenen süre boyunca devam etmediğini bildirir.","gloss":"sütün kesilmesi ile geri dönme umudu","neighbor_only":"Sütü kesilen ya da sütü kuşkulu olan hayvanda sütün geri dönmesi umudunu bildirir.","neighbor_ref":"root_001015/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da kesilmiş veya belirsiz hale gelmiş süt verimi durumunu konu alır."},{"boundary_match":"opposed","distinction":"Odak dal süt veriminin sona eren kutbundadır; komşu dal aynı alanın bol ve güçlü verim kutbundadır.","focus_only":"Sütün kaybolmasını, kesilmesini veya beklenenden az sürmesini bildirir.","gloss":"süt kesilmesi ile süt bolluğu","neighbor_only":"Dişi devenin süt bakımından çok verimli ve bol oluşunu bildirir.","neighbor_ref":"root_000200/B005","relation_type":"polarity_pair","shared_zone":"İki dal da dişi devenin süt veriminin durumu üzerinde ortak bir nicelik ekseni kurar."}],"source_phrase_ar":"كذب لبن الناقة ذهب وفيه نظر وقياسه صحيح (maqayis); كذب لبن الناقة أي ذهب (sihah); كذب لبن الناقة إذا ظن أن يدوم مدة فلم يدم (mufradat)","source_summary":"Toplu kanıt sütün gitmesi çekirdeğinde birleşir; bunun yanında, devam edeceği sanılan sütün beklenen süreyi tamamlamadan kesilmesi biçiminde daha ayrıntılı bir yorum da verir.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه كذب لبن الناقة إذا ذهب أو ظن دوامه فلم يدم","what_is_not_ar":"لا يدخل فيه كذب الخبر، ولا كذب الحملة، ولا كذب عليك في الإغراء"},"support_links":[]},{"boundary":"Dal yalnız yaban hayvanının koşma, durma ve arkasına bakma dizisine bağlıdır; genel durma ya da genel koşu anlamı değildir.","branch_kind":"collocation","branch_ref":"root_001290/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَٰذِب","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:ka`*ib|ROOT:k*b|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"96:16:2:1","qac_word_ref":"96:16:2","surface_ar":"كَٰذِبَةٍ"}],"gloss":"koşup arkasına bakmak için durmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yaban hayvanı önce belirli bir mesafe koşar, ardından hareketini durdurur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Durmanın amacı hayvanın arkasında kalan yere veya şeye bakmasıdır."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaban hayvanını, koşudan sonraki durmayı ve durmanın geriye bakma amacını birlikte karşılar.","boundary_detail":"Dal yalnız yaban hayvanının koşma, durma ve arkasına bakma dizisine bağlıdır; genel durma ya da genel koşu anlamı değildir.","branch_image_ar":"كذب الوحشي إذا جرى ثم وقف","concept_gloss":"koşup arkasına bakmak için durmak","contextual_glosses":[{"applicability":"Yaban hayvanının hareket dizisinin anlatı içinde doğal bir cümleyle çevrildiği bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Önce koşmayı, sonra durup geride kalana bakmayı doğal anlatım sırasıyla korur."},"facet_ids":["F001","F002"],"text":"bir süre koştu, sonra dönüp baktı","usage_role":"contextual"}],"definition":"Bir yaban hayvanının belirli bir mesafe koştuktan sonra arkasında ne olduğunu görmek için durmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yaban hayvanı önce belirli bir mesafe koşar, ardından hareketini durdurur."},{"facet_id":"F002","role":"specialization","statement":"Durmanın amacı hayvanın arkasında kalan yere veya şeye bakmasıdır."}],"identity_rationale":"Tek kaynaklı ifade, yaban hayvanının belirli bir mesafe koşmasından sonra arkasına bakmak için durduğu aşamalı hareketi eksiksiz biçimde tanımlar. Geçici dal çerçevesi katılımcıyı, hareket sırasını ve amacı korur.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yaban hayvanı bir mesafe koşup arkasına bakmak için durdu"}],"lexicalization_note":"Tanım yalnız yaban hayvanını özne alan kalıba ve belirtilen hareket dizisine bağlıdır; yalın biçime bir hareket anlamı yüklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hayvanda hareketin kesilmesi, ileri hareket ve bakış amacıyla doğrudan karşılaştırma sağlayan dört aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın katılımcısı yaban hayvanıdır ve amaç arkasına bakmaktır; komşu dal av köpeğinin ilgisini veya takibini kesmesine odaklanır.","focus_only":"Yaban hayvanı koşusunu geriye bakmak amacıyla durdurur.","gloss":"koşudan sonra durma ile avdan vazgeçme","neighbor_only":"Köpek avını yakaladıktan sonra gevşer, ondan döner veya başka şeyle oyalanır.","neighbor_ref":"root_001084/B005","relation_type":"near_synonym","shared_zone":"Bir hayvanın koşu veya takip hareketini bir aşamadan sonra kesmesi iki dalda ortaktır."},{"boundary_match":"partial","distinction":"Odak dal belirli bir koşu-sonrası bakış dizisidir; komşu dal daha genel durdurma, kalma ve konaklama ilişkilerini kapsar.","focus_only":"Koşudan sonra özellikle geriye bakmak için gerçekleşen kısa durmayı bildirir.","gloss":"geriye bakmak için durma ile konaklama","neighbor_only":"Binek hayvanını tutmayı, bir yerde kalmayı, inmeyi veya bir kişiye yönelmeyi kapsar.","neighbor_ref":"root_000997/B003","relation_type":"near_neighbor","shared_zone":"Hareket halindeki bir canlının ilerlemeyi kesmesi iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal koşu sonrasındaki durmayı temel alır; komşu dal kesintisiz ve güçlü ileri hareketi temel alır.","focus_only":"Koşunun ardından hareketin kesilmesini ve geriye bakmayı içerir.","gloss":"koşuyu kesme ile hızla ileri atılma","neighbor_only":"Binek hayvanının hızla ileri atılmasını ve kendini öne fırlatır gibi ilerlemesini bildirir.","neighbor_ref":"root_001209/B005","relation_type":"near_neighbor","shared_zone":"İki dal da hayvanın hızlı ilerleyişini konu alan hareket sahnesindedir."},{"boundary_match":"thematic_only","distinction":"Odak dalın çekirdeği koşu sonrasında durma dizisidir; komşu dal ise önceki bir hareket gerektirmeyen bakış eylemidir.","focus_only":"Bakışı, öncesindeki koşu ve durma dizisinin amacı olarak içerir.","gloss":"hareket dizisi ile dikkatli bakış","neighbor_only":"Baş veya gözleri kaldırarak bir şeye dikkatle bakma eylemini doğrudan bildirir.","neighbor_ref":"root_000256/B008","relation_type":"thematic","shared_zone":"Bir şeyi görmek üzere yöneltilen bakış, iki anlamın aynı sahnede bulunabilen unsurudur."}],"source_phrase_ar":"كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه (jamhara)","source_qualifications":[{"kind":"sole_attestation","summary":"Yaban hayvanı bir mesafe koştuktan sonra arkasına bakmak için durur."}],"source_summary":"Bu özel kullanım tek bir kaynakta, yaban hayvanının koşu sonrasında arkasına bakmak amacıyla durduğu ardışık hareket olarak tanıklanır.","sources":["JA"],"what_is_ar":"يدخل فيه كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه","what_is_not_ar":"لا يدخل فيه كذب الحملة، ولا كذب اللبن، ولا الكذب في القول"},"support_links":[]},{"boundary":"Dal, ilgili yalın biçimin 'kişinin iç benliği' adını taşımasıyla sınırlıdır; kişinin yalan söylemesi veya benliğin aldatıcılığı anlamını içermez.","branch_kind":"bare","branch_ref":"root_001290/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَٰذِب","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:ka`*ib|ROOT:k*b|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"96:16:2:1","qac_word_ref":"96:16:2","surface_ar":"كَٰذِبَةٍ"}],"gloss":"iç benlik","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözcük, bir yalan niteliği yüklemeden doğrudan kişinin iç benliğini adlandırır."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynak ifadesindeki doğrudan adlandırmayı, yalan söyleme niteliği eklemeden karşılar.","boundary_detail":"Dal, ilgili yalın biçimin 'kişinin iç benliği' adını taşımasıyla sınırlıdır; kişinin yalan söylemesi veya benliğin aldatıcılığı anlamını içermez.","branch_image_ar":"النفس الكذوب","concept_gloss":"iç benlik","contextual_glosses":[{"applicability":"Eski ve tek kaynaklı adlandırmanın modern Türkçede açıklanması gereken bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözcüğün kişiyi içeriden kuran benliği adlandırmasını açık biçimde korur."},"facet_ids":["F001"],"text":"kişinin kendi iç benliği","usage_role":"explanatory"}],"definition":"İlgili sözcüğün, kişideki iç benliği veya kendi olma bilincini doğrudan adlandıran bir isim olarak kullanılmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözcük, bir yalan niteliği yüklemeden doğrudan kişinin iç benliğini adlandırır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kaynak ifadesinde bulunmayan yalan söyleme veya aldatma niteliğini benliğe yükler.","collision":"Kişiyi yalan söyleyen biri olarak betimleyen başka daldaki sıfat anlamıyla karışır.","fit":"broadening","loses":null,"preserves":"Benliği konu alan bir adlandırma bulunduğu izlenimini kısmen korur."},"text":"yalancı benlik"}],"identity_rationale":"Kaynak ifadesi iç benliği 'yalancı' diye niteleyen bir söz öbeği kurmaz; ilgili sözcüğü doğrudan iç benliğin adı olarak eşitler. Dal korunabilir, ancak tanım bir ahlak niteliği değil, bağımsız bir adlandırma olarak yeniden çerçevelenmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"iç benlik; kişinin kendisi"}],"lexicalization_note":"Tanım sözcüğün yalın biçimde doğrudan iç benliği adlandırmasını verir; başka dallardaki kişi sıfatları veya özel kalıplar bu anlama alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; iç benliği doğrudan adlandıran veya onun işlevini konu alan üç yararlı karşılaştırma seçildi, yalnız kişilik değişimi ve uzak tematik kullanımlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnız iç benliği adlandırır; komşu dal iç benliği bedenin yaşamsal özü, kanı ve kalbiyle bir araya getiren daha geniş bir anlam kümesidir.","focus_only":"Tek bir sözcüğün doğrudan iç benlik adı olarak kullanımını bildirir.","gloss":"iç benlik ile yaşam özü","neighbor_only":"İç benliğin yanında kan, yaşam özü ve kalp gibi birbiriyle ilişkili adlandırmaları da kapsar.","neighbor_ref":"root_000187/B004","relation_type":"near_synonym","shared_zone":"Kişinin iç varlığı veya kendisi anlamında iki dal büyük ölçüde örtüşebilir."},{"boundary_match":"partial","distinction":"Odak dal bağımsız iç benlik adıdır; komşu dal bu değeri belirli bir kalıp içinde verir ve ayrıca yakın dost anlamına genişler.","focus_only":"Yalın bir sözcükle kişinin iç benliğini doğrudan adlandırır.","gloss":"iç benlik ile kişinin kendisi","neighbor_only":"Belirli bir soru kalıbında kişinin kendisini, başka kullanımda ise yakın ve seçkin dostu bildirir.","neighbor_ref":"root_000059/B006","relation_type":"near_synonym","shared_zone":"Kişinin kendisini veya iç benliğini gösteren kullanımlarda iki dal örtüşür."},{"boundary_match":"thematic_only","distinction":"Odak dal varlığın adıdır; komşu dal bu varlığa yüklenen süsleme ve yanıltıcı yönlendirme eylemidir.","focus_only":"İç benliği yalnızca bir varlık olarak adlandırır.","gloss":"iç benlik ile benliğin yönlendirmesi","neighbor_only":"İç benliğin veya kötülüğe yönelten bir gücün bir işi süsleyip kişiye çekici göstermesini bildirir.","neighbor_ref":"root_000763/B002","relation_type":"thematic","shared_zone":"İç benlik iki anlamın aynı düşünsel sahnesinde yer alır."}],"source_phrase_ar":"الكذوب النفس (jamhara)","source_qualifications":[{"kind":"sole_attestation","summary":"Sözcük herhangi bir ahlak niteliği eklenmeden doğrudan kişinin iç benliğini adlandırır."}],"source_summary":"Bu yalın adlandırma tek bir kaynakta, ilgili sözcüğün doğrudan kişinin iç benliğiyle eşitlenmesi biçiminde tanıklanır.","sources":["JA"],"what_is_ar":"يدخل فيه إطلاق الكذوب على النفس","what_is_not_ar":"لا يدخل فيه وصف الرجل بالكذاب أو الكذوب، ولا أكاذيب الأخبار"},"support_links":[]},{"boundary":"Dal, boyası veya deseni gerçek dokuma bezemesi sanısı veren kumaşla sınırlıdır; genel yalan, her desenli kumaş veya kişi adı değildir.","branch_kind":"bare","branch_ref":"root_001290/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَٰذِب","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:ka`*ib|ROOT:k*b|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"96:16:2:1","qac_word_ref":"96:16:2","surface_ar":"كَٰذِبَةٍ"}],"gloss":"dokuma bezemesi sanısı veren boyalı kumaş","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne, çeşitli boya renkleriyle renklendirilmiş veya yüzeyine desen işlenmiş bir kumaştır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Boya ve desen, kumaşın dokuma yoluyla bezenmiş olduğu izlenimini verir."}}],"root_ar":"ك ذ ب","root_id":"root_001290","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesnenin kumaş oluşunu, boya veya deseni ve gerçek dokuma bezemesi gibi görünmesini birlikte karşılar.","boundary_detail":"Dal, boyası veya deseni gerçek dokuma bezemesi sanısı veren kumaşla sınırlıdır; genel yalan, her desenli kumaş veya kişi adı değildir.","branch_image_ar":"الكذابة ثوب يكذب بحاله","concept_gloss":"dokuma bezemesi sanısı veren boyalı kumaş","contextual_glosses":[{"applicability":"Kumaş türünün üretim görünüşüyle birlikte açıkça anlatılması gereken bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Boyama veya yüzey deseniyle oluşturulan dokuma bezemesi izlenimini korur."},"facet_ids":["F001","F002"],"text":"dokuma desenli gibi görünen boyalı kumaş","usage_role":"explanatory"}],"definition":"Çeşitli renklerle boyanmış veya desenlenmiş, bu yüzden dokuma yoluyla bezenmiş gibi görünen bir kumaş ya da giysidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne, çeşitli boya renkleriyle renklendirilmiş veya yüzeyine desen işlenmiş bir kumaştır."},{"facet_id":"F002","role":"specialization","statement":"Boya ve desen, kumaşın dokuma yoluyla bezenmiş olduğu izlenimini verir."}],"identity_rationale":"Kaynak ifadesi çeşitli renklerle boyanmış veya desenlenmiş bir kumaşı, dokuma yoluyla bezenmiş gibi görünmesi üzerinden tanımlar; bir açıklama bu yanıltıcı görünüşü adlandırmanın gerekçesi yapar. Geçici çerçeve nesneyi ve görünüş ilişkisini doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"dokuma bezemesi sanısı veren boyalı veya desenli kumaş"}],"lexicalization_note":"Tanım yalın bir kumaş adını ve onu ayıran görünüş özelliğini verir; genel aldatıcı görünüş anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dokuma bezemesi, renk etkisi, boyama, resimli kumaş ve yüzeyle yanıltma sınırlarını gösteren beş aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal boya veya desenin dokuma bezemesi sanısı vermesine dayanır; komşu dal gerçek dokuma bezemesi ve onun üretimiyle ilgilidir.","focus_only":"Boya veya yüzey deseniyle gerçek dokuma bezemesi varmış izlenimi veren kumaşı adlandırır.","gloss":"bezemeye benzeyen boya ile gerçek dokuma bezemesi","neighbor_only":"Kumaştaki gerçek dokuma bezemesini, kenar süslemesini ve bu işi yapanları kapsar.","neighbor_ref":"root_000340/B004","relation_type":"near_neighbor","shared_zone":"Kumaş yüzeyindeki bezeme görünüşü iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal dokuma bezemesi sanısına dayanır; komşu dal kumaş renginin bakışa göre değişmesine dayanır.","focus_only":"Birden çok boya veya desenle dokunmuş gibi görünen kumaşı bildirir.","gloss":"boyalı desen yanılsaması ile değişken renk görünüşü","neighbor_only":"Bakış açısına göre renkleri değişiyormuş gibi görünen belirli bir kumaş türünü bildirir.","neighbor_ref":"root_001252/B010","relation_type":"near_neighbor","shared_zone":"Renkli bir kumaşın görünüşünün algıda özel bir etki oluşturması iki dalda ortaktır."},{"boundary_match":"field_only","distinction":"Odak dal bezeme sanısı veren tasarlanmış görünüşü adlandırır; komşu dal belirli renkleri ve boyanın düzensiz tutmasını konu alır.","focus_only":"Çok renkli boya veya desenin dokuma bezemesi izlenimi vermesini temel alır.","gloss":"yanıltıcı bezeme ile alacalı boya","neighbor_only":"Sarı boya, belirli bitkisel renkler ve boyanın alacalı ya da iyi tutmamış çıkmasını kapsar.","neighbor_ref":"root_001428/B005","relation_type":"same_field","shared_zone":"Her iki dal da boyanmış kumaşın renk ve yüzey görünüşü alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal üretim biçimini olduğundan farklı gösteren genel bezeme izlenimine dayanır; komşu dal belirli resim motifleriyle tanımlanır.","focus_only":"Boyanmış veya desenlenmiş yüzeyin dokuma bezemesi sanısı vermesini bildirir.","gloss":"bezeme sanısı veren kumaş ile resimli kumaş","neighbor_only":"Üzerinde kule biçimleri veya başka resimler bulunan belirli bir süslü kumaşı bildirir.","neighbor_ref":"root_000101/B005","relation_type":"same_field","shared_zone":"İki dal da yüzeyi resim veya desenle süslenmiş kumaşları konu alır."},{"boundary_match":"thematic_only","distinction":"Odak dal yalnız kumaş ve dokuma bezemesi görünüşüne bağlıdır; komşu dal metal kaplama işleminden genel yanıltıcı gösterime uzanır.","focus_only":"Kumaşta boya veya desenin dokuma bezemesi sanısı uyandırmasını bildirir.","gloss":"kumaş görünüşü ile kaplama yoluyla yanıltma","neighbor_only":"Bir metali altın veya gümüşle kaplamayı ve bir şeyi gerçek niteliğinden farklı göstermeyi bildirir.","neighbor_ref":"root_001458/B005","relation_type":"thematic","shared_zone":"Bir nesnenin yüzey işlemiyle üretim veya madde niteliğinden farklı görünmesi iki alanda ortaktır."}],"source_phrase_ar":"الكذابة ثوب يصبغ بألوان الصبغ كأنه موشي (ayn); الكذابة ثوب ينقش بلون صبغ كأنه موشى وذلك لأنه يكذب بحاله (mufradat)","source_summary":"Kaynaklar, çeşitli renklerle boyanıp desenlenen ve böylece dokuma bezemesi varmış gibi görünen bir kumaş üzerinde birleşir; toplu kanıt bu yanıltıcı görünüşü adlandırmanın gerekçesi olarak açıklar.","sources":["AY","MU"],"what_is_ar":"يدخل فيه الكذابة للثوب المصبوغ بألوان أو المنقوش كأنه موشى لأنه يكذب بحاله","what_is_not_ar":"لا يدخل فيه الكذب في القول، ولا التكذيب، ولا أسماء الأشخاص"},"support_links":[]},{"boundary":"Saçı tarama ya da uzatma bu dalın parçası değildir; burada ön saç bölgesi ile onu tutmaya dayalı eylemler belirleyicidir.","branch_kind":"mixed_non_bare","branch_ref":"root_001512/B001","candidate_links":[{"candidate_id":"cand_f4fffa0771c9ea0583d1","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَاصِيَة","morph_features":"STEM|POS:N|LEM:naASiyap|ROOT:nSy|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:16:1:1","qac_word_ref":"96:16:1","surface_ar":"نَاصِيَةٍ"}],"gloss":"alın saç çizgisi; buradan tutup çekme ve denetim altına alma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Alındaki saç sınırı ya da ön saçın çıktığı yer, dalın bedensel çekirdeğidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişiyi ön saç bölgesinden kavramak ve çekmek, bedensel çekirdekten türeyen eylem anlamıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İki kişinin birbirinin ön saçından tutup çekişmesi, eylemin karşılıklı gerçekleşen biçimidir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir şeyin ön kısmından tutma görüntüsü, belirli bir söz öbeğinde onun üzerinde denetim ve söz sahibi olmayı anlatır."}}],"root_ar":"ن ص ي","root_id":"root_001512","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedensel bölgeyi, bu bölgeden tutma eylemlerini ve söz öbeğine bağlı denetim uzantısını birlikte temsil eden açıklayıcı üst karşılıktır.","boundary_detail":"Saçı tarama ya da uzatma bu dalın parçası değildir; burada ön saç bölgesi ile onu tutmaya dayalı eylemler belirleyicidir.","branch_image_ar":"الناصية والأخذ بها","concept_gloss":"alın saç çizgisi; buradan tutup çekme ve denetim altına alma","contextual_glosses":[{"applicability":"Ön saçın başladığı bedensel bölgenin adlandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bedensel çekirdeği doğal ve açık biçimde karşılar."},"facet_ids":["F001"],"text":"alındaki saç çizgisi","usage_role":"general"},{"applicability":"Bir kişinin ön saç bölgesinin kavranıp çekildiği eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tutma yerini ve çekme eylemini eksiksiz korur."},"facet_ids":["F002"],"text":"ön saçından tutup çekmek","usage_role":"contextual"},{"applicability":"İki tarafın aynı eylemi karşılıklı yaptığı çekişme bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemin iki taraflı ve karşılıklı oluşunu korur."},"facet_ids":["F003"],"text":"birbirlerinin ön saçından tutuşmak","usage_role":"contextual"},{"applicability":"Yalnızca tutma görüntüsüyle bir şey üzerinde yetki ve denetim kurulduğunu anlatan söz öbeğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Söz öbeğine bağlı denetim ve egemenlik sonucunu korur."},"facet_ids":["F004"],"text":"denetimi altında tutmak","usage_role":"contextual"}],"definition":"Alındaki saç sınırını veya ön saçın çıktığı yeri bildirir; ayrıca birini bu bölgeden tutup çekmeyi, iki kişinin birbirini buradan tutmasını ve belirli bir söz öbeğinde bir şey üzerinde denetim sahibi olmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Alındaki saç sınırı ya da ön saçın çıktığı yer, dalın bedensel çekirdeğidir."},{"facet_id":"F002","role":"extension","statement":"Bir kişiyi ön saç bölgesinden kavramak ve çekmek, bedensel çekirdekten türeyen eylem anlamıdır."},{"facet_id":"F003","role":"associated_use","statement":"İki kişinin birbirinin ön saçından tutup çekişmesi, eylemin karşılıklı gerçekleşen biçimidir."},{"facet_id":"F004","role":"extension","statement":"Bir şeyin ön kısmından tutma görüntüsü, belirli bir söz öbeğinde onun üzerinde denetim ve söz sahibi olmayı anlatır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Saçın başlangıç sınırını, tutma eylemlerini ve denetim uzantısını karşılamaz.","preserves":"Ön taraftaki saç kümesi düşüncesini kısmen korur."},"text":"perçem"},{"category":"confusable","error_profile":{"adds":"Saçtan bağımsız deri ve kemik bölgesini anlamın merkezi yapar.","collision":"Yakın bir beden bölgesinin adıyla karışır.","fit":"displacement","loses":"Saç sınırını ve bu bölgeden tutmaya dayalı bütün eylem anlamlarını kaybeder.","preserves":"Başın ön bölgesine ilişkin yer bilgisini korur."},"text":"alın"}],"identity_rationale":"Kaynak ifadesi, anlamı hem alındaki saç sınırı ve ön saçın çıktığı yer hem de buradan tutma, çekme, karşılıklı çekişme ve bu eylem üzerinden kurulan denetim anlatımı olarak açıkça temellendirir.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"alındaki saç çizgisi ya da ön saçın çıktığı yer"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"birini ön saçından tutmak veya çekmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"karşılıklı olarak ön saçlarından tutup çekişmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"alındaki saç çizgisi için bölgesel bir söyleyiş"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"ön saçlardan tutma"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"onu denetimi altında tutan ve üzerinde söz sahibi olan"}],"lexicalization_note":"Tanım, beden bölgesini bildiren yalın kullanımı; tutma, karşılıklı çekişme ve denetim bildiren eylem ve söz öbeklerinden ayrı katmanlarda tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan dört karşılaştırma beden bölgesi, tutma eylemi, saç bakımı ve bitişik alın alanıyla karışma risklerini en doğrudan açıklayanlardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Eylem bağlamında güçlü bir örtüşme vardır; ancak odak dal bedensel bölgeyi ve karşılıklı çekişmeyi de içerirken komşu, tutmanın baskı ve aşağılama sonucuna yönelir.","focus_only":"Bu dal, ön saç bölgesinin kendi adını ve karşılıklı tutuşmayı da kapsar.","gloss":"ön saçtan tutma ve boyun eğdirme","neighbor_only":"Komşu dal, tutmanın ardından gelen baskı ve aşağılamayı daha belirgin biçimde öne çıkarır.","neighbor_ref":"root_000713/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da birini başın önündeki saç bölgesinden elle tutmayı anlatır."},{"boundary_match":"partial","distinction":"Komşu, saç tutamı ve bitim sınırının adlandırılmasına odaklanır; odak dal ise ön saçın başlangıç yerini, oradan tutmayı ve bu eylemin uzantılarını bir araya getirir.","focus_only":"Bu dal ön saçın başlangıç yerinden tutma, çekme ve denetim uzantılarını kapsar.","gloss":"ön saç tutamı ve saç bitim sınırı","neighbor_only":"Komşu dal ön saç tutamını ve saç bitiminin ön ya da arka sınırını adlandırır.","neighbor_ref":"root_001232/B006","relation_type":"near_neighbor","shared_zone":"İki dal da başın önündeki saç ve saçın bittiği sınırla ilgilidir."},{"boundary_match":"field_only","distinction":"Ortak alan saçtır, fakat çekirdekler ayrıdır: burada beden bölgesi ve kavrama eylemi; komşuda bakım, uzama ve belirli bir hazırlama uygulaması vardır.","focus_only":"Bu dal ön saç bölgesini ve onu kavrayıp çekmeyi anlatır.","gloss":"saçı tarama ve uzatma","neighbor_only":"Komşu dal saçı tarama, saçın uzaması ve ön saçı uzatıp çekme uygulamalarını anlatır.","neighbor_ref":"root_001512/B002","relation_type":"same_field","shared_zone":"Her iki dalın katılımcısı başın önündeki saç olabilir."},{"boundary_match":"field_only","distinction":"Odak dal saç çizgisiyle ve saçtan tutmayla sınırlıdır; komşu ise saçtan bağımsız alın yüzeyi ve kemiğidir.","focus_only":"Bu dal saçın alındaki başlangıç yerini ve buradan tutmayı merkez alır.","gloss":"alın ve alın kemiği","neighbor_only":"Komşu dal kaşlarla ön saç bölgesi arasındaki alın yüzeyini ve alın kemiğini merkez alır.","neighbor_ref":"root_000219/B001","relation_type":"same_field","shared_zone":"İki dal başın ön bölümünde birbirine bitişik bölgeleri gösterir."}],"source_phrase_ar":"الناصية قصاص الشعر (maqayis;ayn;sihah;mufradat)؛ الناصية منبت الشعر في مقدم الرأس (tahdhib)؛ نصوته قبضت على ناصيته ومددتها (maqayis;ayn;sihah;tahdhib;mufradat)؛ ناصيته أخذ كل واحد بناصية صاحبه (maqayis;ayn;tahdhib;mufradat)؛ آخذ بناصيتها أي متمكن منها (mufradat)","source_summary":"Kaynakların ortak anlatımı, ön saçın başladığı yeri bu bölgeden tutma ve çekme eylemleriyle ilişkilendirir; denetim anlamı da aynı tutma görüntüsüne dayanan söz öbeğinde belirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه قصاص الشعر ومنبته في مقدم الرأس والقبض على الناصية ومدها والجذب بها والمناصاة والتمكن المجازي بالأخذ بالناصية","what_is_not_ar":"ليس هو تسريح الشعر ولا طول الشعر ولا نبات النَّصِي ولا اختيار الصفوة"},"support_links":["sup_ed56121597e410ee2d7b"]},{"boundary":"Bu dal saçın kendisini veya saç çizgisini adlandırmaz; bakım, uzama ve belirli bir hazırlama eylemiyle sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001512/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَاصِيَة","morph_features":"STEM|POS:N|LEM:naASiyap|ROOT:nSy|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:16:1:1","qac_word_ref":"96:16:1","surface_ar":"نَاصِيَةٍ"}],"gloss":"saçı tarama, saçın uzaması ve ölünün ön saçını çekip uzatma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Saçı taramak ve düzenli bir görünüşe getirmek, dalın bakım eylemi çekirdeğidir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Saçın uzun hale gelmesi, bakım eyleminden ayrı bir durum değişikliği anlamıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ölünün başı hazırlanırken ön saçını uzatıp çekmek, belirli katılımcı ve bağlama bağlı özel kullanımdır."}}],"root_ar":"ن ص ي","root_id":"root_001512","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın birbirinden ayrılması gereken bakım, durum değişikliği ve özel hazırlama kullanımlarını topluca gösteren açıklayıcı karşılıktır.","boundary_detail":"Bu dal saçın kendisini veya saç çizgisini adlandırmaz; bakım, uzama ve belirli bir hazırlama eylemiyle sınırlıdır.","branch_image_ar":"تسريح الشعر وطوله","concept_gloss":"saçı tarama, saçın uzaması ve ölünün ön saçını çekip uzatma","contextual_glosses":[{"applicability":"Bir kişinin saçına bakım yapıp onu taradığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Saç bakımındaki tarama ve düzenleme eylemlerini korur."},"facet_ids":["F001"],"text":"saçını tarayıp düzene sokmak","usage_role":"general"},{"applicability":"Saçın zaman içinde daha uzun hale geldiği durum değişikliği bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Saçın uzunluğundaki artışı doğrudan korur."},"facet_ids":["F002"],"text":"saçı uzamak","usage_role":"contextual"},{"applicability":"Yalnızca ölünün başı hazırlanırken ön saçının çekilip uzatıldığı özel bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Özel katılımcıyı, ön saç bölgesini ve uzatıp çekme eylemini korur."},"facet_ids":["F003"],"text":"ölünün ön saçını çekip uzatmak","usage_role":"explanatory"}],"definition":"Saçı tarayıp düzene sokmayı ve saçın uzamasını anlatır; ayrıca ölünün başı hazırlanırken ön saçının uzatılıp çekilmesini bildiren özel bir kullanım taşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Saçı taramak ve düzenli bir görünüşe getirmek, dalın bakım eylemi çekirdeğidir."},{"facet_id":"F002","role":"core","statement":"Saçın uzun hale gelmesi, bakım eyleminden ayrı bir durum değişikliği anlamıdır."},{"facet_id":"F003","role":"specialization","statement":"Ölünün başı hazırlanırken ön saçını uzatıp çekmek, belirli katılımcı ve bağlama bağlı özel kullanımdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Saçın kendiliğinden uzamasını ve ölünün ön saçına özgü uygulamayı karşılamaz.","preserves":"Tarama ve düzenleme eylemlerini genel olarak korur."},"text":"saç bakımı"}],"identity_rationale":"Kaynak ifadesi, saçı tarayıp düzene sokma, saçın uzaması ve ölünün ön saçını hazırlama sırasında uzatıp çekme kullanımlarını açıkça aynı dalda verir.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"saçın uzaması"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"ölünün başı hazırlanırken ön saçını çekip uzatmak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kadının saçını tarayıp düzene sokması"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"saçını tarayıp düzene sokmak"}],"lexicalization_note":"Tanım, saçın uzamasını bildiren kullanımı; tarama ve ölünün ön saçını uzatıp çekme bildiren kişi ve bağlam bağımlı kullanımlardan ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen dört karşılaştırma tarama, saç uzunluğu, saç tutamları ve ön saç bölgesi bakımından en yakın sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Tarama bağlamında birbirine yaklaşırlar; ancak odak dalın uzunluk ve özel hazırlama kullanımları, komşunun ise belirli saç yapısı anlamı ayrıca vardır.","focus_only":"Bu dal saçın uzamasını ve ölünün ön saçına özgü hazırlama eylemini de kapsar.","gloss":"saçı tarama ve orta yapılı saç","neighbor_only":"Komşu dal saçın ne çok kıvırcık ne de dümdüz olan yapısını da adlandırır.","neighbor_ref":"root_000546/B010","relation_type":"near_synonym","shared_zone":"İki dal da saçı tarayıp düzenleme eylemini kapsar."},{"boundary_match":"partial","distinction":"Odak dal genel uzama değişikliğine izin verir; komşu ise saçın bolluğunu ve ulaştığı belirli uzunluk sınırını adlandırır.","focus_only":"Bu dal uzama sürecini, taramayı ve özel bir ön saç uygulamasını bildirir.","gloss":"gür ve kulaklara kadar uzanan saç","neighbor_only":"Komşu dal saçın bolluğunu ve kulak çevresine erişen belirli uzunluk düzeyini bildirir.","neighbor_ref":"root_001666/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da saç uzunluğuyla ilgili bir durumu anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal eylem ve durum değişikliğidir; komşu ise belirli saç parçaları ile bu işi yapan kişiyi de adlandıran ayrı bir kavram kümesidir.","focus_only":"Bu dal tarama eyleminin yanı sıra uzama ve ölünün ön saçını çekme kullanımlarını içerir.","gloss":"saç tutamları ve saçı düzenleyen kişi","neighbor_only":"Komşu dal saç tutamlarını, yanağa veya başa yayılan saçları ve saçı düzenleyen kişiyi adlandırır.","neighbor_ref":"root_001420/B012","relation_type":"near_neighbor","shared_zone":"Her iki dal saçın düzenlenmesi ve şekillendirilmesi alanına girer."},{"boundary_match":"field_only","distinction":"Bu dalda bakım ve uzama belirleyicidir; komşu dalda ise beden bölgesinin adı ve o bölgeden kavrama eylemi belirleyicidir.","focus_only":"Bu dal saç bakımı, saçın uzaması ve özel hazırlama eylemini anlatır.","gloss":"alın saç çizgisi ve oradan tutma","neighbor_only":"Komşu dal ön saçın başladığı yeri ve oradan tutup çekmeyi anlatır.","neighbor_ref":"root_001512/B001","relation_type":"same_field","shared_zone":"Her iki dal başın önündeki saçla ilgili kullanımlar barındırır."}],"source_phrase_ar":"تنصت المرأة إذا رجلت شعرها (sihah;tahdhib)؛ أن تنصى أي تسرح شعرها (tahdhib)؛ انتصى الشعر طال (maqayis;sihah;mufradat)؛ تنصون ميتكم أي تمدون ناصيته (maqayis;sihah;tahdhib;mufradat)","source_summary":"Kaynaklar saçın taranıp düzenlenmesini, uzun hale gelmesini ve ölünün ön saçının hazırlık sırasında uzatılıp çekilmesini ayrı kullanımlar olarak birlikte aktarır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه تنصية الشعر وتسريحه وترجيله ومد ناصية الميت وطول الشعر","what_is_not_ar":"ليس هو أصل الناصية نفسها ولا الأخذ بها للغلبة ولا صفوة القوم"},"support_links":[]},{"boundary":"Geride kalan bölüm kendiliğinden seçkin sayılmamalı; önden gidenler ve üst kesimden evlenme de çekirdeğin bağımlı uzantıları olarak ayrı tutulmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001512/B003","candidate_links":[{"candidate_id":"cand_6927a041038dedb94467","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَاصِيَة","morph_features":"STEM|POS:N|LEM:naASiyap|ROOT:nSy|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:16:1:1","qac_word_ref":"96:16:1","surface_ar":"نَاصِيَةٍ"}],"gloss":"seçkin kesim, en iyiyi seçme ve önde gelme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun ya da herhangi bir şeyin en iyi ve seçkin kesimi, dalın temel adlandırmasıdır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şey içinden en iyi olanı seçip almak, adlandırmayla bağlantılı eylem çekirdeğidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Topluluğun önde gelenleri ile bir topluluğun önderi veya en seçkin kişisi, üstünlük ölçütünün kişi alanındaki uzantısıdır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kimi kullanımda söz, seçilmişlik yüklemeden yalnızca geride kalan bölümü bildirir."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Önden giden kişiler, en önde bulunma düşüncesine dayanan ayrı bir kullanımdır."}},{"facet_id":"F006","role":"associated_use","source_fields":["distinctive_facets[F006]"],"statements":{"statement":"Bir topluluğun en yüksek konumdaki kesiminden evlenmek, seçkinlik çekirdeğine bağlı özel bir toplumsal kullanımdır."}}],"root_ar":"ن ص ي","root_id":"root_001512","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın en güçlü ortak çekirdeği olan seçkin kesim, seçme eylemi ve önderlik kullanımlarını birlikte temsil eder.","boundary_detail":"Geride kalan bölüm kendiliğinden seçkin sayılmamalı; önden gidenler ve üst kesimden evlenme de çekirdeğin bağımlı uzantıları olarak ayrı tutulmalıdır.","branch_image_ar":"النَّصِيَّة والصفوة","concept_gloss":"seçkin kesim, en iyiyi seçme ve önde gelme","contextual_glosses":[{"applicability":"Bir topluluk veya şey içindeki üstün sayılan bölümün adlandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Üstünlük ölçütünü ve topluluk içinden ayrılan kesimi korur."},"facet_ids":["F001"],"text":"en iyi ve seçkin kesim","usage_role":"general"},{"applicability":"Bir şey içinden üstün sayılan parçanın seçildiği eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Seçme işlemini ve seçilenin en iyi sayılmasını korur."},"facet_ids":["F002"],"text":"en iyisini seçip almak","usage_role":"contextual"},{"applicability":"Seçilmişlik ya da üstünlük yüklenmeden yalnızca kalan kısmın anlatıldığı sınırlı kullanımda geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kalan bölüm anlamını seçkinlik eklemeden korur."},"facet_ids":["F004"],"text":"geride kalan bölüm","usage_role":"contextual"},{"applicability":"Bir topluluk içinde diğerlerinden önce ilerleyen kişilerin adlandırıldığı kullanımda geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Katılımcıların başkalarından önce gitmesini korur."},"facet_ids":["F005"],"text":"önden gidenler","usage_role":"contextual"}],"definition":"Bir topluluğun ya da şeyin en iyi ve önde gelen kesimini, bu kesimi seçmeyi ve bir kişinin topluluğunun önderi sayılmasını anlatır. Kimi kullanımlarda yalnızca geride kalan bölüm, önden gidenler veya üst konumdaki bir kesimden evlenme anlamı taşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun ya da herhangi bir şeyin en iyi ve seçkin kesimi, dalın temel adlandırmasıdır."},{"facet_id":"F002","role":"core","statement":"Bir şey içinden en iyi olanı seçip almak, adlandırmayla bağlantılı eylem çekirdeğidir."},{"facet_id":"F003","role":"extension","statement":"Topluluğun önde gelenleri ile bir topluluğun önderi veya en seçkin kişisi, üstünlük ölçütünün kişi alanındaki uzantısıdır."},{"facet_id":"F004","role":"source_variant","statement":"Kimi kullanımda söz, seçilmişlik yüklemeden yalnızca geride kalan bölümü bildirir."},{"facet_id":"F005","role":"source_variant","statement":"Önden giden kişiler, en önde bulunma düşüncesine dayanan ayrı bir kullanımdır."},{"facet_id":"F006","role":"associated_use","statement":"Bir topluluğun en yüksek konumdaki kesiminden evlenmek, seçkinlik çekirdeğine bağlı özel bir toplumsal kullanımdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Seçme eylemini, şeylerin en iyi bölümünü, geride kalan bölümü ve önden gidenleri karşılamaz.","preserves":"Topluluğun üstün sayılan kişilerini doğal biçimde karşılar."},"text":"seçkinler"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Seçkin kesimi, seçme eylemini ve kaynak değişkelerini kaybeder.","preserves":"Bir topluluğun başında bulunan kişi kullanımını korur."},"text":"önder"}],"identity_rationale":"Kaynak ifadesinin ağırlık merkezi bir topluluğun ya da şeyin en iyi ve önde gelen kesimi ile onu seçme eylemidir; ancak aynı ifade yalnızca geride kalan bölümü, önden gidenleri ve üst konumdaki bir kesimden evlenmeyi de ayrıca verir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir topluluğun ya da şeyin en iyi kesimi; kimi bağlamda geride kalan bölüm"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şeyin en iyisini seçip almak"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"insanların önde gelenleri ve seçkinleri"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"bir topluluğun en yüksek konumdaki kesiminden evlenmek"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"topluluğunun önderi ve en seçkin kişisi"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"önden gidenler"}],"lexicalization_note":"Tanım, seçkin kesimi ve seçme eylemini; geride kalan bölüm, önden gidenler, önderlik ve üst kesimden evlenme bildiren sınırlı kullanımlardan ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçme, en iyi bölümü alma, önderlik ve danışan ileri gelenler eksenindeki dört karşılaştırma dalın çekirdeğini ve yan kullanımlarını en iyi sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Seçme çekirdeği yakındır; odak dal seçkin kesimin adı ile birkaç ayrı kaynak değişkesini de içerirken komşu dal yeğleme ve ayrıcalık verme yönünü kapsar.","focus_only":"Bu dal geride kalan bölüm, önden gidenler, önderlik ve üst kesimden evlenme kullanımlarını da taşır.","gloss":"en iyiyi seçme ve ayrı tutma","neighbor_only":"Komşu dal birini ya da bir şeyi özellikle yeğleyip ona ayrıcalık tanıma eylemini de içerir.","neighbor_ref":"root_000873/B002","relation_type":"near_synonym","shared_zone":"İki dal da en iyi sayılan kişi veya şeyi seçme ve seçilmiş kesimi gösterme alanında örtüşür."},{"boundary_match":"partial","distinction":"Eylem çekirdeğinde yakınlık vardır; fakat odak dal kişi topluluğu ve konum bildiren kullanımlara genişler, komşu dal ise seçilip alınan en iyi bölüm üzerinde yoğunlaşır.","focus_only":"Bu dal seçkin topluluğu, önderliği, kalan bölümü ve önden gidenleri de adlandırır.","gloss":"bir şeyin en iyi bölümünü almak","neighbor_only":"Komşu dal bir şeyin en duru veya en iyi bölümünü alma eylemine daha sıkı bağlıdır.","neighbor_ref":"root_000620/B007","relation_type":"near_synonym","shared_zone":"Her iki dal bir şey içinden en iyi sayılan bölümü seçip alma eylemini anlatır."},{"boundary_match":"partial","distinction":"Odak dalda önderlik seçkinlik alanının bir uzantısıdır; komşuda ise başta bulunma ve yönetme kavramın doğrudan çekirdeğidir.","focus_only":"Bu dal en iyi kesimi ve onu seçme eylemini önderlikten bağımsız olarak da anlatır.","gloss":"önderlik ve başta bulunma","neighbor_only":"Komşu dal başta bulunmayı, yönetmeyi ve önde ilerlemeyi doğrudan merkez alır.","neighbor_ref":"root_000529/B002","relation_type":"near_neighbor","shared_zone":"İki dal bir kişinin topluluk içinde önde ve üstün konumda bulunmasını anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal üstünlük ve seçilmişlik niteliğine dayanır; komşu dalda ise önde gelenlerin ortak görüşme için bir araya gelmesi belirleyici koşuldur.","focus_only":"Bu dal seçkin kişi veya bölümü danışma ya da toplanma koşulu olmadan gösterebilir.","gloss":"danışmak için toplanan önde gelenler","neighbor_only":"Komşu dal önde gelenlerin bir görüş, danışma ve konuşma çevresinde toplanmasını içerir.","neighbor_ref":"root_001441/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal bir topluluğun önde gelen ve saygın kişilerini gösterebilir."}],"source_phrase_ar":"النصية من القوم ومن كل شيء الخيار (maqayis;sihah)؛ انتصيت الشيء اخترته (maqayis;sihah)؛ نخبة الناس وخيارهم هم نصية انتصوا (ayn)؛ نواصي الناس أشرافهم والنصية الخيار الأشراف (sihah;tahdhib)؛ النصية البقية (sihah;tahdhib)؛ الأنصاء السابقون (tahdhib)؛ فلان ناصية قومه وفلان نصية قوم أي خيارهم (mufradat)؛ تنصيتهم إذا تزوجت في الذروة منهم والناصية (sihah)","source_summary":"Kaynakların birleşik anlatımı seçkin kesim, en iyiyi seçme ve önderlik çevresinde yoğunlaşır; bunun yanında geride kalan bölüm, önden gidenler ve yüksek konumdaki kesimden evlenme kullanımlarını da korur.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الخيار من القوم أو الأشياء والأشراف والسابقون والبقية المختارة وتنصي القوم بمعنى أخذ الذروة منهم","what_is_not_ar":"ليس هو الناصية الحسية ولا نبات النَّصِي إلا من جهة التشبيه"},"support_links":["sup_65aa5d5b161877ad020f"]},{"boundary":"Dal genel olarak her türlü ot ya da otlağı değil, belirli bitkiyi ve o bitkinin bolluğunu bildiren kullanımı kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001512/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَاصِيَة","morph_features":"STEM|POS:N|LEM:naASiyap|ROOT:nSy|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:16:1:1","qac_word_ref":"96:16:1","surface_ar":"نَاصِيَةٍ"}],"gloss":"tazeyken değerli bir otlak bitkisi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir bitkinin taze haldeyken değerli bir otlak yemi olması, dalın temel bitki anlamıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bitki beyazlaştığında, irileştiğinde veya kuruduğunda gelişim evresine göre başka adlarla anılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir arazide bu belirli bitkinin bolca yetişmesi, bitki adından kurulan ayrı eylem anlamıdır."}}],"root_ar":"ن ص ي","root_id":"root_001512","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli bitkinin taze evredeki temel adlandırmasını ve otlak değerini veren en kısa doğal karşılıktır.","boundary_detail":"Dal genel olarak her türlü ot ya da otlağı değil, belirli bitkiyi ve o bitkinin bolluğunu bildiren kullanımı kapsar.","branch_image_ar":"نبات النَّصِي","concept_gloss":"tazeyken değerli bir otlak bitkisi","contextual_glosses":[{"applicability":"Bitkinin henüz taze olduğu evrede adlandırıldığı genel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bitki türünü genel bir açıklamayla ve taze evre sınırıyla karşılar."},"facet_ids":["F001"],"text":"taze otlak bitkisi","usage_role":"general"},{"applicability":"Bitkinin taze dönemden kuruma ve irileşme dönemine geçişinin açıklandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aynı bitkinin gelişim evresine bağlı ad değişikliğini korur."},"facet_ids":["F001","F002"],"text":"kuruyunca başka ad alan otlak bitkisi","usage_role":"explanatory"},{"applicability":"Bir arazi üzerinde söz konusu belirli bitkinin çok bulunduğunu anlatan eylem bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Arazi katılımcısını ve belirli bitkinin bolluğunu korur."},"facet_ids":["F003"],"text":"o bitkinin arazide bolca yetişmesi","usage_role":"contextual"}],"definition":"Tazeyken değerli bir otlak bitkisi sayılan belirli bir bitkiyi anlatır; beyazlaşıp irileşmesi veya kurumasıyla başka adlara geçer. Ayrı bir eylem kullanımı, bu bitkinin bir arazide çokça yetiştiğini bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir bitkinin taze haldeyken değerli bir otlak yemi olması, dalın temel bitki anlamıdır."},{"facet_id":"F002","role":"specialization","statement":"Bitki beyazlaştığında, irileştiğinde veya kuruduğunda gelişim evresine göre başka adlarla anılır."},{"facet_id":"F003","role":"associated_use","statement":"Bir arazide bu belirli bitkinin bolca yetişmesi, bitki adından kurulan ayrı eylem anlamıdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Her türlü otsu bitkiyi kapsayarak belirli bitki ve gelişim evresi sınırını aşar.","collision":"Genel bitki sınıfıyla özel bitki anlamı birbirine karışır.","fit":"broadening","loses":null,"preserves":"Bunun bir bitki olduğunu genel düzeyde korur."},"text":"ot"}],"identity_rationale":"Kaynak ifadesi belirli bir otlak bitkisini, tazeyken değerli yem oluşunu, beyazlaşma ve kuruma evrelerinde başka adlarla anılmasını ve bu bitkinin bir yerde çok yetişmesini birlikte açıkça bildirir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"tazeyken değerli bir otlak bitkisi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"o bitkinin bir arazide çokça yetişmesi"}],"lexicalization_note":"Tanım, bitkinin kendi adını bildiren kullanımı; o bitkinin bir arazide çokça yetişmesini bildiren eylem kullanımından ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan karşılaştırmalar belirli otlak bitkisi, genel taze yem, genel arazi otu ve kurumuş bitki sınırlarını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"İşlev ve bolluk yapısı benzese de adlandırılan bitkiler ayrıdır; odak dal ayrıca kendi bitkisinin gelişim evresine bağlı ad değişimini içerir.","focus_only":"Bu dal farklı bir belirli otlak bitkisini ve onun kuruma evresindeki ad değişimini kapsar.","gloss":"koyunların sevdiği yeşil otlak bitkisi","neighbor_only":"Komşu dal koyunların sevdiği başka bir bitkiyi ve o bitkinin arazi üzerindeki bolluğunu anlatır.","neighbor_ref":"root_000160/B007","relation_type":"near_neighbor","shared_zone":"İki dal da tazeyken otlanan belirli bir bitkiyi ve onun arazide bol oluşunu anlatır."},{"boundary_match":"partial","distinction":"Odak dal tek bir bitki adıdır; komşu ise tür kimliğinden bağımsız olarak taze ve yeşil yem niteliğini merkez alır.","focus_only":"Bu dal belirli bir bitkiyi ve onun evreye bağlı ad değişimini anlatır.","gloss":"taze ve yeşil yem bitkileri","neighbor_only":"Komşu dal çeşitli ot ve bitkilerin taze, yeşil yem olma niteliğini genel bir sınıf olarak anlatır.","neighbor_ref":"root_000571/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal taze halde otlanan yeşil bitkileri kapsayan bağlamlarda buluşur."},{"boundary_match":"field_only","distinction":"Odak dal tür ve evre bakımından sınırlıdır; komşu dal ise arazi örtüsü olarak otları genel biçimde kapsar.","focus_only":"Bu dal belirli bitkiyi, taze evresini ve kuruyunca ad değiştirmesini kapsar.","gloss":"arazideki ot ve yem bitkileri","neighbor_only":"Komşu dal arazi üzerindeki ot ve yem bitkilerini tür ayırmadan genel olarak adlandırır.","neighbor_ref":"root_001317/B004","relation_type":"same_field","shared_zone":"İki dal da arazide yetişen ve otlatmada kullanılan bitkiler alanındadır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği taze haldeki belirli bitkidir ve kuruma bir evre değişimidir; komşu dalda kurumuş ve bırakılmış bitki doğrudan çekirdektir.","focus_only":"Bu dal taze halde değerli olan belirli bitkiyi ve sonraki evrelerini izler.","gloss":"kurumuş ve bırakılmış bitki","neighbor_only":"Komşu dal kuruyup hayvanlarca kırılmış ya da çoban tarafından bırakılmış bitki kalıntısını anlatır.","neighbor_ref":"root_001578/B010","relation_type":"near_neighbor","shared_zone":"İki dal otlak bitkilerinin kuruma evresiyle ilişkilidir."}],"source_phrase_ar":"النصي نبات من أفضل المراعي (ayn;mufradat)؛ النصى نبت ما دام رطبا فإذا ابيض فهو الطريفة وإذا ضخم ويبس فهو الحلي (sihah)؛ النصي نبت معروف ما دام رطبا فإذا يبس فهو حلي (tahdhib)؛ أنصت الأرض أي كثر نصيها (sihah)","source_summary":"Kaynaklar belirli bitkiyi taze dönemde değerli bir otlak yemi olarak tanıtır; gelişim ve kuruma evrelerinde adının değiştiğini, ayrıca bir arazinin bu bitki bakımından bol olabildiğini belirtir.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه النَّصِي نباتا رطبا أو مرعى فاضلا وما يقال في الأرض إذا كثر فيها","what_is_not_ar":"ليس هو نصية القوم إلا إذا صرح المصدر بالتشبيه"},"support_links":[]},{"boundary":"Anlam genel arazi veya çöl adı değildir; iki açık arazi parçası arasındaki bitişiklik ilişkisine bağlıdır.","branch_kind":"non_bare","branch_ref":"root_001512/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَاصِيَة","morph_features":"STEM|POS:N|LEM:naASiyap|ROOT:nSy|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:16:1:1","qac_word_ref":"96:16:1","surface_ar":"نَاصِيَةٍ"}],"gloss":"bir çöl düzlüğünün başka bir çöl düzlüğüne bitişmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki çöl düzlüğünün veya ıssız açık arazi parçasının birbirine doğrudan bağlanması, yapının çekirdeğidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bağlantının bir arazinin diğerinin ön kısmını kavraması gibi tasarlanması, uzamsal ilişkiyi açıklayan görüntüdür."}}],"root_ar":"ن ص ي","root_id":"root_001512","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca iki açık ve ıssız arazi parçasının birbirine bağlandığını bildiren sınırlı yapı için geçerlidir.","boundary_detail":"Anlam genel arazi veya çöl adı değildir; iki açık arazi parçası arasındaki bitişiklik ilişkisine bağlıdır.","branch_image_ar":"مفازة تناصي مفازة","concept_gloss":"bir çöl düzlüğünün başka bir çöl düzlüğüne bitişmesi","contextual_glosses":[{"applicability":"Birbirini izleyen iki ıssız açık arazi parçasının doğrudan bağlandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki arazi katılımcısını ve aralarındaki bağlantıyı korur."},"facet_ids":["F001"],"text":"bir ıssız açık arazinin ötekine bağlanması","usage_role":"general"},{"applicability":"Uzamsal bağlantının kavrama benzetmesiyle açıklandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bitişiklik ilişkisini ve onu görünür kılan kavrama benzetmesini korur."},"facet_ids":["F001","F002"],"text":"öteki arazinin ön kısmını kavrar gibi bitişmek","usage_role":"explanatory"}],"definition":"Bir çöl düzlüğü ya da ıssız açık arazinin başka birine doğrudan bitişmesini anlatır; bağlantı, bir arazinin ötekinin ön kısmını kavramasına benzetilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki çöl düzlüğünün veya ıssız açık arazi parçasının birbirine doğrudan bağlanması, yapının çekirdeğidir."},{"facet_id":"F002","role":"extension","statement":"Bağlantının bir arazinin diğerinin ön kısmını kavraması gibi tasarlanması, uzamsal ilişkiyi açıklayan görüntüdür."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Başka bir araziye bitişme koşulu bulunmayan bütün çölleri kapsar.","collision":"Genel arazi adıyla iki arazi arasındaki özel bağlantı karışır.","fit":"broadening","loses":null,"preserves":"İlişkinin katılımcısı olan arazi türünü korur."},"text":"çöl"}],"identity_rationale":"Kaynak ifadesi, bir çöl düzlüğü ya da ıssız açık arazinin başka birine bitişmesini ortak çekirdek olarak verir ve bu bağlantıyı birinin ötekinin ön kısmını kavramasına benzetir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bir çöl düzlüğünün başka bir çöl düzlüğüne, onun önünü kavrar gibi bitişmesi"}],"lexicalization_note":"Tanım yalnızca iki çöl düzlüğü ya da ıssız açık arazi arasında bağlantı kuran sınırlı ifadeye uygulanır; yalın bir kök anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen üç karşılaştırma tek arazinin uzanması, genel ıssız arazi ve gerçek kavrama eylemiyle karışma sınırlarını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ilişkisel olup iki arazi katılımcısı ister; komşu dal tek arazinin uzunlamasına yayılmasını kendi niteliği olarak verir.","focus_only":"Bu dal iki ayrı çöl düzlüğü arasındaki bitişiklik ilişkisini gerektirir.","gloss":"uzayıp giden çöl düzlüğü","neighbor_only":"Komşu dal tek bir çöl düzlüğünün kendi içinde uzanmasını bildirir.","neighbor_ref":"root_001447/B004","relation_type":"near_neighbor","shared_zone":"İki dal da çöl düzlüğünün uzamsal düzenini anlatır."},{"boundary_match":"field_only","distinction":"Odak dal arazilerin birbirine bitişmesiyle sınırlıdır; komşu dal ise tek arazinin genişlik, susuzluk ve ıssızlık özelliklerini merkez alır.","focus_only":"Bu dal iki ıssız arazi arasındaki bağlantıyı anlatır.","gloss":"geniş, susuz ve ıssız arazi","neighbor_only":"Komşu dal susuz, insansız, uzak ve geniş bir ıssız arazinin kendisini anlatır.","neighbor_ref":"root_000664/B008","relation_type":"same_field","shared_zone":"Her iki dal çöl veya ıssız açık arazi alanına girer."},{"boundary_match":"thematic_only","distinction":"Ortaklık yalnızca görüntüdedir: burada sonuç iki arazinin bitişmesidir; komşuda ise bir insanın saç bölgesine yönelik gerçek bedensel eylem vardır.","focus_only":"Bu dal gerçek bir uzamsal bağlantıyı, yalnızca kavrama görüntüsüyle betimler.","gloss":"ön saçtan gerçekten tutup çekme","neighbor_only":"Komşu dal bir kişinin ön saç bölgesini gerçekten tutma ve çekme eylemini anlatır.","neighbor_ref":"root_001512/B001","relation_type":"thematic","shared_zone":"İki dalda da bir şeyin ön kısmını kavrama görüntüsü bulunur."}],"source_phrase_ar":"مفازة تناصي أخرى كأنها تتصل بها كالقابضة على ناصيتها (maqayis)؛ مفازة تناصي مفازة إذا كانت الأولى متصلة بالأخرى (ayn)؛ فلاة تناصي فلاة أي تتصل بها (sihah;tahdhib)؛ تناصي أرض كذا وتواصيها أي تتصل بها (tahdhib)","source_summary":"Kaynakların ortak anlatımı, iki çöl düzlüğü veya ıssız açık arazi parçası arasındaki doğrudan bağlantıyı bildirir; kavrama görüntüsü bu uzamsal bitişikliği açıklayan benzetmedir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الفلاة أو المفازة التي تتصل بأخرى كأن إحداهما تمسك بناصية الأخرى","what_is_not_ar":"ليس هو الأخذ الحقيقي بالناصية ولا نبات الأرض"},"support_links":[]},{"boundary":"Dal genel karın bölgesini veya her karın ağrısını değil, batıcı ve kişiyi yerinde durmaktan alıkoyan sancıyı anlatır.","branch_kind":"bare","branch_ref":"root_001512/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَاصِيَة","morph_features":"STEM|POS:N|LEM:naASiyap|ROOT:nSy|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:16:1:1","qac_word_ref":"96:16:1","surface_ar":"نَاصِيَةٍ"}],"gloss":"karında batıcı, huzursuz eden sancı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Karında hissedilen batma ve sancı, dalın bedensel duyum çekirdeğidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ağrının kişiyi yerinde rahat duramaz hale getirmesi, bedensel duyumun davranışsal sonucudur."}}],"root_ar":"ن ص ي","root_id":"root_001512","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Karındaki batma duyumunu ve bu duyumun kişiyi rahat duramaz hale getiren etkisini birlikte karşılayan doğal üst ifadedir.","boundary_detail":"Dal genel karın bölgesini veya her karın ağrısını değil, batıcı ve kişiyi yerinde durmaktan alıkoyan sancıyı anlatır.","branch_image_ar":"نَصْو البطن المزعج","concept_gloss":"karında batıcı, huzursuz eden sancı","contextual_glosses":[{"applicability":"Karında iğne batması gibi hissedilen ağrının doğrudan adlandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bedensel konumu ve ağrının batıcı niteliğini korur."},"facet_ids":["F001"],"text":"karında batıcı sancı","usage_role":"general"},{"applicability":"Ağrının kişiyi hareket etmeye zorlayan huzursuz edici etkisinin öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karın sancısını ve kişinin rahat duramaması sonucunu korur."},"facet_ids":["F001","F002"],"text":"yerinde durdurmayan karın sancısı","usage_role":"explanatory"}],"definition":"Karında duyulan batıcı bir ağrı veya sancıdır; şiddeti kişiyi yerinde rahat duramaz hale getirebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Karında hissedilen batma ve sancı, dalın bedensel duyum çekirdeğidir."},{"facet_id":"F002","role":"extension","statement":"Ağrının kişiyi yerinde rahat duramaz hale getirmesi, bedensel duyumun davranışsal sonucudur."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Batıcı olmayan ve kişiyi yerinde durmaktan alıkoymayan bütün karın ağrılarını kapsar.","collision":"Özel sancı türü genel karın ağrısı sınıfıyla karışır.","fit":"broadening","loses":null,"preserves":"Ağrının karın bölgesinde bulunmasını korur."},"text":"karın ağrısı"},{"category":"confusable","error_profile":{"adds":"Bedensel ağrı bulunmayan ruhsal veya genel tedirginlik durumlarını kapsar.","collision":"Bedensel sancının sonucu bağımsız bir ruhsal durumla karışır.","fit":"displacement","loses":"Karındaki bedensel konumu ve batıcı ağrı çekirdeğini kaybeder.","preserves":"Kişinin rahat duramaması sonucunu kısmen korur."},"text":"huzursuzluk"}],"identity_rationale":"Kaynak ifadesi, karında duyulan batma veya sancıyı ve bu ağrının kişiyi yerinde rahat duramaz hale getirmesini aynı anlamın iki yönü olarak açıkça verir.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"karında duyulan, kişiyi rahat duramaz hale getiren batıcı sancı"}],"lexicalization_note":"Tanım yalın dalı karındaki batıcı sancıyla sınırlar; komşu alanlardan organ, genel karın bölgesi veya ruhsal huzursuzluk anlamı almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen dört karşılaştırma organ ağrısı, kaygıyla sıçrama, ağrıdan büzülme ve genel karın bölgesiyle karışma risklerini açıklar.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal belirli bir organ seçmeden sancının niteliğini verir; komşu dal ise ağrıyı belirli bir organ ve onun hastalığıyla sınırlar.","focus_only":"Bu dal karın içinde yeri belirlenmemiş batıcı sancıyı ve huzursuz edici etkisini anlatır.","gloss":"belirli bir iç organ ve onun ağrısı","neighbor_only":"Komşu dal belirli bir iç organı, onun yerini, yaralanmasını ve hastalığını anlatır.","neighbor_ref":"root_001280/B001","relation_type":"same_field","shared_zone":"İki dal karın içindeki bedensel ağrı bağlamlarında yan yana gelebilir."},{"boundary_match":"partial","distinction":"Odak dalın nedeni karındaki bedensel sancıdır; komşuda ise neden kaygı uyandıran bir olaydır ve sonuç yerinden yükselme veya sıçramadır.","focus_only":"Bu dal huzursuzluğu karındaki batıcı ağrıdan doğurur.","gloss":"kaygıyla yerinden sıçrama","neighbor_only":"Komşu dal dışarıdan gelen kaygı verici bir olayın kişiyi yerinden sıçratmasını anlatır.","neighbor_ref":"root_000781/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal kişiyi bulunduğu yerde rahat bırakmayan bir rahatsızlık sonucu içerir."},{"boundary_match":"partial","distinction":"Odak dalda ağrının yeri karındır ve temel duyum batmadır; komşuda temel sonuç dönme ve büzülmedir, karın koşulu yoktur.","focus_only":"Bu dal karında batıcı bir ağrı ve hareket etme huzursuzluğu bildirir.","gloss":"ağrıdan kıvrılıp büzülme","neighbor_only":"Komşu dal ağrı yüzünden bedenin veya bir şeyin dönüp büzülmesini bildirir.","neighbor_ref":"root_000863/B005","relation_type":"near_neighbor","shared_zone":"İki dal ağrının kişinin duruşunu veya hareketini bozması bakımından örtüşür."},{"boundary_match":"field_only","distinction":"Odak dal bir duyum ve ağrı türüdür; komşu dal ise duyumdan bağımsız olarak beden bölgesini veya iç kısmı adlandırır.","focus_only":"Bu dal karın içinde duyulan belirli bir sancı türünü anlatır.","gloss":"karın ve bir şeyin iç bölümü","neighbor_only":"Komşu dal insan veya hayvanın karnını ve daha genel olarak şeylerin iç kısmını adlandırır.","neighbor_ref":"root_000128/B001","relation_type":"same_field","shared_zone":"Karın, odak daldaki ağrının gerçekleştiği beden bölgesidir."}],"source_phrase_ar":"أجد في بطني نصوا ووخزا (tahdhib)؛ النصو مثل المفس سمي نصوا لأنه ينصوك أي يزعجك عن القرار (tahdhib)؛ وجدت في بطني حصوا ونصوا وقبصا بمعنى واحد (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, karındaki batıcı sancıyı kişinin yerinde rahat durmasını engelleyebilen bir ağrı olarak açıklar."}],"source_summary":"Bu dal için kaynaklar arası ortak bir özet yoktur; anlam tek kaynakta bedensel duyum ve onun huzursuz edici sonucu olarak aktarılır.","sources":["TA"],"what_is_ar":"يدخل فيه النَّصْو في البطن بمعنى الوخز أو ما يزعج عن القرار","what_is_not_ar":"ليس هو الناصية ولا النَّصِي النبات ولا النصية بمعنى الخيار"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["96:16:1"],"branch_refs":[],"candidate_id":"cand_e39180c19e5561ee3c7b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001512"],"scope":"focus_ayah","source_local_id":"96:16:1:cross-ayah-apposition","source_type":"word_analysis","support_ids":["sup_04e1399cfaa283dfa817","sup_6e95d88b1ef505ed2f2e"],"title":"genitive apposition reaches back (96:15)","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:1","qac_refs":["96:16:1:1"],"status":"accepted"}},{"anchor_refs":["96:16:1"],"branch_refs":[],"candidate_id":"cand_a68a38535af5eaea5b83","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001512"],"scope":"focus_ayah","source_local_id":"96:16:1:forelock-seizure-field","source_type":"word_analysis","support_ids":["sup_04e1399cfaa283dfa817","sup_8dd6a40df425c9129a43"],"title":"rare forelock field specializes seizure imagery","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:1","qac_refs":["96:16:1:1"],"status":"accepted"}},{"anchor_refs":["96:16:1"],"branch_refs":[],"candidate_id":"cand_7544f12f44696e653272","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001512"],"scope":"focus_ayah","source_local_id":"96:16:1:indefinite-reclassification","source_type":"word_analysis","support_ids":["sup_04e1399cfaa283dfa817","sup_111f44d59fa5fd8d631f"],"title":"definite target becomes classified bearer","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:1","qac_refs":["96:16:1:1"],"status":"accepted"}},{"anchor_refs":["96:16:1"],"branch_refs":[],"candidate_id":"cand_26492ad49b105eedb301","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001512"],"scope":"focus_ayah","source_local_id":"96:16:1:one-forelock-two-adjectives","source_type":"word_analysis","support_ids":["sup_04e1399cfaa283dfa817","sup_d453e9e8985a3954d629"],"title":"agreement binds both qualities to one forelock","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:1","qac_refs":["96:16:1:1"],"status":"accepted"}},{"anchor_refs":["96:16:1"],"branch_refs":[],"candidate_id":"cand_6e24ad919f7eb4b5b041","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001512"],"scope":"focus_ayah","source_local_id":"96:16:1:representative-forelock","source_type":"word_analysis","support_ids":["sup_04e1399cfaa283dfa817","sup_fea365e777e906e82c82"],"title":"front of the head bears the whole person's stance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:1","qac_refs":["96:16:1:1"],"status":"accepted"}},{"anchor_refs":["96:16:1"],"branch_refs":[],"candidate_id":"cand_0ca0542bd00ec788f78f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001512"],"scope":"focus_ayah","source_local_id":"96:16:1:verbless-portrait","source_type":"word_analysis","support_ids":["sup_04e1399cfaa283dfa817","sup_f038b289899223428cba"],"title":"the prior threat freezes into a diagnostic portrait","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:1","qac_refs":["96:16:1:1"],"status":"accepted"}},{"anchor_refs":["96:16:2"],"branch_refs":[],"candidate_id":"cand_b6dc3ca4ffc6e8cd27fc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"96:16:2:case-variant-apparatus","source_type":"word_analysis","support_ids":["sup_14b1feada16be6f1320d","sup_1521e3c54e7dcec1a2e4"],"title":"variant cases show alternatives to received apposition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:2","qac_refs":["96:16:2:1"],"status":"accepted"}},{"anchor_refs":["96:16:2"],"branch_refs":[],"candidate_id":"cand_0fbc97f285577aaf3379","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"96:16:2:denial-becomes-attribute","source_type":"word_analysis","support_ids":["sup_1521e3c54e7dcec1a2e4","sup_f17f5b28998fc869ad5d"],"title":"the earlier denial returns as an attribute","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:2","qac_refs":["96:16:2:1"],"status":"accepted"}},{"anchor_refs":["96:16:2"],"branch_refs":[],"candidate_id":"cand_cbcfedd28bfb1064744c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"96:16:2:falsehood-lexical-content","source_type":"word_analysis","support_ids":["sup_1521e3c54e7dcec1a2e4","sup_2ad42ab9aefdb650f02f"],"title":"falsehood and fabrication are the selected sense","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:2","qac_refs":["96:16:2:1"],"status":"accepted"}},{"anchor_refs":["96:16:2"],"branch_refs":[],"candidate_id":"cand_69c6eedee2137c1213e7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"96:16:2:first-adjective-of-forelock","source_type":"word_analysis","support_ids":["sup_1521e3c54e7dcec1a2e4","sup_d9dfd7f27c80f85da456"],"title":"lying is grammatically attached to the forelock","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:2","qac_refs":["96:16:2:1"],"status":"accepted"}},{"anchor_refs":["96:16:2"],"branch_refs":[],"candidate_id":"cand_a45461f9dae40ed16dbe","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"96:16:2:forward-summons-test","source_type":"word_analysis","support_ids":["sup_1521e3c54e7dcec1a2e4","sup_c6942b6239f71157454c"],"title":"the false claimant moves toward a public test","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:2","qac_refs":["96:16:2:1"],"status":"accepted"}},{"anchor_refs":["96:16:2"],"branch_refs":[],"candidate_id":"cand_5a0df9f69f3a37aa6c57","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"96:16:2:masking-and-failure-pressure","source_type":"word_analysis","support_ids":["sup_1521e3c54e7dcec1a2e4","sup_cc0b3bb920753a3b2994"],"title":"masking and failure color the exposed falsehood","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:2","qac_refs":["96:16:2:1"],"status":"accepted"}},{"anchor_refs":["96:16:2"],"branch_refs":[],"candidate_id":"cand_7465db832b98f3b545d4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"96:16:2:paired-adjective-progression","source_type":"word_analysis","support_ids":["sup_1521e3c54e7dcec1a2e4","sup_446bd60d217ae7fa0556"],"title":"falsehood pairs tightly with sinning","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:2","qac_refs":["96:16:2:1"],"status":"accepted"}},{"anchor_refs":["96:16:3"],"branch_refs":[],"candidate_id":"cand_626016c632ba92115a8c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:16:3:case-variant-apparatus","source_type":"word_analysis","support_ids":["sup_91ff1f87197666590793","sup_e80958174240dc5e72e8"],"title":"variant cases expose the received genitive force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:3","qac_refs":["96:16:3:1"],"status":"accepted"}},{"anchor_refs":["96:16:3"],"branch_refs":[],"candidate_id":"cand_0a04f64bdcc4ccc1b1fb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:16:3:closing-genitive-adjective","source_type":"word_analysis","support_ids":["sup_91ff1f87197666590793","sup_9716279e1c7b2f2c6b6e"],"title":"the final adjective remains inside the apposition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:3","qac_refs":["96:16:3:1"],"status":"accepted"}},{"anchor_refs":["96:16:3"],"branch_refs":[],"candidate_id":"cand_4f3b5fcdd449b57dc9e9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:16:3:cross-surah-and-surah-echoes","source_type":"word_analysis","support_ids":["sup_91ff1f87197666590793","sup_9a17a0a5c0a7c30a1061"],"title":"sinner-label echoes become local diagnosis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:3","qac_refs":["96:16:3:1"],"status":"accepted"}},{"anchor_refs":["96:16:3"],"branch_refs":[],"candidate_id":"cand_cb4c593fa5507492aaf3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:16:3:culpable-active-participle","source_type":"word_analysis","support_ids":["sup_91ff1f87197666590793","sup_93901e7f9e702b836f13"],"title":"active participle points to culpable sin","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:3","qac_refs":["96:16:3:1"],"status":"accepted"}},{"anchor_refs":["96:16:3"],"branch_refs":[],"candidate_id":"cand_c6b950a57476d734c090","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:16:3:falsehood-to-sin-pairing","source_type":"word_analysis","support_ids":["sup_5039f7c7c350a4bf3e44","sup_91ff1f87197666590793"],"title":"falsehood lands directly in sinning","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:3","qac_refs":["96:16:3:1"],"status":"accepted"}},{"anchor_refs":["96:16:3"],"branch_refs":[],"candidate_id":"cand_516b15a48a1c383f8a27","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:16:3:final-closure-and-cadence","source_type":"word_analysis","support_ids":["sup_91ff1f87197666590793","sup_94572f32d6e984a4c042"],"title":"the ayah closes on sounded moral misdirection","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:3","qac_refs":["96:16:3:1"],"status":"accepted"}},{"anchor_refs":["96:16:3"],"branch_refs":[],"candidate_id":"cand_3ebf3e2fa2e40fde9f35","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:16:3:forward-counter-summons","source_type":"word_analysis","support_ids":["sup_91ff1f87197666590793","sup_ca42687aa491fb1bb4f7"],"title":"the diagnosis prepares the counter-summons","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:3","qac_refs":["96:16:3:1"],"status":"accepted"}},{"anchor_refs":["96:16:3"],"branch_refs":[],"candidate_id":"cand_ae3f7db1844312c6acc8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:16:3:hamza-and-qiraat-pressure","source_type":"word_analysis","support_ids":["sup_6f18afcc03e29b1ef02d","sup_91ff1f87197666590793"],"title":"the closing word carries a recitational pressure point","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:3","qac_refs":["96:16:3:1"],"status":"accepted"}},{"anchor_refs":["96:16:3"],"branch_refs":[],"candidate_id":"cand_03f08c9b29bca69609a7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:16:3:missing-the-mark-image","source_type":"word_analysis","support_ids":["sup_91ff1f87197666590793","sup_e3fbc56dad7c74a79a3f"],"title":"sin is pictured as failed direction","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:3","qac_refs":["96:16:3:1"],"status":"accepted"}},{"anchor_refs":["96:16:1"],"branch_refs":[],"candidate_id":"cand_fcd4b0157f047379d241","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001512"],"scope":"focus_ayah","source_local_id":"96:16:1:1","source_type":"qac_morpheme","support_ids":["sup_5a62ada94d5f58ace691"],"title":"QAC root occurrence: ن ص ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["96:16:2"],"branch_refs":[],"candidate_id":"cand_e06bbc3f853505f4fe5f","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"96:16:2:1","source_type":"qac_morpheme","support_ids":["sup_c69db18d61cb88b77356"],"title":"QAC root occurrence: ك ذ ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["96:16:3"],"branch_refs":[],"candidate_id":"cand_d1a46346bcef39be09a7","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000420"],"scope":"focus_ayah","source_local_id":"96:16:3:1","source_type":"qac_morpheme","support_ids":["sup_882008081a807689de16"],"title":"QAC root occurrence: خ ط ء","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["96:16:2"],"branch_refs":[],"candidate_id":"cand_a5fd08d55897a2f295e9","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001290"],"scope":"focus_ayah","source_local_id":"96:16:2:dagger-alif-marker","source_type":"word_analysis","support_ids":["sup_1521e3c54e7dcec1a2e4","sup_db56f9c4008447a5d16d"],"title":"minor spelling marker without separate payoff","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:16:2","qac_refs":["96:16:2:1"],"status":"accepted"}},{"anchor_refs":["96:16"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"96:16","branch_refs":["root_000420/B002","root_001290/B001","root_001512/B001"],"candidate_id":"cand_f4fffa0771c9ea0583d1","commentary_obligation":"review","hft_ref":"hft_601088f1f9b35504feb8","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b1_embodied_control_point","source_type":"hft","support_ids":["sup_ed56121597e410ee2d7b"],"title":"b1_embodied_control_point","trust":"legacy_unbound"},{"anchor_refs":["96:16"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"96:16","branch_refs":["root_000420/B001","root_001290/B004","root_001512/B003"],"candidate_id":"cand_6927a041038dedb94467","commentary_obligation":"review","hft_ref":"hft_75841db858113ecc9cea","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b2_failed_leading_trajectory","source_type":"hft","support_ids":["sup_65aa5d5b161877ad020f"],"title":"b2_failed_leading_trajectory","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"نَاصِيَةٍۢ كَٰذِبَةٍ خَاطِئَةٍۢ","qac_morphemes":[{"lemma_ar":"نَاصِيَة","morph_features":"STEM|POS:N|LEM:naASiyap|ROOT:nSy|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:16:1:1","qac_word_ref":"96:16:1","root_ar":"ن ص ي","surface_ar":"نَاصِيَةٍ"},{"lemma_ar":"كَٰذِب","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:ka`*ib|ROOT:k*b|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"96:16:2:1","qac_word_ref":"96:16:2","root_ar":"ك ذ ب","surface_ar":"كَٰذِبَةٍ"},{"lemma_ar":"خَاطِئَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:xaATi}ap|ROOT:xTA|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"96:16:3:1","qac_word_ref":"96:16:3","root_ar":"خ ط ء","surface_ar":"خَاطِئَةٍ"}],"word_analysis_qac_refs":[["96:16:1:1"],["96:16:2:1"],["96:16:3:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["96:16:1","96:16:2","96:16:3"]},"focus_surface_evidence":{"arabic_uthmani":"نَاصِيَةٍۢ كَٰذِبَةٍ خَاطِئَةٍۢ","qac_morphemes":[{"lemma_ar":"نَاصِيَة","morph_features":"STEM|POS:N|LEM:naASiyap|ROOT:nSy|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:16:1:1","qac_word_ref":"96:16:1","root_ar":"ن ص ي","surface_ar":"نَاصِيَةٍ"},{"lemma_ar":"كَٰذِب","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:ka`*ib|ROOT:k*b|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"96:16:2:1","qac_word_ref":"96:16:2","root_ar":"ك ذ ب","surface_ar":"كَٰذِبَةٍ"},{"lemma_ar":"خَاطِئَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:xaATi}ap|ROOT:xTA|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"96:16:3:1","qac_word_ref":"96:16:3","root_ar":"خ ط ء","surface_ar":"خَاطِئَةٍ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["96:16:1:1"],["96:16:2:1"],["96:16:3:1"]],"word_analysis_refs":["96:16:1","96:16:2","96:16:3"],"word_rows":[{"analysis_record_ref":"96:16:1","analytic_gloss_range_en":"an indefinite genitive appositive forelock, locally the seized front of the person and the representative bearer of the following moral qualities","analytic_root_gloss_range_en":"forelock, frontness, taking by the forelock, and prominence or leadership; locally the concrete forelock is selected while representative frontness remains active as pressure","qac_refs":["96:16:1:1"],"root":{"arabic":"ن ص ي","transliteration":"n-ṣ-y"},"surface":{"arabic":"نَاصِيَةٍۢ","transliteration":"nāṣiyatin"}},{"analysis_record_ref":"96:16:2","analytic_gloss_range_en":"a feminine active participial adjective meaning lying or false, locally attributed to the forelock as the first diagnostic quality","analytic_root_gloss_range_en":"falsehood, lying, denial, fabrication, and some construction-bound failure or deceptive-appearance uses; locally the falsehood/lying participial branch is selected, with failure or masking only as image-pressure","qac_refs":["96:16:2:1"],"root":{"arabic":"ك ذ ب","transliteration":"k-dh-b"},"surface":{"arabic":"كَٰذِبَةٍ","transliteration":"kādhibatin"}},{"analysis_record_ref":"96:16:3","analytic_gloss_range_en":"a feminine active participial adjective of culpable sinning or erring, locally the closing modifier of the forelock after falsehood","analytic_root_gloss_range_en":"sinning, culpable error, and missing the right course or target; locally the active participle leans toward culpable transgression rather than accidental mistake","qac_refs":["96:16:3:1"],"root":{"arabic":"خ ط أ","transliteration":"kh-ṭ-ʾ"},"surface":{"arabic":"خَاطِئَةٍۢ","transliteration":"khāṭiʾatin"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":2,"assigned_records":[{"anchor_refs":["96:16"],"branch_refs":["root_000420/B002","root_001290/B001","root_001512/B001"],"candidate_id":"cand_f4fffa0771c9ea0583d1","evidence_scope":"focus_ayah","hft_ref":"hft_601088f1f9b35504feb8","item_id":"b1_embodied_control_point","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b1_embodied_control_point","support_id":"sup_ed56121597e410ee2d7b"},{"anchor_refs":["96:16"],"branch_refs":["root_000420/B001","root_001290/B004","root_001512/B003"],"candidate_id":"cand_6927a041038dedb94467","evidence_scope":"focus_ayah","hft_ref":"hft_75841db858113ecc9cea","item_id":"b2_failed_leading_trajectory","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b2_failed_leading_trajectory","support_id":"sup_65aa5d5b161877ad020f"}],"diagnostics":[],"lane_counts":{"global":9,"macro":7,"micro":2},"packet_summary":{"ayah_count":19,"focus_ref":"96:16","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ص ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":false,"target_occurrences":7,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"د ع و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000478","furuq_root_norm":"د ع و","furuq_source_root_norm":"د ع و","is_dominant":true,"target_occurrences":77,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000477","furuq_root_norm":"د ع ع","furuq_source_root_norm":"د ع ع","is_dominant":false,"target_occurrences":22,"target_rank":2}]},{"qac_root":"ن د و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001487","furuq_root_norm":"ن د ي","furuq_source_root_norm":"ن د ي","is_dominant":true,"target_occurrences":33,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001486","furuq_root_norm":"ن د و","furuq_source_root_norm":"ن د و","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001563","furuq_root_norm":"ن و د","furuq_source_root_norm":"ن و د","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ط و ع","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000956","furuq_root_norm":"ط و ع","furuq_source_root_norm":"ط و ع","is_dominant":true,"target_occurrences":96,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000706","furuq_root_norm":"س ط ع","furuq_source_root_norm":"س ط ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["96:1","96:2","96:3","96:4","96:5","96:6","96:7","96:8","96:9","96:10","96:11","96:12","96:13","96:14","96:15","96:16","96:17","96:18","96:19"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"96:16","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":9,"unstructured_record_count":0},"identity":{"ayah_ref":"96:16","lane":"micro","linguistic_source_ref":"96:16","surface_ref":"96:16","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"96:16","target_tokens":[["Yalancı",["96:16:2"]],["günahkâr",["96:16:3"]],["bir",["96:16:1"]],["perçemden",["96:16:1"]]],"text":"Yalancı, günahkâr bir perçemden."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":2,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":19,"id":"s096-p01-001-019","label":"Whole surah","number":1,"refs":["96:1","96:2","96:3","96:4","96:5","96:6","96:7","96:8","96:9","96:10","96:11","96:12","96:13","96:14","96:15","96:16","96:17","96:18","96:19"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:1","source_type":"word_analysis","support_id":"sup_04e1399cfaa283dfa817","text":"{\"gloss_range\":\"an indefinite genitive appositive forelock, locally the seized front of the person and the representative bearer of the following moral qualities\",\"prose\":\"{{ar:نَاصِيَةٍۢ}} ({{tr:nāṣiyatin}}) is not a new free-standing noun. Its genitive case reaches back to the seized {{ar:ٱلنَّاصِيَةِ}} ({{tr:al-nāṣiyati}}) (96:15), so this ayah reopens the same object as an appositive description. The shift from the definite forelock to an indefinite forelock classifies the target: it is a forelock of this kind, one that can receive the paired qualities {{ar:كَٰذِبَةٍ خَاطِئَةٍۢ}} ({{tr:kādhibatin khāṭiʾatin}}). The concrete front of the head remains the local sense, while the root's frontness and prominence make that body part stand for the exposed leading face of the person. The rare forelock seizure field also brings control-and-judgment parallels into the background, then narrows them onto this one morally described forelock (11:56; 55:41). With no finite verb, the prior threat pauses into a still diagnostic portrait, and the repeated -atin cadence binds the noun and its two modifiers into one heard unit.\",\"root_display\":\"{{ar:ن ص ي}} ({{tr:n-ṣ-y}})\",\"root_gloss_range\":\"forelock, frontness, taking by the forelock, and prominence or leadership; locally the concrete forelock is selected while representative frontness remains active as pressure\",\"surface_display\":\"{{ar:نَاصِيَةٍۢ}} ({{tr:nāṣiyatin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:1:indefinite-reclassification","source_type":"word_analysis","support_id":"sup_111f44d59fa5fd8d631f","text":"{\"blocking_evidence\":null,\"headline\":\"definite target becomes classified bearer\",\"reader_payoff\":\"The reader sees the already identified forelock re-presented as a morally classified type, not merely repeated for reference.\",\"reason\":\"The prior definite form (96:15) is restated here as an indefinite genitive noun, allowing the known object to receive classifying adjectives.\",\"representative_source_ids\":[\"QG-699facb0\",\"MG-19e372df\",\"QF-c49a9d91\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:2:case-variant-apparatus","source_type":"word_analysis","support_id":"sup_14b1feada16be6f1320d","text":"{\"blocking_evidence\":null,\"headline\":\"variant cases show alternatives to received apposition\",\"reader_payoff\":\"The reader can register that variant case possibilities expose how strongly the received genitive keeps blame inside the appositive chain.\",\"reason\":\"The variant rows are useful as apparatus, but the aligned local word remains genitive and adjectival.\",\"representative_source_ids\":[\"QF-802e5121\",\"QF-d9725cec\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:2","source_type":"word_analysis","support_id":"sup_1521e3c54e7dcec1a2e4","text":"{\"gloss_range\":\"a feminine active participial adjective meaning lying or false, locally attributed to the forelock as the first diagnostic quality\",\"prose\":\"{{ar:كَٰذِبَةٍ}} ({{tr:kādhibatin}}) is the first adjective of the forelock, not a separate predicate. Its feminine genitive form keeps lying attached to {{ar:نَاصِيَةٍۢ}} ({{tr:nāṣiyatin}}), so falsehood is placed on the seized front itself. The root selects the ordinary falsehood and denial field here, with fabrication sharpening the blame; failure and masking images survive only as pressure, because the local form is a participial adjective, not one of those construction-bound idioms. The word also turns the denial (96:13) into a nominal attribute here: the earlier act of denying becomes the quality of the forelock. In the phrase, it stands between body-part and sinning, so the portrait moves from exposed front to epistemic falsehood and then to moral error, with the paired -atin cadence making the two adjectives sound cumulative. Variant-case notes show what the received genitive is doing: it keeps the blame inside the appositive chain rather than letting it become an independent censure or proclamation. The lying diagnosis then points forward to the public challenge to call the assembly (96:17).\",\"root_display\":\"{{ar:ك ذ ب}} ({{tr:k-dh-b}})\",\"root_gloss_range\":\"falsehood, lying, denial, fabrication, and some construction-bound failure or deceptive-appearance uses; locally the falsehood/lying participial branch is selected, with failure or masking only as image-pressure\",\"surface_display\":\"{{ar:كَٰذِبَةٍ}} ({{tr:kādhibatin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:2:falsehood-lexical-content","source_type":"word_analysis","support_id":"sup_2ad42ab9aefdb650f02f","text":"{\"blocking_evidence\":null,\"headline\":\"falsehood and fabrication are the selected sense\",\"reader_payoff\":\"The reader notices that the first quality is epistemic blame: the forelock is marked by falsehood and fabricated denial before sin is named.\",\"reason\":\"The local active participle coheres with the root's accepted falsehood and denial branches, while unrelated idiomatic branches are not imported.\",\"representative_source_ids\":[\"QS-a7fd1f79\",\"QS-cefdcb25\",\"QI-ce658498\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:2:paired-adjective-progression","source_type":"word_analysis","support_id":"sup_446bd60d217ae7fa0556","text":"{\"blocking_evidence\":null,\"headline\":\"falsehood pairs tightly with sinning\",\"reader_payoff\":\"The reader hears falsehood as the first half of a tightly paired double judgment, moving from lying into sinning without a loose conjunction.\",\"reason\":\"Both participles are adjacent adjectives of the same noun, and the lack of a conjunction supports a compact cumulative reading.\",\"representative_source_ids\":[\"QT-c392c456\",\"QT-ea5272b7\",\"QE-228b0f6a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:3:falsehood-to-sin-pairing","source_type":"word_analysis","support_id":"sup_5039f7c7c350a4bf3e44","text":"{\"blocking_evidence\":null,\"headline\":\"falsehood lands directly in sinning\",\"reader_payoff\":\"The reader hears lying and sinning as mutually reinforcing qualities of the same forelock, not as separable accusations.\",\"reason\":\"The two adjacent feminine participles modify the same noun without a conjunction, and the CRITICAL rows give concrete same-phrase and corpus pairing support.\",\"representative_source_ids\":[\"QI-4d9821c4\",\"QT-19f3fdf0\",\"QE-596d8d3f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"96:16:1:1","source_type":"qac_morpheme","support_id":"sup_5a62ada94d5f58ace691","text":"{\"lemma_ar\":\"نَاصِيَة\",\"morph_features\":\"STEM|POS:N|LEM:naASiyap|ROOT:nSy|F|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"96:16:1:1\",\"qac_word_ref\":\"96:16:1\",\"root_ar\":\"ن ص ي\",\"surface_ar\":\"نَاصِيَةٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:1:cross-ayah-apposition","source_type":"word_analysis","support_id":"sup_6e95d88b1ef505ed2f2e","text":"{\"blocking_evidence\":null,\"headline\":\"genitive apposition reaches back (96:15)\",\"reader_payoff\":\"The reader notices that this ayah completes the forelock phrase (96:15) rather than beginning an independent sentence.\",\"reason\":\"QAC and attachment evidence identify {{ar:نَاصِيَةٍۢ}} ({{tr:nāṣiyatin}}) as a genitive badal for the forelock governed by the prior phrase (96:15), and the variants sharpen but do not replace that local dependency.\",\"representative_source_ids\":[\"QG-58e15a5f\",\"QG-d03059d3\",\"MT-defda65b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:3:hamza-and-qiraat-pressure","source_type":"word_analysis","support_id":"sup_6f18afcc03e29b1ef02d","text":"{\"blocking_evidence\":null,\"headline\":\"the closing word carries a recitational pressure point\",\"reader_payoff\":\"The reader can hear that the final word's hamza creates a catch at the point of sin, while a canonical smoothing variant shows the sense remains stable as the sound changes.\",\"reason\":\"The QAC grammar notes the hamza in the root, and the CRITICAL qiraat rows treat smoothing as a sound contrast rather than a semantic replacement.\",\"representative_source_ids\":[\"QF-bd9092ee\",\"QF-e2b04a89\",\"QP-c8c68839\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"96:16:3:1","source_type":"qac_morpheme","support_id":"sup_882008081a807689de16","text":"{\"lemma_ar\":\"خَاطِئَة\",\"morph_features\":\"STEM|POS:ADJ|ACT|PCPL|LEM:xaATi}ap|ROOT:xTA|F|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"ADJ\",\"qac_ref\":\"96:16:3:1\",\"qac_word_ref\":\"96:16:3\",\"root_ar\":\"خ ط ء\",\"surface_ar\":\"خَاطِئَةٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:1:forelock-seizure-field","source_type":"word_analysis","support_id":"sup_8dd6a40df425c9129a43","text":"{\"blocking_evidence\":null,\"headline\":\"rare forelock field specializes seizure imagery\",\"reader_payoff\":\"The reader hears the rare forelock vocabulary as part of a seizure-and-control field that is narrowed here onto one morally described forelock (11:56; 55:41).\",\"reason\":\"The root is low-occurrence and the CRITICAL rows name concrete forelock-control parallels; local grammar narrows that field to the appositive object here.\",\"representative_source_ids\":[\"QI-71cf2d3f\",\"QI-cdbd0442\",\"MI-238366b3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:3","source_type":"word_analysis","support_id":"sup_91ff1f87197666590793","text":"{\"gloss_range\":\"a feminine active participial adjective of culpable sinning or erring, locally the closing modifier of the forelock after falsehood\",\"prose\":\"{{ar:خَاطِئَةٍۢ}} ({{tr:khāṭiʾatin}}) closes the appositive chain as the second adjective of the same forelock. Its genitive case still depends on the prior forelock phrase (96:15), so the ayah ends inside the same boundary-spanning construction. Variant-case evidence sharpens that point: accusative censure or nominative proclamation would loosen the final blame, while the received genitive keeps it dependent on the seized forelock. The active participle makes the final quality culpable sinning rather than accidental error; the missing-the-mark image gives that sin directional force, as though the leading front points wrong. Because it follows {{ar:كَٰذِبَةٍ}} ({{tr:kādhibatin}}) without a conjunction, the phrase does not add a loose second charge but lands falsehood directly in moral transgression. Wider sinner-label and transgression scenes remain echoes, not controls: confession or condemnation contexts and the Pharaonic great-sin scene frame the moral field while the local verse keeps the diagnosis on the forelock (12:29; 12:91; 12:97; 69:9; 96:6). The written hamza and the smoothed canonical variant make the final word a real recitational pressure point, while the triple -atin cadence seals the body, falsehood, and sinning into one compact diagnosis. That closing diagnosis also supplies the culpability answered by the public challenge and counter-summons that follow (96:17; 96:18).\",\"root_display\":\"{{ar:خ ط أ}} ({{tr:kh-ṭ-ʾ}})\",\"root_gloss_range\":\"sinning, culpable error, and missing the right course or target; locally the active participle leans toward culpable transgression rather than accidental mistake\",\"surface_display\":\"{{ar:خَاطِئَةٍۢ}} ({{tr:khāṭiʾatin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:3:culpable-active-participle","source_type":"word_analysis","support_id":"sup_93901e7f9e702b836f13","text":"{\"blocking_evidence\":null,\"headline\":\"active participle points to culpable sin\",\"reader_payoff\":\"The reader notices that the closing word names culpable transgression, not a mere accidental mistake.\",\"reason\":\"The local form is an active participial adjective; missing V4 rows for the root do not contradict the CRITICAL distinction between culpable sinning and unintentional error.\",\"representative_source_ids\":[\"MG-86825094\",\"QS-293c812f\",\"QI-c5fbd048\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:3:final-closure-and-cadence","source_type":"word_analysis","support_id":"sup_94572f32d6e984a4c042","text":"{\"blocking_evidence\":null,\"headline\":\"the ayah closes on sounded moral misdirection\",\"reader_payoff\":\"The reader notices the final word sealing the ayah semantically, rhythmically, and directionally rather than merely adding another adjective.\",\"reason\":\"The word is the final adjective, completes the triple indefinite cadence, and carries the missing-the-mark payoff.\",\"representative_source_ids\":[\"QT-cd58a6e4\",\"QP-67c66061\",\"QY-33115ebb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:3:closing-genitive-adjective","source_type":"word_analysis","support_id":"sup_9716279e1c7b2f2c6b6e","text":"{\"blocking_evidence\":null,\"headline\":\"the final adjective remains inside the apposition\",\"reader_payoff\":\"The reader sees the last word still grammatically tied to the forelock seized in the prior phrase (96:15), not detached as a new sentence.\",\"reason\":\"QAC and attachment evidence mark {{ar:خَاطِئَةٍۢ}} ({{tr:khāṭiʾatin}}) as the second genitive adjective modifying the appositive forelock.\",\"representative_source_ids\":[\"QG-00043cc3\",\"QG-38d41b75\",\"QG-b063292f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:3:cross-surah-and-surah-echoes","source_type":"word_analysis","support_id":"sup_9a17a0a5c0a7c30a1061","text":"{\"blocking_evidence\":null,\"headline\":\"sinner-label echoes become local diagnosis\",\"reader_payoff\":\"The reader can connect this final participle to wider sinner-label and transgression scenes, while keeping the local verse focused on the forelock's diagnosis (12:29; 12:91; 12:97; 69:9; 96:6).\",\"reason\":\"The cited echoes are useful as parallels and thematic narrowing, but they do not control the local parse or turn the forelock into those scenes.\",\"representative_source_ids\":[\"QI-e415b08b\",\"MI-25b1bae1\",\"QE-9e258737\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:2:forward-summons-test","source_type":"word_analysis","support_id":"sup_c6942b6239f71157454c","text":"{\"blocking_evidence\":null,\"headline\":\"the false claimant moves toward a public test\",\"reader_payoff\":\"The reader sees the lying diagnosis pushed forward toward the challenge to call the assembly (96:17).\",\"reason\":\"The row names a concrete forward bridge from this adjective to the speech-act challenge (96:17), and nothing in the local evidence blocks it.\",\"representative_source_ids\":[\"QB-7330d88e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"96:16:2:1","source_type":"qac_morpheme","support_id":"sup_c69db18d61cb88b77356","text":"{\"lemma_ar\":\"كَٰذِب\",\"morph_features\":\"STEM|POS:ADJ|ACT|PCPL|LEM:ka`*ib|ROOT:k*b|F|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"ADJ\",\"qac_ref\":\"96:16:2:1\",\"qac_word_ref\":\"96:16:2\",\"root_ar\":\"ك ذ ب\",\"surface_ar\":\"كَٰذِبَةٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:3:forward-counter-summons","source_type":"word_analysis","support_id":"sup_ca42687aa491fb1bb4f7","text":"{\"blocking_evidence\":null,\"headline\":\"the diagnosis prepares the counter-summons\",\"reader_payoff\":\"The reader sees the final moral diagnosis as the culpability that prepares the answer to the public challenge (96:17; 96:18).\",\"reason\":\"The CRITICAL row gives a concrete forward bridge to the next challenge and answer (96:17; 96:18), and the local adjective supplies the moral diagnosis that bridge depends on.\",\"representative_source_ids\":[\"QB-2cc27da6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:2:masking-and-failure-pressure","source_type":"word_analysis","support_id":"sup_cc0b3bb920753a3b2994","text":"{\"blocking_evidence\":null,\"headline\":\"masking and failure color the exposed falsehood\",\"reader_payoff\":\"The reader can feel falsehood as a failed and covering front that is exposed by the threatened seizure, while the local sense remains lying.\",\"reason\":\"V4 treats failure and deceptive-appearance material as separate or construction-bound branches, so these rows survive as image-pressure around falsehood, not as replacement meanings.\",\"representative_source_ids\":[\"QS-3d2f50dc\",\"QS-d838dc73\",\"QY-754848a3\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:1:one-forelock-two-adjectives","source_type":"word_analysis","support_id":"sup_d453e9e8985a3954d629","text":"{\"blocking_evidence\":null,\"headline\":\"agreement binds both qualities to one forelock\",\"reader_payoff\":\"The reader sees and hears one forelock carrying both qualities, with agreement and repeated -atin cadence preventing the traits from drifting apart.\",\"reason\":\"Both following participles agree with the noun as adjectives, and the sound rows reinforce the same local unity.\",\"representative_source_ids\":[\"QG-1db34a81\",\"QP-09b3781f\",\"QP-961d7a3a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:2:first-adjective-of-forelock","source_type":"word_analysis","support_id":"sup_d9dfd7f27c80f85da456","text":"{\"blocking_evidence\":null,\"headline\":\"lying is grammatically attached to the forelock\",\"reader_payoff\":\"The reader sees falsehood placed on the seized forelock itself, not left as a detached accusation.\",\"reason\":\"QAC and attachment evidence mark {{ar:كَٰذِبَةٍ}} ({{tr:kādhibatin}}) as an active participial adjective agreeing with the forelock.\",\"representative_source_ids\":[\"QG-58a421f4\",\"QG-b576dfb0\",\"MG-f2c4bc48\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:2:dagger-alif-marker","source_type":"word_analysis","support_id":"sup_db56f9c4008447a5d16d","text":"{\"blocking_evidence\":null,\"headline\":\"minor spelling marker without separate payoff\",\"reader_payoff\":null,\"reason\":\"The row records a form detail, but it does not change the local sense, syntax, or payoff beyond the retained participial-adjective topic.\",\"representative_source_ids\":[\"QF-2fea57ba\"],\"status\":\"dropped_filler\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:3:missing-the-mark-image","source_type":"word_analysis","support_id":"sup_e3fbc56dad7c74a79a3f","text":"{\"blocking_evidence\":null,\"headline\":\"sin is pictured as failed direction\",\"reader_payoff\":\"The reader feels the final sinning adjective as misdirected aim: the front that should orient the person points off target.\",\"reason\":\"The root-image claim is coherent with the local word and is not blocked by the absence of V4 guardrail rows for this root.\",\"representative_source_ids\":[\"QS-36726b1b\",\"QS-d5771dc2\",\"MS-2f4bd641\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:3:case-variant-apparatus","source_type":"word_analysis","support_id":"sup_e80958174240dc5e72e8","text":"{\"blocking_evidence\":null,\"headline\":\"variant cases expose the received genitive force\",\"reader_payoff\":\"The reader can register that variant case alternatives would make censure or proclamation more independent, while the received genitive keeps the final blame dependent on the seized forelock.\",\"reason\":\"The variant rows are retained as apparatus; the aligned local word remains genitive and adjectival.\",\"representative_source_ids\":[\"QF-177331c7\",\"QF-1a5173b0\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:1:verbless-portrait","source_type":"word_analysis","support_id":"sup_f038b289899223428cba","text":"{\"blocking_evidence\":null,\"headline\":\"the prior threat freezes into a diagnostic portrait\",\"reader_payoff\":\"The reader feels the movement from threatened action (96:15) into a still portrait that names the seized object's qualities.\",\"reason\":\"The ayah has no finite verb and opens with the appositive noun, so the CRITICAL portrait reading is locally licensed.\",\"representative_source_ids\":[\"QT-493953ef\",\"QT-f61c3a5e\",\"QB-ea23edf4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:2:denial-becomes-attribute","source_type":"word_analysis","support_id":"sup_f17f5b28998fc869ad5d","text":"{\"blocking_evidence\":null,\"headline\":\"the earlier denial returns as an attribute\",\"reader_payoff\":\"The reader notices that the denial (96:13) returns here as a participial quality attached to the seized forelock.\",\"reason\":\"The same root appears in the surah with a form and role shift, from a finite denial verb (96:13) to a Form I participial adjective here.\",\"representative_source_ids\":[\"QI-0fea742f\",\"QE-6d988d85\",\"QE-9ce963fd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:16:1:representative-forelock","source_type":"word_analysis","support_id":"sup_fea365e777e906e82c82","text":"{\"blocking_evidence\":null,\"headline\":\"front of the head bears the whole person's stance\",\"reader_payoff\":\"The reader notices that the seized body part becomes the visible representative of the person's false and erring stance.\",\"reason\":\"The local seizure frame selects the concrete forelock, while dictionary evidence and the attached adjectives support representative frontness; cognition or leadership claims are kept as metonymic pressure, not as a replacement sense.\",\"representative_source_ids\":[\"QS-13c6a688\",\"QS-35fe6d2e\",\"QS-f731fd1b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"نَاصِيَةٍۢ كَٰذِبَةٍ خَاطِئَةٍۢ","ayah_ref":"96:16"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000420/B002","root_001290/B001","root_001512/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001512","role":"The branch's forelock and seizure by it supplies both the concrete body part and its function as a graspable control point.","root":"ن ص ي","source_ref":"96:16","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001290","role":"The branch's falsehood against truth in speech or action makes the first adjective an active distortion rather than a decorative insult.","root":"ك ذ ب","source_ref":"96:16","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000420","role":"The branch's culpable and intentional wrongdoing makes the second adjective mark accountable agency rather than accidental error.","root":"خ ط ء","source_ref":"96:16","source_word_indices":["3"]}],"changed_reading":{"after":"The agent's graspable control point is itself presented as the bodily source and bearer of false action and deliberate wrongdoing.","before":"A forelock belonging to someone who lies and sins."},"confidence":"strong","focus_anchor":"The noun at word 1 is directly modified by the feminine adjectives at words 2 and 3.","mechanism":"The forelock is both a body part and a graspable point of control. Grammatical agreement relocates false speech or action and deliberate wrongdoing from an unnamed owner onto that controlling front, making moral agency bodily and seizable.","model_id":"b1_embodied_control_point"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b1_embodied_control_point","source_type":"hft","support_id":"sup_ed56121597e410ee2d7b","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"نَاصِيَةٍۢ كَٰذِبَةٍ خَاطِئَةٍۢ","ayah_ref":"96:16"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000420/B001","root_001290/B004","root_001512/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001512","role":"The branch's chosen elite, noble leaders, and forerunners supplies the foremost or leading element in the trajectory.","root":"ن ص ي","source_ref":"96:16","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_001290","role":"The branch's charge proving false when it is not carried through turns truth into a test of whether the lead action fulfills its claim.","root":"ك ذ ب","source_ref":"96:16","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000420","role":"The branch's missing or passing beyond the right direction supplies the trajectory's deviation.","root":"خ ط ء","source_ref":"96:16","source_word_indices":["3"]}],"changed_reading":{"after":"A foremost agent is diagnosed as a failed lead: its claim does not hold in action and its course misses what is right.","before":"Two moral defects are listed on a body part."},"confidence":"exploratory","focus_anchor":"The inventories of all three focus words permit a coordinated front, performance, and direction model.","mechanism":"The forelock's select or foremost branch supplies a leading edge; falsehood as a charge that fails supplies a test of enacted truth; error as missing the right direction supplies the failed course. Together they depict a leader or front that cannot make its claim true in motion and veers from what is right.","model_id":"b2_failed_leading_trajectory"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b2_failed_leading_trajectory","source_type":"hft","support_id":"sup_65aa5d5b161877ad020f","trust":"legacy_unbound"}]}
</lane_packet_json>
